# -*- coding: utf-8 -*-
"""
Arma guia.html: para qué sirve cada hoja, en qué casos rinde, con qué va antes
o después, y dónde conviene tener cuidado.

No es una herramienta: es la hoja de ruta del profesional. Por eso no lleva kit,
ni guardado, ni notas. Se reconstruye sola al correr construir.py.

    python guia.py
"""
from pathlib import Path
import html as _h

import guiones
import rieles
import sesion

SALTO = chr(10)

AQUI = Path(__file__).resolve().parent
DESTINO = AQUI.parent

COLORES = {
    "ACT":                     "#3f9b86",
    "Cognitivo-conductual":    "#2f6f8f",
    "DBT":                     "#5f77b8",
    "Compasión y mindfulness": "#4a8a7a",
    "Vínculos y pareja":       "#9c5d6e",
    "Psicología positiva":     "#c9962f",
    "Crisis y consumo":        "#b0503f",
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
  "paraque":"Clarificación por elección y no por escritura: seis surcos de veinticuatro, y la distancia "
            "entre lo que importa y lo que efectivamente se regó. Entre sembrar y regar hay un paso "
            "de enraizar: cada surco dice qué cuida por debajo y se renombra con las palabras de la "
            "persona, que es donde la conducta deja de pasar por valor.",
  "conviene":[
    "Cuando preguntar «¿cuáles son tus valores?» produce silencio o discurso aprendido.",
    "Personas poco verbales, o que no escriben, o que se pierden en la brújula.",
    "Sobrecarga con culpa difusa: todo importa y nada se mueve.",
    "Vida partida en dos, con todo el combustible en un solo frente."],
  "secuencia":[
    ("Alternativa a", "La brújula de valores, cuando hace falta algo más concreto y menos verbal."),
    ("Después va", "El bus, o activación conductual si lo que falla es arrancar.")],
  "cuidado":"Si no logra sembrar ni tres surcos, la conversación no es sobre valores sino sobre el "
            "aplanamiento. Conviene tamizar sintomatología depresiva antes de seguir. Y si los surcos "
            "se quedan sin raíz, la hoja se está usando como lista de tareas: el contador «sin raíz» "
            "dice exactamente dónde falta preguntar."},

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
            "Ese ciclo es la repetición útil, y por eso el marcador cuenta retornos y no fallos. "
            "La corriente trae los pensamientos sola, y hacia el final llegan en racimo.",
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
 {"archivo":"pp-tres-cosas-buenas.html", "titulo":"Tres cosas buenas y mi mejor versión", "etq":"Gratitud y metas",
  "paraque":"Entrenar la atención hacia lo que sale bien con un diario de tres cosas buenas, y convertir "
            "una imagen de una mejor versión de uno mismo en un plan apoyado en las propias fortalezas.",
  "conviene":[
    "Síntomas depresivos con atención fija en lo negativo y comparaciones con los demás.",
    "Personas que ya identificaron sus fortalezas y no saben cómo usarlas.",
    "Como práctica continua durante toda la terapia: el diario se revisa al inicio de cada sesión."],
  "secuencia":[
    ("Después de", "Mis fortalezas del carácter, que da las fortalezas distintivas para el plan."),
    ("Junto a", "Mi flor PERMAH, para ver en qué área del bienestar cae la mejor versión."),
    ("Tarea", "Tres cosas buenas cada noche y el plan compartido con alguien que reciba noticias.")],
  "cuidado":"En un duelo o una situación muy dura el diario puede no salir de forma auténtica: no se "
            "fuerza y se buscan alternativas. Y la gente se acostumbra: conviene variar el formato."},
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
 {"archivo":"act-matriz.html", "titulo":"La matriz", "etq":"Punto de vista",
  "paraque":"Un solo diagrama para ordenar lo que importa, lo que se interpone, lo que se hace para "
            "alejarse y lo que se hace o podría hacerse para acercarse. Sirve igual para problemas "
            "distintos y habla en palabras de la persona, sin conceptos técnicos.",
  "conviene":[
    "Evitación en muchas áreas, con ciclos de alivio inmediato y costo a largo plazo.",
    "Personas a las que los conceptos de la terapia de aceptación y compromiso las mandan a la cabeza.",
    "Como mapa compartido para volver a él sesión tras sesión.",
    "Trabajo con parejas, familias o equipos, donde cada uno ordena su propia matriz."],
  "secuencia":[
    ("Abre", "El trabajo con la matriz: después vienen la funcionalidad de los movimientos de alejamiento y los ganchos."),
    ("Junto a", "La brújula de valores, para desarrollar el cuadrante de quién y qué importa.")],
  "cuidado":"Se empieza por quién importa, para que la primera mirada sea un acierto, y no se busca "
            "una lista completa. Si la persona dice «me autosaboteo», se pregunta qué se le ve "
            "haciendo: arriba van conductas observables."},
 {"archivo":"act-los-ganchos.html", "titulo":"Los ganchos", "etq":"Matriz, paso 3",
  "paraque":"Reconocer qué engancha a la persona y darse cuenta de que mordió por lo que hace después, "
            "no por analizar el gancho.",
  "conviene":[
    "Después de la matriz, cuando ya se distinguen movimientos hacia y de alejamiento.",
    "Reacciones que se repiten ante los mismos disparadores: rabia, autocrítica, ganas de consumir.",
    "Personas que buscan entender de dónde viene cada pensamiento antes de poder moverse."],
  "secuencia":[
    ("Después de", "La matriz y la revisión de si los movimientos de alejamiento funcionan."),
    ("Junto a", "Soltar el anzuelo, para ensayar la defusión con un gancho concreto."),
    ("Tarea", "Notar ganchos en la semana y lo que se hizo después.")],
  "cuidado":"No se corrige cómo clasifica: si pone una conducta en el cebo o algo externo, se sigue. "
            "Tampoco se sugiere que los ganchos «están solo en la cabeza»."},
 {"archivo":"act-el-cielo-y-el-clima.html", "titulo":"El cielo y el clima", "etq":"Dejar espacio",
  "paraque":"Dejar de pelear con un pensamiento, un sentimiento o un dolor dándole espacio: se nombra, "
            "se le da forma y la respiración va hacia adentro y alrededor.",
  "conviene":[
    "Emociones o sensaciones que se intentan apartar y vuelven con más fuerza.",
    "Dolor físico persistente con lucha alrededor.",
    "Insomnio con pensamientos que no dejan dormir, combinada con respiración."],
  "secuencia":[
    ("Después de", "Poner los pies en la tierra y desengancharse, como en la guía de la OPS."),
    ("Junto a", "La cuerda y el monstruo, que muestra el costo de pelear."),
    ("Tarea", "Practicar en la cama cuando no se puede dormir, o cuando aparece el dolor.")],
  "cuidado":"No es una técnica para que se vaya: si la persona la usa para eso y el clima no cambia, "
            "concluye que falló. Se calibra la lucha, no la intensidad."},
 {"archivo":"act-empujar-el-papel.html", "titulo":"Empujar el papel", "etq":"Preocupación y rumia",
  "paraque":"Hacer visible, en el cuerpo y en un minuto, lo que cuesta pelear con la preocupación o la "
            "rumia, y probar la alternativa: dejar el pensamiento al lado y seguir con lo que importa.",
  "conviene":[
    "Preocupación o rumia que ocupan horas del día.",
    "Personas que ya intentaron distraerse, suprimir o discutir sus pensamientos sin resultado.",
    "Intervenciones breves: es el centro de la primera sesión del protocolo."],
  "secuencia":[
    ("Antes de", "Identificar el «papá», sus «hijitos» y lo que se hace para dejar de pensar."),
    ("Después de", "La matriz, que da el esquema de arriba a la derecha y abajo a la izquierda."),
    ("Abre paso a", "Hojas en el arroyo y La palabra repetida, como práctica de defusión.")],
  "cuidado":"Con papel real funciona mejor: el terapeuta sostiene la hoja y ofrece resistencia. La hoja "
            "no reemplaza eso, lo resume. Y el «papá» se busca con cuidado: suele ser el pensamiento "
            "que más dolería creer cierto."},
 {"archivo":"act-quien-lleva-los-globos.html", "titulo":"Quién lleva los globos",
  "etq":"Defusión y elección",
  "paraque":"Tres movimientos seguidos sobre lo mismo: ponerlo enfrente, notar quién lo mira y que hay "
            "sitio para ese y para todos, y elegir quién manda en el paso siguiente. Es defusión con "
            "perspectiva y con dirección, no solo con distancia.",
  "conviene":[
    "Ya observa sus pensamientos, y cuando aparecen sigue haciendo lo que ellos dicen.",
    "Hojas en el arroyo se le volvió una manera de esperar a que pasen.",
    "Conducta reactiva o impulsiva: lo siente y lo hace, sin intervalo en medio.",
    "Preocupación y rumia, después de Empujar el papel: es el ejercicio que abre la segunda sesión "
    "de ese protocolo."],
  "secuencia":[
    ("Necesita antes", "La brújula o El jardín: sin algo que importe no hay hacia dónde elegir."),
    ("Después de", "Hojas en el arroyo, que entrena solo la distancia."),
    ("Junto a", "El tablero o El cielo y el clima, que dan la imagen de tener sitio."),
    ("Antes de", "La radio que no se apaga y El bus: de elegir en la hoja a hacer con el ruido puesto.")],
  "cuidado":"Aquí los globos no se sueltan: si la persona espera que se vayan, se volvió control. «Que "
            "mande el globo» es una respuesta válida y no se corrige. El respaldo es de laboratorio, con "
            "muestras pequeñas y casi todas no clínicas: sumar perspectiva y elección rindió más que la "
            "sola distancia en conducta problema, tolerancia al malestar y rendimiento en una tarea, "
            "pero los estudios no separan cuál de las dos cosas aporta, y sobre el malestar reportado "
            "la ventaja fue pequeña e irregular. Con disociación o despersonalización, ojos abiertos y "
            "sin insistir en la pregunta de quién mira."},
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
 {"archivo":"tcc-aplazar-la-preocupacion.html", "titulo":"Aplazar la preocupación", "etq":"Metacognitiva",
  "paraque":"Poner a prueba la creencia de que la preocupación o la rumiación son incontrolables: se "
            "deja el desencadenante en paz y se aplaza el proceso a un momento breve más tarde en el día.",
  "conviene":[
    "Ansiedad generalizada con preocupación que se vive como imposible de parar.",
    "Rumiación depresiva o pensamientos intrusivos después de un trauma.",
    "Personas que intentan suprimir los pensamientos y confunden eso con controlarlos."],
  "secuencia":[
    ("Antes de", "Practicar el mindfulness desapegado con un pensamiento neutro, como un tigre."),
    ("Después de", "Los experimentos de intentar perder el control, en sesión y luego en casa."),
    ("Tarea", "Aplazar con todos los desencadenantes y volver a calificar la creencia en la sesión siguiente.")],
  "cuidado":"Aplazar no es suprimir: el pensamiento puede quedarse en la mente, lo que se deja para "
            "después es el proceso de preocuparse. Se revisa con detalle cómo se aplicó: suele usarse "
            "solo con algunos desencadenantes, o se confunde con distraerse."},
 {"archivo":"tcc-balance-decisional.html", "titulo":"Balance decisional", "etq":"Motivación",
  "paraque":"Trabajar la ambivalencia explorando con honestidad los pros y contras de cambiar y de seguir "
            "igual, responder a lo que sostiene no cambiar y llegar a un objetivo con pasos concretos.",
  "conviene":[
    "Al inicio del tratamiento, antes de los módulos que exigen esfuerzo, como la exposición.",
    "Cuando la motivación baja o hay un retroceso: se vuelve a revisar el balance.",
    "Ambivalencia fuerte que no se resuelve con las preguntas de importancia y confianza."],
  "secuencia":[
    ("Después de", "Importancia y confianza, si la ambivalencia pide más que dos preguntas."),
    ("Abre paso a", "La escalera de exposición o la activación conductual, según el objetivo."),
    ("Se repite", "Antes de las exposiciones y cada vez que la motivación flaquee.")],
  "cuidado":"Las celdas de lo bueno de seguir igual y lo difícil de cambiar suelen quedar vacías. No se "
            "sigue sin explorarlas: ahí están los obstáculos que aparecerán después."},
 {"archivo":"tcc-ventana-de-sueno.html", "titulo":"Ventana de sueño", "etq":"Insomnio",
  "paraque":"Consolidar el sueño ajustando el tiempo en la cama al tiempo que de verdad se duerme, con una "
            "hora fija para levantarse, y ampliarlo semana a semana según la eficiencia.",
  "conviene":[
    "Insomnio crónico con mucho tiempo despierto en la cama.",
    "Personas que se acuestan cada vez más temprano o se quedan en cama para recuperar sueño.",
    "Cuando ya hay al menos una semana de diario de sueño."],
  "secuencia":[
    ("Antes de", "Una o dos semanas de diario de sueño, que dan los promedios."),
    ("Junto a", "El control de estímulos, que se acuerda en la misma sesión."),
    ("Se ajusta", "Cada semana, al comienzo de la sesión, con el diario.")],
  "cuidado":"Nunca menos de cuatro horas y media en la cama. Puede estar contraindicada con antecedentes "
            "de manía, apnea obstructiva, convulsiones, parasomnias o riesgo de caídas. Al comienzo se "
            "duerme algo menos: conviene anticiparlo."},
 {"archivo":"tcc-lista-abc.html", "titulo":"Lista de tareas A-B-C", "etq":"Organización",
  "paraque":"Reunir todo lo pendiente en una sola lista y priorizar con una regla simple: todas las A "
            "antes que cualquier B, para no llenar el día con lo fácil y dejar lo importante.",
  "conviene":[
    "Adultos con TDAH o con dificultades de organización y postergación.",
    "Personas que se sienten ocupadas todo el día y no avanzan en lo importante.",
    "Como base de otras habilidades: la lista y el calendario sostienen el resto del programa."],
  "secuencia":[
    ("Antes de", "Acordar un calendario y una sola lista maestra, que reemplacen los papelitos."),
    ("Abre paso a", "La solución de problemas, cuando las A se quedan sin hacer una y otra vez."),
    ("Tarea", "Mirar la lista cada día a una hora fija y armar la lista del día con sus letras.")],
  "cuidado":"El error más común es calificar demasiadas tareas como A. Y no buscar el sistema perfecto: "
            "uno sencillo y cómodo, sostenido al menos tres meses."},
 {"archivo":"tcc-inoculacion-de-estres.html", "titulo":"Inoculación de estrés", "etq":"Estrés",
  "paraque":"Recorrer las tres fases del entrenamiento: entender el estrés y separar lo cambiable de lo que "
            "no, reunir un repertorio de afrontamiento y ensayarlo con dosis de estrés crecientes.",
  "conviene":[
    "Estrés laboral, de crianza o por enfermedad, con situaciones que se repiten.",
    "Preparación para algo difícil que se sabe que viene: una cirugía, una audiencia, un examen.",
    "Ira o ansiedad ante situaciones interpersonales concretas."],
  "secuencia":[
    ("Junto a", "Autoinstrucciones, que arma las frases para antes, durante y después."),
    ("Usa", "La solución de problemas para lo cambiable y la respiración lenta para lo que no."),
    ("Tarea", "La siguiente dosis como experimento personal, acordado con la persona.")],
  "cuidado":"La dosis sube solo después de varios éxitos; si una se desborda, se vuelve a una más suave. "
            "Y no se abruma con opciones: pocas herramientas, las que encajen."},
]),
("Compasión y mindfulness", [
 {"archivo":"cft-ritmo-tranquilizador.html", "titulo":"Respiración de ritmo tranquilizador", "etq":"Sistema de calma",
  "paraque":"Enlentecer la respiración y atender a la sensación de ir más despacio, para suavizar las "
            "emociones de amenaza. Es una de las primeras prácticas de la terapia centrada en la compasión.",
  "conviene":[
    "Activación alta, ansiedad o enojo que no dejan pensar ni practicar otra cosa.",
    "Como puerta de entrada a las prácticas compasivas.",
    "Para instalar desde la primera sesión el hábito de practicar entre sesiones."],
  "secuencia":[
    ("Antes de", "El espacio de respiración y las prácticas de autocompasión."),
    ("Tarea", "Treinta segundos, dos o tres veces al día, con un recordatorio acordado.")],
  "cuidado":"No es respiración consciente: aquí sí se cambia el ritmo. Si atender al cuerpo o a la "
            "respiración incomoda, no se convierte en exposición: se busca otro foco tranquilizador."},
 {"archivo":"cft-espacio-de-respiracion.html", "titulo":"Espacio de respiración de tres minutos", "etq":"Mindfulness",
  "paraque":"Llevar la práctica al día y usarla como primer paso ante lo difícil: reconocer lo que hay, "
            "reunir la atención en la respiración y ampliarla al cuerpo entero.",
  "conviene":[
    "Prevención de recaídas en depresión, dentro o fuera del programa completo.",
    "Momentos del día en que se entra en piloto automático o en rumiación.",
    "Antes de responder en una situación difícil."],
  "secuencia":[
    ("Después de", "Alguna práctica formal más larga, como el escáner corporal."),
    ("Abre paso a", "Las puertas del cuerpo, del pensamiento y de la acción hábil.")],
  "cuidado":"No es un tiempo muerto para escapar de la crisis: si se usa para que lo desagradable se "
            "vaya, se vuelve a la modalidad «hacer». Tampoco importa que dure exactamente tres minutos."},
 {"archivo":"cft-pausa-de-autocompasion.html", "titulo":"Pausa de autocompasión", "etq":"Autocompasión",
  "paraque":"Responder a un momento difícil con los tres componentes de la autocompasión: reconocer que "
            "duele, recordar que le pasa a cualquiera y ofrecerse lo que hace falta, consuelo o fuerza.",
  "conviene":[
    "Autocrítica dura ante errores o fracasos.",
    "Vergüenza o sensación de estar solo con el problema.",
    "Como práctica informal breve, para usar en el día cuando aparece el estrés."],
  "secuencia":[
    ("Después de", "La respiración de ritmo tranquilizador, si la activación es alta."),
    ("Abre paso a", "El yo compasivo, para trabajar la autocrítica con más profundidad."),
    ("Tarea", "La tarjeta con las tres frases y el gesto, en los momentos acordados.")],
  "cuidado":"Al comienzo puede sentirse peor: es el contragolpe, dolor que ya estaba y sale cuando se "
            "abre la puerta a la amabilidad. Se avanza más despacio, y con historia de trauma se "
            "practica primero en sesión. No se usa para que el malestar desaparezca."},
 {"archivo":"cft-el-yo-compasivo.html", "titulo":"El yo compasivo", "etq":"Autocrítica",
  "paraque":"Pasar de la perspectiva de amenaza a una organizada por la compasión, ensayándola como un "
            "papel, y desde ahí acompañar a la versión de uno que sufre.",
  "conviene":[
    "Autocrítica y vergüenza arraigadas.",
    "Ansiedad ante situaciones que activan viejas experiencias de humillación.",
    "Personas que dicen «yo no soy así»: el papel evita la discusión."],
  "secuencia":[
    ("Después de", "La respiración de ritmo tranquilizador, que abre la práctica."),
    ("Junto a", "La pausa de autocompasión, para el día a día."),
    ("Tarea", "Ponerse el papel en momentos tranquilos y acordados; después, una carta desde el yo compasivo.")],
  "cuidado":"No es un escape de la situación difícil: se sale de la amenaza para volver a ella desde "
            "otra perspectiva. Con vergüenza muy intensa se empieza por acompañar a otra persona."},
]),
("Crisis y consumo", [
 {"archivo":"crisis-plan-de-seguridad.html", "titulo":"Plan de seguridad", "etq":"Riesgo suicida",
  "paraque":"Un plan escrito con la persona, en sus palabras, de lo que hará si la crisis vuelve: de lo "
            "que puede hacer sola a lo que requiere ayuda, con teléfonos concretos y los medios fuera de alcance.",
  "conviene":[
    "Después de una valoración de riesgo suicida, en un momento de calma.",
    "Tras un intento o una autolesión, antes de terminar el contacto.",
    "Como parte del seguimiento: se revisa en cada encuentro."],
  "secuencia":[
    ("Después de", "La valoración del riesgo, que va primero."),
    ("Junto a", "La tarjeta de crisis de DBT, para las habilidades del segundo paso.")],
  "cuidado":"No reemplaza la ruta de urgencias: con plan en curso, intención o incapacidad de "
            "mantenerse a salvo, se activa la ruta. Y es más útil que pedir un contrato de no suicidio."},
 {"archivo":"crisis-surfear-el-impulso.html", "titulo":"Surfear el impulso", "etq":"Prevención de recaídas",
  "paraque":"Atravesar el deseo de consumir sin obedecerlo ni pelear con él: nombrarlo como impulso, "
            "observarlo en el cuerpo y dejar que suba y baje como una ola.",
  "conviene":[
    "Consumo de sustancias o apuestas con deseo intenso ante señales o emociones.",
    "Personas que intentan suprimir el deseo y terminan más atrapadas en él.",
    "Como práctica en sesión antes de usarla en situaciones reales."],
  "secuencia":[
    ("Junto a", "El plan de prevención de recaídas y la identificación de situaciones de riesgo."),
    ("Complementa", "Hojas en el arroyo: la misma actitud de observar sin actuar.")],
  "cuidado":"Si hubo consumo, se revisa como información para la próxima vez, no como fracaso: una "
            "caída no borra lo aprendido."},
 {"archivo":"crisis-importancia-y-confianza.html", "titulo":"Importancia y confianza", "etq":"Entrevista motivacional",
  "paraque":"Explorar la ambivalencia con dos preguntas de escala y evocar, en palabras de la persona, "
            "sus razones para cambiar y sus recursos para lograrlo.",
  "conviene":[
    "Ambivalencia ante un cambio: consumo, adherencia al tratamiento, volver a la actividad.",
    "Una tarea acordada que no se hizo: se revisan la importancia y la confianza antes de insistir.",
    "Mantenimiento: después de un tropiezo, para volver a las razones y a la confianza."],
  "secuencia":[
    ("Después de", "Enfocar: acordar juntos de qué cambio se está hablando."),
    ("Abre paso a", "El balance decisional, si la ambivalencia es fuerte; el plan, si las dos reglas están altas."),
    ("Se repite", "En sesiones posteriores, para ver cómo se mueven.")],
  "cuidado":"El número no se discute ni se corrige. Si se pregunta «¿por qué no un 10?», la persona "
            "responde con sus razones para no cambiar: la pregunta va siempre hacia el número más bajo."},
]),
(
  "Ampliación clínica (Lotes 1, 2 y 3)",
  [{'archivo': 'act-echar-el-ancla.html',
  'conviene': ['Desbordamiento emocional en sesión, crisis de ansiedad, oleadas de duelo o '
               'recuerdos intrusivos.',
               'Cuando una práctica contemplativa larga como el arroyo o el cielo queda grande por '
               'el nivel de activación.',
               'Rumiación o disociación incipiente donde hace falta recuperar contacto inmediato '
               'con el cuerpo y el cuarto.',
               'Como primera habilidad portátil antes de abordar exposición, defusión o valores.'],
  'cuidado': 'El riesgo principal es que se use como técnica de distracción o relajación para '
             'hacer desaparecer la emoción. Por eso el primer paso (A) nombra lo que sigue adentro '
             'y en la escena el oleaje nunca se detiene: si la persona mide el éxito por haberse '
             'calmado, al próximo pico sentirá que el ancla no sirve.',
  'etq': 'Momento presente',
  'paraque': 'Sujetar a la persona en medio de una tormenta emocional con la secuencia ACE '
             '(reconocer lo que hay adentro, conectar con el cuerpo e involucrarse en lo que hay '
             'aquí), dejando claro que el ancla no se echa para apagar el mar sino para no ser '
             'arrastrado.',
  'secuencia': [('Antes de',
                 'Cualquier otra hoja experiencial si la persona llega muy activada o tomada por '
                 'la tormenta.'),
                ('Junto a', 'Los ganchos, que entrena el mismo retorno en la vida cotidiana.'),
                ('Abre paso a',
                 'El cielo y el clima o La cuerda y el monstruo una vez que hay piso firme.')],
  'titulo': 'Echar el ancla'},
 {'archivo': 'met-el-interruptor.html',
  'conviene': ['Ansiedad por tener ansiedad, culpa por estar triste, rabia por sentir miedo o '
               'vergüenza por seguir pasándolo mal.',
               'Personas que se reprochan sentir lo que sienten y multiplican cada emoción con una '
               'segunda capa de juicio.',
               'Cuando El polígrafo resulta demasiado centrado en activación fisiológica y hace '
               'falta incluir tristeza, culpa o fatiga.'],
  'cuidado': 'Apagar el interruptor no apaga la onda primaria. Si la persona busca dónde está el '
             'botón para apagar también la tristeza o el miedo inicial, conviene señalar en la '
             'pantalla que la primera ola sigue moviéndose y que justamente por eso ya no hace '
             'falta pelear.',
  'etq': 'Aceptación',
  'paraque': 'Separar de un vistazo el malestar limpio (la emoción primaria que sube y baja con la '
             'vida) del malestar sucio (la pelea secundaria que se enciende encima) y mostrar '
             'cuánta energía queda libre al soltar el interruptor.',
  'secuencia': [('Después de',
                 'El costo de la lucha, para ubicar el interruptor dentro de su repertorio '
                 'habitual.'),
                ('Junto a', 'El polígrafo o La cuerda y el monstruo.'),
                ('Antes de',
                 'El cielo y el clima o El bus y los pasajeros, para invertir la energía '
                 'liberada.')],
  'titulo': 'El interruptor de la lucha'},
 {'archivo': 'met-las-manos.html',
  'conviene': ['Fusión aguda con frases categóricas («no voy a poder», «siempre arruino todo») que '
               'acaparan toda la conversación.',
               'Cuando la persona cree que para poder actuar primero tiene que dejar de pensar '
               'eso.',
               'Personas muy concretas a las que observar hojas en un arroyo les resulta lejano o '
               'abstracto.'],
  'cuidado': 'Conviene hacerlo también con las manos reales en el consultorio antes o a la par de '
             'mover el control en pantalla. Cuidar que al llegar al regazo no se interprete que '
             'las manos desaparecieron: siguen ahí abajo con las mismas palabras escritas.',
  'etq': 'Defusión',
  'paraque': 'Hacer vivir en el cuerpo y en diez segundos qué es la fusión (las manos pegadas a la '
             'cara tapando toda la habitación) y qué es la defusión (bajarlas al regazo sin que se '
             'borre lo escrito, recuperando la vista y las manos).',
  'secuencia': [('Antes de',
                 'Soltar el anzuelo o Hojas en el arroyo, como introducción física e inmediata a '
                 'la defusión.'),
                ('Junto a',
                 'Empujar el papel, que añade el gasto de energía al intento de apartarlas.'),
                ('Abre paso a', 'De FEAR a DARE o El bus y los pasajeros.')],
  'titulo': 'Las manos como pensamientos'},
 {'archivo': 'met-el-escenario.html',
  'conviene': ['Visión de túnel donde un único problema, síntoma o temor parece ocupar el cien por '
               'ciento de la vida.',
               'Autocrítica o dolor crónico que eclipsan vínculos, gustos y pequeños logros '
               'cotidianos.',
               'Como alternativa al tablero cuando la metáfora de una partida o pelea entre '
               'blancas y negras no encaja con la vivencia.'],
  'cuidado': 'Encender las luces generales no es pensamiento positivo ni tapar al actor difícil '
             'con cosas bonitas. El personaje que gritaba se queda en el centro de las tablas; lo '
             'que cambia es que deja de ser lo único iluminado.',
  'etq': 'Yo observador',
  'paraque': 'Mostrar cómo la atención estrecha funciona igual que un reflector cerrado sobre el '
             'actor más ruidoso, y cómo abrir las luces de todo el escenario y notar la butaca del '
             'observador devuelve proporción sin expulsar a nadie de las tablas.',
  'secuencia': [('Alternativa a',
                 'El tablero y El cielo y el clima dentro del trabajo con el yo como contexto.'),
                ('Junto a',
                 'Echar el ancla, cuyo tercer paso (E) equivale a encender las luces del '
                 'escenario.'),
                ('Antes de',
                 'La brújula de valores o El jardín de valores, para mirar a los otros actores que '
                 'estaban a oscuras.')],
  'titulo': 'El escenario y el reflector'},
 {'archivo': 'act-fear-a-dare.html',
  'conviene': ['Cuando la persona ya clarificó valores en La brújula o El jardín, pero vuelve a la '
               'sesión siguiente sin haber podido dar el paso.',
               'Procrastinación persistente y planes de acción que se abandonan a mitad de semana.',
               'Cierres de sesión donde hace falta blindar el compromiso frente a los obstáculos '
               'previsibles.'],
  'cuidado': 'No hace falta llenar las cuatro letras si solo una o dos están frenando el paso. Si '
             'la barrera es E (Exceso en la meta o falta real de recursos), insistir con '
             'aceptación o defusión sola sería invalidante: ahí toca partir la meta a la mitad.',
  'etq': 'Acción comprometida',
  'paraque': 'Diagnosticar qué barrera específica está frenando un paso valioso (Fusión, Exceso en '
             'la meta, Aversión al malestar o quedar Remoto del valor) y encender su antídoto DARE '
             '(Defusión, Aceptación, Realismo en la meta y Enlace con el valor).',
  'secuencia': [('Después de',
                 'La brújula de valores, El jardín de valores o El bus y los pasajeros.'),
                ('Junto a',
                 'Reglas irrompibles y metas de persona viva cuando la barrera principal es la '
                 'exigencia de perfección.'),
                ('Conecta con',
                 'Soltar el anzuelo (si pesa la F) o El cielo y el clima (si pesa la A).')],
  'titulo': 'De FEAR a DARE'},
 {'archivo': 'act-camino-de-vida.html',
  'conviene': ['Primera consulta o intervenciones breves de una a cuatro sesiones (enfoque FACT).',
               'Personas que llegan atascadas en intentos repetidos de quitarse un malestar antes '
               'de retomar su vida.',
               'Cuando La matriz resulta demasiado esquemática y la imagen de un sendero con dos '
               'extremos se entiende más rápido.'],
  'cuidado': 'El giro de 180° es de orientación de los pies, no de resultados mágicos. Conviene '
             'subrayar que uno gira en el mismo punto del camino en el que está y con el mismo '
             'malestar encima: lo único que cambia hoy es hacia dónde da el primer paso corto.',
  'etq': 'Formulación breve',
  'paraque': 'Formular el caso en una sola sesión o en consulta breve situando los cuatro pilares '
             'vitales, el costo de correr hacia el alivio inmediato y el giro de 180° en pequeños '
             'movimientos de pies hacia una vida con sentido.',
  'secuencia': [('Alternativa a',
                 'La matriz y El costo de la lucha en contextos de atención breve o focalizada.'),
                ('Abre paso a',
                 'De FEAR a DARE o La brújula de valores para sostener el rumbo después del primer '
                 'giro.')],
  'titulo': 'El camino de vida y el giro'},
 {'archivo': 'act-perfeccionismo.html',
  'conviene': ['Parálisis por perfeccionismo, revisión interminable, miedo a entregar avances o a '
               'hablar si no se tiene certeza total.',
               'Autoexigencia rígida donde la persona cree que si suelta el látigo autocrítico '
               'perderá todo su compromiso.',
               'Sobrecontrol y miedo al error en el trabajo, en proyectos personales o en el trato '
               'con otros.'],
  'cuidado': 'La regla de la persona muerta tiene que presentarse con humor cálido y respeto, '
             'nunca como burla. Y al presentar los dos maestros conviene dejar claro que el '
             'maestro compasivo no es permisivo ni indiferente: sostiene el valor con firmeza, '
             'pero cuenta con el error como parte de estar vivo.',
  'etq': 'Acción comprometida',
  'paraque': 'Desarmar el perfeccionismo clínico traduciendo metas de persona muerta («no '
             'equivocarme», «no sentir duda») en metas de persona viva, y cambiando la voz del '
             'crítico implacable por la del maestro firme y compasivo para ensayar un paso '
             'deliberadamente imperfecto.',
  'secuencia': [('Junto a', 'De FEAR a DARE y El yo compasivo.'),
                ('Después de',
                 'Los ochenta años o La brújula de valores, cuando el rendimiento tapó a los '
                 'valores.'),
                ('Antes de',
                 'La escalera de exposición, usando pasos imperfectos como práctica conductual.')],
  'titulo': 'Reglas irrompibles y metas de persona viva'},
 {'archivo': 'met-las-dos-caras.html',
  'conviene': ['Duelo, rupturas, pérdidas, enfermedad, cambios vitales dolorosos o distancia con '
               'seres queridos.',
               'Culpa o tristeza profunda en personas que intentan anestesiarse para no sufrir y '
               'terminan sintiéndose vacías.',
               'Cuando trabajar valores por separado parece frío y trabajar aceptación sola parece '
               'pedir resignación.'],
  'cuidado': 'No usarla para romantizar el sufrimiento ni para decir que el dolor «es bueno». El '
             'dolor duele; lo que la moneda muestra es por qué vale la pena hacerle sitio cuando '
             'del otro lado vive un vínculo o un valor que la persona no quiere apagar.',
  'etq': 'Aceptación y valores',
  'paraque': 'Conectar directamente aceptación y valores mostrando que el dolor y el amor son las '
             'dos caras de una misma moneda: solo dejaría de doler si dejara de importar, y llevar '
             'la moneda entera permite honrar lo que se ama.',
  'secuencia': [('Después de', 'Echar el ancla si el dolor en sesión es muy intenso.'),
                ('Junto a', 'El jardín de valores o Los ochenta años.'),
                ('Abre paso a',
                 'Pausa de autocompasión y un gesto pequeño de honra en la semana.')],
  'titulo': 'Las dos caras de la moneda'},
 {'archivo': 'dbt-aceptacion-radical.html',
  'conviene': ['Pérdidas, rupturas, diagnósticos médicos o decisiones ajenas que la persona vive '
               'como «no debería haber pasado».',
               'Amargura o parálisis crónica donde toda la energía se va en exigir que el pasado '
               'hubiera sido distinto.',
               'Después de Verificar los hechos o Solución de problemas, cuando el hecho es real y '
               'no admite cambio inmediato.'],
  'cuidado': 'Nunca pedir aceptación radical sobre situaciones de abuso o riesgo actual que sí '
             'requieren acción o protección. Y aclarar desde el inicio que aceptar no es aprobar, '
             'perdonar ni rendirse: si no se hace esa distinción, la persona siente que le piden '
             'resignarse.',
  'etq': 'Tolerancia al malestar',
  'paraque': 'Distinguir el dolor limpio de un hecho que hoy no se puede cambiar frente al '
             'sufrimiento de pelear contra él, entrenando girar la mente una y otra vez con manos '
             'dispuestas y media sonrisa.',
  'secuencia': [('Después de',
                 'Tarjeta de crisis si la activación está muy alta, o Solución de problemas cuando '
                 'se comprueba que el hecho hoy no es modificable.'),
                ('Junto a', 'Las dos caras de la moneda o El interruptor de la lucha.'),
                ('Abre paso a',
                 'Mente sabia y un paso pequeño con lo que sí depende de la persona hoy.')],
  'titulo': 'Aceptación radical y girar la mente'},
 {'archivo': 'dbt-abc-please.html',
  'conviene': ['Desregulación emocional frecuente donde cualquier roce cotidiano dispara crisis '
               'porque el cuerpo lleva días sin sueño o sin comida regular.',
               'Agotamiento, apatía o sensación de que «todo me supera».',
               'Prevención de recaídas y armado de rutinas mínimas de cuidado.'],
  'cuidado': 'No convertir los ocho puntos en un pliego de exigencias nuevas para alguien agotado: '
             'se revisa el panorama completo en el escudo y se acuerda proteger un solo ladrillo '
             'sencillo esta semana.',
  'etq': 'Regulación emocional',
  'paraque': 'Hacer visible cómo el descuido del cuerpo (PLEASE) y la falta de momentos gratos, '
             'competencia y ensayo previo (ABC) suben la línea base de reactividad, y elegir un '
             'solo ladrillo concreto para proteger hoy.',
  'secuencia': [('Se detecta en',
                 'Análisis en cadena (como vulnerabilidad previa al episodio) y Tarjeta diaria.'),
                ('Junto a', 'Activación conductual y Ventana de sueño.'),
                ('Antes de',
                 'Situaciones exigentes previsibles, usando la C de anticiparse y ensayar (Cope '
                 'Ahead).')],
  'titulo': 'Escudo ante la vulnerabilidad: ABC PLEASE'},
 {'archivo': 'rodbt-autoinvestigacion.html',
  'conviene': ['Rigidez, perfeccionismo interpersonal, necesidad de corregir a otros o desconexión '
               'fría cuando algo incomoda.',
               'Personas muy reflexivas que usan el análisis intelectual para defenderse y no '
               'sentir vulnerabilidad.',
               'Soledad emocional en personas que por fuera parecen funcionar de manera '
               'impecable.'],
  'cuidado': 'La autoinvestigación no es reestructuración cognitiva ni busca contestar rápido la '
             'pregunta para quedarse tranquilo. Si la persona responde enseguida con una '
             'explicación lógica, señalar con calidez que la mente volvió a cerrarse y volver a '
             'dejar abierta la pregunta.',
  'etq': 'Apertura radical (RO-DBT)',
  'paraque': 'Desarmar el cierre del sobrecontrol (tener siempre razón en mente fija o apagarse en '
             'mente fatalista) activando primero seguridad social en el cuerpo (Gran Tres + 1) y '
             'sosteniendo abierta una pregunta en el propio borde.',
  'secuencia': [('Junto a',
                 'Reglas irrompibles y metas de persona viva, cuando el sobrecontrol domina el '
                 'cuadro.'),
                ('Conecta con',
                 'Fuera y dentro de sesión (FAP), para llevar la apertura al vínculo en vivo.')],
  'titulo': 'Mente fija, mente fatalista y autoinvestigación'},
 {'archivo': 'fap-dentro-y-fuera.html',
  'conviene': ['Dificultades interpersonales crónicas, miedo a la intimidad, complacencia excesiva '
               'o evitación del conflicto.',
               'Cuando en plena consulta se nota que la persona cambia de tema, pide disculpas por '
               'sentir o habla solo en abstracto.',
               'Procesos estancados donde se habla mucho sobre los vínculos de afuera sin que nada '
               'cambie en vivo.'],
  'cuidado': 'Requiere una alianza sólida y que el profesional reciba la CCR2 con autenticidad '
             'cálida (Amor/Sintonía), sin ponerse técnico ni defensivo. Nunca señalar una CCR1 '
             'como reproche: se nombra siempre como una protección comprensible que hoy podemos '
             'ampliar juntos.',
  'etq': 'Relación en vivo (FAP)',
  'paraque': 'Trazar el paralelo entre cómo la persona se protege o se aísla en su vida cotidiana '
             'y cómo asoma eso mismo en la sesión (CCR1), para ensayar aquí y ahora un movimiento '
             'de Conciencia, Coraje y Amor (CCR2).',
  'secuencia': [('Junto a',
                 'La matriz o La brújula de valores (ámbito de relaciones íntimas y amistad).'),
                ('Antes de',
                 'Pedir y decir que no, usando primero el consultorio como lugar seguro de '
                 'ensayo.')],
  'titulo': 'Fuera y dentro de sesión: el puente interpersonal'},
 {'archivo': 'cft-tres-circulos.html',
  'conviene': ['Autoexigencia agotadora, ansiedad de desempeño y culpa al descansar.',
               'Personas que confunden estar ocupadas o rendir con estar reguladas.',
               'Inicio del trabajo en terapia centrada en la compasión (CFT) para desculpabilizar '
               'por qué cuesta tanto calmarse.'],
  'cuidado': 'En algunas personas abrir el círculo verde despierta al principio alerta o tristeza '
             '(«bajar la guardia me da miedo»). Conviene anticiparlo: si el verde lleva años '
             'apagado, se entra de a pocos segundos.',
  'etq': 'Sistema de calma',
  'paraque': 'Mapear de un vistazo el balance entre amenaza (rojo), impulso/logro (azul) y '
             'calma/vínculo (verde), haciendo visible la trampa de usar el sobreesfuerzo azul para '
             'intentar callar el miedo rojo.',
  'secuencia': [('Abre paso a',
                 'Ritmo tranquilizador, Pausa de autocompasión y El yo compasivo, que entrenan '
                 'directamente el círculo verde.'),
                ('Junto a', 'El crítico interno y las voces ante el tropiezo.')],
  'titulo': 'Los tres círculos de regulación emocional'},
 {'archivo': 'cft-voces-y-critico.html',
  'conviene': ['Autocrítica feroz tras cualquier error, descuido o rechazo.',
               'Cuando la persona teme que si deja de tratarse duro se volverá mediocre o '
               'complaciente.',
               'Mezcla confusa de rabia, miedo y tristeza tras un tropiezo.'],
  'cuidado': 'No se trata de pelear contra el crítico ni de expulsarlo de la mesa (eso sería más '
             'sistema de amenaza contra uno mismo), sino de agradecer su intento torpe de proteger '
             'y retirarle el micrófono del maltrato.',
  'etq': 'Autocrítica',
  'paraque': 'Hacer el análisis funcional del crítico interno (de qué amenaza teme que nos dañen) '
             'y sentar en la mesa a las partes ansiosa, triste y enfadada para que el yo compasivo '
             'las coordine sin maltrato.',
  'secuencia': [('Después de', 'Los tres círculos de regulación emocional y El yo compasivo.'),
                ('Junto a',
                 'Soltar el anzuelo o La palabra repetida cuando una frase del crítico es muy '
                 'repetitiva.')],
  'titulo': 'El crítico interno y las voces ante el tropiezo'},
 {'archivo': 'par-el-baile-de-pareja.html',
  'conviene': ['Parejas atrapadas en el ciclo persecución-retirada (uno reclama e insiste, el otro '
               'se calla o se defiende con lógica).',
               'Consultas individuales por conflicto de pareja recurrente donde todo el relato se '
               'va en buscar quién tuvo la culpa.',
               'Cuando cada intento de hablar termina exactamente en la misma pelea.'],
  'cuidado': 'Cuidar la simetría: ni quien reclama es «el intenso culpable» ni quien se calla es '
             '«el frío indiferente». Ambos hacen movimientos desesperados para protegerse del '
             'dolor de apego. Contraindicado encuadrar como baile simétrico si hay violencia o '
             'coacción.',
  'etq': 'Ciclo emocional (EFT)',
  'paraque': 'Desescalar el conflicto de pareja mostrando cómo el movimiento protector de uno en '
             'la superficie dispara el del otro en un bucle infinito, y bajar juntos bajo el agua '
             'hacia las emociones blandas y necesidades de apego.',
  'secuencia': [('Junto a',
                 'Tener razón o cuidar el vínculo (IBCT), que complementa el mapa con la '
                 'separación unificada frente al «ESO».'),
                ('Conecta con',
                 'Pedir y decir que no, una vez que se habla desde abajo del agua y no desde el '
                 'ataque.')],
  'titulo': 'El baile negativo y el iceberg del vínculo'},
 {'archivo': 'par-tener-razon-o-cuidar.html',
  'conviene': ['Diferencias de temperamento, ritmo o estilo en la pareja que ya son conocidas y '
               'vuelven una y otra vez.',
               'Luchas de poder crónicas por tener la razón o demostrar quién aporta más.',
               'Agotamiento por discusiones circulares donde ambos salen heridos.'],
  'cuidado': 'Nombrar «el ESO» con humor o perspectiva nunca debe sonar a minimizar el dolor del '
             'otro. Primero se valida por qué duele (unión empática) y junto con eso se mira el '
             'patrón como equipo.',
  'etq': 'Aceptación en pareja (IBCT)',
  'paraque': 'Pasar de la polarización (intentar ganar el juicio y cambiar al otro) a la '
             'separación unificada y la unión empática: sentarse del mismo lado del banco para '
             'mirar al problema como «nuestro ESO» y hablar con revelación blanda.',
  'secuencia': [('Junto a', 'El baile negativo y el iceberg del vínculo.'),
                ('Conecta con',
                 'La brújula de valores o Los ochenta años, para recordar qué clase de compañero '
                 'se elige ser.')],
  'titulo': 'Tener razón o cuidar el vínculo: frente al «ESO»'},
 {'archivo': 'pp-afecto-positivo.html',
  'conviene': ['Anhedonia, aplanamiento afectivo o depresión donde ya hay activación conductual '
               'pero la persona «no siente gusto por nada».',
               'Tendencia automática a descontar cualquier momento bueno («dura poco», «antes '
               'disfrutaba más»).',
               'Cuando el diario clásico de Tres cosas buenas se queda corto porque los '
               'pensamientos aguafiestas anulan el registro.'],
  'cuidado': 'El «hilo de luz» no es positivismo tóxico ni decir que «todo pasa por algo bueno». '
             'Solo busca notar qué fortaleza o qué apoyo sobrevivió en medio de algo que sí fue '
             'doloroso.',
  'etq': 'Afecto positivo (PAT)',
  'paraque': 'Reentrenar la sensibilidad a la recompensa en la anhedonia y el ánimo bajo '
             'sosteniendo un instante grato sin que lo apaguen los «ladrones del saboreo», '
             'encontrando un hilo de luz en lo difícil y haciendo un gesto pequeño hacia afuera.',
  'secuencia': [('Después de',
                 'Activación conductual, cuando la persona ya hace cosas pero su atención pasa de '
                 'largo por el agrado.'),
                ('Junto a', 'Tres cosas buenas y mi mejor versión.')],
  'titulo': 'Saborear, hilo de luz y dar'},
 {'archivo': 'pp-cuatro-fuentes-sentido.html',
  'conviene': ['Enfermedad médica crónica o grave, pérdidas vitales, jubilación, duelos o crisis '
               'existenciales.',
               'Sensación de vacío o desmoralización cuando una fuente habitual (como el trabajo o '
               'la salud física) se ve limitada.',
               'Cierres de proceso para integrar historia, valores y legado.'],
  'cuidado': 'Si la persona está atravesando una limitación severa, la fuente actitudinal y la '
             'experiencial suelen ser las más accesibles en el día a día: no exigir grandes '
             'proyectos creativos cuando el cuerpo pide presencia y dignidad.',
  'etq': 'Sentido vital (IMCP)',
  'paraque': 'Explorar de dónde beber sentido cuando la vida cambia o se estrecha, recorriendo las '
             'cuatro fuentes de Breitbart y Frankl: histórica (legado), actitudinal (postura ante '
             'el límite), creativa (lo que cuido) y experiencial (amor, belleza y humor).',
  'secuencia': [('Junto a',
                 'La brújula de valores, Los ochenta años y Las dos caras de la moneda.'),
                ('Después de',
                 'Aceptación radical, cuando ya se reconoció el límite real y se busca cómo '
                 'habitarlo con dignidad.')],
  'titulo': 'Las cuatro fuentes de sentido y el legado'},
 {'archivo': 'pp-perdon-reach.html',
  'conviene': ['Rencor crónico o rumia de injusticia hacia alguien del pasado que sigue '
               'consumiendo el presente de la persona.',
               'Cuando la persona quiere soltar el peso de la rabia pero teme que perdonar sea dar '
               'la razón al otro o volver a exponerse.',
               'Heridas familiares, de pareja o laborales antiguas ya cerradas en los hechos pero '
               'abiertas en la memoria.'],
  'cuidado': 'Dejar clarísimo desde el paso 1 que perdonar aquí no obliga a reconciliarse ni a '
             'retomar vínculo con alguien dañino, y que la estación E (entender el contexto del '
             'otro) jamás equivale a excusar ni minimizar el daño sufrido.',
  'etq': 'Perdón (REACH)',
  'paraque': 'Trabajar heridas interpersonales pasadas diferenciando el perdón de la justificación '
             'y de la reconciliación, y recorriendo las cinco estaciones REACH para soltar la '
             'rumia amarga.',
  'secuencia': [('Después de',
                 'Aceptación radical, que prepara el terreno reconociendo que el pasado no se '
                 'puede reescribir.'),
                ('Junto a',
                 'Pausa de autocompasión para sostener el dolor de la herida antes de recorrer la '
                 'estación E.')],
  'titulo': 'Soltar el rencor: los cinco pasos REACH'},
 {'archivo': 'esq-mapa-de-modos.html',
  'conviene': ['Patrones antiguos de carácter o de relación donde la persona oscila entre apagarse '
               '(protector desconectado), someterse o atacar.',
               'Cuando la reestructuración cognitiva estándar no toca la herida emocional de '
               'fondo.',
               'Preparación visual antes del diálogo con sillas o de la reescritura en '
               'imaginación.'],
  'cuidado': 'Al modo protector desconectado nunca se lo ataca ni se le pide que desaparezca a la '
             'fuerza: aprendió a levantar ese muro para proteger al niño cuando no había otra '
             'defensa. Se le agradece su oficio y se le pide dar un paso al costado.',
  'etq': 'Terapia de esquemas',
  'paraque': 'Poner en un solo lienzo qué voz parental presionó o atacó, qué sintió la parte niño '
             'vulnerable, qué muro levantó el modo de afrontamiento y cómo entra el Adulto sano a '
             'poner límite y cuidar.',
  'secuencia': [('Después de',
                 'La flecha descendente, cuando aparecen creencias nucleares de abandono, defecto '
                 'o exigencia implacable.'),
                ('Junto a', 'El crítico interno y las voces ante el tropiezo (CFT).')],
  'titulo': 'Mapa de modos en escena'},
 {'archivo': 'tcc-experimento-conductual.html',
  'conviene': ['Cuando la persona dice «entiendo con la cabeza que no va a pasar nada malo, pero '
               'igual lo siento verdadero».',
               'Ansiedad social, perfeccionismo, pánico o preocupación con muletas de seguridad '
               'muy instaladas.',
               'Para pasar del debate verbal en papel al aprendizaje por experiencia directa.'],
  'cuidado': 'La predicción a probar tiene que ser concreta y observable («nadie me va a dirigir '
             'la palabra»), no una lectura de mente imposible de verificar («pensarán mal de mí en '
             'secreto»). Y sin soltar la muleta, el experimento se invalida.',
  'etq': 'Comprobación empírica',
  'paraque': 'Diseñar una prueba empírica en la vida real soltando deliberadamente la conducta de '
             'seguridad para contrastar lo que la mente predijo frente a lo que ocurrió en los '
             'hechos.',
  'secuencia': [('Después de', 'Registro de pensamientos o La flecha descendente.'),
                ('Junto a',
                 'La escalera de exposición, convirtiendo cada peldaño en una prueba de '
                 'hipótesis.')],
  'titulo': 'El experimento conductual'},
 {'archivo': 'tcc-arco-emocional.html',
  'conviene': ['Cuadros mixtos de ansiedad, depresión o desregulación emocional (enfoque '
               'transdiagnóstico de Barlow).',
               'Para detectar evitaciones emocionales sutiles como mirar el celular, apurarse o '
               'pedir reaseguro.',
               'Como mapa de formulación compartido con el consultante desde las primeras '
               'sesiones.'],
  'cuidado': 'La acción alternativa no se hace para que la emoción desaparezca en el acto, sino '
             'para cambiar la relación con ella y comprobar que no hacía falta escapar.',
  'etq': 'Protocolo unificado',
  'paraque': 'Formular cualquier episodio emocional intenso en sus tres engranajes (pensamientos, '
             'sensaciones y conducta impulsada por la emoción) y entrenar el giro hacia una acción '
             'alternativa que corte las evitaciones sutiles.',
  'secuencia': [('Alternativa a',
                 'Análisis funcional cuando se quiere trabajar el mapa directamente con el '
                 'consultante.'),
                ('Abre paso a',
                 'Exposición a las sensaciones físicas y La escalera de exposición.')],
  'titulo': 'El arco emocional y la acción alternativa'},
 {'archivo': 'tcc-exposicion-interoceptiva.html',
  'conviene': ['Pánico, agorafobia, ansiedad por la salud o miedo intenso a las propias reacciones '
               'corporales.',
               'Antes de las exposiciones en vivo, para perderle el miedo al cuerpo dentro del '
               'consultorio.',
               'Personas que monitorean constantemente su pulso, su respiración o su mareo.'],
  'cuidado': 'Descartar antes condiciones médicas que contraindiquen el ejercicio (asma no '
             'controlada, afecciones cardíacas, embarazo de riesgo, epilepsia). El profesional '
             'hace el ejercicio a la par con la persona para modelar tranquilidad.',
  'etq': 'Exposición interoceptiva',
  'paraque': 'Inducir en el consultorio durante 30 o 60 segundos las sensaciones corporales '
             'temidas (falta de aire, mareo, taquicardia, calor) y observar en el minuto siguiente '
             'cómo bajan solas sin hacer conductas de rescate.',
  'secuencia': [('Después de', 'El arco emocional o El polígrafo.'),
                ('Antes de', 'La escalera de exposición en situaciones externas.')],
  'titulo': 'Exposición a las sensaciones físicas'},
 {'archivo': 'tcc-intolerancia-incertidumbre.html',
  'conviene': ['Trastorno de ansiedad generalizada y preocupación crónica que salta de un tema a '
               'otro.',
               'Personas que revisan diez veces, piden garantías constantes o no delegan nada por '
               'intolerancia a la incertidumbre.',
               'Cuando Aplazar la preocupación necesita completarse con exposiciones conductuales '
               'a la duda.'],
  'cuidado': 'No entrar jamás a responderle el «¿y si…?» dándole garantías de que no va a pasar: '
             'tranquilizar desde el sillón del profesional funciona como otra muleta y alimenta la '
             'intolerancia a la incertidumbre.',
  'etq': 'Incertidumbre (TAG)',
  'paraque': 'Clasificar la preocupación entre problemas actuales modificables y escenarios '
             'hipotéticos («¿y si…?»), detectar las muletas con las que se intenta comprar certeza '
             'al 100 % y ensayar pequeños pasos conviviendo con la duda.',
  'secuencia': [('Junto a', 'Aplazar la preocupación y Solución de problemas.'),
                ('Conecta con',
                 'El experimento conductual, soltando una muleta de certeza cada semana.')],
  'titulo': 'El árbol de la preocupación y la incertidumbre'},
 {'archivo': 'tcc-pastel-autoevaluacion.html',
  'conviene': ['Perfeccionismo clínico donde cualquier error en el trabajo o en el desempeño '
               'derrumba la autoestima entera.',
               'Adicción al trabajo o vida estrechada alrededor de un único rol.',
               'Rupturas o cambios vitales donde se perdió la única fuente de valía que la persona '
               'cultivaba.'],
  'cuidado': 'El pastel ampliado no cambia solo por dibujarlo en sesión: para que la tajada '
             'dominante ceda espacio de verdad, hay que dedicar horas reales en la semana a las '
             'tajadas pequeñas.',
  'etq': 'Perfeccionismo y valía',
  'paraque': 'Visualizar en un gráfico circular cuánto del valor personal depende hoy de una sola '
             'tajada (rendir o no fallar) y construir un segundo pastel más estable activando '
             'otras áreas de la vida.',
  'secuencia': [('Junto a',
                 'Reglas irrompibles y metas de persona viva (ACT) y La flecha descendente.'),
                ('Abre paso a',
                 'Activación conductual para poner en agenda acciones de las tajadas nuevas.')],
  'titulo': 'El pastel de la autoevaluación'},
 {'archivo': 'tcc-trap-a-trac.html',
  'conviene': ['Depresión, apatía, retraimiento o bloqueo ante pendientes acumulados.',
               'Cuando la persona programó actividades en Activación conductual pero no las hizo '
               'porque esperó a tener ganas.',
               'Rumiación en cama o aislamiento como respuesta automática al desánimo.'],
  'cuidado': 'El paso TRAC tiene que ser lo bastante pequeño como para caber en un día malo (diez '
             'minutos, una cuadra, un mensaje honesto). Si se diseña para un día con energía alta, '
             'vuelve a alimentar el bucle TRAP.',
  'etq': 'Activación conductual',
  'paraque': 'Mapear el análisis funcional de la evitación depresiva (Disparador + Respuesta + '
             'Patrón de evitación = TRAP) y accionar el cambio de aguja hacia un afrontamiento '
             'alternativo pequeño (TRAC).',
  'secuencia': [('Junto a',
                 'Activación conductual, como su herramienta compañera para destrabar la '
                 'evitación.'),
                ('Conecta con',
                 'El bus y los pasajeros (ACT): actuar de afuera hacia adentro llevando el desgano '
                 'a bordo.')],
  'titulo': 'Salir de la trampa: de TRAP a TRAC'},
 {'archivo': 'tcc-episodio-de-ira.html',
  'conviene': ['Estallidos verbales, discusiones recurrentes o irritabilidad que daña vínculos o '
               'el trabajo.',
               'Personas que sienten que la rabia les sube «de cero a cien en un segundo» sin '
               'aviso previo.',
               'También cuando la ira no explota hacia afuera sino que queda rumiándose por horas '
               'con resentimiento.'],
  'cuidado': 'En el eslabón 2 no se discute si el otro se portó mal o no: aunque el otro haya sido '
             'injusto, la exigencia rígida («no debería haber pasado») es lo que incendia el '
             'cuerpo y deja a la persona sin mando.',
  'etq': 'Manejo de la ira',
  'paraque': 'Desarmar en cinco eslabones un episodio de ira o irritabilidad para identificar la '
             'exigencia rígida («no debería») y la primera señal corporal que permite cortar la '
             'escalada a tiempo.',
  'secuencia': [('Junto a', 'Autoinstrucciones e Inoculación de estrés.'),
                ('Después va',
                 'Pedir y decir que no (DBT) para expresar el límite de forma asertiva una vez que '
                 'bajó la espuma.')],
  'titulo': 'Anatomía del episodio de ira'},
 {'archivo': 'tcc-dosificar-energia.html',
  'conviene': ['Dolor crónico, fibromialgia, fatiga crónica, enfermedades médicas o agotamiento '
               'por sobrecarga.',
               'Personas todo-o-nada que en cuanto se sienten un poco mejor quieren recuperar toda '
               'la semana atrasada.',
               'Frustración repetida por recaídas físicas tras días de sobreesfuerzo.'],
  'cuidado': 'Parar cuando todavía queda energía se siente antinatural y suele despertar culpa o '
             'miedo a no terminar. Conviene ensayarlo en sesión y elegir cuotas muy modestas al '
             'principio.',
  'etq': 'Dolor y fatiga',
  'paraque': 'Romper la montaña rusa de sobreexigirse en los días con menos dolor hasta colapsar '
             'en cama, instalando cuotas de actividad guiadas por tiempo y pausas programadas '
             'antes del agotamiento.',
  'secuencia': [('Junto a', 'Activación conductual y El interruptor de la lucha.'),
                ('Conecta con',
                 'Los tres círculos de regulación emocional (CFT), cuando el círculo azul empuja a '
                 'ignorar las señales del cuerpo.')],
  'titulo': 'Dosificar la energía: salir del sobrecarga-colapso'}]
),
(
  "Ampliación ACT en literatura clásica (Lote 4)",
  [{'archivo': 'met-trampa-china.html',
  'conviene': ['Cuando la persona dice «he intentado de todo para quitarme esta ansiedad y cada '
               'vez es peor».',
               'Comparar la lucha contra el malestar con meter los índices en el cilindro tejido y '
               'tirar con fuerza hacia afuera.',
               'Mover el deslizador de tensión para contrastar el reflejo de escapar con el gesto '
               'de empujar suavemente hacia adentro.',
               'Escribir a qué sensación concreta se le puede dar hoy un milímetro de holgura en '
               'lugar de jalar.'],
  'cuidado': 'Cuanto más fuerte tiras para escapar de lo que sientes, más se cierra el tejido; '
             'acercarte con suavidad te devuelve el espacio.',
  'etq': 'Aceptación · Metáfora viva',
  'paraque': 'Mostrar en segundos por qué la respuesta intuitiva de jalar hacia afuera para '
             'librarse de la ansiedad o los recuerdos dolorosos aprieta más el tubo de bambú, y '
             'cómo el movimiento contraintuitivo de acercarse con suavidad hacia la experiencia '
             'afloja la presión.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona dice «he intentado de todo para quitarme esta ansiedad y cada '
                 'vez es peor».'),
                ('En sesión',
                 'Comparar la lucha contra el malestar con meter los índices en el cilindro tejido '
                 'y tirar con fuerza hacia afuera. · Mover el deslizador de tensión para '
                 'contrastar el reflejo de escapar con el gesto de empujar suavemente hacia '
                 'adentro. · Escribir a qué sensación concreta se le puede dar hoy un milímetro de '
                 'holgura en lugar de jalar.'),
                ('Abre paso a', 'Arenas movedizas, El dial de la disposición')],
  'titulo': 'La Trampa China para Dedos'},
 {'archivo': 'met-invitado-incomodo.html',
  'conviene': ['Cuando la persona pospone su vida social, afectiva o vocacional hasta el día en '
               'que «ya no sienta incomodidad».',
               'Ponerle nombre a la fiesta valiosa que hoy está en marcha y al invitado molesto '
               'que tocó el timbre.',
               'Alternar entre «Cerrar la puerta y vigilar» y «Permitir que entre y volver a mi '
               'fiesta» para ver qué pasa con el anfitrión.',
               'Acordar cómo atender a los invitados que sí importan aunque el visitante ruidoso '
               'siga merodeando cerca del bufé.'],
  'cuidado': 'No hace falta que te caiga bien el invitado incómodo; solo hace falta que dejes de '
             'abandonar tu propia fiesta por vigilarle la puerta.',
  'etq': 'Aceptación y valores',
  'paraque': 'Evidenciar el costo vital de abandonar la propia fiesta (los valores y vínculos) por '
             'quedarse en la puerta forcejeando para que no entre un vecino ruidoso (la '
             'inseguridad, el miedo o la tristeza).',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona pospone su vida social, afectiva o vocacional hasta el día en '
                 'que «ya no sienta incomodidad».'),
                ('En sesión',
                 'Ponerle nombre a la fiesta valiosa que hoy está en marcha y al invitado molesto '
                 'que tocó el timbre. · Alternar entre «Cerrar la puerta y vigilar» y «Permitir '
                 'que entre y volver a mi fiesta» para ver qué pasa con el anfitrión. · Acordar '
                 'cómo atender a los invitados que sí importan aunque el visitante ruidoso siga '
                 'merodeando cerca del bufé.'),
                ('Abre paso a', 'La diana de valores, El bus y los pasajeros')],
  'titulo': 'El Invitado Incómodo en la Fiesta'},
 {'archivo': 'met-arenas-movedizas.html',
  'conviene': ['En crisis de ansiedad, rumiación nocturna o hipervigilancia corporal donde el '
               'esfuerzo por calmarse multiplica la agitación.',
               'Identificar las formas de «pataleo» actuales (revisar el cuerpo, pelear con la '
               'mente, buscar garantías).',
               'Cambiar el selector a la postura de flotación: abrir los brazos, soltar el peso y '
               'aumentar el área de contacto con la sensación presente.',
               'Definir cómo sería hoy «flotar con lo que hay» durante cinco minutos sin exigir '
               'que desaparezca.'],
  'cuidado': 'En las arenas movedizas, patalear hunde; extender los brazos y apoyarte por completo '
             'sobre la superficie es lo que te permite flotar.',
  'etq': 'Aceptación · Metáfora viva',
  'paraque': 'Explicar por qué las maniobras de urgencia para «salir ya» del pánico, el insomnio o '
             'el bajón emocional hunden un pie mientras intentan levantar el otro, y cómo extender '
             'el cuerpo sobre la superficie permite flotar.',
  'secuencia': [('Cuándo introducirla',
                 'En crisis de ansiedad, rumiación nocturna o hipervigilancia corporal donde el '
                 'esfuerzo por calmarse multiplica la agitación.'),
                ('En sesión',
                 'Identificar las formas de «pataleo» actuales (revisar el cuerpo, pelear con la '
                 'mente, buscar garantías). · Cambiar el selector a la postura de flotación: abrir '
                 'los brazos, soltar el peso y aumentar el área de contacto con la sensación '
                 'presente. · Definir cómo sería hoy «flotar con lo que hay» durante cinco minutos '
                 'sin exigir que desaparezca.'),
                ('Abre paso a', 'Echar el ancla, La trampa china')],
  'titulo': 'Las Arenas Movedizas'},
 {'archivo': 'act-pasear-la-mente.html',
  'conviene': ['Cuando la persona confunde tener un pensamiento de duda o desgano con una orden '
               'obligatoria de detenerse.',
               'Escribir o pulsar los comentarios típicos que la mente suelta cuando se intenta '
               'dar un paso importante.',
               'Colocar a la par la dirección que eligen los pies de la persona que camina.',
               'Practicar agradecerle a la mente su charla («gracias, mente, por avisarme») sin '
               'pedirle que se calle para poder avanzar.'],
  'cuidado': 'Tu mente puede ir todo el paseo diciendo que no vas a poder, y tus pies pueden '
             'seguir caminando exactamente hacia donde tú eliges.',
  'etq': 'Defusión en movimiento',
  'paraque': 'Llevar la defusión del sillón a la acción cotidiana: notar cómo la mente opina, '
             'compara, advierte y critica sin descanso mientras los pies eligen libremente por qué '
             'calle caminar.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona confunde tener un pensamiento de duda o desgano con una orden '
                 'obligatoria de detenerse.'),
                ('En sesión',
                 'Escribir o pulsar los comentarios típicos que la mente suelta cuando se intenta '
                 'dar un paso importante. · Colocar a la par la dirección que eligen los pies de '
                 'la persona que camina. · Practicar agradecerle a la mente su charla («gracias, '
                 'mente, por avisarme») sin pedirle que se calle para poder avanzar.'),
                ('Abre paso a', 'Cambiar «pero» por «y», La cinta de sushi')],
  'titulo': 'Sacar a Pasear a tu Mente'},
 {'archivo': 'act-pero-por-y.html',
  'conviene': ['Cuando el discurso en sesión está lleno de «sí, pero...» donde el malestar aparece '
               'como requisito que debe resolverse antes de actuar.',
               'Anotar la acción valiosa en el primer bloque y la sensación o pensamiento difícil '
               'en el segundo.',
               'Conmutar el interruptor central de «PERO» a «Y» para observar cómo pasan de '
               'excluirse a coexistir.',
               'Llevarse escrita la frase con «Y» como recordatorio de bolsillo para la semana.'],
  'cuidado': 'Un simple «y» devuelve la verdad de la experiencia: puedes sentir miedo y al mismo '
             'tiempo dar el paso que te importa.',
  'etq': 'Defusión · Desliteralización',
  'paraque': 'Desactivar la trampa gramatical del «pero» —que convierte cualquier emoción o '
             'pensamiento en una contradicción que bloquea la acción («quiero ir, pero estoy '
             'ansioso»)— sustituyéndolo por «y» («quiero ir, y estoy ansioso»).',
  'secuencia': [('Cuándo introducirla',
                 'Cuando el discurso en sesión está lleno de «sí, pero...» donde el malestar '
                 'aparece como requisito que debe resolverse antes de actuar.'),
                ('En sesión',
                 'Anotar la acción valiosa en el primer bloque y la sensación o pensamiento '
                 'difícil en el segundo. · Conmutar el interruptor central de «PERO» a «Y» para '
                 'observar cómo pasan de excluirse a coexistir. · Llevarse escrita la frase con '
                 '«Y» como recordatorio de bolsillo para la semana.'),
                ('Abre paso a', 'Sacar a pasear a tu mente, El dial de la disposición')],
  'titulo': 'Cambiar «Pero» por «Y»'},
 {'archivo': 'met-cinta-de-sushi.html',
  'conviene': ['Cuando la persona se siente culpable por el solo hecho de que un pensamiento '
               'aparezca en su cabeza o cree que pensarlo equivale a desearlo.',
               'Mirar la banda en movimiento y agregar los platillos repetitivos que la cocina de '
               'la mente ha estado sacando hoy.',
               'Distinguir qué pasa cuando se «compra» el platillo frente a dejarlo seguir su '
               'recorrido por el riel.',
               'Nombrar qué conversación o tarea valiosa sigue en la mesa mientras la cinta '
               'continúa girando al fondo.'],
  'cuidado': 'La cocina de la mente saca platillos de todo tipo sin preguntarte; tu libertad está '
             'en decidir cuáles dejas pasar de largo por el riel.',
  'etq': 'Defusión · Metáfora viva',
  'paraque': 'Observar los pensamientos intrusivos, catastróficos o autocríticos como platillos '
             'que desfilan solos por la banda transportadora de un restaurante: verlos pasar no '
             'obliga a levantarlos ni a tragarlos.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona se siente culpable por el solo hecho de que un pensamiento '
                 'aparezca en su cabeza o cree que pensarlo equivale a desearlo.'),
                ('En sesión',
                 'Mirar la banda en movimiento y agregar los platillos repetitivos que la cocina '
                 'de la mente ha estado sacando hoy. · Distinguir qué pasa cuando se «compra» el '
                 'platillo frente a dejarlo seguir su recorrido por el riel. · Nombrar qué '
                 'conversación o tarea valiosa sigue en la mesa mientras la cinta continúa girando '
                 'al fondo.'),
                ('Abre paso a', 'Hojas en el arroyo, Describir vs. evaluar')],
  'titulo': 'El Tren de Sushi de los Pensamientos'},
 {'archivo': 'act-piloto-automatico.html',
  'conviene': ['Cuando la persona siente que los días se le pasan en blanco, atrapada en '
               'preocupaciones futuras o reproches del pasado mientras su cuerpo funciona en '
               'automático.',
               'Elegir una actividad cotidiana breve que suele hacerse mirando pantallas o '
               'rumiando.',
               'Marcar las cinco anclas sensoriales (vista, tacto/temperatura, sonido, aroma/sabor '
               'y postura) para encender la presencia.',
               'Registrar dónde tiende a irse la mente y cómo invitarla de vuelta con amabilidad '
               'una y otra vez.'],
  'cuidado': 'Salir del piloto automático no requiere irse a una montaña; empieza la próxima vez '
             'que tomes un vaso de agua notando de verdad su temperatura.',
  'etq': 'Momento presente',
  'paraque': 'Entrenar la atención flexible en las actividades reales del día a día (caminar, '
             'ducharse, tomar café, escuchar), pasando de hacer las cosas ausente en la rumiación '
             'a habitar el presente con los cinco sentidos.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona siente que los días se le pasan en blanco, atrapada en '
                 'preocupaciones futuras o reproches del pasado mientras su cuerpo funciona en '
                 'automático.'),
                ('En sesión',
                 'Elegir una actividad cotidiana breve que suele hacerse mirando pantallas o '
                 'rumiando. · Marcar las cinco anclas sensoriales (vista, tacto/temperatura, '
                 'sonido, aroma/sabor y postura) para encender la presencia. · Registrar dónde '
                 'tiende a irse la mente y cómo invitarla de vuelta con amabilidad una y otra '
                 'vez.'),
                ('Abre paso a', 'Echar el ancla, El punto dulce')],
  'titulo': 'Salir del Piloto Automático'},
 {'archivo': 'act-hecho-o-juicio.html',
  'conviene': ['Cuando la persona relata situaciones o se describe a sí misma usando adjetivos '
               'globales condenatorios como si fueran hechos físicos.',
               'Resolver juntos las cinco tarjetas de entrenamiento distinguiendo hecho observable '
               'de juicio valorativo.',
               'Tomar la frase autocrítica actual y dividirla en dos columnas: lo que registraría '
               'una cámara de video y lo que la mente añade encima.',
               'Redactar una descripción limpia desde el presente que reconozca el juicio como un '
               'producto mental.'],
  'cuidado': '«Tembló mi voz dos veces» es un hecho; «fue un desastre y soy un incapaz» es una '
             'evaluación que tu mente pegó encima.',
  'etq': 'Momento presente y defusión',
  'paraque': 'Separar las propiedades primarias observables de un suceso (lo que vería una cámara) '
             'de las evaluaciones secundarias («desastre», «fracaso», «insoportable») que la mente '
             'funde con la realidad.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona relata situaciones o se describe a sí misma usando adjetivos '
                 'globales condenatorios como si fueran hechos físicos.'),
                ('En sesión',
                 'Resolver juntos las cinco tarjetas de entrenamiento distinguiendo hecho '
                 'observable de juicio valorativo. · Tomar la frase autocrítica actual y dividirla '
                 'en dos columnas: lo que registraría una cámara de video y lo que la mente añade '
                 'encima. · Redactar una descripción limpia desde el presente que reconozca el '
                 'juicio como un producto mental.'),
                ('Abre paso a', 'La cinta de sushi, Soltar el anzuelo')],
  'titulo': 'Describir vs. Evaluar: ¿Hecho o Juicio?'},
 {'archivo': 'act-observador-en-el-tiempo.html',
  'conviene': ['Cuando la persona se siente rota, definida por una crisis reciente o fusionada con '
               'un autoconcepto rígido («yo soy así y no puedo cambiar»).',
               'Evocar con detalle una escena de la niñez, otra de años atrás y la experiencia '
               'corporal de este mismo instante.',
               'Notar el hilo continuo: el cuerpo, los roles y los miedos cambiaron por completo, '
               'pero el testigo que los observó es el mismo «Yo».',
               'Mirar la dificultad actual desde ese espacio consciente que no se daña con lo que '
               'contiene.'],
  'cuidado': 'Todo lo que has pensado y sentido ha cambiado miles de veces, pero quien mira detrás '
             'de tus ojos ha estado ahí entero desde el principio.',
  'etq': 'Yo como contexto',
  'paraque': 'Guiar de forma estructurada el ejercicio clásico del Observador de Hayes et al. '
             '(1999): recorrer un recuerdo infantil, uno de hace unos años y el instante actual '
             'para notar que quien mira detrás de los ojos es más amplio y continuo que cualquier '
             'etapa o emoción.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona se siente rota, definida por una crisis reciente o fusionada '
                 'con un autoconcepto rígido («yo soy así y no puedo cambiar»).'),
                ('En sesión',
                 'Evocar con detalle una escena de la niñez, otra de años atrás y la experiencia '
                 'corporal de este mismo instante. · Notar el hilo continuo: el cuerpo, los roles '
                 'y los miedos cambiaron por completo, pero el testigo que los observó es el mismo '
                 '«Yo». · Mirar la dificultad actual desde ese espacio consciente que no se daña '
                 'con lo que contiene.'),
                ('Abre paso a', 'La casa y los muebles, El tablero de ajedrez')],
  'titulo': 'El Observador Continuo a través del Tiempo'},
 {'archivo': 'met-dos-montanas.html',
  'conviene': ['Al encuadrar el trabajo terapéutico o cuando la persona se siente en un callejón '
               'sin salida y se juzga con dureza por no ver la solución.',
               'Observar el gráfico de las dos montañas y distinguir qué sabe quien lleva las '
               'botas puestas frente a qué se ve desde la ladera de enfrente.',
               'Describir la roca que hoy parece bloquear todo el paso vista de cerca.',
               'Cambiar de montaña para mirar el propio recorrido con la amplitud y el respeto con '
               'que se miraría a un ser querido.'],
  'cuidado': 'Nadie está libre de subir su propia montaña; mirar desde la montaña de enfrente solo '
             'nos regala el ángulo para ver que el sendero continúa.',
  'etq': 'Yo-contexto y perspectiva',
  'paraque': 'Horizontalizar la relación clínica y entrenar la toma de perspectiva hacia uno '
             'mismo: comprender que mirar desde afuera (como desde una montaña vecina) permite ver '
             'senderos que la roca pegada a la cara nos oculta.',
  'secuencia': [('Cuándo introducirla',
                 'Al encuadrar el trabajo terapéutico o cuando la persona se siente en un callejón '
                 'sin salida y se juzga con dureza por no ver la solución.'),
                ('En sesión',
                 'Observar el gráfico de las dos montañas y distinguir qué sabe quien lleva las '
                 'botas puestas frente a qué se ve desde la ladera de enfrente. · Describir la '
                 'roca que hoy parece bloquear todo el paso vista de cerca. · Cambiar de montaña '
                 'para mirar el propio recorrido con la amplitud y el respeto con que se miraría a '
                 'un ser querido.'),
                ('Abre paso a', 'El observador en el tiempo, El yo compasivo')],
  'titulo': 'La Metáfora de las Dos Montañas'},
 {'archivo': 'met-la-casa-y-los-muebles.html',
  'conviene': ['Cuando un recuerdo doloroso, una etiqueta diagnóstica o un estado de ánimo se vive '
               'como si ocupara el cien por ciento de la identidad.',
               'Ubicar en el plano de la casa qué mueble incómodo y qué mueble viejo están hoy en '
               'un rincón, junto con los muebles valiosos que también habitan ahí.',
               'Revisar cuánto cuesta encerrarse en una sola esquina peleando con el mueble '
               'molesto.',
               'Elegir qué habitación valiosa de la casa se va a habitar hoy aunque ese mueble '
               'siga en su rincón.'],
  'cuidado': 'Por más pesado o ruidoso que sea un mueble, un mueble jamás se vuelve la casa ni '
             'estropea el espacio de las habitaciones.',
  'etq': 'Yo como contexto · Metáfora viva',
  'paraque': 'Distinguir entre los contenidos psicológicos transitorios (muebles que entran, '
             'envejecen o incomodan) y el contexto consciente que los aloja (la casa), mostrando '
             'que ningún mueble convierte a la casa en mueble.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando un recuerdo doloroso, una etiqueta diagnóstica o un estado de ánimo se '
                 'vive como si ocupara el cien por ciento de la identidad.'),
                ('En sesión',
                 'Ubicar en el plano de la casa qué mueble incómodo y qué mueble viejo están hoy '
                 'en un rincón, junto con los muebles valiosos que también habitan ahí. · Revisar '
                 'cuánto cuesta encerrarse en una sola esquina peleando con el mueble molesto. · '
                 'Elegir qué habitación valiosa de la casa se va a habitar hoy aunque ese mueble '
                 'siga en su rincón.'),
                ('Abre paso a', 'El observador en el tiempo, El cielo y el clima')],
  'titulo': 'La Casa y los Muebles'},
 {'archivo': 'act-diana-de-valores.html',
  'conviene': ['En evaluación inicial de valores, revisión periódica de proceso o cuando la '
               'persona siente que su semana está desbalanceada.',
               'Nombrar qué cualidad personal importa en cada uno de los cuatro cuadrantes '
               '(trabajo/vocación, relaciones, salud y tiempo libre).',
               'Mover los cuatro deslizadores para ver en tiempo real dónde caen los dardos sobre '
               'la diana.',
               'Identificar el obstáculo interno del cuadrante más alejado y diseñar una acción '
               'concreta para acercar ese dardo un anillo hacia el centro.'],
  'cuidado': 'El blanco de la diana no es que todo salga fácil; es que tu conducta de hoy apunte '
             'hacia la persona que eliges ser.',
  'etq': 'Valores y acción',
  'paraque': "Aplicar visualmente el Bull's-Eye Values Survey (Lundgren et al., 2012): ubicar en "
             'cuatro cuadrantes vitales qué tan cerca del centro valioso están hoy las propias '
             'acciones (no los resultados externos) y elegir un paso hacia el centro.',
  'secuencia': [('Cuándo introducirla',
                 'En evaluación inicial de valores, revisión periódica de proceso o cuando la '
                 'persona siente que su semana está desbalanceada.'),
                ('En sesión',
                 'Nombrar qué cualidad personal importa en cada uno de los cuatro cuadrantes '
                 '(trabajo/vocación, relaciones, salud y tiempo libre). · Mover los cuatro '
                 'deslizadores para ver en tiempo real dónde caen los dardos sobre la diana. · '
                 'Identificar el obstáculo interno del cuadrante más alejado y diseñar una acción '
                 'concreta para acercar ese dardo un anillo hacia el centro.'),
                ('Abre paso a', 'Brújula de valores, El punto dulce')],
  'titulo': "La Diana de Valores (Bull's-Eye)"},
 {'archivo': 'act-punto-dulce.html',
  'conviene': ['Cuando la persona dice «no sé qué me importa, nada me entusiasma» o enumera '
               'únicamente obligaciones impuestas desde afuera.',
               'Evocar sin prisa una escena real —grande o cotidiana— donde sintió que la vida '
               'tenía sabor y presencia.',
               'Notar la resonancia corporal de ese recuerdo y pulsar los ingredientes de valor '
               'que estaban vivos ahí dentro.',
               'Diseñar una forma pequeña de sembrar hoy una gota de esa misma cualidad en la '
               'semana actual.'],
  'cuidado': 'Tus valores más profundos no se inventan con la cabeza; se descubren al mirar qué '
             'momentos de tu vida tuvieron verdadero sabor.',
  'etq': 'Valores experienciales',
  'paraque': 'Conectar con los valores propios cuando las preguntas directas («¿cuáles son tus '
             'valores?») disparan respuestas racionales, complacientes o llenas de «deberías», '
             'entrando en cambio por un recuerdo vivo de plenitud y dulzura (Wilson y DuFrene, '
             '2009).',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona dice «no sé qué me importa, nada me entusiasma» o enumera '
                 'únicamente obligaciones impuestas desde afuera.'),
                ('En sesión',
                 'Evocar sin prisa una escena real —grande o cotidiana— donde sintió que la vida '
                 'tenía sabor y presencia. · Notar la resonancia corporal de ese recuerdo y pulsar '
                 'los ingredientes de valor que estaban vivos ahí dentro. · Diseñar una forma '
                 'pequeña de sembrar hoy una gota de esa misma cualidad en la semana actual.'),
                ('Abre paso a', 'La diana de valores, Las dos caras de la moneda')],
  'titulo': 'El Ejercicio del Punto Dulce (Sweet Spot)'},
 {'archivo': 'act-dial-disposicion.html',
  'conviene': ['Cuando la persona mide el éxito de su semana por «cuánta ansiedad sentí» en vez de '
               'por «cuánta apertura tuve para vivir lo que me importa».',
               'Ubicar en la primera perilla el nivel actual de malestar reconociendo que no '
               'obedece al control directo.',
               'Mover la segunda perilla (disposición) para comprobar cómo cambia la ecuación del '
               'sufrimiento añadido.',
               'Dejar por escrito en qué situación valiosa se subirá hoy el dial de la disposición '
               'y qué sensación se llevará en la mochila.'],
  'cuidado': 'La perilla del malestar no tiene cable directo a tu voluntad, pero la perilla de tu '
             'disposición a avanzar está cien por ciento en tus manos.',
  'etq': 'Acción comprometida y aceptación',
  'paraque': 'Mostrar con dos perillas interactivas la metáfora de las dos escalas de Hayes et al. '
             '(1999): dejar de forcejear con la perilla del malestar (que se traba al intentar '
             'bajarla) para subir la perilla de la disposición a abrir espacio y actuar.',
  'secuencia': [('Cuándo introducirla',
                 'Cuando la persona mide el éxito de su semana por «cuánta ansiedad sentí» en vez '
                 'de por «cuánta apertura tuve para vivir lo que me importa».'),
                ('En sesión',
                 'Ubicar en la primera perilla el nivel actual de malestar reconociendo que no '
                 'obedece al control directo. · Mover la segunda perilla (disposición) para '
                 'comprobar cómo cambia la ecuación del sufrimiento añadido. · Dejar por escrito '
                 'en qué situación valiosa se subirá hoy el dial de la disposición y qué sensación '
                 'se llevará en la mochila.'),
                ('Abre paso a', 'De FEAR a DARE, El interruptor de la lucha')],
  'titulo': 'El Dial de la Disposición vs. el Dial del Dolor'}]
),
]

