"""Renders the programmatic pay-conversion pages.

Imported by build.py (which passes its own helpers in) so there is no circular
import and build.py stays readable.

Deliberate choices:
  * No FAQPage schema. The questions would be templated across every page, which
    is the most machine-generated thing we could ship, and Google stopped showing
    FAQ rich results for sites like this one anyway.
  * The real calculator is embedded, pre-filled with this page's figure, rather
    than linked. The page should answer the follow-up question too.
  * The tax section explains why no one can give a single take-home number,
    instead of brushing the question off. "after taxes" is the most common
    follow-up search, so it deserves a real answer.
"""
import os

import salary_pages as SP

MAIN = "salary-to-hourly-calculator/"
_FORM = None


def _form_html(src_dir):
    global _FORM
    if _FORM is None:
        with open(os.path.join(src_dir, "forms", "salary-to-hourly-calculator.html"),
                  encoding="utf-8") as f:
            _FORM = f.read()
    return _FORM


def _prefilled_form(src_dir, kind, value):
    """The live calculator, already showing this page's number."""
    form = _form_html(src_dir)
    if kind == "salary":
        return form.replace('value="75000"', f'value="{value:.0f}"', 1)
    form = form.replace('value="75000"', f'value="{value:g}"', 1)
    form = form.replace('<option value="year" selected>Year</option>',
                        '<option value="year">Year</option>')
    return form.replace('<option value="hour">Hour</option>',
                        '<option value="hour" selected>Hour</option>')


def _row(label, value, note=""):
    n = f'<td class="pay-note">{note}</td>' if note else "<td></td>"
    return f'<tr><th scope="row">{label}</th><td><strong>{value}</strong></td>{n}</tr>'


def _conversion_table(d):
    m = SP.money
    return f"""<table class="conv-table">
  <caption>Gross pay, before tax</caption>
  <thead><tr><th scope="col">Period</th><th scope="col">Amount</th><th scope="col"></th></tr></thead>
  <tbody>
   {_row("Per hour", m(d["hourly"]), f"{d['hours_per_week']:g} hours a week")}
   {_row("Per day", m(d["daily"]), "8-hour day")}
   {_row("Per week", m(d["weekly"]))}
   {_row("Every 2 weeks", m(d["biweekly"]), "26 pay periods")}
   {_row("Twice a month", m(d["semimonthly"]), "24 pay periods")}
   {_row("Per month", m(d["monthly"]))}
   {_row("Per year", m(d["annual"], cents=False))}
  </tbody>
 </table>"""


def _variants_table(annual):
    rows = []
    for hours, weeks, label in SP.VARIANTS:
        v = SP.from_salary(annual, hours, weeks)
        rows.append(f'<tr><th scope="row">{label}</th><td><strong>{SP.money(v["hourly"])}</strong></td>'
                    f'<td class="pay-note">{v["yearly_hours"]:,.0f} hours a year</td></tr>')
    return f"""<table class="conv-table">
  <caption>The same pay on a different schedule</caption>
  <thead><tr><th scope="col">Schedule</th><th scope="col">Hourly</th><th scope="col"></th></tr></thead>
  <tbody>{"".join(rows)}</tbody>
 </table>"""


def _tax_section(lbl):
    return f"""<h2>Why nobody can tell you your take-home pay</h2>
  <p>Every figure above is <strong>gross pay</strong> &mdash; what you earn before anything comes out.
     Search for "{lbl} after taxes" and you will find sites that hand you one confident number.
     Treat those carefully, because the honest answer depends on things only you know.</p>
  <p>Four separate deductions decide what actually reaches your account:</p>
  <ul>
   <li><strong>Income tax</strong>, charged in bands. This is the part most people get wrong: moving
       into a higher band does not tax all of your income at that rate, only the slice above the
       threshold. Your effective rate is always lower than your top band.</li>
   <li><strong>Social security or national insurance</strong> &mdash; usually a flat percentage,
       sometimes capped once you pass a certain income.</li>
   <li><strong>Where you live.</strong> Two people both earning {lbl} take home noticeably different
       amounts if one lives somewhere with a regional or state income tax and the other does not.</li>
   <li><strong>What you have opted into</strong> &mdash; pension or retirement contributions, health
       cover and similar. These come out before you ever see the money, and they differ per person
       even inside the same company.</li>
  </ul>
  <p>Because of the last two especially, a single "after tax" figure for {lbl} would be wrong for most
     of the people reading it. Your most recent payslip is the only accurate source, and it already
     has the number on it.</p>"""


