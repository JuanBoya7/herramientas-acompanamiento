# -*- coding: utf-8 -*-
"""
Pone al día las tres hojas anteriores al kit (la flor PERMAH, las fortalezas
del carácter y el registro de pensamientos) sin tocar sus motores.

Parte siempre de las copias de _respaldo/, les aplica los arreglos propios de
cada una y después les agrega lo que comparten todas las demás:
  - bloque de notas del profesional, plegado
  - botón "Copiar resumen" para pasar lo diligenciado a la historia clínica
  - la barra de botones al final de la hoja, no fija en pantalla
y les quita los campos de identificación, el crédito y el aviso.

    python armonizar_antiguas.py
"""
import re, shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI.parent
RESPALDO = AQUI / "_respaldo"
ARCHIVOS = ["flor-permah.html", "fortalezas-del-caracter.html", "registro-de-pensamientos.html"]

CSS = """
  /* --- añadido al armonizar con el resto de las hojas --- */
  details.notas-pro{background:linear-gradient(180deg,#faf8fd,#fff);border:1px solid var(--linea);
    border-left:5px solid #7a6a9c;border-radius:var(--radio);padding:14px 20px;margin-bottom:16px}
  details.notas-pro summary{cursor:pointer;font-size:15px;font-weight:700;color:#5b4d7a;
    list-style:none;display:flex;align-items:center;gap:10px}
  details.notas-pro summary::-webkit-details-marker{display:none}
  details.notas-pro summary::before{content:"\\270E";display:inline-flex;align-items:center;
    justify-content:center;width:27px;height:27px;border-radius:50%;background:#efeaf7;font-size:14px}
  details.notas-pro label.etiqueta{font-size:13.5px;font-weight:600;display:block;margin:14px 0 5px}
  details.notas-pro textarea{width:100%;font:inherit;font-size:14.5px;color:var(--tinta);
    border:1px solid var(--linea);border-radius:8px;padding:9px 11px;background:#fdfefe;
    min-height:70px;resize:vertical}
  details.notas-pro .ayuda{margin:6px 0 0;font-size:13.5px;color:var(--tinta-suave)}
  .barra{position:static;display:flex;gap:10px;justify-content:center;flex-wrap:wrap;
    background:var(--papel);border:1px solid var(--linea);border-radius:var(--radio);
    padding:14px 20px;margin-top:22px;box-shadow:none}
  .brindis{position:fixed;bottom:26px;left:50%;transform:translateX(-50%);
    background:var(--tinta);color:#fff;font-size:13.5px;padding:8px 16px;border-radius:8px;
    z-index:30;opacity:0;transition:opacity .2s;pointer-events:none}
  .brindis.visible{opacity:.94}
  /* la lectura condensada: el cuadro y su indicación al lado */
  .combinaciones{display:grid;gap:8px;margin-top:12px}
  .combi{display:grid;grid-template-columns:minmax(150px,34%) 1fr;
    border:1px solid var(--linea);border-radius:9px;overflow:hidden;font-size:13px}
  .combi .cual{padding:9px 13px;background:#f6f9fb;border-right:1px solid var(--linea)}
  .combi .cual b{display:block;font-size:13.5px;color:var(--tinta);margin-bottom:1px}
  .combi .cual span{color:var(--tinta-suave);font-size:12px;line-height:1.4}
  .combi .quehacer{padding:9px 13px;color:var(--tinta-suave);line-height:1.45}
  .combi.activo{border-color:var(--acento);box-shadow:0 0 0 2px var(--acento-claro)}
  .combi.activo .cual{background:var(--acento-claro)}
  .combi.activo .cual b,.combi.activo .quehacer{color:var(--tinta)}
  @media (max-width:620px){.combi{grid-template-columns:1fr}
    .combi .cual{border-right:0;border-bottom:1px solid var(--linea)}}
  @media print{ .brindis,.borrar{display:none !important} }
"""

