#!/usr/bin/env bash
# Baixa o par de fontes open-source de um estilo, do Google Fonts (todas OFL/Apache).
#   ./baixar-fontes.sh utilitario          baixa o par do estilo
#   ./baixar-fontes.sh --listar            mostra os estilos disponíveis
#   ./baixar-fontes.sh "Space Mono:700"    baixa uma família avulsa
# Gera fonts.css com as faces em base64 e confere os acentos pt-BR de cada uma.
set -euo pipefail

UA="Mozilla/5.0 (Windows NT 6.1; WOW64)"     # UA antigo faz a API devolver TTF
DEST=${DEST:-.}

pares () { case "$1" in
  brutalista)  echo "Anton:400|IBM Plex Mono:400";;
  riso)        echo "Bricolage Grotesque:800|Newsreader:400";;
  janelas)     echo "Archivo Black:400|Space Mono:400";;
  colagem)     echo "Bodoni Moda:900|Karla:400";;
  neubrutal)   echo "Chivo:900|Chivo Mono:400";;
  editorial)   echo "Fraunces:700|Work Sans:400";;
  *) return 1;;
esac; }

if [ "${1:-}" = "--listar" ] || [ $# -eq 0 ]; then
  echo "estilos:"
  echo "  brutalista   Anton 400               / IBM Plex Mono 400"
  echo "  riso         Bricolage Grotesque 800 / Newsreader 400"
  echo "  janelas      Archivo Black 400       / Space Mono 400"
  echo "  colagem      Bodoni Moda 900         / Karla 400"
  echo "  neubrutal    Chivo 900               / Chivo Mono 400"
  echo "  editorial    Fraunces 700            / Work Sans 400"
  echo
  echo "todas OFL/Apache, acentos pt-BR conferidos glifo a glifo."
  exit 0
fi

if par=$(pares "$1"); then
  TITULO=${par%%|*}; CORPO=${par##*|}
  echo "estilo $1 → título: ${TITULO%%:*} · corpo: ${CORPO%%:*}"
else
  TITULO="$1"; CORPO=""
fi

baixa () {                                   # $1 = "Família:pesos" → imprime o caminho do ttf
  local fam=${1%%:*} pesos=${1##*:}
  local q=${fam// /+}
  local url
  url=$(curl -sS -A "$UA" "https://fonts.googleapis.com/css2?family=${q}:wght@${pesos}" \
        | grep -oE "https://[^)]+\.ttf" | tail -1)
  [ -n "$url" ] || url=$(curl -sS -A "$UA" "https://fonts.googleapis.com/css2?family=${q}" \
        | grep -oE "https://[^)]+\.ttf" | tail -1)
  [ -n "$url" ] || { echo "  não encontrei $fam no Google Fonts" >&2; return 1; }
  local out="$DEST/${fam// /-}-${pesos%%,*}.ttf"   # peso no nome: evita o título sobrescrever o corpo
  curl -sS -o "$out" "$url"
  echo "$out"
}

ARQS=()
for f in "$TITULO" "$CORPO"; do
  [ -n "$f" ] || continue
  a=$(baixa "$f") && ARQS+=("$a")
done

# confere acentos e monta o fonts.css
python3 - "${ARQS[@]}" <<'PY'
from fontTools.ttLib import TTFont
import base64, sys, os
alvo='ÁÀÂÃÉÊÍÓÔÕÚÜÇáàâãéêíóôõúüç'
nomes=['Titulo','Corpo']; css=[]
for i,p in enumerate(sys.argv[1:]):
    t=TTFont(p); cm=t.getBestCmap()
    falta=[c for c in alvo if ord(c) not in cm]
    fam=[str(r) for r in t['name'].names if r.nameID==4][0]
    print(f"  {fam:34s} {'acentos completos' if not falta else 'FALTAM: '+''.join(falta)}")
    if falta:
        print("     → troque a fonte ou use a skill abrasileirar-fonte")
    b=open(p,'rb').read()
    css.append("@font-face{font-family:'%s';font-weight:400;font-style:normal;"
               "src:url(data:font/ttf;base64,%s) format('truetype')}"
               % (nomes[i] if i<2 else fam, base64.b64encode(b).decode()))
open('fonts.css','w').write('\n'.join(css))
print(f"  fonts.css: {os.path.getsize('fonts.css')//1024} KB — use font-family:'Titulo' e 'Corpo'")
PY
