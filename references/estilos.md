# Os seis estilos

Seis, fixos. Não são seis pontos de partida para variar — são seis sistemas fechados, cada um com paleta, par tipográfico, lógica de grafismo e regra de material próprios. O usuário escolhe um; você executa aquele.

**Por que fixos e não uma biblioteca aberta:** direção inventada na hora sai bonita na capa e quebra no card 5. Estas seis já passaram pelo teste de escala, e cada verbete carrega o cuidado que aquele estilo custou para descobrir.

Cada um tem **três referências fixas** em `assets/referencias/`, uma por arquétipo de layout. Mostre-as ao usuário na etapa 1.

## O briefing que vale para os seis

> **posts inspired in editorial graphic posters**

Não é enfeite de prompt — é a régua de composição, e entra em toda geração de imagem e em toda decisão de diagramação. Cartaz editorial quer dizer: **uma ideia por peça, hierarquia brutal entre o grande e o pequeno, e vazio como decisão**. Um cartaz não tem três blocos de peso igual disputando o olho. Tem um evento, e o resto é colofão.

Traduzindo para o card:

- Um elemento domina. Título ou imagem, nunca os dois no mesmo peso
- A razão entre o maior e o menor corpo tipográfico é de pelo menos **2,5:1**
- O que não é o evento fica pequeno, no pé ou na margem, e **pode simplesmente não existir**
- Vazio contíguo, não distribuído: um vão grande vale mais que quatro folgas iguais

## Os três arquétipos de layout

As três referências de cada estilo são o mesmo sistema visual em três composições diferentes. Use-as também como repertório de diagramação — **um carrossel de oito cards que usa os três em rodízio tem ritmo; um que usa só um vira oito paredes iguais.**

| Arquétipo | Mecanismo | Serve bem a |
|---|---|---|
| **Editorial split** | duas colunas assimétricas; título domina uma, o resto se espreme na outra | capa, card de virada |
| **Cascata Z** | camadas sobrepostas, giradas, algumas cortadas pela borda | processo, acúmulo, "e tem mais" |
| **Bento assimétrico** | células de tamanhos desiguais, uma sempre deixada vazia | comparação, lista, dado |

## Escolha

Os seis rodam **sem nenhum gerador de imagem** — todo grafismo é CSS/SVG. Dois mudam de patamar com gerador conectado, e isso entra na conversa da etapa 1:

| Estilo | Sem gerador | Com gerador conectado |
|---|---|---|
| Brutalista vetorial | completo | capa ganha imagem em corte duro |
| **Risografia com textura** | funciona | **muda de patamar** — a tinta riso existe para cair sobre imagem |
| Janelas | completo | capa ganha imagem dentro da janela |
| **Mixed media / colagem** | funciona | **muda de patamar** — o recorte fotográfico é o centro do estilo |
| Neo-brutalismo colorido | completo | capa ganha imagem em corte duro |
| Minimalista editorial quente | completo | uma imagem grande sangrando por um lado |

Regra fixa: **havendo gerador conectado, a capa sempre recebe imagem gerada**, qualquer que seja o estilo.

## As fontes

Doze famílias, todas open-source do Google Fonts (OFL/Apache), **acentos pt-BR conferidos glifo a glifo** — `ÁÀÂÃÉÊÍÓÔÕÚÜÇ áàâãéêíóôõúüç` mais `º ª « » — " "`. Nenhuma sai de acervo pessoal: o carrossel precisa ser reproduzível por quem clonar a skill.

```bash
assets/baixar-fontes.sh riso        # baixa o par, confere acentos, gera fonts.css
assets/baixar-fontes.sh --listar
```

O script grava `fonts.css` com as duas faces em base64, sob os nomes `Titulo` e `Corpo`.

## A cauda que vale para os seis

Depois do bloco do estilo e do assunto, toda geração termina com:

> `Poster artwork only, no device mockup, no frame, no border. ABSOLUTELY NO TEXT, no lettering,`
> `no numbers, no logos, no words anywhere.`

E a lista de antipadrões, que é a mesma para todos: `no gradient mesh, no glow, no neon, no
glassmorphism, no blur, no 3D render, no drop shadow, no bokeh, no rounded corners, no emoji, no
stock photo look`.