NOTAS = """
<details class="notas-pro">
  <summary>Notas del profesional</summary>
  <div class="cuerpo">
    <label class="etiqueta">Observaciones del proceso</label>
    <textarea id="proObservaciones" placeholder="Qué se observó al trabajar la hoja: disposición, evitaciones, lo que costó, lo que se movió."></textarea>
    <label class="etiqueta">Hipótesis de trabajo</label>
    <textarea id="proHipotesis" placeholder="Cómo se lee esto dentro de la formulación del caso."></textarea>
    <label class="etiqueta">Tarea acordada</label>
    <textarea id="proTarea" placeholder="Qué se acordó practicar entre sesiones, con qué registro."></textarea>
    <label class="etiqueta">Para la próxima sesión</label>
    <textarea id="proProxima" placeholder="Qué revisar, qué habilidad sigue, qué quedó pendiente."></textarea>
    <p class="ayuda" style="margin-top:12px">
      <label style="cursor:pointer"><input type="checkbox" id="proNoImprimir" style="width:auto;margin-right:7px">
      No incluir estas notas al imprimir</label>
    </p>
  </div>
</details>
"""


def armonizar(d, kit_js):
    # 1. Fuera los campos de identificación: son recursos de sesión. Sus ids
    #    quedan ocultos porque el guardar() original los referencia por nombre.
    bloque = re.search(r'\n?\s*<div class="campos-id">.*?</div>\s*(?=\n)', d, flags=re.S)
    if bloque:
        ids = re.findall(r'<input[^>]*id="([^"]+)"', bloque.group(0))
        ocultos = "".join('<input type="hidden" id="%s">' % i for i in ids)
        d = d.replace(bloque.group(0), "\n  " + ocultos + "\n", 1)

    # 2. el crédito se queda solo con la procedencia del material, como la
    #    línea de fuente del resto de las hojas; el aviso se va entero
    def procedencia(m):
        txt = m.group(1)
        for sobra in ["&middot; Ruta de Atención Clínica, FUAA",
                      "Ruta de Atención Clínica &middot; Espacio de consejería &middot; FUAA",
                      "&middot; Ruta de Atención Clínica", "&middot; FUAA"]:
            txt = txt.replace(sobra, "")
        txt = re.sub(r"\s+", " ", txt).strip(" ·\n")
        return '<p class="fuente">%s</p>' % txt if txt else ""
    d = re.sub(r'<p class="credito">(.*?)</p>', procedencia, d, count=1, flags=re.S)
    d = re.sub(r'\n?\s*<p class="aviso">.*?</p>', "", d, count=1, flags=re.S)

    # 3. la barra deja de estar fija y entra al final de la hoja, con el
    #    botón de copiar resumen delante de los demás
    barra = re.search(r'<div class="barra">.*?</div>\s*', d, flags=re.S)
    if barra:
        texto = barra.group(0)
        d = d.replace(texto, "", 1)
        texto = texto.replace('<div class="barra">',
                              '<div class="barra">\n  '
                              '<button onclick="Kit.copiar()">Copiar resumen</button>', 1)
        # justo antes del cierre de la envoltura
        d = re.sub(r'\n</div>\s*\n\s*<script>',
                   "\n" + NOTAS.strip() + "\n\n" + texto.rstrip() +
                   '\n</div>\n<div class="brindis" id="brindis"></div>\n\n<script>',
                   d, count=1)

    if 'id="brindis"' not in d:
        d = d.replace("<script>", '<div class="brindis" id="brindis"></div>\n<script>', 1)

    # 4. el CSS y el kit
    d = d.replace("</style>", CSS + "</style>", 1)
    d = d.replace("</body>", "<script>\n" + kit_js + "\nKit.soloModo();\n</script>\n</body>", 1)
    return d


