"""PII engine for live use: detection + conversation memory + redaction.

  detect  : rules (checksum/context) -> tagger (ONNX) -> format checks      (pii.tagger.engine)
  memory  : values found earlier in a conversation are caught again later and keep their token
            ("Ramesh Kumar" = [NAME_1] in message 1 -> "Ramesh" alone in message 5 is still [NAME_1])
  redact  : mode "token" -> [NAME_1] with the real value kept in the vault
            mode "mask"  -> [NAME], nothing stored (irreversible; for analytics/logs)

The vault here is in-memory for the demo; M6 replaces it with an encrypted store.
"""
import os
import re
import threading
import time
from dataclasses import dataclass, field

from .rules import Span, resolve_overlaps
from .tagger import engine as build_engine

MODEL_VERSION = os.environ.get("PII_MODEL_VERSION", "tagger-piiranha@m3")


def norm(value: str) -> str:
    return re.sub(r"[\s\-.]", "", value).lower()


@dataclass
class Conversation:
    tokens: dict = field(default_factory=dict)     # (label, normalised value) -> token
    counters: dict = field(default_factory=dict)   # label -> last number used
    vault: dict = field(default_factory=dict)      # token -> real value
    names: dict = field(default_factory=dict)      # name part (lower) -> token, for later mentions
    last_used: float = field(default_factory=time.time)


class Engine:
    def __init__(self, model_path: str | None = None, use_onnx: bool = True):
        from .model_store import ensure_model
        model_path = ensure_model(model_path)
        if use_onnx:
            from .onnx_tagger import OnnxTagger
            tagger = OnnxTagger(model_path, "model.onnx")
        else:
            from .tagger import Tagger
            tagger = Tagger(model_path)
        self._detect = build_engine(tagger)
        self._lock = threading.Lock()       # tokenizer + model are not thread-safe
        self._convs: dict[str, Conversation] = {}
        self._conv_lock = threading.Lock()

    def detect(self, text: str) -> list[Span]:
        with self._lock:
            return self._detect(text)

    def _conv(self, cid: str | None) -> Conversation:
        with self._conv_lock:
            if cid is None:
                return Conversation()
            c = self._convs.setdefault(cid, Conversation())
            c.last_used = time.time()
            return c

    def _remembered(self, text: str, conv: Conversation, spans: list[Span]) -> list[Span]:
        """Earlier names (full or a single part) mentioned again without the model catching them."""
        extra = []
        for part in conv.names:
            for m in re.finditer(rf"(?<!\w){re.escape(part)}(?!\w)", text, re.I):
                if all(m.end() <= s.start or m.start() >= s.end for s in spans + extra):
                    extra.append(Span(m.start(), m.end(), "NAME", "memory"))
        return extra

    def redact(self, text: str, conversation_id: str | None = None, mode: str = "token") -> dict:
        t0 = time.perf_counter()
        conv = self._conv(conversation_id)
        spans = self.detect(text)
        spans = resolve_overlaps(spans + self._remembered(text, conv, spans))
        out, cursor, entities = [], 0, []
        for s in sorted(spans, key=lambda s: s.start):
            value = text[s.start:s.end]
            if mode == "mask":
                token = f"[{s.label}]"
            else:
                key = (s.label, norm(value))
                token = conv.tokens.get(key)
                if token is None and s.label == "NAME":   # "Ramesh" after "Ramesh Kumar"
                    token = conv.names.get(value.strip(".").lower())
                if token is None:
                    conv.counters[s.label] = conv.counters.get(s.label, 0) + 1
                    token = f"[{s.label}_{conv.counters[s.label]}]"
                    conv.vault[token] = value
                conv.tokens[key] = token
                if s.label == "NAME":
                    for part in [value] + value.split():
                        if len(part.strip(".")) >= 3:
                            conv.names.setdefault(part.strip(".").lower(), token)
            out.append(text[cursor:s.start])
            out.append(token)
            cursor = s.end
            entities.append({"label": s.label, "token": token, "start": s.start, "end": s.end, "source": s.source})
        out.append(text[cursor:])
        return {
            "redacted": "".join(out),
            "entities": entities,
            "ms": round((time.perf_counter() - t0) * 1000, 2),
            "model_version": MODEL_VERSION,
            "mode": mode,
        }

    def vault(self, conversation_id: str) -> dict:
        return dict(self._conv(conversation_id).vault)

    def reset(self, conversation_id: str):
        with self._conv_lock:
            self._convs.pop(conversation_id, None)
