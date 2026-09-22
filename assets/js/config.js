/* CalcMyFin settings: the ONLY file you need to edit to turn on analytics, ads and partner offers. */
window.CMF_CONFIG = {
  /* Google Analytics 4 Measurement ID, e.g. "G-ABC123XYZ9". Leave "" to disable. */
  ga4Id: "G-5HGGSG34F1",

  /* Google AdSense. Paste your publisher ID after approval, e.g. "ca-pub-1234567890123456".
     With only a client ID, Auto ads can fill the page. For more control, create display ad units
     in AdSense and paste their slot IDs below; empty slots stay hidden. */
  adsense: {
    client: "",
    slots: {
      "after-results": "",   // just below every calculator (highest-earning spot)
      "in-content": "",      // inside the article, after the example
      "sidebar": "",         // sticky 300x600 on desktop
      "home-top": "",        // homepage, under "Most popular"
      "footer": ""           // above the footer on every page
    }
  },

  /* Other ad networks (Ezoic, Mediavine, Raptive, etc.) can target the same slots by their IDs:
     #ad-after-results, #ad-in-content, #ad-sidebar, #ad-home-top, #ad-footer.
     Add their loader script URL here and it will be loaded on every page. */
  extraAdScripts: [],

  /* Partner / affiliate offers, shown in a labeled "Sponsored" box right under the calculator result.
     Each calculator belongs to one group (see OFFERS in src/content.py); the box also shows a headline
     built from the visitor's own result. A group with no offers shows nothing.
     Preview the layout on any calculator with ?offers=preview.

     Offer fields: name, text, cta (button label), url (your affiliate link),
                   badge (optional, e.g. "Top pick"), fine (optional fine print, e.g. "Rates as of Oct 2026").
     Example: { name: "Compare mortgage rates", text: "See personalized rates from multiple lenders.",
                cta: "Compare rates", url: "https://partner.example.com/?aff=calcmyfin" } */
  partners: {
    //            used by: mortgage, home affordability, amortization, rent vs. buy
    mortgage:  { title: "Compare mortgage rates", offers: [] },
    //            used by: refinance, mortgage payoff
    refinance: { title: "See if refinancing could lower your rate", offers: [] },
    //            used by: CD, savings goal, emergency fund, inflation
    savings:   { title: "Earn more on your savings", offers: [] },
    //            used by: loan payment, debt payoff
    debt:      { title: "Lower your interest costs", offers: [] },
    //            used by: credit card payoff
    cards:     { title: "Pay less interest on your card", offers: [] },
    //            used by: auto loan
    auto:      { title: "Compare auto loan rates", offers: [] },
    //            used by: compound interest, retirement, 401(k)
    invest:    { title: "Start investing for the long term", offers: [] },
    //            used by: budget, net worth, salary to hourly
    budget:    { title: "Tools to stay on top of your money", offers: [] },
    //            used by: life insurance
    insurance: { title: "Protect your family", offers: [] }
  }
};