# ---------------------------------------------------------------- arreglos
def limpiar_lenguaje(d):
    """Fuera las referencias a la vida universitaria y a la institución."""
    cambios = [
        ("&middot; Ruta de Atención Clínica, FUAA", ""),
        ("Ruta de Atención Clínica &middot; Espacio de consejería &middot; FUAA", ""),
        ("¿Para qué estás estudiando esto? ¿Sigue siendo tuya esa respuesta?",
         "¿Para qué estás haciendo lo que haces? ¿Sigue siendo tuya esa respuesta?"),
        ("¿Cuánto te está costando, en horas de sueño, sostener las notas que tienes?",
         "¿Cuánto te está costando, en horas de sueño, sostener el ritmo que llevas?"),
        ("Es el perfil que antecede a la deserción y a los cambios de programa, y a menudo se disfraza de pereza o desmotivación. Frecuente en quienes eligieron carrera por otros.",
         "Es el perfil que antecede a dejarlo todo o a cambiar de rumbo, y a menudo se disfraza de pereza o desmotivación. Frecuente en quienes eligieron su camino para complacer a otros."),
        ("Significado. Vale más una conversación vocacional honesta que un plan de estudio o de hábitos.",
         "Significado. Vale más una conversación honesta sobre el rumbo que un plan de hábitos."),
        ("Nadie a su alrededor lo nota porque las notas están bien.",
         "Nadie a su alrededor lo nota porque por fuera todo sigue funcionando."),
        ("Estudiantes que procesan el malestar pensándolo.",
         "Procesan el malestar pensándolo."),
        ("Frecuente en quienes trabajan y estudian, o sostienen a su familia.",
         "Frecuente en quienes sostienen dos frentes a la vez, o sostienen a su familia."),
        ("Representantes de curso, líderes de trabajo en grupo, los que alzan la voz por otros.",
         "Los que alzan la voz por otros y terminan liderando cualquier grupo en el que estén."),
        ("Estudiantes ordenados, cautelosos y poco expresivos.",
         "Personas ordenadas, cautelosas y poco expresivas."),
        ("Ej. 'Perdí la materia, no sirvo para esta carrera.'",
         "Ej. 'Me salió mal, no sirvo para esto.'"),
        ("¿Qué has logrado este semestre, aunque te parezca poco?",
         "¿Qué has sacado adelante últimamente, aunque te parezca poco?"),
        ("o al inicio en estudiantes que consultan por una preocupación puntual y no por malestar global.",
         "o al inicio en quien consulta por una preocupación puntual y no por malestar global."),
        ("¿Qué estás haciendo hoy que quisieras seguir haciendo cuando lleguen los parciales?",
         "¿Qué estás haciendo hoy que quisieras seguir haciendo cuando vengan las semanas difíciles?"),
        ("El estudiante que cumple con todo y lo paga con el cuerpo",
         "Cumple con todo y lo paga con el cuerpo"),
        ("Es el perfil clásico previo al burnout académico.",
         "Es el perfil clásico previo al agotamiento."),
        ("Es muy común en estudiantes que migraron de ciudad para estudiar, y en quienes usan la productividad para no sentir el aislamiento.",
         "Muy común en quien cambió de ciudad, y en quien usa la productividad para no sentir el aislamiento."),
        ("Aparece en estudiantes muy vocacionados, cuidadores familiares y quienes trabajan y estudian a la vez.",
         "Aparece en gente muy vocacionada, en cuidadores familiares y en quienes sostienen dos frentes a la vez."),
        ("puede ser una etapa sana de la vida universitaria, o una evitación bien montada",
         "puede ser una etapa sana de la vida, o una evitación bien montada"),
        ("Frecuente tras una pérdida, una ruptura o un semestre perdido",
         "Frecuente tras una pérdida, una ruptura o una temporada en blanco"),
        ("Aparece a menudo en estudiantes con vida espiritual o comunitaria activa.",
         "Aparece a menudo en quienes tienen una vida espiritual o comunitaria activa."),
        ("¿Qué esperas de este semestre, en concreto?",
         "¿Qué esperas de los próximos meses, en concreto?"),
        ('<label>Programa / semestre <input type="text" id="programa"></label>',
         '<label>Momento <input type="text" id="programa" placeholder="Ej. Sesión 2"></label>'),
        ("Ej. Ayer 4:00 p.m., salí del parcial de estadística. Comparé respuestas con dos compañeros y las mías no coincidían.",
         "Ej. Ayer 4:00 p.m., salí de una reunión. Repasé lo que dije y me pareció que había quedado mal."),
        ("Ej. 'Me fue mal en un parcial de una materia difícil. Eso me preocupa y tiene solución: puedo revisar con el monitor y todavía quedan dos notas.'",
         "Ej. 'Salió peor de lo que esperaba. Eso me preocupa y tiene solución: puedo hablarlo y todavía hay margen.'"),
        ("Ej. 'El martes le escribo al monitor para pedir asesoría antes del segundo parcial.'",
         "Ej. 'El martes le escribo para pedir una reunión corta.'"),
    ]
    for viejo, nuevo in cambios:
        d = d.replace(viejo, nuevo)
    return d


