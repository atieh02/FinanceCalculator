function calcCompound(){
 const principal=readNumber('principal'), contribution=readNumber('contribution'), rate=clamp(document.getElementById('compound-rate').value,0,LIMITS.RATE_MAX), years=clamp(document.getElementById('compound-years').value,1,LIMITS.YEARS_MAX);const freq=clamp(document.getElementById('frequency').value,1,365);document.getElementById('compound-rate').value=rate;document.getElementById('compound-years').value=years;
 const periods=years*freq, r=rate/100/freq;let balance=principal;for(let i=0;i<periods;i++){balance*=1+r;balance+=contribution*12/freq;if(balance>LIMITS.OUTPUT_MAX){balance=Infinity;break;}}
 const contributions=principal+contribution*12*years;const growth=Number.isFinite(balance)?Math.max(0,balance-contributions):Infinity;setText('compound-result',money(balance));setText('compound-contributions',money(contributions));setText('compound-growth',money(growth));setText('compound-rate-display',percent(rate));
 setMessage('compound-note',rate===0?'With a 0% rate, the result is simply the starting amount plus contributions.':'This estimate assumes a constant rate and regular contributions. Real returns vary and are not guaranteed.');
}
bindInputs(['principal','contribution','compound-rate','compound-years','frequency'],calcCompound);calcCompound();
