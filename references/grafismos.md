# Grafismos — desenhar, capturar ou gerar

Para cada card, decida a rota **antes** de produzir, e escreva a decisão no plano que o usuário aprova.

```
Dá para desenhar? (estrutura, interface, processo, dado, ícone, lista, comparação)
  └─ sim → DESENHAR em HTML/CSS/SVG            ← quase sempre cai aqui
  └─ não ↓
O valor do card está em PROVAR como a tela é de fato?
  └─ sim → CAPTURAR a tela real
  └─ não ↓
É retrato, cena, textura, ilustração, atmosfera?
  └─ sim → GERAR
  └─ não → provavelmente o card não precisa de grafismo
```

**Interface desenhada em blocos ganha de print com filtro aplicado.** Print filtrado parece print filtrado: o filtro não conserta a paleta errada, não tira o que não interessa e não protege o dado pessoal que está na tela. A abstração desenhada nasce na direção aprovada, mostra só o esqueleto que explica a ferramenta, e é a mesma linguagem dos outros cards. O print é a exceção — entra quando o card existe justamente para provar "é assim que a tela é".

Na dúvida, desenhe. Gerar custa uma rodada de prompt, uma de download, uma de recorte e quase sempre uma de refação. Um `<div>` custa uma linha e sai exatamente como você pediu.

---

## O grafismo é mudo

**Grafismo não gera texto.** Se você desenhou algo e precisou escrever um rótulo para ele se
explicar, o problema é o desenho — troque o desenho, não acrescente a legenda.

