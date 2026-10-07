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
