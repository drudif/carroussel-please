# Geradores de imagem — o guia para quem nunca conectou nada

Esta é a etapa em que quem não é técnico costuma travar. Conduza com paciência: explique **o que muda no resultado** antes de pedir qualquer coisa, ofereça o caminho sem cadastro primeiro, e trate conectar como opcional de verdade — a maioria dos carrosséis fica ótima sem nenhum gerador.

## Como apresentar ao usuário

Comece pelo que ele ganha, não pelo que precisa fazer:

> Antes de montar a arte, uma decisão que muda o visual: eu posso desenhar os grafismos em código, gerar imagens de graça, ou usar um gerador melhor se você quiser conectar um. Te explico as três em trinta segundos e você escolhe — dá pra começar sem conectar nada e mudar de ideia depois.

### O que muda, na prática

**A capa muda de patamar.** Com um gerador conectado, a capa passa a receber imagem gerada sempre — e a capa é o card que decide se os outros sete serão vistos.

**O número que importa:** sem gerador são **9 estilos** disponíveis na biblioteca; com qualquer gerador conectado, **16**. Os 7 extras são os que precisam de retrato, cena, textura ou colagem — Vaporwave, Pontilhismo, Mixed Media, Kawaii, Wabi Sabi, Rebus e Y2K.

| | O que você faz | O que aparece no card |
|---|---|---|
| **Só código** | nada | Formas, grades, ícones, diagramas, abstrações de interface. Preciso e na sua paleta exata. Não faz retrato nem cena. |
| **Pollinations** | nada | Tudo do código, mais textura, ilustração e cena. Resolução média — bom como fundo sob retícula, fraco em detalhe fino. |
| **Chave de API** (Gemini ou OpenAI) | criar uma conta e copiar uma chave, ~5 min | Imagem em alta, controle melhor do estilo, consistência entre cards. Custa centavos por imagem. |
| **MCP** (Higgsfield, Magnific) | autorizar um conector, ~2 min | Vários modelos, ampliação, remoção de fundo, controle de movimento. Consome créditos da assinatura. |

Diga também o que **não** muda: a tipografia é sempre desenhada em código, em qualquer um dos quatro. Nenhum gerador escreve texto de forma confiável em português — o acento é a primeira coisa que sai errada. Isso não é limitação do plano gratuito; é limitação de todos eles.

---

## Caminho 1 — Pollinations (o padrão, zero configuração)

Não pede conta, chave, cartão nem instalação. Se o usuário não quiser decidir nada, é aqui que você fica.

```bash
PROMPT=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))" \
  "risograph print, two ink plates, coarse halftone, flat frontal composition, no gradient, no glow, no 3D, no text, no lettering anywhere")

curl -sS --max-time 90 -o grafismo.jpg \
  "https://image.pollinations.ai/prompt/$PROMPT?width=1080&height=1350&seed=42&nologo=true"
```

Comportamento verificado:

| | |
|---|---|
| Proporção | respeitada com precisão — 1080×1350 devolve 0,800 exato |
| Resolução | limitada a ~590 mil pixels: 686×858 no 4:5, 768×768 no quadrado |
| Determinismo | mesma seed e mesmo prompt devolvem o mesmo arquivo |
| Modelo | `sana` — confira em `curl https://image.pollinations.ai/models` |
| Custo | zero |

Peça sempre na **proporção** do card, não no tamanho — a proporção é respeitada e é o que importa. Use a seed para variar de forma controlada: mesmo prompt com quatro seeds dá quatro composições comparáveis.

---

## Caminho 2 — Chave de API

Vale a pena quando o carrossel depende de imagem de verdade: retrato, produto, cena. Explique o custo em termos reais — **alguns centavos por imagem**, e um carrossel usa poucas.

### Gemini (o "nano banana")

O modelo de imagem do Google. Bom em diagrama, texto legível em inglês e edição de imagem existente.

1. Abra **aistudio.google.com/apikey** e entre com a conta Google
2. Clique em **Create API key** e escolha um projeto (se não tiver, ele cria um)
3. Copie a chave — começa com `AIza...`
4. **Guarde num arquivo, não no chat.** No terminal:

```bash
echo 'export GEMINI_API_KEY="cole-a-chave-aqui"' >> ~/.zshrc
source ~/.zshrc
```

5. Confirme que funcionou:

```bash
[ -n "$GEMINI_API_KEY" ] && echo "chave carregada" || echo "não carregou — reabra o terminal"
```

