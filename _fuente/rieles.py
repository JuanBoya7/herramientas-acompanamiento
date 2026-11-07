# -*- coding: utf-8 -*-
"""
Columnas laterales, organización clínica por subgrupos y mapa interactivo del
hexaflex para el índice (`index.html`), la guía de uso (`guia.html`) y el
panel lateral de cada herramienta.
"""
import html as _h
import json as _json

ENFOQUES = [
    "ACT",
    "Cognitivo-conductual",
    "DBT",
    "Compasión y mindfulness",
    "Psicología positiva",
    "Crisis y consumo",
]

ESTILOS_HEX = {
    "abierto": {
        "nombre": "Estilo abierto",
        "corto": "Abierto",
        "color": "#c26a4e",
        "procesos": ["aceptacion", "defusion"],
        "desc": "Aceptación y defusión: soltar la lucha con el malestar y desliteralizar los pensamientos.",
    },
    "centrado": {
        "nombre": "Estilo centrado",
        "corto": "Centrado",
        "color": "#3f83a6",
        "procesos": ["presente", "yo"],
        "desc": "Momento presente y yo como contexto: notar aquí y ahora desde una perspectiva que contiene lo que aparece.",
    },
    "comprometido": {
        "nombre": "Estilo comprometido",
        "corto": "Comprometido",
        "color": "#3f9b86",
        "procesos": ["valores", "accion"],
        "desc": "Valores y acción comprometida: elegir direcciones propias y sostener pasos concretos.",
    },
    "centro": {
        "nombre": "Centro del hexaflex",
        "corto": "Transversal",
        "color": "#2f6f8f",
        "procesos": ["formulacion"],
        "desc": "Flexibilidad psicológica y formulación: visión conjunta de los seis procesos y punto de vista.",
    },
}

# Los 6 vértices del hexaflex + el nodo central de formulación y flexibilidad.
# Las coordenadas (cx, cy) recrean la disposición clásica de Hayes et al. (2012)
# y Harris (2009): izquierda = abierto, centro = centrado, derecha = comprometido.
PROCESOS_HEX = [
    {
        "id": "formulacion",
        "corto": "Flexibilidad y matriz",
        "svg_t": "Flexibilidad",
        "svg_s": "Formulación y matriz",
        "titulo": "Centro del hexaflex · Flexibilidad psicológica y formulación",
        "estilo": "centro",
        "polos": "Rigidez psicológica ↔ Flexibilidad psicológica",
        "color": "#2f6f8f",
        "cx": 280, "cy": 225,
        "desc": "Mapas transversales para formular el caso en los seis procesos o integrar experiencia interna, cinco sentidos y dirección en un solo diagrama.",
    },
    {
        "id": "aceptacion",
        "corto": "Aceptación",
        "svg_t": "Aceptación",
        "svg_s": "Contactar sin evitar",
        "titulo": "Aceptación y desesperanza creativa",
        "estilo": "abierto",
        "polos": "Evitación experiencial ↔ Aceptación",
        "color": "#c26a4e",
        "cx": 108, "cy": 152,
        "desc": "Soltar la agenda de control al comprobar su costo a largo plazo y abrir espacio voluntario a emociones y sensaciones.",
    },
    {
        "id": "defusion",
        "corto": "Defusión",
        "svg_t": "Defusión",
        "svg_s": "Desliteralizar",
        "titulo": "Defusión cognitiva",
        "estilo": "abierto",
        "polos": "Fusión cognitiva ↔ Defusión",
        "color": "#c05c78",
        "cx": 108, "cy": 298,
        "desc": "Cambiar la relación con los pensamientos: mirarlos como palabras o corriente que pasa sin tener que obedecerlos ni discutirlos.",
    },
    {
        "id": "presente",
        "corto": "Momento presente",
        "svg_t": "Momento presente",
        "svg_s": "Contactar lo directo",
        "titulo": "Contacto con el momento presente",
        "estilo": "centrado",
        "polos": "Pasado y futuro ↔ Contacto con el presente",
        "color": "#5f77b8",
        "cx": 280, "cy": 72,
        "desc": "Advertir en el momento qué aparece por dentro y por los cinco sentidos, notar cuándo se mordió un anzuelo y volver a la situación.",
    },
    {
        "id": "yo",
        "corto": "Yo como contexto",
        "svg_t": "Yo como contexto",
        "svg_s": "Tomar perspectiva",
        "titulo": "Yo como contexto (yo observador)",
        "estilo": "centrado",
        "polos": "Yo conceptualizado ↔ Yo observador",
        "color": "#3f83a6",
        "cx": 280, "cy": 378,
        "desc": "Distinguir entre el contenido que aparece (piezas, clima, etiquetas, globos) y la perspectiva estable desde la que se nota.",
    },
    {
        "id": "valores",
        "corto": "Valores",
        "svg_t": "Valores",
        "svg_s": "Elegir dirección",
        "titulo": "Clarificación de valores",
        "estilo": "comprometido",
        "polos": "Valores difusos o impuestos ↔ Valores propios",
        "color": "#3f9b86",
        "cx": 452, "cy": 152,
        "desc": "Elegir direcciones propias de vida, diferenciarlas de las metas y del deber ajeno, y contrastar cuánto lugar tuvieron en la semana.",
    },
    {
        "id": "accion",
        "corto": "Acción comprometida",
        "svg_t": "Acción comprometida",
        "svg_s": "Construir patrones",
        "titulo": "Acción comprometida",
        "estilo": "comprometido",
        "polos": "Inacción o impulsividad ↔ Acción con dirección",
        "color": "#6ea24f",
        "cx": 452, "cy": 298,
        "desc": "Sostener pasos concretos al servicio de lo que importa llevando el ruido o los pasajeros a bordo, sin esperar a que callen.",
    },
]

PROC_POR_ID = {p["id"]: p for p in PROCESOS_HEX}

# Subgrupos clínicos dentro de cada enfoque. En ACT coinciden con los procesos del hexaflex.
SUBGRUPOS = {
    "ACT": [
        (p["id"], p["titulo"], p["desc"], p["color"], ESTILOS_HEX[p["estilo"]]["nombre"])
        for p in PROCESOS_HEX
    ],
    "Cognitivo-conductual": [
        ("tcc-formulacion", "1 · Formulación funcional y motivación",
         "Entender qué mantiene la conducta en sus tres sistemas de respuesta y explorar la ambivalencia antes de pedir esfuerzo.",
         "#2f6f8f", "Evaluación y arranque"),
        ("tcc-cognitivo", "2 · Pensamientos, creencias y preocupación",
         "Cuestionar pensamientos automáticos, descender a creencias nucleares o aplazar el proceso repetitivo de preocuparse.",
         "#3b7a9e", "Trabajo cognitivo y metacognitivo"),
        ("tcc-exposicion", "3 · Exposición y activación conductual",
         "Acercarse de forma graduada sin conductas de seguridad y recuperar fuentes de agrado y dominio en la semana.",
         "#2c7c6c", "Cambio conductual directo"),
        ("tcc-afrontamiento", "4 · Afrontamiento, autorregulación y hábitos",
         "Resolver problemas modificables, preparar autoinstrucciones y dosis de estrés, organizar pendientes y consolidar el sueño.",
         "#4e6b8c", "Habilidades y autorregulación"),
    ],
    "DBT": [
        ("dbt-analisis", "1 · Análisis conductual y seguimiento",
         "Reconstruir eslabón por eslabón un episodio problema y registrar la semana entre sesiones.",
         "#5f77b8", "Evaluación y registro"),
        ("dbt-habilidades", "2 · Módulos de habilidades",
         "Atención plena (mente sabia), tolerancia al malestar, regulación emocional y efectividad interpersonal.",
         "#4c64a6", "Entrenamiento de habilidades"),
    ],
    "Compasión y mindfulness": [
        ("cft-calma", "1 · Sistema de calma y atención al presente",
         "Bajar la activación fisiológica con un ritmo respiratorio tranquilo y abrir una pausa de tres minutos en el día.",
         "#4a8a7a", "Regulación y presencia"),
        ("cft-compasion", "2 · Autocompasión y trabajo con la autocrítica",
         "Responder al sufrimiento y a la voz autocrítica desde una perspectiva cálida, sabia y firme.",
         "#3d7668", "Perspectiva compasiva"),
    ],
    "Psicología positiva": [
        ("pp-recursos", "Bienestar, fortalezas y sentido",
         "Mirar qué áreas del bienestar se conservan, nombrar las fortalezas disponibles y dirigir la atención a lo que funciona.",
         "#c9962f", "Evaluación de recursos y metas"),
    ],
    "Crisis y consumo": [
        ("crisis-intervencion", "Seguridad en crisis, manejo del impulso y motivación",
         "Acordar un plan de seguridad ante el riesgo suicida, atravesar el deseo de consumir sin obedecerlo y evocar razones propias de cambio.",
         "#b0503f", "Riesgo y prevención de recaídas"),
    ],
}

