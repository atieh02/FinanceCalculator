function calcLoan(){
 const amount=readNumber('loan-amount'), rate=clamp(document.getElementById('loan-rate').value,0,LIMITS.RATE_MAX), years=clamp(document.getElementById('loan-term').value,1,LIMITS.YEARS_MAX), extra=readNumber('loan-extra');document.getElementById('loan-rate').value=rate;document.getElementById('loan-term').value=years;
 const base=amount?fixedPayment(amount,rate,years):0;const payment=base+extra;let bal=amount,interest=0,months=0;while(bal>0.005&&months<LIMITS.MONTHS_MAX){const i=bal*(rate/100/12);interest+=i;const p=Math.min(bal,Math.max(0,payment-i));bal-=p;months++;if(payment<=i+1e-9)break;}
 const complete=bal<=0.005;setText('loan-payment',moneyCapped(base,2));setText('loan-total',complete?moneyCapped(amount+interest):'Not reached');setText('loan-interest',complete?moneyCapped(interest):'—');setText('loan-time',complete?yearsMonths(months):'Not reached');
 setMessage('loan-note',complete?(extra>0?`With the extra payment included, this estimate reaches zero in ${yearsMonths(months)}.`:'This is the standard fixed-payment estimate for the term you entered.'):(amount===0?'Enter a loan amount to see a payment.':'The payment is not high enough to cover ongoing interest. Increase the payment or reduce the rate.'));
}
bindInputs(['loan-amount','loan-rate','loan-term','loan-extra'],calcLoan);calcLoan();