**A ordem importa:** estilo → assunto → cauda. O modelo pesa mais o começo do prompt, e o que
precisa dominar é o estilo. Assunto primeiro devolve uma foto de banco de imagem com a paleta
sugerida por cima.

## A régua da entrelinha

**Este é o defeito mais fácil de deixar passar em pt-BR, e o mais caro.** Título em caixa alta com entrelinha apertada fica lindo em inglês e quebra em português: o til do `Ã` e o agudo do `Ó` sobem **acima da altura da linha inteira** e batem na letra de cima. O resultado não lê como erro de espaçamento — lê como sujeira, e o leitor não sabe dizer o que está errado.

Aconteceu em produção nos três estilos ao mesmo tempo: `ESSE CARROSSEL` com o til de `NÃO` grudado no `SS`, e `FEITO` com o agudo de `SÓ` cortando o `T`.

**O piso não se estima, se calcula:**

```
entrelinha mínima = (topo do acento em caixa alta) − (transbordo óptico do S/O/C/G/U) + 0,04
```

`baixar-fontes.sh` calcula isso sozinho e grava em `fonts.css` como variável CSS. Use a variável em vez do número:

```css
h1 { line-height: var(--lh-titulo) }
```

Os seis já vêm calculados:

| Estilo | Título | Piso | Se a linha de cima tiver `Q`, `J` ou `Ç` |
|---|---|---|---|
| brutalista | Anton | **1,15** | 1,45 |
| riso | Bricolage Grotesque | **0,97** | 1,19 |
| janelas | Archivo Black | **0,94** | 1,14 |
| colagem | Bodoni Moda | **1,09** | 1,33 |
| neubrutal | Chivo | **0,95** | 1,15 |
| editorial | Fraunces | **0,99** | 1,19 |

Repare que **Anton é o caso extremo**: caixa alta de 0,867 em, mas o acento chega a 1,101 — mais alto que o próprio corpo da fonte. É por isso que ela é a única do conjunto que precisa de entrelinha maior que o tamanho da letra.

A coluna da direita só entra quando as duas condições se encontram: a linha de cima tem descendente **e** a de baixo tem acento na mesma região horizontal. Não suba a entrelinha inteira por causa de um `Ç` que está no outro canto — olhe o PNG.

**O corpo de texto não precisa disso.** Ele é caixa baixa e é diagramado entre 1,35 e 1,45 por
legibilidade, o que já passa folgado do piso — por isso o `--lh-corpo` que o script calcula é
**conferência, não valor de uso**: se o que você diagramou ficar abaixo dele, alguma coisa está
errada no seu CSS, não na fonte.

## Palavra não é a unidade, caractere é

A régua de 25 palavras foi feita para fonte proporcional. **Dois dos seis estilos usam
monoespaçada no corpo** — IBM Plex Mono no brutalista, Space Mono em janelas — e ali o mesmo
texto ocupa muito mais.

O número que serve para os dois casos: **a 34px sobre uma coluna de 924px, uma mono cabe ~45
caracteres por linha.** 280 caracteres viram 7 linhas e mais de 330px de altura, que em vários
cards é mais que a zona de grafismo inteira. Conte caracteres, ou rode o `?medir=1` e olhe a
altura da `.gfx` antes de fechar o texto.

---

# 1 · BRUTALISTA VETORIAL

`brutalista-1-split.jpg` · `brutalista-2-cascata.jpg` · `brutalista-3-bento.jpg`

**Mecanismo:** formas vetoriais chapadas de aresta dura sobre papel cru. Blocos de cor sangram pela borda em vez de flutuarem dentro do card. Tipografia condensada gigante, apertada, tratada como material de construção — ela é uma das formas, não uma legenda sobre elas. Fios de 4 a 6px estruturam. Nenhum arredondamento, nenhum gradiente, nenhuma sombra suave.

**Paleta**

| cor | hex | uso |
|---|---|---|
| papel | `#EDEAE3` | fundo |
| tinta | `#111111` | tipografia, fios, blocos |
| sinal | `#E33420` | um acento saturado, em no máximo dois elementos por card |

**Fontes:** Anton 400 (`Titulo`) · IBM Plex Mono 400 (`Corpo`) — `baixar-fontes.sh brutalista`

