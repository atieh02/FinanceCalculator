// 2026 IRS limits: https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500
const K_LIMIT = 24500, K_CATCHUP = 8000, K_CATCHUP_60_63 = 11250;
function kLimit(age) { return K_LIMIT + (age >= 60 && age <= 63 ? K_CATCHUP_60_63 : age >= 50 ? K_CATCHUP : 0); }
function calc401k() {
  const age = Math.round(clamp(document.getElementById('k-age').value, 18, 80));
  const retire = Math.max(age, Math.round(clamp(document.getElementById('k-retire').value, 19, 85)));
  const start = readNumber('k-balance', 0, 1e8), salary0 = readNumber('k-salary', 0, 1e8);
  const pct = clamp(document.getElementById('k-contrib').value, 0, 100), matchRate = clamp(document.getElementById('k-matchrate').value, 0, 200);
  const matchCap = clamp(document.getElementById('k-matchcap').value, 0, 100), raise = clamp(document.getElementById('k-raise').value, 0, 20) / 100;
  const ret = clamp(document.getElementById('k-return').value, 0, 20) / 100, infl = clamp(document.getElementById('k-infl').value, 0, 15) / 100;
  const useLimit = document.getElementById('k-limit').value === '1';
  let bal = start, salary = salary0, yours = 0, employer = 0, capped = false;
  const labels = ['Age ' + age], vYours = [start], vEmp = [0], vGrowth = [0];
  for (let a = age; a < retire; a++) {
    let mine = salary * pct / 100;
    if (useLimit && mine > kLimit(a)) { mine = kLimit(a); capped = true; }
    const match = salary * Math.min(pct, matchCap) / 100 * matchRate / 100;
    bal = bal * (1 + ret) + mine + match;
    yours += mine; employer += match; salary *= 1 + raise;
    labels.push('Age ' + (a + 1)); vYours.push(start + yours); vEmp.push(employer); vGrowth.push(Math.max(0, bal - start - yours - employer));
  }
  const years = retire - age, today = bal / Math.pow(1 + infl, years), growth = Math.max(0, bal - start - yours - employer);
  setText('k-result', money(bal));
  setText('k-today', money(today));
  setText('k-yours', money(start + yours));
  setText('k-employer', money(employer));
  setText('k-growth', money(growth));
  setText('k-income', money(bal * 0.04 / 12));
  const C = window.CMFChart && CMFChart.colors;
  if (C) CMFChart.area(document.getElementById('k-chart'), labels, [
    { label: 'You', color: C.brand, values: vYours }, { label: 'Employer', color: C.brand2, values: vEmp }, { label: 'Growth', color: C.gold, values: vGrowth }]);
  let note;
  if (pct < matchCap && matchRate > 0) {
    const missed = salary0 * (matchCap - pct) / 100 * matchRate / 100;
    note = `You're leaving ${money(missed)} of free employer match on the table this year. Raising your contribution to ${percent(matchCap)} captures all of it.`;
  } else if (capped) {
    note = `Your contributions hit the IRS limit (${money(K_LIMIT)} in 2026, more with catch-up at 50+) in some years, so they're capped. Consider an IRA or taxable account for extra savings.`;
  } else {
    note = `You're getting the full match. Over ${years} years your employer adds ${money(employer)}. Assumes a steady ${percent(ret * 100)} return; real markets go up and down.`;
  }
  setMessage('k-note', note);
}
bindInputs(['k-age', 'k-retire', 'k-balance', 'k-salary', 'k-contrib', 'k-matchrate', 'k-matchcap', 'k-raise', 'k-return', 'k-infl'], calc401k);
document.getElementById('k-limit').addEventListener('change', calc401k);
calc401k();
