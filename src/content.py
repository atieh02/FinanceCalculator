"""Site-wide settings and all page copy. Edit text here, then run `python src/build.py`."""
import os

SITE = {
    "name": "CalcMyFin",
    "domain": "calcmyfin.com",
    # Canonical origin (override with the BASE_URL env var for local testing only)
    "base_url": os.environ.get("BASE_URL", "https://calcmyfin.com").rstrip("/"),
    "tagline": "Free financial calculators that show their math",
    "description": "Free, private personal finance calculators for mortgages, loans, debt payoff, savings, "
                   "retirement and budgeting. No sign-up, clear formulas, instant results.",
    "email": "hello@calcmyfin.com",
    "updated": "2026-09-22",
    "updated_human": "September 2026",
    "locale": "en_US",
    # IndexNow (Bing, Yandex, etc.): the key file /<key>.txt is written by build.py; run src/indexnow.py after publishing
    "indexnow_key": "8e6c086f06f5a4e9db937d4b66a0c756",
}

CATEGORIES = [
    ("home", "Home & Mortgage", "Payments, affordability and the real cost of owning a home."),
    ("debt", "Loans & Debt", "Loan payments, payoff plans and what interest really costs."),
    ("grow", "Saving & Investing", "Watch money grow and plan how to reach your goals."),
    ("plan", "Budget & Income", "Budgets, net worth and what your paycheck is really worth."),
    ("protect", "Safety Net", "Emergency savings and life insurance coverage."),
]