**Entrelinha do título: `1.15`** — `var(--lh-titulo)`. A maior das seis; ver a régua da entrelinha.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `VECTOR BRUTALISM illustration, screenprinted on raw paper. Exactly three flat colours and`
> `nothing else: raw paper #EDEAE3, ink #111111, signal red #E33420. Posterised hard-edged flat`
> `shapes with thick confident contours, like a cut linocut. PRINTED SURFACE: the flat areas carry`
> `the irregularity of screenprinted ink — micro speckle, slight ink starvation at the edges of`
> `large fields, visible paper tooth. No gradient, no midtone, no shading, no soft falloff, no`
> `airbrush — the irregularity is texture, never a tonal ramp. The signal red appears in exactly`
> `ONE element. Flat frontal, no perspective, no depth of field, no photographic lighting.`

A distinção que segura o estilo: **irregularidade de tinta, não rampa tonal**. `ink starvation` e
`paper tooth` dão superfície impressa; `soft falloff` e `airbrush` dariam meio-tom, que é o que o
estilo proíbe. Se o modelo devolver degradê, o culpado é ter pedido textura sem proibir rampa.

**Grafismo:** 100% CSS/SVG. Retângulo, círculo, diagonal, seta grossa, tabela de fio duplo, número gigante em marca-d'água. Nunca imagem no corpo do carrossel.

**Material:** **grão de impressão suave e permanente**, em duas camadas — grão fino em `opacity:.09`
e dente de papel largo em `.05`, ambos em `mix-blend-mode:multiply` e **por cima de tudo, inclusive
da tipografia**. Tinta impressa não escolhe onde assentar.

Isto foi revisto em produção: a primeira versão do estilo declarava *nenhum material*, com o
argumento de que vetor é limpo por definição. Errado. Sem grão, cor chapada em 1080×1350 lê como
**exportação de software**, não como peça impressa — e o brutalismo vetorial cita cartaz, não
interface. A dose é o que separa: acima de `.12` vira papel amassado e aí sim lê como filtro.

**Ritmo:** o bloco de cor muda de tamanho, lado e sangria a cada card; a tipografia fica ancorada à esquerda.

**Cuidado verificado:** Anton é muito condensada. Título de quatro linhas em caixa alta vira parede preta e o olho não acha onde entrar — **máximo três linhas na capa**. E IBM Plex Mono é larga: 25 palavras nela ocupam mais que em qualquer outra do conjunto, então corte antes de diagramar.

**O cartaz aqui:** cartaz de protesto suíço. Uma palavra enorme, uma forma, e ar.

---

# 2 · RISOGRAFIA COM TEXTURA

`riso-1-split.jpg` · `riso-2-cascata.jpg` · `riso-3-bento.jpg`

**Mecanismo:** duas tintas spot que se sobrepõem e multiplicam, gerando uma terceira cor onde cruzam. Erro de registro deliberado. Retícula de meio-tom visível e fibra de papel por cima de tudo. **Nada é 100% chapado** — a graça do estilo é que a superfície tem defeito.

**Paleta**

| cor | hex | uso |
|---|---|---|
| papel | `#F4F0E6` | fundo |
| tinta A | `#0078BF` | azul-riso — massa principal |
| tinta B | `#FF6C2F` | laranja-riso — acento e a cópia deslocada |
| cruzamento | — | **não escolha essa cor**: ela nasce do `multiply` das duas |

**Fontes:** Bricolage Grotesque 800 (`Titulo`) · Newsreader 400 (`Corpo`) — `baixar-fontes.sh riso`

**Entrelinha do título: `0.97`** — `var(--lh-titulo)`.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `RISOGRAPH PRINT on a duplicator, exactly two spot inks: riso blue #0078BF and riso orange`
> `#FF6C2F on cream paper #F4F0E6. Where the inks overlap they multiply into a third dark colour.`
> `PRINTED SURFACE, and it is the point: coarse visible halftone dot screen in both inks with the`
> `dots clearly resolvable, deliberate plate misregistration with the orange plate offset several`
> `millimetres, roller streaks running in the feed direction, patchy ink coverage with occasional`
> `voids, visible paper fibre, slight show-through. Nothing is perfectly flat and nothing is`
> `perfectly registered — the defects ARE the style. Reduced to two plates; not full-colour`
> `photography, not a digital print.`

