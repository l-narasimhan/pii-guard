"""Build labelled training data from templates + fake values.

Slots like {NAME} are filled with fake values; the character span of every
PII slot is recorded as it's inserted, so labels are exact by construction.
Hard-negative slots ({ORDER}, {AWB}, {ORG}...) add look-alike text with no label.

Some templates are held out entirely and appear only in the test set, so the
test measures generalisation, not memorised sentence shapes.

    python -m pii.generate            # writes data/{train,valid,test}.jsonl
"""
import json
import random
import re
from pathlib import Path

from . import fake

SLOT_LABEL = {
    "NAME": "NAME", "FIRST": "NAME", "NAME2": "NAME", "NAME3": "NAME",
    "PHONE": "PHONE", "PHONE2": "PHONE", "ADDR": "ADDRESS", "EMAIL": "EMAIL",
    "UPI": "UPI", "AADHAAR": "AADHAAR", "PAN": "PAN", "GSTIN": "GSTIN", "CARD": "CARD",
    "BANK": "BANK_ACCT", "PASSPORT": "PASSPORT", "VOTER": "VOTER_ID", "VEHICLE": "VEHICLE",
    "DOB": "DOB", "IP": "IP",
}

# (template, lang). Hinglish = Hindi in Latin script mixed with English.
CHAT = [
    ("Hi, my name is {NAME} and my order {ORDER} hasn't arrived yet. Please call me on {PHONE}.", "en"),
    ("this is {FIRST}, can you update my address to {ADDR}? thanks", "en"),
    ("Refund not received for order {ORDER}. My UPI is {UPI}", "en"),
    ("I paid {AMT} using card {CARD} but the order shows failed", "en"),
    ("Please send the invoice to {EMAIL}, order {ORDER}", "en"),
    ("delivery guy called from {PHONE2}?? who is this. my number is {PHONE}", "en"),
    ("my aadhaar number is {AADHAAR} for KYC", "en"),
    ("PAN for the GST invoice: {PAN}. Name on PAN {NAME}", "en"),
    ("Hi team, AWB {AWB} stuck since {DATE}. Contact {PHONE}", "en"),
    ("I want to return the {PRODUCT}, pickup from {ADDR}", "en"),
    ("Can you deliver to my office instead? {ADDR}. Ask for {NAME} at reception", "en"),
    ("Wrong item received. Ordered {SKU} but got something else. {REF}", "en"),
    ("my email changed, new one is {EMAIL}. old phone {PHONE} also not working", "en"),
    ("refund to bank pls, a/c no {BANK} IFSC {IFSC}, name {NAME}", "en"),
    ("is {PIN} serviceable? want to order before {FEST}", "en"),
    ("Ordered from {ORG}, they said call {HELPLINE}. Still no update on {ORDER}", "en"),
    ("my dob is {DOB}, why is age verification failing?", "en"),
    ("Hi, {NAME} here from {ORG}. Our GSTIN is {GSTIN}, please correct invoice {INV}", "en"),
    ("passport no {PASSPORT} uploaded for international shipping, pls verify", "en"),
    ("the rider {NAME2} with bike {VEHICLE} was very rude", "en"),
    ("Login issue, getting blocked from IP {IP}. account email {EMAIL}", "en"),
    ("please reach my wife {NAME2} on {PHONE2} if I don't pick up", "en"),
    ("voter id {VOTER} is my address proof, is that ok?", "en"),
    ("{FEST} sale order {ORDER} for {AMT} still not shipped from {ORG}", "en"),
    ("Hello I am {NAME}, {PHONE}, {EMAIL}. Order {ORDER} arrived damaged", "en"),
    ("bhai mera order {ORDER} abhi tak nahi aaya, mera number {PHONE} hai", "hi"),
    ("mera naam {NAME} hai, address change karna hai: {ADDR}", "hi"),
    ("refund kab aayega? UPI id {UPI} pe bhej do", "hi"),
    ("delivery wale ko bolo {ADDR} pe aaye, {FIRST} ka ghar", "hi"),
    ("haan ji, aadhaar {AADHAAR} hai mera, KYC kar do", "hi"),
    ("{FEST} ke pehle {PIN} pe delivery hogi kya?", "hi"),
    ("maine {AMT} pay kiya card {CARD} se, paisa kat gaya order nahi hua", "hi"),
    ("sir {ORG} se order kiya tha {ORDER}, abhi tak dispatch nahi hua", "hi"),
    ("mere bhai {NAME2} ko de dena parcel, uska number {PHONE2}", "hi"),
    ("email pe bhejo invoice: {EMAIL}", "hi"),
    ("AWB {AWB} track nahi ho raha, kya scene hai", "hi"),
    ("PAN {PAN} daal diya hai, ab bhi error aa raha", "hi"),
    ("account number {BANK} hai, khata {NAME} ke naam pe hai", "hi"),
    ("rider {NAME2} ne bola gaadi {VEHICLE} hai, but koi aaya hi nahi", "hi"),
    ("kal se {HELPLINE} pe call kar raha hoon, koi uthata nahi. {REF}", "hi"),
    ("mera janm tithi {DOB} hai, form me galat aa raha", "hi"),
    ("{SKU} wala item damage aaya, {REF}", "hi"),
    ("{FIRST} bol raha hoon, parcel {ADDR} pe chhod dena, gate pe guard ko", "hi"),
    ("{ORG} wale {FIRST} ji ne bola tha {DATE} tak aa jayega", "hi"),
    ("Agent: Can I have your registered mobile number?\nCustomer: haan, {PHONE}\nAgent: And your name?\nCustomer: {NAME}", "hi"),
    ("Agent: Please confirm the delivery address.\nCustomer: {ADDR}\nAgent: Thank you {FIRST} ji.", "en"),
    ("Agent: Order {ORDER} is out for delivery.\nCustomer: ok, rider ka number do\nAgent: {NAME3}, {PHONE2}", "hi"),
    ("Customer: my card {CARD} got charged twice\nAgent: Sorry {FIRST}, refund of {AMT} initiated, {REF}", "en"),
]

