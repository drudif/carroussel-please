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
| **vazio** — o material principal é a área que não tem nada | terminal | **compete com o material.** Ocupa exatamente o que sustenta a peça |
| **vazio + imagem em bloco** | superminimal | **é o evento.** A cor da peça vem dela — sem imagem, o card é só tipografia sobre branco |
| **vazio + uma foto** | editorial | o sistema prevê **uma** imagem grande sangrando por um lado. Uma, não oito |

**Foto trazida pelo usuário cai na primeira linha**, e por isso lê como nível 2: o que decide é
onde está a massa da peça, não de onde o arquivo veio.

**Com uma ressalva que inverte parte da tabela:** foto do usuário entra **sem tratamento** por
padrão, e estilo que vive de *converter* a foto perde o que tem de melhor. Aí o que serve é
estilo que **emoldura** — **editorial** primeiro, que já é vazio mais uma foto grande, e
**colagem**, que recorta em vez de converter. **Risografia é a que mais sofre:** a tinta riso
existe para cair sobre a imagem, e sem isso vira papel colorido com foto por cima.

Daí sai a ordem em que os estilos são abertos:

| nível | abra primeiro | também funcionam, com o custo dito |
|---|---|---|
| **3 · só código** | **terminal**, **brutalista** | superminimal fica de pé, mas magro — ele quer imagem · riso e colagem viram retícula e recorte desenhados |
| **2 · banco aberto, ou fotos do próprio usuário** | **superminimal**, **colagem**, **riso** | superminimal é o que mais ganha: recorte limpo cai direto no branco, sem tratamento · brutalista só se quantizar em três degraus · terminal não pede foto |
| **1 · gerador** | **riso**, **colagem**, **superminimal** | terminal não pede imagem |

**Brutalista, neo-brutalismo e editorial são polivalentes** — servem nos três níveis, e isso se
diz com essas palavras em qualquer um deles. Não é prêmio de consolação: **quem não quer que a
peça dependa de imagem escolhe exatamente ali**, e essa decisão só aparece se ela for nomeada.

**O funil ordena, não esconde.** Os sete continuam disponíveis e o usuário sabe que são sete. Se
ele escolher fora da recomendação, diga o que muda em uma linha, ofereça mudar de nível **uma
vez**, e siga com a escolha dele.

### O critério roda nos dois sentidos

A mesma pergunta que ordena os estilos **lê uma referência trazida pelo usuário**: olhe onde está
a massa da peça — foto, forma ou vazio — e você tem o caminho que ela exige e o estilo de que ela
está mais perto. É por isso que a oferta de mandar referência mora na etapa 1 e não na 2: ela
responde à pergunta do nível, só que de trás para frente.

