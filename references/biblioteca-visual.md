# Biblioteca visual

Dezoito referências em `assets/referencias/`. Cada verbete descreve o **mecanismo de composição**, não a aparência — aparência se copia e sai igual, mecanismo se aplica a qualquer assunto.

## A regra que organiza a biblioteca

**O que você pode propor depende do que o usuário tem.** Confira no perfil, na etapa 0, antes de montar as cinco direções:

| O usuário tem | Você propõe |
|---|---|
| Só código, sem gerador | **os 9 do nível CSS** — nenhum depende de imagem |
| Pollinations, chave de API ou MCP | os 9 do nível CSS **mais** os 7 do nível imagem |

Não proponha uma direção do nível imagem para quem não tem gerador. Ela vai ser aprovada, e você trava na etapa 6.

## A trava contra as cinco iguais

**Antes de renderizar, escreva qual é o mecanismo de cada uma das cinco.** Se dois se repetirem, troque antes de gastar render. O defeito clássico é propor cinco direções que trocam de cor e continuam sendo a mesma composição: tipografia grande no topo, um fio, corpo abaixo, elemento no pé.

## As fontes

Todas open-source, do Google Fonts, licenças OFL ou Apache. Nenhuma sai do acervo pessoal de ninguém — o carrossel precisa ser reproduzível por quem instalar a skill.

```bash
assets/baixar-fontes.sh utilitario     # baixa o par, confere acentos, gera fonts.css
assets/baixar-fontes.sh --listar       # lista os estilos
```

O script grava `fonts.css` com as duas faces em base64, sob os nomes `Titulo` e `Corpo`. Ele confere `ÁÀÂÃÉÊÍÓÔÕÚÜÇ` em cada uma e avisa se faltar glifo. **As dezesseis famílias abaixo foram verificadas: todas têm acento pt-BR completo.**

---

# Nível CSS — funcionam sem nenhum gerador

## 22 · BAUHAUS — [22-bauhaus.png](../assets/referencias/22-bauhaus.png)
**Mecanismo:** geometria primária em escalas muito contrastantes — um círculo enorme, um quadrado médio, um retângulo pequeno sangrando a borda — organizada por peso visual, com uma linha fina atravessando o card inteiro para amarrar.
**Paleta:** papel `#EFEBE2` · preto `#111` · vermelho `#E01B1B` · azul `#2B54C8` · amarelo `#F2C200`
**Fontes:** `bauhaus` → Archivo Black / Archivo
**Escala:** as formas mudam de tamanho e posição a cada card; a tipografia fica ancorada. O ritmo é automático.
**Cuidado:** círculo grande demais rouba o card do texto. Deixe-o sangrar em vez de crescer.

## 23 · BRUTALISMO — [23-brutalismo.png](../assets/referencias/23-brutalismo.png)
**Mecanismo:** tipografia monoespaçada crua sobre blocos sólidos, arestas duras, zero arredondamento. Retícula grossa como imagem. Elementos de interface deixados no estado bruto — botão padrão, caixa de seleção, borda de 1px.
**Paleta:** papel `#F2F0EA` · uma tinta saturada (`#3B33C4` ou `#E8336E`) · preto
**Fontes:** `brutalismo` → Space Mono 700 / Space Mono 400
**Escala:** ótima. O bloco de cor muda de tamanho e posição; a tipografia mono mantém o sistema.

## 27 · POP ART — [27-popart.png](../assets/referencias/27-popart.png)
**Mecanismo:** contorno preto grosso em tudo, cores primárias chapadas, retícula Ben-Day visível, e o conteúdo dividido em quadros como página de quadrinhos. Balão de fala carrega a frase.
**Paleta:** amarelo `#FFD400` · vermelho `#E4002B` · azul `#0057B8` · preto · branco
**Fontes:** `popart` → Bungee / Archivo
**Escala:** os quadros mudam de arranjo a cada card. O balão de fala pode carregar o texto do card, virando grafismo e informação ao mesmo tempo.

## 38 · UTILITÁRIO — [38-utilitario.png](../assets/referencias/38-utilitario.png)
**Mecanismo:** grade de manual técnico. Números grandes como marcadores, réguas e cotas, campos rotulados, tabela de dados no pé. Zero decoração — cada elemento existe porque informa.
**Paleta:** off-white `#F4F3F0` · preto · um acento funcional (`#E85A2A` ou `#4A6B4F`) · cinzas
**Fontes:** `utilitario` → IBM Plex Sans 700 / IBM Plex Mono
**Escala:** excelente, e é a mais fácil de todas. O número do passo é o ritmo.
**Por que serve bem a assunto técnico:** ele explica um processo sem precisar ilustrar nada.

