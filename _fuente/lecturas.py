import base64
# -*- coding: utf-8 -*-
"""
Construye `lecturas-act.html`: tablero alterno e independiente de lecturas
acompañadas de ACT (al estilo de ACT Toolkit), organizado por los seis
procesos del hexaflex.

Cada lectura se abre en un lector con ilustración, texto, idea clave,
preguntas de reflexión y práctica sugerida, y ofrece:
  - Descargar PDF (diseño de las historias clínicas de JB adaptado a ACT
    y al color del proceso de la lectura)
  - Enviar por WhatsApp (comparte el PDF en móvil; en computador descarga
    el PDF y abre WhatsApp con el mensaje y el enlace limpio)
  - Enviar por correo (descarga el PDF y abre el correo con asunto y mensaje)
  - Copiar el enlace limpio en modo paciente (?lectura=slug&modo=paciente)

    python lecturas.py
"""
import html as _h
import json
from pathlib import Path

import datos_lecturas_act as datos

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI.parent / "lecturas-act.html"

PROFESIONAL = "Juan Boya Guerra"
CREDENCIAL = "Psicólogo Clínico y de la Salud · T.P. 186609"

PLANTILLA = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lecturas ACT · Lectura acompañada y reflexión</title>
<meta name="description" content="__N__ lecturas de Terapia de Aceptación y Compromiso organizadas por los seis procesos del hexaflex, con preguntas de reflexión y envío en PDF.">
<style>
  :root{
    --tinta:#1f2d2b; --tinta-suave:#5b6b68; --linea:#dfe6e4; --papel:#ffffff; --fondo:#f5f7f4;
    --acento:#2d7a5e; --acento-claro:#e6f4ef; --radio:14px;
    --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
    --sans:"Segoe UI",system-ui,-apple-system,Roboto,"Helvetica Neue",Arial,sans-serif;
  }
  *{box-sizing:border-box}
  html{scroll-behavior:smooth}
  body{margin:0;font-family:var(--sans);color:var(--tinta);background:var(--fondo);line-height:1.55;font-size:16px}
  a{color:inherit}
  button{font:inherit;cursor:pointer}
  .envoltura{max-width:1320px;margin:0 auto;padding:22px 22px 60px}

  /* ---------- Cabecera ---------- */
  .tapa{position:relative;overflow:hidden;border-radius:22px;padding:34px 38px 30px;
    background:linear-gradient(120deg,#eef6f2 0%,#fbf6ee 55%,#f3eef6 100%);border:1px solid var(--linea)}
  .tapa::after{content:"";position:absolute;right:-40px;top:-40px;width:380px;height:300px;
    background:url("arte/fondo-act-arriba.webp") right top/contain no-repeat;opacity:.55;pointer-events:none}
  .tapa .volver{position:relative;z-index:1;display:inline-flex;gap:6px;align-items:center;font-size:13.5px;
    text-decoration:none;color:var(--tinta-suave);border:1px solid var(--linea);background:#fff;border-radius:999px;padding:5px 13px}
  .tapa .volver:hover{color:var(--acento);border-color:var(--acento)}
  .tapa .kicker{position:relative;z-index:1;display:block;margin-top:18px;font-size:11.5px;font-weight:700;
    letter-spacing:.16em;text-transform:uppercase;color:var(--acento)}
  .tapa h1{position:relative;z-index:1;font-family:var(--serif);font-weight:600;font-size:clamp(28px,3.4vw,42px);
    line-height:1.12;margin:6px 0 10px;letter-spacing:-.4px;max-width:820px}
  .tapa p{position:relative;z-index:1;margin:0;max-width:760px;color:var(--tinta-suave);font-size:15.5px}
  .tapa .datos{position:relative;z-index:1;display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}
  .tapa .datos span{font-size:12.5px;background:#fff;border:1px solid var(--linea);border-radius:999px;padding:4px 12px;color:var(--tinta-suave)}

  /* ---------- Hexaflex y filtros ---------- */
  .mapa{display:grid;grid-template-columns:minmax(260px,330px) 1fr;gap:22px;align-items:center;margin-top:20px;
    background:var(--papel);border:1px solid var(--linea);border-radius:var(--radio);padding:18px 22px}
  @media(max-width:820px){.mapa{grid-template-columns:1fr}}
  .hex svg{width:100%;height:auto;display:block}
  .hex .nodo{cursor:pointer}
  .hex .nodo circle{transition:transform .15s,stroke-width .15s;transform-box:fill-box;transform-origin:center}
  .hex .nodo:hover circle,.hex .nodo.activo circle{stroke-width:4;transform:scale(1.08)}
  .hex .nodo text{font-size:11.5px;font-weight:700;fill:#fff;pointer-events:none}
  .hex .centro-t{font-family:var(--serif);font-size:13px;fill:var(--tinta-suave)}
  .filtros h2{font-family:var(--serif);font-weight:600;font-size:21px;margin:0 0 4px}
  .filtros .ayuda{margin:0 0 12px;font-size:14px;color:var(--tinta-suave)}
  .buscador{width:100%;font:inherit;font-size:15px;padding:10px 16px;border:1px solid var(--linea);border-radius:999px;background:#fbfcfb}
  .buscador:focus{outline:none;border-color:var(--acento);background:#fff}
  .chips{display:flex;flex-wrap:wrap;gap:7px;margin-top:11px}
  .chip{font-size:13px;border:1px solid var(--linea);background:#fff;color:var(--tinta-suave);border-radius:999px;
    padding:5px 13px;display:inline-flex;gap:7px;align-items:center;line-height:1.3}
  .chip .pt{width:8px;height:8px;border-radius:50%;flex:0 0 auto}
  .chip:hover{border-color:var(--acento);color:var(--tinta)}
  .chip[aria-pressed="true"]{background:var(--tinta);border-color:var(--tinta);color:#fff;font-weight:600}
  .cuenta{margin-top:10px;font-size:13px;color:var(--tinta-suave);font-weight:600}

  /* ---------- Secciones por proceso ---------- */
  .proceso{margin-top:30px}
  .proceso[hidden]{display:none}
  .proc-cab{display:flex;gap:16px;align-items:flex-start;flex-wrap:wrap;border-radius:var(--radio);padding:18px 22px;
    background:var(--suave);border:1px solid var(--borde);border-left:6px solid var(--color)}
  .proc-cab .izq{flex:1 1 420px;min-width:0}
  .proc-cab .estilo{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--color)}
  .proc-cab h2{font-family:var(--serif);font-weight:600;font-size:25px;margin:2px 0 4px;letter-spacing:-.2px}
  .proc-cab p{margin:0;font-size:14.5px;color:var(--tinta-suave);max-width:780px}
  .proc-cab .num{font-family:var(--serif);font-size:34px;color:var(--color);line-height:1;font-weight:600}
  .proc-cab .num small{display:block;font-family:var(--sans);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--tinta-suave);font-weight:600}
  .rejilla{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,265px),1fr));gap:16px;margin-top:16px}
  .tarjeta{display:flex;flex-direction:column;min-width:0;text-align:left;background:var(--papel);border:1px solid var(--linea);
    border-radius:var(--radio);overflow:hidden;padding:0;color:inherit;transition:transform .14s,box-shadow .14s,border-color .14s}
  .tarjeta:hover{transform:translateY(-3px);box-shadow:0 8px 22px rgba(31,45,43,.10);border-color:var(--color)}
  .tarjeta[hidden]{display:none}
  .tarjeta .img{aspect-ratio:4/3;background:#ffffff center/contain no-repeat;border-bottom:1px solid var(--linea);padding:6px}
  .tarjeta .cuerpo{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}
  .tarjeta .meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:11.5px}
  .tarjeta .tipo{font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--color);background:var(--suave);border-radius:999px;padding:2px 9px}
  .tarjeta .tiempo{color:var(--tinta-suave)}
  .tarjeta b{font-family:var(--serif);font-size:17.5px;line-height:1.28;font-weight:600;overflow-wrap:break-word}
  .tarjeta .res{font-size:13.5px;color:var(--tinta-suave);line-height:1.45}
  .tarjeta .leer{margin-top:auto;padding-top:8px;font-size:13px;font-weight:600;color:var(--color)}
  .sin{margin-top:24px;padding:24px;border:1px dashed var(--linea);border-radius:var(--radio);text-align:center;color:var(--tinta-suave)}
  .sin[hidden]{display:none}
  .pie{margin-top:40px;font-size:13px;color:var(--tinta-suave);text-align:center}

  /* ---------- Lector ---------- */
  .lector{position:fixed;inset:0;z-index:50;background:rgba(24,34,32,.45);display:flex;justify-content:center;overflow-y:auto;padding:28px 14px}
  .lector[hidden]{display:none}
  .hoja-l{position:relative;width:100%;max-width:860px;background:var(--papel);border-radius:20px;overflow:hidden;
    box-shadow:0 20px 60px rgba(0,0,0,.25);align-self:flex-start}
  .l-hero{display:grid;grid-template-columns:260px 1fr;gap:0;background:var(--suave);border-bottom:1px solid var(--borde)}
  @media(max-width:680px){.l-hero{grid-template-columns:1fr}}
  .l-hero .img{min-height:220px;background:#ffffff center/contain no-repeat;padding:12px}
  @media(max-width:680px){.l-hero .img{height:220px;min-height:220px;padding:8px}}
  .l-hero .txt{padding:24px 28px}
  .l-hero .estilo{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--color)}
  .l-hero h2{font-family:var(--serif);font-weight:600;font-size:clamp(23px,2.6vw,30px);line-height:1.18;margin:6px 0 10px}
  .l-hero .res{margin:0;color:var(--tinta-suave);font-size:15px}
  .l-hero .meta{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;font-size:12.5px}
  .l-hero .meta span{background:#fff;border:1px solid var(--borde);border-radius:999px;padding:3px 11px;color:var(--tinta-suave)}
  .cerrar{position:absolute;top:12px;right:12px;z-index:2;width:38px;height:38px;border-radius:50%;border:1px solid var(--linea);background:#fff;font-size:20px;line-height:1}
  .l-cuerpo{padding:26px 34px 30px}
  @media(max-width:600px){.l-cuerpo{padding:22px 20px}}
  .l-cuerpo h3{font-family:var(--serif);font-weight:600;font-size:19px;margin:26px 0 10px;display:flex;align-items:center;gap:10px}
  .l-cuerpo h3::before{content:"";width:10px;height:10px;background:var(--color);transform:rotate(45deg);flex:0 0 auto}
  .l-cuerpo h3:first-child{margin-top:0}
  .l-cuerpo .lect p{font-family:var(--serif);font-size:18px;line-height:1.7;margin:0 0 14px;color:#24312f}
  .clave{margin:18px 0 6px;padding:16px 20px;border-radius:12px;background:var(--suave);border-left:5px solid var(--color);
    font-family:var(--serif);font-size:18px;font-style:italic;line-height:1.5}
  .preg{counter-reset:p;display:flex;flex-direction:column;gap:14px}
  .preg .p{counter-increment:p}
  .preg label{display:flex;gap:10px;font-size:15.5px;font-weight:600;line-height:1.45}
  .preg label::before{content:counter(p);flex:0 0 26px;height:26px;border-radius:50%;background:var(--color);color:#fff;
    font-size:13px;display:flex;align-items:center;justify-content:center;margin-top:1px}
  .preg textarea{width:100%;margin-top:7px;min-height:74px;resize:vertical;font:inherit;font-size:15px;padding:10px 12px;
    border:1px solid var(--linea);border-radius:10px;background:#fbfcfb}
  .preg textarea:focus{outline:none;border-color:var(--color);background:#fff}
  .practica{padding:14px 18px;border-radius:12px;border:1px dashed var(--color);background:#fff;font-size:15.5px}
  .fuente{margin-top:22px;font-size:12.5px;color:var(--tinta-suave);border-top:1px solid var(--linea);padding-top:12px}
  .rel{display:inline-flex;margin-top:10px;font-size:13.5px;font-weight:600;color:var(--color);text-decoration:none;border:1px solid var(--borde);
    border-radius:999px;padding:6px 14px;background:var(--suave)}
  .envio{border-top:1px solid var(--linea);background:#fafbfa;padding:20px 34px 26px}
  @media(max-width:600px){.envio{padding:18px 20px}}
  .envio h4{margin:0 0 4px;font-size:15px}
  .envio .ayuda{margin:0 0 12px;font-size:13px;color:var(--tinta-suave)}
  .envio .campos{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:10px;margin-bottom:14px}
  .envio label{font-size:12px;font-weight:600;color:var(--tinta-suave);display:block}
  .envio input{width:100%;margin-top:4px;font:inherit;font-size:14px;padding:8px 11px;border:1px solid var(--linea);border-radius:9px;background:#fff}
  .acciones{display:flex;flex-wrap:wrap;gap:9px}
  .btn{display:inline-flex;align-items:center;gap:8px;border-radius:999px;padding:9px 16px;font-size:14px;font-weight:600;border:1px solid var(--linea);background:#fff;color:var(--tinta)}
  .btn:hover{border-color:var(--color)}
  .btn.pdf{background:var(--color);border-color:var(--color);color:#fff}
  .btn.wa{background:#1f8f55;border-color:#1f8f55;color:#fff}
  .btn.mail{background:#3c5a78;border-color:#3c5a78;color:#fff}
  .btn[disabled]{opacity:.6;cursor:progress}
  .btn svg{width:17px;height:17px}
  .brindis{position:fixed;left:50%;bottom:26px;transform:translateX(-50%);z-index:80;background:var(--tinta);color:#fff;font-size:14px;
    padding:10px 18px;border-radius:10px;opacity:0;transition:opacity .2s;pointer-events:none;max-width:92vw;text-align:center}
  .brindis.ver{opacity:.95}

  /* ---------- Modo paciente (enlace limpio) ---------- */
  body.paciente{background:#f3f6f4}
  body.paciente .envoltura{display:none}
  body.paciente .lector{position:static;background:transparent;padding:22px 12px 50px}
  body.paciente .cerrar,body.paciente .solo-pro{display:none !important}
  body.paciente .hoja-l{box-shadow:0 8px 30px rgba(0,0,0,.08)}

  /* ---------- Hoja PDF (estética de historias clínicas JB, 2 páginas A4 calibradas) ---------- */
  .pdf-hoja{width:210mm;margin:0 auto;background:#fff;color:#22302e;font-family:var(--sans)}
  .pdf-pag{
    width:210mm;
    height:296.8mm;
    box-sizing:border-box;
    padding:12mm 14mm 13mm;
    position:relative;
    overflow:hidden;
    background:#fff;
    display:flex;
    flex-direction:column;
  }
  .pdf-pag.pag-1{page-break-after:always}
  .pdf-pag.pag-2{page-break-after:auto}
  .pdf-pag .f-arriba{position:absolute;top:0;right:0;width:85mm;height:60mm;background:url("__FONDO_ARRIBA__") right top/contain no-repeat;opacity:.85;pointer-events:none}
  .pdf-pag .f-abajo{position:absolute;bottom:0;right:0;width:80mm;height:55mm;background:url("__FONDO_ABAJO__") right bottom/contain no-repeat;opacity:.85;pointer-events:none}
  .pdf-pag > *{position:relative;z-index:1}
  .h-cab{border-radius:3mm;padding:3.5mm 5mm;margin-bottom:3.5mm;
    background:linear-gradient(90deg,var(--suave) 0%,rgba(255,255,255,.6) 60%,rgba(255,255,255,0) 90%);border-left:1.5mm solid var(--color)}
  .h-cab.mini{margin-bottom:4mm;padding:2.5mm 4mm}
  .h-cab .k{font-size:7.5pt;font-weight:700;letter-spacing:.15em;text-transform:uppercase;color:var(--color)}
  .h-cab h1{font-family:var(--serif);font-weight:600;font-size:17pt;line-height:1.18;margin:2px 0;color:#1d2a28}
  .h-cab.mini h1{font-size:14pt}
  .h-cab .sub{font-size:8.5pt;color:#5b6b68}
  .h-cab .para{margin-top:1.5mm;font-size:8pt;color:#3f4e4b}
  .h-intro{display:grid;grid-template-columns:36mm 1fr;gap:4mm;align-items:center;margin-bottom:3.5mm}
  .h-intro img{width:36mm;height:36mm;object-fit:contain;background:#fff;border-radius:2.5mm;border:1px solid var(--borde);padding:1mm}
  .h-intro .res{font-family:var(--serif);font-size:10pt;line-height:1.45;color:#2c3a38;margin:0 0 2mm}
  .h-intro .chips-p{display:flex;gap:2mm;flex-wrap:wrap}
  .h-intro .chips-p span{font-size:7.5pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--color);background:var(--suave);border:1px solid var(--borde);border-radius:999px;padding:1px 7px}
  .h-intro .desc-p{margin-top:1.5mm;font-size:8.5pt;color:#5b6b68;line-height:1.35}
  .pdf-hoja h2{font-family:var(--serif);font-weight:600;font-size:11pt;margin:3mm 0 2mm;color:#1d2a28;display:flex;align-items:center;gap:2mm}
  .pdf-hoja h2::before{content:"";width:2.2mm;height:2.2mm;background:var(--color);transform:rotate(45deg);flex:0 0 auto}
  .pdf-hoja .lect{font-family:var(--serif);font-size:9.8pt;line-height:1.58;color:#24312f}
  .pdf-hoja .lect p{margin:0 0 2.5mm;text-align:justify}
  .pdf-hoja .clave-p{margin:3mm 0 0;padding:2.8mm 4mm;border-radius:2.5mm;background:var(--suave);border-left:1.2mm solid var(--color);
    font-family:var(--serif);font-style:italic;font-size:9.6pt;line-height:1.45;color:#263331}
  .pdf-hoja .pie-pag{margin-top:auto;padding-top:2.5mm;border-top:1px solid #e2ece9;font-size:7.5pt;color:#728280;display:flex;justify-content:space-between}
  .pdf-hoja .q{margin:0 0 3.5mm}
  .pdf-hoja .q b{display:flex;gap:2mm;font-size:9.5pt;line-height:1.4;color:#1e2c2a}
  .pdf-hoja .q b i{font-style:normal;flex:0 0 4.5mm;height:4.5mm;border-radius:50%;background:var(--color);color:#fff;font-size:7.5pt;font-weight:700;display:flex;align-items:center;justify-content:center}
  .pdf-hoja .q .resp{margin:1.5mm 0 0 6.5mm;font-family:var(--serif);font-size:9pt;color:#2c3a38;white-space:pre-wrap;background:rgba(255,255,255,.8);border:1px solid var(--borde);border-radius:2mm;padding:2mm 3mm}
  .pdf-hoja .q .lineas{margin:1.5mm 0 0 6.5mm;height:12mm;background:repeating-linear-gradient(transparent 0 3.8mm,var(--borde) 3.8mm 4mm)}
  .pdf-hoja .prac{padding:3mm 4mm;border:1px dashed var(--color);border-radius:2.5mm;background:rgba(255,255,255,.85);font-size:9pt;line-height:1.48;color:#22302e}
  .pdf-hoja .fte{margin-top:3mm;font-size:7.5pt;color:#6a7976;line-height:1.35}
  .pdf-hoja .firma{margin-top:3.5mm;padding-top:2mm;border-top:1px solid var(--borde);display:flex;justify-content:space-between;gap:3mm;font-size:8pt;color:#5b6b68}
  .pdf-hoja .firma b{display:block;font-size:9pt;color:#22302e}

  @media print{
    body.imprimiendo > *:not(#zona-impresion){display:none !important}
    body.imprimiendo #zona-impresion{display:block !important}
    @page{size:A4 portrait;margin:0}
  }
  #zona-impresion{display:none}
</style>
</head>
<body>
<div class="envoltura" id="tablero">
  <header class="tapa">
    <a class="volver" href="index.html">&larr; Herramientas interactivas</a>
    <span class="kicker">Lecturas ACT · Lectura acompañada y reflexión</span>
    <h1>Lecturas para leer en sesión y llevar a casa</h1>
    <p>Metáforas, ejercicios experienciales y hojas de reflexión de la Terapia de Aceptación y Compromiso,
    organizadas por los seis procesos del hexaflex. Cada lectura se acompaña de preguntas para conversar
    con el paciente y puede enviarse como PDF por WhatsApp o por correo.</p>
    <div class="datos"><span>__N__ lecturas</span><span>6 procesos del hexaflex</span><span>Respaldo en manuales oficiales de ACT</span></div>
  </header>

  <section class="mapa" aria-label="Filtrar por proceso">
    <div class="hex">__HEX__</div>
    <div class="filtros">
      <h2>Buscar una lectura</h2>
      <p class="ayuda">Toca un vértice del hexaflex o filtra por tipo de recurso.</p>
      <input class="buscador" id="buscar" type="search" placeholder="Buscar por título, metáfora o idea…" autocomplete="off">
      <div class="chips" id="chipsProc" role="group" aria-label="Proceso">__CHIPS_PROC__</div>
      <div class="chips" id="chipsTipo" role="group" aria-label="Tipo de recurso">__CHIPS_TIPO__</div>
      <div class="cuenta" id="cuenta"></div>
    </div>
  </section>

__SECCIONES__
  <div class="sin" id="sinRes" hidden>Ninguna lectura coincide con la búsqueda.</div>
  <p class="pie">__PROF__ · __CRED__</p>
</div>

<div class="lector" id="lector" hidden role="dialog" aria-modal="true" aria-labelledby="lTitulo">
  <article class="hoja-l" id="hojaL">
    <button type="button" class="cerrar" id="lCerrar" aria-label="Cerrar">&times;</button>
    <div class="l-hero">
      <div class="img" id="lImg"></div>
      <div class="txt">
        <span class="estilo" id="lEstilo"></span>
        <h2 id="lTitulo"></h2>
        <p class="res" id="lRes"></p>
        <div class="meta" id="lMeta"></div>
      </div>
    </div>
    <div class="l-cuerpo">
      <h3>Lectura</h3>
      <div class="lect" id="lLect"></div>
      <div class="clave" id="lClave"></div>
      <h3>Para reflexionar</h3>
      <div class="preg" id="lPreg"></div>
      <h3>Práctica sugerida</h3>
      <div class="practica" id="lPrac"></div>
      <div class="fuente"><b>Fuente:</b> <span id="lFuente"></span></div>
      <a class="rel solo-pro" id="lRel" href="#">Abrir la herramienta interactiva relacionada &rarr;</a>
    </div>
    <div class="envio">
      <h4>Guardar o enviar esta lectura</h4>
      <p class="ayuda solo-pro">El PDF incluye lo que se haya escrito en las preguntas. En celular o tableta, WhatsApp y correo adjuntan el PDF directamente; en computador se descarga el PDF para arrastrarlo al chat o al correo, que se abren con el mensaje listo.</p>
      <div class="campos solo-pro">
        <div><label for="eNombre">Nombre del paciente (opcional)</label><input id="eNombre" type="text" placeholder="Aparece en el PDF"></div>
        <div><label for="eTel">WhatsApp (opcional)</label><input id="eTel" type="tel" placeholder="Ej.: 573001234567"></div>
        <div><label for="eCorreo">Correo (opcional)</label><input id="eCorreo" type="email" placeholder="paciente@correo.com"></div>
      </div>
      <div class="acciones">
        <button type="button" class="btn pdf" id="bPdf">__ICO_PDF__ Descargar PDF</button>
        <button type="button" class="btn wa solo-pro" id="bWa">__ICO_WA__ Enviar por WhatsApp</button>
        <button type="button" class="btn mail solo-pro" id="bMail">__ICO_MAIL__ Enviar por correo</button>
        <button type="button" class="btn solo-pro" id="bLink">__ICO_LINK__ Copiar enlace</button>
        <button type="button" class="btn" id="bPrint">__ICO_PRINT__ Imprimir</button>
      </div>
    </div>
  </article>
</div>

<div id="zona-impresion"></div>
<div class="brindis" id="brindis"></div>

<script>
const PROCESOS = __PROCESOS_JSON__;
const LECTURAS = __LECTURAS_JSON__;
const PROF = __PROF_JSON__, CRED = __CRED_JSON__;


const por = id => document.getElementById(id);
const P = Object.fromEntries(PROCESOS.map(p => [p.id, p]));
const L = Object.fromEntries(LECTURAS.map(l => [l.slug, l]));
const esc = s => String(s).replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
let actual = null;
let filtroProc = "todos", filtroTipo = "todos";

function brindis(t){
  const b = por("brindis"); b.textContent = t; b.classList.add("ver");
  clearTimeout(brindis.t); brindis.t = setTimeout(() => b.classList.remove("ver"), 3200);
}
function colores(el, p){
  el.style.setProperty("--color", p.color);
  el.style.setProperty("--suave", p.suave);
  el.style.setProperty("--borde", p.borde);
}

/* ---------------- Filtros ---------------- */
function filtrar(){
  const q = por("buscar").value.trim().toLowerCase();
  let n = 0;
  document.querySelectorAll(".proceso").forEach(sec => {
    let visibles = 0;
    sec.querySelectorAll(".tarjeta").forEach(t => {
      const l = L[t.dataset.slug];
      const txt = (l.titulo + " " + l.resumen + " " + l.tipo + " " + l.lectura.join(" ")).toLowerCase();
      const ok = (filtroProc === "todos" || l.proceso === filtroProc) &&
                 (filtroTipo === "todos" || l.tipo === filtroTipo) &&
                 (!q || txt.includes(q));
      t.hidden = !ok; if(ok){ visibles++; n++; }
    });
    sec.hidden = visibles === 0;
  });
  por("cuenta").textContent = n + (n === 1 ? " lectura" : " lecturas");
  por("sinRes").hidden = n > 0;
  document.querySelectorAll(".hex .nodo").forEach(g => g.classList.toggle("activo", g.dataset.proc === filtroProc));
}
function marcar(grupo, valor){
  document.querySelectorAll("#" + grupo + " .chip").forEach(c => c.setAttribute("aria-pressed", c.dataset.v === valor ? "true" : "false"));
}
document.querySelectorAll("#chipsProc .chip").forEach(c => c.addEventListener("click", () => { filtroProc = c.dataset.v; marcar("chipsProc", filtroProc); filtrar(); }));
document.querySelectorAll("#chipsTipo .chip").forEach(c => c.addEventListener("click", () => { filtroTipo = c.dataset.v; marcar("chipsTipo", filtroTipo); filtrar(); }));
document.querySelectorAll(".hex .nodo").forEach(g => g.addEventListener("click", () => {
  filtroProc = filtroProc === g.dataset.proc ? "todos" : g.dataset.proc;
  marcar("chipsProc", filtroProc); filtrar();
  if(filtroProc !== "todos") document.querySelector('.proceso[data-proc="' + filtroProc + '"]').scrollIntoView({behavior:"smooth", block:"start"});
}));
por("buscar").addEventListener("input", filtrar);

/* ---------------- Lector ---------------- */
function claveResp(slug){ return "lecturas-act:" + slug; }
function guardarResp(){
  if(!actual) return;
  const r = [...document.querySelectorAll("#lPreg textarea")].map(t => t.value);
  try{ localStorage.setItem(claveResp(actual.slug), JSON.stringify(r)); }catch(e){}
}
function abrir(slug, empujar){
  const l = L[slug]; if(!l) return;
  actual = l; const p = P[l.proceso];
  colores(por("hojaL"), p);
  por("lImg").style.backgroundImage = "url('arte/lecturas/" + l.slug + ".webp')";
  por("lEstilo").textContent = p.estilo_nombre + " · " + p.nombre;
  por("lTitulo").textContent = l.titulo;
  por("lRes").textContent = l.resumen;
  por("lMeta").innerHTML = "<span>" + esc(l.tipo) + "</span><span>" + esc(l.tiempo) + " de lectura</span>";
  por("lLect").innerHTML = l.lectura.map(x => "<p>" + esc(x) + "</p>").join("");
  por("lClave").textContent = l.clave;
  let prev = [];
  try{ prev = JSON.parse(localStorage.getItem(claveResp(l.slug)) || "[]"); }catch(e){}
  por("lPreg").innerHTML = l.preguntas.map((q, i) =>
    '<div class="p"><label for="lq' + i + '">' + esc(q) + '</label><textarea id="lq' + i + '" placeholder="Escribir aquí (opcional)…">' + esc(prev[i] || "") + '</textarea></div>').join("");
  document.querySelectorAll("#lPreg textarea").forEach(t => t.addEventListener("input", guardarResp));
  por("lPrac").textContent = l.practica;
  por("lFuente").textContent = l.fuente;
  por("lRel").href = l.herramienta;
  por("lector").hidden = false;
  if(!document.body.classList.contains("paciente")) document.body.style.overflow = "hidden";
  por("lector").scrollTop = 0;
  if(empujar){
    const u = new URL(location.href); u.searchParams.set("lectura", slug); u.searchParams.delete("modo");
    history.pushState({slug}, "", u);
  }
  document.title = l.titulo + " · Lecturas ACT";
}
function cerrar(){
  por("lector").hidden = true; document.body.style.overflow = ""; actual = null;
  const u = new URL(location.href); u.searchParams.delete("lectura"); u.searchParams.delete("modo");
  history.pushState({}, "", u);
  document.title = "Lecturas ACT · Lectura acompañada y reflexión";
}
document.querySelectorAll(".tarjeta").forEach(t => t.addEventListener("click", () => abrir(t.dataset.slug, true)));
por("lCerrar").addEventListener("click", cerrar);
por("lector").addEventListener("click", e => { if(e.target === por("lector") && !document.body.classList.contains("paciente")) cerrar(); });
document.addEventListener("keydown", e => { if(e.key === "Escape" && !por("lector").hidden && !document.body.classList.contains("paciente")) cerrar(); });
window.addEventListener("popstate", () => {
  const s = new URL(location.href).searchParams.get("lectura");
  if(s && L[s]) abrir(s, false); else if(!por("lector").hidden){ por("lector").hidden = true; document.body.style.overflow = ""; }
});

/* ---------------- Hoja PDF ---------------- */
function nombreArchivo(l){ return "Lectura ACT - " + l.titulo.replace(/[\\/:*?"<>|«»]/g, "").replace(/\s+/g, " ").trim().slice(0, 80) + ".pdf"; }
function enlacePaciente(l){
  const u = new URL(location.href); u.search = ""; u.hash = "";
  u.searchParams.set("lectura", l.slug); u.searchParams.set("modo", "paciente");
  return u.toString();
}
function construirHoja(l){
  const p = P[l.proceso];
  const resp = [...document.querySelectorAll("#lPreg textarea")].map(t => t.value.trim());
  const nombre = (por("eNombre").value || "").trim();
  const fecha = new Date().toLocaleDateString("es-CO", {day:"numeric", month:"long", year:"numeric"});
  const d = document.createElement("div");
  d.className = "pdf-hoja"; colores(d, p);
  d.innerHTML =
    '<div class="pdf-pag pag-1">' +
      '<div class="f-arriba"></div>' +
      '<div class="h-cab">' +
        '<div class="k">Terapia de Aceptación y Compromiso · ' + esc(p.nombre) + '</div>' +
        '<h1>' + esc(l.titulo) + '</h1>' +
        '<div class="sub">' + esc(p.estilo_nombre) + ' · ' + esc(l.tipo) + ' · ' + esc(l.tiempo) + ' de lectura</div>' +
        '<div class="para">' + (nombre ? "Preparado para: <b>" + esc(nombre) + "</b> · " : "") + esc(fecha) + '</div>' +
      '</div>' +
      '<div class="h-intro">' +
        '<img src="arte/lecturas/' + l.slug + '.webp" alt="Ilustración">' +
        '<div>' +
          '<p class="res">' + esc(l.resumen) + '</p>' +
          '<div class="chips-p"><span>' + esc(p.corto) + '</span><span>' + esc(l.tipo) + '</span></div>' +
          '<p class="desc-p">' + esc(p.desc) + '</p>' +
        '</div>' +
      '</div>' +
      '<h2>Lectura</h2>' +
      '<div class="lect">' + l.lectura.map(x => "<p>" + esc(x) + "</p>").join("") + '</div>' +
      '<div class="clave-p">' + esc(l.clave) + '</div>' +
      '<div class="pie-pag">' +
        '<span>Lecturas ACT · Material de consulta y reflexión</span>' +
        '<span>Página 1 de 2 · Continúa con las preguntas de reflexión y práctica &rarr;</span>' +
      '</div>' +
    '</div>' +
    '<div class="pdf-pag pag-2">' +
      '<div class="f-abajo"></div>' +
      '<div class="h-cab mini">' +
        '<div class="k">Terapia de Aceptación y Compromiso · Taller de reflexión</div>' +
        '<h1>' + esc(l.titulo) + '</h1>' +
        '<div class="sub">Preguntas de reflexión y práctica personal</div>' +
      '</div>' +
      '<h2>Para reflexionar en sesión o en casa</h2>' +
      l.preguntas.map((q, i) => '<div class="q"><b><i>' + (i + 1) + '</i>' + esc(q) + '</b>' +
        (resp[i] ? '<div class="resp">' + esc(resp[i]) + '</div>' : '<div class="lineas"></div>') + '</div>').join("") +
      '<h2>Práctica sugerida para la semana</h2>' +
      '<div class="prac">' + esc(l.practica) + '</div>' +
      '<div class="fte"><b>Fuente clínica:</b> ' + esc(l.fuente) + '</div>' +
      '<div class="firma">' +
        '<div><b>' + esc(PROF) + '</b>' + esc(CRED) + '</div>' +
        '<div style="text-align:right">Material de acompañamiento terapéutico<br>Uso personal del paciente</div>' +
      '</div>' +
      '<div class="pie-pag">' +
        '<span>Lecturas ACT · Reflexión y práctica</span>' +
        '<span>Página 2 de 2</span>' +
      '</div>' +
    '</div>';
  return d;
}
const H2PDF_LOCAL = "arte/html2pdf.bundle.min.js";
const H2PDF_CDN = "https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js";
let cargaLib = null;
function cargarH2P(){
  if(window.html2pdf) return Promise.resolve();
  if(cargaLib) return cargaLib;
  cargaLib = new Promise((ok, mal) => {
    const s = document.createElement("script");
    s.src = H2PDF_LOCAL;
    s.onload = ok;
    s.onerror = () => {
      const s2 = document.createElement("script");
      s2.src = H2PDF_CDN;
      s2.onload = ok;
      s2.onerror = () => { cargaLib = null; mal(new Error("sin conexión")); };
      document.head.appendChild(s2);
    };
    document.head.appendChild(s);
  });
  return cargaLib;
}
async function generarPdf(l){
  await cargarH2P();
  const hoja = construirHoja(l);
  const wrap = document.createElement("div");
  wrap.style.cssText = "position:fixed;left:-9999px;top:0;width:210mm;z-index:-9999;background:#ffffff;visibility:visible;";
  wrap.appendChild(hoja);
  document.body.appendChild(wrap);

  try {
    const imgs = hoja.querySelectorAll("img");
    await Promise.all(Array.from(imgs).map(img => {
      if(img.complete) return Promise.resolve();
      return new Promise(res => { img.onload = res; img.onerror = res; });
    }));
    if(document.fonts && document.fonts.ready) await document.fonts.ready;

    const opts = {
      margin: 0,
      filename: nombreArchivo(l),
      image: {type: "jpeg", quality: 0.95},
      html2canvas: {scale: 2, useCORS: true, backgroundColor: "#ffffff"},
      jsPDF: {unit: "mm", format: "a4", orientation: "portrait"},
      pagebreak: {mode: "css"}
    };
    return await html2pdf().set(opts).from(hoja).outputPdf("blob");
  } finally {
    wrap.remove();
  }
}
function descargar(blob, nombre){
  const a = document.createElement("a"); a.href = URL.createObjectURL(blob); a.download = nombre;
  document.body.appendChild(a); a.click(); setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 1500);
}
function imprimir(l){
  const z = por("zona-impresion"); z.innerHTML = ""; z.appendChild(construirHoja(l));
  document.body.classList.add("imprimiendo");
  setTimeout(() => { window.print(); document.body.classList.remove("imprimiendo"); }, 400);
}
async function conBoton(btn, fn){
  btn.disabled = true; const t = btn.innerHTML; btn.innerHTML = "Preparando PDF…";
  try{ await fn(); } finally { btn.disabled = false; btn.innerHTML = t; }
}
function mensaje(l){
  const nombre = (por("eNombre").value || "").trim();
  return (nombre ? "Hola, " + nombre + ". " : "Hola. ") +
    "Te comparto la lectura «" + l.titulo + "» que conversamos en sesión. " +
    "Léela con calma y, si quieres, responde las preguntas de reflexión para retomarlas en nuestro próximo encuentro.";
}
async function obtenerPdf(l){
  try{ return await generarPdf(l); }
  catch(e){ brindis("No se pudo generar el PDF aquí (¿sin conexión?). Se abre la impresión para guardarlo como PDF."); imprimir(l); return null; }
}

por("bPdf").addEventListener("click", e => conBoton(e.currentTarget, async () => {
  const b = await obtenerPdf(actual); if(b){ descargar(b, nombreArchivo(actual)); brindis("PDF descargado."); }
}));
por("bPrint").addEventListener("click", () => imprimir(actual));
por("bLink").addEventListener("click", async () => {
  const u = enlacePaciente(actual);
  try{ await navigator.clipboard.writeText(u); brindis("Enlace limpio copiado."); } catch(e){ prompt("Copia el enlace:", u); }
});
por("bWa").addEventListener("click", e => conBoton(e.currentTarget, async () => {
  const l = actual, texto = mensaje(l) + "\n\n" + enlacePaciente(l);
  const b = await obtenerPdf(l); if(!b) return;
  const f = new File([b], nombreArchivo(l), {type: "application/pdf"});
  if(navigator.canShare && navigator.canShare({files: [f]})){
    try{ await navigator.share({files: [f], title: l.titulo, text: mensaje(l)}); return; } catch(err){ if(err && err.name === "AbortError") return; }
  }
  descargar(b, nombreArchivo(l));
  const tel = (por("eTel").value || "").replace(/\D/g, "");
  window.open("https://wa.me/" + tel + "?text=" + encodeURIComponent(texto), "_blank");
  brindis("PDF descargado: arrástralo al chat de WhatsApp que se acaba de abrir.");
}));
por("bMail").addEventListener("click", e => conBoton(e.currentTarget, async () => {
  const l = actual;
  const b = await obtenerPdf(l); if(!b) return;
  const f = new File([b], nombreArchivo(l), {type: "application/pdf"});
  const correo = (por("eCorreo").value || "").trim();
  const asunto = "Lectura ACT: " + l.titulo;
  const cuerpo = mensaje(l) + "\n\nAdjunto el PDF. También puedes leerla en línea aquí:\n" + enlacePaciente(l) + "\n\nUn saludo,\n" + PROF + "\n" + CRED;
  if(!correo && navigator.canShare && navigator.canShare({files: [f]}) && /Android|iPhone|iPad/i.test(navigator.userAgent)){
    try{ await navigator.share({files: [f], title: asunto, text: cuerpo}); return; } catch(err){ if(err && err.name === "AbortError") return; }
  }
  descargar(b, nombreArchivo(l));
  location.href = "mailto:" + encodeURIComponent(correo) + "?subject=" + encodeURIComponent(asunto) + "&body=" + encodeURIComponent(cuerpo);
  brindis("PDF descargado: adjúntalo al correo que se acaba de abrir.");
}));

/* ---------------- Arranque ---------------- */
(function(){
  const q = new URL(location.href).searchParams;
  const s = q.get("lectura");
  if(q.get("modo") === "paciente" && s && L[s]) document.body.classList.add("paciente");
  filtrar();
  if(s && L[s]) abrir(s, false);
})();
</script>
</body>
</html>
"""

ICONOS = {
    "PDF": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v12m0 0l-4-4m4 4l4-4M4 17v3h16v-3"/></svg>',
    "WA": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm0 18.2a8.2 8.2 0 01-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1112 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 01-3.3-2.9c-.3-.4.3-.4.8-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 00-.7.3 3 3 0 00-.9 2.2 5.2 5.2 0 001.1 2.8 11.9 11.9 0 004.6 4c1.7.7 2.4.8 3.2.7a2.8 2.8 0 001.9-1.3 2.3 2.3 0 00.2-1.3c-.1-.1-.2-.2-.4-.3z"/></svg>',
    "MAIL": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "LINK": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 14a4 4 0 005.7 0l3-3a4 4 0 00-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 00-5.7 0l-3 3a4 4 0 005.7 5.7l1-1"/></svg>',
    "PRINT": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9V3h12v6M6 18H4v-6h16v6h-2M8 14h8v7H8z"/></svg>',
}


def hexaflex():
    """Hexágono con los seis procesos en la disposición clásica del hexaflex."""
    import math
    orden = ["presente", "aceptacion", "valores", "defusion", "accion", "yo"]
    # posiciones: arriba (presente), arriba-izq (aceptación), arriba-der (valores),
    # abajo-izq (defusión), abajo-der (acción), abajo (yo como contexto)
    angulos = {"presente": -90, "valores": -30, "accion": 30, "yo": 90, "defusion": 150, "aceptacion": 210}
    cx, cy, r = 160, 150, 108
    pts = {k: (cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for k, a in angulos.items()}
    ciclo = ["presente", "valores", "accion", "yo", "defusion", "aceptacion"]
    poly = " ".join("%.1f,%.1f" % pts[k] for k in ciclo)
    lineas = []
    for i, a in enumerate(ciclo):
        for b in ciclo[i + 1:]:
            lineas.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#dfe6e4" stroke-width="1.2"/>' % (*pts[a], *pts[b]))
    P = {p["id"]: p for p in datos.PROCESOS}
    nodos = []
    for k in orden:
        x, y = pts[k]
        p = P[k]
        etq = p["corto"].replace("Acción comprometida", "Acción").replace("Momento presente", "Presente").replace("Yo como contexto", "Yo-contexto")
        nodos.append(
            '<g class="nodo" data-proc="%s" role="button" tabindex="0" aria-label="%s"><title>%s</title>'
            '<circle cx="%.1f" cy="%.1f" r="38" fill="%s" stroke="#fff" stroke-width="3"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle">%s</text></g>'
            % (k, _h.escape(p["nombre"]), _h.escape(p["nombre"]), x, y, p["color"], x, y + 4, _h.escape(etq))
        )
    return (
        '<svg viewBox="0 0 320 300" role="img" aria-label="Hexaflex: toca un proceso para filtrar las lecturas">'
        '<polygon points="%s" fill="#f8faf8" stroke="#c9d5d1" stroke-width="2"/>%s'
        '<text class="centro-t" x="160" y="146" text-anchor="middle">Flexibilidad</text>'
        '<text class="centro-t" x="160" y="163" text-anchor="middle">psicológica</text>%s</svg>'
        % (poly, "".join(lineas), "".join(nodos))
    )


def construir():
    P = {p["id"]: p for p in datos.PROCESOS}
    tipos = sorted({l["tipo"] for l in datos.LECTURAS})
    chips_proc = '<button type="button" class="chip" data-v="todos" aria-pressed="true">Todos los procesos</button>' + "".join(
        '<button type="button" class="chip" data-v="%s" aria-pressed="false"><span class="pt" style="background:%s"></span>%s</button>'
        % (p["id"], p["color"], _h.escape(p["corto"])) for p in datos.PROCESOS
    )
    chips_tipo = '<button type="button" class="chip" data-v="todos" aria-pressed="true">Todos los tipos</button>' + "".join(
        '<button type="button" class="chip" data-v="%s" aria-pressed="false">%s</button>' % (_h.escape(t), _h.escape(t)) for t in tipos
    )
    secciones = []
    for p in datos.PROCESOS:
        suyas = [l for l in datos.LECTURAS if l["proceso"] == p["id"]]
        tarjetas = "\n".join(
            '      <button type="button" class="tarjeta" data-slug="%s">'
            '<span class="img" style="background-image:url(\'arte/lecturas/%s.webp\')" role="img" aria-label="Ilustración"></span>'
            '<span class="cuerpo"><span class="meta"><span class="tipo">%s</span><span class="tiempo">%s</span></span>'
            '<b>%s</b><span class="res">%s</span><span class="leer">Leer y reflexionar &rarr;</span></span></button>'
            % (l["slug"], l["slug"], _h.escape(l["tipo"]), _h.escape(l["tiempo"]), _h.escape(l["titulo"]), _h.escape(l["resumen"]))
            for l in suyas
        )
        secciones.append(
            '  <section class="proceso" data-proc="%s" id="p-%s" style="--color:%s;--suave:%s;--borde:%s">\n'
            '    <div class="proc-cab"><div class="izq"><span class="estilo">%s</span><h2>%s</h2><p>%s</p></div>'
            '<div class="num">%d<small>lecturas</small></div></div>\n'
            '    <div class="rejilla">\n%s\n    </div>\n  </section>'
            % (p["id"], p["id"], p["color"], p["suave"], p["borde"], _h.escape(p["estilo_nombre"]),
               _h.escape(p["nombre"]), _h.escape(p["desc"]), len(suyas), tarjetas)
        )

    def js(o):
        return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")

    fondo_arriba = "data:image/webp;base64," + base64.b64encode((DESTINO.parent / "arte" / "fondo-act-arriba.webp").read_bytes()).decode("ascii")
    fondo_abajo = "data:image/webp;base64," + base64.b64encode((DESTINO.parent / "arte" / "fondo-act-abajo.webp").read_bytes()).decode("ascii")
    out = PLANTILLA
    reemplazos = {
        "__FONDO_ARRIBA__": fondo_arriba,
        "__FONDO_ABAJO__": fondo_abajo,
        "__N__": str(len(datos.LECTURAS)),
        "__HEX__": hexaflex(),
        "__CHIPS_PROC__": chips_proc,
        "__CHIPS_TIPO__": chips_tipo,
        "__SECCIONES__": "\n".join(secciones),
        "__PROF__": _h.escape(PROFESIONAL),
        "__CRED__": _h.escape(CREDENCIAL),
        "__PROCESOS_JSON__": js(datos.PROCESOS),
        "__LECTURAS_JSON__": js(datos.LECTURAS),
        "__PROF_JSON__": js(PROFESIONAL),
        "__CRED_JSON__": js(CREDENCIAL),
    }
    for k, v in ICONOS.items():
        reemplazos["__ICO_%s__" % k] = v
    for k, v in reemplazos.items():
        out = out.replace(k, v)
    DESTINO.write_text(out, encoding="utf-8")
    return len(datos.LECTURAS)


if __name__ == "__main__":
    n = construir()
    print("lecturas-act.html con %d lecturas." % n)
