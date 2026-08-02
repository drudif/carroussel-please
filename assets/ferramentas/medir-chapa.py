#!/usr/bin/env python3
"""Lê cada chapa limpa e devolve onde o texto cabe. A informação já está na imagem —
posicionar na mão é chutar duas vezes o que dá para medir uma.

Para cada chapa devolve:
  lado      'esq' | 'dir'   — de que lado está a área livre
  topo, alt — o bloco livre mais alto, em px de 1080×1350
  larg      — largura utilizável naquele lado
  fundo     'papel' | 'tinta'  — decide a cor do tipo e se pode multiplicar
  pe        — onde começa a faixa do lede
"""
import sys, json
import numpy as np
from PIL import Image

W, H = 1080, 1350
MARGEM = 44
LIMIAR = 0.14          # fração de tinta que ainda conta como "livre"
ALT_MIN = 300          # bloco menor que isso não serve para título
# o pé precisa caber régua + até três linhas de corpo 34 + respiro + assinatura.
# sem esse teto o lede fica espremido no rodapé, que foi o defeito da primeira montagem.
PE_MAX = 1100
PE_ALT = 215        # régua + até três linhas de 34 + respiro


def regua(im):
    """A régua laranja da chapa É o divisor entre a zona do título e a do sub.
    O gerador a desenhou ali de propósito; ler a imagem em vez de dividir por conta
    própria foi o que faltou nas montagens anteriores."""
    a = np.array(im).astype(int)
    lar = (a[:, :, 0] > a[:, :, 2] + 55) & (a[:, :, 0] > 150)
    for y in range(int(H * .25), H - 40):
        faixa = lar[y:y + 14]
        if faixa.any(axis=0).mean() > .34:        # corrida horizontal longa
            grosso = lar[y:y + 40].sum(axis=0).max()
            if grosso <= 26:                      # fina: é régua, não campo de cor
                return y
    return None


def classificar(arq):
    im = Image.open(arq).convert("RGB").resize((W, H), Image.LANCZOS)
    a = np.array(im).astype(int)
    # tinta = qualquer pixel que não seja o papel creme
    papel = (a[:, :, 0] > 205) & (a[:, :, 1] > 198) & (a[:, :, 2] > 180)
    return im, ~papel


def maior_vao(perfil):
    """maior sequência de linhas abaixo do limiar → (topo, altura)"""
    melhor = (0, 0)
    ini = None
    for y, v in enumerate(list(perfil) + [1.0]):
        if v < LIMIAR and ini is None:
            ini = y
        elif v >= LIMIAR and ini is not None:
            if y - ini > melhor[1]:
                melhor = (ini, y - ini)
            ini = None
    return melhor


def medir(arq):
    im, tinta = classificar(arq)
    meio = int(W * 0.60)
    esq = tinta[:, :meio].mean(axis=1)
    dir_ = tinta[:, W - meio:].mean(axis=1)

    cand = []
    for lado, perfil in (("esq", esq), ("dir", dir_)):
        topo, alt = maior_vao(perfil)
        if alt >= ALT_MIN:
            cand.append({"lado": lado, "topo": int(topo), "alt": int(alt),
                         "larg": meio - MARGEM * 2, "fundo": "papel"})

    if not cand:
        # chapa coberta de tinta: o tipo vai VAZADO, e não pode multiplicar.
        # escolhe a faixa mais uniforme, que é onde a letra vai sofrer menos.
        g = np.array(im.convert("L")).astype(float)
        var = np.array([g[y:y + 40].std() for y in range(0, H - 40, 20)])
        alto = max(6, len(var) // 3)              # terço de cima: é onde o título mora
        y = int(np.argmin(var[:alto]) * 20)
        cand.append({"lado": "esq", "topo": max(140, y), "alt": 620,
                     "larg": meio - MARGEM * 2, "fundo": "tinta"})

    b = max(cand, key=lambda c: c["alt"])

    # O pé mora DENTRO da mesma faixa livre, no fim dela — porque foi assim que o
    # gabarito foi gerado: zona do título e zona do sub são vizinhas, não opostas.
    # Procurar de baixo para cima punha a régua em cima do grafismo do card seguinte.
    r = regua(im)
    if r is not None and b["topo"] + 120 < r < H - 90:
        pe = r                                    # a régua da chapa manda
        b["regua_propria"] = True
    else:
        pe = min(PE_MAX, b["topo"] + b["alt"] - PE_ALT)
        pe = max(pe, b["topo"] + 200)
        b["regua_propria"] = False
    b["pe"] = int(pe)

    # o campo atrás do lede não se decide pelo perfil da coluna do título — decide-se
    # medindo o RETÂNGULO onde o lede vai cair. E não basta ter tinta: campo uniforme
    # (o azul chapado do card 4) lê bem com tipo claro por cima, sem faixa nenhuma.
    # Faixa só quando a área é AGITADA, porque aí a letra briga com o desenho.
    cx0, cx1 = MARGEM, W - MARGEM
    cy0, cy1 = b["pe"] - 20, min(H - 60, b["pe"] + 200)
    rec = tinta[cy0:cy1, cx0:cx1]
    g = np.array(im.convert("L")).astype(float)[cy0:cy1, cx0:cx1]
    cobertura, agito = rec.mean(), g.std()
    b["campo"] = bool(cobertura > .12 and agito > 26)
    b["agito"] = round(float(agito), 1)
    b["cobertura"] = round(float(cobertura), 3)

    # o título tem de caber no vão: limita a altura do bloco ao espaço até o pé
    b["alt"] = int(max(120, b["pe"] - b["topo"] - 46))
    b["arq"] = arq
    return b


if __name__ == "__main__":
    saida = {}
    for arq in sys.argv[1:]:
        m = medir(arq)
        saida[arq] = m
        print(f"{arq:16} {m['lado']}  topo {m['topo']:4}  alt {m['alt']:4}  "
              f"fundo {m['fundo']:5}  pe {m['pe']:4}{'*' if m['regua_propria'] else ' '} "
              f"campo {str(m['campo']):5} "
              f"(cobertura {m['cobertura']}, agito {m['agito']})")
    json.dump(saida, open("chapas.json", "w"), indent=1)
