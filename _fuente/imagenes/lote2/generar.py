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
    "pero-fondo": ("16:9",
        "Side view of a country landscape with a dirt path running horizontally across the whole image; the walking line of the "
        "path is at 80% of the image height. LEFT half: a shaded meadow under a soft grey overcast sky. RIGHT 40%: the path "
        "climbs gently toward a sunlit green hill with a small house and warm golden light. At exactly 55% of the width a low "
        "rustic wooden fence crosses the landscape from the foreground to the background, with an EMPTY opening where the path "
        "passes: two sturdy fence posts on each side of the path and NO gate between them. No people, no animals, no gate."),
    "juicio-fondo": ("16:9",
        "A quiet room seen straight on: a plain wooden table top occupying the lower 38% of the image, seen slightly from above, "
        "completely EMPTY (nothing on it). Behind it a soft pale plaster wall, a window on the far left letting in morning light, "
        "a faint shadow of leaves on the wall. No objects on the table, no people."),
    "piloto-fondo": ("16:9",
        "Morning in a small home kitchen, side view. On the LEFT third: " + MUJER + ", standing by the counter next to a window, "
        "holding a steaming cup with both hands, shoulders relaxed. On the counter: a kettle, a sink with a thin stream of water "
        "running from the tap, a plant on the window sill, a wooden floor under her bare feet. The RIGHT half of the image is a "
        "calm pale wall with soft light and very few details. Warm morning light."),
    "observador-fondo": ("16:9",
        "Wide landscape: a path crossing a meadow from left to right toward ONE large solitary tree on the horizon at 86% of the "
        "width. Three figures seen from BEHIND stand along the path, evenly spaced at 18%, 40% and 62% of the width, all looking "
        "toward the tree, with their feet at 82% of the image height: a little girl about 8 years old, a teenage girl, and "
        + MUJER + " -- the same person at three ages, same dark hair. Pale open sky, soft hills. Nothing else."),
    "diana-fondo": ("16:9",
        "Front view of a large round wooden target board leaning against a big tree trunk in a garden. The target is a perfect "
        "circle centered exactly in the middle of the image, its diameter 86% of the image height. It has a small center disc and "
        "SEVEN concentric rings, and is divided by one vertical and one horizontal line into four equal quadrants, each quadrant "
        "tinted with a different muted color: top-left terracotta, top-right slate blue, bottom-left ochre, bottom-right sage "
        "green; the tints get lighter toward the rim. NO darts, NO pins, no numbers. Grass and soft foliage at the sides."),
    "dulce-fondo": ("16:9",
        "A wooden porch at sunset. On the LEFT third: " + MUJER + ", sitting on the porch steps holding a warm cup, eyes closed, "
        "a soft smile, body turned toward the right. The RIGHT two thirds of the image: a wide, luminous, almost empty sunset "
        "sky over a calm sea, glowing softly in warm apricot and pale teal, with no clouds and no objects (empty space)."),
    # ---------- lote 4 (2026-11-10): rework de diez metáforas antiguas; todo en 3:2
    "tablero-fondo": ("3:2",
        "Top-down view, seen almost straight from above, of an EMPTY wooden chessboard with 8 by 8 squares in cream and "
        "soft slate-teal, lying on a pale wooden table. The board is a perfect square centered in the image and its side is "
        "84% of the image height. No pieces at all. Soft light, a little of the table visible at left and right."),
    "poligrafo-fondo": ("3:2",
        "Side view of a quiet examination room. On the LEFT third: " + MUJER + ", sitting stiffly in a wooden chair, thin wires "
        "from her fingertips and a strap around her chest going to an old vintage polygraph machine on a desk at 40% of the width. "
        "From the machine a very wide strip of BLANK cream chart paper unrolls to the right and fills the right 55% of the "
        "image like a long empty scroll (completely blank, no lines drawn on it). Soft grey-blue wall."),
    "radio-fondo": ("3:2",
        "A cozy study room seen straight on. On the LEFT: a wooden shelf at mid height holding an old vintage radio with a "
        "round speaker and two knobs. On the RIGHT two thirds: a wooden desk under a window with morning light, with an open "
        "notebook, a cup and a small plant; an empty chair pushed back. No people."),
    "interruptor-fondo": ("3:2",
        "A plain pale plaster wall of an old house seen straight on, with a wooden wainscot along the bottom fifth. On the "
        "RIGHT side, centered at 80% of the width and 45% of the height, a large antique brass switch plate with an EMPTY slot "
        "in the middle (no lever, no toggle). The rest of the wall is empty and softly lit from a window out of frame on the left."),
    "escenario-fondo": ("3:2",
        "A small old theater seen from the back of the stalls. Heavy teal velvet curtains open at both sides, an EMPTY wooden "
        "stage floor occupying the middle of the image (stage floor line at 62% of the image height), dark backdrop. In the "
        "foreground at the bottom: the backs of three rows of empty velvet seats, and in the nearest row, slightly right of "
        "center, " + MUJER + " seen from behind, sitting and watching the stage. No one on stage, no spotlight."),
    "moneda-fondo": ("3:2",
        "A worn wooden table top seen from above at a slight angle, filling the whole image, softly lit by a window from the "
        "left with a faint shadow of leaves; completely EMPTY, nothing on it."),
    "ochenta-fondo": ("3:2",
        "An evening garden party seen from the front. A long table with a white cloth across the middle of the image, a simple "
        "cake with candles in the center, glasses and plates, warm string lights between the trees above. At the center behind "
        "the table sits an elderly woman with white hair in a loose bun and an off-white sweater, smiling. On each side of her, "
        "behind the table, there are three EMPTY wooden chairs (six empty chairs in total). No other people."),
    "palabra-fondo": ("3:2",
        "A kitchen table seen straight on, slightly from above: on the LEFT third a glass of milk and a milk carton with a "
        "blank label. Behind, a soft pale wall filling the RIGHT two thirds, empty and softly lit (empty space). No people, no text."),
    "papel-fondo": ("3:2",
        "A bright living room seen straight on: a wooden bench or simple sofa centered at the bottom (its seat at 72% of the "
        "image height), EMPTY. Behind it a large window with plants on the sill, a bookshelf, a framed family photo, a guitar "
        "leaning on the wall: a warm lived-in room. No people."),
    "anzuelo-fondo": ("3:2",
        "Underwater cross-section of a calm lake: the water surface is a wavy horizontal line at 16% of the image height with "
        "pale sky above; below, clear teal-green water getting deeper toward the bottom, a few water plants and stones on the "
        "lake bed at the bottom edge, soft light rays. No fish, no hooks, no boats."),
    "hoja-ajedrez": ("3:2",
        "Prop sheet: " + HOJA + "Six wooden chess pieces seen from above at a slight three-quarter angle, all at the same "
        "scale: Cell 1: a cream-white pawn. Cell 2: a cream-white knight. Cell 3: a cream-white queen. "
        "Cell 4: a dark slate-black pawn. Cell 5: a dark slate-black knight. Cell 6: a dark slate-black queen."),
    "hoja-actores": ("3:2",
        "Character sheet: " + HOJA + "Six different stage characters, full body, standing, front view, all at the same scale, "
        "like actors in a small theater: Cell 1: a figure in a dark hooded cloak shouting with arms raised, dramatic. "
        "Cell 2: a stern figure pointing a finger, in a grey coat. Cell 3: a small hunched worried figure wringing hands. "
        "Cell 4: a calm woman with a watering can and an apron. Cell 5: a man holding a guitar, relaxed. "
        "Cell 6: two friends arm in arm, laughing."),
    "hoja-invitados": ("3:2",
        "Character sheet: " + HOJA + "Six different party guests, each shown from the waist up, sitting, raising a glass in a "
        "toast, front view, all at the same scale: Cell 1: a middle-aged woman with short hair. Cell 2: a young man with "
        "glasses. Cell 3: an elderly man with a cardigan. Cell 4: a young woman with curly hair. Cell 5: a child holding a "
        "cup with both hands. Cell 6: a middle-aged man with a beard."),
    "hoja-varios": ("3:2",
        "Prop sheet: " + HOJA +
        "Cell 1: an old bronze coin seen exactly from the front (a perfect circle), engraved with a rain cloud and falling drops. "
        "Cell 2: the reverse of the same bronze coin, seen exactly from the front (a perfect circle), engraved with a heart "
        "and sprouting leaves. "
        "Cell 3: a calm lake fish (trout) in strict side view, swimming to the right. "
        "Cell 4: " + MUJER + ", sitting, full body, side view facing RIGHT, arms rigid and fully stretched forward, straining "
        "to push a sheet of handwritten paper away from her. "
        "Cell 5: the same woman sitting, full body, front three-quarter view, relaxed, a sheet of handwritten paper resting "
        "on her lap, hands open on her knees, looking ahead. "
        "Cell 6: an antique brass toggle switch lever seen from the front, a short brass handle with a round ball tip, "
        "pointing straight UP."),
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


PUERTA = "C:/Users/User/Documents/Varios/_agentes/generar-imagen.py"


def generar(nombre):
    """Regla del docente: Nano Banana primero hasta agotar la cuota; OpenAI solo de contingencia."""
    formato, brief = PEDIDOS[nombre]
    salida = AQUI / (nombre + ".jpg")
    cmd = [sys.executable, PUERTA, "--descripcion", brief + " " + ESTILO, "--salida", str(salida), "--formato", formato]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(nombre, "->", (r.stdout.strip().splitlines() or ["?"])[-1][:200], flush=True)


if __name__ == "__main__":
    pedidos = sys.argv[1:]
    for n in PEDIDOS:
        if (pedidos and n in pedidos) or (not pedidos and not (AQUI / (n + ".jpg")).exists()):
            generar(n)