# Encadenamientos que se repiten. Cada uno es una secuencia de hojas.
# Correcciones de redacción tras el rework de escenas (ver ajustes_texto.py).
import ajustes_texto as _ajustes
_FICHAS = {e["archivo"]: e for _g, _l in GUIA for e in _l}
_HALLADOS_GUIA = _ajustes.aplicar(_FICHAS)
for _g, _l in GUIA:
    for _i, _e in enumerate(_l): _l[_i] = _FICHAS[_e["archivo"]]

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
           ("Quién lleva los globos","act-quien-lleva-los-globos.html"),
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
    border-radius:999px;padding:5px 12px;background:#fff;white-space:normal;line-height:1.35}
  .ruta .cadena a:hover{border-color:var(--acento);color:var(--acento)}
  .ruta .cadena i{color:#b3bfca;font-style:normal;font-size:14px}

  h2.enfoque{margin:26px 0 2px;font-size:20px;display:flex;align-items:center;gap:10px}
  h2.enfoque::before{content:"";width:13px;height:13px;border-radius:50%;background:currentColor}

  .fichas{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,380px),1fr));gap:14px;
    margin-top:13px}
  .ficha-guia{background:var(--papel);border:1px solid var(--linea);border-left-width:5px;
    border-radius:var(--radio);padding:16px 19px;min-width:0;overflow-wrap:break-word}
  .ficha-guia.hx-item-vinculado{border-style:dashed;border-left-style:solid;background:#fafcfe}
  .ficha-guia .hx-tags{margin:0 0 10px}
  .ficha-guia .cab{display:flex;align-items:flex-start;justify-content:space-between;flex-wrap:wrap;gap:8px;
    margin-bottom:6px}
  .ficha-guia h3{margin:0;font-size:17px;line-height:1.3;letter-spacing:-.2px;min-width:0;flex:1 1 200px;overflow-wrap:break-word}
  .ficha-guia h3 a{color:inherit;text-decoration:none}
  .ficha-guia h3 a:hover{text-decoration:underline}
  .ficha-guia .etq{font-size:10.5px;text-transform:uppercase;letter-spacing:.8px;font-weight:700;
    white-space:normal;max-width:100%;overflow-wrap:anywhere;line-height:1.3;border-radius:999px;padding:3px 10px;flex:0 0 auto}
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
  .ficha-guia details.guion{margin-top:12px;border-top:1px dashed var(--linea);padding-top:10px}
  .ficha-guia details.guion summary{cursor:pointer;font-size:13px;color:var(--acento);
    font-weight:600;list-style:none;display:inline-flex;align-items:center;gap:7px}
  .ficha-guia details.guion summary::-webkit-details-marker{display:none}
  .ficha-guia details.guion summary::before{content:"+";display:inline-flex;align-items:center;
    justify-content:center;width:16px;height:16px;border:1px solid var(--linea);border-radius:4px;
    font-size:13px;line-height:1}
  .ficha-guia details.guion[open] summary::before{content:"−"}
  .ficha-guia .tramo-guion{margin-top:13px}
  .ficha-guia .tramo-guion p{margin:0 0 7px;font-size:13.5px;line-height:1.55;
    color:var(--tinta-suave)}
  /* lo entrecomillado es lo que se dice en voz alta, tal cual */
  .ficha-guia .tramo-guion p.dice{color:#23404f;background:var(--acento-claro);border-radius:8px;
    padding:10px 13px;font-size:14px;line-height:1.5;margin-bottom:8px}
  /* y lo tachado es lo que arruina el ejercicio */
  .ficha-guia .tramo-guion p.no{color:var(--alerta);background:var(--alerta-fondo);
    border:1px solid var(--alerta-linea);border-radius:8px;padding:8px 12px;font-size:13.5px;
    margin-bottom:6px}
  @media (max-width:760px){.fichas{grid-template-columns:1fr}}
  @media print{
    body{background:#fff}
    .volver{display:none}
    .ficha-guia,.ruta{break-inside:avoid}
    details.guion > *{display:block}
    .fichas{grid-template-columns:1fr 1fr}
  }
"""


def con_guiones(guia):
    """Engancha a cada ficha el guion de sesión que le corresponda, si lo tiene."""
    for _, hojas in guia:
        for h in hojas:
            libreto = guiones.GUIONES.get(h["archivo"])
            if libreto:
                h["guion"] = libreto
    return guia


def guion(bloques):
    """El guion de sesión, plegado dentro de la ficha.

    Cada bloque es (título, [líneas]). Una línea que empieza por « es lo que se
    dice en voz alta y se pinta como tal; una que empieza por ✗ es lo que no se
    dice. El resto son indicaciones para quien acompaña.
    """
    partes = []
    for titulo, lineas in bloques:
        cuerpo = []
        for l in lineas:
            clase = ' class="dice"' if l.startswith("«") else (
                    ' class="no"' if l.startswith("✗") else "")
            cuerpo.append("        <p%s>%s</p>" % (clase, l))
        partes.append('      <div class="tramo-guion"><div class="rot">%s</div>%s%s%s      </div>'
                      % (titulo, SALTO, SALTO.join(cuerpo), SALTO))
    return (SALTO + '      <details class="guion">' + SALTO +
            "        <summary>Guion para proponerlo en sesión</summary>" + SALTO +
            SALTO.join(partes) + SALTO + "      </details>")


def ficha(h, color, enfoque):
    info = rieles.info_organizacion(h["archivo"])
    atrs_hx = ""
    if info["proc"]:
        atrs_hx = (
            f' data-proc="{info["proc"]}"'
            f' data-proc-sec="{",".join(info["sec"])}"'
            f' data-estilo="{info["estilo"]}"'
        )
    insignias = rieles.insignias_hexaflex(h["archivo"])
    bloque_insignias = f"\n      {insignias}" if insignias else ""
    conviene = "\n".join("        <li>%s</li>" % c for c in h["conviene"])
    pasos = "\n".join('      <div class="paso"><b>%s</b> %s</div>' % (r, t)
                      for r, t in h["secuencia"])
    aviso = ('\n      <div class="aviso-uso"><b>Cuidado</b>%s</div>' % h["cuidado"]) \
        if h.get("cuidado") else ""
    libreto = guion(h["guion"]) if h.get("guion") else ""
    return f"""    <div class="ficha-guia" style="border-left-color:{color}" data-item data-enf="{enfoque}" data-titulo="{_h.escape(h['titulo'])}" data-href="{h['archivo']}"{atrs_hx}>
      <div class="cab">
        <h3><a href="{h['archivo']}">{h['titulo']}</a></h3>
        <span class="etq" style="color:{color};background:{color}1a">{h['etq']}</span>
      </div>{bloque_insignias}
      <p class="paraque"><b>Para abrir la conversación:</b> {sesion.descripcion(h['archivo'])}</p>
      <p class="paraque">{h['paraque']}</p>
      <div class="rot">Conviene en</div>
      <ul>
{conviene}
      </ul>
      <div class="rot">Secuencia</div>
{pasos}{aviso}{libreto}
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

    todas = []
    for _, hojas in con_guiones(GUIA):
        todas.extend(hojas)
    todas.sort(key=lambda h: (rieles.info_organizacion(h["archivo"])["orden_org"], h["archivo"]))

    bloques = []
    for enfoque in rieles.ENFOQUES:
        color = COLORES[enfoque]
        propias = [h for h in todas if rieles.info_organizacion(h["archivo"])["enfoque"] == enfoque]
        if not propias:
            continue
        subs = rieles.SUBGRUPOS.get(enfoque, [])
        panel_hx = ("\n" + rieles.bloque_hexaflex()) if enfoque == "ACT" else ""

        if len(subs) > 1:
            bloques_sub = []
            for sub_id, sub_titulo, sub_desc, sub_color, sub_est in subs:
                de_sub = [h for h in propias if rieles.info_organizacion(h["archivo"])["subgrupo"] == sub_id]
                if not de_sub:
                    continue
                fichas = "\n".join(ficha(h, sub_color if enfoque == "ACT" else color, enfoque) for h in de_sub)
                corto = rieles.PROC_POR_ID[sub_id]["corto"] if sub_id in rieles.PROC_POR_ID else sub_titulo.split("·")[-1].strip()
                atr_proc = f' data-subproc="{sub_id}"' if enfoque == "ACT" else ""
                aviso_vinc = (
                    '<p class="sub-vinc-aviso" hidden>También vinculadas con el proceso elegido desde este vértice del hexaflex</p>'
                    if enfoque == "ACT" else ""
                )
                bloques_sub.append(f"""  <div class="subgrupo" data-subgrupo="{sub_id}" data-subcorto="{_h.escape(corto)}"{atr_proc} style="--sub-c:{sub_color}">
    <div class="subgrupo-cab">
      <h3><span class="sub-punto"></span>{_h.escape(sub_titulo)}</h3>
      <span class="sub-est">{_h.escape(sub_est)}</span>
    </div>
    <p class="sub-desc">{_h.escape(sub_desc)}</p>
    {aviso_vinc}
    <div class="fichas">
{fichas}
    </div>
  </div>""")
            interior = f'  <div class="subgrupos">\n{chr(10).join(bloques_sub)}\n  </div>'
        else:
            fichas = "\n".join(ficha(h, color, enfoque) for h in propias)
            interior = f'  <div class="fichas">\n{fichas}\n  </div>'

        bloques.append(f"""<section data-grupo="{enfoque}">
<h2 class="enfoque" style="color:{color}">{enfoque}</h2>{panel_hx}
{interior}
</section>""")

    rutas = "\n".join(ruta(r) for r in RUTAS)
    cuantas = len(todas)

    salida = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guía rápida de uso</title>
<style>
{kit_css}
{CSS}
{rieles.CSS}
</style>
</head>
<body data-extra="&lt;a class=&quot;extra&quot; href=&quot;#encadenamientos&quot;&gt;Encadenamientos frecuentes&lt;/a&gt;&lt;a class=&quot;extra&quot; href=&quot;index.html&quot;&gt;Volver a las herramientas&lt;/a&gt;">
<div class="envoltura con-rieles">

<div class="cab">
<a class="volver" href="index.html">&larr; Volver a las herramientas</a> <a class="volver" href="lecturas-act.html" style="margin-left:8px">Lecturas ACT &rarr;</a>

<header class="tapa">
  <h1>Guía rápida de uso</h1>
  <p class="sub">Para qué sirve cada una de las {cuantas} hojas, en qué casos rinde, con qué va
  antes o después, y dónde conviene tener cuidado. Los títulos abren la herramienta.</p>
</header>
</div>

{rieles.controles("Buscar una hoja por nombre, uso o cuidado…")}

<main class="centro">
<section class="bloque" id="encadenamientos">
  <h2>Encadenamientos frecuentes</h2>
  <p class="ayuda">No son protocolos: son los órdenes que suelen funcionar. Lo que casi nunca
  funciona es empezar por el final.</p>
  <div class="rutas">
{rutas}
  </div>
</section>

{chr(10).join(bloques)}

<div class="sin-resultados" id="sin-resultados" hidden>Ninguna hoja coincide con el filtro y la búsqueda.</div>
</main>

{rieles.MAPA}

</div>
<script>{rieles.JS}</script>
</body>
</html>
"""
    (DESTINO / "guia.html").write_text(salida, encoding="utf-8")
    return cuantas


if __name__ == "__main__":
    n = construir()
    print(f"  guia.html con {n} fichas")
