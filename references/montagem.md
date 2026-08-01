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

### `--user-data-dir` faz o Chrome não encerrar — a armadilha mais cara

**Leia esta antes das outras.** Com um perfil novo, o Chrome roda a inicialização de primeiro
uso, **escreve o PNG e não encerra**. A chamada de bash fica presa até o timeout, e o sintoma
engana: o arquivo chega em ~4s e está correto, então quem não olhar o disco conclui que a
captura falhou e vai depurar a página.

Medido nesta máquina, mesma URL, mesmo Chrome:

| | tempo |
|---|---|
| sem `--user-data-dir` | **sai sozinho em 2s** |
| com `--user-data-dir` num diretório novo | escreve o PNG e **nunca sai** |

**A correção é não passar o flag.** `exportar.sh` não passa. Ele só é necessário quando você
precisa de perfis simultâneos, e aí o encerramento vira problema seu:

```bash
nohup "$CHROME" --headless ... --user-data-dir="$DIR" --screenshot="$OUT" "$URL" \
  </dev/null >/dev/null 2>&1 & disown
for i in $(seq 1 40); do [ -s "$OUT" ] && sleep 1 && break; sleep 1; done
pkill -9 -f "user-data-dir=$DIR"     # o único identificador único por invocação
```

O erro que costuma preceder este: **subir o servidor com `&` na mesma chamada da captura.**
A ferramenta de bash espera o processo de fundo, e a chamada trava por outro motivo. Servidor
é uma chamada própria, em background de verdade. Quem conserta isso acrescentando
`--user-data-dir` troca um travamento por outro.

### Armadilhas verificadas

**Título com `nowrap` transborda em silêncio, e `scrollWidth` não denuncia.** Num bloco, o
`scrollWidth` devolve a largura do bloco enquanto o texto couber — sete cards com a mesma
medida é a assinatura de um medidor inútil. Meça encolhendo o elemento até o conteúdo:

```js
h.style.display = 'inline-block';                 // encolhe até a linha mais larga
const larg = h.getBoundingClientRect().width;
h.style.display = '';
```

É o que o `?medir=1` do esqueleto faz, junto com a altura das zonas. **Rode antes de capturar** —
título transbordando e zona de grafismo esmagada produzem PNG do tamanho certo, e por isso
passam na conferência automática.

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

**A área viva é um quadrado de 924×924 no centro do card** — `x 78..1002`, `y 213..1137`. Texto
mora ali, inclusive o pé; fora dela até a borda é sangria, onde grafismo entra e texto não.

Dois cortes se encaixam nessa conta. O **1:1 central**, `y 135..1215`, é o que o Explore aplica e
**é também a página do PDF do LinkedIn** — e página tem margem, que é o que os 78px seguintes
reservam. Contar a margem a partir da borda de 1350 entrega 165px de folga no Instagram e 15px no
LinkedIn: o mesmo card, respirando num e espremido no outro, sem que a exportação possa fazer
nada a respeito.

Gabarito por query, para conferir sem adivinhar:

```js
const GUIA = qs.get('safe') ? `
  <div style="position:absolute;left:0;right:0;top:135px;height:1080px;
       border:2px dashed #E11;z-index:99;pointer-events:none"></div>
  <div style="position:absolute;left:78px;top:213px;width:924px;height:924px;
       border:2px dashed #0A0;z-index:99;pointer-events:none"></div>` : '';
