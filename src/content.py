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
    ("grow", "Saving & Investing", "Watch money grow and plan how to reach your goals."),
    ("plan", "Budget & Planning", "Budgets, net worth and what your paycheck is really worth."),
    ("protect", "Safety Net", "Emergency savings and life insurance coverage."),
]

# Each calculator: slug, category, name (short), title (<title>), description (meta),
# h1, lead, how (steps), formula (html), example (callable -> html, filled by build.py),
# tips, faqs [(q, a)], sources [(label, url)], related [slugs], js
CALCULATORS = [
    {
        "slug": "compound-interest-calculator", "cat": "grow", "name": "Compound Interest",
        "card": "How savings and investments grow over time.",
        "title": "Compound Interest Calculator: See Your Money Grow",
        "description": "Free compound interest calculator with monthly contributions. See how your savings or "
                       "investments grow over time and how much comes from interest versus deposits.",
        "h1": "Compound Interest Calculator",
        "lead": "See how a starting balance and regular monthly deposits grow with compound interest. The chart shows "
                "how much of your future balance comes from your own contributions and how much from growth.",
        "how": ["Enter your starting amount and how much you'll add each month.",
                "Add an expected annual interest rate or return.",
                "Choose how many years and how often interest compounds."],
        "formula": "<p>For a starting principal <strong>P</strong>, annual rate <strong>r</strong> compounded <strong>n</strong> "
                   "times per year for <strong>t</strong> years:</p>"
                   "<p class=\"formula\">A = P(1 + r/n)<sup>nt</sup></p>"
                   "<p>Monthly contributions are added each compounding period and grow the same way. The calculator "
                   "steps through every period so the result matches how a savings or investment account actually grows.</p>",
        "tips": ["Time matters more than amount. Starting 10 years earlier can double your final balance.",
                 "The Rule of 72: divide 72 by your rate to estimate how many years it takes money to double.",
                 "Automate monthly deposits so saving happens before spending.",
                 "Investment returns vary year to year. Use a conservative rate for planning."],
        "faqs": [
            ("What is compound interest?",
             "Interest earned on both your original money and the interest it has already earned. Over long periods "
             "this snowball effect means growth accelerates, which is why starting early is so powerful."),
            ("What rate should I use?",
             "For savings accounts, use the account's APY. For long-term stock investing, many people plan with a "
             "conservative 5–7% average, but returns are never guaranteed and can be negative in any given year."),
            ("Does compounding frequency matter?",
             "Somewhat. Daily compounding earns slightly more than monthly or yearly at the same rate, but the "
             "difference is small compared with the effect of your rate, deposits and time."),
            ("How is this different from simple interest?",
             "Simple interest is paid only on the original principal. Compound interest pays interest on interest, "
             "so balances grow faster, and the gap widens every year."),
        ],
        "sources": [("Investor.gov: Compound interest", "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator"),
                    ("FDIC: Deposit insurance", "https://www.fdic.gov/resources/deposit-insurance/")],
        "related": ["savings-goal-calculator", "retirement-calculator", "inflation-calculator"],
        "js": "compound-interest.js",
    },
    {
        "slug": "retirement-calculator", "cat": "grow", "name": "Retirement",
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
        "related": ["401k-calculator", "compound-interest-calculator", "inflation-calculator"],
        "js": "retirement.js",
    },
    {
        "slug": "401k-calculator", "cat": "grow", "name": "401(k)", "added": "2026-09-22",
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
                    ("Investor.gov: Compound interest calculator", "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator")],
        "related": ["retirement-calculator", "compound-interest-calculator", "salary-to-hourly-calculator"],
        "js": "401k.js",
    },
    {
        "slug": "savings-goal-calculator", "cat": "grow", "name": "Savings Goal",
        "card": "How much to save each month to hit a goal.",
        "title": "Savings Goal Calculator: How Much to Save Each Month",
        "description": "Calculate how much you need to save each month to reach a savings goal by a target date. "
                       "Includes your current savings and interest (APY) earned along the way.",
        "h1": "Savings Goal Calculator",
        "lead": "Pick a goal, like a down payment, a car or a trip, and a deadline. We'll work out exactly how much to "
                "save each month, counting what you already have and the interest your savings will earn.",
        "how": ["Enter your savings goal and how much you've saved so far.",
                "Choose how many years (and months) until you need the money.",
                "Add the APY your savings account pays."],
        "formula": "<p>The APY is converted to a monthly rate <strong>i</strong> = (1 + APY)<sup>1/12</sup> − 1. Over "
                   "<strong>n</strong> months your current savings grow to S(1 + i)<sup>n</sup>, and the required monthly "
                   "deposit is:</p><p class=\"formula\">PMT = [Goal − S(1 + i)<sup>n</sup>] × i ÷ [(1 + i)<sup>n</sup> − 1]</p>",
        "tips": ["Keep short-term goals in an FDIC-insured high-yield savings account, not in stocks.",
                 "Automate a transfer on payday so the money is saved before you can spend it.",
                 "Break big goals into monthly milestones to track progress.",
                 "Online banks often pay much higher APYs than traditional savings accounts."],
        "faqs": [
            ("Where should I keep money for a savings goal?",
             "For goals within about five years, a high-yield savings account, money market account or CDs are "
             "typical because the money stays safe and accessible. Deposits at FDIC-insured banks are protected up "
             "to $250,000 per depositor, per bank, per ownership category."),
            ("What's the difference between APY and APR?",
             "APY (annual percentage yield) includes the effect of compounding, so it shows what you'll actually earn "
             "in a year. Savings accounts advertise APY, which is what this calculator uses."),
            ("What if I can't afford the monthly amount?",
             "Extend the deadline, lower the goal, or find a higher-yield account. Try different timelines above. "
             "Adding just a few months can bring the payment down noticeably."),
            ("Does this account for taxes on interest?",
             "No. Interest from savings accounts is generally taxable as ordinary income, so your after-tax growth "
             "will be a little lower."),
        ],
        "sources": [("FDIC: Understanding deposit insurance", "https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance/"),
                    ("Investor.gov: Saving and investing", "https://www.investor.gov/introduction-investing")],
        "related": ["compound-interest-calculator", "emergency-fund-calculator", "budget-calculator"],
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
             "Earning a return above the inflation rate preserves purchasing power. Common tools include "
             "high-yield savings (short term), diversified investments (long term), I bonds and TIPS."),
            ("Why does my retirement plan need to consider inflation?",
             "Retirement can last decades. At 3% inflation, prices roughly double in about 24 years, so a fixed "
             "income buys about half as much by the end."),
        ],
        "sources": [("BLS: Consumer Price Index", "https://www.bls.gov/cpi/"),
                    ("Federal Reserve: Why does the Fed aim for 2% inflation?", "https://www.federalreserve.gov/faqs/economy_14400.htm")],
        "related": ["retirement-calculator", "compound-interest-calculator", "salary-to-hourly-calculator"],
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
        "slug": "emergency-fund-calculator", "cat": "protect", "name": "Emergency Fund",
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
                 "Keep the fund in a separate, FDIC-insured high-yield savings account so it earns interest but stays accessible.",
                 "Aim for more months if your income is irregular or you're the only earner.",
                 "Refill the fund right after you use it."],
        "faqs": [
            ("How much should I have in my emergency fund?",
             "A common guideline is three to six months of essential expenses. Consider more if you're self-employed, "
             "work in a volatile industry, have dependents, or are a single-income household."),
            ("Where should I keep my emergency fund?",
             "Somewhere safe and easy to reach, like a high-yield savings account or money market account at an "
             "FDIC-insured bank. Avoid investing it in stocks, since you may need it when markets are down."),
            ("Should I pay off debt or build an emergency fund first?",
             "Many people build a small starter fund first so an unexpected bill doesn't go on a credit card, then "
             "focus on high-interest debt, then finish the full fund."),
            ("What counts as an emergency?",
             "Unexpected, necessary expenses: job loss, medical bills, urgent car or home repairs. Planned costs like "
             "vacations or holiday gifts should have their own savings goal."),
        ],
        "sources": [("CFPB: An essential guide to building an emergency fund", "https://www.consumerfinance.gov/an-essential-guide-to-building-an-emergency-fund/"),
                    ("FDIC: Deposit insurance", "https://www.fdic.gov/resources/deposit-insurance/")],
        "related": ["savings-goal-calculator", "budget-calculator", "life-insurance-calculator"],
        "js": "emergency-fund.js",
    },
    {
        "slug": "life-insurance-calculator", "cat": "protect", "name": "Life Insurance",
        "card": "Estimate how much coverage your family needs.",
        "title": "Life Insurance Calculator: How Much Coverage Do I Need?",
        "description": "Estimate how much life insurance you need based on income replacement, debts, future costs like "
                       "college, and the savings and coverage you already have.",
        "h1": "Life Insurance Calculator",
        "lead": "Estimate how much life insurance would protect the people who depend on you. We combine income "
                "replacement, debts and future costs, then subtract the savings and coverage you already have.",
        "how": ["Enter your annual income and how many years of income you'd want to replace.",
                "Add debts you'd want paid off, such as your mortgage and loans.",
                "Include future costs like college or final expenses.",
                "Subtract savings and existing life insurance."],
        "formula": "<p class=\"formula\">Coverage = Income × Years + Debts + Future costs − Existing assets</p><p>This "
                   "income-replacement approach is similar to the popular DIME method (Debt, Income, Mortgage, Education). "
                   "Many advisers suggest roughly 10–15 times income as a quick starting point.</p>",
        "tips": ["Term life insurance is usually the most affordable way to get a large amount of coverage.",
                 "Match the term length to your longest obligation, such as your mortgage or kids reaching adulthood.",
                 "Workplace coverage is often limited and may not follow you if you change jobs.",
                 "Review your coverage after major life events: marriage, a new child, a new home."],
        "faqs": [
            ("How much life insurance do I need?",
             "Enough to replace your income for the years your family would need it, pay off major debts, and cover "
             "future goals like college, minus what your savings and existing policies already cover. The calculator "
             "above adds this up for you."),
            ("Term or whole life insurance?",
             "Term life covers a set period (such as 20 or 30 years) and is much cheaper per dollar of coverage. Whole "
             "life lasts your entire life and builds cash value, but costs significantly more. Most families' needs "
             "are met with term coverage."),
            ("Do I need life insurance if I'm single?",
             "Often not, unless someone depends on your income, you co-signed debts, or you want to cover final "
             "expenses. Needs grow with a partner, children or a mortgage."),
            ("Is workplace life insurance enough?",
             "Employer coverage is usually one or two times salary, which is typically far less than a family needs, "
             "and it may end when you leave the job."),
        ],
        "sources": [("NAIC: Life insurance buyer's guide", "https://content.naic.org/consumer/life-insurance.htm"),
                    ("Insurance Information Institute: Life insurance", "https://www.iii.org/insurance-basics/life-insurance")],
        "related": ["emergency-fund-calculator", "net-worth-calculator", "retirement-calculator"],
        "js": "life-insurance.js",
    },
]

