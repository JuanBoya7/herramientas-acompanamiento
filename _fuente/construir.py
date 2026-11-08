# -*- coding: utf-8 -*-
"""
Ensambla las herramientas de la Ruta de Atención Clínica.

Cada archivo de partes/*.parte trae su metadata, su CSS, su HTML y su JS.
El script los mete dentro de plantilla.html junto con kit.css y kit.js, y
escribe un HTML autónomo (sin dependencias, funciona con doble clic) en la
carpeta Herramientas. Al final genera index.html con todas las fichas.

    python construir.py            -> construye todo
    python construir.py brujula    -> solo las partes que contengan "brujula"
"""
import html as _h
import sys, re
from pathlib import Path

import guia
import rieles
import sesion

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI.parent
PARTES = AQUI / "partes"

# Herramientas que ya existían y se listan en el índice sin reconstruirse.
YA_HECHAS = [
    {
        "archivo": "flor-permah.html", "titulo": "Mi flor PERMAH", "orden": "01",
        "enfoque": "Psicología positiva", "etiqueta": "Bienestar",
        "resumen": "Seis áreas del bienestar dibujadas como una flor que se abre o se marchita. "
                   "Devuelve un perfil con doce lecturas posibles y por dónde empezar.",
        "fuente": "Modelo PERMAH (Seligman) · taller Flourish",
    },
    {
        "archivo": "fortalezas-del-caracter.html", "titulo": "Mis fortalezas del carácter",
        "orden": "02", "enfoque": "Psicología positiva", "etiqueta": "Recursos",
        "resumen": "Las 24 fortalezas VIA en un mostrador del que se eligen tres o cinco. "
                   "Al revelarlas nombra la virtud dominante y qué hacer con ella.",
        "fuente": "Clasificación VIA de fortalezas (Peterson y Seligman)",
    },
    {
        "archivo": "registro-de-pensamientos.html", "titulo": "Registro de pensamientos",
        "orden": "01", "enfoque": "Cognitivo-conductual", "etiqueta": "Reestructuración",
        "resumen": "El registro clásico en siete pasos: situación, emoción, pensamiento caliente, "
                   "trampas, evidencia a favor y en contra, alternativa y recalificación.",
        "fuente": "Terapia Cognitiva (Beck) · Ruiz, Díaz y Villalobos, cap. 8",
    },
]

ORDEN_ENFOQUES = [
    ("ACT", "Terapia de aceptación y compromiso, terapia centrada en la compasión funcional y FAP: veintiocho herramientas —metáforas vivas, ejercicios experienciales y mapas de formulación— organizadas alrededor de los seis procesos del hexaflex."),
    ("Cognitivo-conductual", "Recorrido clínico desde la formulación funcional, el protocolo unificado y el mapa de modos hasta los experimentos conductuales, la exposición interoceptiva y en vivo, la activación y la autorregulación."),
    ("DBT", "Habilidades de terapia dialéctico-conductual y apertura radical (RO-DBT) —atención plena, aceptación radical, tolerancia al malestar, regulación emocional ABC PLEASE, efectividad interpersonal y autoinvestigación— junto con análisis en cadena y tarjeta diaria."),
    ("Compasión y mindfulness", "Prácticas breves para equilibrar los tres sistemas de regulación emocional, activar el sistema de calma y responder al crítico interno desde el yo compasivo."),
    ("Vínculos y pareja", "Terapia focalizada en las emociones (EFT) y terapia conductual integrativa de pareja (IBCT): desescalar el ciclo negativo persecución-retirada, escuchar el apego bajo el agua y cuidar el vínculo."),
    ("Psicología positiva", "El punto de partida, el sentido y los recursos disponibles: bienestar PERMAH, fortalezas del carácter, afecto positivo, las cuatro fuentes de sentido y el proceso REACH del perdón."),
    ("Crisis y consumo", "Para los momentos de riesgo y ambivalencia: el plan de seguridad ante la crisis suicida, el manejo del impulso de consumo y la exploración motivacional del cambio."),
]


def leer_partes(ruta):
    """Divide un .parte en sus secciones @@meta, @@css, @@html, @@js."""
    texto = ruta.read_text(encoding="utf-8")
    trozos, actual, buffer = {}, None, []
    for linea in texto.splitlines():
        marca = re.match(r"^@@(meta|css|html|js)\s*$", linea)
        if marca:
            if actual:
                trozos[actual] = "\n".join(buffer).strip("\n")
            actual, buffer = marca.group(1), []
        elif actual:
            buffer.append(linea)
    if actual:
        trozos[actual] = "\n".join(buffer).strip("\n")

    meta = {}
    for linea in trozos.get("meta", "").splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            meta[clave.strip()] = valor.strip()
    return meta, trozos


