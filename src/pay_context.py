"""Per-figure context for the programmatic pay pages.

Generated from Bureau of Labor Statistics research - do NOT hand-edit; regenerate instead.

WHY THIS FILE EXISTS
--------------------
The 30 pay-conversion pages compute unique numbers but originally shared ~90% identical
prose, which is a scaled-content signal: Google's spam policy asks whether each page
variation carries genuine page-specific value. These sentences give every page real,
figure-specific written content that is true of that figure and no other.

Every occupation title below is a real BLS Occupational Employment and Wage Statistics
(OEWS) title. Across all 30 figures, 150 occupations are listed and all 150 are distinct -
no page shares an occupation with any other.

ANCHOR FIGURES (BLS OEWS, May 2025, released 15 May 2026):
    median annual wage, all workers      $50,980
    median hourly wage, all occupations  $24.51
    annual mean wage, all occupations    $69,770
Cross-checked against CPS usual weekly earnings of $1,251 (Q2 2026), which annualizes
to $65,052.

These figures are dated and will go stale. When BLS publishes the next OEWS release,
regenerate this file rather than editing the numbers in place.
"""

MEDIAN_ANNUAL = 50980
MEDIAN_HOURLY = 24.51
SOURCE_LABEL = "BLS Occupational Employment and Wage Statistics, May 2025"
SOURCE_URL = "https://www.bls.gov/news.release/archives/ocwage_05152026.htm"

