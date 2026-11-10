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
  "El momento clínico no es sembrar: es tener que dejar dieciocho afuera."]),

 ("Cómo se presenta", [
  "«Un jardín tiene espacio para seis surcos, y aquí hay veinticuatro semillas. Lo que "
  "dejes afuera no es que no importe: es que no cabe.»",
  "«No hay respuesta correcta, y no voy a opinar de lo que siembres.»"]),

 ("Al enraizar", [
  "Las veinticuatro semillas están redactadas como conductas, a propósito: por ahí entra quien no "
  "sabe nombrar valores. El paso de enraizar existe para que la conducta no se quede haciendo de "
  "valor, y es el momento donde más fácil se desvía el ejercicio hacia metas.",
  "«Cuando dices «bajarle al consumo», eso suena a una acción. ¿Qué hay detrás de esa intención, "
  "qué quieres proteger?»",
  "«Entonces, en vez de llamar a este surco «comprar menos», ¿cómo lo llamarías tú? ¿Te representa?» "
  "El rótulo del surco se escribe con sus palabras, no con las de la lista.",
  "«Si esa parte de tu vida estuviera más presente estos meses, ¿qué cambiaría en cómo te tratas?»",
  "«¿Qué versión de ti estás cuidando cuando eliges esta semilla?»",
  "Las fichas de «qué cuida» son un repertorio para destrabar, no un menú que haya que usar. Si la "
  "persona lo dice con otras palabras, va el «+».",
  "Un surco puede quedarse sin raíz y no pasa nada: el contador lo deja a la vista y es material "
  "para la próxima sesión. Lo que no conviene es rellenarlo por completar."]),

 ("Durante", [
  "Cuando dude a quién dejar afuera, no ayudarle a decidir. Esa incomodidad es el ejercicio.",
  "Si dice «es que todos importan»: «claro que sí, y aun así hay seis surcos».",
  "Al regar: «con lo que hiciste esta semana, no con lo que quisieras hacer». Esa frase es la que "
  "separa el jardín de una lista de buenas intenciones.",
  "Al elegir la regadera: «¿cuál quieres regar esta semana porque de verdad te importa, no porque "
  "deberías?»"]),

 ("Al terminar", [
  "«¿Cuál está más marchito?» Esperar.",
  "Y solo después: «¿qué es lo más pequeño que lo regaría?»",
  "El qué día, a qué hora y en qué lugar se acuerda hablando y queda escrito en «tarea "
  "acordada», al pie de la hoja. En la hoja no hay agenda, a propósito."]),

 ("Lo que no se dice", [
  "✗ «Deberías regar más la familia.» El jardín es suyo, incluidas las decisiones que incomodan.",
  "✗ Comparar unos surcos con otros, o con los de otra persona.",
  "✗ Convertir el surco más seco en tarea de la semana antes de saber qué lo secó.",
  "✗ Poner la raíz uno mismo. Si el profesional elige la ficha de «qué cuida», el valor pasó a ser "
  "suyo y el ejercicio se acabó."]),

 ("Qué hacer con lo que salga", [
  "No logra sembrar ni tres: la conversación ya no es de valores, es de aplanamiento. Conviene "
  "tamizar sintomatología depresiva antes de seguir.",
  "Siembra seis y los riega todos al máximo: suele ser deseabilidad. Bajar a la semana concreta, "
  "día por día, y volver a regar.",
  "Aparece un surco que riega mucho y que no eligió como valor: mirarlo. Casi siempre es evitación "
  "bien disfrazada de responsabilidad.",
  "Una misma maleza marcada en varios surcos, o en todos: no es una barrera de esa área, es un "
  "proceso que atraviesa la vida entera. Ahí la conversación deja de ser por surcos y pasa a ser "
  "por el proceso: qué hace con eso cuando aparece, no en cuál jardín aparece."]),
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


"cft-pausa-de-autocompasion.html": [
 ("Antes de empezar", [
  "Primero el gesto, después las palabras. Se prueban dos o tres formas de tocarse con apoyo y se "
  "queda la que sostenga; si ninguna, se sigue sin gesto.",
  "La situación, leve o moderada. Con la más grave del historial se aprende a desbordarse, no a "
  "practicar."]),

 ("Cómo se propone", [
  "«Vamos a probar algo breve para los momentos difíciles. No es para que el malestar se vaya, sino "
  "para tratarte como tratarías a alguien que quieres cuando está mal.»",
  "Se dice despacio, con pausas entre las frases. El guía no agrega explicaciones mientras la persona "
  "practica."]),

 ("Después", [
  "«¿Qué notaste?» Y luego, por partes: «¿pasó algo al decir la primera frase?», «¿y con la de que a "
  "cualquiera le pasa?», «¿necesitabas consuelo o fuerza?».",
  "Si dice que se sintió peor, se valida sin alarma: el dolor no lo creó la práctica, estaba antes."]),

 ("Lo que no se dice", [
  "✗ «Tienes que quererte más.»",
  "✗ «Hay gente que está peor que tú.» Es lo contrario de la humanidad compartida.",
  "✗ «Respira y ya se te pasa.»"]),
],

"cft-el-yo-compasivo.html": [
 ("Cómo se presenta", [
  "Como un papel de actor. «No se trata de si ya eres así. Los actores hacen personajes muy distintos "
  "de ellos: imaginan cómo se sentirían, qué pensarían, qué harían. Vamos a hacer lo mismo.»",
  "Si aparece «eso no soy yo», no se discute: es justo lo que el papel permite dejar de lado."]),

 ("Mientras se conduce", [
  "Pausas largas entre cualidades. Quien acompaña no llena el silencio.",
  "Al traer la situación: «¿Tiene sentido que se sienta así?» y «No es su culpa, ¿verdad?», con "
  "tiempo para que responda."]),

 ("Después", [
  "«¿Cómo fue imaginarte así?» Si solo pudo imaginarlo, se valida: al principio es lo esperable.",
  "Se practica fuera en momentos favorables, no en plena crisis."]),

 ("Lo que no se dice", [
  "✗ «Tienes que ser más compasivo contigo.»",
  "✗ «Deja de pensar en eso y piensa en algo bonito.» No es una distracción: se vuelve a la situación."]),
],

# --------------------------------------------------------------- la matriz
# Paso 1 de Polk, Schoendorff, Webster y Olaz (2016): montar el punto de vista.
"act-matriz.html": [
 ("Antes de proponerlo", [
  "Primero, lo que trae a la persona. Se le devuelve lo escuchado hasta que diga «sí, es eso»; "
  "sin ese paso, la matriz llega como una técnica más y no como su propia experiencia ordenada.",
  "Se pide permiso para mostrar un punto de vista. La hoja no se abre antes de ese sí."]),

 ("Cómo se presenta", [
  "«Es solo un punto de vista. No digo que sea el único ni el correcto: a mucha gente le ha "
  "servido para hacer lo que le importa aunque aparezcan obstáculos.»",
  "La línea horizontal antes que los cuadrantes: «A un conejo se le puede ver yendo hacia una "
  "zanahoria o alejándose de un perro que ladra. A nosotros también, y además hacia personas y "
  "cosas que importan y lejos de cosas que aparecen por dentro, que nadie ve.»",
  "Se empieza abajo a la derecha, y por quién antes que por qué: «¿Quién te importa?» Casi todos "
  "nombran a alguien, y la primera mirada tiene que ser un acierto."]),

 ("Durante", [
  "Ritmo liviano. Una persona y un par de cosas por cuadrante bastan: «buena muestra; no buscamos "
  "que esté completo».",
  "Abajo a la izquierda se abre normalizando: «¿Haces todo el tiempo lo que te acerca a quien te "
  "importa?» Ante el no: «entonces algo se interpone». Los obstáculos de afuera se reconocen y se "
  "dejan para después.",
  "Terminado abajo, y antes de subir, señalando los dos cuadrantes: «¿Quién puede notar quién te "
  "importa y lo que aparece?» Se espera el «yo». El paso 2 de la hoja lo retoma al final.",
  "Al subir se avisa el cambio: «abajo estaba lo que nadie ve; arriba, lo que cualquiera podría "
  "verte hacer».",
  "Si dice «me autosaboteo» o «evito», se pregunta una sola vez: «¿y qué se te ve haciendo cuando "
  "evitas?». Si no sale una conducta, se anota lo que dijo, con sus palabras, y se sigue.",
  "Ordena la persona. Si algo queda donde no parece ir —«no sentir ansiedad» como lo que importa, "
  "el jefe como lo que se interpone—, se deja así: el orden se afina con la práctica.",
  "Se señalan los cuadrantes en la pantalla, y que la persona también señale. Se apunta a su "
  "experiencia; el diagrama no se explica."]),

 ("Al terminar", [
  "«Si pudieras elegir entre una vida que va sobre todo por este lado (izquierda) y una que va "
  "sobre todo por este otro (derecha), ¿cuál elegirías?»",
  "«¿Te interesa aprender a elegir con más facilidad esto (arriba a la derecha) aunque aparezca "
  "aquello (abajo a la izquierda)?» Ese sí es el acuerdo de trabajo.",
  "La práctica de la semana es de notar, no de hacer. Si no la hace, que note que no la hizo: "
  "eso también es notar, y en la sesión siguiente cuenta como logro."]),

 ("Lo que no se dice", [
  "✗ «Valores», «aceptación», «defusión». Se habla de quién y qué importa, de lo que aparece y de "
  "lo que se ve hacer.",
  "✗ «Eso va en el otro cuadrante.» Corregir el orden le enseña a ordenar para quien acompaña, no "
  "a mirar su experiencia.",
  "✗ «Lo de la izquierda está mal.» Alejarse no es un error: es lo que se hace, y en el paso "
  "siguiente se mira si funciona.",
  "✗ Empezar por el problema. Si la primera pregunta va a la izquierda, la sesión se va al relato "
  "de lo que no funciona y cuesta volver a la derecha."]),

 ("Qué hacer con lo que salga", [
  "Dice que nadie le importa: «Entre una vida en la que alguien o algo importa y una en la que nada "
  "importa, ¿cuál elegirías?» Se anota «alguien o algo que importe» y encontrarlo pasa a ser parte "
  "del trabajo.",
  "No se nombra a sí misma entre quienes importan: se le hace notar después de abajo a la "
  "izquierda, con suavidad. Si sale una historia, no se discute; se pide permiso para anotar «yo».",
  "Lo mismo aparece en los dos lados de arriba —dormir, el ejercicio, el teléfono—: «¿quién puede "
  "saber si esta vez fue para acercarte o para alejarte?».",
  "Pregunta «¿y cómo hago eso?»: es una habilidad, y ya empezó a practicarla al elegir la derecha "
  "con todo lo de abajo a la izquierda presente. No se dan soluciones hechas; la matriz sirve para "
  "encontrar las suyas.",
  "Se va a un relato largo: se valida, y se invita a ubicarlo: «eso que acabas de decir, ¿dónde "
  "iría en la matriz?»."]),
],

