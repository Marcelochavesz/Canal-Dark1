#!/usr/bin/env python3
"""Compõe capas de 1280x720 com a autoridade em destaque, em três modelos de teste A/B.

Modelos:
    faixa    autoridade à esquerda, símbolo à direita, texto em 3 linhas com faixa colorida (padrão tipo Lewis Howes)
    retrato  autoridade grande em preto e branco, texto em comando com sublinhado e assinatura (padrão tipo Napoleon Hill)
    prazo    autoridade à direita, palavra, número ou prazo gigante com brilho à esquerda (padrão de "em 30 dias")

Uso:
    python3 compor_capa.py --modelo faixa --autoridade foto_proctor.png \
        --linha1 "SEU" --palavra "TETO" --linha3 "FINANCEIRO" --simbolo teto --saida capa.png

A foto da autoridade deve ter licença ou autorização de uso. Use --autoridade placeholder para testar o layout.
Fontes: Anton e Dancing Script, ambas SIL Open Font License (ver pasta fontes).
"""
import argparse
import math
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

W, H = 1280, 720
PASTA = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(PASTA, "fontes", "Anton-Regular.ttf")
ASSINATURA = os.path.join(PASTA, "fontes", "DancingScript-Bold.ttf")
INCLINACAO = 12  # graus, como em itálico

# Identidade do canal. "marca" é o padrão; "vermelha" é variação de teste da faixa.
PALETAS = {
    "marca": dict(fundo=((8, 18, 34), (22, 40, 58)), faixa=(14, 90, 102), destaque=(255, 200, 61),
                  texto=(255, 255, 255), acento=(230, 62, 28), contorno=(0, 0, 0)),
    "vermelha": dict(fundo=((8, 18, 34), (22, 40, 58)), faixa=(230, 62, 28), destaque=(255, 255, 255),
                     texto=(255, 255, 255), acento=(255, 200, 61), contorno=(0, 0, 0)),
}


# ---------------------------------------------------------------- texto
def fonte(tamanho, caminho=None):
    return ImageFont.truetype(caminho or FONTE, tamanho)


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
    base = Image.new("RGBA", (w + extra, h), (0, 0, 0, 0))
    base.paste(img, (0, 0))
    return base.transform(base.size, Image.AFFINE, (1, k, -k * h, 0, 1, 0), resample=Image.BICUBIC)


