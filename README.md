# um-carrossel-por-favor

Skill para [Claude Code](https://claude.com/claude-code) que monta carrossel de feed com
arte-final: direção de arte, texto revisado e arquivos prontos para Instagram e LinkedIn.

O princípio que organiza tudo: **modelo de imagem erra letra, e erra o acento primeiro.** Toda
palavra que o leitor vai ler é renderizada em HTML/CSS e capturada em PNG. O gerador entra só
onde não há texto.

## Instalar

```bash
git clone https://github.com/drudif/um-carrossel-por-favor.git ~/.claude/skills/um-carrossel-por-favor
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
| 0 | Introdução | sobre o que é · o que você já tem · identidade fechada? · como assina e onde publica |
| 1 | Conexão | a skill **verifica** se há gerador ligado. Não havendo, oferece conectar e ajuda no passo a passo |
| 2 | Estilo | um dos **dois catálogos**, conforme a etapa 1. Sete estilos, três referências cada |
| 3 | Direção | aprovação, e a direção registrada em `DIRECAO.md` |
| 4 | Análise e texto | lê o seu material, **propõe o número de cards com o motivo**, e escreve ou organiza o texto |
| 5 | Anti-slop + imagens | a régua no texto e a imagem de cada card, as duas antes de você ver qualquer coisa |
| 6 | O mapa | por card: título, corpo e a imagem descrita. **É a única aprovação** |
| 7 | Produção | a arte, os PNGs, os PDFs |

**A conexão vem antes do estilo, e é de propósito.** É ela que decide qual catálogo você vê:
sem gerador, recomendar risografia seria vender o que não se entrega — a tinta riso existe para
cair sobre imagem. O catálogo A ordena pelo que aguenta o caminho sem gerador e diz, em laranja,
quais dois perdem qualidade ali. O catálogo B põe os sete em pé de igualdade.

Essa etapa já foi uma pergunta de três opções — *sem foto · banco · sob medida* — e sumia em toda
sessão de teste, sempre pelo meio. A saída não foi escrever melhor: foi **deixar de perguntar**.
A capacidade se verifica, o resto vira binário, e a escolha entre banco e desenho deixou de ser
pergunta abstrata para virar **referência dentro do catálogo**.

**Você pode mandar a sua própria referência** em vez de escolher pelo catálogo: de como a peça
parece dá para deduzir o que ela custa para fazer. A skill lê, diz de qual dos sete ela está mais
perto, e **confirma com você antes de seguir** — você pode ter gostado da paleta, da tipografia
ou da foto, e cada uma leva a um estilo diferente. Ela não vira um oitavo estilo.

**Você vê arte uma vez: pronta.** Não há preview intermediário — ele chegaria antes de a imagem
estar decidida, mostrando uma peça que talvez nem seja a que será produzida, com texto ainda
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
| 7 | Superminimal | branco, preto, e a imagem como bloco chapado — nenhum grafismo em volta |

Cada um traz paleta em hex, par tipográfico open-source com acentos pt-BR conferidos glifo a
glifo, entrelinha calculada a partir das métricas da fonte, e três referências visuais fixas.

## Imagem: de onde ela vem

**Desenho em código.** SVG e CSS, custo zero, e é o padrão para tudo o que é estrutura — grade,
diagrama, abstração de interface, ícone, tabela. Nos estilos de forma — brutalista, terminal,
neo-brutalismo — costuma ganhar de banco de imagem, porque nasce na paleta e carrega o conceito.

**Bancos abertos.** Dupe e Openverse, tratados na paleta do estilo. Não pede chave nem cadastro.
É o que faz o **superminimal** funcionar sem gerador: recorte limpo cai direto no branco.

**Fotos suas.** Entram **como elas são** — sem duotone, sem retícula, sem remapear paleta. Você
escolheu aquela foto porque é o seu produto, o seu trabalho, a pessoa certa. O tratamento só entra
se você pedir, e a skill pergunta uma vez, depois do estilo escolhido.

**Gerador conectado.** Higgsfield, Magnific, ou chave própria de Gemini/OpenAI. É o único caminho
em que a imagem responde ao seu assunto, e aqui roda o *laço do gabarito*: gera o card inteiro com
texto só para ter o que diagramar, mede a composição, acha a fonte open-source mais próxima com a
`regua-fonte.py`, refaz a imagem sem texto, e monta a tipografia real por cima. O gerador compõe
melhor do que escreve — o laço usa cada um no que ele faz bem.

Custo, dito antes de começar: **4 créditos por card no caminho feliz, 6 a 8 quando a geometria
precisa de segunda tentativa.**

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

Fontes: treze famílias do Google Fonts, **todas OFL**, embutidas no pacote com a licença de
cada uma. Para os sete estilos a skill não precisa de rede em momento nenhum.

MIT.