# Partner offers: which offer group each calculator shows (groups are filled in assets/js/config.js),
# and a headline that quotes the visitor's own result. {element-id} is replaced with that element's text.
# POLICY: offers must never promote interest: no interest-based loans, mortgages or refinancing, credit cards,
# balance transfers, debt consolidation loans, interest-bearing savings/CDs, conventional insurance,
# gambling or speculative trading. Groups:
#   budget  - budgeting and debt-freedom tools that don't sell credit
#   invest  - ethical, interest-free investing and physical gold
#   protect - cooperative protection plans and non-credit protection services
OFFERS = {
    "compound-interest-calculator": ("invest", "Your money could grow to {compound-result}. Ethical investing lets it grow without interest-bearing bonds."),
    "retirement-calculator": ("invest", "You're on track for about {retirement-result}. Ethical, interest-free funds let you save for retirement in line with your values."),
    "401k-calculator": ("invest", "Your 401(k) could reach {k-result}. Ethical funds and IRAs let you invest without interest-bearing assets."),
    "inflation-calculator": ("invest", "Inflation turns today's money into {in-power} of buying power. Physical gold and ethical investing are common ways to protect it."),
    "savings-goal-calculator": ("budget", "You need to set aside {sg-monthly} a month. A budget that automates it makes the goal stick."),
    "budget-calculator": ("budget", "Your savings target is {budget-savings} a month. A budgeting app makes it automatic."),
    "net-worth-calculator": ("budget", "Your net worth is {net-worth}. Tracking it automatically shows your progress month by month."),
    "salary-to-hourly-calculator": ("budget", "You earn about {sh-hourly} an hour. A budget app shows where every paycheck goes."),
    "emergency-fund-calculator": ("budget", "Your target is {emergency-result}. A budget helps you build it steadily without borrowing."),
    "life-insurance-calculator": ("protect", "You may need about {life-result} of coverage. Cooperative protection plans are an alternative to conventional insurance."),
}

POPULAR = ["401k-calculator", "compound-interest-calculator", "retirement-calculator",
           "savings-goal-calculator", "budget-calculator", "salary-to-hourly-calculator"]

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