**Não peça "risograph" e pare aí.** O modelo entrega uma foto com filtro de duotone e chama de riso.
O que produz o material de verdade é nomear os defeitos um a um: ponto resolvível, registro fora,
listra de rolo, cobertura irregular, fibra. Cada um que você tirar, o modelo suaviza.

**Grafismo:** CSS. Retícula com `radial-gradient`, fibra com `feTurbulence`, erro de registro com cópia deslocada em `mix-blend-mode:multiply`. Receitas em [grafismos.md](grafismos.md).

**Material:** obrigatório — é o estilo. Retícula em `opacity:.38`, fibra em `.16`. **Sempre abaixo do texto** na ordem de empilhamento; retícula sobre corpo de texto come a leitura, que é a prioridade 1.

**Imagem gerada:** onde este estilo mais compensa. Retrato, objeto, cena — sempre passada por duotone das duas tintas antes de entrar. Imagem escura precisa de `brightness(1.4)` antes do duotone, ou vira mancha.

**Ritmo:** muda qual tinta domina o card. Um azul, o seguinte laranja, um terceiro só no cruzamento.

**Cuidado verificado:** o deslocamento do erro de registro **precisa escalar com o corpo do texto**. 8px sobre um título de 150px é sutil; sobre um de 60px cria letra fantasma e a palavra passa a ler errado — já aconteceu de "ABRASILEIRAR" ler "ABRASILEITRAR". Depois de aplicar, leia a palavra em voz alta olhando o PNG.

**O cartaz aqui:** cartaz de festival impresso em riso. Imagem grande, uma frase, colofão miúdo no pé.

---

# 3 · JANELAS

`janelas-1-split.jpg` · `janelas-2-cascata.jpg` · `janelas-3-bento.jpg`

**Mecanismo:** fundo preto e, por cima, janelas de sistema operacional antigo em ângulos e tamanhos diferentes, algumas cortadas pela borda. **As janelas carregam conteúdo real** — o grafismo e a informação são a mesma coisa. O verde ácido é a tinta, não o campo.

**Paleta**

| cor | hex | uso |
|---|---|---|
| fundo | `#0B0B0B` | o card inteiro |
| tinta | `#D9F218` | tipografia, bordas, barras de título, sombra dura |
| janela | `#1A1A1A` | corpo das janelas |
| corte | `#E4002B` | risco, alerta, o que foi cortado |

**Por que negativo e não positivo:** a versão de campo verde existiu e foi descartada. **Verde ácido chapado em 1080×1350 cansa o olho no feed**, e não sobra contraste para destacar nada dentro dele — tudo vira o mesmo grito. Invertido, o verde vira acento, o card ganha densidade, e a célula vazia do bento passa a ser respiro de verdade em vez de mais um vão de cor. A versão positiva está em `referencias/_descartado/`, caso o assunto peça.

**Fontes:** Archivo Black 400 (`Titulo`) · Space Mono 400 (`Corpo`) — `baixar-fontes.sh janelas`

**Entrelinha do título: `0.94`** — `var(--lh-titulo)`.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `SCREEN-NATIVE NEGATIVE POSTER. Near-black #0B0B0B ground; acid green #D9F218 is the ink and`
> `never the field. Flat rectangles with 3px acid green outlines and hard offset acid green shadows`
> `with zero blur; dark charcoal #1A1A1A interiors. One accent of red #E4002B. Everything reads as`
> `an old operating system rendered in two colours. No gradient, no glow, no light emission, no`
> `photographic lighting, no dark-room photography.`

**Grafismo:** CSS. Janela = borda verde de 3px, barra de título com o nome real da etapa, sombra dura deslocada de 7px em verde, `transform:rotate()` de 1 a 3 graus. Cursor de seta em SVG apontando para a janela que importa.

**Material:** **nenhum.** Estilo nativo de tela — papel, fibra e grão envelhecem o que deveria parecer interface. A textura vem da sombra dura.

**Ritmo:** muda quais janelas aparecem, o ângulo, o tamanho e qual está em primeiro plano. O cursor muda de posição.