## 39 · MID-CENTURY — [39-midcentury.png](../assets/referencias/39-midcentury.png)
**Mecanismo:** formas orgânicas recortadas — bumerangue, folha, olho, semicírculo — em cores terrosas quentes, sobrepostas sem grade rígida, com muito espaço respirando ao redor.
**Paleta:** creme `#F5EFE0` · laranja queimado `#D96B2B` · azul `#2E5EA8` · verde-oliva `#7A8C4A` · preto
**Fontes:** `midcentury` → Poppins 700 / DM Sans
**Escala:** boa. As formas se recombinam a cada card como um alfabeto.

## 50 · NEO-BRUTALISMO — [50-neobrutalismo.png](../assets/referencias/50-neobrutalismo.png)
**Mecanismo:** blocos com borda preta grossa e sombra dura deslocada, sobre fundo de cor saturada com grade milimetrada. Componentes de interface — botão, balão, janela, estrela — usados como elementos gráficos. Assimetria deliberada.
**Paleta:** lavanda `#C9A7F5` · rosa `#F5A7C9` · azul `#7FB2F0` · amarelo `#F5D547` · preto
**Fontes:** `neobrutalismo` → Space Grotesk 700 / Space Grotesk 400
**Escala:** excelente. Os blocos mudam de posição e tamanho; a sombra dura mantém a identidade.
**Cuidado:** é o estilo mais usado em post de design hoje. Distintivo hoje, genérico em seis meses.

## 51 · SUÍÇO — [51-suico.jpeg](../assets/referencias/51-suico.jpeg)
**Mecanismo:** grade de colunas **visível como fio fino**, e o conteúdo obedecendo a ela de forma ostensiva. Título gigantesco ocupando colunas da esquerda, blocos pequenos de texto em colunas específicas, vazio como decisão.
**Paleta:** uma cor chapada de fundo (`#B01B12`) · branco · fio a 20%
**Fontes:** `suico` → Inter 900 / Inter 400
**Escala:** o título muda de coluna a cada card. **Sem variar a posição, oito cards viram oito paredes iguais** — este é o estilo que mais precisa de disciplina de ritmo.

## 52 · MEMPHIS — [52-memphis.jpeg](../assets/referencias/52-memphis.jpeg)
**Mecanismo:** campos de cor chapada dividindo o card em zonas irregulares, com um bloco de listras diagonais quebrando uma delas. Formas soltas espalhadas sem grade. Tipografia com sombra sólida deslocada.
**Paleta:** rosa `#F49AC8` · amarelo `#FFE500` · verde menta `#8FD9B6` · azul `#3A5FD9` · preto e branco
**Fontes:** `memphis` → Rubik Mono One / Rubik
**Escala:** boa, mas cansa. **Reduza a densidade de formas a cada card** em vez de manter.

## 53 · JANELAS — [53-janelas.jpeg](../assets/referencias/53-janelas.jpeg)
**Mecanismo:** fundo de cor agressiva e, por cima, **janelas de sistema operacional antigo** em ângulos e tamanhos diferentes, algumas cortadas pela borda. A tipografia é uma massa preta no centro, e as janelas passam por trás e por cima dela.
**Paleta:** verde ácido `#D9F218` · preto · cinza de janela `#C0C0C0` · branco
**Fontes:** `janelas` → Archivo Black / Space Mono
**Escala:** a melhor da biblioteca para assunto de software — **as janelas carregam conteúdo real**, então o grafismo é a informação. Cada card muda quais janelas aparecem e o que mostram.
**Cuidado verificado:** janela posicionada por cima do bloco de título come letra. Defina a zona do título primeiro e posicione as janelas fora dela.

---

# Nível imagem — precisam de gerador

Só proponha se o perfil confirmar Pollinations, chave de API ou MCP.

## 26 · VAPORWAVE — [26-vaporwave.png](../assets/referencias/26-vaporwave.png)
**Mecanismo:** busto clássico ou objeto recortado flutuando sobre grade em perspectiva, com janelas de sistema antigo, texto japonês decorativo e glitch de VHS.
**Paleta:** rosa `#FF6EC7` · ciano `#00E5FF` · roxo `#7B2FF7` · azul-noite
**Fontes:** `vaporwave` → VT323 / Space Mono
**Precisa gerar:** o busto e a textura de glitch. A grade e as janelas são CSS.
**Cuidado:** encosta no antipadrão de glow e neon. Mantenha o brilho fora.

## 32 · PONTILHISMO — [32-pontilhismo.png](../assets/referencias/32-pontilhismo.png)
**Mecanismo:** imagem inteira reduzida a aglomerado de pontos, alto contraste, uma ou duas tintas. A tipografia entra chapada por cima, sem textura, criando contraste entre o granulado e o liso.
**Paleta:** uma tinta escura + um papel colorido (`#F2C8D8`, `#C89B6B`)
**Fontes:** `pontilhismo` → Playfair Display 900 / Newsreader
**Precisa gerar:** a imagem. O pontilhado se aplica depois em CSS com `radial-gradient` e alto contraste.

