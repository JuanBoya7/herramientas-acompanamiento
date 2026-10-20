# Ilustraciones para las herramientas

Generadas con la herramienta integrada de generación de imágenes de Codex, en modo de
generación de imágenes nuevas. No se utilizó la alternativa CLI. Los PNG originales se copian
al proyecto y se incrustan como datos dentro del HTML; no hay peticiones a un servicio de imágenes
al abrir una herramienta. Se conserva el canal de transparencia del monstruo.

## Arroyo — `arroyo-acuarela.png`

Especificación del prompt empleado, resumida:

> Ilustración en acuarela sobria para una herramienta terapéutica dirigida a adultos. Arroyo
> horizontal que corre de izquierda a derecha, composición panorámica aproximadamente 7:3.
> Agua turquesa pálida y centro despejado entre el 25 % y el 75 % de la altura, para superponer
> hojas y pensamientos animados. Orillas con musgo, piedras y helechos discretos. Textura de
> papel y pigmentos suaves. Sin hojas flotantes, personas, texto, controles ni interfaz.

Uso: fondo de la escena en `met-hojas-en-el-arroyo.html`. Las hojas, los pensamientos y el
movimiento se dibujan por separado para mantenerlos interactivos y legibles.

## Monstruo — `monstruo-acuarela.png`

Especificación del prompt empleado, resumida:

> Una sola criatura de cuerpo completo en acuarela, sobre fondo realmente transparente.
> Pelaje gris ciruela, pequeños cuernos, volumen y textura orgánica; carácter incómodo sin
> estética de terror ni estilo infantil. Mira hacia la izquierda y se inclina hacia la derecha
> como resistiendo un tirón. Brazos extendidos hacia la izquierda, manos sujetando una cuerda
> invisible aproximadamente al 35 % de la altura de la figura. Sin dibujar la cuerda, escenario,
> texto ni otros personajes. Mantener toda la silueta dentro del encuadre.

Uso: personaje en `met-la-cuerda.html`. El tamaño, la cuerda y la postura de la persona siguen
respondiendo a las decisiones durante la práctica.

## Paisajes de las escenas (2026-10-20)

Acuarelas generadas con GPT Image a través de Codex, con `arroyo-acuarela.png` como
referencia de técnica, para que todas las escenas se vean de una misma mano. Se guardan
en JPEG (90–170 KB), sin transparencia, porque son fondos. Cada escena crea el elemento
`<image>` una sola vez y lo reutiliza: el dibujo se repinta 25 veces por segundo.

| Archivo | Escena | Cómo encaja |
|---|---|---|
| `bus-acuarela.jpg` | `met-el-bus` | Campo andino; el borde inferior del campo cae sobre la berma de la carretera |
| `cielo-acuarela.jpg` | `act-el-cielo-y-el-clima` | Cielo despejado, recortado a la elipse que crece con cada ciclo |
| `lago-acuarela.jpg` | `act-los-ganchos` | Lago visto de lado; la línea del agua cae en `AGUA` |
| `campo-acuarela.jpg` | `met-el-hoyo` | Cielo y pradera; su borde inferior sigue a la superficie, que sube al cavar |
| `mar-acuarela.jpg` | `crisis-surfear-el-impulso` | Mar en calma; el horizonte queda detrás de la ola dibujada |
| `colinas-acuarela.jpg` | `act-quien-lleva-los-globos` | Colinas bajas; su borde inferior cae sobre el suelo del camino |

En los pedidos se excluyen personas, animales, texto y los objetos que la escena dibuja
encima (bus, ganchos, olas, globos), y se pide dejar despejada la zona central.

## Figuras y suelos (2026-10-20)

Figuras en acuarela con fondo transparente (WebP, 3–40 KB), generadas con GPT Image (Codex)
con el arroyo o el monstruo como referencia de técnica. Se dibujan con `Kit.figura(clave, href,
attrs)`, que crea cada `<image>` una sola vez. Cada figura conserva el tamaño y los puntos de
apoyo del dibujo vectorial que reemplaza (manos, pies, ruedas, tabla), así que la lógica de
cada escena no cambió.

| Archivo | Escena | Notas |
|---|---|---|
| `bus-cuerpo.webp`, `bus-rueda.webp`, `bandera.webp` | `met-el-bus` | Ruedas aparte para que giren; las cabezas de los pasajeros siguen en vector |
| `pez.webp` | `act-los-ganchos` | |
| `surfista.webp` | `crisis-surfear-el-impulso` | Gira con la pendiente de la ola, como la tabla anterior |
| `cavador.webp`, `soltado.webp` | `met-el-hoyo` | Cavando se inclina con cada palada; soltada, se endereza |
| `caminante.webp`, `caminante-mano.webp` | `act-quien-lleva-los-globos` | La mano de atrás sostiene el ramo; la otra pose se estira hacia el globo de enfrente; apagada = gris |
| `cuerda-jala.webp`, `cuerda-suelta.webp` | `met-la-cuerda` | La caída dentro del hoyo sigue en vector, con textura |
| `hoja.webp` | `met-hojas-en-el-arroyo` | Cada hoja guarda su propia imagen |
| `asfalto-`, `tierra-`, `sendero-acuarela.jpg` | bus, hoyo y cuerda, globos | Suelos |

Lo que depende de lo que se elige (globos, clima, cabezas, cebos, orillas) sigue en vector,
con el filtro `Kit.acuarela(svg)`: borde irregular y pigmento desparejo, un filtro por escena.
La cuerda recibió además cielo y pradera (`campo-acuarela.jpg`) y tierra a los lados del hoyo.
