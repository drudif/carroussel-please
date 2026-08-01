# Perfil — a conversa de setup

O perfil mora em `~/.claude/carrossel-perfil.md` e roda **uma vez**. Nos carrosséis seguintes, mostre um resumo de três linhas e pergunte só o que mudou.

## Como conduzir

Uma pergunta por mensagem, seguindo o protocolo de [texto.md](texto.md). Toda pergunta pode ser pulada — pulada vira `[CONFIRMAR]` no arquivo, e você segue com o padrão indicado.

**Sem jargão.** Quem instala esta skill pode nunca ter aberto um terminal por vontade própria. Nada de "MCP", "chave de API", "área de segurança", "1080×1350" ou "duotone" nas perguntas. Esses termos existem no seu trabalho, não na conversa. Se um deles for inevitável, explique em uma frase e siga.

Agrupe em três rodadas curtas: **quem publica**, **como parece**, **com o que produz**.

São nove perguntas. A de imagem **não está aqui** — ela é a etapa 1, logo depois do perfil.

---

## Rodada 1 — quem publica

**1. Quem assina?** Nome e arroba. Se houver mais de uma conta — pessoal e marca —, qual é a deste trabalho. Muda a voz inteira.

**2. Onde publica?** Instagram, LinkedIn, os dois, outro lugar. Define quantidade de cards e densidade de texto; a tabela está em [texto.md](texto.md).
→ Padrão: Instagram, 8 a 10 cards.

**3. Para quem?** Uma frase sobre quem lê. "Criativo de agência que não programa" e "dev sênior" produzem carrosséis opostos a partir do mesmo assunto.

**4. Qual a voz?** Dois ou três adjetivos e, se existir, um post que soou certo. Se o projeto tiver `.agents/social-media-context-sms.md`, **leia o arquivo e pule a pergunta** — a voz já está documentada lá.

---

## Rodada 2 — como parece

**5. Sua marca tem cor e fonte fechadas?** Se tiver, elas vencem qualquer sugestão sua. Peça as cores e o nome das fontes.
→ Padrão: não tem; a direção nasce na etapa 2, dentro dos sete estilos.

Se ele tiver fonte de marca, confira o arquivo antes de prometer usá-la:

```bash
ls ~/Library/Fonts | sed 's/-.*//;s/\..*//' | sort -u
```

Fonte que não está instalada não entra. E fonte de marca precisa passar pela conferência de acentos da etapa 3 como qualquer outra.

**6. Tem logo ou assinatura para o rodapé?** Caminho do arquivo, ou só o arroba em texto.
→ Padrão: arroba em texto, e só na capa e no fecho.

*(Não pergunte se vai impulsionar. A área de segurança do corte quadrado é obrigatória sempre — post orgânico vira impulsionado depois sem ninguém refazer a arte.)*

---

## Rodada 3 — com o que produz

**Não pergunte de imagem nesta rodada.** A pergunta de como as ilustrações são feitas é a
**etapa 1** da SKILL.md, e ela é a primeira coisa depois do perfil por um motivo: **é ela que
filtra os estilos**. Cada nível favorece uns e enfraquece outros, e a etapa 2 abre já pelos que
funcionam melhor no nível escolhido.

**E não a antecipe em versão binária** — *"você quer gerar imagem ou desenhar tudo?"*. Binário
**não distingue banco aberto de desenho em código**, que são duas opções diferentes e ambas sem
conectar nada. Quem responde "desenho tudo, sem conectar nada" pode estar recusando o gerador,
não o banco. Toda vez que essa pergunta vazou para cá, a etapa 1 depois foi tratada como já
respondida e o meio sumiu do trabalho inteiro — e com ele o funil de estilos.

Se o assunto é imagético e o banco aberto renderia — retrato histórico, obra em domínio
público, lugar, objeto — isso vale um segundo da etapa 1, não uma pergunta a mais aqui.

**7. Onde salvo o trabalho?**
→ Padrão: `./carrossel-<assunto>/`

**8. Quantos cards?** Recomende, com o motivo: 8 a 10 no Instagram (teto de 10), 9 a 10 se o
LinkedIn é o destino principal.

Isto **não é detalhe de produção, é pré-requisito da etapa 2**: uma direção que fecha bem em
6 cards vira parede em 10, e é olhando as três referências de arquétipo do estilo que se julga
se ela aguenta o número. Sem o número, não há o que julgar.

E **pergunte uma vez só.** Sabendo o número, a etapa 2 confirma — *"são sete, certo?"* — nunca
repete a pergunta do zero.

**9. Guardo isso pra não perguntar de novo?** Se sim, grave o arquivo. Se não, vale só nesta sessão.

---

## O arquivo

```markdown
# Perfil de carrossel

atualizado: AAAA-MM-DD

## Quem
- assina: Nome (@arroba)
- plataformas: Instagram (8–10 cards) · LinkedIn (PDF)
- público: uma frase
- voz: adjetivos · fonte da voz: caminho do arquivo, se houver

## Visual
- identidade fixa: sim/não · paleta: #HEX #HEX #HEX
- fontes de marca: Nome (arquivo.ttf) — acentos conferidos em AAAA-MM-DD
- assinatura: @arroba, só na capa e no fecho

## Produção
- geração de imagem: nenhuma | chave de API (qual) | conector (qual)
- verificado em: AAAA-MM-DD
- pasta padrão: ./carrossel-<assunto>/

## Pendências
- [CONFIRMAR] o que ficou por responder
```

## Regras do arquivo

- **Nunca grave segredo**: chave, token, URL com parâmetro de acesso. Registre o fato — `chave configurada em AAAA-MM-DD` — nunca o valor. Se o usuário mandar uma chave no chat, use, avise na hora que ela ficou exposta e diga para trocar depois.
- Registre **quando** verificou cada conector. Autorização expira, e perfil de três meses atrás não é evidência de que funciona hoje.
- Pergunta pulada vira `[CONFIRMAR]` explícito, nunca palpite disfarçado de fato.
