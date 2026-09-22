function calcSavingsGoal() {
  const goal = readNumber('sg-goal'), cur = readNumber('sg-current');
  const years = clamp(document.getElementById('sg-years').value, 0, 60), extraMonths = clamp(document.getElementById('sg-months').value, 0, 11);
  const apy = clamp(document.getElementById('sg-apy').value, 0, 30);
  const n = Math.round(years * 12 + extraMonths);
  const i = Math.pow(1 + apy / 100, 1 / 12) - 1;
  const grown = cur * Math.pow(1 + i, n);
  let pmt;
  if (n === 0) pmt = Math.max(0, goal - cur);
  else if (grown >= goal) pmt = 0;
  else pmt = i === 0 ? (goal - grown) / n : (goal - grown) * i / (Math.pow(1 + i, n) - 1);
  const deposits = n === 0 ? pmt : pmt * n;
  const finalBal = n === 0 ? cur + pmt : Math.max(goal, grown);
  const interest = Math.max(0, finalBal - cur - deposits);
  setText('sg-monthly', money(pmt, 2));
  setText('sg-deposits', money(deposits));
  setText('sg-interest', money(interest));
  setText('sg-nointerest', n ? money(Math.max(0, goal - cur) / n, 2) + '/mo' : '—');
  // growth chart (yearly points; monthly if under 2 years)
  const C = window.CMFChart && CMFChart.colors;
  if (C && n > 0) {
    const step = n <= 24 ? 1 : 12, labels = [], contrib = [], earned = [];
    let bal = cur;
    for (let m = 0; m <= n; m++) {
      if (m > 0) bal = bal * (1 + i) + pmt;
      if (m % step === 0 || m === n) {
        const c = cur + pmt * m;
        labels.push(step === 1 ? 'M' + m : 'Yr ' + (m / 12).toFixed(m % 12 ? 1 : 0));
        contrib.push(c); earned.push(Math.max(0, bal - c));
      }
    }
    CMFChart.area(document.getElementById('sg-chart'), labels, [
      { label: 'What you put in', color: C.brand, values: contrib }, { label: 'Growth', color: C.gold, values: earned }]);
  } else if (C) document.getElementById('sg-chart').innerHTML = '';
  let note;
  if (goal === 0) note = 'Enter a savings goal to get started.';
  else if (cur >= goal) note = 'You have already reached this goal. Nice work!';
  else if (pmt === 0) note = `Your current savings should grow to your goal on their own at a ${percent(apy)} return.`;
  else if (n === 0) note = 'Add a timeline to spread the goal into monthly amounts.';
  else if (apy === 0) note = `Setting aside ${money(pmt, 2)} a month for ${yearsMonths(n)} reaches ${money(goal)}.`;
  else note = `Setting aside ${money(pmt, 2)} a month for ${yearsMonths(n)} reaches ${money(goal)}, with about ${money(interest)} coming from investment growth. Returns aren't guaranteed.`;
  setMessage('sg-note', note);
}
bindInputs(['sg-goal', 'sg-current', 'sg-years', 'sg-months', 'sg-apy'], calcSavingsGoal);
calcSavingsGoal();
