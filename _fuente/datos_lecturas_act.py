# -*- coding: utf-8 -*-
"""
Catálogo de las 48 lecturas acompañadas y hojas de reflexión de ACT
con respaldo en literatura clínica oficial (Hayes et al., 1999/2012;
Wilson y Luciano, 2002; Hayes y Smith, 2005; Wilson y DuFrene, 2009;
Harris, 2009/2019; Lundgren et al., 2012; Polk y Schoendorff, 2014).
"""

PROCESOS = [
    {
        "id": "aceptacion",
        "nombre": "Aceptación y disposición",
        "corto": "Aceptación",
        "estilo": "abierto",
        "estilo_nombre": "Estilo abierto",
        "color": "#c26a4e",
        "suave": "#f8ece6",
        "borde": "#e5bfb0",
        "desc": "Abandonar la lucha estéril contra las emociones, recuerdos y sensaciones dolorosas para abrirles espacio y recuperar la libertad de moverse.",
    },
    {
        "id": "defusion",
        "nombre": "Defusión cognitiva",
        "corto": "Defusión",
        "estilo": "abierto",
        "estilo_nombre": "Estilo abierto",
        "color": "#b8762e",
        "suave": "#f8f0e4",
        "borde": "#e4c89e",
        "desc": "Dar un paso atrás respecto a los pensamientos, reglas e historias mentales para mirarlos como palabras e imágenes pasajeras y no como órdenes absolutas.",
    },
    {
        "id": "presente",
        "nombre": "Contacto con el momento presente",
        "corto": "Momento presente",
        "estilo": "centrado",
        "estilo_nombre": "Estilo centrado",
        "color": "#3f83a6",
        "suave": "#eaf2f7",
        "borde": "#b3cfe0",
        "desc": "Traer la atención de manera flexible y curiosa a la experiencia física y sensorial del aquí y ahora, saliendo del piloto automático.",
    },
    {
        "id": "yo",
        "nombre": "Yo como contexto",
        "corto": "Yo como contexto",
        "estilo": "centrado",
        "estilo_nombre": "Estilo centrado",
        "color": "#5f77b8",
        "suave": "#eceff8",
        "borde": "#bbc5e5",
        "desc": "Contactar con el espacio consciente («yo, aquí, ahora») que observa y alberga todos los pensamientos y emociones sin quedar reducido a ninguno de ellos.",
    },
    {
        "id": "valores",
        "nombre": "Clarificación de valores",
        "corto": "Valores",
        "estilo": "comprometido",
        "estilo_nombre": "Estilo comprometido",
        "color": "#3f9b86",
        "suave": "#eaf6f2",
        "borde": "#b0d9ce",
        "desc": "Elegir libremente las cualidades de acción y las direcciones vitales que dan sentido, sabor y dignidad a la propia existencia.",
    },
    {
        "id": "accion",
        "nombre": "Acción comprometida",
        "corto": "Acción comprometida",
        "estilo": "comprometido",
        "estilo_nombre": "Estilo comprometido",
        "color": "#2d7a5e",
        "suave": "#e6f4ef",
        "borde": "#a3d1c0",
        "desc": "Construir patrones de conducta sostenibles, paso a paso, guiados por los valores elegidos y llevando en la mochila el malestar que aparezca en el camino.",
    },
]

