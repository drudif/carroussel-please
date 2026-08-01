# carrossel

Skill para [Claude Code](https://claude.com/claude-code) que monta carrossel de feed com
arte-final: direção de arte, texto revisado e arquivos prontos para Instagram e LinkedIn.

O princípio que organiza tudo: **modelo de imagem erra letra, e erra o acento primeiro.** Toda
palavra que o leitor vai ler é renderizada em HTML/CSS e capturada em PNG. O gerador entra só
onde não há texto.

## Instalar

```bash
git clone https://github.com/drudif/carroussel-please.git ~/.claude/skills/carrossel
```

Depois é só pedir um carrossel no Claude Code — a skill se ativa sozinha.

**Não depende de nenhuma outra skill estar instalada.** A régua anti-slop vem embutida, e as
regras de conversa, formato e julgamento visual estão incorporadas. Ver [CREDITOS.md](CREDITOS.md).

Precisa de Google Chrome, usado em modo headless para capturar, e de Python 3:

```bash
pip3 install pillow fonttools
```

## O que ela entrega

| Destino | Arquivo |
|---|---|
| Instagram | PNG 1080×1350, um por card |
| LinkedIn | PDF 1080×1080, recortado da área de segurança dos mesmos PNGs |
| Stories | PNG 1080×1920, se pedirem |

Mais um `TEXTOS.md` com o texto de cada card, a legenda e o alt text. **A arte lê esse
arquivo.** Mudou uma palavra lá, avisa no chat e a arte se regenera — sem mexer em código, e
sem desmanchar a diagramação, porque o corpo se reajusta ao espaço já reservado em cada card.

## Como funciona

Oito etapas com trava entre elas. Refazer oito cards renderizados custa muito mais do que uma
pergunta.

| | Etapa | O que acontece |
|---|---|---|
| 0 | Perfil | quem assina, onde publica. Roda uma vez e fica salvo |
| 1 | Nível de imagem | gerador conectado, banco aberto, ou só desenho em código |
| 2 | Estilo | sete fixos, escolhidos pelas três referências visuais de cada um |
| 3 | Direção | aprovação, e a direção fica registrada em `DIRECAO.md` |
| 4 | Conteúdo | três perguntas, e o mapa dos cards antes de escrever o texto |
| 5 | Anti-slop | o texto passa por uma régua antes de você ver |
| 6 | Aprovação | você lê o que ficou e ajusta no `.md` |
| 7 | Produção | a arte, os PNGs, os PDFs |

**O nível de imagem vem antes do estilo, e é de propósito.** Cada nível favorece estilos
diferentes — terminal e iridescente nasceram sem foto, riso e colagem mudam de patamar com uma —,
então a escolha do nível já ordena a lista. Os sete continuam à vista; o que muda é por onde a
conversa começa.

**Você vê arte uma vez: pronta.** Não há preview intermediário — ele chegaria antes da etapa 2,
mostrando uma peça feita por um caminho que talvez nem seja o escolhido, com texto ainda
provisório. A escolha de estilo se faz nas 21 referências fixas que já vêm na skill.

## Os sete estilos

| | Estilo | Em uma linha |
|---|---|---|
| 1 | Brutalista vetorial | forma chapada de aresta dura sobre papel cru |
| 2 | Risografia com textura | duas tintas que se multiplicam, erro de registro |
| 3 | Terminal | paleta de editor de código sobre off-white, grade de caractere, muito vazio |
| 4 | Mixed media / colagem | camadas de origens diferentes, toda emenda à mostra |
| 5 | Neo-brutalismo colorido | contorno preto grosso e sombra dura sobre campo saturado |
| 6 | Minimalista editorial quente | duas colunas, geometria precisa, e muito vazio |
| 7 | Iridescente minimal | campo chapado que troca de cor a cada card, uma forma grande |

Cada um traz paleta em hex, par tipográfico open-source com acentos pt-BR conferidos glifo a
glifo, entrelinha calculada a partir das métricas da fonte, e três referências visuais fixas.

## Imagem: três níveis, e nenhum obrigatório

**Mínimo — só código.** SVG e CSS, custo zero, e é o padrão. Para os estilos de forma
(brutalista, terminal, neo-brutalismo, iridescente) costuma ganhar de banco de imagem, porque o desenho
nasce na paleta e carrega o conceito.

**Médio — bancos abertos.** Dupe e Openverse, tratados na paleta do estilo. Não pede chave nem
cadastro. Rende quando o tema é imagético; em tema abstrato, o desenho ainda ganha.

**Rico — gerador conectado.** MCP (Higgsfield, Magnific) ou chave própria de Gemini/OpenAI. É
o único nível em que a imagem responde ao briefing. Aqui a skill roda o *laço do gabarito*:
gera o card inteiro com texto só para ter o que diagramar, mede a composição, acha a fonte
open-source mais próxima, refaz a imagem sem texto usando a primeira como referência, e monta
a tipografia real por cima. O gerador compõe melhor do que escreve — o laço usa cada um no que
ele faz bem.

**A chave nunca é colada no chat.** Você exporta no terminal e diz "pronto".

## O que ela nunca faz

- Deixar palavra legível sair de gerador de imagem
- Pedir para colar chave no chat, ou gravar chave em arquivo
- Avançar de etapa sem resposta explícita nas travas
- Entregar sem ter aberto e olhado cada PNG
- Mandar você abrir uma pasta para ver o próprio trabalho

## Créditos

Traz embutido o `sprayantislop` (Fernando Drudi) sobre o Zero-Lero (MIT, Vinicius Stanula), e
destilados de `brainstorming`, `carousel-writer-sms`, `bencium-innovative-ux-designer` e
`high-end-visual-design`. Procedência completa em [CREDITOS.md](CREDITOS.md).

Fontes: Google Fonts, todas OFL ou Apache.

MIT.
