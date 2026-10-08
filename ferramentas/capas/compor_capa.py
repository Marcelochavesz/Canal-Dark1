#!/usr/bin/env python3
"""Compõe uma capa de 1280x720 no estilo "faixa": fundo, faixa colorida inclinada e texto em 3 linhas.

Uso:
    python3 compor_capa.py --linha1 "SEU" --palavra "TETO" --linha3 "FINANCEIRO" \
        --simbolo teto --paleta padrao --saida capa.png

O fundo pode ser uma imagem sua (--fundo caminho.jpg) ou uma arte provisória (--simbolo).
Fonte: Anton, licença SIL Open Font License (ver fontes/Anton-OFL.txt).
"""
import argparse
import math
import os
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

W, H = 1280, 720
PASTA = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(PASTA, "fontes", "Anton-Regular.ttf")
INCLINACAO = 12  # graus, como em itálico

PALETAS = {
    # cor da faixa, cor da palavra grande, cor das linhas pequenas, contorno
    "padrao": dict(faixa=(230, 62, 28), palavra=(255, 255, 255), linhas=(255, 255, 255), contorno=(0, 0, 0)),
    "propria": dict(faixa=(14, 90, 102), palavra=(255, 200, 61), linhas=(255, 255, 255), contorno=(0, 0, 0)),
}


def fonte(tamanho):
    return ImageFont.truetype(FONTE, tamanho)


def ajustar(texto, largura_max, inicio, minimo=30):
    """Maior tamanho de fonte, a partir de `inicio`, em que o texto cabe em `largura_max`."""
    t = inicio
    while t > minimo:
        x0, _, x1, _ = fonte(t).getbbox(texto)
        if x1 - x0 <= largura_max:
            break
        t -= 2
    return t


def inclinar(img, graus=INCLINACAO):
    """Inclina a imagem para a direita, no topo, como um itálico sintético."""
    k = math.tan(math.radians(graus))
    w, h = img.size
    extra = int(k * h)
    saida = Image.new("RGBA", (w + extra, h), (0, 0, 0, 0))
    base = saida.copy()
    base.paste(img, (0, 0))
    return base.transform(saida.size, Image.AFFINE, (1, k, -k * h, 0, 1, 0), resample=Image.BICUBIC)


