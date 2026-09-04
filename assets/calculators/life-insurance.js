const { MONEY_MAX } = LIMITS;
const fields=['income','debts','future','assets','multiplier'];
function calcLife(){
  const income=readNumber('income'), debts=readNumber('debts'), future=readNumber('future'), assets=readNumber('assets');
  const multiplier=clamp(document.getElementById('multiplier').value,5,20);
  document.getElementById('multiplier').value=multiplier;
  const raw=income*multiplier+debts+future-assets;
  const result=Math.max(0, Math.min(LIMITS.OUTPUT_MAX, raw));
  setText('life-result', money(result));
  document.getElementById('life-breakdown').innerHTML=`<div class="breakdown-row"><span>Income × ${multiplier}</span><strong>${money(income*multiplier)}</strong></div><div class="breakdown-row"><span>Outstanding debts</span><strong>+ ${money(debts)}</strong></div><div class="breakdown-row"><span>Future costs</span><strong>+ ${money(future)}</strong></div><div class="breakdown-row"><span>Existing assets/coverage</span><strong>− ${money(assets)}</strong></div>`;
}
bindInputs(fields,calcLife); calcLife();