# Documents: (id, header, [(line, required)]). Optional lines are dropped at random
# and the order of body lines is lightly shuffled, so each doc looks different.
DOCS = [
    ("kyc_form", "CUSTOMER KYC FORM", [
        ("Name: {NAME}", True), ("Father's Name: {NAME2}", False), ("Date of Birth: {DOB}", False),
        ("PAN: {PAN}", False), ("Aadhaar No: {AADHAAR}", False), ("Address: {ADDR}", True),
        ("Mobile: {PHONE}", True), ("Email: {EMAIL}", False), ("Bank A/c No: {BANK}", False),
        ("IFSC: {IFSC}", False), ("Date: {DATE}", False)]),
    ("invoice", "TAX INVOICE", [
        ("Seller: {ORG}", True), ("GSTIN: {GSTIN}", True), ("Invoice No: {INV}   Date: {DATE}", True),
        ("Bill To: {NAME}", True), ("{ADDR}", True), ("Phone: {PHONE}", False),
        ("Item: {PRODUCT}   SKU: {SKU}   Amount: {AMT}", True), ("Order ID: {ORDER}", False),
        ("For support call {HELPLINE}", False)]),
    ("pod", "PROOF OF DELIVERY", [
        ("AWB: {AWB}", True), ("Consignee: {NAME}", True), ("Delivery Address: {ADDR}", True),
        ("Received by: {NAME2} (family member)", False), ("Delivered on: {DATE}", True),
        ("Rider: {NAME3}   Vehicle: {VEHICLE}", False), ("Contact: {PHONE}", False)]),
    ("complaint", "To,\nThe Customer Care Manager,\n{ORG}", [
        ("Subject: Complaint regarding order {ORDER}", True),
        ("I, {NAME}, residing at {ADDR}, placed order {ORDER} on {DATE} for {AMT}.", True),
        ("The {PRODUCT} received was damaged and no one has responded on {HELPLINE}.", False),
        ("You may contact me at {PHONE} or {EMAIL}.", True), ("Yours sincerely,\n{NAME}", True)]),
    ("seller_onboarding", "SELLER REGISTRATION", [
        ("Business Name: {ORG}", True), ("GSTIN: {GSTIN}", True), ("Proprietor: {NAME}", True),
        ("PAN: {PAN}", True), ("Aadhaar: {AADHAAR}", False), ("Registered Address: {ADDR}", True),
        ("Contact: {PHONE} / {EMAIL}", True), ("Settlement A/c: {BANK}   IFSC: {IFSC}", False)]),
    ("export_invoice", "COMMERCIAL INVOICE (EXPORT)", [
        ("Exporter: {ORG}, GSTIN {GSTIN}", True), ("Shipper contact: {NAME}, {PHONE}", True),
        ("Passport No: {PASSPORT}", False), ("Consignee: {NAME2}", True), ("Invoice: {INV}", True),
        ("Description: {PRODUCT}   Value: {AMT}", True)]),
    ("app_log", "", [
        ("2026-10-09 14:22:01 INFO login ok user={EMAIL} ip={IP}", True),
        ("2026-10-09 14:22:07 INFO order_created id={ORDER} amount={AMT}", True),
        ("2026-10-09 14:23:15 WARN payment_retry upi={UPI} ref={REF}", False),
        ("2026-10-09 14:23:40 INFO shipment awb={AWB} pin={PIN}", False),
        ("2026-10-09 14:24:02 DEBUG notify sms to={PHONE}", False)]),
    # held out: never seen in training
    ("rider_onboarding", "DELIVERY PARTNER ONBOARDING", [
        ("Name: {NAME}", True), ("DOB: {DOB}", True), ("Mobile: {PHONE}", True),
        ("Vehicle No: {VEHICLE}", True), ("Voter ID (EPIC): {VOTER}", False), ("Aadhaar: {AADHAAR}", False),
        ("Emergency Contact: {NAME2}, {PHONE2}", False), ("Hub: {ORG}, {PIN}", False)]),
    ("payment_receipt", "PAYMENT RECEIPT", [
        ("Received from: {NAME}", True), ("Amount: {AMT}", True), ("Mode: Card {CARD}", False),
        ("UPI: {UPI}", False), ("Reference: {REF}", True), ("Order: {ORDER}", True), ("Email: {EMAIL}", False)]),
]

