#!/usr/bin/env bash
# Captura os cards em PNG, confere e monta os dois PDFs.
#   ./exportar.sh              8 cards, pasta atual
#   ./exportar.sh 10           10 cards
#   ./exportar.sh 10 safe      + gabarito de área de segurança em _safe-NN.png
#
# Rode de dentro da pasta que tem o cards.html.
set -euo pipefail

N=${1:-8}
SAFE=${2:-}
PORTA=${PORTA:-8910}
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
[ -x "$CHROME" ] || { echo "Chrome não encontrado em: $CHROME"; exit 1; }
[ -f cards.html ] || { echo "cards.html não está nesta pasta"; exit 1; }

# O HTML lê o TEXTOS.md com fetch('../TEXTOS.md'). Servir só a pasta da arte põe o
# arquivo FORA do escopo do servidor e o fetch devolve 404 sem explicar — então
# quando o .md está um nível acima, quem é servida é a pasta do trabalho inteira.
if [ -f ../TEXTOS.md ]; then
  RAIZ=".."
  BASE="$(basename "$PWD")/cards.html"
else
  RAIZ="."
  BASE="cards.html"
fi

# ── trava do nível de imagem ───────────────────────────────────────────────────
# Quatro testes seguidos falharam pelo mesmo motivo: a decisão da etapa 2 não
# sobreviveu até aqui — ou porque a pergunta nunca foi feita, ou porque foi feita
# com duas opções em vez de três. Prosa não segurou. Isto segura, porque roda
# sempre e é a última coisa entre a arte e a entrega.
DIR_MD=""
[ -f DIRECAO.md ] && DIR_MD="DIRECAO.md"
[ -f ../DIRECAO.md ] && DIR_MD="../DIRECAO.md"

NIVEL=""
# o `|| true` não é decoração: com pipefail, o grep sem achar nada derruba o script
# inteiro — e a trava morria em silêncio, saindo com erro e sem imprimir uma linha
[ -n "$DIR_MD" ] && NIVEL=$(grep -i '^imagem:' "$DIR_MD" | head -1 | cut -d: -f2- | tr -d ' ' || true)

if [ -z "$NIVEL" ]; then
  echo "PARADO — não há nível de imagem gravado."
  echo
  if [ -z "$DIR_MD" ]; then
    echo "  Não achei DIRECAO.md. A etapa 3 devia ter gravado: paleta, fontes, grade"
    echo "  e a linha do nível de imagem."
  else
    echo "  $DIR_MD existe mas não tem a linha 'imagem:'."
  fi
  echo
  echo "  A etapa 2 pergunta como as imagens do carrossel são feitas, e tem TRÊS"
  echo "  opções — não duas:"
  echo "     1 · feitas sob medida por um gerador conectado"
  echo "     2 · de banco aberto (Dupe, Openverse) — não conecta nada"
  echo "     3 · sem foto nenhuma, tudo desenhado em código"
  echo
  echo "  A opção 2 é a que some sozinha. Se você não fez essa pergunta ao usuário,"
  echo "  faça agora: montar sem ela é escolher no lugar dele."
  echo
  echo "  Depois grave no DIRECAO.md, uma linha:   imagem: 2 · dupe + openverse"
  echo
  echo "  Já perguntou e só faltou gravar? FORCA=1 ./exportar.sh $N"
  [ -z "${FORCA:-}" ] && exit 1
fi

