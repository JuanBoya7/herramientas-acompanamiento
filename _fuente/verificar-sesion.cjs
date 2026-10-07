/* Prueba de integración de las 47 hojas, con contexto de navegador vacío. */
const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs=require('fs'); const path=require('path'); const {pathToFileURL}=require('url');
const root=path.resolve(__dirname,'..');
const out=path.join(root,'_respaldos','2026-10-07-prioridad-en-sesion','qa');
fs.mkdirSync(out,{recursive:true});
const files=fs.readdirSync(root).filter(f=>f.endsWith('.html')&&!['index.html','guia.html'].includes(f));
(async()=>{
 const browser=await chromium.launch({channel:'msedge',headless:true});
 const context=await browser.newContext({viewport:{width:1600,height:1000}});
 const page=await context.newPage(); const errors=[]; let current=''; const report=[];
 page.on('pageerror',e=>errors.push({file:current,message:e.message}));
 for(const file of files){
   current=file; const row={file,layouts:[],controls:0};
   await page.goto(pathToFileURL(path.join(root,file)).href);
   await page.waitForTimeout(150);
   row.primary=await page.locator('body').getAttribute('data-sesion');
   const chip=page.locator('.sesion-principal button.chip:not(.mas):visible').first();
   if(await chip.count()){await chip.click();row.controls++;}
   for(const width of [1600,1000,390]){
     await page.setViewportSize({width,height:1000});
     await page.waitForTimeout(80);
     const bounds=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,
       overflow:[...document.querySelectorAll('.sesion-principal *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>innerWidth+2&&!e.closest('svg,.desliza,.desliza-c');}).slice(0,5).map(e=>e.id||e.className)}));
     row.layouts.push(bounds);
     if(width===1600||width===390) await page.screenshot({path:path.join(out,file.replace('.html','')+'-'+width+'.png')});
   }
   // Abrir cada apoyo debe dejar intacta la superficie principal y sus controles.
   await page.setViewportSize({width:1000,height:1000});
   for(const detail of await page.locator('details.sesion-apoyo').all()){
     if(await detail.isVisible()) await detail.locator(':scope > summary').click();
   }
   row.openLayouts=[];
   for(const width of [1000,390]){
     await page.setViewportSize({width,height:1000});
     row.openLayouts.push(await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth})));
   }
   const state=await page.evaluate(()=>({ids:[...document.querySelectorAll('[id]')].map(e=>e.id),
      primaryVisible:!!document.querySelector('.sesion-principal,[data-secuencia]'),
      closedWizard:document.querySelectorAll('.sesion-principal .cerrado').length}));
   row.duplicateIds=state.ids.filter((v,i,a)=>a.indexOf(v)!==i);
   row.closedWizard=state.closedWizard;
   await page.evaluate(()=>{window.dispatchEvent(new Event('beforeprint'));window.dispatchEvent(new Event('afterprint'));});
   report.push(row); console.log(file, row.layouts.some(r=>r.scroll>r.width+2)?'OVERFLOW':'OK');
 }
 fs.writeFileSync(path.join(out,'resultado.json'),JSON.stringify({report,errors},null,2));
 const failed=report.filter(r=>[...r.layouts,...r.openLayouts].some(l=>l.scroll>l.width+2));
 console.log(JSON.stringify({pages:report.length,errors,overflow:failed.map(r=>r.file),duplicates:report.filter(r=>r.duplicateIds.length)}));
 if(errors.length||failed.length||report.some(r=>r.duplicateIds.length)) process.exitCode=1;
 await browser.close();
})().catch(e=>{console.error(e);process.exitCode=1;});