def linha(texto, tamanho, cor, contorno, espessura, brilho=None):
    """Linha de texto com contorno, sombra e, se pedido, brilho. Devolve uma imagem RGBA inclinada."""
    f = fonte(tamanho)
    x0, y0, x1, y1 = f.getbbox(texto, stroke_width=espessura)
    pad = espessura + (30 if brilho else 6)
    img = Image.new("RGBA", (x1 - x0 + 2 * pad, y1 - y0 + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((pad - x0 + 4, pad - y0 + 6), texto, font=f, fill=(0, 0, 0, 160), stroke_width=espessura, stroke_fill=(0, 0, 0, 160))
    d.text((pad - x0, pad - y0), texto, font=f, fill=cor, stroke_width=espessura, stroke_fill=contorno)
    if brilho:
        halo = Image.new("RGBA", img.size, brilho + (0,))
        halo.putalpha(img.split()[3].filter(ImageFilter.GaussianBlur(14)).point(lambda v: min(255, v * 2)))
        img = Image.alpha_composite(halo, img)
    return inclinar(img)


def assinatura(texto, tamanho, cor):
    f = fonte(tamanho, ASSINATURA)
    x0, y0, x1, y1 = f.getbbox(texto)
    img = Image.new("RGBA", (x1 - x0 + 20, y1 - y0 + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.text((12 - x0, 12 - y0), texto, font=f, fill=(0, 0, 0, 180))
    d.text((10 - x0, 10 - y0), texto, font=f, fill=cor)
    return img


# ---------------------------------------------------------------- fundo e símbolos
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
        d.ellipse((centro[0] - r, centro[1] - r, centro[0] + r, centro[1] + r), fill=tuple(int(v * (t ** 1.6) * forca) for v in cor))
    return ImageChops.add(img, camada.filter(ImageFilter.GaussianBlur(25)))


def cobrir(img, w, h):
    r = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * r) + 1, int(img.height * r) + 1), Image.LANCZOS)
    x, y = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def desenhar_simbolo(nome, cx, cy, s):
    """Símbolo sobre uma camada transparente, centrado em (cx, cy) e na escala s."""
    camada = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    if nome == "teto":
        d.polygon([(cx - 330 * s, cy - 25 * s), (cx + 330 * s, cy - 25 * s), (cx + 330 * s, cy + 25 * s), (cx - 330 * s, cy + 25 * s)],
                  fill=(170, 210, 235, 90), outline=(215, 238, 252, 200))
        for dx in (-220, -60, 110, 260):
            d.line([(cx + dx * s, cy - 25 * s), (cx + (dx - 70) * s, cy + 25 * s)], fill=(235, 247, 255, 150), width=max(2, int(3 * s)))
    elif nome == "termostato":
        r = 215 * s
        d.ellipse((cx - r - 18 * s, cy - r - 18 * s, cx + r + 18 * s, cy + r + 18 * s), fill=(40, 50, 62, 255), outline=(200, 205, 212, 255), width=max(2, int(6 * s)))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(12, 20, 30, 255))
        for i in range(0, 270, 18):
            a = math.radians(135 + i)
            principal = i % 54 == 0
            d.line([(cx + (r - 14 * s) * math.cos(a), cy + (r - 14 * s) * math.sin(a)), (cx + (r - 44 * s) * math.cos(a), cy + (r - 44 * s) * math.sin(a))],
                   fill=(255, 190, 80, 255) if principal else (150, 160, 175, 255), width=max(2, int((7 if principal else 4) * s)))
        a = math.radians(285)
        d.line([(cx, cy), (cx + (r - 70 * s) * math.cos(a), cy + (r - 70 * s) * math.sin(a))], fill=(255, 90, 50, 255), width=max(3, int(10 * s)))
        d.ellipse((cx - 16 * s, cy - 16 * s, cx + 16 * s, cy + 16 * s), fill=(230, 230, 235, 255))
    elif nome == "caderno":
        d.rounded_rectangle((cx - 250 * s, cy - 235 * s, cx + 250 * s, cy + 235 * s), radius=int(14 * s), fill=(238, 232, 218, 255), outline=(120, 100, 80, 255), width=max(2, int(4 * s)))
        d.line([(cx - 250 * s, cy - 160 * s), (cx + 250 * s, cy - 160 * s)], fill=(170, 160, 145, 255), width=max(2, int(3 * s)))
        for i in range(7):
            x = cx - 215 * s + i * 62 * s
            d.rounded_rectangle((x, cy - 115 * s, x + 48 * s, cy - 67 * s), radius=int(6 * s), outline=(60, 60, 70, 255), width=max(2, int(4 * s)),
                                fill=(255, 255, 255, 255) if i else (120, 200, 140, 255))
        for dy in (-5, 45, 95, 145):
            d.line([(cx - 215 * s, cy + dy * s), (cx + 215 * s, cy + dy * s)], fill=(185, 178, 165, 255), width=max(2, int(3 * s)))
    elif nome == "porta":
        for a in range(-60, 61, 12):
            x2 = cx + 520 * math.tan(math.radians(a)) * s
            d.polygon([(cx - 8 * s, cy), (cx + 8 * s, cy), (x2 + 18 * s, cy - 420 * s), (x2 - 18 * s, cy - 420 * s)], fill=(255, 225, 140, 40))
        d.rounded_rectangle((cx - 120 * s, cy - 240 * s, cx + 120 * s, cy + 250 * s), radius=int(10 * s), fill=(255, 232, 160, 255), outline=(255, 250, 220, 255), width=max(2, int(6 * s)))
        for dx, dy, rr in [(-190, 170, 26), (-130, 230, 20), (170, 195, 28), (220, 250, 20), (-230, 90, 18), (230, 110, 18), (-170, -60, 16), (190, -40, 16)]:
            x, y, r = cx + dx * s, cy + dy * s, rr * s
            d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 200, 60, 255), outline=(200, 140, 20, 255), width=max(2, int(3 * s)))
            d.ellipse((x - r / 2, y - r / 2, x + r / 2, y + r / 2), outline=(255, 235, 150, 255), width=max(2, int(3 * s)))
    else:
        raise SystemExit(f"símbolo desconhecido: {nome}. Use teto, termostato, caderno ou porta.")
    return camada


