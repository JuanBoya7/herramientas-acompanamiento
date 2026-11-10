# -*- coding: utf-8 -*-
"""
Arte en acuarela del segundo lote de escenas (2026-11-09): fondos 16:9 y hojas 3x2 de figuras
y objetos, con Nano Banana (Antigravity abierto) y la semilla de estilo del hexaflex.
Después:  python recortar.py

    python generar.py            # lo que falte
    python generar.py arenas-fondo hoja-figuras   # solo esos (rehace)
"""
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REF = AQUI.parent / "grids_v2" / "referencia-estilo.jpg"
SCRIPT = r"C:\Users\User\Documents\Varios\_agentes\generar-imagen-nanobanana.ps1"

ESTILO = ("Soft loose watercolor on white paper, delicate thin ink lines only where needed, muted palette of deep teal, "
          "slate blue-grey, sage, warm sand and soft ochre, refined editorial picture-book quality for adults. "
          "NOT cartoon, NOT cute, no thick black outlines, no flat vector colors, no saturated colors. No text, no letters, no numbers anywhere.")
MUJER = ("a young adult woman, dark hair in a loose low bun, loose off-white sweater, wide teal-grey trousers, "
         "face in profile or from behind with minimal features")
HOJA = ("a grid of 3 columns by 2 rows with six separate items on PURE WHITE background, each centered in its cell, "
        "nothing else in the cells (no floor, no ground shadow, no scenery), wide white gaps between cells, nothing crossing between cells. ")

