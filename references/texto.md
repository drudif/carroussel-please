# Texto — conversa, estrutura e plataforma

Este arquivo condensa duas skills que a `carrossel` não pode depender de encontrar instaladas: o protocolo de conversa da **`brainstorming`** e as regras de formato da **`carousel-writer-sms`**. Procedência e o que ficou de fora estão em [CREDITOS.md](../CREDITOS.md).

> **Se alguma das duas estiver instalada nesta máquina, use a instalada** — ela é a fonte, esta é a cópia de trabalho.

---

## O protocolo de conversa

Vale nas etapas 0, 1, 3 e 5 — em toda pergunta que a skill faz.

0. **Antes de perguntar, tente parsear.** O usuário responde em bloco — *"com mcp higsfield layout risografia"* fecha duas etapas de uma vez. Se a mensagem respondeu N etapas, ecoe as N decisões numa frase afirmativa e peça o aceite. A regra 1 vale para o que **falta**, e aplicá-la ao que já foi dito é o mesmo defeito que ela existe para evitar.
1. **Uma pergunta por mensagem.** Bloco de cinco perguntas volta com três respondidas e duas perdidas.
2. **Múltipla escolha sempre que couber.** Escolher entre opções nomeadas é mais rápido e mais preciso que redigir do zero. Ponha a sua recomendação em primeiro e diga que é a sua recomendação.
3. **Aprovação a cada bloco, não no fim.** Cada etapa tem uma trava. Nada avança sem resposta explícita.
4. **Pergunta pulada vira `[CONFIRMAR]` explícito**, nunca um palpite disfarçado de fato.
5. **Nada de produção antes da aprovação.** Vale para os cards de arte e para o texto — refazer oito cards renderizados custa muito mais do que uma pergunta.

O que **não** veio da `brainstorming`: o documento de spec, a passagem para `writing-plans`, o companion visual em navegador. Um carrossel não tem arquitetura para documentar; a spec dele é o `DIRECAO.md` e o `TEXTOS.md`.

---

## Quando o texto já vem pronto

A rodada 2 do perfil pergunta isso antes de qualquer coisa de direção, e a resposta manda na
etapa 4. **Texto pronto não passa pela entrevista** — devolver ao usuário um mapa do que ele
mesmo escreveu queima uma rodada e soa a desatenção.

O que continua valendo em cima do texto dele:

- **A estrutura das quatro zonas abaixo vira diagnóstico, não fôrma.** Leia procurando o que
  falta — costuma faltar contexto, que é o card que mais some por parecer dispensável — e
  **aponte em uma linha** em vez de reescrever
- **A régua anti-slop roda**, com a ressalva que já está lá: guia de voz da marca vence qualquer
  regra daqui, e o que parece fórmula pode ser voz deliberada. Na dúvida, aponte e deixe ele
  decidir
- **O alt text quase nunca vem junto.** Escreva você, um por card

## A estrutura, em quatro zonas

Vale para qualquer plataforma. O que muda de uma para outra é a quantidade, não a forma.

**Capa.** Um título que sustenta a promessa e uma linha que a torna concreta. Duas a três linhas, no máximo. O teste: se este card fosse um post sozinho, ele ganharia atenção? Se não, os outros sete não serão vistos.

**Contexto.** Uma ou duas frases enquadrando o problema. É a ponte entre o gancho e o valor, e é o card que mais some por parecer dispensável — sem ele o leitor não sabe por que deveria se importar.

**Corpo.** Uma ideia por card, sem exceção — **essa** não cede. O tamanho do corpo, sim, e
generosamente: ver a seção abaixo.

**Fecho.** Uma frase que fecha a tese e uma ação concreta. Não desperdice o último card com "obrigado por ler".

### O corpo dos cards do meio: 25 palavras era pouco

**A régua era 25 palavras, e ela estava estragando o carrossel.** Cortar tudo para caber nesse
teto mata justamente o que precisa de **linearidade** para ser entendido — um raciocínio com dois
passos, uma causa e sua consequência, um "por isso" que depende do que veio antes. Picado em
sentenças de 25 palavras, o argumento vira tópico solto e o leitor não reconstrói o fio.

