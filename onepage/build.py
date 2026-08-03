#!/usr/bin/env python3
"""Monta a one-page. Mobile primeiro, e sem um único arquivo de imagem:
os grafismos são SVG desenhado, com a retícula e o erro de
registro da risografia feitos em CSS. É o princípio da própria skill —
desenhar vem antes de gerar — aplicado à página que a explica.

Fontes: Anton comprimida 0.728 no título, como nos cards. Newsreader no corpo.
"""
import base64
import json

A = json.load(open("assets.json"))

# o cavalo da capa, recortado do fundo no Higgsfield e embutido como os outros
# assets: a página continua um arquivo só, que abre offline e sem servidor.
CAVALO = base64.b64encode(open("gfx/cavalo.webp", "rb").read()).decode()

# os três selos, desenhados uma vez e usados no topo e no pé
def icone(d):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{d}"/></svg>'

IG = icone("M12 2.2c3.2 0 3.6 0 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.25.07 1.63.07 4.8s0 3.56-.07 4.81c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.25.06-1.63.07-4.85.07s-3.6 0-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.2 15.55 2.2 15.17 2.2 12s0-3.56.07-4.81c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.44 2.2 8.82 2.2 12 2.2m0 2.15c-3.13 0-3.5.01-4.73.07-.9.04-1.39.19-1.71.32-.43.17-.74.37-1.06.69-.32.32-.52.63-.69 1.06-.13.32-.28.81-.32 1.71-.06 1.23-.07 1.6-.07 4.73s.01 3.5.07 4.73c.4.9.19 1.39.32 1.71.17.43.37.74.69 1.06.32.32.63.52 1.06.69.32.13.81.28 1.71.32 1.23.06 1.6.07 4.73.07s3.5-.01 4.73-.07c.9-.04 1.39-.19 1.71-.32.43-.17.74-.37 1.06-.69.32-.32.52-.63.69-1.06.13-.32.28-.81.32-1.71.06-1.23.07-1.6.07-4.73s-.01-3.5-.07-4.73c-.04-.9-.19-1.39-.32-1.71a2.85 2.85 0 0 0-.69-1.06 2.85 2.85 0 0 0-1.06-.69c-.32-.13-.81-.28-1.71-.32-1.23-.06-1.6-.07-4.73-.07m0 3.65a5.99 5.99 0 1 1 0 11.99 5.99 5.99 0 0 1 0-11.99m0 9.88a3.89 3.89 0 1 0 0-7.78 3.89 3.89 0 0 0 0 7.78m7.63-10.12a1.4 1.4 0 1 1-2.8 0 1.4 1.4 0 0 1 2.8 0")
LI = icone("M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5M3 9h4v12H3zm7 0h3.8v1.65h.05c.53-.95 1.83-1.95 3.77-1.95 4.03 0 4.78 2.5 4.78 5.75V21h-4v-5.6c0-1.34-.03-3.06-1.9-3.06-1.9 0-2.2 1.45-2.2 2.96V21h-4z")
MAIL = icone("M2.4 5.4h19.2v13.2H2.4zm1.9 1.5L12 12.3l7.7-5.4zm15.4 1.7-7.7 5.4-7.7-5.4v8.5h15.4z")

# ── os grafismos, desenhados ────────────────────────────────────────────────
# vocabulário da risografia: chapa azul, chapa laranja deslocada, e o cruzamento
# escurecendo no multiply. Mesma lógica das duas chapas dos cards.
def peca(svg, w=120, h=120):
    return f'<svg class="pc" viewBox="0 0 {w} {h}" aria-hidden="true">{svg}</svg>'

AZUL, LAR = "#0078BF", "#FF6C2F"

def par(forma, cor=AZUL, fantasma=LAR, dx=8, dy=6):
    """Erro de registro: a chapa de baixo aparece só como franja na borda.
    Empilhar as duas inteiras com multiply escurece a peça toda e ela vira preta —
    na risografia o cruzamento acontece na sobra, não na área inteira."""
    return (f'<g transform="translate({dx},{dy})" fill="{fantasma}">{forma}</g>'
            f'<g fill="{cor}">{forma}</g>')

