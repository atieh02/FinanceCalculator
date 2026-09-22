function calcInflation() {
  const amount = readNumber('in-amount'), years = clamp(document.getElementById('in-years').value, 1, 100);
  const rate = clamp(document.getElementById('in-rate').value, -10, 50);
  const g = 1 + rate / 100;
  const future = amount * Math.pow(g, years), power = amount / Math.pow(g, years);
  setText('in-future', money(future, 2));
  setText('in-power', money(power, 2));
  setText('in-lost', amount > 0 ? percent((1 - power / amount) * 100, 1) : '—');
  setText('in-double', rate > 0 ? (Math.log(2) / Math.log(g)).toFixed(1) + ' years' : 'Never');
  const C = window.CMFChart && CMFChart.colors;
  if (C) {
    const labels = [], cost = [], step = years > 40 ? 5 : years > 15 ? 2 : 1;
    for (let y = 0; y <= years; y += step) { labels.push('Yr ' + y); cost.push(amount * Math.pow(g, y)); }
    if ((years % step) !== 0) { labels.push('Yr ' + years); cost.push(future); }
    CMFChart.area(document.getElementById('in-chart'), labels, [{ label: `Cost of ${money(amount)} of today's goods`, color: C.coral, values: cost }]);
  }
  setMessage('in-note', amount === 0 ? 'Enter an amount to see the effect of inflation.' :
    rate <= 0 ? 'With zero or negative inflation (deflation), money keeps or gains purchasing power.' :
      `At ${percent(rate)} a year, prices rise ${percent((future / amount - 1) * 100, 0)} over ${years} years. Money earning less than ${percent(rate)} loses real value.`);
}
bindInputs(['in-amount', 'in-years', 'in-rate'], calcInflation);
calcInflation();
