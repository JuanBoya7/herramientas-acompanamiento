# -*- coding: utf-8 -*-
"""
Recorte inteligente de las láminas 3x2 en 48 viñetas completas.

1. Busca la franja blanca horizontal real que separa las dos filas
   (perfil de proyección, cerca de la mitad).
2. En cada fila busca las dos franjas verticales blancas cerca de 1/3 y 2/3.
3. En cada celda toma la caja exacta del dibujo (píxeles no blancos),
   la amplía con margen y la centra en un lienzo CUADRADO blanco, sin cortar nada.
"""
import os
import numpy as np
from PIL import Image

HERR = r"C:\Users\User\Documents\Varios\FUAA\2026\2026-2\RUTA DE ATENCIÓN CLÍNICA\Recursos, ruta de atención\Herramientas"
GRIDS = os.path.join(HERR, "_fuente", "imagenes", "grids_v2")
OUT = os.path.join(HERR, "arte", "lecturas")
LADO = 560

MAPA = [
    ("grid-01-aceptacion-a.jpg", ['el-hoyo-y-la-pala','costo-de-la-lucha','el-poligrafo','soltar-la-cuerda','empujar-el-papel','limpio-y-sucio']),
    ("grid-02-aceptacion-b.jpg", ['dos-caras-moneda','trampa-china','invitado-incomodo','arenas-movedizas','hacer-espacio','soltar-el-ancla']),
    ("grid-03-defusion-a.jpg", ['soltar-el-anzuelo','palabra-repetida','hojas-en-el-arroyo','manos-como-pensamientos','pasear-la-mente','pero-por-y']),
    ("grid-04-defusion-b.jpg", ['cinta-de-sushi','radio-mental','nombrar-la-historia','agradecer-a-la-mente','voces-de-dibujos','estoy-teniendo-el-pensamiento']),
    ("grid-05-presente.jpg", ['cinco-sentidos','aterrizar-en-el-cuerpo','piloto-automatico','hecho-o-juicio','pausa-de-tres-minutos','presencia-en-sesion']),
    ("grid-06-yo-contexto.jpg", ['tablero-de-ajedrez','cielo-y-clima','quien-lleva-los-globos','escenario-y-butaca','observador-en-el-tiempo','dos-montanas']),
    ("grid-07-valores.jpg", ['casa-y-muebles','brujula-de-valores','jardin-de-valores','ochenta-anos','diana-de-valores','punto-dulce']),
    ("grid-08-accion.jpg", ['pasajeros-del-autobus','punto-de-eleccion','paso-mas-pequeno','vasija-de-barro','dial-de-disposicion','cruzar-el-pantano']),
]


def mascara(arr):
    # "tinta": cualquier canal claramente por debajo del blanco
    return (arr.min(axis=2) < 232)


def mejor_corte(perfil, centro, ventana):
    """Índice dentro de [centro-ventana, centro+ventana] con menos tinta (centro de la franja más blanca)."""
    a, b = max(1, centro - ventana), min(len(perfil) - 2, centro + ventana)
    seg = perfil[a:b]
    minimo = seg.min()
    idx = np.where(seg <= minimo + max(1, seg.max() * 0.01))[0]
    # agrupa índices consecutivos y elige la franja más ancha
    grupos, ini = [], idx[0]
    for i, j in zip(idx, idx[1:]):
        if j != i + 1:
            grupos.append((ini, i)); ini = j
    grupos.append((ini, idx[-1]))
    g = max(grupos, key=lambda t: t[1] - t[0])
    return a + (g[0] + g[1]) // 2


def caja(m):
    ys, xs = np.where(m)
    if len(xs) == 0:
        return None
    # descarta motas sueltas: percentiles en vez de extremos absolutos
    x0, x1 = np.percentile(xs, 0.2), np.percentile(xs, 99.8)
    y0, y1 = np.percentile(ys, 0.2), np.percentile(ys, 99.8)
    return int(x0), int(y0), int(x1), int(y1)


def procesar(nombre, slugs):
    img = Image.open(os.path.join(GRIDS, nombre)).convert("RGB")
    arr = np.asarray(img)
    m = mascara(arr)
    h, w = m.shape
    fila = mejor_corte(m.sum(axis=1), h // 2, int(h * 0.12))
    filas = [(0, fila), (fila, h)]
    k = 0
    for (y0, y1) in filas:
        perfil = m[y0:y1].sum(axis=0)
        c1 = mejor_corte(perfil, w // 3, int(w * 0.07))
        c2 = mejor_corte(perfil, 2 * w // 3, int(w * 0.07))
        cols = [(0, c1), (c1, c2), (c2, w)]
        for (x0, x1) in cols:
            sub = m[y0:y1, x0:x1]
            bb = caja(sub)
            slug = slugs[k]; k += 1
            if bb is None:
                print("  ! celda vacía", slug); continue
            bx0, by0, bx1, by1 = bb
            bx0 += x0; bx1 += x0; by0 += y0; by1 += y0
            bw, bh = bx1 - bx0, by1 - by0
            lado = int(max(bw, bh) * 1.14)          # margen de 7% por lado
            cx, cy = (bx0 + bx1) // 2, (by0 + by1) // 2
            lienzo = Image.new("RGB", (lado, lado), (255, 255, 255))
            recorte = img.crop((bx0, by0, bx1, by1))
            # máscara para pegar solo esta celda (evita colar trozos del vecino)
            mm = Image.fromarray((m[by0:by1, bx0:bx1] * 255).astype("uint8")).convert("L")
            lienzo.paste(recorte, ((lado - bw) // 2, (lado - bh) // 2))
            final = lienzo.resize((LADO, LADO), Image.Resampling.LANCZOS)
            final.save(os.path.join(OUT, slug + ".webp"), "WEBP", quality=88, method=6)
            print(f"  {slug:32s} caja {bw}x{bh}")
    return k


total = 0
for n, s in MAPA:
    print(n)
    total += procesar(n, s)
print("Viñetas:", total)