"act-los-ganchos.html": [
 ("Cómo se presenta", [
  "Con preguntas, no con la explicación: «¿Cómo sabe un pez que mordió un anzuelo?» Hasta llegar a "
  "«porque lo arrastran en otra dirección».",
  "«¿Necesitaría entender el anzuelo, analizarlo o saber quién sostiene la caña?» Se deja que "
  "responda que no."]),

 ("Mientras el pez nada", [
  "En cada gancho, la persona decide en voz alta. Si muerde, no se corrige: se mira adónde lo "
  "llevó y se vuelve a soltar el pez.",
  "«¿Qué haces tú cuando aparece este?»"]),

 ("Lo que no se dice", [
  "✗ «Eso es solo un pensamiento, no es real.»",
  "✗ «Tienes que evitar esos ganchos.» Los ganchos siguen en el agua; se aprende a notarlos."]),
],

"act-el-cielo-y-el-clima.html": [
 ("Cómo se presenta", [
  "«Por malo que sea el clima, el cielo tiene espacio para él. Y el clima nunca le hace daño al "
  "cielo. Tarde o temprano cambia.»",
  "Primero se nombra y se le da forma. Cuanto más concreto el objeto, más fácil dejarle espacio."]),

 ("Mientras dura", [
  "Poca voz. Si la persona abre los ojos para ver si el objeto encogió, se nombra con suavidad: "
  "«no hace falta que cambie».",
  "En la pantalla el clima cambia solo, a veces crece: está bien. Lo que crece de verdad es el cielo."]),

 ("Lo que no se dice", [
  "✗ «Respira hasta que se te pase.»",
  "✗ «¿Ya se fue?» Esa pregunta convierte la práctica en otra forma de lucha."]),
],

"act-empujar-el-papel.html": [
 ("Con papel de verdad", [
  "Si se puede, primero con hojas reales: se escribe el «papá» en una, la persona trabaja en otra, y "
  "de pronto se le pone el papel frente a la cara. Cuando empuja, se ofrece resistencia con el brazo.",
  "«¿Qué pasó con el informe? ¿Cuánta fuerza pusiste? ¿Qué conseguiste empujando?»"]),

 ("Las preguntas que sostienen el ejercicio", [
  "«¿Se pone el papel más fuerte o más débil cuando empujas?»",
  "«¿Te sientes así al final del día: cansado, con los hombros tensos?»",
  "«Si empujando solo le das más fuerza, ¿qué se te ocurre que podrías hacer?» Se moldea la respuesta "
  "hasta que aparezca dejar de empujar."]),

 ("Después", [
  "Los binoculares: dentro de un año y dentro de cinco, empujando y sin empujar. «¿Quién estaría "
  "mandando en tu vida?»"]),

 ("Lo que no se dice", [
  "✗ «Ese pensamiento no es cierto.» No se discute el contenido.",
  "✗ «Ignóralo.» Dejarlo al lado no es ignorarlo: se mira y se elige dónde ponerlo."]),
],

"act-quien-lleva-los-globos.html": [
 ("Antes de proponerlo", [
  "Pide algo que importe ya nombrado. La tercera parte del ejercicio es elegir hacia dónde, y sin "
  "dirección queda en mirar globos.",
  "Va mejor después de haber practicado observar. Esta hoja le suma dos cosas a esa práctica: quién "
  "está mirando, y quién manda.",
  "No se anuncia como alivio. Los globos se quedan, y eso se dice desde el comienzo."]),

 ("Cómo se presenta", [
  "«Vamos a hacer lo mismo varias veces: primero con cosas que no pesan, después con las que sí.»",
  "«No se trata de que se vayan. Aquí los globos no se sueltan: se llevan en la mano.»"]),

 ("La parte neutra", [
  "«Nota tu respiración… ¿Quién la está notando?»",
  "«Deja que llegue un pensamiento, el que sea. Ponlo en el globo y míralo como mirarías un cuadro. "
  "¿Te das cuenta de que eres tú quien lo está mirando?»",
  "Se hace entera las primeras veces. Es donde se aprende el movimiento, y con lo difícil ya no hay "
  "que explicarlo."]),

 ("Con lo difícil", [
  "«Tú estás aquí y eso está allá, enfrente. No hay que hacer nada con él.»",
  "«¿Quién está mirando ese pensamiento?» Se espera la respuesta. El botón dice «Soy yo» y lo aprieta "
  "la persona.",
  "«Imagina que tienes sitio para este y para todos los que has tenido hoy. Como los lunares: uno "
  "camina a donde quiere con ellos puestos.»",
  "«Imagínate cuando eso manda en lo que haces. ¿Qué haces?… Ahora imagínate mandando tú, con eso "
  "en la mano.»",
  "«¿Quién quieres que mande en lo que haces ahora: tú o lo que sientes?»"]),

 ("Durante", [
  "Los pasos los marca la persona, a su ritmo. No se aprieta por ella ni se le adelanta la respuesta.",
  "Si elige que mande el globo, no se corrige ni se repite el ensayo. La hoja muestra un momento "
  "cómo queda, y viene el siguiente.",
  "Callarse en la elección. Los segundos con los dos botones a la vista son el ejercicio."]),

 ("Al terminar", [
  "Mirar el ramo antes de hablar: todo eso estuvo ahí, y la figura caminó o no caminó.",
  "La pregunta de la hoja lleva a un paso fuera de la sesión. El cuándo se acuerda hablando."]),

 ("Lo que no se dice", [
  "✗ «Suéltalo.» En esta hoja no se suelta nada: se lleva.",
  "✗ «Tú no eres tus pensamientos.» Son suyos, y es más que cualquiera de ellos. Dicho como eslogan "
  "borra la mitad.",
  "✗ «Muy bien, mandaste tú.» Convierte la elección en desempeño, y la próxima vez elegirá para "
  "quedar bien.",
  "✗ «¿Verdad que pesa menos?» Pide en voz alta que el globo cambie."]),

 ("Qué hacer con lo que salga", [
  "Mandó en todas, muy rápido: preguntar qué hizo con el globo. Si la respuesta es «no le hice caso», "
  "lo empujó, y eso es otra cosa.",
  "Mandó el globo varias veces: es su patrón dibujado, no un fallo. «¿Se parece a algo de esta "
  "semana?»",
  "Dice «pero es que es verdad»: no se discute. «Puede ser verdad. ¿Quién lo está mirando?»",
  "Se queda en «no sé quién mira» o se angustia con la pregunta: no se insiste. Se vuelve a la "
  "respiración y a lo que hay alrededor."]),
],

"tcc-aplazar-la-preocupacion.html": [
 ("Antes de proponerlo", [
  "Primero la pregunta que abre la duda: «Si la preocupación es incontrolable, ¿cómo es que se "
  "detiene cuando suena el teléfono? ¿Y cuando duermes?»",
  "Distinguir con cuidado: no se controla el pensamiento que llega; se elige no seguir el proceso de "
  "preocupación que viene después."]),

 ("Cómo se presenta", [
  "«No te pido que no tengas el pensamiento. Puede estar ahí. Solo dite: es un desencadenante, lo "
  "dejo en paz y me ocupo más tarde.»",
  "«Es un experimento para comprobar hasta qué punto la preocupación es incontrolable.»"]),

 ("En la sesión siguiente", [
  "No basta un «sí, lo hice». Se pregunta con qué desencadenantes, cuántas veces, y qué hizo "
  "exactamente con el pensamiento."]),

 ("Lo que no se dice", [
  "✗ «Trata de no pensar en eso.» Es supresión, lo contrario de lo que se busca.",
  "✗ «Tienes que usar el rato de preocupación.» No es obligatorio."]),
],

"crisis-importancia-y-confianza.html": [
 ("Cómo se pregunta", [
  "«En una escala del 0 al 10, ¿qué tan importante es para ti…?» Y después: «¿Por qué un 6 y no un 0?»",
  "La respuesta es lenguaje de cambio. Se refleja y se afirma, sin agregar razones propias."]),

 ("Hacia arriba", [
  "«¿Qué haría falta para pasar de un 6 a un 8?» También evoca: lo que la persona necesita para avanzar."]),

 ("Lo que no se dice", [
  "✗ «¿Por qué no un 10?» Invita a defender el no cambio.",
  "✗ «Pero debería ser más importante para ti.»",
  "✗ Elogios generales como «¡qué bien!». Se afirma lo concreto: «Has sido muy constante con esto»."]),
],