```

Capture uma série com `&safe=1` e guarde como `_safe-0N.png`. **Vermelho é a página do LinkedIn; verde é o quadrado vivo** — nada de texto pode cruzar o verde.

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

Use a variável, nunca um número escolhido a olho. A tabela dos sete estilos está em
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

## Duas armadilhas de cor que a captura não denuncia

Ambas produzem PNG do tamanho certo, com contagem de cores normal, e **só aparecem quando você
abre e olha**. As duas aconteceram na mesma produção.

### Texto sobre campo escuro não herda a cor do campo

O padrão é desenhar o campo como um `<div>` de fundo e o texto como outro `<div>` posicionado por
cima. Os dois são **irmãos**, não pai e filho — então o texto herda a cor do card, que é a tinta
escura, e some no campo escuro.

```html
<!-- errado: o texto herda #111 do card e desaparece -->
<div class="campo-escuro"></div>
<div class="conteudo">o que sobra é verificável</div>
```

Ou o texto vira filho do campo, ou ele declara a própria cor. Vale a mesma checagem para todo
elemento que atravessa uma divisa de campo.

### Acento cruzando divisa de campo

A régua da entrelinha resolve colisão entre linhas. Ela **não** resolve o glifo que sobe para dentro
de outro campo de cor: um `Õ` de 190px posicionado logo abaixo de uma divisa tem o til renderizado
**acima** dela, no campo de cima — e se as duas cores forem iguais, o acento simplesmente não existe.

A palavra continua legível o suficiente para o erro passar: `ÕÊ` vira `OE`, que ainda lê como
alguma coisa. Deixe pelo menos `1,2 × tamanho da fonte` de folga entre a divisa e o topo do texto
acentuado, ou mova o texto inteiro para dentro de um campo só.

## O texto mora no `.md`, não no HTML

O usuário vai querer trocar uma palavra depois de ver a arte. **Sempre.** Se o texto estiver
embutido no HTML, cada troca é uma edição de código feita por você a partir de uma descrição no
chat — lento, impreciso, e some a cada rodada.

Inverta: o `TEXTOS.md` é a fonte, o HTML só desenha. Aí a instrução ao usuário — *edita o arquivo e
me avisa* — passa a ser verdade mecânica, e a rodada de correção vira um comando.

**No `TEXTOS.md`**, um bloco por card, com formato fixo:

```markdown
**01 · capa**
ESSE / CARROSSEL / NÃO FOI FEITO
Foi feito com uma só skill — que você instala e usa agora.
```

Primeira linha depois do cabeçalho é o título, segunda é o corpo, ` / ` marca quebra de linha.
Explique isso **dentro do próprio arquivo**, em uma citação no topo — é lá que o usuário vai estar
quando precisar da informação.

**Estilo cujo grafismo carrega texto estende o formato.** Em terminal, colagem e neo-brutalismo
metade das palavras do card pode viver dentro do desenho — e costuma ser justamente o que o
usuário vai querer corrigir. Sem uma linha para elas, a promessa *"edita o `.md` e me avisa"* é
falsa para metade da peça. A extensão é uma quarta forma de linha, começada por `>`:

```markdown
**03 · o desenho**
A PLATAFORMA / FOI DESENHADA / PRA ISSO
63,8% do planeta é usuário ativo de rede social.
> DELBIANCO, 2023 | 63,8% da população mundial é usuária ativa de rede social.
> ALOUFI ET AL., 2022 | attention hijacking: o design premia absorção rápida.
```

Antes da `|` vai o rótulo do elemento — barra de janela, tira de fita, aba; depois, o conteúdo
dentro dele. **Explique a extensão no topo do próprio arquivo também**, com o exemplo do estilo
que está em uso, não com o genérico.

**No HTML:**

```js
const TX = {};
async function carregarTextos(){
  const md = await fetch('../TEXTOS.md').then(r => r.text());
  for (const m of md.matchAll(/^\*\*(\d{2}) · [^*]*\*\*\n(.+)\n(.+)$/gm))
    TX[+m[1]] = { titulo: m[2].trim().split(' / ').join('<br>'), corpo: m[3].trim() };
  const faltando = [...Array(N)].map((_,i)=>i+1).filter(n => !TX[n]);
  if (faltando.length) throw new Error('TEXTOS.md sem os cards: ' + faltando.join(', '));
}
```

**Falhe alto, não baixo.** Se um card não parseou, pinte a página inteira de vermelho com a
mensagem. Card faltando renderiza como card vazio, e card vazio passa na captura sem reclamar —
o mesmo defeito silencioso do PNG em branco.

**O que continua no HTML:** corpo tipográfico de cada título, composição, grafismo. Isso é
direção de arte, não conteúdo — e o usuário não deve precisar mexer.

**Uma pegadinha de servidor:** se o `TEXTOS.md` está um nível acima do HTML, sirva a pasta do
trabalho inteira, não a subpasta da arte. `fetch('../TEXTOS.md')` sai do escopo do servidor e
devolve 404 sem explicar.

Use `--directory` **sempre**, com caminho absoluto: o `cwd` do bash do agente volta ao
diretório inicial a cada chamada, então `python3 -m http.server 8910` sozinho sobe onde você
não espera. E a URL passa a incluir a subpasta:

```bash
python3 -m http.server 8910 --directory /caminho/carrossel-assunto   # chamada própria
# http://localhost:8910/arte/cards.html?card=1
```

## O `body` da página de captura precisa estar zerado

Se o HTML de trabalho empilha os cards com `padding` e `gap` no `body` — e ele empilha, porque é
assim que você olha todos de uma vez —, **a captura de um card só sai deslocada por esse padding e
perde a mesma quantidade no pé**. O arquivo tem 1080×1350, a contagem de cores parece normal, e o
defeito só aparece quando você mede.

Aconteceu neste projeto: 26px de deslocamento em todos os PNGs, e o corte 1:1 do LinkedIn comendo
a paginação por causa disso.

```css
body{ padding:26px; gap:26px }          /* a folha de contato */
body.solo{ padding:0; gap:0 }           /* a captura de um card */
```

```js
if (q.get('card')) document.body.classList.add('solo');
```

**A conferência**, e vale para qualquer exportação: leia o pixel do canto do PNG. Se não for a cor
de fundo do card, a captura pegou a página em volta.

---

## Cinco armadilhas de código que a captura não denuncia

Todas verificadas em produção. As três primeiras produzem um PNG do tamanho certo, com
contagem de cores plausível, e nada de útil dentro.

### `const` declarado duas vezes mata o script inteiro

Sobrescrever o motor de desenho de um estilo redeclarando `const DESENHO` num escopo que já o
tem derruba o script todo, e **a captura sai com a cor de fundo da página**. Sobrescreva as
chaves — `DESENHO.capa = ...` — em vez de redeclarar.

### `file://` sem caminho absoluto

