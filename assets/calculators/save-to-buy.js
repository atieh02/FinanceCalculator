function calcSaveToBuy() {
  const price = readNumber('sb-price', 0, 1e8), saved = readNumber('sb-saved', 0, 1e8), monthly = readNumber('sb-monthly', 0, 1e7);
  const rise = clamp(document.getElementById('sb-rise').value, 0, 30) / 100, ret = clamp(document.getElementById('sb-return').value, 0, 20) / 100;
  const i = Math.pow(1 + ret, 1 / 12) - 1;
  const target = m => price * Math.pow(1 + rise, m / 12);
  let bal = saved, m = 0;
  const labels = ['Now'], put = [saved], grow = [0];
  while (bal < target(m) && m < LIMITS.MONTHS_MAX) {
    m++;
    bal = bal * (1 + i) + monthly;
    if (m % 12 === 0) { labels.push('Yr ' + m / 12); put.push(saved + monthly * m); grow.push(Math.max(0, bal - saved - monthly * m)); }
  }
  const reached = bal >= target(m);
  const contrib = monthly * m, growth = Math.max(0, bal - saved - contrib);
  const when = new Date(); when.setMonth(when.getMonth() + m);
  setText('sb-time', !price ? '—' : reached ? (m === 0 ? 'Right now' : yearsMonths(m)) : 'Not reached');
  setText('sb-date', reached && price ? when.toLocaleDateString('en-US', { month: 'long', year: 'numeric' }) : '—');
  setText('sb-price-then', price ? money(target(m)) : '—');
  setText('sb-contrib', money(contrib));
  setText('sb-growth', money(growth));
  const C = window.CMFChart && CMFChart.colors;
  if (C && reached && m >= 12) {
    if (m % 12) { labels.push(yearsMonths(m)); put.push(saved + contrib); grow.push(growth); }
    CMFChart.area(document.getElementById('sb-chart'), labels, [
      { label: 'What you set aside', color: C.brand, values: put }, { label: 'Growth', color: C.gold, values: grow }]);
  } else if (C) document.getElementById('sb-chart').innerHTML = '';
  let note;
  if (!price) note = 'Enter a price to see when you can buy.';
  else if (m === 0) note = 'You already have enough to buy it outright.';
  else if (!reached) note = 'At this pace the price rises faster than your savings. Try setting aside more each month.';
  else {
    const extra = Math.max(50, Math.round(monthly * 0.25 / 10) * 10);
    let b2 = saved, m2 = 0;
    while (b2 < target(m2) && m2 < LIMITS.MONTHS_MAX) { m2++; b2 = b2 * (1 + i) + monthly + extra; }
    note = `Setting aside ${money(monthly)} a month gets you there in ${yearsMonths(m)}, with no borrowing. Adding ${money(extra)} more a month would get you there ${yearsMonths(m - m2)} sooner.`;
  }
  setMessage('sb-note', note);
}
bindInputs(['sb-price', 'sb-saved', 'sb-monthly', 'sb-rise', 'sb-return'], calcSaveToBuy);
calcSaveToBuy();