"tcc-balance-decisional.html": [
 ("Cómo se llena", [
  "Las cuatro celdas, sin saltarse ninguna. Si queda en blanco lo bueno de seguir igual: «¿Qué te "
  "impidió cambiar esto antes?»",
  "Se valida: «Cambiar la propia conducta es un trabajo muy duro, sobre todo algo practicado por años.»"]),

 ("Cómo se responde", [
  "Se usa lo que la persona dijo. Si seguir igual es «más fácil»: «¿Cuánto trabajo te supone hoy "
  "manejar esto?» Muchas veces descubre que seguir igual también cuesta.",
  "Se refleja selectivamente lo que apoya el cambio, sin descartar lo otro."]),

 ("Lo que no se dice", [
  "✗ «Es obvio que te conviene cambiar.»",
  "✗ Llenar las celdas por la persona. Sus razones valen porque son suyas."]),
],

"tcc-ventana-de-sueno.html": [
 ("Cómo se presenta", [
  "Tiene algo paradójico y conviene decirlo: a quien duerme poco se le pide pasar menos tiempo en la "
  "cama. «Quedarse más en la cama da más oportunidad de dormir, pero el sueño sale superficial y cortado.»",
  "Se anticipa que al principio dormirá algo menos, y que más adelante costará mantenerse despierto "
  "hasta la hora."]),

 ("Cada semana", [
  "Lo primero de la sesión es el diario: la persona lee los números, se calcula la eficiencia y se "
  "ajusta la ventana. Si no se revisa primero, deja de llenarse."]),

 ("Lo que no se dice", [
  "✗ «Si una noche duermes mal, quédate más en la cama al otro día.»",
  "✗ «Levántate cuando te despiertes, a la hora que sea.» La hora de levantarse es fija."]),
],

"tcc-lista-abc.html": [
 ("Cómo se arma", [
  "Primero volcar todo, sin calificar. Después las letras, de a una tarea, discutiendo cada A: "
  "«¿Tiene que estar hecha hoy o mañana?»",
  "Se juega el día en los dos órdenes con sus propias tareas. La diferencia la ve la persona."]),

 ("En la sesión siguiente", [
  "«¿Cuándo miraste la lista?» antes que «¿qué hiciste?». Si no se miró, se revisa el momento del día "
  "al que se ató, no la fuerza de voluntad.",
  "Si una A se quedó sin hacer, se vuelve a calificar al día siguiente. No es un fracaso: es "
  "información sobre cuánto cabe en un día."]),

 ("Lo que no se dice", [
  "✗ «Tienes que ser más organizado.»",
  "✗ «Cuando encuentres la aplicación ideal, empezamos.»"]),
],

"pp-tres-cosas-buenas.html": [
 ("Cómo se presenta el diario", [
  "«La mente recuerda con más facilidad lo que salió mal que lo que salió bien. Quejarse es fácil; "
  "apreciar lo bueno requiere atención y esfuerzo.»",
  "Tres cosas cada noche, cada una con una frase sobre por qué pasó. Lo que importa es la frase."]),

 ("La visualización", [
  "Se lee despacio, con tiempo en cada pregunta. Si la persona no logra ideas concretas, una imagen "
  "clara de la mejor versión también sirve para orientar el camino.",
  "Después se escribe sin pensarlo mucho, tal como se visualizó."]),

 ("En la sesión siguiente", [
  "Se empieza por el diario. Si no se llenó, se reconstruye ahí mismo mirando la semana."]),

 ("Lo que no se dice", [
  "✗ «Hay gente que está peor; agradece lo que tienes.»",
  "✗ «Tienes que ser más positivo.»"]),
],

"tcc-inoculacion-de-estres.html": [
 ("Cómo se presenta", [
  "Como una vacuna: «Se trata de exponerte a dosis que activen tus defensas sin vencerlas. Con cada "
  "una que manejas, la siguiente se vuelve posible.»",
  "El objetivo no es quitar el estrés por completo, sino usarlo: verlo como un reto o un problema "
  "por resolver."]),

 ("Al ensayar en la imaginación", [
  "La escena incluye estresarse: la tensión que sube, el pensamiento catastrófico, y luego cómo lo "
  "nota y lo afronta. Una escena donde todo sale bien enseña menos."]),

 ("Después de cada tarea", [
  "Preguntar como Colombo: «¿Cómo lo lograste? ¿Qué hiciste exactamente?» Que el mérito lo ponga la persona.",
  "Si reporta un fracaso, revisar su criterio de éxito: a veces un éxito parcial se lee como fracaso total."]),

 ("Lo que no se dice", [
  "✗ «La próxima vez no te vas a estresar.»",
  "✗ Proponer diez técnicas a la vez."]),
],

# ============================================================================
# Guiones de las 28 herramientas nuevas (Lotes 1, 2 y 3)
# ============================================================================

'act-echar-el-ancla.html': [('Antes de proponerlo',
  ['Se usa cuando la marejada ya está aquí, o para ensayar en frío qué hacer cuando llegue. No '
   'hace falta esperar a que la persona entienda la teoría: se guía en vivo con voz pausada.',
   'Aclarar desde el arranque para qué sirve un ancla. Si no se dice con todas las letras, la '
   'persona la usará para intentar calmarse y sentirá que fracasó si la ansiedad sigue.']),
 ('Cómo se presenta',
  ['«Cuando llega una tormenta en alta mar, los barcos echan el ancla. ¿Para qué la echan? No es '
   'para que pare la tormenta: las anclas no controlan el clima. La echan para sujetarse al fondo '
   'y que las olas no los estrellen contra las rocas mientras pasa el temporal.»',
   '«Vamos a hacer tres movimientos muy simples —reconocer lo que hay adentro, conectar con el '
   'cuerpo y abrir la atención a este lugar— y los vamos a repetir un par de veces como quien '
   'suelta cadena hasta tocar fondo.»']),
 ('Durante (el ciclo A → C → E)',
  ['En la A (Reconocer): «Nota con suavidad qué está pasando ahora mismo por dentro: qué '
   'pensamiento, qué emoción o qué sensación hay en el pecho o en el estómago. No intentes '
   'cambiarlo ni empujarlo; solo reconócelo, como quien dice: aquí hay tormenta.»',
   'En la C (Conectar con el cuerpo): «Y mientras eso sigue ahí adentro, lleva el mando a tu '
   'cuerpo. Empuja despacio los pies contra el suelo… siente la firmeza del piso… endereza un poco '
   'la espalda… estira los dedos o suelta los hombros. No estás huyendo de la ola: estás notando '
   'que además de la ola tienes cuerpo.»',
   'En la E (Involucrarse): «Y ahora, manteniendo el contacto con tus pies y dejando que lo de '
   'adentro siga donde está, mira alrededor. Nota tres cosas que puedas ver en este cuarto… '
   'escucha dos sonidos… y nota que estamos tú y yo aquí, en esta conversación.»',
   'Hacer clic en bajar un tramo del ancla y repetir dos ciclos más de treinta segundos. El efecto '
   'suele aparecer en la segunda o tercera vuelta.']),
 ('Al terminar',
  ['«Fíjate en el barco de la pantalla: el mar no se apagó, las olas siguen pasando, pero ya no va '
   'a la deriva. ¿Qué notas distinto ahora respecto a hace dos minutos?»']),
 ('Lo que no se dice',
  ['✗ «Respira profundo para que se te pase la ansiedad.» Eso convierte el ancla en otra '
   'estrategia de control y dispara el interruptor de la lucha.',
   '✗ «Concéntrate en la habitación para no pensar en eso.» Echar el ancla es ampliar el foco para '
   'que quepan las dos cosas, no distraerse.']),
 ('Qué hacer con lo que salga',
  ['Dice «sigo igual de angustiado»: «Es esperable, el ancla no apaga la tormenta. La pregunta es '
   'si ahora mismo sientes un poco más de mando sobre tus manos, tus pies y lo que estás haciendo '
   'aquí conmigo.»',
   'Le cuesta cerrar los ojos o mirar hacia adentro: en trauma o pánico se hace siempre con los '
   'ojos abiertos y pasando muy rápido por la A para apoyarse más tiempo en los pies (C) y en el '
   'cuarto (E).'])],

'met-el-interruptor.html': [('Antes de proponerlo',
  ['Conviene cuando la persona no solo sufre por una emoción difícil, sino que además se pelea con '
   'ella: se da rabia tener miedo, se culpa por estar triste o se asusta de estar ansiosa.']),
 ('Cómo se presenta',
  ['«Imagina que en el fondo de la mente tenemos un interruptor como este: el interruptor de la '
   'lucha. En cuanto aparece una emoción incómoda, por costumbre el interruptor salta a ENCENDIDO '
   'y empezamos a pelear contra lo que sentimos.»',
   '«Vamos a poner primero qué emoción llegó hoy por su cuenta, y qué se encendió encima cuando '
   'empezaste a pelear con ella.»']),
 ('Durante',
  ['Dejar correr unos segundos la escena con la lucha encendida: «Mira los anillos rojos y la '
   'barra de energía de abajo. Tienes la emoción original y, encima, tienes la rabia por sentirla, '
   'el miedo a que no se vaya y el agotamiento de pelear.»',
   'Al apagar el interruptor: «Ahora suéltalo y mira con cuidado qué cambia y qué NO cambia en el '
   'dibujo.» Callarse unos segundos para que vea que la onda azul sigue subiendo y bajando.']),
 ('Al terminar',
  ['«La ola de abajo sigue moviéndose porque estás vivo y las cosas te importan. Lo que '
   'desapareció fue la tormenta roja de encima. Si hoy no tuvieras que gastar ese ochenta por '
   'ciento de energía en pelearte con lo que sientes, ¿en qué te gustaría usarlo?»']),
 ('Lo que no se dice',
  ['✗ «Si aceptas la emoción se te va a quitar más rápido.» Eso es volver a encender el '
   'interruptor con un disfraz más sutil.',
   '✗ Dar a entender que el malestar limpio no duele. Duele de verdad; la diferencia es que no '
   'lleva encima la paliza extra de la lucha.']),
 ('Qué hacer con lo que salga',
  ['Dice «pero es que el interruptor se me enciende solo»: «Claro, lleva años en automático. No se '
   'trata de que no se encienda nunca, sino de notar cuando saltó y bajarlo las veces que haga '
   'falta.»'])],