def construir(ruta, plantilla, kit_css, kit_js):
    meta, trozos = leer_partes(ruta)
    faltan = [c for c in ("archivo", "titulo", "sub", "fuente", "enfoque", "resumen") if c not in meta]
    if faltan:
        raise SystemExit(f"{ruta.name}: faltan claves en @@meta -> {', '.join(faltan)}")

    # La mayoría son recursos de sesión y no llevan datos de identificación.
    # Solo las que existen para dejar registro declaran "identificacion: si".
    if meta.get("identificacion", "").lower() in ("si", "sí", "true", "1"):
        identificacion = """  <div class="campos-id">
    <label>Nombre o iniciales <input type="text" id="nombre" placeholder="Opcional"></label>
    <label>Fecha <input type="text" id="fecha"></label>
    <label>{campo3} <input type="text" id="sesion" placeholder="{campo3ph}"></label>
    <label class="solo-clinica">Profesional <input type="text" id="profesional" placeholder="Quien acompaña"></label>
  </div>""".format(campo3=meta.get("campo3", "Sesión"),
                   campo3ph=meta.get("campo3ph", "Ej. Sesión 3"))
    else:
        identificacion = ""

    # Las hojas expositivas se marcan con "lamina: si". Ya no nacen en
    # lámina: se marcan como laminables y el kit pone el botón que la
    # enciende. En consulta uno a uno la letra grande estorbaba.
    laminable = meta.get("lamina", "").lower() in ("si", "sí", "true", "1")
    lamina = ' data-laminable="1"' if laminable else ""
    boton_lamina = ("  <button class='botonLamina' onclick='Kit.lamina()'>Modo lámina</button>" + "\n"
                    if laminable else "")

    salida = plantilla
    for clave, valor in [
        ("{{LAMINA}}", lamina),
        ("{{BOTON_LAMINA}}", boton_lamina),
        ("{{IDENTIFICACION}}", identificacion),
        ("{{KIT_CSS}}", kit_css),
        ("{{KIT_JS}}", kit_js),
        ("{{CSS_PROPIO}}", trozos.get("css", "")),
        ("{{CONTENIDO}}", trozos.get("html", "")),
        ("{{JS_PROPIO}}", trozos.get("js", "")),
        ("{{TITULO}}", meta["titulo"]),
        ("{{SUB}}", meta["sub"]),
        ("{{FUENTE}}", meta["fuente"]),
        ("{{CAMPO3}}", meta.get("campo3", "Sesión")),
        ("{{CAMPO3PH}}", meta.get("campo3ph", "Ej. Sesión 3")),
    ]:
        salida = salida.replace(clave, valor)

    quedan = re.findall(r"\{\{[A-Z_0-9]+\}\}", salida)
    if quedan:
        raise SystemExit(f"{ruta.name}: quedaron marcadores sin reemplazar -> {set(quedan)}")

    destino = DESTINO / meta["archivo"]
    destino.write_text(sesion.aplicar(salida, meta["archivo"]), encoding="utf-8")
    meta["resumen"] = sesion.descripcion(meta["archivo"])
    return meta, destino


def _tarjeta_indice(f):
    info = rieles.info_organizacion(f["archivo"])
    atrs_hx = ""
    if info["proc"]:
        atrs_hx = (
            f' data-proc="{info["proc"]}"'
            f' data-proc-sec="{",".join(info["sec"])}"'
            f' data-estilo="{info["estilo"]}"'
        )
    insignias = rieles.insignias_hexaflex(f["archivo"])
    return f"""        <a class="ficha" href="{f['archivo']}" data-item data-enf="{f['enfoque']}" data-titulo="{_h.escape(f['titulo'])}" data-href="{f['archivo']}"{atrs_hx}>
          <span class="etq">{_h.escape(f.get('etiqueta', f['enfoque']))}</span>
          <b>{_h.escape(f['titulo'])}</b>
          <span class="dice">{_h.escape(f['resumen'])}</span>
          {insignias}
          <span class="ref">{_h.escape(f['fuente'])}</span>
        </a>"""


