function calcAuto() {
  const price = readNumber('al-price', 0, 1e8), trade = readNumber('al-trade', 0, 1e8), down = readNumber('al-down', 0, 1e8);
  const taxRate = clamp(document.getElementById('al-tax').value, 0, 20), fees = readNumber('al-fees', 0, 1e6);
  const rate = clamp(document.getElementById('al-rate').value, 0, 50), months = Number(document.getElementById('al-term').value) || 60;
  const taxable = Math.max(0, price - trade), tax = taxable * taxRate / 100;
  const financed = Math.max(0, price - trade - down + tax + fees);
  const payment = financed ? fixedPayment(financed, rate, months / 12) : 0;
  const interest = Math.max(0, payment * months - financed);
  setText('al-payment', money(payment, 2));
  setText('al-financed', money(financed));
  setText('al-taxamt', money(tax));
  setText('al-interest', money(interest));
  setText('al-total', money(down + trade + payment * months));
  const C = window.CMFChart && CMFChart.colors;
  if (C) CMFChart.donut(document.getElementById('al-chart'), [
    { label: 'Principal', value: financed, color: C.brand }, { label: 'Interest', value: interest, color: C.coral }]);
  let note;
  if (price === 0) note = 'Enter the vehicle price to see a payment.';
  else if (financed === 0) note = 'Your trade-in and down payment cover the full cost. No loan needed.';
  else if (months >= 72) note = `A ${months}-month term keeps the payment down, but you'll pay ${money(interest)} in interest and may owe more than the car is worth for a while. Try 60 months to compare.`;
  else note = `Over ${months} months you'd pay ${money(interest)} in interest. Every extra $1,000 down lowers the payment by about ${money(fixedPayment(1000, rate, months / 12), 2)}.`;
  setMessage('al-note', note);
}
bindInputs(['al-price', 'al-trade', 'al-down', 'al-tax', 'al-fees', 'al-rate', 'al-term'], calcAuto);
document.getElementById('al-term').addEventListener('change', calcAuto);
calcAuto();