A checagem: cubra o texto do grafismo com a mão. Se o desenho continua dizendo a mesma coisa, o
texto era enfeite. A regra inteira, com os cinco sintomas vistos em produção, está em
[anti-slop.md](anti-slop.md#o-grafismo-não-gera-texto) — é a mesma auditoria de slot, aplicada
ao desenho.

## Desenhar — a rota padrão

A maior parte do que um carrossel precisa é geometria, e geometria é o que CSS faz melhor.

### Abstração de interface

Quando o card apresenta um app, uma versão **desenhada** da interface costuma bater o print: você controla o que aparece, o resultado nasce na paleta certa, e nenhum dado real vaza. Reduza a tela ao seu esqueleto — barra, pílulas de filtro, grade de cards, lista, campo de composição — e desenhe em blocos.

Duas telas diferentes precisam de **lógicas diferentes**, não da mesma grade com cor trocada. Um feed que esvazia é uma lista vertical com itens riscados; um catálogo é uma parede de cards. Se dois grafismos do mesmo carrossel se confundem, um dos dois está errado.

```html
<!-- lista que esvazia: os dois últimos já foram lidos -->
<div class="linha lido">
  <div class="marca"></div>
  <div class="corpo"><i style="width:38%"></i><i style="width:24%"></i>
    <div class="risco"></div></div>
  <div class="acao vazia"></div>
</div>
```

```css
.lido{opacity:.45}
.risco{position:absolute;left:18px;right:18px;top:50%;height:4px;background:var(--tinta)}
```

### Ícones que já existem no produto

Se o site ou app do usuário tem ícones próprios, **reaproveite o desenho**. Muitos são SVG de `<rect>` ou `<path>` direto no HTML — extraia e use:

```bash
python3 - <<'PY'
import re, json
s = open('caminho/index.html', encoding='utf-8').read()
out = []
for m in re.finditer(r'<svg class="ICONE"([^>]*)>(.*?)</svg>', s, re.S):
    vb = re.search(r'viewBox="([^"]+)"', m.group(1)).group(1)
    inner = re.sub(r'<!--.*?-->', '', m.group(2), flags=re.S)
    out.append({'vb': vb, 'd': re.sub(r'\s+', ' ', inner).strip()})
json.dump(out, open('icones.json','w'), ensure_ascii=False, indent=1)
print(len(out), 'ícones extraídos')
PY
```

No card, renderize com `fill:var(--tinta)` e `shape-rendering="crispEdges"` se forem pixel art. Ícone do próprio produto é a diferença entre um card genérico e um card que é daquela ferramenta.

### Textura de impressão

**Cor chapada em 1080×1350 lê como exportação de software.** Todo estilo que cita impressão — e são
quatro dos sete — precisa de uma camada de material permanente, mesmo os que parecem "limpos por
definição". O brutalista vetorial foi definido sem material e teve que ser revisto: vetor limpo
sobre tela grande não parece cartaz, parece PDF.

A dose é o que separa material de filtro: **grão fino em `.07`–`.10`, dente de papel largo em
`.04`–`.06`**, ambos em `multiply` e por cima de tudo, inclusive da tipografia — tinta impressa não
escolhe onde assentar. Acima de `.12` vira papel amassado.

**Essa dose é a EFETIVA, e não é o número que você escreve no `opacity` da camada.** As texturas
são SVG com `opacity` própria no `<rect>` de dentro, e as duas se multiplicam: o `.grao` do
esqueleto tem `opacity:.34` na camada e `.4` no rect, o que dá **`.136` de dose real**. Ler o
`.34` como se fosse a dose e "corrigir" para `.10` apaga o grão. Quando comparar com esta tabela,
multiplique.

E a textura entra **nos dois lugares**: na peça, em CSS, e no prompt da imagem gerada. Imagem lisa
dentro de card texturizado denuncia a colagem na hora.

Duas camadas, ambas discretas. Exagero vira papel amassado, que lê como filtro:

```css
/* retícula de meio-tom, sobre a arte — nunca sobre o texto */
.retic{position:absolute;inset:0;z-index:9;pointer-events:none;
  mix-blend-mode:multiply;opacity:.38;
  background-image:radial-gradient(circle,rgba(0,0,0,.6) 1.1px,transparent 1.3px);
  background-size:5px 5px}

/* fibra do papel: ruído alongado numa direção */
.fibra{position:absolute;inset:0;z-index:44;pointer-events:none;
  mix-blend-mode:multiply;opacity:.16;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='420' height='420'><filter id='f'><feTurbulence type='fractalNoise' baseFrequency='.012 .16' numOctaves='2'/><feColorMatrix type='saturate' values='0'/></filter><rect width='420' height='420' filter='url(%23f)' opacity='.55'/></svg>")}
```

A retícula fica **abaixo** do texto na ordem de empilhamento. Retícula sobre corpo de texto come a leitura, que é a prioridade 1.

### Duotone sobre imagem

Mapeia a luminância de qualquer imagem para duas tintas. Os `tableValues` são o componente RGB da tinta escura e da clara, em 0–1:

```html
<filter id="duo" color-interpolation-filters="sRGB">
  <feColorMatrix type="saturate" values="0"/>
  <feComponentTransfer>
    <feFuncR type="table" tableValues="0.169 0.949"/>  <!-- escura clara -->
    <feFuncG type="table" tableValues="0.247 0.929"/>
    <feFuncB type="table" tableValues="0.847 0.894"/>
  </feComponentTransfer>
</filter>
```

Para derivar de qualquer par:

```python
h = lambda c: [int(c[i:i+2],16)/255 for i in (1,3,5)]
tinta, papel = h('#2B3FD8'), h('#F2EDE4')
for canal, t, p in zip('RGB', tinta, papel):
    print(f'<feFuncR type="table" tableValues="{t:.3f} {p:.3f}"/>'.replace('FuncR', f'Func{canal}'))
```

**Se a imagem for escura**, o mapeamento joga tudo na tinta e o resultado vira uma mancha. Clareie antes: `filter:brightness(1.4) contrast(1.05) url(#duo)`.

### Erro de registro

Duas cópias da mesma coisa, uma deslocada, `mix-blend-mode:multiply`. O deslocamento **precisa escalar com o corpo do texto** — 8px sobre um título de 150px é sutil, sobre um de 60px cria letra fantasma e a palavra passa a ler errado:

```css
.tt s::before{content:attr(d);position:absolute;left:5px;top:4px;
              color:var(--acento);z-index:-1;opacity:.6}
.tt.xl s::before{left:8px;top:7px}    /* acima de 120px */
.tt.flat s::before{display:none}       /* onde precisa de leitura limpa */
```

Depois de aplicar, **leia a palavra em voz alta olhando o PNG**. Se você hesitou, o leitor no feed não vai nem tentar.

---

## Capturar — a exceção, não a regra

Só quando o card existe para **provar** como a tela é: um antes e depois, uma prova de que o produto existe, uma tela que o leitor vai reconhecer. Fora disso, desenhe.

As armadilhas técnicas estão em [montagem.md](montagem.md).

Antes de usar: **olhe o print procurando dado pessoal.** Nome, e-mail, cliente, valor, token. Tratamento de duotone abstrai bastante, mas título de card continua legível para quem ampliar — e ampliar é grátis. Avise o usuário e ofereça a versão desenhada, que quase sempre comunica melhor de qualquer forma.

---

## Gerar — o último recurso, com uma exceção fixa

**A exceção: o gerador conectado.** Aí não é mais último recurso — todos os cards nascem de
gabarito gerado, e a tipografia entra por cima em HTML. É o laço do gabarito, em
[geradores.md](geradores.md#o-laço-do-gabarito--quando-há-gerador-conectado). O iridescente
minimal é a única exceção: só recebe imagem a pedido do usuário.

Nos demais cards, só quando o card pede retrato, cena, textura ou ilustração. Como chamar cada gerador está em [geradores.md](geradores.md).

### A imagem nasce dentro do estilo, não é convertida para ele

**O erro:** gerar uma foto neutra em preto e branco e aplicar duotone por cima em CSS. O resultado é
uma foto tingida, não uma peça daquela direção. O tratamento fica sendo uma **camada**, e camada se
percebe: a fotografia continua tendo profundidade, meio-tom e luz fotográfica por baixo da tinta,
enquanto o resto do card é chapado.

**A regra:** a imagem é **função do estilo**, não uma foto que recebe o estilo no fim. A
especificação inteira entra no prompt, antes do assunto — paleta em hex com o papel de cada cor,
idioma visual, material, traço, e o que aquele estilo proíbe.

**Não escreva o prompt do zero.** Cada um dos sete estilos tem um **bloco de prompt pronto** em
[estilos.md](estilos.md), verificado. A montagem é sempre:

```
bloco do estilo  →  assunto (a metáfora)  →  cauda universal
```

**A ordem importa.** O modelo pesa mais o começo, e o que precisa dominar é o estilo. Começar pelo
assunto devolve foto de banco de imagem com a paleta sugerida por cima — que é exatamente o defeito.

E **as proibições diferem por estilo**: o brutalista proíbe meio-tom, o editorial quente exige
meio-tom. Um bloco genérico com a paleta trocada mata metade das direções.

| No prompt vai | Exemplo |
|---|---|
| A paleta em hex, com o papel de cada cor | `exactly three flat colours: paper #EDEAE3, ink #111111, signal red #E33420` |
| O nome do idioma visual | `VECTOR BRUTALISM illustration`, `two-plate screenprint`, `risograph print` |
| O material do estilo | `coarse halftone screen, visible plate misregistration, paper fibre` |
| O que o estilo proíbe | `no gradient, no midtone, no shading, no soft falloff` |
| Onde o acento aparece | `the signal red appears in exactly ONE element` |

**Consequência prática:** se a imagem já veio na paleta, **tire o duotone do CSS**. Ele achata o
acento — o vermelho que o gerador colocou num único elemento vira tinta escura, e você perde
exatamente o que fazia a imagem pertencer ao estilo.

Quando ainda vale converter em CSS: imagem que o usuário trouxe, print de tela, ou quando o estilo
pede a mesma foto em tratamentos diferentes ao longo do carrossel.

### O assunto da imagem vem do tema; o tratamento vem do estilo

Este é o erro mais fácil de cometer na geração, porque o resultado sai bonito e passa despercebido: você escolhe uma imagem que combina com a **direção visual** em vez de uma que fala do **assunto do carrossel**.

Um monitor antigo combina com um estilo que cita tela. Uma pilha de papel combina com um cartaz suíço. Ambos são decoração de estilo — nenhum diz o que o carrossel está falando.

**O teste da troca.** Pegue a imagem de uma direção e coloque na outra. Se continuar fazendo sentido, ela não era sobre o tema: era sobre o estilo. Imagem que fala do assunto não sobrevive à troca, porque ela pertence àquele conteúdo e não àquela paleta.

**Como montar o briefing, em três passos:**

1. **Nomeie o tema numa frase** — o que o carrossel está realmente dizendo. Não o formato, o argumento
2. **Ache a manifestação física dele** — que objeto, gesto, cena ou material existe no mundo que encarna esse argumento? É aqui que está o trabalho de direção
3. **Descreva essa manifestação na linguagem do estilo** — a mesma cena vira foto de flash duro no neo-brutalismo, nanquim com retícula no pop art, linha técnica no utilitário

O passo 2 é o que separa direção de arte de escolha de banco de imagem. Se você pulou direto do tema para "uma foto que combina", caiu na armadilha.

| Tema do carrossel | Manifestação fraca (estilo) | Manifestação forte (tema) |
|---|---|---|
| Skill que monta carrossel | monitor antigo, teclado | uma sequência de cards impressos saindo de uma máquina; uma mão passando por uma tira de quadros |
| IA generativa aplicada a criação | robô, cérebro, circuito | a mesma imagem repetida com variações mínimas; um objeto sendo remontado peça por peça |
| Ferramenta que remove fundo | tesoura, Photoshop | o retrato recortado sobre o xadrez de transparência |
| Feed que se organiza sozinho | pasta, ícone de arquivo | uma pilha bagunçada e a mesma pilha alinhada, lado a lado |

Repare que as fortes **mostram o que a coisa faz**, e as fracas mostram o assunto de que a coisa trata. A diferença é a mesma entre desenhar a interface do produto e desenhar barras decorativas.

**Um atalho que funciona quando o tema é o próprio formato:** represente o formato. Um carrossel é uma sequência — então uma tira de quadros, uma folha de contato, um baralho aberto em leque, uma esteira. O leitor reconhece a forma do que está segurando na mão.

### O prompt de um grafismo que vai receber tipografia por cima

- **Proíba texto explicitamente**, com redundância: `no text, no lettering, no words, no readable text anywhere`. O modelo insiste em escrever, e escreve errado.
- **Nomeie as tintas em hex** e diga quantas são
- **Peça composição frontal e plana** — `flat, frontal, no perspective, no depth of field`
- **Proíba a lista do slop**: `no gradient, no glow, no 3D, no drop shadow, no bokeh`
- **Deixe zona vazia** para a tipografia entrar: `generous empty area on the left third`
- **Fixe a seed** quando quiser reproduzir ou variar de forma controlada

### Depois de gerar, sempre

1. Baixe e **confira que o arquivo tem tamanho maior que zero**
2. **Abra e olhe** — o modelo entrega imagem errada com a mesma confiança da certa
3. **Recorte a moldura**: geradores costumam devolver o desenho dentro de uma margem branca ou de uma borda decorativa, que dentro do card vira caixa-dentro-de-caixa

```python
from PIL import Image
im = Image.open('gerado.png').convert('RGB'); w, h = im.size
m = int(w * .15)                                  # ajuste olhando
im.crop((m, m, w-m, h-m)).save('gerado-crop.png')
```

4. **Veio texto por acidente?** Não tente corrigir com prompt — recorte fora, ou cubra com um bloco de tinta chapada, que é peça legítima de composição impressa e custa uma linha de CSS
5. Se a imagem entra num card 1080×1350 e o gerador devolveu menos que isso, ela vai ser ampliada. Sob a retícula de meio-tom isso não aparece; em detalhe fino, aparece muito. É mais um motivo para desenhar.

---

## O alt text é o melhor briefing de imagem que existe na pasta

O alt text de cada card é escrito na etapa 4, **antes de a arte existir**, e descreve o que o
leitor deveria ver. Isso faz dele um briefing melhor do que qualquer assunto inventado na hora
de gerar: ele já passou pela entrevista, já está no assunto do card, e já foi aprovado.

> *"faixa laranja com o contorno de uma piscina vazia vista de cima — ralo no meio e escada
> num canto"*

Use como assunto da chapa ou do desenho. E **confira a volta**: se a arte divergiu, o alt text
virou descrição falsa de uma imagem real, que é pior do que alt text ausente. A checagem da
etapa 7 pede isso explicitamente.

## Banco de imagem — se buscar assunto, nunca estilo

Verificado contra três bancos. Pedir **estilo** devolve o que o rótulo significa para quem sobe
foto: `collage` devolve foto de scrapbook, `mixed media` devolve print de ícone de app,
`organic shapes` devolve a ilustração decorativa genérica que a régua anti-slop existe para
barrar. Pedir **assunto** funciona: `sequence` devolve fases da lua, `pushing buttons` devolve
painel industrial, `lever` devolve alavanca de câmbio.

**O estilo é nosso e entra no tratamento, depois.** A busca tem dois eixos: o assunto vem do
card, e a forma vem do `image_type` do banco — nada além disso.

### A escolha da foto depende do tratamento, não só do assunto

Alto contraste e silhueta alimentam o brutalista e matam o riso. Gradação alimenta o riso e
vira mancha no brutalista. A colagem aceita quase tudo, porque não converte a imagem: recorta.

### Foto em estilo chapado exige quantizar antes de mapear

Rampa contínua de 256 níveis serve riso e editorial. No brutalista reprova — o estilo é chapa
de cor, não transição. Quantize o cinza em **três degraus** antes de mapear na paleta, e a foto
vira serigrafia. Sem isso vira meio-tom e some.

### Acervo tem período

Não existe acervo público de forma vetorial chapada do século XX: no Art Institute são **275
obras em domínio público entre 1920 e 1975**, num acervo de 62 mil. O domínio público nos EUA
para em ~1930, e é justamente o período que brutalismo e neo-brutalismo citam.
Gravura acadêmica recolorida na paleta certa continua sendo gravura acadêmica — combina com a
paleta e briga com tudo o mais.

Para esses três estilos, **desenhar ganha do banco**. Foto, no entanto, funciona no brutalista
quando chapada em três degraus: o que falha ali é época, não fotografia.

### Ordem dos bancos

**Dupe** primeiro, pelo acervo — fotografia editorial contemporânea, luz dura, recorte limpo,
sem cara de banco. **Openverse** depois, que é a segura: filtro `cc0` e `pdm` no parâmetro.

Ressalva do Dupe, dita **antes** de usar: não é API pública. O endpoint é o backend que o site
chama (`POST /api/v1/content/search`, corpo `{"label": "..."}`), sem termos publicados para uso
programático, sem versionamento, e a licença é de quem subiu a foto — confira caso a caso.

### Desenho é autorado para a proporção do slot

Um desenho compartilhado entre estilos falha por construção: uma coluna vertical de seis
círculos numa faixa deitada desequilibra em todos. **Desenhe para a proporção do slot e para o
idioma do estilo** — grade de olhos 4×3 numa faixa deitada, chave deitada numa faixa deitada,
chapas sangrando em vez de retângulos flutuando dentro de uma caixa.
