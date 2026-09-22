function fvMonthly(m, i, n) { return n <= 0 ? 0 : (i === 0 ? m * n : m * (Math.pow(1 + i, n) - 1) / i); }
function calcWaiting() {
  const monthly = readNumber('cw-monthly', 0, 1e7), ret = clamp(document.getElementById('cw-return').value, 0, 20) / 100;
  const years = Math.round(clamp(document.getElementById('cw-years').value, 1, 70));
  const delay = Math.round(Math.min(clamp(document.getElementById('cw-delay').value, 0, 69), years - 1));
  const i = ret / 12, n = years * 12, nLater = (years - delay) * 12;
  const now = fvMonthly(monthly, i, n), later = fvMonthly(monthly, i, nLater), cost = Math.max(0, now - later);
  const unit = fvMonthly(1, i, nLater), catchup = unit ? now / unit : 0;
  setText('cw-cost', money(cost));
  setText('cw-now', money(now));
  setText('cw-later', money(later));
  setText('cw-delay-label', delay);
  setText('cw-catchup', money(catchup, 2));
  const pctLost = now ? Math.round(cost / now * 100) : 0;
  setMessage('cw-note', !monthly ? 'Enter a monthly amount to compare.' : delay === 0 ? 'Starting now gives your money the most time to grow.' :
    `Waiting ${delay} year${delay === 1 ? '' : 's'} means about ${pctLost}% less at the end, even though you'd invest for ${years - delay} of the ${years} years. To catch up you'd need to invest ${money(catchup, 2)} a month instead of ${money(monthly)}.`);
}
bindInputs(['cw-monthly', 'cw-return', 'cw-years', 'cw-delay'], calcWaiting);
calcWaiting();