**A barra de título é o campo da citação.** Foi o achado que decidiu uma escolha de estilo em
produção: `1854 · WALDEN`, `DELBIANCO, 2023`, `ÖZPENÇE, 2024`. A fonte fica **dentro** do
grafismo em vez de virar rodapé miúdo, e nenhum card é gasto com bibliografia. Isso faz de
janelas o estilo certo para **conteúdo que precisa de fonte visível** — artigo, dado, pesquisa,
processo com etapas nomeadas.

Vale a mesma regra de sempre, e ela é o que separa isso de slop: a barra só carrega **referência
que existe de fato**. Rótulo inventado ali é grafismo produzindo texto.

**Cuidado verificado:** janela posicionada por cima do bloco de título **come letra** — aconteceu na própria referência de cascata, onde a palavra "DISRUPT" foi cortada ao meio por uma janela. Defina a zona do título primeiro, com empilhamento rígido; as janelas ficam com o que sobra. E o defeito irmão, que passou despercebido em produção: **janela por cima do texto de outra
janela.** Aqui os elementos se sobrepõem por projeto, então o que come letra raramente é o texto
do card sobre o desenho — é um pedaço do desenho sobre o texto de outro pedaço. Só aparece
olhando o PNG.

**O cartaz aqui:** cartaz de rave dos anos 90 feito no computador da época. Tipografia que ocupa, e o sistema à mostra.

---

# 4 · MIXED MEDIA · COLAGEM MODERNA

`colagem-1-split.jpg` · `colagem-2-cascata.jpg` · `colagem-3-bento.jpg`

**Mecanismo:** camadas de origens diferentes no mesmo plano — recorte fotográfico em preto e branco com borda de tesoura, forma vetorial chapada, rabisco de marcador, tira de fita, retícula grossa, fragmento de papel milimetrado. **Nenhuma emenda é escondida:** toda borda é cortada, rasgada ou colada.

**Paleta**

| cor | hex | uso |
|---|---|---|
| kraft | `#E9E5DA` | fundo |
| tinta | `#141414` | tipografia e recortes fotográficos |
| rosa | `#F0357A` | a cor que grita — uma zona por card |
| verde-garrafa | `#0E5C3F` | a cor que segura — camada de fundo, sublinhado |

**Fontes:** Bodoni Moda 900 (`Titulo`) · Karla 400 (`Corpo`) — `baixar-fontes.sh colagem`

**Entrelinha do título: `1.09`** — `var(--lh-titulo)`.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `MODERN MIXED-MEDIA COLLAGE. Palette: kraft paper #E9E5DA, black #141414, hot pink #F0357A,`
> `bottle green #0E5C3F. Layers of clearly different origin sharing one plane: a coarsely halftoned`
> `black-and-white photographic cut-out with visible scissor edges, flat vector shapes, hand-drawn`
> `marker scribbles, strips of matte tape, fragments of graph paper. Every edge is cut, torn or`
> `taped — nothing is seamless. Each layer carries its own material: long fibre on the kraft,`
> `halftone over the flat inks, fine grain on the paper strips. Scanned-flatbed feel.`

A didone é escolha de mecanismo, não de gosto: colagem moderna cita a revista recortada, e o contraste extremo da Bodoni é o que faz a letra parecer **recortada com tesoura** em vez de digitada.

**Grafismo:** CSS mais recorte. Borda rasgada com `clip-path` de polígono irregular, fita com retângulo semiopaco girado, papel milimetrado com `repeating-linear-gradient`, rabisco em `<path>` SVG de traço grosso.

**Material:** kraft com grão em `opacity:.14`, e cada camada com a sua própria borda. É o único estilo em que **camadas diferentes podem ter texturas diferentes** — é isso que a palavra "mixed" está fazendo ali.

**Imagem gerada:** o recorte fotográfico é o centro. Preto e branco de alto contraste, recortado com fundo transparente, com margem branca de papel visível na borda.

**Ritmo:** muda quantas camadas e qual material está por cima. Um card de três camadas depois de um de seis já é ritmo.

**Cuidado verificado — é o mais sério dos seis:** **o ruído da colagem é inimigo do título.** Na própria referência de cascata, o título ficou sobre a pilha de camadas e a leitura sofreu. Neste estilo a tipografia precisa de **um plano limpo reservado por baixo** — uma tira de papel chapado, uma zona de kraft deixada livre, ou um bloco de cor sólida. Sem esse plano, a hierarquia de leitura cai, e leitura é a prioridade 1.