# Organización canónica de las 47 herramientas:
# archivo -> (enfoque, subgrupo, orden, proc_principal, [proc_secundarios], nota_vinculo)
ORGANIZACION = {
    # --- ACT: 1. Centro del hexaflex (Formulación y matriz) ---
    "act-por-donde-entrar.html": (
        "ACT", "formulacion", 1, "formulacion", [],
        "Evalúa como continuos los seis procesos del hexaflex y señala por cuál conviene entrar."
    ),
    "act-matriz.html": (
        "ACT", "formulacion", 2, "formulacion", ["presente", "yo", "valores", "accion"],
        "Cruza en un solo mapa la discriminación en el presente (cinco sentidos vs experiencia interna), el yo que nota en el centro, quién importa y los movimientos hacia o de alejamiento."
    ),

    # --- ACT: 2. Aceptación y desesperanza creativa ---
    "met-el-hoyo.html": (
        "ACT", "aceptacion", 3, "aceptacion", [],
        "Desesperanza creativa inicial: muestra que cavar alivia un segundo y solo hace más hondo el hoyo."
    ),
    "act-costo-de-la-lucha.html": (
        "ACT", "aceptacion", 4, "aceptacion", ["valores"],
        "Contrasta el alivio inmediato de las estrategias de control con lo que han costado a largo plazo en las áreas valiosas."
    ),
    "met-el-poligrafo.html": (
        "ACT", "aceptacion", 5, "aceptacion", [],
        "Hace visible en vivo cómo la exigencia de no sentir dispara la activación y sube el piso de malestar."
    ),
    "met-la-cuerda.html": (
        "ACT", "aceptacion", 6, "aceptacion", ["accion"],
        "Soltar la cuerda no elimina al monstruo: detiene el arrastre y deja las manos libres para hacer lo que importa."
    ),
    "act-empujar-el-papel.html": (
        "ACT", "aceptacion", 7, "aceptacion", ["defusion", "accion"],
        "Compara en dos rondas el cansancio y el bloqueo de empujar la preocupación frente a dejarla en la mesa y avanzar en la tarea."
    ),

    # --- ACT: 3. Defusión cognitiva ---
    "act-soltar-el-anzuelo.html": (
        "ACT", "defusion", 8, "defusion", [],
        "Prueba cinco maneras breves de desliteralizar un mismo pensamiento pegajoso para ver cuál le resta agarre."
    ),
    "met-la-palabra-repetida.html": (
        "ACT", "defusion", 9, "defusion", ["yo"],
        "Vacía por repetición una autoetiqueta del yo conceptualizado hasta que se nota como sonido."
    ),
    "met-hojas-en-el-arroyo.html": (
        "ACT", "defusion", 10, "defusion", ["presente", "yo"],
        "Entrena observar los pensamientos desde la orilla, notar el instante en que la atención se fue con la corriente y volver al presente."
    ),

    # --- ACT: 4. Contacto con el momento presente ---
    "act-los-ganchos.html": (
        "ACT", "presente", 11, "presente", ["defusion", "accion"],
        "Entrena advertir en el momento que se mordió un gancho por lo que se hace después, discriminar cinco sentidos de lo interno y seguir nadando."
    ),

    # --- ACT: 5. Yo como contexto ---
    "met-el-tablero.html": (
        "ACT", "yo", 12, "yo", ["aceptacion"],
        "Cambia la posición desde la pelea entre piezas blancas y negras hacia el tablero que las contiene sin gasto."
    ),
    "act-el-cielo-y-el-clima.html": (
        "ACT", "yo", 13, "yo", ["aceptacion", "presente"],
        "Une la perspectiva del cielo que tiene sitio para cualquier clima con la práctica de respirar y abrir espacio al malestar presente."
    ),
    "act-quien-lleva-los-globos.html": (
        "ACT", "yo", 14, "yo", ["defusion", "accion"],
        "Encuadre deíctico y jerárquico: poner el contenido en un globo enfrente, notar quién lo mira y elegir quién manda en el siguiente paso."
    ),

    # --- ACT: 6. Valores ---
    "act-brujula-de-valores.html": (
        "ACT", "valores", 15, "valores", ["accion"],
        "Mide en doce ámbitos la distancia entre la importancia elegida y las acciones de la última semana."
    ),
    "met-jardin-de-valores.html": (
        "ACT", "valores", 16, "valores", ["accion"],
        "Separa la semilla y su raíz (el valor que cuida) del riego semanal en conductas concretas."
    ),
    "met-los-ochenta-anos.html": (
        "ACT", "valores", 17, "valores", [],
        "Clarifica qué huella vincular se quiere dejar y la contrasta con cómo se vivió el último mes."
    ),

    # --- ACT: 7. Acción comprometida ---
    "met-la-radio.html": (
        "ACT", "accion", 18, "accion", ["defusion", "aceptacion"],
        "Puente entre defusión, apertura y acción: terminar una tarea paso a paso mientras la radio mental sigue encendida."
    ),
    "met-el-bus.html": (
        "ACT", "accion", 19, "accion", ["valores", "aceptacion", "defusion"],
        "Mantener el bus en marcha hacia el destino elegido con los pasajeros gritando a bordo, sin gastar la energía en discutir."
    ),

    # --- Cognitivo-conductual (12) ---
    "tcc-analisis-funcional.html": ("Cognitivo-conductual", "tcc-formulacion", 1, "", [], ""),
    "tcc-balance-decisional.html": ("Cognitivo-conductual", "tcc-formulacion", 2, "", [], ""),
    "registro-de-pensamientos.html": ("Cognitivo-conductual", "tcc-cognitivo", 3, "", [], ""),
    "tcc-flecha-descendente.html": ("Cognitivo-conductual", "tcc-cognitivo", 4, "", [], ""),
    "tcc-aplazar-la-preocupacion.html": ("Cognitivo-conductual", "tcc-cognitivo", 5, "", [], ""),
    "tcc-escalera-de-exposicion.html": ("Cognitivo-conductual", "tcc-exposicion", 6, "", [], ""),
    "tcc-activacion-conductual.html": ("Cognitivo-conductual", "tcc-exposicion", 7, "", [], ""),
    "tcc-solucion-de-problemas.html": ("Cognitivo-conductual", "tcc-afrontamiento", 8, "", [], ""),
    "tcc-autoinstrucciones.html": ("Cognitivo-conductual", "tcc-afrontamiento", 9, "", [], ""),
    "tcc-inoculacion-de-estres.html": ("Cognitivo-conductual", "tcc-afrontamiento", 10, "", [], ""),
    "tcc-lista-abc.html": ("Cognitivo-conductual", "tcc-afrontamiento", 11, "", [], ""),
    "tcc-ventana-de-sueno.html": ("Cognitivo-conductual", "tcc-afrontamiento", 12, "", [], ""),

    # --- DBT (6) ---
    "dbt-analisis-en-cadena.html": ("DBT", "dbt-analisis", 1, "", [], ""),
    "dbt-tarjeta-diaria.html": ("DBT", "dbt-analisis", 2, "", [], ""),
    "dbt-mente-sabia.html": ("DBT", "dbt-habilidades", 3, "", [], ""),
    "dbt-tarjeta-de-crisis.html": ("DBT", "dbt-habilidades", 4, "", [], ""),
    "dbt-verificar-los-hechos.html": ("DBT", "dbt-habilidades", 5, "", [], ""),
    "dbt-pedir-y-decir-no.html": ("DBT", "dbt-habilidades", 6, "", [], ""),

    # --- Compasión y mindfulness (4) ---
    "cft-ritmo-tranquilizador.html": ("Compasión y mindfulness", "cft-calma", 1, "", [], ""),
    "cft-espacio-de-respiracion.html": ("Compasión y mindfulness", "cft-calma", 2, "", [], ""),
    "cft-pausa-de-autocompasion.html": ("Compasión y mindfulness", "cft-compasion", 3, "", [], ""),
    "cft-el-yo-compasivo.html": ("Compasión y mindfulness", "cft-compasion", 4, "", [], ""),

    # --- Psicología positiva (3) ---
    "flor-permah.html": ("Psicología positiva", "pp-recursos", 1, "", [], ""),
    "fortalezas-del-caracter.html": ("Psicología positiva", "pp-recursos", 2, "", [], ""),
    "pp-tres-cosas-buenas.html": ("Psicología positiva", "pp-recursos", 3, "", [], ""),

    # --- Crisis y consumo (3) ---
    "crisis-plan-de-seguridad.html": ("Crisis y consumo", "crisis-intervencion", 1, "", [], ""),
    "crisis-surfear-el-impulso.html": ("Crisis y consumo", "crisis-intervencion", 2, "", [], ""),
    "crisis-importancia-y-confianza.html": ("Crisis y consumo", "crisis-intervencion", 3, "", [], ""),
}


