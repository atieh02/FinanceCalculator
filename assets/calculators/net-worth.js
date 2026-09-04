function addNetRow(listId,label='Other item'){
 const list=document.getElementById(listId); if(list.children.length>=10)return;
 const row=document.createElement('div');row.className='dynamic-row';row.innerHTML=`<div class="field"><label>${label} name</label><input class="item-name" type="text" value="${label}"></div><div class="field"><label>Current value</label><div class="input-wrap"><span>$</span><input class="item-value" type="number" min="0" max="${LIMITS.MONEY_MAX}" step="1" value="0"></div></div><button type="button" class="remove" aria-label="Remove ${label}">Remove</button>`;
 row.querySelector('.remove').addEventListener('click',()=>{row.remove();calcNetWorth()});row.querySelectorAll('input').forEach(i=>i.addEventListener('input',calcNetWorth));list.appendChild(row);
}
function sumSelector(selector){return [...document.querySelectorAll(selector)].reduce((s,e)=>s+clamp(Number(e.value)||0,0,LIMITS.MONEY_MAX),0)}
function calcNetWorth(){
 const assets=sumSelector('#assets-list input[type=number]'), liabilities=sumSelector('#liabilities-list input[type=number]'), net=assets-liabilities;
 setText('assets-total',money(assets));setText('liabilities-total',money(liabilities));setText('net-worth',moneyCapped(net));
 setMessage('net-worth-note',net<0?'A negative net worth is a snapshot, not a verdict. It can change as balances, savings, and asset values change.':'Net worth is a snapshot. The useful comparison is usually how the relationship between what you own and owe changes over time.');
}
document.getElementById('add-asset')?.addEventListener('click',()=>{addNetRow('assets-list','Other asset');calcNetWorth()});document.getElementById('add-liability')?.addEventListener('click',()=>{addNetRow('liabilities-list','Other liability');calcNetWorth()});document.querySelectorAll('#assets-list input,#liabilities-list input').forEach(i=>i.addEventListener('input',calcNetWorth));calcNetWorth();
