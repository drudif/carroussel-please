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
  bauhaus)      echo "Archivo Black:400|Archivo:400,700";;
  brutalismo)   echo "Space Mono:700|Space Mono:400";;
  popart)       echo "Bungee:400|Archivo:400,700";;
  utilitario)   echo "IBM Plex Sans:700|IBM Plex Mono:400";;
  midcentury)   echo "Poppins:700|DM Sans:400";;
  neobrutalismo) echo "Space Grotesk:700|Space Grotesk:400";;
  suico)        echo "Inter:900|Inter:400";;
  memphis)      echo "Rubik Mono One:400|Rubik:400,700";;
  janelas)      echo "Archivo Black:400|Space Mono:400";;
  vaporwave)    echo "VT323:400|Space Mono:400";;
  pontilhismo)  echo "Playfair Display:900|Newsreader:400";;
  mixedmedia)   echo "Alfa Slab One:400|Libre Baskerville:400";;
  kawaii)       echo "Fredoka:600|Nunito:400";;
  wabisabi)     echo "Cormorant Garamond:700|Karla:400";;
  rebus)        echo "Inter:700|Inter:400";;
  y2k)          echo "Bungee:400|Space Grotesk:400";;
  *) return 1;;
esac; }

if [ "${1:-}" = "--listar" ] || [ $# -eq 0 ]; then
  echo "estilos:  bauhaus brutalismo popart utilitario midcentury neobrutalismo"
  echo "          suico memphis janelas vaporwave pontilhismo mixedmedia"
  echo "          kawaii wabisabi rebus y2k"
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