E cuidado com o segundo risco, que é de conteúdo: colagem convida a encher. Recorte que não diz nada sobre o assunto é ornamento, e ornamento é slot vazio — vale o mesmo teste da troca de [grafismos.md](grafismos.md).

**O cartaz aqui:** cartaz de exposição montado à mão e escaneado. A mão aparece no resultado, e é essa a graça.

---

# 5 · NEO-BRUTALISMO COLORIDO

`neubrutal-1-split.jpg` · `neubrutal-2-cascata.jpg` · `neubrutal-3-bento.jpg`

**Mecanismo:** blocos com contorno preto grosso e sombra dura deslocada, sobre campo saturado com grade milimetrada. **Componentes de interface usados como elemento gráfico** — botão, caixa de seleção, balão, estrela, aba, barra de progresso. Assimetria deliberada, tudo girado de 2 a 4 graus.

**Paleta**

| cor | hex | uso |
|---|---|---|
| amarelo | `#FFD84D` | campo ou bloco |
| azul elétrico | `#2B4FE8` | campo ou bloco |
| rosa | `#FF5C8A` | bloco, nunca campo |
| menta | `#4BD9A8` | bloco, e é a que costuma ficar vazia |
| preto | `#000000` | contorno de 5px, sombra dura, tipografia |

Ao contrário dos outros cinco, **este estilo não tem uma cor de fundo fixa** — o campo muda a cada card. É parte do ritmo.

**Fontes:** Chivo 900 (`Titulo`) · Chivo Mono 400 (`Corpo`) — `baixar-fontes.sh neubrutal`

**Entrelinha do título: `0.95`** — `var(--lh-titulo)`.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `COLOURFUL NEO-BRUTALISM. Palette: yellow #FFD84D, electric blue #2B4FE8, hot pink #FF5C8A,`
> `mint #4BD9A8, pure black. Flat blocks outlined in 5px pure black with hard offset black shadows`
> `and absolutely zero blur, over a saturated colour field overprinted with a fine millimetric grid.`
> `Interface components as graphic elements — button, checkbox, speech bubble, star, toggle.`
> `Deliberate asymmetry, elements rotated 2 to 4 degrees. No gradient, no glow, no soft shadow.`

**Grafismo:** CSS puro, e o mais fácil dos seis. `border:5px solid #000` mais `box-shadow:8px 8px 0 #000`, sem blur nenhum. Grade com `repeating-linear-gradient` fino por baixo de tudo.

**Material:** nenhum além da grade milimetrada. Grão aqui suja o contorno.

**Ritmo:** muda a cor do campo e qual componente de interface aparece.

**Cuidado verificado — de estratégia, não de execução:** este é **o visual mais usado em post de design hoje**. Ele acerta fácil e envelhece rápido: distintivo agora, genérico em seis meses. Diga isso ao usuário **na hora em que ele escolhe**, não depois de pronto — é informação que muda a decisão, e escondê-la é entregar uma peça com prazo de validade sem avisar.

O segundo risco é de slop: a interface desenhada convida a escrever dentro dela. Botão com "baixar", aba com "opções", barra com "85%". **Nenhuma dessas palavras veio da etapa 4.** Vale a regra do grafismo mudo.

**O cartaz aqui:** cartaz de festa impresso em serigrafia de duas passadas, com o registro fora de esquadro de propósito.

---

# 6 · MINIMALISTA EDITORIAL QUENTE

`editorial-1-split.jpg` · `editorial-2-cascata.jpg` · `editorial-3-bento.jpg`

**Mecanismo:** grade de duas colunas assimétricas e muito vazio. Título em serifa de contraste alto ocupando a coluna larga; corpo pequeno confinado à coluna estreita. Um único elemento de cor por card. Fio fino como única decoração. É o estilo que mais confia no vazio.

**Paleta**

| cor | hex | uso |
|---|---|---|
| papel quente | `#F2EBDF` | fundo |
| tinta | `#1E1B16` | tipografia — quase preto, nunca preto |
| terracota | `#C4562F` | o acento, um por card |
| oliva | `#6E7355` | segunda cor, só em card que precise de duas |