'met-las-manos.html': [('Antes de proponerlo',
  ['Rinde muchísimo más si la persona hace el gesto con sus propias manos mientras mueve el '
   'control de la hoja. Invitarla con naturalidad; si prefiere no hacerlo, la escena en pantalla '
   'sostiene el ejercicio igual.']),
 ('Cómo se presenta',
  ['«Imagina por un momento que tus manos son tus pensamientos. Pon las palmas abiertas frente a '
   'ti, como si fueran las dos páginas de un libro, y fíjate qué frases tendrían escritas hoy.»',
   '«Ahora sube las manos despacio hasta taparte los ojos, casi tocando la cara, y quédate ahí '
   'unos segundos.»']),
 ('Durante',
  ['Con las manos pegadas a la cara (distancia 0 %): «Mirando el mundo así, a un centímetro de '
   'esas palabras, ¿cuánto alcanzas a ver de este cuarto o de mí? ¿Y qué tan fácil sería abrazar a '
   'alguien, cocinar o manejar con las manos ocupadas ahí arriba?»',
   'Al pasar a media distancia y luego al regazo (100 %): «Ahora bájalas muy despacio hasta '
   'apoyarlas en el regazo. Fíjate bien: ¿se borraron las palabras que estaban escritas en tus '
   'palmas?» Esperar la respuesta: siguen ahí.']),
 ('Al terminar',
  ['«No se borró ni una letra; siguen ahí abajo si miras hacia las manos. Pero ahora ves todo el '
   'cuarto y tienes las manos libres. ¿Qué vuelve a entrar en tu vista cuando no esperas a que se '
   'borren las frases para bajar las manos?»']),
 ('Lo que no se dice',
  ['✗ «¿Ves que esos pensamientos son falsos o no tienen importancia?» La defusión no discute si '
   'son verdaderos o falsos: muestra qué pasa cuando los llevamos pegados a los ojos.',
   '✗ «Tira esos pensamientos a la basura.» En la hoja las manos jamás se cortan ni se esconden: '
   'quedan a la vista en el regazo.']),
 ('Qué hacer con lo que salga',
  ['Dice «pero al rato se me vuelven a subir a la cara»: «Es lo más normal del mundo: los brazos '
   'tienen ese hábito. Cada vez que notes que tienes el paisaje tapado, no te pelees con las '
   'manos: solo vuelve a apoyarlas en el regazo.»'])],

'met-el-escenario.html': [('Antes de proponerlo',
  ['Útil cuando la persona siente que un problema o un pensamiento difícil es todo lo que existe '
   'hoy, y también para introducir el yo observador sin lenguaje abstracto.']),
 ('Cómo se presenta',
  ['«Imagina que todo lo que piensas, sientes y vives hoy está ocurriendo sobre las tablas de un '
   'teatro. En este momento hay un actor en el centro gritando a todo pulmón, y el técnico de '
   'luces cerró el reflector únicamente sobre él.»']),
 ('Durante',
  ['Con el reflector cerrado: «Cuando toda la luz cae sobre ese personaje y el resto está a '
   'oscuras, parece gigante y parece que fuera el único en la sala.»',
   'Al encender las luces de todo el escenario: «Mira lo que ocurre cuando subimos la luz general. '
   'No echamos al actor ruidoso de las tablas —sigue ahí en el medio—, pero ahora ves quiénes más '
   'estaban en escena esperando en la penumbra.»',
   'Al pasar a mirar desde la butaca: «Y da un paso más atrás: nota la butaca desde la que estás '
   'viendo todo el espectáculo. Los actores cambian, entran y salen, pero tú eres quien los mira '
   'desde el asiento.»']),
 ('Al terminar',
  ['«Sin tener que sacar a empujones al que grita, ¿a qué rincón del escenario eliges dirigir tu '
   'mirada ahora?»']),
 ('Lo que no se dice',
  ['✗ «Ignora al actor negativo y piensa solo en las cosas lindas.» Eso es apagar un reflector '
   'para cerrar otro, y en cuanto el problema grite más fuerte volverá a ganar.',
   '✗ Explicar con jerga qué es el yo como contexto: la imagen de la butaca ya hizo el trabajo.']),
 ('Qué hacer con lo que salga',
  ['Le cuesta nombrar otros actores en las tablas: empezar por cosas mínimas y presentes («el '
   'hecho de que viniste hoy», «el café de esta mañana», «alguien que te quiere»), sin forzar '
   'grandes alegrías.'])],

'met-las-dos-caras.html': [('Antes de proponerlo',
  ['Es una metáfora delicada y profunda para momentos de pérdida, duelo, ruptura o dolor por '
   'vínculos e ideales heridos. Requiere un ritmo pausado y mucha calidez.']),
 ('Cómo se presenta',
  ['«A veces tratamos el dolor como si fuera un error que no debería estar ahí. Pero míralo como '
   'esta moneda: en una cara está lo que hoy te duele tanto, y en el reverso está lo que amas, lo '
   'que cuidas o el tipo de persona que quieres ser.»',
   '«Donde no importa nada, no duele nada. Solo te dejaría de doler si te dejara de importar.»']),
 ('Durante',
  ['Al girar entre la cara del dolor y la del valor: «Detrás de esta tristeza o de este vacío, '
   '¿qué amor o qué cuidado está hablando? Si este dolor fuera un testigo de lo que para ti es '
   'sagrado, ¿de qué daría fe?»',
   'Al pulsar «Intentar partir o esconder la moneda»: «Imagina que tuviéramos un botón para '
   'arrancarte hoy toda esta tristeza. Para lograrlo tendríamos que arrancarte también el cariño, '
   'la historia compartida y el valor del otro lado. No se puede tirar media moneda.»',
   'Al pulsar «Llevar la moneda completa en la mano»: dejar unos segundos de silencio mirando las '
   'dos caras juntas sobre la palma.']),
 ('Al terminar',
  ['«Si eliges quedarte con la moneda entera —con el dolor que pesa en una cara y el amor que vive '
   'en la otra—, ¿con qué gesto pequeño podrías honrar hoy ese lado valioso?»']),
 ('Lo que no se dice',
  ['✗ «Tienes que agradecer el dolor porque te hace más fuerte.» No se romantiza el daño: el dolor '
   'duele; lo que se honra es el valor del reverso.',
   '✗ Apurar el giro hacia el valor sin haber validado antes el peso real de la cara que duele.']),
 ('Qué hacer con lo que salga',
  ['Dice «preferiría no sentir nada aunque se apague todo»: validarlo sin discutir. Cuando el '
   'dolor es muy agudo, anestesiarse tienta de verdad; señalar con suavidad en la moneda qué ha '
   'pasado en su vida las semanas en que intentó apagar la moneda entera.'])],

'dbt-aceptacion-radical.html': [('Antes de proponerlo',
  ['Asegurarse primero de que el hecho realmente no se puede cambiar hoy. Si el problema todavía '
   'tiene arreglo práctico, toca Solución de problemas, no aceptación radical.',
   'Validar a fondo el dolor antes de hablar de aceptar. Si se propone aceptar demasiado rápido, '
   'suena a «supéralo ya».']),
 ('Cómo se presenta',
  ['«Hay cosas que duelen y que hoy ya son un hecho. Pelear con ellas diciendo que no deberían '
   'haber pasado es muy humano, pero fíjate qué nos cobra: al dolor que ya estaba le suma la '
   'amargura de la pelea.»',
   '«Aceptar aquí no significa decir que estuvo bien, ni darle la razón a nadie, ni rendirse. '
   'Significa dejar de pelear con el capítulo que ya ocurrió para tener las manos libres en el '
   'capítulo de hoy.»']),
 ('Durante (el giro en el cuerpo)',
  ['Al mostrar la encrucijada: «Girar la mente no se logra discutiendo con uno mismo; ayuda mucho '
   'más empezar por el cuerpo. Probemos ahora mismo: apoya las manos sobre los muslos con las '
   'palmas abiertas hacia arriba y suelta los dedos.»',
   'En la media sonrisa: «Afloja la mandíbula y la frente, y deja una media sonrisa casi '
   'imperceptible, como quien le avisa al cuerpo que en este segundo no tiene que atacar ni '
   'defenderse.»',
   "Al pulsar girar otra vez: «En cinco minutos la mente va a volver al 'no debería'. Es normal. "
   'No fallaste: solo toca notar que subiste al camino de arriba y volver a girar hacia abajo.»']),
 ('Al terminar',
  ['«Con las palmas abiertas y dejando ese hecho tal como fue, ¿cuál es el paso más pequeño que '
   'hoy sí está en tus manos dar?»']),
 ('Lo que no se dice',
  ['✗ «Tienes que aceptar y pasar la página.» La aceptación radical se hace en pasos de un minuto, '
   'no por decreto.',
   '✗ «Todo pasa por algo.» Eso invalida el dolor real del hecho.']),
 ('Qué hacer con lo que salga',
  ['Dice «si lo acepto siento que digo que no me importó»: señalar el recuadro de la hoja: aceptar '
   'el hecho es el único punto de partida desde el que se puede cuidar de verdad lo que importa.'])],

