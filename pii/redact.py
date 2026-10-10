"""Turn detected spans into redacted text.

Same value -> same token within one call, so "[NAME_1] ... [NAME_1]" still
reads as one person. `vault` maps tokens back to real values; in production
it lives in a separate, access-controlled store, never next to the text.

    python -m pii.redact "call me at 98450 12345, PAN ABCPK1234M"
"""
import re
import sys

from .rules import Span, detect


def _norm(value: str) -> str:
    return re.sub(r"[\s-]", "", value).lower()


def redact(text: str, spans: list[Span] | None = None) -> tuple[str, dict[str, str]]:
    spans = detect(text) if spans is None else spans
    counters: dict[str, int] = {}
    seen: dict[tuple[str, str], str] = {}
    vault: dict[str, str] = {}
    out, cursor = [], 0
    for s in sorted(spans, key=lambda s: s.start):
        value = text[s.start:s.end]
        key = (s.label, _norm(value))
        if key not in seen:
            counters[s.label] = counters.get(s.label, 0) + 1
            seen[key] = f"[{s.label}_{counters[s.label]}]"
            vault[seen[key]] = value
        out.append(text[cursor:s.start])
        out.append(seen[key])
        cursor = s.end
    out.append(text[cursor:])
    return "".join(out), vault


if __name__ == "__main__":
    text = " ".join(sys.argv[1:]) or sys.stdin.read()
    red, vault = redact(text)
    print(red)
    for token, value in vault.items():
        print(f"  {token} = {value}", file=sys.stderr)
