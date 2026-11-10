# -*- coding: utf-8 -*-
"""
Correcciones de redacción de la guía (`guia.py`) y los guiones (`guiones.py`) tras el rework de
escenas de noviembre de 2026: frases que describían controles que ya no existen (deslizadores,
tarjetas, botones con otro nombre). Se aplican al importar esos módulos, sobre las cadenas ya
cargadas, porque los literales están partidos en varios renglones.

Cada entrada: (archivo, fragmento viejo, fragmento nuevo). Si un fragmento ya no aparece, se avisa
por consola en vez de fallar: significa que alguien editó el texto de origen y esta entrada sobra.
"""
REEMPLAZOS = [
 ("met-invitado-incomodo.html",
  "Alternar entre «Cerrar la puerta y vigilar» y «Permitir que entre y volver a mi fiesta» para ver qué pasa con el anfitrión.",
  "Dejar que el visitante golpee solo y probar «Ir a trancar la puerta» y «Volver a la mesa aunque toque» para ver qué pasa con el anfitrión y con la fiesta."),
 ("met-invitado-incomodo.html",
  "Compare ambos botones de la hoja para ver cómo vigilar la puerta deja al anfitrión fuera de su propia fiesta.",
  "Pruebe en la escena «Ir a trancar la puerta»: el anfitrión queda empujando de espaldas a su mesa y la sala se enfría."),
 ("met-arenas-movedizas.html", "Cambie a «Extender el cuerpo y flotar»:",
  "Suelte el botón de patalear y toque «Tenderse y abrir los brazos»:"),
 ("act-pasear-la-mente.html",
  "Use los botones de charla rápida o escriba la frase exacta en el globo de voz de la mente.",
  "Marque en las fichas lo que suele comentar su mente, o agréguelo con el «+»: saldrá en los globos de la nube."),
 ("act-pasear-la-mente.html", "Complete el recuadro de la derecha:",
  "Elija arriba hacia dónde van hoy sus pies y deje correr la escena:"),
 ("act-dial-disposicion.html", "«Imagine dos perillas de 0 a 10.", "«Imagine dos perillas en un radio viejo."),
 ("act-dial-disposicion.html",
  "Mueva ambos deslizadores para observar cómo cambia el mensaje clínico según la combinación.",
  "Mantenga apretado «Forzar la del malestar» y suéltelo: la perilla rebota más alto y la música se corta. Luego gire la de la disposición y note que la música suena con la otra donde esté."),
 ("met-la-casa-y-los-muebles.html",
  "Complete las tres casillas dentro del plano de la casa para ampliar el campo de atención.",
  "Escriba los tres muebles arriba y mírelos aparecer en la casa; pruebe «Sacar el mueble a empujones» y vea cómo vuelve solo a su rincón."),
 ("met-trampa-china.html",
  "Mover el deslizador de tensión para contrastar el reflejo de escapar con el gesto de empujar suavemente hacia adentro.",
  "Mantener apretado «Tirar hacia afuera» y luego tocar «Acercar los dedos» para contrastar el reflejo de escapar con el gesto de empujar suavemente hacia adentro."),
 ("met-trampa-china.html",
  "Mueva el deslizador hacia la derecha para visualizar cómo el intento de escapar reduce el espacio vital.",
  "Mantenga apretado «Tirar hacia afuera» para ver cómo el intento de escapar alarga y cierra el tubo sobre los dedos."),
 ("met-trampa-china.html", "Deslice ahora el control hacia la izquierda.", "Toque ahora «Acercar los dedos», una vez y otra."),
 ("act-pero-por-y.html",
  "Escriba ambos lados en la tarjeta y observe el efecto de bloqueo con el interruptor en «PERO».",
  "Elija arriba las dos mitades de la frase y observe la escena con «PERO»: el portón está cerrado y la tarde cae mientras ella espera."),
 ("act-pero-por-y.html", "Conmute el botón hacia «Y»", "Toque «Cambiar \"pero\" por \"y\"»"),
 ("act-hecho-o-juicio.html",
  "Resolver juntos las cinco tarjetas de entrenamiento distinguiendo hecho observable de juicio valorativo.",
  "Recibir juntos las frases que llegan a la escena y decidir, una por una, si las vería la cámara o las pone la mente."),
 ("act-hecho-o-juicio.html", "Tomar la frase autocrítica actual y dividirla en dos columnas:",
  "Tomar la frase autocrítica actual y separarla en dos partes:"),
 ("act-hecho-o-juicio.html",
  "Complete las cinco tarjetas interactivas comentando por qué cada una es hecho o evaluación.",
  "Deje llegar las frases a la escena y comente cada una antes de tocar «Lo vería la cámara» o «Lo pone la mente»; la que nadie atiende se pega sola a la taza."),
 ("act-hecho-o-juicio.html", "sepárenla juntos en las dos columnas:", "sepárenla juntos en los dos campos:"),
 ("act-piloto-automatico.html",
  "Recorra y marque las cinco casillas sensoriales preparando el ensayo concreto:",
  "Escriba los tres detalles sensoriales y ensaye en la escena: cuando la bruma tape la cocina, vuelva tocando uno de los tres sentidos. Prepare así el ensayo concreto:"),
 ("act-observador-en-el-tiempo.html", "invite a recorrer las tres tarjetas:", "invite a recorrer las tres escenas:"),
 ("act-diana-de-valores.html",
  "Mover los cuatro deslizadores para ver en tiempo real dónde caen los dardos sobre la diana.",
  "Clavar los cuatro dardos tocando la diana, uno por cuadrante."),
 ("act-diana-de-valores.html", "«Al mover los deslizadores y ver sus cuatro dardos en la diana,", "«Al clavar sus cuatro dardos en la diana,"),
 ("act-punto-dulce.html", "Toque los botones de cualidades", "Marque las fichas de cualidades"),
 ("met-el-interruptor.html", "«Mira los anillos rojos y la barra de energía de abajo.",
  "«Mira la ola roja y dentada que se montó encima de la azul."),
 ("met-el-interruptor.html", "ese ochenta por ciento de energía", "toda esa energía"),
]


def _cambiar(x, viejo, nuevo, cuenta):
    if isinstance(x, str):
        if viejo in x:
            cuenta[0] += 1
            return x.replace(viejo, nuevo)
        return x
    if isinstance(x, list):
        for i, v in enumerate(x): x[i] = _cambiar(v, viejo, nuevo, cuenta)
        return x
    if isinstance(x, tuple):
        return tuple(_cambiar(v, viejo, nuevo, cuenta) for v in x)
    if isinstance(x, dict):
        for k in list(x): x[k] = _cambiar(x[k], viejo, nuevo, cuenta)
        return x
    return x


def aplicar(por_archivo):
    """por_archivo: dict archivo -> estructura (se modifica y se devuelve). Devuelve los fragmentos hallados."""
    hallados = set()
    for archivo, viejo, nuevo in REEMPLAZOS:
        if archivo in por_archivo:
            cuenta = [0]
            por_archivo[archivo] = _cambiar(por_archivo[archivo], viejo, nuevo, cuenta)
            if cuenta[0]: hallados.add((archivo, viejo))
    return hallados
