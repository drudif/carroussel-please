---
name: deslopar
description: Use ao escrever, editar ou revisar texto de marketing/publicidade ou apresentações em pt-BR — landing pages, posts, e-mails, press releases, decks de venda/pitch, campanhas. Também quando o usuário pedir para "deslopar", "tirar cara de IA", "matar o lero" ou reclamar que um texto/deck soa genérico, inflado ou "de ChatGPT".
metadata:
  language: pt-BR
  base: Camada léxico-estrutural vendorizada de Zero-Lero (MIT, Vinicius Stanula) + módulos próprios de decks, claims e briefing.
---

# Deslopar

Elimine slop de IA em texto e apresentações de marketing em pt-BR.

Dois princípios regem tudo:

1. **Densidade é o tell, não a instância.** Um "além disso" é humano; um por parágrafo é máquina. Busque **famílias flexionáveis, não strings** — o slop migra ("Em resumo" vira "Resumindo:"). Flagre por acúmulo.
2. **Em apresentação, a unidade do slop é o slot, não a frase.** Eyebrow, subtítulo, card, stat tile: o template cria a caixa e o texto nasce para preenchê-la. Audite o slot antes de tocar no texto — reescrever texto de slot que não deveria existir é tratar sintoma.

## Fluxo de trabalho

**Passo 0 — Entrevista de briefing (antes de gerar qualquer coisa).** Se o usuário está presente e o briefing não responde objetivo, público, ativos reais e o que só essa marca pode dizer: **pergunte antes de escrever** (máximo 5 perguntas, numa rodada só, **cada uma com a opção explícita de pular**) → [briefing.md](briefing.md). Especificidade nasce do insumo, não da revisão. Pergunta pulada ou usuário ausente: siga com placeholders — a entrevista melhora o teto, mas sua ausência não suspende nenhuma regra.

**Deck/apresentação** — nesta ordem, sem pular:
1. **Auditoria de slots** → [slots.md](slots.md)
2. **Teste do fio** (títulos em sequência contam o argumento?) → decks.md
3. **Claims** no que sobrou (regra inegociável abaixo)
4. **Camada léxico-estrutural** no texto restante → [frases.md](frases.md) e [estruturas.md](estruturas.md)

**Texto corrido (landing, post, e-mail, release):**
1. **Claims** primeiro (dado inventado é o defeito mais grave — regra inegociável abaixo)
2. **Estruturas** (contraste binário, fôrmas de gênero, ritmo) → estruturas.md
3. **Léxico** (famílias de frases) → frases.md
4. Transformações de referência em [exemplos.md](exemplos.md)

## A regra inegociável: números não se inventam

O defeito nº 1 da geração de copy por IA não é estilo — é **dado fabricado com cara de fato**: "85 mil clientes", "NPS de 72", depoimento com nome e cidade. Em publicidade isso é risco jurídico (CONAR/CDC), não só de qualidade.

- Ao **gerar**: toda métrica, estatística, prêmio ou depoimento que não veio do briefing entra como placeholder explícito — `[CONFIRMAR: nº de usuários]` — nunca como número plausível. Depoimento não fornecido = slot marcado como pendente, jamais fabricado.
- Ao **revisar**: todo número sem fonte no briefing vira pergunta ao cliente. Todo superlativo verificável ("o melhor", "o único", "nº 1") exige comprovação ou corte.
- Depoimento com a fôrma `aspas + nome abreviado + profissão + cidade`, granularidade idêntica em todos: assinatura de fabricação. Depoimento só entra se existir (fornecido e autorizado); se o layout pede prova social e não há, o slot fica marcado como pendente. Depoimento real se reconhece pela assimetria: comprimentos diferentes, um detalhe que só o cliente real diria.
- Superlativo verificável ("o melhor", "o único", "nº 1", "líder") exige comprovação documentável; urgência/escassez ("últimas unidades", "só hoje") só com restrição real, número e data.

## Verificações rápidas (antes de entregar)

- Algum número, métrica ou depoimento que não veio do briefing? Placeholder ou corte.
- Entrega com 5+ `[CONFIRMAR]` e o usuário estava disponível sem nenhuma pergunta feita? Volte ao Passo 0 e entreviste.
- A headline serviria para o concorrente? Se sim, não é headline — ancore em algo que só esta marca pode dizer.
- Contraste binário em qualquer versão ("Não é X, é Y" / "é mais do que X" / "vai muito além de")? Afirme Y, corte a rampa. O tell é a reversão, não o "não".
- Frase terminando em vírgula + gerúndio de benefício ("...otimizando seu tempo")? Corte ou concretize.
- "Simples assim.", "sem burocracia", "Chega de X. Chega de Y."? Demonstre em vez de declarar.
- Família "ressaltar/destacar", moldura temporal de abertura, conclusão rotulada? Corte e afirme direto.
- Eyebrow que reformula o título, subtítulo que reformula os dois? Mate o eco — cada nível carrega informação de natureza diferente ou morre.
- Todos os slides com os mesmos slots preenchidos, subtítulos do mesmo comprimento, grids de 3 sempre? Assimetria deliberada.
- Quiasmo/espelhamento formulaico ("Você cuida do X, a gente cuida do Y")? Um por peça, no máximo.
- Vazamento pt-pt ("utilizador", "registar", "equipa")? Traduza para pt-BR.
- Leia em voz alta: soa como locutor de comercial ou coach de LinkedIn? Ainda tem slop.

## Pontuação

Avalie 1–10 por dimensão; abaixo de 42/60, revise e repasse:

| Dimensão | Pergunta |
|---|---|
| Objetividade | Afirmações diretas ou anúncios e molduras? |
| Ritmo | Variado ou metronômico? |
| Confiança no leitor | Respeita quem lê ou conduz pela mão e mendiga engajamento? |
| Autenticidade | Soa como esta marca falando, ou como "conteúdo"? |
| Distintividade | O concorrente poderia assinar? |
| Integridade de claims | Todo dado tem fonte ou placeholder? |

## Exceções e limites

- **Guia de voz da marca vence qualquer regra daqui.** Fórmula deliberada de marca fica; documente a exceção.
- **Nunca altere fato, número, nome ou compromisso real** ao deslopar.
- **Cuidado com o slop ao contrário:** texto que obedece tudo ao pé da letra fica picotado e robótico. A fôrma de gênero (landing, thread) existe porque funciona — o tell é a execução completa e na ordem canônica, não o uso de elementos dela. Quebre a ordem, pule etapas, deixe assimetria.
- Travessão é legítimo em pt-BR; o tell é o travessão duplo estilo inglês cravado em frase comercial, em densidade.
