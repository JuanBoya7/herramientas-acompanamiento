/* ---------------- Hoja PDF (jsPDF vectorial, campos rellenables) ----------------
   Se dibuja directamente con jsPDF: texto real (seleccionable y nítido), sin capturas de
   pantalla. Primero se intenta que todo quepa en UNA hoja reduciendo levemente la letra y
   los espacios; si con la letra mínima legible no cabe, se reparte en dos hojas con la
   letra cómoda, sin recortar contenido. Las respuestas son campos de formulario. */
const PDF_LOCAL = "arte/jspdf.umd.min.js";
const PDF_CDN = "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";
const FONDO_ARRIBA = "__FONDO_ARRIBA__";
const FONDO_ABAJO = "__FONDO_ABAJO__";
let cargaLib = null;
function cargarJsPDF(){
  if(window.jspdf) return Promise.resolve();
  if(cargaLib) return cargaLib;
  cargaLib = new Promise((ok, mal) => {
    const s = document.createElement("script");
    s.src = PDF_LOCAL; s.onload = ok;
    s.onerror = () => {
      const s2 = document.createElement("script");
      s2.src = PDF_CDN; s2.onload = ok;
      s2.onerror = () => { cargaLib = null; mal(new Error("sin biblioteca")); };
      document.head.appendChild(s2);
    };
    document.head.appendChild(s);
  });
  return cargaLib;
}
function nombreArchivo(l){ return "Lectura ACT - " + l.titulo.replace(/[\\/:*?"<>|«»]/g, "").replace(/\s+/g, " ").trim().slice(0, 80) + ".pdf"; }
function enlacePaciente(l){
  const u = new URL(location.href); u.search = ""; u.hash = "";
  u.searchParams.set("lectura", l.slug); u.searchParams.set("modo", "paciente");
  return u.toString();
}
/* Las fuentes base del PDF usan la tabla WinAnsi: se normaliza lo que no está en ella. */
const pdfTxt = s => String(s || "").replace(/—/g, "–").replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/…/g, "...");
function rgb(h){ const n = parseInt(h.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; }
function mezcla(h, k){ const c = rgb(h); return c.map(v => Math.round(v + (255 - v) * k)); }
function aJpeg(src, lado){
  return new Promise(ok => {
    const im = new Image();
    im.onload = () => {
      try{
        const k = Math.min(1, lado / Math.max(im.naturalWidth, im.naturalHeight));
        const c = document.createElement("canvas");
        c.width = Math.round(im.naturalWidth * k); c.height = Math.round(im.naturalHeight * k);
        const x = c.getContext("2d"); x.fillStyle = "#fff"; x.fillRect(0, 0, c.width, c.height);
        x.drawImage(im, 0, 0, c.width, c.height);
        ok({data: c.toDataURL("image/jpeg", 0.9), w: c.width, h: c.height});
      }catch(e){ ok(null); } // archivo abierto con doble clic: el navegador no deja leer la imagen
    };
    im.onerror = () => ok(null);
    im.src = src;
  });
}

const A4 = {w: 210, h: 297}, MX = 15, MT = 13, MB = 17;
const PT = 0.3528; // mm por punto

/* Maqueta la lectura. Con dibujar=false solo mide. Devuelve {paginas, desborda}. */
function maquetar(doc, d, k, unaPagina, dibujar){
  const p = d.p, l = d.l, ancho = A4.w - 2 * MX;
  const C = rgb(p.color), S = rgb(p.suave), B = rgb(p.borde), T = [34, 48, 46], G = [91, 107, 104];
  let y = MT, pagina = 1, desborda = false;
  const tope = () => A4.h - MB;
  const lh = (pt, f) => pt * PT * f;
  function salto(h){
    if(y + h <= tope()) return;
    if(unaPagina){ desborda = true; return; }
    if(dibujar){ doc.addPage(); fondo("abajo"); }
    pagina++; y = MT + 2;
  }
  function fondo(cual){
    if(!dibujar) return;
    const im = cual === "arriba" ? d.fArriba : d.fAbajo;
    if(!im) return;
    const h = A4.w * im.h / im.w;
    doc.addImage(im.data, "JPEG", 0, cual === "arriba" ? 0 : A4.h - h, A4.w, h, cual, "FAST");
  }
  function fuente(fam, est, pt, col){ doc.setFont(fam, est); doc.setFontSize(pt); doc.setTextColor(...(col || T)); }
  function lineas(txt, w){ return doc.splitTextToSize(pdfTxt(txt), w); }
  function parrafo(txt, x, w, fam, est, pt, f, col, justificar){
    fuente(fam, est, pt, col);
    const ls = lineas(txt, w), h = lh(pt, f);
    ls.forEach((ln, i) => {
      salto(h);
      if(dibujar){
        const ultima = i === ls.length - 1;
        if(justificar && !ultima) doc.text(ln, x, y + pt * PT * 0.8, {align: "justify", maxWidth: w});
        else doc.text(ln, x, y + pt * PT * 0.8);
      }
      y += h;
    });
  }
  function titulo2(txt){
    salto(9 * k + 12);   // un subtítulo nunca queda solo al pie
    y += 2.6 * k;
    if(dibujar){
      doc.setFillColor(...C);
      const cx = MX + 1.3, cy = y + 2.1;
      doc.triangle(cx - 1.3, cy, cx, cy - 1.3, cx + 1.3, cy, "F"); doc.triangle(cx - 1.3, cy, cx, cy + 1.3, cx + 1.3, cy, "F");
      fuente("times", "bold", 12 * k, [29, 42, 40]); doc.text(pdfTxt(txt), MX + 4.6, y + 3.4);
    }
    y += 6.6 * k;
  }

  /* 1 · Cabecera */
  fondo("arriba");
  if(unaPagina) fondo("abajo");
  fuente("times", "bold", 18.5 * k);
  const tl = lineas(l.titulo, ancho - 50);
  const hCab = 6 + tl.length * lh(18.5 * k, 1.12) + 9.5;
  if(dibujar){
    doc.setFillColor(...S); doc.roundedRect(MX, y, ancho * 0.78, hCab, 2.5, 2.5, "F");
    doc.setFillColor(...C); doc.rect(MX, y, 1.4, hCab, "F");
    fuente("helvetica", "bold", 7.3, C);
    doc.text(pdfTxt("TERAPIA DE ACEPTACIÓN Y COMPROMISO · " + p.nombre.toUpperCase()), MX + 5, y + 5, {charSpace: 0.35});
    fuente("times", "bold", 18.5 * k, [29, 42, 40]);
    tl.forEach((ln, i) => doc.text(ln, MX + 5, y + 6 + (i + 0.82) * lh(18.5 * k, 1.12)));
    const yb = y + 6 + tl.length * lh(18.5 * k, 1.12) + 4;
    fuente("helvetica", "normal", 8.4, G);
    doc.text(pdfTxt(p.estilo_nombre + " · " + l.tipo + " · " + l.tiempo + " de lectura"), MX + 5, yb);
    fuente("helvetica", "normal", 8, [63, 78, 75]);
    doc.text(pdfTxt((d.nombre ? "Preparado para: " + d.nombre + "   ·   " : "") + d.fecha), MX + 5, yb + 4.2);
  }
  y += hCab + 4 * k;

  /* 2 · Ilustración y resumen */
  const lado = d.ilus ? 33 * k : 0, xr = MX + (lado ? lado + 5 : 0), wr = ancho - (xr - MX);
  const y0 = y;
  if(dibujar && d.ilus){
    doc.setDrawColor(...B); doc.setLineWidth(0.3);
    doc.roundedRect(MX, y, lado, lado, 2, 2, "S");
    doc.addImage(d.ilus.data, "JPEG", MX + 0.8, y + 0.8, lado - 1.6, lado - 1.6, "ilus", "FAST");
  }
  y += lado ? 1.5 : 0;
  parrafo(l.resumen, xr, wr, "times", "italic", 11 * k, 1.38, [44, 58, 56], false);
  y += 1.6;
  parrafo(p.desc, xr, wr, "helvetica", "normal", 8.2 * k, 1.38, G, false);
  y = Math.max(y, y0 + lado) + 1.5 * k;

  /* 3 · Lectura */
  titulo2("Lectura");
  l.lectura.forEach(par => { parrafo(par, MX, ancho, "times", "normal", 10.6 * k, 1.42, [36, 49, 47], true); y += 1.7 * k; });

  /* 4 · Idea clave */
  fuente("times", "italic", 10.6 * k);
  const cl = lineas(l.clave, ancho - 12), hc = cl.length * lh(10.6 * k, 1.38) + 6 * k;
  salto(hc + 2);
  y += 1.2 * k;
  if(dibujar){
    doc.setFillColor(...S); doc.roundedRect(MX, y, ancho, hc, 2, 2, "F");
    doc.setFillColor(...C); doc.rect(MX, y, 1.2, hc, "F");
    fuente("times", "italic", 10.6 * k, [38, 51, 49]);
    cl.forEach((ln, i) => doc.text(ln, MX + 6, y + 3 * k + (i + 0.8) * lh(10.6 * k, 1.38)));
  }
  y += hc + 1.5 * k;

  /* 5 · Preguntas con campo rellenable */
  titulo2("Para reflexionar");
  l.preguntas.forEach((q, i) => {
    fuente("helvetica", "bold", 9.5 * k);
    const ql = lineas(q, ancho - 8), hq = ql.length * lh(9.5 * k, 1.32);
    const r = d.resp[i] || "";
    fuente("helvetica", "normal", 9.5);
    const rl = r ? lineas(r, ancho - 12).length : 0;
    const hb = Math.max(17 * k, rl * lh(9.5, 1.35) + 5) + (d.extra || 0);
    salto(hq + hb + 3);
    if(dibujar){
      doc.setFillColor(...C); doc.circle(MX + 2.3, y + 2.1, 2.3, "F");
      fuente("helvetica", "bold", 7.5, [255, 255, 255]); doc.text(String(i + 1), MX + 2.3, y + 2.1 + 0.95, {align: "center"});
      fuente("helvetica", "bold", 9.5 * k, [30, 44, 42]);
      ql.forEach((ln, j) => doc.text(ln, MX + 7, y + (j + 0.8) * lh(9.5 * k, 1.32)));
    }
    y += hq + 1.4;
    if(dibujar){
      const xb = MX + 7, wb = ancho - 7;
      doc.setFillColor(255, 255, 255); doc.setDrawColor(...B); doc.setLineWidth(0.35);
      doc.roundedRect(xb, y, wb, hb, 1.8, 1.8, "FD");
      if(!r){ // renglones tenues para quien lo imprime y escribe a mano
        doc.setDrawColor(...mezcla(p.borde, 0.45)); doc.setLineWidth(0.2);
        for(let yy = y + 7; yy < y + hb - 1.5; yy += 6.2) doc.line(xb + 3, yy, xb + wb - 3, yy);
      }
      const f = new doc.AcroFormTextField();
      f.fieldName = "respuesta_" + (i + 1);
      f.Rect = [xb + 1, y + 0.8, wb - 2, hb - 1.6];
      f.multiline = true; f.fontSize = 9.5; f.fontName = "helvetica";
      f.value = pdfTxt(r); f.textColor = "#22302e";
      doc.addField(f);
    }
    y += hb + 2.6 * k;
  });

  /* 6 · Práctica sugerida */
  titulo2("Práctica para los próximos días");
  fuente("helvetica", "normal", 9.6 * k);
  const pl = lineas(l.practica, ancho - 8), hp = pl.length * lh(9.6 * k, 1.42) + 5.5 * k;
  salto(hp + 1);
  if(dibujar){
    doc.setDrawColor(...C); doc.setLineWidth(0.35); doc.setLineDashPattern([1.4, 1], 0);
    doc.roundedRect(MX, y, ancho, hp, 2, 2, "S"); doc.setLineDashPattern([], 0);
    fuente("helvetica", "normal", 9.6 * k, T);
    pl.forEach((ln, i) => doc.text(ln, MX + 4, y + 2.8 * k + (i + 0.8) * lh(9.6 * k, 1.42)));
  }
  y += hp + 2.2 * k;

  /* 7 · Fuente */
  parrafo("Fuente: " + l.fuente, MX, ancho, "helvetica", "italic", 7.4, 1.35, [106, 121, 118], false);

  return {paginas: pagina, desborda, sobra: tope() - y};
}

function pies(doc, total){
  for(let i = 1; i <= total; i++){
    doc.setPage(i);
    const y = A4.h - 10;
    doc.setDrawColor(226, 236, 233); doc.setLineWidth(0.3); doc.line(MX, y - 3.5, A4.w - MX, y - 3.5);
    doc.setFont("helvetica", "bold"); doc.setFontSize(8); doc.setTextColor(34, 48, 46);
    doc.text(pdfTxt(PROF), MX, y);
    const w = doc.getTextWidth(pdfTxt(PROF));
    doc.setFont("helvetica", "normal"); doc.setTextColor(114, 130, 128);
    doc.text(pdfTxt("  ·  " + CRED), MX + w, y);
    doc.text(pdfTxt("Lecturas ACT" + (total > 1 ? "  ·  Página " + i + " de " + total : "")), A4.w - MX, y, {align: "right"});
  }
}

async function generarPdf(l){
  await cargarJsPDF();
  const {jsPDF} = window.jspdf;
  const d = {
    l, p: P[l.proceso],
    resp: [...document.querySelectorAll("#lPreg textarea")].map(t => t.value.trim()),
    nombre: (por("eNombre").value || "").trim(),
    fecha: new Date().toLocaleDateString("es-CO", {day: "numeric", month: "long", year: "numeric"}),
  };
  [d.ilus, d.fArriba, d.fAbajo] = await Promise.all([
    aJpeg("arte/lecturas/" + l.slug + ".webp?v=2", 640), aJpeg(FONDO_ARRIBA, 900), aJpeg(FONDO_ABAJO, 900)]);
  const nuevo = () => new jsPDF({unit: "mm", format: "a4", orientation: "portrait", compress: true});
  // Una sola hoja si cabe con la letra al 100 % o reducida hasta el 86 %; si no, dos hojas al 100 %.
  let k = null, sobra = 0;
  for(const e of [1, 0.97, 0.94, 0.91, 0.88, 0.86]){
    const m = maquetar(nuevo(), d, e, true, false);
    if(!m.desborda){ k = e; sobra = m.sobra; break; }
  }
  // Lo que sobra al pie de la hoja única se reparte entre las casillas de respuesta.
  d.extra = k ? Math.min(18, Math.max(0, (sobra - 3) / l.preguntas.length)) : 0;
  const doc = nuevo();
  const r = maquetar(doc, d, k || 1, k !== null, true);
  pies(doc, r.paginas);
  doc.setProperties({title: l.titulo + " · Lecturas ACT", author: PROF, subject: "Lectura de Terapia de Aceptación y Compromiso", creator: "Herramientas de acompañamiento"});
  return doc.output("blob");
}
function descargar(blob, nombre){
  const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = nombre;
  document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
}
async function conBoton(btn, fn){
  btn.disabled = true; const t = btn.innerHTML; btn.innerHTML = "Preparando PDF…";
  try{ await fn(); } finally { btn.disabled = false; btn.innerHTML = t; }
}
function mensaje(l){
  const nombre = (por("eNombre").value || "").trim();
  return (nombre ? "Hola, " + nombre + ". " : "Hola. ") +
    "Te comparto la lectura «" + l.titulo + "» que conversamos en sesión. " +
    "Léela con calma y, si quieres, responde las preguntas en el mismo PDF para retomarlas en nuestro próximo encuentro.";
}
async function obtenerPdf(l){
  try{ return await generarPdf(l); }
  catch(e){ console.error(e); brindis("No se pudo preparar el PDF en este equipo. Se abre la impresión del navegador."); window.print(); return null; }
}
async function imprimir(l){
  const b = await obtenerPdf(l); if(!b) return;
  const u = URL.createObjectURL(b);
  const w = window.open(u, "_blank");
  if(!w) descargar(b, nombreArchivo(l));
  setTimeout(() => URL.revokeObjectURL(u), 60000);
}