# picked so every label still appears in test; each label also stays in training via other templates
# ---- M3 additions (from M2 gap analysis). New wording, not copied from the hand-written test set. ----
SLOT_LABEL.update({
    "FIRSTN": "NAME", "PHONEX": "PHONE", "PHA": "PHONE", "PHB": "PHONE", "LANDLINE": "PHONE",
    "FPHONE": "PHONE", "EMAILX": "EMAIL", "PANX": "PAN", "UPIX": "UPI", "BANKX": "BANK_ACCT",
    "ADDRX": "ADDRESS", "DL": "DL",
})
N_CHAT_V1 = len(CHAT)
CHAT += [
    # lone first names: thanks, greetings, relations, honorifics
    ("thank you {FIRSTN} for sorting this out so quickly", "en"),
    ("{FIRSTN} ji ne promise kiya tha refund 2 din me aayega", "hi"),
    ("{FIRSTN} madam please look into order {ORDER}", "en"),
    ("hello {FIRSTN}, still no update from your side", "en"),
    ("my sister {FIRSTN} will collect it, she's at home after 5", "en"),
    ("{FIRSTN} sir, AWB {AWB} pe koi movement nahi hai", "hi"),
    ("I spoke to {FIRSTN} on chat yesterday, she said two days", "en"),
    ("ok thanks {FIRSTN} 🙏", "en"),
    ("parcel {FIRSTN} ko de dena, woh gate pe hoga", "hi"),
    ("{FIRSTN} bhaiya kal aaye the par ghar pe koi nahi tha", "hi"),
    ("wife {FIRSTN} ka number {PHONE2} hai, usko call karo", "hi"),
    # south Indian languages in Latin script
    ("nanna hesaru {NAME}, order {ORDER} innu bandilla", "kn"),
    ("{ADDRX} ge kalsi, mane hatra guard idare", "kn"),
    ("ee number ge call maadi {PHONE}, office nalli iddini", "kn"),
    ("en per {NAME}, parcel innum varavillai", "ta"),
    ("{ADDR} ku anuppunga, {FIRSTN} kitta kudunga", "ta"),
    ("indha number ku call pannunga {PHONE}", "ta"),
    ("na peru {NAME}, order inka raaledu", "te"),
    ("{ADDRX} ki pampandi, {FIRSTN} ki ivvandi", "te"),
    ("ee number ki call cheyyandi {PHONE}", "te"),
    ("ente peru {NAME}, order ithu vare vannilla", "ml"),
    ("{ADDR} il ethikkanam, {PHONE} il vilikku", "ml"),
    # disguised / unusual numbers and IDs
    ("my mobile is {PHONEX}, whatsapp same", "en"),
    ("number {PHA} ... wait, full number {PHA} {PHB}", "en"),
    ("first part {PHA}, second part {PHB}, call pls", "en"),
    ("mob{PHONE} pe call karo", "hi"),
    ("if mobile off call home {LANDLINE}", "en"),
    ("landline {LANDLINE} pe raat ko call karna", "hi"),
    ("I'm abroad, reach me on {FPHONE}", "en"),
    ("son is in US, his number {FPHONE}, he placed the order", "en"),
    ("mail me at {EMAILX}", "en"),
    ("email id {EMAILX} hai, wahan bhejo", "hi"),
    ("PAN {PANX} hai mera, invoice me daalo", "hi"),
    ("my pan is {PANX}", "en"),
    ("refund this upi {UPIX}", "en"),
    ("{UPIX} pe paisa bhej do", "hi"),
    ("put the refund in {BANKX} {IFSC}", "en"),
    ("{BANKX} canara bank, isme refund karo", "hi"),
    ("driving licence {DL} uploaded for rider signup", "en"),
    ("DL number {DL} hai, verify karo", "hi"),
    # informal addresses
    ("deliver at {ADDRX}", "en"),
    ("ghar ka pata: {ADDRX}", "hi"),
    ("rider is lost, tell him {ADDRX}", "en"),
    # hard negatives (no PII)
    ("my aadhaar ending {MASKED}, is that enough for kyc?", "en"),
    ("paid by card ending {LAST4}, still pending", "en"),
    ("is {LOCALITY} serviceable for express?", "en"),
    ("{LOCALITY} side delivery kab start hoga?", "hi"),
    ("wrote to {INBOX} three times, no reply", "en"),
    ("Agent: Hello, how may I help you?\nCustomer: order {ORDER} late hai\nAgent: Checking, please hold", "hi"),
    ("Support: order {ORDER} is packed\nCustomer: ok thanks", "en"),
    ("got {FEST} offer from {ORG}, coupon not applying", "en"),
    ("account ending {LAST4} me paisa nahi aaya", "hi"),
]
# held out for test: the original picks + every 4th new template
_NEW_HELD = ["{FIRSTN} madam please", "I spoke to {FIRSTN}", "en per {NAME}", "na peru {NAME}", "{ADDRX} ki pampandi",
             "number {PHA} ... wait", "if mobile off call home", "son is in US", "email id {EMAILX}", "my pan is {PANX}",
             "{UPIX} pe paisa", "DL number {DL}", "rider is lost", "paid by card ending", "{LOCALITY} side delivery",
             "Support: order {ORDER} is packed"]
