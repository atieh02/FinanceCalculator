const TROY_OZ_G = 31.1034768;
// Fallback prices, used only if the live price service can't be reached (approximate, September 2026).
const GS_METALS = {
  gold: { symbol: 'XAU', fallback: 4340, purity: '0.999' },
  silver: { symbol: 'XAG', fallback: 66, purity: '0.999' },
  platinum: { symbol: 'XPT', fallback: 1800, purity: '0.999' }
};
const GS_API = 'https://api.gold-api.com/price/';
const GS_CACHE_MS = 5 * 60 * 1000;
// A spot price from a shared link counts as the visitor's own; never overwrite it with the live price.
let gsSpotEdited = new URLSearchParams(location.search).has('gs-spot');

function calcGold() {
  const metal = document.getElementById('gs-metal').value;
  const purity = clamp(document.getElementById('gs-purity').value, 0, 1);
  const weight = readNumber('gs-weight', 0, 1e7), unitG = Number(document.getElementById('gs-unit').value) || 1;
  const spot = readNumber('gs-spot', 0, 1e6), premium = clamp(document.getElementById('gs-premium').value, 0, 100) / 100;
  const grams = weight * unitG, pureOz = grams * purity / TROY_OZ_G, value = pureOz * spot;
  setText('gs-value', money(value, 2));
  setText('gs-pure', `${pureOz.toLocaleString('en-US', { maximumFractionDigits: 3 })} troy oz (${(pureOz * TROY_OZ_G).toLocaleString('en-US', { maximumFractionDigits: 2 })} g)`);
  setText('gs-pergram', money(spot * purity / TROY_OZ_G, 2));
  setText('gs-buy', money(value * (1 + premium), 2));
  const name = metal[0].toUpperCase() + metal.slice(1);
  setMessage('gs-note', !weight ? 'Enter a weight to see the value.' :
    `Based on ${money(spot, 2)} per troy ounce of pure ${metal}. Spot prices move throughout the day. ${name} jewelry or scrap usually sells for less than its metal value.`);
}

function gsStatus(text) { const el = document.getElementById('gs-live'); if (el) el.textContent = text; }

function gsCached(symbol) {
  try {
    const c = JSON.parse(sessionStorage.getItem('cmf-spot-' + symbol) || 'null');
    return c && Date.now() - c.t < GS_CACHE_MS ? c : null;
  } catch (e) { return null; }
}

async function gsLivePrice(metal) {
  const m = GS_METALS[metal];
  const cached = gsCached(m.symbol);
  if (cached) return cached;
  const ctrl = new AbortController(), timer = setTimeout(() => ctrl.abort(), 6000);
  try {
    const res = await fetch(GS_API + m.symbol, { signal: ctrl.signal, cache: 'no-store' });
    const data = await res.json();
    const price = Number(data.price);
    if (!res.ok || !Number.isFinite(price) || price <= 0) throw new Error('bad price');
    const out = { price: Math.round(price * 100) / 100, at: data.updatedAt || new Date().toISOString(), t: Date.now() };
    try { sessionStorage.setItem('cmf-spot-' + m.symbol, JSON.stringify(out)); } catch (e) { /* storage unavailable */ }
    return out;
  } finally { clearTimeout(timer); }
}

async function gsLoadLive() {
  const metal = document.getElementById('gs-metal').value;
  if (gsSpotEdited) { gsStatus('Using the price you entered.'); return; }
  gsStatus('Loading the live spot price…');
  try {
    const live = await gsLivePrice(metal);
    if (gsSpotEdited || document.getElementById('gs-metal').value !== metal) return;
    document.getElementById('gs-spot').value = live.price;
    const time = new Date(live.at).toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' });
    gsStatus(`Live spot price, updated ${time}. You can type your own.`);
  } catch (e) {
    if (gsSpotEdited) return;
    document.getElementById('gs-spot').value = GS_METALS[metal].fallback;
    gsStatus('Live price unavailable right now, so a recent price is shown. Enter today\'s price for an exact value.');
  }
  calcGold();
}

document.getElementById('gs-spot').addEventListener('input', e => {
  if (e.isTrusted) { gsSpotEdited = true; gsStatus('Using the price you entered.'); }
});
document.getElementById('gs-metal').addEventListener('change', e => {
  // Shared links and Reset re-apply values programmatically: keep their spot price and just recalculate
  if (!e.isTrusted) { calcGold(); return; }
  const d = GS_METALS[document.getElementById('gs-metal').value];
  document.getElementById('gs-purity').value = d.purity;
  gsSpotEdited = false;
  document.getElementById('gs-spot').value = d.fallback;
  calcGold();
  gsLoadLive();
});
bindInputs(['gs-weight', 'gs-spot', 'gs-premium'], calcGold);
['gs-purity', 'gs-unit'].forEach(id => document.getElementById(id).addEventListener('change', calcGold));
calcGold();
gsLoadLive();
