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

---

## Etapa 0 — Perfil

Leia `~/.claude/carrossel-perfil.md`. **Se existir**, mostre um resumo de três linhas e pergunte só o que muda neste trabalho. **Se não existir**, faça a conversa de setup e grave ao final.

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

## Etapa 2 — Aprovação da direção

Não avance sem resposta explícita. Se o usuário pedir mistura de dois estilos, produza a mistura e mostre antes de seguir — estilos misturados costumam brigar, e é melhor descobrir agora.

Ao fechar, registre em `DIRECAO.md` na pasta do trabalho: paleta em hex com o uso de cada cor, fontes com nome de arquivo, lógica de grade, e como cada tipo de card se comporta.

**Cheque os acentos antes de fechar.** Os doze pares dos seis estilos já foram conferidos glifo a glifo. Mas se o usuário trouxe fonte de marca, renderize `ÁÀÂÃÉÊÍÓÔÕÚÜÇ áàâãéêíóôõúüç` e olhe — o navegador troca só o glifo faltante por outra fonte, o que é pior do que quebrar, porque passa despercebido. Faltando: troque a fonte, ou use **`abrasileirar-fonte`** para desenhar os acentos no traço da própria fonte.

## Etapa 3 — Conteúdo

Só agora. As cinco perguntas, a estrutura em quatro zonas, as regras de tamanho e a tabela de formato por plataforma estão em [references/texto.md](references/texto.md).

A regra que vale em qualquer plataforma: **um card = uma ideia**, e o corpo cabe em 25 palavras. Se não coube, são dois cards.

## Etapa 4 — Anti-slop

**Obrigatório, antes de mostrar qualquer texto ao usuário** — capa, corpo, CTA, legenda e alt text. Está embutida em [references/anti-slop.md](references/anti-slop.md), com os arquivos em `references/anti-slop/`. Não precisa instalar nada.

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
2. `assets/baixar-fontes.sh <estilo>` gera o `fonts.css` com as faces embutidas
3. `assets/exportar.sh` captura os PNGs em 1080×1350 e monta o PDF
4. **Abra cada PNG e olhe.** Captura falha em silêncio: sai arquivo do tamanho certo, em branco
5. Passe a checagem antipadrão abaixo

**Apresente o resultado ao usuário, não o caminho da pasta.** Uma folha de contato em artefato, ou as imagens direto na mensagem. Mandar alguém abrir um diretório para ver o próprio trabalho é a pior parte de uma entrega boa.

### Formatos

| Destino | Arquivo | Observação |
|---|---|---|
| Instagram | PNG 1080×1350 (4:5) | um por card |
| LinkedIn | PDF sequencial, mesmas páginas | documento nativo, até 300 páginas e 100 MB |
| Stories | PNG 1080×1920 | só se pedirem |

O PDF do LinkedIn usa os mesmos PNGs. O feed de lá é mais largo e reduz o documento: o piso geral de corpo é **30px** sobre 1080, e **34px** quando o LinkedIn é o destino principal.

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
- [ ] Nenhum texto corrido sobre grafismo
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
