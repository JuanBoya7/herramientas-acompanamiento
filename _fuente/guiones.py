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

}
