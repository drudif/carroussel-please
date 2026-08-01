# Os sete estilos

Sete, fixos. Não são sete pontos de partida para variar — são sete sistemas fechados, cada um com paleta, par tipográfico, lógica de grafismo e regra de material próprios. O usuário escolhe um; você executa aquele.

**Por que fixos e não uma biblioteca aberta:** direção inventada na hora sai bonita na capa e quebra no card 5. Estas sete já passaram pelo teste de escala, e cada verbete carrega o cuidado que aquele estilo custou para descobrir.

Cada um tem **três referências fixas** em `assets/referencias/`, uma por arquétipo de layout. Mostre-as ao usuário na etapa 2.

## O briefing que vale para os sete

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

## O critério: de onde vem a espessura da peça

**A escolha do estilo é um funil, e quem abre o funil é o nível de imagem da etapa 1.** Não é
questão de gosto: cada estilo tira o que tem de melhor de uma fonte diferente, e a foto ajuda,
atrapalha ou é indiferente conforme essa fonte.

| origem | estilos | o que a foto faz |
|---|---|---|
| **superfície fotográfica processada** — retícula, duotone, recorte | riso, colagem | **é o centro.** Sem ela o estilo funciona, mas em versão reduzida |
| **forma desenhada** — geometria chapada, contorno, fio | brutalista, neubrutal | **é acessório.** Entra na capa e sai do miolo sem prejuízo |
| **vazio** — o material principal é a área que não tem nada | terminal, iridescente | **compete com o material.** Ocupa exatamente o que sustenta a peça |
| **vazio + uma foto** | editorial | o sistema prevê **uma** imagem grande sangrando por um lado. Uma, não oito |

Daí sai a ordem em que os estilos são abertos:

| nível | abra primeiro | também funcionam, com o custo dito |
|---|---|---|
| **3 · só código** | **terminal**, **iridescente** | riso e colagem viram retícula e recorte desenhados — funciona, mas tira o centro do estilo |
| **2 · banco aberto** | **colagem**, **riso** | brutalista só se quantizar em três degraus · terminal e iridescente não pedem foto |
| **1 · gerador** | **riso**, **colagem** | terminal não pede imagem · iridescente só a pedido do usuário |

**Brutalista, neo-brutalismo e editorial são polivalentes** — servem nos três níveis, e isso se
diz com essas palavras em qualquer um deles. Não é prêmio de consolação: **quem não quer que a
peça dependa de imagem escolhe exatamente ali**, e essa decisão só aparece se ela for nomeada.

**O funil ordena, não esconde.** Os sete continuam disponíveis e o usuário sabe que são sete. Se
ele escolher fora da recomendação, diga o que muda em uma linha, ofereça mudar de nível **uma
vez**, e siga com a escolha dele.

## Escolha

Os sete rodam **sem nenhum gerador de imagem** — todo grafismo é CSS/SVG. Dois mudam de patamar com gerador conectado:

| Estilo | Sem gerador | Com gerador conectado |
|---|---|---|
| Brutalista vetorial | completo | capa ganha imagem em corte duro |
| **Risografia com textura** | funciona | **muda de patamar** — a tinta riso existe para cair sobre imagem |
| Terminal | completo | não pede imagem: o estilo é fio, ficha e vazio |
| **Mixed media / colagem** | funciona | **muda de patamar** — o recorte fotográfico é o centro do estilo |
| Neo-brutalismo colorido | completo | capa ganha imagem em corte duro |
| Minimalista editorial quente | completo | uma imagem grande sangrando por um lado |
| **Iridescente minimal** | completo | **só se o usuário pedir** — ver a exceção abaixo |

Regra fixa: **havendo gerador conectado, a capa recebe imagem gerada** — com **uma** exceção, o
iridescente minimal, que vive do campo chapado e do vazio e perde os dois quando entra foto. Ali a
imagem só entra a pedido do usuário.

## As fontes