LECTURAS = [
    # ==================== 1. ACEPTACIÓN (12) ====================
    {
        "slug": "el-hoyo-y-la-pala",
        "titulo": "La persona en el hoyo: soltar la pala",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-el-hoyo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 4: The Person in the Hole). Guilford Press.",
        "resumen": "Comprender por qué las estrategias lógicas para quitarse el dolor suelen hacer el hoyo más hondo, y por qué el primer paso es dejar de cavar.",
        "lectura": [
            "Imagina que te ponen una venda en los ojos, te entregan una bolsa con herramientas y te dejan en un campo abierto con la instrucción de recorrerlo. Sin saberlo, en ese terreno hay pozos profundos. Caminas como mejor sabes y, de pronto, caes dentro de un hoyo bastante hondo.",
            "Haces entonces lo más razonable que haría cualquiera: abres tu bolsa de herramientas para salir de ahí. Sacas lo que hay adentro y encuentras una pala. Así que empiezas a cavar con disciplina, con esfuerzo, por la derecha, por la izquierda, con paladas rápidas y con paladas lentas.",
            "Sin embargo, por más que te esfuerzas, notas algo desconcertante: el hoyo no se achica, sino que cada mes es más profundo y oscuro. Tal vez pienses que necesitas una pala de oro, o un manual de excavación más moderno. Pero la primera ley de los hoyos es muy sencilla: por más perfecta que sea tu técnica, una pala solo sirve para hacer el hoyo más grande. Antes de poder usar una escalera, primero hace falta abrir la mano y soltar la pala."
        ],
        "clave": "El problema no es que te haya faltado esfuerzo; es que las herramientas para «no sentir» funcionan como una pala dentro de un pozo.",
        "preguntas": [
            "¿Cuáles han sido tus «palas» favoritas para intentar no sentir ansiedad, tristeza o incertidumbre?",
            "En el corto plazo cavar parece aliviar un instante, pero a largo plazo: ¿te ha sacado del hoyo o ha vuelto tu vida más estrecha?",
            "¿Cómo sería hoy detener la mano un momento y mirar el hoyo sin dar una palada más?"
        ],
        "practica": "Hoy, cada vez que notes el impulso urgente de «arreglar» o apagar una emoción incómoda, nombra en silencio: «Estoy agarrando la pala» y suelta los hombros durante tres respiraciones."
    },
    {
        "slug": "costo-de-la-lucha",
        "titulo": "El balance de la lucha: qué te ha costado no sentir",
        "proceso": "aceptacion",
        "tipo": "Hoja de reflexión",
        "tiempo": "5 min",
        "herramienta": "act-costo-de-la-lucha.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (2012). Terapia de Aceptación y Compromiso (2.ª ed., Desesperanza creativa). Desclée De Brouwer.",
        "resumen": "Revisar con honestidad y sin culpa si la agenda de control emocional ha cumplido su promesa o si se ha cobrado pedazos valiosos de la vida.",
        "lectura": [
            "Desde pequeños aprendemos una regla que funciona de maravilla en el mundo exterior: «Si algo te incomoda, identifícalo, combátelo y elimínalo». Si tienes frío, te pones un abrigo; si una silla tiene un clavo, lo sacas. Es completamente comprensible que apliques esa misma regla a tu mundo interior.",
            "Bajo esa lógica, nos prometemos que cuando por fin logremos eliminar la inseguridad, los recuerdos dolorosos o el miedo, entonces sí empezaremos a vivir de lleno. Y ponemos en marcha decenas de estrategias: posponer, analizar mil veces, distraernos, aislarnos, buscar garantías o exigirnos perfección.",
            "Pero vale la pena hacer una pausa y consultar no lo que dice la teoría, sino lo que muestra tu propia experiencia: después de meses o años de aplicar ese plan, ¿el malestar desapareció para siempre o sigue volviendo? Y mientras tanto, ¿cuánta vitalidad, cuántos encuentros y cuántos proyectos quedaron en sala de espera?"
        ],
        "clave": "No eres tú quien está roto; es el plan de «primero dejar de sentir para después empezar a vivir» el que no funciona.",
        "preguntas": [
            "¿Qué emociones, pensamientos o recuerdos has intentado mantener a raya con más fuerza en el último año?",
            "¿Qué actividades, conversaciones o vínculos importantes has ido dejando de lado para evitar encontrarte con ese malestar?",
            "Si pudieras recuperar toda la energía que hoy gastas en esa pelea interna, ¿en qué área de tu vida te gustaría invertirla?"
        ],
        "practica": "Haz una lista breve de tres cosas valiosas que has pospuesto «hasta sentirte mejor» y elige una versión pequeña de una de ellas para realizar hoy con lo que sientes."
    },
    {
        "slug": "el-poligrafo",
        "titulo": "La trampa del polígrafo: cuando prohibirte sentir dispara la alarma",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "met-el-poligrafo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Polygraph Metaphor). Guilford Press.",
        "resumen": "Observar por qué exigirnos estar calmados a toda costa multiplica instantáneamente la activación que queríamos evitar.",
        "lectura": [
            "Imagina que te conectan al detector de mentiras más sensible del mundo. Tiene cables en tu pecho, en tus dedos y en tu frente para medir cada latido y cada gota de sudor. Entonces te dan una tarea sencilla: «Tu única misión durante los próximos cinco minutos es mantenerte cien por ciento relajado».",
            "Para asegurarte de que te esfuerces de verdad, añaden una condición: «Si la aguja detecta el más mínimo chispazo de nerviosismo o ansiedad, recibirás una descarga terrible». ¿Qué crees que pasaría en tu cuerpo medio segundo después de escuchar esa orden?",
            "En cuanto notas el primer latido rápido, te asustas de estar poniéndote nervioso, y ese susto hace saltar la aguja al máximo. Nuestro sistema nervioso no tiene un botón de apagado voluntario: cuando tratamos a nuestras propias emociones como una amenaza que no puede ocurrir bajo ningún concepto, encendemos la alarma por el hecho mismo de sentir la alarma."
        ],
        "clave": "En el mundo emocional, vigilar con miedo si ya nos calmamos es el combustible más rápido para encender la ansiedad.",
        "preguntas": [
            "¿En qué situaciones de tu vida te pones un «polígrafo» encima exigiéndote que no se te note ni una gota de nervios o tristeza?",
            "¿Qué pasa con tu cuerpo cuando te dices: «No puedo ponerme ansioso ahora mismo»?",
            "¿Qué cambiaría si tuvieras permiso total para que la aguja se mueva todo lo que quiera mientras tú haces lo tuyo?"
        ],
        "practica": "La próxima vez que notes activación física, di para tus adentros: «Está permitido que mi corazón lata rápido ahora mismo; no necesito pasar ningún examen de calma»."
    },
    {
        "slug": "soltar-la-cuerda",
        "titulo": "Tirar de la cuerda con el monstruo",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-la-cuerda.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Tug-of-War with a Monster). Guilford Press.",
        "resumen": "Descubrir que ganar la guerra contra el monstruo del malestar no es jalar más fuerte hasta tumbarlo, sino soltar la cuerda para liberar las manos.",
        "lectura": [
            "Imagina que estás en una competencia de tirar de la cuerda frente a un monstruo enorme: el monstruo de tu ansiedad, de tu tristeza o de tus dudas más oscuras. Entre él y tú hay un abismo sin fondo, y tú sientes que si aflojas un solo centímetro te arrastrará al vacío.",
            "Así que clavas los talones, aprietas los dientes y tiras con todas tus fuerzas. Pero hay una ley extraña en este juego: cuanto más fuerte jalas tú hacia atrás, más grande se vuelve el monstruo y más tensa queda la soga. Tienes las dos manos quemadas por la cuerda, la vista clavada en él y los pies inmóviles al borde del barranco.",
            "Soltar la cuerda no hace que el monstruo desaparezca por arte de magia: él sigue del otro lado haciendo ruido y mostrando los dientes. Pero si no tienes la soga en las manos, por más que él tire ya no puede arrastrarte al precipicio, y tus manos y tus pies quedan libres para girar hacia tu vida."
        ],
        "clave": "No necesitas vencer al monstruo para recuperar tu vida; solo necesitas dejar de sujetar el otro extremo de la soga.",
        "preguntas": [
            "¿Cómo se ve hoy el «monstruo» con el que has estado tirando de la cuerda y qué te grita para que sigas jalando?",
            "Mientras tienes las dos manos ocupadas sujetando la soga, ¿qué cosas importantes no puedes abrazar ni construir?",
            "¿Cómo se siente en tus brazos y en tu pecho imaginar que hoy dejas caer la soga al suelo?"
        ],
        "practica": "Haz el gesto físico real de apretar los puños durante cinco segundos notando la tensión en los antebrazos y, al exhalar, abre las palmas por completo dejándolas caer sobre tus piernas."
    },
    {
        "slug": "empujar-el-papel",
        "titulo": "Empujar el papel con los brazos tensos o apoyarlo en el regazo",
        "proceso": "aceptacion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-empujar-el-papel.html",
        "fuente": "Harris, R. (2009). ACT Made Simple: An Easy-to-Read Primer on Acceptance and Commitment Therapy. New Harbinger.",
        "resumen": "Sentir en los propios músculos la diferencia entre mantener un pensamiento doloroso lejos a fuerza de brazos y dejarlo descansar en el regazo.",
        "lectura": [
            "Toma una hoja de papel o una libreta e imagina que en ella están escritos los pensamientos, recuerdos y sensaciones que más te incomodan hoy. Ahora sujétala con ambas manos y estira los brazos todo lo que puedas para mantenerla lo más lejos posible de tu pecho, empujando con fuerza hacia afuera.",
            "Al principio parece una buena solución: el papel está lejos de ti. Pero ¿qué pasaría si tuvieras que sostener esa postura durante una hora, o durante todo el día? Tus hombros empezarían a temblar de fatiga, no podrías usar las manos para cocinar, escribir ni saludar a nadie, y toda tu atención estaría absorbida por sostener el papel lejos.",
            "Ahora baja los brazos despacio y deja que la hoja descanse suavemente sobre tu regazo. Fíjate en la paradoja: físicamente el papel está hoy más cerca de tu cuerpo que hace un momento, pero tus hombros están sueltos, tu vista está despejada y tus manos han vuelto a ser tuyas."
        ],
        "clave": "Dejar que el malestar descanse en tu regazo lo acerca físicamente, pero te devuelve al instante tus brazos, tu energía y tu horizonte.",
        "preguntas": [
            "¿Qué pensamiento o emoción has estado manteniendo «con los brazos estirados» lejos de ti últimamente?",
            "¿Dónde notas en tu cuerpo el cansancio acumulado de estar empujando esa experiencia todo el día?",
            "¿Qué te permite hacer hoy con tus manos el gesto de bajar esa hoja al regazo?"
        ],
        "practica": "Si tienes esta hoja impresa o una libreta cerca, sostenlo treinta segundos con los brazos tensos frente a ti y luego apóyalo en tus piernas notando el alivio muscular."
    },
    {
        "slug": "limpio-y-sucio",
        "titulo": "Malestar limpio y malestar sucio: el interruptor de la lucha",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-el-interruptor.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Clean vs. Dirty Discomfort). · Harris, R. (2009). The Struggle Switch.",
        "resumen": "Distinguir el dolor natural de estar vivos (malestar limpio) del sufrimiento extra que fabricamos al enojarnos o asustarnos por sentirlo (malestar sucio).",
        "lectura": [
            "En la vida humana existe un dolor que ningún ser vivo puede esquivar: la tristeza cuando algo valioso se pierde, el miedo cuando nos importa el resultado, la decepción cuando algo falla. En ACT llamamos a eso «malestar limpio»: sube y baja como las olas del mar, duele de verdad, pero no está estancado.",
            "El problema empieza cuando en el fondo de nuestra mente salta encendido el «interruptor de la lucha». Apenas aparece la tristeza, nos decimos: «No debería seguir triste, soy débil». Apenas aparece la ansiedad, nos enojamos con nosotros mismos por sentirla, o nos da pánico que nos dé pánico.",
            "De pronto, encima del dolor original tenemos rabia por estar tristes, vergüenza por tener miedo y culpa por estar agotados. Ese segundo piso de pelea es el «malestar sucio». No podemos elegir no sentir el primer oleaje de la vida, pero sí podemos bajar el interruptor que nos castiga por sentirlo."
        ],
        "clave": "El dolor limpio viene incluido con el hecho de amar y vivir; el sufrimiento sucio se enciende cuando nos peleamos con nuestra propia emoción.",
        "preguntas": [
            "En lo que estás atravesando hoy, ¿cuál es la emoción primaria o «malestar limpio» que apareció naturalmente?",
            "¿Qué segunda capa de reproches, rabia o susto («malestar sucio») se enciende encima cuando no aceptas sentir eso?",
            "Si hoy bajas el interruptor de la lucha y dejas únicamente la emoción limpia, ¿cuánto peso extra se quita de tus hombros?"
        ],
        "practica": "Cuando aparezca una emoción difícil hoy, pon una mano en el pecho y di: «Esto es dolor limpio de estar vivo; elijo no sumarle pelea encima»."
    },
    {
        "slug": "dos-caras-moneda",
        "titulo": "Las dos caras de la misma moneda: por qué duele donde importa",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-las-dos-caras.html",
        "fuente": "Wilson, K. G. y Luciano, M. C. (2002). Terapia de Aceptación y Compromiso (ACT): Un tratamiento conductual orientado a los valores. Pirámide.",
        "resumen": "Reconocer que el dolor psicológico y los valores más profundos son el anverso y el reverso indivisibles de una misma moneda.",
        "lectura": [
            "Toma una moneda en tu mano y mírala con detenimiento. En una cara está grabado aquello que hoy más te duele: el miedo a fallar, la tristeza de una pérdida, el temor al rechazo o la preocupación por los tuyos. Es comprensible que quieras cortar o tirar a la basura esa mitad de la moneda.",
            "Pero ahora dale la vuelta. En el reverso exacto de ese dolor encontrarás siempre algo que amas profundamente. Solo nos duele perder aquello que nos importa cuidar; solo nos da miedo equivocarnos en aquello que valoramos hacer bien; solo nos hiere la distancia donde anhelamos cercanía.",
            "Nadie puede partir una moneda por el espesor para quedarse únicamente con la cara del amor y tirar la cara de la vulnerabilidad. Si tiras la moneda para no volver a sentir dolor, tiras también lo que da sentido a tu vida. Abrir la palma para llevar la moneda entera es el acto más valiente de aceptación."
        ],
        "clave": "Allí donde hay un dolor vivo, dale la vuelta a la moneda: en el reverso encontrarás intacto lo que más te importa en la vida.",
        "preguntas": [
            "¿Qué dolor, temor o herida está grabado hoy en la cara visible de tu moneda?",
            "Si le das la vuelta con cuidado, ¿qué valor, qué amor o qué anhelo profundo vive en el otro lado de esa misma moneda?",
            "¿Estás dispuesto a llevar contigo la moneda completa (el valor junto con la vulnerabilidad) para no renunciar a lo que amas?"
        ],
        "practica": "Escribe en una tarjeta pequeña: «Me duele [X] porque me importa profundamente [Y]» y consérvala a la vista esta semana."
    },
    {
        "slug": "trampa-china",
        "titulo": "La trampa china de dedos: acercarse para aflojar",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "met-trampa-china.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 3: Chinese Finger Trap Metaphor). Guilford Press.",
        "resumen": "Comprobar cómo el impulso instintivo de tirar hacia afuera para escapar del malestar cierra más el tejido, mientras que inclinarse hacia adentro abre espacio.",
        "lectura": [
            "¿Has visto alguna vez esos pequeños cilindros tejidos de bambú llamados trampas chinas para dedos? Metes un dedo índice por cada extremo y, cuando intentas sacarlos tirando hacia afuera, el trenzado de bambú se estira, se estrecha y atrapa tus dedos como una prensa.",
            "Cuanto más desesperado tiras hacia afuera para liberarte, más implacable se vuelve el apriete. La lógica común te grita: «¡Tienes que jalar con más fuerza!». Pero el diseño mismo del tubo convierte tu fuerza de escape en la fuerza que te aprisiona.",
            "La única manera de recuperar la holgura es hacer un movimiento que parece contrario al sentido común: dejar de tirar hacia afuera y acercar suavemente ambos dedos hacia el centro del cilindro. En cuanto te inclinas un milímetro hacia adentro, las fibras de bambú se ensanchan y tus dedos vuelven a tener espacio para moverse."
        ],
        "clave": "Tirar con urgencia para escapar de lo que sientes estrecha el tubo; acercarte con suavidad a tu experiencia afloja las fibras.",
        "preguntas": [
            "¿De qué maneras has estado «tirando hacia afuera» con urgencia para zafarte de una sensación incómoda?",
            "¿Has notado cómo ese tirón hace que el problema ocupe cada vez más espacio en tu cabeza?",
            "¿Qué significaría hoy acercarte un milímetro con curiosidad y suavidad hacia esa sensación en lugar de jalar?"
        ],
        "practica": "Ante una sensación física incómoda hoy, en vez de contraerte para echarla, inhala imaginando que te inclinas suavemente hacia ella para darle espacio."
    },
    {
        "slug": "invitado-incomodo",
        "titulo": "El invitado incómodo en la fiesta",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-invitado-incomodo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Joe the Bum Metaphor). Guilford Press.",
        "resumen": "Ver el costo de abandonar nuestra propia fiesta valiosa por quedarnos toda la noche en la puerta forcejeando con un visitante molesto.",
        "lectura": [
            "Imagina que organizas una fiesta muy especial en tu casa e invitas a todas las personas del vecindario. La música suena, la comida está servida y están ahí quienes más quieres. Pero de pronto toca el timbre aquel vecino ruidoso, maloliente y pesado que a nadie le cae bien.",
            "Molesto, decides que no puedes permitirle pasar: corres a la entrada, le cierras la puerta en la cara y apoyas la espalda contra la madera para que no se cuele. El problema es que él sigue empujando desde afuera. Y mientras tú pasas horas enteras sudando en el pasillo custodiando el picaporte, la fiesta ocurre en la sala sin ti.",
            "¿Qué pasa si sueltas el cerrojo y le dices: «Está bien, pasa si quieres, aunque no me gusten tus modales»? Él entrará, dirá alguna tontería y comerá algo del bufé, pero tú habrás recuperado tu fiesta, tu música y tus conversaciones con quienes de verdad te importan."
        ],
        "clave": "No hace falta que te guste el invitado incómodo; solo hace falta que dejes de perderte tu propia fiesta por vigilarle la puerta.",
        "preguntas": [
            "¿Cuál es la «fiesta» (los vínculos, proyectos o momentos valiosos) que hoy quieres disfrutar en tu vida?",
            "¿Cómo se llama el «invitado incómodo» (miedo, duda, desgano, recuerdo) por el que a veces te quedas trancando la puerta?",
            "Si hoy le permites estar en un rincón de la sala sin discutir con él, ¿a qué parte de tu fiesta puedes regresar ahora mismo?"
        ],
        "practica": "Hoy, cuando aparezca ese pensamiento o emoción molesta, dile mentalmente: «Puedes quedarte cerca del bufé si quieres; yo vuelvo a mi reunión»."
    },
    {
        "slug": "arenas-movedizas",
        "titulo": "Flotar en las arenas movedizas",
        "proceso": "aceptacion",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "met-arenas-movedizas.html",
        "fuente": "Hayes, S. C. y Smith, S. (2005). Sal de tu mente, entra en tu vida (Cap. 2: Arenas movedizas). Desclée De Brouwer.",
        "resumen": "Sustituir el pataleo desesperado que nos hunde en el pánico o la tristeza por el gesto de extender el cuerpo y entrar en contacto amplio con el presente.",
        "lectura": [
            "Si alguna vez cayeras en arenas movedizas, todo tu instinto de supervivencia te gritaría una sola orden: «¡Patalea y saca una pierna ya mismo!». Pero al levantar un pie con desesperación, todo el peso de tu cuerpo se concentra sobre el otro pie, creando un vacío que te succiona al doble de velocidad.",
            "Con el pánico, el insomnio o la angustia intensa ocurre exactamente la misma física: cuanto más pataleamos revisando si ya se nos quitó, peleando con el reloj o forzando la mente, más rápido nos hundimos en la agitación.",
            "Los rescatistas enseñan que para salir de las arenas movedizas hay que hacer lo opuesto a patalear: soltar la lucha, abrir los brazos en cruz y recostarse de espaldas sobre el lodo. Al poner más superficie de tu cuerpo en contacto con la arena —no menos—, el cuerpo deja de hundirse y empieza a flotar."
        ],
        "clave": "En las arenas movedizas del malestar, patalear hunde; extender los brazos y tocar con amplitud la experiencia presente te permite flotar.",
        "preguntas": [
            "Cuando llega una oleada fuerte de ansiedad o desánimo, ¿cuál es tu forma automática de «patalear»?",
            "¿Qué le pasa a tu nivel de agotamiento cuando llevas una hora pataleando contra lo que sientes?",
            "¿Cómo sería hoy «extender los brazos y flotar de espaldas» con esa sensación durante cinco minutos sin exigirle que desaparezca?"
        ],
        "practica": "Si hoy sientes urgencia interna, descruza los brazos y las piernas, abre las palmas y respira lento sintiendo todo el respaldo de la silla sosteniéndote."
    },
    {
        "slug": "hacer-espacio",
        "titulo": "Respirar hacia adentro y hacer espacio (Expansión)",
        "proceso": "aceptacion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "4 min",
        "herramienta": "act-empujar-el-papel.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Cap. 8: Expansion — Observe, Breathe, Allow). New Harbinger.",
        "resumen": "Practicar los cuatro pasos de la expansión corporal (observar, respirar, abrir espacio y permitir) ante un nudo emocional presente.",
        "lectura": [
            "Las emociones no son enemigos abstractos flotando en el aire; en el fondo, son oleadas de sensaciones físicas en el cuerpo: calor en la cara, presión en el esternón, un nudo en la garganta o vacío en el estómago. Cuando las rechazamos, nuestros músculos se contraen alrededor de ellas como un puño cerrado.",
            "La práctica de hacer espacio recorre cuatro pasos sencillos. Primero, observa tu cuerpo con la curiosidad de un científico amable y ubica dónde se siente con más claridad la emoción hoy: ¿qué forma, tamaño o temperatura tendría si pudieras dibujarla?",
            "Segundo, respira despacio imaginando que el aire entra directamente hacia esa zona y circula a su alrededor. Tercero, al exhalar, imagina que tu pecho o tu abdomen se ensanchan como si abrieran una habitación más amplia alrededor de la sensación. Cuarto, permítele estar ahí sin pedirle que se vaya ni que te guste: simplemente déjala ser mientras tú sigues siendo mucho más grande que ella."
        ],
        "clave": "No respiramos para expulsar la sensación del cuerpo, sino para aflojar el puño que la apretaba y abrirle espacio alrededor.",
        "preguntas": [
            "Si recorres tu cuerpo ahora mismo, ¿en qué lugar exacto (pecho, garganta, estómago, hombros) notas la emoción de hoy?",
            "Si esa sensación tuviera una forma, un peso o una temperatura, ¿cómo la describirías sin juzgarla?",
            "Al imaginar que tu cuerpo se ensancha un poco alrededor de ella al respirar, ¿qué cambia en tu relación con esa sensación?"
        ],
        "practica": "Dedica dos minutos hoy a apoyar una mano tibia sobre la zona del cuerpo donde sientas tensión, respirando hacia esa mano como gesto de permiso y cuidado."
    },
    {
        "slug": "soltar-el-ancla",
        "titulo": "Echar el ancla en medio de la tormenta emocional (ACE)",
        "proceso": "aceptacion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-echar-el-ancla.html",
        "fuente": "Harris, R. (2019). ACT Made Simple (2.ª ed., Dropping Anchor: Acknowledge, Come back into your body, Engage). New Harbinger.",
        "resumen": "Usar la secuencia ACE para sujetar el barco al fondo firme durante una tormenta emocional sin pretender que el mar se calme de golpe.",
        "lectura": [
            "Cuando una tormenta repentina sorprende a un barco cerca de los arrecifes, el capitán sabe que ningún ancla del mundo tiene el poder de apagar el viento ni de planchar las olas. La función del ancla es otra muy distinta: sujetar el casco al fondo firme para que las olas no estrellen el barco contra las rocas mientras pasa el temporal.",
            "Puedes echar el ancla en treinta segundos siguiendo tres letras: A, C, E. La «A» es Reconocer (Acknowledge): nota en silencio y sin pelearte qué pensamientos, recuerdos o emociones están agitándose dentro de ti ahora mismo.",
            "La «C» es Conectar con el cuerpo (Come back into your body): presiona suavemente las plantas de los pies contra el suelo, estira la espalda y mueve despacio los dedos de las manos para sentir que tú tienes el timón físico. Y la «E» es Involucrarte en el entorno (Engage): mira a tu alrededor, identifica cinco objetos de la habitación y vuelve de lleno a la tarea o conversación que tienes delante."
        ],
        "clave": "El ancla no se lanza para apagar la tormenta, sino para mantenerte firme y al mando mientras el oleaje pasa.",
        "preguntas": [
            "A — Reconocer: ¿Qué pensamientos o emociones están soplando con fuerza dentro de tu barco hoy?",
            "C — Cuerpo: Al apoyar con firmeza ambos pies en el piso y enderezar la espalda, ¿notas que sigues teniendo mando sobre tu cuerpo?",
            "E — Entorno: ¿En qué actividad concreta de este momento eliges involucrar tu atención ahora mismo?"
        ],
        "practica": "Practica un ciclo corto de 30 segundos de A-C-E tres veces al día (incluso cuando el mar esté tranquilo) para que el ancla esté lista cuando llegue el oleaje."
    },

    # ==================== 2. DEFUSIÓN COGNITIVA (12) ====================
    {
        "slug": "soltar-el-anzuelo",
        "titulo": "Los anzuelos de la mente: cuándo muerdes y cuándo nadas libre",
        "proceso": "defusion",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "act-soltar-el-anzuelo.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Hooks Metaphor). New Harbinger.",
        "resumen": "Ver los pensamientos difíciles como anzuelos con carnada que caen al agua: no podemos impedir que caigan, pero sí dejar de morderlos.",
        "lectura": [
            "Imagina que nadas por un río cristalino y que desde la orilla caen al agua decenas de anzuelos brillantes con carnada: «¿Y si todo sale mal?», «No eres suficiente», «Deberían tratarte distinto», «No vas a poder con esto». Tú no lanzaste esos anzuelos al agua; tu mente los arroja de manera automática todo el día.",
            "Mientras el anzuelo flota cerca de ti y tú simplemente lo ves brillar en el agua, eres completamente libre de nadar hacia donde quieras. El problema ocurre en el instante en que muerdes la carnada: de pronto el hilo se tensa y empiezas a ser arrastrado lejos de lo que estabas haciendo, dando vueltas en círculos de angustia o enojo.",
            "Desengancharte no consiste en romper la caña de pescar ni en secar el río para que nunca más caiga un anzuelo. Consiste en notar el tirón en la boca, reconocer: «Acabo de picar con el anzuelo de siempre», soltarlo con suavidad y volver a nadar hacia tu orilla valiosa."
        ],
        "clave": "Que un anzuelo caiga frente a tus ojos no te quita la libertad; lo único que te arrastra es morder la carnada.",
        "preguntas": [
            "¿Cuáles son los dos o tres «anzuelos con carnada» más frecuentes que tu mente lanza al agua esta semana?",
            "Cuando muerdes uno de esos anzuelos, ¿cómo se nota en tu conducta (te aíslas, discutes, postergas, das vueltas en la cama)?",
            "¿Qué gesto o frase breve te ayuda a escupir el anzuelo en cuanto notas el tirón?"
        ],
        "practica": "Cada vez que te descubras rumiando hoy, di en voz baja: «Acabo de morder un anzuelo», mira un punto fijo de la habitación y retoma lo que estabas haciendo."
    },
    {
        "slug": "palabra-repetida",
        "titulo": "Leche, leche, leche: cuando las palabras vuelven a ser sonido",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "met-la-palabra-repetida.html",
        "fuente": "Titchener, E. B. (1916). A Beginner's Psychology. · Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Milk, Milk, Milk Exercise).",
        "resumen": "Comprobar experimentalmente que las palabras que tanto nos asustan no son las cosas mismas, sino ruidos y sílabas construidos por la mente.",
        "lectura": [
            "Si ahora mismo piensas en la palabra «limón» o en la palabra «leche», tu mente hace un truco asombroso: aunque no haya ni una gota de leche ni medio limón en esta habitación, casi puedes ver el color blanco o sentir la acidez en la lengua. Nuestra mente funde la palabra con la cosa real como si fueran una sola pieza.",
            "Por eso, cuando tu mente pronuncia palabras duras como «fracaso», «solo» o «incapaz», tu cuerpo reacciona con el mismo sobresalto que si estuvieras frente a un precipicio físico. Creemos estar tocando una verdad sólida, cuando en realidad estamos escuchando una cadena de sílabas.",
            "En 1916, Titchener demostró qué ocurre cuando repites en voz alta y muy rápido la palabra «leche, leche, leche» durante treinta segundos seguidos: de pronto el líquido blanco desaparece y solo queda un sonido curioso chocando entre la lengua y el paladar. Las palabras nunca fueron la realidad; solo son vehículos de sonido."
        ],
        "clave": "Una palabra puede hacerte salivar o temblar como si fuera real, pero al mirarla de cerca descubres que solo son sílabas y aire.",
        "preguntas": [
            "¿Qué palabra única o etiqueta corta («fracaso», «culpable», «raro», «inútil») tiene hoy el poder de encogerte el estómago apenas suena?",
            "Cuando tu mente pronuncia esa palabra, ¿qué imágenes o sensaciones físicas trae pegadas como si fueran hechos?",
            "Al repetir primero «limón» y luego esa palabra difícil notando únicamente sus sílabas y su sonido, ¿qué cambia en su peso?"
        ],
        "practica": "Elige una etiqueta dura de una sola palabra y repítela en voz alta a buen ritmo durante 25 segundos observando cómo se desarma en puro sonido."
    },
    {
        "slug": "hojas-en-el-arroyo",
        "titulo": "Hojas flotando en el arroyo",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "5 min",
        "herramienta": "met-hojas-en-el-arroyo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Leaves on a Stream Exercise). Guilford Press.",
        "resumen": "Practicar la contemplación serena de los propios pensamientos colocándolos uno por uno sobre hojas que siguen el cauce natural del agua.",
        "lectura": [
            "Imagina que estás sentado en la orilla tranquila de un arroyo de montaña en un día templado. El agua corre a su propio ritmo frente a ti, y de los árboles caen hojas anchas que flotan suavemente río abajo hasta perderse tras la curva.",
            "Durante los próximos minutos, tu única tarea es quedarte sentado en la orilla observando qué pensamientos, imágenes o juicios aparecen en tu mente. Cada vez que surja un pensamiento —sea agradable, doloroso, aburrido o preocupante—, deposítalo con suavidad sobre una de las hojas y déjala flotar al ritmo de la corriente.",
            "No empujes la hoja para que se vaya más rápido, ni te metas al agua para retenerla. Si tu mente dice «este ejercicio es tonto» o «no lo estoy haciendo bien», coloca también ese pensamiento sobre otra hoja. Y si de pronto notas que dejaste la orilla y estás nadando dentro del pensamiento, simplemente reconócelo con amabilidad y vuelve a sentarte en el pasto de la orilla."
        ],
        "clave": "Tu lugar está en la orilla firme; los pensamientos tienen su propio cauce si no te lanzas al agua detrás de ellos.",
        "preguntas": [
            "¿Qué pensamientos aparecieron hoy que te dieron más ganas de meterte al río a empujarlos o a discutirlos?",
            "¿En qué momento notaste que habías dejado la orilla y qué te ayudó a regresar a tu puesto de observador?",
            "¿Qué diferencia sientes entre «estar dentro de la corriente de pensamientos» y «mirarlos pasar desde la orilla»?"
        ],
        "practica": "Realiza tres minutos de Hojas en el arroyo hoy antes de dormir o antes de una tarea exigente, dejando que el río lleve su propio ritmo."
    },
    {
        "slug": "manos-como-pensamientos",
        "titulo": "Las manos como pensamientos: a un centímetro de los ojos o en el regazo",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "met-las-manos.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Hands as Thoughts Metaphor, cap. 6). New Harbinger.",
        "resumen": "Vivir en diez segundos qué es la fusión (mirar la vida con las manos tapando la cara) y qué es la defusión (bajarlas al regazo sin borrar lo escrito).",
        "lectura": [
            "Pon tus dos manos abiertas con las palmas hacia ti, juntas como las páginas de un libro abierto. Imagina que en esas palmas están escritas todas las advertencias, críticas y temores que tu mente te repite hoy. Ahora sube las manos despacio hasta cubrirte por completo los ojos y la cara.",
            "Quédate ahí unos segundos mirando a través de los huecos entre los dedos. Eso es exactamente la fusión: las palabras están tan pegadas a tus ojos que tapan casi toda la habitación, te desconectan de quien tienes enfrente y además dejan tus dos manos ocupadas e inútiles para hacer cualquier cosa valiosa.",
            "Ahora separa las manos muy despacio de tu rostro y apóyalas abiertas sobre tu regazo. Fíjate bien en un detalle fundamental: las palabras escritas en tus palmas no se borraron ni desaparecieron; siguen ahí abajo si decides mirarlas. Pero ahora ves la habitación entera y tienes las manos libres para abrazar, trabajar y vivir."
        ],
        "clave": "Defusionarse no es cortarse las manos ni borrar lo escrito en ellas; es bajarlas de la cara para recuperar la vista y las manos.",
        "preguntas": [
            "¿Qué frases concretas llevan hoy escritas tus manos cuando se te suben a tapar la cara?",
            "Cuando miras tu día a través de esas manos pegadas a los ojos, ¿qué cosas valiosas de tu alrededor dejas de ver?",
            "Al apoyar las manos abiertas en el regazo sin exigir que se borren las letras, ¿qué vuelve a entrar en tu campo visual?"
        ],
        "practica": "Haz el gesto físico completo hoy una vez: lleva las manos a los ojos cinco segundos y bájalas muy lento al regazo respirando hondo."
    },
    {
        "slug": "pasear-la-mente",
        "titulo": "Sacar la mente a pasear: quién habla y quién elige la calle",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "4 min",
        "herramienta": "act-pasear-la-mente.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 6: Taking Your Mind for a Walk). Guilford Press.",
        "resumen": "Caminar eligiendo libremente la dirección con los pies mientras la mente va al lado comentando, juzgando y prediciendo sin parar.",
        "lectura": [
            "En uno de los ejercicios más memorables creados por Kelly Wilson y sus colegas, dos personas salen a caminar: una hace de «Persona» y la otra hace de su «Mente». La única regla para la Persona es elegir libremente por dónde caminar; la regla de la Mente es ir un paso atrás hablando sin callarse ni un segundo: opinando, comparando, advirtiendo peligros, criticando el paso y proponiendo volver atrás.",
            "A los pocos metros ocurre una revelación: la Mente puede decir con total convicción «no dobles a la izquierda, va a salir mal, estás cansado», y sin embargo las piernas de la Persona pueden doblar tranquilamente a la izquierda.",
            "No hace falta discutir con la Mente, ni convencerla de que piense positivo, ni esperar a que guarde silencio para poder cruzar la calle. Ella hace su trabajo de toda la vida —producir palabras sin descanso— y tú haces el tuyo: elegir con tus pies hacia dónde quieres caminar hoy."
        ],
        "clave": "Tu mente puede ir todo el camino diciendo «no vas a poder», y tus pies pueden seguir caminando exactamente hacia donde tú eliges.",
        "preguntas": [
            "Cuando intentas dar un paso importante para ti, ¿cuál es el monólogo favorito con el que tu mente intenta frenarte?",
            "¿Qué ha pasado cuando te has detenido en medio de la acera a discutir con ella para intentar callarla?",
            "¿Hacia qué calle o acción valiosa eligen doblar tus pies hoy mientras llevas a tu mente de paseo?"
        ],
        "practica": "Sal a caminar diez minutos hoy notando el parloteo de tu mente como si fuera un acompañante ruidoso, eligiendo tú cada esquina sin discutirle."
    },
    {
        "slug": "pero-por-y",
        "titulo": "Cambiar «pero» por «y»: salir de la trampa de la contradicción",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-pero-por-y.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 6: Replacing «But» with «And»). Guilford Press.",
        "resumen": "Sustituir la palabra «pero» —que convierte a cualquier emoción en un freno obligatorio— por la palabra «y», permitiendo sentir y actuar a la vez.",
        "lectura": [
            "Fíjate en una palabra diminuta que usamos decenas de veces al día: «pero». Etimológicamente, «pero» viene de «periculum» (obstáculo o freno). Cuando dices: «Quiero ir a esa reunión, pero tengo ansiedad», el «pero» coloca a las dos mitades de tu frase en guerra: dice que como hay ansiedad, entonces no puedes ir.",
            "Casi sin darnos cuenta, un simple conector del lenguaje nos encierra en una celda donde primero tendríamos que borrar el miedo, la pereza o la tristeza para tener permiso de movernos. Sin embargo, en la realidad física no hay ninguna contradicción entre querer a alguien y estar enojado, ni entre valorar un proyecto y sentir miedo.",
            "Prueba ahora a cambiar únicamente esa palabra por un «y»: «Quiero ir a esa reunión, Y tengo ansiedad». De golpe la trampa se abre: ya no hay excusa ni bloqueo, sino dos verdades vivas que caben juntas mientras tú das el paso."
        ],
        "clave": "El «pero» convierte tu emoción en un candado; el «y» abre la puerta para que puedas sentir lo que sientes y aun así avanzar.",
        "preguntas": [
            "Escribe la frase con «pero» que más te ha estado frenando esta semana (ej.: «Quiero..., pero...»).",
            "Reescríbela ahora cambiando la palabra «pero» por «Y» en mayúsculas: ¿cómo suena al leerla en voz alta?",
            "¿Qué paso concreto queda habilitado hoy mismo cuando ambas partes de la frase pueden viajar juntas con ese «y»?"
        ],
        "practica": "Durante el día de hoy, cada vez que te escuches decir «sí, pero...», detente un segundo y repítelo diciendo «sí, y además...»."
    },
    {
        "slug": "cinta-de-sushi",
        "titulo": "El tren de sushi de los pensamientos",
        "proceso": "defusion",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "met-cinta-de-sushi.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Sushi Train Metaphor). New Harbinger.",
        "resumen": "Observar las ideas e imágenes intrusivas como platillos que desfilan solos por una banda transportadora sin obligación de comprarlos ni tragarlos.",
        "lectura": [
            "En muchos restaurantes japoneses los platillos viajan sobre una banda transportadora que gira sin descanso frente a las mesas. En la cocina del fondo, el chef prepara de todo: platillos deliciosos, platillos picantes, combinaciones extrañas y alguno que jamás te gustaría probar.",
            "Tu mente funciona exactamente igual que ese chef: allá en el fondo, sin pedirte permiso, cocina pensamientos todo el día basándose en tu historia, tus miedos y lo que has vivido, y los pone a girar sobre la banda transportadora frente a ti.",
            "Cuando nos fusionamos, creemos que porque un platillo pasó frente a nuestros ojos estamos obligados a levantarlo, pagarlo y tragárnoslo entero; o nos levantamos furiosos a golpear la banda para que ese plato no vuelva a salir. La defusión es mucho más sencilla: es quedarte sentado en tu mesa, ver pasar el platillo extraño, decir «mira lo que acaba de sacar la cocina hoy» y dejar que siga su vuelta por el riel."
        ],
        "clave": "No puedes controlar qué platillos saca la cocina de tu mente, pero sí decides cuáles levantas de la cinta y cuáles dejas pasar de largo.",
        "preguntas": [
            "¿Qué dos o tres «platillos repetidos» ha estado sacando la cocina de tu mente con más frecuencia estos días?",
            "¿Qué le pasa a tu tarde cuando levantas uno de esos platillos amargos y te quedas masticándolo durante horas?",
            "Si hoy dejas que ese platillo siga rodando por el riel sin tocarlo, ¿a qué conversación o tarea de tu mesa puedes volver?"
        ],
        "practica": "Cuando aparezca un pensamiento intrusivo o autocrítico hoy, imagínalo servido sobre un platillo de colores pasando de izquierda a derecha por la cinta."
    },
    {
        "slug": "radio-mental",
        "titulo": "Radio Catástrofe: cuando la emisora suena de fondo",
        "proceso": "defusion",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "met-la-radio.html",
        "fuente": "Harris, R. (2007). The Happiness Trap (Radio Doom and Gloom). Robinson.",
        "resumen": "Tratar el parloteo ansioso y pesimista de la mente como una radio encendida en la esquina del cuarto que no tiene botón de apagado.",
        "lectura": [
            "Imagina que en un rincón de tu cabeza transmite las veinticuatro horas del día una emisora llamada «Radio Catástrofe FM». Su programación es siempre la misma: por la mañana pasa el resumen de todos tus errores del pasado; al mediodía transmite boletines urgentes sobre todo lo que podría salir mal mañana; y por la noche emite comparaciones en las que tú siempre sales perdiendo.",
            "El problema es que esta radio vino de fábrica sin enchufe y sin botón de apagado. Si te acercas al parlante a gritarle al locutor para que se calle, o te quedas pegado escuchando cada boletín por si acaso dice algo importante, tu día entero queda secuestrado por la emisora.",
            "Pero todos hemos tenido alguna vez un radio o un televisor encendido en otra habitación mientras cocinamos o conversamos con un amigo: el aparato sigue haciendo ruido allá al fondo, pero nosotros dejamos de prestarle oído porque estamos ocupados en lo que nos importa."
        ],
        "clave": "No hace falta desenchufar la emisora mental para vivir; basta con dejarla sonar como ruido de fondo mientras atiendes lo que tienes delante.",
        "preguntas": [
            "Si la emisora que más transmite en tu mente tuviera un nombre propio («Radio Perfección», «Radio Todo Saldrá Mal», «Radio Culpa»), ¿cómo se llamaría?",
            "¿Cuáles son los tres «grandes éxitos» o noticias repetidas que ese locutor pasa todos los días?",
            "¿Cómo puedes responderle hoy con una sonrisa breve («Ya está transmitiendo otra vez Radio Catástrofe») y volver a lo tuyo?"
        ],
        "practica": "Hoy, cuando empiece el boletín de preocupaciones, di mentalmente: «Gracias, Radio Catástrofe, por el reporte del clima» y continúa con tu actividad."
    },
    {
        "slug": "nombrar-la-historia",
        "titulo": "Ponerle título al libro: «Ya empezó la historia de...»",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-soltar-el-anzuelo.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Naming the Story). · Hayes, S. C. et al. (2012).",
        "resumen": "Empaquetar largos encadenamientos de rumiación bajo el título de una película o libro conocido para reconocerlos en un segundo sin releerlos enteros.",
        "lectura": [
            "Si tuvieras que reunir todas tus preocupaciones, recuerdos dolorosos y autocríticas en una autobiografía, notarías que la mente no inventa un argumento nuevo cada mañana. Casi siempre vuelve a proyectar las mismas tres o cuatro películas conocidas que llevan años en cartelera.",
            "Cuando nos enganchamos, nos sentamos en primera fila cada vez que empieza la función como si fuera una noticia de último minuto, sufriendo capítulo por capítulo. En cambio, cuando le pones un título claro a esa narrativa —por ejemplo, «La historia de que no soy suficiente», «La película de que me quedaré solo» o «El cuento de que todo es urgente»—, ganas perspectiva al instante.",
            "La próxima vez que empiece el primer párrafo, no necesitas volver a leer las trescientas páginas: basta con ver la portada, sonreír con suavidad y decir: «Ah, mira, ya empezó otra vez la historia de siempre; ya me conozco el final»."
        ],
        "clave": "Reconocer la portada del viejo cuento te ahorra tener que volver a sufrir las trescientas páginas cada tarde.",
        "preguntas": [
            "Si esa narrativa repetitiva que suele atraparte fuera un libro o una película, ¿qué título llevaría en la portada?",
            "¿Cuáles son las escenas clásicas que siempre aparecen cuando tu mente abre ese libro?",
            "¿Qué cambia cuando al notar la primera frase dices simplemente: «Ahí está otra vez la historia de [título]»?"
        ],
        "practica": "Ponle hoy un título breve a tu historia mental más frecuente y úsalo como etiqueta rápida cada vez que asome el primer párrafo."
    },
    {
        "slug": "agradecer-a-la-mente",
        "titulo": "Darle las gracias a tu mente: desarmar la pelea con amabilidad",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-pasear-la-mente.html",
        "fuente": "Hayes, S. C. y Smith, S. (2005). Sal de tu mente, entra en tu vida (Cap. 5: Agradecer a tu mente). Desclée De Brouwer.",
        "resumen": "Reemplazar la discusión agotadora contra las advertencias catastróficas de la mente por un agradecimiento cortés y desliteralizado.",
        "lectura": [
            "Por extraño que parezca, cuando tu mente te lanza advertencias sombrías («no vayas, harás el ridículo», «no confíes, te van a lastimar», «mejor quédate quieto»), en el fondo está intentando hacer aquello para lo que evolucionó hace miles de años: protegerte de cualquier peligro posible para que sobrevivas.",
            "Es como un guardaespaldas hiperactivo y un poco exagerado que ve tigres dientes de sable detrás de cada correo electrónico y de cada conversación difícil. Si te pones a gritarle o a discutir con él para demostrarle que está equivocado, el guardaespaldas cree que no lo escuchaste y empieza a gritar el doble de fuerte.",
            "Por eso en ACT practicamos un giro lleno de humor amable y respeto: cuando tu mente te suelte su advertencia más dramática, mírala como a ese vigilante bienintencionado pero alarmista y dile con sinceridad: «Muchas gracias, mente, por intentar cuidarme; ya tomé nota del aviso, y de todos modos voy a dar este paso»."
        ],
        "clave": "Cuando agradeces a tu mente sin discutirle ni obedecerle, la pelea se termina en dos segundos.",
        "preguntas": [
            "¿De qué peligro intenta «protegerte» tu mente cuando te lanza sus pensamientos más duros o pesimistas?",
            "¿Qué pasa cuando intentas callarla a la fuerza o ganarle una discusión lógica?",
            "¿Cómo se siente responderle hoy con calidez: «Gracias por el aviso, mente; igual elijo seguir adelante»?"
        ],
        "practica": "Ensaya hoy tres veces llevar una mano al pecho o hacer una leve inclinación de cabeza diciendo: «Gracias, mente, qué creativa estás hoy»."
    },
    {
        "slug": "voces-de-dibujos",
        "titulo": "Cantar el pensamiento o escucharlo en cámara lenta",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "met-la-palabra-repetida.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Silly Voices & Musical Thoughts). · Hayes, S. C. et al. (1999).",
        "resumen": "Cambiar el tono solemne y autoritario de un pensamiento autocrítico para revelar que su poder intimidante provenía de cómo lo escuchábamos.",
        "lectura": [
            "¿Has notado con qué tono de voz suelen hablar los pensamientos autocríticos en nuestra cabeza? Casi siempre suenan con la voz grave de un juez severo, un trueno solemne o una sentencia inapelable. Ese tono grave es gran parte del truco que nos hace obedecerlos al instante.",
            "Sin cambiar ni una sola palabra de la frase que te preocupa —porque en ACT no intentamos reemplazar el pensamiento por otro «positivo»—, podemos cambiar el envoltorio acústico en el que se presenta. Por ejemplo, escuchando exactamente esa misma frase cantada con la melodía de «Cumpleaños feliz», o dicha en cámara ultralenta como un disco que se queda sin batería, o con la voz aguda de un personaje de dibujo animado.",
            "El propósito jamás es burlarse de tu sufrimiento ni minimizar lo que vives, sino comprobar algo liberador: las palabras siguen siendo las mismas, pero en cuanto pierden su disfraz de juez supremo, dejan de tenerte contra la pared."
        ],
        "clave": "No hace falta cambiar las palabras del pensamiento para desactivar su hechizo; basta con quitarle la toga de juez solemne.",
        "preguntas": [
            "¿Qué frase corta de autocrítica o temor suena hoy en tu cabeza con voz de sentencia solemne?",
            "Si escuchas mentalmente esa misma frase exacta cantada con la música de «Cumpleaños feliz» o dicha en cámara lenta, ¿qué le ocurre a su autoridad?",
            "¿Qué te muestra este experimento sobre la diferencia entre «una frase en mi mente» y «la verdad absoluta»?"
        ],
        "practica": "Toma hoy un pensamiento repetitivo de menos de seis palabras y pronúncialo una vez muy despacio, alargando cada vocal como en cámara lenta."
    },
    {
        "slug": "estoy-teniendo-el-pensamiento",
        "titulo": "Dos pasos atrás con las palabras: «Estoy notando que tengo el pensamiento de que...»",
        "proceso": "defusion",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-soltar-el-anzuelo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (I'm having the thought that...). Guilford Press.",
        "resumen": "Usar el prefijo clásico de ACT para introducir distancia psicológica inmediata entre la persona que observa y la frase que produce su mente.",
        "lectura": [
            "Existe una diferencia enorme entre decir «No soy capaz de hacer esto» y decir «Estoy teniendo el pensamiento de que no soy capaz de hacer esto». En la primera frase, tú estás fundido dentro del pensamiento como si fuera un hecho físico; en la segunda, acabas de dar un paso atrás y nombras lo que realmente está pasando en el presente: hay un pensamiento ocurriendo.",
            "Podemos incluso dar un segundo paso atrás y decir: «Estoy notando que estoy teniendo el pensamiento de que no soy capaz de hacer esto». Observa cómo con esas pocas palabras el pensamiento pasa de estar pegado a tus ojos a quedar frente a ti, sobre la mesa, donde puedes mirarlo con calma.",
            "Este sencillo giro verbal es una de las herramientas más investigadas y potentes de ACT porque no te pide mentirte ni forzarte a pensar lo contrario: simplemente llama al pensamiento por su verdadero nombre."
        ],
        "clave": "Nombrar un pensamiento como pensamiento abre al instante un metro de aire limpio entre tú y lo que dice tu cabeza.",
        "preguntas": [
            "1. Escribe el pensamiento difícil tal como sale en crudo: «...».",
            "2. Ahora anteponle el primer paso: «Estoy teniendo el pensamiento de que...» y léelo despacio.",
            "3. Ahora da el segundo paso completo: «Estoy notando que estoy teniendo el pensamiento de que...». ¿Qué distancia sientes entre el paso 1 y el paso 3?"
        ],
        "practica": "Usa durante todo el día de hoy la muletilla «Estoy notando que mi mente me dice que...» cada vez que aparezca un juicio duro."
    },

    # ==================== 3. MOMENTO PRESENTE (6) ====================
    {
        "slug": "cinco-sentidos",
        "titulo": "Los cinco sentidos (5-4-3-2-1): aterrizar aquí y ahora",
        "proceso": "presente",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-los-ganchos.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Notice Five Things). New Harbinger.",
        "resumen": "Volver del viaje mental hacia el pasado o el futuro utilizando los cinco canales sensoriales como anclas inmediatas al presente.",
        "lectura": [
            "Nuestra mente es una máquina del tiempo extraordinaria: puede saltar diez años hacia atrás para revivir un reproche o proyectarse seis meses hacia adelante para imaginar diez catástrofes en un minuto. Pero mientras la mente viaja en el tiempo, tu cuerpo tiene una propiedad maravillosa: solo puede existir en el presente.",
            "Tus ojos no pueden ver el mañana; tus oídos no pueden escuchar el ayer; tus manos solo pueden tocar la textura que está aquí ahora mismo. Por eso los cinco sentidos son la puerta más directa para volver a casa cuando la rumiación o la ansiedad te sacan del momento.",
            "Haz una pausa breve y recorre sin prisa: nombra cinco cosas que tus ojos vean ahora mismo en la habitación (fijándote en un reflejo de luz o un color que no habías notado); cuatro texturas o apoyos que sienta tu piel; tres sonidos cercanos o lejanos; dos aromas del aire; y el sabor actual en tu boca."
        ],
        "clave": "La mente viaja al pasado y al futuro sin descanso, pero tus sentidos solo habitan en el aquí y el ahora.",
        "preguntas": [
            "Al detenerte a mirar de verdad tu entorno ahora mismo, ¿qué detalle visual o sonido descubres que antes habías pasado por alto?",
            "¿En qué momentos del día sueles notar que tu cuerpo está en un lugar pero tu mente está a kilómetros de distancia?",
            "¿Cuál de los cinco sentidos (la vista, el tacto de los pies, el oído o la respiración) te resulta más fácil usar como puerta de retorno?"
        ],
        "practica": "Tres veces hoy —al sentarte a comer, al abrir una puerta o al esperar en una fila—, detente a notar tres colores, tres sonidos y tres puntos de apoyo corporal."
    },
    {
        "slug": "aterrizar-en-el-cuerpo",
        "titulo": "Pies en el suelo: volver a habitar el cuerpo",
        "proceso": "presente",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-echar-el-ancla.html",
        "fuente": "Strosahl, K. D., Robinson, P. J. y Gustavsson, T. (2012). Brief Interventions for Radical Change: Principles and Practice of Focused ACT. New Harbinger.",
        "resumen": "Re-enraizar la atención en las plantas de los pies y el eje corporal cuando la tormenta mental amenaza con desconectarnos.",
        "lectura": [
            "Cuando estamos atrapados en una tormenta de preocupaciones, parece como si viviéramos únicamente del cuello hacia arriba, flotando dentro de una nube ruidosa de ideas mientras el resto del cuerpo desaparece o se tensa en silencio.",
            "Sin embargo, debajo de tus zapatos el suelo sigue estando ahí, sólido y estable, sosteniendo todo tu peso sin pedirte nada a cambio. Llevar la atención hacia las plantas de los pies no es un truco para dejar de pensar, sino una manera de ampliar el foco para recordar que tienes piso firme debajo de ti.",
            "Presiona suavemente los talones y las puntas de los pies contra el suelo. Nota la firmeza del piso, sube la atención por las piernas hasta sentir el asiento sosteniendo tu pelvis, deja que los hombros bajen dos centímetros lejos de las orejas y mira el cuarto que te rodea: estás aquí."
        ],
        "clave": "Cuando la cabeza parece un torbellino, tus pies siguen apoyados sobre tierra firme aquí y ahora.",
        "preguntas": [
            "Antes de hacer esta pausa, ¿cómo estaban tus hombros, tu mandíbula y tu respiración?",
            "Al llevar la atención a la presión de las plantas de tus pies contra el suelo, ¿qué sensación de soporte o estabilidad aparece?",
            "¿En qué situación difícil de esta semana puedes usar el apoyo de tus pies en el suelo sin que nadie siquiera lo note?"
        ],
        "practica": "Cada vez que te levantes de una silla hoy, siente durante dos segundos el peso completo de tu cuerpo pasando a las plantas de los pies."
    },
    {
        "slug": "piloto-automatico",
        "titulo": "Salir del piloto automático en una rutina diaria",
        "proceso": "presente",
        "tipo": "Ejercicio experiencial",
        "tiempo": "4 min",
        "herramienta": "act-piloto-automatico.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (2012). Terapia de Aceptación y Compromiso (Contacto con el momento presente en la vida cotidiana).",
        "resumen": "Convertir una actividad cotidiana que solemos hacer ausentes y acelerados en un espacio vivo de presencia plena.",
        "lectura": [
            "¿Te ha pasado alguna vez que llegas al final de una ducha sin saber si ya te pusiste jabón, o terminas una taza de café sin haber saboreado un solo sorbo porque estabas repasando mentalmente una discusión o una lista de pendientes? A eso lo llamamos vivir en piloto automático.",
            "El piloto automático es útil para no tener que reaprender a atarnos los zapatos cada mañana, pero cuando se adueña de todo el día nos deja una sensación extraña de cansancio y vacío: hicimos mil cosas, pero no estuvimos presentes en ninguna de nuestras propias horas.",
            "Entrenar el contacto con el momento presente en ACT no exige retirarse a una cueva en silencio; se entrena en medio de la vida real. Consiste en elegir una pequeña actividad que ya haces todos los días y comprometerte a habitarla con los cinco sentidos encendidos, trayendo la atención de vuelta con amabilidad las diez o veinte veces que se vaya a los pendientes."
        ],
        "clave": "No hace falta añadir una hora más a tu agenda para practicar presencia; basta con estar de verdad en lo que ya estás haciendo.",
        "preguntas": [
            "¿Qué actividad cotidiana de tu día (tomar café, caminar una cuadra, ducharte, escuchar a alguien en casa) sueles hacer casi siempre en piloto automático?",
            "Mientras tu cuerpo hace esa actividad, ¿a qué preocupaciones suele irse tu mente?",
            "Si mañana realizas esa misma actividad con los sentidos encendidos, ¿qué detalles de temperatura, aroma, sonido o gesto vas a notar?"
        ],
        "practica": "Elige hoy una sola rutina de tres minutos (por ejemplo, el primer café o lavarte las manos y la cara) y hazla sin pantallas, atendiendo cada sensación."
    },
    {
        "slug": "hecho-o-juicio",
        "titulo": "Describir frente a evaluar: ¿está en el objeto o en mi mente?",
        "proceso": "presente",
        "tipo": "Hoja de reflexión",
        "tiempo": "4 min",
        "herramienta": "act-hecho-o-juicio.html",
        "fuente": "Hayes, S. C. y Smith, S. (2005). Sal de tu mente, entra en tu vida (Propiedades primarias vs. secundarias). Desclée De Brouwer.",
        "resumen": "Aprender a separar los hechos observables del presente (lo que vería una cámara) de los juicios valorativos globales que nuestra mente les pega encima.",
        "lectura": [
            "En ACT distinguimos dos tipos de atributos muy diferentes. Los primeros son las descripciones o propiedades primarias: «esta manzana es roja, redonda y pesa ciento cincuenta gramos». Si todos los seres humanos desaparecieran hoy del planeta, la manzana seguiría siendo redonda y pesando lo mismo.",
            "Los segundos son las evaluaciones o juicios: «esta manzana es buenísima» o «es espantosa». Esas etiquetas no están dentro de la cáscara de la manzana; están en la relación de una mente que la compara y la califica. El problema surge cuando nuestra mente pega el juicio sobre el hecho con tanta fuerza que creemos que la etiqueta forma parte de la realidad física.",
            "Decir «ayer olvidé un dato en mi presentación y me tembló la voz» es describir un hecho del presente. Decir «fue un desastre humillante y soy un incompetente» es una evaluación mental añadida encima. Volver a la descripción limpia nos devuelve al suelo real."
        ],
        "clave": "Los hechos están en el mundo; los juicios («desastre», «inútil», «imposible») son etiquetas adhesivas que fabrica nuestra mente.",
        "preguntas": [
            "¿Qué situación reciente o aspecto de ti mismo has estado calificando con una etiqueta dura o global?",
            "Si una cámara de video hubiera grabado únicamente los hechos físicos sin ningún adjetivo valorativo, ¿qué habría registrado?",
            "¿Qué etiquetas o evaluaciones pegó tu mente encima de esos hechos y cómo puedes separarlas hoy?"
        ],
        "practica": "Reescribe hoy una queja o autocrítica usando la fórmula: «El hecho observable es [...], y noto que mi mente le añade el juicio de [...]»."
    },
    {
        "slug": "pausa-de-tres-minutos",
        "titulo": "Tres respiraciones para notar dónde están tus pies y tu corazón",
        "proceso": "presente",
        "tipo": "Ejercicio experiencial",
        "tiempo": "3 min",
        "herramienta": "act-por-donde-entrar.html",
        "fuente": "Wilson, K. G. y DuFrene, T. (2009). Mindfulness for Two. · Segal, Williams y Teasdale (2013).",
        "resumen": "Hacer un alto breve en medio de la jornada para abrir la atención a lo que está ocurriendo adentro, centrarse en la respiración y elegir el siguiente paso.",
        "lectura": [
            "A lo largo del día vamos acumulando velocidad como una rueda cuesta abajo: pasamos de una tarea a otra, de un mensaje a otro, arrastrando la tensión de la hora anterior sin darnos cuenta siquiera de cómo estamos respirando.",
            "Esta pausa cabe en apenas tres respiraciones conscientes o en tres minutos de reloj. En el primer momento, detén tus manos y pregúntate con honestidad: «¿Cómo está mi clima interno ahora mismo? ¿Qué pensamientos cruzan mi mente, qué emoción hay en mi pecho y qué tensión hay en mi cuerpo?», sin intentar cambiar nada.",
            "En el segundo momento, reúne suavemente tu atención en el movimiento físico del aire entrando y saliendo de tu abdomen, sintiendo el ancla de tus pies en el piso. Y en el tercer momento, vuelve a abrir el foco hacia la habitación y pregúntate: «Desde aquí, ¿cuál es el paso más consciente y valioso que elijo dar ahora?»."
        ],
        "clave": "Basta una pausa de tres respiraciones conscientes para dejar de reaccionar por inercia y volver a elegir tu respuesta.",
        "preguntas": [
            "1. Al detenerte ahora mismo, ¿qué notas en tu cuerpo, en tu emoción y en el ritmo de tus pensamientos?",
            "2. Al acompañar tres respiraciones completas sintiendo el peso de tu cuerpo en la silla, ¿qué cambia en tu ritmo interno?",
            "3. Al volver a abrir los ojos al momento presente, ¿con qué actitud eliges continuar tu próxima hora?"
        ],
        "practica": "Haz esta pausa de tres respiraciones hoy justo antes de entrar a casa o antes de iniciar una conversación importante."
    },
    {
        "slug": "presencia-en-sesion",
        "titulo": "Lo que pasa afuera y lo que pasa aquí entre nosotros",
        "proceso": "presente",
        "tipo": "Hoja de reflexión",
        "tiempo": "4 min",
        "herramienta": "fap-dentro-y-fuera.html",
        "fuente": "Kohlenberg, R. J. y Tsai, M. (1991). Functional Analytic Psychotherapy. · Wilson, K. G. y DuFrene, T. (2009). Mindfulness for Two.",
        "resumen": "Notar cómo las mismas barreras y anhelos que vivimos en nuestras relaciones cotidianas se hacen presentes en vivo aquí y ahora.",
        "lectura": [
            "Muchas veces pensamos que hablar de nuestras dificultades consiste únicamente en contar historias de lo que ocurrió allá afuera durante la semana. Pero nuestras formas de protegernos, de callar lo que necesitamos, de temer el juicio o de buscar cercanía no se quedan en la calle: entran con nosotros a cada conversación importante.",
            "Por eso, además de mirar lo que pasó afuera, es profundamente transformador prestar atención a lo que ocurre aquí y ahora en el presente: cuando te cuesta mirar a los ojos al hablar de algo doloroso, cuando cambias de tema para no incomodar, o cuando por primera vez te animas a decir en voz alta lo que de verdad sientes.",
            "Cada vez que notas en vivo ese instante de vulnerabilidad y eliges quedarte presente un segundo más en lugar de esconderte, estás ensayando en tiempo real una forma nueva y más libre de relacionarte contigo y con los demás."
        ],
        "clave": "El momento presente de un encuentro honesto es el laboratorio vivo donde aprendemos a mostrarnos sin armadura.",
        "preguntas": [
            "Cuando estás con otras personas en tu vida diaria, ¿de qué manera sueles esconder lo que sientes o ponerte una armadura para protegerte?",
            "¿Has notado algún momento en que esa misma precaución o dificultad para pedir, decir que no o abrirte aparece también aquí en consulta?",
            "¿Qué pequeño gesto de honestidad o autenticidad te gustaría practicar hoy en tus conversaciones cercanas?"
        ],
        "practica": "En tu próxima conversación significativa de esta semana, nota si aparece el impulso de decir «todo bien» por automático y anímate a compartir una frase genuina."
    },
]

