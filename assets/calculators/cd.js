function calcCD() {
  const deposit = readNumber('cd-deposit', 0, 1e8), apy = clamp(document.getElementById('cd-apy').value, 0, 25) / 100;
  const months = Number(document.getElementById('cd-term').value) || 12, tax = clamp(document.getElementById('cd-tax').value, 0, 60) / 100;
  const other = clamp(document.getElementById('cd-compare').value, 0, 25) / 100;
  const balance = deposit * Math.pow(1 + apy, months / 12), interest = balance - deposit;
  const otherInt = deposit * Math.pow(1 + other, months / 12) - deposit, extra = interest - otherInt;
  setText('cd-balance', money(balance, 2));
  setText('cd-interest', money(interest, 2));
  setText('cd-aftertax', money(interest * (1 - tax), 2));
  setText('cd-other', money(otherInt, 2));
  setText('cd-extra', extra >= 0 ? money(extra, 2) : '−' + money(-extra, 2));
  const C = window.CMFChart && CMFChart.colors;
  if (C) CMFChart.donut(document.getElementById('cd-chart'), [
    { label: 'Deposit', value: deposit, color: C.brand }, { label: 'Interest', value: interest, color: C.gold }]);
  const term = months % 12 === 0 ? `${months / 12}-year` : `${months}-month`;
  let note;
  if (!deposit) note = 'Enter a deposit amount to see your earnings.';
  else if (extra > 0) note = `This ${term} CD earns ${money(extra, 2)} more than an account at ${percent(other * 100)} APY. Rates change often, so compare several banks before you open one.`;
  else note = `The other account earns as much or more. A CD only makes sense if it pays a higher APY or you want to lock in today's rate.`;
  setMessage('cd-note', note);
}
bindInputs(['cd-deposit', 'cd-apy', 'cd-tax', 'cd-compare'], calcCD);
document.getElementById('cd-term').addEventListener('change', calcCD);
calcCD();
