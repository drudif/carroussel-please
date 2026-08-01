# A passada anti-slop

**Está embutida.** Não precisa instalar nada, não precisa clonar repositório, não depende de outra skill estar presente. Os arquivos vivem em `references/anti-slop/`.

Isso é deliberado: a etapa 5 é obrigatória, e etapa obrigatória não pode depender de uma dependência externa que pode não estar lá.

## Como rodar

Antes de mostrar **qualquer** texto ao usuário — capa, corpo, CTA, legenda, alt text — leia e aplique, nesta ordem:

1. **[anti-slop/REGRAS.md](anti-slop/REGRAS.md)** — os dois princípios, a regra inegociável de claims, a pontuação
2. **[anti-slop/slots.md](anti-slop/slots.md)** — a auditoria de slots. Carrossel é peça diagramada: a unidade do slop é o slot, não a frase
3. **[anti-slop/estruturas.md](anti-slop/estruturas.md)** — contraste binário, fôrmas de gênero, ritmo
4. **[anti-slop/frases.md](anti-slop/frases.md)** — as famílias léxicas, flexionáveis
5. **[anti-slop/exemplos.md](anti-slop/exemplos.md)** — transformações de referência, quando estiver em dúvida

## Os dois princípios

**Densidade é o tell, não a instância.** Um "além disso" é humano; um por parágrafo é máquina. Procure famílias flexionáveis, não strings — o slop migra, "Em resumo" vira "Resumindo:".

**Em peça diagramada, a unidade do slop é o slot.** Eyebrow, rótulo, número, rodapé: o template cria a caixa e o texto nasce para preencher. Audite se o slot deveria existir antes de reescrever o que está dentro dele. Isso conecta direto com o padrão de composição da skill — slot que não carrega informação sai, e o vazio que sobra vira respiro.

## O que mais aparece em carrossel

| Padrão | Correção |
|---|---|
| Contraste binário na capa — "não é X, é Y", "mais do que X" | Afirme Y direto. O tell é a reversão, não o "não" |
| Número de performance sem fonte — "em 30 segundos", "3x mais rápido" | Corte, ou substitua por algo verificável |
| Comparação de preço inventada — "sem mensalidade" | Só entra se for fato do briefing |
| Falsa intimidade — "Aquele PDF que você..." | Tire o "aquele". O fato sobrevive sem a piscadela |
| **Substantivo sem artigo** — "com data errada", "é literalmente sistema" | "com **a** data errada", "é **um** sistema". Sintaxe do inglês em frase de português; ver [anti-slop/estruturas.md](anti-slop/estruturas.md#substantivo-pelado-o-artigo-que-o-inglês-não-põe-e-o-português-põe) para as exceções, que são reais |
| Enquadramento de produtividade — "sobra tempo pra" | Diga o que a ferramenta faz, não o tempo que economiza |
| CTA em pergunta — "Quer fazer as suas?" | Vira afirmação |
| Eyebrow que só existe porque o template tem a caixa | Mata o slot inteiro |
| Todos os cards com a mesma estrutura e comprimento | Assimetria deliberada em pelo menos um |

## O grafismo não gera texto

Este é o mesmo defeito de slot, aplicado ao desenho — e é o mais fácil de cometer, porque parece trabalho de design.

Você desenha um diagrama e ele fica com uma área vazia. Você escreve um rótulo para preencher. Você desenha um botão e escreve "baixar" dentro. Você desenha quatro camadas e escreve "4 CAMADAS" na lateral. **Nenhuma dessas palavras veio da etapa 4.** Elas nasceram da necessidade gráfica, e é exatamente isso que a régua derruba.

**A regra:** o grafismo só pode conter texto que (a) foi aprovado na etapa 4, ou (b) é dado duro e verdadeiro do produto — um número de versão, uma dimensão, um nome de etapa que existe de fato.

Tudo o mais o desenho comunica **por forma**: posição, tamanho, repetição, corte, seta, contraste. Se o desenho só se entende com legenda, o desenho está errado — troque o desenho, não acrescente a legenda.

Sintomas, todos vistos em produção:

| No grafismo apareceu | Por que é slop |
|---|---|
| Rótulo nomeando o que a forma já mostra | O desenho não estava se explicando; a palavra virou muleta |
| Botão desenhado com "baixar", "escolher", "ver mais" | Interface fictícia produzindo copy fictícia |
| Contagem descritiva — "4 camadas", "6 etapas", "3 cortes" | O leitor conta sozinho. O número existe para preencher |
| Rodapé com o resumo do que a skill faz | É a legenda do post migrando para dentro da arte |
| Termo técnico que o público não tem — "área segura", "1080×1350" | Vocabulário de quem produz, não de quem lê |

**A checagem:** cubra o texto do grafismo com a mão. Se o desenho continua dizendo a mesma coisa, o texto era enfeite — tire. Se o desenho fica mudo, ele não era um desenho, era um diagrama precisando de manual.

## A regra inegociável

**Número não se inventa.** Toda métrica, estatística, prêmio ou depoimento que não veio do briefing entra como `[CONFIRMAR: o quê]`, nunca como número plausível. Em publicidade isso é risco jurídico, não só de qualidade.

Hipérbole retórica sobre o leitor — "as 400 abas que você jurou que ia ler" — não cai nessa regra: não é métrica do produto e ninguém lê como dado. Mas diga isso ao usuário em vez de decidir sozinho; a fronteira é fina.

## O registro dos cortes

Grave o registro **no arquivo**, não na resposta. Ele serve para consulta e para você não repetir o corte.

**Não apresente a lista ao usuário.** No momento em que ele precisa julgar o texto, a memória de cálculo atrapalha. A única exceção é um corte que atropelou o que parecia escolha deliberada de voz — esse você aponta, em uma linha, para ele decidir.

## Os limites

**Guia de voz da marca vence qualquer regra daqui.** Fórmula deliberada da marca fica — documente a exceção em vez de aplicar a regra por cima.

**Cuidado com o slop ao contrário.** Texto que obedece tudo ao pé da letra fica picotado e robótico. A fôrma existe porque funciona; o tell é a execução completa e na ordem canônica, não o uso de um elemento dela.

**Nunca altere fato, número, nome ou compromisso real** ao deslopar.

**Se você passou o texto e não cortou nada, você não aplicou.** Volte e aplique.

---

## Procedência

O conteúdo de `references/anti-slop/` é a skill **sprayantislop** ([github.com/drudif/sprayantislop](https://github.com/drudif/sprayantislop)), de Fernando Drudi, embutida aqui na íntegra.

A camada léxico-estrutural dela é, por sua vez, derivada de **Zero-Lero**, de Vinicius Stanula, sob licença MIT. O aviso de copyright está preservado em [anti-slop/LICENSE-zero-lero](anti-slop/LICENSE-zero-lero), como a licença exige.

Se a `sprayantislop` estiver instalada como skill independente e for mais nova que esta cópia, use a instalada — ela é a fonte.
