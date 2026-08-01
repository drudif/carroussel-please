---
name: carrossel
description: Use quando o usuário pedir um carrossel para Instagram ou LinkedIn com arte pronta — "faz um carrossel", "post pro Instagram", "cards pro feed", "slides pro Insta", "carrossel de projetos", "documento pro LinkedIn", "monta a arte do carrossel". Também quando um carrossel gerado por modelo de imagem saiu com letra torta ou acento errado e precisa ser refeito, ou quando o usuário quer transformar prints de um app, um processo ou uma lista em post editorial. Entrega PNGs 1080x1350 e um PDF sequencial.
metadata:
  language: pt-BR
  estilos: 6, fixos — ver references/estilos.md
  geracao-de-imagem: opcional; chave de API ou conector. Quatro dos seis estilos não precisam
  embutido: sprayantislop (Fernando Drudi) sobre Zero-Lero (MIT, Vinicius Stanula)
  destilado: brainstorming, carousel-writer-sms, bencium-innovative-ux-designer, high-end-visual-design
  autossuficiente: não depende de nenhuma outra skill estar instalada — ver CREDITOS.md
---

# Carrossel

Carrossel de feed com arte-final. **Toda tipografia é renderizada em HTML/CSS e capturada em PNG.** Modelo de imagem entra só onde não há palavra a ler.

Tudo de que a skill precisa está dentro dela. Nada aqui depende de outra skill estar instalada — ver [CREDITOS.md](CREDITOS.md).

## Os três princípios

**1. Modelo de imagem erra letra — e erra o acento primeiro.** Nenhuma palavra que o leitor vai ler sai de gerador de imagem. Nem o título, nem a paginação, nem o arroba. Não é preferência de qualidade: é a diferença entre entregar e refazer.

**2. Desenhar vem antes de gerar.** A maior parte do que um carrossel precisa — grade, blocos, ícones, abstração de interface, diagrama, tabela — se desenha em HTML/CSS/SVG com controle total e custo zero. **Interface desenhada em blocos ganha de print com filtro aplicado.** O gerador entra no que não se desenha: retrato, cena, textura, colagem. Ver [references/grafismos.md](references/grafismos.md).

**3. Nada avança sem aprovação.** Seis etapas com trava entre elas. Refazer oito cards renderizados custa muito mais do que uma pergunta.

## O fluxo

```dot
digraph carrossel {
  "0 · Perfil" [shape=box];
  "1 · Estilo" [shape=box];
  "2 · Direção aprovada?" [shape=diamond];
  "3 · Conteúdo" [shape=box];
  "4 · Anti-slop" [shape=box];
  "5 · Texto aprovado?" [shape=diamond];
  "6 · Produção" [shape=box];
  "PNG + PDF" [shape=doublecircle];

  "0 · Perfil" -> "1 · Estilo" -> "2 · Direção aprovada?";
  "2 · Direção aprovada?" -> "1 · Estilo" [label="não"];
  "2 · Direção aprovada?" -> "3 · Conteúdo" [label="sim"];
  "3 · Conteúdo" -> "4 · Anti-slop" -> "5 · Texto aprovado?";
  "5 · Texto aprovado?" -> "3 · Conteúdo" [label="não"];
  "5 · Texto aprovado?" -> "6 · Produção" [label="sim"];
  "6 · Produção" -> "PNG + PDF";
}
```

O protocolo de como perguntar — uma por vez, múltipla escolha, trava a cada bloco — está em [references/texto.md](references/texto.md). Este arquivo diz *o quê* e *em que ordem*.

## Duas regras de conversa que valem o fluxo inteiro

### Nunca pergunte duas vezes a mesma coisa

Na etapa 0 você já ficou sabendo: **quem assina, onde publica, o assunto e quantos cards.**
Nada disso se pergunta de novo mais adiante. Se precisar confirmar, **afirme e peça o aceite**
— "são sete cards, certo?" — nunca "quantos cards você quer?". Repetir a pergunta faz parecer
que você não estava prestando atenção, e é a queixa mais comum de quem testa a skill.

