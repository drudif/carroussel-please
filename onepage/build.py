#!/usr/bin/env python3
"""Monta a one-page. Mobile primeiro, e sem um único arquivo de imagem:
a faixa do topo e os grafismos são SVG desenhado, com a retícula e o erro de
registro da risografia feitos em CSS. É o princípio da própria skill —
desenhar vem antes de gerar — aplicado à página que a explica.

Fontes: Anton comprimida 0.728 no título, como nos cards. Newsreader no corpo.
"""
import json

A = json.load(open("assets.json"))

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

FAIXA = "".join(peca(f) for f in (CIRCULO, QUADRADO, MEIA, BARRAS, ARCO, ANEL, TRI, CIRCULO))

HTML = """<title>Do zero ao primeiro carrossel</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
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

/* ── faixa do topo, desenhada ─────────────────────────────────────────── */
.faixa{{display:flex;gap:0;align-items:flex-end;overflow:hidden;
        height:clamp(120px,26vh,190px);padding-top:env(safe-area-inset-top)}}
.faixa .pc{{flex:0 0 auto;height:100%;width:auto;transform:translateY(14%)}}
.faixa .pc:nth-child(2n){{transform:translateY(6%) scale(.88)}}
.faixa .pc:nth-child(3n){{transform:translateY(20%) scale(1.06)}}

header .chapeu{{padding:24px 20px 0;max-width:660px;margin:0 auto}}
h1{{font-family:'T';font-weight:400;font-size:clamp(46px,13.5vw,92px);line-height:1.14;
    letter-spacing:.004em;margin:0;color:var(--azul);text-transform:uppercase;
    transform:scaleX(.728);transform-origin:left top;width:137.4%;white-space:nowrap}}
h1 em{{font-style:normal;color:var(--laranja)}}
.chapeu p{{margin:14px 0 0;font-size:17px;color:var(--fraco);max-width:32ch}}
.regua{{height:7px;background:var(--laranja);width:96px;margin:22px 0 0}}

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
  <div class="faixa">{faixa}</div>
  <div class="chapeu">
    <h1>Do zero ao<br><em>primeiro</em><br><em>carrossel</em></h1>
    <p>Um guia para quem nunca instalou nada parecido. Sem terminal, sem comando,
    sem palavra difícil.</p>
    <div class="regua"></div>
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
    github.com/drudif/carroussel-please e precisa ir para a pasta de skills do Claude.
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
  <span class="passo">Passo 3 · pode pular</span>
  <h2>Conectar um<br>gerador de imagem</h2>

  <p>A skill funciona sem isso: ela desenha as ilustrações sozinha, e em vários estilos o
  desenho fica melhor que foto. <strong>Só faça este passo se quiser ilustração feita sob
  medida para o seu assunto.</strong></p>

  <h3>Como conectar</h3>
  <ol>
    <li>No aplicativo, clique no botão <strong>+</strong> ao lado do campo de conversa</li>
    <li>Escolha <strong>Conectores</strong></li>
    <li>Procure o gerador que você quer, clique em conectar e entre na conta dele</li>
  </ol>
  <p>Só isso. Ele passa a aparecer sozinho quando a skill precisar de uma imagem.</p>

  <h3>Se você já tem conta</h3>
  <table class="tabela">
    <tr><td>Gemini</td><td>Sim, e é o mais fácil. A chave é grátis</td></tr>
    <tr><td>ChatGPT</td><td>A assinatura Plus <strong>não serve</strong>. O acesso automático é cobrado à parte</td></tr>
    <tr><td>Higgsfield</td><td>Sim, direto pelos conectores. Gasta crédito da assinatura</td></tr>
    <tr><td>Midjourney</td><td>Não dá para conectar. Mas você pode gerar por lá e entregar o arquivo</td></tr>
  </table>

  <div class="nota">
    <p><b>Nunca cole uma senha ou chave na conversa.</b> O que passa por ali fica registrado.
    Quando a skill precisar de uma, ela te ensina a guardar no seu computador, e você só
    responde “pronto”.</p>
  </div>
</section>

<div class="marca">{peca_alvo}</div>

<section>
  <span class="passo">Pronto</span>
  <h2>Agora<br>é só pedir</h2>
  <p>Abra o aplicativo, vá na aba Code, e peça o carrossel. Ele pergunta o assunto, mostra seis
  estilos para você escolher, revisa o texto e monta a arte.</p>
  <p>No fim você recebe as imagens do Instagram, o PDF do LinkedIn, e um arquivo chamado
  <strong>TEXTOS.md</strong>. Quer trocar uma palavra? Edita nesse arquivo, avisa na conversa,
  e a arte se refaz sozinha.</p>
</section>

<footer>
  <p>Ficou com dúvida em algum passo, ou quer me mostrar o que saiu? Me chama.</p>

  <nav class="contato">
    <a href="https://instagram.com/fdrudi">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.2c3.2 0 3.6 0 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.25.07 1.63.07 4.8s0 3.56-.07 4.81c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.25.06-1.63.07-4.85.07s-3.6 0-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.2 15.55 2.2 15.17 2.2 12s0-3.56.07-4.81c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.44 2.2 8.82 2.2 12 2.2m0 2.15c-3.13 0-3.5.01-4.73.07-.9.04-1.39.19-1.71.32-.43.17-.74.37-1.06.69-.32.32-.52.63-.69 1.06-.13.32-.28.81-.32 1.71-.06 1.23-.07 1.6-.07 4.73s.01 3.5.07 4.73c.4.9.19 1.39.32 1.71.17.43.37.74.69 1.06.32.32.63.52 1.06.69.32.13.81.28 1.71.32 1.23.06 1.6.07 4.73.07s3.5-.01 4.73-.07c.9-.04 1.39-.19 1.71-.32.43-.17.74-.37 1.06-.69.32-.32.52-.63.69-1.06.13-.32.28-.81.32-1.71.06-1.23.07-1.6.07-4.73s-.01-3.5-.07-4.73c-.04-.9-.19-1.39-.32-1.71a2.85 2.85 0 0 0-.69-1.06 2.85 2.85 0 0 0-1.06-.69c-.32-.13-.81-.28-1.71-.32-1.23-.06-1.6-.07-4.73-.07m0 3.65a5.99 5.99 0 1 1 0 11.99 5.99 5.99 0 0 1 0-11.99m0 9.88a3.89 3.89 0 1 0 0-7.78 3.89 3.89 0 0 0 0 7.78m7.63-10.12a1.4 1.4 0 1 1-2.8 0 1.4 1.4 0 0 1 2.8 0"/></svg>
      @fdrudi
    </a>
    <a href="https://linkedin.com/in/fdrudi">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5M3 9h4v12H3zm7 0h3.8v1.65h.05c.53-.95 1.83-1.95 3.77-1.95 4.03 0 4.78 2.5 4.78 5.75V21h-4v-5.6c0-1.34-.03-3.06-1.9-3.06-1.9 0-2.2 1.45-2.2 2.96V21h-4z"/></svg>
      /in/fdrudi
    </a>
    <a href="mailto:f.drudi@gmail.com">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M2.4 5.4h19.2v13.2H2.4zm1.9 1.5L12 12.3l7.7-5.4zm15.4 1.7-7.7 5.4-7.7-5.4v8.5h15.4z"/></svg>
      f.drudi@gmail.com
    </a>
  </nav>

  <p>Skill em <a href="https://github.com/drudif/carroussel-please">github.com/drudif/carroussel-please</a>.
  Esta página não usa nenhum arquivo de imagem: os grafismos são desenhados em código, como a
  skill faz com os cards.</p>
</footer>
</main>
"""

open("index.html", "w").write(HTML.format(
    faixa=FAIXA,
    peca_laptop=peca(QUADRADO), peca_pasta=peca(ARCO),
    peca_plugue=peca(ANEL), peca_alvo=peca(CHEQUE), **A))
print(len(open("index.html").read()) // 1024, "KB")
