"""Static site generator for CalcMyFin.

    python src/build.py        # canonical URLs -> https://calcmyfin.com, writes CNAME for GitHub Pages

Writes pages into the repo root (GitHub Pages serves it as-is).
"""
import html
import json
import math
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import CALCULATORS, CATEGORIES, HOME_FAQS, POPULAR, SITE  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
BY_SLUG = {c["slug"]: c for c in CALCULATORS}
CAT = {k: (name, blurb) for k, name, blurb in CATEGORIES}
ASSET_V = SITE["updated"].replace("-", "")  # cache-busting query string

# ---------------------------------------------------------------- icons
ICON_PATHS = {
    "home": '<path d="M3 11.5 12 4l9 7.5"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
    "debt": '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M3 10h18"/><path d="M7 15h4"/>',
    "grow": '<path d="M4 19V5"/><path d="M4 19h16"/><path d="m7 15 4-4 3 3 5-6"/>',
    "plan": '<path d="M12 3a9 9 0 1 0 9 9h-9z"/><path d="M14 3.3A9 9 0 0 1 20.7 10H14z"/>',
    "protect": '<path d="M12 3 5 6v6c0 4.2 3 7.8 7 9 4-1.2 7-4.8 7-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
    "share": '<path d="M4 12v7a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-7"/><path d="m16 6-4-4-4 4"/><path d="M12 2v14"/>',
    "print": '<path d="M6 9V3h12v6"/><rect x="3" y="9" width="18" height="8" rx="2"/><path d="M7 14h10v7H7z"/>',
    "reset": '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/>',
    "check": '<path d="m5 12 5 5 9-10"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
}


def icon(name, cls="icon"):
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON_PATHS[name]}</svg>')


LOGO = ('<svg class="logo-mark" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" rx="9" fill="#0f5c4d"/>'
        '<path d="M9 21.5 14 16l3.5 3.5L23 12" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" '
        'stroke-linejoin="round"/><circle cx="23" cy="12" r="2.3" fill="#f2b441"/></svg>')

esc = html.escape


# ---------------------------------------------------------------- url helpers
def page_url(path):
    """Absolute canonical URL for a site path like '' or 'mortgage-calculator/'."""
    return f"{SITE['base_url']}/{path}"


class Page:
    def __init__(self, path, depth):
        self.path, self.depth = path, depth

    def rel(self, target):
        """Relative link from this page to a site path ('' = home, 'x/' = folder)."""
        prefix = "../" * self.depth
        return (prefix + target) or "./"

    def asset(self, target):
        return self.rel(target) + (f"?v={ASSET_V}" if target.endswith((".css", ".js")) else "")


def link_tokens(text, pg):
    """Replace {slug} tokens in copy with relative links."""
    return re.sub(r"\{([a-z0-9-]+)\}", lambda m: pg.rel(m.group(1) + "/"), text)


# ---------------------------------------------------------------- layout pieces
def head(pg, title, description, og_image, jsonld, extra="", robots="index,follow"):
    canonical = page_url(pg.path)
    full_title = title if title.endswith(SITE["name"]) else f"{title} | {SITE['name']}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">
<meta name="robots" content="{robots},max-image-preview:large">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0f5c4d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['name']}">
<meta property="og:locale" content="{SITE['locale']}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{page_url(og_image)}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
<meta name="twitter:image" content="{page_url(og_image)}">
<link rel="icon" href="{pg.rel('favicon.svg')}" type="image/svg+xml">
<link rel="icon" href="{pg.rel('assets/img/favicon-32.png')}" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{pg.rel('assets/img/apple-touch-icon.png')}">
<link rel="manifest" href="{pg.rel('manifest.webmanifest')}">
<link rel="stylesheet" href="{pg.asset('assets/css/site.css')}">
<script src="{pg.asset('assets/js/config.js')}"></script>
<script src="{pg.asset('assets/js/app.js')}" defer></script>
{extra}<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False, separators=(',', ':'))}</script>
</head>
"""


def header(pg, current=None):
    groups = []
    for key, name, _ in CATEGORIES:
        items = "".join(
            f'<li><a href="{pg.rel(c["slug"] + "/")}"{" aria-current=\"page\"" if c["slug"] == current else ""}>'
            f'{esc(c["name"])}</a></li>' for c in CALCULATORS if c["cat"] == key)
        groups.append(f'<div class="mega-group"><p class="mega-title">{icon(key)}{esc(name)}</p><ul>{items}</ul></div>')
    return f"""<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
 <div class="nav">
  <a class="brand" href="{pg.rel('')}" aria-label="{SITE['name']} home">{LOGO}<span>Calc<b>My</b>Fin</span></a>
  <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-menu">{icon('menu')}<span class="sr-only">Menu</span></button>
  <nav id="site-menu" class="nav-menu" aria-label="Primary">
   <div class="has-mega">
    <button class="mega-btn" type="button" aria-expanded="false">Calculators {icon('chev', 'icon chev')}</button>
    <div class="mega">{''.join(groups)}</div>
   </div>
   <a href="{pg.rel('mortgage-calculator/')}">Mortgage</a>
   <a href="{pg.rel('compound-interest-calculator/')}">Investing</a>
   <a href="{pg.rel('debt-payoff-calculator/')}">Debt</a>
   <a href="{pg.rel('about/')}">About</a>
  </nav>
 </div>
