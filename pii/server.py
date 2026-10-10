"""PII Guard local service (stdlib HTTP server).

  GET  /                 chat demo page
  GET  /health           {"status": "ok", ...}
  POST /redact           {"text", "conversation_id"?, "mode"?: "token"|"mask"} -> redacted text + entities
  POST /vault            {"conversation_id"}  -> token->value map   (demo mode only)
  POST /reset            {"conversation_id"}

Fail closed: any error returns 503 with blocked=true and never echoes the input.
Logs carry counts, labels and timings only, never text.

Config (env):
  PII_MODE     demo (default): demo page + /vault on   |  prod: both off
  PII_API_KEY  if set, POST calls need header  X-API-Key: <key>
  PII_HOST     bind address (default 127.0.0.1; 0.0.0.0 in Docker)
  PII_PORT     default 5240
  model: see pii/model_store.py (PII_MODEL_DIR, PII_MODEL_REPO, HF_TOKEN)

    .venv/bin/python -m pii.server            # http://localhost:5240
"""
import hmac
import json
import logging
import os
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from .engine import MODEL_VERSION, Engine

PORT = int(os.environ.get("PII_PORT", 5240))
HOST = os.environ.get("PII_HOST", "127.0.0.1")
MODE = os.environ.get("PII_MODE", "demo")
API_KEY = os.environ.get("PII_API_KEY", "")
STATIC = Path(__file__).parent / "static"
MAX_CHARS = 20_000
log = logging.getLogger("pii-guard")
ENGINE: Engine | None = None
STARTED = time.time()


class Handler(BaseHTTPRequestHandler):
    server_version = "PIIGuard/0.4"

    def log_message(self, *args):  # silence default access log (it would include paths only, but keep it quiet)
        pass

    def _send(self, code: int, body, ctype="application/json"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _json(self) -> dict:
        n = int(self.headers.get("Content-Length", 0))
        return json.loads(self.rfile.read(n) or b"{}")

    def _authorised(self) -> bool:
        return not API_KEY or hmac.compare_digest(self.headers.get("X-API-Key", ""), API_KEY)

    def do_GET(self):
        if self.path in ("/", "/index.html") and MODE == "demo":
            return self._send(200, (STATIC / "chat.html").read_bytes(), "text/html; charset=utf-8")
        if self.path == "/health":
            return self._send(200, {"status": "ok", "model_version": MODEL_VERSION, "mode": MODE,
                                    "uptime_s": round(time.time() - STARTED)})
        self._send(404, {"error": "not found"})

    def do_POST(self):
        if not self._authorised():
            return self._send(401, {"error": "missing or wrong X-API-Key", "blocked": True})
        try:
            body = self._json()
            if self.path == "/redact":
                text = body.get("text", "")
                if not isinstance(text, str) or len(text) > MAX_CHARS:
                    return self._send(413, {"error": f"text must be a string under {MAX_CHARS} chars", "blocked": True})
                mode = body.get("mode", "token")
                res = ENGINE.redact(text, body.get("conversation_id"), "mask" if mode == "mask" else "token")
                counts = {}
                for e in res["entities"]:
                    counts[e["label"]] = counts.get(e["label"], 0) + 1
                log.info("redact chars=%d entities=%s ms=%.1f mode=%s", len(text), counts, res["ms"], res["mode"])
                return self._send(200, res)
            if self.path == "/vault" and MODE == "demo":
                return self._send(200, {"vault": ENGINE.vault(body["conversation_id"]),
                                        "note": "demo only; production vault access is restricted (M6)"})
            if self.path == "/reset":
                ENGINE.reset(body["conversation_id"])
                return self._send(200, {"ok": True})
            self._send(404, {"error": "not found"})
        except Exception as exc:  # fail closed: never pass the input through
            log.error("redaction failed: %s", type(exc).__name__)
            self._send(503, {"error": "redaction unavailable", "blocked": True})


WARMUP = [  # a few lengths, so the first real requests aren't slow
    "hi", "Ramesh Kumar here, 98450 12345",
    "mera naam Ramesh hai, address flat 4B Prestige Shantiniketan, Whitefield 560066, PAN ABCPK1234M",
    "CUSTOMER KYC FORM\nName: Suresh Iyer\nDOB: 12-07-1979\nAadhaar: 9536 4556 8158\nMobile: 98450 12345\n" * 4,
]


def main(port: int = PORT):
    global ENGINE
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    if MODE == "prod" and not API_KEY:
        log.warning("PII_MODE=prod without PII_API_KEY: anyone who can reach the port can call /redact")
    t0 = time.time()
    ENGINE = Engine()
    for _ in range(3):
        for text in WARMUP:
            ENGINE.redact(text)
    log.info("engine ready in %.1fs (%s, mode=%s, auth=%s)", time.time() - t0, MODEL_VERSION, MODE, bool(API_KEY))
    srv = ThreadingHTTPServer((HOST, port), Handler)
    log.info("PII Guard on http://%s:%d", HOST, port)
    srv.serve_forever()


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else PORT)