Antes de perguntar qualquer coisa, releia o que já foi dito na conversa. Se a resposta está lá,
use.

### Fale como quem explica para um cliente, não para outro programador

A pessoa do outro lado quer um post bonito. Ela não precisa saber como a peça é feita.

| não diga | diga |
|---|---|
| "vou renderizar em HTML/CSS e capturar via headless" | "vou montar a arte e te mostrar" |
| "aplicando duotone com mapeamento de rampa na paleta" | "vou deixar a foto nas cores do estilo" |
| "o corpo está com 30px, abaixo do piso" | "o texto ficou pequeno demais para o feed, vou subir" |
| "gerando o gabarito para extrair as coordenadas" | *não diga nada — isso é trabalho interno* |
| "detectei conflito na área de segurança" | "isso ia sumir no corte do LinkedIn, arrumei" |

**Etapa intermediária não se narra.** Gabarito, medição, teste de fonte, chapa limpa: some com
tudo. Quem pede um carrossel quer ver o carrossel.

E quando algo der errado, diga **o que ficou ruim e o que você vai fazer** — não o nome técnico
do defeito.

---

## Etapa 0 — Perfil

Leia `~/.claude/carrossel-perfil.md`. **Se existir**, mostre um resumo de três linhas e pergunte só o que muda neste trabalho. **Se não existir**, faça a conversa de setup e grave ao final.

**Há um terceiro estado, e ele é pedido com frequência:** *"esquece o que está salvo, faz como
se eu fosse novo"*. Quem acabou de instalar a skill quer testá-la na própria máquina, e o
perfil dele atrapalha o teste. Nesse caso rode o setup inteiro e **não leia o arquivo** — mas
**não sobrescreva nem apague o arquivo real**, e ao fim pergunte se o resultado deve substituir
o que estava lá. Se ele disse "ignore o gerador conectado" junto, trate como quem nunca
conectou nada: as opções sem conexão vão na conversa como se fossem as únicas.

As perguntas estão em [references/perfil.md](references/perfil.md), em três rodadas curtas e **sem jargão**. Elas cobrem: quem assina e onde publica, se há identidade de marca fechada, e se o usuário quer gerar imagem ou desenhar tudo.

Antes de propor estilo você precisa saber também: **o assunto e quantos cards**. Sem isso não dá para testar se uma direção escala.

## Etapa 1 — Estilo

São **seis, fixos**, especificados em [references/estilos.md](references/estilos.md) com paleta em hex, par tipográfico, material e o cuidado verificado de cada um:

| | Estilo | Em uma linha |
|---|---|---|
| 1 | **Brutalista vetorial** | forma chapada de aresta dura sobre papel cru, tipografia condensada como material |
| 2 | **Risografia com textura** | duas tintas que se multiplicam, erro de registro, retícula e fibra |
| 3 | **Janelas** | janelas de sistema em fundo preto, carregando conteúdo real |
| 4 | **Mixed media / colagem** | camadas de origens diferentes, toda emenda à mostra |
| 5 | **Neo-brutalismo colorido** | contorno preto grosso e sombra dura sobre campo saturado |
| 6 | **Minimalista editorial quente** | duas colunas, serifa de contraste alto, e muito vazio |

**Não descreva os seis e peça para escolher.** Cada um tem três referências fixas em `assets/referencias/` — mostre-as. Depois renderize **capa e um card do meio** dos que ele considerar, com o texto provisório do assunto real. É barato e é a única forma honesta de escolher.

Avise, sempre: *o texto do preview é provisório; a decisão aqui é de direção visual.*

Duas coisas ditas **na hora da escolha**, não depois:

- **Se houver gerador conectado**, dois estilos mudam de patamar — risografia e colagem —, e a capa passa a receber imagem gerada sempre. Se não houver, quatro deles ficam completos assim mesmo
- **O neo-brutalismo colorido tem prazo de validade.** É o visual mais usado em post de design hoje: acerta fácil e envelhece rápido. Isso muda a decisão, então é informação de antes

