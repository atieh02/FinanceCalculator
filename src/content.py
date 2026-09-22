"""Site-wide settings and all page copy. Edit text here, then run `python src/build.py`."""
import os

SITE = {
    "name": "CalcMyFin",
    "domain": "calcmyfin.com",
    # Canonical origin (override with the BASE_URL env var for local testing only)
    "base_url": os.environ.get("BASE_URL", "https://calcmyfin.com").rstrip("/"),
    "tagline": "Free financial calculators that show their math",
    "description": "Free, private personal finance calculators for investing, retirement, 401(k), savings goals, "
                   "budgeting and net worth. No sign-up, clear formulas, instant results.",
    "email": "hello@calcmyfin.com",
    "updated": "2026-09-22",
    "updated_human": "September 2026",
    "locale": "en_US",
    # IndexNow (Bing, Yandex, etc.): the key file /<key>.txt is written by build.py; run src/indexnow.py after publishing
    "indexnow_key": "8e6c086f06f5a4e9db937d4b66a0c756",
}

CATEGORIES = [
    ("grow", "Investing & Growth", "Watch your money grow, protect it from inflation and reach your goals."),
    ("retire", "Retirement", "Plan your nest egg, early retirement and how long your savings will last."),
    ("plan", "Budget & Planning", "Budgets, emergency savings, net worth and buying with cash instead of debt."),
]