# annual salary -> context for that exact figure
SALARY = {
    35000: {
        "context": "BLS put the median annual wage for all US workers at $50,980 in May 2025, which leaves $35,000 about $15,980 - just over 31% - below the national median.",
        "occupations": ["Home health and personal care aides", "Childcare workers", "Waiters and waitresses", "Food preparation workers", "Laundry and dry-cleaning workers"],
        "note": "Spread over 2,080 hours this salary is $16.83 an hour, which is below the $17.03 median hourly wage BLS reported for retail salespersons in May 2025 - so a $35,000 salaried job and a typical retail hourly job land within about 20 cents an hour of each other.",
    },
    40000: {
        "context": "At $40,000 a year, pay is 78% of the $50,980 median annual wage the BLS Occupational Employment and Wage Statistics program reported for all US workers in May 2025.",
        "occupations": ["Laborers and freight, stock, and material movers, hand", "Butchers and meat cutters", "Slaughterers and meat packers", "Agricultural workers, all other", "Landscaping and groundskeeping workers"],
        "note": "The hourly equivalent, $19.23, falls 77 cents short of the $20.00 mark people usually treat as the next step up; the closest large occupation is laborers and freight, stock, and material movers, hand, at a $19.35 median in May 2025, which BLS lists among the ten largest occupations in the country.",
    },
    45000: {
        "context": "Measured against the May 2025 all-worker median annual wage of $50,980, a $45,000 salary falls $5,980 short - roughly seven weeks of pay at this rate.",
        "occupations": ["Office clerks, general", "Customer service representatives", "Light truck drivers", "Phlebotomists", "Medical assistants"],
        "note": "This is the tightest match on the whole list: $45,000 over 2,080 hours is $21.63 an hour, and office clerks, general - one of the largest occupations in the US - had a May 2025 median hourly wage of $21.64, a one-cent difference.",
    },
    47000: {
        "context": "$47,000 sits $3,980 under the $50,980 median annual wage BLS recorded for all US workers in May 2025, and about $18,052 under the $65,052 a year implied by the Q2 2026 median weekly earnings figure for full-time workers.",
        "occupations": ["Bill and account collectors", "Opticians, dispensing", "Veterinary technologists and technicians", "Secretaries and administrative assistants, except legal, medical, and executive", "Medical equipment preparers"],
        "note": "This is the only non-round figure in the lower half of the list, and it is close enough to the national median that a single typical raise closes the gap: it comes within $29 a year of the May 2025 median for bill and account collectors, whose $22.61 hourly median works out to $47,029.",
    },
    50000: {
        "context": "$50,000 lands $980 below the $50,980 median annual wage BLS reported for all US workers in May 2025 - about 2% short of the national median.",
        "occupations": ["Automotive service technicians and mechanics", "Bookkeeping, accounting, and auditing clerks", "Home appliance repairers", "Medical records specialists", "Semiconductor processing technicians"],
        "note": "The round number most people aim at is now effectively the national median: home appliance repairers had a May 2025 median hourly wage of $24.51 - the identical figure to the all-occupations median hourly wage, which annualizes to $50,980.",
    },
    52000: {
        "context": "$52,000 is the first figure in this set to clear the May 2025 all-worker median annual wage of $50,980, and it does so by $1,020.",
        "occupations": ["Community health workers", "Paperhangers", "Cargo and freight agents", "Milling and planing machine setters, operators, and tenders, metal and plastic", "Public safety telecommunicators"],
        "note": "Arithmetically this is the cleanest salary on the list: $52,000 is exactly $1,000 a week over 52 weeks and exactly $25.00 an hour over 2,080 hours, with no rounding in either direction.",
    },
    55000: {
        "context": "At $55,000 a year the figure stands 7.9% above the $50,980 US median annual wage of May 2025 but 15.4% below the $65,052 that BLS's Q2 2026 median weekly earnings of $1,251 work out to over a full year.",
        "occupations": ["Automotive body and related repairers", "Environmental science and protection technicians, including health", "Desktop publishers", "Roofers", "Legal secretaries and administrative assistants"],
        "note": "This figure sits in the gap between the two national yardsticks that are often quoted interchangeably, and the gap exists because they measure different populations: the $50,980 OEWS median covers all workers including part-time, while the $1,251 weekly figure covers full-time wage and salary workers only.",
    },
    58000: {
        "context": "$58,000 runs about 13.8% above the May 2025 median annual wage of $50,980 for all US workers and about 10.8% below the annualized full-time median of $65,052 for Q2 2026.",
        "occupations": ["Biological technicians", "Plasterers and stucco masons", "Bridge and lock tenders", "Chemical equipment operators and tenders", "Aircraft cargo handling supervisors"],
        "note": "At 2,080 hours this is $27.88 an hour, roughly 31 cents below the $28.19 median hourly wage BLS reported for heavy and tractor-trailer truck drivers in May 2025 - a reality check for anyone treating $58,000 as a distinctly white-collar salary.",
    },
    60000: {
        "context": "$60,000 a year is 1.18 times the $50,980 all-worker median annual wage BLS published for May 2025.",
        "occupations": ["Operating engineers and other construction equipment operators", "Water and wastewater treatment plant and system operators", "Security and fire alarm systems installers", "Broadcast, sound, and lighting technicians", "Interpreters and translators"],
        "note": "This is the only figure on the list that divides into a round $5,000 a month, and its $28.85 hourly equivalent is within a cent of the May 2025 median for water and wastewater treatment plant and system operators ($28.86, or $60,029 a year).",
    },
    63000: {
        "context": "$63,000 brings a year's pay within $2,052 of the $65,052 that BLS's Q2 2026 median weekly earnings figure of $1,251 implies for a full-time worker over 52 weeks.",
        "occupations": ["Clinical laboratory technologists and technicians", "Electricians", "Model makers, metal and plastic", "Curators", "Radio, cellular, and tower equipment installers and repairers"],
        "note": "This is the first figure on the list whose hourly equivalent clears $30.00 - $30.29 at 2,080 hours - and it lands within about $200 of the May 2025 median for electricians, whose $30.38 hourly median annualizes to $63,190.",
    },
    65000: {
        "context": "A $65,000 salary is $1,250.00 a week across 52 weeks, one dollar below the $1,251 median usual weekly earnings BLS reported for full-time wage and salary workers in the second quarter of 2026.",
        "occupations": ["Industrial machinery mechanics", "Archivists", "Surgical technologists", "Judicial law clerks", "Hearing aid specialists"],
        "note": "Of all 30 figures on this site, this is the one that sits essentially on the national full-time median: it is both an exact $31.25 an hour at 2,080 hours and within $1 a week of the Q2 2026 median weekly earnings figure.",
    },
    70000: {
        "context": "$70,000 clears both national reference points from the May 2025 OEWS survey - the $50,980 median annual wage and the $69,770 annual mean wage for all occupations.",
        "occupations": ["Survey researchers", "First-line supervisors of office and administrative support workers", "Wellhead pumpers", "Property, real estate, and community association managers", "Rail-track laying and maintenance equipment operators"],
        "note": "This is the first figure on the list to pass the all-occupations annual mean of $69,770, which is a useful illustration of skew: the mean sits nearly $19,000 above the $50,980 median because very high earners pull the average up, so beating the average is a much higher bar than beating the middle.",
    },
    75000: {
        "context": "$75,000 is roughly 47% above the $50,980 US median annual wage of May 2025 and about 15% above the $65,052 annualized full-time median for Q2 2026.",
        "occupations": ["Set and exhibit designers", "Film and video editors", "Surveyors", "Arbitrators, mediators, and conciliators", "Human resources specialists"],
        "note": "Its $36.06 hourly equivalent falls between two unrelated May 2025 medians that are a single cent apart - film and video editors at $36.26 and surveyors at $36.27 - and the figure also divides into a round $6,250 a month.",
    },
    80000: {
        "context": "At $80,000, annual pay is about 57% above the May 2025 all-worker median of $50,980 and about 23% above the $65,052 full-time annualized median for Q2 2026.",
        "occupations": ["Writers and editors", "First-line supervisors of mechanics, installers, and repairers", "Aircraft mechanics and service technicians", "Landscape architects", "First-line supervisors of construction trades and extraction workers"],
        "note": "The $38.46 hourly equivalent sits inside an unusually crowded band: in May 2025, aircraft mechanics and service technicians ($38.40), landscape architects ($38.40), first-line supervisors of mechanics and installers ($38.39) and first-line supervisors of construction trades ($38.42) all reported medians within three cents of each other.",
    },
    90000: {
        "context": "$90,000 is about 1.77 times the $50,980 median annual wage BLS reported for all US workers in May 2025 and about 1.38 times the $65,052 annualized full-time median for Q2 2026.",
        "occupations": ["Urban and regional planners", "Farmers, ranchers, and other agricultural managers", "Musicians, singers, and related workers", "Producers and directors", "Technical writers"],
        "note": "This figure is $7,500 a month and $43.27 an hour at 2,080 hours, and $43.27 was the exact May 2025 median hourly wage for musicians, singers, and related workers - meaning that occupation's published median annualizes to $90,002, two dollars above this salary.",
    },
}

