# Perfil — a entrevista de setup

O perfil mora em `~/.claude/carrossel-perfil.md` e roda **uma vez**. Nos carrosséis seguintes, mostre um resumo de três linhas e pergunte só o que mudou.

## Como conduzir

Uma pergunta por vez, seguindo `brainstorming`. Múltipla escolha sempre que der. Toda pergunta pode ser pulada — pulada vira `[CONFIRMAR]` no arquivo, e você segue com o padrão indicado.

Não faça as onze de uma vez. Agrupe em três rodadas curtas: **quem publica**, **como parece**, **com o que produz**.

---

## Rodada 1 — quem publica

**1. Quem assina?** Nome e handle. Se houver mais de uma conta (pessoal e marca), qual é a deste trabalho — muda a voz inteira.

**2. Onde publica?** Instagram, LinkedIn, ambos, outra. Define formato, número de cards e densidade de texto.
→ Padrão: Instagram 4:5, 8 a 10 cards.

**3. Para quem?** Uma frase sobre quem lê. "Criativo de agência que não programa" e "dev sênior" produzem carrosséis opostos a partir do mesmo assunto.

**4. Qual a voz?** Peça dois ou três adjetivos e, se existir, um exemplo de post que soou certo. Se o usuário já tem `.agents/social-media-context-sms.md` no projeto, **leia esse arquivo e pule esta pergunta** — a voz já está documentada lá.

---

## Rodada 2 — como parece

**5. Existe identidade visual fechada?** Paleta em hex, fontes, logo. Se sim, ela vence qualquer sugestão sua.
→ Padrão: sem identidade fixa; a direção nasce na etapa 1.

**6. Quais fontes estão instaladas?** Rode e mostre o resultado:

```bash
ls ~/Library/Fonts | sed 's/-.*//;s/\..*//' | sort -u
```

Fonte instalada é fonte que você pode usar sem baixar nada. Pergunte se alguma é obrigatória ou proibida.

**7. Tem logo ou assinatura para o rodapé?** Caminho do arquivo, ou o handle em texto.
→ Padrão: handle em texto.

*(Não pergunte se vai impulsionar. A área de segurança do corte 1:1 é obrigatória sempre — post orgânico vira impulsionado depois sem ninguém refazer a arte.)*

---

## Rodada 3 — com o que produz

**9. Quais geradores de imagem você tem?** Esta é a pergunta que destrava a etapa 6 — e é a que mais muda o resultado, então explique o ganho **em número** antes de pedir qualquer coisa:

> Sem conectar nada, eu tenho **9 estilos visuais** para te propor, todos desenhados em CSS. Conectando um gerador, sobem para **16** — os mesmos 9 mais 7 que precisam de imagem de verdade: retrato, cena, textura, colagem. Dá pra começar sem conectar e mudar de ideia depois.

Depois disso, as opções:

| Opção | O que exige | O que entrega |
|---|---|---|
| **Pollinations** (padrão) | nada — sem conta, sem chave | 686×858 no 4:5, determinístico por seed, grátis e ilimitado |
| **Higgsfield** via MCP | conta e conector autorizado | resolução alta, muitos modelos, consome créditos |
| **Magnific** via MCP | conta e conector autorizado | ampliação e recomposição de imagem existente |
| **Nenhum** | — | tudo desenhado em código; funciona para a maioria dos carrosséis |

Pollinations é o piso e sempre está disponível. Os outros são teto, não substituto — mesmo com Higgsfield conectado, a regra de desenhar antes de gerar continua valendo.

Se o usuário disser que tem Higgsfield ou Magnific, **confirme que o MCP responde** com uma chamada barata de leitura antes de contar com ele:

```
mcp__..._higs__balance      → devolve créditos e plano
```

MCP listado não é MCP autorizado. Se voltar erro de autenticação, avise que o conector precisa ser autorizado nas configurações e siga com Pollinations.

**10. Onde salvar o trabalho?** Pasta do projeto.
→ Padrão: `./carrossel-<assunto>/`

**11. Guardo este perfil?** Se sim, grave. Se não, use só nesta sessão.

---

## O arquivo

```markdown
# Perfil de carrossel

atualizado: AAAA-MM-DD

## Quem
- assina: Nome (@handle)
- plataformas: Instagram (4:5, 8–10 cards) · LinkedIn (PDF)
- público: uma frase
- voz: adjetivos · fonte da voz: caminho do arquivo, se houver

## Visual
- identidade fixa: sim/não · paleta: #HEX #HEX #HEX
- fontes disponíveis: Nome (arquivo.ttf), Nome (arquivo.ttf)
- fontes obrigatórias: · proibidas:
- assinatura de rodapé: @handle ou caminho do logo

## Produção
- gerador padrão: pollinations
- mcps disponíveis: higgsfield (verificado AAAA-MM-DD) · magnific (não)
- pasta padrão: ./carrossel-<assunto>/

## Pendências
- [CONFIRMAR] o que ficou por responder
```

## Regras do arquivo

- **Nunca grave segredo**: token, chave de API, URL com parâmetro de acesso. Se o usuário mandar uma, use na sessão e avise que ela precisa ser rotacionada depois.
- Registre **quando** você verificou cada MCP. Autorização expira, e um perfil de três meses atrás não é evidência de que funciona hoje.
- Pergunta pulada vira `[CONFIRMAR]` explícito, nunca um palpite disfarçado de fato.
