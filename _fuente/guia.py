# -*- coding: utf-8 -*-
"""
Arma guia.html: para qué sirve cada hoja, en qué casos rinde, con qué va antes
o después, y dónde conviene tener cuidado.

No es una herramienta: es la hoja de ruta del profesional. Por eso no lleva kit,
ni guardado, ni notas. Se reconstruye sola al correr construir.py.

    python guia.py
"""
from pathlib import Path

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI.parent

COLORES = {
    "Metáforas vivas":      "#c26a4e",
    "Psicología positiva":  "#c9962f",
    "ACT":                  "#3f9b86",
    "DBT":                  "#5f77b8",
    "Cognitivo-conductual": "#2f6f8f",
}

# Cada hoja: archivo, título, para qué (el mecanismo, en una línea),
# en qué casos rinde, cómo se encadena y qué cuidado tiene.
GUIA = [
("Metáforas vivas", [
 {"archivo":"met-el-tablero.html", "titulo":"El tablero", "etq":"Yo observador",
  "paraque":"Saca a la persona de la posición de pieza. Entrena el yo como contexto: no cambia el "
            "contenido, cambia desde dónde se lo mira.",
  "conviene":[
    "Fusión con la historia sobre uno mismo: «soy ansioso», «soy el que arruina las cosas».",
    "Identidad organizada alrededor de un diagnóstico, un rol o un fracaso.",
    "Lucha interna crónica entre lo que se quiere creer y lo que aparece.",
    "Cuando cuestionar el contenido de frente endurece la creencia."],
  "secuencia":[
    ("Después de", "El costo de la lucha, para que el cambio de posición no se lea como un truco más."),
    ("Junto a", "Hojas en el arroyo: el tablero da la metáfora, el arroyo da la práctica."),
    ("Abre paso a", "La brújula de valores y El bus.")],
  "cuidado":"Si se usa para que las piezas negras salgan del tablero, sigue siendo una jugada "
            "dentro de la partida. El indicador es que la persona pregunte si «funcionó»."},

 {"archivo":"met-jardin-de-valores.html", "titulo":"El jardín de valores", "etq":"Valores",
  "paraque":"Clarificación por elección y no por escritura: seis surcos de veinte, y la distancia "
            "entre lo que importa y lo que efectivamente se regó.",
  "conviene":[
    "Cuando preguntar «¿cuáles son tus valores?» produce silencio o discurso aprendido.",
    "Personas poco verbales, o que no escriben, o que se pierden en la brújula.",
    "Sobrecarga con culpa difusa: todo importa y nada se mueve.",
    "Vida partida en dos, con todo el combustible en un solo frente."],
  "secuencia":[
    ("Alternativa a", "La brújula de valores, cuando hace falta algo más concreto y menos verbal."),
    ("Después va", "El bus, o activación conductual si lo que falla es arrancar.")],
  "cuidado":"Si no logra sembrar ni tres surcos, la conversación no es sobre valores sino sobre el "
            "aplanamiento. Conviene tamizar sintomatología depresiva antes de seguir."},

 {"archivo":"met-la-cuerda.html", "titulo":"La cuerda y el monstruo", "etq":"Aceptación",
  "paraque":"Que la persona compruebe en pantalla que la fuerza alimenta la lucha, y que soltar no "
            "es una forma disimulada de ganar.",
  "conviene":[
    "Evitación experiencial franca: ansiedad, pánico, rabia, ganas de consumir, recuerdos.",
    "Quien «ha intentado todo» y sigue igual.",
    "Cuando la agenda de control está tan instalada que cualquier técnica se convierte en arma."],
  "secuencia":[
    ("Junto a", "El costo de la lucha: uno hace el inventario, el otro lo hace sentir."),
    ("Después", "Hojas en el arroyo o Soltar el anzuelo, y luego El bus.")],
  "cuidado":"Si soltar se entiende como resignarse, hay que retroceder al inventario de costos. La "
            "hoja lo deja explícito: el monstruo sigue ahí."},

 {"archivo":"met-hojas-en-el-arroyo.html", "titulo":"Hojas en el arroyo", "etq":"Defusión",
  "paraque":"No entrena calmarse ni dejar de pensar: entrena notar que uno se enganchó y volver. "
            "Ese ciclo es la repetición útil, y por eso la hoja cuenta enganches.",
  "conviene":[
    "Rumiación depresiva y preocupación anticipatoria: es su indicación más clara.",
    "Fusión que ya resistió la reestructuración: hizo el registro completo y sigue enganchado.",
    "Quien discute con su propia mente y siempre pierde.",
    "Como preparación, cuando el enganche impide arrancar cualquier conducta."],
  "secuencia":[
    ("Después de", "El costo de la lucha: sin desesperanza creativa se escucha como otra técnica "
                   "para sacarse cosas de encima."),
    ("Junto a", "El tablero, que instala la posición desde la que se mira."),
    ("Antes de", "La escalera de exposición y El bus.")],
  "cuidado":"El botón de enganche se puede quitar desde la hoja. Conviene dejarlo cuando marcar ayuda a que volver sea un acto y no una idea, y quitarlo cuando el botón se vuelve puntaje y la persona empieza a marcar para quedar bien; sin él, el enganche se pregunta después, sabiendo que el reporte retrospectivo siempre queda corto. La trampa más frecuente no es engancharse: es mirar el agua para no ver las hojas. Eso es evitación con buena presentación, y deja la agenda de control intacta. Lo que se entrena es mirar la hoja de frente y dejarla pasar igual. Por encima de 70 u 80 de activación no hay práctica contemplativa que funcione: ahí va "
            "la Tarjeta de crisis. Con disociación o intrusiones traumáticas, ojos abiertos mirando "
            "el arroyo de la pantalla, minuto y medio y anclaje. En psicosis activa, la instrucción "
            "de observar los pensamientos como objetos puede confundir."},

 {"archivo":"met-el-bus.html", "titulo":"El bus y los pasajeros", "etq":"Acción comprometida",
  "paraque":"Comprobar que el bus se mueve con los pasajeros gritando, y que discutir con ellos "
            "cuesta energía y no suma kilómetros.",
  "conviene":[
    "Evitación conductual cuando los valores ya están claros.",
    "Procrastinación y el «cuando me sienta mejor, lo hago».",
    "Ansiedad social y de desempeño: los gritos suben justo al acercarse a lo que importa.",
    "Quien se detiene a razonar con su mente cada vez que aparece un obstáculo."],
  "secuencia":[
    ("Necesita antes", "La brújula o El jardín: sin destino, el bus se vuelve autoexigencia."),
    ("Después de", "Defusión, si el enganche es muy alto."),
    ("Junto a", "La escalera de exposición cuando la evitación es situacional.")],
  "cuidado":"Si el destino es prestado, la hoja convierte el valor ajeno en un plan y aprieta más "
            "la trampa. Vale la pena revisar de quién es la dirección."},

 {"archivo":"met-los-ochenta-anos.html", "titulo":"Los ochenta años", "etq":"Valores",
  "paraque":"Separar logro de vínculo. Nadie se levanta a decir un logro: se levantan a decir cómo "
            "los trataste. Y la mesa muestra la distancia con el último mes.",
  "conviene":[
    "Vida organizada enteramente por rendimiento.",
    "Vacío con buen funcionamiento aparente.",
    "Decisiones vitales grandes, y revisiones de rumbo.",
    "Cuando los valores declarados suenan a deber y no a elección."],
  "secuencia":[
    ("Después de", "La brújula, cuando lo declarado parece puesto por otros."),
    ("Antes de", "El bus, para que la frase más apagada se convierta en conducta.")],
  "cuidado":"Es la hoja que más culpa moviliza, y la culpa produce evitación, no cambio. Nombrar "
            "explícitamente que la distancia es información y no un veredicto, y bajar de inmediato "
            "a una acción pequeña. No usarla en duelo reciente agudo ni con riesgo sin preparar."},

 {"archivo":"met-el-poligrafo.html", "titulo":"El polígrafo", "etq":"Desesperanza creativa",
  "paraque":"Demuestra la agenda de control desde dentro del mecanismo: cada intento de bajar la "
            "activación la dispara, y sube el piso al que vuelve. No lo dice el profesional, lo "
            "dice el papel de registro.",
  "conviene":[
    "Reglas del tipo «no debo sentir esto» y «si lo siento, algo anda mal».",
    "Ansiedad por la ansiedad, y pánico con miedo a las propias sensaciones.",
    "Quien llega pidiendo técnicas para dejar de sentir.",
    "Cuando toda habilidad que se enseña se convierte en otra arma de control."],
  "secuencia":[
    ("Junto a", "El costo de la lucha: uno hace el inventario, el polígrafo lo hace ocurrir en vivo."),
    ("Antes de", "La cuerda y el monstruo, que trabaja lo mismo desde el esfuerzo y no desde la regla."),
    ("Abre paso a", "Hojas en el arroyo y a la brújula de valores.")],
  "cuidado":"El punto es la inutilidad de la agenda de control, no la desesperanza a secas. Si la "
            "persona sale con «entonces no hay nada que hacer», faltó cerrar hacia valores en la "
            "misma sesión. Con pánico activo, no usarla antes de tener anclaje disponible."},

 {"archivo":"met-la-palabra-repetida.html", "titulo":"La palabra repetida", "etq":"Defusión",
  "paraque":"Vacía una etiqueta de significado por repetición hasta que solo queda el sonido. "
            "Toca la fusión con el autoconcepto sin discutir ni una vez el contenido.",
  "conviene":[
    "Autoetiquetas fusionadas: «soy un inútil», «soy débil», «soy un fracaso».",
    "Cuando la reestructuración ya se hizo completa y la creencia no se movió.",
    "Personas poco verbales o adolescentes, porque no exige argumentar nada.",
    "Como demostración rápida y corporal de qué es la defusión."],
  "secuencia":[
    ("Después de", "El costo de la lucha o El polígrafo, para que no se lea como un truco de autoayuda."),
    ("Junto a", "Soltar el anzuelo, que trabaja la misma fusión desde la conducta."),
    ("Antes de", "Hojas en el arroyo, que la lleva a práctica sostenida.")],
  "cuidado":"Es para un descriptor de uno mismo, de una o dos palabras. No usarla con palabras "
            "ligadas a trauma, a abuso o al nombre de quien hizo daño: repetir eso no defusiona, "
            "revictimiza. Tiene que decirse en voz alta, así que hace falta privacidad real. Si la "
            "calificación no baja, no es un fracaso: se mira qué la sostiene."},

 {"archivo":"met-la-radio.html", "titulo":"La radio que no se apaga", "etq":"Defusión",
  "paraque":"Separa hacer de estar en silencio. Lo que mide es la tarea terminada con el ruido "
            "encendido, y no el ruido apagado.",
  "conviene":[
    "Quien condiciona actuar a que la mente se calle: «cuando deje de pensar en eso, lo hago».",
    "Rumia de fondo permanente que no llega a impedir del todo, pero desgasta.",
    "Ansiedad de desempeño y bloqueo al empezar.",
    "Como puente entre la defusión y la acción, cuando ya se practicó observar."],
  "secuencia":[
    ("Después de", "Hojas en el arroyo: primero observar, después hacer con eso puesto."),
    ("Junto a", "El bus y los pasajeros, que es la misma lección a escala de vida."),
    ("Antes de", "Activación conductual o La escalera de exposición.")],
  "cuidado":"No es entrenar a ignorar. Si la persona termina la tarea disociando o poniéndose en "
            "automático, eso es evitación y conviene preguntarlo directamente. Con alucinaciones "
            "auditivas la metáfora de la radio puede tomarse literal: revisar antes de proponerla."},

 {"archivo":"met-el-hoyo.html", "titulo":"El hombre en el hoyo", "etq":"Desesperanza creativa",
  "paraque":"Separa la sensación de avanzar del avance. La barra se llena mientras se cava y se "
            "vacía al soltar el botón; la profundidad es lo único que se queda.",
  "conviene":[
    "Primera o segunda sesión, para instalar desesperanza creativa sin discurso.",
    "Quien lleva años haciendo cosas para resolverlo y sigue exactamente igual.",
    "Conductas de seguridad que alivian en el momento y sostienen el problema.",
    "Comprobación compulsiva y búsqueda interminable de información."],
  "secuencia":[
    ("Es puerta de entrada", "Sirve para abrir el trabajo, incluso antes de tener formulación."),
    ("En lugar de", "El costo de la lucha, cuando escribir e inventariar cansa o aburre."),
    ("Abre paso a", "La cuerda y el monstruo, y después a la brújula de valores.")],
  "cuidado":"La metáfora no ofrece salida y no hay que fabricarle una: su trabajo es que la pala "
            "deje de parecer la herramienta. Soltar la pala no es rendirse, y conviene decirlo con "
            "todas las letras. Si aparece desesperanza con contenido de muerte, se detiene la hoja "
            "y se pasa a la Tarjeta de crisis."},
]),

("Psicología positiva", [
 {"archivo":"flor-permah.html", "titulo":"Mi flor PERMAH", "etq":"Bienestar",
  "paraque":"Mapa rápido de seis áreas del bienestar: qué se conserva, qué se atiende y por dónde "
            "empezar.",
  "conviene":[
    "Primeras sesiones, cuando la consulta llega difusa: «no sé qué me pasa».",
    "Consulta por un tema puntual, para comprobar si de verdad es puntual.",
    "Cierres de proceso, repitiéndola para comparar con la primera vez."],
  "secuencia":[
    ("Al inicio", "Antes de decidir enfoque; orienta hacia valores, activación o habilidades."),
    ("Se repite", "En el cierre, como medida de contraste.")],
  "cuidado":"No es un instrumento psicométrico y no debe presentarse como tal. Con un perfil plano "
            "y todo bajo, tamizar antes de planificar nada."},

 {"archivo":"fortalezas-del-caracter.html", "titulo":"Mis fortalezas del carácter", "etq":"Recursos",
  "paraque":"Nombrar lo que ya funciona y convertirlo en palanca, en vez de trabajar solo sobre el "
            "déficit.",
  "conviene":[
    "Autoestima muy baja con la mirada puesta enteramente en lo que falta.",
    "Desmoralización y sensación de no tener con qué.",
    "Procesos estancados, para recuperar agencia.",
    "Construcción de alianza en las primeras sesiones."],
  "secuencia":[
    ("Junto a", "La flor PERMAH, en la fase de evaluación."),
    ("Se retoma", "Al planificar acción: la fortaleza elegida es la vía de entrada.")],
  "cuidado":"Si queda en elogio, se lee como minimización. Cada fortaleza elegida tiene que quedar "
            "anclada a un ejemplo conductual concreto antes de pasar a la siguiente."},
]),

("ACT", [
 {"archivo":"act-brujula-de-valores.html", "titulo":"La brújula de valores", "etq":"Valores",
  "paraque":"Doce ámbitos con dos calibradores: cuánto importa y cuánto se actuó. La distancia es "
            "la información, y la casilla de «me la pusieron» es lo que más rinde.",
  "conviene":[
    "Cuando hay lenguaje suficiente para calibrar y tolerancia a una hoja larga.",
    "Sospecha de valores prestados: se rinde para quedar bien con quien mira.",
    "Desmotivación crónica que no cede con técnicas de organización.",
    "Antes de programar cualquier conducta comprometida."],
  "secuencia":[
    ("Después de", "El costo de la lucha."),
    ("Antes de", "El bus o Activación conductual."),
    ("Alternativa", "El jardín de valores, si la persona se pierde en doce ámbitos.")],
  "cuidado":"Si ningún ámbito pasa de 4 en importancia, no insistir con la hoja: el tema es el "
            "aplanamiento, no los valores."},

 {"archivo":"act-costo-de-la-lucha.html", "titulo":"El costo de la lucha", "etq":"Desesperanza creativa",
  "paraque":"Inventario completo de estrategias de control, cada una con su alivio inmediato y su "
            "resultado a la larga. La diferencia entre esas dos columnas es toda la conversación.",
  "conviene":[
    "Casi siempre al principio de un proceso ACT: es la puerta.",
    "Quien llega pidiendo una técnica para eliminar el malestar.",
    "Consumo, evitación, rumia, control, comprobación: cualquier repertorio de escape.",
    "Cuando la persona se culpa por no haberlo logrado con esfuerzo."],
  "secuencia":[
    ("Va primero", "Antes de cualquier trabajo de aceptación o de defusión."),
    ("Junto a", "La cuerda y el monstruo, que lo pone en el cuerpo.")],
  "cuidado":"Con apertura baja, insistir se lee como pedirle a la persona que se resigne: quedarse "
            "en el costo y retomar después. Y revisar si alguna estrategia es de riesgo —consumo, "
            "autolesión, restricción alimentaria— para atenderla por su propia vía."},

 {"archivo":"act-por-donde-entrar.html", "titulo":"Por dónde entrar", "etq":"Formulación",
  "paraque":"Los seis procesos como continuos. No devuelve un perfil para el consultante: devuelve "
            "la puerta de entrada y con qué hoja seguir.",
  "conviene":[
    "Al formular el caso, antes de elegir herramienta.",
    "En supervisión, y con practicantes que están aprendiendo a formular.",
    "Cuando el proceso se estanca y hay que revisar por dónde se entró."],
  "secuencia":[
    ("Antes de", "Elegir cualquier otra hoja de ACT."),
    ("Se rehace", "A mitad de proceso, para ver qué se movió.")],
  "cuidado":"No se llena delante del consultante como si fuera una prueba. Es material del "
            "profesional."},

 {"archivo":"act-soltar-el-anzuelo.html", "titulo":"Soltar el anzuelo", "etq":"Defusión",
  "paraque":"Cinco defusiones cortas sobre un mismo pensamiento, con una sola medida, para "
            "averiguar cuál le sirve a esta persona en concreto.",
  "conviene":[
    "Hay un pensamiento pegajoso identificable y repetido.",
    "Autocrítica dura: «soy un fracaso», «no sirvo».",
    "Después de la flecha descendente, aplicado sobre la creencia del fondo.",
    "Cuando hace falta algo portátil, de diez segundos y de pie."],
  "secuencia":[
    ("Después de", "El costo de la lucha."),
    ("Junto a", "Hojas en el arroyo: el arroyo entrena el proceso, este prueba técnicas."),
    ("Antes de", "Exposición o acción comprometida.")],
  "cuidado":"Mismo riesgo que el arroyo: si se usa para que el pensamiento se vaya, deja de "
            "funcionar. Que ninguna mueva la cifra admite tres lecturas y conviene distinguirlas "
            "antes de insistir."},
]),

("DBT", [
 {"archivo":"dbt-analisis-en-cadena.html", "titulo":"Análisis en cadena", "etq":"Análisis conductual",
  "paraque":"Reconstruir la cadena que lleva a una conducta problema y ubicar, eslabón por eslabón, "
            "qué habilidad cabía ahí.",
  "conviene":[
    "Conducta problema recurrente y concreta: autolesión, consumo, atracón, explosión, abandono.",
    "Después de un episodio, para convertirlo en aprendizaje y no en culpa.",
    "Formación de practicantes: es la hoja que enseña a analizar."],
  "secuencia":[
    ("Después del episodio", "Nunca en caliente."),
    ("Alimenta", "La tarjeta de crisis y la tarjeta diaria.")],
  "cuidado":"Una cadena por vez, la más grave o la más reciente. Y vigilar el tono: la hoja se "
            "convierte fácilmente en interrogatorio culpabilizador si se pierde la curiosidad."},

 {"archivo":"dbt-tarjeta-de-crisis.html", "titulo":"Tarjeta de crisis", "etq":"Tolerancia al malestar",
  "paraque":"El termómetro decide qué habilidad cabe según la activación, y con lo elegido arma una "
            "tarjeta del tamaño de un carné.",
  "conviene":[
    "Desregulación intensa y recurrente.",
    "Impulsos de autolesión, consumo o fuga.",
    "Como psicoeducación expositiva, por su formato de lámina."],
  "secuencia":[
    ("Se llena en frío", "Y se relee en caliente. Nunca al revés."),
    ("Antes de", "Cualquier trabajo que movilice: exposición, trauma, Los ochenta años.")],
  "cuidado":"El agua fría de TIP tiene contraindicación médica: problema cardíaco, presión baja, "
            "trastorno alimentario, embarazo o betabloqueantes. Es la única habilidad del conjunto "
            "que hay que consultar antes."},

 {"archivo":"dbt-verificar-los-hechos.html", "titulo":"Verificar los hechos y acción opuesta",
  "etq":"Regulación emocional",
  "paraque":"Averiguar si la emoción se ajusta a los hechos. Si se ajusta, se resuelve el problema; "
            "si no, se hace lo contrario de lo que pide, y completo.",
  "conviene":[
    "Emociones intensas y frecuentes que la persona da por hechos.",
    "Culpa y vergüenza desproporcionadas.",
    "Rabia que organiza la conducta, miedo social, celos."],
  "secuencia":[
    ("Después de", "Mente sabia, si no hay claridad sobre qué se está sintiendo."),
    ("Deriva a", "Solución de problemas cuando la emoción sí se ajusta.")],
  "cuidado":"Una emoción por vez: la acción opuesta de la rabia y la del miedo son contrarias entre "
            "sí. Y no aplicar acción opuesta cuando la emoción se ajusta: ahí lo que toca es "
            "cambiar algo afuera."},

 {"archivo":"dbt-pedir-y-decir-no.html", "titulo":"Pedir y decir que no", "etq":"Efectividad interpersonal",
  "paraque":"Ordenar objetivo, relación y autorrespeto —de ese orden depende qué habilidad manda— y "
            "salir con un guion para ensayar.",
  "conviene":[
    "Sumisión, complacencia, incapacidad de poner límites.",
    "También el extremo contrario: quien pide con agresión y pierde la relación.",
    "Conflictos de pareja o familiares que se repiten con el mismo guion.",
    "Antes de una conversación concreta y fechada."],
  "secuencia":[
    ("Necesita antes", "Claridad sobre el valor en juego: La brújula."),
    ("Junto a", "La escalera de exposición, si la conversación se viene evitando.")],
  "cuidado":"Si la relación es de riesgo o hay violencia, la habilidad no basta y puede exponer a la "
            "persona. Primero seguridad, después efectividad."},

 {"archivo":"dbt-mente-sabia.html", "titulo":"Mente sabia", "etq":"Mindfulness",
  "paraque":"Una decisión concreta pasa por las tres mentes, por separado, y la sabia aparece "
            "después del silencio, no como promedio.",
  "conviene":[
    "Decisiones atascadas que llevan semanas dando vueltas.",
    "Impulsividad: decide en caliente y se arrepiente.",
    "El patrón inverso: analiza sin decidir nunca.",
    "Sesión corta, de una sola pieza."],
  "secuencia":[
    ("Antes de", "Solución de problemas o Verificar los hechos.")],
  "cuidado":"No forzar la mente sabia antes de haber escuchado de verdad a las otras dos: lo que "
            "sale entonces es la mente racional disfrazada."},

 {"archivo":"dbt-tarjeta-diaria.html", "titulo":"Tarjeta diaria", "etq":"Registro",
  "paraque":"Datos de la semana entre sesiones: emociones, impulsos, conductas y qué habilidad se "
            "usó. Sustituye el relato retrospectivo por el registro.",
  "conviene":[
    "Procesos DBT y cualquier seguimiento de conductas de riesgo.",
    "Cuando el relato de la semana es poco fiable o se reconstruye desde el ánimo del día.",
    "Para ver patrón semanal en vez de episodios sueltos."],
  "secuencia":[
    ("Transversal", "Se revisa al inicio de cada sesión, antes de decidir el tema del día.")],
  "cuidado":"Que no la llene es información, no fracaso. Suele significar que la tarjeta es "
            "demasiado grande o que no se acordó para qué sirve."},
]),

("Cognitivo-conductual", [
 {"archivo":"registro-de-pensamientos.html", "titulo":"Registro de pensamientos", "etq":"Reestructuración",
  "paraque":"Los siete pasos clásicos: situación, emoción, pensamiento caliente, trampas, evidencia "
            "a favor y en contra, alternativa y recalificación.",
  "conviene":[
    "Distorsiones identificables y bien delimitadas.",
    "Ansiedad y depresión leve a moderada.",
    "Buena capacidad verbal y disposición a escribir.",
    "Psicoeducación cognitiva: es la hoja que enseña el modelo."],
  "secuencia":[
    ("Alimenta", "La flecha descendente, con el pensamiento caliente que salga."),
    ("Deriva a", "Defusión si tras varios registros la creencia no se mueve.")],
  "cuidado":"Cuando debatir el contenido ya se volvió parte del problema, o la fusión es muy alta, "
            "un registro más refuerza la pelea. Ahí toca cambiar de vía, no insistir."},

 {"archivo":"tcc-flecha-descendente.html", "titulo":"La flecha descendente", "etq":"Creencias nucleares",
  "paraque":"Bajar del pensamiento automático hasta el fondo, y romper el todo o nada poniendo a "
            "personas reales en un continuo.",
  "conviene":[
    "Patrones que se repiten en situaciones muy distintas.",
    "Cuando la reestructuración de superficie no sostiene entre sesiones.",
    "Formulación cognitiva del caso."],
  "secuencia":[
    ("Después de", "Varios registros de pensamientos."),
    ("Alimenta", "Soltar el anzuelo, aplicado sobre la creencia del fondo.")],
  "cuidado":"Es muy activadora. No hacerla al final de la sesión ni sin tiempo para cerrar, y "
            "dosificar con vulnerabilidad alta: se llega rápido a material que duele."},

 {"archivo":"tcc-escalera-de-exposicion.html", "titulo":"La escalera de exposición", "etq":"Exposición",
  "paraque":"Jerarquía por unidades subjetivas de ansiedad, ensayos registrados y control explícito "
            "de las conductas de seguridad.",
  "conviene":[
    "Fobias específicas, ansiedad social, agorafobia.",
    "TOC, con prevención de respuesta.",
    "Ansiedad por la salud y evitación interoceptiva."],
  "secuencia":[
    ("Después de", "Psicoeducación, y de la Tarjeta de crisis si hay desregulación."),
    ("Junto a", "El bus, que da el marco de aceptación: se avanza con el ruido puesto."),
    ("Junto a", "Autoinstrucciones para el momento de entrar.")],
  "cuidado":"Mientras haya conductas de seguridad sin identificar, la exposición no extingue: "
            "consolida. Y el criterio es repetir hasta que deje de dar ansiedad, no hasta que se "
            "aguante."},

 {"archivo":"tcc-activacion-conductual.html", "titulo":"Activación conductual", "etq":"Activación",
  "paraque":"Registro de agrado y dominio en cuatro cuadrantes, y programación por horario: las "
            "ganas llegan después de empezar, no antes.",
  "conviene":[
    "Depresión, anhedonia, inhibición psicomotora.",
    "Duelo con retirada de actividades.",
    "Procrastinación instalada y el «no tengo ganas de nada».",
    "Cuando el cuadrante vacío es el de agrado y por fuera todo sigue saliendo."],
  "secuencia":[
    ("Va temprano", "Antes que el trabajo cognitivo en depresión moderada o grave."),
    ("Después", "La flor PERMAH para comparar, o valores cuando ya hay movimiento.")],
  "cuidado":"Programar de más produce incumplimiento, y el incumplimiento confirma la creencia de "
            "que no puede. Tres actividades, no diez."},

 {"archivo":"tcc-solucion-de-problemas.html", "titulo":"Solución de problemas", "etq":"Afrontamiento",
  "paraque":"Orientación, definición, generación de alternativas sin juzgar, matriz de decisión, "
            "ejecución y verificación.",
  "conviene":[
    "Problemas externos reales y modificables ahora.",
    "Sobrecarga y decisiones prácticas acumuladas.",
    "Cuando el malestar sí responde a una situación que se puede cambiar.",
    "Baja percepción de autoeficacia para resolver."],
  "secuencia":[
    ("Después de", "Verificar los hechos, cuando la emoción se ajusta."),
    ("Junto a", "Mente sabia, para la parte de decidir.")],
  "cuidado":"El error más frecuente es aplicarla a lo que no se puede resolver ahora. Si el "
            "problema no admite solución en este momento, lo que corresponde es tolerancia al "
            "malestar o aceptación, y confundirlas deja a la persona intentando lo imposible."},

 {"archivo":"tcc-autoinstrucciones.html", "titulo":"Autoinstrucciones", "etq":"Autorregulación",
  "paraque":"Una frase propia para cada una de las cuatro fases del afrontamiento, ensayada antes "
            "y llevada encima el día que toca.",
  "conviene":[
    "Ansiedad de desempeño y situaciones puntuales anticipables.",
    "Impulsividad: mete una pausa verbal entre el impulso y la acción.",
    "Adolescentes, y quien se bloquea y necesita andamiaje.",
    "Cuando el diálogo interno actual es abiertamente hostil."],
  "secuencia":[
    ("Junto a", "La escalera de exposición, para el momento de entrar."),
    ("Antes de", "La situación temida, ensayada al menos dos veces.")],
  "cuidado":"Si la frase se usa para tranquilizarse o para discutir con el pensamiento, se vuelve "
            "control encubierto. Y no sustituye a la exposición: la acompaña."},

 {"archivo":"tcc-analisis-funcional.html", "titulo":"Análisis funcional", "etq":"Formulación",
  "paraque":"Antecedentes, conducta en los tres sistemas de respuesta y consecuencias, con la "
            "hipótesis funcional derivada de lo marcado.",
  "conviene":[
    "Siempre que la topografía confunda: la misma conducta con funciones opuestas.",
    "Conductas cuya función no es obvia, o que el entorno mantiene sin saberlo.",
    "Supervisión y formación de practicantes.",
    "Cuando el plan no funciona y hay que revisar la hipótesis, no la técnica."],
  "secuencia":[
    ("Antes de", "Elegir cualquier técnica: la función determina el procedimiento."),
    ("Se rehace", "Cada vez que el plan falla.")],
  "cuidado":"No es hoja de consultante. Y si la consecuencia es intermitente, hay que advertirle al "
            "entorno que al retirar el refuerzo la conducta aumenta antes de bajar, o el plan se "
            "abandona en la primera semana."},
]),
]

