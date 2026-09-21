# El taller

Esta carpeta es el taller. **No hace falta abrirla para usar las herramientas**: los archivos
`.html` de la carpeta de arriba funcionan solos, con doble clic, sin internet y sin nada instalado.
Esto sirve únicamente para cuando haya que cambiar algo en todas a la vez.

## Qué hay aquí

| Archivo | Para qué |
|---|---|
| `kit.css` | Los estilos que comparten las 26 hojas: colores, fichas, calibradores, modo lámina, impresión. |
| `kit.js` | El motor común: fichas con «+», guardado local, copiar resumen, mostrador de arrastre y el reloj de las escenas que se mueven. |
| `plantilla.html` | El esqueleto: cabecera, notas del profesional plegadas y barra de botones al final. |
| `partes/*.parte` | El contenido propio de cada herramienta. Una por archivo. |
| `construir.py` | Junta todo y escribe los `.html` autónomos, el `index.html` y la guía. |
| `guia.py` | El contenido clínico de `guia.html`: para qué sirve cada hoja, en qué casos y con qué va antes o después. |
| `guiones.py` | Los guiones de sesión: qué se dice en voz alta al proponer cada metáfora, qué no se dice y qué hacer con lo que salga. |
| `armonizar_antiguas.py` | Rehace las tres hojas anteriores al kit desde `_respaldo/`, sin tocar sus motores. |
| `revisar.py` | Comprueba las hojas construidas antes de repartirlas. |
| `_respaldo/` | Las tres hojas anteriores al kit, como estaban antes de armonizarlas. |

## Cómo se reconstruye

```bash
python construir.py
```

Reescribe las 26 herramientas, el índice y la guía de uso. Para trabajar sobre una sola, se le pasa un pedazo del
nombre y solo esa se imprime en pantalla (igual se reconstruyen todas, que toma menos de un segundo):

```bash
python construir.py brujula
```

Las tres hojas antiguas van por su cuenta y **siempre se rehacen desde el respaldo**, así que los
cambios que haya que hacerles se escriben dentro de `armonizar_antiguas.py`, no en el HTML de
arriba, que se sobreescribe:

```bash
python armonizar_antiguas.py
```

Y antes de repartir nada:

```bash
python revisar.py
```

Avisa de lo único que rompe una hoja en silencio: JavaScript que pide por id un elemento que ya no
está en el HTML. Es exactamente lo que dejó a las fortalezas del carácter sin casillas durante un
tiempo. También avisa de llaves descuadradas y de restos de lenguaje que ya no corresponde.

## La guía de uso

`guia.html` no es una herramienta: es la hoja de ruta del profesional, y por eso no lleva kit, ni
guardado, ni notas. Su contenido vive en `guia.py`, en dos estructuras:

- `GUIA`, con una ficha por hoja: para qué sirve, en qué casos rinde, cómo se encadena y qué
  cuidado tiene.
- `RUTAS`, con los encadenamientos que se repiten en consulta.

**Al agregar una herramienta nueva hay que agregarle también su ficha ahí**, o quedará en el índice
sin indicación de uso.

Los guiones de sesión van aparte, en `guiones.py`, en un diccionario indexado por nombre de archivo.
Cada guion es una lista de bloques `(título, [líneas])`, y dentro de las líneas: las que empiezan
por `«` son lo que se dice en voz alta, las que empiezan por `✗` son lo que no se dice, y el resto
son indicaciones para quien acompaña. La ficha los muestra plegados.

Solo llevan guion las hojas experienciales, donde la manera de proponerlas decide si el ejercicio
ocurre o se convierte en otra cosa. Las de registro y las de evaluación no lo necesitan.

Al cambiar el número de elementos de una lista hay que barrer la prosa que lo menciona, que vive
en cuatro sitios distintos y es fácil dejar uno atrás: el `sub` y el `resumen` de `@@meta`, los
`<p class="ayuda">` dentro de la hoja, la ficha en `guia.py` y las frases del guion en
`guiones.py`. Al pasar el jardín de veinte a veinticuatro semillas quedaron tres sitios diciendo
veinte y uno diciendo que se dejaban catorce afuera.