def construir_indice(fichas, kit_css):
    bloques = []
    for enfoque, descripcion in ORDEN_ENFOQUES:
        propias = [f for f in fichas if f["enfoque"] == enfoque]
        if not propias:
            continue
        subs = rieles.SUBGRUPOS.get(enfoque, [])
        panel_hx = ("\n" + rieles.bloque_hexaflex()) if enfoque == "ACT" else ""

        if len(subs) > 1:
            bloques_sub = []
            for sub_id, sub_titulo, sub_desc, sub_color, sub_est in subs:
                de_sub = [f for f in propias if rieles.info_organizacion(f["archivo"])["subgrupo"] == sub_id]
                if not de_sub:
                    continue
                tarjetas = "\n".join(_tarjeta_indice(f) for f in de_sub)
                corto = rieles.PROC_POR_ID[sub_id]["corto"] if sub_id in rieles.PROC_POR_ID else sub_titulo.split("·")[-1].strip()
                atr_proc = f' data-subproc="{sub_id}"' if enfoque == "ACT" else ""
                aviso_vinc = (
                    '<p class="sub-vinc-aviso" hidden>También vinculadas con el proceso elegido desde este vértice del hexaflex</p>'
                    if enfoque == "ACT" else ""
                )
                bloques_sub.append(f"""      <div class="subgrupo" data-subgrupo="{sub_id}" data-subcorto="{_h.escape(corto)}"{atr_proc} style="--sub-c:{sub_color}">
        <div class="subgrupo-cab">
          <h3><span class="sub-punto"></span>{_h.escape(sub_titulo)}</h3>
          <span class="sub-est">{_h.escape(sub_est)}</span>
        </div>
        <p class="sub-desc">{_h.escape(sub_desc)}</p>
        {aviso_vinc}
        <div class="rejilla">
{tarjetas}
        </div>
      </div>""")
            interior = f'    <div class="subgrupos">\n{chr(10).join(bloques_sub)}\n    </div>'
        else:
            tarjetas = "\n".join(_tarjeta_indice(f) for f in propias)
            interior = f'    <div class="rejilla">\n{tarjetas}\n    </div>'

        bloques.append(
            f"""  <section class="bloque" data-grupo="{enfoque}">
    <h2>{enfoque}</h2>
    <p class="ayuda">{descripcion}</p>{panel_hx}
{interior}
  </section>"""
        )

    css_extra = """
  .rejilla{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,280px),1fr));
    gap:13px;margin-top:10px}
  a.ficha{display:flex;flex-direction:column;min-width:0;overflow-wrap:break-word;border:1px solid var(--linea);border-radius:10px;padding:15px 17px;
    text-decoration:none;color:inherit;background:#fdfefe;transition:border-color .13s,
    transform .13s,box-shadow .13s}
  a.ficha:hover{border-color:var(--acento);transform:translateY(-2px);
    box-shadow:0 3px 12px rgba(47,111,143,.12)}
  a.ficha.hx-item-vinculado{border-style:dashed;background:#fafcfe}
  a.ficha .etq{align-self:flex-start;display:inline-block;font-size:10.5px;text-transform:uppercase;
    letter-spacing:.8px;font-weight:700;color:var(--acento);background:var(--acento-claro);
    border-radius:999px;padding:3px 10px;margin-bottom:8px;max-width:100%;white-space:normal;overflow-wrap:anywhere;line-height:1.3}
  a.ficha b{display:block;font-size:16.5px;line-height:1.3;margin-bottom:6px;letter-spacing:-.2px;overflow-wrap:break-word}
  a.ficha .dice{display:block;font-size:13.5px;color:var(--tinta-suave);line-height:1.45}
  a.ficha .ref{display:block;font-size:11.5px;color:var(--tinta-suave);font-style:italic;
    margin-top:auto;padding-top:8px;border-top:1px dashed var(--linea)}
  a.ficha .hx-tags{margin-bottom:8px}
  .comoUsar{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;
    margin-top:14px}
  .comoUsar div{font-size:13.5px;color:var(--tinta-suave)}
  .comoUsar b{display:block;color:var(--tinta);font-size:14px;margin-bottom:3px}
  a.aGuia{display:flex;align-items:center;gap:16px;background:var(--papel);
    border:1px solid var(--acento);border-left-width:5px;border-radius:var(--radio);
    padding:16px 22px;margin-bottom:16px;text-decoration:none;color:inherit;
    transition:box-shadow .13s,transform .13s}
  a.aGuia:hover{box-shadow:0 3px 12px rgba(47,111,143,.14);transform:translateY(-1px)}
  a.aGuia .quees{flex:1}
  a.aGuia b{display:block;font-size:17px;letter-spacing:-.2px;margin-bottom:2px}
  a.aGuia span{display:block;font-size:13.5px;color:var(--tinta-suave);line-height:1.45}
  a.aGuia .flecha{flex:0 0 auto;font-size:20px;color:var(--acento)}
"""

    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Herramientas de acompañamiento</title>
