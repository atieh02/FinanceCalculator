const TROY_OZ_G = 31.1034768;
// Example starting prices only; visitors are asked to enter today's live spot price.
const GS_DEFAULTS = { gold: { spot: 3300, purity: '0.999' }, silver: { spot: 38, purity: '0.999' }, platinum: { spot: 1300, purity: '0.999' } };
let gsSpotEdited = false;
function calcGold() {
  const metal = document.getElementById('gs-metal').value;
  const purity = clamp(document.getElementById('gs-purity').value, 0, 1);
  const weight = readNumber('gs-weight', 0, 1e7), unitG = Number(document.getElementById('gs-unit').value) || 1;
  const spot = readNumber('gs-spot', 0, 1e6), premium = clamp(document.getElementById('gs-premium').value, 0, 100) / 100;
  const grams = weight * unitG, pureOz = grams * purity / TROY_OZ_G, value = pureOz * spot;
  setText('gs-value', money(value, 2));
  setText('gs-pure', `${pureOz.toLocaleString('en-US', { maximumFractionDigits: 3 })} troy oz (${(pureOz * TROY_OZ_G).toLocaleString('en-US', { maximumFractionDigits: 2 })} g)`);
  setText('gs-pergram', money(spot * purity / TROY_OZ_G, 2));
  setText('gs-buy', money(value * (1 + premium), 2));
  const name = metal[0].toUpperCase() + metal.slice(1);
  setMessage('gs-note', !weight ? 'Enter a weight to see the value.' :
    `Based on ${money(spot, 2)} per troy ounce of pure ${metal}. Spot prices change throughout the day, so enter today's live price for an exact figure. ${name} jewelry or scrap usually sells for less than its metal value.`);
}
document.getElementById('gs-spot').addEventListener('input', () => { gsSpotEdited = true; });
document.getElementById('gs-metal').addEventListener('change', () => {
  const d = GS_DEFAULTS[document.getElementById('gs-metal').value];
  document.getElementById('gs-purity').value = d.purity;
  if (!gsSpotEdited) document.getElementById('gs-spot').value = d.spot;
  calcGold();
});
bindInputs(['gs-weight', 'gs-spot', 'gs-premium'], calcGold);
['gs-purity', 'gs-unit'].forEach(id => document.getElementById(id).addEventListener('change', calcGold));
calcGold();
