function amStart() {
  const v = document.getElementById('am-start').value;
  const m = /^(\d{4})-(\d{2})$/.exec(v || '');
  if (m) return { y: +m[1], m: +m[2] - 1 };
  const d = new Date(); d.setMonth(d.getMonth() + 1);
  return { y: d.getFullYear(), m: d.getMonth() };
}
function monthLabel(start, i) {
  const t = start.m + i;
  return new Date(start.y + Math.floor(t / 12), t % 12, 1).toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
}
function calcAmort() {
  const amount = readNumber('am-amount', 0, 1e8), rate = clamp(document.getElementById('am-rate').value, 0, 50);
  const term = clamp(document.getElementById('am-term').value, 1, 50), extra = readNumber('am-extra', 0, 1e7);
  const view = document.getElementById('am-view').value, start = amStart();
  const payment = amount ? fixedPayment(amount, rate, term) : 0, r = rate / 100 / 12;
  const rows = [], yearly = [];
  let b = amount, interest = 0, i = 0;
  while (b > 0.005 && i < term * 12) {
    const it = b * r, prin = Math.min(b, payment + extra - it);
    b -= prin; interest += it;
    rows.push({ label: monthLabel(start, i), prin, it, b: Math.max(0, b) });
    const yi = Math.floor(i / 12);
    if (!yearly[yi]) yearly[yi] = { label: 'Year ' + (yi + 1), prin: 0, it: 0, b: 0 };
    yearly[yi].prin += prin; yearly[yi].it += it; yearly[yi].b = Math.max(0, b);
    i++;
  }
  setText('am-payment', money(payment, 2));
  setText('am-interest', money(interest));
  setText('am-total', money(amount + interest));
  setText('am-count', whole(rows.length));
  setText('am-payoff', rows.length ? rows[rows.length - 1].label : '—');
  const list = view === 'month' ? rows : yearly;
  document.getElementById('am-col').textContent = view === 'month' ? 'Payment' : 'Year';
  document.getElementById('am-rows').innerHTML = list.map(x =>
    `<tr><td>${x.label}</td><td>${money(x.prin, 2)}</td><td>${money(x.it, 2)}</td><td>${money(x.b, 2)}</td></tr>`).join('');
  const C = window.CMFChart && CMFChart.colors;
  if (C && yearly.length) {
    let cp = 0, ci = 0;
    const labels = ['Start'], prinVals = [0], intVals = [0];
    yearly.forEach((y, k) => { cp += y.prin; ci += y.it; labels.push('Yr ' + (k + 1)); prinVals.push(cp); intVals.push(ci); });
    CMFChart.area(document.getElementById('am-chart'), labels, [
      { label: 'Principal paid', color: C.brand, values: prinVals }, { label: 'Interest paid', color: C.coral, values: intVals }]);
  }
  let note = '';
  if (!amount) note = 'Enter a loan amount to build the schedule.';
  else if (rows.length) {
    const first = rows[0];
    note = `Your first payment is ${Math.round(first.it / (first.it + first.prin) * 100)}% interest.` +
      (extra ? ` Paying ${money(extra)} extra finishes ${yearsMonths(term * 12 - rows.length)} early.` : ' Add an extra monthly payment to see how much sooner you could finish.');
  }
  setMessage('am-note', note);
}
bindInputs(['am-amount', 'am-rate', 'am-term', 'am-extra', 'am-start'], calcAmort);
['am-view', 'am-start'].forEach(id => document.getElementById(id).addEventListener('change', calcAmort));
calcAmort();
