#!/usr/bin/env python3
"""Generate the synthetic supporter dataset for Analytics Sessions 3 & 4.

FACILITATOR ONLY — this script does not ship to attendees, the CSVs it writes do.

Everything here is fictional. No real supporter, donor or patient data is used,
and none of the generated values correspond to a real person (ADR 0001).

The defects are deliberate and are the teaching material. Every one of them is
counted and written to facilitator/defect-manifest.md so the answer keys can
state exact numbers. Fixed seed => regenerating gives byte-identical files.

Run:  uv run facilitator/generate_data.py
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 130
REF_DATE = date(2026, 8, 17)  # Session 3
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

rnd = random.Random(SEED)
manifest: dict[str, int] = {}


def note(key: str, n: int = 1) -> None:
    manifest[key] = manifest.get(key, 0) + n


FIRST = """Aisha Amara Ben Callum Chloe Daniel Deborah Eleanor Elliot Emeka Fatima
Freya Gareth Grace Hannah Harun Imogen Isaac Jasmin Joseph Kai Karolina Leah Liam
Lucy Mahmoud Maya Niamh Noah Olive Omar Priya Rachel Rhys Rosa Samuel Sian Sofia
Tariq Theo Uche Verity Wei Yusuf Zainab Zara""".split()

LAST = """Abiola Ahmed Baptiste Bright Carrick Chen Dalgleish Duffy Ellery Fenton
Gill Grewal Hargreaves Iqbal Jarvis Kowalski Lindqvist Mensah Morrow Nkemelu
Okafor Pemberton Quainton Rashid Sandoval Sharpe Tewari Thornbury Uddin Vasquez
Wainwright Whitlock Yeboah Zielinski""".split()

REGIONS = ["London", "South East", "South West", "East of England", "West Midlands",
           "East Midlands", "Yorkshire & Humber", "North West", "North East",
           "Scotland", "Wales", "Northern Ireland"]

POSTCODE_AREAS = ["M", "B", "LS", "NE", "BS", "CF", "EH", "G", "L", "SW", "N", "SE", "BT"]

CHANNELS = ["Web", "Direct Mail", "Event", "Telephone", "Partner", "Social"]

# --------------------------------------------------------------------------
# supporters.csv
# --------------------------------------------------------------------------

N_SUPPORTERS = 4000
supporters = []
seen_people = []

# Tenure differs by acquisition channel, deliberately. Events were the big
# acquisition push years ago; Direct Mail is where the recent supporters came
# from. This is what makes the Session 4 hypothesis reverse when you control for
# time on the database: Event supporters have given more in total simply
# because they have been here longer, while Direct Mail supporters give more
# per year. Neither fact is visible without asking the second question.
TENURE_DAYS = {
    "Event":       (1500, 3600),
    "Partner":     (1000, 3400),
    "Telephone":   (600, 3000),
    "Web":         (200, 2200),
    "Social":      (120, 1600),
    "Direct Mail": (60, 1200),
}
# Annual giving rate by channel — the inverse ordering.
GIVING_RATE = {
    "Direct Mail": 1.55, "Web": 1.25, "Social": 1.15,
    "Telephone": 1.00, "Partner": 0.85, "Event": 0.70,
}

for i in range(1, N_SUPPORTERS + 1):
    first = rnd.choice(FIRST)
    last = rnd.choice(LAST)
    dob = date(rnd.randint(1946, 2006), rnd.randint(1, 12), rnd.randint(1, 28))
    channel = rnd.choice(CHANNELS)
    lo, hi = TENURE_DAYS[channel]
    signup = REF_DATE - timedelta(days=rnd.randint(lo, hi))
    last_act = signup + timedelta(days=rnd.randint(0, (REF_DATE - signup).days))
    status = rnd.choices(
        ["Active", "Lapsed", "Inactive", "Deceased"], weights=[62, 22, 14, 2]
    )[0]
    area = rnd.choice(POSTCODE_AREAS)
    postcode = f"{area}{rnd.randint(1, 40)} {rnd.randint(1, 9)}{rnd.choice('ABDEFGHJLNPQRSTUWXYZ')}{rnd.choice('ABDEFGHJLNPQRSTUWXYZ')}"
    supporters.append({
        "supporter_id": i,
        "first_name": first,
        "last_name": last,
        "date_of_birth": dob.isoformat(),
        "email": f"{first.lower()}.{last.lower()}{i}@example.com",
        "postcode": postcode,
        "region": rnd.choice(REGIONS),
        "sign_up_date": signup.isoformat(),
        "source_channel": channel,
        "marketing_consent": rnd.choice([0, 1]),
        "status": status,
        "last_activity_date": last_act.isoformat(),
    })
    seen_people.append((first, last, dob.isoformat()))

# --- defect: the 'Activ' typo (status vocabulary) -------------------------
typo_rows = rnd.sample([s for s in supporters if s["status"] == "Active"], 18)
for s in typo_rows:
    s["status"] = "Activ"
note("supporters.status = 'Activ' (typo, should be Active)", 18)

# --- defect: blank emails --------------------------------------------------
for s in rnd.sample(supporters, 124):
    s["email"] = ""
note("supporters.email blank", 124)

# --- defect: malformed emails (no @) --------------------------------------
for s in rnd.sample([s for s in supporters if s["email"]], 31):
    s["email"] = s["email"].replace("@", ".")
note("supporters.email malformed (no @)", 31)

# --- defect: blank region --------------------------------------------------
for s in rnd.sample(supporters, 40):
    s["region"] = ""
note("supporters.region blank", 40)

# --- defect: marketing_consent stored as Y/N text in some rows ------------
for s in rnd.sample(supporters, 15):
    s["marketing_consent"] = "Y" if rnd.random() < 0.5 else "N"
note("supporters.marketing_consent as 'Y'/'N' text instead of 1/0", 15)

# --- defect: future sign_up_date ------------------------------------------
for s in rnd.sample(supporters, 9):
    s["sign_up_date"] = (REF_DATE + timedelta(days=rnd.randint(5, 200))).isoformat()
note("supporters.sign_up_date in the future", 9)

# --- defect: last_activity_date before sign_up_date -----------------------
for s in rnd.sample(supporters, 14):
    s["last_activity_date"] = (
        date.fromisoformat(s["sign_up_date"]) - timedelta(days=rnd.randint(10, 400))
    ).isoformat()
note("supporters.last_activity_date before sign_up_date", 14)

# --- defect: duplicate people (same name + dob, new supporter_id) ---------
next_id = N_SUPPORTERS + 1
dupes = rnd.sample(supporters, 22)
for s in dupes:
    clone = dict(s)
    clone["supporter_id"] = next_id
    clone["email"] = ""
    clone["sign_up_date"] = (
        date.fromisoformat(s["sign_up_date"]) + timedelta(days=rnd.randint(1, 900))
    ).isoformat()
    clone["source_channel"] = rnd.choice(CHANNELS)
    supporters.append(clone)
    next_id += 1
note("supporters: same person twice (same name + DOB, different supporter_id)", 22)

# --- noise (NOT a defect): inconsistent postcode formatting ---------------
for s in rnd.sample(supporters, 300):
    s["postcode"] = s["postcode"].lower().replace(" ", "")
note("[NOISE] supporters.postcode lowercase / unspaced — realistic, not a defect", 300)

TOTAL_SUPPORTERS = len(supporters)

# --------------------------------------------------------------------------
# campaigns.csv — the messy free-text category problem (Lauren's shape)
# --------------------------------------------------------------------------

CAMPAIGN_THEMES = {
    "Christmas appeal": ["Xmas Appeal", "Christmas appeal", "XMAS-APPEAL", "christmas",
                         "Christmas Appeal 2024", "Xmas", "Chirstmas appeal"],
    "Spring appeal": ["Spring Appeal", "spring appeal", "SPRING", "Spring Campaign",
                      "spring-appeal"],
    "Donor recruitment": ["Donor Recruitment", "donor recruit", "RECRUITMENT",
                          "Recruitment - donors", "New donor drive", "donor-recruitment"],
    "Regular giving": ["Regular Giving", "regular giving", "RG", "Monthly giving",
                       "Reg. Giving", "monthly-givers"],
    "Legacy": ["Legacy", "legacy giving", "LEGACY", "Gifts in Wills", "wills"],
    "Events": ["Events", "event", "EVENTS", "Challenge Events", "challenge-events",
               "Marathon"],
    "Corporate": ["Corporate", "corporate partnership", "CORP", "Partnerships"],
    "Newsletter": ["Newsletter", "newsletter", "NEWS", "Supporter newsletter", "e-news"],
}

campaigns = []
code_n = 1
for theme, variants in CAMPAIGN_THEMES.items():
    for _ in range(rnd.randint(20, 26)):
        start = REF_DATE - timedelta(days=rnd.randint(30, 1400))
        campaigns.append({
            "campaign_code": f"CMP{code_n:04d}",
            "campaign_name": f"{rnd.choice(variants)} {start.year} {rnd.choice(['', 'wave 2', 'North', 'test', 'v2', ''])}".strip(),
            "category_raw": rnd.choice(variants),
            "channel": rnd.choice(["Email", "Direct Mail", "SMS", "Social", "Phone"]),
            "start_date": start.isoformat(),
            "end_date": (start + timedelta(days=rnd.randint(7, 90))).isoformat(),
            "owner_team": rnd.choice(["Fundraising", "Marketing", "Supporter Care",
                                      "Register Growth"]),
            "_true_category": theme,
        })
        code_n += 1

rnd.shuffle(campaigns)
note("campaigns: distinct free-text spellings of "
     f"{len(CAMPAIGN_THEMES)} real categories",
     sum(len(v) for v in CAMPAIGN_THEMES.values()))

# --- defect: blank category_raw -------------------------------------------
for c in rnd.sample(campaigns, 12):
    c["category_raw"] = ""
note("campaigns.category_raw blank", 12)

# --- defect: end_date before start_date -----------------------------------
for c in rnd.sample(campaigns, 6):
    c["end_date"] = (date.fromisoformat(c["start_date"]) - timedelta(days=rnd.randint(1, 20))).isoformat()
note("campaigns.end_date before start_date", 6)

# --------------------------------------------------------------------------
# donations.csv
# --------------------------------------------------------------------------

donations = []
active_ids = [s["supporter_id"] for s in supporters]
PAYMENTS = ["Direct Debit", "Card", "Cash", "Cheque", "Standing Order", "Online"]
d_id = 1
for s in supporters:
    signup = date.fromisoformat(s["sign_up_date"])
    years = max((REF_DATE - signup).days / 365.25, 0.4)
    rate = GIVING_RATE[s["source_channel"]]
    # gifts accumulate with tenure, at a per-year rate that depends on channel
    expected = years * rate
    n = max(0, int(rnd.gauss(expected, expected * 0.55)))
    if rnd.random() < 0.16:
        n = 0  # never gave
    for _ in range(n):
        span = max((REF_DATE - signup).days, 1)
        ddate = signup + timedelta(days=rnd.randint(0, span))
        donations.append({
            "donation_id": d_id,
            "supporter_id": s["supporter_id"],
            "donation_date": ddate.isoformat(),
            "amount_gbp": round(rnd.choice([5, 10, 15, 20, 25, 50, 100, 250]) *
                                rnd.choice([1, 1, 1, 1.5, 2]), 2),
            "campaign_code": rnd.choice(campaigns)["campaign_code"],
            "payment_method": rnd.choice(PAYMENTS),
            "gift_aid": rnd.choice([0, 1]),
            "refunded": 0,
        })
        d_id += 1

# --- realistic: some donations refunded ------------------------------------
for d in rnd.sample(donations, 213):
    d["refunded"] = 1
note("[BY DESIGN] donations.refunded = 1 — valid data, but the two reports "
     "disagree about whether to include it", 213)

# --- defect: orphan supporter_id ------------------------------------------
for d in rnd.sample(donations, 30):
    d["supporter_id"] = rnd.randint(90000, 99999)
note("donations.supporter_id with no matching supporter (orphan)", 30)

# --- defect: negative and zero amounts ------------------------------------
for d in rnd.sample(donations, 12):
    d["amount_gbp"] = -abs(d["amount_gbp"])
note("donations.amount_gbp negative", 12)
for d in rnd.sample(donations, 8):
    d["amount_gbp"] = 0
note("donations.amount_gbp zero", 8)

# --- defect: duplicate donation rows --------------------------------------
for d in rnd.sample(donations, 44):
    clone = dict(d)
    clone["donation_id"] = d_id
    d_id += 1
    donations.append(clone)
note("donations: same donation entered twice (identical supporter/date/amount, "
     "different donation_id)", 44)

# --- defect: campaign_code that is not in campaigns.csv -------------------
for d in rnd.sample(donations, 17):
    d["campaign_code"] = f"CMP{rnd.randint(9000, 9999)}"
note("donations.campaign_code with no matching campaign", 17)

# --- defect: donation_date before the supporter signed up -----------------
by_id = {s["supporter_id"]: s for s in supporters}
moved = 0
for d in rnd.sample(donations, 60):
    s = by_id.get(d["supporter_id"])
    if not s:
        continue
    d["donation_date"] = (
        date.fromisoformat(s["sign_up_date"]) - timedelta(days=rnd.randint(5, 300))
    ).isoformat()
    moved += 1
note("donations.donation_date before the supporter's sign_up_date", moved)

rnd.shuffle(donations)

# --------------------------------------------------------------------------
# campaign_activity.csv — email sends (the DotDigital shape)
# --------------------------------------------------------------------------

activity = []
a_id = 1
consented = [s for s in supporters if s["marketing_consent"] in (1, "Y")]
email_campaigns = [c for c in campaigns if c["channel"] == "Email"]
for c in email_campaigns:
    audience = rnd.sample(consented, rnd.randint(200, 900))
    for s in audience:
        opened = 1 if rnd.random() < 0.31 else 0
        clicked = 1 if opened and rnd.random() < 0.18 else 0
        activity.append({
            "activity_id": a_id,
            "campaign_code": c["campaign_code"],
            "supporter_id": s["supporter_id"],
            "sent_date": c["start_date"],
            "opened": opened,
            "clicked": clicked,
            "unsubscribed": 1 if rnd.random() < 0.004 else 0,
        })
        a_id += 1

# --- defect: clicked = 1 while opened = 0 ---------------------------------
for a in rnd.sample([a for a in activity if a["opened"] == 0], 77):
    a["clicked"] = 1
note("campaign_activity: clicked = 1 while opened = 0 (impossible)", 77)

# --------------------------------------------------------------------------
# fulfilment_tasks.csv — the operational / throughput shape (Lucie's team)
# --------------------------------------------------------------------------

TASK_TYPES = ["Welcome pack", "Swab kit dispatch", "Consent follow-up",
              "Address change", "Gift Aid declaration", "Complaint",
              "Data request", "Thank-you letter"]
TEAMS = ["Supporter Care", "Register Operations", "Fundraising Ops"]
AGENTS = [f"agent_{i:02d}" for i in range(1, 27)]

# Three deliberate structures, none of them visible without the right question:
#   1. Complaints really are slower than everything else.
#   2. Resolution time really has been getting worse over the last two quarters.
#   3. Recent tasks are far more likely to still be open — so the naive average
#      over *completed* tasks makes the recent months look BETTER than they are,
#      because the slow recent cases have not finished yet and leave the sample.
# (2) and (3) point in opposite directions. Whichever an analyst finds first
# depends entirely on whether they thought about the missing rows.
BASE_DAYS = {
    "Complaint": 31, "Data request": 24, "Consent follow-up": 18,
    "Gift Aid declaration": 16, "Address change": 12, "Welcome pack": 11,
    "Swab kit dispatch": 9, "Thank-you letter": 8,
}

tasks = []
for i in range(1, 6001):
    age_days = rnd.randint(1, 540)
    created = REF_DATE - timedelta(days=age_days)
    ttype = rnd.choice(TASK_TYPES)
    due = created + timedelta(days=rnd.choice([2, 5, 10, 20]))

    # the real slowdown: +55% on anything created in the last ~5 months
    drift = 1.0 + (0.55 * max(0.0, (150 - age_days) / 150.0))
    target = BASE_DAYS[ttype] * drift
    duration = max(0, int(rnd.gauss(target, target * 0.5)))

    # a task is only finished if enough time has passed — this is what makes
    # recent, slow work disappear from any average taken over completed rows
    done = duration <= age_days and rnd.random() < 0.94
    completed = created + timedelta(days=duration) if done else None
    tasks.append({
        "task_id": i,
        "task_type": ttype,
        "assigned_team": rnd.choice(TEAMS),
        "assigned_to": rnd.choice(AGENTS),
        "created_date": created.isoformat(),
        "due_date": due.isoformat(),
        "completed_date": completed.isoformat() if completed else "",
        "status": "Completed" if done else rnd.choice(["Open", "In Progress", "Blocked"]),
        "priority": rnd.choices(["Low", "Normal", "High", "Urgent"],
                                weights=[20, 55, 20, 5])[0],
    })

# --- defect: two spellings of the same status -----------------------------
for t in rnd.sample([t for t in tasks if t["status"] == "Completed"], 190):
    t["status"] = "Complete"
note("fulfilment_tasks.status: 'Complete' and 'Completed' both used for the "
     "same state", 190)

# --- defect: completed_date before created_date ---------------------------
for t in rnd.sample([t for t in tasks if t["completed_date"]], 11):
    t["completed_date"] = (
        date.fromisoformat(t["created_date"]) - timedelta(days=rnd.randint(1, 30))
    ).isoformat()
note("fulfilment_tasks.completed_date before created_date", 11)

# --- defect: status says done but completed_date is blank -----------------
for t in rnd.sample([t for t in tasks if t["status"] in ("Complete", "Completed")], 46):
    t["completed_date"] = ""
note("fulfilment_tasks: status Complete(d) but completed_date blank", 46)

# --- defect: assigned_to blank --------------------------------------------
for t in rnd.sample(tasks, 58):
    t["assigned_to"] = ""
note("fulfilment_tasks.assigned_to blank", 58)

# --------------------------------------------------------------------------
# write
# --------------------------------------------------------------------------


def write(name: str, rows: list[dict], drop: tuple[str, ...] = ()) -> None:
    rows = [{k: v for k, v in r.items() if k not in drop} for r in rows]
    path = DATA / name
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"{path.relative_to(ROOT)}: {len(rows)} rows")


DATA.mkdir(exist_ok=True)
write("supporters.csv", supporters)
write("campaigns.csv", campaigns, drop=("_true_category",))
write("donations.csv", donations)
write("campaign_activity.csv", activity)
write("fulfilment_tasks.csv", tasks)

# the answer key for the classification exercise — facilitator only
with (ROOT / "facilitator" / "campaign-category-key.csv").open(
        "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["campaign_code", "category_raw", "true_category"])
    for c in campaigns:
        w.writerow([c["campaign_code"], c["category_raw"], c["_true_category"]])

# --------------------------------------------------------------------------
# the two competing "Active supporters" numbers — the Session 3 spine
# --------------------------------------------------------------------------

cutoff = REF_DATE - timedelta(days=365)

a_status = sum(1 for s in supporters if s["status"] == "Active")
a_status_incl_typo = sum(1 for s in supporters if s["status"] in ("Active", "Activ"))

donors_12m = {d["supporter_id"] for d in donations
              if d["donation_date"] >= cutoff.isoformat() and d["refunded"] == 0}
a_donated = len([s for s in supporters if s["supporter_id"] in donors_12m])

a_activity = sum(1 for s in supporters if s["last_activity_date"] >= cutoff.isoformat())

income_all = sum(d["amount_gbp"] for d in donations)
income_net = sum(d["amount_gbp"] for d in donations if d["refunded"] == 0)
income_net_positive = sum(d["amount_gbp"] for d in donations
                          if d["refunded"] == 0 and d["amount_gbp"] > 0)

lines = [
    "# Defect manifest — FACILITATOR ONLY",
    "",
    f"Generated by `facilitator/generate_data.py`, seed {SEED}, reference date "
    f"{REF_DATE.isoformat()}. Regenerating reproduces these files exactly.",
    "",
    "## Row counts",
    "",
    "| File | Rows |",
    "|---|---|",
    f"| supporters.csv | {TOTAL_SUPPORTERS} |",
    f"| campaigns.csv | {len(campaigns)} |",
    f"| donations.csv | {len(donations)} |",
    f"| campaign_activity.csv | {len(activity)} |",
    f"| fulfilment_tasks.csv | {len(tasks)} |",
    "",
    "## The four answers to \"how many active supporters?\"",
    "",
    "This is the spine of Session 3. Every one of these is defensible, and they",
    "all disagree. Nobody in the room can tell which is right without agreeing a",
    "definition first — which is the point.",
    "",
    "| Definition | Number |",
    "|---|---|",
    f"| `status = 'Active'` (what Fundraising Summary does) | **{a_status}** |",
    f"| `status IN ('Active','Activ')` — same, once you notice the typo | **{a_status_incl_typo}** |",
    f"| donated in the last 12 months, refunds excluded (what Supporter Engagement does) | **{a_donated}** |",
    f"| any activity in the last 12 months | **{a_activity}** |",
    "",
    f"The typo alone moves the headline number by {a_status_incl_typo - a_status}.",
    "",
    "## The three answers to \"what was our income?\"",
    "",
    "| Definition | Amount |",
    "|---|---|",
    f"| every row in donations.csv | £{income_all:,.2f} |",
    f"| refunds excluded | £{income_net:,.2f} |",
    f"| refunds excluded and negatives/zeroes excluded | £{income_net_positive:,.2f} |",
    "",
    "## Deliberate defects",
    "",
    "| Defect | Count |",
    "|---|---|",
]
for k in sorted(manifest):
    lines.append(f"| {k} | {manifest[k]} |")
lines += [
    "",
    "## Things that look wrong and are not",
    "",
    "Rejecting these is half the data-quality exercise. A rule that fires on",
    "healthy data trains everyone to ignore the alerts.",
    "",
    "- **Postcode formatting** — 300 rows are lowercase and unspaced. Realistic",
    "  messiness, not a defect. Normalise on read; do not raise an alert.",
    "- **`refunded = 1`** — 213 real refunds. Valid data. The *disagreement*",
    "  about whether to count them is the lesson, not the rows themselves.",
    "- **`marketing_consent = 0`** — a lawful choice, not a quality failure.",
    "- **Supporters with zero donations** — ~29% by design. Normal.",
    "- **`status = 'Deceased'`** — real and correct; ~2%.",
    "",
]
(ROOT / "facilitator" / "defect-manifest.md").write_text("\n".join(lines), encoding="utf-8")
print("facilitator/defect-manifest.md written")