# Encadenamientos que se repiten. Cada uno es una secuencia de hojas.
RUTAS = [
 {"nombre":"Ansiedad y evitación", "color":"#c26a4e",
  "cuando":"Evitación experiencial con agenda de control instalada.",
  "pasos":[("El hombre en el hoyo","met-el-hoyo.html"),
           ("El costo de la lucha","act-costo-de-la-lucha.html"),
           ("El polígrafo","met-el-poligrafo.html"),
           ("La cuerda y el monstruo","met-la-cuerda.html"),
           ("Hojas en el arroyo","met-hojas-en-el-arroyo.html"),
           ("La escalera de exposición","tcc-escalera-de-exposicion.html"),
           ("El bus y los pasajeros","met-el-bus.html")]},

 {"nombre":"Depresión y retirada", "color":"#5f77b8",
  "cuando":"Anhedonia, inhibición, semana vacía.",
  "pasos":[("Mi flor PERMAH","flor-permah.html"),
           ("Activación conductual","tcc-activacion-conductual.html"),
           ("Registro de pensamientos","registro-de-pensamientos.html"),
           ("El jardín de valores","met-jardin-de-valores.html"),
           ("El bus y los pasajeros","met-el-bus.html")]},

 {"nombre":"Rumiación y fusión", "color":"#3f9b86",
  "cuando":"Le da vueltas, discute con su mente, la reestructuración no sostiene.",
  "pasos":[("El costo de la lucha","act-costo-de-la-lucha.html"),
           ("El tablero","met-el-tablero.html"),
           ("Hojas en el arroyo","met-hojas-en-el-arroyo.html"),
           ("La palabra repetida","met-la-palabra-repetida.html"),
           ("Soltar el anzuelo","act-soltar-el-anzuelo.html"),
           ("La radio que no se apaga","met-la-radio.html"),
           ("El bus y los pasajeros","met-el-bus.html")]},

 {"nombre":"Desregulación y riesgo", "color":"#8a3d3d",
  "cuando":"Conductas de riesgo recurrentes, crisis frecuentes.",
  "pasos":[("Tarjeta de crisis","dbt-tarjeta-de-crisis.html"),
           ("Tarjeta diaria","dbt-tarjeta-diaria.html"),
           ("Análisis en cadena","dbt-analisis-en-cadena.html"),
           ("Verificar los hechos","dbt-verificar-los-hechos.html"),
           ("Pedir y decir que no","dbt-pedir-y-decir-no.html")]},

 {"nombre":"Vacío y falta de rumbo", "color":"#c9962f",
  "cuando":"Funciona bien y no sabe para qué; consulta por sinsentido.",
  "pasos":[("Mi flor PERMAH","flor-permah.html"),
           ("Mis fortalezas del carácter","fortalezas-del-caracter.html"),
           ("La brújula de valores","act-brujula-de-valores.html"),
           ("Los ochenta años","met-los-ochenta-anos.html"),
           ("El bus y los pasajeros","met-el-bus.html")]},
]

