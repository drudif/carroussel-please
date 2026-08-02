#!/usr/bin/env bash
# Gera o fonts.css de um estilo, com as faces embutidas em base64.
#   ./fontes.sh riso               o par do estilo, LIDO DO DISCO — sem rede
#   ./fontes.sh --listar           mostra os estilos disponíveis
#   ./fontes.sh "Space Mono:700"   baixa uma família avulsa do Google Fonts
#
# As 15 faces dos sete estilos moram em assets/fontes/, todas OFL, com a licença de
# cada família ao lado. Elas são EMBUTIDAS, não baixadas, por um motivo que não é
# conveniência: o piso de entrelinha e o comprimento de linha do laço do gabarito são
# CALCULADOS A PARTIR DO ARQUIVO. Uma revisão da fonte no Google não quebra nada — ela
# só faz esses números passarem a ser outros, em silêncio, num sistema que existe para
# eles serem estáveis entre os oito cards. Além disso o download dependia de mandar um
# User-Agent antigo para a API devolver TTF em vez de woff2, que é comportamento não
# documentado: no dia em que parar, a etapa 7 morre com o usuário esperando.
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FONTES="$AQUI/fontes"
UA="Mozilla/5.0 (Windows NT 6.1; WOW64)"     # UA antigo faz a API devolver TTF
DEST=${DEST:-.}

pares () { case "$1" in
  brutalista)  echo "Anton:400|IBM Plex Mono:400";;
  riso)        echo "Antonio:700|Newsreader:400";;
  riso-imagem) echo "Bricolage Grotesque:800|Newsreader:400";;
  terminal)    echo "Cascadia Mono:300|Cascadia Mono:400";;
  iridescente) echo "Hanken Grotesk:500|Hanken Grotesk:400";;
  colagem)     echo "Bodoni Moda:900|Karla:400";;
  neubrutal)   echo "Chivo:900|Chivo Mono:400";;
  editorial)   echo "Fraunces:700|Work Sans:400";;
  *) return 1;;
esac; }

