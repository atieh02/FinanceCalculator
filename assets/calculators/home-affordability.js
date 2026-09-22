function calcAfford() {
  const val = id => document.getElementById(id).value;
  const income = readNumber('ha-income'), debts = readNumber('ha-debts'), down = readNumber('ha-down');
  const rate = clamp(val('ha-rate'), 0, LIMITS.RATE_MAX), years = Number(val('ha-term')) || 30;
  const taxRate = clamp(val('ha-tax'), 0, 10), ins = readNumber('ha-ins', 0, 1e6), hoa = readNumber('ha-hoa', 0, 1e5);
  const [front, back] = val('ha-dti').split('/').map(Number);
  const gm = income / 12;
  const frontCap = gm * front / 100, backCap = gm * back / 100 - debts;
  const maxPay = Math.max(0, Math.min(frontCap, backCap));
  const f = fixedPayment(1, rate, years), t = taxRate / 100 / 12, fixed = ins / 12 + hoa;
  let price = (maxPay - fixed + f * down) / (f + t);
  if (!Number.isFinite(price) || price < down) {
    // even with no loan, taxes/insurance on a home worth the down payment exceed the budget
    price = t > 0 ? Math.min(down, Math.max(0, (maxPay - fixed) / t)) : (maxPay >= fixed ? down : 0);
  }
  price = Math.max(0, Math.min(price, LIMITS.OUTPUT_MAX));
  const loan = Math.max(0, price - down), pi = loan * f, tih = price * t + fixed;
  setText('ha-price', money(price));
  setText('ha-payment', money(maxPay, 2));
  setText('ha-loan', money(loan));
  setText('ha-pi', money(pi, 2));
  setText('ha-tih', money(tih, 2));
  setText('ha-downpct', price > 0 ? percent(Math.min(100, down / price * 100), 1) : '—');
  const C = window.CMFChart && CMFChart.colors;
  if (C) CMFChart.donut(document.getElementById('ha-chart'), [
    { label: 'Principal & interest', value: pi, color: C.brand }, { label: 'Property tax', value: price * t, color: C.gold },
    { label: 'Insurance', value: ins / 12, color: C.slate }, { label: 'HOA', value: hoa, color: C.indigo }]);
  let note;
  if (income === 0) note = 'Enter your annual income to see an estimate.';
  else if (maxPay === 0) note = 'Your monthly debts already exceed the back-end limit, so no housing payment fits these guidelines. Paying down debt would raise your range.';
  else {
    const binding = frontCap <= backCap ? `the ${front}% housing limit` : `the ${back}% total-debt limit (your other debts are the constraint)`;
    note = `Your budget is set by ${binding}. ` + (down / Math.max(price, 1) < 0.2 ? 'With under 20% down, a conventional loan would usually add PMI, which isn\'t included here.' : 'With 20%+ down you would typically avoid PMI.');
  }
  setMessage('ha-note', note);
}
bindInputs(['ha-income', 'ha-debts', 'ha-down', 'ha-rate', 'ha-term', 'ha-tax', 'ha-ins', 'ha-hoa', 'ha-dti'], calcAfford);
['ha-term', 'ha-dti'].forEach(id => document.getElementById(id).addEventListener('change', calcAfford));
calcAfford();