</header>
"""


def footer(pg):
    cols = []
    for key, name, _ in CATEGORIES:
        links = "".join(f'<li><a href="{pg.rel(c["slug"] + "/")}">{esc(c["name"])} calculator</a></li>'
                        for c in CALCULATORS if c["cat"] == key)
        cols.append(f'<div><p class="foot-title">{esc(name)}</p><ul>{links}</ul></div>')
    return f"""<div class="ad-wrap ad-wrap-footer"><aside class="ad" data-ad="footer" id="ad-footer" aria-label="Advertisement"></aside></div>
<footer class="site-footer">
 <div class="footer-inner">
  <div class="foot-brand">
   <a class="brand" href="{pg.rel('')}">{LOGO}<span>Calc<b>My</b>Fin</span></a>
   <p>{esc(SITE['tagline'])}. Private by design: your numbers never leave your browser.</p>
  </div>
  <div class="foot-cols">{''.join(cols)}</div>
 </div>
 <div class="footer-legal">
  <p>© <span data-year>2026</span> {SITE['name']}. Educational estimates only, not financial, tax, legal or investment advice.</p>
  <nav aria-label="Legal"><a href="{pg.rel('about/')}">About</a><a href="{pg.rel('contact/')}">Contact</a><a href="{pg.rel('privacy-policy/')}">Privacy</a><a href="{pg.rel('terms/')}">Terms</a><a href="{pg.rel('disclaimer/')}">Disclaimer</a><a href="#" data-consent-open>Privacy choices</a></nav>
 </div>
