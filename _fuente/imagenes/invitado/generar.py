# -*- coding: utf-8 -*-
"""
Imágenes de «El invitado incómodo» (met-16): un fondo en acuarela y una hoja 3x2 con las
seis figuras, generadas con Nano Banana (Antigravity) usando como semilla de estilo las
acuarelas del juego de roles del hexaflex. Después:  python recortar.py

    python generar.py fondo | figuras
"""
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REF = AQUI.parent / "grids_v2" / "referencia-estilo.jpg"
SCRIPT = r"C:\Users\User\Documents\Varios\_agentes\generar-imagen-nanobanana.ps1"

ESTILO = ("Soft loose watercolor on white paper, delicate thin ink lines only where needed, muted palette of deep teal, "
          "slate blue-grey, sage, warm sand and soft ochre, refined editorial picture-book quality for adults. "
          "NOT cartoon, NOT cute, no thick black outlines, no flat vector colors, no saturated colors. No text, no letters anywhere.")

FONDO = (
    "Wide cutaway side view of a small house at night, like a stage set, 2:1 composition. "
    "LEFT 34% of the image: an outdoor wooden porch under a deep blue night sky with stars and a small porch lamp, a few plants. "
    "At exactly 34% from the left: the house's front wall with an EMPTY open doorway (no door leaf at all, just the empty frame), "
    "the doorway reaching from the floor to about 50% of the image height. "
    "RIGHT 66%: a warm cozy living room seen in cutaway, string lights along the ceiling, a long wooden table on the right half "
    "with food, glasses and candles, five friends seated on the FAR side of the table laughing and talking (small, mid-ground), "
    "an armchair and a lamp near the doorway on the inside. "
    "The floor line is a continuous horizontal line at 91% of the image height across porch and room. "
    "Leave the floor area between the doorway and the table, and the porch floor near the door, EMPTY of people and objects "
    "(other figures will be placed there). " + ESTILO
)

FIGURAS = (
    "Character sheet: a grid of 3 columns by 2 rows with six separate full-body figures on PURE WHITE background, "
    "all drawn at the SAME scale, each standing with feet on an invisible baseline at the bottom of its cell, side view, "
    "nothing else in the cells (no floor, no shadow, no furniture, no door), wide white gaps between cells. "
    "Figures 1-3 are the HOST: a young adult woman, dark hair in a loose low bun, loose off-white sweater, wide teal-grey trousers. "
    "Figure 1 (top-left): the host leaning hard with her shoulder and both palms against an invisible door on the LEFT side, "
    "body tilted to the left, legs braced, tense, her back turned to the right. "
    "Figure 2 (top-center): the host standing relaxed and smiling, holding a glass, body turned slightly to the RIGHT as if talking with friends. "
    "Figure 3 (top-right): the host walking to the RIGHT, mid-stride. "
    "Figures 4-6 are the UNWELCOME GUEST: a scruffy middle-aged man with messy grey hair and stubble, a long patched muddy coat, "
    "worn boots; grumpy and awkward but not scary, not a villain. "
    "Figure 4 (bottom-left): the guest knocking hard on an invisible door to the RIGHT, fist raised, leaning forward. "
    "Figure 5 (bottom-center): the guest standing with arms crossed, grumbling, facing LEFT. "
    "Figure 6 (bottom-right): the guest walking to the RIGHT, hands in coat pockets, shuffling. " + ESTILO
)


def generar(nombre, brief, formato):
    salida = AQUI / (nombre + ".jpg")
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", SCRIPT,
           "-Descripcion", brief, "-Salida", str(salida), "-Formato", formato, "-Paleta", "libre", "-EstiloRef", str(REF)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(nombre, "->", salida if salida.exists() else "SIN IMAGEN\n" + r.stdout[-1200:] + r.stderr[-1200:], flush=True)


if __name__ == "__main__":
    pedidos = sys.argv[1:] or ["fondo", "figuras"]
    if "fondo" in pedidos:
        generar("fondo", FONDO, "16:9")
    if "figuras" in pedidos:
        generar("figuras", FIGURAS, "3:2")
