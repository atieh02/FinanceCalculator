function riRun(savings, w0, i, infl, cap) {
  let b = savings, w = w0, m = 0, total = 0;
  const yearly = [savings];
  while (b > 0 && m < cap) {
    if (m && m % 12 === 0) w *= 1 + infl;
    const take = Math.min(w, b * (1 + i));
    b = b * (1 + i) - take; total += take; m++;
    if (m % 12 === 0) yearly.push(Math.max(0, b));
  }
  return { months: m, left: b, total, yearly };
}
function calcRetIncome() {
  const savings = readNumber('ri-savings', 0, 1e9), w = readNumber('ri-withdraw', 0, 1e7);
  const i = clamp(document.getElementById('ri-return').value, 0, 15) / 100 / 12, infl = clamp(document.getElementById('ri-infl').value, 0, 15) / 100;
  const horizon = Math.round(clamp(document.getElementById('ri-years').value, 1, 60));
  const r = riRun(savings, w, i, infl, 1200);
  const forever = r.left > 0;
  // sustainable starting withdrawal for the chosen horizon (binary search)
  let lo = 0, hi = Math.max(1, savings);
  for (let k = 0; k < 60; k++) { const mid = (lo + hi) / 2; if (riRun(savings, mid, i, infl, horizon * 12).left > 0) lo = mid; else hi = mid; }
  setText('ri-lasts', !savings || !w ? '—' : forever ? '100+ years' : yearsMonths(r.months));
  setText('ri-sustain', savings ? money(lo) : '—');
  setText('ri-years-label', horizon);
  setText('ri-rate', savings ? percent(w * 12 / savings * 100, 1) : '—');
  setText('ri-total', money(r.total));
  const C = window.CMFChart && CMFChart.colors;
  if (C && savings && w && r.yearly.length > 1) {
    const vals = r.yearly.slice(0, 61), labels = vals.map((_, k) => 'Yr ' + k);
    CMFChart.area(document.getElementById('ri-chart'), labels, [{ label: 'Savings balance', color: C.brand, values: vals }]);
  } else if (C) document.getElementById('ri-chart').innerHTML = '';
  let note;
  if (!savings) note = 'Enter your savings to see how long they last.';
  else if (!w) note = 'Enter a monthly withdrawal.';
  else {
    const rate = w * 12 / savings * 100;
    note = (forever ? 'At this pace your savings keep growing faster than you spend them.' : `Withdrawals of ${money(w)} a month, rising with inflation, run out after ${yearsMonths(r.months)}.`) +
      ` Your first-year withdrawal rate is ${percent(rate, 1)}${rate > 5 ? ', above the 3–5% range many experts suggest' : rate >= 3 ? ', within the 3–5% range many experts suggest' : ''}. To last ${horizon} years, start at about ${money(lo)} a month.`;
  }
  setMessage('ri-note', note);
}
bindInputs(['ri-savings', 'ri-withdraw', 'ri-return', 'ri-infl', 'ri-years'], calcRetIncome);
calcRetIncome();
