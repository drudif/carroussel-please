# Perfil — a conversa de setup

O perfil roda **uma vez**. Nos carrosséis seguintes, mostre um resumo de três linhas e pergunte
só o que mudou.

**Onde ele mora, nesta ordem:**

1. `~/.claude/carrossel-perfil.md` — o padrão, e vale para todos os trabalhos
2. `carrossel-perfil.md` **na pasta do trabalho** — quando não há `~/` gravável, que é o caso
   de ambiente em container. Vale só para aquele trabalho, e é melhor que não ter nenhum

Procure nos dois antes de perguntar qualquer coisa. Rodar o setup inteiro em cima de um perfil
que existe é a queixa nº 1 de quem testa a skill, e ela não some só porque o arquivo mudou de
lugar.

## Como conduzir

Uma pergunta por mensagem, seguindo o protocolo de [texto.md](texto.md). Toda pergunta pode ser pulada — pulada vira `[CONFIRMAR]` no arquivo, e você segue com o padrão indicado.

**Sem jargão.** Quem instala esta skill pode nunca ter aberto um terminal por vontade própria. Nada de "MCP", "chave de API", "área de segurança", "1080×1350" ou "duotone" nas perguntas. Esses termos existem no seu trabalho, não na conversa. Se um deles for inevitável, explique em uma frase e siga.

Agrupe em quatro rodadas curtas: **quem publica**, **o que já existe**, **como parece**, **com o
que produz**.

São onze perguntas. A de nível de imagem **não está aqui** — ela é a etapa 1, logo depois do
perfil.

**A rodada 2 é a que muda mais coisa depois.** Ela não é sobre gosto: é o inventário do que o
usuário traz pronto, e a resposta dela reescreve duas etapas adiante. Perguntar direção visual
antes de saber se o texto já existe é montar entrevista para quem não precisa dela.

---

## Rodada 1 — quem publica

**1. Quem assina?** Nome e arroba. Se houver mais de uma conta — pessoal e marca —, qual é a deste trabalho. Muda a voz inteira.

**2. Onde publica?** Instagram, LinkedIn, os dois, outro lugar. Define quantidade de cards e densidade de texto; a tabela está em [texto.md](texto.md).
→ Padrão: Instagram, 8 a 10 cards.

**3. Para quem?** Uma frase sobre quem lê. "Criativo de agência que não programa" e "dev sênior" produzem carrosséis opostos a partir do mesmo assunto.

**4. Qual a voz?** Dois ou três adjetivos e, se existir, um post que soou certo. Se o projeto tiver `.agents/social-media-context-sms.md`, **leia o arquivo e pule a pergunta** — a voz já está documentada lá.

---

## Rodada 2 — o que já existe

Duas perguntas, e são as que mais economizam rodada no fluxo inteiro. **Faça-as antes de
qualquer pergunta de direção visual.**

**5. O texto dos cards já existe?**

| resposta | o que muda |
|---|---|
| **não, é para você escrever** | fluxo normal: a etapa 4 faz a entrevista de três perguntas e propõe o mapa |
| **tenho um rascunho** | a etapa 4 vira edição, não entrevista. Leia, aponte o que falta para fechar o arco, e proponha só o delta |
| **está pronto e aprovado** | **a etapa 4 não roda.** Peça o arquivo ou o texto colado, ecoe o que leu, passe a régua anti-slop e leve direto para a aprovação da etapa 6 |

Tendo texto, peça no formato do `TEXTOS.md` **ou aceite como vier e converta você** — não faça o
usuário formatar nada. E **ecoe uma linha do que leu** antes de seguir: *"li 8 cards, assinatura
@fulano, assunto X"*. É o que separa um arquivo mandado por engano de oito cards do trabalho
errado.

**6. Você já tem as imagens, ou é para eu resolver isso?**

| resposta | o que muda |
|---|---|
| **é para você resolver** | fluxo normal: a etapa 1 pergunta como as imagens são feitas, com as três opções |
| **tenho as fotos** | elas são **material**, e vêm com os direitos de quem mandou. A etapa 1 continua acontecendo, mas só para o que faltar — e o tratamento continua vindo do estilo |

**Material não é referência**, e confundir os dois põe a foto do usuário dentro do card sem
ninguém ter decidido isso. Se ele mandar imagem sem dizer qual das duas é, pergunte — a
distinção está na [etapa 1 da SKILL.md](../SKILL.md#se-ele-trouxer-uma-referência-própria).

Uma coisa dita agora e não na entrega: **foto pronta não dispensa tratamento.** Ela entra na
paleta e no material do estilo escolhido como qualquer outra, senão lê como colagem de duas
peças. E se as fotos não cobrirem todos os cards, diga isso agora — o resto sai de banco ou de
desenho, e essa é uma decisão dele.

---

## Rodada 3 — como parece

**7. Sua marca tem cor e fonte fechadas?** Se tiver, elas vencem qualquer sugestão sua. Peça as cores e o nome das fontes.
→ Padrão: não tem; a direção nasce na etapa 2, dentro dos sete estilos.

Se ele tiver fonte de marca, confira o arquivo antes de prometer usá-la:

```bash
ls ~/Library/Fonts | sed 's/-.*//;s/\..*//' | sort -u
```

Fonte que não está instalada não entra. E fonte de marca precisa passar pela conferência de acentos da etapa 3 como qualquer outra.

**8. Tem logo ou assinatura para o rodapé?** Caminho do arquivo, ou só o arroba em texto.
→ Padrão: arroba em texto, e só na capa e no fecho.

*(Não pergunte se vai impulsionar. A área de segurança do corte quadrado é obrigatória sempre — post orgânico vira impulsionado depois sem ninguém refazer a arte.)*

---

## Rodada 4 — com o que produz

**Não pergunte de imagem nesta rodada, nem em versão binária** — *"quer gerar imagem ou desenhar
tudo?"*. Binário não distingue **banco aberto** de **desenho em código**, e toda vez que a
pergunta vazou para cá a etapa 1 foi tratada como já respondida: o meio sumiu do trabalho
inteiro, e com ele o funil de estilos. Ela é a etapa 1, com três opções.

**9. Onde salvo o trabalho?**
→ Padrão: `./carrossel-<assunto>/`

**10. Quantos cards?** Recomende, com o motivo: 8 a 10 no Instagram (teto de 10), 9 a 10 se o
LinkedIn é o destino principal.

Isto **não é detalhe de produção, é pré-requisito da etapa 2**: uma direção que fecha bem em
6 cards vira parede em 10, e é olhando as três referências de arquétipo do estilo que se julga
se ela aguenta o número. Sem o número, não há o que julgar.

E **pergunte uma vez só.** Sabendo o número, a etapa 2 confirma — *"são sete, certo?"* — nunca
repete a pergunta do zero.

**11. Guardo isso pra não perguntar de novo?** Se sim, grave o arquivo. Se não, vale só nesta sessão.

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

## Material que o usuário costuma trazer
- texto: escreve ele | manda rascunho | manda pronto
- imagens: nenhuma, a skill resolve | costuma mandar as fotos

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