Treze famílias, todas open-source do Google Fonts (OFL/Apache), **acentos pt-BR conferidos glifo a glifo** — `ÁÀÂÃÉÊÍÓÔÕÚÜÇ áàâãéêíóôõúüç` mais `º ª « » — " "`. Nenhuma sai de acervo pessoal: o carrossel precisa ser reproduzível por quem clonar a skill.

```bash
assets/baixar-fontes.sh riso        # baixa o par, confere acentos, gera fonts.css
assets/baixar-fontes.sh --listar
```

O script grava `fonts.css` com as duas faces em base64, sob os nomes `Titulo` e `Corpo`.

## A cauda que vale para os sete

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

Os sete já vêm calculados:

| Estilo | Título | Piso | Se a linha de cima tiver `Q`, `J` ou `Ç` |
|---|---|---|---|
| brutalista | Anton | **1,15** | 1,45 |
| riso | Antonio | **1,18** | 1,49 |
| riso *com imagem* | Bricolage Grotesque | **0,97** | 1,19 |
| terminal | Cascadia Mono Light | **0,98** | 1,20 |
| colagem | Bodoni Moda | **1,09** | 1,33 |
| neubrutal | Chivo | **0,95** | 1,15 |
| editorial | Fraunces | **0,99** | 1,19 |
| iridescente | Hanken Grotesk Medium | **0,97** | 1,16 |

Repare que **Anton é o caso extremo**: caixa alta de 0,867 em, mas o acento chega a 1,101 — mais alto que o próprio corpo da fonte. É por isso que ela é a única do conjunto que precisa de entrelinha maior que o tamanho da letra.

A coluna da direita só entra quando as duas condições se encontram: a linha de cima tem descendente **e** a de baixo tem acento na mesma região horizontal. Não suba a entrelinha inteira por causa de um `Ç` que está no outro canto — olhe o PNG.

**O corpo de texto não precisa disso.** Ele é caixa baixa e é diagramado entre 1,35 e 1,45 por
legibilidade, o que já passa folgado do piso — por isso o `--lh-corpo` que o script calcula é
**conferência, não valor de uso**: se o que você diagramou ficar abaixo dele, alguma coisa está
errada no seu CSS, não na fonte.

## Palavra não é a unidade, caractere é

A régua de 25 palavras foi feita para fonte proporcional. **Dois dos sete estilos usam
monoespaçada no corpo** — IBM Plex Mono no brutalista, Cascadia Mono no terminal — e ali o mesmo
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

**Entrelinha do título: `1.15`** — `var(--lh-titulo)`. A maior das sete; ver a régua da entrelinha.

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

**Fontes:** **Antonio 700** (`Titulo`) · Newsreader 400 (`Corpo`) — `baixar-fontes.sh riso`

**Entrelinha do título: `1.18`** — `var(--lh-titulo)`.

**O par muda quando entra imagem gerada.** Com o card composto só de tipo e forma — o nível 3,
que é o padrão —, a Antonio é a certa: condensada, ela devolve linha longa em corpo grande, e é
corpo grande que faz a chapa fora de registro ler como material em vez de defeito. O
deslocamento de 9px que some numa Bricolage de 70px é evidente numa Antonio de 110px.

Havendo imagem gerada por baixo, a Antonio perde: sobre foto reticulada a haste fina de uma
condensada some, e aí volta a **Bricolage Grotesque 800**, que é pesada o bastante para se
segurar — `baixar-fontes.sh riso-imagem`, entrelinha `0.97`.

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
# 3 · TERMINAL

`terminal-1-split.jpg` · `terminal-2-cascata.jpg` · `terminal-3-bento.jpg`

**Mecanismo:** tipografia monoespaçada **leve** sobre chumbo escuro. Tudo encaixa numa grade de
caractere, o **recuo é a hierarquia**, fios de 2px separam, e a cor entra só em fichas curtas —
barra, bloco pequeno, uma célula chapada. Muito vazio, nada de peso.