# Each calculator: slug, category, name (short), title (<title>), description (meta),
# h1, lead, how (steps), formula (html), example (callable -> html, filled by build.py),
# tips, faqs [(q, a)], sources [(label, url)], related [slugs], js
CALCULATORS = [
    {
        "slug": "investment-growth-calculator", "cat": "grow", "name": "Investment Growth", "added": "2026-09-22",
        "renamed_from": "compound-interest-calculator",
        "card": "How your investments could grow over time.",
        "title": "Investment Growth Calculator: See Your Money Grow",
        "description": "Free investment growth calculator with monthly contributions. See how your investments could "
                       "grow over time and how much comes from growth versus your own deposits.",
        "h1": "Investment Growth Calculator",
        "lead": "See how a starting balance and regular monthly investments could grow when returns are reinvested. "
                "The chart shows how much of your future balance comes from your own contributions and how much from growth.",
        "how": ["Enter your starting amount and how much you'll invest each month.",
                "Add the average yearly return you expect from your investments.",
                "Choose how many years, and how often returns are added to your balance."],
        "formula": "<p>For a starting amount <strong>P</strong>, expected yearly return <strong>r</strong> added "
                   "<strong>n</strong> times per year for <strong>t</strong> years:</p>"
                   "<p class=\"formula\">A = P(1 + r/n)<sup>nt</sup></p>"
                   "<p>Monthly contributions are added along the way and grow the same way. The calculator steps through "
                   "every period, so gains are reinvested and start earning returns of their own.</p>",
        "tips": ["Time matters more than amount. Starting 10 years earlier can double your final balance.",
                 "The Rule of 72: divide 72 by your expected return to estimate how many years it takes money to double.",
                 "Automate monthly investing so it happens before spending.",
                 "Returns vary year to year and can be negative. Use a conservative figure for planning."],
        "faqs": [
            ("How does investment growth snowball?",
             "When gains are reinvested, they start producing gains of their own. Early on, most of your balance is "
             "your own money; over long periods growth can become the larger part, which is why starting early matters."),
            ("What return should I use?",
             "It depends on what you invest in. For a long-term, diversified stock portfolio many people plan with a "
             "conservative 5–7% average, but returns are never guaranteed and can be negative in any given year."),
            ("Does it matter how often returns are added?",
             "A little. More frequent reinvestment grows slightly faster at the same yearly return, but the effect is "
             "small compared with your return, contributions and time."),
            ("Is this a guaranteed result?",
             "No. The calculator assumes a steady average return to show the shape of long-term growth. Real markets "
             "rise and fall, so treat the result as one possible scenario."),
        ],
        "sources": [("Investor.gov: Introduction to investing", "https://www.investor.gov/introduction-investing"),
                    ("Investor.gov: Rule of 72", "https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-72")],
        "related": ["cost-of-waiting-calculator", "retirement-calculator", "inflation-calculator"],
        "js": "investment-growth.js",
    },
    {
        "slug": "retirement-calculator", "cat": "retire", "name": "Retirement",
        "card": "Project your nest egg and retirement income.",
        "title": "Retirement Calculator: Are You Saving Enough?",
        "description": "Free retirement calculator. Project your 401(k) or IRA balance at retirement with employer "
                       "match, salary growth and investment returns, and estimate the income it could provide.",
        "h1": "Retirement Calculator",
        "lead": "Project how much you could have at retirement from your current savings, monthly contributions and "
                "employer match, then estimate the yearly income that nest egg might support.",
        "how": ["Enter your age, planned retirement age and current retirement savings.",
                "Add your monthly contribution, salary and employer match percentage.",
                "Adjust the expected return, salary growth, inflation and withdrawal rate."],
        "formula": "<p>Each year until retirement, the balance grows by your expected return, then your contributions "
                   "and employer match are added. Contributions rise with your salary growth rate. At retirement, "
                   "first-year income is estimated as <strong>balance × withdrawal rate</strong>, commonly 4%, a "
                   "guideline from historical studies of sustainable withdrawals over about 30 years.</p>",
        "tips": ["Always contribute enough to get the full employer match. It's an immediate return on your money.",
                 "Raise your contribution by 1% each year, or whenever you get a raise.",
                 "Look at the inflation-adjusted (real) return to judge what your future balance will actually buy.",
                 "The 4% rule is a starting point, not a guarantee. Markets and lifespans vary."],
        "faqs": [
            ("How much do I need to retire?",
             "A common starting estimate is 25 times your expected yearly spending in retirement (the flip side of the "
             "4% rule), minus what Social Security or pensions will cover. Your actual number depends on lifestyle, "
             "health costs and retirement length."),
            ("What is the 4% rule?",
             "A guideline suggesting you can withdraw about 4% of your savings in the first year of retirement, then "
             "adjust for inflation, with a good chance of the money lasting around 30 years. It comes from studies of "
             "historical market returns and isn't a guarantee."),
            ("What return should I assume?",
             "Many planners use 5–7% for a diversified stock-heavy portfolio before inflation, and lower as you move "
             "to bonds near retirement. Try several rates to see a range of outcomes."),
            ("Does this include Social Security?",
             "No. It projects your personal savings only. Check your estimated benefit at ssa.gov and add it to the "
             "income figure for a fuller picture."),
        ],
        "sources": [("IRS: Retirement plans", "https://www.irs.gov/retirement-plans"),
                    ("SSA: Retirement benefits", "https://www.ssa.gov/benefits/retirement/")],
        "related": ["401k-calculator", "retirement-income-calculator", "fire-calculator"],
        "js": "retirement.js",
    },
    {
        "slug": "401k-calculator", "cat": "retire", "name": "401(k)", "added": "2026-09-22",
        "card": "Your 401(k) at retirement, with employer match and IRS limits.",
        "title": "401(k) Calculator: Employer Match & Retirement Balance",
        "description": "Free 401(k) calculator. Project your balance at retirement from your salary, contribution rate "
                       "and employer match, with 2026 IRS contribution limits and catch-up contributions built in.",
        "h1": "401(k) Calculator",
        "lead": "Project how much your 401(k) could grow by retirement. Enter your salary, contribution rate and employer "
                "match to see your future balance, how much is free money from your employer, and whether you're "
                "leaving any match on the table.",
        "how": ["Enter your age, the age you plan to retire and your current 401(k) balance.",
                "Add your salary and the percentage of pay you contribute.",
                "Enter your employer's match, for example 50% of what you put in, up to 6% of salary.",
                "Adjust expected raises, investment return and inflation to test different scenarios."],
        "formula": "<p>For each year until retirement:</p><ul>"
                   "<li><strong>Your contribution</strong> = salary × your contribution %, capped at the IRS limit "
                   "for your age if the limit option is on</li>"
                   "<li><strong>Employer match</strong> = salary × min(your %, match cap %) × match rate</li>"
                   "<li><strong>New balance</strong> = previous balance × (1 + return) + your contribution + employer match</li></ul>"
                   "<p>Your salary grows by the raise you enter each year. For 2026 the IRS employee limit is <strong>$24,500</strong>, "
                   "plus an <strong>$8,000</strong> catch-up at age 50 or older, or <strong>$11,250</strong> at ages 60 to 63. "
                   "The calculator holds these limits at 2026 levels, which is conservative because they usually rise with inflation. "
                   "The inflation-adjusted figure divides the result by (1 + inflation)<sup>years</sup>.</p>",
        "tips": ["Always contribute at least enough to get the full employer match. It's an instant 50% to 100% return.",
                 "Raise your contribution by 1% each year, or whenever you get a raise, until you reach 15% or more.",
                 "Check your plan's fund fees. A 1% difference in fees can cost tens of thousands of dollars over a career.",
                 "At 50 and older, catch-up contributions let you save thousands more each year."],
        "faqs": [
            ("How much can I contribute to a 401(k) in 2026?",
             "The IRS limit on employee contributions is $24,500 for 2026. Workers aged 50 and older can add an $8,000 "
             "catch-up contribution, for $32,500 in total, and those aged 60 to 63 can add $11,250 instead. Employer "
             "contributions don't count toward the employee limit."),
            ("What is a good 401(k) contribution rate?",
             "A common guideline is to save 15% of pay for retirement, including any employer match. At minimum, "
             "contribute enough to capture the full match, since that's free money."),
            ("How does an employer match work?",
             "A typical formula is '50% up to 6%': if you contribute 6% of your salary, your employer adds 3%. If you "
             "contribute only 4%, they add 2%. The calculator warns you if your rate is below your match cap."),
            ("Traditional or Roth 401(k)?",
             "Traditional contributions lower your taxable income now and are taxed when withdrawn. Roth contributions "
             "are taxed now and qualified withdrawals are tax-free. Roth tends to favor people who expect a higher tax "
             "rate in retirement. The growth projection is the same either way; only the taxes differ."),
            ("What return should I assume?",
             "Long-run stock market returns have historically averaged high single digits per year before inflation, "
             "but with large swings. Many planners use 5% to 7% for a diversified portfolio. Try several rates to see a range."),
        ],
        "sources": [("IRS: 401(k) limit increases to $24,500 for 2026", "https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500"),
                    ("IRS: Retirement topics - catch-up contributions", "https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-catch-up-contributions"),
                    ("Investor.gov: Retirement savings accounts", "https://www.investor.gov/introduction-investing/investing-basics/investment-accounts/tax-advantaged-accounts/retirement-savings")],
        "related": ["retirement-calculator", "investment-growth-calculator", "fire-calculator"],
        "js": "401k.js",
    },
    {
        "slug": "savings-goal-calculator", "cat": "grow", "name": "Savings Goal",
        "card": "How much to save each month to hit a goal.",
        "title": "Savings Goal Calculator: How Much to Save Each Month",
        "description": "Calculate how much you need to save each month to reach a savings goal by a target date. "
                       "Includes what you've already saved and an optional expected return.",
        "h1": "Savings Goal Calculator",
        "lead": "Pick a goal, like a car, a home or a trip, and a deadline. We'll work out exactly how much to set aside "
                "each month, counting what you already have and, if you invest it, the return you expect.",
        "how": ["Enter your savings goal and how much you've saved so far.",
                "Choose how many years (and months) until you need the money.",
                "Optionally add the yearly return you expect if the money is invested. Leave it at 0% for cash savings."],
        "formula": "<p>With no return, the monthly amount is simply (Goal − Savings) ÷ months. With an expected yearly "
                   "return <strong>R</strong>, the monthly rate is <strong>i</strong> = (1 + R)<sup>1/12</sup> − 1, your "
                   "current savings grow to S(1 + i)<sup>n</sup> over <strong>n</strong> months, and the monthly amount is:</p>"
                   "<p class=\"formula\">PMT = [Goal − S(1 + i)<sup>n</sup>] × i ÷ [(1 + i)<sup>n</sup> − 1]</p>",
        "tips": ["For money you'll need within a few years, keep it somewhere safe and easy to reach. Short-term investing can lose value.",
                 "Automate a transfer on payday so the money is set aside before you can spend it.",
                 "Break big goals into monthly milestones to track progress.",
                 "Buying with savings instead of borrowing means the price you see is the price you pay."],
        "faqs": [
            ("Where should I keep money for a savings goal?",
             "For goals within a few years, most people keep the money somewhere stable and accessible rather than in "
             "the stock market, because a market drop right before you need it could delay your goal."),
            ("Should I enter an expected return?",
             "Only if the money will actually be invested. For cash savings, leave it at 0%. For longer goals invested in "
             "a diversified portfolio, use a conservative figure, since returns aren't guaranteed."),
            ("What if I can't afford the monthly amount?",
             "Extend the deadline or lower the goal. Try different timelines above. Adding just a few months can bring "
             "the monthly amount down noticeably."),
            ("Does this include taxes?",
             "No. If your savings are invested, taxes on gains can reduce your growth slightly."),
        ],
        "sources": [("MyMoney.gov", "https://www.mymoney.gov/"),
                    ("Investor.gov: Introduction to investing", "https://www.investor.gov/introduction-investing")],
        "related": ["save-to-buy-calculator", "emergency-fund-calculator", "budget-calculator"],
        "js": "savings-goal.js",
    },
    {
        "slug": "inflation-calculator", "cat": "grow", "name": "Inflation",
        "card": "What money will be worth, and what things will cost, later.",
        "title": "Inflation Calculator: Future Value & Purchasing Power",
        "description": "See how inflation affects your money. Calculate what something will cost in the future and "
                       "how much purchasing power today's dollars will lose over time.",
        "h1": "Inflation Calculator",
        "lead": "See how rising prices change the value of money. Find out what today's price will be in the future, "
                "and how much today's dollars will actually buy, at the inflation rate you choose.",
        "how": ["Enter an amount of money or a price today.",
                "Choose how many years into the future.",
                "Set an average yearly inflation rate. The Federal Reserve's long-run target is 2%."],
        "formula": "<p>With an average inflation rate <strong>i</strong> over <strong>t</strong> years:</p>"
                   "<p class=\"formula\">Future cost = Amount × (1 + i)<sup>t</sup></p>"
                   "<p class=\"formula\">Future purchasing power = Amount ÷ (1 + i)<sup>t</sup></p>"
                   "<p>The first shows what the same goods will cost later. The second shows what today's cash, left "
                   "uninvested, will be worth in today's dollars.</p>",
        "tips": ["Cash left in a 0% account loses buying power every year inflation is positive.",
                 "Use inflation-adjusted numbers when planning long-term goals like retirement.",
                 "Series I savings bonds and TIPS are designed to keep pace with inflation.",
                 "Negotiate raises that at least match inflation to maintain your real income."],
        "faqs": [
            ("What is a normal inflation rate?",
             "The Federal Reserve targets 2% average inflation over the long run. Actual inflation varies. It has "
             "been much higher at times, such as in the early 1980s and 2022. Try a few rates to see the range."),
            ("How is inflation measured in the US?",
             "The most common measure is the Consumer Price Index (CPI), published monthly by the Bureau of Labor "
             "Statistics. It tracks the prices of a broad basket of goods and services."),
            ("How do I protect my money from inflation?",
             "Earning a return above the inflation rate preserves purchasing power. Common approaches include "
             "diversified long-term investments and real assets such as property or physical gold."),
            ("Why does my retirement plan need to consider inflation?",
             "Retirement can last decades. At 3% inflation, prices roughly double in about 24 years, so a fixed "
             "income buys about half as much by the end."),
        ],
        "sources": [("BLS: Consumer Price Index", "https://www.bls.gov/cpi/"),
                    ("Federal Reserve: Why does the Fed aim for 2% inflation?", "https://www.federalreserve.gov/faqs/economy_14400.htm")],
        "related": ["retirement-calculator", "investment-growth-calculator", "fire-calculator"],
        "js": "inflation.js",
    },
    {
        "slug": "budget-calculator", "cat": "plan", "name": "50/30/20 Budget",
        "card": "Split take-home pay into needs, wants and savings.",
        "title": "Budget Calculator: 50/30/20 Rule Monthly Budget",
        "description": "Build a simple monthly budget with the 50/30/20 rule. Split your take-home pay into needs, "
                       "wants and savings, and customize the percentages to fit your life.",
        "h1": "50/30/20 Budget Calculator",
        "lead": "Turn your take-home pay into a simple, balanced budget. The 50/30/20 rule gives you a starting split "
                "for needs, wants and savings, and you can adjust the percentages to fit your situation.",
        "how": ["Enter your take-home (after-tax) pay and choose monthly or yearly.",
                "Keep the default 50/30/20 split or adjust the percentages.",
                "Use the dollar amounts as monthly spending targets."],
        "formula": "<p>Monthly take-home pay × each percentage. By default <strong>50%</strong> goes to needs (housing, "
                   "utilities, groceries, insurance, minimum debt payments), <strong>30%</strong> to wants (dining, "
                   "entertainment, travel) and <strong>20%</strong> to savings and extra debt payments. The three "
                   "percentages should add up to 100%.</p>",
        "tips": ["If needs exceed 50%, trim wants first rather than cutting savings to zero.",
                 "Count extra debt payments beyond the minimum as part of your 20%.",
                 "Review your budget every few months or whenever your income changes.",
                 "Try 60/20/20 or 70/20/10 if you live in a high-cost area. The framework is flexible."],
        "faqs": [
            ("What is the 50/30/20 rule?",
             "A simple budgeting framework popularized by Senator Elizabeth Warren and Amelia Warren Tyagi in the book "
             "\"All Your Worth\": spend about 50% of after-tax income on needs, 30% on wants and 20% on savings and "
             "debt repayment."),
            ("Is it based on gross or net income?",
             "Net, meaning your take-home pay after taxes and deductions. If retirement contributions come out of "
             "your paycheck, you can count them toward the 20% savings bucket."),
            ("What counts as a need versus a want?",
             "Needs are expenses you must pay to live and work: rent or mortgage, utilities, groceries, insurance, "
             "transportation and minimum loan payments. Wants are everything else: streaming, dining out, vacations, "
             "upgrades."),
            ("What if 50/30/20 doesn't work for me?",
             "Change the percentages. The goal is to spend intentionally and save consistently, not to hit exact "
             "numbers. High-cost areas often need a larger needs share."),
        ],
        "sources": [("CFPB: Consumer tools", "https://www.consumerfinance.gov/consumer-tools/"),
                    ("MyMoney.gov", "https://www.mymoney.gov/")],
        "related": ["net-worth-calculator", "emergency-fund-calculator", "salary-to-hourly-calculator"],
        "js": "budget.js",
    },
    {
        "slug": "net-worth-calculator", "cat": "plan", "name": "Net Worth",
        "card": "Add up what you own and owe for a snapshot.",
        "title": "Net Worth Calculator: Assets Minus Liabilities",
        "description": "Calculate your net worth in minutes. Add up your assets and liabilities, including home, savings, "
                       "investments, mortgage and debts, to get a clear snapshot of your finances.",
        "h1": "Net Worth Calculator",
        "lead": "Add up everything you own and everything you owe to get a clear snapshot of your financial health. "
                "Tracking net worth over time is one of the best ways to see real progress.",
        "how": ["Enter the current value of your assets: cash, investments, retirement accounts, home and vehicles.",
                "Enter what you owe: mortgage, car loans, student loans and credit cards.",
                "Add extra rows for anything else, then check your net worth."],
        "formula": "<p class=\"formula\">Net worth = Total assets − Total liabilities</p><p>Use realistic market values "
                   "for things like your home and car (what they'd sell for today), and current payoff balances for debts.</p>",
        "tips": ["Recalculate every 3–6 months and watch the trend, not a single number.",
                 "A negative net worth is common early in a career or after school. It's a starting point.",
                 "Paying down debt and saving both raise net worth, and so does avoiding new debt.",
                 "Be conservative with car and home values so the snapshot stays realistic."],
        "faqs": [
            ("What is a good net worth?",
             "It depends on age, income and location. More useful than comparing with others is tracking whether "
             "yours grows each year. A popular rough benchmark is age × pre-tax income ÷ 10, but treat it as a loose guide."),
            ("Should I include my home?",
             "Yes. Include its current market value as an asset and the mortgage balance as a liability. The "
             "difference is your home equity."),
            ("Do retirement accounts count?",
             "Yes. 401(k)s, IRAs and similar accounts are assets. Some people also track a \"liquid\" net worth "
             "excluding retirement and home equity."),
            ("How often should I calculate net worth?",
             "Every few months is plenty. Values like investments move daily, so the long-term trend matters more "
             "than any single snapshot."),
        ],
        "sources": [("Federal Reserve: Survey of Consumer Finances", "https://www.federalreserve.gov/econres/scfindex.htm"),
                    ("MyMoney.gov", "https://www.mymoney.gov/")],
        "related": ["budget-calculator", "retirement-calculator", "emergency-fund-calculator"],
        "js": "net-worth.js",
    },
    {
        "slug": "salary-to-hourly-calculator", "cat": "plan", "name": "Salary to Hourly",
        "card": "Convert salary to hourly, weekly and monthly pay.",
        "title": "Salary to Hourly Calculator: Convert Your Pay",
        "description": "Convert a yearly salary to an hourly wage, or hourly pay to annual salary. See your pay per "
                       "hour, day, week, two weeks, month and year based on your actual hours.",
        "h1": "Salary to Hourly Calculator",
        "lead": "Convert any pay rate into every other: hourly, daily, weekly, biweekly, monthly and yearly. Set your "
                "real hours and weeks worked for an accurate comparison between job offers.",
        "how": ["Enter your pay and choose whether it's per hour, week, month or year.",
                "Set how many hours you work per week and weeks per year.",
                "Read your pay at every other interval in the results."],
        "formula": "<p>Everything is converted through an annual figure. A full-time schedule of 40 hours × 52 weeks is "
                   "<strong>2,080 hours</strong> a year, so:</p><p class=\"formula\">Hourly = Annual salary ÷ (hours per week × weeks per year)</p>"
                   "<p>Daily pay assumes a 5-day week, biweekly is annual ÷ 26 and monthly is annual ÷ 12.</p>",
        "tips": ["A quick rule: $1 per hour ≈ $2,000 per year for full-time work.",
                 "Compare total compensation, including benefits, 401(k) match and paid time off, not just salary.",
                 "Salaried roles with long hours can have a lower effective hourly rate than they appear.",
                 "These are gross (pre-tax) figures. Take-home pay will be lower after taxes and deductions."],
        "faqs": [
            ("How do I convert salary to hourly?",
             "Divide your annual salary by the hours you work in a year. For a standard 40-hour week that's 2,080 hours, "
             "so a $60,000 salary is about $28.85 per hour."),
            ("How many work hours are in a year?",
             "40 hours × 52 weeks = 2,080 hours. If you get two weeks of unpaid time off, it's 40 × 50 = 2,000 hours. "
             "Adjust the weeks per year above to match."),
            ("Is this before or after taxes?",
             "Before taxes (gross pay). Federal, state and payroll taxes, plus deductions like health insurance and "
             "retirement contributions, reduce your take-home pay."),
            ("How much is $20 an hour per year?",
             "At 40 hours a week for 52 weeks, $20 an hour is $41,600 a year before taxes, about $3,467 a month."),
        ],
        "sources": [("U.S. Department of Labor: Wages", "https://www.dol.gov/general/topic/wages"),
                    ("BLS: Occupational employment and wages", "https://www.bls.gov/oes/")],
        "related": ["budget-calculator", "inflation-calculator", "retirement-calculator"],
        "js": "salary-hourly.js",
    },
    {
        "slug": "emergency-fund-calculator", "cat": "plan", "name": "Emergency Fund",
        "card": "Your cash-cushion target and progress.",
        "title": "Emergency Fund Calculator: How Much Should You Save?",
        "description": "Calculate how big your emergency fund should be based on your essential monthly expenses, "
                       "and track your progress toward a 3- to 6-month savings cushion.",
        "h1": "Emergency Fund Calculator",
        "lead": "Work out how much cash to keep for emergencies like a job loss, car repair or medical bill, based on "
                "your essential monthly costs, and see how close you are to your target.",
        "how": ["Add up your essential monthly expenses: housing, utilities, food, insurance, transportation and minimum debt payments.",
                "Choose how many months of expenses you want covered.",
                "Enter what you've already saved to see your progress."],
        "formula": "<p class=\"formula\">Target = Essential monthly expenses × Months of coverage</p><p>Use essential costs "
                   "only (what you'd still need to pay if your income stopped), not your full current spending.</p>",
        "tips": ["Start with a mini-goal of $1,000 or one month of expenses, then build up.",
                 "Keep the fund in a separate account so it's easy to reach but not mixed with everyday spending.",
                 "Aim for more months if your income is irregular or you're the only earner.",
                 "Refill the fund right after you use it."],
        "faqs": [
            ("How much should I have in my emergency fund?",
             "A common guideline is three to six months of essential expenses. Consider more if you're self-employed, "
             "work in a volatile industry, have dependents, or are a single-income household."),
            ("Where should I keep my emergency fund?",
             "Somewhere safe and easy to reach, kept separate from your everyday spending money. Avoid investing it "
             "in stocks, since you may need it when markets are down."),
            ("Should I pay off debt or build an emergency fund first?",
             "Many people build a small starter fund first, so an unexpected bill doesn't push them into borrowing, "
             "then work on clearing any debt, then finish the full fund."),
            ("What counts as an emergency?",
             "Unexpected, necessary expenses: job loss, medical bills, urgent car or home repairs. Planned costs like "
             "vacations or holiday gifts should have their own savings goal."),
        ],
        "sources": [("CFPB: An essential guide to building an emergency fund", "https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/"),
                    ("MyMoney.gov", "https://www.mymoney.gov/")],
        "related": ["savings-goal-calculator", "budget-calculator", "net-worth-calculator"],
        "js": "emergency-fund.js",
    },
    {
        "slug": "save-to-buy-calculator", "cat": "plan", "name": "Save to Buy", "added": "2026-09-22",
        "card": "How long to save up and pay cash instead of borrowing.",
        "title": "Save-to-Buy Calculator: How Long to Save and Pay Cash",
        "description": "Find out how long it takes to save up and buy a car, home or other big purchase with cash. "
                       "Includes what you've saved, your monthly savings and rising prices.",
        "h1": "Save-to-Buy Calculator",
        "lead": "Plan to buy it outright. Enter the price and what you can set aside each month to see exactly when "
                "you'll have enough, even if the price rises while you save.",
        "how": ["Enter the price of what you want to buy and how much you've already saved.",
                "Add how much you can set aside each month.",
                "Set how fast the price tends to rise each year. Use 0% if it stays the same.",
                "Optionally add an expected return if you'll invest the savings. Leave it at 0% for cash."],
        "formula": "<p>The calculator runs month by month. Each month your savings grow by the monthly return (if any) "
                   "and your monthly amount is added, while the price rises by the yearly price increase spread across "
                   "the months:</p><p class=\"formula\">Savings<sub>m</sub> = Savings<sub>m−1</sub> × (1 + i) + Monthly</p>"
                   "<p class=\"formula\">Price<sub>m</sub> = Price × (1 + g)<sup>m ÷ 12</sup></p>"
                   "<p>The first month when your savings reach the price is when you can buy.</p>",
        "tips": ["Paying cash means the sticker price is the whole price: no extra charges and no monthly bill afterwards.",
                 "Set up an automatic transfer on payday so your monthly amount is saved first.",
                 "A slightly older or smaller model can cut months or years off your timeline.",
                 "Keep your emergency fund separate so a surprise bill doesn't reset your progress."],
        "faqs": [
            ("Is it better to save up or finance a purchase?",
             "Saving up means you pay only the price and own the item outright from day one, with no ongoing "
             "payments. The trade-off is waiting. This calculator shows exactly how long that wait is."),
            ("What if the price goes up while I save?",
             "Enter a yearly price increase. The calculator raises the target a little every month so your date "
             "reflects what the item will cost when you're ready to buy."),
            ("How can I reach my goal sooner?",
             "Increase your monthly amount, put windfalls like bonuses toward the goal, sell things you no longer "
             "need, or choose a less expensive option. Try different numbers above to see the effect."),
            ("Where should I keep the money while I save?",
             "For purchases within a few years, somewhere stable and easy to reach is usually best, since investments "
             "can lose value right when you need the money."),
        ],
        "sources": [("MyMoney.gov", "https://www.mymoney.gov/"),
                    ("CFPB: Consumer tools", "https://www.consumerfinance.gov/consumer-tools/")],
        "related": ["savings-goal-calculator", "budget-calculator", "emergency-fund-calculator"],
        "js": "save-to-buy.js",
    },
    {
        "slug": "gold-silver-calculator", "cat": "grow", "name": "Gold & Silver Value", "added": "2026-09-22",
        "card": "What your gold, silver or platinum is worth by weight and purity.",
        "title": "Gold & Silver Value Calculator: Price by Weight & Karat",
        "description": "Free gold and silver calculator. Find the value of gold, silver or platinum by weight, unit "
                       "and purity (karat or fineness), plus the likely cost including a dealer premium.",
        "h1": "Gold & Silver Value Calculator",
        "lead": "Work out what your gold, silver or platinum is worth from its weight and purity. The calculator loads "
                "the latest spot price automatically and shows the metal value, the price per gram and what it would "
                "likely cost to buy from a dealer.",
        "how": ["Choose the metal and enter its weight in grams, troy ounces, kilograms or tola.",
                "Pick the purity: karat for gold jewelry (24K, 22K, 18K...) or fineness for bars and coins (.999, .925).",
                "The latest spot price per troy ounce loads automatically. Tap Refresh price for the newest quote.",
                "Optionally set a dealer premium to estimate what buying the same metal would cost."],
        "formula": "<p>Everything is converted to troy ounces of pure metal first:</p>"
                   "<p class=\"formula\">Pure troy oz = Weight in grams × Purity ÷ 31.1035</p>"
                   "<p class=\"formula\">Metal value = Pure troy oz × Spot price</p>"
                   "<p>Purity is the karat ÷ 24 for gold (22K = 91.67%) or the fineness for bullion (.999 = 99.9%). The "
                   "buying estimate adds the dealer premium: Value × (1 + premium).</p>",
        "tips": ["Precious metals are priced per troy ounce (31.1 grams), which is heavier than a regular ounce (28.35 grams).",
                 "Jewelry usually sells for less than its metal value because buyers pay for the metal, not the design.",
                 "Compare the total price per ounce, including premium and shipping, across several dealers.",
                 "Be wary of sellers who pressure you, promise quick profits or discourage you from taking delivery."],
        "faqs": [
            ("What is a troy ounce?",
             "The standard unit for precious metals. One troy ounce equals 31.1035 grams, about 10% more than the "
             "everyday (avoirdupois) ounce of 28.35 grams."),
            ("What does karat mean?",
             "Karat measures gold purity out of 24 parts. 24K is essentially pure gold, 22K is 22/24 or 91.67% gold, "
             "18K is 75% and 14K is about 58.3%. The rest is other metals that add strength or color."),
            ("Why do dealers charge more than the spot price?",
             "Spot is the price for large wholesale amounts. Coins and small bars carry a premium for minting, "
             "handling and the dealer's margin. Enter a premium to estimate your real cost."),
            ("Is the metal value what I'll get when I sell?",
             "Usually not quite. Buyers typically pay somewhat below spot, especially for jewelry or scrap, so treat "
             "the metal value as the upper end of what you might receive."),
            ("Is the spot price live?",
             "Yes. When you open the calculator it loads the latest spot price for the metal you choose and shows "
             "when it was last updated. Prices move throughout the day, so tap Refresh price to get the newest quote."),
        ],
        "sources": [("CFTC: Precious metals fraud advisory", "https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/fraudadv_preciousmetals.html"),
                    ("NIST: Units of mass", "https://www.nist.gov/pml/owm/si-units-mass")],
        "related": ["inflation-calculator", "investment-growth-calculator", "net-worth-calculator"],
        "js": "gold-silver.js",
    },
    {
        "slug": "cost-of-waiting-calculator", "cat": "grow", "name": "Cost of Waiting", "added": "2026-09-22",
        "card": "What putting off investing could cost you.",
        "title": "Cost of Waiting Calculator: What Delaying Investing Costs",
        "description": "See how much delaying investing could cost you. Compare starting today with starting later, "
                       "and find the monthly amount you'd need to catch up.",
        "h1": "Cost of Waiting Calculator",
        "lead": "Every year you wait gives your money less time to grow. Compare investing the same amount starting "
                "today with starting a few years from now, and see what it would take to catch up.",
        "how": ["Enter how much you can invest each month.",
                "Add the average yearly return you expect.",
                "Enter how many years until you'll need the money, for example until retirement.",
                "Choose how many years you might wait before starting."],
        "formula": "<p>Both scenarios use the future value of regular monthly investments:</p>"
                   "<p class=\"formula\">FV = M × [(1 + i)<sup>n</sup> − 1] ÷ i</p>"
                   "<p>where <strong>M</strong> is the monthly amount, <strong>i</strong> the monthly return and "
                   "<strong>n</strong> the number of months invested. Waiting shortens <strong>n</strong>. The catch-up "
                   "amount is the monthly investment that reaches the start-now balance in the shorter time.</p>",
        "tips": ["The earliest dollars you invest have the most time to grow, so small amounts started early can beat larger amounts started late.",
                 "If you can't invest much today, start with something and increase it with every raise.",
                 "Automate your monthly investment so waiting never becomes the default.",
                 "Returns aren't guaranteed. Use a conservative figure for planning."],
        "faqs": [
            ("Why does waiting cost so much?",
             "Growth builds on itself. Money invested early has more years for its gains to produce further gains, "
             "so the last years of a long investment period often add the most."),
            ("Is it ever sensible to wait?",
             "Building an emergency fund and clearing any debt first are common reasons to hold off. Waiting to "
             "'time the market' is harder, because no one can reliably predict short-term moves."),
            ("What does the catch-up amount mean?",
             "It's how much you'd need to invest each month after waiting to end up with the same balance as starting "
             "today. It's usually much more than the original monthly amount."),
            ("What return should I use?",
             "For a long-term diversified portfolio many people plan with 5–7% a year. Try a few rates to see a range."),
        ],
        "sources": [("Investor.gov: Introduction to investing", "https://www.investor.gov/introduction-investing"),
                    ("Investor.gov: Rule of 72", "https://www.investor.gov/introduction-investing/investing-basics/glossary/rule-72")],
        "related": ["investment-growth-calculator", "retirement-calculator", "fire-calculator"],
        "js": "cost-of-waiting.js",
    },
    {
        "slug": "fire-calculator", "cat": "retire", "name": "FIRE (Early Retirement)", "added": "2026-09-22",
        "card": "Your FIRE number and when you could retire early.",
        "title": "FIRE Calculator: When Can You Retire Early?",
        "description": "Free FIRE calculator. Find your financial independence number from your spending and see how "
                       "many years until you could retire early based on your savings and investment return.",
        "h1": "FIRE Calculator",
        "lead": "FIRE means Financial Independence, Retire Early. Find the portfolio size that could cover your yearly "
                "spending, then see how many years of saving and investing it takes to get there.",
        "how": ["Enter your current age, yearly spending and how much you already have invested.",
                "Add how much you save and invest each year.",
                "Set an expected return after inflation. Many planners use 4–5%.",
                "Choose a withdrawal rate. 4% is common; early retirees often choose 3–3.5% for a longer retirement."],
        "formula": "<p class=\"formula\">FIRE number = Yearly spending ÷ Withdrawal rate</p>"
                   "<p>At a 4% withdrawal rate that's 25 times your yearly spending. Each year your portfolio grows by the "
                   "expected real (after-inflation) return and your yearly savings are added, until it reaches the "
                   "FIRE number. Using a real return keeps everything in today's dollars.</p>",
        "tips": ["Your spending matters twice: lower spending means both a smaller FIRE number and more to invest each year.",
                 "Raising your savings rate usually shortens the timeline more than chasing a higher return.",
                 "A lower withdrawal rate (3–3.5%) adds a safety margin for retirements that may last 40+ years.",
                 "Plan for health coverage and irregular costs before leaving full-time work."],
        "faqs": [
            ("What is my FIRE number?",
             "It's the amount invested that could support your yearly spending indefinitely under your withdrawal "
             "rate. At 4%, it's 25 times your yearly spending; at 3.5% it's about 28.6 times."),
            ("Why use a real return?",
             "A real return is your expected return minus inflation. Using it keeps your FIRE number and spending in "
             "today's dollars, so the result is easier to picture."),
            ("Is the 4% rule safe for early retirement?",
             "It was based on retirements of about 30 years. Early retirements can last much longer, so many people "
             "use 3–3.5% or stay flexible, spending less after bad market years."),
            ("What are Lean FIRE and Fat FIRE?",
             "Lean FIRE means retiring on a modest budget; Fat FIRE means a larger one. Try different spending levels "
             "above to see how much each changes your timeline."),
        ],
        "sources": [("Investor.gov: Is my money going to run out in retirement?", "https://www.investor.gov/additional-resources/spotlight/directors-take/my-money-going-run-out-retirement"),
                    ("FINRA: Managing your retirement portfolio", "https://www.finra.org/investors/learn-to-invest/types-investments/retirement/managing-retirement-income/managing-your-retirement-portfolio")],
        "related": ["retirement-income-calculator", "retirement-calculator", "cost-of-waiting-calculator"],
        "js": "fire.js",
    },
    {
        "slug": "retirement-income-calculator", "cat": "retire", "name": "Retirement Income", "added": "2026-09-22",
        "card": "How long your savings will last, and how much you can withdraw.",
        "title": "Retirement Income Calculator: How Long Will Savings Last?",
        "description": "See how long your retirement savings will last with monthly withdrawals that rise with "
                       "inflation, and how much you could withdraw each month to make them last.",
        "h1": "Retirement Income Calculator",
        "lead": "Find out how long your nest egg could last. Enter your savings, how much you plan to withdraw each "
                "month and your expected return, and see when the money would run out, or how much you can safely take.",
        "how": ["Enter your savings at retirement.",
                "Add how much you plan to withdraw each month.",
                "Set your expected yearly return and inflation. Withdrawals rise with inflation every year.",
                "Choose how many years you want the money to last to see a sustainable monthly amount."],
        "formula": "<p>The calculator runs month by month: the balance grows by the monthly return, then your withdrawal "
                   "is taken out. Once a year the withdrawal rises by inflation. It counts how many months pass before "
                   "the balance reaches zero.</p><p>The sustainable amount is the starting monthly withdrawal that "
                   "brings the balance to zero exactly at the end of the period you choose.</p>",
        "tips": ["Withdrawing about 3–5% of your savings in the first year is the range many experts suggest.",
                 "Being flexible, spending a little less after a bad market year, helps savings last longer.",
                 "Add Social Security and other income before deciding how much you need to withdraw.",
                 "Plan for a long life. Retirement can last 30 years or more."],
        "faqs": [
            ("How long will my retirement savings last?",
             "It depends on your balance, how much you withdraw, your return and inflation. The calculator combines "
             "all four; try higher inflation or lower returns to stress-test your plan."),
            ("What is a safe withdrawal rate?",
             "Many experts suggest starting in the 3–5% range of your savings in the first year and adjusting for "
             "inflation after that. Withdrawing conservatively early in retirement leaves more room for bad years."),
            ("Why do withdrawals rise each year?",
             "Prices rise over time, so the same lifestyle costs more each year. Raising withdrawals with inflation "
             "keeps your spending power steady."),
            ("Does this include Social Security?",
             "No. Enter only what you'll take from savings. Subtract Social Security, pensions or other income from "
             "your monthly spending first."),
        ],
        "sources": [("Investor.gov: Is my money going to run out in retirement?", "https://www.investor.gov/additional-resources/spotlight/directors-take/my-money-going-run-out-retirement"),
                    ("SSA: Retirement benefits", "https://www.ssa.gov/benefits/retirement/")],
        "related": ["fire-calculator", "retirement-calculator", "401k-calculator"],
        "js": "retirement-income.js",
    },
]