def info_organizacion(archivo):
    """Devuelve diccionario con la ubicación clínica y de hexaflex para un archivo."""
    enf, sub, orden, proc, sec, vinc = ORGANIZACION[archivo]
    estilo = PROC_POR_ID[proc]["estilo"] if proc in PROC_POR_ID else ""
    es_metafora = archivo.startswith("met-") or archivo in {
        "act-los-ganchos.html",
        "act-el-cielo-y-el-clima.html",
        "act-empujar-el-papel.html",
        "act-quien-lleva-los-globos.html",
    }
    return {
        "enfoque": enf,
        "subgrupo": sub,
        "orden_org": orden,
        "proc": proc,
        "sec": sec,
        "vinc": vinc,
        "estilo": estilo,
        "es_metafora": es_metafora,
    }


def insignias_hexaflex(archivo):
    """Píldoras de proceso principal, vínculos secundarios en el hexaflex y nota de enlace."""
    info = info_organizacion(archivo)
    if not info["proc"]:
        return ""
    p = PROC_POR_ID[info["proc"]]
    sec_chips = "".join(
        '<span class="hx-tag sec" data-sec-chip="%s" title="También vinculada con %s">+ %s</span>'
        % (s, _h.escape(PROC_POR_ID[s]["corto"]), _h.escape(PROC_POR_ID[s]["corto"]))
        for s in info["sec"]
    )
    tipo_chip = '<span class="hx-tipo">Metáfora viva</span>' if info["es_metafora"] else ""
    nota = (
        '<span class="hx-vinc-nota" hidden><b>Vínculo en el hexaflex:</b> %s</span>'
        % _h.escape(info["vinc"])
        if info["vinc"] else ""
    )
    return (
        '<span class="hx-tags">'
        '<span class="hx-tag pri" style="color:%s;background:%s18;border-color:%s44">%s</span>'
        '%s%s</span>%s'
        % (p["color"], p["color"], p["color"], _h.escape(p["corto"]), sec_chips, tipo_chip, nota)
    )