'rodbt-autoinvestigacion.html': [('Antes de proponerlo',
  ['En RO-DBT no buscamos encontrar la respuesta correcta ni debatir pensamientos: buscamos '
   'practicar la humildad de no saber todavía y sostener una pregunta abierta en el borde '
   'personal.']),
 ('Cómo se presenta',
  ["«A veces nuestra mente se protege cerrándose de dos maneras: o poniéndose fija ('yo tengo "
   "razón y punto') o poniéndose fatalista ('para qué intentarlo, nada sirve'). Las dos nos "
   'ahorran la incomodidad de dudar, pero nos dejan solos.»',
   '«Vamos a hacer algo distinto: primero le damos al cuerpo señal de seguridad y después abrimos '
   'una pregunta sin apurarnos a contestarla.»']),
 ('Durante (Gran Tres + 1 y el borde)',
  ['Guiar primero la postura: «Recuéstate de verdad en el respaldo de la silla… haz una exhalación '
   'larga… sube un milímetro las cejas y deja una sonrisa suave de boca cerrada. Fíjate qué cambia '
   'en el pecho cuando dejas la postura de guardia.»',
   'Al elegir la pregunta de autoinvestigación: «Ahora lee esa pregunta y quédate con ella unos '
   'segundos. Si tu cabeza salta enseguida a justificarse o a explicarlo todo, solo nota cómo '
   'apareció la defensa y vuelve a la pregunta.»']),
 ('Al terminar',
  ['«No la contestes ahora. ¿Cómo sería llevarte esa pregunta abierta esta semana y observar qué '
   'te muestra cuando vuelva a aparecer la tensión?»']),
 ('Lo que no se dice',
  ['✗ Responderle nosotros la pregunta o darle una interpretación cerrada.',
   '✗ Usar la autoinvestigación para que se culpe: el borde se mira con curiosidad y cejas '
   'levantadas, nunca con látigo.']),
 ('Qué hacer con lo que salga',
  ['Intenta convertir la pregunta en una tarea intelectual perfecta: sonreír con calidez y '
   'nombrarlo: «fíjate cómo hasta abrirnos queremos hacerlo con diez en calificación; respira en '
   'el respaldo y déjala sin resolver».'])],

'fap-dentro-y-fuera.html': [('Antes de proponerlo',
  ['Se usa cuando ya hay calidez y confianza suficientes en la relación terapéutica, y cuando '
   'notamos en vivo un gesto de evitación o una oportunidad de cercanía auténtica.']),
 ('Cómo se presenta',
  ['«Me doy cuenta de algo valioso: eso que me cuentas que te pasa afuera con la gente que '
   'quieres, a veces también se asoma un poquito aquí entre nosotros. Y lejos de ser un problema, '
   'nos da un puente seguro para ensayar algo distinto hoy mismo.»']),
 ('Durante (Conciencia, Coraje y Amor)',
  ['Al marcar el paralelo (Paso 1): validar con mucha suavidad por qué aprendió a protegerse así '
   'afuera y aquí.',
   'Al iluminar el puente ACL: «En este momento, ¿qué estás notando que te cuesta decirme o '
   'mostrarme (Conciencia)? ¿Cómo sería animarte a decirlo un diez por ciento más directo aquí '
   'conmigo (Coraje)?»',
   'Cuando la persona da el paso (CCR2): recibirlo en vivo con sintonía genuina, nombrando el '
   'impacto que tiene escucharlo sin disfraces (Amor / refuerzo natural).']),
 ('Al terminar',
  ['«Acabas de cruzar el puente aquí conmigo y no se rompió el vínculo; al contrario, estamos más '
   'cerca. ¿Con quién de tu vida de afuera tendría sentido probar un paso parecido esta semana?»']),
 ('Lo que no se dice',
  ['✗ Señalar la conducta de sesión (CCR1) con tono de crítica o de interpretación fría de '
   'experto.',
   '✗ Pedir un acto de coraje (CCR2) y responderle después con un comentario neutro o cambiando de '
   'tema.']),
 ('Qué hacer con lo que salga',
  ['Le da mucho pudor hablar de lo que pasa en la sesión: no forzar. Nombrar ese pudor con respeto '
   'ya es en sí mismo el primer paso sobre el puente.'])],

'cft-tres-circulos.html': [('Antes de proponerlo',
  ['Ideal para quitar la vergüenza en personas que viven atrapadas entre la ansiedad (rojo) y la '
   'hiperproductividad (azul).']),
 ('Cómo se presenta',
  ['«Nuestro cerebro no fue diseñado para hacernos fáciles las cosas, sino para sobrevivir. Por '
   'eso trae tres sistemas: el rojo para detectar peligros, el azul para correr tras metas y '
   'recursos, y el verde para descansar, digerir y sentirnos seguros con otros.»',
   '«Mueve los tres controles para dibujar cómo han estado repartidos estos tres círculos en tu '
   'vida últimamente.»']),
 ('Durante',
  ['Cuando dibuje un rojo y un azul grandes con un verde diminuto: «Mira ese dibujo: no es que '
   'estés fallando, es que cuando el círculo rojo te asusta, usas el círculo azul de trabajar y '
   'exigirte más para intentar sentirte a salvo. Pero el azul también gasta energía y nunca '
   'enciende la calma.»']),
 ('Al terminar',
  ['«El círculo verde no se llena terminando diez pendientes más en el azul: solo se llena con '
   'gestos de pausa, calidez y ritmo lento. ¿Cuál sería un gesto mínimo para darle de comer al '
   'verde hoy?»']),
 ('Lo que no se dice',
  ['✗ «Tienes que apagar el círculo rojo.» El rojo es necesario; lo que buscamos es que el verde '
   'tenga tamaño para regularlo.']),
 ('Qué hacer con lo que salga',
  ['Dice «si entro al círculo verde siento que pierdo el tiempo o me da culpa»: nombrarlo como el '
   'miedo a la calma y empezar con pausas de apenas treinta segundos.'])],

'cft-voces-y-critico.html': [('Antes de proponerlo',
  ['Sirve cuando tras un error la persona queda tomada por una sola voz punitiva o por un '
   'torbellino confuso de emociones.']),
 ('Cómo se presenta',
  ['«Cuando algo sale mal, parece que adentro hubiera una sola voz gritando, pero en realidad hay '
   'varias partes sentadas a la mesa. Vamos a escuchar primero qué te dijo el crítico, de qué '
   'peligro teme que te pase algo, y cómo quedaron las otras partes.»']),
 ('Durante',
  ['En el paso 2 (función protectora): «Imagina que ese crítico interno es un guardia muy asustado '
   'que aprendió un único método torpe: gritarte a ti primero antes de que el mundo te rechace o '
   'te humille. ¿De qué amenaza está intentando cuidarte?»',
   'En el paso 3 (mesa de las partes): dar un momento a la parte ansiosa, a la triste y a la '
   'enfadada, y luego invitar al Yo compasivo a tomar la cabecera de la mesa.']),
 ('Al terminar',
  ['«Cuando el Yo compasivo se sienta a la cabecera, no echa a nadie a patadas: ve el miedo detrás '
   'del crítico y cuida a la parte herida sin maltrato.»']),
 ('Lo que no se dice',
  ['✗ «Cállate a tu crítico interno.» Pelear con el crítico a gritos es seguir dentro del mismo '
   'sistema de amenaza.']),
 ('Qué hacer con lo que salga',
  ['Teme que sin el crítico no avanzará: contrastar el látigo del crítico con la firmeza cálida de '
   'un buen entrenador que sí quiere que aprendas, pero no te insulta cuando tropiezas.'])],

'par-el-baile-de-pareja.html': [('Antes de proponerlo',
  ['Funciona tanto con la pareja presente como en sesión individual para salir de la lógica de '
   'tribunal (quién tiene la culpa) y pasar a la lógica del ciclo.']),
 ('Cómo se presenta',
  ['«Cuando una pelea importante se repite una y otra vez, deja de ser por los platos o por el '
   'horario: es un baile que se activa solo. Vamos a mirar primero los pasos que se ven por encima '
   'del agua y después qué hay debajo.»']),
 ('Durante',
  ['En la superficie: «Fíjate en el signo de infinito: cuanto más reclama o insiste la posición A '
   'para sentir que importa, más se abruma y se cierra la posición B; y cuanto más se cierra B '
   'para no empeorar todo, más sola se siente A y más fuerte golpea la puerta.»',
   "Al pulsar 'Mirar bajo el agua': bajar el tono de voz: «Debajo del reclamo suele haber miedo a "
   'quedarse solo o no importar; y debajo del silencio suele haber miedo a fallar y no ser nunca '
   'suficiente para el otro.»']),
 ('Al terminar',
  ['«Si el adversario no es tu pareja sino este baile que los deja solos a los dos, ¿qué frase '
   'dicha desde abajo del agua ayudaría a frenar la música apenas empiece a sonar?»']),
 ('Lo que no se dice',
  ['✗ Darle la razón a una de las dos posiciones como si fuera más madura que la otra: tanto '
   'presionar como replegarse mantienen el bucle.']),
 ('Qué hacer con lo que salga',
  ['Dice «pero es que él/ella empezó»: «En un círculo infinito cualquiera de los dos cree siempre '
   'que solo está reaccionando al movimiento anterior del otro. Por eso la única salida es mirar '
   'el baile juntos.»'])],

