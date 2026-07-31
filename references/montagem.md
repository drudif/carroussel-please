# Montagem e exportação

Um único HTML com todos os cards, controlado por `?card=N`. Chrome headless captura cada um em PNG. O PDF sai dos PNGs.

## O arquivo único

```js
const qs = new URLSearchParams(location.search);
const q  = qs.get('card');
document.getElementById('root').innerHTML =
  q ? CARDS[+q-1]() : CARDS.map(f => f()).join('');
```

Sem `?card=` você vê a folha de contato inteira e revisa o **ritmo** do carrossel — se nada muda de posição ou escala entre os cards, ele é uma parede. Com `?card=3` você captura o card 3 sozinho, no pixel exato.

## Empilhamento rígido

O texto reserva a altura de que precisa; o grafismo fica com o que sobra. Isso torna sobreposição impossível por construção, em vez de virar um ajuste que se refaz a cada mudança de texto:

```css
.card{display:flex;flex-direction:column;padding:var(--SY) var(--M);
      width:1080px;height:1350px;overflow:hidden;position:relative}
.head{flex:0 0 auto}
.txt {flex:0 0 auto}                        /* cresce com o conteúdo */
.gfx {flex:1 1 auto;min-height:0;overflow:hidden;
      margin:38px calc(var(--M) * -1) 30px} /* sangra nas laterais */
.foot{flex:0 0 auto}
```

Título pode atravessar a arte — o contraste é grande e funciona como pôster. **Corpo de texto, nunca.**

## Fonte local

Duas rotas. Escolha uma e não misture:

**Página em `file://`** — `@font-face` com caminho absoluto e a flag `--allow-file-access-from-files`.

**Página em `http://localhost`** — a fonte precisa vir do mesmo esquema. **Página servida por HTTP não carrega subrecurso `file://`, com flag ou sem.** O navegador cai no fallback **em silêncio**: a arte renderiza inteira com a fonte errada, sem erro no console e sem nada quebrado na tela. É o erro mais caro deste fluxo, porque parece que funcionou.

A rota à prova disso é embutir em base64:

```python
import base64
faces = []
for nome, arq in [('Titulo','XanhMono-Regular.ttf'), ('Corpo','CascadiaMono.ttf')]:
    b = open(f'/Users/você/Library/Fonts/{arq}','rb').read()
    faces.append("@font-face{font-family:'%s';font-weight:400;font-style:normal;"
                 "src:url(data:font/ttf;base64,%s) format('truetype')}"
                 % (nome, base64.b64encode(b).decode()))
open('fonts.css','w').write('\n'.join(faces))
```

Confirme que carregou, sem confiar na aparência:

```js
document.fonts.ready.then(() => console.log(document.fonts.check("64px 'Titulo'")));
```

`false` significa fallback. Para **página web publicada** (não para captura), reduza a fonte aos glifos usados com `fontTools.subset` e salve em woff2 — costuma cair de 1 MB para menos de 40 KB, o que importa quando alguém abre no celular.

## Captura

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
python3 -m http.server 8910 >/dev/null 2>&1 & SRV=$!
sleep 2
for n in 1 2 3 4 5 6 7 8; do
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --virtual-time-budget=6000 --window-size=1080,1350 \
    --screenshot="out/card-0$n.png" "http://localhost:8910/cards.html?card=$n" >/dev/null 2>&1
done
kill $SRV
```

`--virtual-time-budget` espera fonte, imagem e layout assentarem. Curto demais captura a página pela metade.

### Armadilhas verificadas

**Chrome headless tem largura mínima de viewport de 500px.** Capturar com `--window-size=390,...` renderiza a 500 e **recorta** para 390 — o resultado parece conteúdo estourando a margem, mas é corte de captura. Para conferir layout estreito de verdade, meça em vez de olhar:

```js
document.title = 'VP=' + document.documentElement.clientWidth +
                 ' SCROLL=' + document.documentElement.scrollWidth;
```

Iguais, nada estoura.

**`const chrome` quebra o script inteiro.** `window.chrome` já existe no navegador; redeclarar dá `SyntaxError: Identifier 'chrome' has already been declared` e o `#root` fica vazio — a página sai em branco sem nenhum aviso. Vale para qualquer nome que o navegador já use.

**Erro de JS só aparece se você for buscar.** A captura entrega um PNG do tamanho certo, em branco:

```bash
"$CHROME" --headless --disable-gpu --enable-logging=stderr --log-level=0 \
  --dump-dom "http://localhost:8910/cards.html?card=2" 2>&1 >/dev/null | grep -i uncaught
```

**No zsh, variável não citada não se separa em palavras.** `for r in $LISTA` itera **uma vez** com a string inteira. Use lista literal, array, ou `${=LISTA}`.

