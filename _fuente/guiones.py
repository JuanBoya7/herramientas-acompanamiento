# -*- coding: utf-8 -*-
"""
Los guiones de sesión de las metáforas vivas.

Viven aparte de guia.py porque son largos y crecen: guia.py dice para qué sirve
cada hoja y en qué casos, y esto dice cómo se propone en voz alta.

Cada guion es una lista de bloques (título, [líneas]). Dentro de las líneas:

    «...»   lo que se dice en voz alta, tal cual
    ✗ ...   lo que no se dice, porque arruina el ejercicio
    resto   indicaciones para quien acompaña

Solo llevan guion las hojas experienciales, donde lo que se dice al presentarlas
decide si el ejercicio ocurre o se convierte en otra cosa. Las de registro y las
de evaluación no lo necesitan: ahí la ficha de uso basta.
"""

GUIONES = {

# ---------------------------------------------------------------- el tablero
"met-el-tablero.html": [
 ("Antes de proponerlo", [
  "Pide que la persona haya intentado ganar de verdad, dentro y fuera de la hoja. Ofrecer «ser el "
  "tablero» antes de que haya sentido la inutilidad de empujar la convierte en una idea bonita y "
  "nada más.",
  "El botón verde no se toca temprano. Que empuje varias veces primero, y que la partida corra "
  "sola un rato: las negras que brotan sin que nadie empuje son la mitad del argumento."]),

 ("Cómo se presenta", [
  "«Vamos a jugar una partida que llevas años jugando. De un lado las piezas que quieres que "
  "ganen, del otro las que quieres que desaparezcan.»",
  "«Empuja todo lo fuerte que quieras. Yo no te voy a decir cuándo parar.»"]),

 ("Durante", [
  "Dejarlo empujar. No sugerir el cambio de posición hasta que aparezca el cansancio, o hasta que "
  "él mismo diga que no sale ninguna.",
  "Cuando llegue ese momento, señalar el marcador sin comentarlo: «mira ese número». El cero de "
  "negras sacadas habla mejor solo.",
  "Al pasar a ser el tablero, apretar y callarse unos segundos antes de decir nada."]),

 ("El cambio de posición", [
  "«Fíjate que las piezas siguen ahí, y siguen llegando. Lo único que cambió es desde dónde las "
  "estás mirando.»",
  "«Y mira el marcador de energía: se detuvo.»"]),

 ("Al terminar", [
  "«¿Qué cosas de tu vida quedaron esperando a que ganaras esta partida?»"]),

 ("Lo que no se dice", [
  "✗ «Tú no eres tus pensamientos.» Es la conclusión del ejercicio, y dicha antes de tiempo se "
  "queda en eslogan.",
  "✗ «Ahora ya no te van a afectar.» Van a afectar igual; lo que cambia es desde dónde se miran.",
  "✗ Explicar el yo observador con teoría. Acaba de ocurrirle; explicarlo lo devuelve a idea."]),

 ("Qué hacer con lo que salga", [
  "Pregunta «¿y entonces cómo saco las negras?»: esa pregunta muestra que sigue siendo pieza. No "
  "se corrige, se devuelve tal cual.",
  "Dice que se sintió aliviado siendo el tablero: bien, y conviene comprobar que no lo esté usando "
  "como técnica para que las piezas se vayan. Si es eso, volvió a la partida.",
  "No consigue soltar la posición de pieza: no se insiste. La hoja hizo su parte mostrando el "
  "cero, y eso ya es material."]),
],

# ------------------------------------------------------- el jardín de valores
"met-jardin-de-valores.html": [
 ("Antes de proponerlo", [
  "Es la alternativa a la brújula cuando preguntar «¿cuáles son tus valores?» produce silencio o "
  "discurso aprendido. No exige escribir ni argumentar.",
  "El momento clínico no es sembrar: es tener que dejar catorce afuera."]),

 ("Cómo se presenta", [
  "«Un jardín tiene espacio para seis surcos, no para veinte. Lo que dejes afuera no es que no "
  "importe: es que no cabe.»",
  "«No hay respuesta correcta, y no voy a opinar de lo que siembres.»"]),

 ("Durante", [
  "Cuando dude a quién dejar afuera, no ayudarle a decidir. Esa incomodidad es el ejercicio.",
  "Si dice «es que todos importan»: «claro que sí, y aun así hay seis surcos».",
  "Al regar: «con lo que hiciste esta semana, no con lo que quisieras hacer». Esa frase es la que "
  "separa el jardín de una lista de buenas intenciones."]),

 ("Al terminar", [
  "«¿Cuál está más marchito?» Esperar.",
  "Y solo después: «¿qué es lo más pequeño que lo regaría?»"]),

 ("Lo que no se dice", [
  "✗ «Deberías regar más la familia.» El jardín es suyo, incluidas las decisiones que incomodan.",
  "✗ Comparar unos surcos con otros, o con los de otra persona.",
  "✗ Convertir el surco más seco en tarea de la semana antes de saber qué lo secó."]),

 ("Qué hacer con lo que salga", [
  "No logra sembrar ni tres: la conversación ya no es de valores, es de aplanamiento. Conviene "
  "tamizar sintomatología depresiva antes de seguir.",
  "Siembra seis y los riega todos al máximo: suele ser deseabilidad. Bajar a la semana concreta, "
  "día por día, y volver a regar.",
  "Aparece un surco que rieg mucho y que no eligió como valor: mirarlo. Casi siempre es evitación "
  "bien disfrazada de responsabilidad."]),
],

# -------------------------------------------------- la cuerda y el monstruo
"met-la-cuerda.html": [
 ("Antes de proponerlo", [
  "No anunciar que al final hay una solución. Si se dice «vas a ver qué hacer», la persona espera "
  "la técnica y no vive el desgaste, que es lo único que enseña esta hoja."]),

 ("Cómo se presenta", [
  "«Al otro lado hay un monstruo y entre los dos un hoyo sin fondo. Ponle el nombre de eso con lo "
  "que llevas años haciendo fuerza.»",
  "«Cuando empiece, él jala solo, hagas lo que hagas. Tú haz lo que harías.»"]),

 ("Durante: no sugerir soltar", [
  "Es lo más importante de esta hoja. Si el profesional dice «suéltala», soltar se convierte en la "
  "respuesta correcta de un examen y deja de ser una elección.",
  "Dejarlo jalar hasta que note que los centímetros que gana le duran cada vez menos, o hasta que "
  "se caiga al hoyo. Las dos cosas sirven.",
  "Si pregunta qué debe hacer: «lo que harías»."]),

 ("Cuando suelte", [
  "«Fíjate en dos cosas: no se cayó, y dejaste de acercarte al borde.»",
  "Después, señalar el contador de segundos con la cuerda en el suelo, y dejarlo correr un rato "
  "sin decir nada. Ese rato incómodo es la práctica."]),

 ("Al terminar", [
  "«¿Qué cosas dejaste de hacer todos estos años porque tenías las manos ocupadas?»"]),

 ("Lo que no se dice", [
  "✗ «Suéltala.» Como instrucción, convierte la aceptación en una tarea más.",
  "✗ «¿Ves? Era más fácil soltar.» No es más fácil, y decirlo invalida lo que acaba de costarle.",
  "✗ «Aceptar es dejar de luchar.» Dicho así suena a resignarse, que es lo contrario."]),

 ("Qué hacer con lo que salga", [
  "Entiende soltar como rendirse: se retrocede al inventario de costos, no se insiste. La hoja lo "
  "deja explícito, el monstruo sigue de pie.",
  "Vuelve a agarrar la cuerda enseguida: normal y útil. «¿Qué te hizo agarrarla otra vez?»",
  "La medida de la sesión son los segundos con la cuerda en el suelo, no si soltó. Quince segundos "
  "sosteniendo valen más que un soltar que dura dos."]),
],

# --------------------------------------------------- el bus y los pasajeros
"met-el-bus.html": [
 ("Antes de proponerlo", [
  "Necesita un destino propio. Si la dirección es prestada, la hoja convierte un valor ajeno en un "
  "plan y aprieta más la trampa. Preguntar de quién es la dirección antes de arrancar."]),

 ("Cómo se presenta", [
  "«Tú manejas. Ellos se subieron sin permiso y no se bajan en la próxima esquina.»",
  "«No hay botón para avanzar: el bus anda solo mientras lo dejes andar. Lo único que vas a poder "
  "tocar es el freno, y aparece cuando ellos griten.»"]),

 ("Durante: callarse cuando aparezca el botón rojo", [
  "La tensión de tenerlo ahí unos segundos y decidir es el ejercicio entero. Cualquier comentario "
  "en ese momento decide por él.",
  "Si para a discutir, no comentarlo mientras ocurre. El tablero lo dice después y lo dice mejor."]),

 ("Al terminar", [
  "Mirar los tres números juntos: kilómetros, reloj y energía.",
  "«¿Dónde se fue el tiempo?»"]),

 ("Lo que no se dice", [
  "✗ «No les hagas caso.» No se puede no hacer caso a propósito.",
  "✗ «Ignóralos.» Ignorar a propósito es otra forma de pelear, y cuesta lo mismo.",
  "✗ Señalar cada parada mientras ocurre. Convierte el viaje en una evaluación."]),

 ("Qué hacer con lo que salga", [
  "Llegó sin parar ninguna vez: no felicitarlo. Preguntar qué hizo con las ganas de tocar el "
  "botón, que es lo que se está entrenando.",
  "Se quedó sin energía antes de llegar: es la mejor sesión posible. Que lea él el tablero y diga "
  "en qué se le fue.",
  "Paró en todas: no es fracaso, es su patrón dibujado. «¿Se parece a algo?»",
  "Dice que discutir «a veces sí sirve»: no discutirlo. Volver a correr el viaje y mirar los "
  "kilómetros."]),
],

# ------------------------------------------------------- los ochenta años
"met-los-ochenta-anos.html": [
 ("Antes de proponerlo", [
  "Es la hoja que más culpa moviliza, y la culpa produce evitación, no cambio. No se abre sin "
  "tener decidido que se baja a una acción pequeña en la misma sesión.",
  "No usarla en duelo reciente agudo, ni con riesgo sin preparar."]),

 ("Cómo se presenta", [
  "«Cumples ochenta años. Hay una mesa larga y tres personas que se levantan a decir quién fuiste "
  "con ellas. No qué lograste: quién fuiste.»",
  "«Elige lo que te gustaría que dijeran. No lo que dirían hoy.»"]),

 ("El calibrador", [
  "«Ahora mueve una sola cosa: cuánto se pareció a eso el último mes.»",
  "Y callarse mientras lo mueve. Las frases que se apagan en la mesa no necesitan comentario."]),

 ("Al terminar", [
  "Primero, nombrar explícitamente que la distancia es información y no un veredicto. Sin esa "
  "frase, la hoja se lee como una acusación.",
  "«¿Cuál de esas frases te dolió más ver apagarse?»",
  "Y de inmediato, sin dejar que se instale la culpa: «¿qué es lo más pequeño que la encendería un "
  "poco esta semana?»"]),

 ("Lo que no se dice", [
  "✗ «¿Y qué estás esperando?» Es un reproche con forma de pregunta.",
  "✗ «Todavía tienes tiempo de cambiarlo.» Consuela, y al consolar desactiva.",
  "✗ Terminar la sesión en la distancia, sin bajar a conducta. Eso deja culpa sin salida."]),

 ("Qué hacer con lo que salga", [
  "Llora: es esperable y no hay que rescatarlo enseguida. Esperar, y después la acción pequeña.",
  "Pone todas las frases al máximo: suele ser evitación del ejercicio. Probar con un invitado que "
  "sepa la verdad, sin adornos.",
  "La culpa se vuelve autoataque: cortar la hoja y pasar a Autoinstrucciones o a la brújula. Aquí "
  "no se sigue empujando."]),
],

# ------------------------------------------------------------- el polígrafo
"met-el-poligrafo.html": [
 ("Antes de proponerlo", [
  "Dura poco y pega fuerte: dos o tres minutos bastan.",
  "Con pánico activo, no antes de tener un anclaje disponible."]),

 ("Cómo se presenta", [
  "«Te conectan a esto y te dan una sola regla: no puedes ponerte ansioso. Si la aguja llega "
  "arriba, llega la descarga.»",
  "«Tienes dos botones para bajarla. Úsalos.»"]),

 ("Durante: invitar a apretar", [
  "No advertir de lo que va a pasar. La lección la da el mecanismo, y avisarla se la quita.",
  "No señalar el piso mientras sube. Que suba solo."]),

 ("El momento", [
  "Cuando ya lleve varios intentos, una sola frase: «mira la línea de abajo».",
  "Y esperar a que él diga qué ve."]),

 ("Al terminar", [
  "«¿Estaba ahí cuando empezaste?»",
  "Y después: «¿cuánto llevas haciendo esto afuera de aquí?»"]),

 ("Lo que no se dice", [
  "✗ «¿Ves que no sirve?» Tiene que llegar él, o no llega.",
  "✗ «Entonces deja de intentar controlarlo.» Es una instrucción de control más, con otro nombre.",
  "✗ Cerrar la sesión en la demostración. Siempre se baja después a valores o a la cuerda."]),

 ("Qué hacer con lo que salga", [
  "No apretó ningún botón: mostrarle el marcador de segundos sin tocar nada y preguntar qué hizo "
  "con las ganas. Ese marcador es la otra mitad de la hoja.",
  "Sale con «entonces no hay nada que hacer»: faltó cerrar. La desesperanza creativa sin salida "
  "hacia valores es solo desesperanza, y eso no se deja para la próxima sesión.",
  "Llegó a la descarga: preguntar qué la produjo. Que el castigo por sentirlo produzca más de lo "
  "que castiga suele ser la frase que se lleva."]),
],

# -------------------------------------------------------- la palabra repetida
"met-la-palabra-repetida.html": [
 ("Antes de proponerlo", [
  "Una o dos palabras, y que sea un descriptor de uno mismo.",
  "Nunca con palabras ligadas a trauma, a abuso ni al nombre de quien hizo daño: repetir eso no "
  "defusiona, revictimiza.",
  "Hace falta privacidad real. Si no la dice en voz alta, no ocurre nada."]),

 ("Cómo se presenta", [
  "«Vamos a hacer un ejercicio que va a sonar absurdo, y esa es exactamente la idea.»",
  "«Primero con una palabra cualquiera, para que veas qué pasa donde no duele.»"]),

 ("Después del turno de ensayo", [
  "«¿Qué le pasó a la palabra?» y dejar que él lo nombre.",
  "Que sea él quien diga «se volvió un sonido» es lo que hace que el segundo turno funcione. Si lo "
  "dice el profesional, el segundo turno se convierte en una expectativa que cumplir."]),

 ("El turno con la palabra propia", [
  "Calibrar antes, sin comentar el número que ponga.",
  "«Lo mismo, con la tuya. En voz alta, y la digo contigo si te ayuda.» Decirla a la par baja "
  "mucho la vergüenza, y la vergüenza es lo que hace que la digan por dentro."]),

 ("Al terminar", [
  "Recalibrar primero, hablar después.",
  "«La palabra no cambió, y lo que dice sigue siendo lo mismo. ¿Qué cambió?»"]),

 ("Lo que no se dice", [
  "✗ «¿Viste que no significa nada?» Sí significa. Lo que cambió es cuánto pesa.",
  "✗ «Entonces no es verdad.» El ejercicio no discute el contenido, y meterlo ahí lo deshace.",
  "✗ Insistir si se resiste a decirla en voz alta. Esa resistencia es información, no un obstáculo."]),

 ("Qué hacer con lo que salga", [
  "El peso no bajó: no es fracaso. «¿Qué la sostiene?» Con frecuencia la respuesta trae la "
  "historia que hay detrás de la palabra, y ahí estaba el trabajo.",
  "Se rió: excelente señal. La risa en este ejercicio es defusión ocurriendo.",
  "Se angustió mucho: parar y anclar. La palabra estaba más cargada de lo que parecía, y conviene "
  "revisar de dónde viene antes de repetir el ejercicio."]),
],

# --------------------------------------------------- la radio que no se apaga
"met-la-radio.html": [
 ("Antes de proponerlo", [
  "Va después de haber practicado observar, no antes. Es el puente entre la defusión y la acción, "
  "y sin la práctica previa se lee como un ejercicio de concentración."]),

 ("Cómo se presenta", [
  "«Hay una emisora que lleva años transmitiendo y no tiene botón de apagado. Vamos a poner lo que "
  "dice la tuya.»",
  "«Al lado hay una tarea de doce pasos. Lo que vamos a mirar es si la terminas, no si la radio se "
  "calla.»"]),

 ("Durante", [
  "No comentar la radio mientras habla.",
  "Si baja el volumen y la emisora empieza a hablar más seguido, dejarlo notar solo. Si se lo "
  "explica el profesional, deja de ser un descubrimiento y pasa a ser un dato."]),

 ("Al terminar", [
  "«¿La terminaste?»",
  "Y después: «¿la radio se apagó en algún momento?»"]),

 ("Lo que no se dice", [
  "✗ «Ignórala.» No se puede a propósito, y el intento cuesta más que la radio.",
  "✗ «Concéntrate y no la escuches.» Eso es supresión, y la supresión sube la frecuencia.",
  "✗ Felicitar por el tiempo que tardó. Convierte la tarea en desempeño y ese no es el punto."]),

 ("Qué hacer con lo que salga", [
  "La apagó varias veces y terminó igual: es el mejor desenlace posible, y conviene nombrarlo tal "
  "cual. Intentó callarla, no lo consiguió, y aun así hizo lo que iba a hacer.",
  "Terminó rápido y dice que ni la vio: preguntar si se puso en automático. El automatismo también "
  "es evitación, y distinguirlo de la disposición vale la conversación.",
  "No terminó: material. Qué la detuvo exactamente, y en qué paso."]),
],

# --------------------------------------------------- el hombre en el hoyo
"met-el-hoyo.html": [
 ("Antes de proponerlo", [
  "Sirve como puerta de entrada, incluso antes de tener formulación. Dos minutos bastan."]),

 ("Cómo se presenta", [
  "«Estás dentro de un hoyo y lo único que te dieron es una pala. Dime con qué has estado "
  "cavando.»",
  "«Mantén apretado el botón todo lo que quieras.»"]),

 ("Durante: dejarlo cavar", [
  "Sin decir nada. La barra de «voy avanzando» hace todo el trabajo, y hablar encima lo estropea.",
  "Si pregunta si eso lo va a sacar: «cava y mira»."]),

 ("El momento", [
  "Cuando suelte el botón y vea la barra vaciarse sola, una sola frase: «esa barra se vació. La "
  "profundidad no.»",
  "Y esperar."]),

 ("Al terminar", [
  "«¿Qué necesitarías, que no sea una pala?»",
  "Aguantar el silencio sin ofrecer la respuesta. La metáfora no tiene salida, y fabricarle una en "
  "ese momento apaga todo lo anterior."]),

 ("Lo que no se dice", [
  "✗ «Deja de cavar.» No hay adónde ir todavía, y sin alternativa suena a quitarle lo único que "
  "tiene.",
  "✗ Ofrecerle la escalera. Su trabajo es que la pala deje de parecer la herramienta, no dar otra.",
  "✗ «Entonces todo lo que has hecho estuvo mal.» No es eso: funcionó para aliviar, y por eso lo "
  "siguió haciendo. Lo que no hizo fue sacarlo."]),

 ("Qué hacer con lo que salga", [
  "Dice «pero algo tengo que hacer»: esa frase es la agenda de control hablando. Se nombra, no se "
  "responde.",
  "Suelta la pala y se queda callado un rato largo: dejarlo. Ese silencio es el trabajo.",
  "Aparece desesperanza con contenido de muerte: se detiene la hoja y se pasa a la Tarjeta de "
  "crisis. Esto no se sigue empujando."]),
],

# -------------------------------------------------------- hojas en el arroyo
"met-hojas-en-el-arroyo.html": [
 ("Antes de proponerlo", [
  "Pide desesperanza creativa ya hecha. Sin eso se escucha como una técnica más para sacarse cosas "
  "de encima, y se usa así.",
  "No se anuncia como relajación y no se promete calma. Anunciada como calma, la persona la evalúa "
  "por si se calmó, y en ese momento el ejercicio ya se perdió.",
  "Se eligen juntos tres o cuatro pensamientos de los de todos los días. Los peores no: con esos "
  "la práctica se vuelve exposición sin preparar."]),

 ("Cómo se presenta", [
  "«Vamos a hacer algo que suena raro, y te aviso desde ya: no es para que te sientas mejor. Puede "
  "que termines igual de incómodo que ahora, y estaría bien.»",
  "«Tu mente va a seguir produciendo todo el rato. No vamos a apagarla ni a discutirle. Vamos a "
  "practicar mirar los pensamientos, en vez de mirar desde ellos.»",
  "«En la pantalla baja un arroyo. Cada hoja trae uno de los que escogimos. Léelo, y déjalo pasar. "
  "No lo empujes, no lo retengas, y tampoco mires el agua para no verlo: se trata de mirarlo de "
  "frente y dejarlo ir igual.»",
  "Todo el encargo cabe en tres verbos, y conviene dejarlos dichos así: leer, soltar, volver a "
  "mirar."]),

 ("Nombrar el enganche antes de que ocurra", [
  "«En algún momento vas a notar que llevas un rato sin leer ninguna hoja, o que le estabas "
  "contestando a una. Eso va a pasar, y no es un error: esa parte es justamente la que estamos "
  "entrenando.»",
  "«Cuando lo notes, vuelve a mirar el arroyo. Si el botón naranja está puesto, márcalo: marcarlo "
  "es parte de volver.»",
  "Decirlo antes evita que lo viva como fracaso cuando ocurra, y le deja un nombre para poder "
  "contarlo después."]),

 ("Durante: callarse", [
  "El guion ya está en la pantalla. No hace falta acompañar con voz, ni narrar, ni repetir la "
  "instrucción a mitad de camino.",
  "Si habla, no se responde el contenido: «eso también va en una hoja».",
  "Si se ríe o dice que esto es raro: «ponlo en una hoja».",
  "Si pide parar antes de tiempo, se para. El tiempo no se negocia.",
  "Mirar cuándo marca, no cuántas veces. Tres marcas seguidas después de un minuto limpio dicen "
  "algo que el total no dice."]),

 ("Al terminar: el orden importa", [
  "«¿Cómo te fue?» Abierta, sin dirección, y después callarse. El silencio lo llena la persona.",
  "«¿En qué momento dejaste de ver el arroyo?» y «¿qué te hizo darte cuenta de que te habías "
  "ido?» El proceso, no el resultado.",
  "«¿Hubo alguna que no pudiste dejar ir? ¿Qué hiciste con esa?» Ahí está el material.",
  "«¿Notaste algo distinto en cómo pesan?» Solo al final, y solo si la persona lo trae. Nunca de "
  "primera."]),

 ("Lo que no se dice", [
  "✗ «¿Verdad que te sientes más tranquilo?» Pide en voz alta la respuesta que arruina el "
  "ejercicio.",
  "✗ «Muy bien, casi no te enganchaste.» Convierte en puntaje lo que era práctica, y la próxima "
  "vez marcará menos para quedar bien.",
  "✗ «Trata de que no te afecten.» Es la agenda de control otra vez, con otro nombre.",
  "✗ «Si te distraes, vuelve a concentrarte.» Esto no es concentración, y llamarlo así cambia lo "
  "que la persona practica.",
  "✗ Explicar la metáfora después de haberla hecho. Ya la vivió; explicarla la devuelve a idea."]),

 ("Qué hacer con lo que salga", [
  "Se enganchó muchas veces: es una buena sesión, y conviene decirlo con esas palabras. La dosis "
  "del ejercicio es el número de retornos, no el de aciertos.",
  "No se enganchó ninguna: casi nunca significa que no se fue. Repetir más corto, o pasar a La "
  "palabra repetida, que no depende de notar.",
  "«Se detuvo el arroyo», «se quedó atascada una hoja»: señal clásica de fusión. Se marca y se "
  "vuelve, sin interpretarla en el momento.",
  "«Quedé tranquilo, me sirvió»: preguntar «¿lo hiciste para que se fueran?». Si la respuesta es "
  "que sí, el ejercicio se volvió control y toca volver a El costo de la lucha.",
  "Quiso acelerar las hojas, empujarlas o saltarse alguna: es la agenda de control apareciendo "
  "dentro del ejercicio. Es de lo mejor que puede pasar, y se nombra.",
  "Se activó, se disoció o no pudo sostener la pantalla: se para, se ancla y se pasa a la Tarjeta "
  "de crisis. La práctica contemplativa no es el lugar."]),
],

# ============================================================================
# Guiones de entrevista. Aquí la técnica es la secuencia de preguntas, así que
# el guion es el orden y los puntos donde la conversación descarrila.
# ============================================================================

"tcc-flecha-descendente.html": [
 ("Por dónde se entra", [
  "Por un pensamiento concreto de una situación concreta. «No sirvo» no sirve de punto de partida; "
  "«pensé que se iban a dar cuenta en la reunión» sí.",
  "«Supongamos, solo para mirar, que eso fuera cierto. ¿Qué significaría para ti?»"]),

 ("La secuencia", [
  "Se repite la misma pregunta con las mismas palabras, cuatro o cinco veces: «¿y qué tendría eso "
  "de malo?», «¿y qué significaría eso sobre ti?»",
  "No reformular para que suene mejor. La repetición monótona es lo que hace bajar; variarla "
  "devuelve a la persona a la superficie.",
  "Se para cuando la respuesta empieza a repetirse, o cuando aparece una frase corta, absoluta y "
  "en primera persona: «soy un fraude», «no valgo». Ahí está el fondo y no se baja más."]),

 ("Dónde descarrila", [
  "Consolar a mitad del descenso corta la cadena y hay que volver a empezar.",
  "Discutir la creencia en el momento en que aparece. Ese no es el momento: apenas es el hallazgo.",
  "Bajar deprisa con alguien muy activado. Si la activación sube mucho, se para y se ancla."]),

 ("Lo que no se dice", [
  "✗ «Pero eso no es verdad.» Justo cuando llega al fondo, invalida lo que acaba de costarle.",
  "✗ «¿Ves cómo exageras?»",
  "✗ Terminar la sesión en el fondo. Siempre se sube antes de cerrar."]),

 ("Cómo se cierra", [
  "Nombrar que lo que apareció es una creencia y no un hecho, y dejarla anotada para trabajarla.",
  "«Si eso fuera solo una frase que tu mente dice, ¿qué harías distinto esta semana?»"]),
],

"dbt-analisis-en-cadena.html": [
 ("Antes de empezar", [
  "Sobre una conducta problema concreta y reciente, no sobre «las veces que me pasa». Una sola, "
  "con día y hora."]),

 ("Cómo se abre", [
  "«Vamos a reconstruir eso como una película, cuadro por cuadro. No para juzgarlo: para ver dónde "
  "había puertas.»"]),

 ("La secuencia", [
  "Vulnerabilidad previa, evento desencadenante, y después eslabón por eslabón sin saltar.",
  "Cada vez que resuma —«y ahí exploté»— devolver: «¿y justo antes de eso?» Los saltos grandes son "
  "donde estaban las puertas.",
  "Describir, no explicar. El análisis en cadena no busca el porqué, busca el qué pasó después."]),

 ("Lo que no se dice", [
  "✗ «¿Por qué hiciste eso?» Pide justificación y trae vergüenza, y la vergüenza cierra la cadena.",
  "✗ «Ahí te equivocaste.»",
  "✗ Pasar a soluciones antes de tener la cadena completa."]),

 ("Cómo se cierra", [
  "Elegir dos o tres eslabones, no diez, y solo ahí buscar qué habría cabido.",
  "Si el tiempo se acaba antes: mejor una cadena completa sin soluciones que media cadena con "
  "soluciones."]),
],

"tcc-analisis-funcional.html": [
 ("Cómo se abre", [
  "«Vamos a mirar para qué sirve eso que haces. Sirve para algo, o no lo harías.»",
  "Esa frase evita que se lea como reproche, que es el riesgo de esta hoja."]),

 ("La secuencia", [
  "Antecedente: dónde, con quién y qué pasó justo antes.",
  "Conducta: en verbos observables. «Me pongo ansioso» no es una conducta; «me fui del salón» sí.",
  "Consecuencia inmediata y consecuencia a la larga, en columnas separadas. La distancia entre las "
  "dos es todo el análisis."]),

 ("Dónde descarrila", [
  "Describir la conducta como rasgo en vez de como acto. Si no se puede filmar, no es la conducta.",
  "Quedarse en la consecuencia a largo plazo, que la persona ya conoce. La que mantiene el "
  "problema es la inmediata, y es la que cuesta admitir."]),

 ("Lo que no se dice", [
  "✗ «Eso es una conducta de evitación.» Etiquetar antes de que se vea lo deja en teoría.",
  "✗ «Entonces lo haces por llamar la atención.»",
  "✗ Proponer la función. Se deduce de los datos o no se deduce."]),

 ("Cómo se cierra", [
  "Leer en voz alta la columna del alivio inmediato, seguida. Suele bastar."]),
],

"dbt-verificar-los-hechos.html": [
 ("Antes de proponerlo", [
  "Solo tiene sentido cuando la emoción no encaja con los hechos, o cuando la intensidad no "
  "encaja. Si encaja, la habilidad es otra: resolver el problema, no verificar."]),

 ("Cómo se abre", [
  "«No vamos a decidir si tienes razón en sentirlo. Vamos a mirar qué pasó exactamente, y después "
  "qué encaja con qué.»"]),

 ("La secuencia", [
  "Nombrar la emoción. Describir el hecho sin una sola interpretación dentro.",
  "Buscar otras interpretaciones posibles, incluidas las aburridas.",
  "Estimar la probabilidad de la temida, y después preguntar si la intensidad encaja con lo que de "
  "verdad hay."]),

 ("Dónde descarrila", [
  "Usarlo para convencer. Si el profesional queda del lado de los hechos y la persona del lado de "
  "la emoción, ya se perdió y toca validar antes de seguir."]),

 ("Lo que no se dice", [
  "✗ «Estás exagerando.»",
  "✗ «No tienes por qué sentirte así.» Invalida, y la invalidación sube la emoción que se estaba "
  "verificando.",
  "✗ Saltar a la acción opuesta antes de haber verificado."]),

 ("Cómo se cierra", [
  "Si los hechos encajan: se valida y se pasa a resolver el problema.",
  "Si no encajan: ahí sí, acción opuesta, y completa."]),
],

"act-costo-de-la-lucha.html": [
 ("La premisa, dicha en voz alta", [
  "«No vamos a mirar si has hecho lo suficiente. Doy por hecho que sí, y con todo lo que tenías. "
  "Vamos a mirar otra cosa: qué te ha costado.»",
  "Sin esa frase la hoja se lee como reproche, y entonces la persona defiende en vez de mirar."]),

 ("La secuencia", [
  "Cada estrategia por separado, y dos preguntas que no se responden juntas: «¿alivió en el "
  "momento?» y «¿lo resolvió a la larga?»",
  "Si contesta las dos de una: «espera, esa es la segunda. ¿Alivió, en el momento?»"]),

 ("Dónde descarrila", [
  "La persona empieza a defender sus estrategias. Cuando eso pasa es que se sintió juzgada: se "
  "vuelve a la premisa y se dice otra vez."]),

 ("Lo que no se dice", [
  "✗ «¿Ves que nada de eso funciona?» Sí funcionó, para aliviar. Por eso lo siguió haciendo.",
  "✗ «Entonces deja de hacerlo.»",
  "✗ Leer el costo como si fuera una factura que se le pasa."]),

 ("Cómo se cierra", [
  "Con la pregunta, no con la conclusión. La desesperanza creativa que cierra el profesional deja "
  "de ser creativa.",
  "«Si esto que has intentado es lo que hay, ¿qué es lo que no has probado?»"]),
],

# ============================================================================
# Guiones de enseñanza. Aquí lo que se transmite es una habilidad, y el riesgo
# está en el mal uso que se instala si se enseña de más o de menos.
# ============================================================================

"dbt-mente-sabia.html": [
 ("Cómo se enseña", [
  "Con los dos estados primero, y con ejemplos suyos, no con los del manual.",
  "«Cuéntame una decisión que tomaste desde la emoción pura.» Y después: «otra desde pura "
  "razón, sin sentir nada.»"]),

 ("La imagen", [
  "«Mente sabia no es el punto medio entre las dos. Es lo que sabes cuando ya paraste de discutir "
  "contigo.»"]),

 ("El ensayo", [
  "En sesión, con una decisión pequeña y real, no hipotética.",
  "Preguntar dónde lo siente en el cuerpo. Sin eso se queda en concepto."]),

 ("El mal uso habitual", [
  "Usarla para justificar lo que ya se quería hacer.",
  "Si la respuesta llega instantánea y cómoda, casi nunca es mente sabia. Vale la pena decirlo: "
  "«¿eso lo sabías antes de preguntarte?»"]),

 ("Lo que no se dice", [
  "✗ «Usa la mente sabia», como consejo suelto y sin ensayo.",
  "✗ «Cálmate y piensa.» Eso es mente racional, que es justamente uno de los dos extremos.",
  "✗ Presentarla como una voz mística o infalible."]),
],

"dbt-pedir-y-decir-no.html": [
 ("Cómo se enseña", [
  "Con una petición real y pendiente de esta semana. En abstracto no se aprende."]),

 ("La intensidad va antes que el guion", [
  "Decidir primero cuánto pedir, de insinuar a insistir. Muchos fracasos son de intensidad y no de "
  "forma: el guion perfecto en la intensidad equivocada no funciona."]),

 ("El ensayo", [
  "Escribirlo, decirlo en voz alta y repetirlo hasta que suene suyo.",
  "Y ensayar el no: qué dice si le dicen que no. Sin eso, la primera negativa desarma todo."]),

 ("El mal uso habitual", [
  "Aplicarlo palabra por palabra suena a robot y la otra persona lo nota. Se ensaya para tener la "
  "estructura, no el libreto."]),

 ("Lo que no se dice", [
  "✗ «Solo tienes que ser más asertivo.»",
  "✗ Prometer que va a funcionar. La habilidad es pedir bien; conseguir no depende de ella.",
  "✗ Cerrar sin acordar una petición concreta, y pequeña."]),
],

"tcc-autoinstrucciones.html": [
 ("Cómo se enseña: modelando", [
  "El profesional dice primero, en voz alta, lo que se diría a sí mismo en esa situación, dudas "
  "incluidas. Si el modelo sale perfecto no sirve de modelo."]),

 ("El orden es la técnica", [
  "La persona lo dice en voz alta, después en voz baja, después por dentro. Ese desvanecimiento "
  "progresivo es lo que hace que quede disponible cuando toque."]),

 ("Las frases", [
  "En sus palabras, cortas y en primera persona.",
  "Una autoinstrucción dice qué hacer, no cómo sentirse: «leo la primera línea» sirve; «voy a "
  "estar tranquilo» no."]),

 ("El mal uso habitual", [
  "Convertirlas en frases motivacionales. En cuanto suenan a taller, dejan de usarse el día que "
  "hacen falta."]),

 ("Lo que no se dice", [
  "✗ «Repítete que sí puedes.»",
  "✗ «Piensa en positivo.»",
  "✗ Dárselas escritas por el profesional. Las que no salen de su boca no vuelven a su cabeza."]),
],

"tcc-solucion-de-problemas.html": [
 ("Antes de proponerlo", [
  "Distinguir problema de malestar. Si no hay un problema resoluble, esta hoja hace daño: convierte "
  "una emoción en una tarea que se falla."]),

 ("La orientación va primero, y es la mitad", [
  "Si la persona cree que los problemas no se resuelven o que ella no es capaz, ninguna lista de "
  "alternativas va a servir.",
  "«¿Esto es un problema que se pueda resolver, o es algo que toca cargar?» Las dos respuestas "
  "llevan a hojas distintas."]),

 ("La generación", [
  "Cantidad antes que calidad, y sin evaluar mientras se generan. Si evalúa a la vez, se queda en "
  "tres y las tres serán las de siempre.",
  "Incluir a propósito una o dos absurdas. Sueltan el resto."]),

 ("El mal uso habitual", [
  "Elegir la mejor alternativa y no probarla. La técnica termina en ejecución y revisión, no en la "
  "lista."]),

 ("Lo que no se dice", [
  "✗ «Es cuestión de organizarse.»",
  "✗ Proponer las alternativas uno mismo, por rápido que sea."]),
],

"act-soltar-el-anzuelo.html": [
 ("Cómo se enseña", [
  "Con un pensamiento que esté activo hoy, no con el más grave del historial."]),

 ("La distinción que sostiene todo", [
  "No es dejar de tener el pensamiento, es dejar de morderlo.",
  "«¿Qué hace tu vida cuando muerdes ese anzuelo?» Y después: «¿qué haría si estuviera ahí y no lo "
  "mordieras?»"]),

 ("El ensayo", [
  "Probar dos o tres formas de defusión en la sesión y quedarse con la que le funcione a él, no "
  "con la que suene mejor."]),

 ("El mal uso habitual", [
  "Usarlo para que el pensamiento se vaya. Si pregunta «¿y cuánto tarda en irse?», volvió a "
  "morder, y conviene nombrarlo sin corregirlo."]),

 ("Lo que no se dice", [
  "✗ «No le hagas caso.»",
  "✗ «Eso es solo un pensamiento», dicho como consuelo. Es una descripción, no un calmante."]),
],

# ============================================================================
# Guiones de acuerdo. Aquí el riesgo no está en cómo se presenta la hoja, sino
# en pactar algo irreal, ambiguo o impuesto.
# ============================================================================

"tcc-escalera-de-exposicion.html": [
 ("Antes de pactar", [
  "La jerarquía la construye la persona. Un peldaño puesto por el profesional se cumple por "
  "obediencia y no enseña nada.",
  "Se empieza por uno que pueda hacer, no por uno que deba."]),

 ("Cómo se acuerda", [
  "Un solo peldaño, con día, y sin puerta de salida en el enunciado.",
  "Explícito antes de empezar: no se sube hasta que ese baje.",
  "Las conductas de seguridad se nombran una por una. Una exposición con conducta de seguridad "
  "dentro no es una exposición."]),

 ("Lo que no se pacta", [
  "✗ Un peldaño elegido por el profesional porque «ya está listo».",
  "✗ «Aguanta hasta que se te pase», sin criterio de bajada.",
  "✗ Subir dos peldaños porque la semana salió bien."]),

 ("En la siguiente sesión", [
  "Preguntar la unidad de ansiedad al empezar, en el pico y al terminar.",
  "Si no bajó, casi siempre pasó una de dos: salió antes de tiempo, o llevaba una conducta de "
  "seguridad que no se había nombrado."]),
],

"tcc-activacion-conductual.html": [
 ("Antes de pactar", [
  "La actividad se elige por valor, no por agrado. Esperar a tener ganas es el problema, no la "
  "solución, y conviene decirlo con esas palabras.",
  "«La ganas vienen después de empezar, no antes. Vamos a probarlo esta semana.»"]),

 ("Cómo se acuerda", [
  "Pequeña, concreta, con día y hora, y que no dependa de que otra persona responda.",
  "Se hace tenga o no tenga ganas. Y se registra dominio y agrado después de hacerla, nunca antes."]),

 ("Lo que no se pacta", [
  "✗ Una semana entera de actividades de golpe.",
  "✗ Algo que dependa de que alguien más conteste o acepte.",
  "✗ «Sal a distraerte.» Eso no es activación conductual, es evitación con buen nombre."]),

 ("En la siguiente sesión", [
  "Mirar dominio y agrado, no si le gustó.",
  "Varias actividades con dominio alto y agrado bajo es exactamente el patrón esperado al empezar, "
  "y conviene decirlo antes de que lo lea como fracaso."]),
],

"dbt-tarjeta-de-crisis.html": [
 ("Antes de pactar", [
  "Se llena fuera de la crisis y con la persona en calma. Una tarjeta hecha en crisis no se usa en "
  "crisis."]),

 ("Cómo se acuerda", [
  "Pocas cosas y muy concretas. Tres habilidades, no ocho: con ocho no lee ninguna.",
  "Los teléfonos van con nombre y número escritos. «Llamar a alguien» no es un plan.",
  "Todo lo que exija concentración se descarta: a noventa de activación no se sostiene."]),

 ("Lo que no se pacta", [
  "✗ Habilidades que solo funcionan con la cabeza fría.",
  "✗ «Respirar profundo» como única opción.",
  "✗ Dejarla solo en el celular, si el celular es parte de lo que se descontrola."]),

 ("La comprobación que casi siempre se olvida", [
  "«¿Dónde va a estar la tarjeta, físicamente?» Y que lo diga en voz alta.",
  "Una tarjeta que no se sabe dónde está es una tarjeta que no existe."]),
],

"dbt-tarjeta-diaria.html": [
 ("Antes de pactar", [
  "Sirve si se llena. Una tarjeta que no se llena no es un fracaso de la persona: es un diseño "
  "demasiado grande."]),

 ("Cómo se acuerda", [
  "Empezar con menos columnas de las que parecen necesarias. Añadir es fácil; quitar cuesta.",
  "El momento del día se acuerda explícito y se engancha a algo que ya ocurre: después de lavarse "
  "los dientes, antes de acostarse."]),

 ("Lo que no se pacta", [
  "✗ Registrar cinco variables desde la primera semana.",
  "✗ Revisarla solo cuando algo va mal, que la convierte en instrumento de castigo."]),

 ("En la siguiente sesión", [
  "Se revisa siempre, aunque esté vacía, y se revisa primero.",
  "Si se mira al final, o solo algunas semanas, deja de llenarse. Eso es predecible y no es "
  "resistencia."]),
],

}