'par-tener-razon-o-cuidar.html': [('Antes de proponerlo',
  ['Muy útil cuando la pareja ya conoce de memoria su tema recurrente y cada conversación se '
   'convierte en un juicio para cambiar al otro.']),
 ('Cómo se presenta',
  ['«Toda pareja tiene un par de temas de fondo que vuelven cada tanto porque son dos personas '
   "distintas. En terapia de pareja lo llamamos 'el ESO'. Cuando aparece 'el ESO', podemos "
   'ponernos uno frente al otro a dispararnos argumentos, o podemos sentarnos del mismo lado del '
   'banco a mirarlo juntos.»']),
 ('Durante',
  ["Con el modo enfrentados: «Miren qué pasa cuando 'el ESO' queda en el medio como un proyectil: "
   'aunque uno gane el debate lógico, la relación pierde.»',
   "Al pulsar 'Pasar al mismo lado del banco': «Aquí sigue existiendo 'el ESO', nadie finge que "
   'desapareció, pero ahora son ustedes dos hombro con hombro mirando un problema que les cae a '
   'ambos, y hablando desde lo que duele en blando en vez de acusar en duro.»']),
 ('Al terminar',
  ["«La próxima vez que asome su 'ESO' en la semana, ¿cómo podrían avisarse con complicidad para "
   'sentarse del mismo lado del banco antes de empezar el juicio?»']),
 ('Lo que no se dice',
  ['✗ Pedir aceptación como si fuera resignarse a cualquier maltrato: la aceptación de diferencias '
   'va siempre sobre una base de respeto y cuidado mutuo.']),
 ('Qué hacer con lo que salga',
  ['Uno de los dos insiste en que su forma es la objetivamente correcta: preguntar con calma '
   'cuánto le ha servido tener esa razón para sentirse cerca el sábado por la tarde.'])],

'tcc-exposicion-interoceptiva.html': [('Antes de proponerlo',
  ['Verificar siempre que no haya contraindicación médica para el ejercicio elegido.',
   'El profesional lo hace al mismo tiempo que el consultante: respirar juntos por el pitillo o '
   'girar juntos en la silla quita solemnidad y modela que la sensación es segura.']),
 ('Cómo se presenta',
  ['«Cuando aparece una sensación como falta de aire o latidos rápidos, la alarma del cerebro '
   'grita peligro y corremos a controlarla. Hoy vamos a provocar a propósito una versión pequeña '
   'de esa sensación aquí conmigo durante un minuto, y después vamos a hacer lo más importante: no '
   'hacer absolutamente nada para bajarla y ver qué hace el cuerpo solo.»']),
 ('Durante',
  ['En el minuto de inducción: animar con calma a sostener el ejercicio sin distraerse.',
   'Al pasar al minuto de observación: «Ahora suelta el ejercicio, apoya las manos tranquilas y '
   'solo observa la sensación como quien mira bajar la espuma de una ola. No respires hondo a '
   'propósito ni intentes apurarla.»']),
 ('Al terminar',
  ['«Fíjate en la curva: subió porque hicimos el ejercicio, y bajó sola sin que tuvieras que '
   'rescatarte. ¿Qué le enseña esto a tu mente para la próxima vez que aparezca en la calle?»']),
 ('Lo que no se dice',
  ['✗ «Si te asustas mucho paramos enseguida e inhalamos profundo para calmarte.» Cortar en el '
   'pico por miedo refuerza exactamente el temor a la sensación.']),
 ('Qué hacer con lo que salga',
  ['Dice «aquí en el consultorio no me da miedo porque estás tú»: excelente observación; después '
   'de dominarlo juntos, el siguiente paso es practicarlo a solas.'])],

# ============================================================================
# Guiones de las 14 herramientas nuevas ACT (Lote 4)
# ============================================================================

'met-trampa-china.html': [('Antes de proponerlo',
  ['Consultantes agotados de emplear estrategias de control y evitación experiencial que han '
   'estrechado su vida.',
   'Objetivo clínico: Experienciar por qué la lucha directa por eliminar el malestar aprieta más '
   'el problema y cómo inclinarse con suavidad hacia la sensación abre espacio para moverse.']),
 ('1. Presentar el cilindro de bambú y el reflejo de jalar',
  ['Invite a imaginar ambos dedos índices dentro de una trampa china de bambú tejido. Diga: '
   '«Cuando sentimos ansiedad o un recuerdo punzante, lo más lógico parece tirar hacia afuera con '
   'fuerza para zafarnos rápido. Pero miremos qué le hace ese tirón al tejido de bambú».',
   'Pregunta guía: «¿Qué estrategias ha usado últimamente para «tirar hacia afuera» y sacarse esta '
   'sensación de encima?»',
   'Pregunta guía: «Cuando jala con más fuerza, ¿el tubo se afloja o le aprieta más los dedos?»',
   'Mueva el deslizador hacia la derecha para visualizar cómo el intento de escapar reduce el '
   'espacio vital.']),
 ('2. Ensayar el movimiento contraintuitivo: acercarse hacia adentro',
  ['Deslice ahora el control hacia la izquierda. Explique: «La única forma de aflojar las fibras '
   'es hacer lo opuesto a lo que grita el reflejo: empujar los dedos suavemente hacia el centro '
   'del tubo. No para quedarse atrapado, sino para crear holgura y poder moverse».',
   'Pregunta guía: «¿A qué sensación física o emoción podría hoy darle un milímetro de holgura en '
   'lugar de jalar?»',
   'Pregunta guía: «¿Cómo se siente en los hombros y en la respiración dejar de tirar por un '
   'instante?»',
   'Cierre anotando el gesto concreto de apertura que la persona practicará cuando note el tirón '
   'automático.'])],

'met-invitado-incomodo.html': [('Antes de proponerlo',
  ['Evitación social, postergación de proyectos valiosos o espera pasiva a «sentirse seguro» antes '
   'de actuar.',
   'Objetivo clínico: Separar la presencia de emociones o pensamientos desagradables de la '
   'capacidad de seguir participando en una vida guiada por valores.']),
 ('1. Nombrar la fiesta valiosa y al visitante molesto',
  ['Plantee la escena de Joe the Bum (Hayes et al., 1999): «Usted organizó una celebración con las '
   'personas y proyectos que más quiere, y de pronto se cuela un vecino ruidoso y malvestido. Si '
   'usted decide que la fiesta no puede seguir mientras él esté ahí, termina pasando toda la noche '
   'en la puerta empujándolo».',
   'Pregunta guía: «¿Cuál es la fiesta valiosa que usted quiere vivir en esta etapa?»',
   'Pregunta guía: «¿Cómo se llama y qué dice ese invitado incómodo cuando aparece sin '
   'invitación?»',
   'Compare ambos botones de la hoja para ver cómo vigilar la puerta deja al anfitrión fuera de su '
   'propia fiesta.']),
 ('2. Volver a la sala aunque el invitado siga cerca del bufé',
  ['Subraye que abrir la puerta no significa que el visitante nos guste ni aplaudir sus modales: '
   'significa elegir estar con los invitados que sí amamos aunque él siga en un rincón.',
   'Pregunta guía: «Si hoy deja de custodiar el picaporte, ¿a qué conversación o actividad de su '
   'fiesta puede regresar ahora mismo?»',
   'Pregunta guía: «¿Está dispuesto a que el invitado incómodo murmure en un rincón con tal de no '
   'perderse su propia vida?»',
   'Deje registrada la acción concreta de participación que realizará esta semana sin esperar a '
   'que el visitante se marche.'])],

'met-arenas-movedizas.html': [('Antes de proponerlo',
  ['Crisis de pánico, insomnio por hiperalerta, rumiación acelerada o miedo al miedo.',
   'Objetivo clínico: Desactivar las respuestas de urgencia y agitación ante el malestar agudo, '
   'entrenando una postura de contacto amplio y apertura corporal.']),
 ('1. Detectar el pataleo que hunde',
  ['Explique la física de las arenas movedizas: «En tierra firme, correr o empujar hacia abajo nos '
   'saca del peligro. Pero en arenas movedizas, cuando usted levanta un pie desesperado, todo el '
   'peso recae en el otro pie y la succión se duplica».',
   'Pregunta guía: «Cuando empieza a sentir el oleaje de ansiedad o tristeza, ¿cuál es su forma '
   'habitual de patalear?»',
   'Pregunta guía: «¿Ese esfuerzo urgente lo ha sacado a la orilla o lo ha dejado más exhausto y '
   'hundido?»',
   'Use el selector en modo «Luchar y patalear» para nombrar sin juicio los intentos de control '
   'que multiplican la presión.']),
 ('2. Extender el cuerpo y flotar sobre la experiencia',
  ['Cambie a «Extender el cuerpo y flotar»: «Quienes salen de las arenas movedizas hacen algo que '
   'parece absurdo: dejan de patalear, abren los brazos y se tienden de espaldas para tocar más '
   'superficie, no menos».',
   'Pregunta guía: «¿Cómo sería hoy «tenderse de espaldas» con esta sensación durante cinco '
   'minutos, respirando con ella sin exigirle que baje?»',
   'Pregunta guía: «Una vez que su cuerpo flota sin gastar fuerzas en pelear, ¿hacia qué orilla '
   'valiosa quiere deslizarse despacio?»',
   'Practique en vivo treinta segundos de soltar los hombros y abrir espacio físico a la sensación '
   'presente.'])],