</footer>
"""


def ad(slot, cls=""):
    return (f'<div class="ad-wrap {cls}"><aside class="ad" data-ad="{slot}" id="ad-{slot}" '
            f'aria-label="Advertisement"></aside></div>')


def breadcrumbs(pg, trail):
    """trail: [(label, path or None)]"""
    items = []
    for label, path in trail:
        items.append(f'<li><a href="{pg.rel(path)}">{esc(label)}</a></li>' if path is not None
                     else f'<li aria-current="page">{esc(label)}</li>')
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{"".join(items)}</ol></nav>'


def org_ld():
    return {"@type": "Organization", "@id": page_url("#org"), "name": SITE["name"], "url": page_url(""),
            "logo": page_url("assets/img/icon-512.png"), "email": SITE["email"]}


def website_ld():
    return {"@type": "WebSite", "@id": page_url("#website"), "name": SITE["name"], "url": page_url(""),
            "description": SITE["description"], "publisher": {"@id": page_url("#org")}, "inLanguage": "en-US"}


def faq_ld(faqs, pg):
    strip = lambda s: re.sub(r"<[^>]+>", "", link_tokens(s, pg))
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in faqs]}


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


# ---------------------------------------------------------------- worked examples (computed, never hand-typed)
def pmt(principal, annual_rate, years):
    n, r = years * 12, annual_rate / 100 / 12
    return principal / n if r == 0 else principal * r * (1 + r) ** n / ((1 + r) ** n - 1)


def usd(x, cents=False):
    return f"${x:,.2f}" if cents else f"${x:,.0f}"


def example(slug):
    if slug == "mortgage-calculator":
        m = pmt(360000, 6.5, 30)
        tot = m + 5400 / 12 + 1800 / 12
        return (f"<p>A <strong>$450,000</strong> home with <strong>$90,000</strong> down (20%) leaves a $360,000 loan. At "
                f"<strong>6.5%</strong> for 30 years, principal and interest is <strong>{usd(m, True)}</strong> a month. Add "
                f"$5,400 a year of property tax and $1,800 of insurance and the full payment is about "
                f"<strong>{usd(tot, True)}</strong>. Over 30 years you'd pay roughly {usd(m * 360 - 360000)} in interest.</p>")
    if slug == "home-affordability-calculator":
        inc, debts, down, rate, yrs, tax, ins = 100000, 500, 60000, 6.5, 30, 1.1, 1500
        gm = inc / 12
        max_pay = min(gm * .28, gm * .36 - debts)
        f = pmt(1, rate, yrs)
        price = (max_pay - ins / 12 + f * down) / (f + tax / 100 / 12)
        return (f"<p>A household earning <strong>$100,000</strong> a year with <strong>$500</strong> in monthly debts can spend "
                f"up to <strong>{usd(max_pay)}</strong> a month on housing under the 28/36 rule. With $60,000 down, a 6.5% "
                f"30-year rate, 1.1% property tax and $1,500 a year of insurance, that supports a home price of about "
                f"<strong>{usd(round(price, -3))}</strong>.</p>")
    if slug == "loan-payment-calculator":
        m = pmt(20000, 9, 5)
        return (f"<p>Borrowing <strong>$20,000</strong> at <strong>9%</strong> for <strong>5 years</strong> costs "
                f"<strong>{usd(m, True)}</strong> a month and about {usd(m * 60 - 20000)} in total interest.</p>")
    if slug == "auto-loan-calculator":
        price, trade, down, taxr, fees = 35000, 5000, 3000, 6, 800
        amt = price - trade - down + (price - trade) * taxr / 100 + fees
        m = pmt(amt, 7, 5)
        return (f"<p>A <strong>$35,000</strong> car with a $5,000 trade-in, $3,000 down, 6% sales tax and $800 in fees means "
                f"financing about <strong>{usd(amt)}</strong>. At <strong>7% APR for 60 months</strong>, the payment is "
                f"<strong>{usd(m, True)}</strong>, with roughly {usd(m * 60 - amt)} in interest.</p>")
    if slug == "debt-payoff-calculator":
        return ("<p>Say you owe $6,000 on a credit card at 24% APR, $900 on a store card at 18% and $9,000 on a car loan at 7%, "
                "and can pay $200 a month beyond the minimums. <strong>Avalanche</strong> sends the extra $200 to the 24% card "
                "first, which cuts the most interest. <strong>Snowball</strong> clears the $900 store card in a few months for a "
                "quick win, then rolls that payment into the next debt. These are the default numbers in the calculator above, "
                "so you can see exactly how much the avalanche saves.</p>")
    if slug == "credit-card-payoff-calculator":
        bal, apr, pay = 5000, 22, 150
        b, i, mth = bal, 0.0, 0
        while b > 0.005 and mth < 1200:
            it = b * apr / 1200
            i += it
            b -= min(b, pay - it)
            mth += 1
        return (f"<p>A <strong>$5,000</strong> balance at <strong>22% APR</strong> paid at <strong>$150 a month</strong> takes "
                f"about <strong>{mth // 12} years and {mth % 12} months</strong> to clear and costs around "
                f"<strong>{usd(i)}</strong> in interest. To finish in 24 months you'd need about "
                f"{usd(bal * (apr / 1200) / (1 - (1 + apr / 1200) ** -24), True)} a month.</p>")
    if slug == "compound-interest-calculator":
        b = 10000
        for _ in range(12 * 20):
            b = b * (1 + .07 / 12) + 300
        dep = 10000 + 300 * 240
        return (f"<p>Start with <strong>$10,000</strong>, add <strong>$300 a month</strong> and earn <strong>7%</strong> "
                f"compounded monthly. After <strong>20 years</strong> you'd have about <strong>{usd(b)}</strong>. You "
                f"contributed {usd(dep)}, so roughly {usd(b - dep)} came from compound growth.</p>")
    if slug == "retirement-calculator":
        bal, contrib, sal = 50000, 500 * 12, 70000
        for _ in range(35):
            bal = bal * 1.06 + contrib + sal * .04
            contrib *= 1.03
            sal *= 1.03
        return (f"<p>A 30-year-old with $50,000 saved, contributing $500 a month with a 4% match on a $70,000 salary (both "
                f"rising 3% a year) and earning 6% could have about <strong>{usd(round(bal, -3))}</strong> at 65. At a 4% "
                f"withdrawal rate that's roughly <strong>{usd(round(bal * .04, -2))}</strong> in first-year income, before "
                f"adjusting for inflation.</p>")
    if slug == "savings-goal-calculator":
        goal, cur, months, apy = 30000, 5000, 36, 4
        i = (1 + apy / 100) ** (1 / 12) - 1
        need = (goal - cur * (1 + i) ** months) * i / ((1 + i) ** months - 1)
        return (f"<p>To reach a <strong>$30,000</strong> down payment in <strong>3 years</strong>, starting with $5,000 in an "
                f"account earning <strong>4% APY</strong>, you'd need to save about <strong>{usd(need, True)}</strong> a "
                f"month. Without any interest it would be {usd((goal - cur) / months, True)}.</p>")
    if slug == "inflation-calculator":
        fut = 100 * 1.03 ** 20
        pp = 100 / 1.03 ** 20
        return (f"<p>At <strong>3%</strong> average inflation, something that costs <strong>$100</strong> today would cost "
                f"about <strong>{usd(fut, True)}</strong> in 20 years. Put the other way, $100 kept as cash would buy only "
                f"about <strong>{usd(pp, True)}</strong> worth of today's goods.</p>")
    if slug == "budget-calculator":
        return ("<p>With <strong>$5,000</strong> of monthly take-home pay, the 50/30/20 rule suggests about <strong>$2,500</strong> "
                "for needs, <strong>$1,500</strong> for wants and <strong>$1,000</strong> for savings and extra debt payments.</p>")
    if slug == "net-worth-calculator":
        return ("<p>Someone with $15,000 in savings, $60,000 in a 401(k), a home worth $350,000 and a $12,000 car has "
                "$437,000 in assets. With a $280,000 mortgage, a $9,000 car loan and $3,000 on credit cards ($292,000 in "
                "liabilities), their net worth is <strong>$145,000</strong>.</p>")
    if slug == "salary-to-hourly-calculator":
        return ("<p>A <strong>$75,000</strong> salary at 40 hours a week for 52 weeks is about <strong>$36.06 an hour</strong>, "
                "$1,442 a week, $2,885 every two weeks and $6,250 a month, all before taxes.</p>")
    if slug == "emergency-fund-calculator":
        return ("<p>If your essential costs are <strong>$3,200</strong> a month, a 6-month emergency fund is "
                "<strong>$19,200</strong>. With $8,000 saved you're about 42% of the way there.</p>")
    if slug == "life-insurance-calculator":
        return ("<p>Replacing a <strong>$80,000</strong> income for 10 years ($800,000), plus a $250,000 mortgage and $100,000 "
                "for college, minus $75,000 in savings and existing coverage, suggests about <strong>$1,075,000</strong> "
                "of life insurance.</p>")
    return ""


# ---------------------------------------------------------------- page types
def calc_card(pg, c, cls="tool-card"):
    return (f'<a class="{cls}" href="{pg.rel(c["slug"] + "/")}" data-search="{esc((c["name"] + " " + c["card"] + " " + CAT[c["cat"]][0]).lower())}">'
            f'<span class="tool-icon cat-{c["cat"]}">{icon(c["cat"])}</span>'
            f'<span class="tool-text"><strong>{esc(c["name"])} calculator</strong><span>{esc(c["card"])}</span></span>'
            f'{icon("arrow", "icon go")}</a>')


def render_calc(c):
    pg = Page(c["slug"] + "/", 1)
    cat_name = CAT[c["cat"]][0]
    form = open(os.path.join(SRC, "forms", c["slug"] + ".html"), encoding="utf-8").read()
    faqs_html = "".join(f'<details class="faq"><summary>{esc(q)}</summary><div>{link_tokens(a, pg)}</div></details>'
                        for q, a in c["faqs"])
    related = "".join(calc_card(pg, BY_SLUG[s], "tool-card compact") for s in c["related"])
    how = "".join(f"<li>{esc(s)}</li>" for s in c["how"])
    tips = "".join(f"<li>{esc(s)}</li>" for s in c["tips"])
    sources = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{esc(l)}</a></li>' for l, u in c["sources"])
    same_cat = "".join(f'<li><a href="{pg.rel(o["slug"] + "/")}">{esc(o["name"])} calculator</a></li>'
                       for o in CALCULATORS if o["cat"] == c["cat"] and o["slug"] != c["slug"])
    jsonld = {"@context": "https://schema.org", "@graph": [
        org_ld(), website_ld(),
        {"@type": "WebApplication", "@id": page_url(pg.path + "#app"), "name": c["title"].split(":")[0],
         "url": page_url(pg.path), "description": c["description"], "applicationCategory": "FinanceApplication",
         "operatingSystem": "Any", "browserRequirements": "Requires JavaScript",
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
         "publisher": {"@id": page_url("#org")}, "isAccessibleForFree": True, "inLanguage": "en-US"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": page_url("")},
            {"@type": "ListItem", "position": 2, "name": cat_name, "item": page_url("#" + c["cat"])},
            {"@type": "ListItem", "position": 3, "name": c["h1"], "item": page_url(pg.path)}]},
        faq_ld(c["faqs"], pg)]}
    body = f"""{head(pg, c['title'], c['description'], f"assets/img/og/{c['slug']}.png", jsonld)}{header(pg, c['slug'])}