Para a régua de gosto — escala, respiro, o que faz uma peça parecer cara e o que a faz parecer gerada por IA — use [references/visual.md](references/visual.md).

## Etapa 1.5 — Qualidade das imagens

**Depois do estilo, antes de qualquer arte.**

Pergunte pelo **resultado**, não pelo que a pessoa tem instalado. Ela escolhe o que quer e
depois descobre o que aquilo exige — o contrário faz escolher no escuro. E nada de "MCP",
"API" ou "nível A": ninguém que nunca conectou nada sabe o que é isso.

◇ **Como você quer as imagens do carrossel?**

| | Opção | O que você ganha | O que precisa |
|---|---|---|---|
| 1 | **Feitas sob medida** | ilustração criada para o seu assunto, no estilo e nas cores escolhidas | uma conta num gerador de imagem, ligada aqui. Te ajudo |
| 2 | **De banco grátis** | fotos e ilustrações de sites abertos, tratadas nas cores do estilo | nada. Já funciona |
| 3 | **Sem foto nenhuma** | tudo desenhado em código, nas cores exatas | nada. Já funciona |

Três coisas ditas junto, em uma linha cada:

- **Só a 1 responde ao seu assunto.** Nas outras duas você usa o que existe
- **A 3 não é a versão pobre.** Em brutalista, janelas e neo-brutalismo o desenho costuma
  ficar melhor que foto, porque nasce já nas cores certas
- **A 2 depende do tema dar foto.** Relacionamento, viagem, comida, trabalho manual: rende.
  Um método, um conceito, uma ferramenta: não existe foto disso, e aí a 3 ganha

### Se escolheu a 1

◇ **Você já tem conta em algum gerador de imagem?**

Diga a verdade **antes** de tentar, porque metade dos casos não conecta:

| conta | dá para ligar? |
|---|---|
| **Gemini** | sim, e é o mais fácil. A chave é grátis |
| **ChatGPT Plus ou Pro** | **a assinatura não serve.** O acesso automático é cobrado à parte |
| **Higgsfield, Magnific** | sim, pelos conectores. Gasta crédito da assinatura |
| **Midjourney** | não dá para ligar. Mas dá para gerar por lá e me entregar o arquivo |

Essa última linha vale para qualquer conta que não conecte: **gerar na mão e entregar o
arquivo funciona.** Não é o ideal, é melhor do que desistir da imagem.

Não tendo conta nenhuma, ofereça a 2 ou a 3 — não empurre assinatura.

O passo a passo de cada ligação está em [references/geradores.md](references/geradores.md).
Em todos: **a chave nunca é colada no chat** — o que passa por aqui fica registrado. A pessoa
guarda no computador dela e responde só "pronto". A skill grava o fato,
`gemini: chave configurada em AAAA-MM-DD`, nunca o valor.

## Etapa 2 — Aprovação da direção

Não avance sem resposta explícita. Se o usuário pedir mistura de dois estilos, produza a mistura e mostre antes de seguir — estilos misturados costumam brigar, e é melhor descobrir agora.

Ao fechar, registre em `DIRECAO.md` na pasta do trabalho: paleta em hex com o uso de cada cor, fontes com nome de arquivo, lógica de grade, e como cada tipo de card se comporta.

**Cheque os acentos antes de fechar.** Os doze pares dos seis estilos já foram conferidos glifo a glifo. Mas se o usuário trouxe fonte de marca, renderize `ÁÀÂÃÉÊÍÓÔÕÚÜÇ áàâãéêíóôõúüç` e olhe — o navegador troca só o glifo faltante por outra fonte, o que é pior do que quebrar, porque passa despercebido. Faltando: troque a fonte, ou use **`abrasileirar-fonte`** para desenhar os acentos no traço da própria fonte.

