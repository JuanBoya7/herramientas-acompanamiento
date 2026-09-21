# -*- coding: utf-8 -*-
"""
Columnas laterales del índice y de la guía de uso.

En pantallas anchas la página usa todo el ancho: a la izquierda, el buscador
y el filtro por enfoque; a la derecha, un mapa con las hojas. Las dos quedan
fijas mientras se recorre el centro. En pantallas medianas y en el teléfono
los filtros vuelven arriba del contenido y el mapa se oculta.

La página que las usa marca:
  - [data-grupo="Enfoque"]  cada bloque que se esconde si queda vacío,
  - [data-item]             cada elemento que se filtra, con data-enf,
                            data-titulo y, si abre otra página, data-href.
El mapa se arma solo a partir de esas marcas.
"""

ENFOQUES = ["Metáforas vivas", "Psicología positiva", "ACT", "DBT", "Cognitivo-conductual"]


def controles(placeholder):
    chips = "".join(
        '<button class="fchip" type="button" data-enf="%s" aria-pressed="false">%s</button>' % (e, e)
        for e in ENFOQUES)
    return f"""<aside class="riel-izq" aria-label="Filtros">
  <div class="controles">
    <input class="buscador" id="buscador" type="search" placeholder="{placeholder}" autocomplete="off">
    <div class="controles-r">Enfoque</div>
    <div class="fila" id="f-enf">
      <button class="fchip" type="button" data-enf="todos" aria-pressed="true">Todos</button>{chips}
    </div>
    <div class="cuenta" id="cuenta"></div>
  </div>
</aside>"""


MAPA = """<aside class="riel-der">
  <nav class="mapa" id="mapa" aria-label="Mapa de las hojas"></nav>
</aside>"""


CSS = """
  /* ---- Distribución con columnas laterales ---- */
  .envoltura.con-rieles{display:grid;grid-template-columns:minmax(0,1fr);
    grid-template-areas:"cab" "izq" "centro"}
  .con-rieles > .cab{grid-area:cab}
  .con-rieles > .riel-izq{grid-area:izq}
  .con-rieles > .centro{grid-area:centro;min-width:0}
  .con-rieles > .riel-der{display:none}
  .controles{background:var(--papel);border:1px solid var(--linea);border-radius:var(--radio);
    padding:14px 16px;margin-bottom:16px}
  .controles .fila{display:flex;flex-wrap:wrap;gap:6px}
  .controles-r{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
    color:var(--tinta-suave);margin:12px 0 6px}
  .buscador{width:100%;box-sizing:border-box;font:inherit;font-size:14px;padding:8px 13px;
    border:1px solid var(--linea);border-radius:999px;background:#fff}
  .buscador:focus{outline:none;border-color:var(--acento)}
  .fchip{font:inherit;font-size:13px;border:1px solid var(--linea);border-radius:999px;
    padding:5px 12px;background:#fff;color:var(--tinta-suave);cursor:pointer}
  .fchip:hover{border-color:var(--acento);color:var(--tinta)}
  .fchip[aria-pressed="true"]{background:var(--acento);border-color:var(--acento);color:#fff;font-weight:600}
  .cuenta{margin-top:12px;font-size:12.5px;color:var(--tinta-suave);line-height:1.45}
  [data-grupo][hidden],[data-item][hidden]{display:none !important}
  .sin-resultados{border:1px dashed var(--linea);border-radius:var(--radio);padding:22px;
    text-align:center;color:var(--tinta-suave);font-size:14px}
  .sin-resultados[hidden]{display:none}

  .mapa-r{display:block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
    color:var(--tinta-suave);margin:2px 0 10px}
  .mapa-g{margin-top:14px}
  .mapa-g[hidden],.mapa li[hidden]{display:none}
  .mapa-g > a{display:block;font-weight:700;font-size:14px;color:var(--tinta);text-decoration:none;
    margin-bottom:4px}
  .mapa ul{list-style:none;margin:0;padding:0 0 0 10px;border-left:2px solid var(--linea)}
  .mapa li a{display:block;font-size:13px;line-height:1.35;color:var(--tinta-suave);text-decoration:none;
    padding:4px 8px;border-radius:6px;margin-left:-2px;border-left:2px solid transparent}
  .mapa a:hover{color:var(--acento);background:var(--acento-claro)}
  .mapa li a.actual{color:var(--acento);border-left-color:var(--acento);background:var(--acento-claro);
    font-weight:600}
  .mapa .extra{display:block;margin-top:16px;font-size:13px;font-weight:600;color:var(--acento);
    text-decoration:none}

  @media (min-width:1280px){
    .envoltura.con-rieles{max-width:none;padding-left:clamp(20px,2vw,36px);
      padding-right:clamp(20px,2vw,36px);
      grid-template-columns:clamp(236px,17vw,290px) minmax(0,1fr) clamp(236px,17vw,290px);
      grid-template-areas:"izq cab der" "izq centro der";grid-template-rows:auto 1fr;
      column-gap:clamp(24px,2.4vw,44px)}
    .con-rieles > .riel-der{display:block;grid-area:der}
    .con-rieles .controles,.con-rieles .mapa{position:sticky;top:20px;max-height:calc(100vh - 40px);
      overflow-y:auto;overscroll-behavior:contain;scrollbar-width:thin}
    .con-rieles .controles{margin:0}
    .con-rieles [id]{scroll-margin-top:18px}
  }
  @media print{
    .con-rieles > .riel-izq,.con-rieles > .riel-der{display:none !important}
    .envoltura.con-rieles{display:block}
  }
"""


