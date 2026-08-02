#!/usr/bin/env python3
"""Busca prancha de domínio público, trata na paleta do estilo, devolve PNG.

    ./prancha.py buscar "anatomia do ouvido"        -> baixa candidatas em cand/
    ./prancha.py tratar cand/ouvido-2.jpg gfx/02.png brutalista --alt 1010

Fonte: Openverse (sem chave). Só licenças cc0 e pdm — domínio público de verdade.
A relevância da busca erra bastante: baixe três, OLHE, e escolha. Não automatize a escolha.
"""
import json, sys, os, urllib.request, urllib.parse, re
from PIL import Image, ImageOps, ImageEnhance

UA = {"User-Agent": "carrossel-skill/2.0"}

# rampa de três paradas: sombra -> sinal -> papel.
# a imagem NASCE na paleta; não é imagem neutra tingida depois.
PALETAS = {
    "brutalista": [(0.0, "#111111"), (0.55, "#E33420"), (1.0, "#EDEAE3")],
    "riso":       [(0.0, "#1B3A6B"), (0.50, "#E8604C"), (1.0, "#F2EDE2")],
    "janelas":    [(0.0, "#000000"), (0.58, "#2F6BFF"), (1.0, "#D8DEE9")],
    "colagem":    [(0.0, "#241F1C"), (0.54, "#C8452D"), (1.0, "#E7DFD2")],
    "neobrutal":  [(0.0, "#000000"), (0.52, "#FF5C8A"), (1.0, "#FFE8A3")],
    "editorial":  [(0.0, "#2A1F16"), (0.62, "#B4622E"), (1.0, "#F3EDE3")],
}


def _get(url, timeout=90):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout).read()


def buscar(termo, n=6, destino="cand"):
    os.makedirs(destino, exist_ok=True)
    url = "https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(
        {"q": termo, "license": "cc0,pdm", "size": "large", "page_size": n})
    res = json.loads(_get(url, 30))["results"]
    slug = re.sub(r"[^a-z0-9]+", "-", termo.lower()).strip("-")[:24]
    for i, r in enumerate(res):
        alvo = f"{destino}/{slug}-{i}.jpg"
        try:
            open(alvo, "wb").write(_get(r["url"]))
            w, h = Image.open(alvo).size
            print(f"{alvo}  {w}x{h}  {r.get('source')}  {r['title'][:44]}")
        except Exception as e:
            print(f"  x {r['url'][:70]} -> {str(e)[:40]}")


def _hexa(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rampa(paradas, n=256):
    ps = [(p, _hexa(c)) for p, c in paradas]
    out = []
    for i in range(n):
        t = i / (n - 1)
        for j in range(len(ps) - 1):
            a, b = ps[j], ps[j + 1]
            if a[0] <= t <= b[0]:
                f = 0 if b[0] == a[0] else (t - a[0]) / (b[0] - a[0])
                out.append(tuple(round(a[1][k] + (b[1][k] - a[1][k]) * f) for k in range(3)))
                break
        else:
            out.append(ps[-1][1])
    return out


def tratar(origem, destino, estilo, larg=1080, alt=1010, foco=0.4,
           contraste=1.9, inverter=False, chapas=0):
    """chapas=N quantiza o cinza em N degraus antes de mapear.

    Sem isso a rampa devolve meio-tom contínuo, que serve a riso e editorial e
    reprova no brutalista: o estilo é chapa de cor, não transição. Com chapas=3
    a foto vira três áreas duras — que é o que serigrafia faz de verdade."""
    im = Image.open(origem).convert("RGB")
    im = ImageOps.fit(im, (larg, alt), method=Image.LANCZOS, centering=(0.5, foco))
    g = ImageOps.grayscale(im)
    g = ImageOps.autocontrast(g, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(contraste)
    if inverter:
        g = ImageOps.invert(g)
    if chapas:
        p = 255 / (chapas - 1)
        g = g.point(lambda v: int(round(v / p) * p))
    lut = _rampa(PALETAS[estilo])
    out = Image.new("RGB", g.size)
    out.putdata([lut[p] for p in g.getdata()])
    os.makedirs(os.path.dirname(destino) or ".", exist_ok=True)
    out.save(destino)
    print(f"{destino}  {out.size}  {estilo}")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "buscar":
        buscar(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 6)
    elif cmd == "tratar":
        kw = {}
        for a in sys.argv[5:]:
            k, v = a.lstrip("-").split("=") if "=" in a else (a.lstrip("-"), None)
            kw[k] = float(v) if v and re.match(r"^[\d.]+$", v) else (True if v is None else v)
        tratar(sys.argv[2], sys.argv[3], sys.argv[4], **{k: (int(v) if k in ("larg", "alt") else v) for k, v in kw.items()})
