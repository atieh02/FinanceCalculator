function rbNum(id, min, max) { return clamp(document.getElementById(id).value, min, max); }
function calcRentBuy() {
  const price = readNumber('rb-price', 0, 1e8), downPct = rbNum('rb-down', 0, 100), rate = rbNum('rb-rate', 0, 30);
  const term = Number(document.getElementById('rb-term').value) || 30, tax = rbNum('rb-tax', 0, 10) / 100;
  const ins = readNumber('rb-ins', 0, 1e6), maint = rbNum('rb-maint', 0, 10) / 100, hoa = readNumber('rb-hoa', 0, 1e5);
  const buyCost = rbNum('rb-buycost', 0, 20) / 100, sellCost = rbNum('rb-sellcost', 0, 20) / 100, appr = rbNum('rb-appr', -10, 20) / 100;
  const rent = readNumber('rb-rent', 0, 1e6), rentInc = rbNum('rb-rentinc', 0, 20) / 100, rentIns = readNumber('rb-rentins', 0, 1e5);
  const years = Math.round(rbNum('rb-years', 1, 30)), ret = rbNum('rb-return', 0, 20) / 100;
  const down = price * downPct / 100, loan = price - down, pay = loan ? fixedPayment(loan, rate, term) : 0;
  const r = rate / 100 / 12, gHome = Math.pow(1 + appr, 1 / 12), gInv = Math.pow(1 + ret, 1 / 12) - 1;
  let value = price, bal = loan, buyerPort = 0, renterPort = down + price * buyCost, breakeven = null;
  let buyMonth1 = 0, rentMonth1 = 0, buyW = 0, rentW = 0;
  for (let m = 1; m <= years * 12; m++) {
    const g = Math.pow(1 + rentInc, Math.floor((m - 1) / 12));
    let mortgage = 0;
    if (bal > 0.005) { const it = bal * r, p = Math.min(bal + it, pay); bal = bal + it - p; mortgage = p; }
    const own = mortgage + value * tax / 12 + value * maint / 12 + ins / 12 * g + hoa * g;
    const rentCost = rent * g + rentIns / 12 * g;
    if (m === 1) { buyMonth1 = own; rentMonth1 = rentCost; }
    value *= gHome;
    buyerPort *= 1 + gInv; renterPort *= 1 + gInv;
    if (own > rentCost) renterPort += own - rentCost; else buyerPort += rentCost - own;
    buyW = value * (1 - sellCost) - bal + buyerPort; rentW = renterPort;
    if (m % 12 === 0 && breakeven === null && buyW >= rentW) breakeven = m / 12;
  }
  const buyWins = buyW >= rentW, diff = Math.abs(buyW - rentW);
  setText('rb-yrs', years);
  setText('rb-verdict', price ? (buyWins ? 'Buying' : 'Renting') : '—');
  setText('rb-buy-wealth', money(buyW));
  setText('rb-rent-wealth', money(rentW));
  setText('rb-buy-month', money(buyMonth1));
  setText('rb-rent-month', money(rentMonth1));
  setText('rb-breakeven', breakeven ? `${breakeven} year${breakeven === 1 ? '' : 's'}` : `More than ${years} years`);
  document.getElementById('rb-buy-card').classList.toggle('best', !!price && buyWins);
  document.getElementById('rb-rent-card').classList.toggle('best', !!price && !buyWins);
  let note;
  if (!price) note = 'Enter a home price to compare.';
  else note = `${buyWins ? 'Buying' : 'Renting'} leaves you about ${money(diff)} wealthier after ${years} year${years === 1 ? '' : 's'}.` +
    (breakeven ? ` Buying pulls ahead in year ${breakeven}, so it pays off if you stay at least that long.` : ` Buying didn't catch up within ${years} years. Try a longer stay.`) +
    (downPct < 20 ? ' PMI isn\'t included, so with under 20% down buying costs a bit more than shown.' : '');
  setMessage('rb-note', note);
}
bindInputs(['rb-price', 'rb-down', 'rb-rate', 'rb-tax', 'rb-ins', 'rb-maint', 'rb-hoa', 'rb-buycost', 'rb-sellcost', 'rb-appr', 'rb-rent', 'rb-rentinc', 'rb-rentins', 'rb-years', 'rb-return'], calcRentBuy);
document.getElementById('rb-term').addEventListener('change', calcRentBuy);
calcRentBuy();