def arreglar_flor(d):
    """La lectura larga se cambia por las combinaciones con su indicación al lado."""
    d = d.replace("""<section class="bloque perfil" id="perfil">
  <div class="campo" style="margin-bottom:6px">
    <div class="etq">Lectura del perfil</div>
  </div>
  <div class="nombre" id="pNombre">—</div>
  <p class="metafora" id="pMetafora"></p>
  <div class="campo"><div class="etq">Qué suele verse así en consulta</div><p id="pConsulta"></p></div>
  <div class="campo"><div class="etq">Por dónde empezar</div><p id="pFoco"></p></div>
  <div class="pregunta" id="pPregunta"></div>
  <div id="pBandera"></div>

  <details class="catalogo">
    <summary>Ver las combinaciones posibles del PERMAH</summary>
    <div class="lista-perfiles" id="catalogo"></div>
  </details>
</section>""",
"""<section class="bloque perfil" id="perfil">
  <div class="campo" style="margin-bottom:6px">
    <div class="etq">Combinaciones del PERMAH</div>
  </div>
  <div class="nombre" id="pNombre">—</div>
  <p class="metafora" id="pMetafora"></p>
  <div class="combinaciones" id="combinaciones"></div>
  <div id="pBandera"></div>
</section>""")

    d = d.replace("""  $("pNombre").textContent=p.nombre;
  $("pMetafora").textContent=p.metafora;
  $("pConsulta").textContent=p.consulta;
  $("pFoco").textContent=rellenar(p.foco);
  $("pPregunta").textContent=rellenar(p.pregunta);""",
"""  $("pNombre").textContent=p.nombre;
  $("pMetafora").textContent=p.metafora;""")

    d = d.replace("""  document.querySelectorAll(".mini").forEach(m=>
    m.classList.toggle("activo", m.dataset.k===p.clave));
}""",
"""  // la combinación vigente queda encendida entre todas las posibles, con su
  // indicación al lado derecho: se ve de un vistazo dónde cae esta persona
  document.querySelectorAll(".combi").forEach(m=>{
    const suya = m.dataset.k===p.clave;
    m.classList.toggle("activo", suya);
    if(suya) m.querySelector(".quehacer").textContent = rellenar(p.foco);
  });
}""")

    d = d.replace("""$("catalogo").innerHTML = PERFILES.map(p=>
  `<div class="mini" data-k="${p.clave}"><b>${p.nombre}</b><span>${p.resumen}</span></div>`).join("");""",
"""$("combinaciones").innerHTML = PERFILES.map(p=>
  `<div class="combi" data-k="${p.clave}">
     <div class="cual"><b>${p.nombre}</b><span>${p.resumen}</span></div>
     <div class="quehacer">${p.foco.replace("{fuerte}","el área más alta").replace("{debil}","la más baja")}</div>
   </div>`).join("");""")
    return d


