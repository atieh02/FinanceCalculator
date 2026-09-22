function calcFire() {
  const age = Math.round(clamp(document.getElementById('fi-age').value, 16, 90));
  const spend = readNumber('fi-spend', 0, 1e8), invested = readNumber('fi-invested', 0, 1e9), save = readNumber('fi-save', 0, 1e8);
  const ret = clamp(document.getElementById('fi-return').value, 0, 15) / 100, rate = clamp(document.getElementById('fi-rate').value, 1, 10) / 100;
  const target = spend / rate;
  let bal = invested, yrs = 0, put = invested;
  const labels = ['Age ' + age], vPut = [invested], vGrow = [0];
  while (bal < target && yrs < 100) {
    bal = bal * (1 + ret) + save; put += save; yrs++;
    labels.push('Age ' + (age + yrs)); vPut.push(put); vGrow.push(Math.max(0, bal - put));
  }
  const reached = bal >= target;
  setText('fi-number', money(target));
  setText('fi-years', !spend ? '—' : reached ? (yrs === 0 ? 'Already there' : `${yrs} year${yrs === 1 ? '' : 's'}`) : 'Not reached');
  setText('fi-age-at', reached && spend ? String(age + yrs) : '—');
  setText('fi-progress', target ? percent(Math.min(100, invested / target * 100), 1) : '—');
  const C = window.CMFChart && CMFChart.colors;
  if (C && reached && yrs > 1) CMFChart.area(document.getElementById('fi-chart'), labels, [
    { label: 'What you invested', color: C.brand, values: vPut }, { label: 'Growth', color: C.gold, values: vGrow }]);
  else if (C) document.getElementById('fi-chart').innerHTML = '';
  let note;
  if (!spend) note = 'Enter your yearly spending to find your FIRE number.';
  else if (!reached) note = 'Your savings don\'t reach the FIRE number within 100 years. Try investing more each year or lowering spending.';
  else if (yrs === 0) note = 'Your investments already cover your spending at this withdrawal rate.';
  else {
    const less = spend * 0.9, t2 = less / rate; let b2 = invested, y2 = 0;
    while (b2 < t2 && y2 < 100) { b2 = b2 * (1 + ret) + save + spend * 0.1; y2++; }
    note = `Your FIRE number is ${Math.round(1 / rate * 10) / 10}× your yearly spending. Spending 10% less (and investing the difference) would get you there in about ${y2} years instead of ${yrs}. Figures are in today's dollars.`;
  }
  setMessage('fi-note', note);
}
bindInputs(['fi-age', 'fi-spend', 'fi-invested', 'fi-save', 'fi-return', 'fi-rate'], calcFire);
calcFire();
