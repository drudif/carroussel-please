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


LIMIAR_COR = 28   # distância euclidiana em RGB (0-441) para contar como "não é o papel"


def cor_de_fundo(a):
    """Amostra cantos e meios de borda em vez de assumir um hex fixo — funciona no
    creme da riso, no kraft da colagem, no chumbo do terminal, em qualquer paleta.
    A régua velha comparava contra `#EDEAE3` fixo e devolvia número errado, com toda
    confiança, em qualquer chapa que não fosse riso — inclusive fundo cinza, que
    passava inteiro como "sem tinta nenhuma".

    Não basta mediana simples dos pontos: a zona de ilustração do laço (geradores.md)
    tem licença explícita para sangrar até a borda, inclusive canto. Um canto coberto
    de ilustração dá amostra errada, e a mediana simples desliza na direção dele. Por
    isso vota: a cor de fundo é a que tem mais OUTRAS amostras por perto — maioria
    vence quando uma ou duas amostras caem em cima de ilustração que sangrou até lá."""
    h, w, _ = a.shape
    k = 30
    pontos = [a[0:k, 0:k], a[0:k, w-k:w], a[h-k:h, 0:k], a[h-k:h, w-k:w],
              a[0:k, w//2-k:w//2+k], a[h-k:h, w//2-k:w//2+k]]
    amostras = [np.median(p.reshape(-1, 3), axis=0) for p in pontos]
    melhor, votos = amostras[0], -1
    for c in amostras:
        n = sum(1 for o in amostras if np.linalg.norm(c - o) < LIMIAR_COR)
        if n > votos:
            melhor, votos = c, n
    return melhor


def regua(tinta):
    """A régua da chapa É o divisor entre a zona do título e a do sub — não importa
    a cor dela. O gerador a desenhou ali de propósito; ler a imagem em vez de dividir
    por conta própria foi o que faltou nas montagens anteriores. `tinta` já é
    relativo ao fundo desta chapa (ver `cor_de_fundo`), então a régua funciona em
    qualquer paleta, não só na laranja da risografia."""
    for y in range(int(H * .25), H - 40):
        faixa = tinta[y:y + 14]
        if faixa.any(axis=0).mean() > .34:        # corrida horizontal longa
            grosso = tinta[y:y + 40].sum(axis=0).max()
            if grosso <= 26:                      # fina: é régua, não campo de cor
                return y
    return None


def classificar(arq):
    im = Image.open(arq).convert("RGB").resize((W, H), Image.LANCZOS)
    a = np.array(im).astype(int)
    papel = cor_de_fundo(a)
    dist = np.linalg.norm(a - papel, axis=2)
    tinta = dist > LIMIAR_COR
    return im, tinta


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
    r = regua(tinta)
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