**O título aqui é pequeno, e isso é o sistema.** Nos outros seis a razão de 2,5:1 se resolve
aumentando o título; neste ela se resolve **encolhendo tudo o mais** e deixando o vazio trabalhar.
Título mono em corpo gigante vira parede de caractere e nega a citação — terminal não grita, lista.

**Ele cita a paleta de um editor, não a captura de tela dele.** Nenhuma janela, nenhuma barra de
título, nenhum ícone, nenhum cursor piscando. Foi o que fez este estilo substituir o `janelas`:
o mesmo público, sem o custo de desenhar interface falsa — e sem o defeito que o janelas cobrava,
de janela por cima de janela comendo letra.

**Paleta**

| cor | hex | uso |
|---|---|---|
| chumbo | `#23272C` | o card inteiro |
| tinta | `#E6E8EA` | tipografia e fios — off-white, nunca branco puro |
| azul | `#6E8BFF` | estrutura — o que ordena |
| verde | `#4ADE9B` | valor — o que é dado |
| âmbar | `#F0B429` | número, medida, quantidade |
| magenta | `#FF6B9D` | o que quebra: erro, exceção, alerta |

**As quatro cores são as claras da família, não as escuras.** Sobre chumbo, o `#2D5BFF` de um tema
claro fecha e vira mancha; o que se lê é a versão levantada. Trocar o fundo de um tema de editor
sem levantar os tokens é o erro que todo mundo comete na primeira tentativa.

As quatro cores têm papel semântico, e é isso que impede o estilo de virar confete: **no máximo
três das quatro por card**, cada uma dizendo a mesma coisa em todos os cards. Cor que muda de
significado entre um card e outro é decoração.

**Fontes:** Cascadia Mono **Light 300** (`Titulo`) · Cascadia Mono 400 (`Corpo`) — `baixar-fontes.sh terminal`

**Entrelinha do título: `0.98`** — `var(--lh-titulo)`. E **teto de corpo: 84px**. É o único dos sete
com teto: aqui o título não cresce até encher o campo, ele para.

Peso leve sobre fundo escuro é o par que funciona — a haste fina ganha contraste do chumbo e a
página respira. O inverso, mono pesada sobre claro, foi a primeira versão deste estilo e lia como
banner.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `MINIMAL CODE-EDITOR POSTER, flat vector artwork. THE ARTWORK FILLS THE ENTIRE IMAGE, EDGE TO`
> `EDGE, FULL BLEED — the dark charcoal #23272C is the background of the image itself. This is NOT`
> `a photograph of a printed sheet and not a screenshot: no paper, no page floating on a surface,`
> `no drop shadow, no table, no mockup, no device. Palette: charcoal ground #23272C, off-white ink`
> `#E6E8EA, and a syntax palette used strictly as small flat colour tokens: blue #6E8BFF, green`
> `#4ADE9B, amber #F0B429, magenta #FF6B9D. Extremely clean and quiet: large empty charcoal areas,`
> `2px hairline rules, everything snapped to an invisible monospaced character grid and to`
> `indentation steps. Colour appears ONLY in short flat bars and small blocks, never as a field.`
> `No window chrome, no title bar, no icons, no UI, no glow, no bloom, no scanlines.`

**A cláusula de sangria não é opcional.** Sem ela as referências voltam como *fotografia de uma
folha impressa sobre uma mesa* — a cor de fundo pedida lê como material, e o modelo desenha o
material. Só a frase `THE ARTWORK FILLS THE ENTIRE IMAGE` resolveu.

**E `no glow` é obrigatório aqui**, o que não vale para nenhum outro estilo: fundo escuro com cor
saturada puxa o modelo para brilho de tela, e brilho neon é o primeiro item da régua antipadrão.

**Grafismo:** 100% CSS/SVG, e mais barato que qualquer outro dos sete: retângulo, fio de 2px,
célula, recuo. Barra curta de cor é a unidade. Nunca ícone, nunca janela, nunca cursor.