CSS = """
  .envoltura{max-width:1120px}
  .volver{display:inline-flex;align-items:center;gap:7px;font-size:13.5px;color:var(--acento);
    text-decoration:none;margin-bottom:14px}
  .volver:hover{text-decoration:underline}
  .volver::before{content:"\\2190"}

  .rutas{display:grid;gap:10px;margin-top:15px}
  .ruta{border:1px solid var(--linea);border-left-width:5px;border-radius:10px;padding:12px 15px;
    background:#fdfefe}
  .ruta .nom{font-size:15px;font-weight:700}
  .ruta .cuando{font-size:12.5px;color:var(--tinta-suave);margin:2px 0 9px}
  .ruta .cadena{display:flex;flex-wrap:wrap;align-items:center;gap:7px}
  .ruta .cadena a{font-size:13px;text-decoration:none;color:var(--tinta);border:1px solid var(--linea);
    border-radius:999px;padding:5px 12px;background:#fff;white-space:nowrap}
  .ruta .cadena a:hover{border-color:var(--acento);color:var(--acento)}
  .ruta .cadena i{color:#b3bfca;font-style:normal;font-size:14px}

  h2.enfoque{margin:26px 0 2px;font-size:20px;display:flex;align-items:center;gap:10px}
  h2.enfoque::before{content:"";width:13px;height:13px;border-radius:50%;background:currentColor}

  .fichas{display:grid;grid-template-columns:repeat(auto-fill,minmax(400px,1fr));gap:13px;
    margin-top:13px}
  .ficha-guia{background:var(--papel);border:1px solid var(--linea);border-left-width:5px;
    border-radius:var(--radio);padding:16px 19px}
  .ficha-guia .cab{display:flex;align-items:baseline;justify-content:space-between;gap:10px;
    margin-bottom:6px}
  .ficha-guia h3{margin:0;font-size:17px;letter-spacing:-.2px}
  .ficha-guia h3 a{color:inherit;text-decoration:none}
  .ficha-guia h3 a:hover{text-decoration:underline}
  .ficha-guia .etq{font-size:10.5px;text-transform:uppercase;letter-spacing:.8px;font-weight:700;
    white-space:nowrap;border-radius:999px;padding:2px 9px}
  .ficha-guia .paraque{margin:0 0 12px;font-size:14px;line-height:1.5}
  .ficha-guia .rot{font-size:10.5px;text-transform:uppercase;letter-spacing:.7px;font-weight:700;
    color:var(--tinta-suave);margin:11px 0 4px}
  .ficha-guia ul{margin:0;padding-left:18px;font-size:13.5px;line-height:1.5;
    color:var(--tinta-suave)}
  .ficha-guia li{margin-bottom:3px}
  .ficha-guia .paso{font-size:13.5px;line-height:1.5;color:var(--tinta-suave);margin-bottom:3px}
  .ficha-guia .paso b{color:var(--tinta);font-weight:600}
  .ficha-guia .aviso-uso{margin-top:11px;background:var(--alerta-fondo);
    border:1px solid var(--alerta-linea);border-radius:8px;padding:9px 12px;font-size:13px;
    color:var(--alerta);line-height:1.5}
  .ficha-guia .aviso-uso b{display:block;font-size:10.5px;text-transform:uppercase;
    letter-spacing:.7px;margin-bottom:2px}
  @media (max-width:760px){.fichas{grid-template-columns:1fr}}
  @media print{
    body{background:#fff}
    .volver{display:none}
    .ficha-guia,.ruta{break-inside:avoid}
    .fichas{grid-template-columns:1fr 1fr}
  }
"""