<main id="main" class="calc-page" data-calc="{c['slug']}" data-cat="{c['cat']}">
 <div class="page-top">
  {breadcrumbs(pg, [("Home", ""), (cat_name, "#" + c["cat"]), (c["h1"], None)])}
  <header class="page-intro">
   <p class="eyebrow cat-{c['cat']}">{icon(c['cat'])}{esc(cat_name)}</p>
   <h1>{esc(c['h1'])}</h1>
   <p class="lead">{esc(c['lead'])}</p>
   <ul class="trust-row"><li>{icon('check')}Free, no sign-up</li><li>{icon('lock')}Private: runs in your browser</li><li>{icon('bolt')}Updated {SITE['updated_human']}</li></ul>
  </header>
 </div>
 <section class="calc-shell" aria-label="{esc(c['name'])} calculator">
  {form}
  <div class="calc-actions">
   <button type="button" class="ghost" data-share>{icon('share')}<span>Copy link to these results</span></button>
   <button type="button" class="ghost" data-print>{icon('print')}<span>Print</span></button>
   <button type="button" class="ghost" data-reset>{icon('reset')}<span>Reset</span></button>
  </div>
 </section>
 {ad('after-results', 'ad-wide')}
 <aside class="partner" data-partner="{c['cat']}" hidden></aside>
 <div class="content-layout">
  <article class="prose">
   <h2 id="how-to-use">How to use the {esc(c['name'].lower())} calculator</h2>
   <ol class="steps">{how}</ol>
   <h2 id="formula">How it's calculated</h2>
   {c['formula']}
   <h2 id="example">Example</h2>
   <div class="example">{example(c['slug'])}</div>
   {ad('in-content')}
   <h2 id="tips">Tips</h2>
   <ul class="tips">{tips}</ul>
   <h2 id="faq">Frequently asked questions</h2>
   <div class="faqs">{faqs_html}</div>
   <h2 id="related">Related calculators</h2>
   <div class="tool-grid compact">{related}</div>
   <h2 id="sources">Sources</h2>
   <ul class="sources">{sources}</ul>
   <p class="disclaimer">This calculator provides educational estimates only and is not financial, tax, legal or investment advice. Results depend on the assumptions you enter; actual terms from lenders, insurers and tax authorities may differ.</p>
  </article>
  <aside class="sidebar">
   <div class="side-card"><p class="side-title">On this page</p><ul class="toc"><li><a href="#how-to-use">How to use it</a></li><li><a href="#formula">The formula</a></li><li><a href="#example">Example</a></li><li><a href="#tips">Tips</a></li><li><a href="#faq">FAQ</a></li></ul></div>
   <div class="side-card"><p class="side-title">More {esc(cat_name.lower())} tools</p><ul class="side-links">{same_cat}</ul></div>
   <div class="sticky-ad">{ad('sidebar')}</div>
  </aside>
 </div>
