const LIMITS = Object.freeze({
  MONEY_MIN: 0,
  MONEY_MAX: 1_000_000_000_000,
  OUTPUT_MAX: 1_000_000_000_000_000,
  RATE_MIN: 0,
  RATE_MAX: 100,
  YEARS_MIN: 1,
  YEARS_MAX: 100,
  MONTHS_MIN: 1,
  MONTHS_MAX: 1200,
  DEBTS_MAX: 20
});

function clamp(value, min, max) {
  const n = Number(value);
  if (!Number.isFinite(n)) return min;
  return Math.min(max, Math.max(min, n));
}
function readNumber(id, min=0, max=LIMITS.MONEY_MAX) {
  const el = typeof id === 'string' ? document.getElementById(id) : id;
  if (!el) return min;
  const n = Number(el.value);
  const safe = Number.isFinite(n) ? clamp(n, min, max) : min;
  if (el.value !== '' && Number(n) !== safe) el.value = safe;
  return safe;
}
function money(n, digits=0) {
  const value = Number(n);
  if (value === Infinity) return 'Above $1 quadrillion';
  if (value === -Infinity) return 'Below −$1 quadrillion';
  if (!Number.isFinite(value)) return '—';
  if (Math.abs(value) > LIMITS.OUTPUT_MAX) return value < 0 ? 'Below −$1 quadrillion' : 'Above $1 quadrillion';
  return new Intl.NumberFormat('en-US', {style:'currency', currency:'USD', maximumFractionDigits:digits, minimumFractionDigits:digits}).format(value);
}
function moneyCapped(n, digits=0) {
  const value = clamp(Number(n), -LIMITS.OUTPUT_MAX, LIMITS.OUTPUT_MAX);
  return money(value, digits);
}
function percent(n, digits=2) {
  return `${Number(n).toLocaleString('en-US',{maximumFractionDigits:digits})}%`;
}
function whole(n) { return Math.round(Number(n)).toLocaleString('en-US'); }
function yearsMonths(totalMonths) {
  if (!Number.isFinite(totalMonths)) return 'Not reached';
  const m = Math.max(0, Math.round(totalMonths));
  return m < 12 ? `${m} month${m===1?'':'s'}` : `${Math.floor(m/12)} yr ${m%12} mo`;
}
function bindInputs(ids, fn) { ids.forEach(id => document.getElementById(id)?.addEventListener('input', fn)); }
function setText(id, text) { const el=document.getElementById(id); if(el) el.textContent=text; }
function setMessage(id, text, type='notice') { const el=document.getElementById(id); if(!el) return; el.className=type; el.textContent=text; }

function fixedPayment(principal, annualRate, years) { const n=years*12, r=annualRate/100/12; return r===0 ? (n?principal/n:0) : principal*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1); }
