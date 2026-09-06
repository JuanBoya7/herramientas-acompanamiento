# -*- coding: utf-8 -*-
"""
Revisa las hojas construidas antes de repartirlas.

Busca lo único que de verdad las rompe en silencio: JavaScript que pide un
elemento por id y ese id ya no está en el HTML. Es lo que pasó cuando el
selector de casillas de las fortalezas se quedó fuera de la hoja: $("b3")
devolvía nada, la excepción cortaba el arranque y la hoja salía en blanco.

También avisa de restos de lenguaje que ya no corresponde y de llaves
descuadradas en el bloque de JavaScript propio de cada hoja.

    python revisar.py
"""
import re, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
HOJAS = AQUI.parent

# ids que el kit crea o consulta a propósito aunque no estén en la hoja
TOLERADOS = {"brindis", "fecha", "nombre", "sesion", "profesional", "proNoImprimir",
             "proObservaciones", "proHipotesis", "proTarea", "proProxima"}

# Registro que ya no corresponde: institucional, de consejería y, sobre todo,
# el que da por hecho que quien tiene la hoja delante es un estudiante. Van
# como expresiones regulares porque palabras como "parcial" o "nota" son
# legítimas en otros usos ("apertura parcial", "notas del profesional").
PROHIBIDO = [
    r"\bFUAA\b",
    r"consejer\w*",
    r"Se responde en voz alta",
    r"\bestudiantes?\b",
    r"\buniversidad\b|\buniversitari\w*",
    r"\bsemestres?\b",
    r"\blos parciales\b|\b[eu]n parcial\b|\bel parcial\b|\bparcial (corto|final)\b",
    r"\bla materia\b|\bla carrera\b|\besta carrera\b|\bde programa\b|\bla U\b",
    r"\b(en|de|la) clase\b|\bdel curso\b|\bel curso\b",
    r"\bdocentes?\b|\bprofesor\w*\b|\bmonitor\b|\btutor[íi]a\b",
    r"\bcuaderno\b|\bestuche\b|\btemario\b|\bquiz\b",
    r"\bnota baja\b|\blas notas\b|\bdeserci[óo]n\b",
]

SALTO = chr(10)
BARRA = chr(92)

# Caracteres tras los cuales una barra abre una expresión regular y no divide.
ANTES_DE_REGEX = set("(,=:[!&|?;{}+-*%~^<>") | {""}


def ids_del_html(d):
    cuerpo = re.sub(r"<script>.*?</script>", "", d, flags=re.S)
    return set(re.findall(r'\sid="([^"]+)"', cuerpo))


def ids_pedidos(d):
    """Los $("literal") y getElementById("literal") del JavaScript."""
    guion = SALTO.join(re.findall(r"<script>(.*?)</script>", d, flags=re.S))
    pedidos = set()
    for m in re.finditer(r'(?:\$|getElementById)\(\s*"([A-Za-z][\w-]*)"\s*\)', guion):
        pedidos.add(m.group(1))
    return pedidos


def _fin_cadena(g, i, comilla):
    """Devuelve el índice justo después de la comilla de cierre."""
    j = i + 1
    while j < len(g):
        c = g[j]
        if c == BARRA:
            j += 2
            continue
        if c == comilla or c == SALTO:
            return j + 1
        j += 1
    return len(g)


def _fin_regex(g, i):
    """Igual, para una expresión regular. Si no cierra en la línea, era división."""
    j, clase = i + 1, False
    while j < len(g):
        c = g[j]
        if c == BARRA:
            j += 2
            continue
        if c == SALTO:
            return i + 1
        if c == "[":
            clase = True
        elif c == "]":
            clase = False
        elif c == "/" and not clase:
            return j + 1
        j += 1
    return i + 1


def llaves(d):
    """Saldo de llaves en el JavaScript propio de la hoja.

    Recorre el texto carácter a carácter en vez de borrar las cadenas con
    expresiones regulares. Dentro de una plantilla `...${...}` las comillas
    son texto corriente, y borrarlas desde fuera se comía la llave de apertura
    y sacaba avisos de hojas que estaban bien.
    """
    guiones = re.findall(r"<script>(.*?)</script>", d, flags=re.S)
    if not guiones:
        return 0
    g = guiones[-1]

    saldo = 0
    pila = ["codigo"]      # dónde vamos: "codigo" o "plantilla"
    marcas = []            # profundidad de llaves al abrir cada ${
    prof, anterior = 0, ""
    i, n = 0, len(g)

    while i < n:
        c = g[i]

        if pila[-1] == "plantilla":
            if c == BARRA:
                i += 2
            elif c == "`":
                pila.pop()
                i += 1
            elif g[i:i + 2] == "${":
                pila.append("codigo")
                marcas.append(prof)
                i += 2
            else:
                i += 1
            continue

        if g[i:i + 2] == "/*":
            j = g.find("*/", i + 2)
            i = n if j < 0 else j + 2
        elif g[i:i + 2] == "//":
            j = g.find(SALTO, i)
            i = n if j < 0 else j
        elif c == '"' or c == "'":
            i = _fin_cadena(g, i, c)
            anterior = "a"
        elif c == "`":
            pila.append("plantilla")
            i += 1
        elif c == "/" and anterior in ANTES_DE_REGEX:
            i = _fin_regex(g, i)
            anterior = "a"
        elif c == "{":
            prof += 1
            saldo += 1
            anterior = c
            i += 1
        elif c == "}":
            if len(pila) > 1 and marcas and prof == marcas[-1]:
                pila.pop()          # cierra un ${ } y no cuenta como llave
                marcas.pop()
            else:
                prof -= 1
                saldo -= 1
            anterior = c
            i += 1
        else:
            if not c.isspace():
                anterior = c
            i += 1

    return saldo


def main():
    problemas = revisadas = 0
    for ruta in sorted(HOJAS.glob("*.html")):
        if ruta.name == "index.html":
            continue
        revisadas += 1
        d = ruta.read_text(encoding="utf-8")
        avisos = []

        faltan = sorted(ids_pedidos(d) - ids_del_html(d) - TOLERADOS)
        if faltan:
            avisos.append("ids que el JS pide y no están: " + ", ".join(faltan))

        desc = llaves(d)
        if desc:
            avisos.append(f"llaves descuadradas en el JS ({desc:+d})")

        restos = []
        for patron in PROHIBIDO:
            for m in re.finditer(patron, d, flags=re.I):
                trozo = d[max(0, m.start() - 45):m.end() + 45].replace(SALTO, " ")
                restos.append("«…%s…»" % re.sub(r"\s+", " ", trozo).strip())
        if restos:
            avisos.append("registro que ya no corresponde:")
            avisos += ["  " + r for r in dict.fromkeys(restos)]

        if avisos:
            problemas += 1
            print(f"{SALTO}  {ruta.name}")
            for a in avisos:
                print(f"      - {a}")

    if problemas:
        print(f"{SALTO}{problemas} hoja(s) con avisos.")
        return 1
    print(f"Las {revisadas} hojas están limpias.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