CIRCULO  = par('<circle cx="60" cy="60" r="52"/>', AZUL, LAR)
QUADRADO = par('<rect x="10" y="10" width="100" height="100"/>', LAR, AZUL)
MEIA     = par('<path d="M8 60a52 52 0 0 1 104 0z"/>', AZUL, LAR)
BARRAS   = par('<rect x="8" y="20" width="104" height="18"/><rect x="8" y="51" width="104" height="18"/><rect x="8" y="82" width="104" height="18"/>', LAR, AZUL)
ARCO     = par('<path d="M14 112V62a46 46 0 0 1 92 0v50H82V62a22 22 0 0 0-44 0v50z"/>', AZUL, LAR)
ANEL     = par('<path d="M60 8a52 52 0 1 0 .1 104A52 52 0 0 0 60 8m0 26a26 26 0 1 1-.1 52A26 26 0 0 1 60 34"/>', LAR, AZUL)
CHEQUE   = par('<path d="M12 62 46 96 110 22 96 10 46 70 24 50z"/>', LAR, AZUL)
TRI      = par('<path d="M60 10 112 110H8z"/>', AZUL, LAR)

# ── os dois cartazes da comparação ──────────────────────────────────────────
# Nem foto nem captura: os dois são desenho. O que separa um do outro é o que
# separa os dois caminhos de verdade — no de baixo a ilustração sangra, cruza o
# título e ocupa a folha; no de cima ela é um bloco que espera a sua vez.
def cartao(dentro):
    return (f'<div class="cartao"><svg viewBox="0 0 160 200" aria-hidden="true">'
            f'<rect width="160" height="200" fill="#FBF8F1"/>{dentro}</svg></div>')

def linhas(y, larguras, cor, h=12, x=14, gap=6):
    return "".join(f'<rect x="{x}" y="{y+i*(h+gap)}" width="{w}" height="{h}" fill="{cor}"/>'
                   for i, w in enumerate(larguras))

SO_CODIGO = (
    linhas(22, (118, 96, 62), AZUL)
    + f'<rect x="14" y="112" width="54" height="54" fill="{LAR}"/>'
    + f'<circle cx="112" cy="139" r="27" fill="none" stroke="{AZUL}" stroke-width="6"/>'
    + linhas(180, (78,), "#B4ADA1", h=5))

COM_GERADOR = (
    '<g style="mix-blend-mode:multiply">'
    f'<path d="M84 92c34-26 82-14 96 12v96H62z" fill="{LAR}"/>'
    f'<circle cx="128" cy="86" r="46" fill="{AZUL}"/>'
    f'<path d="M-8 128c40-38 92-30 118 6l16 66H-8z" fill="{AZUL}"/>'
    f'<path d="M22 200c0-40 26-70 60-72l24 72z" fill="{LAR}"/>'
    '</g>'
    + linhas(20, (128, 104, 74), AZUL)
    + f'<rect x="0" y="176" width="160" height="24" fill="#FBF8F1" opacity=".92"/>'
    + linhas(184, (96,), "#6B655C", h=5))


COMPARAR = (f'<div class="comparar">{cartao(SO_CODIGO)}{cartao(COM_GERADOR)}</div>'
            '<div class="par-legenda">'
            '<p><b>sem gerador</b>A ilustração é um bloco: forma, grade, diagrama. Nasce na '
            'paleta certa e custa zero — mas fica <em>ao lado</em> do texto.</p>'
            '<p><b>com gerador</b>O cartaz inteiro nasce composto: a imagem sangra pela borda, '
            'cruza o título e ocupa a folha. A letra entra por cima, limpa.</p>'
            '</div>')

