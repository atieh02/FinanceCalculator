function calcBudget(){
  const entry=readNumber('income'); const annual=document.getElementById('period').value==='annual'; const monthly=annual?entry/12:entry;
  const needs=clamp(document.getElementById('needs-pct').value,0,100), wants=clamp(document.getElementById('wants-pct').value,0,100), savings=clamp(document.getElementById('savings-pct').value,0,100); const total=needs+wants+savings;
  ['needs-pct','wants-pct','savings-pct'].forEach(id=>document.getElementById(id).value=clamp(document.getElementById(id).value,0,100));
  setText('budget-needs',money(monthly*needs/100)); setText('budget-wants',money(monthly*wants/100)); setText('budget-savings',money(monthly*savings/100));
  document.getElementById('needs-bar').style.width=`${total?needs/total*100:0}%`;document.getElementById('wants-bar').style.width=`${total?wants/total*100:0}%`;document.getElementById('savings-bar').style.width=`${total?savings/total*100:0}%`;
  setText('budget-monthly',money(monthly));
  if(total!==100) setMessage('budget-warning',`Your percentages currently total ${percent(total,1)}. Set them to exactly 100% to allocate all income.`,'error'); else setMessage('budget-warning','The 50/30/20 split is a starting framework. You can change the percentages to test a budget that fits your situation.');
}
bindInputs(['income','period','needs-pct','wants-pct','savings-pct'],calcBudget);calcBudget();