HELD_OUT_CHAT = {4, 9, 13, 17, 18, 19, 20, 24, 29, 36, 39, 44} | {
    i for i in range(N_CHAT_V1, len(CHAT)) if any(CHAT[i][0].startswith(h) for h in _NEW_HELD)}
HELD_OUT_DOCS = {"rider_onboarding", "payment_receipt", "visitor_log"}
SLOT_RE = re.compile(r"\{([A-Z0-9]+)\}")
ROW_RE = re.compile(r"([A-Z]+?)R(\d+)")  # {NAMER2} = NAME of row-person 2
PERSON_SLOTS = {"NAME", "FIRST", "PHONE", "EMAIL", "UPI", "PHONEX", "PHA", "PHB", "EMAILX", "UPIX"}


class Sample:
    """Fills slots for one example; repeated slots reuse the same value."""

    def __init__(self, r: random.Random, chat: bool):
        self.r, self.chat = r, chat
        self.p1, self.p2, self.p3 = fake.Person(r), fake.Person(r), fake.Person(r)
        self.rows: dict[int, fake.Person] = {}
        self.cache: dict[str, str] = {}

    @staticmethod
    def base(slot: str) -> str:
        m = ROW_RE.fullmatch(slot)
        return m.group(1) if m else slot

    def value(self, slot: str) -> str:
        if slot in self.cache:
            return self.cache[slot]
        m = ROW_RE.fullmatch(slot)
        if m:
            base, idx = m.group(1), int(m.group(2))
            p = self.rows.setdefault(idx, fake.Person(self.r))
        else:
            base, p = slot, self.p1
        self.cache[slot] = self.make(base, p)
        return self.cache[slot]

    def make(self, slot: str, p: "fake.Person") -> str:
        r = self.r
        makers = {
            "NAME": lambda: p.name, "FIRST": lambda: p.first, "NAME2": lambda: self.p2.name,
            "NAME3": lambda: self.p3.name, "PHONE": lambda: p.phone(self.chat), "PHONE2": lambda: self.p2.phone(self.chat),
            "ADDR": lambda: fake.address(r), "EMAIL": p.email, "UPI": p.upi,
            "AADHAAR": lambda: fake.aadhaar(r), "PAN": lambda: self.pan(),
            "GSTIN": lambda: fake.gstin(r, self.pan()), "CARD": lambda: fake.card(r),
            "BANK": lambda: fake.bank_acct(r), "PASSPORT": lambda: fake.passport(r),
            "VOTER": lambda: fake.voter_id(r), "VEHICLE": lambda: fake.vehicle(r),
            "DOB": lambda: fake.dob(r), "IP": lambda: fake.ip(r),
            "ORDER": lambda: fake.order_id(r), "AWB": lambda: fake.awb(r), "SKU": lambda: fake.sku(r),
            "INV": lambda: fake.invoice_no(r), "AMT": lambda: fake.amount(r), "PIN": lambda: fake.pincode(r),
            "ORG": lambda: r.choice(fake.ORGS), "HELPLINE": lambda: fake.helpline(r),
            "DATE": lambda: fake.date(r), "REF": lambda: fake.ref_no(r), "IFSC": lambda: fake.ifsc(r),
            "PRODUCT": lambda: r.choice(fake.PRODUCTS), "FEST": lambda: r.choice(fake.FESTIVALS),
            # M3 additions
            "FIRSTN": lambda: r.choice(fake.FIRST), "PHONEX": lambda: fake.phone_messy(r, p.mobile),
            "PHA": lambda: p.mobile[:5], "PHB": lambda: p.mobile[5:], "LANDLINE": lambda: fake.landline(r),
            "FPHONE": lambda: fake.foreign_phone(r), "EMAILX": lambda: fake.email_obfuscated(r, p.first, p.last),
            "PANX": lambda: fake.pan_spaced(self.pan(), r), "UPIX": lambda: fake.upi_unknown(r, p.first),
            "BANKX": lambda: fake.bank_acct(r), "ADDRX": lambda: fake.address_informal(r),
            "DL": lambda: fake.driving_licence(r), "LOCALITY": lambda: fake.locality(r),
            "MASKED": lambda: fake.masked_id(r), "LAST4": lambda: fake.digits(r, 4),
            "INBOX": lambda: fake.company_inbox(r), "ROLE": lambda: r.choice(fake.ROLES),
            "TIME": lambda: f"{r.randint(8, 21)}:{r.randint(0, 59):02d}",
        }
        return makers[slot]()

    def pan(self) -> str:
        if "_pan" not in self.cache:
            self.cache["_pan"] = self.p1.pan()
        return self.cache["_pan"]

    def render(self, template: str) -> tuple[str, list[dict]]:
        out, spans, pos, cursor = [], [], 0, 0
        for m in SLOT_RE.finditer(template):
            lit = template[cursor:m.start()]
            out.append(lit)
            pos += len(lit)
            val = self.value(m.group(1))
            label = SLOT_LABEL.get(self.base(m.group(1)))
            if label:
                spans.append({"start": pos, "end": pos + len(val), "label": label})
            out.append(val)
            pos += len(val)
            cursor = m.end()
        out.append(template[cursor:])
        return "".join(out), spans