**Material: nenhum, e é regra.** Grão e fibra citam impresso, e este estilo cita tela — a limpeza
é o material dele. Ruído aqui não envelhece a peça, suja. E **brilho também não entra**: nada de
glow atrás de token, nada de scanline, nada de vinheta. Chumbo chapado.

**Ritmo:** muda a profundidade do recuo e qual cor domina. Um card em azul, o seguinte com uma
única ficha magenta, um terceiro só em fio e vazio.

**Cuidado verificado:** este é o único dos sete em que **o título vai em caixa baixa** e com teto
de corpo. Mono em caixa alta cresce demais na largura e vira parede, e a régua de ~45 caracteres
por linha a 34px sobre 924px encurta ainda mais quando o corpo sobe. Caixa baixa é também o que o
estilo cita: código não grita.

O outro risco é o fundo escuro. **Escuro com acento saturado é o visual que hoje lê como IA** — e a
régua antipadrão da própria skill derruba. O que separa este estilo daquilo são três coisas, e as
três precisam estar presentes: **peso leve** (não bold), **quatro cores com papel semântico** (não
um neon só), e **vazio de verdade** (não card cheio com glow).

O segundo risco é escrever código de verdade no grafismo. **Barra colorida é muda; `const x = 3`
não é** — e ali vale a regra de sempre: texto dentro de grafismo só se veio da etapa 4.

**O cartaz aqui:** cartaz de conferência de linguagem de programação, impresso em fundo escuro.
Uma ideia, muito vazio, e a cor entrando como marcação.

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

**Cuidado verificado — é o mais sério dos sete:** **o ruído da colagem é inimigo do título.** Na própria referência de cascata, o título ficou sobre a pilha de camadas e a leitura sofreu. Neste estilo a tipografia precisa de **um plano limpo reservado por baixo** — uma tira de papel chapado, uma zona de kraft deixada livre, ou um bloco de cor sólida. Sem esse plano, a hierarquia de leitura cai, e leitura é a prioridade 1.

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

**Grafismo:** CSS puro, e o mais fácil dos sete. `border:5px solid #000` mais `box-shadow:8px 8px 0 #000`, sem blur nenhum. Grade com `repeating-linear-gradient` fino por baixo de tudo.

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

Repare que este é o **único dos sete que pede meio-tom**. Colar aqui o `no midtone` dos outros
estilos mata a direção — é por isso que os blocos são separados e não um só com a paleta trocada.

**Grafismo:** pouquíssimo. Fio, número de página grande em marca-d'água, filete separando colunas, uma tabela quando o conteúdo for comparativo. A referência de bento mostra o melhor achado do estilo: **a grade de fio virando a própria decoração**, com seis das nove células deixadas vazias.

**Material:** grão de papel em `opacity:.10`. Nada mais — este estilo morre com textura por cima.

**Imagem gerada:** uma por carrossel, no máximo duas. Grande, ocupando um terço, **sangrando por um lado**. Imagem pequena e centrada aqui parece thumbnail.

**Ritmo:** muda **qual coluna o título ocupa e onde o vazio fica**. Sem variar isso, oito cards viram oito paredes iguais — é o estilo que mais precisa de disciplina de ritmo e o que mais castiga a falta dela.

**Cuidado verificado:** é o oposto de um carrossel de feed — pouco contraste e muito vazio convidam a diagramar o corpo pequeno. Não caia nisso: **o piso de 30px vale aqui como em todos os outros**, e 34 se o destino é LinkedIn. O vazio deste estilo é a margem, não o corpo do texto. E Fraunces tem eixo óptico: em corpo grande use o corte de display, ou os traços finos somem.

E um risco de estilo, não de execução: papel creme com serifa e acento terracota é hoje **um dos clichês de peça gerada por IA**. O que salva esta direção é o rigor da grade e a quantidade de vazio — se o card ficar "aconchegante" em vez de rigoroso, ele caiu no clichê. Compare com `editorial-1-split.jpg`: dois terços do card são papel vazio, e é isso que o tira do lugar-comum.

