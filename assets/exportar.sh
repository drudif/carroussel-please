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

# ── acha o navegador em vez de assumir onde ele está ──────────────────────────
# O caminho do Chrome do macOS estava cravado aqui, e isso amarrava a skill a uma
# máquina. A arte não é "gerada": ela é IMPRESSA por um navegador — é daí que vem
# a letra certa, com acento. Sem navegador não existe etapa 7, e é melhor dizer
# isso alto do que montar meia arte.
acha_navegador () {
  local c
  for c in "${CHROME:-}" \
      "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
      "/Applications/Chromium.app/Contents/MacOS/Chromium" \
      "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" \
      "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" \
      /usr/bin/google-chrome /usr/bin/google-chrome-stable \
      /usr/bin/chromium /usr/bin/chromium-browser \
      /opt/google/chrome/chrome /snap/bin/chromium; do
    [ -n "$c" ] && [ -x "$c" ] && { echo "$c"; return 0; }
  done
  for c in google-chrome google-chrome-stable chromium chromium-browser \
           chrome microsoft-edge; do
    command -v "$c" >/dev/null 2>&1 && { command -v "$c"; return 0; }
  done
  # container com Playwright instalado é o caso mais comum fora de desktop
  c=$(ls -d "$HOME"/.cache/ms-playwright/chromium-*/chrome-linux/chrome 2>/dev/null | head -1 || true)
  [ -n "$c" ] && [ -x "$c" ] && { echo "$c"; return 0; }
  return 1
}

if ! CHROME=$(acha_navegador); then
  echo "PARADO — não há navegador nesta máquina, e sem ele não sai arte."
  echo
  echo "  A arte deste carrossel não é gerada por modelo de imagem: ela é IMPRESSA."
  echo "  A skill escreve uma página com o card e um navegador tira a foto dela — é"
  echo "  por isso que a letra sai certa, com acento. Sem navegador, não há impressora."
  echo
  echo "  Procurei: Chrome, Chromium, Brave e Edge, no macOS e no Linux, no PATH e no"
  echo "  cache do Playwright."
  echo
  echo "  O QUE FAZER — e diga isto ao usuário, não monte arte pela metade:"
  echo "    · o texto, a direção e os arquivos JÁ ESTÃO prontos nesta pasta"
  echo "    · num computador com Chrome, rodar este mesmo script entrega os PNGs"
  echo "    · aqui, o que dá para entregar é o TEXTOS.md e o DIRECAO.md fechados"
  echo
  echo "  Se o navegador existe e eu não achei:   CHROME=/caminho/dele ./exportar.sh $N"
  exit 1
fi

# rodando como root — container —, o sandbox do Chrome derruba a chamada
SANDBOX=""
[ "$(id -u)" = "0" ] && SANDBOX="--no-sandbox"

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

# ── trava da conexão ──────────────────────────────────────────────────────────
# Isto já foi a trava do "nível de imagem", com três opções — e a do meio sumia em
# toda sessão de teste. A correção não foi escrever melhor: foi deixar de perguntar.
# A capacidade de gerar imagem se VERIFICA (uma chamada de balance), o resto virou
# binário, e a escolha entre banco e desenho deixou de ser pergunta para virar
# referência dentro do catálogo. Esta linha é a prova de que a catraca rodou.
DIR_MD=""
[ -f DIRECAO.md ] && DIR_MD="DIRECAO.md"
[ -f ../DIRECAO.md ] && DIR_MD="../DIRECAO.md"

CONECTOR=""
# o `|| true` não é decoração: com pipefail, o grep sem achar nada derruba o script
# inteiro — e a trava morria em silêncio, saindo com erro e sem imprimir uma linha
[ -n "$DIR_MD" ] && CONECTOR=$(grep -i '^conector:' "$DIR_MD" | head -1 | cut -d: -f2- | sed 's/^ *//' || true)

