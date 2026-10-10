"""Rule layer: fast, deterministic detection of structured Indian PII.

Each detector = a regex for the shape + a validity check (checksum or
context keyword), so random numbers aren't flagged. Returns character
spans; overlaps are resolved by preferring the longer / higher-priority span.
"""
import re
from dataclasses import dataclass


@dataclass
class Span:
    start: int
    end: int
    label: str
    source: str = "rule"

    def text(self, s: str) -> str:
        return s[self.start:self.end]


# ---------- checksums ----------

_VD = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5],
    [2, 3, 4, 0, 1, 7, 8, 9, 5, 6], [3, 4, 0, 1, 2, 8, 9, 5, 6, 7],
    [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
    [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3],
    [8, 7, 6, 5, 9, 3, 2, 1, 0, 4], [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
]
_VP = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4],
    [5, 8, 0, 3, 7, 9, 6, 1, 4, 2], [8, 9, 1, 6, 0, 4, 3, 5, 2, 7],
    [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
    [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8],
]
_VINV = [0, 4, 3, 2, 1, 5, 6, 7, 8, 9]


def verhoeff_valid(digits: str) -> bool:
    """Aadhaar's last digit is a Verhoeff check digit."""
    c = 0
    for i, d in enumerate(reversed(digits)):
        c = _VD[c][_VP[i % 8][int(d)]]
    return c == 0


def verhoeff_check_digit(digits: str) -> str:
    c = 0
    for i, d in enumerate(reversed(digits)):
        c = _VD[c][_VP[(i + 1) % 8][int(d)]]
    return str(_VINV[c])


def luhn_valid(digits: str) -> bool:
    """Payment card numbers end in a Luhn check digit."""
    total = 0
    for i, d in enumerate(reversed(digits)):
        n = int(d)
        if i % 2 == 1:
            n = n * 2 - 9 if n > 4 else n * 2
        total += n
    return total % 10 == 0


def card_plausible(d: str) -> bool:
    """Known card prefix + length (Visa, Mastercard, RuPay, Amex, Diners); cuts random Luhn hits."""
    n = len(d)
    if d[0] == "4":
        return n in (13, 16, 19)
    if d[:2] in ("51", "52", "53", "54", "55") or "2221" <= d[:4] <= "2720":
        return n == 16
    if d[:2] in ("60", "65", "81", "82") or d[:3] == "508":
        return n == 16
    if d[:2] in ("34", "37"):
        return n == 15
    if d[:2] in ("36", "38") or d[:3] in ("300", "301", "302", "303", "304", "305"):
        return n == 14
    return False


_B36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def gstin_check_char(first14: str) -> str:
    total = 0
    for i, ch in enumerate(first14.upper()):
        prod = _B36.index(ch) * (2 if i % 2 else 1)
        total += prod // 36 + prod % 36
    return _B36[(36 - total % 36) % 36]


def gstin_valid(g: str) -> bool:
    g = g.upper()
    return len(g) == 15 and gstin_check_char(g[:14]) == g[14]


# ---------- patterns ----------

# no digit (or digit+separator) directly before/after: stops matching inside longer numbers
_NB = r"(?<!\w)(?<!\d[ \t-])"
_NA = r"(?![ \t-]?\d)"

UPI_HANDLES = (
    "okaxis|oksbi|okhdfcbank|okicici|ybl|ibl|axl|paytm|ptyes|ptsbi|pthdfc|ptaxis|"
    "apl|upi|axisbank|icici|sbi|hdfcbank|kotak|yesbank|freecharge|jupiteraxis|fam|slice|naviaxis"
)
STATE_CODES = (
    "AP|AR|AS|BR|CG|CH|DD|DL|GA|GJ|HP|HR|JH|JK|KA|KL|LA|LD|MH|ML|MN|MP|MZ|NL|OD|OR|PB|PY|RJ|SK|TN|TR|TS|UK|UP|WB|AN"
)

RE_AADHAAR = re.compile(_NB + r"([2-9]\d{3})([ \t-]?)(\d{4})\2(\d{4})" + _NA)
RE_PHONE = re.compile(_NB + r"(?:(?:\+91|91|0)[ \t-]?)?[6-9](?:[ \t-]?\d){9}" + _NA)
RE_CARD = re.compile(r"(?<![\w-])(?:\d{4}[ \t-]?){3}\d{1,7}(?!\d)")
RE_PAN = re.compile(r"\b[A-Z]{3}[ABCFGHLJPT][A-Z]\d{4}[A-Z]\b", re.I)
RE_GSTIN = re.compile(r"\b\d{2}[A-Z]{5}\d{4}[A-Z][1-9A-Z]Z[0-9A-Z]\b", re.I)
RE_EMAIL = re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")
RE_UPI = re.compile(r"\b[\w.-]{2,64}@(?:" + UPI_HANDLES + r")\b(?!\.\w)", re.I)
RE_VEHICLE = re.compile(
    r"\b(?:" + STATE_CODES + r")[ \t-]?\d{1,2}[ \t-]?[A-Z]{1,3}[ \t-]?\d{4}\b", re.I
)
RE_DL = re.compile(
    r"\b(?:" + STATE_CODES + r")[ \t-]?\d{2}[ \t-]?(?:19|20)\d{2}[ \t-]?\d{7}\b", re.I
)
RE_DL_OLD = re.compile(  # older state formats, need a "DL/licence" keyword: MH-1996-342322, GJ-AR-2000-239385
    r"(?:\bDL\b|licen[cs]e)[^\n]{0,15}?\b([A-Z]{2}[ \t-]?(?:[A-Z0-9]{2}[ \t-]?)?(?:19|20)\d{2}[ \t-]?\d{6,7})\b", re.I
)
RE_IP6 = re.compile(r"(?<![\w:])(?:[0-9a-f]{1,4}:){7}[0-9a-f]{1,4}(?![\w:])", re.I)
RE_IP = re.compile(r"\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|1?\d?\d)\b")
# context-gated: only flag when a keyword says what the value is
RE_BANK = re.compile(
    r"\b(?:a/c|acct|account|acc\.?\s*no|khata|bank)\b[^\n\d]{0,20}?(\d{9,18})(?!\d)", re.I
)
RE_PASSPORT = re.compile(r"passport[^\n]{0,20}?\b([A-PR-WY][1-9]\d{6})\b", re.I)
RE_VOTER = re.compile(r"(?:voter|epic)[^\n]{0,20}?\b([A-Z]{3}\d{7})\b", re.I)
_DATE = (
    r"\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}"
    r"|\d{1,2}(?:st|nd|rd|th)?\s+(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*,?\s+\d{4}"
)
RE_DOB = re.compile(
    r"(?:dob|d\.o\.b\.?|date of birth|birth\s*date|born(?: on)?|janm(?:\s*tithi)?)[^\n\d]{0,12}?(" + _DATE + r")",
    re.I,
)