def render_pay_page(ctx, kind, value, values, idx):
    """kind is 'salary' or 'hourly'. ctx carries build.py's helpers."""
    esc, Page, head, header, footer, breadcrumbs = (
        ctx["esc"], ctx["Page"], ctx["head"], ctx["header"], ctx["footer"], ctx["breadcrumbs"])
    org_ld, website_ld, page_url, write = (
        ctx["org_ld"], ctx["website_ld"], ctx["page_url"], ctx["write"])
    m = SP.money

    if kind == "salary":
        d = SP.from_salary(value)
        slug, folder = SP.salary_slug(value), "salary"
        lbl = SP.salary_label(value)
        h1 = f"{lbl} a Year Is How Much an Hour?"
        answer = (f"<strong>{lbl} a year is {m(d['hourly'])} an hour</strong> at 40 hours a week. "
                  f"That is {m(d['weekly'])} a week and {m(d['monthly'])} a month, before tax.")
        desc = (f"{lbl} a year is {m(d['hourly'])} an hour at 40 hours a week. "
                f"See it per day, week, two weeks and month, plus other schedules.")
        maths = (f"A full-time year is 40 hours &times; 52 weeks = <strong>2,080 hours</strong>. "
                 f"{lbl} &divide; 2,080 = <strong>{m(d['hourly'])}</strong> an hour.")
        nb_label = lambda v: f"{SP.salary_label(v)} a year"
        nb_path = lambda v: f"../{SP.salary_slug(v)}/"
        near = SP.nearest(SP.HOURLY, d["hourly"])
        flip = (f'<p class="pay-flip">Paid by the hour instead? See '
                f'<a href="../../hourly/{SP.hourly_slug(near)}/">'
                f'{SP.hourly_label(near)} an hour is how much a year</a>.</p>')
    else:
        d = SP.from_hourly(value)
        slug, folder = SP.hourly_slug(value), "hourly"
        lbl = SP.hourly_label(value)
        h1 = f"{lbl} an Hour Is How Much a Year?"
        answer = (f"<strong>{lbl} an hour is {m(d['annual'], cents=False)} a year</strong> at 40 hours "
                  f"a week. That is {m(d['weekly'])} a week and {m(d['monthly'])} a month, before tax.")
        desc = (f"{lbl} an hour is {m(d['annual'], cents=False)} a year at 40 hours a week. "
                f"See it per day, week, two weeks and month, plus other schedules.")
        maths = (f"A full-time year is 40 hours &times; 52 weeks = <strong>2,080 hours</strong>. "
                 f"{lbl} &times; 2,080 = <strong>{m(d['annual'], cents=False)}</strong> a year.")
        nb_label = lambda v: f"{SP.hourly_label(v)} an hour"
        nb_path = lambda v: f"../{SP.hourly_slug(v)}/"
        near = SP.nearest(SP.SALARIES, d["annual"])
        flip = (f'<p class="pay-flip">On a salary instead? See '
                f'<a href="../../salary/{SP.salary_slug(near)}/">'
                f'{SP.salary_label(near)} a year is how much an hour</a>.</p>')

    path = f"{folder}/{slug}/"
    pg = Page(path, 2)
    nb_html = "".join(f'<li><a href="{nb_path(v)}">{nb_label(v)}</a></li>'
                      for v in SP.neighbours(values, idx))

    jsonld = {"@context": "https://schema.org", "@graph": [
        org_ld(), website_ld(),
        {"@type": "WebPage", "@id": page_url(path), "name": h1, "url": page_url(path),
         "description": desc, "isPartOf": {"@id": page_url("#website")},
         "dateModified": ctx["updated"], "inLanguage": "en-US"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": page_url("")},
            {"@type": "ListItem", "position": 2, "name": "Pay Converter", "item": page_url("salary/")},
            {"@type": "ListItem", "position": 3, "name": h1, "item": page_url(path)}]}]}

    body = f"""{head(pg, h1, desc, 'assets/img/og/salary-to-hourly-calculator.png', jsonld)}{header(pg)}
<main id="main" class="static-page pay-page" data-calc="salary-to-hourly-calculator" data-cat="plan">
 {breadcrumbs(pg, [("Home", ""), ("Pay Converter", "salary/"), (h1, None)])}
 <article class="prose narrow">
  <h1>{esc(h1)}</h1>
  <p class="pay-answer">{answer}</p>
  <p class="pay-maths">{maths}</p>
  {_conversion_table(d)}
  <h2>On a different schedule</h2>
  <p>Not everyone works 40 hours across 52 weeks. Here is the same pay on the schedules
     people most often actually work.</p>
  {_variants_table(d['annual'])}
  <h2>Try your own numbers</h2>
 </article>
 <section class="calc-shell" aria-label="Pay converter">
  {_prefilled_form(ctx['src_dir'], kind, value)}
 </section>
 <article class="prose narrow">
  {flip}
  {_tax_section(lbl)}
  <h2>Nearby figures</h2>
  <ul class="pay-nearby">{nb_html}</ul>
  <p><a href="{pg.rel(MAIN)}">Open the full salary to hourly calculator</a> for any figure, or
     <a href="{pg.rel('salary/')}">browse every salary we have converted</a>.</p>
 </article>
</main>
{footer(pg)}<script src="{pg.asset('assets/js/charts.js')}" defer></script>
<script src="{pg.asset('assets/calculators/common.js')}" defer></script>
<script src="{pg.asset('assets/calculators/' + ctx['calc_js'])}" defer></script>
</body>
</html>
"""
    write(f"{folder}/{slug}/index.html", body)
    return path
