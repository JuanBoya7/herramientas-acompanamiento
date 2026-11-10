# -*- coding: utf-8 -*-
"""
Prepara el arte del lote 2 para las partes:
- Fondos: recorte a 2:1 (caja dada en píxeles del original) y JPEG de 1400 px en ../<nombre>-acuarela.jpg.
  Con --rejilla deja además en _vista/ una copia de 700x350 con rejilla cada 50 px, para leer
  coordenadas del viewBox.
- Hojas 3x2: seis recortes con fondo transparente (WebP) en ../, con el alto pedido; imprime
  la proporción ancho/alto de cada uno (las usan las partes).

    python recortar.py [--rejilla]
"""
import json
import sys
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

AQUI = Path(__file__).resolve().parent
IMGS = AQUI.parent

# nombre de salida: (archivo, caja de recorte o None = todo)
FONDOS = {
    "arenas-acuarela": ("arenas-fondo.jpg", (45, 55, 1335, 700)),
    "sushi-acuarela": ("sushi-fondo.jpg", (88, 62, 1300, 668)),
    "montanas-acuarela": ("montanas-fondo.jpg", (0, 20, 1376, 708)),
    "casa-acuarela": ("casa-fondo.jpg", (0, 40, 1376, 728)),
    "calle-acuarela": ("calle-fondo.jpg", None),
    "dial-acuarela": ("dial-fondo.jpg", None),
    # lote 3 (OpenAI entrega 1536x1024, 3:2): dos recortadas a 2:1 y cuatro enteras (viewBox 700x467)
    "pero-acuarela": ("pero-fondo.jpg", (0, 110, 1536, 878)),
    "juicio-acuarela": ("juicio-fondo.jpg", (0, 200, 1536, 968)),
    "piloto-acuarela": ("piloto-fondo.jpg", None),
    "observador-acuarela": ("observador-fondo.jpg", None),
    "diana-acuarela": ("diana-fondo.jpg", None),
    "dulce-acuarela": ("dulce-fondo.jpg", None),
}
# hoja: [(nombre, alto en px)]
HOJAS = {
    "hoja-figuras.jpg": [("arenas-lucha", 320), ("arenas-tendida", 150), ("sushi-persona", 340),
                         ("montanas-escaladora", 220), ("paseo-discute", 320), ("paseo-mente", 200)],
    "hoja-platos.jpg": [("sushi-plato-%d" % i, 150) for i in range(1, 7)],
    "hoja-muebles.jpg": [("casa-sillon", 200), ("casa-cajas", 200), ("casa-armario", 240),
                         ("casa-lampara", 240), ("casa-piano", 200), ("casa-espejo", 240)],
    "hoja-objetos.jpg": [("trampa-mano", 200), ("pero-porton-cerrado", 240), ("pero-porton-abierto", 240),
                         ("juicio-taza", 200), ("dial-perilla", 240), ("juicio-camara", 260)],
}


# ajustes por recorte: "rayas" borra trazos horizontales finos (mesa insinuada), "mitad" toma media celda
# "blanco": umbral más alto para objetos muy claros (piel, loza), que si no se agujerean
OPCIONES = {"sushi-persona": {"rayas": True}, "paseo-discute": {"mitad": "der"},
            "trampa-mano": {"blanco": 247}, "juicio-taza": {"blanco": 247},
            # "huecos": además quita el blanco encerrado (entre las tablas de un portón)
            "pero-porton-cerrado": {"huecos": True}, "pero-porton-abierto": {"huecos": True}}


def sin_reticula(hoja):
    """Borra las líneas de cuadrícula que a veces dibuja el modelo entre celdas: filas o columnas
    con tinta en más del 60 % del largo y de no más de 6 px de grosor (un portón o un brazo
    horizontales también llenan filas, pero son gruesos)."""
    arr = np.asarray(hoja).copy()
    tinta = arr.min(axis=2) < 215
    H, W = tinta.shape

    def finas(marcadas):
        idx = np.where(marcadas)[0]
        grupos, ini = [], None
        for i, v in enumerate(idx):
            if ini is None: ini = v
            if i == len(idx) - 1 or idx[i + 1] != v + 1:
                if v - ini < 6: grupos.append((ini, v))
                ini = None
        return grupos

    # solo cerca de los cortes nominales (tercios del ancho, mitad del alto) y casi continuas
    cerca = lambda v, total, cortes: any(abs(v - total * c) < total * 0.08 for c in cortes)
    for a, b in finas(tinta.sum(axis=0) > H * 0.85):
        if cerca(a, W, (1 / 3, 2 / 3)): arr[:, max(0, a - 2):b + 3] = 255
    for a, b in finas(tinta.sum(axis=1) > W * 0.85):
        if cerca(a, H, (0.5,)): arr[max(0, a - 2):b + 3, :] = 255
    return Image.fromarray(arr)


def sin_rayas(fig):
    """Quita trazos horizontales finos y largos sobre blanco (<= 5 px de grosor, >= 30 px seguidos)."""
    a = np.asarray(fig).copy()
    alfa = a[:, :, 3] > 40
    h, w = alfa.shape
    grosor = np.zeros((h, w), np.int32)
    for x in range(w):
        run = 0
        for y in range(h):
            run = run + 1 if alfa[y, x] else 0
            grosor[y, x] = run
        for y in range(h - 2, -1, -1):
            if alfa[y, x] and alfa[y + 1, x]: grosor[y, x] = grosor[y + 1, x]
    fino = alfa & (grosor <= 5)
    for y in range(h):
        x = 0
        while x < w:
            if fino[y, x]:
                x1 = x
                while x1 < w and fino[y, x1]: x1 += 1
                if x1 - x >= 12: a[y, x:x1, 3] = 0
                x = x1
            else: x += 1
    return Image.fromarray(a)