def doc_template(r: random.Random, header: str, lines: list) -> str:
    body = [l for l, req in lines if req or r.random() < 0.6]
    for i in range(len(body) - 1):  # light shuffle: swap neighbours sometimes
        if r.random() < 0.2:
            body[i], body[i + 1] = body[i + 1], body[i]
    return "\n".join(([header] if header else []) + body)


# ---- table / list documents: several people per document ----
def rows(r, n_min=2, n_max=5):
    return range(1, r.randint(n_min, n_max) + 1)


def csv_export(r):
    head = r.choice(["id,name,phone,city,rating", "customer_name,mobile,email,order_id", "name|phone|pincode"])
    lines = []
    for i in rows(r):
        if head.startswith("id,"):
            lines.append(f"{100 + i},{{NAMER{i}}},{{PHONER{i}}},{{LOCALITYR{i}}},{r.randint(1, 5)}")
        elif head.startswith("customer"):
            lines.append(f"{{NAMER{i}}},{{PHONER{i}}},{{EMAILR{i}}},{{ORDERR{i}}}")
        else:
            lines.append(f"{{NAMER{i}}}|{{PHONER{i}}}|{{PINR{i}}}")
    return "\n".join([r.choice(["Customer feedback export", "Export.csv", "report_oct.csv"]), head] + lines)