def arreglar_fortalezas(d):
    """El perfil se revela solo al completar, y las casillas se pintan siempre."""
    # El selector de 3 o 5 casillas vivía dentro del bloque de identificación.
    # Al quitar ese bloque, $("b3") quedaba en nada, la excepción cortaba el
    # arranque justo antes de pintar las casillas y la hoja salía sin ranuras.
    # Se muda al panel de las casillas, que es donde tiene sentido.
    selector = ('    <div class="cuantas">Casillas\n'
                '      <button id="b3" onclick="cambiarCupo(3)">3</button>\n'
                '      <button id="b5" onclick="cambiarCupo(5)">5</button>\n'
                '    </div>\n')
    assert selector in d, "no se encontró el selector de casillas"
    d = d.replace(selector, "")
    d = d.replace("    <h2>Mis fortalezas</h2>\n",
                  "    <h2>Mis fortalezas</h2>\n" + selector)

    # fuera el botón de revelar
    d = d.replace('  <button class="oro" id="btnRevelar" onclick="revelar()" disabled>Revelar el perfil</button>\n', "")
    d = d.replace("""      Completa las casillas y conversa cada elección.<br>
      El perfil se revela al final, con el botón de abajo.""",
"""      Completa las casillas y el perfil aparece solo.""")
    d = d.replace("""     El perfil se revela al final, con el botón de abajo.</div>`;""",
"""     El perfil aparece solo al completarlas.</div>`;""")

    # el perfil se revela solo; sin botón que habilitar
    d = d.replace("""  $("pista").textContent = faltan>0
    ? `Arrastra una fortaleza hasta una casilla. En el celular, tócala. Faltan ${faltan}.`
    : "Listo. Cuando hayan conversado cada una, revela el perfil abajo.";
  $("btnRevelar").disabled = faltan>0;
  if(faltan>0) ocultarPerfil();
  guardar();""",
"""  $("pista").textContent = faltan>0
    ? `Arrastra una fortaleza hasta una casilla. En el celular, tócala. Faltan ${faltan}.`
    : "Listo. Ahí abajo está el perfil.";
  // el perfil aparece solo al completar las casillas: no hace falta botón
  if(faltan>0) ocultarPerfil(); else revelar(true);
  guardar();""")

    # revelar() ya no debe arrastrar la pantalla si se llama solo
    d = d.replace("""  $("perfil").scrollIntoView({behavior:"smooth",block:"start"});""",
"""  if(!automatico) $("perfil").scrollIntoView({behavior:"smooth",block:"start"});""")
    d = d.replace("function revelar(){", "function revelar(automatico){")

    # el arranque, a prueba de fallos: si algo de lo guardado falla, las
    # casillas se pintan igual. Antes una excepción dejaba la hoja en blanco.
    d = d.replace("""CAMPOS.forEach(c=>$(c).addEventListener("input",guardar));
cargar();
if(!$("fecha").value) $("fecha").value=new Date().toLocaleDateString("es-CO");
$("b3").classList.toggle("on",cupo===3); $("b5").classList.toggle("on",cupo===5);
pintarCasillas();""",
"""try{
  CAMPOS.forEach(c=>{ const e=$(c); if(e) e.addEventListener("input",guardar); });
  cargar();
  if($("fecha") && !$("fecha").value) $("fecha").value=new Date().toLocaleDateString("es-CO");
}catch(e){}
if(cupo!==3 && cupo!==5) cupo = 3;
$("b3").classList.toggle("on",cupo===3); $("b5").classList.toggle("on",cupo===5);
pintarCasillas();""")
    return d


ARREGLOS = {
    "flor-permah.html": arreglar_flor,
    "fortalezas-del-caracter.html": arreglar_fortalezas,
}


def main():
    kit_js = (AQUI / "kit.js").read_text(encoding="utf-8")
    for nombre in ARCHIVOS:
        origen = RESPALDO / nombre
        if not origen.exists():
            print(f"  falta el respaldo de {nombre}")
            continue
        d = origen.read_text(encoding="utf-8")
        d = limpiar_lenguaje(d)
        if nombre in ARREGLOS:
            d = ARREGLOS[nombre](d)
        d = armonizar(d, kit_js)
        (DESTINO / nombre).write_text(d, encoding="utf-8")
        print(f"  {nombre:38s} rehecha desde el respaldo")


if __name__ == "__main__":
    main()