JS = r"""
(function(){
  const $ = id => document.getElementById(id);
  const norm = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  const items = [...document.querySelectorAll("[data-item]")];
  const grupos = [...document.querySelectorAll("[data-grupo]")];
  items.forEach(el => { el.dataset.txt = norm(el.textContent); });

  // Mapa: un encabezado por enfoque y, debajo, sus hojas.
  const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  $("mapa").innerHTML = '<span class="mapa-r">Las hojas</span>' + grupos.map((g, gi) => {
    if (!g.id) g.id = "grupo-" + gi;
    const suyos = items.filter(it => g.contains(it));
    return '<div class="mapa-g" data-g="' + g.id + '"><a href="#' + g.id + '">' + esc(g.dataset.grupo) + '</a><ul>' +
      suyos.map((it, ii) => {
        if (!it.id) it.id = g.id + "-" + ii;
        const destino = it.dataset.href || ("#" + it.id);
        return '<li data-i="' + it.id + '"><a href="' + esc(destino) + '" data-i="' + it.id + '">' + esc(it.dataset.titulo) + '</a></li>';
      }).join("") + '</ul></div>';
  }).join("") + (document.body.dataset.extra || "");

  let enf = "todos";
  function aplicar(){
    const q = norm($("buscador").value.trim());
    let n = 0;
    items.forEach(it => {
      const ok = (enf === "todos" || it.dataset.enf === enf) && (!q || it.dataset.txt.includes(q));
      it.hidden = !ok;
      $("mapa").querySelector('li[data-i="' + it.id + '"]').hidden = !ok;
      if (ok) n++;
    });
    grupos.forEach(g => {
      const vacio = !items.some(it => !it.hidden && g.contains(it));
      g.hidden = vacio;
      $("mapa").querySelector('[data-g="' + g.id + '"]').hidden = vacio;
    });
    $("cuenta").textContent = n + (n === 1 ? " hoja" : " hojas") +
      (enf === "todos" ? "" : " de " + enf) + (q ? (n === 1 ? " que coincide" : " que coinciden") + " con la búsqueda" : "");
    const vacia = $("sin-resultados");
    if (vacia) vacia.hidden = n > 0;
  }
  $("f-enf").addEventListener("click", ev => {
    const b = ev.target.closest(".fchip"); if (!b) return;
    enf = b.dataset.enf;
    $("f-enf").querySelectorAll(".fchip").forEach(c => c.setAttribute("aria-pressed", String(c === b)));
    aplicar();
  });
  $("buscador").addEventListener("input", aplicar);
  aplicar();

  // La hoja o el bloque que está en pantalla se marca en el mapa: el último
  // cuyo comienzo ya pasó por el tercio superior de la ventana.
  function marcar(){
    const limite = innerHeight / 3;
    let actual = null;
    items.forEach(it => { if (!it.hidden && it.getBoundingClientRect().top <= limite) actual = it; });
    const m = $("mapa"), previo = m.querySelector("a.actual");
    const a = actual ? m.querySelector('a[data-i="' + actual.id + '"]') : null;
    if (a === previo) return;
    if (previo) previo.classList.remove("actual");
    if (!a) return;
    a.classList.add("actual");
    const r = a.getBoundingClientRect(), rm = m.getBoundingClientRect();
    if (r.top < rm.top || r.bottom > rm.bottom) m.scrollTop += r.top - rm.top - rm.height / 3;
  }
  let pendiente = false;
  addEventListener("scroll", () => {
    if (pendiente) return;
    pendiente = true;
    requestAnimationFrame(() => { pendiente = false; marcar(); });
  }, { passive: true });
})();
"""
