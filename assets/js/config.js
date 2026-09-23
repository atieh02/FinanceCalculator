/* CalcMyFin settings: the ONLY file you need to edit to turn on analytics, ads and partner offers. */
window.CMF_CONFIG = {
  /* Google Analytics 4 Measurement ID, e.g. "G-ABC123XYZ9". Leave "" to disable. */
  ga4Id: "G-5HGGSG34F1",

  /* Google AdSense. Paste your publisher ID after approval, e.g. "ca-pub-1234567890123456".
     With only a client ID, Auto ads can fill the page. For more control, create display ad units
     in AdSense and paste their slot IDs below; empty slots stay hidden. */
  adsense: {
    client: "ca-pub-2461339126089376",
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
     Example: { name: "Budgeting app", text: "See where every dollar goes and build savings automatically.",
                cta: "Try it free", url: "https://partner.example.com/?aff=calcmyfin" } */
  /* POLICY: offers must never promote interest. Do NOT add interest-based loans, mortgages or refinancing,
     credit cards, balance transfers, debt consolidation loans, interest-bearing savings/CDs, conventional
     insurance, gambling, or speculative trading (options, margin, crypto speculation). */
  partners: {
    //          used by: budget, net worth, salary to hourly, emergency fund, savings goal, save to buy
    budget:  { title: "Take control of your money", offers: [] },
    //          used by: investment growth, retirement, 401(k), inflation, gold & silver, cost of waiting,
    //                   FIRE, retirement income
    invest:  { title: "Ethical ways to grow your money", offers: [] }
  }
};