'act-pasear-la-mente.html': [('Antes de proponerlo',
  ['Fusión con pensamientos de incapacidad («no voy a poder», «no tiene caso») que paralizan la '
   'iniciativa.',
   'Objetivo clínico: Practicar en vivo la independencia entre el flujo verbal de la mente '
   '(evaluaciones, advertencias, excusas) y la conducta elegida por la persona.']),
 ('1. Separar al hablante incesante de quien camina',
  ['Introduzca el ejercicio de Kelly Wilson: «En el paseo de la vida caminamos junto a nuestra '
   'mente. Ella nunca se calla: opina del clima, advierte peligros, critica y compara. El problema '
   'no es que hable, sino creer que no podemos dar un paso hasta que ella esté de acuerdo».',
   'Pregunta guía: «¿Cuál es el comentario favorito que su mente le repite apenas usted intenta '
   'hacer algo nuevo?»',
   'Pregunta guía: «Si escuchamos esa frase como el parloteo habitual de un acompañante ruidoso, '
   '¿hace falta discutir con ella?»',
   'Use los botones de charla rápida o escriba la frase exacta en el globo de voz de la mente.']),
 ('2. Elegir la calle con los pies mientras la mente opina',
  ['Complete el recuadro de la derecha: «Mientras su mente dice exactamente eso, ¿hacia dónde '
   'deciden caminar sus pies hoy?».',
   'Pregunta guía: «¿Qué le diría a su mente con cortesía («gracias por el dato, mente») antes de '
   'dar el paso?»',
   'Pregunta guía: «¿Qué pequeña acción hará hoy llevando a su mente de paseo aunque ella siga '
   'protestando todo el camino?»',
   'Refuerce que el éxito del ejercicio es caminar con la mente hablando, no lograr que se '
   'calle.'])],

'act-pero-por-y.html': [('Antes de proponerlo',
  ['Cuando el consultante justifica la inacción con fórmulas del tipo «quiero hacerlo, pero siento '
   'miedo / cansancio / duda».',
   'Objetivo clínico: Transformar la conjunción adversativa «pero» (que coloca a las emociones '
   'como barreras incompatibles con la acción) en la conjunción copulativa «y».']),
 ('1. Desmontar la trampa del «pero»',
  ['Explique cómo funciona la palabra «pero» (Hayes et al., 1999): «En nuestro idioma, lo que va '
   "después del 'pero' anula a lo que iba antes. Si digo 'quiero ir a la reunión, pero estoy "
   "nervioso', mi mente escucha que hasta que no se quite el nervio es imposible ir».",
   'Pregunta guía: «¿Cuál es hoy su frase con «pero» más frecuente?»',
   'Pregunta guía: «¿Qué pasa con su libertad de moverse cuando el «pero» pone a la emoción como '
   'guardián de la puerta?»',
   'Escriba ambos lados en la tarjeta y observe el efecto de bloqueo con el interruptor en '
   '«PERO».']),
 ('2. Activar el «Y» e integrar ambas verdades',
  ['Conmute el botón hacia «Y» y lea en voz alta la nueva frase: «Quiero hacer X, Y estoy '
   'sintiendo Y». Ambas cosas son cien por ciento ciertas al mismo tiempo.',
   'Pregunta guía: «Al leer la frase con «Y» en lugar de «pero», ¿qué cambia en su postura '
   'corporal?»',
   'Pregunta guía: «¿Dónde puede aplicar este cambio de una sola palabra hoy mismo cuando su mente '
   'le proponga posponer algo?»',
   'Invite a llevarse la frase con «Y» como recordatorio práctico para los momentos de '
   'indecisión.'])],

'met-cinta-de-sushi.html': [('Antes de proponerlo',
  ['Rumiación, pensamientos intrusivos o tendencia a engancharse a debatir cada idea que cruza por '
   'la mente.',
   'Objetivo clínico: Desliteralizar pensamientos repetitivos o intrusivos observándolos desfilar '
   'como eventos transitorios que no requieren respuesta ni análisis.']),
 ('1. Poner los pensamientos sobre los platillos de la banda',
  ['Presente la imagen del restaurante de sushi con banda transportadora (Harris, 2009): «El chef '
   'de la cocina —su mente— prepara platillos todo el día: recuerdos, comparaciones, escenarios '
   'catastróficos. Que un platillo pase frente a usted no significa que usted lo haya pedido ni '
   'que esté obligado a comérselo».',
   'Pregunta guía: «¿Qué tres platillos ha estado sacando la cocina de su mente con más '
   'insistencia esta semana?»',
   'Pregunta guía: «¿Qué le pasa a su tarde cuando levanta ese platillo de la cinta y se pone a '
   'masticarlo durante horas?»',
   'Agregue los pensamientos de la persona para que los vea desfilar gráficamente por la banda.']),
 ('2. Dejar girar el riel y volver a la mesa',
  ['Destaque que tampoco sirve golpear la banda ni gritarle al chef para que deje de cocinar; '
   'basta con mirar el platillo, notar su etiqueta y dejar que siga su vuelta.',
   'Pregunta guía: «Si hoy deja que ese platillo siga rodando por el riel sin tocarlo, ¿a qué '
   'conversación o actividad de su mesa puede volver?»',
   'Pregunta guía: «¿Cómo puede notar la próxima aparición de ese pensamiento con un simple «ahí '
   'va otra vez el platillo de siempre»?»',
   'Cierre vinculando la observación desapegada con la atención puesta en la tarea presente.'])],

'act-piloto-automatico.html': [('Antes de proponerlo',
  ['Sensación de vivir acelerado, desconectado, en rumiación constante o sin disfrutar las '
   'actividades cotidianas.',
   'Objetivo clínico: Pasar de la desconexión habitual (actuar perdido en preocupaciones) al '
   'contacto directo con la experiencia sensorial presente en rutinas diarias.']),
 ('1. Detectar dónde se enciende el piloto automático',
  ['Normalice que la mente humana viaja al futuro y al pasado mientras el cuerpo hace tareas '
   'conocidas, pero señale el costo: nos perdemos la vida real y alimentamos la rumiación.',
   'Pregunta guía: «¿Qué actividad de todos los días suele hacer con el cuerpo aquí y la cabeza a '
   'mil kilómetros?»',
   'Pregunta guía: «Mientras hace esa actividad en automático, ¿en qué preocupaciones o pendientes '
   'suele quedarse atrapada su mente?»',
   'Elija una actividad sencilla y cotidiana que ocurrirá con certeza en las próximas 24 horas.']),
 ('2. Encender las cinco anclas sensoriales',
  ['Recorra y marque las cinco casillas sensoriales preparando el ensayo concreto: qué mirará, qué '
   'textura o temperatura notará, qué sonidos escuchará y cómo sentirá el apoyo del cuerpo.',
   'Pregunta guía: «Cuando note que a los diez segundos la mente vuelve a irse a los pendientes, '
   '¿cómo la traerá de regreso sin regañarse?»',
   'Pregunta guía: «¿En qué momento exacto de mañana practicará estos tres minutos de presencia '
   'plena?»',
   'Recuerde que notar que uno se distrajo y volver con amabilidad es el corazón mismo del '
   'entrenamiento.'])],

'act-hecho-o-juicio.html': [('Antes de proponerlo',
  ['Autocrítica severa, etiquetado global («soy un fracaso», «todo está mal») o fusión con '
   'evaluaciones catastróficas.',
   'Objetivo clínico: Distinguir entre las propiedades descriptivas observables de la realidad '
   '(hechos) y las valoraciones que la mente añade y toma como verdades absolutas (juicios).']),
 ('1. Entrenar el oído clínico con las cinco frases',
  ['Explique la distinción de Hayes y Smith (2005): «Las propiedades primarias están en las cosas '
   '(la mesa es de madera); las evaluaciones están en nuestra relación verbal con ellas (la mesa '
   'es horrible). Nuestra mente pega la evaluación sobre el hecho y luego reacciona como si el '
   'juicio fuera físico».',
   'Pregunta guía: «Recorramos estas cinco frases: ¿cuáles registraría una cámara de video y '
   'cuáles requieren una mente que califique?»',
   'Pregunta guía: «¿Qué diferencia siente en el cuerpo entre decir «me tembló la voz dos veces» y '
   'decir «fue un desastre total»?»',
   'Complete las cinco tarjetas interactivas comentando por qué cada una es hecho o evaluación.']),
 ('2. Desarmar la evaluación propia actual',
  ['Pida escribir la frase dura con la que llegó hoy a sesión y sepárenla juntos en las dos '
   'columnas: hechos puros a la izquierda y etiquetas añadidas a la derecha.',
   'Pregunta guía: «Si dejamos únicamente lo que vería una cámara sin adjetivos, ¿qué queda del '
   'suceso?»',
   'Pregunta guía: «¿Cómo suena reformular la frase diciendo: «El hecho es X, y noto que mi mente '
   'está produciendo el juicio de Y»?»',
   'Verifique que la reformulación final mantenga el juicio etiquetado explícitamente como '
   'juicio.'])],

'act-observador-en-el-tiempo.html': [('Antes de proponerlo',
  ['Fusión con el autoconcepto dañado, duelos de rol, vergüenza intensa o temor a ser destruido '
   'por las propias emociones.',
   'Objetivo clínico: Facilitar el contacto experiencial con el Yo como contexto (la perspectiva '
   'continua «yo, aquí, ahora») a través de distintas etapas de la biografía.']),
 ('1. Recorrer las tres escenas vitales',
  ['Con voz pausada, invite a recorrer las tres tarjetas: primero un recuerdo claro de la '
   'infancia, luego una escena significativa de hace unos años y finalmente las sensaciones de '
   'este preciso instante.',
   'Pregunta guía: «En aquel recuerdo de su niñez, ¿quién estaba mirando por detrás de sus ojos?»',
   'Pregunta guía: «Aunque su cuerpo, sus ideas y sus problemas de entonces cambiaron por '
   'completo, ¿es o no es el mismo «Yo» quien está notando esta hoja hoy?»',
   'Permita que la persona escriba brevemente cada escena para activar el indicador del testigo '
   'continuo.']),
 ('2. Habitar el espacio que no se rompe con lo que contiene',
  ['Subraye la conclusión experiencial: «Si usted puede notar sus pensamientos y su dolor de hoy, '
   'usted no puede ser esos pensamientos ni ese dolor; usted es el espacio consciente donde ellos '
   'aparecen y pasan».',
   'Pregunta guía: «Desde ese testigo que ha atravesado décadas enteras sin romperse, ¿cómo se ve '
   'la dificultad de esta semana?»',
   'Pregunta guía: «¿Qué cambia cuando recuerda que esta emoción es un contenido más pasando por '
   'usted, y no la totalidad de quien usted es?»',
   'Cierre conectando esa amplitud del Yo observador con un gesto amable hacia sí mismo hoy.'])],

