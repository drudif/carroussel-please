# Decks e apresentações: o slop mora no slot

O template cria a caixa (eyebrow, subtítulo, card, stat tile) e o gerador preenche a caixa porque ela existe — não porque há algo a dizer. Texto sob demanda de layout é genérico por construção. Portanto: **audite o layout antes do texto.**

## Passo 1 — Auditoria de slots

### Teste de existência
Para cada elemento de texto do slide: *se eu apagar, o slide perde informação?* Se não perde, o elemento morre. Não se reescreve texto de slot que não deveria existir.

### Regra do eco vertical
Eyebrow, título e subtítulo só coexistem se cada um carrega informação de **natureza diferente** — navegação/contexto ≠ afirmação ≠ evidência ou consequência. Se dois se reformulam, mate um.

| Eyebrow | Veredito |
|---|---|
| "Fase 2 — Lançamento", "Concorrência", "Q3 2026" | Legítimo: navegação que o título não pode carregar |
| "INOVAÇÃO" acima de "Uma abordagem inovadora" | Eco — corte |
| "O KAVIO" acima de "O sistema operacional financeiro do MEI" | Eco de categoria — o título já diz de quem se fala |
| "VAMOS CONSTRUIR", "NOSSA VISÃO" | Enchimento de slot — corte |

É o padrão bold lead-in (`**Rótulo:** frase que reformula o rótulo`, ver estruturas.md) em versão vertical.

### Simetria fabricada = conteúdo fabricado
Grid de 3 cards iguais força o gerador a inventar o terceiro benefício e esticar o card curto. **O conteúdo dita o grid, nunca o contrário**: 2 itens, 4 desiguais, um card maior. Todos os slides com os mesmos slots preenchidos e subtítulos do mesmo comprimento = metrônomo visual; deixe slides sem subtítulo, sem eyebrow, com um número só.

### Stat tile sem número real vira prosa ou morre
O tile "+300%" é o slot mais perigoso: demanda dado, e dado sob demanda de layout é dado inventado. Todo tile passa pela regra inegociável de claims (SKILL.md). Sem número do briefing → `[CONFIRMAR]` visível ou o tile sai do layout.

## Passo 2 — Teste do fio

**Leitura só de títulos:** leia os títulos dos slides em sequência, sem o resto. Eles sozinhos contam o argumento? Título é **afirmação** ("TikTok Shop cresce 3× mais rápido no Nordeste"), não categoria ("Análise de mercado"). Título-categoria é o que *cria* a demanda por subtítulo; quando o título afirma, a maioria dos subtítulos morre sozinha.

**Teste da transcrição:** cole todo o texto do deck como prosa corrida e rode frases.md + estruturas.md em cima. Sem a diagramação para disfarçar, os ecos e gerúndios pós-vírgula ficam nus. Deck slopado e post de LinkedIn fragmentado são o mesmo fenômeno: profundidade fabricada por diagramação.

## Geração: argumento primeiro, layout depois

Escreva o fio como uma linha por slide — essas linhas viram os títulos-afirmação. Só então cada slide escolhe o layout que a evidência daquele ponto pede. **Slot é opt-in por necessidade do conteúdo, nunca herdado do template.** É a inversão exata do fluxo que produz slop.

## Clichês de pitch (famílias)

- "O [sistema operacional / Uber / Netflix / Nubank] de X"
- "democratizar o acesso a X"
- "na intersecção de X e Y"
- "não somos apenas um app, somos um ecossistema/plataforma/movimento"
- "ganha-ganha", "destravar valor", "alavancas de crescimento"
- "o mercado endereçável de R$ X bi" sem fonte
- Slide de missão com "nasceu para transformar"

**Correção:** o que a empresa faz, para quem, com que resultado medido.

## Antes/depois (do corpus de baseline desta skill)

**Antes** — slide de produto, slots completos:

> *Eyebrow:* O KAVIO
> *Título:* O sistema operacional financeiro do microempreendedor
> *Subtítulo:* Gestão de fluxo de caixa, DAS, emissão de nota e separação PJ/PF em um app que o MEI abre todos os dias.

**Depois:**

> *Título:* O app que o MEI abre todos os dias: caixa, DAS, nota e separação PJ/PF
> *(sem eyebrow — o fio já situa; sem subtítulo — o título absorveu a única informação real, e "sistema operacional de X" era clichê de pitch)*

**Antes** — slide de tração com dados fabricados:

> *Título:* 85 mil MEIs ativos, crescendo 18% ao mês
> *Subtítulo:* Retenção acima de 70% em 6 meses e NPS de 72: um canal de distribuição engajado, não apenas uma base de downloads.

**Depois:**

> *Título:* `[CONFIRMAR: MAU]` MEIs ativos, `[CONFIRMAR: crescimento m/m]`
> *Subtítulo:* Retenção `[CONFIRMAR]` em 6 meses. *(contraste "não apenas uma base de downloads" cortado — afirmação direta; nenhum número entra sem briefing)*
