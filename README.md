# Herramientas de acompañamiento

Veintinueve hojas de trabajo interactivas para el espacio clínico. Cada una es **un solo archivo
HTML** que funciona con doble clic: sin instalación, sin servidor y sin conexión.

Todo se elige, se calibra o se arrastra. Cada hoja lleva plegado un bloque de notas del
profesional, un botón para pasar lo trabajado a la historia clínica y una versión de impresión
limpia.

**Empezar por [`index.html`](index.html)**, o por la [guía de uso](guia.html), que dice para qué
sirve cada hoja, en qué casos rinde, con qué va antes o después y dónde conviene tener cuidado.

## Qué hay

| Enfoque | Hojas |
|---|---|
| **Metáforas vivas** | El tablero · El jardín de valores · La cuerda y el monstruo · Hojas en el arroyo · El bus y los pasajeros · Los ochenta años · El polígrafo · La palabra repetida · La radio que no se apaga · El hombre en el hoyo |
| **Psicología positiva** | Mi flor PERMAH · Mis fortalezas del carácter |
| **ACT** | La brújula de valores · El costo de la lucha · Por dónde entrar · Soltar el anzuelo |
| **DBT** | Análisis en cadena · Tarjeta de crisis · Verificar los hechos · Pedir y decir que no · Mente sabia · Tarjeta diaria |
| **Cognitivo-conductual** | Registro de pensamientos · Flecha descendente · Escalera de exposición · Activación conductual · Solución de problemas · Autoinstrucciones · Análisis funcional |

Ocho de ellas tienen **escena viva**: la metáfora ocurre en tiempo real y no espera a que se
apriete un botón. El monstruo jala solo, el bus avanza solo, las piezas negras brotan solas, la
aguja del polígrafo se mueve sola y las hojas bajan solas por el arroyo. Lo que sí lleva botón es
la decisión: jalar, discutir, empujar, controlar, cavar o soltar.

## Privacidad

Estas hojas **no contienen ni recogen datos de ninguna persona atendida**. Lo que se diligencia
queda en el navegador del equipo donde se usa (`localStorage`), no viaja a ningún servidor y no
llega a este repositorio. En un computador compartido conviene cerrar con *Empezar de nuevo*.

## Para modificarlas

El contenido de cada hoja vive en `_fuente/partes/*.parte` y los archivos HTML de arriba son el
producto: **se sobreescriben en cada construcción**, así que no se editan a mano.

```bash
cd _fuente
python construir.py      # rehace las hojas, index.html y guia.html
python revisar.py        # comprueba las hojas antes de repartirlas
```

Los detalles del taller, el criterio de diseño y las funciones del kit están en
[`_fuente/LEEME.md`](_fuente/LEEME.md).

## Procedencia

Las hojas se apoyan en fuentes publicadas, citadas dentro de cada una: el manual ACT de Díaz
Corbobés, el manual de habilidades DBT de Linehan, la terapia cognitiva de Beck, y la
clasificación VIA y el modelo PERMAH de Seligman. Las metáforas de ACT (el tablero, el bus, la
cuerda, las hojas en el arroyo, el hombre en el hoyo, el polígrafo) provienen de Hayes, Strosahl y
Wilson.