<style>
{kit_css}
{css_extra}
{rieles.CSS}
</style>
</head>
<body data-extra="&lt;a class=&quot;extra&quot; href=&quot;guia.html&quot;&gt;Guía rápida de uso &amp;rarr;&lt;/a&gt;">
<div class="envoltura con-rieles">

<div class="cab">
<header class="tapa">
  <h1>Herramientas de acompañamiento</h1>
  <p class="sub">{len(fichas)} hojas de trabajo interactivas para el espacio clínico, cada una en
  un solo archivo que funciona sin internet. Todo se elige, se calibra o se arrastra; cada hoja
  lleva plegado un bloque de notas del profesional y un botón para pasar lo trabajado a la
  historia clínica.</p>
</header>

<a class="aGuia" href="guia.html">
  <span class="quees">
    <b>Guía rápida de uso</b>
    <span>Para qué sirve cada hoja, en qué casos rinde, con qué va antes o después, y dónde
    conviene tener cuidado. Incluye el mapa del hexaflex y los encadenamientos que suelen funcionar.</span>
  </span>
  <span class="flecha">&rarr;</span>
</a>

<a class="aGuia" href="lecturas-act.html" style="border-color:#c26a4e">
  <span class="quees">
    <b>Lecturas ACT para leer y reflexionar</b>
    <span>Tablero alterno con 48 metáforas, ejercicios y hojas de reflexión ilustradas, organizadas por el
    hexaflex. Cada lectura trae preguntas para conversar y se envía como PDF por WhatsApp o por correo.</span>
  </span>
  <span class="flecha" style="color:#c26a4e">&rarr;</span>
</a>
</div>

{rieles.controles("Buscar una hoja por nombre, proceso o técnica…")}

<main class="centro">
{chr(10).join(bloques)}

  <div class="sin-resultados" id="sin-resultados" hidden>Ninguna hoja coincide con el filtro y la búsqueda.</div>

  <section class="bloque">
    <h2>Cómo se usan</h2>
    <div class="comoUsar">
      <div><b>Se abren con doble clic</b>No necesitan instalación, servidor ni conexión. Se pueden
      copiar a una memoria o enviar por correo y siguen funcionando.</div>
      <div><b>Guardan en el equipo</b>Lo que se trabaja queda en el navegador de esa máquina, no
      viaja a ningún servidor. Si se usa un computador compartido, conviene cerrar con
      <i>Empezar de nuevo</i>.</div>
      <div><b>Se imprimen</b>El botón <i>Imprimir / Guardar PDF</i> deja una hoja limpia, sin
      botones ni opciones no marcadas, para entregar o archivar.</div>
      <div><b>Pasan a la historia clínica</b>El botón <i>Copiar resumen</i> arma un texto plano con
      lo diligenciado y las notas del profesional, listo para pegar.</div>
    </div>
  </section>
</main>

{rieles.MAPA}

</div>
<script>{rieles.JS}</script>
</body>
</html>
"""


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else ""
    plantilla = (AQUI / "plantilla.html").read_text(encoding="utf-8")
    kit_css = (AQUI / "kit.css").read_text(encoding="utf-8")
    kit_js = (AQUI / "kit.js").read_text(encoding="utf-8")

    fichas = [dict(f, resumen=sesion.descripcion(f['archivo'])) for f in YA_HECHAS]
    hechas = 0
    for ruta in sorted(PARTES.glob("*.parte")):
        meta, destino = construir(ruta, plantilla, kit_css, kit_js)
        fichas.append(meta)
        hechas += 1
        if not filtro or filtro in ruta.name:
            print(f"  {destino.name}  ({destino.stat().st_size // 1024} KB)")

    orden_enf = {n: i for i, (n, _) in enumerate(ORDEN_ENFOQUES)}
    fichas.sort(key=lambda f: (
        orden_enf.get(f["enfoque"], 99),
        rieles.info_organizacion(f["archivo"])["orden_org"],
    ))

    # Cada herramienta lleva el índice de todas las hojas.
    for f in fichas:
        ruta = DESTINO / f["archivo"]
        if ruta.exists():
            rieles.inyectar_indice(ruta, fichas)

    indice = DESTINO / "index.html"
    indice.write_text(construir_indice(fichas, kit_css), encoding="utf-8")

    # La guía de uso se rehace con el resto: comparte los estilos del kit.
    en_guia = guia.construir(kit_css)
    assert len(fichas) == len(sesion.REVISION), 'Falta revisar una herramienta'
    sesion.documentar()

    print(f"\n{hechas} herramientas construidas + index.html con {len(fichas)} fichas"
          f" + guia.html con {en_guia}.")


if __name__ == "__main__":
    main()
