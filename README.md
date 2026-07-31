# carrossel

Skill para [Claude Code](https://claude.com/claude-code) que produz carrossel de Instagram e LinkedIn com arte-final: PNGs 1080×1350 e um PDF sequencial.

O princípio que organiza tudo: **modelo de imagem erra letra, e erra o acento primeiro.** Toda palavra que o leitor vai ler é renderizada em HTML/CSS e capturada em PNG. O gerador de imagem entra só onde não há texto.

## Instalar

```bash
git clone <url> ~/.claude/skills/carrossel
```

Só isso. **Não depende de nenhuma outra skill estar instalada** — a régua anti-slop vem embutida, e as regras de conversa, de formato e de julgamento visual estão incorporadas. Ver [CREDITOS.md](CREDITOS.md).

Precisa de `python3` com `Pillow` e `fonttools`, e do Google Chrome, usado em modo headless para capturar. Costumam já estar na máquina.

## Usar

Peça em português:

- "faz um carrossel sobre X"
- "monta a arte desses cards pro Instagram"
- "quero um documento pro LinkedIn com esses seis projetos"

Seis etapas, com aprovação entre elas:

1. **Perfil** — quem assina, onde publica, com o que produz. Roda uma vez e fica salvo
2. **Estilo** — você vê as referências dos seis e escolhe; a skill renderiza capa e card do meio antes de você decidir
3. **Conteúdo** — gancho, tese, passos, fechamento
4. **Anti-slop** — o texto inteiro passa pela régua, obrigatoriamente
5. **Aprovação do texto** — limpo, e editável direto no `TEXTOS.md` se você preferir
6. **Produção** — PNGs, PDF, legenda e alt text

## Os seis estilos

Fechados, não infinitos. Cada um com paleta em hex, par tipográfico open-source com acentos pt-BR conferidos glifo a glifo, regra de material própria, e o cuidado que ele custou para descobrir. Três referências visuais cada, em `assets/referencias/`.

| Estilo | Fontes |
|---|---|
| Brutalista vetorial | Anton / IBM Plex Mono |
| Risografia com textura | Bricolage Grotesque / Newsreader |
| Janelas | Archivo Black / Space Mono |
| Mixed media / colagem | Bodoni Moda / Karla |
| Neo-brutalismo colorido | Chivo / Chivo Mono |
| Minimalista editorial quente | Fraunces / Work Sans |

Especificação completa em [references/estilos.md](references/estilos.md).

## Gerar imagem é opcional

**Quatro dos seis estilos ficam completos sem nenhum gerador** — a maior parte do que um card precisa é estrutura, e estrutura se desenha melhor em código do que se gera: sai na paleta exata, custa zero e não vaza dado nenhum.

Dois deles mudam de patamar com gerador conectado: a risografia, que existe para a tinta cair sobre imagem, e a colagem, cujo centro é o recorte fotográfico. Quem quiser conectar tem o passo a passo de chave de API (Gemini, OpenAI) e de conector (Higgsfield, Magnific) em [references/geradores.md](references/geradores.md), escrito para quem nunca conectou nada.

## Estrutura

```
SKILL.md                   fluxo, princípios, checagens, red flags
CREDITOS.md                o que foi incorporado, em que densidade e por quê
references/
  perfil.md                a conversa de setup, sem jargão
  estilos.md               os seis, com paleta, fonte, material e cuidado
  texto.md                 protocolo de conversa, estrutura e formato por plataforma
  visual.md                a régua de gosto, traduzida para peça estática
  grafismos.md             desenhar, capturar ou gerar — e as receitas de CSS
  geradores.md             chaves de API e conectores, passo a passo
  anti-slop.md             a régua, embutida
  anti-slop/               os arquivos da régua
  montagem.md              esqueleto, captura, área de segurança, PDF, armadilhas
assets/
  esqueleto.html           mecânica pronta, estética neutra
  baixar-fontes.sh         baixa o par do estilo, confere acentos, gera fonts.css
  exportar.sh              captura os PNGs, confere e monta o PDF
  referencias/             18 referências visuais, 3 por estilo
```

## Créditos

A régua anti-slop é a [`sprayantislop`](https://github.com/drudif/sprayantislop), de Fernando Drudi, embutida na íntegra, derivada de Zero-Lero (MIT, Vinicius Stanula) com o aviso preservado.

As regras de conversa, de formato por plataforma e de julgamento visual foram destiladas de `brainstorming`, `carousel-writer-sms`, `bencium-innovative-ux-designer` e `high-end-visual-design`. O que entrou de cada uma, o que ficou de fora e por quê está em [CREDITOS.md](CREDITOS.md) — inclusive dois conflitos entre elas, e como foram resolvidos.

O que é só desta skill: a ordem das seis etapas, os seis estilos fechados, a regra de desenhar antes de gerar, e a montagem em código.
