"""Fake-but-valid Indian PII values and look-alike non-PII (hard negatives).

All values are synthetic. Aadhaar/GSTIN/card numbers carry correct check
digits so they look exactly like real ones to the rules.
"""
import random

from .rules import gstin_check_char, luhn_valid, verhoeff_check_digit

FIRST = """Ramesh Suresh Mahesh Rajesh Anil Sunil Vijay Sanjay Arun Kiran Prakash Ravi Manoj
Deepak Amit Rohit Rahul Vikram Arjun Karthik Venkatesh Srinivas Naveen Harish Ganesh Mohan
Murali Senthil Balaji Prasad Abdul Imran Faizan Salman Irfan Joseph Thomas George Gurpreet
Harjeet Manpreet Jasvinder Farhan Aditya Ishaan Kunal Nikhil Pranav Siddharth Varun Yash
Priya Lakshmi Anjali Kavya Divya Pooja Sneha Neha Shruti Meera Radha Sunita Geeta Rekha
Anita Deepa Swati Shalini Asha Uma Padma Revathi Kavitha Bhavana Sangeetha Nandini Ayesha
Fatima Zainab Mary Teresa Simran Harleen Ananya Diya Ishita Riya Tanvi Aarohi Meenakshi
Savitri Shanti Durga Gauri Parvati Bharati Jyoti Kusum Hema Latha Rukmini Chitra Sudha
Debashish Subhash Arindam Sourav Tanmoy Bikash Pradeep Jitendra Dinesh Lokesh Yogesh Ritesh""".split()

LAST = """Kumar Sharma Verma Gupta Singh Yadav Patel Shah Mehta Joshi Desai Kulkarni Deshpande
Patil Pawar Jadhav Reddy Rao Naidu Iyer Iyengar Nair Menon Pillai Krishnan Subramanian
Raghavan Gowda Hegde Shetty Bhat Kamath Das Bose Chatterjee Banerjee Mukherjee Ghosh Sen
Roy Dutta Mishra Tiwari Pandey Dubey Tripathi Srivastava Saxena Agarwal Bansal Goyal Jain
Khan Ansari Siddiqui Qureshi Shaikh Sayyed Fernandes DSouza Pereira Rodrigues Thomas
Kaur Gill Sandhu Dhillon Grewal Chauhan Rathore Thakur Negi Rawat Bisht Mahajan Kapoor
Malhotra Khanna Chopra Bhatia Arora Sethi Murthy Shastri Achari Chettiar Mudaliar""".split()

CITIES = {
    "Bengaluru": ("560", ["Whitefield", "Koramangala", "Indiranagar", "HSR Layout", "Jayanagar",
                          "Malleshwaram", "Electronic City", "Marathahalli", "Yelahanka", "BTM Layout"]),
    "Mumbai": ("400", ["Andheri West", "Bandra East", "Powai", "Dadar", "Borivali", "Malad West"]),
    "Thane": ("400", ["Thane West", "Ghodbunder Road", "Majiwada"]),
    "Delhi": ("110", ["Lajpat Nagar", "Dwarka Sector 12", "Rohini Sector 7", "Karol Bagh", "Saket"]),
    "Hyderabad": ("500", ["Gachibowli", "Kukatpally", "Madhapur", "Ameerpet", "Kondapur"]),
    "Chennai": ("600", ["T Nagar", "Velachery", "Adyar", "Anna Nagar", "Tambaram"]),
    "Pune": ("411", ["Kothrud", "Hinjewadi", "Viman Nagar", "Baner", "Wakad"]),
    "Kolkata": ("700", ["Salt Lake Sector V", "Behala", "Garia", "New Town"]),
    "Gurugram": ("122", ["DLF Phase 3", "Sector 56", "Sohna Road"]),
    "Noida": ("201", ["Sector 62", "Sector 137", "Sector 18"]),
    "Ahmedabad": ("380", ["Navrangpura", "Satellite", "Bopal"]),
    "Jaipur": ("302", ["Malviya Nagar", "Vaishali Nagar", "Mansarovar"]),
    "Lucknow": ("226", ["Gomti Nagar", "Aliganj", "Indira Nagar"]),
    "Kochi": ("682", ["Kakkanad", "Edappally", "Kaloor"]),
}
SOCIETIES = """Prestige Shantiniketan|Sobha Dream Acres|Brigade Metropolis|Hiranandani Gardens|Lodha Palava|
DLF Park Place|Godrej Woods|Mantri Espana|Purva Panorama|Raheja Vihar|Shanti Kunj Apartments|
Sai Krupa Residency|Green Valley Apartments|Sri Lakshmi Nilayam|Ganga Enclave|Rose Garden CHS""".replace("\n", "").split("|")
LANDMARKS = ["near Hanuman temple", "opp. SBI ATM", "behind Reliance Fresh", "near bus stand",
             "next to Apollo Pharmacy", "opp. Ganesh temple", "near metro station",
             "behind govt school", "near water tank", "opposite petrol pump", "near masjid",
             "beside St. Mary's church"]