## Etapa 3 — Conteúdo

**Três perguntas, e só.** Escrever card a card não é trabalho do usuário — é da `carousel-writer-sms`, embutida em [references/texto.md](references/texto.md). A entrevista define *o que* e *como* dizer ao longo do carrossel, não arranca o texto pronto dele.

Uma por vez:

◇ Qual é sua tese — a única coisa que o leitor tem que levar embora?
◇ Como termina? (comentar · salvar · seguir · instalar · outro)
◇ Tem algum dado seu, número ou história, que só você poderia contar?

▸ Com isso, **proponha o mapa dos cards**: uma sinopse de uma linha por card, numerada, mais o gancho da capa. Não é o texto final, é o roteiro — e é sobre ele que o usuário opina.

◇ O mapa fecha assim?

Só depois do mapa aprovado o texto é escrito de verdade.

**Por que nesta ordem:** discutir o mapa custa uma rodada; descobrir na etapa 5 que o carrossel conta a história errada custa todas. E sete linhas de roteiro se julgam melhor que sete blocos de texto acabado, onde a redação disputa atenção com a estrutura.

A regra que vale em qualquer plataforma: **um card = uma ideia**. Essa não cede nunca.

**O tamanho do corpo, sim.** As 25 palavras são a régua do Instagram; o LinkedIn aceita
profundidade, e quando o usuário marca os dois destinos as duas regras se contradizem. Quem
ganha:

- **Marcou só Instagram** → 25 palavras, e se não coube são dois cards
- **Marcou LinkedIn, com ou sem Instagram** → o teto passa a ser **físico, não editorial**:
  o corpo cresce até onde a zona do grafismo começaria a ser esmagada, e quem diz onde é isso
  é o `?medir=1`, não a contagem. Costuma dar o dobro
- **Assunto que exige traduzir termo** — "função executiva", "externalidade", qualquer coisa
  que o público não tem — **entra no segundo caso mesmo em post só de Instagram.** Cortar a
  tradução para caber na régua entrega um card que não explica nada, e a crítica que volta é
  "está superficial"

E há uma saída que não custa card nem palavra do corpo: **em janelas, colagem e neo-brutalismo
o grafismo carrega texto de verdade.** A definição do conceito vai para dentro da janela, da
tira de papel ou do balão, e o corpo continua sendo só o argumento. É como se tem o dobro de
conteúdo sem perder "uma ideia por card" — e o que vai ali é conteúdo aprovado na etapa 3, o
que mantém a regra do grafismo mudo de pé.

## Etapa 4 — Anti-slop

**Só texto.** Capa, corpo, CTA, legenda e alt text. Está embutida em [references/anti-slop.md](references/anti-slop.md), com os arquivos em `references/anti-slop/`. Não precisa instalar nada.

**A revisão de slop gráfico saiu daqui.** Ela produzia texto genérico para descrever problema visual — o oposto do que esta etapa existe para fazer. O que é visual se resolve olhando o PNG na etapa 6, com a checagem antipadrão.

**Obrigatório antes de mostrar qualquer texto ao usuário.**

Se você passou o texto e não cortou nada, você não aplicou. Volte e aplique.

**Grave o registro dos cortes no arquivo, não na resposta.** No momento em que o usuário precisa julgar o texto, a memória de cálculo atrapalha. A única exceção é um corte que atropelou o que parecia escolha deliberada de voz — esse você aponta, em uma linha, para ele decidir.

## Etapa 5 — Aprovação do texto

Mostre os cards numerados, a legenda e o alt text, **limpo** — sem justificar o que foi cortado.

**Diga isto, com estas palavras ou parecidas:**

> Os textos estão em `TEXTOS.md`, na pasta do trabalho. **Se quiser mudar qualquer palavra, edita
> direto lá e me avisa aqui** — eu regero a arte a partir do arquivo. Você não precisa mexer em
> código nem descrever a alteração no chat.