# Partner offers: which offer group each calculator shows (groups are filled in assets/js/config.js),
# and a headline that quotes the visitor's own result. {element-id} is replaced with that element's text.
# POLICY: offers must never promote interest: no interest-based loans, mortgages or refinancing, credit cards,
# balance transfers, debt consolidation loans, interest-bearing savings/CDs, conventional insurance,
# gambling or speculative trading. Groups:
#   budget  - budgeting and debt-freedom tools that don't sell credit
#   invest  - ethical, interest-free investing and physical gold
OFFERS = {
    "investment-growth-calculator": ("invest", "Your money could grow to {compound-result}. Ethical investing lets it grow without interest-bearing bonds."),
    "retirement-calculator": ("invest", "You're on track for about {retirement-result}. Ethical, interest-free funds let you save for retirement in line with your values."),
    "401k-calculator": ("invest", "Your 401(k) could reach {k-result}. Ethical funds and IRAs let you invest without interest-bearing assets."),
    "inflation-calculator": ("invest", "Inflation turns today's money into {in-power} of buying power. Physical gold and ethical investing are common ways to protect it."),
    "savings-goal-calculator": ("budget", "You need to set aside {sg-monthly} a month. A budget that automates it makes the goal stick."),
    "budget-calculator": ("budget", "Your savings target is {budget-savings} a month. A budgeting app makes it automatic."),
    "net-worth-calculator": ("budget", "Your net worth is {net-worth}. Tracking it automatically shows your progress month by month."),
    "salary-to-hourly-calculator": ("budget", "You earn about {sh-hourly} an hour. A budget app shows where every paycheck goes."),
    "emergency-fund-calculator": ("budget", "Your target is {emergency-result}. A budget helps you build it steadily without borrowing."),
    "save-to-buy-calculator": ("budget", "You could buy it with cash in {sb-time}. A budget helps you hit your monthly target."),
    "gold-silver-calculator": ("invest", "Your metal is worth about {gs-value} at today's spot price. Compare dealer prices before you buy."),
    "cost-of-waiting-calculator": ("invest", "Waiting would cost you about {cw-cost}. Ethical investing lets you start today."),
    "fire-calculator": ("invest", "You could reach financial independence in {fi-years}. Ethical, low-cost investing helps you get there."),
    "retirement-income-calculator": ("invest", "At this pace your savings last {ri-lasts}. Ethical investing keeps your nest egg working."),
}

POPULAR = ["401k-calculator", "investment-growth-calculator", "fire-calculator",
           "retirement-calculator", "gold-silver-calculator", "budget-calculator"]

HOME_FAQS = [
    ("Are these calculators free?",
     "Yes. Every calculator on CalcMyFin is free to use with no sign-up, no email and no limits."),
    ("Is my information private?",
     "Your numbers never leave your device. All calculations run in your browser, and we don't collect or store "
     "the values you enter."),
    ("How accurate are the results?",
     "Each calculator uses standard, published formulas, and we show the math on every page. Results are "
     "educational estimates: lenders, insurers and tax rules can change the real numbers."),
    ("Is this financial advice?",
     "No. CalcMyFin provides educational tools to help you explore scenarios. For decisions about insurance, "
     "taxes, investing or major debts, consider talking with a qualified professional."),
]