</main>
{footer(pg)}<script src="{pg.asset('assets/js/charts.js')}" defer></script>
<script src="{pg.asset('assets/calculators/common.js')}" defer></script>
<script src="{pg.asset('assets/calculators/' + c['js'])}" defer></script>
</body>
</html>
"""
    write(os.path.join(c["slug"], "index.html"), body)


def render_home():
    pg = Page("", 0)
    popular = "".join(calc_card(pg, BY_SLUG[s], "tool-card feature") for s in POPULAR)
    sections = []
    for key, name, blurb in CATEGORIES:
        cards = "".join(calc_card(pg, c) for c in CALCULATORS if c["cat"] == key)
        sections.append(f'<section class="cat-section" id="{key}"><div class="cat-head"><span class="tool-icon cat-{key}">{icon(key)}</span>'
                        f'<div><h2>{esc(name)} calculators</h2><p>{esc(blurb)}</p></div></div><div class="tool-grid">{cards}</div></section>')
    faqs_html = "".join(f'<details class="faq"><summary>{esc(q)}</summary><div>{esc(a)}</div></details>' for q, a in HOME_FAQS)
    items = [{"@type": "ListItem", "position": i + 1, "url": page_url(c["slug"] + "/"), "name": c["h1"]}
             for i, c in enumerate(CALCULATORS)]
    jsonld = {"@context": "https://schema.org", "@graph": [
        org_ld(), website_ld(),
        {"@type": "ItemList", "name": "Personal finance calculators", "itemListElement": items},
        faq_ld(HOME_FAQS, pg)]}
    body = f"""{head(pg, 'Free Financial Calculators: Mortgage, Loans, Savings & Retirement | CalcMyFin', SITE['description'], 'assets/img/og/home.png', jsonld)}{header(pg)}
