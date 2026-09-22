function payoffRun(balance, rate, payment, extra, lump) {
  const r = rate / 100 / 12;
  let b = Math.max(0, balance - lump), interest = 0, months = 0;
  while (b > 0.005 && months < LIMITS.MONTHS_MAX) {
    const it = b * r;
    const pay = Math.min(b + it, payment + extra);
    if (pay <= it) return { months: Infinity, interest: Infinity };
    interest += it; b = b + it - pay; months++;
  }
  return { months, interest };
}
function calcPayoff() {
  const balance = readNumber('mp-balance', 0, 1e8), rate = clamp(document.getElementById('mp-rate').value, 0, 30);
  const years = clamp(document.getElementById('mp-years').value, 1, 40), extra = readNumber('mp-extra', 0, 1e7), lump = readNumber('mp-lump', 0, 1e8);
  const payment = balance ? fixedPayment(balance, rate, years) : 0;
  const base = payoffRun(balance, rate, payment, 0, 0), fast = payoffRun(balance, rate, payment, extra, lump);
  const savedMonths = base.months - fast.months, savedInt = base.interest - fast.interest;
  setText('mp-payment', money(payment, 2));
  setText('mp-oldtime', yearsMonths(base.months));
  setText('mp-newtime', yearsMonths(fast.months));
  setText('mp-newint', money(fast.interest));
  setText('mp-saved-int', money(Math.max(0, savedInt)));
  setText('mp-saved-time', savedMonths > 0 ? yearsMonths(savedMonths) : '0 months');
  const C = window.CMFChart && CMFChart.colors;
  if (C) CMFChart.donut(document.getElementById('mp-chart'), [
    { label: 'Principal', value: balance, color: C.brand },
    { label: 'Interest you pay', value: fast.interest, color: C.coral },
    { label: 'Interest saved', value: Math.max(0, savedInt), color: C.gold }]);
  let note;
  if (!balance) note = 'Enter your loan balance to see your payoff date.';
  else if (!extra && !lump) note = `Try adding an extra amount. Even ${money(Math.max(25, Math.round(payment / 12 / 5) * 5))} a month makes a difference.`;
  else note = `Paying ${extra ? money(extra) + ' extra a month' : ''}${extra && lump ? ' and ' : ''}${lump ? money(lump) + ' now' : ''} clears the loan in ${yearsMonths(fast.months)} instead of ${yearsMonths(base.months)}, keeping ${money(savedInt)} of interest in your pocket.`;
  setMessage('mp-note', note);
}
bindInputs(['mp-balance', 'mp-rate', 'mp-years', 'mp-extra', 'mp-lump'], calcPayoff);
calcPayoff();
