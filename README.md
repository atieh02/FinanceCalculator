# CalcMyFin: free personal finance calculators

Static site hosted on GitHub Pages. 15 calculators, each with a full guide (formula, worked example, FAQ, sources), structured data, and ad-ready / affiliate-ready layout.

## Everyday tasks

| I want to… | Do this |
|---|---|
| Turn on **Google Analytics** | Put your `G-XXXXXXX` ID in `assets/js/config.js` → `ga4Id` |
| Turn on **AdSense** (after approval) | Put `ca-pub-…` in `config.js` → `adsense.client`, add slot IDs, and replace `ads.txt` with the line AdSense gives you |
| Add **affiliate offers** | Add offers to `config.js` → `partners.<group>.offers` (groups: home, budget, invest, protect). **Offers must never promote interest: no interest-based loans, credit cards, interest-bearing savings/CDs, conventional insurance, gambling or speculative trading.** Which calculator uses which group, and its personalized headline, is set in `OFFERS` in `src/content.py`. Preview any calculator with `?offers=preview` |
| Tell **Bing/IndexNow** about changes | After publishing: `python src/indexnow.py` (all pages) or `python src/indexnow.py 401k-calculator` |
| Edit page **text / SEO titles** | Edit `src/content.py`, then run `python src/build.py` |
| Add a **new calculator** | Add an entry to `CALCULATORS` in `src/content.py`, a form in `src/forms/<slug>.html`, a script in `assets/calculators/`, then build |
| Change the **domain** | Edit `domain` and `base_url` in `src/content.py`, rebuild, update DNS at Cloudflare |
| Preview ad positions | Open any page with `?ads=preview` |

## Structure

```
src/content.py      all page copy, titles, descriptions, FAQs, sources
src/build.py        generates every HTML page, sitemap.xml, robots.txt, manifest
src/forms/          calculator form markup
src/make_images.py  favicons + social share images (needs Pillow)
assets/css/site.css design system
assets/js/config.js analytics / ads / affiliate settings   <- edit this
assets/js/app.js    nav, consent, analytics events, ads, share links, search
assets/js/charts.js tiny SVG chart library
assets/calculators/ one script per calculator (+ common.js helpers)
```

## Analytics events (GA4)

`calculator_start`, `share_results`, `shared_link_open`, `print_results`, `reset_calculator`, `affiliate_view`, `affiliate_click`,
`outbound_click`, `select_calculator`, `faq_open`, `search`, `consent_choice`. Page views, scrolls and sessions come from GA4 automatically.
