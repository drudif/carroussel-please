#!/usr/bin/env python3
"""Busca no Dupe. Sem chave, sem cadastro.

    ./dupe.py "torn paper" 8

ATENÇÃO — isto NÃO é uma API pública. O site é uma SPA e este endpoint é o backend
que ela chama; descobri o formato lendo o bundle. Consequências, que a skill precisa
dizer ao usuário antes de usar:
  · não há termos publicados para uso programático
  · não há versionamento: pode mudar ou fechar sem aviso
  · a licença de cada foto é do autor que subiu, e precisa ser conferida caso a caso
Por isso o Dupe entra DEPOIS do Pixabay na ordem de prioridade, e antes da Openverse
só porque o acervo é mais moderno e mais editorial.
"""
import json, os, sys, urllib.request, time

API = "https://content-api-prod-6gxsdymdsq-ue.a.run.app/api/v1/content/search"
CDN = "https://d3p3fw3rutb1if.cloudfront.net/photos/"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/124 Safari/537.36",
      "Origin": "https://dupephotos.com", "Referer": "https://dupephotos.com/",
      "Content-Type": "application/json"}


def buscar(label, n=8, dest="cand-dupe"):
    os.makedirs(dest, exist_ok=True)
    req = urllib.request.Request(API, data=json.dumps({"label": label}).encode(), headers=UA)
    hits = json.loads(urllib.request.urlopen(req, timeout=40).read())
    slug = "".join(c if c.isalnum() else "-" for c in label.lower())[:22]
    achados = []
    for i, h in enumerate(hits[:n]):
        iid = h.get("img_id")
        if not iid:
            continue
        alvo = f"{dest}/{slug}-{i:02d}.jpg"
        try:
            r = urllib.request.Request(CDN + iid, headers=UA)
            open(alvo, "wb").write(urllib.request.urlopen(r, timeout=60).read())
            from PIL import Image
            w, h2 = Image.open(alvo).size
            print(f"  {alvo}  {w}x{h2}  {str(h.get('title'))[:40]}")
            achados.append({"arq": alvo, "label": label, "id": h["id"],
                            "titulo": h.get("title"), "w": w, "h": h2})
            time.sleep(.2)
        except Exception as e:
            print(f"  x {iid[:12]}: {str(e)[:44]}")
    json.dump(achados, open(f"{dest}/{slug}.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(achados)} baixadas — OLHE todas antes de escolher.")
    return achados


if __name__ == "__main__":
    buscar(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 8)
