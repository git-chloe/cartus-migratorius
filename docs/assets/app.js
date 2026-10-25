'use strict';
(() => {
  const seasons = ['Winter','Spring','Summer','Fall'];
  const values = {
    all: {Winter:58,Spring:112,Summer:134,Fall:107},
    mapped: {Winter:29,Spring:85,Summer:82,Fall:51}
  };
  const buttons = [...document.querySelectorAll('.season-toggle')];
  const draw = (type) => {
    const rows = values[type];
    const max = Math.max(...Object.values(rows));
    seasons.forEach(season => {
      const fill = document.querySelector(`[data-season="${season}"]`);
      const text = document.querySelector(`[data-value="${season}"]`);
      if (fill) fill.style.width = `${100*rows[season]/max}%`;
      if (text) text.textContent = String(rows[season]);
    });
    buttons.forEach(btn => btn.setAttribute('aria-pressed',btn.dataset.type === type ? 'true':'false'));
    const total = Object.values(rows).reduce((a,b)=>a+b,0);
    const subtitle=document.getElementById('season-counter');
    if (subtitle) subtitle.textContent = (type==='all' ? 'All reported requests' : 'Reports with coordinates') + ` · n = ${total}`;
    const takeaway=document.getElementById('season-takeaway');
    if (takeaway) takeaway.textContent = type==='all'
      ? 'Summer leads across all 411 reports (134).'
      : 'Spring narrowly leads among the 247 geocoded reports (85 vs. 82 in summer).';
  };
  buttons.forEach(button => button.addEventListener('click',()=>draw(button.dataset.type)));
  draw('all');
  const picker=document.getElementById('map-picker');
  if(picker) picker.addEventListener('change',()=>{
    const valid=['seasonal-migration','known-habitats','recurring-habitats','wheres-wheeldo','golden-wheel','double-isolation','woodroffe-witnesses'];
    if (!valid.includes(picker.value)) return;
    const next=`maps/${picker.value}.html`;
    document.getElementById('field-map').src=next;
    document.getElementById('map-open').href=next;
  });
})();