**Fontes:** Fraunces 700 (`Titulo`) · Work Sans 400 (`Corpo`) — `baixar-fontes.sh editorial`

**Entrelinha do título: `0.99`** — `var(--lh-titulo)`.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `WARM MINIMAL EDITORIAL PRINT. Palette: warm paper #F2EBDF, near-black warm ink #1E1B16, one`
> `terracotta accent #C4562F, occasionally muted olive #6E7355. Quiet and refined: soft directional`
> `daylight from one side, fine film grain, restrained contrast **with real mid-tones**. Enormous`
> `amounts of empty paper — emptiness is the primary element. Very fine hairline rules. No saturated`
> `colour, no gradient, no glow, no bokeh, no hard flash.`

Repare que este é o **único dos seis que pede meio-tom**. Colar aqui o `no midtone` dos outros
estilos mata a direção — é por isso que os blocos são separados e não um só com a paleta trocada.

**Grafismo:** pouquíssimo. Fio, número de página grande em marca-d'água, filete separando colunas, uma tabela quando o conteúdo for comparativo. A referência de bento mostra o melhor achado do estilo: **a grade de fio virando a própria decoração**, com seis das nove células deixadas vazias.

**Material:** grão de papel em `opacity:.10`. Nada mais — este estilo morre com textura por cima.

**Imagem gerada:** uma por carrossel, no máximo duas. Grande, ocupando um terço, **sangrando por um lado**. Imagem pequena e centrada aqui parece thumbnail.

**Ritmo:** muda **qual coluna o título ocupa e onde o vazio fica**. Sem variar isso, oito cards viram oito paredes iguais — é o estilo que mais precisa de disciplina de ritmo e o que mais castiga a falta dela.

**Cuidado verificado:** é o oposto de um carrossel de feed — pouco contraste e muito vazio convidam a diagramar o corpo pequeno. Não caia nisso: **o piso de 30px vale aqui como em todos os outros**, e 34 se o destino é LinkedIn. O vazio deste estilo é a margem, não o corpo do texto. E Fraunces tem eixo óptico: em corpo grande use o corte de display, ou os traços finos somem.

E um risco de estilo, não de execução: papel creme com serifa e acento terracota é hoje **um dos clichês de peça gerada por IA**. O que salva esta direção é o rigor da grade e a quantidade de vazio — se o card ficar "aconchegante" em vez de rigoroso, ele caiu no clichê. Compare com `editorial-1-split.jpg`: dois terços do card são papel vazio, e é isso que o tira do lugar-comum.

**O cartaz aqui:** página de abertura de revista de arquitetura. É a mais literal das seis em relação ao briefing.

---

## A conversa da etapa 1

Não descreva os seis em texto e peça para escolher. **Mostre as três referências do estilo** —
`<estilo>-1-split.jpg`, `-2-cascata.jpg`, `-3-bento.jpg` — abertas, não descritas. São três de
propósito: uma capa bonita não prova nada, e o que quebra no card 5 é o estilo não ter três
arquétipos de layout. É isso que a pessoa está julgando.

**Não renderize nada com o assunto dele aqui.** Preview do trabalho real só existe na etapa 7,
com o texto aprovado e o nível de imagem decidido — a regra está no topo da SKILL.md. Preview de
estilo chega antes da etapa 2, então mostra uma peça feita por um caminho de produção que talvez
nem seja o escolhido, com texto provisório que ainda vai mudar: o usuário opina duas vezes sobre
a mesma coisa e a segunda contradiz a primeira.

Se o usuário pedir **mistura de dois estilos**, resolva por escrito: diga qual dos dois manda em
cada camada — paleta, tipografia, material, grafismo. Estilo misturado quebra quando os dois
disputam a mesma camada; a paleta de um com a grade do outro quase sempre perde os dois.

---

## Procedência das referências

As dezoito imagens de `assets/referencias/` foram geradas com **Nano Banana Pro** via MCP do Higgsfield, em 4:5, 2K, a partir de prompts que combinam: o briefing de sistema acima, a especificação de paleta e material de cada estilo, os três arquétipos de layout do variance engine da `high-end-visual-design`, e a lista de antipadrões da `bencium-innovative-ux-designer` aplicada como negativa. Os masters em resolução cheia ficam fora do repositório.