**CSS por caminho absoluto quebra em `file://`.** `href="/style.css"` resolve para a raiz do disco. Sirva a pasta com `python3 -m http.server`.

**Deploy protegido devolve 403.** Peça um print ao usuário. Se ele mandar a URL com o parâmetro de acesso, use e **avise que o segredo precisa ser rotacionado** — o que passa pelo chat fica no chat.

**App pesado estoura o tempo.** Rode em background e com `--user-data-dir` num diretório temporário.

## Conferência automática

Não substitui olhar, mas pega o que o olho cansado deixa passar:

```python
from PIL import Image
for n in range(1, 9):
    im = Image.open(f'out/card-0{n}.png'); w, h = im.size
    assert (w, h) == (1080, 1350), f'card {n}: {w}x{h}'
    g = im.convert('L')
    esc = sum(1 for p in g.crop((0, h-8, w, h)).getdata() if p < 110)
    print(f'card-0{n}: ok', '← conteúdo colado no pé' if esc > 400 else '')
```

Depois disso, **abra cada PNG e olhe**. As duas coisas que só aparecem olhando: linha de título colidindo com a de baixo, e palavra que o erro de registro tornou ilegível.

## Área de segurança

Se o post vai ser impulsionado, todo conteúdo essencial fica dentro do **corte 1:1 central** — em 1080×1350, entre y=135 e y=1215. É o corte que o Explore aplica, e é o mais agressivo que o material encontra.

Gabarito por query, para conferir sem adivinhar:

```js
const GUIA = qs.get('safe') ? `
  <div style="position:absolute;left:0;right:0;top:135px;height:1080px;
       border:2px dashed #E11;z-index:99;pointer-events:none"></div>
  <div style="position:absolute;left:78px;right:78px;top:146px;bottom:146px;
       border:2px dashed #0A0;z-index:99;pointer-events:none"></div>` : '';
```

Capture uma série com `&safe=1` e guarde como `_safe-0N.png`. Vermelho é o corte 1:1; verde é a margem confortável.

## PDF para LinkedIn

```python
from PIL import Image
paginas = [f'out/card-0{n}.png' for n in range(1, 9)]
ims = [Image.open(p).convert('RGB') for p in paginas]
ims[0].save('carrossel-linkedin.pdf', save_all=True, append_images=ims[1:],
            resolution=150.0, title='<título>', author='<autor>')
```

`resolution=150` dá páginas de 7,20 × 9,00 polegadas a partir de 1080×1350, mantendo o 4:5 exato. O LinkedIn aceita até 300 páginas e 100 MB.

Confira a estrutura sem depender de biblioteca extra:

```python
import re
b = open('carrossel-linkedin.pdf','rb').read()
print('páginas:', len(re.findall(rb'/Type\s*/Page[^s]', b)))
print('imagens:', len(re.findall(rb'/Subtype\s*/Image', b)))
mb = [float(x) for x in re.findall(rb'/MediaBox\s*\[([^\]]+)\]', b)[0].split()]
print(f'proporção: {mb[2]/mb[3]:.3f}')
print('trailer ok:', b.rstrip().endswith(b'%%EOF'))
```

O feed do LinkedIn é mais largo e reduz o documento, então corpo abaixo de 30px sobre 1080 fica no limite de leitura. Se o carrossel for prioritariamente para lá, suba os corpos antes de exportar.

## Entrelinha em pt-BR — o piso é calculado, não estimado

Título em caixa alta com entrelinha apertada fica lindo em inglês e **quebra em português**: o til
do `Ã` e o agudo do `Ó` sobem acima da altura da linha e batem na letra de cima. Não lê como erro
de espaçamento — lê como sujeira, e o leitor não sabe dizer o que está errado.

`baixar-fontes.sh` calcula o piso de cada face e grava em `fonts.css`:

```css
h1 { line-height: var(--lh-titulo) }
```

Use a variável, nunca um número escolhido a olho. A tabela dos seis estilos está em
[estilos.md](estilos.md).

**A conferência:** renderize o título com `ÃÕÇ` e `Ó` em linhas seguidas, amplie o PNG a 200% e
olhe a junção. Se o acento encosta na letra de cima, encosta — 1px de folga ainda lê como colisão.

## Grafismo se ancora na zona, não em pixel

A zona de grafismo é o que sobra depois do bloco de texto, e **ela muda de altura quando o título
reflui** — trocar uma palavra, corrigir a entrelinha ou mudar o corpo já desloca tudo. Grafismo
posicionado em pixel absoluto sobra pela borda ou deixa um terço do card vazio.

Ancore em porcentagem da zona, ou em `bottom`:

```css
.gfx > .bloco   { top: 0;    height: 62% }
.gfx > .rodape  { top: 66%;  bottom: 0   }   /* absorve qualquer sobra */
```

O último elemento de cada zona sempre em `bottom:0`. É ele que absorve a diferença.
