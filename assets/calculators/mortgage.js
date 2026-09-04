function calcMortgage(){
 const home=readNumber('home-price'), down=readNumber('down-payment');const loan=Math.max(0,home-down);const rate=clamp(document.getElementById('rate').value,0,LIMITS.RATE_MAX);const years=clamp(document.getElementById('term').value,1,LIMITS.YEARS_MAX);const tax=readNumber('property-tax');const insurance=readNumber('insurance');const hoa=readNumber('hoa');const pmiRate=clamp(document.getElementById('pmi').value,0,10);
 document.getElementById('rate').value=rate;document.getElementById('term').value=years;const pi=loan?fixedPayment(loan,rate,years):0;const pmi=(down/home<0.2&&home>0)?loan*pmiRate/100/12:0;const total=pi+tax/12+insurance/12+hoa+pmi;const interest=Math.max(0,pi*years*12-loan);
 setText('mortgage-payment',moneyCapped(total,2));setText('principal-interest',moneyCapped(pi,2));setText('mortgage-loan',moneyCapped(loan));setText('mortgage-interest',moneyCapped(interest));setText('mortgage-pmi',moneyCapped(pmi,2));
 setMessage('mortgage-note',home===0?'Enter a home price to see an estimate.':down>home?'Down payment cannot exceed the home price; the loan is shown as $0.':'This is an estimate. Taxes, insurance, PMI, HOA fees, rate type, closing costs, and lender rules can change the real payment.');
}
bindInputs(['home-price','down-payment','rate','term','property-tax','insurance','hoa','pmi'],calcMortgage);calcMortgage();