## 33 · MIXED MEDIA — [33-mixedmedia.png](../assets/referencias/33-mixedmedia.png)
**Mecanismo:** camadas de origens diferentes no mesmo plano — foto em preto e branco, forma vetorial chapada, traço à mão, papel milimetrado ao fundo. O recorte invade a área do texto.
**Paleta:** papel `#F6F0E2` · preto · um vetor saturado · uma foto dessaturada
**Fontes:** `mixedmedia` → Alfa Slab One / Libre Baskerville
**Precisa gerar:** os recortes fotográficos.

## 35 · KAWAII — [35-kawaii.png](../assets/referencias/35-kawaii.png)
**Mecanismo:** personagem com rosto simples repetido em várias poses, cercado de elementos pequenos flutuando, sobre fundo pastel com brilhos. Cada card é uma cena com o mesmo elenco.
**Paleta:** rosa `#FFD1E3` · azul bebê `#BFE3FF` · amarelo `#FFF3B0` · marrom de contorno
**Fontes:** `kawaii` → Fredoka 600 / Nunito
**Precisa gerar:** o personagem. Gere todas as poses na mesma sessão com a mesma seed base, ou ele muda de cara no meio do carrossel.

## 44 · WABI SABI — [44-wabisabi.png](../assets/referencias/44-wabisabi.png)
**Mecanismo:** muito vazio, assimetria calculada, uma imagem de textura natural ocupando um terço, tipografia pequena e discreta em corpo generoso de entrelinha.
**Paleta:** areia `#E8E2D6` · argila `#B9A48C` · verde-oliva `#6E7355` · carvão
**Fontes:** `wabisabi` → Cormorant Garamond 700 / Karla
**Precisa gerar:** a textura natural.
**Cuidado:** é o oposto de um carrossel de feed — pouco texto, pouco contraste. Só quando a mensagem for calma.

## 47 · REBUS — [47-rebus.png](../assets/referencias/47-rebus.png)
**Mecanismo:** a frase é escrita com **palavras substituídas por imagens pequenas** embutidas na linha de texto. Layout limpo, tipografia grande, e o pictograma faz o trabalho de significado.
**Paleta:** off-white · preto · as imagens trazem a cor
**Fontes:** `rebus` → Inter 700 / Inter 400
**Precisa gerar:** os pictogramas — pequenos, o que reduz o custo.
**Por que é forte:** é o único mecanismo em que a imagem **é sintaxe**, não decoração. Funciona muito bem para explicar processo.

## 54 · Y2K — [54-y2k.jpeg](../assets/referencias/54-y2k.jpeg)
**Mecanismo:** tipografia inflada em cromo disposta em arco, sobre fundo iridescente líquido, com brilhos de quatro pontas.
**Paleta:** rosa `#F5C2DC` · azul bebê `#BBD9F2` · cromo
**Fontes:** `y2k` → Bungee / Space Grotesk
**Precisa gerar:** o cromo e o fundo.
**Problema sério:** o título curvo e cromado não é reproduzível em HTML de forma confiável, o que colide com o princípio de que toda palavra é código. Se escolher, o título vira exceção documentada e precisa ser conferido letra a letra.

---

# Proibidos — na biblioteca para você reconhecer, não para propor

Estes dois estão na pasta com o sufixo `PROIBIDO` porque batem de frente na checagem antipadrão da skill. Se o usuário pedir um deles explicitamente, explique o custo antes de aceitar.

## AURORA — [xx-aurora-PROIBIDO.png](../assets/referencias/xx-aurora-PROIBIDO.png)
Gradiente iridescente, blur, glow suave, sobreposição translúcida. É o visual que hoje lê como "gerado por IA" com mais força, e três dos seus elementos estão na lista de corte.

## GLASSMORPHISM — [xx-glassmorphism-PROIBIDO.png](../assets/referencias/xx-glassmorphism-PROIBIDO.png)
Fundo fosco, blur, semitransparência, sombra suave, tinta neon. Mesmo problema, agravado: virou o padrão de apresentação de produto de software, então além de genérico é datado.

**A saída honesta**, se o usuário insistir: pegue o que essas duas fazem bem — profundidade por camadas — e resolva com **camadas opacas sobrepostas e deslocamento**, em vez de blur e transparência. O efeito de profundidade sobrevive; o carimbo de IA some.

---

## Como usar na etapa 1

1. Cheque no perfil quais níveis estão disponíveis
2. Escolha **cinco mecanismos diferentes** dentro do que está liberado
3. Escreva o mecanismo de cada uma antes de renderizar; dois iguais, troque
4. Rode `baixar-fontes.sh <estilo>` para cada direção que for renderizar
5. Adapte a paleta ao assunto — a da referência é ponto de partida, não obrigação
6. Renderize capa **e** card do meio
7. Diga ao usuário qual referência originou cada direção