if [ "${1:-}" = "--listar" ] || [ $# -eq 0 ]; then
  echo "estilos (embutidos em assets/fontes/, sem rede):"
  echo "  brutalista   Anton 400               / IBM Plex Mono 400"
  echo "  riso         Antonio 700             / Newsreader 400"
  echo "  riso-imagem  Bricolage Grotesque 800 / Newsreader 400"
  echo "  terminal     Cascadia Mono 300       / Cascadia Mono 400"
  echo "  iridescente  Hanken Grotesk 500      / Hanken Grotesk 400"
  echo "  colagem      Bodoni Moda 900         / Karla 400"
  echo "  neubrutal    Chivo 900               / Chivo Mono 400"
  echo "  editorial    Fraunces 700            / Work Sans 400"
  echo
  echo "  riso-imagem é para imagem passando POR BAIXO DO TIPO — colagem, foto tratada"
  echo "  sangrando atrás das letras. NÃO é o caso do laço do gabarito, onde o tipo cai"
  echo "  em zona chapada declarada: ali o par é 'riso', com Antonio. Ver estilos.md."
  echo
  echo "todas OFL, licença em assets/fontes/LICENCA-<familia>.txt,"
  echo "acentos pt-BR conferidos glifo a glifo."
  exit 0
fi

# ── resolve o par: do disco quando é estilo, da rede quando é família avulsa ────
arquivo_local () {                           # $1 = "Família:peso" → caminho, ou vazio
  local fam=${1%%:*} peso=${1##*:}
  local f="$FONTES/${fam// /-}-${peso}.ttf"
  [ -f "$f" ] && echo "$f"
}

baixa () {                                   # só para família avulsa (fonte de marca)
  local fam=${1%%:*} pesos=${1##*:}
  local q=${fam// /+} url
  url=$(curl -sS -A "$UA" "https://fonts.googleapis.com/css2?family=${q}:wght@${pesos}" \
        | grep -oE "https://[^)]+\.ttf" | tail -1)
  [ -n "$url" ] || url=$(curl -sS -A "$UA" "https://fonts.googleapis.com/css2?family=${q}" \
        | grep -oE "https://[^)]+\.ttf" | tail -1)
  [ -n "$url" ] || { echo "  não encontrei $fam no Google Fonts" >&2; return 1; }
  local out="$DEST/${fam// /-}-${pesos%%,*}.ttf"
  curl -sS -o "$out" "$url"
  echo "$out"
}

if par=$(pares "$1"); then
  TITULO=${par%%|*}; CORPO=${par##*|}
  echo "estilo $1 → título: ${TITULO%%:*} · corpo: ${CORPO%%:*}   (do disco, sem rede)"
else
  TITULO="$1"; CORPO=""
  echo "família avulsa: ${TITULO%%:*} — baixando. Confira os acentos no que voltar."
fi

ARQS=()
for f in "$TITULO" "$CORPO"; do
  [ -n "$f" ] || continue
  if a=$(arquivo_local "$f"); then ARQS+=("$a")
  elif a=$(baixa "$f"); then ARQS+=("$a")
  else exit 1; fi
done

# ── acentos, pisos de entrelinha, fonts.css ────────────────────────────────────
python3 - "${ARQS[@]}" <<'PY'
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
import base64, sys, os, math

ALVO   = 'ÁÀÂÃÉÊÍÓÔÕÚÜÇáàâãéêíóôõúüç'
ACENTO = 'ÃÕÁÀÂÉÊÍÓÔÚÜ'   # o que sobe acima da caixa alta
OVER   = 'SOCGU'          # transbordo óptico da caixa alta abaixo da linha de base
DESC   = 'QJÇ'            # descendentes de verdade

# Duas folgas, e a diferença entre elas é a lição inteira desta trava.
#
# FOLGA resolve COLISÃO: acento da linha de baixo contra a letra de cima. 1px de gap
# ainda lê como encosto, então 0,04em basta.
#
# FOLGA_Q resolve LEITURA, que é outro problema. A cauda de Ç, Q ou J não precisa
# encostar para estragar a palavra: basta pousar SOBRE uma letra da linha de baixo, e
# ela vira o acento dela. Medido num PNG entregue: com 0,04 a folga era de 3px e
# "NA PISTA" leu "NA PISTÁ" por causa do Ç de "ALMOÇO" logo acima. Com 0,24 são 18px
# e a cauda volta a pertencer à palavra de cima. Não encostar não é o critério.
FOLGA   = 0.04
FOLGA_Q = 0.24

nomes=['Titulo','Corpo']; css=[]; lh={}
for i,p in enumerate(sys.argv[1:]):
    t=TTFont(p); cm=t.getBestCmap(); gs=t.getGlyphSet(); u=t['head'].unitsPerEm
    fam=[str(r) for r in t['name'].names if r.nameID==4][0]

    falta=[c for c in ALVO if ord(c) not in cm]
    print(f"  {fam:34s} {'acentos completos' if not falta else 'FALTAM: '+''.join(falta)}")
    if falta:
        print("     → troque a fonte ou use a skill abrasileirar-fonte")

    def lim(chars, idx, fn):
        v=0
        for c in chars:
            g=cm.get(ord(c))
            if not g: continue
            bp=BoundsPen(gs)
            try: gs[g].draw(bp)
            except Exception: continue
            if bp.bounds: v=fn(v, bp.bounds[idx])
        return v/u
    sobe = lim(ACENTO,3,max); over = lim(OVER,1,min); desc = lim(DESC,1,min)
    piso  = math.ceil((sobe-over+FOLGA)*100)/100
    pisoQ = math.ceil((sobe-desc+FOLGA_Q)*100)/100
    nome = nomes[i] if i<2 else fam
    lh[nome] = piso; lh[nome+'-q'] = pisoQ
    print(f"     entrelinha mínima em caixa alta: {piso}  ·  {pisoQ} com Q, J ou Ç na linha de cima")

    b=open(p,'rb').read()
    css.append("@font-face{font-family:'%s';font-weight:400;font-style:normal;"
               "src:url(data:font/ttf;base64,%s) format('truetype')}"
               % (nome, base64.b64encode(b).decode()))

css.insert(0, ':root{' + ''.join(f'--lh-{k.lower()}:{v};' for k,v in lh.items()) + '}')
open('fonts.css','w').write('\n'.join(css))
print(f"  fonts.css: {os.path.getsize('fonts.css')//1024} KB — font-family:'Titulo' e 'Corpo'")
print( "             titulo: line-height:var(--lh-titulo). O esqueleto troca sozinho para")
print( "             var(--lh-titulo-q) na linha que tiver Ç, Q ou J — não faça isso na mão,")
print( "             e NÃO recalcule por string: o piso publicado já é o pior caso da família.")
print( "             corpo: diagrame entre 1.35 e 1.45 (--lh-corpo é conferência, não uso)")
PY