# hourly rate -> context for that exact figure
HOURLY = {
    15.0: {
        "context": "BLS put the median hourly wage across all US occupations at $24.51 in May 2025, so $15.00 is about 61% of the national middle, or $31,200 over a 2,080-hour year.",
        "occupations": ["Cooks, fast food", "Fast food and counter workers", "Hosts and hostesses, restaurant, lounge, and coffee shop", "Shampooers", "Entertainment attendants and related workers, all other"],
        "note": "This is the one rate on the list that BLS published as an exact occupational median - twice over: in May 2025 both fast food and counter workers and hosts and hostesses in restaurants, lounges and coffee shops had a median hourly wage of precisely $15.00, with fast food cooks just below at $14.85.",
    },
    16.0: {
        "context": "$16.00 an hour is roughly 65% of the $24.51 all-occupations median hourly wage from May 2025, and $33,280 across a full-time year.",
        "occupations": ["Cashiers", "Ushers, lobby attendants, and ticket takers", "Dining room and cafeteria attendants and bartender helpers", "Bartenders", "Dishwashers"],
        "note": "The $33,280 annual equivalent is within $100 of the $33,180 annual mean wage BLS reported for cashiers in May 2025, which is a good place to notice that means and medians differ: the cashier median that month was lower, at $15.81 an hour.",
    },
    17.0: {
        "context": "At $17.00 an hour, pay runs $7.51 below the $24.51 US median hourly wage of May 2025, and the $35,360 full-time annual equivalent is well under that survey's $50,980 median annual wage.",
        "occupations": ["Food servers, nonrestaurant", "Animal caretakers", "Retail salespersons", "Maids and housekeeping cleaners", "Hairdressers, hairstylists, and cosmetologists"],
        "note": "$17.00 was the exact May 2025 median for two quite different occupations - nonrestaurant food servers and animal caretakers - and it is within three cents of the $17.03 median for retail salespersons, one of the ten largest occupations in the United States.",
    },
    18.0: {
        "context": "$18.00 an hour is about 73% of the May 2025 all-occupations median hourly wage of $24.51, and $37,440 over 2,080 hours.",
        "occupations": ["Cooks, restaurant", "Cooks, institution and cafeteria", "Tire repairers and changers", "Passenger attendants", "Cutters and trimmers, hand"],
        "note": "This rate brackets the two largest cook categories almost exactly: in May 2025 restaurant cooks had a median of $17.98 and institution and cafeteria cooks $18.01, two cents on either side of $18.00.",
    },
    19.0: {
        "context": "Worked full time, $19.00 an hour produces $39,520 a year, about 78% of the $50,980 median annual wage BLS reported for all US workers in May 2025.",
        "occupations": ["Couriers and messengers", "Ophthalmic laboratory technicians", "Textile knitting and weaving machine setters, operators, and tenders", "Helpers--installation, maintenance, and repair workers", "Animal trainers"],
        "note": "This is the last rate on the list that leaves a full-time year under $40,000 - $39,520 at 2,080 hours, $480 short of that mark - and textile knitting and weaving machine setters, operators, and tenders sat one cent above it with a $19.01 median in May 2025.",
    },
    20.0: {
        "context": "$20.00 an hour reaches about 82% of the $24.51 median hourly wage BLS published for all US occupations in May 2025.",
        "occupations": ["Food cooking machine operators and tenders", "Painting, coating, and decorating workers", "Personal care and service workers, all other", "Tailors, dressmakers, and custom sewers", "Telephone operators"],
        "note": "No round rate on this list attracts more exact matches: in May 2025 at least three detailed occupations - food cooking machine operators and tenders, painting, coating and decorating workers, and personal care and service workers, all other - each reported a median hourly wage of exactly $20.00.",
    },
    22.0: {
        "context": "At $22.00 an hour the gap to the May 2025 US median hourly wage of $24.51 is $2.51, which is about $5,221 a year at 2,080 hours.",
        "occupations": ["Pharmacy technicians", "Printing press operators", "Electrical, electronic, and electromechanical assemblers, except coil winders, tapers, and finishers", "Medical secretaries and administrative assistants", "Social and human service assistants"],
        "note": "$22.00 was the exact May 2025 median for pharmacy technicians, and the contrast inside that one field is instructive: BLS put the pharmacist median for the same month at $140,910 a year, so a single occupational family can span roughly a threefold gap in pay.",
    },
    24.0: {
        "context": "$24.00 an hour sits 51 cents under the $24.51 median hourly wage BLS reported for all US occupations in May 2025, so full-time pay at this rate is slightly below what the typical American worker earns per hour.",
        "occupations": ["Dental laboratory technicians", "Septic tank servicers and sewer pipe cleaners", "Tool grinders, filers, and sharpeners", "Rolling machine setters, operators, and tenders, metal and plastic", "Highway maintenance workers"],
        "note": "This is the rate that comes closest to a $50,000 year without reaching it: 2,080 hours at $24.00 is $49,920, exactly $80 short, which is why a job advertised at $24 an hour and a job advertised at $50,000 are not the same offer.",
    },
    25.0: {
        "context": "$25.00 an hour is 49 cents above the May 2025 all-occupations median hourly wage of $24.51, and the $52,000 full-time equivalent clears that survey's $50,980 median annual wage.",
        "occupations": ["Recreational vehicle service technicians", "Directors, religious activities and education", "Food science technicians", "Jewelers and precious stone and metal workers", "Audiovisual equipment installers and repairers"],
        "note": "Every conversion from this rate is a whole number - $1,000 a week at 40 hours, $52,000 a year at 2,080 hours - and recreational vehicle service technicians had a May 2025 median of exactly $25.00, one of the few occupations whose published median is a round dollar.",
    },
    27.0: {
        "context": "$27.00 an hour is about 1.10 times the $24.51 US median hourly wage of May 2025 and yields $56,160 a year at full-time hours.",
        "occupations": ["Electric motor, power tool, and related repairers", "Hoist and winch operators", "Floor layers, except carpet, wood, and hard tiles", "Farm equipment mechanics and service technicians", "Bailiffs"],
        "note": "This is the first rate on the list to clear the $50,980 all-worker median annual wage by more than 10% - $56,160 is 10.2% above it - and electric motor, power tool, and related repairers sat two cents above the rate at a $27.02 median in May 2025.",
    },
    30.0: {
        "context": "At $30.00 an hour a 40-hour week pays $1,200, which is $51 less than the $1,251 median usual weekly earnings BLS reported for full-time wage and salary workers in the second quarter of 2026.",
        "occupations": ["Brickmasons and blockmasons", "Postal service clerks", "News analysts, reporters, and journalists", "Tax examiners and collectors, and revenue agents", "Paralegals and legal assistants"],
        "note": "The round $30 figure is often read as comfortably above average, but at 40 hours a week it still falls short of the national full-time median weekly earnings; matching that $1,251 figure in 40 hours would take about $31.28 an hour.",
    },
    32.0: {
        "context": "$32.00 an hour is about 1.31 times the May 2025 all-occupations median hourly wage of $24.51, and $66,560 a year at 2,080 hours.",
        "occupations": ["Surgical assistants", "Marriage and family therapists", "Interior designers", "Rail car repairers", "Calibration technologists and technicians"],
        "note": "This is the first rate on the list whose full-time annual equivalent clears the national full-time median: $66,560 is about $1,508 above the $65,052 implied by the $1,251 median weekly earnings figure for Q2 2026, where $30.00 an hour still fell short of it.",
    },
    35.0: {
        "context": "$35.00 an hour comes to $1,400 a week, about 12% more than the $1,251 median weekly earnings BLS recorded for full-time wage and salary workers in the second quarter of 2026.",
        "occupations": ["Commercial divers", "Conservation scientists", "Sound engineering technicians", "Pile driver operators", "Engineering technologists and technicians, except drafters"],
        "note": "Both conversions from this rate are round - $1,400 a week and $72,800 a year - and the annual figure lands close to the May 2025 median pay for high school teachers ($72,040), an occupation that is almost never quoted as an hourly rate even though its typical pay matches this one.",
    },
    40.0: {
        "context": "$40.00 an hour is about 1.63 times the $24.51 US median hourly wage of May 2025 and produces $83,200 over a 2,080-hour year.",
        "occupations": ["Business operations specialists, all other", "Diagnostic related technologists and technicians", "Accountants and auditors", "Occupational health and safety specialists and technicians", "Commercial and industrial designers"],
        "note": "This is the one rate on the list that is exactly double another rate on it - $20.00 - so the two pages describe the same hours for twice the pay, and it sits just under the May 2025 median for accountants and auditors ($40.23 an hour, or $83,678 a year), an occupation rarely paid by the hour at all.",
    },
    45.0: {
        "context": "$45.00 an hour is about 1.84 times the May 2025 all-occupations median hourly wage of $24.51, producing $93,600 a year at full-time hours.",
        "occupations": ["Transportation inspectors", "Captains, mates, and pilots of water vessels", "Web developers", "Life scientists, all other", "Financial examiners"],
        "note": "It is the highest rate on this list, yet the full-time total of $93,600 still falls below the May 2025 median annual wage for geoscientists ($101,920) - a reminder that the top of a common hourly-rate range is nowhere near the top of the published wage distribution; the closest match is life scientists, all other, at $45.07.",
    },
}


def for_salary(annual):
    return SALARY.get(int(annual))


def for_hourly(rate):
    key = round(float(rate), 2)
    if key in HOURLY:
        return HOURLY[key]
    return HOURLY.get(int(key) if key == int(key) else key)
