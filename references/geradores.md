# Gerar imagem — o guia para quem nunca conectou nada

É aqui que quem não é técnico trava. Conduza com paciência: diga **o que muda no resultado** antes de pedir qualquer coisa, e trate conectar como opcional de verdade. Quatro dos seis estilos ficam completos sem nenhum gerador.

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

Os quatro estilos que ficam completos assim: brutalista vetorial, janelas, neo-brutalismo colorido, minimalista editorial quente.

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

**Comportamento verificado:** job travado existe. Um em cada cinco fica em `in_progress` indefinidamente enquanto os vizinhos terminam em 20 segundos. O sintoma é a resposta trazer `width: 896` em vez da resolução pedida. **Não fique repolando** — dispare de novo com o prompt levemente reescrito; sai na segunda. E o proxy devolve 502 esporádico, que é transitório: espere e repita.

### Magnific — como usar

Serve para **ampliar e recompor imagem existente**, não para criar do zero. Útil quando o usuário traz uma imagem pequena que precisa ocupar o card, ou quando uma geração ficou boa na composição e curta na resolução.

---

## Depois de gerar, sempre

1. Baixe e **confirme que o arquivo tem tamanho maior que zero**
2. **Abra e olhe.** O modelo entrega imagem errada com a mesma confiança da certa
3. **Recorte a moldura** se vier margem branca ou borda decorativa — dentro do card vira caixa-dentro-de-caixa
4. Se veio texto por acidente, não tente corrigir com prompt: recorte fora, ou cubra com um bloco de tinta chapada, que é peça legítima de composição impressa

O briefing de imagem — como escolher o assunto, o teste da troca, o que proibir no prompt — está em [grafismos.md](grafismos.md).