def bloque_hexaflex():
    """Genera el panel interactivo del hexaflex para la sección de ACT."""
    # Conteo de hojas principales y secundarias por proceso
    conteos = {}
    for p in PROCESOS_HEX:
        pid = p["id"]
        pri = sum(1 for _, v in ORGANIZACION.items() if v[3] == pid)
        sec = sum(1 for _, v in ORGANIZACION.items() if pid in v[4])
        conteos[pid] = (pri, sec)

    # Orden del anillo exterior para el polígono y las cuerdas K6
    anillo_ids = ["presente", "valores", "accion", "yo", "defusion", "aceptacion"]
    anillo = [PROC_POR_ID[i] for i in anillo_ids]

    # Cuerdas internas del hexaflex (todas las diagonales entre los 6 vértices)
    lineas_svg = []
    for i in range(len(anillo)):
        for j in range(i + 1, len(anillo)):
            a, b = anillo[i], anillo[j]
            es_borde = (j == i + 1) or (i == 0 and j == len(anillo) - 1)
            clase = "hx-borde" if es_borde else "hx-cuerda"
            lineas_svg.append(
                f'<line class="{clase}" data-a="{a["id"]}" data-b="{b["id"]}" '
                f'x1="{a["cx"]}" y1="{a["cy"]}" x2="{b["cx"]}" y2="{b["cy"]}"/>'
            )

    # Radios al nodo central (Flexibilidad psicológica)
    centro = PROC_POR_ID["formulacion"]
    for a in anillo:
        lineas_svg.append(
            f'<line class="hx-radio" data-a="formulacion" data-b="{a["id"]}" '
            f'x1="{centro["cx"]}" y1="{centro["cy"]}" x2="{a["cx"]}" y2="{a["cy"]}"/>'
        )

    # Polígono de fondo suave
    pts = " ".join(f'{a["cx"]},{a["cy"]}' for a in anillo)
    poligono = f'<polygon class="hx-fondo-poly" points="{pts}"/>'

    # Nodos interactivos (6 vértices + centro)
    nodos_svg = []
    for p in PROCESOS_HEX:
        pid = p["id"]
        cx, cy = p["cx"], p["cy"]
        pri, sec = conteos[pid]
        es_centro = pid == "formulacion"
        w, h = (156, 62) if es_centro else (152, 58)
        rx = 14 if es_centro else 11
        x, y = cx - w // 2, cy - h // 2
        cuenta_txt = f"{pri} hojas" if sec == 0 else f"{pri} princ. · +{sec} vinc."
        nodos_svg.append(f"""      <g class="hx-nodo{' hx-nodo-centro' if es_centro else ''}" data-hx="{pid}" data-estilo="{p['estilo']}" role="button" tabindex="0" aria-pressed="false" aria-label="{_h.escape(p['corto'])}: {cuenta_txt}">
        <rect class="hx-caja" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" style="--hx-c:{p['color']}" stroke="{p['color']}"/>
        <circle cx="{x + 15}" cy="{y + 18}" r="5" fill="{p['color']}"/>
        <text class="hx-t" x="{x + 26}" y="{y + 22}">{_h.escape(p['svg_t'])}</text>
        <text class="hx-s" x="{cx}" y="{y + 38}" text-anchor="middle">{_h.escape(p['svg_s'])}</text>
        <text class="hx-n" x="{cx}" y="{y + 51}" text-anchor="middle" fill="{p['color']}">{cuenta_txt}</text>
      </g>""")

    # Chips de estilos de respuesta
    chips_estilo = "".join(
        f'<button type="button" class="hx-est-btn" data-hx-estilo="{k}" style="--hx-c:{v["color"]}" aria-pressed="false">'
        f'<b>{_h.escape(v["nombre"])}</b><span>{_h.escape(v["desc"].split(":")[0])}</span></button>'
        for k, v in ESTILOS_HEX.items() if k != "centro"
    )

    # Chips rápidos por proceso
    chips_proc = (
        '<button type="button" class="hx-chip" data-hx-chip="todos" aria-pressed="true">Todos los procesos (19)</button>'
        + "".join(
            f'<button type="button" class="hx-chip" data-hx-chip="{p["id"]}" style="--hx-c:{p["color"]}" aria-pressed="false">'
            f'<span class="hx-dot" style="background:{p["color"]}"></span>{_h.escape(p["corto"])} '
            f'<small>({conteos[p["id"]][0]}{("+" + str(conteos[p["id"]][1])) if conteos[p["id"]][1] else ""})</small></button>'
            for p in PROCESOS_HEX
        )
    )

    datos_js = _json.dumps(
        {
            p["id"]: {
                "titulo": p["titulo"],
                "corto": p["corto"],
                "estilo": ESTILOS_HEX[p["estilo"]]["nombre"],
                "polos": p["polos"],
                "color": p["color"],
                "desc": p["desc"],
                "pri": conteos[p["id"]][0],
                "sec": conteos[p["id"]][1],
            }
            for p in PROCESOS_HEX
        },
        ensure_ascii=False,
    )
    estilos_js = _json.dumps(ESTILOS_HEX, ensure_ascii=False)

    return f"""    <div class="hx-panel" id="hx-panel" data-hx-datos='{_h.escape(datos_js)}' data-hx-estilos='{_h.escape(estilos_js)}'>
      <div class="hx-fig">
        <svg class="hx-svg" id="hx-svg" viewBox="0 0 560 432" role="img" aria-label="Hexaflex de la flexibilidad psicológica: toca un proceso para filtrar sus herramientas">
          <g class="hx-cols-etq" aria-hidden="true">
            <text x="108" y="24" text-anchor="middle">ESTILO ABIERTO</text>
            <text x="280" y="24" text-anchor="middle">ESTILO CENTRADO</text>
            <text x="452" y="24" text-anchor="middle">ESTILO COMPROMETIDO</text>
          </g>
          {poligono}
          <g class="hx-red">
            {chr(10).join("            " + l for l in lineas_svg)}
          </g>
{chr(10).join(nodos_svg)}
        </svg>
      </div>
      <div class="hx-info">
        <div class="hx-info-cab">
          <span class="hx-kicker">Mapa interactivo del hexaflex</span>
          <button type="button" class="hx-reset" id="hx-reset" hidden>Ver los 6 procesos (19 hojas)</button>
        </div>
        <div class="hx-estilos-bar" role="group" aria-label="Filtrar por estilo de respuesta">
          {chips_estilo}
        </div>
        <div class="hx-chips-bar" role="group" aria-label="Filtrar por proceso del hexaflex">
          {chips_proc}
        </div>
        <div class="hx-lectura" id="hx-lectura">
          <div class="hx-lec-top">
            <b id="hx-lec-titulo">Los seis procesos y el centro del hexaflex</b>
            <span class="hx-lec-polos" id="hx-lec-polos">19 herramientas integradas (metáforas vivas y ejercicios ACT)</span>
          </div>
          <p id="hx-lec-desc">Toca cualquier vértice del hexágono, el centro o uno de los tres estilos de respuesta para reunir arriba las herramientas principales de ese proceso junto con las hojas que tienden puentes hacia él.</p>
        </div>
      </div>
    </div>"""


def controles(placeholder):
    chips = "".join(
        '<button class="fchip" type="button" data-enf="%s" aria-pressed="false">%s</button>' % (e, e)
        for e in ENFOQUES
    )
    return f"""<aside class="riel-izq" aria-label="Filtros">
  <div class="controles">
    <input class="buscador" id="buscador" type="search" placeholder="{placeholder}" autocomplete="off">
    <div class="controles-r">Enfoque</div>
    <div class="fila" id="f-enf">
      <button class="fchip" type="button" data-enf="todos" aria-pressed="true">Todos</button>{chips}
    </div>
    <div class="controles-r" id="f-hx-rot">Proceso del hexaflex (ACT)</div>
    <div class="fila" id="f-hx-riel">
      <button class="fchip hx-rchip" type="button" data-hx-riel="todos" aria-pressed="true">Todos</button>
      {"".join('<button class="fchip hx-rchip" type="button" data-hx-riel="%s" aria-pressed="false"><span class="hx-dot" style="background:%s"></span>%s</button>' % (p["id"], p["color"], _h.escape(p["corto"])) for p in PROCESOS_HEX)}
    </div>
    <div class="cuenta" id="cuenta"></div>
  </div>
</aside>"""