def linha(texto, tamanho, cor, contorno, espessura):
    """Desenha uma linha de texto com contorno e a inclina. Devolve uma imagem RGBA."""
    f = fonte(tamanho)
    x0, y0, x1, y1 = f.getbbox(texto, stroke_width=espessura)
    pad = espessura + 6
    img = Image.new("RGBA", (x1 - x0 + 2 * pad, y1 - y0 + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # sombra
    d.text((pad - x0 + 4, pad - y0 + 6), texto, font=f, fill=(0, 0, 0, 160), stroke_width=espessura, stroke_fill=(0, 0, 0, 160))
    d.text((pad - x0, pad - y0), texto, font=f, fill=cor, stroke_width=espessura, stroke_fill=contorno)
    return inclinar(img)


def cobrir(img, w, h):
    """Redimensiona e corta a imagem para cobrir w x h."""
    r = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def vinheta(img, forca=0.55):
    mascara = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mascara)
    d.ellipse((-W * 0.25, -H * 0.35, W * 1.25, H * 1.35), fill=255)
    mascara = mascara.filter(ImageFilter.GaussianBlur(120))
    escuro = Image.new("RGB", (W, H), (0, 0, 0))
    return Image.composite(img, Image.blend(img, escuro, forca), mascara)


# ---------------------------------------------------------------- artes provisórias
def gradiente(cima, baixo):
    img = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        d.line([(0, y), (W, y)], fill=tuple(int(cima[i] + (baixo[i] - cima[i]) * t) for i in range(3)))
    return img


def brilho(img, centro, raio, cor, forca=1.0):
    camada = Image.new("RGB", (W, H), (0, 0, 0))
    d = ImageDraw.Draw(camada)
    for r in range(raio, 0, -8):
        t = 1 - r / raio
        c = tuple(int(v * (t ** 1.6) * forca) for v in cor)
        d.ellipse((centro[0] - r, centro[1] - r, centro[0] + r, centro[1] + r), fill=c)
    camada = camada.filter(ImageFilter.GaussianBlur(25))
    from PIL import ImageChops
    return ImageChops.add(img, camada)


def arte(simbolo, lado_texto):
    """Arte provisória na metade oposta ao texto. Substituir por imagem gerada na versão final."""
    cx = 330 if lado_texto == "dir" else 950
    fundo = gradiente((8, 18, 34), (22, 40, 58))
    if simbolo == "teto":
        fundo = brilho(fundo, (cx, 120), 420, (255, 190, 80), 0.9)
        d = ImageDraw.Draw(fundo, "RGBA")
        d.polygon([(cx - 330, 235), (cx + 330, 235), (cx + 330, 285), (cx - 330, 285)], fill=(170, 210, 235, 70), outline=(210, 235, 250, 170))
        for dx in (-220, -60, 110, 260):
            d.line([(cx + dx, 235), (cx + dx - 70, 285)], fill=(230, 245, 255, 120), width=3)
        # silhueta
        d.ellipse((cx - 42, 400, cx + 42, 484), fill=(6, 10, 18, 255))
        d.rounded_rectangle((cx - 90, 490, cx + 90, 720), radius=70, fill=(6, 10, 18, 255))
        d.line([(cx, 395), (cx, 292)], fill=(255, 215, 130, 150), width=3)
    elif simbolo == "termostato":
        fundo = brilho(fundo, (cx, 360), 380, (255, 170, 70), 0.55)
        d = ImageDraw.Draw(fundo, "RGBA")
        r = 215
        d.ellipse((cx - r - 18, 360 - r - 18, cx + r + 18, 360 + r + 18), fill=(40, 50, 62, 255), outline=(200, 205, 212, 255), width=6)
        d.ellipse((cx - r, 360 - r, cx + r, 360 + r), fill=(12, 20, 30, 255))
        for i in range(0, 270, 18):
            a = math.radians(135 + i)
            x0, y0 = cx + (r - 14) * math.cos(a), 360 + (r - 14) * math.sin(a)
            x1, y1 = cx + (r - 44) * math.cos(a), 360 + (r - 44) * math.sin(a)
            d.line([(x0, y0), (x1, y1)], fill=(255, 190, 80, 255) if i % 54 == 0 else (150, 160, 175, 255), width=7 if i % 54 == 0 else 4)
        a = math.radians(135 + 150)
        d.line([(cx, 360), (cx + (r - 70) * math.cos(a), 360 + (r - 70) * math.sin(a))], fill=(255, 90, 50, 255), width=10)
        d.ellipse((cx - 16, 344, cx + 16, 376), fill=(230, 230, 235, 255))
    elif simbolo == "caderno":
        fundo = brilho(fundo, (cx, 300), 400, (255, 175, 80), 0.7)
        d = ImageDraw.Draw(fundo, "RGBA")
        d.rounded_rectangle((cx - 250, 130, cx + 250, 600), radius=14, fill=(238, 232, 218, 255), outline=(120, 100, 80, 255), width=4)
        d.line([(cx - 250, 205), (cx + 250, 205)], fill=(170, 160, 145, 255), width=3)
        for i in range(7):
            x = cx - 215 + i * 62
            d.rounded_rectangle((x, 250, x + 48, 298), radius=6, outline=(60, 60, 70, 255), width=4, fill=(255, 255, 255, 255) if i else (120, 200, 140, 255))
        for y in (360, 410, 460, 510):
            d.line([(cx - 215, y), (cx + 215, y)], fill=(185, 178, 165, 255), width=3)
        d.polygon([(cx + 180, 470), (cx + 330, 330), (cx + 345, 345), (cx + 195, 485)], fill=(30, 36, 50, 255))
    elif simbolo == "porta":
        fundo = brilho(fundo, (cx, 330), 460, (255, 200, 90), 1.0)
        d = ImageDraw.Draw(fundo, "RGBA")
        for a in range(-60, 61, 12):
            x2 = cx + 520 * math.tan(math.radians(a))
            d.polygon([(cx - 8, 330), (cx + 8, 330), (x2 + 18, 0), (x2 - 18, 0)], fill=(255, 225, 140, 40))
        d.rounded_rectangle((cx - 120, 150, cx + 120, 640), radius=10, fill=(255, 232, 160, 255), outline=(255, 250, 220, 255), width=6)
        d.ellipse((cx - 28, 440, cx + 28, 496), fill=(6, 10, 18, 255))
        d.rounded_rectangle((cx - 40, 490, cx + 40, 640), radius=30, fill=(6, 10, 18, 255))
        for i, (dx, dy, rr) in enumerate([(-190, 560, 26), (-130, 620, 20), (170, 585, 28), (220, 640, 20), (-230, 480, 18), (230, 500, 18)]):
            d.ellipse((cx + dx - rr, dy - rr, cx + dx + rr, dy + rr), fill=(255, 200, 60, 255), outline=(200, 140, 20, 255), width=3)
            d.ellipse((cx + dx - rr / 2, dy - rr / 2, cx + dx + rr / 2, dy + rr / 2), outline=(255, 235, 150, 255), width=3)
    else:
        raise SystemExit(f"símbolo desconhecido: {simbolo}. Use teto, termostato, caderno ou porta.")
    return fundo


# ---------------------------------------------------------------- composição
def compor(args):
    pal = PALETAS[args.paleta]
    if args.fundo:
        base = vinheta(ImageEnhance.Brightness(cobrir(Image.open(args.fundo).convert("RGB"), W, H)).enhance(0.8))
    else:
        base = arte(args.simbolo, args.lado)
    cena = base.convert("RGBA")

    bloco_l = 610
    x_centro = 940 if args.lado == "dir" else 340
    esp = 8
    l1 = linha(args.linha1, ajustar(args.linha1, bloco_l - 40, 96), pal["linhas"], pal["contorno"], esp - 2) if args.linha1 else None
    l3 = linha(args.linha3, ajustar(args.linha3, bloco_l - 40, 96), pal["linhas"], pal["contorno"], esp - 2) if args.linha3 else None
    pw = linha(args.palavra, ajustar(args.palavra, bloco_l - 70, 230), pal["palavra"], pal["contorno"], esp + 2)

    folga = 22
    alturas = [i.height for i in (l1, pw, l3) if i is not None]
    total = sum(alturas) + folga * (len(alturas) + 1)
    y = (H - total) // 2 + folga

    faixa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(faixa)
    k = math.tan(math.radians(INCLINACAO))
    cobertura = []
    if l1 is not None:
        cobertura.append((l1, y)); y += l1.height + folga
    fy0 = y - 6
    fy1 = y + pw.height + 6
    largura_faixa = max(pw.width + 90, bloco_l)
    x0, x1 = x_centro - largura_faixa // 2, x_centro + largura_faixa // 2
    desloc = k * (fy1 - fy0) / 2
    fd.polygon([(x0 + desloc + 10, fy0 + 10), (x1 + desloc + 10, fy0 + 10), (x1 - desloc + 10, fy1 + 10), (x0 - desloc + 10, fy1 + 10)], fill=(0, 0, 0, 120))
    fd.polygon([(x0 + desloc, fy0), (x1 + desloc, fy0), (x1 - desloc, fy1), (x0 - desloc, fy1)], fill=pal["faixa"] + (255,))
    cobertura.append((pw, y)); y += pw.height + folga
    if l3 is not None:
        cobertura.append((l3, y))
    cena = Image.alpha_composite(cena, faixa)
    for img, yy in cobertura:
        cena.alpha_composite(img, (int(x_centro - img.width / 2), int(yy)))

    if args.marca:
        d = ImageDraw.Draw(cena, "RGBA")
        f = fonte(30)
        x0m, y0m, x1m, y1m = f.getbbox(args.marca)
        bx = 28 if args.lado == "dir" else W - (x1m - x0m) - 68
        d.rounded_rectangle((bx, H - 78, bx + (x1m - x0m) + 40, H - 28), radius=10, fill=(0, 0, 0, 175))
        d.text((bx + 20, H - 74), args.marca, font=f, fill=(255, 255, 255, 230))
    return cena.convert("RGB")


def main():
    p = argparse.ArgumentParser(description="Compõe uma capa 1280x720 no estilo faixa.")
    p.add_argument("--linha1", default="", help="linha pequena de cima")
    p.add_argument("--palavra", required=True, help="palavra ou expressão grande, sobre a faixa")
    p.add_argument("--linha3", default="", help="linha pequena de baixo")
    p.add_argument("--paleta", choices=sorted(PALETAS), default="padrao")
    p.add_argument("--lado", choices=["dir", "esq"], default="dir", help="lado do texto")
    p.add_argument("--fundo", help="imagem de fundo (JPG ou PNG)")
    p.add_argument("--simbolo", choices=["teto", "termostato", "caderno", "porta"], default="teto", help="arte provisória, se não houver --fundo")
    p.add_argument("--marca", default="", help="texto pequeno de marca no canto, por exemplo o nome do canal")
    p.add_argument("--saida", required=True)
    a = p.parse_args()
    if not os.path.exists(FONTE):
        sys.exit(f"fonte não encontrada: {FONTE}")
    compor(a).save(a.saida, quality=92)
    print("capa salva em", a.saida)


if __name__ == "__main__":
    main()