LECTURAS.extend([
    # ==================== 4. YO COMO CONTEXTO (7) ====================
    {
        "slug": "tablero-de-ajedrez",
        "titulo": "El tablero de ajedrez: dejar la guerra entre blancas y negras",
        "proceso": "yo",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-el-tablero.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Chessboard Metaphor, cap. 7). Guilford Press.",
        "resumen": "Descubrir que no somos ni las piezas blancas ni las piezas negras en batalla, sino el tablero estable que las sostiene a todas.",
        "lectura": [
            "Imagina un tablero de ajedrez infinito cubierto de piezas blancas y piezas negras. Las piezas blancas son tus pensamientos positivos, tus confianzas, tus buenos recuerdos y tus días de calma. Las piezas negras son tus miedos, tus dudas, tus culpas y tus recuerdos amargos.",
            "Casi todos vivimos subidos al lomo de un caballo blanco intentando ganar una guerra definitiva: queremos reunir suficientes piezas blancas para barrer del mapa a todas las piezas negras de una vez por todas. El problema es que en este juego las piezas blancas mismas atraen a las negras: en cuanto dices «tengo que estar seguro», aparece al frente el peón negro de «¿y si todo sale mal?». Y mientras dura la batalla, vives agotado recibiendo golpes.",
            "Pero en esa escena hay algo más que piezas blancas y negras: está el tablero de madera sobre el que se apoyan. Al tablero no lo hieren ni las jugadas de las negras ni las de las blancas; él las sostiene a todas en contacto íntimo y, al mismo tiempo, es más amplio que cualquier partida. Si tú no fueras las piezas, sino el tablero, la guerra ya habría terminado."
        ],
        "clave": "Cuando dejas de pelear desde las piezas blancas contra las negras y habitas el tablero, ninguna jugada puede destruirte.",
        "preguntas": [
            "¿Cuáles son hoy las «piezas negras» que más intentas derribar y con qué «piezas blancas» tratas de combatirlas?",
            "¿Cuánto cansancio te ha dejado vivir metido a nivel de las piezas peleando esa partida interminable?",
            "Si te sitúas hoy en el nivel del tablero que sostiene a ambas sin dañarse, ¿hacia dónde puedes llevar el tablero entero hoy?"
        ],
        "practica": "Cuando notes hoy un debate interno («sí puedo» vs. «no puedo»), imagina ambas frases como dos piezas de madera sobre un mismo tablero tranquilo."
    },
    {
        "slug": "cielo-y-clima",
        "titulo": "El cielo y el clima: ninguna tormenta mancha el cielo",
        "proceso": "yo",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "act-el-cielo-y-el-clima.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (The Sky and the Weather). · Pema Chödrön / Tradición contemplativa adaptada a ACT.",
        "resumen": "Reconocer nuestra conciencia observadora como el cielo despejado por el que cruzan todo tipo de nubes y tormentas sin alterarlo.",
        "lectura": [
            "Mira hacia arriba en un día de tormenta cerrada. Cuando las nubes negras cubren todo el horizonte y cae granizo, parece que el cielo azul hubiera desaparecido. Sin embargo, cualquiera que haya subido en un avión sabe qué ocurre apenas atraviesas la capa de nubes: allá arriba el cielo azul sigue exactamente igual de limpio, inmenso e intacto que siempre.",
            "En tu vida interior, tus emociones, estados de ánimo, pensamientos y sensaciones físicas son el clima: hay mañanas de sol tibio, tardes de niebla espesa y noches de tormenta eléctrica. El clima cambia por su cuenta una y otra vez; ningún ser humano puede ordenar que sea primavera los trescientos sesenta y cinco días del año.",
            "Tú no eres el clima; tú eres el cielo que da cabida al clima. Ni el huracán más violento ha dejado jamás una cicatriz en el cielo, y por más espesa que sea hoy la nube que estás atravesando, el espacio consciente que la nota sigue intacto detrás de ella."
        ],
        "clave": "Las emociones son el clima cambiante; tú eres el cielo amplio que las contiene sin romperse jamás.",
        "preguntas": [
            "Si tuvieras que describir tu «clima interno» de hoy en términos meteorológicos (llovizna, viento fuerte, neblina, bochorno), ¿cómo está hoy?",
            "¿Qué ocurre cuando te confundes con el clima y crees que «tú eres la tormenta» o que esta nube durará para siempre?",
            "¿Cómo cambia tu respiración al recordar que detrás de esta nube sigue estando el cielo despejado desde el que observas?"
        ],
        "practica": "Mira por una ventana al cielo real durante un minuto hoy y repite con calma: «Esto que siento es el clima de esta hora; yo soy el cielo que lo aloja»."
    },
    {
        "slug": "quien-lleva-los-globos",
        "titulo": "Quién lleva los globos en la mano",
        "proceso": "yo",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "act-quien-lleva-los-globos.html",
        "fuente": "Wilson, K. G. y Luciano, M. C. (2002). Terapia de Aceptación y Compromiso (ACT). Pirámide.",
        "resumen": "Diferenciar los globos de colores que flotan sobre nuestra cabeza (recuerdos, miedos, juicios) del caminante que sujeta los hilos y elige el sendero.",
        "lectura": [
            "Imagina que vas caminando por un sendero llevando en tu mano el cordel de varios globos inflados con helio. En cada globo hay escrita una historia, un temor o una sensación: en uno dice «no soy suficientemente bueno», en otro «tengo miedo a fracasar», en otro «recuerdo de aquel error». Cuando sopla el viento, los globos chocan entre sí, hacen ruido y tiran del hilo hacia arriba.",
            "A veces miramos tanto hacia arriba que llegamos a creer que los globos son quienes deciden por dónde se camina, o nos sentamos en el suelo esperando a que todos los globos oscuros se desinflen solos antes de dar otro paso.",
            "Pero baja la mirada un momento: los globos flotan en el aire, pero quien tiene las botas puestas sobre la tierra firme eres tú. Aunque hoy lleves cinco globos ruidosos flotando sobre el hombro, eres tú quien sostiene el hilo y son tus piernas las que deciden hacia qué horizonte avanzar."
        ],
        "clave": "Los globos pueden hacer ruido arriba con el viento, pero quien tiene los pies sobre el sendero eres tú.",
        "preguntas": [
            "¿Qué tres «globos» han estado flotando más alto y llamando más tu atención durante esta semana?",
            "¿Cuántas veces has detenido tu caminata esperando a que un globo desaparezca antes de seguir?",
            "Si aceptas llevar esos globos atados a la muñeca sin pelear con ellos, ¿hacia dónde eliges caminar hoy con tus botas?"
        ],
        "practica": "Imagina hoy tus preocupaciones como globos flotando medio metro detrás de tu hombro mientras tus pies siguen avanzando hacia tu tarea."
    },
    {
        "slug": "escenario-y-butaca",
        "titulo": "El reflector, el escenario completo y la butaca",
        "proceso": "yo",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-el-escenario.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Stage Show Metaphor). New Harbinger.",
        "resumen": "Ampliar la luz desde el reflector estrecho clavado sobre el problema hacia todo el escenario vital y la butaca tranquila desde donde observamos.",
        "lectura": [
            "Imagina que tu experiencia de este momento es el escenario de un gran teatro. En el centro de las tablas hay un actor ruidoso y dramático —tu problema actual, tu dolor o tu preocupación— y el técnico de luces ha cerrado el reflector al máximo enfocando únicamente la cara de ese actor, dejando todo el resto del teatro a oscuras.",
            "Con esa luz cerrada de túnel, parece que en tu vida no existiera absolutamente nada más que ese problema. Pero ahora hagamos dos movimientos. Primero, encendamos las luces generales de todo el escenario: el actor ruidoso sigue ahí en medio, pero ahora ves que a su alrededor también están tus afectos, tus capacidades, tu cuerpo respirando, los colores del cuarto y las cosas que valoras.",
            "Y segundo, da un paso más atrás y nota desde dónde estás viendo toda la función: tú estás sentado en la butaca tranquila de la platea, observando tanto al actor ruidoso como al resto de la escena."
        ],
        "clave": "El sufrimiento cierra el reflector sobre un solo rincón; la conciencia plena enciende las luces de todo el escenario y recuerda la butaca.",
        "preguntas": [
            "¿Cuál es el «actor ruidoso» sobre el que tu mente ha tenido clavado el reflector estrecho estos días?",
            "Cuando enciendes la luz general de todo el escenario de tu vida hoy, ¿qué otras presencias, recursos o vínculos vuelven a verse?",
            "¿Cómo se siente mirar toda la obra sentado con calma desde la butaca del observador?"
        ],
        "practica": "Cuando sientas visión de túnel ante un problema hoy, haz una pausa y nombra tres cosas valiosas que siguen sobre las tablas aunque el problema grite."
    },
    {
        "slug": "observador-en-el-tiempo",
        "titulo": "El observador continuo a través del tiempo",
        "proceso": "yo",
        "tipo": "Ejercicio experiencial",
        "tiempo": "5 min",
        "herramienta": "act-observador-en-el-tiempo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 7: Observer Exercise). Guilford Press.",
        "resumen": "Contactar con la continuidad inalterable del «Yo, aquí, ahora» que ha sido testigo de nuestra infancia, nuestra juventud y nuestro presente.",
        "lectura": [
            "Cierra un momento los ojos o baja la mirada y trae a la memoria un recuerdo nítido de cuando tenías siete u ocho años. Mira con calma dónde estabas, qué veían tus ojos entonces y cómo se sentía aquel mundo. Ahora haz una pausa y nota algo extraordinario: quien miraba a través de tus ojos en aquel recuerdo infantil eras tú.",
            "Ahora viaja a un recuerdo de hace apenas unos años —un día importante, difícil o feliz— y vuelve a notar quién estaba ahí adentro observando esa escena. Y finalmente regresa a este preciso segundo: siente el peso de tu cuerpo en la silla y mira tus manos hoy.",
            "Casi todas las células de tu cuerpo de los ocho años ya no existen; tus pensamientos, tus roles, tus amistades y tus miedos cambiaron miles de veces. Sin embargo, el testigo silencioso que miraba por detrás de tus ojos entonces es exactamente el mismo «Yo» que está leyendo esta línea hoy. Si puedes notar todos esos cambios, tú eres más grande y más estable que cualquiera de ellos."
        ],
        "clave": "Tu cuerpo, tus ideas y tus emociones cambian sin cesar, pero el testigo consciente detrás de tus ojos ha permanecido entero desde el principio.",
        "preguntas": [
            "Al recordar a aquel niño o niña que fuiste y conectarlo con quien eres hoy, ¿qué sientes al notar que «quien mira» es el mismo?",
            "¿Cuántas tormentas emocionales que en otro año parecían definitivas pasaron por tu vida sin lograr destruir a ese observador?",
            "Desde esa presencia continua y más amplia, ¿qué mensaje de calma o compañía puedes ofrecerte en la dificultad de hoy?"
        ],
        "practica": "Mira una fotografía tuya de otra época (o tus propios ojos en el espejo) reconociendo al testigo continuo que ha atravesado toda tu historia."
    },
    {
        "slug": "dos-montanas",
        "titulo": "Los dos escaladores en montañas vecinas",
        "proceso": "yo",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-dos-montanas.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 1: Two Mountains Metaphor). Guilford Press.",
        "resumen": "Comprender el valor de tomar distancia para mirar nuestra propia subida como la veríamos desde una montaña vecina.",
        "lectura": [
            "Imagina que tanto tú como yo somos escaladores subiendo cada uno su propia montaña, separadas por un valle. A veces, cuando estás en medio de un tramo empinado, es fácil imaginar que los demás —o tu propio terapeuta— están sentados cómodamente en la cima sin piedras ni tropiezos. Pero la verdad es que todo ser humano está subiendo su propia ladera con su propia mochila.",
            "La única ventaja que existe desde la montaña de enfrente no es ser superior ni estar libre de dificultades, sino el ángulo de visión: cuando tú tienes la cara pegada contra una roca gigante de tu camino, parece que la montaña se hubiera terminado; en cambio, desde la montaña de enfrente se alcanza a ver que dos metros a la derecha el sendero continúa despejado.",
            "Aprender a tomar perspectiva en ACT es desarrollar la capacidad de cruzar imaginariamente el valle para mirar tu propia montaña desde enfrente, con la misma amplitud, paciencia y compasión con la que mirarías a un ser querido que está subiendo."
        ],
        "clave": "De cerca, una piedra tapa toda la vista; mirada desde la montaña de enfrente, se ve todo lo que ya has subido y por dónde sigue el sendero.",
        "preguntas": [
            "¿Cuál es la «roca pegada a la cara» que hoy te hace sentir que el camino está bloqueado?",
            "Si cruzaras a la montaña de enfrente y miraras todo tu recorrido de los últimos años, ¿qué fortaleza o avance tuyo se haría visible?",
            "¿Qué consejo amable y realista le darías desde esa montaña vecina al escalador que hoy lleva tus botas?"
        ],
        "practica": "Cuando te sientas atascado hoy, pregúntate: «Si un buen amigo estuviera exactamente en este punto de su montaña, ¿qué sendero lateral le señalaría yo?»."
    },
    {
        "slug": "casa-y-muebles",
        "titulo": "La casa firme y los muebles que cambian",
        "proceso": "yo",
        "tipo": "Metáfora",
        "tiempo": "3 min",
        "herramienta": "met-la-casa-y-los-muebles.html",
        "fuente": "Wilson, K. G. y Luciano, M. C. (2002). Terapia de Aceptación y Compromiso (ACT): Un tratamiento conductual orientado a los valores. Pirámide.",
        "resumen": "Distinguir entre los muebles que entran o estorban dentro de las habitaciones (emociones, etiquetas, recuerdos) y la casa espaciosa que los alberga.",
        "lectura": [
            "Imagina una casa amplia, luminosa y bien cimentada. A lo largo de los años, a esa casa han entrado toda clase de muebles: algunos cómodos y hermosos que tú mismo elegiste, otros antiguos heredados de la infancia que nadie pidió, y alguno pesado y con resortes rotos que hoy resulta muy incómodo en un rincón de la sala.",
            "Cuando sufrimos, cometemos dos errores comprensibles: primero, llegamos a creer que ese mueble viejo y feo es la casa entera («soy mi depresión», «soy mi inseguridad»); y segundo, nos quedamos encerrados todo el día frente a ese rincón intentando romper el mueble a martillazos, dejando sin usar el jardín, la cocina y el estudio.",
            "Por más pesado, ruidoso o polvoriento que sea un mueble, un mueble jamás se convierte en la casa ni reduce el tamaño de sus muros. Tú eres la casa completa; ese pensamiento o ese dolor es solo un mueble más ocupando una esquina mientras tú eliges qué habitación habitar hoy."
        ],
        "clave": "Ningún mueble —ni el más incómodo ni el más hermoso— se convierte jamás en la casa que lo aloja.",
        "preguntas": [
            "¿Qué «mueble incómodo» o qué «mueble viejo heredado» ha estado llamando toda tu atención en un rincón de tu casa hoy?",
            "Además de ese mueble molesto, ¿qué otros muebles valiosos (afectos, intereses, cualidades tuyas) siguen dentro de tu casa?",
            "¿Qué habitación valiosa de tu vida eliges abrir y usar hoy sin esperar a que desaparezca el mueble del rincón?"
        ],
        "practica": "Nombra hoy una etiqueta dura con la que suelas definirte y reformúlala diciendo: «Ese es un mueble antiguo en una esquina; yo soy toda la casa»."
    },

    # ==================== 5. CLARIFICACIÓN DE VALORES (6) ====================
    {
        "slug": "brujula-de-valores",
        "titulo": "La brújula frente al mapa de metas: viajar hacia el Este",
        "proceso": "valores",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "act-brujula-de-valores.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 8: Values as a Compass / Heading East). Guilford Press.",
        "resumen": "Comprender la diferencia crucial entre una meta (un destino que se tacha al llegar) y un valor (una dirección de brújula que está disponible en cada paso).",
        "lectura": [
            "En ACT es fundamental no confundir los valores con las metas. Una meta es como llegar a una ciudad en el mapa, casarse, obtener un título o terminar un informe: es algo que está en el futuro y que, una vez alcanzado, se tacha de la lista y se termina.",
            "Un valor, en cambio, es como la dirección «hacia el Este» en una brújula: por más kilómetros que camines hacia el Este, jamás llegas a un cartel donde se acabe el Este; siempre puedes dar un paso más en esa dirección. «Casarse» es una meta; «ser una pareja amorosa, presente y leal» es un valor que se vive hoy, mañana y dentro de veinte años.",
            "Esto tiene una consecuencia liberadora: las metas dependen de muchas cosas que no controlas y a veces se demoran o se cierran. Pero tu brújula de valores depende cien por ciento de ti y está disponible en este preciso minuto, incluso en medio de un día difícil."
        ],
        "clave": "Las metas están en el futuro y se tachan al llegar; tus valores son una brújula que puedes poner en práctica en los próximos cinco minutos.",
        "preguntas": [
            "En el área que más te preocupa hoy, ¿cuál es la «meta» externa que buscabas y cuál es el «valor» (la cualidad de persona que quieres ser) detrás de ella?",
            "Aunque la meta externa todavía no se haya cumplido, ¿de qué manera puedes caminar un paso «hacia tu Este» hoy mismo?",
            "¿Qué tres palabras resumen la dirección de tu brújula personal para esta etapa de tu vida?"
        ],
        "practica": "Antes de empezar tu próxima tarea o conversación de hoy, pregúntate: «Más allá del resultado, ¿qué cualidad mía quiero poner en juego aquí?»."
    },
    {
        "slug": "jardin-de-valores",
        "titulo": "El jardín de la vida: dónde pones tu regadera hoy",
        "proceso": "valores",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-jardin-de-valores.html",
        "fuente": "Wilson, K. G. y Luciano, M. C. (2002). Terapia de Aceptación y Compromiso (ACT): La metáfora del jardín. Pirámide.",
        "resumen": "Notar cómo descuidamos nuestros canteros valiosos cuando pasamos el día arrodillados arrancando malezas inevitables.",
        "lectura": [
            "Imagina que eres el jardinero del único terreno que se te ha dado: tu propia vida. En ese jardín tú elegiste sembrar semillas que te importan de corazón: el cantero de tus vínculos afectivos, el de tu vocación, el de tu salud y el de tu crecimiento personal.",
            "Sin embargo, como en toda tierra fértil bajo el sol, entre tus plantas brotan también malezas sin que nadie las siembre: miedos, recuerdos espinosos, dudas y cansancio. Si decides que no volverás a regar tus flores hasta que no quede ni un solo tallo de maleza en todo el terreno, pasarás los años de rodillas escarbando barro y, cuando levantes la vista, tus rosales se habrán secado por falta de agua.",
            "Las plantas de tu jardín no crecen porque odies la maleza; crecen únicamente allí donde viertes el agua de tu tiempo, tu presencia y tus manos hoy."
        ],
        "clave": "Tus flores no florecen por el tiempo que pasas peleando con la maleza, sino por el agua de atención y cuidado que les das hoy.",
        "preguntas": [
            "¿Cuáles son los tres o cuatro «canteros» más importantes de tu jardín vital en este momento?",
            "¿Qué cantero ha recibido menos agua últimamente porque estabas ocupado peleando con alguna «maleza» interna?",
            "¿Con qué pequeño gesto de diez minutos puedes echarle hoy un poco de agua fresca a ese cantero descuidado?"
        ],
        "practica": "Elige hoy un solo cantero de tu jardín y dedícale una acción concreta de riego antes de que termine el día, dejando la maleza tranquila a un lado."
    },
    {
        "slug": "ochenta-anos",
        "titulo": "El brindis de tus ochenta años: por qué quieres ser recordado",
        "proceso": "valores",
        "tipo": "Ejercicio experiencial",
        "tiempo": "5 min",
        "herramienta": "met-los-ochenta-anos.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Eighty-First Birthday / Epitaph Exercise). · Harris, R. (2009).",
        "resumen": "Mirar nuestra vida actual en perspectiva desde una celebración futura para distinguir qué es urgente en apariencia y qué es verdaderamente importante.",
        "lectura": [
            "Imagina que han pasado las décadas y hoy se celebra tu cumpleaños número ochenta. En un lugar cálido se han reunido las personas cuyas vidas tocaste a lo largo de tu camino: familia, amistades, compañeros de ruta. En un momento de la velada, alguien que te conoce bien se pone de pie, levanta su copa y dice unas palabras sobre quién fuiste tú en su vida.",
            "No te detengas en qué dirías por quedar bien, sino en qué te conmovería escuchar en el fondo de tu corazón si pudieras elegir libremente tu huella. Casi nadie sueña con que en sus ochenta años digan: «Logró no sentir nunca nervios y jamás cometió un error». En cambio, anhelamos escuchar que estuvimos presentes, que amamos con valentía, que nos levantamos y que fuimos fieles a lo que nos importaba.",
            "La buena noticia es que ese discurso todavía no está tallado en piedra: cada decisión pequeña que tomas hoy escribe un renglón real de esa historia."
        ],
        "clave": "Mirar desde el horizonte de tus ochenta años despeja al instante el ruido del día y muestra qué merece hoy tu valentía.",
        "preguntas": [
            "Si alguien muy querido levantara su copa en tus ochenta años para agradecer cómo estuviste presente en su vida, ¿qué te gustaría de corazón que pudiera decir?",
            "En tu trabajo, estudio o contribución al mundo, ¿qué huella o actitud tuya querrías que se recordara?",
            "Mirando tu semana actual desde esa mesa de tus ochenta años, ¿qué pequeño giro te pide hoy tu vida para acercarte a esa persona?"
        ],
        "practica": "Redacta en tres líneas el brindis que te gustaría inspirar y léelo al comenzar la semana para orientar tu agenda."
    },
    {
        "slug": "diana-de-valores",
        "titulo": "La diana de valores (Bull's-Eye): cuán cerca del centro vives hoy",
        "proceso": "valores",
        "tipo": "Hoja de reflexión",
        "tiempo": "4 min",
        "herramienta": "act-diana-de-valores.html",
        "fuente": "Lundgren, T., Luoma, J. B., Dahl, J., Strosahl, K. y Melin, L. (2012). The Bull's-Eye Values Survey. Cognitive and Behavioral Practice, 19(4), 518-526.",
        "resumen": "Ubicar en los cuatro cuadrantes de la diana qué tan alineada estuvo nuestra conducta de esta semana con nuestros valores reales.",
        "lectura": [
            "Imagina una diana de tiro al blanco dividida en cuatro grandes cuadrantes que abarcan toda la vida: (1) Trabajo, estudio o contribución; (2) Relaciones e intimidad; (3) Salud física y autocuidado; y (4) Tiempo libre, recreación y comunidad.",
            "En esta diana, dar en el centro exacto no significa que todo te haya salido fácil ni que los demás hayan hecho lo que tú querías; significa que tu propia conducta de esta semana reflejó de lleno a la persona que eliges ser en esa área. Estar en el anillo exterior, en cambio, significa que tus días se fueron en automático o evitando el malestar, lejos de lo que valoras.",
            "Mirar dónde cayeron tus cuatro dardos esta semana no es un tribunal para culparte; es un mapa amable y preciso para elegir qué dardo quieres acercar un solo anillo hacia el centro en las próximas cuarenta y ocho horas."
        ],
        "clave": "El centro de la diana no mide tu suerte ni tu falta de miedo; mide cuánto se parecen tus pasos de hoy a lo que amas.",
        "preguntas": [
            "Del 1 (borde lejano) al 7 (centro exacto), ¿dónde ubicarías hoy tu dardo en Trabajo/Vocación, en Relaciones, en Salud y en Tiempo libre?",
            "En el cuadrante donde el dardo quedó más lejos del centro, ¿qué pensamiento o incomodidad actuó como obstáculo?",
            "¿Qué acción concreta y pequeña realizarás en los próximos dos días para acercar ese dardo un anillo hacia el blanco?"
        ],
        "practica": "Dibuja un círculo pequeño dividido en cuatro en tu agenda del lunes y marca un punto en cada cuadrante para elegir tu enfoque de la semana."
    },
    {
        "slug": "punto-dulce",
        "titulo": "El ejercicio del punto dulce: cuando la vida tiene sabor",
        "proceso": "valores",
        "tipo": "Ejercicio experiencial",
        "tiempo": "4 min",
        "herramienta": "act-punto-dulce.html",
        "fuente": "Wilson, K. G. y DuFrene, T. (2009). Mindfulness for Two: An Acceptance and Commitment Therapy Approach to Mindfulness in Psychotherapy. New Harbinger.",
        "resumen": "Entrar al contacto con los valores no desde las reglas racionales del «debería», sino recordando un instante real de plenitud y dulzura vital.",
        "lectura": [
            "Cuando nos preguntan de frente «¿cuáles son tus valores?», nuestra mente racional suele responder recitando deberes aprendidos: «debería ser más productivo, debería esforzarme más, debería quedar bien con todos». Pero los deberes fríos rara vez encienden el corazón.",
            "Kelly Wilson propuso buscar los valores en otro lugar: en lo que él llama un momento de «punto dulce» (Sweet Spot). Trae a tu memoria algún instante real de tu vida —no hace falta que sea un logro grandioso; puede ser una caminata al atardecer, una charla en la cocina, un gesto de ternura o una tarde creando algo— en el que sentiste que todo encajaba y que la vida tenía verdadero sabor.",
            "Quédate un momento dentro de ese recuerdo sintiendo cómo responde tu pecho al evocarlo. Aquellas cualidades que estaban encendidas en ese instante —cercanía, calma, curiosidad, libertad, cuidado— son tus valores auténticos hablándote sin disfraces."
        ],
        "clave": "Tus valores reales no tienen voz de sargento que exige «deberías»; tienen el sabor cálido de los momentos en que te sentiste plenamente vivo.",
        "preguntas": [
            "¿Qué momento real de tu vida (grande o sencillo) viene a tu memoria cuando buscas un instante de «punto dulce» y plenitud?",
            "¿Qué ingrediente o cualidad tuya estaba viva en esa escena (conexión, presencia, creatividad, cuidado, libertad)?",
            "¿De qué manera sencilla puedes invitar hoy una gota de ese mismo sabor a tu día actual?"
        ],
        "practica": "Dedica hoy quince minutos a recrear deliberadamente un pequeño momento con el ingrediente principal de tu «punto dulce»."
    },

    # ==================== 6. ACCIÓN COMPROMETIDA (7) ====================
    {
        "slug": "pasajeros-del-autobus",
        "titulo": "El autobús y los pasajeros ruidosos: quién lleva el volante",
        "proceso": "accion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "met-el-bus.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 6: Passengers on the Bus Metaphor). Guilford Press.",
        "resumen": "Mantener las manos en el volante rumbo al cartel de nuestros valores aunque los pasajeros de atrás se levanten a amenazar y hacer ruido.",
        "lectura": [
            "Imagina que eres el conductor de un autobús cuyo cartel delantero lleva escrito el rumbo de tus valores. A lo largo de tu historia han ido subiendo al autobús distintos pasajeros: algunos amables, y otros francamente intimidantes, con chaquetas de cuero y frases hirientes —tus miedos antiguos, tu crítico interno, tus recuerdos de vergüenza y tus dudas—.",
            "Mientras conduces por las calles conocidas y seguras donde ellos mandan, los pasajeros van sentados en el fondo bastante callados. Pero en el instante mismo en que pones la luz de giro para doblar hacia una avenida que a ti te importa de verdad, los pasajeros se levantan de golpe, caminan por el pasillo hasta tu asiento y te gritan al oído: «¡Si doblas por ahí te irá pésimo! ¡Vuelve atrás ahora mismo!».",
            "Si detienes el autobús para pelear con ellos e intentar bajarlos a empujones, el autobús no avanza ni un metro. Y si haces el trato de doblar donde ellos ordenan para que se vuelvan a sentar al fondo, les has entregado el volante. La única salida es permitirles gritar todo lo que quieran en el pasillo mientras tus manos siguen girando el volante hacia tu rumbo."
        ],
        "clave": "Los pasajeros más ruidosos solo gritan cuando estás avanzando hacia algo importante; déjalos hablar en el pasillo y conserva el volante.",
        "preguntas": [
            "¿Qué dice hoy el cartel luminoso del frente de tu autobús (hacia qué dirección valiosa quieres conducir)?",
            "¿Qué dos o tres «pasajeros ruidosos» se acercan al asiento del conductor a amenazarte apenas intentas girar hacia ese rumbo?",
            "¿Estás dispuesto a dejarlos viajar hablando en el pasillo mientras tú mantienes las manos en el volante?"
        ],
        "practica": "Cuando hoy sientas miedo justo antes de hacer algo valioso, sonríe y di: «Los pasajeros se levantaron a gritar porque acabo de doblar hacia donde me importa»."
    },
    {
        "slug": "punto-de-eleccion",
        "titulo": "El punto de elección: movimientos de acercamiento y de alejamiento",
        "proceso": "accion",
        "tipo": "Hoja de reflexión",
        "tiempo": "4 min",
        "herramienta": "act-camino-de-vida.html",
        "fuente": "Harris, R. (2019). ACT Made Simple (2.ª ed., The Choice Point). · Ciarrochi, Bailey y Harris (2014). · Polk y Schoendorff (2014, The ACT Matrix).",
        "resumen": "Mapear en una bifurcación clara cada momento difícil para distinguir entre actuar para escapar del dolor y actuar para construir la vida que importa.",
        "lectura": [
            "Decenas de veces al día llegamos a una encrucijada que en ACT llamamos el «Punto de Elección». Abajo están la situación que enfrentas hoy y los pensamientos y emociones difíciles que se disparan dentro de ti. Y frente a tus pies se abren exactamente dos flechas posibles.",
            "La flecha hacia la izquierda son los «movimientos de alejamiento»: todo aquello que hacemos gobernados por la urgencia de aliviar, evitar o anestesiar el malestar del momento (postergar, encerrarnos, atacar, revisar mil veces, rendirnos). Dan un respiro de diez minutos, pero nos alejan de la persona que queremos ser.",
            "La flecha hacia la derecha son los «movimientos de acercamiento»: las acciones grandes o pequeñas que nos acercan a nuestros valores y a la vida que queremos construir, llevando el malestar con nosotros. Cada vez que notas que estás en la bifurcación, recuperas el poder de elegir qué flecha caminar."
        ],
        "clave": "En cada momento difícil hay dos caminos: actuar para huir del malestar un rato, o actuar para acercarte a la persona que eliges ser.",
        "preguntas": [
            "¿Cuál es la situación difícil y el anzuelo interno (pensamiento o emoción) que hoy te pone frente al Punto de Elección?",
            "¿Cuáles suelen ser tus «movimientos de alejamiento» automáticos cuando ese anzuelo tira de ti?",
            "¿Cuál es hoy un «movimiento de acercamiento» concreto que refleje a la persona que quieres ser en esta situación?"
        ],
        "practica": "Dibuja una pequeña «V» con dos flechas en un papel hoy y escribe en la flecha derecha la acción que elegiste para esta tarde."
    },
    {
        "slug": "paso-mas-pequeno",
        "titulo": "De FEAR a DARE: el paso más pequeño posible",
        "proceso": "accion",
        "tipo": "Hoja de reflexión",
        "tiempo": "4 min",
        "herramienta": "act-fear-a-dare.html",
        "fuente": "Harris, R. (2009). ACT Made Simple (Barriers to Action: FEAR & DARE). · Hayes, Strosahl y Wilson (2012).",
        "resumen": "Destrabar el bloqueo ante la acción identificando las cuatro barreras clásicas (FEAR) y reduciendo el paso hasta que sea realizable hoy.",
        "lectura": [
            "Cuando sabemos qué nos importa pero aun así no logramos movernos, casi siempre está operando alguna de las cuatro barreras que en ACT se resumen en la sigla FEAR: Fusión con pensamientos de incapacidad; Exceso de expectativas o metas gigantescas; Aversión a la incomodidad; o lejanía (Remoteness) respecto de nuestros valores reales.",
            "Su antídoto directo es DARE: Defusión de las excusas mentales; Aceptación de que habrá incomodidad en el arranque; Metas Realistas ajustadas a los recursos reales de hoy; y Abrazar (Embrace) el valor que le da sentido al esfuerzo.",
            "La pregunta mágica de la acción comprometida nunca es «¿cómo resuelvo todo el problema de un salto?», sino: «Con la energía y el tiempo que tengo realmente hoy, ¿cuál es el paso más pequeño, imperfecto y concreto que sí estoy dispuesto a dar en los próximos diez minutos?»."
        ],
        "clave": "Un paso diminuto e imperfecto dado hoy en tu dirección valiosa vale más que un plan perfecto que nunca arranca.",
        "preguntas": [
            "De las cuatro barreras (Fusión con «no puedo», Meta demasiado grande, Evitar la incomodidad, o Desconexión del valor), ¿cuál te está frenando más hoy?",
            "Si partes la meta a la mitad —y luego otra vez a la mitad— hasta que dure menos de diez minutos, ¿cómo queda ese primer paso?",
            "¿A qué hora exacta de hoy darás ese paso pequeño llevando contigo las ganas o el desgano que haya?"
        ],
        "practica": "Aplica hoy la regla de los cinco minutos: comprométete únicamente a realizar los primeros cinco minutos de la acción valiosa que venías postergando."
    },
    {
        "slug": "vasija-de-barro",
        "titulo": "Metas de persona viva frente a la trampa del perfeccionismo",
        "proceso": "accion",
        "tipo": "Hoja de reflexión",
        "tiempo": "4 min",
        "herramienta": "act-perfeccionismo.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). (Dead Man's Rule). · Lins et al. (2024). ACT for Perfectionism.",
        "resumen": "Reemplazar la exigencia rígida de «no equivocarme ni sentir dudas» por el compromiso vivo de aprender, ensayar y reparar con compasión.",
        "lectura": [
            "El psicólogo Ogden Lindsley formuló una regla clínica inolvidable llamada la «Regla del hombre muerto»: si lo que te propones como meta es algo que un cadáver puede hacer mejor que tú, entonces no es una meta para una persona viva. Un cadáver jamás comete un error, jamás tiembla al hablar en público, jamás siente ansiedad y jamás dice una frase torpe.",
            "El perfeccionismo nos vende el espejismo de que exigimos tanto porque valoramos la excelencia, pero en la práctica funciona como una jaula de evitación: por pánico a que la vasija de barro salga con una grieta, dejamos de moldear el barro, posponemos entregas y nos tratamos con látigo ante cualquier tropiezo humano.",
            "La acción comprometida en ACT cambia las metas de cadáver («no fallar nunca, no sentir nervios») por metas de persona viva: animarte a entregar el borrador imperfecto, hablar aunque tiemble la voz y acompañarte como un buen maestro que corrige con firmeza y calidez a la vez."
        ],
        "clave": "No equivocarse ni sentir miedo solo lo logra quien no está vivo; vivir con sentido incluye el permiso de hacer las cosas de manera humana e imperfecta.",
        "preguntas": [
            "¿En qué área de tu vida te has estado imponiendo una «regla de persona muerta» (no equivocarme, no dudar, no mostrar vulnerabilidad)?",
            "¿Qué precio en postergación, agotamiento o dureza contigo mismo te ha cobrado esa exigencia de perfección?",
            "¿Qué «paso imperfecto de persona viva» te das permiso de ensayar esta semana?"
        ],
        "practica": "Realiza hoy deliberadamente una tarea al 85% de perfección y entrégala o termínala a tiempo, practicando soltar el 15% de sobre-revisión ansiosa."
    },
    {
        "slug": "dial-de-disposicion",
        "titulo": "El dial de la disposición frente al dial del malestar",
        "proceso": "accion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "act-dial-disposicion.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Cap. 5: Two Scales Metaphor). Guilford Press.",
        "resumen": "Quitar la mano de la perilla incontrolable de la ansiedad para accionar la perilla de la disposición a abrir espacio y avanzar.",
        "lectura": [
            "Imagina un tablero de instrumentos frente a ti con dos grandes perillas graduadas de cero a diez. La primera perilla se llama «Malestar» (ansiedad, tristeza, recuerdos, cansancio). Casi todos intentamos meter la mano para bajar esa perilla a cero antes de salir a vivir; pero esa perilla tiene un resorte oculto: cuanto más la fuerzas hacia abajo, más se traba y más sube.",
            "Al lado hay una segunda perilla que casi nadie mira y que se llama «Disposición» (apertura a sentir lo que haya con tal de hacer lo que importa). A diferencia de la primera, esta segunda perilla no tiene trabas ni depende del clima: es la única del tablero que está conectada directamente a tu elección.",
            "Cuando la disposición está en cero, tu único proyecto del día es que el malestar baje. Cuando subes tu disposición a ocho, nueve o diez, el malestar puede subir o bajar como quiera, pero tú vuelves a ser dueño de tus pasos."
        ],
        "clave": "La perilla del malestar no obedece a tu voluntad, pero la perilla de tu disposición a avanzar está cien por ciento en tus manos.",
        "preguntas": [
            "Del 0 al 10, ¿en cuánto está hoy tu perilla de malestar y cuánta fuerza has gastado tratando de forzarla hacia abajo?",
            "En la situación valiosa que tienes por delante hoy, ¿a qué número eliges subir tu perilla de Disposición?",
            "¿Qué sensación o pensamiento concreto estás dispuesto a llevar contigo hoy al subir ese dial?"
        ],
        "practica": "Antes de enfrentar un reto hoy, haz el gesto con los dedos de girar una perilla imaginaria hacia el 10 diciendo: «Subo mi disposición al máximo»."
    },
    {
        "slug": "cruzar-el-pantano",
        "titulo": "Cruzar el pantano cuando la montaña está del otro lado",
        "proceso": "accion",
        "tipo": "Metáfora",
        "tiempo": "4 min",
        "herramienta": "act-por-donde-entrar.html",
        "fuente": "Hayes, S. C., Strosahl, K. D. y Wilson, K. G. (1999). Acceptance and Commitment Therapy (Swamp Metaphor, cap. 9). Guilford Press.",
        "resumen": "Reconocer la diferencia entre revolcarse en el barro por gusto y atravesar un pantano difícil porque del otro lado está la montaña que elegimos subir.",
        "lectura": [
            "Imagina que emprendes el camino hacia una montaña hermosa que tú mismo elegiste escalar. Llevas tu mochila y tu mapa, pero a mitad del sendero descubres algo que no aparecía en las fotos: entre tú y la base de la montaña se extiende un pantano ancho, frío y lleno de barro.",
            "Si en ese momento alguien te preguntara: «¿Te gusta el barro frío?», tu respuesta honesta sería: «Por supuesto que no». Si el pantano fuera el destino final, lo más sensato sería dar media vuelta e irse a casa. Pero el pantano no es el destino: es simplemente el terreno real que está entre tus botas y la montaña que amas.",
            "En ACT jamás abrimos espacio al dolor por masoquismo ni porque nos guste sufrir. Entramos al pantano de una conversación difícil, de un duelo, de una exposición al miedo o de un cambio vital únicamente cuando sabemos con claridad qué montaña valiosa nos espera del otro lado."
        ],
        "clave": "No entramos al pantano porque nos guste el barro, sino porque del otro lado está la montaña que elegimos para nuestra vida.",
        "preguntas": [
            "¿Cuál es el «pantano» incómodo (miedo, esfuerzo, conversación pendiente o incertidumbre) que hoy aparece frente a tus botas?",
            "¿Cuál es la «montaña valiosa» que está del otro lado y por la cual sí vale la pena mojarse los pies en este tramo?",
            "¿Qué primer paso firme dentro del sendero vas a dar esta semana manteniendo la vista en tu montaña?"
        ],
        "practica": "Completa hoy en una frase tu brújula de travesía: «Elijo atravesar la incomodidad de [...] porque al otro lado está mi valor de [...]»."
    },
])
