"""Rule-layer tests. Run: python -m tests.test_rules  (from the project root)"""
import random

from pii import fake
from pii.redact import redact
from pii.rules import detect, gstin_valid, luhn_valid, verhoeff_check_digit, verhoeff_valid


def labels(text):
    return [(s.label, text[s.start:s.end]) for s in detect(text)]


def has(text, label, value):
    assert (label, value) in labels(text), f"expected {label}={value!r} in {labels(text)} for {text!r}"


def none_of(text, label=None):
    found = [l for l in labels(text) if label is None or l[0] == label]
    assert not found, f"expected no {label or 'PII'} but got {found} for {text!r}"


def valid_aadhaar(seed=1):
    base = random.Random(seed).choice("23456789") + "".join(random.Random(seed + 1).choice("0123456789") for _ in range(10))
    return base + verhoeff_check_digit(base)


def test_checksums():
    a = valid_aadhaar()
    assert verhoeff_valid(a)
    assert not verhoeff_valid(a[:-1] + str((int(a[-1]) + 1) % 10))
    assert luhn_valid("4111111111111111") and not luhn_valid("4111111111111112")
    g = fake.gstin(random.Random(3), "ABCPK1234M")
    assert gstin_valid(g) and not gstin_valid(g[:-1] + ("A" if g[-1] != "A" else "B"))


def test_aadhaar():
    a = valid_aadhaar()
    has(f"my aadhaar is {a[:4]} {a[4:8]} {a[8:]}", "AADHAAR", f"{a[:4]} {a[4:8]} {a[8:]}")
    has(f"aadhar {a}", "AADHAAR", a)
    bad = a[:-1] + str((int(a[-1]) + 1) % 10)
    none_of(f"number {bad}", "AADHAAR")
    none_of(f"AWB {a} stuck", "AADHAAR")          # tracking context
    none_of(f"UTR {a} received", "AADHAAR")


def test_phone():
    for p in ["9845012345", "98450 12345", "+91 98450 12345", "+91-9845012345", "09845012345", "98450-12345"]:
        has(f"call me on {p} pls", "PHONE", p)
    none_of("helpline 1800 102 7777", "PHONE")
    none_of("ref no 4521098765", "PHONE")         # starts with 4: not a mobile
    none_of("order OD984501234567891234", "PHONE")  # inside a longer ID
    has("1. A. Banerjee, 9830012345\n2. S. Ghosh", "PHONE", "9830012345")  # numbers don't span lines


def test_ids():
    has("PAN: ABCPK1234M", "PAN", "ABCPK1234M")
    has("pan abcpk1234m", "PAN", "abcpk1234m")
    g = fake.gstin(random.Random(5), "ABCPK1234M")
    assert labels(f"GSTIN {g}") == [("GSTIN", g)]  # not also a PAN
    has("card 4111 1111 1111 1111 charged", "CARD", "4111 1111 1111 1111")
    none_of("IFSC SBIN0001234")
    none_of("deliver to 560066 pls")              # pincode alone
    has("bike KA 01 AB 1234", "VEHICLE", "KA 01 AB 1234")
    has("ip 49.207.12.4 blocked", "IP", "49.207.12.4")


def test_dl_and_inboxes():
    has("DL No: KA0520190012345", "DL", "KA0520190012345")
    has("licence MH-12-2015-0045678", "DL", "MH-12-2015-0045678")
    none_of("mail customercare@shopkart.in or support@abc.com", "EMAIL")
    has("mail ramesh.k@shopkart.in", "EMAIL", "ramesh.k@shopkart.in")


def test_m3_rule_upgrades():
    has("ip 2e3e:77a0:3970:255c:1564:687f:fa0d:1a22 blocked", "IP", "2e3e:77a0:3970:255c:1564:687f:fa0d:1a22")
    has("DL No: MH-1996-342322", "DL", "MH-1996-342322")
    none_of("Shipment tracking 7788123456 cleared customs", "PHONE")
    has("order late, call 9845012345", "PHONE", "9845012345")
    has("tracking update pls, my number 9845012345", "PHONE", "9845012345")


def test_email_vs_upi():
    has("mail ramesh.k@gmail.com", "EMAIL", "ramesh.k@gmail.com")
    has("upi ramesh.k@okaxis", "UPI", "ramesh.k@okaxis")
    assert labels("pay 9845012345@ybl") == [("UPI", "9845012345@ybl")]


def test_context_gated():
    has("a/c no 50100123456789 IFSC HDFC0001234", "BANK_ACCT", "50100123456789")
    none_of("qty 50100123456789")
    has("passport no M1234567", "PASSPORT", "M1234567")
    has("voter id ABC1234567", "VOTER_ID", "ABC1234567")
    has("DOB: 14/03/1988", "DOB", "14/03/1988")
    has("born on 3rd Jan 1992", "DOB", "3rd Jan 1992")
    none_of("delivery date 12/10/2026", "DOB")


def test_redact_consistent_tokens():
    text = "call 98450 12345 or +91 9845012345, mail a.b@gmail.com"
    red, vault = redact(text)
    assert red == "call [PHONE_1] or [PHONE_2], mail [EMAIL_1]", red
    red2, _ = redact("98450 12345 then 98450-12345 again")
    assert red2 == "[PHONE_1] then [PHONE_1] again", red2
    assert vault["[EMAIL_1]"] == "a.b@gmail.com"


if __name__ == "__main__":
    tests = [v for k, v in dict(globals()).items() if k.startswith("test_")]
    for t in tests:
        t()
        print(f"ok  {t.__name__}")
    print(f"{len(tests)} tests passed")
