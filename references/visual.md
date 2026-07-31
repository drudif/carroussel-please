# A régua visual

Destilado de duas skills de julgamento estético — **`bencium-innovative-ux-designer`** e **`high-end-visual-design`** — traduzido para o meio desta skill: uma peça **estática**, de 1080×1350, que será vista no feed a um braço de distância e passada em dois segundos.

A tradução não é cosmética. As duas skills foram escritas para interface viva, e a maior parte do que elas ensinam é sobre **comportamento** — hover, easing, revelação por scroll, colapso responsivo. Nada disso existe num PNG. O que sobrevive é julgamento de composição, escala e cor, e é isso que está aqui.

> **Se alguma das duas estiver instalada, consulte a instalada** para julgamento de gosto em interface. Para carrossel, o que vale é este arquivo. Procedência em [CREDITOS.md](../CREDITOS.md).

---

## O que transferiu

### Comprometa-se com a direção inteira

A regra original é "escolha um extremo estético e execute com precisão, sem meias medidas". Aqui ela vira: **execute o estilo escolhido sem amaciar.** Riso com pouca textura vira impressão suja. Brutalismo com canto arredondado vira app. Colagem com as bordas alinhadas vira grade. O estilo pela metade não fica no meio do caminho — fica errado, porque perde a razão de ser sem ganhar outra.

### A lista de antipadrões

Bate com a checagem da `SKILL.md` e é a parte mais valiosa das duas skills. Se algum destes aparecer, a peça lê como gerada por IA:

**Fontes** — Inter, Roboto, Arial, Helvetica, Open Sans, fonte de sistema como escolha principal, e **Space Grotesk**, que virou o default seguro de todo modelo. Os seis estilos já resolvem isso: nenhum par tipográfico deles está nesta lista.

**Cor** — azul de SaaS `#3B82F6`, gradiente roxo sobre branco, gradiente índigo→violeta, iridescência.

**Efeito** — vidro fosco, blur de fundo, blob 3D, esfera de vidro, forma orgânica renderizada, glow atrás de texto, sombra gigante e difusa embaixo de tudo.

**Composição** — hero centralizado com três cards iguais embaixo, ícone dentro de tile pastel arredondado, emoji como elemento gráfico, tudo centralizado, canto arredondado em tudo.

### Atmosfera vem de material, não de cor

A recomendação original é preferir textura, padrão e fotografia a campos de cor chapada. Traduzida: **um campo de cor sozinho não sustenta oito cards.** O que dá espessura é a camada de material — retícula, fibra, grão, erro de registro, grade milimetrada, papel rasgado. Cada um dos seis estilos declara qual material usa e em que opacidade, e três deles declaram **nenhum** — o que também é uma decisão, não uma omissão.

### Macro-respiro

"Dobre o seu padrão de espaçamento" é a regra que mais separa peça cara de peça amadora. Num card de 1080×1350: margem lateral nunca abaixo de **58px**, e o vão entre o bloco de texto e o grafismo nunca abaixo de **22px**.

E o vazio precisa ser **contíguo**. Quatro folgas iguais de 40px leem como erro de diagramação; um vão único de 160px lê como decisão. Este é o ajuste que mais melhora um card fraco.

### Escala tipográfica com disciplina

Defina a escala antes de diagramar e fique nela. Para 1080 de largura, uma escala que funcionou:

| Papel | px | Observação |
|---|---|---|
| Título de capa | 100–130 | três a cinco linhas; entrelinha pelo piso da fonte |
| Título de card | 90–125 | duas a três linhas |
| Corpo | 30–36 | **nunca abaixo de 30**; 34 se o destino é LinkedIn |
| Legenda, rótulo | 17–19 | só onde carregar informação verdadeira |

**Sobre o corpo:** 30 é piso, não alvo. O erro comum é diagramar o corpo pequeno porque *sobra espaço* —
e sobra justamente porque o título já domina. Corpo de 26px sobre 1080 parece elegante na tela do
computador e some no feed, que é onde a peça vive. Se o texto não couber em 30px, **corte o texto**,
não reduza o corpo: a hierarquia é leitura > respiro > grafismo, e o corpo é leitura.

A razão entre o maior e o menor corpo fica em pelo menos **2,5:1**. Abaixo disso não há hierarquia, só tamanhos diferentes.

### Todo elemento justifica a existência

"Comece pela complexidade e remova até chegar na solução mais simples que ainda funciona." Em carrossel isso encontra a auditoria de slots do anti-slop e vira a mesma regra por dois caminhos: **slot que não carrega informação sai, e o vazio que sobra vira respiro.**

---

## O que não transferiu, e por quê

Documentado porque o erro seria aplicar mesmo assim — a orientação está escrita nas duas skills, com autoridade, e não vale aqui.

| O que elas ensinam | Por que não vale em carrossel |
|---|---|
| Coreografia de movimento, `cubic-bezier`, física de mola | Não há movimento num PNG |
| Estados de hover, tensão cinética em botão | Não há interação |
| Revelação por scroll, `IntersectionObserver` | Não há scroll dentro do card |
| Colapso responsivo abaixo de 768px | O card é 1080×1350, fixo, sempre |
| `backdrop-blur`, arquétipo "Ethereal Glass" | **É o antipadrão que a skill existe para evitar.** Uma das duas skills recomenda vidro fosco com blur pesado e a outra o proíbe. Aqui a proibição vence |
| Aninhamento "Double-Bezel" com `rounded-[2rem]` | Concentric squircle é linguagem de produto de software. Num cartaz, lê como print de app dentro do card |
| Pílula de eyebrow antes de todo título | Colide de frente com a auditoria de slots do anti-slop: é exatamente o slot que nasce do template e é preenchido por necessidade. **O anti-slop vence** |
| Guardas de performance de GPU | Renderização é headless e única |

As duas últimas linhas são conflito real entre skills, não omissão. Resolvidos aqui e resolvidos assim.

---

## O teste final

Duas perguntas, olhando o PNG pronto:

**Dá para dizer que esta peça é desta direção, sem ler o texto?** Se a resposta depende do conteúdo, a direção não pegou — ela virou fundo colorido.

**Onde o olho entra?** Deve haver uma resposta única e óbvia. Se houver duas, faltou hierarquia; se não houver nenhuma, faltou o evento.

---

## O piso do corpo é 34, não 30

Corrigido depois de ver o sub espremido em produção. O LinkedIn reduz o documento no feed e a
maioria dos carrosséis vai para os dois destinos: **34px é o piso, 30 é exceção justificada.**

E a largura da linha do sub também é medida: ele não corre a folha inteira quando a ilustração
está do outro lado — respeita a mesma coluna do título.
