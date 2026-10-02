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
}