STREETS = ["MG Road", "Station Road", "100 Feet Road", "Link Road", "Gandhi Marg", "Nehru Street",
           "Temple Road", "Main Bazaar Road", "Old Airport Road"]

ORGS = ["Ganesh Traders", "Lakshmi General Stores", "Sri Balaji Enterprises", "Ramesh Medicals",
        "Krishna Dairy", "Sai Ram Kirana", "Annapurna Foods Pvt Ltd", "Mahalaxmi Textiles",
        "Shree Krishna Electronics", "Gupta & Sons", "Raju Mobiles", "Venkateswara Agencies",
        "Patel Brothers Hardware", "Murugan Stores", "Fatima Bakery", "Joseph & Co"]
PRODUCTS = ["Amul Taaza 1L", "boAt Airdopes 141", "Prestige induction cooktop", "Nike running shoes",
            "Samsung M14 back cover", "Tata Salt 1kg", "Aashirvaad Atta 5kg", "Philips trimmer",
            "Milton bottle 1L", "Lakme kajal", "Parle-G family pack", "Bajaj mixer grinder"]
FESTIVALS = ["Diwali", "Ganesh Chaturthi", "Hanuman Jayanti", "Eid", "Christmas", "Pongal",
             "Onam", "Durga Puja", "Holi", "Navratri"]
EMAIL_DOMAINS = ["gmail.com", "yahoo.co.in", "outlook.com", "rediffmail.com", "hotmail.com"]
UPI_SUFFIX = ["okaxis", "oksbi", "okhdfcbank", "okicici", "ybl", "ibl", "paytm", "axl"]
BANK_CODES = ["SBIN", "HDFC", "ICIC", "UTIB", "KKBK", "PUNB", "CNRB", "BARB", "IDIB", "YESB"]
STATE_VEH = ["KA", "MH", "DL", "TN", "TS", "AP", "KL", "UP", "GJ", "RJ", "WB", "HR"]
WORDS = "zero one two three four five six seven eight nine".split()
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTHS_LONG = ["January", "February", "March", "April", "May", "June", "July", "August",
               "September", "October", "November", "December"]


def digits(r: random.Random, n: int) -> str:
    return "".join(r.choice("0123456789") for _ in range(n))


