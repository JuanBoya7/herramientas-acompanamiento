# -*- coding: utf-8 -*-
"""
Recorta la hoja de figuras del invitado (3x2 sobre blanco) en seis WebP con fondo
transparente (inundación del blanco desde los bordes de cada celda, borde suavizado),
y deja el fondo como JPEG de 1400 px. Imprime la proporción ancho/alto de cada figura,
que met-16-invitado-incomodo.parte usa en FIG.
"""
import json
from collections import deque
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

AQUI = Path(__file__).resolve().parent
IMGS = AQUI.parent
NOMBRES = ["invitado-anfitrion-empuja", "invitado-anfitrion-mesa", "invitado-anfitrion-camina",
           "invitado-toca", "invitado-rezonga", "invitado-ronda"]
ALTO = 300


def corte(perfil, centro, ventana):
    a, b = max(1, centro - ventana), min(len(perfil) - 2, centro + ventana)
    seg = perfil[a:b]
    return a + int(np.argmin(seg))


def transparente(celda):
    arr = np.asarray(celda.convert("RGB")).astype(np.int16)
    h, w, _ = arr.shape
    blanco = (arr.min(axis=2) > 228) & ((arr.max(axis=2) - arr.min(axis=2)) < 22)
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
    tinta = ~fuera
    # Borra las rayas verticales finas (la «puerta invisible» que el modelo insinúa junto a las
    # manos): columnas casi llenas de tinta en las que cada tramo horizontal mide <= 5 px.
    alto_col = tinta.sum(axis=0)
    for x in np.where(alto_col > h * 0.35)[0]:
        for y in np.where(tinta[:, x])[0]:
            a = x
            while a > 0 and tinta[y, a - 1]: a -= 1
            b = x
            while b < w - 1 and tinta[y, b + 1]: b += 1
            if b - a <= 5: tinta[y, a:b + 1] = False
    alfa = Image.fromarray(np.where(tinta, 255, 0).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    rgba = celda.convert("RGBA"); rgba.putalpha(alfa)
    return rgba


def main():
    hoja = Image.open(AQUI / "figuras.jpg").convert("RGB")
    W, H = hoja.size
    tinta = (np.asarray(hoja).min(axis=2) < 225)
    fila = corte(tinta.sum(axis=1), H // 2, H // 8)
    proporciones = {}
    i = 0
    for (y0, y1) in ((0, fila), (fila, H)):
        prof = tinta[y0:y1].sum(axis=0)
        c1, c2 = corte(prof, W // 3, W // 10), corte(prof, 2 * W // 3, W // 10)
        for (x0, x1) in ((0, c1), (c1, c2), (c2, W)):
            fig = transparente(hoja.crop((x0, y0, x1, y1)))
            caja = fig.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
            fig = fig.crop(caja)
            fig = fig.resize((max(1, round(fig.width * ALTO / fig.height)), ALTO), Image.LANCZOS)
            fig.save(IMGS / (NOMBRES[i] + ".webp"), "WEBP", quality=88, method=6)
            proporciones[NOMBRES[i]] = round(fig.width / fig.height, 3)
            i += 1
    fondo = Image.open(AQUI / "fondo.jpg").convert("RGB")
    fondo = fondo.resize((1400, round(1400 * fondo.height / fondo.width)), Image.LANCZOS)
    fondo.save(IMGS / "invitado-fiesta-acuarela.jpg", "JPEG", quality=84)
    print(json.dumps(proporciones, indent=1))
    print("fondo", fondo.size)


if __name__ == "__main__":
    main()