def payout_sheet(r):
    lines = [f"{{NAMER{i}}}  {{BANKXR{i}}}  {{AMTR{i}}}" for i in rows(r)]
    return "\n".join([r.choice(["Rider payout - week 41", "Vendor payments due", "Weekly settlement"])] + lines)


def manifest(r):
    lines = [f"{i}. {{NAMER{i}}}, {r.choice(['{ADDRR' + str(i) + '}', '{ADDRXR' + str(i) + '}'])}, {{PHONER{i}}}"
             for i in rows(r)]
    return "\n".join([r.choice(["Courier manifest", "Delivery run sheet", "Pickup list"])] + lines)


def whatsapp_export(r):
    lines = []
    for k in range(r.randint(2, 5)):
        who = r.choice(["{NAMER1}", "Support", "{NAMER1}"])
        msg = r.choice(["parcel nahi aaya", "please share order id", "{ORDER}", "number {PHONER1}",
                        "address {ADDRR1}", "ok", "kab tak aayega?", "refund {UPIR1} pe"])
        lines.append(f"[{{DATE}}, {{TIMER{k}}}] {who}: {msg}")
    return "WhatsApp chat export\n" + "\n".join(lines)


def email_signature(r):
    return r.choice(["Regards,", "Thanks & regards,", "Best,"]) + "\n{NAME}\n{ROLE}, {ORG}\n" + \
        r.choice(["{PHONE} | {EMAIL}", "Mob: {PHONE}", "{EMAIL}", "{PHONE}"])


def visitor_log(r):  # held out
    lines = [f"{{NAMER{i}}}  {{PHONER{i}}}  in {{TIMER{2 * i}}}  out {{TIMER{2 * i + 1}}}" for i in rows(r)]
    return "\n".join([r.choice(["Visitor log - Hub", "Gate register", "Attendance"])] + lines)


DOC_BUILDERS = [(d[0], (lambda r, h=d[1], l=d[2]: doc_template(r, h, l))) for d in DOCS] + [
    ("csv_export", csv_export), ("payout_sheet", payout_sheet), ("manifest", manifest),
    ("whatsapp_export", whatsapp_export), ("email_signature", email_signature), ("visitor_log", visitor_log),
]


def make(r: random.Random, split: str) -> dict:
    test = split == "test"
    chat = r.random() < 0.6
    s = Sample(r, chat)
    if chat:
        pool = [i for i in range(len(CHAT)) if (i in HELD_OUT_CHAT) == test]
        i = r.choice(pool)
        template, lang = CHAT[i]
        text, spans = s.render(template)
        if r.random() < 0.35:
            text = text.lower()  # same length, spans still valid
        return {"text": text, "spans": spans, "source": "chat", "template": f"chat_{i}", "lang": lang}
    pool = [d for d in DOC_BUILDERS if (d[0] in HELD_OUT_DOCS) == test]
    tid, build = r.choice(pool)
    text, spans = s.render(build(r))
    return {"text": text, "spans": spans, "source": "doc", "template": tid, "lang": "en"}


def main(out_dir: str = "data", n_train: int = 15000, n_valid: int = 1500, n_test: int = 2000, seed: int = 7):
    r = random.Random(seed)
    out = Path(out_dir)
    out.mkdir(exist_ok=True)
    for split, n in [("train", n_train), ("valid", n_valid), ("test", n_test)]:
        with open(out / f"{split}.jsonl", "w") as f:
            for k in range(n):
                ex = make(r, split)
                ex["id"] = f"{split}-{k:05d}"
                f.write(json.dumps(ex, ensure_ascii=False) + "\n")
        print(f"{split}: {n} examples -> {out / f'{split}.jsonl'}")


if __name__ == "__main__":
    main()
