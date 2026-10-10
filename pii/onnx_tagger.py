"""Export the tagger to ONNX, quantise to int8, and serve it with onnxruntime (CPU).

Same predictions pipeline as pii.tagger.Tagger, just a faster runtime:
  export  : PyTorch -> ONNX graph (fp32)
  quantise: weights -> int8 (dynamic quantisation; ~4x smaller, faster on CPU)

    .venv/bin/python -m pii.onnx_tagger export models/tagger-piiranha
    .venv/bin/python -m pii.onnx_tagger bench  models/tagger-piiranha data/handwritten.jsonl
"""
import json
import statistics
import sys
import time
from pathlib import Path

import numpy as np
from transformers import AutoTokenizer

from .rules import Span
from .tagdata import decode


def export(path: str):
    import torch
    from onnxruntime.quantization import QuantType, quantize_dynamic
    from transformers import AutoModelForTokenClassification

    out = Path(path) / "onnx"
    out.mkdir(exist_ok=True)
    tok = AutoTokenizer.from_pretrained(path)
    model = AutoModelForTokenClassification.from_pretrained(path).eval()
    sample = tok("Thanks Divya, call 98450 12345", return_tensors="pt")
    fp32 = out / "model.onnx"
    torch.onnx.export(
        model, (sample["input_ids"], sample["attention_mask"]), str(fp32),
        input_names=["input_ids", "attention_mask"], output_names=["logits"],
        dynamic_axes={"input_ids": {0: "b", 1: "t"}, "attention_mask": {0: "b", 1: "t"}, "logits": {0: "b", 1: "t"}},
        opset_version=17, dynamo=False,
    )
    int8 = out / "model.int8.onnx"
    quantize_dynamic(str(fp32), str(int8), weight_type=QuantType.QInt8)
    for f in (fp32, int8):
        print(f"{f}: {f.stat().st_size / 1e6:.0f} MB")


class OnnxTagger:
    def __init__(self, path: str, variant: str = "model.int8.onnx", threads: int = 4):
        import onnxruntime as ort
        opts = ort.SessionOptions()
        opts.intra_op_num_threads = threads
        self.name = f"onnx({variant})"
        self.tok = AutoTokenizer.from_pretrained(path)
        self.sess = ort.InferenceSession(str(Path(path) / "onnx" / variant), opts, providers=["CPUExecutionProvider"])

    def __call__(self, text: str) -> list[Span]:
        enc = self.tok(text, truncation=True, max_length=384, stride=64, return_overflowing_tokens=True,
                       return_offsets_mapping=True, padding=True, return_tensors="np")
        logits = self.sess.run(["logits"], {"input_ids": enc["input_ids"].astype(np.int64),
                                            "attention_mask": enc["attention_mask"].astype(np.int64)})[0]
        by_char: dict[tuple, int] = {}
        for win_off, win_tags in zip(enc["offset_mapping"].tolist(), logits.argmax(-1).tolist()):
            for off, t in zip(win_off, win_tags):
                if off[0] != off[1]:
                    by_char[tuple(off)] = t
        offs = sorted(by_char)
        return decode(text, offs, [by_char[o] for o in offs])


def bench(path: str, data: str):
    """Agreement with the PyTorch tagger + latency, on the same texts."""
    from .tagger import Tagger
    texts = [json.loads(l)["text"] for l in open(data)]
    ref = Tagger(path)
    for variant in ("model.onnx", "model.int8.onnx"):
        t = OnnxTagger(path, variant)
        same, times = 0, []
        for x in texts:
            a = {(s.start, s.end, s.label) for s in ref(x)}
            t0 = time.perf_counter(); b = {(s.start, s.end, s.label) for s in t(x)}
            times.append((time.perf_counter() - t0) * 1000)
            same += a == b
        q = statistics.quantiles(times, n=20)
        print(f"{variant}: identical output on {same}/{len(texts)} texts; "
              f"latency mean {statistics.mean(times):.1f} ms, p95 {q[18]:.1f} ms")
    times = []
    for x in texts:
        t0 = time.perf_counter(); ref(x); times.append((time.perf_counter() - t0) * 1000)
    print(f"pytorch (reference): latency mean {statistics.mean(times):.1f} ms, p95 {statistics.quantiles(times, n=20)[18]:.1f} ms")


if __name__ == "__main__":
    cmd, path = sys.argv[1], sys.argv[2]
    export(path) if cmd == "export" else bench(path, sys.argv[3])
