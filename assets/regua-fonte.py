#!/usr/bin/env python3
"""
Régua de substituição de fonte — acha a open-source mais próxima do que o gerador desenhou.

    ./regua-fonte.py gabarito-01.png 210,340 "O ALMOÇO" Antonio-700.ttf Bricolage-800.ttf ...

  1 · o PNG do gabarito
  2 · a faixa vertical `topo,base` em pixels onde mora a linha de título a casar
  3 · A STRING QUE ESTÁ NAQUELA FAIXA, exatamente como o modelo a desenhou
  4 · as candidatas. Sem elas, testa todas as faces embutidas em assets/fontes/

**A string é obrigatória e não é firula.** As três medidas dependem de quais letras foram
medidas: "AÇÃO" contra "AÇÃOMBERSGH" dá razão largura/caixa-alta 1,76 contra 3,87 na MESMA
fonte, e a régua elege a candidata errada com toda a confiança. Rasterizar a candidata com a
string do gabarito é o que torna a comparação uma comparação.

POR QUE ISTO EXISTE COMO CÓDIGO. A régua estava descrita em geradores.md com as três medidas
e uma tabela de exemplo, e nenhuma linha executável. Quem precisa dela na etapa 7 ou reescreve
do zero — foi ~1h numa produção real — ou pula a régua. Pular a régua é o que quase entregou
uma Bricolage Grotesque com o DOBRO da largura do que o modelo tinha desenhado.

AS TRÊS MEDIDAS, e casar só a largura não basta:

  razão largura/caixa-alta   quanto a letra é larga em relação à própria altura. É a que
                             manda no comprimento de linha, e comprimento de linha é o que
                             faz os oito cards lerem como uma série só
  densidade de tinta         fração de pixel coberto dentro da caixa do texto. Distingue uma
                             condensada leve de uma condensada pesada, que a razão não vê
  espessura da haste         mediana das corridas horizontais de tinta. É o que estraga
                             quando se comprime uma fonte para forçar a razão a fechar

O gabarito é medido por projeção do PNG; as candidatas, rasterizando a mesma string.
"""
import sys, os, statistics
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("falta o Pillow:  pip3 install pillow")

AQUI   = Path(__file__).resolve().parent
FONTES = AQUI / "fontes"


# ── medidas, iguais para o gabarito e para as candidatas ──────────────────────────────
def medidas(mascara):
    """mascara: 2D de bool, True = tinta. Devolve (razão, densidade, espessura)."""
    alt = len(mascara)
    linhas_com_tinta = [y for y, l in enumerate(mascara) if any(l)]
    if not linhas_com_tinta:
        return None
    topo, base = linhas_com_tinta[0], linhas_com_tinta[-1]
    caixa_alta = base - topo + 1

    cols = [x for x in range(len(mascara[0])) if any(mascara[y][x] for y in range(alt))]
    larg = cols[-1] - cols[0] + 1

    tinta = sum(sum(l) for l in mascara)
    densidade = tinta / (larg * caixa_alta)

    # espessura da haste: corridas horizontais de tinta, medianas. A mediana e não a média
    # porque a serifa e a junção de curva produzem corridas longas que puxam a média.
    corridas = []
    for y in range(topo, base + 1):
        n = 0
        for x in range(len(mascara[0])):
            if mascara[y][x]:
                n += 1
            elif n:
                corridas.append(n); n = 0
        if n:
            corridas.append(n)
    if not corridas:
        return None
    haste = statistics.median(corridas) / caixa_alta

    return larg / caixa_alta, densidade, haste


def do_png(caminho, faixa):
    topo, base = (int(v) for v in faixa.split(","))
    im = Image.open(caminho).convert("L").crop((0, topo, Image.open(caminho).width, base))
    px = im.load()
    w, h = im.size
    # limiar por Otsu simples: a chapa tem duas populações, tinta e papel
    hist = im.histogram()
    total = sum(hist)
    soma = sum(i * hist[i] for i in range(256))
    sb = wb = mx = lim = 0
    for i in range(256):
        wb += hist[i]
        if wb == 0 or wb == total:
            continue
        wf = total - wb
        sb += i * hist[i]
        entre = wf * wb * ((sb / wb) - ((soma - sb) / wf)) ** 2
        if entre > mx:
            mx, lim = entre, i
    return [[px[x, y] < lim for x in range(w)] for y in range(h)]