def corte(perfil, centro, ventana):
    a, b = max(1, centro - ventana), min(len(perfil) - 2, centro + ventana)
    seg = perfil[a:b]
    idx = np.where(seg == seg.min())[0] + a
    return int(idx[np.argmin(np.abs(idx - centro))])     # el mínimo más cercano al corte nominal


def transparente(celda, umbral=226):
    arr = np.asarray(celda.convert("RGB")).astype(np.int16)
    h, w, _ = arr.shape
    blanco = (arr.min(axis=2) > umbral) & ((arr.max(axis=2) - arr.min(axis=2)) < 24)
    fuera = np.zeros((h, w), bool)
    q = deque()
    for x in range(w):
        for y in (0, h - 1):
            if blanco[y, x] and not fuera[y, x]: fuera[y, x] = True; q.append((y, x))
    for y in range(h):
        for x in (0, w - 1):
            if blanco[y, x] and not fuera[y, x]: fuera[y, x] = True; q.append((y, x))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            yy, xx = y + dy, x + dx
            if 0 <= yy < h and 0 <= xx < w and blanco[yy, xx] and not fuera[yy, xx]:
                fuera[yy, xx] = True; q.append((yy, xx))
    alfa = Image.fromarray(np.where(fuera, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = celda.convert("RGBA"); rgba.putalpha(alfa)
    return rgba


def hojas(solo=None):
    props = {}
    for archivo, celdas in HOJAS.items():
        if solo and solo not in archivo: continue
        p = AQUI / archivo
        if not p.exists():
            print("falta", archivo); continue
        hoja = sin_reticula(Image.open(p).convert("RGB"))
        W, H = hoja.size
        tinta = (np.asarray(hoja).min(axis=2) < 225)
        fila = corte(tinta.sum(axis=1), H // 2, H // 8)
        i = 0
        for (y0, y1) in ((0, fila), (fila, H)):
            prof = tinta[y0:y1].sum(axis=0)
            c1, c2 = corte(prof, W // 3, W // 10), corte(prof, 2 * W // 3, W // 10)
            for (x0, x1) in ((0, c1), (c1, c2), (c2, W)):
                nombre, alto = celdas[i]; i += 1
                op = OPCIONES.get(nombre, {})
                if op.get("mitad") == "der": x0 = (x0 + x1) // 2
                fig = transparente(hoja.crop((x0, y0, x1, y1)), op.get("blanco", 226))
                if op.get("rayas"): fig = sin_rayas(fig)
                if op.get("huecos"):
                    a = np.asarray(fig).copy(); rgb = a[:, :, :3].astype(np.int16)
                    a[(rgb.min(axis=2) > 232) & ((rgb.max(axis=2) - rgb.min(axis=2)) < 18), 3] = 0
                    fig = Image.fromarray(a)
                caja = fig.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
                fig = fig.crop(caja)
                fig = fig.resize((max(1, round(fig.width * alto / fig.height)), alto), Image.LANCZOS)
                fig.save(IMGS / (nombre + ".webp"), "WEBP", quality=88, method=6)
                props[nombre] = round(fig.width / fig.height, 3)
    print(json.dumps(props, indent=1))


def fondos(rejilla):
    vista = AQUI / "_vista"; vista.mkdir(exist_ok=True)
    for nombre, (archivo, caja) in FONDOS.items():
        p = AQUI / archivo
        if not p.exists():
            print("falta", archivo); continue
        im = Image.open(p).convert("RGB")
        if caja: im = im.crop(caja)
        w, h = im.size
        if caja and abs(w / h - 2) > 0.01:          # centra a 2:1
            if w / h > 2: d = (w - 2 * h) // 2; im = im.crop((d, 0, w - d, h))
            else: d = (h - w // 2) // 2; im = im.crop((0, d, w, h - d))
        if caja: im = im.resize((1400, 700), Image.LANCZOS)
        im.save(IMGS / (nombre + ".jpg"), "JPEG", quality=84)
        print(nombre, im.size)
        if rejilla:
            k = 700 / im.width
            v = im.resize((1400, round(im.height * k * 2)), Image.LANCZOS)
            d = ImageDraw.Draw(v)
            for x in range(0, 700, 50):
                d.line([(x * 2, 0), (x * 2, v.height)], fill=(255, 0, 0), width=1); d.text((x * 2 + 3, 2), str(x), fill=(255, 0, 0))
            for y in range(0, v.height // 2, 50):
                d.line([(0, y * 2), (v.width, y * 2)], fill=(0, 0, 255), width=1); d.text((3, y * 2 + 2), str(y), fill=(0, 0, 255))
            v.save(vista / (nombre + ".jpg"), quality=80)


if __name__ == "__main__":
    solo = next((a for a in sys.argv[1:] if not a.startswith("--")), None)   # p. ej. "objetos": solo esa hoja
    if not solo or solo == "fondos": fondos("--rejilla" in sys.argv)
    if solo != "fondos": hojas(solo)
