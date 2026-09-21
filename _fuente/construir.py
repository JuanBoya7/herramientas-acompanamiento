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
import sys, re
from pathlib import Path

import guia
import rieles

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
    ("Metáforas vivas", "Recursos experienciales, no clasificadores: la metáfora se juega y se "
                        "atraviesa dentro de la hoja, y el cambio ocurre al usarla."),
    ("Psicología positiva", "El punto de partida: cómo está la vida hoy y con qué cuenta la persona."),
    ("ACT", "Terapia de aceptación y compromiso: dejar de pelear con lo interno y moverse hacia lo que importa."),
    ("DBT", "Habilidades de terapia dialéctico-conductual, en módulos que se pueden trabajar sueltos."),
    ("Cognitivo-conductual", "Técnicas clásicas de evaluación, reestructuración, exposición y activación."),
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
    destino.write_text(salida, encoding="utf-8")
    return meta, destino


TARJETA = """      <a class="ficha" href="{archivo}" data-item data-enf="{enfoque}" data-titulo="{titulo}" data-href="{archivo}">
        <span class="etq">{etiqueta}</span>
        <b>{titulo}</b>
        <span class="dice">{resumen}</span>
        <span class="ref">{fuente}</span>
      </a>"""


def construir_indice(fichas, kit_css):
    bloques = []
    for enfoque, descripcion in ORDEN_ENFOQUES:
        propias = [f for f in fichas if f["enfoque"] == enfoque]
        if not propias:
            continue
        tarjetas = "\n".join(
            TARJETA.format(
                archivo=f["archivo"],
                enfoque=f["enfoque"],
                etiqueta=f.get("etiqueta", f["enfoque"]),
                titulo=f["titulo"],
                resumen=f["resumen"],
                fuente=f["fuente"],
            )
            for f in propias
        )
        bloques.append(
            f"""  <section class="bloque" data-grupo="{enfoque}">
    <h2>{enfoque}</h2>
    <p class="ayuda">{descripcion}</p>
    <div class="rejilla">
{tarjetas}
    </div>
  </section>"""
        )

    css_extra = """
  .rejilla{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));
    gap:11px;margin-top:15px}
  a.ficha{display:block;border:1px solid var(--linea);border-radius:10px;padding:14px 16px;
    text-decoration:none;color:inherit;background:#fdfefe;transition:border-color .13s,
    transform .13s,box-shadow .13s}
  a.ficha:hover{border-color:var(--acento);transform:translateY(-2px);
    box-shadow:0 3px 12px rgba(47,111,143,.12)}
  a.ficha .etq{display:inline-block;font-size:10.5px;text-transform:uppercase;
    letter-spacing:.8px;font-weight:700;color:var(--acento);background:var(--acento-claro);
    border-radius:999px;padding:2px 9px;margin-bottom:8px}
  a.ficha b{display:block;font-size:16.5px;margin-bottom:5px;letter-spacing:-.2px}
  a.ficha .dice{display:block;font-size:13.5px;color:var(--tinta-suave);line-height:1.45}
  a.ficha .ref{display:block;font-size:11.5px;color:var(--tinta-suave);font-style:italic;
    margin-top:9px;padding-top:8px;border-top:1px dashed var(--linea)}
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
    conviene tener cuidado. Incluye los encadenamientos que suelen funcionar.</span>
  </span>
  <span class="flecha">&rarr;</span>
</a>
</div>

{rieles.controles("Buscar una hoja por nombre, técnica o uso…")}

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

    fichas = list(YA_HECHAS)
    hechas = 0
    for ruta in sorted(PARTES.glob("*.parte")):
        meta, destino = construir(ruta, plantilla, kit_css, kit_js)
        fichas.append(meta)
        hechas += 1
        if not filtro or filtro in ruta.name:
            print(f"  {destino.name}  ({destino.stat().st_size // 1024} KB)")

    orden = {n: i for i, (n, _) in enumerate(ORDEN_ENFOQUES)}
    fichas.sort(key=lambda f: (orden.get(f["enfoque"], 99), f.get("orden", "99")))

    indice = DESTINO / "index.html"
    indice.write_text(construir_indice(fichas, kit_css), encoding="utf-8")

    # La guía de uso se rehace con el resto: comparte los estilos del kit.
    en_guia = guia.construir(kit_css)

    print(f"\n{hechas} herramientas construidas + index.html con {len(fichas)} fichas"
          f" + guia.html con {en_guia}.")


if __name__ == "__main__":
    main()
