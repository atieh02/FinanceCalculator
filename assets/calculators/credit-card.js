function calcCard(){
 const balance=readNumber('card-balance'),apr=clamp(document.getElementById('card-apr').value,0,LIMITS.RATE_MAX),min=readNumber('card-minimum'),extra=readNumber('card-extra');document.getElementById('card-apr').value=apr;
 let bal=balance,interest=0,months=0;const payment=min+extra;while(bal>0.005&&months<LIMITS.MONTHS_MAX){const i=bal*apr/100/12;interest+=i;const p=Math.min(bal,Math.max(0,payment-i));bal-=p;months++;if(payment<=i+1e-9)break;}
 const complete=bal<=0.005;setText('card-time',complete?yearsMonths(months):'Not reached');setText('card-interest',complete?moneyCapped(interest):'—');setText('card-total',complete?moneyCapped(balance+interest):'Not reached');
 const targetMonths=clamp(document.getElementById('target-months').value,1,120);let targetPayment=0;if(balance>0){const r=apr/100/12;targetPayment=r===0?balance/targetMonths:balance*r/(1-Math.pow(1+r,-targetMonths));}setText('card-target-payment',moneyCapped(targetPayment));setText('card-rate',percent(apr));
 setMessage('card-note',complete?(extra>0?`Your modeled payment is ${money(payment)} per month, including the extra amount.`:'Enter an extra payment to see how paying above the minimum changes the timeline.'):'The current payment does not cover ongoing interest. Increase the payment.');
}
bindInputs(['card-balance','card-apr','card-minimum','card-extra','target-months'],calcCard);calcCard();