Cuidado con el CSS que vive dentro de `guia.py`: está en una cadena de Python, así que un escape
CSS como `2` se lee como escape octal y sale un carácter de control. Ahí van los caracteres
literales.

## Cómo se agrega una herramienta nueva

Se crea un archivo en `partes/` con extensión `.parte` y cuatro secciones:

```
@@meta
archivo: tcc-mi-herramienta.html     ← nombre del HTML que se genera
titulo: Mi herramienta
orden: 07                            ← posición dentro de su enfoque en el índice
enfoque: Cognitivo-conductual        ← uno de los cuatro de ORDEN_ENFOQUES en construir.py
etiqueta: Exposición                 ← la etiqueta de color de la ficha del índice
identificacion: si                   ← opcional; solo si la hoja existe para dejar registro
lamina: si                           ← opcional; para las hojas que se exponen o se proyectan
sub: El párrafo de presentación que va bajo el título.
fuente: De dónde sale el procedimiento, con capítulo o ficha.
resumen: Una o dos frases para la ficha del índice.
@@css
  /* estilos propios de esta hoja */
@@html
  <!-- el contenido, sin cabecera ni barra: eso lo pone la plantilla -->
@@js
  /* la lógica, terminando en Kit.iniciar({...}) */
```

`identificacion` se omite en casi todas: son recursos de sesión, no formularios. Solo la llevan las
que existen para dejar registro (análisis en cadena, tarjeta diaria, escalera de exposición y
análisis funcional).

`lamina` ya no enciende nada por sí sola: marca la hoja como proyectable y el kit le pone un
botón «Modo lámina» en la barra, que sube el tamaño de letra y se recuerda en ese equipo. La
llevan las hojas de DBT, que se usan tanto para trabajar como para exponer. Nacían en lámina y en
consulta uno a uno la letra grande alargaba la hoja sin aportar nada.

## El criterio de diseño

Vale la pena tenerlo presente al agregar cualquier herramienta nueva:

1. **La hoja no explica: muestra.** Las indicaciones se reducen al mínimo indispensable. Lo que se
   puede enseñar hablando no se escribe en la pantalla, porque el texto de más rompe la inmersión.
2. **Todo se elige, se calibra o se arrastra.** Tres o cuatro fichas, las más frecuentes, y un
   botón `+` para que la persona ponga la suya. El texto libre existe, va plegado y es opcional.
3. **La metáfora se juega, no se narra.** Los empujones, los jalones, los tramos y el riego cambian
   el dibujo. Lo que la escena ya dice no se repite en un párrafo debajo.
4. **Lo que no depende de la persona, ocurre solo.** En las hojas con escena viva el monstruo jala,
   el bus avanza, las piezas negras brotan, la aguja se mueve y las hojas bajan por el arroyo sin
   que nadie apriete nada. Un botón para producir lo que en la vida real llega sin permiso pone a
   la persona en el papel de autor, y ese es justamente el papel del que la hoja tiene que sacarla.
   Lo que sí lleva botón es la decisión: jalar, discutir, empujar, controlar, cavar o soltar.
5. **Una pregunta, no un informe.** Donde antes iba una lectura larga va una sola pregunta para
   abrir la conversación. Cuando la lectura sirve, se muestra condensada: todas las combinaciones
   posibles a la vista, con su indicación al lado y la vigente encendida.
6. **Nada de días ni de horas en la hoja.** El compromiso, el cuándo y el con qué se acuerdan
   hablando. La hoja deja el recordatorio, no la agenda.
7. **Todo cabe en un archivo.** Sin dependencias, sin servidor, sin conexión.
8. **Uso clínico.** No hay selector de modo ni mención institucional: son hojas de consulta.

## Lo que el kit hace solo, sin que la hoja pida nada

Al llamar a `Kit.iniciar` —o a `Kit.soloModo` en las tres antiguas— se aplican tres arreglos de
presentación que no tocan el contenido de ninguna hoja:

