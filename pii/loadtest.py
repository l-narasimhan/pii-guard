"""Load test the running service: N concurrent clients posting real-style messages.

Latency is measured client-side (includes HTTP), per message.

    .venv/bin/python -m pii.loadtest            # 1/4/8/16 clients flat out, then 10/30/50 msg/s steady
"""
import json
import random
import statistics
import sys
import threading
import time
import urllib.request

URL = "http://localhost:5240/redact"


def texts():
    rows = [json.loads(l)["text"] for l in open("data/handwritten.jsonl")]
    rows += [json.loads(l)["text"] for l in open("data/test.jsonl")][:500]
    return rows


def client(i, msgs, stop, lat, errors):
    r = random.Random(i)
    cid = f"load-{i}"
    while not stop.is_set():
        body = json.dumps({"text": r.choice(msgs), "conversation_id": cid}).encode()
        req = urllib.request.Request(URL, body, {"Content-Type": "application/json"})
        t0 = time.perf_counter()
        try:
            urllib.request.urlopen(req, timeout=10).read()
            lat.append((time.perf_counter() - t0) * 1000)
        except Exception:
            errors.append(1)


def run(n, seconds, msgs):
    stop, lat, errors = threading.Event(), [], []
    ts = [threading.Thread(target=client, args=(i, msgs, stop, lat, errors)) for i in range(n)]
    for t in ts:
        t.start()
    time.sleep(seconds)
    stop.set()
    for t in ts:
        t.join()
    q = statistics.quantiles(lat, n=100)
    return {"clients": n, "msgs": len(lat), "per_sec": len(lat) / seconds, "p50": q[49], "p95": q[94],
            "p99": q[98], "errors": len(errors)}


def steady(rate: float, seconds: int, msgs):
    """Open-loop: send `rate` messages/sec regardless of replies (how real traffic arrives)."""
    lat, errors, threads = [], [], []
    r = random.Random(7)

    def one(text, cid):
        req = urllib.request.Request(URL, json.dumps({"text": text, "conversation_id": cid}).encode(),
                                     {"Content-Type": "application/json"})
        t0 = time.perf_counter()
        try:
            urllib.request.urlopen(req, timeout=10).read()
            lat.append((time.perf_counter() - t0) * 1000)
        except Exception:
            errors.append(1)

    start = time.perf_counter()
    for k in range(int(rate * seconds)):
        time.sleep(max(0.0, start + k / rate - time.perf_counter()))
        t = threading.Thread(target=one, args=(r.choice(msgs), f"chat-{k % 200}"))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    q = statistics.quantiles(lat, n=100)
    return f"| {rate:.0f} msg/s steady | {len(lat)} | {q[49]:.1f} | {q[94]:.1f} | {q[98]:.1f} | {len(errors)} |"


if __name__ == "__main__":
    secs = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    msgs = texts()
    print("| Concurrent clients | Messages/sec | p50 ms | p95 ms | p99 ms | Errors |")
    print("|---|---|---|---|---|---|")
    for n in (1, 4, 8, 16):
        r = run(n, secs, msgs)
        print(f"| {r['clients']} | {r['per_sec']:.0f} | {r['p50']:.1f} | {r['p95']:.1f} | {r['p99']:.1f} | {r['errors']} |", flush=True)
    print("\n| Steady arrival rate | Messages | p50 ms | p95 ms | p99 ms | Errors |\n|---|---|---|---|---|---|")
    for rate in (10, 30, 50):
        print(steady(rate, secs, msgs), flush=True)
