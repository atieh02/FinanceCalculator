/* CalcMyFin site behaviour: nav, consent, analytics, ads, partners, share links, search. */
(function () {
  "use strict";
  var CFG = window.CMF_CONFIG || {};
  var doc = document, root = doc.documentElement;
  var qs = new URLSearchParams(location.search);
  var CONSENT_KEY = "cmf-consent";

  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }
  function $(s, el) { return (el || doc).querySelector(s); }
  function $$(s, el) { return Array.prototype.slice.call((el || doc).querySelectorAll(s)); }
  function loadScript(src, attrs) {
    var s = doc.createElement("script"); s.async = true; s.src = src;
    Object.keys(attrs || {}).forEach(function (k) { s.setAttribute(k, attrs[k]); });
    doc.head.appendChild(s); return s;
  }

  /* ---------------- consent (Google Consent Mode v2) ---------------- */
  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = window.gtag || gtag;
  var choice = store(CONSENT_KEY); // "granted" | "denied" | null
  var granted = choice !== "denied";
  gtag("consent", "default", {
    ad_storage: granted ? "granted" : "denied", ad_user_data: granted ? "granted" : "denied",
    ad_personalization: granted ? "granted" : "denied", analytics_storage: granted ? "granted" : "denied",
    wait_for_update: 500
  });

  function setConsent(value) {
    store(CONSENT_KEY, value);
    var g = value === "granted" ? "granted" : "denied";
    gtag("consent", "update", { ad_storage: g, ad_user_data: g, ad_personalization: g, analytics_storage: g });
    var b = $(".consent"); if (b) b.remove();
  }
  function showConsent(force) {
    if ((!force && store(CONSENT_KEY)) || $(".consent")) return;
    var box = doc.createElement("div");
    box.className = "consent"; box.setAttribute("role", "dialog"); box.setAttribute("aria-label", "Privacy choices");
    var policy = doc.querySelector('a[href$="privacy-policy/"]');
    box.innerHTML = '<p>We use cookies for analytics and to show ads that keep CalcMyFin free. Your calculator inputs never leave your device. ' +
      (policy ? '<a href="' + policy.getAttribute("href") + '">Privacy policy</a>' : "") + '</p>' +
      '<div class="btns"><button class="primary" data-c="granted">Accept</button><button class="secondary" data-c="denied">Opt out of cookies</button></div>';
    box.addEventListener("click", function (e) { var c = e.target.getAttribute("data-c"); if (c) { setConsent(c); track("consent_choice", { choice: c }); } });
    doc.body.appendChild(box);
  }

  /* ---------------- analytics ---------------- */
  // Only measure the live site, so local previews and tests don't pollute the reports
  var liveHost = /(^|\.)calcmyfin\.com$/.test(location.hostname);
  var gaOn = !!CFG.ga4Id && liveHost;
  if (gaOn) {
    loadScript("https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(CFG.ga4Id));
    gtag("js", new Date());
    gtag("config", CFG.ga4Id, { page_title: doc.title });
  }
  function track(name, params) {
    if (gaOn) gtag("event", name, params || {});
  }

  /* ---------------- ads ---------------- */
  var ads = CFG.adsense || {};
  if (qs.get("ads") === "preview") root.classList.add("ads-preview");
  function initAds() {
    if (!ads.client) return;
    root.classList.add("ads-on");
    loadScript("https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + encodeURIComponent(ads.client), { crossorigin: "anonymous" });
    var slots = ads.slots || {};
    $$(".ad[data-ad]").forEach(function (el) {
      var id = slots[el.getAttribute("data-ad")];
      if (!id) { el.parentNode.style.display = "none"; return; }  // unconfigured: let Auto ads decide
      el.innerHTML = '<span class="ad-label">Advertisement</span><ins class="adsbygoogle" style="display:block" data-ad-client="' +
        ads.client + '" data-ad-slot="' + id + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { (window.adsbygoogle = window.adsbygoogle || []).push({}); } catch (e) {}
    });
  }
  (CFG.extraAdScripts || []).forEach(function (src) { if (src) loadScript(src); });

  /* ---------------- partner offers ---------------- */
  /* Partner offers: shown under the result only when config.js has offers for this page's group.
     Preview the layout with ?offers=preview (example offers, links go nowhere). */
  var PREVIEW_OFFERS = [
    { name: "Example partner A", text: "This is where an approved offer's short description appears.", cta: "See rates", url: "#", badge: "Example" },
    { name: "Example partner B", text: "A second offer. Up to three fit side by side on desktop.", cta: "Check eligibility", url: "#" }
  ];
  function initPartners() {
    var box = $(".partner[data-partner]"); if (!box) return;
    var group = box.getAttribute("data-partner");
    var p = (CFG.partners || {})[group] || {};
    var offers = qs.get("offers") === "preview" ? PREVIEW_OFFERS : (p.offers || []);
    if (!offers.length) return;
    var html = '<div class="partner-box"><div class="partner-head"><h2>' + esc(p.title || "Recommended next step") +
      '</h2><span class="sponsored">Sponsored</span></div><p class="partner-hook" hidden></p><div class="offers">';
    offers.forEach(function (o, i) {
      html += '<div class="offer">' + (o.badge ? '<span class="offer-badge">' + esc(o.badge) + '</span>' : "") +
        '<strong>' + esc(o.name) + '</strong><p>' + esc(o.text || "") + '</p><a class="btn" href="' +
        esc(o.url) + '" target="_blank" rel="sponsored noopener" data-offer="' + esc(o.name) + '" data-pos="' + (i + 1) + '">' +
        esc(o.cta || "Learn more") + '</a>' + (o.fine ? '<small class="offer-fine">' + esc(o.fine) + '</small>' : "") + '</div>';
    });
    html += '</div><p class="partner-note">We may earn a commission if you sign up through these links, at no cost to you. It never affects our calculators. <a href="' +
      esc((doc.querySelector('a[href$="disclaimer/"]') || { getAttribute: function () { return "#"; } }).getAttribute("href")) + '">Advertiser disclosure</a></p></div>';
    box.innerHTML = html; box.hidden = false;

    // Personal headline: fill {element-id} tokens with the visitor's current results
    var tpl = box.getAttribute("data-hook") || "", hookEl = $(".partner-hook", box);
    function updateHook() {
      if (!tpl) return;
      var ok = true;
      var text = tpl.replace(/\{([a-z0-9-]+)\}/g, function (_, id) {
        var el = doc.getElementById(id), v = el ? el.textContent.trim() : "";
        if (!v || v === "—" || /not reached|above \$1/i.test(v)) ok = false;
        return v;
      });
      hookEl.textContent = text; hookEl.hidden = !ok;
    }
    // calculator scripts load after this one, so refresh once they've produced their first result
    updateHook();
    if (doc.readyState !== "complete") window.addEventListener("load", updateHook);
    doc.addEventListener("DOMContentLoaded", updateHook);
    var shell = $(".calc-shell");
    if (shell) ["input", "change", "click"].forEach(function (ev) { shell.addEventListener(ev, function () { setTimeout(updateHook, 0); }); });

    box.addEventListener("click", function (e) {
      var a = e.target.closest("a[data-offer]");
      if (a) track("affiliate_click", { offer: a.getAttribute("data-offer"), position: a.getAttribute("data-pos"), offer_group: group, calculator: calcName() });
    });
    if ("IntersectionObserver" in window) {
      var seen = new IntersectionObserver(function (entries) {
        if (entries[0].isIntersecting) { track("affiliate_view", { offer_group: group, calculator: calcName() }); seen.disconnect(); }
      }, { threshold: 0.5 });
      seen.observe(box);
    }
  }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }
  function calcName() { var m = $("main[data-calc]"); return m ? m.getAttribute("data-calc") : "home"; }

  /* ---------------- calculator helpers: share / print / reset ---------------- */
  // read-only fields (e.g. a live price) are never shared, restored or reset
  function fields() { return $$(".calc-shell input[id]:not([readonly]), .calc-shell select[id]"); }
  function fire(el) { el.dispatchEvent(new Event("input", { bubbles: true })); el.dispatchEvent(new Event("change", { bubbles: true })); }
  function initCalc() {
    var shell = $(".calc-shell"); if (!shell) return;
    var defaults = {};
    fields().forEach(function (el) { defaults[el.id] = el.value; });
    // restore values from a shared link
    var applied = false;
    fields().forEach(function (el) {
      if (qs.has(el.id)) { el.value = qs.get(el.id); applied = true; }
    });
    if (applied) setTimeout(function () { fields().forEach(fire); track("shared_link_open", { calculator: calcName() }); }, 60);

    var started = false;
    shell.addEventListener("input", function () {
      if (!started) { started = true; track("calculator_start", { calculator: calcName() }); }
    });
    var share = $("[data-share]"), print = $("[data-print]"), reset = $("[data-reset]");
    if (share) share.addEventListener("click", function () {
      var p = new URLSearchParams();
      fields().forEach(function (el) { if (el.value !== "") p.set(el.id, el.value); });
      var url = location.origin + location.pathname + "?" + p.toString();
      var done = function () { var t = share.querySelector("span"); share.classList.add("done"); t.textContent = "Link copied!"; setTimeout(function () { share.classList.remove("done"); t.textContent = "Copy link to these results"; }, 2200); };
      if (navigator.clipboard) navigator.clipboard.writeText(url).then(done, function () { prompt("Copy this link:", url); });
      else prompt("Copy this link:", url);
      history.replaceState(null, "", url);
      track("share_results", { calculator: calcName() });
    });
    if (print) print.addEventListener("click", function () { track("print_results", { calculator: calcName() }); window.print(); });
    if (reset) reset.addEventListener("click", function () {
      fields().forEach(function (el) { if (el.id in defaults) { el.value = defaults[el.id]; fire(el); } });
      history.replaceState(null, "", location.pathname);
      track("reset_calculator", { calculator: calcName() });
    });
  }

  /* ---------------- homepage search ---------------- */
  var CMF = window.CMF = window.CMF || {};
  CMF.initSearch = function () {
    var input = $("#calc-search"); if (!input) return;
    var t;
    input.addEventListener("input", function () {
      var q = input.value.trim().toLowerCase(), any = false;
      $$(".home .tool-card").forEach(function (card) {
        var hit = !q || card.getAttribute("data-search").indexOf(q) > -1 || q.split(/\s+/).every(function (w) { return card.getAttribute("data-search").indexOf(w) > -1; });
        card.hidden = !hit; if (hit) any = true;
      });
      $$(".cat-section, .popular").forEach(function (sec) { sec.hidden = !$$(".tool-card", sec).some(function (c) { return !c.hidden; }); });
      $(".no-results").hidden = any;
      clearTimeout(t); if (q) t = setTimeout(function () { track("search", { search_term: q }); }, 900);
    });
  };

  /* ---------------- nav ---------------- */
  function initNav() {
    var toggle = $(".nav-toggle"), menu = $("#site-menu"), mega = $(".has-mega"), btn = $(".mega-btn");
    if (toggle) toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open"); toggle.setAttribute("aria-expanded", open);
    });
    if (btn) btn.addEventListener("click", function (e) {
      e.stopPropagation(); var open = mega.classList.toggle("open"); btn.setAttribute("aria-expanded", open);
    });
    doc.addEventListener("click", function (e) { if (mega && !mega.contains(e.target)) { mega.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); } });
    doc.addEventListener("keydown", function (e) { if (e.key === "Escape" && mega) { mega.classList.remove("open"); btn.setAttribute("aria-expanded", "false"); } });
  }

  /* ---------------- generic tracking ---------------- */
  function initTracking() {
    doc.addEventListener("click", function (e) {
      var a = e.target.closest("a"); if (!a) return;
      if (a.hostname && a.hostname !== location.hostname && !a.hasAttribute("data-offer")) track("outbound_click", { link_url: a.href, calculator: calcName() });
      if (a.closest(".tool-card")) track("select_calculator", { destination: a.getAttribute("href"), from: calcName() });
      if (a.hasAttribute("data-consent-open")) { e.preventDefault(); showConsent(true); }
    });
    $$(".faq").forEach(function (d) { d.addEventListener("toggle", function () { if (d.open) track("faq_open", { question: d.querySelector("summary").textContent, calculator: calcName() }); }); });
  }

  function ready() {
    $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
    initNav(); initCalc(); initPartners(); initTracking();
    if (doc.readyState === "complete") initAds(); else window.addEventListener("load", initAds);
    setTimeout(function () { showConsent(false); }, 1200);
  }
  if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", ready); else ready();
})();