if [ -n "$NIVEL" ]; then
  case "$NIVEL" in
    1*|gerador*)
      # isole o status: com pipefail, o ls falhando num glob vazio derruba o teste
      # inteiro e a trava dispara mesmo com o gabarito ali do lado
      TEM=$(ls gabarito-*.png chapa-*.png ../gabarito/*.png 2>/dev/null | head -1 || true)
      if [ -z "$TEM" ]; then
        echo "PARADO — o DIRECAO.md diz nível 1 (gerador ligado) e não há gabarito nenhum aqui."
        echo
        echo "  Nível 1 não é 'ilustração gerada e colada no card'. O card inteiro nasce"
        echo "  composto pelo gerador e a tipografia entra por cima, limpa. O laço está em"
        echo "  references/geradores.md e os arquivos ficam como gabarito-NN.png e chapa-NN.png."
        echo
        echo "  Montar sem ele desperdiça a única coisa que o nível 1 compra, e cobra crédito"
        echo "  por um resultado de nível 2."
        echo
        echo "  Se o laço já rodou e as chapas têm outro nome: FORCA=1 ./exportar.sh $N"
        [ -z "${FORCA:-}" ] && exit 1
      fi ;;
  esac
fi

mkdir -p out
python3 -m http.server "$PORTA" --directory "$RAIZ" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true' EXIT
sleep 2

URL="http://localhost:$PORTA/$BASE"

# 1 · erro de JS derruba a página inteira e a captura sai em branco, sem avisar
ERRO=$("$CHROME" --headless --disable-gpu --virtual-time-budget=4000 --enable-logging=stderr \
  --log-level=0 --dump-dom "$URL?card=1" 2>&1 >/dev/null \
  | grep -i "uncaught" | head -3 || true)
if [ -n "$ERRO" ]; then echo "ERRO DE JS — nada foi capturado:"; echo "$ERRO"; exit 1; fi

# 2 · captura
#    NÃO acrescente --user-data-dir aqui. Com um perfil novo o Chrome roda a
#    inicialização de primeiro uso, escreve o PNG e NÃO ENCERRA — a chamada trava
#    até o timeout. Medido: sem o flag sai sozinho em 2s; com ele, nunca sai.
for i in $(seq 1 "$N"); do
  nn=$(printf "%02d" "$i")
  "$CHROME" --headless --disable-gpu --hide-scrollbars --virtual-time-budget=6000 \
    --window-size=1080,1350 --screenshot="out/card-$nn.png" \
    "$URL?card=$i" >/dev/null 2>&1
  [ -n "$SAFE" ] && "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --virtual-time-budget=6000 --window-size=1080,1350 --screenshot="out/_safe-$nn.png" \
    "$URL?card=$i&safe=1" >/dev/null 2>&1
  echo "  card-$nn.png"
done

# 3 · conferência: tamanho certo, arquivo não vazio, nada colado no pé
#     Não dá para conferir a área de segurança contando pixel: grão, fibra e imagem
#     sangrada mudam a faixa descartada tanto quanto conteúdo mudaria — medido, 99,97%
#     dos pixels fora do corte e 99,67% dos de dentro desviam igual. Para isso existe
#     o `safe`, que desenha as guias no PNG para você olhar.
python3 - "$N" <<'PY'
import sys, os
from PIL import Image
n = int(sys.argv[1]); alerta = 0
for i in range(1, n+1):
    f = f'out/card-{i:02d}.png'
    if not os.path.exists(f) or os.path.getsize(f) == 0:
        print(f'  FALTOU {f}'); alerta += 1; continue
    im = Image.open(f); w, h = im.size
    if (w, h) != (1080, 1350):
        print(f'  TAMANHO ERRADO {f}: {w}x{h}'); alerta += 1; continue
    g = im.convert('L')
    esc = sum(1 for p in g.crop((0, h-8, w, h)).getdata() if p < 110)
    if esc > 400:
        print(f'  conteúdo colado no pé: {f}'); alerta += 1
print('  conferência automática: ok' if not alerta else f'  {alerta} ponto(s) para olhar')
PY

# 4 · os dois PDFs
#    Instagram é 4:5. O LinkedIn é QUADRADO, e sai do recorte central do mesmo PNG.
#    Não rediagrame: o recorte só entrega margem se a margem tiver sido reservada na
#    diagramação — a área viva é o quadrado de 924x924 em x78..1002, y213..1137. Card
#    diagramado com o texto em y=150 sai com 15px de respiro na página do LinkedIn, e
#    nao ha nada que a exportacao possa fazer por ele.
python3 - "$N" <<'PY'
import sys, os
from PIL import Image
n = int(sys.argv[1])
pngs = [f'out/card-{i:02d}.png' for i in range(1, n+1)]

v = [Image.open(p).convert('RGB') for p in pngs]
v[0].save('carrossel-1080x1350.pdf', save_all=True, append_images=v[1:], resolution=150.0)

q = [im.crop((0, 135, 1080, 1215)) for im in v]
q[0].save('carrossel-linkedin-1080.pdf', save_all=True, append_images=q[1:], resolution=150.0)

for f in ('carrossel-1080x1350.pdf', 'carrossel-linkedin-1080.pdf'):
    print(f'  {f} — {n} páginas, {os.path.getsize(f)//1024} KB')
PY

echo
echo "Pronto. AGORA ABRA CADA PNG E OLHE — a conferência automática não vê"
echo "linha de título colidindo, palavra que o erro de registro tornou ilegível,"
echo "nem grafismo cobrindo o texto de outro grafismo."
[ -n "$SAFE" ] || echo "Rode com 'safe' se quiser as guias do corte 1:1 desenhadas por cima."