class Person:
    """One consistent fake person, so email/UPI/PAN match the name."""

    def __init__(self, r: random.Random):
        self.r = r
        self.first = r.choice(FIRST)
        self.last = r.choice(LAST)
        self.mobile = r.choice("6789") + digits(r, 9)

    @property
    def name(self):
        r = self.r.random()
        if r < 0.12:
            return f"{self.first} {self.r.choice('ABCDEGHKMNPRSTV')}. {self.last}"
        if r < 0.2:
            return f"{self.first[0]}. {self.last}"
        return f"{self.first} {self.last}"

    def phone(self, spoken_ok: bool = True):
        m, r = self.mobile, self.r.random()
        if spoken_ok and r < 0.04:
            return " ".join(WORDS[int(c)] for c in m)  # spoken form, rules can't catch
        forms = [m, f"{m[:5]} {m[5:]}", f"+91 {m[:5]} {m[5:]}", f"+91-{m}", f"0{m}",
                 f"{m[:5]}-{m[5:]}", f"{m[:4]} {m[4:7]} {m[7:]}", f"+91{m}"]
        return self.r.choice(forms)

    def email(self):
        f, l = self.first.lower(), self.last.lower()
        user = self.r.choice([f"{f}.{l}", f"{f}{l[0]}", f"{f}{digits(self.r, 2)}", f"{l}.{f}{digits(self.r, 3)}",
                              f"{f}_{l}"])
        return f"{user}@{self.r.choice(EMAIL_DOMAINS)}"

    def upi(self):
        if self.r.random() < 0.3:
            return f"{self.mobile}@{self.r.choice(['ybl', 'paytm', 'ibl', 'axl'])}"
        return f"{self.first.lower()}.{self.last[0].lower()}{self.r.choice(['', digits(self.r, 2)])}@{self.r.choice(UPI_SUFFIX)}"

    def pan(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ("".join(self.r.choice(letters) for _ in range(3)) + "P" + self.last[0].upper()
                + digits(self.r, 4) + self.r.choice(letters))


def address(r: random.Random) -> str:
    city = r.choice(list(CITIES))
    prefix, localities = CITIES[city]
    loc = r.choice(localities)
    pin = prefix + digits(r, 3)
    soc, lm, st = r.choice(SOCIETIES), r.choice(LANDMARKS), r.choice(STREETS)
    flat = f"{r.choice('ABCDE')}-{r.randint(1, 18)}{r.randint(0, 9)}{r.randint(1, 8)}"
    forms = [
        f"Flat {flat}, {soc}, {lm}, {loc}, {city} - {pin}",
        f"H.No. {r.randint(1, 20)}-{r.randint(1, 9)}-{r.randint(10, 400)}/{r.randint(1, 90)}, {st}, {loc}, {city} {pin}",
        f"#{r.randint(1, 999)}, {r.randint(1, 20)}th Cross, {r.randint(1, 12)}th Main, {loc}, {city} {pin}",
        f"{r.randint(1, 300)}, Gali No. {r.randint(1, 15)}, {loc}, {city}",
        f"{flat}, {soc}, {loc}",
        f"{soc}, flat {flat}, {lm}, {loc} {pin}",
        f"Plot {r.randint(1, 400)}, {st}, {lm}, {loc}, {city}",
    ]
    return r.choice(forms)


def aadhaar(r: random.Random) -> str:
    base = r.choice("23456789") + digits(r, 10)
    n = base + verhoeff_check_digit(base)
    return r.choice([f"{n[:4]} {n[4:8]} {n[8:]}", n, f"{n[:4]}-{n[4:8]}-{n[8:]}"])


def gstin(r: random.Random, pan: str) -> str:
    first14 = f"{r.randint(1, 37):02d}{pan}{r.choice('123456789')}Z"
    return first14 + gstin_check_char(first14)


def card(r: random.Random) -> str:
    n = (r.choice(["4", "5" + r.choice("12345"), "60", "65", "81"]) + digits(r, 14))[:15]
    n += next(c for c in "0123456789" if luhn_valid(n + c))
    return r.choice([" ".join(n[i:i + 4] for i in range(0, 16, 4)), n, "-".join(n[i:i + 4] for i in range(0, 16, 4))])


def bank_acct(r: random.Random) -> str:
    return r.choice("123456789") + digits(r, r.randint(8, 17))


def ifsc(r: random.Random) -> str:
    return f"{r.choice(BANK_CODES)}0{digits(r, 6)}"


def passport(r: random.Random) -> str:
    return r.choice("ABCDEFGHJKLMNPRSTUVWY") + r.choice("123456789") + digits(r, 6)


def voter_id(r: random.Random) -> str:
    return "".join(r.choice("ABCDEFGHJKLMNPRSTUVWXYZ") for _ in range(3)) + digits(r, 7)


def vehicle(r: random.Random) -> str:
    s, d = r.choice(STATE_VEH), f"{r.randint(1, 60):02d}"
    l = "".join(r.choice("ABCDEFGHJKLMNPRSTUVWXYZ") for _ in range(r.choice([1, 2, 2])))
    n = digits(r, 4)
    return r.choice([f"{s} {d} {l} {n}", f"{s}{d}{l}{n}", f"{s}-{d}-{l}-{n}"])


def dob(r: random.Random) -> str:
    d, m, y = r.randint(1, 28), r.randint(1, 12), r.randint(1955, 2006)
    return r.choice([f"{d:02d}/{m:02d}/{y}", f"{d:02d}-{m:02d}-{y}", f"{d} {MONTHS_LONG[m - 1]} {y}",
                     f"{d}{'th' if d > 3 else ['st', 'nd', 'rd'][d - 1]} {MONTHS[m - 1]} {y}"])


def ip(r: random.Random) -> str:
    return f"{r.choice([49, 103, 106, 117, 122, 157, 182, 203])}.{r.randint(0, 255)}.{r.randint(0, 255)}.{r.randint(1, 254)}"


# ---------- hard negatives: look like PII, aren't ----------

def order_id(r):
    return r.choice([f"OD{digits(r, 18)}", f"FK-{digits(r, 6)}", f"#ORD-{digits(r, 5)}",
                     f"{digits(r, 3)}-{digits(r, 7)}-{digits(r, 7)}", f"ORD{digits(r, 9)}"])


def awb(r):
    return r.choice([digits(r, 12), f"FMPC{digits(r, 10)}", f"SF{digits(r, 11)}FPL", digits(r, 13)])


def sku(r):
    return r.choice([f"SKU-{r.choice(['BLR', 'MUM', 'DEL'])}-{digits(r, 5)}",
                     f"{r.choice(['AMUL', 'TATA', 'BOAT', 'MILTON'])}-{r.choice(['1L', '500G', '141', 'BLK'])}-{digits(r, 3)}"])


def invoice_no(r):
    return r.choice([f"INV/2026-27/{digits(r, 5)}", f"GST/{digits(r, 4)}/26", f"TI-{digits(r, 6)}"])


def amount(r):
    v = r.randint(49, 48000)
    return r.choice([f"₹{v:,}", f"Rs. {v}", f"INR {v:,}.00", f"Rs {v}/-"])


def pincode(r):
    prefix, _ = CITIES[r.choice(list(CITIES))]
    return prefix + digits(r, 3)


def helpline(r):
    return r.choice(["1800 102 7777", "1800-419-0505", "1800 208 9898", "1800-123-4455"])


def date(r):
    d, m = r.randint(1, 28), r.randint(1, 12)
    return r.choice([f"{d:02d}/{m:02d}/2026", f"{d} {MONTHS[m - 1]} 2026", f"2026-{m:02d}-{d:02d}"])


def ref_no(r):
    return r.choice([f"UTR {digits(r, 12)}", f"REF-{digits(r, 5)}", f"TKT#{digits(r, 6)}", f"TXN2026{digits(r, 10)}"])


# ---------- M3 additions: messy real-world forms (from M2 gap analysis) ----------

UNKNOWN_UPI = ["superyes", "mbk", "waicici", "pingpay", "kbl", "cnrb", "aubank", "rbl", "idfcbank", "jio"]
SHOPS = ["Raju tea stall", "Sri Sai bakery", "Apollo pharmacy", "More supermarket", "Iyengar bakery",
         "Ganesh kirana", "SBI ATM", "Indian Oil pump", "Sagar hotel", "Reliance Trends", "post office"]
COLORS = ["blue", "green", "yellow", "white", "brown", "red", "pink"]
SHRINES = ["shiv mandir", "Hanuman mandir", "masjid", "church", "gurudwara", "Ayyappa temple",
           "Sai Baba mandir", "Durga mandir"]
ORDINALS = ["1st", "2nd", "3rd", "4th", "5th", "last", "corner"]
ROLES = ["Ops Manager", "Store Manager", "Accounts", "Procurement Head", "Hub Incharge", "Proprietor"]
COMPANY_SLUGS = ["shopkart", "quickbasket", "dailydrop", "fastkart", "zipmart", "kiranakart"]
INBOX_USERS = ["support", "customercare", "care", "help", "orders", "noreply", "billing"]
FOREIGN = ["+971 5{a} {b} {c}", "+1 415 {b} {c}", "+44 7{a}{a} {c}{a}", "+65 9{b} {c}", "+966 5{a} {b} {c}"]
LANDLINE = ["080-{b}{a} {c}", "011 {c} {c}", "044-{b}{a} {c}", "022 {b}{a} {c}", "(080) {c}{c}", "040-{c}{c}"]


def phone_messy(r: random.Random, mobile: str) -> str:
    """Disguised mobile: letter O for zero, odd grouping, dots."""
    k = r.random()
    if k < 0.4 and "0" in mobile:
        i = mobile.index("0") if r.random() < 0.5 else mobile.rindex("0")
        m = mobile[:i] + "O" + mobile[i + 1:]
        return r.choice([m, f"{m[:5]} {m[5:]}"])
    if k < 0.7:
        return f"{mobile[:3]}.{mobile[3:6]}.{mobile[6:]}"
    return f"{mobile[:2]} {mobile[2:4]} {mobile[4:6]} {mobile[6:8]} {mobile[8:]}"


def landline(r: random.Random) -> str:
    return r.choice(LANDLINE).format(a=digits(r, 1), b=r.choice("23456") + digits(r, 2), c=digits(r, 4))


def foreign_phone(r: random.Random) -> str:
    return r.choice(FOREIGN).format(a=digits(r, 1), b=digits(r, 3), c=digits(r, 4))


def email_obfuscated(r: random.Random, first: str, last: str) -> str:
    f, l, d = first.lower(), last.lower(), r.choice(["gmail", "yahoo", "outlook", "rediffmail"])
    return r.choice([f"{f} dot {l} at {d} dot com", f"{f}.{l}[at]{d}.com", f"{f}{l[0]} at {d} dot com",
                     f"{f}.{l} (at) {d}.com"])


def pan_spaced(pan: str, r: random.Random) -> str:
    return r.choice([f"{pan[:5]} {pan[5:9]} {pan[9]}", f"{pan[:5]}-{pan[5:9]}-{pan[9]}", f"{pan[:3]} {pan[3:]}"])


def upi_unknown(r: random.Random, first: str) -> str:
    return f"{first.lower()}{r.choice(['', digits(r, 2), '.' + digits(r, 3)])}@{r.choice(UNKNOWN_UPI)}"


def address_informal(r: random.Random) -> str:
    city = r.choice(list(CITIES))
    prefix, localities = CITIES[city]
    loc, n = r.choice(localities), r.randint(1, 15)
    shop, shrine = r.choice(SHOPS), r.choice(SHRINES)
    forms = [
        f"{r.choice(ORDINALS)} house after {shop}, {r.choice(COLORS)} gate, {loc}",
        f"gali no {n}, {shrine} ke peeche, {loc}",
        f"{shrine} ke saamne wali building, {r.choice(ORDINALS)} floor, {loc}",
        f"behind {shop}, {n}th street, {loc} {prefix}{digits(r, 3)}",
        f"opp {shop}, {r.choice(COLORS)} building {r.choice(ORDINALS)} floor, {loc}",
        f"{n}ne cross, {shrine} hatra, {loc}",
        f"{shrine} pakkam, {n}th street, {loc}, {city}",
        f"house with {r.choice(COLORS)} gate near {shop}, {loc}",
    ]
    return r.choice(forms)


def driving_licence(r: random.Random) -> str:
    s, rto, y, n = r.choice(STATE_VEH), f"{r.randint(1, 60):02d}", str(r.randint(1995, 2025)), digits(r, 7)
    return r.choice([f"{s}{rto}{y}{n}", f"{s}{rto} {y}{n}", f"{s}-{rto}-{y}-{n}", f"{s}{rto} {y} {n}"])


def locality(r: random.Random) -> str:
    return r.choice(CITIES[r.choice(list(CITIES))][1])


def masked_id(r: random.Random) -> str:
    return r.choice([f"XXXX XXXX {digits(r, 4)}", f"xxxxxxxx{digits(r, 4)}", f"******{digits(r, 4)}",
                     f"{r.choice('6789')}{digits(r, 1)}XXXXXX{digits(r, 2)}", f"XXXXX{digits(r, 4)}X"])


def company_inbox(r: random.Random) -> str:
    return f"{r.choice(INBOX_USERS)}@{r.choice(COMPANY_SLUGS)}.{r.choice(['in', 'com', 'co.in'])}"


ORGS += ["Meena Bazaar", "Arun Ice Creams", "Sri Krishna Sweets", "Lakshmi Jewellers", "Shanti Sagar Hotel",
         "Kamath Hotel", "Iyer Mess", "Sharma Dhaba", "Reddy Brothers Agencies", "Nair Tea House"]
FESTIVALS += ["Ram Navami", "Janmashtami", "Ugadi", "Bakrid", "Guru Nanak Jayanti", "Karthigai Deepam"]