def ficha(h, color):
    conviene = "\n".join("        <li>%s</li>" % c for c in h["conviene"])
    pasos = "\n".join('      <div class="paso"><b>%s</b> %s</div>' % (r, t)
                      for r, t in h["secuencia"])
    aviso = ('\n      <div class="aviso-uso"><b>Cuidado</b>%s</div>' % h["cuidado"]) \
        if h.get("cuidado") else ""
    return f"""    <div class="ficha-guia" style="border-left-color:{color}">
      <div class="cab">
        <h3><a href="{h['archivo']}">{h['titulo']}</a></h3>
        <span class="etq" style="color:{color};background:{color}1a">{h['etq']}</span>
      </div>
      <p class="paraque">{h['paraque']}</p>
      <div class="rot">Conviene en</div>
      <ul>
{conviene}
      </ul>
      <div class="rot">Secuencia</div>
{pasos}{aviso}
    </div>"""


def ruta(r):
    eslabones = ' <i>&rarr;</i> '.join(
        '<a href="%s">%s</a>' % (a, n) for n, a in r["pasos"])
    return f"""    <div class="ruta" style="border-left-color:{r['color']}">
      <div class="nom">{r['nombre']}</div>
      <div class="cuando">{r['cuando']}</div>
      <div class="cadena">{eslabones}</div>
    </div>"""


