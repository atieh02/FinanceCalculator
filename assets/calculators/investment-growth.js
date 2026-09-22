function calcCompound(){
 const principal=readNumber('principal'), contribution=readNumber('contribution'), rate=clamp(document.getElementById('compound-rate').value,0,LIMITS.RATE_MAX), years=clamp(document.getElementById('compound-years').value,1,LIMITS.YEARS_MAX);const freq=clamp(document.getElementById('frequency').value,1,365);document.getElementById('compound-rate').value=rate;document.getElementById('compound-years').value=years;
 const periods=Math.round(years*freq), r=rate/100/freq, perDeposit=contribution*12/freq;let balance=principal;
 const labels=['Now'],deposits=[principal],growth=[0];
 for(let i=1;i<=periods;i++){balance*=1+r;balance+=perDeposit;if(balance>LIMITS.OUTPUT_MAX){balance=Infinity;break;}
   if(i%freq===0||i===periods){const yr=i/freq,dep=principal+perDeposit*i;labels.push('Yr '+Math.round(yr));deposits.push(dep);growth.push(Math.max(0,balance-dep));}}
 const contributions=principal+contribution*12*years;const earned=Number.isFinite(balance)?Math.max(0,balance-contributions):Infinity;setText('compound-result',money(balance));setText('compound-contributions',money(contributions));setText('compound-growth',money(earned));setText('compound-rate-display',percent(rate));
 const C=window.CMFChart&&CMFChart.colors;if(C&&Number.isFinite(balance))CMFChart.area(document.getElementById('compound-chart'),labels,[{label:'Your contributions',color:C.brand,values:deposits},{label:'Investment growth',color:C.gold,values:growth}]);
 setMessage('compound-note',rate===0?'With a 0% return, the result is simply the starting amount plus contributions.':`About ${Number.isFinite(balance)&&balance>0?Math.round(earned/balance*100):0}% of your final balance comes from investment growth. This assumes a steady return; real returns vary and aren't guaranteed.`);
}
bindInputs(['principal','contribution','compound-rate','compound-years','frequency'],calcCompound);document.getElementById('frequency').addEventListener('change',calcCompound);calcCompound();