- **Un paso a la vez.** Si hay tres o más secciones numeradas —`.paso` o `.bloque`, lo que cuenta
  es el `<span class="num">`— se pliegan todas menos la que se está trabajando, con un
  «Siguiente» al pie. Los pasos siguen en el documento, así que el motor de cada hoja los sigue
  encontrando, y al imprimir se abren todos. Los pasos que la hoja oculta con `hidden` —las dos
  ramas de Verificar los hechos— no cuentan mientras no estén a la vista, y el que la hoja destape
  se abre solo.
- **La ayuda detrás de un signo.** Los `<p class="ayuda">` que cuelgan directamente de la sección
  pasan a un «?» junto al título. Los que acompañan a un campo dentro del `.cuerpo` se quedan
  donde están: esos sí son indicaciones de uso.
- **El botón de lámina**, en las hojas marcadas con `lamina: si`.

Nada de esto hay que pedirlo desde la hoja. Al agregar una herramienta nueva, basta con numerar
las secciones como siempre.

## Las funciones del kit que más se usan

```js
Kit.chips("idContenedor", ["Una", "Otra"], alCambiar)         // fichas + boton "+"
Kit.chips("idContenedor", ["Una", "Otra"], alCambiar, true)   // sin el "+"
Kit.opciones("idContenedor", [["Título","Descripción"]], alCambiar, unica)
Kit.activas("idContenedor")                              // devuelve lo marcado
Kit.agregarLibre("idContenedor", "texto")                // pone una ficha propia
Kit.mostrador({bancoId, ranurasId, cupo, items, etiquetas, alCambiar})
Kit.gota(7)                                              // gota que se llena segun el nivel
Kit.reloj(fn)                                            // latido de escena: fn(dt) unas 25 veces por segundo
Kit.svg("circle", {cx:10, cy:10, r:5})                   // crear nodos SVG
Kit.mezcla("#c26a4e", "#3f7d5a", 0.5)                    // interpolar dos colores
Kit.brindis("Mensaje breve")                             // aviso flotante
```

Los `items` del mostrador aceptan `color`, y con él la pieza, su ranura y el rótulo del grupo salen
del mismo color: sirve para distinguir categorías de un vistazo.

Y el arranque, al final de cada `@@js`:

Las escenas que se mueven usan `Kit.reloj`, un solo latido por hoja. Se declara junto al resto
del estado y se arranca cuando la persona decide empezar:

```js
const escena = Kit.reloj(latido);   // latido(dt) recibe los segundos transcurridos
escena.andar();                     // empieza
escena.parar();                     // se detiene
escena.anda();                      // ¿está andando?
```

Se pausa sola cuando la pestaña se va al fondo y retoma sin saltos al volver, así que una hoja
abierta en segundo plano no gasta batería. Dentro de `latido` no se llama a `Kit.guardar()`: el
guardado va en las acciones, no en cada cuadro.

```js
Kit.iniciar({
  clave: "identificador-unico",   // dónde guarda en este equipo
  extra: () => ({...}),           // opcional: estado propio que no vive en inputs
  restaurar: d => {...},          // opcional: cómo recuperarlo
  alCambiar: refrescar,           // se llama al cargar y cuando algo cambia
  resumen: resumen                // el texto que arma "Copiar resumen"
});
```

## Las columnas laterales del índice y de la guía

`rieles.py` arma las dos columnas que usan `index.html` y `guia.html` en pantallas anchas: a la
izquierda, el buscador y el filtro por enfoque; a la derecha, el mapa de las hojas, las dos fijas
mientras se recorre el centro. En pantallas medianas y en el teléfono los filtros vuelven arriba y
el mapa se oculta. La página solo marca `data-grupo` en cada bloque de enfoque y `data-item` (con
`data-enf` y `data-titulo`, y `data-href` si abre otra página) en cada ficha; el mapa se arma solo.
Las hojas de trabajo no usan este módulo.
