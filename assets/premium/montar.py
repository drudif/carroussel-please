#!/usr/bin/env python3
"""Gera o HTML dos sete cards a partir da MEDIÇÃO das chapas, não de números na mão.

O corpo de cada título sai de duas restrições, e a menor manda:
  · comprimento de linha do gabarito (580px, já comprimido) — o que faz os sete
    lerem como a mesma série;
  · altura do vão medido na chapa — o que impede o título de invadir a ilustração.
"""
import json, subprocess
from PIL import Image, ImageDraw, ImageFont
import numpy as np

COMP = .728            # compressão horizontal da Anton
LINHA = 580            # comprimento de linha do gabarito
CORPO_MIN = 118        # abaixo disso o título deixa de ser título
CAIXA = .8575          # caixa alta da Anton, em fração do corpo
ENTRE = .93            # entrelinha, do gabarito
ANTON = "../fontes-teste/Anton-400.ttf"

CARDS = [
 dict(n=1, img="y01.png",
      linhas=[("Esse","azul"),("Carrossel","azul"),("Não foi feito","laranja"),
              ("Só com","azul"),("Um prompt","azul")],
      lede="Foi feito com uma só skill — que você instala e usa agora."),
 dict(n=2, img="y02.png",
      # o título veio sem ` / ` no .md: a quebra é decisão da skill.
      # quatro linhas equilibradas, a mais longa em 10 caracteres.
      linhas=[("Você traz","azul"),("O briefing","azul"),("E ela te","laranja"),("Entrevista","laranja")],
      lede="A skill vai perguntar sobre o gancho, a tese, os passos e o fechamento — uma coisa por vez."),
 dict(n=3, img="y03.png",
      linhas=[("Seis estilos","azul"),("Diferentes","laranja")],
      lede="Você escolhe na tela. Se tiver conta num gerador de imagem, dá pra conectar."),
 dict(n=4, img="y04.png",
      linhas=[("Sem","papel"),("Cheirinho","laranja"),("De IA","papel")],
      lede='O texto é revisado. Tchau, "não é X, é Y", tchau travessão, tchau número sem fonte.'),
 dict(n=5, img="y05.png",
      linhas=[("Você","azul"),("Aprova.","laranja")],
      lede="Carrossel completo na tela pra você conferir."),
 dict(n=6, img="y06.png",
      linhas=[("Pronto","azul"),("Pro IG","laranja"),("E LinkedIn","azul")],
      lede="PNG vertical para o Instagram e PDF quadrado para o LinkedIn."),
 dict(n=7, img="y07.png",
      linhas=[("Instala","azul"),("E usa","azul"),("Agora","laranja")],
      lede='Se não sabe por onde começar, comenta aqui "como faz?" que eu te mando o passo a passo.'),
]


def largura(txt, corpo):
    f = ImageFont.truetype(ANTON, corpo)
    im = Image.new("L", (corpo * 18, corpo * 3), 255)
    ImageDraw.Draw(im).text((corpo, corpo // 2), txt.upper(), font=f, fill=0)
    a = np.array(im) < 128
    if not a.any():
        return 0
    _, xs = np.where(a)
    return (xs.max() - xs.min()) * COMP


def corpo_por_linha(linhas):
    c = 240
    for _ in range(30):
        w = max(largura(t, c) for t, _ in linhas)
        if abs(w - LINHA) <= 3:
            break
        c = max(20, int(c * LINHA / max(w, 1)))
    return c


def corpo_por_altura(linhas, alt):
    n = len(linhas)
    # altura do bloco = (n-1) passos + 1 caixa alta
    return int(alt / ((n - 1) * ENTRE + CAIXA))


M = json.load(open("chapas.json"))
saida = []
for c in CARDS:
    m = M[c["img"]]
    a, b = corpo_por_linha(c["linhas"]), corpo_por_altura(c["linhas"], m["alt"])
    corpo, campo_tit = min(a, b), False
    if b < CORPO_MIN and m["fundo"] == "tinta":
        # a chapa não tem vão que sirva. Em vez de encolher a letra até sumir, o título
        # sobe POR CIMA da ilustração com campo chapado atrás — mesma lógica do lede:
        # a leitura não cede, o grafismo cede.
        corpo, campo_tit = a, True
    if b < CORPO_MIN and m["fundo"] == "papel":
        # sem vão e sobre papel: o título sobe por cima da ilustração e MULTIPLICA.
        # Cobrir com campo chapado apagaria o desenho — foi o que lavou os anéis do 07.
        corpo = a
    bloco = (len(c["linhas"]) - 1) * corpo * ENTRE + corpo * CAIXA
    if campo_tit:
        topo = max(120, min(m["pe"] - bloco - 60, m["topo"] - bloco * .45))
    elif bloco > m["alt"]:
        topo = max(90, min(m["pe"] - bloco - 40, m["topo"] - bloco * .55))
    else:
        topo = m["topo"] + max(24, (m["alt"] - bloco) / 2)  # centra no vão medido
    tit = "<br>".join(f'<span class="{cor}">{t}</span>' for t, cor in c["linhas"])
    saida.append(dict(img=c["img"], lado=m["lado"], corpo=corpo, topo=int(topo),
                      pe=m["pe"], campo=m["campo"], fundo=m["fundo"],
                      campo_tit=campo_tit, bloco=int(bloco), regua_propria=m.get("regua_propria", False),
                      tit=tit, lede=c["lede"]))
    print(f"card {c['n']}: corpo {corpo:3} (linha {a}, altura {b}) · topo {int(topo):4} "
          f"· bloco {int(bloco):4} · vão {m['alt']:4} · {m['lado']} · {m['fundo']}"
          f"{'  ← campo atrás do título' if campo_tit else ''}")

json.dump(saida, open("cards.json", "w"), ensure_ascii=False, indent=1)