<main id="main" class="home">
 <section class="hero">
  <div class="hero-inner">
   <p class="eyebrow">{len(CALCULATORS)} free calculators · no sign-up</p>
   <h1>Free financial calculators that <span class="hl">show their math</span></h1>
   <p class="lead">Plan a mortgage, pay off debt, grow your savings and budget with confidence. Clear formulas, instant results, and your numbers never leave your device.</p>
   <div class="search" role="search">
    {icon('search')}
    <label class="sr-only" for="calc-search">Search calculators</label>
    <input id="calc-search" type="search" placeholder="Search calculators: mortgage, 401k, debt…" autocomplete="off">
   </div>
   <ul class="trust-row light"><li>{icon('check')}100% free</li><li>{icon('lock')}Private by design</li><li>{icon('bolt')}Instant results</li></ul>
  </div>
 </section>
 <section class="popular" aria-labelledby="popular-h"><h2 id="popular-h">Most popular</h2><div class="tool-grid feature-grid">{popular}</div></section>
 <p class="no-results" hidden>No calculators match that search. Try “loan”, “savings” or “retire”.</p>
 {ad('home-top', 'ad-wide')}
 {''.join(sections)}
 <section class="why">
  <h2>Why people use CalcMyFin</h2>
  <div class="why-grid">
   <div><span class="why-icon">{icon('check')}</span><h3>Transparent formulas</h3><p>Every calculator explains exactly how the numbers are worked out, with a worked example, so you can trust and check the result.</p></div>
   <div><span class="why-icon">{icon('lock')}</span><h3>Private by design</h3><p>No accounts, no forms, no data collection. All math runs in your browser and nothing you type is sent anywhere.</p></div>
   <div><span class="why-icon">{icon('bolt')}</span><h3>Built for real decisions</h3><p>Taxes, insurance, PMI, employer match, inflation: the details that change the real answer are included, not ignored.</p></div>
  </div>
 </section>
 <section class="home-faq"><h2>Common questions</h2><div class="faqs">{faqs_html}</div></section>
</main>
{footer(pg)}<script>document.addEventListener('DOMContentLoaded',function(){{window.CMF&&CMF.initSearch&&CMF.initSearch();}});</script>
</body>
</html>
"""
    write("index.html", body)


STATIC = {
    "about": ("About CalcMyFin", "About CalcMyFin: who builds these free financial calculators, how we check the math, and our editorial standards.", """
<h1>About CalcMyFin</h1>
<p class="lead">CalcMyFin makes free, straightforward calculators for the money decisions most people face: buying a home, paying off debt, saving for goals and planning for retirement.</p>
<h2>What we believe</h2>
<p>Money tools should be honest and easy to understand. Every calculator on this site shows the formula it uses and a worked example, so you can see exactly where a number comes from instead of trusting a black box.</p>
<h2>How we build and check our calculators</h2>
<ul>
<li><strong>Standard formulas.</strong> We use widely published formulas, like the fixed-rate amortization formula for loans and standard compounding for savings, and explain them on each page.</li>
<li><strong>Tested edge cases.</strong> Inputs are validated so zero rates, very large balances and payments that don't cover interest are handled clearly instead of producing misleading results.</li>
<li><strong>Trusted references.</strong> Guidance and definitions are based on public sources such as the Consumer Financial Protection Bureau, the Federal Reserve, the FDIC, the IRS and the Bureau of Labor Statistics, which we link on each page.</li>
<li><strong>Regular reviews.</strong> Pages show when they were last updated, and we revisit assumptions as rules and typical rates change.</li>
</ul>
<h2>Privacy first</h2>
<p>There's no account to create and nothing to submit. The numbers you enter are processed in your browser and are never sent to us. See our <a href="../privacy-policy/">privacy policy</a> for details about analytics and advertising.</p>
<h2>How the site is funded</h2>
<p>CalcMyFin is free because it is supported by advertising and, in some places, clearly labeled partner links. Advertisers and partners never influence our formulas or results.</p>
<h2>Important note</h2>
<p>Our calculators provide educational estimates, not personalized financial, tax, legal or investment advice. For important decisions, consider speaking with a qualified professional. Read our full <a href="../disclaimer/">disclaimer</a>.</p>
<p>Questions or found an error? <a href="../contact/">Contact us</a>. We read every message.</p>
"""),
    "contact": ("Contact CalcMyFin", "Contact the CalcMyFin team with questions, feedback, corrections or partnership inquiries.", """
<h1>Contact us</h1>
<p class="lead">We'd love to hear from you, whether it's a question, a bug, a correction or an idea for a new calculator.</p>
<p class="contact-email"><a href="mailto:{email}">{email}</a></p>
<ul>
<li><strong>Found an error?</strong> Tell us the calculator and the numbers you entered, and we'll look into it.</li>
<li><strong>Calculator request?</strong> Let us know what money question you're trying to answer.</li>
<li><strong>Partnerships and advertising:</strong> please include your company and website.</li>
</ul>
<p>We can't give personalized financial advice by email. For decisions specific to your situation, a qualified financial professional can help.</p>
"""),
    "privacy-policy": ("Privacy Policy", "How CalcMyFin handles your data, cookies, analytics and advertising.", """