HTML = """<meta charset="utf-8">
<title>O passo a passo da skill</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Guia para quem nunca instalou nada: instalar o Claude Code, instalar a skill de carrossel e ligar um gerador de imagem.">
<style>
@font-face{{font-family:'T';src:url(data:font/woff2;base64,{fTitulo}) format('woff2');font-weight:400;font-display:swap}}
@font-face{{font-family:'C';src:url(data:font/woff2;base64,{fCorpo}) format('woff2');font-weight:400;font-display:swap}}

:root{{
  --azul:#0078BF; --laranja:#FF6C2F;
  --fundo:#F4F0E6; --texto:#1A1713; --fraco:#6B655C; --linha:#DFD8CA; --caixa:#FBF8F1;
  --bloco:#141210; --bloco-txt:#EDE7DA; --mistura:multiply;
}}
@media (prefers-color-scheme:dark){{
  :root{{--fundo:#141210;--texto:#EDE7DA;--fraco:#968E81;--linha:#2C2823;--caixa:#1D1A16;
         --bloco:#0B0A09;--bloco-txt:#EDE7DA;--mistura:screen}}
}}
:root[data-theme="dark"]{{--fundo:#141210;--texto:#EDE7DA;--fraco:#968E81;--linha:#2C2823;--caixa:#1D1A16;--bloco:#0B0A09;--mistura:screen}}
:root[data-theme="light"]{{--fundo:#F4F0E6;--texto:#1A1713;--fraco:#6B655C;--linha:#DFD8CA;--caixa:#FBF8F1;--bloco:#141210;--mistura:multiply}}

*{{box-sizing:border-box}}
html{{-webkit-text-size-adjust:100%}}
body{{margin:0;background:var(--fundo);color:var(--texto);
     font:400 17px/1.6 'C',Georgia,serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
.env{{padding:0 20px;max-width:660px;margin:0 auto}}

/* retícula de meio-tom por cima de tudo: é o que faz a página ter a mesma
   superfície impressa dos cards, sem nenhuma imagem */
body::after{{content:"";position:fixed;inset:0;z-index:99;pointer-events:none;
  mix-blend-mode:var(--mistura);opacity:.055;
  background-image:radial-gradient(#000 26%,transparent 27%);background-size:4px 4px}}

header .chapeu{{padding:calc(30px + env(safe-area-inset-top)) 20px 0;max-width:660px;
                margin:0 auto;position:relative}}

/* O cavalo é a abertura, e o título passa por cima dele: as patas traseiras saem
   de trás da letra. Quem define a altura do palco é a imagem, em fluxo normal —
   o título é absoluto por cima. Assim não há número mágico de altura para
   desmanchar quando a folha muda de largura. */
.palco{{position:relative}}
.cavalo{{display:block;width:min(86%,600px);height:auto;margin:0 -20px 0 auto;
         position:relative;z-index:1;pointer-events:none;user-select:none}}
.palco h1{{position:absolute;left:0;top:40%;z-index:3}}
h1{{font-family:'T';font-weight:400;font-size:clamp(46px,13.5vw,92px);line-height:1.14;
    letter-spacing:.004em;margin:0;color:var(--azul);text-transform:uppercase;
    transform:scaleX(.728);transform-origin:left top;width:137.4%;white-space:nowrap;
    /* sombra chapada, sem borrão: é o deslocamento de chapa da risografia, e é
       ela que descola a letra da ilustração sem precisar de caixa atrás.
       O x sai maior porque o scaleX(.728) encolhe o deslocamento junto. */
    text-shadow:9px 7px 0 #FFFFFF}}
h1 em{{font-style:normal;color:var(--laranja)}}

/* a sobrancelha: o endereço da skill, primeira coisa da folha */
.sobrancelha{{display:inline-block;font-family:'C';font-size:11.5px;letter-spacing:.12em;
  text-transform:uppercase;color:var(--laranja);text-decoration:none;
  border-bottom:2px solid var(--laranja);padding-bottom:4px;margin:0 0 16px;
  position:relative;z-index:3}}
.sobrancelha:hover,.sobrancelha:focus-visible{{color:var(--texto);border-color:var(--texto)}}
.chapeu p{{margin:14px 0 0;font-size:17px;color:var(--fraco);max-width:32ch}}
.regua{{height:7px;background:var(--laranja);width:96px;margin:22px 0 0}}
/* quem assina, no alto: os dois perfis onde o carrossel é publicado */
.assina{{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 0;position:relative;z-index:3}}
.assina a{{display:inline-flex;align-items:center;gap:7px;text-decoration:none;
  font-family:'C';font-size:14px;color:var(--texto);border:2px solid var(--azul);
  padding:6px 11px;box-shadow:3px 3px 0 var(--laranja);
  transition:transform .12s,box-shadow .12s}}
.assina a:hover,.assina a:focus-visible{{transform:translate(1px,1px);box-shadow:2px 2px 0 var(--laranja)}}
.assina svg{{width:15px;height:15px;fill:var(--azul);flex:0 0 auto}}
@media (prefers-reduced-motion:reduce){{.assina a{{transition:none}}}}

/* ── conteúdo ─────────────────────────────────────────────────────────── */
section{{margin-top:58px}}
h2{{font-family:'T';font-weight:400;font-size:clamp(34px,9vw,52px);line-height:1.14;
    letter-spacing:.004em;margin:-.1em 0 12px;color:var(--azul);text-transform:uppercase;
    transform:scaleX(.728);transform-origin:left top;width:137.4%}}
.passo{{display:block;font-family:'C';font-size:12px;letter-spacing:.22em;text-transform:uppercase;
        color:var(--laranja);margin-bottom:8px}}
h3{{font-family:'T';font-weight:400;font-size:25px;line-height:1.14;margin:32px 0 8px;letter-spacing:.01em;
    text-transform:uppercase;transform:scaleX(.728);transform-origin:left top;width:137.4%}}
p{{margin:0 0 18px}}
a{{color:var(--azul);text-underline-offset:3px}}
strong{{font-weight:400;box-shadow:inset 0 -.48em 0 #FF6C2F33}}
ol,ul{{margin:0 0 18px;padding-left:20px}} li{{margin-bottom:10px}}

.copiar{{background:var(--bloco);color:var(--bloco-txt);border-radius:10px;margin:18px 0;
         padding:16px 18px;font-size:16px;line-height:1.55;overflow-wrap:anywhere}}
.copiar .quem{{display:block;font-family:'C';font-size:11.5px;letter-spacing:.2em;
               text-transform:uppercase;color:var(--laranja);margin-bottom:9px}}

.nota{{background:var(--caixa);border-left:6px solid var(--laranja);padding:16px 18px;margin:22px 0}}
.nota b{{font-weight:400;color:var(--laranja)}}
.aviso{{background:var(--caixa);border-left:6px solid var(--azul);padding:16px 18px;margin:22px 0}}
.nota p:last-child,.aviso p:last-child{{margin-bottom:0}}

/* grafismo entre seções: uma peça só, grande, sangrando */
.marca{{display:flex;justify-content:center;margin:44px 0 40px}}
.marca .pc{{height:110px;width:auto}}

/* os dois cartazes lado a lado — desenhados, como tudo aqui */
.comparar{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:26px 0 12px}}
.cartao{{position:relative;border:2px solid var(--linha);background:#FBF8F1;overflow:hidden}}
.cartao svg{{display:block;width:100%;height:auto}}
.par-legenda{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:26px}}
.par-legenda p{{margin:0;font-size:14px;line-height:1.5;color:var(--fraco)}}
.par-legenda b{{display:block;width:max-content;margin:0 0 7px;font-family:'C';font-weight:400;
                font-size:11px;letter-spacing:.18em;text-transform:uppercase;
                color:#FBF8F1;background:var(--azul);padding:4px 8px}}
.par-legenda em{{font-style:italic;color:var(--texto)}}

/* uma rota de conexão: cabeçalho com o custo e o tempo à mostra */
.rota{{border-top:3px solid var(--azul);padding-top:14px;margin:34px 0 0}}
.rota .etiqueta{{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;
                 font-family:'C';font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;
                 color:var(--fraco);margin-bottom:2px}}
.rota .etiqueta .b{{color:var(--laranja)}}
.rota h3{{margin-top:6px}}

.tabela{{width:100%;border-collapse:collapse;margin:20px 0;font-size:15.5px}}
.tabela td{{padding:11px 0;border-bottom:1px solid var(--linha);vertical-align:top}}
.tabela td:first-child{{font-family:'T';font-weight:400;text-transform:uppercase;font-size:17px;
                        padding-right:16px;white-space:nowrap;color:var(--texto);letter-spacing:.01em}}

footer{{margin-top:66px;border-top:1px solid var(--linha);padding:26px 0 40px;
        color:var(--fraco);font-size:14.5px}}
footer p{{margin:0 0 22px}}
.contato{{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 24px}}
.contato a{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;
  font-family:'C';font-size:15px;color:var(--texto);
  border:2px solid var(--azul);padding:9px 15px;
  box-shadow:4px 4px 0 var(--laranja);transition:transform .12s,box-shadow .12s}}
.contato a:hover,.contato a:focus-visible{{transform:translate(2px,2px);box-shadow:2px 2px 0 var(--laranja)}}
.contato svg{{width:17px;height:17px;fill:var(--azul);flex:0 0 auto}}
@media (prefers-reduced-motion:reduce){{.contato a{{transition:none}}}}

@media (min-width:720px){{
  body{{font-size:18px}}
  section{{margin-top:78px}}
  .marca .pc{{height:130px}}
}}
</style>

<header>
  <div class="chapeu">
    <a class="sobrancelha" href="https://github.com/drudif/um-carrossel-por-favor">github.com/drudif/um-carrossel-por-favor</a>
    <div class="palco">
      <img class="cavalo" src="data:image/webp;base64,{cavalo}" alt="" aria-hidden="true">
      <h1>O passo<br>a passo<br><em>da skill</em></h1>
    </div>
    <p>Um guia para quem tá começando no Claude Code.</p>
    <div class="regua"></div>
    <nav class="assina">
      <a href="https://instagram.com/fdrudi">{ig} @fdrudi</a>
      <a href="https://linkedin.com/in/fdrudi">{li} /in/fdrudi</a>
    </nav>
  </div>
</header>

<main class="env">

<section>
  <span class="passo">Antes de começar</span>
  <h2>O que você<br>vai ter no fim</h2>
  <p>Um programa no seu computador que conversa com você por escrito. Você pede
  “faz um carrossel sobre tal coisa”, ele faz algumas perguntas, e devolve as imagens
  prontas para postar no Instagram e no LinkedIn.</p>

  <div class="aviso">
    <p><b>Uma coisa antes de tudo:</b> o plano gratuito do Claude <strong>não dá acesso a
    isso</strong>. É preciso ter um plano pago. Se você está no gratuito, o programa vai abrir
    mas pedir para você assinar — e não é erro seu.</p>
  </div>

  <p>São três passos, e nenhum passa de dez minutos.</p>
</section>

<div class="marca">{peca_laptop}</div>

<section>
  <span class="passo">Passo 1</span>
  <h2>Instalar<br>o aplicativo</h2>

  <p>Entre em <a href="https://claude.ai/download">claude.ai/download</a> e baixe o aplicativo
  para o seu computador. Instale como você instalaria qualquer outro programa: abre o arquivo
  baixado e segue.</p>

  <p>Abra o aplicativo e <strong>entre com a sua conta Claude</strong>.</p>

  <h3>Onde clicar</h3>
  <ol>
    <li>No topo da janela tem três abas. Clique em <strong>Code</strong></li>
    <li>Escolha <strong>Local</strong> — significa trabalhar com os arquivos do seu computador</li>
    <li>Clique em <strong>Select folder</strong> e escolha uma pasta para guardar os carrosséis.
    Pode criar uma nova, chamada “carrosseis”, na sua área de trabalho</li>
  </ol>

  <p>Pronto. A partir daqui é só escrever no campo de texto, como numa conversa.</p>

  <div class="nota">
    <p><b>Se você usa Windows:</b> o aplicativo precisa de um programa chamado Git para funcionar
    com arquivos locais. Baixe em <a href="https://git-scm.com/downloads/win">git-scm.com</a>,
    instale clicando em “próximo” até o fim, e reabra o Claude. No Mac isso já vem pronto.</p>
  </div>
</section>

<div class="marca">{peca_pasta}</div>

<section>
  <span class="passo">Passo 2</span>
  <h2>Instalar<br>a skill</h2>

  <p>Aqui está a parte boa: <strong>você não instala nada.</strong> Você pede, e ele faz.
  Copie o texto abaixo e cole no campo de conversa:</p>

  <div class="copiar">
    <span class="quem">cole isto na conversa</span>
    Instala a skill de carrossel pra mim. Ela está em
    github.com/drudif/um-carrossel-por-favor e precisa ir para a pasta de skills do Claude.
    Depois confere se instalou e me avisa.
  </div>

  <p>Ele vai pedir sua permissão para rodar umas coisas — clique em aceitar. Quando terminar,
  vai dizer que está pronto.</p>

  <h3>Se faltar algo</h3>
  <p>A skill usa o Google Chrome e duas peças do Python para montar as imagens. Se ele avisar
  que falta alguma, responda assim:</p>

  <div class="copiar">
    <span class="quem">cole isto na conversa</span>
    Instala o que estiver faltando pra skill funcionar e me avisa quando puder testar.
  </div>

  <h3>Testar</h3>
  <div class="copiar">
    <span class="quem">cole isto na conversa</span>
    faz um carrossel sobre como eu organizo minha semana
  </div>

  <p>Se ele começar a perguntar onde você publica e como assina os posts, deu certo.</p>
</section>

<div class="marca">{peca_plugue}</div>

<section>
  <span class="passo">Passo 3 · dá para pular, mas leia antes</span>
  <h2>Ligar um<br>gerador de imagem</h2>

  <p>Este é o passo que <strong>mais muda o resultado</strong>, e é o único que a maioria das
  pessoas pula sem saber o que está deixando na mesa. Vale ler antes de decidir.</p>

  <p>Sem gerador, a skill desenha as ilustrações ela mesma, em código. Isso é bom de verdade —
  em quatro dos sete estilos o desenho fica <em>melhor</em> que foto, porque nasce exatamente na
  paleta e mostra só o que interessa. O que ele não faz é retrato, cena e textura.</p>

  <p>Com gerador ligado, muda a natureza do card:</p>

  {comparar}

  <p>A imagem passa a responder <strong>ao seu assunto</strong>, em vez de ser a forma abstrata
  que dava para desenhar. Uma boa imagem é o que mais segura audiência no seu carrossel.</p>

  <div class="aviso">
    <p><b>Não tem gerador e nem quer ter?</b> Então mande <strong>fotos suas</strong> — do
    celular, do seu trabalho, ou de banco gratuito: <a href="https://unsplash.com">unsplash.com</a>,
    <a href="https://pexels.com">pexels.com</a>, <a href="https://pixabay.com">pixabay.com</a>.
    Confira a licença de cada uma, porque “gratuito” quer dizer coisas diferentes em cada site.
    Suas fotos entram <strong>como vieram</strong>, sem filtro, a menos que você peça.</p>
  </div>

  <h3>São dois caminhos, e eles são diferentes</h3>
  <p>Um é uma autorização, o outro é uma chave. Escolha um só — não precisa dos dois.</p>

  <div class="rota">
    <div class="etiqueta"><span class="b">Caminho 1</span> · dois minutos · nenhuma senha</div>
    <h3>Conector</h3>
    <p>Um conector é uma autorização: você dá ao Claude permissão de usar a <em>sua</em> conta
    de um serviço, clicando em aceitar numa janela — como quando um site pede para entrar com
    o Google. Nenhuma senha passa pela conversa.</p>

    <ol>
      <li>No aplicativo, clique no <strong>+</strong> ao lado do campo onde você escreve</li>
      <li>Escolha <strong>Conectores</strong></li>
      <li>Procure o serviço na lista, clique em <strong>Conectar</strong></li>
      <li>Abre uma janela do serviço pedindo para você entrar e autorizar. Aceite</li>
      <li>A janela fecha sozinha. Acabou</li>
    </ol>

    <p>O melhor deles para carrossel é o <strong>Higgsfield</strong>: é o que compõe cartaz
    melhor, e é assinatura mensal com créditos inclusos. <strong>Custo por card: 4 créditos</strong>
    no caminho normal, 6 a 8 quando a composição precisa de segunda tentativa. Um carrossel de
    oito cards fica na faixa de 32 a 50 créditos — vale conferir seu saldo antes de começar.</p>

    <div class="copiar">
      <span class="quem">para conferir se ligou, cole na conversa</span>
      Confere se o Higgsfield está conectado aqui e me diz quantos créditos eu tenho.
    </div>

    <p>Se ele responder com o número de créditos, está ligado. <strong>Aparecer na lista não é
    o mesmo que estar autorizado</strong>, e é por isso que se confere assim.</p>
  </div>

  <div class="rota">
    <div class="etiqueta"><span class="b">Caminho 2</span> · cinco minutos · uma chave</div>
    <h3>Chave de API</h3>
    <p>Uma chave de API é um código comprido que a sua conta gera para um programa usar no seu
    lugar. <strong>Trate como senha:</strong> quem tiver a sua chave gasta na sua conta. Você
    cria uma vez, guarda no seu computador, e não pensa mais nisso.</p>

    <h3>Gemini — o mais fácil, e a chave é grátis</h3>
    <ol>
      <li>Abra <a href="https://aistudio.google.com/apikey">aistudio.google.com/apikey</a> e
      entre com a sua conta do Google</li>
      <li>Clique em <strong>Create API key</strong> — o botão azul no canto direito</li>
      <li>Ele pede um projeto. Se você não tiver nenhum, escolha criar; o nome não importa</li>
      <li>Aparece um código começando com <strong>AIza…</strong> Copie e guarde por um minuto:
      depois de fechar a janela ele não aparece de novo</li>
    </ol>
    <p>Criar a chave é grátis e não pede cartão. <strong>Gerar imagem costuma ser cobrado</strong>,
    em centavos por imagem — o preço está na própria página, e vale olhar antes de rodar um
    carrossel inteiro.</p>

    <h3>OpenAI — se você preferir o modelo do ChatGPT</h3>
    <ol>
      <li>Abra <a href="https://platform.openai.com/api-keys">platform.openai.com/api-keys</a></li>
      <li><strong>Create new secret key</strong>, dê um nome qualquer, copie. Começa com
      <strong>sk-…</strong> e <strong>só aparece uma vez</strong></li>
      <li>Vá em <strong>Settings → Billing</strong> e ponha crédito. Sem crédito a chave existe,
      mas toda tentativa falha com erro</li>
    </ol>
    <div class="nota">
      <p><b>Pagar o ChatGPT Plus não serve para isso.</b> A assinatura e a API são duas contas
      separadas, cobradas à parte — é a confusão mais cara deste passo, e a razão de muita gente
      achar que já tem acesso quando não tem.</p>
    </div>

    <h3>Onde colar a chave</h3>
    <p><strong>Não é na conversa.</strong> A chave mora num arquivo de configuração do seu
    computador, e quem põe ela lá é você, num programa chamado Terminal — o Claude escreve a
    linha pronta, você só troca o pedaço da chave e cola. É o único comando deste guia inteiro,
    e existe justamente para a chave <em>não</em> passar pelo chat.</p>

    <div class="copiar">
      <span class="quem">cole isto na conversa, com a chave já copiada</span>
      Criei uma chave de API do Gemini. Me ensina a guardar ela no meu computador,
      passo a passo, sem eu precisar colar a chave aqui na conversa.
    </div>

    <p>Ele te dá a linha, você cola no Terminal, troca a parte escrita
    <em>cole-a-chave-aqui</em> pela sua chave, dá Enter, e responde só <strong>“pronto”</strong>
    na conversa. A skill anota que existe chave configurada e a data — nunca o valor.</p>
  </div>

  <h3>Se você já tem conta em algum</h3>
  <table class="tabela">
    <tr><td>Gemini</td><td><strong>Sim</strong> — chave de API, grátis de criar, cobrada por imagem. É o mais fácil de todos</td></tr>
    <tr><td>Higgsfield</td><td><strong>Sim</strong> — conector, dois cliques. Gasta os créditos da sua assinatura. É o que compõe cartaz melhor</td></tr>
    <tr><td>Magnific</td><td><strong>Sim</strong> — conector. Mas serve para ampliar e recompor imagem que já existe, não para criar do zero</td></tr>
    <tr><td>ChatGPT</td><td><strong>A assinatura Plus não serve.</strong> Dá para usar a API da OpenAI, que é cobrada à parte</td></tr>
    <tr><td>Midjourney</td><td><strong>Não conecta.</strong> Mas você pode gerar por lá e entregar o arquivo pronto na conversa</td></tr>
  </table>

  <div class="nota">
    <p><b>Nunca cole uma senha ou chave na conversa.</b> O que passa por ali fica registrado.
    Se colar sem querer, não tem drama: volte no site onde criou, apague aquela chave e crie
    outra. Leva um minuto e a antiga deixa de funcionar na hora.</p>
  </div>

  <div class="aviso">
    <p><b>Travou em algum passo?</b> Não recomece do início — descreva na conversa o que você
    está vendo na tela e siga dali. E se cansar, pule: dá para ligar depois, a qualquer momento,
    e o carrossel sai do mesmo jeito, com o desenho no lugar da foto.</p>
  </div>
</section>

<div class="marca">{peca_alvo}</div>

<section>
  <span class="passo">Pronto</span>
  <h2>Agora<br>é só pedir</h2>
  <p>Abra o aplicativo, vá na aba Code, e peça o carrossel. Ele pergunta o assunto, mostra
  <strong>sete estilos</strong> para você escolher — com três exemplos de cada, para você
  escolher olhando e não lendo —, revisa o texto e monta a arte.</p>
  <p>No fim você recebe as imagens do Instagram, o PDF do LinkedIn, e um arquivo chamado
  <strong>TEXTOS.md</strong>. Quer trocar uma palavra? Edita nesse arquivo, avisa na conversa,
  e a arte se refaz sozinha.</p>
</section>

<footer>
  <p>Ficou com dúvida em algum passo, ou quer me mostrar o que saiu? Me chama.</p>

  <nav class="contato">
    <a href="https://instagram.com/fdrudi">{ig} @fdrudi</a>
    <a href="https://linkedin.com/in/fdrudi">{li} /in/fdrudi</a>
    <a href="mailto:f.drudi@gmail.com">{mail} f.drudi@gmail.com</a>
  </nav>

  <p>Skill em <a href="https://github.com/drudif/um-carrossel-por-favor">github.com/drudif/um-carrossel-por-favor</a>.
  Os grafismos desta página são desenhados em código, como a skill faz com os cards — a única
  imagem é o cavalo, recortado da capa de um carrossel feito com ela.</p>
</footer>
</main>
"""

open("index.html", "w").write(HTML.format(
    comparar=COMPARAR, cavalo=CAVALO, ig=IG, li=LI, mail=MAIL,
    peca_laptop=peca(QUADRADO), peca_pasta=peca(ARCO),
    peca_plugue=peca(ANEL), peca_alvo=peca(CHEQUE), **A))
print(len(open("index.html").read()) // 1024, "KB")
