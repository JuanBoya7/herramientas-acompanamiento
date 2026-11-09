# -*- coding: utf-8 -*-
"""
Genera las cuadrículas 3x2 de las lecturas ACT con Nano Banana (Antigravity) usando como
semilla de estilo las acuarelas del juego de roles del hexaflex
(referencia-estilo.jpg = mosaico de hexaflex-recurso-1..6.webp del Seminario).

Codex quedó descartado el 2026-11-09: con la suscripción actual ninguno de sus modelos trae
la herramienta de imágenes. El script de Nano Banana está en _agentes y detecta solo la
dirección y el token del servidor de Antigravity (que debe estar abierto).

    python generar_grids.py                 # las que falten
    python generar_grids.py grid-02 grid-05 # solo esas (rehace aunque existan)
"""
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REF = AQUI / "referencia-estilo.jpg"
CELDAS = json.loads((AQUI / "celdas.json").read_text(encoding="utf-8"))
SCRIPT = r"C:\Users\User\Documents\Varios\_agentes\generar-imagen-nanobanana.ps1"

ESTILO = (
    "Style: exactly the same hand as the style seed. Soft loose watercolor illustration on white paper, "
    "delicate thin graphite and ink lines only where needed, gentle washes that bleed and fade into the white paper at the edges, "
    "muted palette of deep teal, slate blue-grey, sage green, warm sand and a few soft ochre touches, calm contemplative mood, "
    "refined editorial picture-book quality for adults. NOT cartoon, NOT comic, NOT cute, no thick black outlines, no flat vector colors, "
    "no saturated colors, no glossy digital look, no photorealism. "
    "Recurring character whenever a woman appears: a young adult woman with dark hair in a loose low bun, loose off-white sweater, "
    "wide teal-grey trousers, simple shoes; face shown in profile or from behind with minimal features. "
    "No text, no letters, no numbers, no words anywhere."
)

POS = ["top-left", "top-center", "top-right", "bottom-left", "bottom-center", "bottom-right"]


def brief(celdas):
    partes = ["Cell %d (%s): %s" % (i + 1, POS[i], desc) for i, (slug, desc) in enumerate(celdas)]
    return (
        "A single landscape sheet containing a grid of 3 columns by 2 rows = six separate watercolor vignettes "
        "on pure white paper. Each vignette is self-contained, roughly square, centered in its cell, fades softly into white, "
        "and is separated from its neighbors by wide clean white gutters (no borders, no frames, no lines between cells, "
        "nothing crossing a gutter). Each vignette must clearly show its metaphor so a viewer understands it at a glance. "
        + " ".join(partes) + " " + ESTILO
    )


def generar(nombre):
    salida = AQUI / (nombre + ".jpg")
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", SCRIPT,
           "-Descripcion", brief(CELDAS[nombre]), "-Salida", str(salida),
           "-Formato", "3:2", "-Paleta", "libre", "-EstiloRef", str(REF)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if salida.exists():
        print(nombre, "->", salida)
        return True
    print(nombre, "SIN IMAGEN\n", r.stdout[-1500:], r.stderr[-1500:])
    return False


if __name__ == "__main__":
    pedidos = sys.argv[1:]
    nombres = [n for n in CELDAS if (not pedidos and not (AQUI / (n + ".jpg")).exists()) or any(n.startswith(p) for p in pedidos)]
    for n in nombres:
        generar(n)