A oferta e a pergunta que desfaz a ambiguidade — *referência de como quer que fique, ou imagem
para entrar na arte?* — estão na [etapa 1 da SKILL.md](../SKILL.md#se-ele-trouxer-uma-referência-própria).
O resto da leitura é aqui.

### Ler uma referência trazida pelo usuário

**Cinco perguntas.** São as mesmas cinco em qualquer referência, e as respostas caem direto no
critério do funil:

| o que olhar | e o que isso quer dizer |
|---|---|
| **Onde está a massa da peça** — foto, forma chapada, ou vazio | é o critério inteiro: define o caminho |
| **A tipografia é o evento ou é legenda** | tipo gigante pede estilo de forma; tipo pequeno pede vazio ou foto |
| **Quantas cores, e são chapadas ou têm rampa** | rampa contínua pede foto ou meio-tom; chapado dispensa os dois |
| **Tem material — grão, retícula, fibra, textura — ou é limpo** | material impresso quase sempre veio de foto processada |
| **A composição é split, cascata, bento ou centralizada** | diz qual arquétipo o carrossel vai puxar. Muito branco com um bloco de imagem e nada mais é sinal de superminimal |

Devolva em **duas frases, sem jargão**, e nessa ordem: o que a peça precisa para existir, e de
qual dos sete ela está mais perto.

> *"Essa aí vive de foto tratada — dá para fazer com banco grátis, e fica ainda mais parecida
> com imagem sob medida. Entre os sete, ela é praticamente a colagem."*

**A referência não vira um oitavo estilo.** Ela escolhe entre os sete e afina o escolhido —
paleta, peso do tipo, quanto de vazio. Direção inventada na hora sai bonita na capa e quebra no
card 5, e é por isso que os sete são fechados. Se o usuário insistir em reproduzir a referência
fora dos sete, é decisão dele: diga em uma linha que a direção não passou por teste de escala,
e siga.

**Se ele já escolheu "feitas sob medida", a referência não mexe no caminho.** Com gerador ligado
os sete funcionam bem, e aí ela serve para afinar o **bloco de prompt** do estilo escolhido:
paleta, peso do tipo, quanto de vazio, que material aparece.

**O que ela NÃO faz é entrar na geração como mídia de referência.** Mídia de referência
sobrescreve a geometria pedida no prompt — medido, três gerações voltaram com a proporção
idêntica ao pixel, por cima de instrução em caixa alta. Num carrossel a composição precisa variar
de card para card, então passar a referência do usuário como imagem congela todos eles no
enquadramento dela. Ver [geradores.md](geradores.md#consistência-entre-os-cards-a-âncora-carrega-tinta-não-composição).

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
| **Superminimal** | funciona, mas magro | **muda de patamar** — a imagem em bloco é o evento do estilo |

Regra fixa: **havendo gerador conectado, todos os cards nascem de gabarito gerado** — não só a
capa. É o laço do gabarito, na etapa 7. A capa é o piso, não o teto: com crédito curto, gere a
capa e o fecho e desenhe o miolo, dizendo o número de créditos ao usuário em vez de decidir em
silêncio.

**Não há mais exceção.** Ela existia para o iridescente minimal, que vivia do campo chapado e
perdia os dois quando entrava foto. O superminimal, que tomou o lugar dele, é o oposto: a imagem
em bloco é o evento.

## As fontes

Doze famílias, quinze faces, **todas OFL 1.1** e **embutidas em `assets/fontes/`** com a licença
de cada uma ao lado. Acentos pt-BR conferidos glifo a glifo — `ÁÀÂÃÉÊÍÓÔÕÚÜÇ áàâãéêíóôõúüç` mais
`º ª « » — " "`. Nenhuma sai de acervo pessoal: o carrossel precisa ser reproduzível por quem
clonar a skill.

```bash
assets/fontes.sh riso        # lê do disco, confere acentos, gera fonts.css — sem rede
assets/fontes.sh --listar
assets/fontes.sh "Space Mono:700"   # família avulsa: aqui sim, baixa
```

O script grava `fonts.css` com as duas faces em base64, sob os nomes `Titulo` e `Corpo`.

**Elas são embutidas e não baixadas** porque o piso de entrelinha e o comprimento de linha do
laço do gabarito são calculados **a partir do arquivo**. Uma revisão da fonte no Google não
quebraria nada — só faria esses números passarem a ser outros, em silêncio, num sistema que
existe para eles serem estáveis entre os oito cards. E **não são subsetadas de propósito**: o
navegador troca só o glifo faltante por outra fonte, sem erro, e os esqueletos usam `→` e `·`.

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

`fontes.sh` calcula isso sozinho e grava em `fonts.css` como variável CSS. Use a variável em vez do número:

```css
h1 { line-height: var(--lh-titulo) }
```

Os sete já vêm calculados, e são **duas** variáveis:

| Estilo | Título | `--lh-titulo` | `--lh-titulo-q` |
|---|---|---|---|
| brutalista | Anton | **1,15** | 1,65 |
| riso | Antonio | **1,18** | 1,69 |
| riso *com imagem por baixo* | Bricolage Grotesque | **0,97** | 1,39 |
| terminal | Cascadia Mono Light | **0,98** | 1,40 |
| colagem | Bodoni Moda | **1,09** | 1,53 |
| neubrutal | Chivo | **0,95** | 1,35 |
| editorial | Fraunces | **0,99** | 1,39 |
| superminimal | Plus Jakarta Sans Medium | **1,06** | 1,48 |

Repare que **Anton é o caso extremo**: caixa alta de 0,867 em, mas o acento chega a 1,101 — mais alto que o próprio corpo da fonte. É por isso que ela é a única do conjunto que precisa de entrelinha maior que o tamanho da letra.

### A segunda coluna resolve leitura, não colisão — e o esqueleto aplica sozinha

A primeira coluna impede que o acento de baixo **encoste** na letra de cima. A segunda resolve
outro defeito, que passou por essa trava e saiu num PNG entregue:

```
EM BROWNING,
O ALMOÇO CHEGA
NA PISTA          ← leu "NA PISTÁ"
```

A cedilha de `ALMOÇO` **não colidiu** — ficou 3px acima do último `A` de `NA PISTA`. E virou o
acento dele. **Não encostar não é o critério; o critério é a cauda continuar pertencendo à
palavra de cima.** Por isso a folga da segunda coluna é óptica, `0,24em`, e não os `0,04em`
geométricos da primeira: com 0,04 são 3px e lê como acento; com 0,24 são 18px e a palavra volta.

Duas consequências práticas:

- **Não escolha a coluna na mão, e não olhe o PNG para decidir.** O esqueleto troca sozinho:
  se qualquer linha do título que não seja a última tem `Ç`, `Q` ou `J`, ele usa
  `--lh-titulo-q`. Julgamento visual foi o que deixou passar
- **Não recalcule o piso por string.** Otimizar para o par de linhas real dá um número menor —
  foi assim que o card acima ficou com `1.221`, que é geometricamente correto e
  tipograficamente errado. **O piso publicado já é o pior caso da família, e é o número seguro**

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

**Fontes:** Anton 400 (`Titulo`) · IBM Plex Mono 400 (`Corpo`) — `fontes.sh brutalista`

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

**Fontes:** **Antonio 700** (`Titulo`) · Newsreader 400 (`Corpo`) — `fontes.sh riso`

**Entrelinha do título: `1.18`** — `var(--lh-titulo)`.

**O par muda quando entra imagem gerada.** Com o card composto só de tipo e forma — o nível 3,
que é o padrão —, a Antonio é a certa: condensada, ela devolve linha longa em corpo grande, e é
corpo grande que faz a chapa fora de registro ler como material em vez de defeito. O
deslocamento de 9px que some numa Bricolage de 70px é evidente numa Antonio de 110px.

**A condição é a imagem passar POR BAIXO DO TIPO** — recorte de colagem, foto tratada sangrando
atrás das letras. Aí a Antonio perde: sobre foto reticulada a haste fina de uma condensada some,
e volta a **Bricolage Grotesque 800**, pesada o bastante para se segurar — `fontes.sh
riso-imagem`.

**Com laço do gabarito, a condição NÃO se aplica, e trocar a fonte estraga o laço.** O laço
existe justamente para o tipo cair numa **zona chapada declarada**, nunca sobre retícula — e o
que ele compra é o sistema de comprimento de linha que o gabarito acabou de entregar. Medido
contra um gabarito real, pela régua de substituição:

| | razão larg/caixa-alta | densidade | espessura da haste | desvio total |
|---|---|---|---|---|
| **gabarito** — o que o modelo desenhou | 4,192 | 0,600 | 15,2% | — |
| Bricolage Grotesque 800 | 8,297 | 0,510 | 23,2% | **166%** |
| Archivo 800 | 8,179 | 0,551 | 25,3% | 170% |
| **Antonio 700** | 4,514 | 0,532 | 14,8% | **21,5%** |

A Bricolage tem **o dobro da largura** do que o modelo desenha. Seguir a regra pela leitura
antiga — *"havendo imagem gerada"*, que descreve exatamente o nível 1 — jogaria fora a única
coisa que o laço compra. **Nível 1 é Antonio.**

**O grão vai ACIMA do texto, e isso é regra, não gosto.** Tipo vetorial nítido sobre chapa
impressa lê como adesivo colado por cima da peça — as duas superfícies não se encontram. Uma
camada de grão ou fibra em `opacity:.13`, **acima de tudo, inclusive do texto**, é o que faz
elas virarem a mesma coisa. Sobre chapa gerada use `.13` e não os `.34` do papel limpo: embaixo
já existe a textura que veio na própria chapa, e somar as duas suja a letra.

**Retícula por cima do texto continua proibida** — ela tem estrutura, e estrutura come a
leitura. Grão fino não é retícula: é ruído sem forma, e a diferença é exatamente essa. Os dois
esqueletos já trazem a camada montada no z-index certo.

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

**Material:** obrigatório — é o estilo. Retícula em `opacity:.38`, fibra em `.16`. **A retícula
fica abaixo do texto; a fibra e o grão, acima** — retícula tem estrutura e come a leitura, que é a
prioridade 1; grão é ruído sem forma e é justamente o que faz tipo e chapa virarem a mesma
superfície. É essa a ordem dos dois esqueletos.

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

**Fontes:** Cascadia Mono **Light 300** (`Titulo`) · Cascadia Mono 400 (`Corpo`) — `fontes.sh terminal`

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

**Fontes:** Bodoni Moda 900 (`Titulo`) · Karla 400 (`Corpo`) — `fontes.sh colagem`

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

**Fontes:** Chivo 900 (`Titulo`) · Chivo Mono 400 (`Corpo`) — `fontes.sh neubrutal`

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

**Fontes:** Fraunces 700 (`Titulo`) · Work Sans 400 (`Corpo`) — `fontes.sh editorial`

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

**Cuidado verificado:** é o oposto de um carrossel de feed — pouco contraste e muito vazio convidam a diagramar o corpo pequeno. Não caia nisso: **o piso de 34px vale aqui como em todos os outros**. O vazio deste estilo é a margem, não o corpo do texto. E Fraunces tem eixo óptico: em corpo grande use o corte de display, ou os traços finos somem.

E um risco de estilo, não de execução: papel creme com serifa e acento terracota é hoje **um dos clichês de peça gerada por IA**. O que salva esta direção é o rigor da grade e a quantidade de vazio — se o card ficar "aconchegante" em vez de rigoroso, ele caiu no clichê. Compare com `editorial-1-split.jpg`: dois terços do card são papel vazio, e é isso que o tira do lugar-comum.

**O cartaz aqui:** página de abertura de revista de arquitetura. É a mais literal das sete em relação ao briefing.

---

# 7 · SUPERMINIMAL

`superminimal-1-split.jpg` · `superminimal-2-cascata.jpg` · `superminimal-3-bento.jpg`

**Mecanismo:** fundo **branco**, texto **preto**, e a imagem entrando como **bloco chapado
direto sobre o branco** — sem moldura, sem sombra, sem borda, sem forma nenhuma acompanhando.
Não existe grafismo neste estilo: **a imagem é o grafismo**, e o resto é vazio e tipografia.

**Este estilo substituiu o iridescente minimal**, que vivia de uma forma geométrica grande e
chapada sobre papel off-white. A troca não foi de paleta: o iridescente **recusava foto** —
era o único dos sete assim —, e o superminimal é o oposto. Aqui a imagem é o evento.

**Paleta**

| cor | hex | uso |
|---|---|---|
| papel | `#FFFFFF` | o fundo de **todos** os cards, sem exceção |
| tinta | `#0B0B0C` | tipografia |
| cinza | `#86868B` | texto secundário, paginação, assinatura |

**Três cores, e nenhuma delas é acento.** A cor da peça vem **das imagens** — é por isso que não
existe cor de destaque aqui. Acrescentar uma mata o estilo: o branco deixa de ser o material e
vira fundo.

**Fontes:** Plus Jakarta Sans **Medium 500** (`Titulo`) · Plus Jakarta Sans 400 (`Corpo`) —
`fontes.sh superminimal`

**Entrelinha do título: `1.06`** — `var(--lh-titulo)`. Com `Ç`, `Q` ou `J` numa linha que não é a
última, o esqueleto troca sozinho para `1.48`.

**A fonte pedida era a Satoshi, e ela não pode ir no pacote.** A licença do Fontshare permite usar,
comercialmente inclusive, e **proíbe redistribuir** — *"uploading them in a public server"*, que é
exatamente o que um repositório público faz. Rodei a régua de substituição contra Satoshi Medium:

| | razão larg/caixa-alta | densidade | haste | desvio |
|---|---|---|---|---|
| **Satoshi Medium** (gabarito) | 6,832 | 0,240 | 10,5% | — |
| **Plus Jakarta Sans 500** | 6,792 | 0,243 | 9,9% | **7,2%** |
| Onest 500 | 6,665 | 0,255 | 10,5% | 9,1% |
| Manrope 500 | 6,648 | 0,238 | 9,5% | 12,2% |
| Geist 500 | 7,104 | 0,266 | 11,5% | 24,2% |

7,2% é casamento apertado — para calibrar, a Antonio ficou a **21,5%** do gabarito da risografia e
foi considerada boa. Quem quiser o traço literal baixa a Satoshi em `fontshare.com` e roda
`fontes.sh "Satoshi:500"`; o caminho de família avulsa existe para isso.

**Tipografia, o que importa:** título grande com `letter-spacing` **negativo** — `-.03em` a
`-.04em` —, que é o que separa esta escola de uma sem-serifa qualquer. Corpo em cinza, pequeno,
com muito ar. E a razão título/corpo aqui é maior que os 2,5:1 da skill: fica perto de **4:1**.

**Grafismo: não existe.** Regra dura, e é o que define o estilo. Nada de forma, fio, régua,
moldura, ícone, tile, contorno ou sombra. Se um card não tem imagem, ele é **só tipografia sobre
branco** — e isso é uma composição legítima, não um card faltando.

**Imagem: em bloco, direto no branco.** Sangrando por uma borda, ou como retângulo com margem
generosa. **Nunca com canto arredondado, nunca com sombra, nunca dentro de moldura.** Foto
recortada em fundo branco é o caso ideal; foto de cena inteira também serve, desde que o bloco
seja limpo.

**Ritmo: é aqui que o estilo se prova.** A diagramação é solta e muda de card para card — o bloco
de imagem sobe, desce, sangra por um lado, ocupa metade, ocupa dois terços, some. O título vai ao
topo num card e ao pé no outro. **Oito cards com a imagem no mesmo lugar viram catálogo de
template**, que é a morte deste estilo — ele não tem material nem cor para disfarçar repetição.

**Bloco de prompt** — cole antes do assunto em toda geração deste estilo:

> `ULTRA-MINIMAL PRODUCT PHOTOGRAPH on a pure WHITE seamless background #FFFFFF that fills the`
> `entire image, edge to edge. One single subject, centred or slightly off-centre, lit with soft`
> `even studio light and a very subtle contact shadow directly beneath it only. Enormous empty`
> `white space around the subject. Colour comes from the subject alone; the ground stays pure`
> `white. Crisp focus, high detail, no vignette. No frame, no border, no rounded corners, no drop`
> `shadow, no gradient, no reflection, no props, no background scenery, no texture.`

**Sem gerador, é o estilo que mais ganha com banco de imagem.** Foto de banco com recorte limpo
cai direto no branco sem tratamento nenhum — e este é o único dos sete em que **não tratar é o
certo**, porque qualquer conversão de cor tira da foto o que ela veio trazer. Em código puro ele
funciona, mas fica sendo tipografia sobre branco com blocos de cor chapada: honesto, e mais magro.

**Cuidado verificado:** o risco aqui não é parecer feito por IA — é **parecer não-feito**. Branco
com pouco texto passa perto de "slide em branco", e o que separa uma coisa da outra é a
tipografia: corpo grande o bastante, `letter-spacing` negativo no título, e o vazio **contíguo**,
não distribuído. Quatro folgas iguais leem como erro de diagramação; um vão único e grande lê como
decisão.

E o segundo: **canto arredondado.** É o reflexo de quem diagrama "estilo Apple" e é exatamente o
que faz a peça ler como print de app dentro do card. Aqui tudo é canto vivo.

**O cartaz aqui:** página de produto. Uma coisa, muito branco, e o nome dela pequeno embaixo.

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
