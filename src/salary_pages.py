"""Programmatic pay-conversion pages.

Targets the long-tail queries the single salary calculator cannot rank for:
    "$65,000 a year is how much an hour"
    "$30 an hour is how much a year"

These are arithmetic, not financial advice, so they carry almost no
"Your Money or Your Life" trust weight - which is exactly why they are the
right pages for this site to compete on.

Every figure below is computed, so no two pages share their numbers.
All amounts are GROSS pay, before tax and deductions.
"""

FULL_WEEK = 40.0
WEEKS = 52.0
FULL_YEAR_HOURS = FULL_WEEK * WEEKS          # 2,080
WORK_DAY = 8.0

# schedules shown in the "other hours" table on every page
VARIANTS = [
    (35.0, 52.0, "35 hours a week"),
    (37.5, 52.0, "37.5 hours a week"),
    (40.0, 50.0, "40 hours, 2 weeks unpaid"),
    (45.0, 52.0, "45 hours a week"),
]

# Deliberately a small first batch. The site has 20 real pages; flooding it with
# 127 generated ones would make it mostly machine-written, which is a site-level
# quality risk. Ship these, measure how many Google indexes, then decide.
# Mix of round numbers (high volume, hard) and odd ones (lower volume, winnable).
SALARIES = [35000, 40000, 45000, 47000, 50000, 52000, 55000, 58000,
            60000, 63000, 65000, 70000, 75000, 80000, 90000]

HOURLY = [15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 22.0, 24.0,
          25.0, 27.0, 30.0, 32.0, 35.0, 40.0, 45.0]


def money(x, cents=True):
    if cents:
        return f"${x:,.2f}"
    return f"${x:,.0f}"


def from_salary(annual, hours=FULL_WEEK, weeks=WEEKS):
    """Every derived figure for a yearly salary."""
    yearly_hours = hours * weeks
    hourly = annual / yearly_hours
    weekly = annual / weeks
    return {
        "annual": annual,
        "hourly": hourly,
        "daily": hourly * WORK_DAY,
        "weekly": weekly,
        "biweekly": weekly * 2,
        "semimonthly": annual / 24,
        "monthly": annual / 12,
        "hours_per_week": hours,
        "weeks": weeks,
        "yearly_hours": yearly_hours,
    }


def from_hourly(rate, hours=FULL_WEEK, weeks=WEEKS):
    return from_salary(rate * hours * weeks, hours, weeks)


def salary_slug(annual):
    return f"{annual}-a-year-is-how-much-an-hour"


def hourly_slug(rate):
    tag = f"{rate:.2f}".rstrip("0").rstrip(".").replace(".", "-")
    return f"{tag}-an-hour-is-how-much-a-year"


def salary_label(annual):
    return money(annual, cents=False)


def hourly_label(rate):
    return money(rate) if rate % 1 else money(rate, cents=False)


def nearest(values, x):
    """Closest value that actually has a page, so cross-links never 404."""
    return min(values, key=lambda v: abs(v - x))


def neighbours(values, i, n=2):
    """Previous/next values for internal linking."""
    lo = max(0, i - n)
    return [v for v in values[lo:i] + values[i + 1:i + 1 + n]]


if __name__ == "__main__":
    print(f"{len(SALARIES)} salary pages + {len(HOURLY)} hourly pages "
          f"= {len(SALARIES) + len(HOURLY)} total")
    d = from_salary(65000)
    print("\n$65,000/yr at 40h x 52w:")
    for k in ("hourly", "daily", "weekly", "biweekly", "semimonthly", "monthly"):
        print(f"   {k:12s} {money(d[k])}")
    print("\nvariants:")
    for h, w, lbl in VARIANTS:
        print(f"   {lbl:28s} {money(from_salary(65000, h, w)['hourly'])}/hour")
    print("\nslugs:", salary_slug(65000), "|", hourly_slug(31.25), "|", hourly_slug(30))
