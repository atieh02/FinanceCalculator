function calcSalary() {
  const amount = readNumber('sh-amount', 0, 1e9), period = document.getElementById('sh-period').value;
  const hours = clamp(document.getElementById('sh-hours').value, 1, 100), weeks = clamp(document.getElementById('sh-weeks').value, 1, 52);
  const toAnnual = { hour: hours * weeks, day: 5 * weeks, week: weeks, biweek: 26, month: 12, year: 1 };
  const annual = amount * toAnnual[period];
  setText('sh-hourly', money(annual / (hours * weeks), 2));
  setText('sh-day', money(annual / (weeks * 5), 2));
  setText('sh-week', money(annual / weeks, 2));
  setText('sh-biweek', money(annual / 26, 2));
  setText('sh-month', money(annual / 12, 2));
  setText('sh-year', money(annual, 0));
  setMessage('sh-note', amount === 0 ? 'Enter your pay to convert it.' :
    `Based on ${whole(hours * weeks)} working hours a year. These are gross (pre-tax) amounts; take-home pay will be lower after taxes and deductions.`);
}
bindInputs(['sh-amount', 'sh-period', 'sh-hours', 'sh-weeks'], calcSalary);
document.getElementById('sh-period').addEventListener('change', calcSalary);
calcSalary();