`--screenshot ... "arquivo.html?card=1"` faz o Chrome procurar um arquivo chamado
`arquivo.html?card=1`, que não existe: sai um PNG branco. Sempre `file://$PWD/...` — e no
Bash do agente **o `$PWD` volta ao diretório inicial a cada chamada**, então use o caminho
absoluto escrito por extenso.

### `transform-origin` do lado errado do alinhamento

Tipografia comprimida com `scaleX()` precisa da origem **do mesmo lado do alinhamento**.
Título alinhado à direita com `transform-origin: left` escorre para fora da folha e você lê
"VOC" e "PER" em vez da frase.

### `mix-blend-mode: multiply` em tipo vazado

Papel multiplicado sobre azul dá azul: o título desaparece. Multiply só quando o fundo do tipo
é **papel**. Sobre campo de tinta, tipo claro e sem mistura.

### Dupla inversão que se cancela

Inverter o cinza **e** trocar as pontas da rampa de cor devolve exatamente a imagem original.
Inverta uma coisa só.

## Medir a chapa antes de diagramar

Posicionar título e lede na mão é chutar o que dá para medir. A chapa carrega a informação:

1. Classifique papel × tinta e faça o perfil de cobertura por linha, na coluna do título
2. A maior corrida abaixo do limiar é o vão do título — lado, topo, altura
3. Se **nenhuma** corrida serve, a chapa é toda tinta: o tipo vai vazado, sem multiply, e a
   faixa escolhida é a de menor variância no terço de cima
4. O campo atrás do lede não se decide pelo perfil da coluna: **mede-se o retângulo onde o
   lede vai cair**. E não basta ter tinta — campo uniforme lê bem com tipo claro por cima.
   Faixa só quando a área é **agitada**, porque aí a letra briga com o desenho
5. Faixa atrás do texto é **caixa do tamanho do texto**, nunca de borda a borda até o pé —
   isso apaga o grafismo inteiro do card

## O bloco do pé é reservado, não é sobra

O pé precisa caber régua, respiro, até três linhas de corpo e folga antes da assinatura: cerca
de **250px**. É esse bloco que define até onde o título pode descer, e não o contrário.
Inverter isso é o que espreme o sub no rodapé.