'met-dos-montanas.html': [('Antes de proponerlo',
  ['Al establecer la alianza terapéutica o cuando la persona se siente atascada y se reprocha no '
   'encontrar la salida sola.',
   'Objetivo clínico: Cultivar una perspectiva amplia, horizontal y compasiva sobre el propio '
   'proceso vital, saliendo del túnel visual que produce el problema inmediato.']),
 ('1. Presentar a los dos escaladores en montañas vecinas',
  ['Comparta la metáfora clásica de Hayes et al. (1999): «Ni yo ni nadie está sentado en la cima '
   'de su montaña sin problemas. Cada uno sube la suya. La única razón por la que a veces puedo '
   'señalarle un sendero es porque desde la montaña de enfrente se ve el mapa que la roca pegada a '
   'su cara le tapa».',
   'Pregunta guía: «¿Cuál es la roca que hoy tiene tan cerca de los ojos que parece ocupar todo el '
   'paisaje?»',
   'Pregunta guía: «¿Cómo cambia la sensación de soledad o exigencia al recordar que todos estamos '
   'subiendo nuestra propia montaña?»',
   'Observe juntos el esquema de las dos montañas y la línea de perspectiva entre ambas.']),
 ('2. Mirar mi propia subida desde la montaña de enfrente',
  ['Invite a la persona a cruzar imaginariamente al mirador de enfrente —como si mirara a un buen '
   'amigo que está en su lugar— para contemplar toda la ladera.',
   'Pregunta guía: «Vista desde enfrente, ¿cuánto camino ha logrado subir ya que desde cerca se le '
   'olvida reconocer?»',
   'Pregunta guía: «¿Qué indicación realista y respetuosa se daría hoy desde esa perspectiva '
   'amplia para el siguiente paso?»',
   'Deje escrita esa frase de perspectiva en el último campo como ancla para la semana.'])],

'met-la-casa-y-los-muebles.html': [('Antes de proponerlo',
  ['Cuando la persona se define por su síntoma («soy depresivo», «soy mi ansiedad») o dedica el '
   'día a pelear con un recuerdo.',
   'Objetivo clínico: Diferenciar la identidad continente (la casa / Yo como contexto) de los '
   'contenidos psicológicos transitorios (los muebles / pensamientos y emociones).']),
 ('1. Inventariar los muebles sin confundirlos con la casa',
  ['Presente la metáfora de Wilson y Luciano (2002): «Imagine que usted es una casa amplia. '
   'Adentro hay muebles cómodos, muebles viejos heredados y algún mueble pesado que hoy estorba. '
   'Pero por más feo que sea un sillón, el sillón jamás es la casa».',
   'Pregunta guía: «¿Qué mueble incómodo y qué relato viejo ocupan hoy un rincón de su sala?»',
   'Pregunta guía: «¿Qué otros muebles valiosos (afectos, capacidades, propósitos) también están '
   'hoy dentro de su casa aunque casi no los mire?»',
   'Complete las tres casillas dentro del plano de la casa para ampliar el campo de atención.']),
 ('2. Habitar las habitaciones valiosas de la casa',
  ['Explore qué ocurre cuando el dueño de la casa se queda todo el día encerrado frente al mueble '
   'feo intentando destruirlo, en lugar de usar la cocina, el jardín o el estudio.',
   'Pregunta guía: «¿Cuánto le está costando quedarse vigilando ese rincón incómodo?»',
   'Pregunta guía: «Si hoy permite que ese mueble esté ahí sin confundirse con él, ¿qué habitación '
   'valiosa de su vida elige habitar hoy?»',
   'Acuerde una acción concreta que represente «usar toda la casa» durante los próximos días.'])],

'act-diana-de-valores.html': [('Antes de proponerlo',
  ['Clarificación de valores, monitoreo de progreso en ACT o reactivación conductual guiada por '
   'sentido.',
   'Objetivo clínico: Evaluar de forma gráfica y conductual la congruencia actual con los valores '
   'en las cuatro áreas vitales y comprometer un movimiento hacia el centro.']),
 ("1. Colocar los cuatro dardos en el Bull's-Eye",
  ["Aclare la regla de oro del Bull's-Eye (Lundgren et al., 2012): «El centro de la diana no mide "
   'si los demás se portan bien ni si todo resulta fácil; mide cuánto se parece su conducta de '
   'esta semana a la persona que usted elige ser en cada cuadrante».',
   'Pregunta guía: «¿Qué cualidad suya quiere poner en juego en trabajo, relaciones, salud y '
   'tiempo personal?»',
   'Pregunta guía: «Al mover los deslizadores y ver sus cuatro dardos en la diana, ¿qué cuadrante '
   'pide hoy su atención con más cariño?»',
   'Ajuste los cuatro controles para que los puntos de colores reflejen el mapa real de esta '
   'semana.']),
 ('2. Nombrar el obstáculo interno y acercar el dardo un anillo',
  ['Ponga el foco en el cuadrante más alejado del centro sin culpa, preguntando qué pensamiento o '
   'emoción ha actuado como viento en contra y qué paso pequeño acerca el dardo.',
   'Pregunta guía: «¿Qué excusa de la mente o qué incomodidad corporal lo ha alejado del centro en '
   'esa área?»',
   'Pregunta guía: «¿Qué acción observable en las próximas 48 horas movería ese dardo un solo '
   'anillo hacia el centro de la diana?»',
   'Verifique que el paso elegido dependa de las manos de la persona y no del resultado externo.'])],

'act-punto-dulce.html': [('Antes de proponerlo',
  ['Consultantes desconectados emocionalmente de sus valores, muy autoexigentes o atrapados en '
   'mandatos ajenos.',
   'Objetivo clínico: Contactar experiencialmente con los valores personales a través de un '
   'recuerdo vivo de plenitud y sentido, sorteando la intelectualización y el «debería».']),
 ('1. Evocar sin prisa una escena de «punto dulce»',
  ['Guíe el ejercicio de Kelly Wilson (2009): «Dejemos por un momento las listas de metas. Busque '
   'en su memoria un momento real —puede ser sencillo o cotidiano— en el que sintió que la vida '
   'tenía sabor, que usted estaba plenamente ahí y no hacía falta nada más».',
   'Pregunta guía: «¿Dónde estaba, qué percibían sus sentidos y qué estaba haciendo usted en ese '
   'momento?»',
   'Pregunta guía: «Al traer esa escena aquí y ahora, ¿qué sensación aparece en su pecho o en su '
   'rostro?»',
   'Invite a redactar la escena en primera persona y a notar la resonancia emocional presente.']),
 ('2. Extraer el ingrediente activo y sembrarlo hoy',
  ['Toque los botones de cualidades para identificar qué valor vivo latía dentro de ese recuerdo, '
   'notando también que si evocar ese momento conmueve o duele es justamente porque eso sigue '
   'importando mucho.',
   'Pregunta guía: «¿Cuál era el ingrediente secreto de vitalidad que estaba encendido en usted en '
   'aquel instante?»',
   'Pregunta guía: «¿Con qué gesto pequeño puede traer hoy una gota de ese mismo ingrediente a su '
   'semana actual?»',
   'Cierre diferenciando el sabor cálido del valor elegido frente a la frialdad de las '
   'obligaciones impuestas.'])],

'act-dial-disposicion.html': [('Antes de proponerlo',
  ['Cuando el consultante condiciona sus pasos a que primero baje la ansiedad o se frustra porque '
   'el malestar reaparece.',
   'Objetivo clínico: Cambiar el objetivo del consultante desde el control emocional (bajar el '
   'dial del malestar) hacia la apertura conductual (subir el dial de la disposición).']),
 ('1. Contrastar las dos perillas del tablero',
  ['Presente la metáfora de las dos escalas (Hayes et al., 1999): «Imagine dos perillas de 0 a 10. '
   'La primera es el malestar; no tiene cable directo a su voluntad y cuando intenta forzarla a '
   'cero se traba y sube. La segunda es la disposición: cuánto espacio elige abrir hoy para dar el '
   'paso que le importa».',
   'Pregunta guía: «¿En qué número está hoy la perilla de su malestar y cuánta energía ha gastado '
   'tratando de bajarla a la fuerza?»',
   'Pregunta guía: «¿Qué pasa en el tablero cuando sube la perilla de la disposición a 8 o 9 '
   'aunque el malestar siga presente?»',
   'Mueva ambos deslizadores para observar cómo cambia el mensaje clínico según la combinación.']),
 ('2. Comprometer la mano con la perilla que sí responde',
  ['Invite a definir en qué situación concreta de esta semana pondrá su mano sobre el dial de la '
   'disposición en lugar de vigilar el termómetro emocional.',
   'Pregunta guía: «¿En qué situación valiosa elige hoy subir su disposición?»',
   'Pregunta guía: «¿Qué sensación física o qué pensamiento está dispuesto a llevar consigo en la '
   'mochila mientras da ese paso?»',
   'Refuerce que la disposición no es resignarse ni querer sufrir, sino elegir vivir con las manos '
   'libres.'])],
}

# Correcciones de redacción tras el rework de escenas (ver ajustes_texto.py).
import ajustes_texto as _ajustes
_HALLADOS_GUIONES = _ajustes.aplicar(GUIONES)