Isso não é conveniência, é a diferença entre uma rodada e cinco. Descrever alteração de texto por
chat é lento e impreciso; abrir o arquivo e digitar é imediato. E **só funciona se a arte ler o
`.md` de verdade** — o padrão está em [references/montagem.md](references/montagem.md). Se você
embutiu o texto no HTML, a promessa é falsa e o usuário vai descobrir na primeira correção.

Ofereça **uma capa alternativa**. A capa é o único card que decide se os outros sete existem.

## Etapa 6 — Produção

Agora, e só agora, monte a arte. O manual técnico completo — esqueleto, captura, área de segurança, PDF e as armadilhas que custam tempo — está em [references/montagem.md](references/montagem.md).

1. Copie `assets/esqueleto.html` para a pasta do trabalho e aplique a direção aprovada. **O HTML lê `TEXTOS.md`; ele não guarda texto**

   **Copie e troque valores. Não reescreva o CSS do zero.** Parece mais rápido escrever um
   arquivo limpo com a direção já aplicada, e é onde a produção quebra: o esqueleto carrega
   propriedades que não parecem importantes e são estruturais — `white-space:nowrap` no `.tt`,
   que impede o título de quebrar sozinho, e `overflow:hidden` no `.gfx`, que é o que faz o
   empilhamento valer para elemento posicionado em absoluto. Quem reescreve perde as duas e
   descobre depois de capturar, olhando. **Mude cor, fonte, tamanho e composição; a mecânica
   fica.** Vale o mesmo para os scripts: `exportar.sh` já traz o laço de captura, a checagem de
   erro de JS e a conferência dos PNGs. Reimplementar isso custa as armadilhas de novo
2. `assets/baixar-fontes.sh <estilo>` gera o `fonts.css` com as faces embutidas
3. `assets/exportar.sh` captura os PNGs em 1080×1350 e monta o PDF
4. **Abra cada PNG e olhe.** Captura falha em silêncio: sai arquivo do tamanho certo, em branco
5. Passe a checagem antipadrão abaixo

**Apresente o resultado ao usuário, não o caminho da pasta.** Mandar alguém abrir um diretório
para ver o próprio trabalho é a pior parte de uma entrega boa.

**Mas confirme que ele viu.** Abrir um PNG com a ferramenta de leitura mostra a imagem **para
você, não para ele** — em várias superfícies isso não chega do outro lado, e a etapa vira uma
pergunta de aprovação sobre uma imagem invisível. Aconteceu em produção: a folha de contato foi
montada, descrita e submetida à decisão, e a resposta foi *"não estou vendo as gerações, onde
estão?"*. Uma rodada inteira queimada.

As rotas, em ordem:

| | Rota | Quando |
|---|---|---|
| 1 | `open <arquivo>` | qualquer superfície local. **É o padrão seguro** — abre no visualizador do sistema, e o arquivo aparece sem ninguém procurar pasta |
| 2 | artefato publicado | onde essa capacidade existir. Melhor para folha de contato, porque o usuário navega |
| 3 | imagem na mensagem | só onde a superfície de fato renderiza para quem lê |

Isso vale nas **duas** entregas visuais: o preview de estilo da etapa 1 e a arte da etapa 6.
Em ambas, **mostre e só então pergunte** — nunca as duas coisas na mesma mensagem sem saber se
a imagem chegou.

### O artefato só aparece com a arte pronta

**Etapa intermediária não vai para o usuário.** Gabarito, chapa limpa, medição, teste de fonte — tudo isso é trabalho seu. O que chega é o carrossel montado, com o texto já aplicado como sugestão final.

Mostrar o caminho parece transparência e é ruído: o usuário passa a opinar sobre uma imagem que vai ser jogada fora, e você gasta uma rodada explicando por que ela não é a peça.

Junto com o artefato, o aviso do `TEXTOS.md` da etapa 5 — e a parte que faz diferença dita explicitamente: **o corpo se reajusta ao espaço já reservado em cada card, então mudar uma palavra não desmancha a diagramação.**