**O cartaz aqui:** página de abertura de revista de arquitetura. É a mais literal das sete em relação ao briefing.

---

# 7 · IRIDESCENTE MINIMAL

`irid-1-split.jpg` · `irid-2-cascata.jpg` · `irid-3-bento.jpg`

**Mecanismo:** fundo **off-white fixo** em todos os cards, e uma forma geométrica grande e
centralizada onde mora toda a cor. A iridescência está na sequência das **formas** — o campo não
muda nunca. Composição centralizada, vazio enorme em volta, tipografia sem serifa e leve.

**O fundo era colorido e alternava; não é mais.** Campo saturado em oito cards cansa o olho no
feed e rouba do grafismo o único lugar onde a cor deveria estar. Com o papel fixo, a peça inteira
vira moldura da forma — que é o que este estilo tem de melhor — e a sequência ganha continuidade
em vez de piscar.

**Paleta**

| cor | hex | uso |
|---|---|---|
| papel | `#F7F5F2` | o fundo de **todos** os cards, sem exceção |
| tinta | `#161327` | tipografia |
| lilás | `#B9A7F0` | forma |
| água | `#7ADAD0` | forma |
| pêssego | `#F2B3A0` | forma |
| céu | `#A9C6F5` | forma |

**Duas ou três cores de forma por card, nunca mais.** O que alterna de um card para o outro é
qual delas domina — e é isso que faz a sequência cambiar.

**Fontes:** Hanken Grotesk **Medium 500** (`Titulo`) · Hanken Grotesk 400 (`Corpo`) — `baixar-fontes.sh iridescente`

**Entrelinha do título: `0.97`** — `var(--lh-titulo)`.

**Peso médio, não bold, e a mesma família nos dois.** Grotesca humanista de terminação macia em
peso médio é o que sustenta o tom — bold aqui endurece a peça e briga com o vazio, que é o
material principal. Uma família só nos dois papéis é parte do mesmo silêncio.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `MINIMAL IRIDESCENT POSTER on a plain OFF-WHITE ground #F7F5F2 that fills the entire image, edge`
> `to edge. CENTRED composition with enormous empty off-white space: one single very large simple`
> `geometric graphic dead centre — circle, arc, lens, arch — built from two or three perfectly FLAT`
> `colours of a pearlescent oil-slick family: lilac #B9A7F0, aqua #7ADAD0, peach #F2B3A0, sky`
> `#A9C6F5. All the colour of the poster lives in that one shape; the rest of the page is bare`
> `off-white. Every colour is absolutely flat and even: no gradient, no mesh, no sheen, no glow, no`
> `shimmer, no texture. Calm, quiet, expensive, almost nothing on the page.`

**Grafismo:** círculo, arco, lente, meia-lua, arco pleno. **Uma forma por card**, grande — ela
ocupa de um terço a metade da altura viva, o que é muito maior do que o grafismo dos outros seis.
100% CSS/SVG.

**Imagem: só quando o usuário pedir.** É o único dos sete que **não recebe imagem gerada na capa
por padrão**, mesmo com gerador conectado — e isso vale contra a regra geral da skill. A peça vive
do papel vazio e de uma forma chapada; foto ocupa os dois ao mesmo tempo e sobra um cartaz de
outro estilo.
Se o usuário pedir imagem, ela entra como forma: recortada dentro do círculo, nunca sangrando.

**Material: nenhum, e é regra dura.** Grão, ruído, brilho, textura e degradê estão proibidos.

**Ritmo:** a cor que domina a forma alterna a cada card, e o tamanho da forma cresce e diminui. Ela
sobe ou desce do centro óptico — nunca fica no meio exato duas vezes seguidas. O fundo não entra
no ritmo: ele é a constante contra a qual o resto varia.

