# carrossel

Skill para [Claude Code](https://claude.com/claude-code) que produz carrossel de Instagram e LinkedIn com arte-final: PNGs 1080×1350 e um PDF sequencial.

O princípio que organiza tudo: **modelo de imagem erra letra, e erra o acento primeiro.** Toda palavra que o leitor vai ler é renderizada em HTML/CSS e capturada em PNG. O gerador de imagem entra só onde não há texto.

## Instalar

```bash
git clone <url> ~/.claude/skills/carrossel
```

Depende de `python3` com `Pillow`, e do Google Chrome (usado em modo headless para capturar). Ambos costumam já estar na máquina.

Para a passada anti-slop obrigatória:

```bash
git clone https://github.com/drudif/sprayantislop ~/.claude/skills/sprayantislop
```

## Usar

Peça em português:

- "faz um carrossel sobre X"
- "monta a arte desses cards pro Instagram"
- "quero um documento pro LinkedIn com esses seis projetos"

A skill conduz seis etapas, com aprovação entre elas:

1. **Layout** — você anexa referências, descreve, ou pede cinco direções que discordam entre si
2. **Aprovação da direção** — com preview renderizado de capa e card do meio
3. **Conteúdo** — gancho, tese, passos, fechamento
4. **Anti-slop** — o texto inteiro passa pela `sprayantislop`
5. **Aprovação do texto** — com o registro do que foi cortado e por quê
6. **Produção** — PNGs e PDF

Na primeira vez ela faz uma entrevista de setup e grava `~/.claude/carrossel-perfil.md`. Nas seguintes, pergunta só o que mudou.

## Geradores de imagem

O padrão é o **Pollinations**: sem conta, sem chave, sem instalação. Funciona para qualquer pessoa no primeiro minuto.

Quem quiser mais qualidade pode conectar uma chave de API (Gemini ou OpenAI) ou um MCP (Higgsfield, Magnific). A skill ensina o passo a passo de cada um — ver [references/geradores.md](references/geradores.md).

E quem não quiser conectar nada continua tendo carrossel: a maior parte do que um card precisa é estrutura, e estrutura se desenha melhor em código do que se gera.

## Estrutura

```
SKILL.md                       fluxo, princípios, checagens, red flags
references/
  perfil.md                    a entrevista de setup e o arquivo de perfil
  direcoes-de-layout.md        como propor direções que divergem e o teste de escala
  grafismos.md                 desenhar, capturar ou gerar — e as receitas de CSS
  geradores.md                 Pollinations, chaves de API e MCPs, passo a passo
  anti-slop.md                 o que a passada derruba em carrossel
  montagem.md                  esqueleto, captura, área de segurança, PDF, armadilhas
assets/
  esqueleto.html               mecânica pronta, estética neutra
  exportar.sh                  captura os PNGs, confere e monta o PDF
```

## Créditos

Costura o que já existe em vez de reimplementar: `using-superpowers` e `brainstorming` para conduzir as decisões, `carousel-writer-sms` para a estrutura de texto por plataforma, [`sprayantislop`](https://github.com/drudif/sprayantislop) para a régua anti-slop, `bencium-innovative-ux-designer` e `frontend-design` para o julgamento visual, `abrasileirar-fonte` quando a fonte de display não tem `ç` nem `ã`.

O que é só desta skill: a ordem das seis etapas, a regra de desenhar antes de gerar, e a montagem em código.
