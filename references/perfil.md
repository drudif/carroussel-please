# Perfil — a conversa de setup

O perfil mora em `~/.claude/carrossel-perfil.md` e roda **uma vez**. Nos carrosséis seguintes, mostre um resumo de três linhas e pergunte só o que mudou.

## Como conduzir

Uma pergunta por mensagem, seguindo o protocolo de [texto.md](texto.md). Toda pergunta pode ser pulada — pulada vira `[CONFIRMAR]` no arquivo, e você segue com o padrão indicado.

**Sem jargão.** Quem instala esta skill pode nunca ter aberto um terminal por vontade própria. Nada de "MCP", "chave de API", "área de segurança", "1080×1350" ou "duotone" nas perguntas. Esses termos existem no seu trabalho, não na conversa. Se um deles for inevitável, explique em uma frase e siga.

Agrupe em três rodadas curtas: **quem publica**, **como parece**, **com o que produz**.

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
→ Padrão: não tem; a direção nasce na etapa 1, dentro dos seis estilos.

Se ele tiver fonte de marca, confira o arquivo antes de prometer usá-la:

```bash
ls ~/Library/Fonts | sed 's/-.*//;s/\..*//' | sort -u
```

Fonte que não está instalada não entra. E fonte de marca precisa passar pela conferência de acentos da etapa 2 como qualquer outra.

**6. Tem logo ou assinatura para o rodapé?** Caminho do arquivo, ou só o arroba em texto.
→ Padrão: arroba em texto, e só na capa e no fecho.

*(Não pergunte se vai impulsionar. A área de segurança do corte quadrado é obrigatória sempre — post orgânico vira impulsionado depois sem ninguém refazer a arte.)*

---

## Rodada 3 — com o que produz

**7. Você quer que eu gere imagens, ou desenho tudo?**

Esta é a única pergunta técnica do setup, então faça o custo e o ganho aparecerem em português antes de pedir qualquer coisa:

> Duas formas de fazer as ilustrações dos cards. **Desenhando em código**, que é o padrão: sai exatamente na sua paleta, custa zero e serve para grade, diagrama, ícone, tela de app. Ou **gerando imagem**, para o que não se desenha — retrato, cena, textura, colagem. Gerar exige conectar uma ferramenta, uma vez, uns dois minutos. Dá pra começar sem conectar nada e mudar de ideia no meio.

O que muda de fato, e é isso que você diz:

- **A capa passa a ter imagem sempre.** Com gerador conectado, isso vira regra fixa — e a capa é o card que decide se os outros sete serão vistos
- **Dois dos seis estilos mudam de patamar**: a risografia, que existe para a tinta cair sobre imagem, e a colagem, cujo centro é o recorte fotográfico. Os outros quatro ficam completos sem nada
- **O texto não muda em nada.** Toda palavra que o leitor vai ler é desenhada pelo navegador, com ou sem gerador. Nenhum modelo de imagem escreve português confiável, e o acento é onde ele erra primeiro

As opções, e como conectar cada uma, estão em [geradores.md](geradores.md). Se ele disser que já tem um conector, **confirme que responde** antes de contar com ele — ferramenta que aparece na lista não é ferramenta autorizada.

**8. Onde salvo o trabalho?**
→ Padrão: `./carrossel-<assunto>/`

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