# a mobile-shaped number right after these words is a reference, unless a contact word is also near
_NOT_PHONE_CTX = re.compile(r"(tracking|awb|order|shipment|consignment|container|invoice|docket|consumer|utr|txn|ref|ticket|batch|lot|sku)\b[^\n]{0,20}$", re.I)
_PHONE_CTX = re.compile(r"(phone|mobile|mob|ph|call|whatsapp|contact|number|no\.?|cell|tel|sms|otp)\b", re.I)


def phone_context_ok(text: str, start: int) -> bool:
    before = text[max(0, start - 35):start]
    return not (_NOT_PHONE_CTX.search(before) and not _PHONE_CTX.search(before))


# a 12-digit number right after these words is a tracking/order number, not Aadhaar
_NOT_AADHAAR_CTX = re.compile(r"(awb|tracking|track|order|invoice|ref|utr|txn|docket|lr)\b[^\n]{0,15}$", re.I)
_AADHAAR_CTX = re.compile(r"(aadhaar|aadhar|adhar|uid)", re.I)

# shared company inboxes are not personal data
_ROLE_INBOX = re.compile(
    r"(support|care|customercare|customer\.care|help|helpdesk|info|noreply|no-reply|orders|sales|billing|admin|contact|hello|team)@",
    re.I,
)

# higher wins when two spans overlap with equal length
PRIORITY = {
    "BANK_ACCT": 10, "GSTIN": 9, "AADHAAR": 8, "CARD": 7, "PAN": 6, "UPI": 6, "EMAIL": 5,
    "PASSPORT": 5, "VOTER_ID": 5, "DL": 5, "VEHICLE": 4, "PHONE": 3, "DOB": 3, "IP": 2,
}


def _digits(s: str) -> str:
    return re.sub(r"\D", "", s)


def detect(text: str) -> list[Span]:
    found: list[Span] = []

    for m in RE_AADHAAR.finditer(text):
        before = text[max(0, m.start() - 30):m.start()]
        if _NOT_AADHAAR_CTX.search(before) and not _AADHAAR_CTX.search(before):
            continue
        if verhoeff_valid(_digits(m.group())):
            found.append(Span(m.start(), m.end(), "AADHAAR"))

    for m in RE_CARD.finditer(text):
        d = _digits(m.group())
        if card_plausible(d) and luhn_valid(d):
            found.append(Span(m.start(), m.end(), "CARD"))

    for m in RE_GSTIN.finditer(text):
        if gstin_valid(m.group()):
            found.append(Span(m.start(), m.end(), "GSTIN"))

    simple = [
        (RE_PHONE, "PHONE"), (RE_PAN, "PAN"), (RE_UPI, "UPI"),
        (RE_EMAIL, "EMAIL"), (RE_VEHICLE, "VEHICLE"), (RE_IP, "IP"), (RE_IP6, "IP"), (RE_DL, "DL"),
    ]
    for rx, label in simple:
        for m in rx.finditer(text):
            if label == "EMAIL" and _ROLE_INBOX.match(m.group()):
                continue  # support@company is not a person's data
            if label == "PHONE" and not phone_context_ok(text, m.start()):
                continue  # "tracking 9087654321" is a reference number
            found.append(Span(m.start(), m.end(), label))

    gated = [(RE_DL_OLD, "DL"), (RE_BANK, "BANK_ACCT"), (RE_PASSPORT, "PASSPORT"), (RE_VOTER, "VOTER_ID"), (RE_DOB, "DOB")]
    for rx, label in gated:
        for m in rx.finditer(text):
            found.append(Span(m.start(1), m.end(1), label))

    return resolve_overlaps(found)


def resolve_overlaps(spans: list[Span]) -> list[Span]:
    """Keep the longest span; break ties by label priority."""
    ranked = sorted(spans, key=lambda s: (-(s.end - s.start), -PRIORITY.get(s.label, 0)))
    kept: list[Span] = []
    for s in ranked:
        if all(s.end <= k.start or s.start >= k.end for k in kept):
            kept.append(s)
    return sorted(kept, key=lambda s: s.start)