if [ -z "$CONECTOR" ]; then
  echo "PARADO — não há linha de conector no DIRECAO.md."
  echo
  if [ -z "$DIR_MD" ]; then
    echo "  Não achei DIRECAO.md. A etapa 3 devia ter gravado paleta, fontes, grade,"
    echo "  e as linhas de estilo e conector."
  else
    echo "  $DIR_MD existe mas não tem a linha 'conector:'."
  fi
  echo
  echo "  A etapa 1 é uma catraca, e ela tem duas partes:"
  echo "     1 · VERIFICAR se há gerador ligado — com uma chamada de balance, não"
  echo "         perguntando. Ferramenta que aparece na lista não é ferramenta autorizada"
  echo "     2 · não havendo, OFERECER conectar, com o passo a passo, e dizer que é a"
  echo "         forma mais rica de trabalhar. Duas respostas valem: 'me ajude a"
  echo "         conectar' e 'seguimos sem'"
  echo
  echo "  A linha do RECUSADO importa tanto quanto a do ligado — sem ela não dá para"
  echo "  distinguir 'ele não quis' de 'ninguém perguntou'. Grave uma das duas:"
  echo "     conector: higgsfield · verificado em AAAA-MM-DD"
  echo "     conector: nenhum · oferecido e recusado em AAAA-MM-DD"
  echo
  echo "  Já perguntou e só faltou gravar? FORCA=1 ./exportar.sh $N"
  [ -z "${FORCA:-}" ] && exit 1
fi

# ── trava do estilo ────────────────────────────────────────────────────────────
# A etapa 2 era a única decisão do fluxo SEM trava, e ela sumiu em produção: o
# usuário subiu uma referência, a leitura dela resolveu para um estilo, e isso foi
# tratado como escolha feita. A escolha só reapareceu no meio da montagem, como
# pergunta sobre um slide vazio — que é a assinatura de gate pulado: a decisão
# volta depois, como problema, em vez de antes, como pergunta.
# Aconteceu no app e não no IDE, porque no IDE as referências abrem e o próprio
# ato de mostrar carrega a etapa. Onde não abrem, nada segurava.
ESTILO=""
[ -n "$DIR_MD" ] && ESTILO=$(grep -i '^estilo:' "$DIR_MD" | head -1 | cut -d: -f2- | sed 's/^ *//' || true)

if [ -z "$ESTILO" ]; then
  echo "PARADO — não há estilo gravado."
  echo
  echo "  O DIRECAO.md precisa de uma linha própria:   estilo: riso · aprovado por ele"
  echo
  echo "  São SETE, fixos: brutalista · riso · terminal · colagem · neubrutal ·"
  echo "  editorial · superminimal. A conexão ordena qual catálogo abre primeiro;"
  echo "  ela não escolhe no lugar do usuário."
  echo
  echo "  E LEIA ISTO se houve referência do usuário: ler a referência RESOLVE para"
  echo "  um estilo, não ESCOLHE por ele. 'resolveu para colagem' é sugestão sua; a"
  echo "  linha 'estilo:' só se escreve depois de ele dizer sim, com essas letras."
  echo
  echo "  Já perguntou e só faltou gravar? FORCA=1 ./exportar.sh $N"
  [ -z "${FORCA:-}" ] && exit 1
fi

# ── a exceção do superminimal ─────────────────────────────────────────────────
# Este estilo é branco, preto e blocos de foto — NÃO TEM GRAFISMO NENHUM. Se o
# usuário subiu as próprias imagens, não sobra nada para o gerador fazer: a
# composição é tipografia sobre branco, que se monta em código. Rodar o laço ali
# gasta crédito para produzir o que já existe, e o gabarito ainda volta com
# imagem inventada disputando espaço com a foto dele.
FOTOS=""
[ -n "$DIR_MD" ] && FOTOS=$(grep -i '^fotos:' "$DIR_MD" | head -1 || true)
ESTILO_L=$(printf '%s' "${ESTILO:-}" | tr '[:upper:]' '[:lower:]')
SEM_LACO=""
case "$ESTILO_L" in
  superminimal*) case "$FOTOS" in *usuário*|*usuario*) SEM_LACO=1;; esac ;;
esac

