function addDebt(data={name:'Debt',balance:1000,apr:10,min:50}){
 const rows=document.getElementById('debts');if(rows.children.length>=LIMITS.DEBTS_MAX)return;
 const row=document.createElement('div');row.className='debt-row';row.innerHTML=`<div class="field debt-name"><label>Debt name</label><input class="debt-name-input" type="text" value="${data.name}"></div><div class="field"><label>Balance</label><div class="input-wrap"><span>$</span><input class="balance" type="number" min="0" max="${LIMITS.MONEY_MAX}" step="1" value="${data.balance}"></div></div><div class="field"><label>APR</label><div class="input-wrap"><input class="apr" type="number" min="0" max="${LIMITS.RATE_MAX}" step="0.01" value="${data.apr}"><span>%</span></div></div><div class="field"><label>Minimum</label><div class="input-wrap"><span>$</span><input class="min" type="number" min="0" max="${LIMITS.MONEY_MAX}" step="1" value="${data.min}"></div></div><button class="remove" type="button">Remove</button>`;
 row.querySelector('.remove').addEventListener('click',()=>{row.remove();calcDebt()});row.querySelectorAll('input').forEach(i=>i.addEventListener('input',calcDebt));rows.appendChild(row);calcDebt();
}
function readDebts(){return [...document.querySelectorAll('.debt-row')].map(r=>({balance:clamp(r.querySelector('.balance').value,0,LIMITS.MONEY_MAX),apr:clamp(r.querySelector('.apr').value,0,LIMITS.RATE_MAX),min:clamp(r.querySelector('.min').value,0,LIMITS.MONEY_MAX)})).filter(d=>d.balance>0)}
function simulate(input,method,extra){
 let ds=input.map(d=>({...d})),interest=0;
 if(!ds.length)return {months:0,interest:0,complete:true};
 const initialMinimum=ds.reduce((a,d)=>a+d.min,0), budget=initialMinimum+extra;
 if(budget<=0)return {months:Infinity,interest:Infinity,complete:false,reason:'No payment available.'};
 for(let month=1;month<=LIMITS.MONTHS_MAX;month++){
   ds.sort(method==='avalanche'?(a,b)=>b.apr-a.apr||b.balance-a.balance:(a,b)=>a.balance-b.balance||b.apr-a.apr);
   let monthlyInterest=0;
   for(const d of ds){const i=d.balance*(d.apr/100/12);d.balance+=i;monthlyInterest+=i} interest+=monthlyInterest;
   let available=budget;
   for(const d of ds){const p=Math.min(d.balance,d.min);d.balance-=p;available-=p}
   if(available>0){for(const d of ds){if(available<=0)break;const p=Math.min(d.balance,available);d.balance-=p;available-=p}}
   ds=ds.filter(d=>d.balance>0.005);
   if(!ds.length)return {months:month,interest,complete:true};
   const balanceBefore=ds.reduce((s,d)=>s+d.balance,0);
   if(!Number.isFinite(balanceBefore)||balanceBefore>LIMITS.OUTPUT_MAX*100)return {months:Infinity,interest:Infinity,complete:false,reason:'Input is too large for a reliable simulation.'};
   const required=ds.reduce((s,d)=>s+d.balance*(d.apr/100/12),0);
   if(budget<=required+1e-9)return {months:Infinity,interest:Infinity,complete:false,reason:'Payments do not cover ongoing interest.'};
 }
 return {months:Infinity,interest:Infinity,complete:false,reason:'Not paid off within the 100-year simulation limit.'};
}
function calcDebt(){
 const debts=readDebts(),extra=readNumber('extra');const a=simulate(debts,'avalanche',extra),s=simulate(debts,'snowball',extra);
 for(const [id,r] of [['avalanche',a],['snowball',s]]){setText(id+'-months',r.complete?yearsMonths(r.months):'Not reached');setText(id+'-interest',r.complete?moneyCapped(r.interest):'—');}
 setMessage('debt-warning',debts.length?(a.complete&&s.complete?'Avalanche and snowball use the same payment budget; the difference is which debt receives extra money first.':(a.reason||s.reason)):'Add at least one debt with a balance to compare payoff methods.');
}
document.getElementById('add-debt').addEventListener('click',()=>addDebt());document.getElementById('extra').addEventListener('input',calcDebt);addDebt({name:'Credit card',balance:2500,apr:24,min:75});addDebt({name:'Student loan',balance:6000,apr:6.5,min:100});
