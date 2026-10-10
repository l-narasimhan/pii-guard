"""Webhook relay: sit between a third-party chat app and your own systems.

    chat app (Freshchat / Zendesk / Intercom / WhatsApp BSP …)
        │  "new message" webhook (raw text)
        ▼
    this relay ──► PII Guard /redact ──► redacted copy ──► your DB / analytics / LLM / CRM
        │
        └── fail closed: if PII Guard is down, answer 503 (vendors retry webhooks) and forward nothing

Every vendor's payload looks different, so the two field paths are configurable:
  RELAY_TEXT_FIELD   dotted path to the message text            (default: message.text)
  RELAY_CONV_FIELD   dotted path to the conversation/ticket id   (default: conversation_id)

Other env:
  PII_GUARD_URL      default http://localhost:5240/redact
  PII_API_KEY        X-API-Key for PII Guard (if set)
  RELAY_SECRET       shared secret to verify the vendor's HMAC-SHA256 signature (header X-Signature)
  RELAY_FORWARD_URL  where to POST the redacted payload; if unset, appended to redacted_messages.jsonl
  RELAY_PORT         default 5250

    python examples/webhook_relay.py
    curl -s localhost:5250/webhook -d '{"conversation_id":"t-1","message":{"text":"Ramesh 98450 12345"}}'
"""
import copy
import hashlib
import hmac
import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

GUARD = os.environ.get("PII_GUARD_URL", "http://localhost:5240/redact")
API_KEY = os.environ.get("PII_API_KEY", "")
SECRET = os.environ.get("RELAY_SECRET", "").encode()
FORWARD = os.environ.get("RELAY_FORWARD_URL", "")
TEXT_FIELD = os.environ.get("RELAY_TEXT_FIELD", "message.text").split(".")
CONV_FIELD = os.environ.get("RELAY_CONV_FIELD", "conversation_id").split(".")
PORT = int(os.environ.get("RELAY_PORT", 5250))


def get(d, path):
    for k in path:
        d = d[k]
    return d


def put(d, path, value):
    for k in path[:-1]:
        d = d[k]
    d[path[-1]] = value


def redact(text: str, conversation_id: str) -> dict:
    req = urllib.request.Request(
        GUARD, json.dumps({"text": text, "conversation_id": conversation_id, "mode": "token"}).encode(),
        {"Content-Type": "application/json", **({"X-API-Key": API_KEY} if API_KEY else {})})
    with urllib.request.urlopen(req, timeout=5) as r:
        return json.load(r)


def forward(payload: dict):
    if not FORWARD:
        with open("redacted_messages.jsonl", "a") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
        return
    req = urllib.request.Request(FORWARD, json.dumps(payload).encode(), {"Content-Type": "application/json"})
    urllib.request.urlopen(req, timeout=10).read()


class Relay(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # never log payloads

    def _reply(self, code: int, body: dict):
        data = json.dumps(body).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        if self.path != "/webhook":
            return self._reply(404, {"error": "not found"})
        raw = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        if SECRET:  # reject anything not signed by the chat vendor
            sig = hmac.new(SECRET, raw, hashlib.sha256).hexdigest()
            if not hmac.compare_digest(sig, self.headers.get("X-Signature", "")):
                return self._reply(401, {"error": "bad signature"})
        try:
            event = json.loads(raw)
            text, conv = get(event, TEXT_FIELD), str(get(event, CONV_FIELD))
        except (ValueError, KeyError, TypeError):
            return self._reply(400, {"error": "unexpected payload shape; set RELAY_TEXT_FIELD / RELAY_CONV_FIELD"})
        try:
            result = redact(text, conv)
        except Exception:
            return self._reply(503, {"error": "PII Guard unavailable; not forwarded (vendor will retry)"})
        clean = copy.deepcopy(event)
        put(clean, TEXT_FIELD, result["redacted"])
        clean["pii"] = {"labels": sorted({e["label"] for e in result["entities"]}),
                        "model_version": result["model_version"]}
        try:
            forward(clean)
        except Exception:
            return self._reply(502, {"error": "downstream unavailable"})
        self._reply(200, {"ok": True, "redacted_entities": len(result["entities"])})


if __name__ == "__main__":
    print(f"relay on http://localhost:{PORT}/webhook -> {GUARD} -> {FORWARD or 'redacted_messages.jsonl'}")
    ThreadingHTTPServer(("127.0.0.1", PORT), Relay).serve_forever()