O Google AI Studio tem faixa gratuita para testar. Geração de imagem costuma ser cobrada — confirme o preço atual na própria página antes de rodar em lote.

### OpenAI (o modelo de imagem do ChatGPT)

1. Abra **platform.openai.com/api-keys**
2. **Create new secret key**, dê um nome, copie — começa com `sk-...`. Ela só aparece uma vez
3. Adicione crédito em **Settings → Billing**. Sem crédito, a chave existe mas toda chamada falha
4. Guarde igual:

```bash
echo 'export OPENAI_API_KEY="cole-a-chave-aqui"' >> ~/.zshrc
source ~/.zshrc
```

A API é separada da assinatura do ChatGPT: pagar o ChatGPT Plus **não** dá crédito de API.

### Regras para qualquer chave

- **Nunca peça que ele cole a chave no chat.** O que passa pelo chat fica registrado. Peça que coloque na variável de ambiente e diga só "pronto"
- **Nunca grave a chave no perfil**, no `DIRECAO.md`, no HTML ou em qualquer arquivo que vá para o git
- No perfil, registre apenas `gemini: chave configurada em AAAA-MM-DD` — o fato, nunca o valor
- Se o usuário colar uma chave mesmo assim, use, avise na hora que ela ficou exposta, e diga para revogar e gerar outra depois

---

## Caminho 3 — MCP (Higgsfield, Magnific)

MCP é o jeito de o Claude falar direto com uma ferramenta externa. Explique assim:

> É como dar ao Claude uma chave da sua conta do Higgsfield, para ele gerar as imagens sem você sair daqui. Você autoriza uma vez e pronto.

### Como conectar

**Se o usuário usa Claude na web ou no app:** Configurações → **Conectores** → procurar a ferramenta → **Conectar** → autorizar na janela que abre. Volta pronto.

**Se usa Claude Code no terminal:** numa sessão interativa, digite `/mcp` para ver os conectores e autorizar. Para adicionar um novo servidor:

```bash
claude mcp add <nome> <comando-ou-url>
```

**Importante:** o fluxo de autorização abre navegador e espera resposta, então **não roda numa sessão automatizada**. Se você estiver num contexto não interativo, avise que a autorização precisa ser feita por ele e siga com Pollinations nesse meio-tempo.

### Verifique antes de contar com o conector

Ferramenta que aparece na lista **não** é ferramenta autorizada. Faça uma chamada barata de leitura antes de planejar em cima dela:

```
mcp__<servidor>_higs__balance     → devolve créditos e plano
```

Se voltar erro de autenticação, o conector não está autorizado. Diga isso claramente, explique onde autorizar, e continue com Pollinations em vez de travar o trabalho.

### Higgsfield — como usar

1. `models_explore` com `action:'recommend'` quando não souber qual modelo serve. Não chute
2. `generate_image` devolve **um job pendente**, não a imagem
3. `job_status` com `sync:true` espera terminar e devolve o `rawUrl`
4. Baixe com `curl`, confirme tamanho maior que zero, **abra e olhe**

Chame `balance` **antes e depois** e reporte o custo real. Estimativa não serve: crédito é dinheiro dele.

Para grafismo com diagrama ou forma precisa, `nano_banana_pro` deu o melhor resultado.

### Magnific — como usar

Serve para **ampliar e recompor imagem existente**, não para criar do zero. Útil quando o usuário traz uma imagem pequena que precisa ocupar o card inteiro, ou quando uma geração ficou boa na composição e curta na resolução.

---

## Se o usuário não quiser conectar nada

Perfeitamente viável, e vale dizer isso em voz alta para ele não sentir que está escolhendo a versão pobre. A maioria dos cards de um carrossel é estrutura — grade, lista, ícone, diagrama, abstração de interface — e estrutura se desenha melhor em código do que se gera. O gerador entra em um ou dois cards, quando o assunto pede retrato ou cena.

---

## A regra que vale para todos

Nenhum gerador escreve texto de forma confiável, e **o acento é onde o erro aparece primeiro** — `ç`, `ã`, `õ`, `ê` saem tortos ou viram outra letra antes de qualquer coisa. Toda palavra que o leitor vai ler é HTML/CSS capturado, sem exceção, inclusive paginação, handle e assinatura.

Se um grafismo veio com texto por acidente, não tente corrigir com prompt: recorte fora, ou cubra com um bloco de tinta chapada, que é peça legítima de composição impressa.
