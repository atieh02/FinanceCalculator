function calcRetirement(){
 const age=clamp(document.getElementById('age').value,18,90),retire=clamp(document.getElementById('retire-age').value,age,100),current=readNumber('retirement-savings'),contribution=readNumber('retirement-contribution'),salary=readNumber('salary'),match=clamp(document.getElementById('match').value,0,100),returnRate=clamp(document.getElementById('return-rate').value,0,30),salaryGrowth=clamp(document.getElementById('salary-growth').value,0,20),inflation=clamp(document.getElementById('inflation').value,0,15),withdrawal=clamp(document.getElementById('withdrawal').value,1,10);
 document.getElementById('retire-age').value=retire;document.getElementById('match').value=match;document.getElementById('return-rate').value=returnRate;document.getElementById('salary-growth').value=salaryGrowth;document.getElementById('inflation').value=inflation;document.getElementById('withdrawal').value=withdrawal;
 let balance=current, annualContribution=contribution*12, annualSalary=salary, paidIn=current;
 const labels=['Age '+age],contribs=[current],growth=[0];
 for(let y=age;y<retire;y++){const employer=annualSalary*match/100;balance*=1+returnRate/100;balance+=annualContribution+employer;paidIn+=annualContribution+employer;annualContribution*=1+salaryGrowth/100;annualSalary*=1+salaryGrowth/100;if(balance>LIMITS.OUTPUT_MAX){balance=Infinity;break;}
   labels.push('Age '+(y+1));contribs.push(paidIn);growth.push(Math.max(0,balance-paidIn));}
 const years=retire-age;const realRate=(1+returnRate/100)/(1+inflation/100)-1;const firstYearIncome=Number.isFinite(balance)?balance*withdrawal/100:Infinity;
 const todays=Number.isFinite(balance)?balance/Math.pow(1+inflation/100,years):Infinity;
 setText('retirement-result',money(balance));setText('retirement-years',`${years} year${years===1?'':'s'}`);setText('retirement-income',money(firstYearIncome));setText('retirement-real-rate',percent(realRate*100));
 const C=window.CMFChart&&CMFChart.colors;if(C&&Number.isFinite(balance))CMFChart.area(document.getElementById('retirement-chart'),labels,[{label:'You + employer put in',color:C.brand,values:contribs},{label:'Investment growth',color:C.gold,values:growth}]);
 setMessage('retirement-note',`In today's dollars that's about ${money(todays)} after ${percent(inflation)} yearly inflation. Assumes a constant ${percent(returnRate)} return and contributions growing ${percent(salaryGrowth)} a year. It's a scenario, not a guarantee.`);
}
bindInputs(['age','retire-age','retirement-savings','retirement-contribution','salary','match','return-rate','salary-growth','inflation','withdrawal'],calcRetirement);calcRetirement();