def fundo(pal, simbolo, cx, cy, s, intensidade=1.0, imagem=None):
    if imagem:
        base = cobrir(Image.open(imagem).convert("RGB"), W, H)
        base = ImageEnhance.Brightness(base).enhance(0.75)
        return base.convert("RGBA")
    base = gradiente(*pal["fundo"])
    base = brilho(base, (cx, cy), 430, (255, 190, 80), 0.8 * intensidade)
    base = base.convert("RGBA")
    sim = desenhar_simbolo(simbolo, cx, cy, s)
    if intensidade < 1:
        sim.putalpha(sim.split()[3].point(lambda v: int(v * intensidade)))
    base.alpha_composite(sim)
    return base


# ---------------------------------------------------------------- autoridade
def busto_placeholder(h, rotulo=True):
    """Busto genérico de homem de cabelo branco e óculos, só para testar o layout. Não é retrato de ninguém."""
    inteiro = _busto(int(h * 1.5))
    w = int(h * 1.05)
    x0 = (inteiro.width - w) // 2
    im = inteiro.crop((x0, 0, x0 + w, h))
    if rotulo:
        dd = ImageDraw.Draw(im, "RGBA")
        f = fonte(max(16, int(h * 0.034)))
        t = "FOTO LICENCIADA ENTRA AQUI"
        bx0, by0, bx1, by1 = f.getbbox(t)
        yy = int(h * 0.66)
        dd.rectangle((0, yy - 6, im.width, yy + (by1 - by0) + 12), fill=(0, 0, 0, 150))
        dd.text(((im.width - (bx1 - bx0)) / 2, yy), t, font=f, fill=(255, 255, 255, 225))
    return im