# com conector ligado, o laço do gabarito é obrigatório: é a única coisa que o
# conector compra, e montar sem ele cobra crédito por um resultado sem ele
if [ -n "$CONECTOR" ] && [ -z "$SEM_LACO" ]; then
  case "$CONECTOR" in
    nenhum*|sem*|nao*|não*) ;;
    *)
      # isole o status: com pipefail, o ls falhando num glob vazio derruba o teste
      # inteiro e a trava dispara mesmo com o gabarito ali do lado
      # gfx/ está aqui porque o esqueleto usa essa pasta para grafismo e a documentação
      # também — a trava dava falso negativo em produção com as chapas lá dentro, e a
      # saída foi symlink. O glob é mais barato que a explicação.
      TEM=$(ls gabarito-*.png chapa-*.png gfx/gabarito-*.png gfx/chapa-*.png \
               ../gabarito/*.png 2>/dev/null | head -1 || true)
      if [ -z "$TEM" ]; then
        echo "PARADO — o DIRECAO.md diz que há gerador ligado e não há gabarito nenhum aqui."
        echo
        echo "  Conector não é 'ilustração gerada e colada no card'. O card inteiro nasce"
        echo "  composto pelo gerador e a tipografia entra por cima, limpa. O laço está em"
        echo "  references/geradores.md e os arquivos ficam como gabarito-NN.png e chapa-NN.png."
        echo
        echo "  Montar sem ele desperdiça a única coisa que o conector compra, e cobra crédito"
        echo "  por um resultado que não precisava dele."
        echo
        echo "  Se o laço já rodou e as chapas têm outro nome: FORCA=1 ./exportar.sh $N"
        [ -z "${FORCA:-}" ] && exit 1
      fi ;;
  esac
fi

mkdir -p out

# a porta era fixa e o bind nunca era conferido. Com dois carrosséis rodando ao mesmo
# tempo (aconteceu nos três testes de UX em paralelo), o segundo processo falhava o
# bind em silêncio e o Chrome capturava o servidor DO OUTRO — PNG do tamanho certo,
# carrossel errado, sem aviso nenhum. Ache uma porta livre e confirme antes de seguir.
achar_porta_livre () {
  local p="$1" tentativas=0
  while [ "$tentativas" -lt 20 ]; do
    if ! lsof -iTCP:"$p" -sTCP:LISTEN >/dev/null 2>&1; then echo "$p"; return 0; fi
    p=$((p + 1)); tentativas=$((tentativas + 1))
  done
  return 1
}
if PORTA=$(achar_porta_livre "$PORTA"); then :; else
  echo "PARADO — não achei porta livre a partir de $PORTA em 20 tentativas."
  exit 1
fi

python3 -m http.server "$PORTA" --directory "$RAIZ" >/dev/null 2>&1 &
SRV=$!
trap 'kill $SRV 2>/dev/null || true' EXIT
sleep 2

# confirma que É este processo quem está ouvindo a porta — não outro servidor que
# subiu entre a checagem acima e o bind (janela pequena, mas foi ela que causou o
# defeito no teste)
if ! kill -0 "$SRV" 2>/dev/null; then
  echo "PARADO — o servidor em $PORTA não subiu (kill -0 falhou logo depois do start)."
  exit 1
fi

URL="http://localhost:$PORTA/$BASE"

# 1 · erro de JS derruba a página inteira e a captura sai em branco, sem avisar
ERRO=$("$CHROME" --headless $SANDBOX --disable-gpu --virtual-time-budget=4000 --enable-logging=stderr \
  --log-level=0 --dump-dom "$URL?card=1" 2>&1 >/dev/null \
  | grep -i "uncaught" | head -3 || true)
if [ -n "$ERRO" ]; then echo "ERRO DE JS — nada foi capturado:"; echo "$ERRO"; exit 1; fi

# 2 · captura
#    NÃO acrescente --user-data-dir aqui. Com um perfil novo o Chrome roda a
#    inicialização de primeiro uso, escreve o PNG e NÃO ENCERRA — a chamada trava
#    até o timeout. Medido: sem o flag sai sozinho em 2s; com ele, nunca sai.
for i in $(seq 1 "$N"); do
  nn=$(printf "%02d" "$i")
  "$CHROME" --headless $SANDBOX --disable-gpu --hide-scrollbars --virtual-time-budget=6000 \
    --window-size=1080,1350 --screenshot="out/card-$nn.png" \
    "$URL?card=$i" >/dev/null 2>&1
  [ -n "$SAFE" ] && "$CHROME" --headless $SANDBOX --disable-gpu --hide-scrollbars \
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
import sys, os, hashlib
from collections import defaultdict
from PIL import Image, ImageStat
n = int(sys.argv[1]); alerta = 0
hashes = defaultdict(list)
for i in range(1, n+1):
    f = f'out/card-{i:02d}.png'
    if not os.path.exists(f) or os.path.getsize(f) == 0:
        print(f'  FALTOU {f}'); alerta += 1; continue
    im = Image.open(f); w, h = im.size
    if (w, h) != (1080, 1350):
        print(f'  TAMANHO ERRADO {f}: {w}x{h}'); alerta += 1; continue
    g = im.convert('L')
    # "conteúdo colado" comparava luminância absoluta (<110) contra um piso pensado
    # para papel claro — em qualquer estilo de fundo escuro (terminal, colagem sobre
    # campo escuro) o fundo sozinho já passa do piso, e a checagem dá alerta em TODO
    # card, sempre, mesmo vazio. A referência agora é a própria imagem: compara a
    # faixa dos 8px finais contra uma faixa de fundo 40–60px acima (mesma cor de
    # papel, sem conteúdo esperado ali). Fundo uniforme — claro ou escuro — tem
    # desvio-padrão ~0 nas duas faixas; letra, fio ou bloco de tinta invadindo o pé
    # cria contraste local (std alto) ou muda a média (a faixa deixa de ser só fundo).
    alvo = g.crop((0, h-8, w, h))
    ref = g.crop((0, h-60, w, h-40))
    media_alvo, media_ref = ImageStat.Stat(alvo).mean[0], ImageStat.Stat(ref).mean[0]
    std_alvo = ImageStat.Stat(alvo).stddev[0]
    if std_alvo > 15 or abs(media_alvo - media_ref) > 40:
        print(f'  conteúdo colado no pé: {f}  (desvio {std_alvo:.0f}, faixa {media_alvo:.0f} vs fundo {media_ref:.0f})')
        alerta += 1
    hashes[hashlib.md5(open(f, 'rb').read()).hexdigest()].append(f)
# PNGs byte a byte idênticos são o defeito que passou pelas checagens acima num dos
# testes de UX: o servidor serviu a pasta ERRADA (outro processo na mesma porta), a
# captura saiu do tamanho certo e em branco, e "ok" foi o que a conferência disse. Card
# 1 igual ao 2 também pega captura que travou e devolveu a MESMA tela pros dois.
for h_, fs in hashes.items():
    if len(fs) > 1:
        print(f'  IDÊNTICOS byte a byte, provável captura da pasta errada: {", ".join(fs)}')
        alerta += 1
print('  conferência automática: ok' if not alerta else f'  {alerta} ponto(s) para olhar')
PY

# 4 · o PDF de cada destino
#    Instagram é 4:5. O LinkedIn é QUADRADO, e sai do recorte central do mesmo PNG.
#    Não rediagrame: o recorte só entrega margem se a margem tiver sido reservada na
#    diagramação — a área viva é o quadrado de 924x924 em x78..1002, y213..1137. Card
#    diagramado com o texto em y=150 sai com 15px de respiro na página do LinkedIn, e
#    nao ha nada que a exportacao possa fazer por ele.
#
#    Qual PDF montar vem da linha `destino:` do DIRECAO.md — sem ela, os dois, que é o
#    comportamento de sempre. Nos três testes de UX em paralelo, "só Instagram" foi
#    apagado à mão porque não havia onde essa decisão morar; agora mora aqui.
DESTINO=""
[ -n "$DIR_MD" ] && DESTINO=$(grep -i '^destino:' "$DIR_MD" | head -1 | cut -d: -f2- | sed 's/^ *//' | tr '[:upper:]' '[:lower:]' || true)
QUER_IG=1; QUER_LI=1
case "$DESTINO" in
  instagram) QUER_LI="" ;;
  linkedin)  QUER_IG="" ;;