# Each calculator: slug, category, name (short), title (<title>), description (meta),
# h1, lead, how (steps), formula (html), example (callable -> html, filled by build.py),
# tips, faqs [(q, a)], sources [(label, url)], related [slugs], js
CALCULATORS = [
    {
        "slug": "mortgage-calculator", "cat": "home", "name": "Mortgage",
        "card": "Monthly payment with taxes, insurance, HOA and PMI.",
        "title": "Mortgage Calculator: Monthly Payment With Taxes & PMI",
        "description": "Free mortgage calculator. Estimate your monthly payment including principal, interest, "
                       "property tax, homeowners insurance, HOA and PMI, plus total interest over the loan.",
        "h1": "Mortgage Calculator",
        "lead": "Estimate your full monthly mortgage payment, not just principal and interest. Add property "
                "taxes, homeowners insurance, HOA dues and PMI to see what owning the home will really cost each month.",
        "how": ["Enter the home price and your down payment.",
                "Add the interest rate and loan term (30 and 15 years are the most common).",
                "Fill in yearly property tax and homeowners insurance. Your listing or a local lender can give estimates.",
                "Add monthly HOA dues and a PMI rate if your down payment is under 20%."],
        "formula": "<p>Principal and interest use the standard fixed-rate amortization formula:</p>"
                   "<p class=\"formula\">M = P × r(1 + r)<sup>n</sup> ÷ [(1 + r)<sup>n</sup> − 1]</p>"
                   "<p>where <strong>P</strong> is the loan amount (home price minus down payment), <strong>r</strong> is the "
                   "monthly interest rate (annual rate ÷ 12) and <strong>n</strong> is the number of monthly payments. "
                   "The full estimate then adds property tax ÷ 12, insurance ÷ 12, monthly HOA dues and, when the down "
                   "payment is below 20%, PMI (loan amount × PMI rate ÷ 12).</p>",
        "tips": ["A 15-year loan has a higher monthly payment but usually costs far less interest overall.",
                 "Putting 20% down on a conventional loan avoids PMI entirely.",
                 "Compare loan estimates from several lenders. Even a small rate difference changes the total cost by thousands.",
                 "Budget for maintenance as well. Many owners set aside 1% or more of the home's value each year."],
        "faqs": [
            ("What is included in a monthly mortgage payment?",
             "Most payments include principal and interest, plus property taxes and homeowners insurance collected "
             "through an escrow account. Depending on the loan you may also pay private mortgage insurance (PMI) and, "
             "separately, HOA dues. This calculator shows all of them together so you can see the full monthly cost."),
            ("When does PMI go away?",
             "On a conventional loan you can usually ask your lender to cancel PMI once you reach 20% equity based on "
             "the original home value, and it is generally removed automatically when you reach 22% equity if your "
             "payments are current. FHA mortgage insurance follows different rules."),
            ("Is a 15-year or 30-year mortgage better?",
             "A 15-year mortgage builds equity faster and typically carries a lower rate, so it costs much less "
             "interest overall, but the monthly payment is higher. A 30-year loan keeps payments lower and more "
             "flexible. Try both terms above to compare the monthly payment and total interest."),
            ("How much house can I afford?",
             "Lenders often look at your debt-to-income ratio. Use our <a href=\"{home-affordability-calculator}\">home "
             "affordability calculator</a> to estimate a price range from your income, debts and down payment."),
            ("How accurate is this estimate?",
             "The principal-and-interest figure uses the exact standard formula. Taxes, insurance, PMI and HOA are "
             "based on the amounts you enter, and closing costs are not included. Your lender's Loan Estimate is "
             "the official figure."),
        ],
        "sources": [("CFPB: Buying a house", "https://www.consumerfinance.gov/owning-a-home/"),
                    ("CFPB: What is private mortgage insurance?", "https://www.consumerfinance.gov/ask-cfpb/what-is-private-mortgage-insurance-en-122/")],
        "related": ["home-affordability-calculator", "loan-payment-calculator", "inflation-calculator"],
        "js": "mortgage.js",
    },
    {
        "slug": "home-affordability-calculator", "cat": "home", "name": "Home Affordability",
        "card": "How much house your income and debts can support.",
        "title": "Home Affordability Calculator: How Much House Can I Afford?",
        "description": "Find out how much house you can afford. Estimate a home price range from your income, "
                       "monthly debts, down payment, interest rate, taxes and insurance using the 28/36 rule.",
        "h1": "How Much House Can I Afford?",
        "lead": "Estimate a realistic home price from your income, existing debts and down payment. The calculator "
                "applies the widely used 28/36 debt-to-income guideline and includes taxes, insurance and HOA dues.",
        "how": ["Enter your gross (pre-tax) annual household income.",
                "Add your monthly debt payments: car loans, student loans, credit card minimums and so on.",
                "Enter your down payment, expected interest rate and loan term.",
                "Adjust the property tax rate, insurance and HOA to match the area you're shopping in."],
        "formula": "<p>Lenders commonly check two debt-to-income (DTI) limits:</p><ul>"
                   "<li><strong>Front-end (28%)</strong>: housing costs should stay at or below 28% of gross monthly income.</li>"
                   "<li><strong>Back-end (36%)</strong>: housing costs plus other monthly debts should stay at or below 36%.</li></ul>"
                   "<p>The calculator takes the <em>lower</em> of the two limits as your maximum monthly housing payment. It then "
                   "solves for the home price whose mortgage principal and interest, property tax, insurance and HOA add up "
                   "to that amount, given your down payment, rate and term.</p>",
        "tips": ["Paying down a car loan or credit card before you apply can raise your price range noticeably.",
                 "A larger down payment lowers the loan amount and can remove PMI.",
                 "Just because a lender approves a figure doesn't mean it fits your budget. Leave room to keep saving.",
                 "Get pre-approved before house hunting so you know your real rate and limit."],
        "faqs": [
            ("What is the 28/36 rule?",
             "It's a common lending guideline: spend no more than 28% of gross monthly income on housing, and no more "
             "than 36% on all debt payments combined. Many lenders allow higher ratios with strong credit or larger "
             "down payments, and FHA and VA loans use their own limits."),
            ("Does this include PMI?",
             "No. PMI depends on your credit score and loan type, so it isn't included in the affordability solve. "
             "With less than 20% down, check the final price in our <a href=\"{mortgage-calculator}\">mortgage "
             "calculator</a> with a PMI estimate added."),
            ("Should I use gross or net income?",
             "Lenders use gross (pre-tax) income for DTI ratios, so this calculator does too. For your own comfort, "
             "compare the payment with your take-home pay using the <a href=\"{budget-calculator}\">budget calculator</a>."),
            ("What counts as monthly debt?",
             "Minimum required payments on car loans, student loans, personal loans, credit cards, child support and "
             "other installment debts. Everyday expenses like groceries and utilities aren't counted in DTI."),
        ],
        "sources": [("CFPB: What is a debt-to-income ratio?", "https://www.consumerfinance.gov/ask-cfpb/what-is-a-debt-to-income-ratio-en-1791/"),
                    ("CFPB: Buying a house", "https://www.consumerfinance.gov/owning-a-home/")],
        "related": ["mortgage-calculator", "budget-calculator", "savings-goal-calculator"],
        "js": "home-affordability.js",
    },
    {
        "slug": "refinance-calculator", "cat": "home", "name": "Refinance", "added": "2026-09-22",
        "card": "New payment, monthly savings and break-even point.",
        "title": "Mortgage Refinance Calculator: Savings & Break-Even Point",
        "description": "Free mortgage refinance calculator. Compare your current loan with a new rate and term to see "
                       "your new monthly payment, monthly savings, break-even point and lifetime interest savings.",
        "h1": "Mortgage Refinance Calculator",
        "lead": "Find out whether refinancing is worth it. Compare your current mortgage with a new rate and term to see "
                "how much you'd save each month, how long it takes to earn back the closing costs, and what changes over "
                "the life of the loan.",
        "how": ["Enter your current loan balance, interest rate and the years left on your mortgage.",
                "Enter the new interest rate you've been quoted and the new loan term.",
                "Add the estimated closing costs and choose whether you'll pay them upfront or roll them into the new loan.",
                "Compare the break-even point with how long you expect to stay in the home."],
        "formula": "<p>Both payments use the standard fixed-rate formula "
                   "<span class=\"formula\">M = P × r(1 + r)<sup>n</sup> ÷ [(1 + r)<sup>n</sup> − 1]</span>, where "
                   "<strong>P</strong> is the balance, <strong>r</strong> the monthly rate and <strong>n</strong> the number "
                   "of payments left. Then:</p><ul>"
                   "<li><strong>Monthly savings</strong> = current payment − new payment</li>"
                   "<li><strong>Break-even</strong> = closing costs ÷ monthly savings (in months)</li>"
                   "<li><strong>Lifetime savings</strong> = all remaining payments on the current loan − (all payments on "
                   "the new loan + closing costs paid upfront)</li></ul>"
                   "<p>If you roll the costs into the loan, they're added to the new balance instead of paid upfront.</p>",
        "tips": ["If you'll move before the break-even point, refinancing usually costs more than it saves.",
                 "Resetting to a new 30-year term lowers the payment but can raise total interest. Compare a shorter term too.",
                 "Get Loan Estimates from at least three lenders on the same day so the rates are comparable.",
                 "Ask about lender credits and points. Paying points lowers the rate but lengthens the break-even."],
        "faqs": [
            ("When is refinancing worth it?",
             "Refinancing tends to make sense when the new rate is meaningfully lower and you plan to stay in the home "
             "past the break-even point, the month when your monthly savings have repaid the closing costs. It can "
             "also make sense to move from an adjustable rate to a fixed rate, or to shorten your term."),
            ("How much does it cost to refinance?",
             "Refinancing has closing costs much like a purchase loan: lender fees, appraisal, title insurance and "
             "government recording charges. They commonly total a few thousand dollars, often around 2% to 5% of the "
             "loan amount. Your Loan Estimate lists them line by line."),
            ("Should I roll closing costs into the new loan?",
             "Rolling costs in means no cash at closing, but you borrow more and pay interest on those costs for the "
             "whole loan. Try both options above to see the difference in lifetime savings."),
            ("Does refinancing restart my mortgage?",
             "Yes. A refinance pays off your old loan with a new one, and the new term starts from zero. If you have 25 "
             "years left and take a new 30-year loan, you'll be paying for 5 extra years unless you pay extra along the way."),
            ("Can I refinance with less than 20% equity?",
             "Often yes, but you may pay mortgage insurance and get a higher rate. FHA, VA and USDA loans have their own "
             "streamline refinance programs with different equity rules."),
        ],
        "sources": [("CFPB: Refinancing your mortgage", "https://www.consumerfinance.gov/ask-cfpb/what-is-a-cash-out-refinance-en-1813/"),
                    ("CFPB: Loan Estimate explainer", "https://www.consumerfinance.gov/owning-a-home/loan-estimate/")],
        "related": ["mortgage-calculator", "mortgage-payoff-calculator", "amortization-calculator"],
        "js": "refinance.js",
    },
    {
        "slug": "mortgage-payoff-calculator", "cat": "home", "name": "Mortgage Payoff", "added": "2026-09-22",
        "card": "How extra payments cut years and interest off your loan.",
        "title": "Mortgage Payoff Calculator: Pay Off Your Mortgage Early",
        "description": "See how extra monthly payments or a lump sum pay off your mortgage early. Calculate your new "
                       "payoff date, the years you'll save and the total interest you'll avoid.",
        "h1": "Mortgage Payoff Calculator",
        "lead": "See what paying a little extra does to your mortgage. Add an extra monthly amount or a one-time lump sum "
                "and find out how many years sooner you'll be mortgage-free, and how much interest you'll keep.",
        "how": ["Enter your current loan balance, interest rate and years remaining.",
                "Add an extra amount you could pay every month.",
                "Optionally add a one-time lump sum paid now, such as a bonus or tax refund.",
                "Compare the new payoff time and interest with your current schedule."],
        "formula": "<p>Your required payment is found with the standard amortization formula "
                   "<span class=\"formula\">M = P × r(1 + r)<sup>n</sup> ÷ [(1 + r)<sup>n</sup> − 1]</span>. The "
                   "calculator then runs the loan month by month: each month interest = balance × r, and the payment plus "
                   "your extra amount goes toward interest first and principal second. Because every extra dollar reduces "
                   "principal immediately, less interest accrues in every later month. That's why small extra payments "
                   "save so much.</p>",
        "tips": ["Tell your servicer to apply extra payments to principal, not to next month's payment.",
                 "Check your loan for prepayment penalties first. Most modern mortgages don't have them.",
                 "One extra payment a year (or 1/12 extra each month) takes several years off a typical 30-year loan.",
                 "Pay off high-interest debt and build an emergency fund before prepaying a low-rate mortgage."],
        "faqs": [
            ("Is it smart to pay off a mortgage early?",
             "It's a guaranteed return equal to your interest rate, and it lowers your monthly costs in retirement. "
             "But money sent to the mortgage is hard to get back. Many people first build an emergency fund, capture "
             "any employer 401(k) match and pay off higher-rate debt."),
            ("How do biweekly payments work?",
             "Paying half your monthly payment every two weeks adds up to 26 half-payments, or 13 full payments, a year. "
             "That's one extra payment annually. You can get the same result by adding 1/12 of your payment each month; "
             "enter that amount as the extra payment above."),
            ("Does paying extra lower my monthly payment?",
             "Usually not. On a standard fixed-rate loan, extra payments shorten the loan rather than lowering the "
             "required payment. Some lenders offer a recast, which re-amortizes the loan after a large lump sum to "
             "lower the payment, often for a fee."),
            ("Should I refinance or pay extra?",
             "If rates have fallen well below yours, a <a href=\"{refinance-calculator}\">refinance</a> can cut interest "
             "on the whole balance. If your rate is already low, extra payments avoid closing costs entirely."),
        ],
        "sources": [("CFPB: Paying off your mortgage early", "https://www.consumerfinance.gov/ask-cfpb/can-i-prepay-my-loan-at-any-time-without-penalty-en-1957/"),
                    ("CFPB: Owning a home", "https://www.consumerfinance.gov/owning-a-home/")],
        "related": ["amortization-calculator", "refinance-calculator", "mortgage-calculator"],
        "js": "mortgage-payoff.js",
    },
    {
        "slug": "amortization-calculator", "cat": "home", "name": "Amortization Schedule", "added": "2026-09-22",
        "card": "Full payment-by-payment schedule for any loan.",
        "title": "Amortization Calculator: Loan Amortization Schedule",
        "description": "Free amortization calculator with a full schedule. See every payment's principal and interest, "
                       "your remaining balance, payoff date and total interest, yearly or monthly.",
        "h1": "Amortization Schedule Calculator",
        "lead": "See exactly where every payment goes. Build a complete amortization schedule for a mortgage, auto loan or "
                "personal loan, with principal, interest and remaining balance, yearly or month by month.",
        "how": ["Enter the loan amount, interest rate and term in years.",
                "Pick the month of your first payment to see real payoff dates.",
                "Add an optional extra monthly payment to see how it shortens the schedule.",
                "Switch the schedule between yearly totals and every monthly payment."],
        "formula": "<p>The fixed monthly payment is "
                   "<span class=\"formula\">M = P × r(1 + r)<sup>n</sup> ÷ [(1 + r)<sup>n</sup> − 1]</span>. For each "
                   "payment:</p><ul><li><strong>Interest</strong> = remaining balance × r</li>"
                   "<li><strong>Principal</strong> = payment (plus any extra) − interest</li>"
                   "<li><strong>New balance</strong> = balance − principal</li></ul>"
                   "<p>Early payments are mostly interest because the balance is largest. As the balance falls, more of "
                   "each payment goes to principal.</p>",
        "tips": ["In the early years of a 30-year mortgage, most of each payment is interest. Extra payments then save the most.",
                 "Compare the total interest on a 15-year and 30-year term. The difference is often surprising.",
                 "Use the schedule to see your balance at the time you might sell or refinance.",
                 "Print the schedule or save the link to track your loan over time."],
        "faqs": [
            ("What is amortization?",
             "Amortization is paying off a loan with regular, equal payments over a set term. Each payment covers that "
             "month's interest and repays part of the principal, so the balance reaches zero at the end of the term."),
            ("Why is so much of my payment interest at first?",
             "Interest is charged on the remaining balance, which is largest at the start. As you pay principal down, "
             "the interest portion shrinks and the principal portion grows, even though the payment stays the same."),
            ("Does this include taxes and insurance?",
             "No. The schedule covers principal and interest only. For a full monthly housing cost including property "
             "tax, insurance, HOA and PMI, use the <a href=\"{mortgage-calculator}\">mortgage calculator</a>."),
            ("Can I use this for car loans and personal loans?",
             "Yes. Any fixed-rate loan with equal monthly payments amortizes the same way. Just enter the amount, APR "
             "and term."),
        ],
        "sources": [("CFPB: What is amortization?", "https://www.consumerfinance.gov/ask-cfpb/what-is-amortization-and-how-could-it-affect-my-auto-loan-en-755/"),
                    ("CFPB: Owning a home", "https://www.consumerfinance.gov/owning-a-home/")],
        "related": ["mortgage-payoff-calculator", "mortgage-calculator", "loan-payment-calculator"],
        "js": "amortization.js",
    },
    {
        "slug": "rent-vs-buy-calculator", "cat": "home", "name": "Rent vs. Buy", "added": "2026-09-22",
        "card": "Is buying or renting the better deal for you?",
        "title": "Rent vs. Buy Calculator: Should I Rent or Buy a Home?",
        "description": "Should you rent or buy? Compare the true cost of owning versus renting, including appreciation, "
                       "maintenance, closing and selling costs, rent increases and investment returns.",
        "h1": "Rent vs. Buy Calculator",
        "lead": "Compare the full financial picture of buying versus renting. The calculator counts mortgage payments, "
                "taxes, maintenance, closing and selling costs and home appreciation against rent, rent increases and what "
                "a renter could earn by investing the difference.",
        "how": ["Enter the home price, down payment and mortgage details for the home you'd buy.",
                "Add ongoing ownership costs: property tax, insurance, maintenance and HOA.",
                "Enter the rent for a comparable home and how fast rent tends to rise.",
                "Choose how many years you'd stay and the return you could earn investing instead."],
        "formula": "<p>The calculator simulates both paths month by month over the years you choose:</p><ul>"
                   "<li><strong>Buying</strong>: mortgage payment + property tax and maintenance (as a % of the home's "
                   "current value) + insurance + HOA. At the end, your wealth is the home's value minus selling costs "
                   "and the remaining loan balance.</li>"
                   "<li><strong>Renting</strong>: rent + renters insurance. The renter invests the down payment and "
                   "closing costs instead.</li>"
                   "<li>Each month, whichever option costs less invests the difference at your chosen return, so both "
                   "paths spend the same amount of money.</li></ul>"
                   "<p>The option with more wealth at the end comes out ahead. Insurance, HOA and renters insurance rise at "
                   "the rent increase rate. PMI and tax deductions aren't included.</p>",
        "tips": ["The longer you stay, the better buying tends to look, because closing and selling costs are spread over more years.",
                 "Small changes to home appreciation and investment return swing the result. Try pessimistic numbers too.",
                 "Budget 1% or more of the home's value each year for maintenance and repairs.",
                 "Renting isn't 'throwing money away' if you actually invest the savings."],
        "faqs": [
            ("Is it better to rent or buy?",
             "It depends on how long you'll stay, local prices compared with rents, interest rates and how you'd invest "
             "otherwise. Buying usually wins over longer periods; renting often wins if you might move within a few "
             "years, because buying and selling costs are high."),
            ("What is the break-even point?",
             "It's the year when buying pulls ahead of renting in total wealth. If you expect to stay longer than the "
             "break-even, buying is likely the better financial choice under your assumptions."),
            ("What costs of owning do people forget?",
             "Maintenance and repairs, property tax increases, HOA dues, closing costs when buying, and selling costs "
             "such as agent commissions and transfer taxes when you move. They can add up to tens of thousands of dollars."),
            ("Does this include the mortgage interest tax deduction?",
             "No. Most households take the standard deduction, so they get no extra benefit from mortgage interest. If "
             "you itemize, buying may look somewhat better than shown."),
        ],
        "sources": [("CFPB: Buying a house", "https://www.consumerfinance.gov/owning-a-home/"),
                    ("HUD: Buying a home", "https://www.hud.gov/topics/buying_a_home")],
        "related": ["home-affordability-calculator", "mortgage-calculator", "budget-calculator"],
        "js": "rent-vs-buy.js",
    },
    {
        "slug": "loan-payment-calculator", "cat": "debt", "name": "Loan Payment",
        "card": "Monthly payment, total interest and payoff time for any loan.",
        "title": "Loan Payment Calculator: Monthly Payment & Total Interest",
        "description": "Calculate the monthly payment on a personal loan, student loan or any fixed-rate loan. "
                       "See total interest, total cost and how extra payments shorten your payoff time.",
        "h1": "Loan Payment Calculator",
        "lead": "Work out the monthly payment on any fixed-rate loan, whether personal, student or business, and see "
                "the total interest you'll pay. Add an extra monthly amount to see how much faster you'd be debt-free.",
        "how": ["Enter the amount you plan to borrow.",
                "Add the annual interest rate (APR) and the loan term in years.",
                "Optionally add an extra monthly payment to see its effect on payoff time and interest."],
        "formula": "<p>The required payment uses the standard amortization formula "
                   "<span class=\"formula-inline\">M = P × r(1 + r)<sup>n</sup> ÷ [(1 + r)<sup>n</sup> − 1]</span>, where "
                   "<strong>P</strong> is the amount borrowed, <strong>r</strong> is the monthly rate and <strong>n</strong> the "
                   "number of payments. The calculator then simulates each month (interest first, then principal) to "
                   "find the payoff date and total interest, including any extra payment you add.</p>",
        "tips": ["Extra payments go straight to principal, so every extra dollar reduces future interest.",
                 "Check whether your lender charges prepayment penalties before paying early.",
                 "A shorter term raises the payment but usually cuts total interest dramatically.",
                 "Compare offers by APR, which includes most fees, rather than by the interest rate alone."],
        "faqs": [
            ("How is a loan payment calculated?",
             "Each payment covers that month's interest (balance × monthly rate) and the rest reduces the principal. "
             "Early payments are mostly interest, and later payments are mostly principal. The formula above finds "
             "the single fixed payment that brings the balance to zero by the end of the term."),
            ("How much does an extra payment save?",
             "It depends on the rate and how early you start, but extra payments made early in a loan save the most, "
             "because they remove principal that would otherwise collect interest for years. Enter an amount above to "
             "see your exact savings in time and interest."),
            ("What's the difference between APR and interest rate?",
             "The interest rate is the cost of borrowing the principal. APR also includes certain fees, such as "
             "origination fees, expressed as a yearly rate, which makes it better for comparing loan offers."),
            ("Can I use this for a car loan?",
             "Yes, but our <a href=\"{auto-loan-calculator}\">auto loan calculator</a> also handles trade-ins, "
             "sales tax and dealer fees."),
        ],
        "sources": [("CFPB: Consumer tools", "https://www.consumerfinance.gov/consumer-tools/"),
                    ("Federal Student Aid: Repayment", "https://studentaid.gov/manage-loans/repayment")],
        "related": ["auto-loan-calculator", "debt-payoff-calculator", "credit-card-payoff-calculator"],
        "js": "loan-payment.js",
    },
    {
        "slug": "auto-loan-calculator", "cat": "debt", "name": "Auto Loan",
        "card": "Car payment with trade-in, sales tax and fees.",
        "title": "Auto Loan Calculator: Estimate Your Monthly Car Payment",
        "description": "Estimate your monthly car payment with our free auto loan calculator. Includes trade-in "
                       "value, down payment, sales tax, fees, APR and loan term, plus total interest paid.",
        "h1": "Auto Loan Calculator",
        "lead": "See what a car will really cost each month. Enter the price, your trade-in and down payment, sales tax "
                "and fees, and compare loan terms to find a payment that fits your budget.",
        "how": ["Enter the vehicle price and the value of any trade-in.",
                "Add your cash down payment.",
                "Enter your state's sales tax rate and any dealer or registration fees you plan to finance.",
                "Add the APR and choose a term in months (36, 48, 60 and 72 are common)."],
        "formula": "<p>The amount financed is: <strong>price − trade-in − down payment + sales tax + fees</strong>. "
                   "Sales tax is applied to the price minus the trade-in, which is how most states handle it (a few "
                   "states tax the full price). The monthly payment then uses the standard amortization formula for "
                   "the APR and number of months you choose.</p>",
        "tips": ["Get pre-approved by a bank or credit union before visiting the dealer so you can compare their offer.",
                 "Longer terms lower the payment but add interest, and you may owe more than the car is worth for longer.",
                 "Negotiate the car's price first, then the financing and trade-in separately.",
                 "Many planners suggest keeping total car costs, including insurance and fuel, well under 15% of take-home pay."],
        "faqs": [
            ("Is sales tax included in my car loan?",
             "It can be. Many buyers roll sales tax and fees into the loan, which this calculator assumes. If you pay "
             "them in cash, set the fees to zero and add the tax amount to your down payment instead."),
            ("What's a good loan term for a car?",
             "Shorter is cheaper. A 36–60 month loan keeps interest lower and helps you avoid negative equity. "
             "72- and 84-month loans reduce the payment but can cost thousands more. Compare terms above."),
            ("Does my trade-in reduce sales tax?",
             "In most states, yes: sales tax is charged on the price minus your trade-in value. A handful of states "
             "tax the full purchase price. Check your state's rules."),
            ("How can I get a lower car payment?",
             "Put more money down, choose a less expensive car, improve your credit score before applying, shop "
             "rates with multiple lenders, or pick a slightly longer term (knowing you'll pay more interest)."),
        ],
        "sources": [("CFPB: Auto loans", "https://www.consumerfinance.gov/consumer-tools/auto-loans/"),
                    ("FTC: Buying a used car from a dealer", "https://consumer.ftc.gov/articles/buying-used-car-dealer")],
        "related": ["loan-payment-calculator", "budget-calculator", "debt-payoff-calculator"],
        "js": "auto-loan.js",
    },
    {
        "slug": "debt-payoff-calculator", "cat": "debt", "name": "Debt Payoff",
        "card": "Avalanche vs. snowball, month by month.",
        "title": "Debt Payoff Calculator: Avalanche vs. Snowball Method",
        "description": "Compare the debt avalanche and debt snowball methods. Enter your debts and extra payment "
                       "to see your debt-free date and total interest for each payoff strategy.",
        "h1": "Debt Payoff Calculator",
        "lead": "List your debts and how much extra you can pay each month. We'll simulate both the avalanche and snowball "
                "methods side by side, so you can see which gets you debt-free sooner and which saves more interest.",
        "how": ["Add each debt with its balance, APR and minimum payment.",
                "Enter the extra amount you can pay each month on top of the minimums.",
                "Compare the debt-free date and total interest for each method."],
        "formula": "<p>Each month the simulation adds interest to every balance (balance × APR ÷ 12), pays every minimum, "
                   "then sends all remaining money to one target debt. <strong>Avalanche</strong> targets the highest APR; "
                   "<strong>snowball</strong> targets the smallest balance. When a debt is paid off, its payment rolls into "
                   "the next target, so your total monthly payment stays the same until you're debt-free.</p>",
        "tips": ["Avalanche almost always saves the most interest. Snowball gives faster early wins.",
                 "The best plan is the one you'll stick with, so pick the method that keeps you motivated.",
                 "Stop adding new balances while you pay down debt, or the plan can't work.",
                 "A 0% balance transfer or consolidation loan can speed things up if the fees are low."],
        "faqs": [
            ("Is the avalanche or snowball method better?",
             "Mathematically, avalanche (highest interest first) usually costs less. Snowball (smallest balance first) "
             "pays off individual debts sooner, which many people find motivating. Enter your real debts to see how "
             "big the difference is for you. Often it's smaller than you'd expect."),
            ("What if my payment doesn't cover the interest?",
             "If your total payment is less than the interest charged each month, the balance can never reach zero. "
             "The calculator will warn you. Increase the extra payment or look at lowering your rates."),
            ("Should I consolidate my debt?",
             "Consolidation can help if the new loan's APR is lower than your current average rate and the fees are "
             "small. Use the <a href=\"{loan-payment-calculator}\">loan payment calculator</a> to compare."),
            ("Does paying off debt raise my credit score?",
             "Lowering credit card balances reduces your credit utilization, which often improves scores. Keep "
             "paying on time, since payment history is the biggest factor."),
        ],
        "sources": [("CFPB: Debt collection and repayment", "https://www.consumerfinance.gov/consumer-tools/debt-collection/"),
                    ("FTC: Coping with debt", "https://consumer.ftc.gov/articles/how-get-out-debt")],
        "related": ["credit-card-payoff-calculator", "loan-payment-calculator", "budget-calculator"],
        "js": "debt-payoff.js",
    },
    {
        "slug": "credit-card-payoff-calculator", "cat": "debt", "name": "Credit Card Payoff",
        "card": "How long to pay off a card, and how to go faster.",
        "title": "Credit Card Payoff Calculator: How Long Will It Take?",
        "description": "See how long it will take to pay off your credit card and how much interest you'll pay. "
                       "Find the monthly payment needed to be debt-free by your target date.",
        "h1": "Credit Card Payoff Calculator",
        "lead": "Find out how long your credit card balance will take to pay off at your current payment, how much "
                "interest it will cost, and exactly what to pay each month to clear it by a date you choose.",
        "how": ["Enter your current balance and the card's APR.",
                "Add the payment you make now and any extra you can afford.",
                "Pick a target number of months to see the payment needed to finish on time."],
        "formula": "<p>Each month the balance grows by APR ÷ 12, then your payment is applied. The calculator repeats "
                   "this until the balance reaches zero to find your payoff time and total interest. The payment "
                   "needed for a target date uses the amortization formula "
                   "<span class=\"formula-inline\">P = B × r ÷ [1 − (1 + r)<sup>−n</sup>]</span>.</p>",
        "tips": ["Paying only the minimum can stretch a balance out for many years. Even $25–50 extra makes a big difference.",
                 "Pay more than the minimum on the highest-APR card first.",
                 "A 0% intro-APR balance transfer can save a lot if you clear it before the promo ends.",
                 "Set up autopay for at least the minimum so you never miss a payment."],
        "faqs": [
            ("Why does my balance barely go down?",
             "At a high APR, most of a small payment goes to interest. On a $5,000 balance at 24% APR, about $100 of "
             "each month's payment is interest. Paying more than the minimum is the fastest way out."),
            ("How is credit card interest calculated?",
             "Most issuers charge interest daily using the average daily balance and your APR ÷ 365. This calculator "
             "uses a monthly approximation (APR ÷ 12), which is very close for planning."),
            ("Should I pay off my card or save?",
             "Most people benefit from a small emergency fund first, then aggressively paying down high-APR cards. "
             "Card interest usually far exceeds what savings earn."),
            ("What is a balance transfer?",
             "Moving a balance to a card with a low or 0% introductory APR. There's usually a 3–5% transfer fee, so it "
             "pays off when you can clear most of the balance during the promo period."),
        ],
        "sources": [("CFPB: Credit cards", "https://www.consumerfinance.gov/consumer-tools/credit-cards/"),
                    ("Federal Reserve: Consumer credit", "https://www.federalreserve.gov/releases/g19/current/")],
        "related": ["debt-payoff-calculator", "loan-payment-calculator", "emergency-fund-calculator"],
        "js": "credit-card.js",
    },
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
        "related": ["cd-calculator", "compound-interest-calculator", "emergency-fund-calculator"],
        "js": "savings-goal.js",
    },
    {
        "slug": "cd-calculator", "cat": "grow", "name": "CD", "added": "2026-09-22",
        "card": "Interest a certificate of deposit earns by maturity.",
        "title": "CD Calculator: Certificate of Deposit Interest & APY",
        "description": "Free CD calculator. See how much interest a certificate of deposit earns by maturity from the "
                       "deposit, APY and term, after taxes, and compare it with a savings account.",
        "h1": "CD Calculator",
        "lead": "Find out exactly what a certificate of deposit will be worth when it matures. Enter your deposit, the "
                "APY and the term to see the interest you'll earn before and after taxes, and how much more it pays than "
                "another account.",
        "how": ["Enter how much you plan to deposit.",
                "Enter the CD's APY (annual percentage yield) and choose its term.",
                "Add your tax rate to see interest after federal and state income tax.",
                "Enter another account's APY, such as your current savings account, to compare."],
        "formula": "<p>Because APY already includes compounding, the value at maturity is:</p>"
                   "<p class=\"formula\">Balance = Deposit × (1 + APY)<sup>months ÷ 12</sup></p>"
                   "<p>Interest earned = balance − deposit. After-tax interest = interest × (1 − tax rate). The comparison "
                   "runs the same formula with the other account's APY, assuming its rate stays the same, which savings "
                   "account rates often don't.</p>",
        "tips": ["Compare APY, not interest rate. APY includes compounding, so it's the apples-to-apples number.",
                 "Online banks and credit unions often pay much higher CD rates than large traditional banks.",
                 "Build a CD ladder (for example, 1-, 2- and 3-year CDs) so some money becomes available every year.",
                 "Check the early withdrawal penalty before you open a CD."],
        "faqs": [
            ("How is CD interest calculated?",
             "Banks compound CD interest daily or monthly, and the APY reflects that compounding over a year. Multiply "
             "your deposit by (1 + APY) raised to the number of years to find the value at maturity."),
            ("Are CDs safe?",
             "CDs at FDIC-insured banks, or NCUA-insured credit unions, are protected up to $250,000 per depositor, per "
             "institution, per ownership category. Your rate is locked for the term, unlike a savings account."),
            ("What happens if I withdraw early?",
             "Most CDs charge an early withdrawal penalty, commonly several months of interest. On a short CD, the "
             "penalty can eat into your principal. Consider a no-penalty CD if you may need the money."),
            ("Is CD interest taxable?",
             "Yes. CD interest is taxed as ordinary income in the year it's credited, even if the CD hasn't matured. CDs "
             "held inside an IRA follow IRA tax rules instead."),
            ("CD or high-yield savings account?",
             "A CD locks in a rate for a set term, which helps if rates fall. A high-yield savings account lets you "
             "withdraw anytime, but its rate can change. Many people keep an emergency fund in savings and use CDs for "
             "money with a known date, like a down payment."),
        ],
        "sources": [("FDIC: Understanding deposit insurance", "https://www.fdic.gov/resources/deposit-insurance/understanding-deposit-insurance/"),
                    ("Investor.gov: Certificates of deposit", "https://www.investor.gov/introduction-investing/investing-basics/investment-products/certificates-deposit-cds")],
        "related": ["savings-goal-calculator", "compound-interest-calculator", "inflation-calculator"],
        "js": "cd.js",
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
        "related": ["budget-calculator", "retirement-calculator", "debt-payoff-calculator"],
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

POPULAR = ["mortgage-calculator", "home-affordability-calculator", "compound-interest-calculator",
           "loan-payment-calculator", "retirement-calculator", "salary-to-hourly-calculator"]

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