def _busto(h):
    S = 3
    Hh = h * S
    Wd = int(h * 0.95) * S
    im = Image.new("RGBA", (Wd, Hh), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    cx = Wd / 2
    u = Hh
    d.polygon([(cx - .46 * u, u), (cx - .41 * u, .62 * u), (cx - .18 * u, .52 * u), (cx + .18 * u, .52 * u), (cx + .41 * u, .62 * u), (cx + .46 * u, u)], fill=(27, 36, 50, 255))
    d.polygon([(cx - .12 * u, .52 * u), (cx + .12 * u, .52 * u), (cx, .82 * u)], fill=(238, 240, 244, 255))
    d.polygon([(cx - .18 * u, .52 * u), (cx - .12 * u, .52 * u), (cx, .86 * u), (cx - .10 * u, .98 * u), (cx - .30 * u, .70 * u)], fill=(40, 52, 70, 255))
    d.polygon([(cx + .18 * u, .52 * u), (cx + .12 * u, .52 * u), (cx, .86 * u), (cx + .10 * u, .98 * u), (cx + .30 * u, .70 * u)], fill=(40, 52, 70, 255))
    d.polygon([(cx - .025 * u, .56 * u), (cx + .025 * u, .56 * u), (cx + .04 * u, .86 * u), (cx, .92 * u), (cx - .04 * u, .86 * u)], fill=(200, 60, 40, 255))
    d.rectangle((cx - .07 * u, .44 * u, cx + .07 * u, .56 * u), fill=(206, 164, 132, 255))
    d.ellipse((cx - .17 * u, .08 * u, cx + .17 * u, .36 * u), fill=(236, 236, 240, 255))
    d.ellipse((cx - .155 * u, .15 * u, cx + .155 * u, .50 * u), fill=(226, 184, 150, 255))
    d.ellipse((cx - .185 * u, .28 * u, cx - .15 * u, .36 * u), fill=(226, 184, 150, 255))
    d.ellipse((cx + .15 * u, .28 * u, cx + .185 * u, .36 * u), fill=(226, 184, 150, 255))
    d.ellipse((cx - .19 * u, .22 * u, cx - .14 * u, .34 * u), fill=(236, 236, 240, 255))
    d.ellipse((cx + .14 * u, .22 * u, cx + .19 * u, .34 * u), fill=(236, 236, 240, 255))
    lw = max(3, int(.008 * u))
    d.rounded_rectangle((cx - .125 * u, .275 * u, cx - .025 * u, .335 * u), radius=int(.015 * u), outline=(40, 40, 50, 255), width=lw)
    d.rounded_rectangle((cx + .025 * u, .275 * u, cx + .125 * u, .335 * u), radius=int(.015 * u), outline=(40, 40, 50, 255), width=lw)
    d.line([(cx - .025 * u, .295 * u), (cx + .025 * u, .295 * u)], fill=(40, 40, 50, 255), width=lw)
    d.arc((cx - .05 * u, .38 * u, cx + .05 * u, .44 * u), 20, 160, fill=(150, 90, 80, 255), width=lw)
    return im.resize((Wd // S, Hh // S), Image.LANCZOS)


def suavizar_bordas(img):
    """Foto sem transparência: esmaece as bordas para se misturar ao fundo."""
    img = img.convert("RGBA")
    m = Image.new("L", img.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((int(img.width * .06), int(img.height * .04), int(img.width * .94), img.height), radius=int(img.width * .1), fill=255)
    img.putalpha(m.filter(ImageFilter.GaussianBlur(img.width * .04)))
    return img


def autoridade(args, altura):
    if args.autoridade == "placeholder":
        img = busto_placeholder(altura, rotulo=not args.sem_rotulo)
    else:
        img = Image.open(args.autoridade)
        img = img.convert("RGBA") if "A" in img.getbands() else suavizar_bordas(img.convert("RGB"))
        r = altura / img.height
        img = img.resize((max(1, int(img.width * r)), altura), Image.LANCZOS)
    if args.pb or args.modelo == "retrato":
        cinza = ImageEnhance.Contrast(ImageOps.grayscale(img.convert("RGB"))).enhance(1.2)
        img = Image.merge("RGBA", (cinza, cinza, cinza, img.split()[3]))
    return img


def com_contorno(img, cor, espessura=7):
    pad = espessura + 12
    base = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    base.paste(img, (pad, pad))
    a = base.split()[3]
    dil = a.filter(ImageFilter.MaxFilter(2 * espessura + 1)).filter(ImageFilter.GaussianBlur(3))
    borda = Image.new("RGBA", base.size, cor + (0,))
    borda.putalpha(dil)
    saida = Image.new("RGBA", base.size, (0, 0, 0, 0))
    saida.alpha_composite(borda)
    saida.alpha_composite(base)
    return saida


def fita_nome(texto, pal):
    f = fonte(36)
    x0, y0, x1, y1 = f.getbbox(texto)
    img = Image.new("RGBA", (x1 - x0 + 56, y1 - y0 + 30), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((0, 0, img.width - 1, img.height - 1), radius=10, fill=(6, 12, 22, 225), outline=pal["destaque"] + (255,), width=3)
    d.text((28 - x0, 15 - y0), texto, font=f, fill=pal["destaque"])
    return img


def colar(cena, img, cx, topo):
    cena.alpha_composite(img, (int(cx - img.width / 2), int(topo)))


# ---------------------------------------------------------------- modelos
def bloco_texto(args, pal, largura, cor_palavra, brilho_palavra=None, tam_palavra=230, tam_linha=96):
    esp = 8
    l1 = linha(args.linha1, ajustar(args.linha1, largura - 40, tam_linha), pal["texto"], pal["contorno"], esp - 2) if args.linha1 else None
    l3 = linha(args.linha3, ajustar(args.linha3, largura - 40, tam_linha), pal["texto"], pal["contorno"], esp - 2) if args.linha3 else None
    pw = linha(args.palavra, ajustar(args.palavra, largura - 70, tam_palavra), cor_palavra, pal["contorno"], esp + 2, brilho_palavra)
    return l1, pw, l3


def empilhar(cena, partes, cx, folga=22, topo=None, desloc_y=0):
    """Empilha as partes (l1, pw, l3) centradas em cx e devolve as posições y de cada uma."""
    alturas = [p.height for p in partes if p is not None]
    total = sum(alturas) + folga * (len(alturas) + 1)
    y = (H - total) // 2 + folga + desloc_y if topo is None else topo
    pos = []
    for p in partes:
        if p is None:
            pos.append(None)
            continue
        pos.append(y)
        y += p.height + folga
    return pos


def modelo_faixa(args, pal):
    escala = {"teto": 0.33, "termostato": 0.49, "caderno": 0.40, "porta": 0.45}[args.simbolo]
    cena = fundo(pal, args.simbolo, 1172, 390, escala, imagem=args.fundo)
    auth = com_contorno(autoridade(args, 660), pal["destaque"])
    colar(cena, auth, 270, H - auth.height + 22)
    l1, pw, l3 = bloco_texto(args, pal, 560, pal["destaque"] if args.paleta == "marca" else pal["texto"])
    pos = empilhar(cena, (l1, pw, l3), 790)
    faixa = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    fd = ImageDraw.Draw(faixa)
    k = math.tan(math.radians(INCLINACAO))
    fy0, fy1 = pos[1] - 6, pos[1] + pw.height + 6
    lf = max(pw.width + 90, 560)
    x0, x1 = 790 - lf // 2, 790 + lf // 2
    dz = k * (fy1 - fy0) / 2
    fd.polygon([(x0 + dz + 10, fy0 + 10), (x1 + dz + 10, fy0 + 10), (x1 - dz + 10, fy1 + 10), (x0 - dz + 10, fy1 + 10)], fill=(0, 0, 0, 120))
    fd.polygon([(x0 + dz, fy0), (x1 + dz, fy0), (x1 - dz, fy1), (x0 - dz, fy1)], fill=pal["faixa"] + (255,))
    cena = Image.alpha_composite(cena, faixa)
    for p, y in zip((l1, pw, l3), pos):
        if p is not None:
            colar(cena, p, 790, y)
    if args.nome:
        colar(cena, fita_nome(args.nome, pal), 270, H - 96)
    return cena


def modelo_retrato(args, pal):
    cena = fundo(pal, args.simbolo, 900, 360, 1.1, intensidade=0.28, imagem=args.fundo)
    auth = autoridade(args, 800)
    # esmaece o lado direito do retrato para se misturar ao fundo
    mascara = Image.new("L", auth.size, 255)
    md = ImageDraw.Draw(mascara)
    for x in range(auth.width):
        t = x / auth.width
        md.line([(x, 0), (x, auth.height)], fill=255 if t < 0.55 else int(255 * max(0.0, 1 - (t - 0.55) / 0.40)))
    auth.putalpha(ImageChops.multiply(auth.split()[3], mascara))
    colar(cena, auth, 330, H - auth.height + 70)
    l1, pw, l3 = bloco_texto(args, pal, 640, pal["destaque"], brilho_palavra=None)
    pos = empilhar(cena, (l1, pw, l3), 910, desloc_y=-48)
    barra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    k = math.tan(math.radians(INCLINACAO))
    by = pos[1] + pw.height + (-6)
    bw = pw.width
    ImageDraw.Draw(barra).polygon([(910 - bw / 2 + 14 + k * 14, by), (910 + bw / 2 + 14 + k * 14, by), (910 + bw / 2 + 14, by + 14), (910 - bw / 2 + 14, by + 14)], fill=pal["acento"] + (255,))
    cena = Image.alpha_composite(cena, barra)
    for p, y in zip((l1, pw, l3), pos):
        if p is not None:
            colar(cena, p, 910, y)
    if args.nome:
        ass = assinatura(args.nome.title() if args.nome.isupper() else args.nome, 58, pal["texto"] + (255,))
        colar(cena, ass, 930, H - ass.height - 14)
    return cena


def modelo_prazo(args, pal):
    cena = fundo(pal, args.simbolo, 420, 380, 0.95, intensidade=0.35, imagem=args.fundo)
    auth = com_contorno(autoridade(args, 650), pal["destaque"])
    colar(cena, auth, 1010, H - auth.height + 22)
    l1, pw, l3 = bloco_texto(args, pal, 640, pal["destaque"], brilho_palavra=pal["destaque"], tam_palavra=280)
    pos = empilhar(cena, (l1, pw, l3), 380)
    barra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    k = math.tan(math.radians(INCLINACAO))
    by = pos[1] + pw.height - 14
    bw = pw.width * 0.9
    ImageDraw.Draw(barra).polygon([(380 - bw / 2 + k * 20, by), (380 + bw / 2 + k * 20, by), (380 + bw / 2, by + 18), (380 - bw / 2, by + 18)], fill=pal["acento"] + (255,))
    cena = Image.alpha_composite(cena, barra)
    for p, y in zip((l1, pw, l3), pos):
        if p is not None:
            colar(cena, p, 380, y)
    if args.nome:
        colar(cena, fita_nome(args.nome, pal), 1010, H - 96)
    return cena


MODELOS = {"faixa": modelo_faixa, "retrato": modelo_retrato, "prazo": modelo_prazo}


def compor(args):
    cena = MODELOS[args.modelo](args, PALETAS[args.paleta])
    if args.marca:
        d = ImageDraw.Draw(cena, "RGBA")
        f = fonte(28)
        x0, y0, x1, y1 = f.getbbox(args.marca)
        bx = 24
        d.rounded_rectangle((bx, 24, bx + (x1 - x0) + 36, 24 + 46), radius=10, fill=(0, 0, 0, 170))
        d.text((bx + 18, 28), args.marca, font=f, fill=(255, 255, 255, 230))
    return cena.convert("RGB")


def main():
    p = argparse.ArgumentParser(description="Compõe uma capa 1280x720 com a autoridade em destaque.")
    p.add_argument("--modelo", choices=sorted(MODELOS), default="faixa")
    p.add_argument("--autoridade", required=True, help="foto da autoridade (PNG com transparência é o ideal) ou 'placeholder'")
    p.add_argument("--nome", default="BOB PROCTOR", help="fita ou assinatura com o nome. Vazio para não mostrar")
    p.add_argument("--linha1", default="", help="linha pequena de cima")
    p.add_argument("--palavra", required=True, help="palavra, número ou prazo grande")
    p.add_argument("--linha3", default="", help="linha pequena de baixo")
    p.add_argument("--paleta", choices=sorted(PALETAS), default="marca")
    p.add_argument("--simbolo", choices=["teto", "termostato", "caderno", "porta"], default="teto")
    p.add_argument("--fundo", help="imagem de fundo própria no lugar da arte provisória")
    p.add_argument("--pb", action="store_true", help="autoridade em preto e branco (o modelo retrato já usa)")
    p.add_argument("--marca", default="", help="texto pequeno de marca no canto, por exemplo o nome do canal")
    p.add_argument("--sem-rotulo", action="store_true", help="tira o rótulo do placeholder")
    p.add_argument("--saida", required=True)
    a = p.parse_args()
    if not os.path.exists(FONTE):
        sys.exit(f"fonte não encontrada: {FONTE}")
    compor(a).save(a.saida, quality=92)
    print("capa salva em", a.saida)


if __name__ == "__main__":
    main()