<h1>Privacy Policy</h1>
<p class="lead">Last updated: {updated}</p>
<h2>The short version</h2>
<p>The numbers you type into our calculators stay in your browser. We don't ask for accounts, names or email addresses to use the site. Like most websites, we use analytics and advertising services that may use cookies, described below.</p>
<h2>Information you enter into calculators</h2>
<p>All calculations run locally in your web browser. The values you enter are not transmitted to or stored on our servers. If you use the "copy link" feature, your inputs are placed in the link's web address so the results can be reopened. That link is only shared if you share it.</p>
<h2>Analytics</h2>
<p>We use Google Analytics to understand how visitors use the site (for example, which pages are visited and how long people stay) so we can improve it. Google Analytics uses cookies and collects information such as your approximate location, device, browser and pages viewed. It does not receive the values you enter into calculators. Learn more at <a href="https://policies.google.com/technologies/partner-sites" rel="noopener" target="_blank">How Google uses information from sites that use its services</a>.</p>
<h2>Advertising</h2>
<p>We may display ads from Google AdSense and other advertising partners. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this site and/or other sites on the internet.</p>
<p>You can opt out of personalized advertising by visiting <a href="https://adssettings.google.com" rel="noopener" target="_blank">Google Ads Settings</a>, or opt out of some third-party vendors' use of cookies at <a href="https://www.aboutads.info/choices/" rel="noopener" target="_blank">aboutads.info</a>.</p>
<h2>Partner links</h2>
<p>Some pages may include clearly labeled sponsored or partner links. If you click one and make a purchase or sign up, we may earn a commission at no extra cost to you. Partners may use their own cookies to track referrals.</p>
<h2>Your choices</h2>
<ul>
<li>Use the <a href="#" data-consent-open>Privacy choices</a> link in the footer to change your cookie preferences.</li>
<li>Most browsers let you block or delete cookies in their settings.</li>
<li>Residents of certain U.S. states (such as California) may have rights to know about, delete or opt out of the "sale" or "sharing" of personal information for targeted advertising. You can exercise the opt-out using the Privacy choices link or contact us.</li>
</ul>
<h2>Children</h2>
<p>This site is not directed to children under 13, and we do not knowingly collect their personal information.</p>
<h2>Changes</h2>
<p>We may update this policy from time to time. The date at the top shows when it was last revised.</p>
<h2>Contact</h2>
<p>Questions? Email <a href="mailto:{email}">{email}</a>.</p>
"""),
    "terms": ("Terms of Use", "The terms that apply when you use CalcMyFin's free financial calculators.", """
<h1>Terms of Use</h1>
<p class="lead">Last updated: {updated}</p>
<p>By using CalcMyFin ("the site") you agree to these terms. If you don't agree, please don't use the site.</p>
<h2>Educational use only</h2>
<p>The calculators and content are provided for general educational and informational purposes. They are not financial, investment, tax, legal or insurance advice, and they are not an offer or recommendation of any product.</p>
<h2>No guarantee of accuracy</h2>
<p>We work hard to keep formulas correct and content current, but results are estimates based on the information you provide and simplifying assumptions. We make no warranty that results are accurate, complete or suitable for your situation. Verify important figures with a qualified professional or the relevant provider.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, CalcMyFin and its owners are not liable for any loss or damage arising from your use of, or reliance on, the site or its results.</p>
<h2>Third-party links and ads</h2>
<p>The site may contain advertisements and links to third-party websites. We are not responsible for their content, products or practices.</p>
<h2>Intellectual property</h2>
<p>The site's design, text and code are owned by CalcMyFin. You may share links to any page and use results for personal purposes.</p>
<h2>Changes</h2>
<p>We may update these terms at any time. Continued use of the site means you accept the updated terms.</p>
<p>Contact: <a href="mailto:{email}">{email}</a></p>
"""),
    "disclaimer": ("Financial Disclaimer", "CalcMyFin provides educational estimates, not financial advice. Read our full disclaimer.", """