MAPA = """<aside class="riel-der">
  <nav class="mapa" id="mapa" aria-label="Mapa de las hojas"></nav>
</aside>
<div class="nav-movil">
  <button type="button" class="sec" id="nm-filtros">Filtros</button>
  <button type="button" id="nm-mapa">Hojas</button>
</div>
<div id="nm-velo" hidden></div>"""


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
  .fchip{font:inherit;font-size:12.5px;border:1px solid var(--linea);border-radius:999px;
    padding:5px 11px;background:#fff;color:var(--tinta-suave);cursor:pointer;
    display:inline-flex;align-items:center;gap:6px}
  .fchip:hover{border-color:var(--acento);color:var(--tinta)}
  .fchip[aria-pressed="true"]{background:var(--acento);border-color:var(--acento);color:#fff;font-weight:600}
  .fchip[aria-pressed="true"] .hx-dot{box-shadow:0 0 0 1.5px #fff}
  .hx-dot{width:7px;height:7px;border-radius:50%;display:inline-block;flex:0 0 auto}
  .cuenta{margin-top:12px;font-size:12.5px;color:var(--tinta-suave);line-height:1.45}
  [data-grupo][hidden],[data-subgrupo][hidden],[data-item][hidden]{display:none !important}
  .sin-resultados{border:1px dashed var(--linea);border-radius:var(--radio);padding:22px;
    text-align:center;color:var(--tinta-suave);font-size:14px}
  .sin-resultados[hidden]{display:none}

  /* ---- Subgrupos clínicos y hexaflex ---- */
  .subgrupos{display:flex;flex-direction:column;gap:18px;margin-top:16px}
  .subgrupo{border:1px solid var(--linea);border-left:4px solid var(--sub-c,var(--acento));
    border-radius:10px;padding:14px 16px 16px;background:#fbfcfd}
  .subgrupo.hx-sub-primario{order:-2;background:#f7fbfa;box-shadow:0 2px 10px rgba(47,111,143,.09)}
  .subgrupo.hx-sub-vinculado{order:1;border-style:dashed;background:#fcfdfe}
  .subgrupo-cab{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:4px}
  .subgrupo-cab h3{margin:0;font-size:16px;color:var(--tinta);display:flex;align-items:center;gap:8px}
  .subgrupo-cab .sub-punto{width:10px;height:10px;border-radius:50%;background:var(--sub-c,var(--acento));flex:0 0 auto}
  .subgrupo-cab .sub-est{font-size:10.5px;text-transform:uppercase;letter-spacing:.7px;font-weight:700;
    color:var(--sub-c,var(--tinta-suave));background:#fff;border:1px solid var(--linea);border-radius:999px;padding:2px 9px}
  .subgrupo > .sub-desc{margin:0 0 12px;font-size:13px;color:var(--tinta-suave);line-height:1.45;max-width:82ch}
  .subgrupo > .sub-vinc-aviso{margin:0 0 10px;font-size:12.5px;font-weight:600;color:var(--acento);
    background:var(--acento-claro);border-radius:7px;padding:5px 10px;display:inline-block}
  .subgrupo > .sub-vinc-aviso[hidden]{display:none}

  /* ---- Panel interactivo del hexaflex ---- */
  .hx-panel{display:grid;grid-template-columns:minmax(300px,470px) minmax(0,1fr);gap:20px;align-items:center;
    background:linear-gradient(180deg,#f8fbfd,#ffffff);border:1px solid var(--linea);border-radius:12px;
    padding:16px 18px;margin-top:14px}
  .hx-svg{display:block;width:100%;max-width:480px;height:auto;margin:0 auto;user-select:none}
  .hx-cols-etq text{font-size:9.5px;font-weight:700;letter-spacing:.11em;fill:#7b8c9d}
  .hx-fondo-poly{fill:#eef5f8;fill-opacity:.5;stroke:none}
  .hx-borde{stroke:#b8c9d8;stroke-width:2;transition:stroke .18s,stroke-width .18s,opacity .18s}
  .hx-cuerda{stroke:#dde6ee;stroke-width:1.3;stroke-dasharray:4 4;transition:stroke .18s,stroke-width .18s,opacity .18s}
  .hx-radio{stroke:#cfdce6;stroke-width:1.4;transition:stroke .18s,stroke-width .18s,opacity .18s}
  .hx-svg.hx-filtrado .hx-borde,.hx-svg.hx-filtrado .hx-cuerda,.hx-svg.hx-filtrado .hx-radio{opacity:.25}
  .hx-svg.hx-filtrado line.hx-linea-activa{opacity:1;stroke:var(--hx-linea-c,#2f6f8f);stroke-width:2.5;stroke-dasharray:none}
  .hx-nodo{cursor:pointer;transition:transform .15s,opacity .15s}
  .hx-nodo:focus{outline:none}
  .hx-caja{fill:#ffffff;stroke-width:1.8;transition:fill .15s,stroke-width .15s,filter .15s}
  .hx-nodo-centro .hx-caja{fill:#f3f8fb;stroke-width:2.2}
  .hx-nodo:hover .hx-caja,.hx-nodo:focus-visible .hx-caja{stroke-width:2.6;filter:drop-shadow(0 3px 8px rgba(31,75,102,.16))}
  .hx-nodo[aria-pressed="true"] .hx-caja{fill:var(--acento-claro);stroke-width:3;filter:drop-shadow(0 4px 10px rgba(31,75,102,.2))}
  .hx-svg.hx-filtrado .hx-nodo:not(.hx-nodo-rel):not([aria-pressed="true"]){opacity:.42}
  .hx-t{font-size:12.5px;font-weight:700;fill:#1d2733}
  .hx-s{font-size:10.5px;fill:#5a6a7d}
  .hx-n{font-size:10px;font-weight:700;letter-spacing:.02em}

  .hx-info{display:flex;flex-direction:column;gap:11px;min-width:0}
  .hx-info-cab{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}
  .hx-kicker{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--acento)}
  .hx-reset{font:inherit;font-size:12px;font-weight:600;color:var(--acento);background:var(--acento-claro);
    border:1px solid var(--acento);border-radius:999px;padding:4px 12px;cursor:pointer}
  .hx-reset:hover{background:var(--acento);color:#fff}
  .hx-estilos-bar{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px}
  .hx-est-btn{font:inherit;text-align:left;background:#fff;border:1px solid var(--linea);
    border-top:3px solid var(--hx-c,var(--acento));border-radius:8px;padding:7px 10px;cursor:pointer;
    transition:border-color .13s,background .13s}
  .hx-est-btn b{display:block;font-size:12.5px;color:var(--tinta)}
  .hx-est-btn span{display:block;font-size:11px;color:var(--tinta-suave);margin-top:1px}
  .hx-est-btn:hover{border-color:var(--hx-c,var(--acento));background:#fafcfd}
  .hx-est-btn[aria-pressed="true"]{background:var(--acento-claro);border-color:var(--hx-c,var(--acento))}
  .hx-chips-bar{display:flex;flex-wrap:wrap;gap:6px}
  .hx-chip{font:inherit;font-size:12px;border:1px solid var(--linea);border-radius:999px;
    padding:4px 10px;background:#fff;color:var(--tinta-suave);cursor:pointer;
    display:inline-flex;align-items:center;gap:5px}
  .hx-chip small{font-size:10.5px;opacity:.8}
  .hx-chip:hover{border-color:var(--hx-c,var(--acento));color:var(--tinta)}
  .hx-chip[aria-pressed="true"]{background:var(--hx-c,var(--acento));border-color:var(--hx-c,var(--acento));
    color:#fff;font-weight:600}
  .hx-chip[aria-pressed="true"] .hx-dot{background:#fff !important}
  .hx-lectura{background:#fff;border:1px solid var(--linea);border-left:4px solid var(--hx-lec-c,var(--acento));
    border-radius:9px;padding:11px 14px}
  .hx-lec-top{display:flex;align-items:baseline;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:4px}
  .hx-lec-top b{font-size:14.5px;color:var(--tinta)}
  .hx-lec-polos{font-size:11.5px;font-weight:600;color:var(--tinta-suave)}
  .hx-lectura p{margin:0;font-size:13px;color:var(--tinta-suave);line-height:1.45}

  /* ---- Etiquetas de hexaflex dentro de cada tarjeta ---- */
  .hx-tags{display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin-top:8px}
  .hx-tag{font-size:10.5px;font-weight:700;border-radius:999px;padding:2px 8px;border:1px solid transparent;line-height:1.3}
  .hx-tag.sec{color:var(--tinta-suave);background:#f3f6f9;border-color:var(--linea);font-weight:600}
  .hx-tag.sec.hx-sec-activo{color:#fff;background:var(--acento);border-color:var(--acento)}
  .hx-tipo{font-size:10px;color:var(--tinta-suave);border:1px dashed var(--linea);border-radius:999px;padding:1px 7px;margin-left:auto}
  .hx-vinc-nota{display:block;margin-top:8px;padding:6px 9px;border-radius:7px;background:var(--acento-claro);
    color:#1f4356;font-size:12px;line-height:1.4}
  .hx-vinc-nota[hidden]{display:none !important}

  @media (max-width:960px){
    .hx-panel{grid-template-columns:1fr}
    .hx-estilos-bar{grid-template-columns:1fr}
  }

  .mapa-r{display:block;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;
    color:var(--tinta-suave);margin:2px 0 10px}
  .mapa-g{margin-top:14px}
  .mapa-g[hidden],.mapa li[hidden]{display:none}
  .mapa-g > a{display:block;font-weight:700;font-size:14px;color:var(--tinta);text-decoration:none;
    margin-bottom:4px}
  .mapa ul{list-style:none;margin:0;padding:0 0 0 10px;border-left:2px solid var(--linea)}
  .mapa li.mapa-sub{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;
    color:var(--tinta-suave);margin:8px 0 2px 4px;pointer-events:none}
  .mapa li a{display:block;font-size:12.5px;line-height:1.35;color:var(--tinta-suave);text-decoration:none;
    padding:3px 8px;border-radius:6px;margin-left:-2px;border-left:2px solid transparent}
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
  /* Celular, tableta y portátil: los rieles no caben al costado, así que dos
     botones flotantes los abren como paneles: el mapa a la derecha y los
     filtros a la izquierda. */
  .nav-movil,.nm-cerrar{display:none}
  @media (max-width:1279px){
    .nav-movil{display:flex;position:fixed;right:14px;bottom:14px;gap:8px;z-index:40}
    .nav-movil button{font:inherit;font-size:14px;font-weight:600;padding:10px 16px;border-radius:999px;
      border:1px solid var(--acento);background:var(--acento);color:#fff;
      box-shadow:0 4px 14px rgba(0,0,0,.2);cursor:pointer}
    .nav-movil button.sec{background:#fff;color:var(--acento)}
    body.panel-mapa .con-rieles > .riel-der{display:block;position:fixed;top:0;right:0;bottom:0;
      width:min(86vw,340px);background:var(--papel);z-index:60;overflow-y:auto;overscroll-behavior:contain;
      padding:14px 16px 40px;box-shadow:-6px 0 24px rgba(0,0,0,.22);box-sizing:border-box}
    body.panel-filtros .controles{position:fixed;top:0;left:0;bottom:0;width:min(86vw,340px);margin:0;
      z-index:60;overflow-y:auto;overscroll-behavior:contain;border-radius:0;
      padding:14px 16px 40px;box-shadow:6px 0 24px rgba(0,0,0,.22);box-sizing:border-box}
    body.panel-mapa .nm-cerrar,body.panel-filtros .nm-cerrar{display:block;margin:0 0 8px auto;font:inherit;
      font-size:13px;font-weight:600;background:#fff;border:1px solid var(--linea);border-radius:8px;
      padding:5px 12px;color:var(--tinta-suave);cursor:pointer}
    body.panel-mapa .nav-movil,body.panel-filtros .nav-movil{display:none}
    #nm-velo{position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:55}
    #nm-velo[hidden]{display:none}
  }
  @media print{
    .nav-movil,#nm-velo,.nm-cerrar{display:none !important}
    .con-rieles > .riel-izq,.con-rieles > .riel-der{display:none !important}
    .envoltura.con-rieles{display:block}
  }
"""


JS = r"""
(function(){
  const $ = id => document.getElementById(id);
  const norm = s => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  const items = [...document.querySelectorAll("[data-item]")];
  const subgrupos = [...document.querySelectorAll("[data-subgrupo]")];
  const grupos = [...document.querySelectorAll("[data-grupo]")];
  items.forEach(el => { el.dataset.txt = norm(el.textContent); });

  // Mapa derecho: encabezado por enfoque, subtítulo de subgrupo y hojas.
  const esc = s => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;");
  $("mapa").innerHTML = '<span class="mapa-r">Las hojas</span>' + grupos.map((g, gi) => {
    if (!g.id) g.id = "grupo-" + gi;
    const subs = subgrupos.filter(sg => g.contains(sg));
    let interior = "";
    if (subs.length) {
      interior = subs.map((sg, si) => {
        if (!sg.id) sg.id = g.id + "-s" + si;
        const suyos = items.filter(it => sg.contains(it));
        const rot = sg.dataset.subcorto ? '<li class="mapa-sub" data-ms="' + sg.id + '">' + esc(sg.dataset.subcorto) + '</li>' : '';
        return rot + suyos.map((it, ii) => {
          if (!it.id) it.id = sg.id + "-" + ii;
          const destino = it.dataset.href || ("#" + it.id);
          return '<li data-i="' + it.id + '"><a href="' + esc(destino) + '" data-i="' + it.id + '">' + esc(it.dataset.titulo) + '</a></li>';
        }).join("");
      }).join("");
    } else {
      const suyos = items.filter(it => g.contains(it));
      interior = suyos.map((it, ii) => {
        if (!it.id) it.id = g.id + "-" + ii;
        const destino = it.dataset.href || ("#" + it.id);
        return '<li data-i="' + it.id + '"><a href="' + esc(destino) + '" data-i="' + it.id + '">' + esc(it.dataset.titulo) + '</a></li>';
      }).join("");
    }
    return '<div class="mapa-g" data-g="' + g.id + '"><a href="#' + g.id + '">' + esc(g.dataset.grupo) + '</a><ul>' +
      interior + '</ul></div>';
  }).join("") + (document.body.dataset.extra || "");

  let enf = "todos";
  let hxModo = "todos"; // "todos" | id de proceso | "estilo:abierto" | "estilo:centrado" | "estilo:comprometido"

  const hxPanel = $("hx-panel");
  const hxDatos = hxPanel ? JSON.parse(hxPanel.dataset.hxDatos || "{}") : {};
  const hxEstilos = hxPanel ? JSON.parse(hxPanel.dataset.hxEstilos || "{}") : {};

  function coincideHex(it) {
    if (it.dataset.enf !== "ACT" || hxModo === "todos") return { ok: true, rol: "pri" };
    const proc = it.dataset.proc || "";
    const secs = (it.dataset.procSec || "").split(",").filter(Boolean);
    if (hxModo.startsWith("estilo:")) {
      const est = hxModo.slice(7);
      const procsEst = (hxEstilos[est] && hxEstilos[est].procesos) || [];
      if (procsEst.includes(proc)) return { ok: true, rol: "pri" };
      if (secs.some(s => procsEst.includes(s))) return { ok: true, rol: "sec" };
      return { ok: false, rol: "" };
    }
    if (proc === hxModo) return { ok: true, rol: "pri" };
    if (secs.includes(hxModo)) return { ok: true, rol: "sec" };
    return { ok: false, rol: "" };
  }

  function actualizarUIHex() {
    const rotRiel = $("f-hx-rot"), cajaRiel = $("f-hx-riel");
    if (rotRiel && cajaRiel) {
      const mostrarHx = (enf === "todos" || enf === "ACT");
      rotRiel.hidden = !mostrarHx;
      cajaRiel.hidden = !mostrarHx;
      cajaRiel.querySelectorAll("[data-hx-riel]").forEach(b => {
        b.setAttribute("aria-pressed", String(b.dataset.hxRiel === hxModo));
      });
    }
    if (!hxPanel) return;
    const svg = $("hx-svg");
    const activos = hxModo === "todos" ? [] : (
      hxModo.startsWith("estilo:")
        ? ((hxEstilos[hxModo.slice(7)] && hxEstilos[hxModo.slice(7)].procesos) || [])
        : [hxModo]
    );
    svg.classList.toggle("hx-filtrado", activos.length > 0);

    // Qué otros procesos quedan conectados por herramientas secundarias
    const relacionados = new Set(activos);
    if (activos.length) {
      items.filter(it => it.dataset.enf === "ACT").forEach(it => {
        const p = it.dataset.proc;
        const secs = (it.dataset.procSec || "").split(",").filter(Boolean);
        if (activos.includes(p)) secs.forEach(s => relacionados.add(s));
        if (secs.some(s => activos.includes(s))) relacionados.add(p);
      });
    }

    svg.querySelectorAll(".hx-nodo").forEach(n => {
      const id = n.dataset.hx;
      n.setAttribute("aria-pressed", String(activos.includes(id)));
      n.classList.toggle("hx-nodo-rel", relacionados.has(id));
    });

    svg.querySelectorAll(".hx-red line").forEach(l => {
      const a = l.dataset.a, b = l.dataset.b;
      const on = (activos.includes(a) && relacionados.has(b)) || (activos.includes(b) && relacionados.has(a));
      l.classList.toggle("hx-linea-activa", on);
      if (on && activos[0] && hxDatos[activos[0]]) {
        l.style.setProperty("--hx-linea-c", hxDatos[activos[0]].color);
      }
    });

    hxPanel.querySelectorAll("[data-hx-chip]").forEach(b => {
      b.setAttribute("aria-pressed", String(b.dataset.hxChip === hxModo));
    });
    hxPanel.querySelectorAll("[data-hx-estilo]").forEach(b => {
      b.setAttribute("aria-pressed", String("estilo:" + b.dataset.hxEstilo === hxModo));
    });

    const btnReset = $("hx-reset");
    if (btnReset) btnReset.hidden = (hxModo === "todos");

    const lec = $("hx-lectura"), t = $("hx-lec-titulo"), p = $("hx-lec-polos"), d = $("hx-lec-desc");
    if (hxModo === "todos") {
      lec.style.setProperty("--hx-lec-c", "#2f6f8f");
      t.textContent = "Los seis procesos y el centro del hexaflex";
      p.textContent = "19 herramientas integradas (metáforas vivas y ejercicios ACT)";
      d.textContent = "Toca cualquier vértice del hexágono, el centro o uno de los tres estilos de respuesta para reunir arriba las herramientas principales de ese proceso junto con las hojas que tienden puentes hacia él.";
    } else if (hxModo.startsWith("estilo:")) {
      const est = hxEstilos[hxModo.slice(7)];
      lec.style.setProperty("--hx-lec-c", est.color);
      t.textContent = est.nombre;
      p.textContent = est.procesos.map(k => hxDatos[k].corto).join(" + ");
      d.textContent = est.desc;
    } else if (hxDatos[hxModo]) {
      const info = hxDatos[hxModo];
      lec.style.setProperty("--hx-lec-c", info.color);
      t.textContent = info.titulo;
      p.textContent = info.estilo + " · " + info.polos;
      d.textContent = info.desc + (info.sec ? ` (${info.pri} principales y ${info.sec} vinculadas desde otros vértices del hexaflex).` : ` (${info.pri} herramientas principales).`);
    }
  }

  function aplicar(){
    const q = norm($("buscador").value.trim());
    let n = 0;
    const activosHx = hxModo === "todos" ? [] : (
      hxModo.startsWith("estilo:")
        ? ((hxEstilos[hxModo.slice(7)] && hxEstilos[hxModo.slice(7)].procesos) || [])
        : [hxModo]
    );

    items.forEach(it => {
      const enfOk = (enf === "todos" || it.dataset.enf === enf);
      const qOk = (!q || it.dataset.txt.includes(q));
      const hx = coincideHex(it);
      const ok = enfOk && qOk && hx.ok;
      it.hidden = !ok;
      it.classList.toggle("hx-item-vinculado", ok && hx.rol === "sec");

      // Mostrar nota de vínculo cuando actúa como herramienta secundaria del proceso elegido
      const nota = it.querySelector(".hx-vinc-nota");
      if (nota) nota.hidden = !(ok && hx.rol === "sec");
      it.querySelectorAll("[data-sec-chip]").forEach(ch => {
        ch.classList.toggle("hx-sec-activo", ok && activosHx.includes(ch.dataset.secChip));
      });

      const li = $("mapa").querySelector('li[data-i="' + it.id + '"]');
      if (li) li.hidden = !ok;
      if (ok) n++;
    });

    subgrupos.forEach(sg => {
      const visibles = items.filter(it => !it.hidden && sg.contains(it));
      sg.hidden = visibles.length === 0;
      const ms = $("mapa").querySelector('li[data-ms="' + sg.id + '"]');
      if (ms) ms.hidden = sg.hidden;

      if (sg.dataset.subproc) {
        const esPri = activosHx.includes(sg.dataset.subproc);
        const esVinc = activosHx.length > 0 && !esPri && visibles.length > 0;
        sg.classList.toggle("hx-sub-primario", esPri);
        sg.classList.toggle("hx-sub-vinculado", esVinc);
        const aviso = sg.querySelector(".sub-vinc-aviso");
        if (aviso) aviso.hidden = !esVinc;
      }
    });

    grupos.forEach(g => {
      const vacio = !items.some(it => !it.hidden && g.contains(it));
      g.hidden = vacio;
      const mg = $("mapa").querySelector('[data-g="' + g.id + '"]');
      if (mg) mg.hidden = vacio;
    });

    let sufijoHx = "";
    if ((enf === "todos" || enf === "ACT") && hxModo !== "todos") {
      sufijoHx = hxModo.startsWith("estilo:")
        ? " (" + hxEstilos[hxModo.slice(7)].nombre.toLowerCase() + ")"
        : " (" + (hxDatos[hxModo] ? hxDatos[hxModo].corto : hxModo) + ")";
    }
    $("cuenta").textContent = n + (n === 1 ? " hoja" : " hojas") +
      (enf === "todos" ? "" : " de " + enf) + sufijoHx +
      (q ? (n === 1 ? " que coincide" : " que coinciden") + " con la búsqueda" : "");
    const vacia = $("sin-resultados");
    if (vacia) vacia.hidden = n > 0;
    actualizarUIHex();
  }

  function fijarHx(nuevo) {
    hxModo = (hxModo === nuevo && nuevo !== "todos") ? "todos" : nuevo;
    if (hxModo !== "todos" && enf !== "todos" && enf !== "ACT") {
      enf = "ACT";
      $("f-enf").querySelectorAll(".fchip").forEach(c => c.setAttribute("aria-pressed", String(c.dataset.enf === "ACT")));
    }
    aplicar();
  }

  $("f-enf").addEventListener("click", ev => {
    const b = ev.target.closest(".fchip"); if (!b) return;
    enf = b.dataset.enf;
    $("f-enf").querySelectorAll(".fchip").forEach(c => c.setAttribute("aria-pressed", String(c === b)));
    aplicar();
  });

  if ($("f-hx-riel")) {
    $("f-hx-riel").addEventListener("click", ev => {
      const b = ev.target.closest("[data-hx-riel]"); if (!b) return;
      fijarHx(b.dataset.hxRiel);
    });
  }

  if (hxPanel) {
    hxPanel.addEventListener("click", ev => {
      const nodo = ev.target.closest(".hx-nodo");
      if (nodo) { fijarHx(nodo.dataset.hx); return; }
      const chip = ev.target.closest("[data-hx-chip]");
      if (chip) { fijarHx(chip.dataset.hxChip); return; }
      const est = ev.target.closest("[data-hx-estilo]");
      if (est) { fijarHx("estilo:" + est.dataset.hxEstilo); return; }
      if (ev.target.closest("#hx-reset")) { fijarHx("todos"); }
    });
    hxPanel.addEventListener("keydown", ev => {
      if (ev.key !== "Enter" && ev.key !== " ") return;
      const nodo = ev.target.closest(".hx-nodo");
      if (nodo) { ev.preventDefault(); fijarHx(nodo.dataset.hx); }
    });
  }

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
  // Paneles en pantallas angostas.
  const velo = $("nm-velo"), riel = document.querySelector(".riel-der"), filtros = document.querySelector(".controles");
  function cerrar(){ document.body.classList.remove("panel-mapa", "panel-filtros"); velo.hidden = true; }
  function abrir(c){ cerrar(); document.body.classList.add(c); velo.hidden = false; }
  [riel, filtros].forEach(p => {
    const x = document.createElement("button");
    x.type = "button"; x.className = "nm-cerrar"; x.textContent = "Cerrar ×";
    x.addEventListener("click", cerrar);
    p.prepend(x);
  });
  $("nm-mapa").addEventListener("click", () => abrir("panel-mapa"));
  $("nm-filtros").addEventListener("click", () => abrir("panel-filtros"));
  velo.addEventListener("click", cerrar);
  document.addEventListener("keydown", ev => { if (ev.key === "Escape") cerrar(); });
  riel.addEventListener("click", ev => { if (ev.target.closest("a")) cerrar(); });

  let pendiente = false;
  addEventListener("scroll", () => {
    if (pendiente) return;
    pendiente = true;
    requestAnimationFrame(() => { pendiente = false; marcar(); });
  }, { passive: true });
})();
"""


# ---------------------------------------------------------------------------
# Índice de hojas dentro de cada herramienta
# ---------------------------------------------------------------------------
INICIO, FIN = "<!--indice-hojas-->", "<!--/indice-hojas-->"

INDICE_CSS = """
.ih-boton{position:fixed;bottom:14px;right:14px;z-index:40;font:inherit;font-size:13.5px;font-weight:600;
  padding:8px 14px;border-radius:999px;border:1px solid var(--acento,#2f6f8f);background:#fff;
  color:var(--acento,#2f6f8f);box-shadow:0 3px 10px rgba(0,0,0,.15);cursor:pointer}
.ih-panel{position:fixed;top:0;left:0;bottom:0;width:min(86vw,300px);box-sizing:border-box;
  background:var(--papel,#fff);border-right:1px solid var(--linea,#dde);z-index:60;overflow-y:auto;
  overscroll-behavior:contain;padding:16px 16px 40px;transform:translateX(-105%);
  transition:transform .2s;box-shadow:6px 0 24px rgba(0,0,0,.2);font-size:14px}
body.ih-abierto .ih-panel{transform:none}
.ih-velo{position:fixed;inset:0;background:rgba(0,0,0,.35);z-index:55}
.ih-velo[hidden]{display:none}
.ih-cerrar{display:block;margin:0 0 10px auto;font:inherit;font-size:13px;font-weight:600;background:#fff;
  border:1px solid var(--linea,#dde);border-radius:8px;padding:5px 12px;color:var(--tinta-suave,#667);cursor:pointer}
.ih-panel .ih-top{display:block;font-weight:700;color:var(--acento,#2f6f8f);text-decoration:none;margin:2px 0 4px}
.ih-panel .ih-g{margin-top:14px}
.ih-panel .ih-g > b{display:block;font-size:13.5px;color:var(--tinta,#223);margin-bottom:4px}
.ih-panel ul{list-style:none;margin:0;padding:0 0 0 10px;border-left:2px solid var(--linea,#dde)}
.ih-panel li.ih-sub{font-size:10.5px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;
  color:var(--tinta-suave,#667);margin:8px 0 2px 4px}
.ih-panel li a{display:block;font-size:13px;line-height:1.35;color:var(--tinta-suave,#667);text-decoration:none;
  padding:4px 8px;border-radius:6px;margin-left:-2px;border-left:2px solid transparent}
.ih-panel li a:hover{color:var(--acento,#2f6f8f);background:var(--acento-claro,#eef5f8)}
.ih-panel li a.actual{color:var(--acento,#2f6f8f);border-left-color:var(--acento,#2f6f8f);
  background:var(--acento-claro,#eef5f8);font-weight:600}
@media (min-width:1500px){
  .ih-boton,.ih-cerrar,.ih-velo{display:none !important}
  .ih-panel{transform:none;box-shadow:none;width:260px;padding-top:22px}
  body{padding-left:260px;box-sizing:border-box}
}
@media print{.ih-boton,.ih-panel,.ih-velo{display:none !important}}
"""

INDICE_JS = """
(function(){
  const b = document.body, v = document.getElementById("ih-velo");
  const cerrar = () => { b.classList.remove("ih-abierto"); v.hidden = true; };
  document.getElementById("ih-boton").addEventListener("click", () => { b.classList.add("ih-abierto"); v.hidden = false; });
  document.getElementById("ih-cerrar").addEventListener("click", cerrar);
  v.addEventListener("click", cerrar);
  document.addEventListener("keydown", e => { if (e.key === "Escape") cerrar(); });
  const a = document.querySelector(".ih-panel a.actual");
  if (a) a.scrollIntoView({ block: "center" });
})();
"""


def indice_hojas(fichas, actual):
    grupos = []
    for enfoque in ENFOQUES:
        suyas = [f for f in fichas if f["enfoque"] == enfoque]
        if not suyas:
            continue
        subs = SUBGRUPOS.get(enfoque, [])
        items_html = []
        if len(subs) > 1:
            for sub_id, sub_titulo, _, _, _ in subs:
                de_sub = [f for f in suyas if info_organizacion(f["archivo"])["subgrupo"] == sub_id]
                if not de_sub:
                    continue
                corto = PROC_POR_ID[sub_id]["corto"] if sub_id in PROC_POR_ID else sub_titulo.split("·")[-1].strip()
                items_html.append('<li class="ih-sub">%s</li>' % _h.escape(corto))
                for f in de_sub:
                    items_html.append(
                        '<li><a href="%s"%s>%s</a></li>' % (
                            f["archivo"],
                            ' class="actual" aria-current="page"' if f["archivo"] == actual else "",
                            _h.escape(f["titulo"]),
                        )
                    )
        else:
            for f in suyas:
                items_html.append(
                    '<li><a href="%s"%s>%s</a></li>' % (
                        f["archivo"],
                        ' class="actual" aria-current="page"' if f["archivo"] == actual else "",
                        _h.escape(f["titulo"]),
                    )
                )
        grupos.append('<div class="ih-g"><b>%s</b><ul>%s</ul></div>' % (_h.escape(enfoque), "".join(items_html)))
    return (
        INICIO + "\n<style>" + INDICE_CSS + "</style>\n"
        '<button type="button" class="ih-boton" id="ih-boton">&#9776; Hojas</button>\n'
        '<nav class="ih-panel" aria-label="Índice de hojas">'
        '<button type="button" class="ih-cerrar" id="ih-cerrar">Cerrar &times;</button>'
        '<a class="ih-top" href="index.html">&larr; Todas las hojas</a>'
        '<a class="ih-top" href="guia.html">Guía rápida de uso</a>'
        + "".join(grupos) + '</nav>\n<div class="ih-velo" id="ih-velo" hidden></div>\n'
        "<script>" + INDICE_JS + "</script>\n" + FIN
    )


def inyectar_indice(ruta, fichas):
    """Pone (o rehace) el índice de hojas en una herramienta ya construida."""
    import re as _re
    d = ruta.read_text(encoding="utf-8")
    bloque = indice_hojas(fichas, ruta.name)
    if INICIO in d:
        d = _re.sub(_re.escape(INICIO) + ".*?" + _re.escape(FIN), lambda m: bloque, d, flags=_re.S)
    else:
        i = d.rindex("</body>")
        d = d[:i] + bloque + "\n" + d[i:]
    ruta.write_text(d, encoding="utf-8")