def do_ttf(caminho, texto, corpo=200):
    try:
        f = ImageFont.truetype(str(caminho), corpo)
    except Exception:
        return None
    im = Image.new("L", (corpo * (len(texto) + 2), corpo * 3), 255)
    ImageDraw.Draw(im).text((corpo // 2, corpo // 2), texto, font=f, fill=0)
    px = im.load()
    w, h = im.size
    return [[px[x, y] < 128 for x in range(w)] for y in range(h)]


# ── main ──────────────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    png, faixa, texto = sys.argv[1], sys.argv[2], sys.argv[3]
    cands = sys.argv[4:] or sorted(str(p) for p in FONTES.glob("*.ttf"))
    if not cands:
        sys.exit(f"nenhuma candidata, e assets/fontes/ está vazio: {FONTES}")

    mask = do_png(png, faixa)
    alvo = medidas(mask)
    if not alvo:
        sys.exit("não achei tinta na faixa — confira topo,base contra o PNG")

    # A faixa cortando o glifo distorce as TRÊS medidas de uma vez e em silêncio: cortar o
    # pé reduz a caixa alta medida, o que infla a razão e a densidade juntas, e a régua
    # elege a candidata errada com toda a confiança. Custou uma eleição errada no teste.
    if any(mask[0]) or any(mask[-1]):
        borda = "topo" if any(mask[0]) else ""
        borda += (" e " if borda and any(mask[-1]) else "") + ("base" if any(mask[-1]) else "")
        sys.exit(f"PARADO — há tinta encostando na {borda} da faixa {faixa}.\n"
                 f"  A faixa precisa conter a linha INTEIRA, do topo do acento ao pé do\n"
                 f"  descendente, com papel dos dois lados. Cortada, ela encolhe a caixa\n"
                 f"  alta medida e as três medidas saem erradas juntas.\n"
                 f"  Abra o PNG, leia as coordenadas da linha, e folgue uns 20px de cada lado.")

    print(f"\n  string medida: {texto!r}")
    print(f"\n  {'':34s} {'razão':>7} {'dens':>7} {'haste':>7} {'desvio':>8}")
    print(f"  {'GABARITO ' + os.path.basename(png):34s} "
          f"{alvo[0]:7.3f} {alvo[1]:7.3f} {alvo[2]*100:6.1f}% {'—':>8}")
    print("  " + "─" * 68)

    placar = []
    for c in cands:
        m = medidas(do_ttf(c, texto) or [[False]])
        if not m:
            print(f"  {os.path.basename(c):34s} não consegui rasterizar")
            continue
        # desvio relativo somado nas três — nenhuma das três sozinha decide
        desvio = sum(abs(m[i] - alvo[i]) / alvo[i] for i in range(3)) * 100
        placar.append((desvio, c, m))

    for desvio, c, m in sorted(placar):
        print(f"  {os.path.basename(c):34s} {m[0]:7.3f} {m[1]:7.3f} {m[2]*100:6.1f}% "
              f"{desvio:7.1f}%")

    if placar:
        d, c, _ = min(placar)
        print(f"\n  → {os.path.basename(c)}, desvio {d:.1f}%")
        print("\n  Depois de escolher, duas coisas que a régua NÃO faz:")
        print("  · confira os acentos glifo a glifo — `fontes.sh` faz isso")
        print("  · NÃO dimensione o corpo pela soma dos avanços do hmtx. Medido, o navegador")
        print("    renderizou de 5,6% a 9,0% mais largo que a conta, e um card transbordou a")
        print("    coluna. Rode o `?medir=1` do esqueleto antes de capturar, sempre que o")
        print("    corpo tiver sido calculado fora do navegador.")


if __name__ == "__main__":
    main()
