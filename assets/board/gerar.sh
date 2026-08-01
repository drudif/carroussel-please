#!/usr/bin/env bash
# Gera assets/board-niveis.png a partir do board.html. Rode de dentro de assets/board/.
#   ./gerar.sh
set -euo pipefail
CHROME=${CHROME:-"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"}
PORTA=${PORTA:-8951}
python3 -m http.server "$PORTA" --directory .. >/dev/null 2>&1 &
SRV=$!; trap 'kill $SRV 2>/dev/null || true' EXIT
sleep 1.5
# O --screenshot captura o VIEWPORT, não a página: com altura fixa o board sai cortado
# em silêncio. Mede a altura do documento primeiro e captura com ela.
ALT=$("$CHROME" --headless --disable-gpu --virtual-time-budget=8000 \
  --dump-dom "http://localhost:$PORTA/board/board.html?medir=1" 2>/dev/null \
  | grep -oE '<i id="?alt"?>[0-9]+' | grep -oE '[0-9]+$' || echo 0)
# fallback silencioso é o que fez o board sair cortado da primeira vez: o dump-dom
# devolve o atributo com aspas, o grep não casou, e a altura padrão passou por certa
[ "${ALT:-0}" -gt 1000 ] || { echo "NÃO MEDI a altura da página — abortando para não gerar board cortado"; exit 1; }
echo "  altura medida: ${ALT}px"
"$CHROME" --headless --disable-gpu --hide-scrollbars --virtual-time-budget=8000 \
  --window-size=1600,"$ALT" --screenshot="/tmp/board-niveis.png" \
  "http://localhost:$PORTA/board/board.html" >/dev/null 2>&1
python3 - <<'PY'
from PIL import Image
import os
# JPG, não PNG: 1600 de largura com fotograma dentro dá 1,4 MB em PNG e 0,7 em JPG,
# e o board vai para dentro do repositório da skill
im = Image.open("/tmp/board-niveis.png").convert("RGB")
im.save("../board-niveis.jpg", quality=92, optimize=True)
print(f"  board-niveis.jpg  {im.size[0]}x{im.size[1]}  {os.path.getsize('../board-niveis.jpg')//1024} KB")
PY
