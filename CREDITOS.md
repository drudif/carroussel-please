# Procedência

A `carroussel-please` é **autossuficiente**: nada dentro dela depende de outra skill estar instalada. Isso é decisão de arquitetura, não conveniência — a promessa é `git clone` e funciona, e uma chamada em tempo de execução para uma skill ausente falha em silêncio na máquina de quem instalou.

Quatro skills foram incorporadas, em **três densidades diferentes**. A densidade foi escolhida pelo que sobrevive à tradução para o meio — uma peça estática de 1080×1350 — e pelo que pode ser redistribuído.

---

## Densidade 1 — íntegra, verbatim

### sprayantislop

**Onde:** `references/anti-slop/` — `REGRAS.md`, `slots.md`, `estruturas.md`, `frases.md`, `exemplos.md`, `briefing.md`
**Autoria:** Fernando Drudi — [github.com/drudif/sprayantislop](https://github.com/drudif/sprayantislop)
**Por que íntegra:** a etapa 5 é obrigatória, e etapa obrigatória não pode depender de uma dependência externa que pode não estar lá. É a única das quatro cuja aplicação parcial não funciona — a régua opera por densidade, e uma versão resumida derruba as instâncias óbvias e deixa passar o padrão.

A camada léxico-estrutural da sprayantislop deriva de **Zero-Lero**, de Vinicius Stanula, sob licença MIT. O aviso de copyright está preservado em [references/anti-slop/LICENSE-zero-lero](references/anti-slop/LICENSE-zero-lero), como a licença exige.

> Se a `sprayantislop` estiver instalada como skill independente e for mais nova que esta cópia, use a instalada — ela é a fonte.

---

## Densidade 2 — compactadas

O que foi extraído são as regras operacionais. O que ficou de fora está listado, para não parecer omissão.

### carousel-writer-sms

**Onde:** [references/texto.md](references/texto.md), seções "A estrutura, em quatro zonas", "Regras de escrita" e "Por plataforma"
**O que entrou:** a tabela de formato por plataforma — quantidade de cards, proporção, densidade de texto, papel da legenda, sinal de engajamento que importa em cada uma — e a estrutura capa/contexto/corpo/fecho, com a regra de 25 palavras por card.
**O que ficou de fora:** os cinco formatos de carrossel (listicle, framework, antes/depois, dados, estudo de caso), os exemplos de saída e a seção de limites. São genéricos e já estão cobertos pelas perguntas da etapa 4.

### brainstorming

**Onde:** [references/texto.md](references/texto.md), seção "O protocolo de conversa"
**O que entrou:** uma pergunta por mensagem, múltipla escolha quando couber, trava de aprovação a cada bloco, nada de produção antes da aprovação, pergunta pulada vira `[CONFIRMAR]`.
**O que ficou de fora:** o documento de spec, a passagem para `writing-plans`, o companion visual em navegador. Um carrossel não tem arquitetura para documentar — a spec dele são o `DIRECAO.md` e o `TEXTOS.md`.

---

## Densidade 3 — destiladas

As duas skills visuais foram escritas para **interface viva**. A maior parte do que elas ensinam é sobre comportamento — hover, easing, revelação por scroll, colapso responsivo —, e nada disso existe num PNG. Copiar verbatim importaria conselho ativamente errado para o meio, além de inflar o contexto com o que nunca vai ser usado.

O destilado está em [references/visual.md](references/visual.md), que documenta **o que transferiu e o que não transferiu, com o motivo de cada rejeição**.

### bencium-innovative-ux-designer

**O que transferiu:** a lista de antipadrões de IA (fontes, cores, efeitos, composições), a regra de se comprometer inteiramente com uma direção estética, a preferência por atmosfera de material sobre campo de cor chapada, e "todo elemento justifica a existência".

### high-end-visual-design

**O que transferiu:** macro-respiro, disciplina de escala tipográfica, e o **variance engine** — que virou os três arquétipos de layout (editorial split, cascata Z, bento assimétrico) usados tanto nas referências geradas quanto como regra de ritmo entre cards.

**Dois conflitos reais, resolvidos:**

| Conflito | Resolução |
|---|---|
| A `high-end-visual-design` recomenda o arquétipo "Ethereal Glass" — vidro fosco com `backdrop-blur` pesado. A `bencium` proíbe glassmorphism | **A proibição vence.** É o antipadrão que esta skill existe para evitar |
| A `high-end-visual-design` manda preceder todo título com uma pílula de eyebrow | **O anti-slop vence.** É exatamente o slot que nasce do template e é preenchido por necessidade |

---

## Por que não copiar tudo verbatim

Além da tradução de meio, dois motivos:

**Contexto.** As quatro somam cerca de 15 mil palavras. Íntegras, elas dominariam o contexto de toda execução da skill, e a maior parte nunca seria usada.

**Procedência.** A `sprayantislop` é do autor desta skill e o Zero-Lero é MIT com aviso preservado — redistribuir é legítimo e está feito. As outras três são de terceiros, e redistribuir texto integral de terceiros num repositório público é problema de licença, não de estilo. Um destilado escrito em palavras próprias, com crédito, resolve as duas coisas.

---

## As referências visuais

As vinte e uma imagens de `assets/referencias/` foram geradas com **Nano Banana Pro** (Google), via conector do Higgsfield, em 4:5 e 2K, a 2 créditos cada. Os prompts combinam: o briefing de sistema `posts inspired in editorial graphic posters`, a especificação de paleta e material de cada estilo, os três arquétipos de layout da `high-end-visual-design`, e a lista de antipadrões da `bencium` aplicada como negativa.

## As fontes

As treze famílias dos sete estilos — **quinze faces, 1,8 MB** — estão **embutidas** em
`assets/fontes/`, e não baixadas em tempo de execução. Todas vieram do Google Fonts e **todas
são OFL 1.1**, não OFL-ou-Apache como esta linha dizia antes de eu conferir arquivo por arquivo.
A licença de cada família viaja junto, em `assets/fontes/LICENCA-<familia>.txt`, que é o que a
OFL exige de quem redistribui.

Anton · IBM Plex Mono · Antonio · Bricolage Grotesque · Newsreader · Cascadia Mono · Bodoni Moda
· Karla · Chivo · Chivo Mono · Fraunces · Work Sans · Hanken Grotesk. Acentos pt-BR conferidos
glifo a glifo nas quinze — o `fontes.sh` reconfere a cada execução e avisa se faltar algum.

**Por que embutidas e não baixadas**, já que baixar funcionava: o piso de entrelinha e o
comprimento de linha do laço do gabarito são calculados **a partir do arquivo**. Uma revisão da
fonte no Google não quebraria nada — ela só faria esses números passarem a ser outros, em
silêncio, num sistema que existe para eles serem estáveis entre os oito cards. E o download
dependia de mandar um User-Agent antigo para a API devolver TTF em vez de woff2, que é
comportamento não documentado.

**Não subsetadas, de propósito.** Reduzir aos glifos usados levaria os 1,8 MB para uns 200 KB, e
reintroduziria exatamente a falha que o `montagem.md` gasta um parágrafo avisando: o navegador
troca **só o glifo faltante** por outra fonte, sem erro no console. Os esqueletos usam `→` no pé
e `·` na paginação. 1,5 MB é barato perto de uma classe nova de erro silencioso.
