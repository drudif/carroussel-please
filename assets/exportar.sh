#!/usr/bin/env bash
# Captura os cards em PNG e monta o PDF sequencial.
#   ./exportar.sh              8 cards, pasta atual
#   ./exportar.sh 10           10 cards
#   ./exportar.sh 10 safe      + gabarito de área de segurança em _safe-NN.png
set -euo pipefail

N=${1:-8}
SAFE=${2:-}
PORTA=${PORTA:-8910}
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
[ -x "$CHROME" ] || { echo "Chrome não encontrado em: $CHROME"; exit 1; }
[ -f cards.html ] || { echo "cards.html não está nesta pasta"; exit 1; }

mkdir -p out
python3 -m http.server "$PORTA" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true' EXIT
sleep 2

# 1 · erro de JS derruba a página inteira e a captura sai em branco, sem avisar
ERRO=$("$CHROME" --headless --disable-gpu --virtual-time-budget=4000 --enable-logging=stderr \
  --log-level=0 --dump-dom "http://localhost:$PORTA/cards.html?card=1" 2>&1 >/dev/null \
  | grep -i "uncaught" | head -3 || true)
if [ -n "$ERRO" ]; then echo "ERRO DE JS — nada foi capturado:"; echo "$ERRO"; exit 1; fi

# 2 · captura
for i in $(seq 1 "$N"); do
  nn=$(printf "%02d" "$i")
  "$CHROME" --headless --disable-gpu --hide-scrollbars --virtual-time-budget=6000 \
    --window-size=1080,1350 --screenshot="out/card-$nn.png" \
    "http://localhost:$PORTA/cards.html?card=$i" >/dev/null 2>&1
  [ -n "$SAFE" ] && "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --virtual-time-budget=6000 --window-size=1080,1350 --screenshot="out/_safe-$nn.png" \
    "http://localhost:$PORTA/cards.html?card=$i&safe=1" >/dev/null 2>&1
  echo "  card-$nn.png"
done

# 3 · conferência: tamanho certo, arquivo não vazio, nada colado no pé
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

# 4 · PDF sequencial para o LinkedIn
python3 - "$N" <<'PY'
import sys
from PIL import Image
n = int(sys.argv[1])
ims = [Image.open(f'out/card-{i:02d}.png').convert('RGB') for i in range(1, n+1)]
ims[0].save('carrossel-linkedin.pdf', save_all=True, append_images=ims[1:], resolution=150.0)
import os; print(f'  carrossel-linkedin.pdf — {n} páginas, {os.path.getsize("carrossel-linkedin.pdf")//1024} KB')
PY

echo
echo "Pronto. AGORA ABRA CADA PNG E OLHE — a conferência automática não vê"
echo "linha de título colidindo nem palavra que o erro de registro tornou ilegível."