PEDIDOS = {
    "arenas-fondo": ("16:9",
        "Cutaway cross-section side view, like a nature diagram, of a swampy clearing. The ground surface is a straight "
        "horizontal line at exactly 50% of the image height across the whole width. ABOVE the line: misty marsh landscape "
        "with reeds, cattails, a few dead trees and pale sky. BELOW the line, in the central 70% of the width: a deep pit of "
        "thick wet grey-brown quicksand shown in cross-section, dense mud with soft swirls, reaching the bottom edge. At the "
        "left and right 15%: firm dark earth with roots and stones in cross-section, and on top of the right bank firm grass "
        "with a fallen branch reaching towards the quicksand. No people, no animals, no objects in the quicksand."),
    "sushi-fondo": ("16:9",
        "Interior of a small conveyor-belt sushi bar seen straight on from the customer's side. A long straight metal conveyor "
        "belt runs horizontally across the whole image, its top surface at about 48% of the image height, completely EMPTY "
        "(no plates, no food). Behind the belt: the kitchen pass, on the far left a doorway with a short dark-blue noren "
        "curtain where plates come out, shelves with bowls, warm paper lamps. In front of the belt, the lower 40% of the image: "
        "a wide wooden counter top seen slightly from above, EMPTY except for a small soy sauce bottle at the far right. "
        "No people, no plates, no sushi."),
    "montanas-fondo": ("16:9",
        "Two neighboring rocky mountains facing each other across a misty valley. LEFT mountain (occupies the left 60% of the "
        "image): a tall steep rock face. On it a climbing route is subtly visible: from the bottom a line of ledges goes "
        "straight up to a big dark OVERHANG at mid-height that blocks the direct way; just below the overhang a narrow grassy "
        "ledge leads sideways to the LEFT and then an easy zig-zag path continues up to the summit, where a small flag stands. "
        "RIGHT mountain (right 30%): a lower peak with a flat ledge on top where a small person sits with binoculars looking "
        "at the left mountain. Pale sky, mist below. No climber on the left mountain."),
    "casa-fondo": ("16:9",
        "Cutaway dollhouse front view of a spacious two-storey house, wide composition: three rooms on the ground floor and "
        "three rooms upstairs, all rooms completely EMPTY (no furniture, no objects, no rugs), wooden floors, pale walls each "
        "in a slightly different soft tone, a window with soft light in every room, open doorways connecting the rooms, "
        "a staircase in the central ground-floor room, the open front door on the far left of the ground floor leading to a "
        "small garden path outside on the left. Roof above, grass below. No people."),
    "calle-fondo": ("16:9",
        "Side view of a quiet tree-lined city sidewalk in the morning. The sidewalk runs horizontally across the whole image; "
        "the walking line (where feet would be) is at 86% of the image height. Behind: muted shopfronts, a bakery window, a "
        "bench, doorways, three street trees. At the far right (last 20% of the width) the street CORNER: the sidewalk forks, "
        "one branch going up-right toward a sunlit park with a visible path, the other going down-right into a shaded narrow "
        "alley. A blank signpost stands at the corner. No people, no cars, no text."),
    "dial-fondo": ("16:9",
        "Front view close-up of the control panel of an old 1940s wooden radio, filling the whole frame. Upper 35%: a woven "
        "fabric speaker grille. Lower part: a brass panel with exactly TWO large identical round dial plates side by side, "
        "the left one centered at 30% of the width and the right one at 70% of the width, both centered at 62% of the height. "
        "Each dial plate is a brass ring with small tick marks all around and a plain EMPTY center (no knob, no pointer, no "
        "needle, no numbers). Warm worn wood around."),
    "hoja-figuras": ("3:2",
        "Character sheet: " + HOJA + "All figures are the SAME woman: " + MUJER + ", all at the same scale. "
        "Cell 1 (top-left): the woman standing upright, full body, front three-quarter view, struggling: both arms raised and "
        "flailing, body twisted, one knee lifting, alarmed. "
        "Cell 2 (top-center): the woman lying flat on her back, perfectly horizontal, strict side view, arms spread wide and "
        "relaxed, legs extended, eyes closed, calm, floating pose. "
        "Cell 3 (top-right): the woman seen from BEHIND, from the waist up, sitting upright with her forearms resting forward "
        "as on a counter. "
        "Cell 4 (bottom-left): the woman as a rock climber seen from behind, wearing a helmet and harness, arms reaching up, "
        "one leg bent, clinging to an invisible wall. "
        "Cell 5 (bottom-center): the woman standing, full body, side view facing LEFT, hands raised mid-argument as if "
        "arguing with someone floating in front of her, tense. "
        "Cell 6 (bottom-right): NOT the woman: a small soft grey cloud-shaped creature, the size of a cat, with two dot eyes, "
        "a small open talking mouth and two thin little arms gesturing; chatty and worried, drawn as loose watercolor wash."),
    "hoja-platos": ("3:2",
        "Prop sheet: " + HOJA + "Each item is a small round ceramic sushi plate seen from the side, slightly from above, all at "
        "the same scale, each carrying one thing: "
        "Cell 1: a small dark storm cloud with rain. Cell 2: a thorny bramble tangle. Cell 3: a tiny thundercloud with lightning. "
        "Cell 4: a cracked old alarm clock. Cell 5: a knotted ball of dark thread. "
        "Cell 6: two pieces of salmon nigiri sushi, appetizing."),
    "hoja-muebles": ("3:2",
        "Prop sheet: " + HOJA + "Six pieces of furniture, side-front view, all at the same scale: "
        "Cell 1: a worn old armchair with a torn cushion. Cell 2: a messy pile of cardboard moving boxes. "
        "Cell 3: a tall heavy dark wooden wardrobe. Cell 4: an elegant floor lamp with a warm shade. "
        "Cell 5: an old upright piano. Cell 6: a cracked standing mirror in a wooden frame."),
    "hoja-objetos": ("3:2",
        "Prop sheet: " + HOJA +
        "Cell 1: a single human hand and forearm in strict side view entering from the LEFT edge of its cell, index finger "
        "fully extended pointing to the RIGHT, the other fingers curled, relaxed. "
        "Cell 2: a rustic wooden farm gate, CLOSED, front view, with its post. "
        "Cell 3: the same rustic wooden farm gate swung wide OPEN, seen at an angle, with its post. "
        "Cell 4: a plain white ceramic cup with a small chip on the rim, side view. "
        "Cell 5: a round dark bakelite radio knob seen exactly from the front (a perfect circle), with a single cream pointer "
        "line going from the center straight UP. "
        "Cell 6: a vintage film camera on a wooden tripod, side view."),
}


def generar(nombre):
    formato, brief = PEDIDOS[nombre]
    salida = AQUI / (nombre + ".jpg")
    cmd = ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", SCRIPT,
           "-Descripcion", brief + " " + ESTILO, "-Salida", str(salida), "-Formato", formato, "-Paleta", "libre", "-EstiloRef", str(REF)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(nombre, "->", "ok" if salida.exists() else "SIN IMAGEN\n" + r.stdout[-800:] + r.stderr[-800:], flush=True)


if __name__ == "__main__":
    pedidos = sys.argv[1:]
    for n in PEDIDOS:
        if (pedidos and n in pedidos) or (not pedidos and not (AQUI / (n + ".jpg")).exists()):
            generar(n)
