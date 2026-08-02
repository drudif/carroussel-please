# Gerar imagem — o guia para quem nunca conectou nada

É aqui que quem não é técnico trava. Conduza com paciência: diga **o que muda no resultado** antes de pedir qualquer coisa, e trate conectar como opcional de verdade. Quatro dos sete ficam completos sem nenhum gerador, e um quinto — o superminimal — resolve com banco de imagem.

## O que muda, em português

| | O que você faz | O que aparece no card |
|---|---|---|
| **Só código** (padrão) | nada | Formas, grades, ícones, diagramas, telas de app desenhadas. Sai exato na sua paleta, custa zero. Não faz retrato nem cena |
| **Chave de API** | criar conta e copiar uma chave, ~5 min | Imagem em alta, controle de estilo, consistência entre cards. Centavos por imagem |
| **Conector** (Higgsfield, Magnific) | autorizar uma vez, ~2 min | Vários modelos, ampliação, remoção de fundo. Consome créditos da assinatura |

E o que **não** muda em nenhuma das três: a tipografia é sempre desenhada em código. Nenhum gerador escreve texto confiável em português — `ç`, `ã`, `õ`, `ê` saem tortos ou viram outra letra antes de qualquer coisa. Isso não é limitação de plano gratuito, é limitação de todos eles.

---

## Caminho 1 — nenhum gerador

Perfeitamente viável, e diga isso em voz alta para ele não sentir que escolheu a versão pobre. A maior parte de um carrossel é estrutura — grade, lista, ícone, diagrama, abstração de interface — e estrutura se **desenha** melhor do que se gera: nasce na paleta certa, mostra só o que interessa, e não vaza dado nenhum.

Os quatro estilos que ficam completos assim: brutalista vetorial, terminal, neo-brutalismo colorido e minimalista editorial quente. O **superminimal** fica de pé em código puro — tipografia preta sobre branco com blocos de cor chapada —, mas é o único dos sete que fica claramente **magro** sem imagem: nele a foto é o evento, e sem gerador quem resolve isso é banco de imagem, não desenho.

---

## Caminho 2 — chave de API

Vale quando o carrossel depende de imagem de verdade. O custo real são **centavos por imagem**, e um carrossel usa poucas.

### Gemini — o "nano banana"

O modelo de imagem do Google. Bom em diagrama e em editar imagem existente.

1. Abra **aistudio.google.com/apikey** e entre com a conta Google
2. **Create API key**, escolha um projeto — se não tiver, ele cria
3. Copie a chave, que começa com `AIza…`
4. **Guarde num arquivo, não no chat:**

```bash
echo 'export GEMINI_API_KEY="cole-a-chave-aqui"' >> ~/.zshrc
source ~/.zshrc
```

5. Confirme:

```bash
[ -n "$GEMINI_API_KEY" ] && echo "chave carregada" || echo "não carregou — reabra o terminal"
```

O AI Studio tem faixa gratuita para testar; geração de imagem costuma ser cobrada. Confirme o preço na própria página antes de rodar em lote.

### OpenAI — o modelo de imagem do ChatGPT

1. Abra **platform.openai.com/api-keys**
2. **Create new secret key**, dê um nome, copie. Começa com `sk-…` e **só aparece uma vez**
3. Adicione crédito em **Settings → Billing**. Sem crédito, a chave existe mas toda chamada falha
4. Guarde igual ao anterior

A API é separada da assinatura: pagar o ChatGPT Plus **não** dá crédito de API.

### Regras para qualquer chave

- **Nunca peça que ele cole a chave no chat.** O que passa pelo chat fica registrado. Peça que ponha na variável de ambiente e diga só "pronto"
- **Nunca grave a chave** no perfil, no `DIRECAO.md`, no HTML ou em qualquer arquivo que vá para o git
- No perfil registre apenas `gemini: chave configurada em AAAA-MM-DD`
- Se ele colar mesmo assim: use, avise na hora que ficou exposta, e diga para revogar e gerar outra

---

## Caminho 3 — conector

Explique o que é sem usar a sigla:

> É dar ao Claude uma chave da sua conta do Higgsfield, para ele gerar as imagens sem você sair daqui. Você autoriza uma vez e pronto.

### Como conectar

**No Claude web ou no app:** Configurações → **Conectores** → procurar a ferramenta → **Conectar** → autorizar na janela que abre.

**No Claude Code, no terminal:** numa sessão interativa, digite `/mcp` para ver e autorizar. Para adicionar um servidor novo:

```bash
claude mcp add <nome> <comando-ou-url>
```

**Importante:** a autorização abre navegador e espera resposta, então **não roda em sessão automatizada**. Num contexto não interativo, avise que ele precisa autorizar e siga desenhando em código nesse meio-tempo.

