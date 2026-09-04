function calcEmergency(){
  const essential=readNumber('essential');
  const months=clamp(document.getElementById('months').value,1,24); document.getElementById('months').value=months;
  const saved=readNumber('saved');
  const target=Math.min(LIMITS.OUTPUT_MAX,essential*months);
  const progress=target>0?Math.min(100,saved/target*100):0;
  document.getElementById('progress-fill').style.width=`${progress}%`;
  setText('emergency-result',money(target));
  if(target===0) setMessage('emergency-note','Enter your essential monthly expenses to see a target.');
  else if(saved>=target) setMessage('emergency-note',`You are at ${Math.round(progress)}% of the selected target. Your savings meet or exceed it.`);
  else setMessage('emergency-note',`${money(target-saved)} more would reach the selected ${months}-month target.`);
  setText('months-help', months<=6?'Three to six months is a common starting range; a larger cushion may make sense when income is variable or harder to replace.':'A larger cushion can be useful when income is variable, household income is concentrated in one source, or major essential costs would be difficult to replace quickly.');
}
bindInputs(['essential','saved','months'],calcEmergency);calcEmergency();