**Cuidado verificado:** este estilo passa **a um degradê de distância do clichê de IA.** Forma
chapada sobre papel lê como cartaz de exposição; a mesma forma com um degradê lilás→azul lê como
capa de SaaS, e a régua antipadrão da skill derruba na hora. **Não existe gradiente aqui** — nem
dentro da forma, nem entre formas que se cruzam.

E o segundo risco é a própria centralização: composição centrada em oito cards vira slide de
template. O que salva é a **assimetria vertical** — a forma sobe num card e desce no outro, e o
título nunca fica à mesma altura duas vezes seguidas. Centralizado no eixo x, não no y.

**O cartaz aqui:** cartaz de exposição de arte contemporânea. Papel, uma forma, e o nome pequeno.

---

## A conversa da etapa 2

**Abra pelos recomendados do nível.** A etapa 1 já fechou o nível de imagem, e o critério acima
diz quais estilos ele favorece — comece por esses dois, uma linha cada dizendo por que aquele
nível funciona neles. Depois, uma frase: *"os outros também funcionam aqui — quer ver?"*. E, em
qualquer nível, nomeie os polivalentes: brutalista, neubrutal e editorial servem nos três, e há
quem escolha justamente por isso.

Não descreva os sete em texto e peça para escolher. **Mostre as três referências do estilo** —
`<estilo>-1-split.jpg`, `-2-cascata.jpg`, `-3-bento.jpg` — abertas, não descritas. São três de
propósito: uma capa bonita não prova nada, e o que quebra no card 5 é o estilo não ter três
arquétipos de layout. É isso que a pessoa está julgando.

**Não renderize nada com o assunto dele aqui.** Preview do trabalho real só existe na etapa 7,
com o texto aprovado e o nível de imagem decidido — a regra está no topo da SKILL.md. Preview de
estilo chega antes de qualquer produção, então mostra uma peça feita por um caminho de produção que talvez
nem seja o escolhido, com texto provisório que ainda vai mudar: o usuário opina duas vezes sobre
a mesma coisa e a segunda contradiz a primeira.

Se o usuário pedir **mistura de dois estilos**, resolva por escrito: diga qual dos dois manda em
cada camada — paleta, tipografia, material, grafismo. Estilo misturado quebra quando os dois
disputam a mesma camada; a paleta de um com a grade do outro quase sempre perde os dois.

---

## Procedência das referências

**As referências têm letreiro; os cards não.** É a única exceção à cauda `ABSOLUTELY NO TEXT` que
vale para toda geração desta skill, e ela é deliberada: a referência existe para mostrar **como o
tipo se comporta dentro daquele sistema** — que tamanho ocupa, onde pousa, quanto de vazio sobra
em volta. Sem uma palavra na peça, o usuário está escolhendo um fundo, não uma direção.

Isso não afrouxa o princípio 1: **nenhuma dessas imagens vira card.** Elas são vitrine, e o
letreiro delas é decorativo — em inglês, curto, e ninguém vai lê-lo como conteúdo.

Duas armadilhas apareceram gerando as duas com texto dos estilos novos, e valem para qualquer
regeração:

- **o modelo imprime o próprio prompt.** Pedir tipografia junto com a paleta em hex devolveu um
  cartaz com `blue #6E8BFF / green #4ADE9B` escrito nele. Some com os hex de perto da instrução
  de tipografia, ou proíba explicitamente: `no colour names, no hexadecimal codes`
- **e imprime os escapes.** Pedir `"quiet systems" on two lines` devolveu a peça com o escape
  literal desenhado nela. Diga *a primeira linha lê X, a segunda lê Y* — sem aspas e sem barra



As vinte e uma imagens de `assets/referencias/` foram geradas com **Nano Banana Pro** via MCP do Higgsfield, em 4:5, 2K, a partir de prompts que combinam: o briefing de sistema acima, a especificação de paleta e material de cada estilo, os três arquétipos de layout do variance engine da `high-end-visual-design`, e a lista de antipadrões da `bencium-innovative-ux-designer` aplicada como negativa. Os masters em resolução cheia ficam fora do repositório.