### Verifique antes de contar com o conector

Ferramenta que aparece na lista **não** é ferramenta autorizada. Faça uma chamada barata de leitura antes de planejar em cima dela:

```
mcp__<servidor>_higs__balance     → devolve créditos e plano
```

Erro de autenticação significa conector não autorizado. Diga isso claramente, explique onde autorizar, e continue desenhando em vez de travar o trabalho.

### Higgsfield — como usar

1. `models_explore` com `action:'recommend'` quando não souber qual modelo serve. Não chute
2. `generate_image` devolve **um job pendente**, não a imagem
3. `job_status` com `sync:true` espera terminar e devolve o `rawUrl`
4. Baixe com `curl`, confirme tamanho maior que zero, **abra e olhe**

Chame `balance` **antes e depois** e reporte o custo real. Estimativa não serve: crédito é dinheiro dele.

Para grafismo com forma precisa ou diagrama, `nano_banana_pro` deu o melhor resultado — foi com ele que as dezoito referências dos estilos foram feitas, a 2 créditos cada.

**Comportamento verificado:** job travado existe, e é **raro** — 1 em 16 na medição mais longa.
O sintoma está descrito em [Sobre jobs travados](#sobre-jobs-travados), no fim deste arquivo, e
**não é** `width:896`. E o proxy devolve 502 esporádico, que é transitório: espere e repita.

### Magnific — como usar

Serve para **ampliar e recompor imagem existente**, não para criar do zero. Útil quando o usuário traz uma imagem pequena que precisa ocupar o card, ou quando uma geração ficou boa na composição e curta na resolução.

---

## Depois de gerar

Baixar, conferir tamanho, **abrir e olhar**, recortar moldura: a lista está em
[grafismos.md](grafismos.md#depois-de-gerar-sempre), com o recorte em Python.

E o briefing de imagem — como escolher o assunto, o teste da troca, o que proibir no prompt —
está no mesmo arquivo.

---

# O laço do gabarito — quando há gerador conectado

Gerador de imagem **compõe tipografia melhor do que a gente compõe sozinho**, e **escreve pior
que o navegador**. O laço abaixo usa cada um no que ele faz bem: a composição vem dele, as
letras vêm do HTML.

**Custo, em faixa — e diga a faixa ao usuário antes de começar, não o melhor caso.** Quem tem
60 créditos precisa saber disso enquanto ainda dá para escolher outro caminho:

| | por card | de onde vem |
|---|---|---|
| caminho feliz | 2 gerações, **4 créditos** | gabarito + chapa limpa |
| geometria precisando de segunda tentativa | **6 a 8 créditos** | vaivém de proporção |

Medido num carrossel real de 8 cards: **16 gerações, 32 créditos** — 5 das extras vieram do
vaivém de geometria e 1 job travou. Aquela medição é de **antes** das duas correções abaixo (a
âncora que prendia composição e a fração de zona que não sobrevivia), que existem justamente
para eliminar esse vaivém; a faixa deve encolher, e o número acima não é a nova expectativa.

## Os cinco passos

**1 · Gera o card inteiro, com título e sub.** O texto no prompt não é para usar — é para o
modelo ter o que diagramar. Sem texto ele devolve ilustração, não cartaz.

**2 · Mede**, com `assets/ferramentas/medir-chapa.py <chapa.png>`. Ela devolve o vão livre —
lado, topo, altura, largura —, se o fundo é papel ou tinta, e onde começa o pé. **A medida é o
produto desta etapa**: ela sobrevive mesmo que a imagem seja descartada, e `topo` e `alt` entram
direto como o `vao:{y,h}` do esqueleto.

**3 · Acha a fonte open-source mais próxima, na hora.** Ver a régua de substituição abaixo.

**4 · Refaz sem texto**, passando a primeira geração como **mídia de referência**. Gerar do
zero devolve outra composição e o gabarito se perde.

> Repare que aqui a mídia de referência é usada **para prender a composição**, e é por isso que
> ela funciona. É o mesmo mecanismo que, usado **entre cards diferentes**, congela os sete no
> enquadramento da capa — ver a âncora, abaixo. A regra única: **mídia de referência prende
> geometria.** No mesmo card isso é o que você quer; entre cards, é o defeito.

**5 · Monta em HTML por cima**, com o texto vindo do `TEXTOS.md`.

## As três zonas — sem elas o laço não fecha

O gabarito precisa nascer com **três zonas declaradas**, e o gerador precisa saber que as três
são obrigatórias. Cole no prompt:

```
THREE ZONES, all mandatory, all inside the central square of the sheet:
1 · HEADLINE ZONE — a clean, uninterrupted area for a very large headline of N lines. Behind
    it nothing but flat ground: bare paper, or one single flat field of solid ink. No halftone,
    no pattern, no illustration detail crosses this zone.
2 · SUBTITLE ZONE — directly below the headline, a clean band tall enough for a thin rule plus
    three lines of small text. Flat ground only. This band is NOT a leftover at the bottom
    edge: it belongs to the composition and must have air beneath it.
3 · ILLUSTRATION ZONE — everything else, free to bleed off the edges and be as dense as it wants.
The three zones INTERLOCK: the illustration may overlap the outer edge of the headline zone so
type and image lock together, but must NEVER enter the area where the letters sit.
```

**Por que isto é obrigatório e não recomendação.** Sem zona declarada a chapa nasce cheia, e a
montagem vira cabo de guerra: protege o texto e a faixa chapada mata o grafismo; protege o
grafismo e a régua sai da folha; encolhe a letra e o título deixa de ser título. Foram três
tentativas, três defeitos, mesma raiz. **Numa chapa cheia não existe montagem certa** — a
hierarquia de sacrifício só funciona quando há o que sacrificar, e depois da tinta seca só há
cobrir.

### Peça zona desenhada, nunca fração — e depois meça

As zonas são controláveis; **a proporção entre elas não é.** O modelo puxa tudo para o meio, e
a fração escrita no prompt não sobrevive de uma rodada para a outra:

| pedi | veio |
|---|---|
| ilustração em 34% | 38%, depois 53% |
| ilustração em 22% | 41% |
| ilustração em 15% | 24% |
| vazio até 84% | 64%, depois 78% |

Os desvios chegaram a **19 pontos percentuais**, e mudaram de sinal entre gerações — calibrar
um "+8%" com uma amostra e a amostra seguinte desmentir foi exatamente o que aconteceu. Por
isso não existe tolerância publicável aqui: pedir fração com margem só mantém a ilusão de
controle. **Não peça fração.** Peça uma faixa desenhada e um campo vazio grande, e aceite onde
a divisa cair.

**O veredito, e ele vale para o laço inteiro: a chapa manda, o layout cede.** Não se planeja o
layout e se força a chapa a caber nele. Gera-se, **mede-se o vão chapado que veio**, e
dimensiona-se o tipo para ele, com teto no comprimento de linha do gabarito.

Como medir o vão está em [montagem.md](montagem.md#medir-a-chapa-antes-de-diagramar) — os
cinco passos do perfil de cobertura. É o passo 2 do laço, e é a entrega real desta etapa.

## Consistência entre os cards: a âncora carrega tinta, não composição

Repetir o bloco de estilo em sete prompts dá sete cartazes primos, não irmãos. Passar a capa
como **mídia de referência** nos outros fecha a impressão — e **sobrescreve a geometria pedida
no texto do prompt**, por cima de instrução em caixa alta.

Medido três vezes, mesmo assunto, `nano_banana_pro`:

| geração | âncora? | pedi | o vão chapado começou em |
|---|---|---|---|
| capa v1 | — | "metade de baixo" | y 648 |
| capa v2 | **sim** | "34%, ilustração compacta" | y 648 — *idêntico à v1* |
| capa v3 | **não** | "30%" | **y 511** |
| card 02 | **sim** | "62% de papel limpo" | y 749, tendo pedido 838 |

Com âncora a proporção da referência voltou ao pixel, mesmo com `RECOMPOSED with a different
vertical proportion` escrito em caixa alta. Sem âncora, a geometria obedeceu na primeira.

**A regra:** a âncora serve para **tinta, retícula e traço**. Se a composição precisa mudar
entre um card e outro — e num carrossel ela precisa, senão são sete paredes iguais —, **a
âncora sai**.

**E isso quase não dói, por um motivo estrutural:** num carrossel de nível 1 **a tipografia é
HTML**. O principal serviço que a âncora prestava — manter o sistema tipográfico e o
comprimento de linha entre os cards — já está garantido pelo CSS, que é o mesmo arquivo para
os sete. Quem segura a impressão sozinho é o **bloco de estilo** do estilo escolhido, que é
longo e específico de propósito.

Então: o bloco de estilo é a âncora; a imagem não é. Use mídia de referência só quando a
composição **deve** repetir — capa e fecho de uma série de duas peças, por exemplo.

Sem essa correção foram 3 gerações perdidas, 6 créditos, num carrossel só.

## A régua de substituição de fonte

**Ela vem pronta: `assets/regua-fonte.py`.**

```bash
./regua-fonte.py chapa-01.png 290,590 "O ALMOÇO"      # candidatas: todas as embutidas
```

Os três argumentos são o PNG, a faixa vertical `topo,base` da linha, e **a string que está
naquela faixa**. A string é obrigatória: as três medidas dependem de quais letras foram medidas,
e comparar `"AÇÃO"` contra uma amostra genérica dá razão largura/caixa-alta 1,31 contra 3,87 na
**mesma fonte** — a régua elege a errada com toda a confiança. O script também para se a faixa
estiver cortando o glifo, que distorce as três medidas juntas e em silêncio.

Nenhuma open-source bate a fonte que o modelo desenha. Testei catorze, incluindo variáveis com
eixo de largura. **Casar só a largura não basta** — são três medidas independentes:

| | gabarito | Saira wdth50 | Saira comprimida .796 | **Anton comprimida .728** |
|---|---|---|---|---|
| razão largura/caixa-alta | 2,504 | 3,138 | 2,497 | **2,499** |
| densidade de tinta | 0,656 | 0,696 | 0,698 | **0,665** |
| espessura da haste | 13,8% | 18,8% | 14,9% | **14,1%** |

Anton comprimida ganhou por um motivo contraintuitivo: **ela já é mais densa, então encolher
devolve a haste à espessura certa em vez de afiná-la.** O desvio de partida cancelou o desvio
da compressão. Comprimir normalmente estraga o traço — aqui não estragou, e só a medição
mostrou isso.

**Confira os acentos glifo a glifo** na instância final. `fontTools.varLib.instancer` gera a
estática; `getBestCmap()` diz o que falta.

## Do gabarito, o que manda é o comprimento de linha

Com fonte diferente as duas medidas não fecham juntas: mantendo a caixa alta, as linhas ficam
mais longas na proporção do desvio e estouram por cima da ilustração. **A que segura a
composição é o comprimento**; a caixa alta cede.

E o corpo de cada card sai de **duas restrições, a menor manda**: o comprimento de linha do
gabarito, que faz os sete lerem como a mesma série, e a altura do vão medido na chapa, que
impede o título de invadir a ilustração. Num carrossel de sete, o comprimento mandou em quatro
e a altura em três — corpos de 107 a 280 px, e mesmo assim um sistema só.

## A régua da chapa é o divisor das zonas

O gerador desenha uma régua fina entre a zona do título e a do sub. **Leia essa régua em vez de
dividir a faixa livre por conta própria** — corrida horizontal longa, com menos de ~26px de
espessura. Ela diz exatamente onde uma zona acaba. Ignorá-la punha a régua da montagem em cima
do grafismo, e desenhava uma segunda régua ao lado da que já existia.

## O que o gerador erra, sempre

**Texto.** Em sete gerações de teste, sete tiveram defeito: letra comida (`ENTIEVISTA`), letra
dobrada (`LINKEDIIN`), palavra repetida (`SÓ SÓ`), frase inteira duplicada. Os **acentos saem
certos** em corpo grande a 2k — `Ã`, `Ó`, `ê` todos bem desenhados —, o que calibra a regra sem
derrubá-la: o modelo já acerta o acento e continua errando a palavra. Como estudo de composição
vale muito; como arte-final, nunca.

**Moldura de maquete.** Volta como folha fotografada mesmo com `no frame, no border, no paper
mockup` escrito. Resolve no recorte, que é mais barato que regerar.

**Miolo vazio**, quando você pede um card "arejado" — ele lê vazio como buraco. E aqui a lição
é maior que o defeito: **descrever o que ocupa o meio vence proibir o vazio.** "Duas formas
geométricas sobrepondo o pé do título, no meio da folha" resolve sozinho; `NO DEAD CENTRE`
sozinho, não. Proibição não diz o que desenhar no lugar.

**Ilustração demais.** Quando a chapa não deixa zona de título utilizável, a correção é
proporção — e proporção cabe num recorte. Reduzir a arte ao terço de cima custa zero; regerar
custa dois créditos e pode travar.

## Sobre jobs travados

`width:896` na resposta **não** é sinal de travamento — é o estado intermediário, e o mesmo job
completa em 1856 depois. Travado é o que fica em `in_progress` depois de três consultas
seguidas. Aí sim: re-dispare com o prompt reescrito, não fique consultando.

Frequência medida: **1 em 16**, não 1 em 5.

### Quando o observado contradiz o que está gravado, atualize o perfil

O `~/.claude/carrossel-perfil.md` carregou o diagnóstico velho de job travado — `1 em 5`,
sintoma `width:896` — depois de este arquivo já ter sido corrigido. Perfil só escrito na etapa 0
envelhece calado, e o custo é você desistir de um job que ia completar.

**Então: comportamento de gerador que você observar e que contradiga o perfil, corrija o perfil
na hora**, com a data. É a única linha do fluxo que a etapa 7 tem permissão de escrever ali.