### Formatos

| Destino | Arquivo | Observação |
|---|---|---|
| Instagram | PNG 1080×1350 (4:5) | um por card |
| LinkedIn | PDF sequencial **1080×1080** | o corte 1:1 central do mesmo PNG — ver abaixo |
| Stories | PNG 1080×1920 | só se pedirem |

**O PDF do LinkedIn é quadrado, e sai do próprio PNG vertical:** recorte cada card em `y=135..1215`
e monte o PDF com os recortes. Não rediagrame nada — **é exatamente a área de segurança**, e é para
isso que ela existe desde o primeiro pixel. Se algo essencial sumiu no corte, o erro está na
diagramação do card, não no recorte.

```python
sq = [Image.open(p).crop((0, 135, 1080, 1215)) for p in pngs]
sq[0].save('linkedin-1080.pdf', 'PDF', resolution=150, save_all=True, append_images=sq[1:])
```

O feed do LinkedIn é largo e reduz o documento: o piso geral de corpo é **30px** sobre 1080, e
**34px** quando o LinkedIn é o destino principal.

### Área de segurança — obrigatória, sempre

Todo conteúdo essencial fica dentro do **corte 1:1 central**: em 1080×1350, entre y=135 e y=1215, com 78px nas laterais. É o corte mais agressivo que o material vai encontrar, e post orgânico vira impulsionado depois sem ninguém refazer a arte. O esqueleto traz o gabarito: `?card=N&safe=1` desenha as caixas por cima.

---

## Padrões de composição

**A capa tem título dominante.** A razão entre o título e o subtítulo é de pelo menos **2,5:1**. Título grande, sub pequeno, e nada mais — sem eyebrow, sem rodapé, sem rótulo, a menos que carreguem informação que o leitor precisa.

**Slot vazio não se preenche, se elimina.** Se o template criou uma caixa e você precisou inventar texto para ela, a caixa sai e o vazio vira respiro. Ver a auditoria de slots em [references/anti-slop.md](references/anti-slop.md).

**O grafismo é mudo.** Se você desenhou algo e precisou escrever um rótulo para ele se explicar, o problema é o desenho. Texto dentro de grafismo só é legítimo se veio da etapa 3, aprovado, ou se é dado duro e verdadeiro.

**Ritmo por arquétipo.** Os três arquétipos de layout — editorial split, cascata Z, bento assimétrico — entram em rodízio ao longo do carrossel. Oito cards no mesmo arquétipo viram oito paredes iguais.

**Havendo gerador conectado, a capa recebe imagem gerada.** Sempre, qualquer que seja o estilo.

Duas regras sobre essa imagem, ambas em [references/grafismos.md](references/grafismos.md):

- **O assunto vem do tema, não do estilo.** O teste da troca reprova imagem que só combina com a paleta
- **A especificação do estilo vai no prompt.** Paleta em hex, idioma visual, material e proibições — o gerador devolve a peça já na linguagem. Foto neutra tingida com duotone depois lê como foto tingida, não como peça da direção. E se a imagem já veio na paleta, **tire o duotone do CSS**: ele achata o acento

## Hierarquia quando algo não couber

Sacrifique nesta ordem, **de baixo para cima**:

1. **Leitura** — nunca cede. Corpo sobre papel sólido, tamanho que se lê no feed
2. **Respiro** — cede pouco. Vão vazio é composição, não desperdício
3. **Grafismo** — cede primeiro. Encolhe, corta, ou sai

Texto sobrepondo grafismo é falha estrutural, não ajuste fino. Resolva com empilhamento rígido — cabeça, texto, grafismo, pé — onde o texto reserva a altura de que precisa e o grafismo fica com o que sobra. O esqueleto já é assim.

## Checagem antes de entregar

Se qualquer item aparecer na arte, ela lê como feita por IA genérica:

- [ ] Gradiente índigo → violeta, ou qualquer gradiente de dois roxos
- [ ] Vidro fosco: card translúcido com blur e borda branca de 1px
- [ ] Blob 3D, esfera de vidro, forma orgânica renderizada
- [ ] Glow neon atrás de texto ou forma
- [ ] Ícone dentro de tile pastel arredondado
- [ ] Sombra gigante e difusa embaixo de tudo
- [ ] Layout de landing de SaaS: hero centralizado e três cards iguais
- [ ] Emoji como elemento gráfico
- [ ] **Texto legível vindo de modelo de imagem**

E mais:

- [ ] Todos os PNGs abertos e olhados, um a um
- [ ] **Nenhum texto coberto — nem por grafismo, nem por outro grafismo.** Em janelas, colagem
      e em qualquer cascata os elementos se sobrepõem por projeto: o que come letra ali não é o
      texto do card sobre o desenho, é um elemento do desenho sobre o texto de outro
- [ ] Nada essencial fora da área de segurança
- [ ] Nenhum corte ou overflow — confira também os 8px finais de cada PNG
- [ ] Print de app real revisado por dado pessoal: nome, e-mail, cliente, token
- [ ] Acentos conferidos, se entrou fonte de fora dos seis estilos
- [ ] Ritmo: passando os cards em sequência, algo muda de posição ou escala
- [ ] Alt text escrito, um por card
- [ ] Legenda passou pela mesma régua anti-slop

## Red flags — pare e volte uma etapa

Estes pensamentos aparecem quando o usuário diz "tenho pressa". Todos custam mais tempo do que economizam.

| O que você vai pensar | O que é verdade |
|---|---|
| "Com pressa, conversa de setup é hostil" | Roda uma vez e fica salva. Errar a lista invalida os oito cards |
| "Descrevo os seis estilos, ele escolhe pelo nome" | Ninguém escolhe direção visual lendo. Mostre a referência e renderize |
| "Adianto a arte enquanto ele responde o texto" | A etapa 1 pode adiantar; direção não depende de copy. A 6 nunca |
| "Meu default escuro com acento neon é bonito e seguro" | É exatamente o visual que hoje lê como IA. Seguro e indistinguível são a mesma coisa |
| "Preview da capa já mostra a direção" | Direção quebra no card 5, não na capa. Renderize um card do meio |
| "O gerador acertou a letra dessa vez" | Acertou nessa geração. Não vai acertar nas oito. E o acento é onde ele erra primeiro |
| "Gero a imagem e ajusto o texto pra caber" | O texto passa a servir a imagem. Inverte a peça inteira |
| "Isso é fácil de desenhar, gero mais rápido" | Gerar custa uma rodada de prompt, uma de download e uma de recorte. Um `<div>` custa uma linha |
| "Depois eu olho os PNGs" | Captura falha em silêncio. Olhe antes de entregar, um por um |
| "Mando a pasta e ele abre" | Entrega é o que ele vê, não o que ele encontra |

## Sobre disparar agentes

**O padrão é fazer tudo aqui, em sequência.** Subagente não pergunta nada ao usuário, e a premissa desta skill é perguntar tudo — as etapas 0, 2 e 5 são indelegáveis por natureza, e a 6 é o laço de renderizar, olhar e ajustar com o usuário no meio, onde um agente só adiciona ida e volta e perde o contexto visual.

Sobra **um** caso em que delegar compensa: renderizar previews de vários estilos em paralelo na etapa 1, num carrossel grande. Isso é opt-in explícito do usuário, nunca padrão.

## Onde delegar

| Situação | Vá para |
|---|---|
| Revisar texto que já existe, fora de carrossel | `sprayantislop` ou `deslopar` |
| Fonte de marca sem acento em pt-BR | `abrasileirar-fonte` |
| Peça única, não swipeable | `post-writer-sms` |
| Só a legenda do post | `caption-writer-sms` |

O que é só desta skill: a ordem das seis etapas, os seis estilos fechados, o desenho antes da geração, e a montagem em código.