**E resumo forçado é slop.** Não é uma opinião de gosto: é a mesma falha da família inteira —
uma fôrma aplicada independentemente do conteúdo. Texto espremido para caber numa contagem fica
telegráfico e sem conectivo, que é exatamente o "slop ao contrário" que o
[anti-slop.md](anti-slop.md#os-limites) já avisa.

**O teto passa a ser físico, e ele foi medido.** No quadrado vivo de 924×924, corpo a 34px com
entrelinha 1,45, título de duas linhas a 104px e o pé reservado:

| o card tem | cabe |
|---|---|
| título de 2 linhas + zona de grafismo preservada | **56 palavras**, 8 linhas |
| título um pouco menor, 92px, com grafismo | **64 palavras**, 9 linhas |
| **sem grafismo** — só título, corpo e pé | **80 palavras**, 11 linhas |

**Esta tabela vale para `assets/esqueleto.html` — a zona de grafismo ali é CSS nosso, com altura
que a gente decide.** Com conector ligado, quem monta o vão é o gerador, não este arquivo: o
`medir-chapa.py` do laço (ver [geradores.md](geradores.md#o-laço-do-gabarito--quando-há-gerador-conectado))
devolveu vãos de **350 a 500px** num carrossel real — abaixo dos ~550–620px que esta tabela supõe
para título de 2 linhas + 55 palavras. Escrever para o teto desta tabela e só depois medir a
chapa é escrever para um vão que pode não existir naquele card: **com conector, o teto de cada
card sai do `alt` medido daquele card, não desta tabela.** A régua está em geradores.md — a
menor entre o comprimento de linha do gabarito e a altura do vão manda, e ela pode dar bem menos
que 55 palavras num card e mais em outro. Escreva as 55–65 como ponto de partida do texto, mas
corte para o vão real depois de medir — nunca o contrário.

Então a régua de trabalho, **para o esqueleto sem conector**:

- **capa e fecho ficam curtos.** Uma promessa e um fechamento não ganham nada com volume
- **os cards do meio carregam o argumento, e podem ir a 55–65 palavras** com grafismo, ou até
  **80 sem ele.** O grafismo é o que cede primeiro na hierarquia da skill — um card que precisa
  explicar tem direito de abrir mão dele
- **quem diz que chegou no limite é o `?medir=1`**, não a contagem: ele mede a altura real com a
  fonte real. Contar palavra é estimativa; medir é medida
- **e não encha para preencher.** O teto subiu, o piso não existe: se a ideia se resolve em duas
  linhas, ela se resolve em duas linhas. Volume por volume é o defeito espelhado do resumo forçado

**Quando dividir em dois cards, então?** Quando são **duas ideias**, não quando o texto ficou
longo. A pergunta certa é *"o leitor entende a segunda parte sem a primeira?"* — se entende, são
dois cards; se não entende, é um card só e ele precisa do espaço.

---

## Regras de escrita

**Os títulos fazem o trabalho pesado.** As pessoas passam o dedo. Se o título de cada card não comunica o ponto sozinho, reescreva o título — não acrescente corpo.

**Escreva a capa por último.** Só depois de saber o que o carrossel entrega dá para escrever a promessa que ele cumpre.

**Cada card precisa de um motivo para o próximo existir.** Um número que continua, um ponto que abre, uma consequência não dita. Mas *sem* transformar isso em fórmula — se todos os cards terminarem em suspense, o carrossel vira anúncio de teleshopping. Um ou dois bastam.

**Assimetria deliberada em pelo menos um card.** Oito cards com a mesma estrutura e o mesmo comprimento leem como template preenchido, que é a definição de slop em peça diagramada.

**Formatação com intenção:** `→` marca direção ou contraste; lista numerada marca processo; negrito puxa o olho para o que importa. Três recursos, não sete.

---

## Por plataforma

| | Instagram | LinkedIn | TikTok (fotos) | Pinterest | Facebook |
|---|---|---|---|---|---|
| **Formato** | carrossel nativo | PDF, documento nativo | post de imagens | Idea Pin | multifoto |
| **Quantidade** | 8–10 (teto de 10) | 7–12, ideal 9–10 | 6–12 | 6–10 páginas | 5–8 |
| **Proporção** | 1080×1350 (4:5) | **1080×1080 (1:1)** | 1080×1920 (9:16) | 1080×1920 | 1:1 |
| **Densidade** | média — o teto medido, sem encher | alta, e é onde o teto de 80 palavras mais vale | mínima — até 6 palavras por card | média, guiada por palavra-chave | média |
| **Legenda** | gancho nos 125 primeiros caracteres | gancho + 2 parágrafos; **link só no comentário** | até 150 caracteres | descrição com palavra-chave | conversacional, 200–500 |
| **Hashtags** | 3 a 10 | 3 a 5 | 3 a 5 | ignoradas — use palavra-chave no texto | 1 a 3 |
| **Sinal que importa** | salvar e enviar | comentário e reação | reassistir | salvar | comentário |

**Instagram:** peça salvamento e envio de forma explícita — são os sinais que a plataforma pesa. Alt text por card, na configuração de acessibilidade.

**LinkedIn:** o feed é largo e reduz o documento, e é onde o teto de 80 palavras mais vale. O piso de corpo — **34px** — está na [etapa 7](../SKILL.md#formatos).

**TikTok:** o texto sobre a imagem *é* o gancho, não a legenda. Áudio em alta amplia a distribuição mesmo em post de fotos.

**Pinterest:** cada página é uma superfície de busca própria. A primeira é a capa de palavra-chave.

**Legenda × texto do card.** Os cards carregam o valor; a legenda arma o swipe e fecha com a ação. Escreva as duas juntas e **não repita** — legenda que reproduz os cards desperdiça os dois.

---

## As perguntas da etapa 4 são três

E são as três da [SKILL.md](../SKILL.md#etapa-4--análise-e-texto) — tese, fechamento, dado próprio.
**Não são cinco.** O gancho da capa e os passos card a card já foram perguntas aqui, e saíram:
os dois se respondem melhor no **mapa dos cards** que você propõe depois, porque o usuário julga
um roteiro pronto mais rápido do que redige um do zero. Perguntar os passos um a um é fazer o
trabalho da skill virar formulário.

Onde ficam os links entrou na tabela por plataforma acima, que é onde a resposta já está.

Depois do mapa aprovado, o texto é escrito — e antes de mostrar qualquer coisa, roda a etapa 5.
Sem exceção.