<h1>Financial Disclaimer</h1>
<p class="lead">Last updated: {updated}</p>
<p>CalcMyFin's calculators and articles are for educational and informational purposes only. They do not constitute financial, investment, tax, legal, accounting or insurance advice, and CalcMyFin is not a licensed financial adviser, broker, lender or insurer.</p>
<h2>Estimates, not quotes</h2>
<p>Results are hypothetical estimates based on the numbers you enter and on standard formulas and assumptions. They are not loan offers, insurance quotes, tax calculations or guarantees of future results. Actual rates, payments, fees, returns and taxes will vary.</p>
<h2>Investment returns</h2>
<p>Projections that use a rate of return assume that rate stays constant, which never happens in real markets. Investments can lose value, and past performance does not predict future results.</p>
<h2>Advertising and partners</h2>
<p>The site is supported by advertising and may include sponsored or partner links, which are always labeled. These relationships do not affect our calculators' formulas or results.</p>
<h2>Get professional advice</h2>
<p>Before making significant financial decisions, consider consulting a qualified professional who can review your full situation.</p>
"""),
}


def render_static():
    for slug, (title, desc, content) in STATIC.items():
        pg = Page(slug + "/", 1)
        jsonld = {"@context": "https://schema.org", "@graph": [
            org_ld(), website_ld(),
            {"@type": "WebPage", "name": title, "url": page_url(pg.path), "description": desc,
             "isPartOf": {"@id": page_url("#website")}, "dateModified": SITE["updated"]},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": page_url("")},
                {"@type": "ListItem", "position": 2, "name": title, "item": page_url(pg.path)}]}]}
        text = content.replace("{email}", SITE["email"]).replace("{updated}", SITE["updated_human"])
        body = f"""{head(pg, title, desc, 'assets/img/og/home.png', jsonld)}{header(pg)}
<main id="main" class="static-page">
 {breadcrumbs(pg, [("Home", ""), (title, None)])}
 <article class="prose narrow">{text}</article>
</main>
{footer(pg)}</body>
</html>
"""
        write(os.path.join(slug, "index.html"), body)


def render_404():
    # 404 pages are served at arbitrary depths, so use absolute paths from the canonical base
    pg = Page("404.html", 0)
    cards = "".join(calc_card(pg, BY_SLUG[s]) for s in POPULAR)
    base = SITE["base_url"] + "/"
    body = head(pg, "Page not found", "The page you were looking for doesn't exist.", "assets/img/og/home.png",
                {"@context": "https://schema.org", "@type": "WebPage", "name": "Page not found"},
                extra=f'<base href="{base}">\n', robots="noindex,follow")
    body += header(pg) + f"""<main id="main" class="static-page"><article class="prose narrow"><h1>Page not found</h1>
<p class="lead">Sorry, that page doesn't exist or has moved. Try one of our most popular calculators:</p></article>
<div class="tool-grid">{cards}</div></main>{footer(pg)}</body></html>"""
    write("404.html", body)


def render_redirects():
    """Old /name.html URLs -> new /name/ folders."""
    olds = [c["slug"] for c in CALCULATORS] + list(STATIC.keys())
    for slug in olds:
        target = page_url(slug + "/")
        write(slug + ".html", f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved</title>
<link rel="canonical" href="{target}"><meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0; url={slug}/"><script>location.replace('{slug}/'+location.search+location.hash)</script>
</head><body><p>This page has moved to <a href="{slug}/">{slug}</a>.</p></body></html>
""")


def render_meta_files():
    urls = [("", "1.0", "weekly")] + [(c["slug"] + "/", "0.9" if c["slug"] in POPULAR else "0.8", "monthly")
                                       for c in CALCULATORS] + [(s + "/", "0.3", "yearly") for s in STATIC]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, pri, freq in urls:
        sm.append(f"  <url><loc>{page_url(path)}</loc><lastmod>{SITE['updated']}</lastmod>"
                  f"<changefreq>{freq}</changefreq><priority>{pri}</priority></url>")
    sm.append("</urlset>\n")
    write("sitemap.xml", "\n".join(sm))
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /src/\n\nSitemap: {page_url('sitemap.xml')}\n")
    write("manifest.webmanifest", json.dumps({
        "name": SITE["name"], "short_name": SITE["name"], "description": SITE["description"],
        "start_url": "./", "display": "standalone", "background_color": "#f6f7f4", "theme_color": "#0f5c4d",
        "icons": [{"src": "assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    write("favicon.svg", LOGO.replace('class="logo-mark" ', 'xmlns="http://www.w3.org/2000/svg" '))
    write(".nojekyll", "")
    # GitHub Pages custom domain (must match the DNS records at Cloudflare)
    write("CNAME", SITE["domain"] + "\n")


def clean_old():
    """Remove files from the original version that the new build replaces."""
    for old in ("assets/style.css", "assets/main.js"):
        p = os.path.join(ROOT, old)
        if os.path.exists(p):
            os.remove(p)


if __name__ == "__main__":
    clean_old()
    render_home()
    for c in CALCULATORS:
        render_calc(c)
    render_static()
    render_404()
    render_redirects()
    render_meta_files()
    print(f"Built {len(CALCULATORS)} calculators + {len(STATIC)} pages for {SITE['base_url']}")
