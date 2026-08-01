<!-- Vendorizado de Zero-Lero (https://github.com/ViniciusStanula/Zero-Lero), MIT License, © Vinicius Stanula. -->

# Estruturas a Evitar

Padrões que não se acham com Ctrl+F: exigem leitura. Exemplos citados vêm dos corpora v1 e v2 que fundamentam esta skill (ver README.md e CHANGELOG.md). Regra de ouro em tudo: flagre densidade e repetição, não a instância isolada.

## Contraste binário

Cria drama falso por negação telegrafada. O padrão mais transferível do slop em qualquer língua; em pt-BR tem quatro realizações principais.

| Padrão | Problema |
|---|---|
| "Não se trata de X. Trata-se de Y." | Reversão telegrafada |
| "Não é (apenas) X. É Y." | Pivô previsível |
| "deixou de ser X e se tornou Y" | Arco de transformação em fôrma ("deixou de ser um diferencial e se tornou uma necessidade" apareceu em 3 textos do corpus com a mesma estrutura) |
| "não apenas X, mas também Y" | Hedge aditivo |
| "X não é tudo. Y é tudo." | Mesma fórmula, roupa de aforismo |
| "A pergunta não é SE. É QUANDO." | Falsa profundidade com maiúsculas |
| "é mais do que um X. É Y." / "vai muito além de X" | **Versão positiva (v2):** mesma reversão telegrafada, sem negação — escapa de quem busca só o "não". O tell é a reversão, não a negação. |

**Correção:** afirme Y. "O home office não é apenas uma mudança de local. É uma mudança de mentalidade." → "O home office muda a mentalidade, não só o endereço." Ou simplesmente: afirme a mudança de mentalidade e pronto.

## Lista negativa

Enumerar o que a coisa não é antes de revelar o que é. Striptease retórico.

> "Ele batia todas as metas. Entregava antes do prazo. Tecnicamente, era impecável. Mas tinha um problema."

**Correção:** comece pelo problema. O leitor não precisa da pista de decolagem.

## Fragmentação dramática (assinatura do LinkedIn brasileiro)

Frases de 1-3 palavras empilhadas, uma por linha, com linha em branco entre cada. Profundidade fabricada por diagramação.

| Padrão | Problema |
|---|---|
| "Ignoram. Resistem. Torcem para que passe." | Staccato em tríade |
| "Mas tinha um problema." (parágrafo de uma linha) | Cliffhanger de feed |
| "Simples assim? Sim. Fácil? Não." | Pergunta-resposta em ping-pong |
| "Foi um divisor de águas." (linha isolada) | Revelação artificial |
| Tríades espelhadas ("De um lado... Do outro...") | Simetria de fôrma |
| "Todo. Santo. Dia." / "Uma coisa de cada vez. Sempre." | **Pontuação dramática palavra-a-palavra (v2):** fragmentação dentro da frase, ponto final como soco |

**Correção:** frases completas, parágrafos de verdade. Se a ideia só impressiona picotada, a ideia é fraca.

## Pergunta retórica como setup

58 linhas com "?" no corpus de 24 textos. Três usos viciados:

| Padrão | Problema |
|---|---|
| "Você já parou para pensar...?" (abertura) | Condescendência de partida |
| "E se eu te dissesse que...?" | Suspense de infomercial |
| "O melhor de tudo? Ele acompanha um estojo..." | Pergunta-autorespondida comercial |
| "Quer saber como? Continue lendo." | Pedágio de atenção |
| Heading em pergunta ("Por que investir em X?") em série | FAQ disfarçado de artigo |
| Pergunta de engajamento no fecho ("Concorda? Comenta aí. 👇") | Mendicância de algoritmo |
| "Mas será que [a coisa] entrega tudo isso mesmo?" (v2) | Gancho de resenha/blog: dúvida fabricada que o texto responderá com "sim" |

**Correção:** afirme. Perguntas sobrevivem quando o texto de fato as investiga em vez de respondê-las na linha seguinte.

## Falsa agência

Coisa inanimada fazendo verbo humano. A IA adora porque evita nomear o ator.

| Padrão | Problema |
|---|---|
| "Os dados nos mostram o caminho" | Dados não mostram nada; alguém os lê e conclui |
| "O mercado exige autenticidade" | Mercado não exige; clientes compram de quem preferem |
| "A cultura organizacional sofre" | Pessoas sofrem; a cultura é o efeito |
| "O sentimento de pertencimento se enfraquece" | Quem deixou de se sentir parte? |
| "A tecnologia deve ser uma aliada" | Aliada de quem, para fazer o quê? |
| "A automação elimina a tentação" | Você deixa de ver o dinheiro parado |

**Correção:** nomeie quem age. Sem ator específico, use "você".

## Gerúndio pós-vírgula (o ", ensuring convenience" brasileiro)

O padrão estrutural mais denso do slop comercial em pt-BR: fato + vírgula + gerúndio de interpretação vazia. Praticamente todo bullet de produto do corpus termina assim.

> "...até 40 horas de reprodução, **proporcionando liberdade total para o seu dia a dia**."
> "...conexão rápida e sem falhas, **elevando sua experiência a outro patamar**."
> "...8 programas pré-definidos, **otimizando o seu tempo na cozinha**."

**Correção:** corte a cláusula (o fato se sustenta) ou substitua pela consequência concreta: "...até 40 horas de reprodução — uma semana de trajetos sem recarregar."

## Gerundismo

Futuro perifrástico de telemarketing. Concentrado em email comercial (100% dos emails do corpus).

| Padrão | Correção |
|---|---|
| "Estaremos enviando" | "Enviaremos" / "Vamos enviar" |
| "Estaremos disponibilizando" | "Vamos disponibilizar" |
| "Vamos estar oferecendo" | "Vamos oferecer" |

## Substantivo pelado (o artigo que o inglês não põe e o português põe)

O inglês diz *with wrong date*, *the subject is system*. O português diz **com a data errada**,
**o assunto é um sistema**. Texto gerado por modelo herda a sintaxe do original e vai soltando
substantivo sem artigo: cada frase soa quase certa, e o acúmulo soa traduzido.

| escrito | como se fala |
|---|---|
| "carrossel de cronologia com data errada é o pior tipo de erro" | "...com **a** data errada..." |
| "o assunto é literalmente sistema" | "o assunto é literalmente **um** sistema" |
| "cliente não lê briefing" | "**o** cliente não lê **o** briefing" |
| "a skill roda entrevista antes de escrever" | "roda **uma** entrevista" |

**Onde o artigo NÃO entra** — e aqui a régua estraga o texto se for aplicada no automático:

- plural genérico: *carrosséis não vendem sozinhos*
- abstrato como objeto direto: *isso exige método*, *faltou tempo*, *o post tem gancho*
- expressão fixa: *em casa*, *por e-mail*, *de cabeça*, *com pressa*
- **título, rótulo e paginação**, onde o telegráfico é a forma. A régua vale para corpo e legenda

**Como flagrar:** leia em voz alta. Se você poria o artigo falando, ele falta. E vale o princípio
da densidade: um substantivo pelado passa, três no mesmo bloco denunciam a origem.

## Esqueleto retórico exposto

O texto anuncia a própria estrutura em vez de fluir.

| Padrão | Problema |
|---|---|
| "Em primeiro lugar... Em seguida... Por fim..." | Sumário ambulante |
| "Neste artigo, vamos explorar..." | Meta-comentário de abertura |
| Heading "## Conclusão" + parágrafo "Em resumo," | Fim rotulado duas vezes (8 headings "Conclusão" + 11 fechos "Em resumo/Em suma" no corpus) |
| "Antes de apresentarmos a lista, é importante destacar..." | Pedágio antes do conteúdo prometido |

**Correção:** corte os anúncios. Se a estrutura é boa, o leitor a percorre sem mapa.

## Aberturas imperativas comerciais

E-commerce do corpus abre 5 de 5 assim:

> "Imagine acordar todos os dias com o aroma de um espresso perfeito..."
> "Descubra um novo nível de qualidade sonora..."
> "Transforme a sua cozinha com..."

**Correção:** comece pelo produto e pelo fato mais forte. "Moedor integrado: café moído na hora" informa mais que "Imagine...".

## Passiva de design

Particípio + advérbio de capricho, escondendo o sujeito.

| Padrão | Problema |
|---|---|
| "foi cuidadosamente pensado para" | Quem pensou? "Cuidadosamente" informa o quê? |
| "desenvolvido com tecnologia de ponta" | Qual tecnologia? |
| "Cada detalhe foi projetado para garantir..." | Bula universal de produto |

**Correção:** nomeie o atributo concreto que o "cuidado" produziu.

## Correlações de abrangência universal

Embalagem de "serve para todos", que não exclui ninguém e por isso não informa nada.

| Padrão | Exemplo do corpus |
|---|---|
| "seja X, seja Y, seja Z" | "seja durante o treino, no trabalho ou relaxando em casa" |
| "tanto para X quanto para Y" | "tanto para empresas quanto para colaboradores" |
| "para todos os perfis" | "atrativos para todos os perfis de viajantes" |

**Correção:** escolha o público real e fale com ele.

## Bullets com bold lead-in (50 instâncias no corpus)

`- **Rótulo:** frase que reformula o rótulo.` — em grupos de 3 a 5, com os dois pontos sempre no mesmo lugar.

> "- **Conteúdo relevante:** produzir materiais que realmente agreguem valor..."

**Correção:** ou o rótulo carrega a informação (lista enxuta), ou a frase carrega (prosa). Os dois juntos é eco. E nem tudo precisa ser bullet: série de ideias conectadas é parágrafo.

## Padrões de ritmo

| Padrão | Correção |
|---|---|
| Parágrafos de comprimento idêntico do início ao fim | Varie: um parágrafo longo, um de uma frase |
| Toda seção fechando em frase de efeito ("A primeira impressão é a que fica.") | Deixe seções terminarem em fato |
| Staccato uniforme (LinkedIn): só frases curtas, uma por linha | Monotonia invertida ainda é monotonia; junte ideias em parágrafos |
| Legato uniforme (institucional): só frases longas subordinadas | Quebre com uma curta |
| Pergunta respondida na linha seguinte, sempre | Corte a pergunta ou deixe-a trabalhar |
| Tríades em série (3 pilares, 3 benefícios, 3 passos) | Teste 2, ou 4 desiguais |
| Fecho motivacional obrigatório ("Comece hoje mesmo!") | 20 dos 24 textos do corpus terminam em exortação; nenhum termina num fato. Termine num fato. |

## Anáforas triplas (v2 — 6/4)

Tríade retórica com palavra-âncora repetida. A skill já cobria tríades de itens; a anáfora é a versão musculosa.

| Padrão | Exemplo do corpus |
|---|---|
| "Sem X, sem Y, sem Z." | "Sem reserva, sem estudo, sem noção." / "Sem perguntas, sem burocracia." |
| "Chega de X. Chega de Y. Chega de Z." | "Chega de travar na hora de falar. Chega de entender a letra... Chega de adiar o seu sonho." |
| "Nada de X. Nada de Y." | variante da mesma fôrma |

**Correção:** uma frase afirmativa que diga o que sobra quando se tira X, Y e Z.

## Autenticidade fabricada (v2 — assinatura da condição "tom humano")

Quando o prompt pede pra não parecer IA, o slop não some: troca de pele. O modelo fabrica os *metadados* da espontaneidade enquanto a estrutura por baixo segue perfeita (intro + 3 pontos + moral). Texto humano de verdade é estruturalmente mais bagunçado.

| Padrão | Problema |
|---|---|
| "Vou ser sincero:" / "Vou abrir o jogo:" como abertura | Franqueza anunciada (ver frases.md) |
| "kkk" / "rs" posicionado no fim de frases estratégicas | Imperfeição calculada |
| "né?" distribuído em intervalos regulares | Oralidade de fôrma |
| "EDIT: não esperava tanta resposta" em texto recém-criado | Histórico falso |
| "P.S.: eu leio todas as respostas, de verdade" | Sinceridade com selo de garantia ("de verdade" é o tell) |
| Estrutura de redação intacta sob verniz casual | Gíria na superfície, esqueleto de dissertação por baixo |

**Correção:** desorganize de verdade ou assuma o registro escrito. Detectar: ignore o tom e olhe só a arquitetura — se cada parágrafo cumpre função de manual, é fôrma.

## Slop dentro de aspas (v2 — press releases 3/3)

Citações fabricadas de executivos carregando os padrões da casa: contraste binário, inflação, missão grandiosa.

> "Esse aporte **não é apenas** um investimento na PagueJá. **É um investimento no** potencial empreendedor do Nordeste brasileiro."

O slop se esconde no discurso direto, onde o leitor (e o revisor) baixa a guarda — aspas parecem fala de pessoa real.

**Correção:** aplique as mesmas regras dentro das aspas. Citação real soa como fala; se a citação tem estrutura de slogan, é redação fantasma.

## Fôrmas de gênero (v2)

O gênero inteiro executado em fôrma canônica, sempre na mesma ordem:

| Gênero | Fôrma-tell |
|---|---|
| Resenha | Título com pergunta → "Vamos direto ao ponto" → seções fixas → "Veredito"/"Vale a pena?" → "Nota: X/10" |
| Thread | "Abre o fio 👇" → numeração n/total → recapitulação com ✅ → "Salva 🔖 / RT" — fecho em três atos idêntico em toda thread |
| YouTube | Gancho → "já deixa o like e se inscreve" → conteúdo em N causas/passos → "comenta aqui embaixo" → "ativa o sininho" |
| Landing | Dores em ❌ → "A verdade que não te contam" → método em 3 módulos → depoimentos ⭐⭐⭐⭐⭐ → oferta riscada → garantia → urgência |
| Depoimentos fabricados | Bloco ⭐⭐⭐⭐⭐ + aspas + nome abreviado + profissão ("— Camila R., analista de marketing") — granularidade idêntica em todos |

**Correção:** a fôrma existe porque funciona, mas a execução completa e na ordem canônica é assinatura de máquina. Quebre a ordem, pule etapas, deixe assimetria.

## Tells de formatação

- Emoji como marcador de seção ou bullet (✅ → 👇 ♻️ 🚀) fora de contexto que o peça
- Headings triádicos perfeitamente paralelos
- Todas as seções com o mesmo comprimento
- Title Case Em Headings (anglicismo: pt-BR usa caixa baixa após a primeira palavra)
- Negrito espalhado em nomes de produto no meio da prosa
- Seções-boilerplate que ninguém pediu: "Conclusão", "Considerações finais", "Principais aprendizados"

## Tells de auditoria (conteúdo já publicado)

- **Artefatos de chat** (ver frases.md): qualquer fragmento de conversa com IA é decisivo.
- **Integridade de citações:** link que dá 404 sem captura em archive.org, DOI que não resolve, fonte que não diz o que o texto afirma. O indicador isolado mais forte de IA publicada sem revisão.
