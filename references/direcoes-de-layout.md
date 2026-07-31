# Direções de layout

A etapa 1 tem três entradas — referência anexada, descrição em palavras, ou "não sei por onde começar". As três terminam no mesmo lugar: uma direção escrita, com paleta em hex e fonte com nome real, que passou no teste de escala.

## Quando o usuário anexa referências

Não elogie a referência. **Extraia dela.** Devolva, para cada imagem:

- **Paleta em hex** — três a cinco cores, com o papel de cada uma (fundo, tinta principal, acento, texto)
- **Tipografia** — que classe é (grotesca, serifada de texto, mono, display), contraste entre título e corpo, caixa e entreletra
- **Lógica de grade** — quantas colunas, se a grade aparece, se o conteúdo sangra
- **Textura** — retícula, grão, papel, ruído, nenhuma
- **O que dá para reproduzir em CSS e o que não dá** — esta linha é a mais útil e a que ninguém escreve

Depois diga, em uma frase, **o que na referência é o que o usuário realmente quer** — quase sempre é uma coisa só, e o resto é acompanhamento. Confirme com ele antes de produzir.

## Quando o usuário descreve em palavras

Traduza adjetivo em especificação. "Clean" não é decisão; `#FFFFFF` com uma tinta e escala tipográfica de 3 níveis é. Devolva a tradução e pergunte se é isso, antes de renderizar.

Se a descrição couber em mais de uma direção muito diferente, **não escolha por ele** — produza duas e mostre.

## Quando ele não sabe por onde começar

Proponha **cinco direções que discordam entre si**. Divergir é o requisito; cinco variações da mesma ideia fazem o usuário escolher entre nada.

Duas direções divergem de verdade quando mudam em **pelo menos três** destes eixos:

| Eixo | Extremos |
|---|---|
| Tipografia | display dominante ↔ tipografia de serviço, discreta |
| Cor | monocromático ↔ duas tintas saturadas ↔ paleta cheia |
| Grade | visível e rígida ↔ invisível ↔ deliberadamente quebrada |
| Textura | limpa e digital ↔ impressa e suja |
| Imagem | full-bleed dominante ↔ contida em placa ↔ ausente |
| Densidade | um elemento por card ↔ card de ficha técnica |

Territórios que costumam divergir bem — use como provocação, não como lista para copiar: tipográfica monocromática · risografia de duas chapas com registro fora · grade suíça com um acento · analógica suja, xerox ou colagem · ficha técnica e tabela de dados · editorial de revista com foto grande.

**Não repita a mesma cinco em todo projeto.** Se você propôs riso da última vez, essa vira a menos interessante desta.

## O teste de escala

Uma direção só passa se você conseguir escrever, antes de recomendar:

1. O que acontece na **capa**
2. O que acontece num card do **meio**
3. O que acontece no card de **índice ou lista**, se houver
4. O que acontece no **CTA**
5. **O que muda a cada swipe** — se nada muda, o carrossel é uma parede

Se você não conseguiu escrever os cinco, a direção não passou. Direção linda que só funciona na capa quebra no card 5, e aí já foram oito cards renderizados.

## O preview

Renderize, para cada direção, **a capa e um card do meio**. Só a capa esconde justamente o problema que o teste de escala procura.

Diga sempre, junto do preview: *o texto aqui é provisório e a decisão é de direção visual*. Sem esse aviso o usuário aprova a direção pensando no texto, e depois pede para mudar o texto sem entender que a direção vai junto.

## O arquivo da direção

Ao fechar, grave `DIRECAO.md` na pasta do trabalho:

```markdown
# Direção: <nome curto>

## Paleta
| cor | hex | uso |
|---|---|---|
| papel | #F2EDE4 | fundo de tudo |
| tinta | #2B3FD8 | títulos, regras, grafismos |
| acento | #FF4A1C | rótulos, marcação, uma peça por card |

## Tipografia
- Display: Nome (arquivo.ttf) — pesos disponíveis: 1
- Corrido: Nome (arquivo.ttf)
- Escala: título 112px · corpo 33px · rótulo 20px (sobre 1080 de largura)
- Acentos pt-BR conferidos: sim/não

## Grade
12 colunas, margem 78px, grade visível a 10% de opacidade

## Comportamento por card
- capa: ...
- projeto/passo: ...
- índice: ...
- CTA: ...

## Teste de escala
O que muda a cada swipe: ...
```

Fonte com **um peso só**: hierarquia por tamanho e cor, nunca `font-weight:bold`. O navegador engorda o desenho artificialmente e a letra sai suja no PNG.
