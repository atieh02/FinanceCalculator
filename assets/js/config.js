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

  /* Partner / affiliate offers shown in a labeled "Sponsored" box under each calculator, by category:
     home, debt, grow, plan, protect. Leave offers empty to hide the box.
     Example offer: { name: "Compare mortgage rates", text: "See personalized rates from top lenders.",
                      cta: "Compare rates", url: "https://partner.example.com/?ref=calcmyfin" } */
  partners: {
    home:    { title: "Ready for the next step?", offers: [] },
    debt:    { title: "Lower your interest costs", offers: [] },
    grow:    { title: "Put your savings to work", offers: [] },
    plan:    { title: "Tools to stay on budget", offers: [] },
    protect: { title: "Protect your family", offers: [] }
  }
};