esac

python3 - "$N" "$QUER_IG" "$QUER_LI" <<'PY'
import sys, os
from PIL import Image
n, quer_ig, quer_li = int(sys.argv[1]), sys.argv[2], sys.argv[3]
pngs = [f'out/card-{i:02d}.png' for i in range(1, n+1)]
v = [Image.open(p).convert('RGB') for p in pngs]

if quer_ig:
    v[0].save('carrossel-1080x1350.pdf', save_all=True, append_images=v[1:], resolution=150.0)
if quer_li:
    q = [im.crop((0, 135, 1080, 1215)) for im in v]
    q[0].save('carrossel-linkedin-1080.pdf', save_all=True, append_images=q[1:], resolution=150.0)

for f, quer in (('carrossel-1080x1350.pdf', quer_ig), ('carrossel-linkedin-1080.pdf', quer_li)):
    if quer:
        print(f'  {f} — {n} páginas, {os.path.getsize(f)//1024} KB')
    else:
        print(f'  {f} — não montado (fora do destino declarado)')
PY

echo
echo "Pronto. AGORA ABRA CADA PNG E OLHE — a conferência automática não vê"
echo "linha de título colidindo, palavra que o erro de registro tornou ilegível,"
echo "nem grafismo cobrindo o texto de outro grafismo."
[ -n "$SAFE" ] || echo "Rode com 'safe' se quiser as guias do corte 1:1 desenhadas por cima."