def construir(kit_css=None):
    if kit_css is None:
        kit_css = (AQUI / "kit.css").read_text(encoding="utf-8")

    bloques = []
    for enfoque, hojas in GUIA:
        color = COLORES[enfoque]
        fichas = "\n".join(ficha(h, color) for h in hojas)
        bloques.append(f"""<h2 class="enfoque" style="color:{color}">{enfoque}</h2>
  <div class="fichas">
{fichas}
  </div>""")

    rutas = "\n".join(ruta(r) for r in RUTAS)
    cuantas = sum(len(h) for _, h in GUIA)

    salida = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guía rápida de uso</title>
<style>
{kit_css}
{CSS}
</style>
</head>
<body>
<div class="envoltura">

<a class="volver" href="index.html">Volver a las herramientas</a>

<header class="tapa">
  <h1>Guía rápida de uso</h1>
  <p class="sub">Para qué sirve cada una de las {cuantas} hojas, en qué casos rinde, con qué va
  antes o después, y dónde conviene tener cuidado. Los títulos abren la herramienta.</p>
</header>

<section class="bloque">
  <h2>Encadenamientos frecuentes</h2>
  <p class="ayuda">No son protocolos: son los órdenes que suelen funcionar. Lo que casi nunca
  funciona es empezar por el final.</p>
  <div class="rutas">
{rutas}
  </div>
</section>

{chr(10).join(bloques)}

</div>
</body>
</html>
"""
    (DESTINO / "guia.html").write_text(salida, encoding="utf-8")
    return cuantas


if __name__ == "__main__":
    n = construir()
    print(f"  guia.html con {n} fichas")
