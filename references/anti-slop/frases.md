<!-- Vendorizado de Zero-Lero (https://github.com/ViniciusStanula/Zero-Lero), MIT License, © Vinicius Stanula. -->

# Frases a Remover

Frequências entre parênteses = `ocorrências/arquivos` nos corpora que fundamentam esta skill: **v1** (24 textos, blog/produto/SEO) e **v2** (32 textos, 12 gêneros, teste adversarial). Ver README.md e CHANGELOG.md. Padrões sem frequência vêm do SOP de referência ou de variantes diretas dos padrões medidos.

Lição do teste adversarial: **listas fixas envelhecem; famílias não.** "Em resumo/Em suma" deu 16 hits no v1 e zero no v2 — o slop migrou para "Resumindo:", "Diante do exposto". Ao buscar, trate cada categoria como família flexionável, não como lista literal.

## Editorializing — a família "ressaltar" (21/16, o padrão nº 1 do pt-BR)

O padrão flexiona: `[é importante / vale / cabe / cumpre / é válido / é fundamental] + [ressaltar / destacar / frisar / salientar / lembrar / mencionar / notar] + que`. Busque a família, não a frase exata.

- "É importante ressaltar que"
- "Vale ressaltar que"
- "Vale destacar que"
- "É importante destacar que"
- "Vale lembrar que"
- "É válido ressaltar que"
- "Cabe destacar que"
- "Cumpre salientar que"
- "É fundamental compreender que"

**Correção:** corte a moldura e afirme o conteúdo. "Vale ressaltar que o prazo conta a partir do pagamento" → "O prazo conta a partir do pagamento."

## Molduras temporais de abertura (10/9)

- "No mundo atual"
- "Nos dias de hoje"
- "No cenário atual"
- "Em um mundo cada vez mais [X]"
- "Em meio à correria do dia a dia"
- "Vivemos em uma era de"

**Correção:** comece pelo assunto. A primeira frase do texto carrega o tell com mais frequência que qualquer outra.

## Conectivos em cadeia (33 combinados)

Flagre densidade, não instância. Um por texto passa; um por parágrafo é máquina.

- "Além disso" (16/14 — quase um por texto no corpus)
- "Dessa forma" / "Desse modo"
- "Nesse sentido" / "Nesse contexto"
- "Por conseguinte"
- "Sendo assim"
- "Em primeiro lugar... Em seguida... Por fim..." (13/6 — esqueleto sequencial exposto)
- "Ademais" / "Outrossim" (raros até no slop; quando aparecem, tell de registro empolado)

**Correção:** corte o conectivo e releia. A maioria das frases se conecta sozinha.

## Marcadores de contraste binário (23 combinados)

Versões frasais do padrão estrutural (ver estruturas.md):

- "Não se trata de X. Trata-se de Y." (13/7)
- "Não é apenas X. É Y."
- "não apenas X, mas também Y"
- "deixou de ser X e se tornou Y" (3 textos do corpus, fórmula idêntica)
- "X não é tudo. Y é tudo."
- "A pergunta não é SE, é QUANDO."
- **Versão positiva (sem negação, v2 — 3/3):** "é mais do que um X. É Y.", "muito mais do que", "vai muito além de". Mesma reversão telegrafada; escapa de buscas por "não". Busque a reversão, não a negação.

**Correção:** afirme Y. Corte a negação (ou a rampa "mais do que") inteira.

## Falsa causalidade dramática (9/9 — um por texto, distribuição mecânica)

- "Não é à toa que"
- "Não é por acaso que"
- "Não é para menos"
- "E não é para menos:"

**Correção:** corte. Se a evidência sustenta a conclusão, ela dispensa o anúncio.

## Verbos de benefício vago (45+ combinados — slop de produto)

Quase sempre em gerúndio pós-vírgula (ver estruturas.md):

| Evite | Use |
|---|---|
| "proporcionando [abstração]" (12/7) | a consequência concreta, com número se houver |
| "garantindo [abstração]" (19/9) | o que acontece de fato |
| "otimizando o seu tempo" | quanto tempo, em quê |
| "impulsionando seus resultados" | qual resultado, quanto |
| "potencializando" | o efeito específico |
| "agregando valor / elegância / sofisticação" | o que muda para quem usa |
| "facilitando o seu dia a dia" (9/8) | a tarefa específica que fica mais fácil |
| "elevando sua experiência a outro patamar" (7/4) | corte; é puro ar |

## "Conta com" (12/7 — verbo-cola de descrição comercial)

"O apartamento conta com 3 quartos", "a plataforma conta com emissão de NF-e".

**Correção:** "tem", ou reestruture pela informação: "3 quartos, 1 suíte". Seis "conta com" numa página de imóvel é assinatura de máquina.

## Gerundismo (4/3 — 100% dos emails do corpus)

- "Estaremos enviando" → "enviaremos" / "vamos enviar"
- "Estaremos oferecendo" → "oferecemos" / "vamos oferecer"
- "Vamos estar disponibilizando" → "vamos disponibilizar"

**Correção:** sem exceção. Conjugue o futuro.

## Tendência vaga em gerúndio (8/8)

- "vem ganhando destaque"
- "vem crescendo de forma consistente"
- "vem se consolidando"
- "vem conquistando cada vez mais adeptos"

**Correção:** quantifique ("cresceu 30% em 2025") ou corte. Movimento sem agente nem número é enchimento.

## Muletas instrumentais e intensificadores

- "através de" (5/4) → "por", "com", "via"
- "cada vez mais" (8/6) → quantifique ou corte
- "de forma [adjetivo]" ("de forma natural e orgânica", "de forma consistente") → advérbio direto ou corte. **É o advérbio disfarçado do pt-BR: escapa de qualquer filtro de "-mente".**
- Densidade de "-mente": "completamente", "cuidadosamente", "significativamente", "extremamente", "totalmente". Um é humano; cinco por seção, não.

## Inflação de significância

- "um verdadeiro / uma verdadeira [X]" (5/5) — "uma verdadeira revolução"
- "divisor de águas" (2/2) / "virada de chave"
- "desempenha um papel fundamental" (6/3)
- "veio para ficar" (3/2) / "é um caminho sem volta"
- "faz toda a diferença" (8/7)
- "transformador / experiência transformadora" ("transform*": 21/13)
- "redefine o conceito de"
- "é prova de que" / "é um testemunho de"

**Correção:** afirme o fato sem o megafone. Se a coisa é importante, o leitor percebe pelo conteúdo.

## Tom promocional-turístico (11/5)

- "deslumbrante"
- "de tirar o fôlego"
- "inesquecível"
- "imperdível"
- "encanta visitantes"
- "paraíso escondido"
- "rico patrimônio cultural"
- "charmosa" / "aconchegante" (em série)
- "uma energia única"

**Correção:** descreva o que se vê e se faz. "Cachoeira de 120 metros" vence "queda d'água de tirar o fôlego".

## Léxico comercial inflado

| Evite | Frequência | Use |
|---|---|---|
| "jornada" (como qualquer atividade) | 8/7 | a atividade real: "curso", "uso", "processo" |
| "experiência" (como produto) | 9/5 | o que a pessoa faz ou recebe |
| "exclusivo" | 8/6 | só se for de fato exclusivo |
| "completo / completa" | 16/12 | o que está incluído |
| "ideal para / perfeito para" | 13/8 | para quem serve e por quê |
| "solução" (para produto) | — | o nome do que é |
| "sob medida / personalizado" | 2/2 | o que se ajusta, como |
| "humanizado" (atendimento) | 2/2 | horário e canal reais |

## Tradutês (calcos do inglês)

- "jornada" → calco de "journey"
- "no final do dia" / "no fim das contas" (2/2) → calco de "at the end of the day"
- "divisor de águas" como muleta → calco de "game-changer"
- "Dito isso," → calco de "That said,"
- "elevar ao próximo nível" → calco de "next level"
- "empoderar" (fora de contexto social) → calco de "empower"
- "engajar / engajamento" em densidade

## Atribuição evasiva (8/4 — zero fontes nomeadas no corpus)

- "Estudos mostram que"
- "Pesquisas indicam que"
- "Pesquisas apontam que"
- "Especialistas apontam que"
- "A ciência comprova"
- "Dados do setor revelam"

**Correção:** nomeie estudo, ano e fonte — ou corte a frase. Autoridade sem fonte é pior que afirmação direta.

## Declarativas vagas

- "Os benefícios são inúmeros."
- "As implicações são profundas."
- "As consequências são reais."
- "As possibilidades são praticamente infinitas."
- "Os resultados falam por si."

**Correção:** nomeie o benefício, a implicação, a consequência. Uma de cada vale mais que o anúncio de todas.

## CTAs e fechos de engajamento (12/9)

- "Gostou? Compartilhe!"
- "Deixe sua opinião nos comentários!"
- "E você, já passou por isso? Conta aqui. 👇"
- "Continue acompanhando o nosso blog"
- "Pense nisso." / "Reflita sobre isso."
- "[coisa] agradece": "Sua mente agradece", "Seus pés agradecem", "O seu eu do futuro agradece" (3 textos, espontâneo — fecho-fórmula brasileiro)
- "Comece hoje mesmo!"
- "Agora é com você."

**Correção:** termine no fato mais forte. Texto que precisa pedir engajamento não confiou no próprio conteúdo.

## Urgência fabricada (slop de email/e-commerce)

- "Corra!" / "Não perca!"
- "as ofertas são por tempo limitado"
- "os estoques estão voando"
- "Não deixe para a última hora"
- "oportunidades como essa só aparecem uma vez por ano"
- "Aproveite enquanto dá tempo"
- P.S. de escassez ("As primeiras 30 inscrições ganham...")

**Correção:** se a restrição é real, declare-a com número e data. Se não é, corte.

## Conclusões rotuladas (família, não lista)

A lista fixa do v1 ("Em resumo/Em suma/Em conclusão") deu zero hits no v2 — as variantes capturaram tudo. Busque a função (rotular o fim e repetir o que o texto já disse), não a frase:

- "Em resumo," / "Em suma," / "Em conclusão,"
- "Resumindo:" / "Recapitulando:"
- "Concluindo,"
- "Diante do exposto, conclui-se que" (registro jurídico)
- "Veredito" (resenhas)
- Headings "Conclusão", "Considerações finais", "Principais aprendizados"

**Correção:** corte o parágrafo-resumo inteiro e termine no último ponto que importa.

## Anúncios de alívio e revelação (v2 — 9/8 combinados)

Rótulo que anuncia a sensação antes de entregar o conteúdo:

- "A boa notícia? [resposta]" / "A boa notícia é que" (6/6 — o escape mais distribuído do v2)
- "O melhor de tudo? [resposta]"
- "E o melhor:" / "A parte boa:"
- "Spoiler:" / "Resultado:" / "Tradução:" + punchline
- "Já adianto a boa notícia:"

**Correção:** entregue o conteúdo. Se a notícia é boa, o leitor percebe.

## Conspiração do silêncio (v2 — 7/5)

Autoridade por exclusividade fabricada — variante dramática da atribuição evasiva:

- "o que ninguém te conta"
- "ninguém fala disso"
- "que poucos sabem" / "um segredo que poucos conhecem"
- "as [instituições] não querem que você saiba"
- "o ponto que ninguém está discutindo"

**Correção:** se a informação é boa, ela dispensa o teatro de revelação. Afirme e fundamente.

## Falsa franqueza (v2 — 4/4 dos textos com pedido de "tom humano")

Honestidade performada em vez de praticada. **Assinatura do slop que sobrevive quando o prompt pede pra não parecer IA:**

- "Vou ser sincero:" / "Vou ser honesto:"
- "Vou abrir o jogo:"
- "Confesso que"
- "A verdade é dura, mas precisa ser dita:"
- "Não é post de coach, prometo."

**Correção:** corte o anúncio e diga a coisa. Franqueza anunciada é o oposto de franqueza.

## Falsa intimidade "aquele/aquela [X]" (v2 — 6/5)

Pressupõe experiência compartilhada que o texto nunca estabeleceu:

- "aquela angústia de domingo à noite"
- "aquele toque dourado que faz toda a diferença"
- "aquela vida que de fora parece resolvida"
- "aquele amigo que vive [X]"

**Correção:** ou descreva a experiência de verdade, ou corte o piscar de olho.

## Hype casual (v2 — 6/4)

Inflação de significância em registro informal — escapa das listas de inflação formal:

- "muda o jogo" / "muda tudo"
- "entrega demais"
- "absurdo" (como elogio)
- "surpreendentemente bem"
- "é outro nível"

**Correção:** o que mudou, quanto, para quem. Mesma regra da inflação formal.

## Imperativos de conforto (v2 — 3/3)

Condescendência embalada de empatia:

- "Respira. A gente resolve."
- "Calma."
- "Confia no processo."
- "Fica tranquilo."

**Correção:** resolva. O conforto vem da solução, não do comando.

## Promessa de simplicidade (v2 — 5/4)

- "Simples assim."
- "sem mistério" / "sem segredo"
- "sem pegadinha" / "sem letra miúda"
- "sem burocracia"
- "descomplicado"

**Correção:** demonstre a simplicidade (passos, tempo, exemplo) em vez de declará-la.

---

# Slop de registro

O teste adversarial v2 mostrou: o slop migra com o registro. Cada gênero tem um dialeto viciado próprio que as listas gerais não pegam. Regra transversal: **o tell é registro em fôrma + público errado** — juridiquês para leigo, liturgia de plataforma executada na ordem canônica, empatia corporativa idêntica em qualquer caso.

## Jurídico (v2 — 17/2, cobertura anterior ~15%)

A IA imita petição mesmo escrevendo para leigos:

- "Cumpre esclarecer" / "Cumpre destacar"
- "Insta salientar"
- "Outrossim" / "Ademais"
- "Em que pese"
- "o referido diploma legal" / "a referida norma"
- "nos termos da legislação vigente"
- "No tocante a"
- "Há que se considerar"
- "Faz-se necessário"
- "Diante do exposto, conclui-se que"

**Nota metodológica:** o v1 refutou "outrossim" como tell — mas não tinha texto jurídico. No registro certo, o empolado domina. **Correção:** se o público é leigo, escreva em português comum; cite a lei pelo número e siga em frente.

## Acadêmico (v2 — 14/2)

- "O presente estudo/trabalho/artigo"
- "a literatura aponta" (atribuição evasiva acadêmica — nomeie os autores)
- "busca-se compreender"
- "espera-se que os achados contribuam"
- "no contexto da contemporaneidade"
- "tece as considerações finais"
- "acerca de" em densidade
- "O artigo está estruturado da seguinte forma:" (anúncio de estrutura)

**Correção:** sujeito definido ("analisamos", "os dados mostram que"), autores nomeados, estrutura sem mapa.

## Corporativo / press release (v2 — 8/3)

- "reforça seu compromisso com"
- "marca um novo capítulo"
- "líder em soluções de"
- "consolidando seu papel como agente de transformação"
- "Estamos extremamente felizes e honrados"
- "trajetória de crescimento acelerado"
- "nasceu com a missão de" (boilerplate "Sobre a empresa")
- Aspas executivas com slop embutido: citação de CEO carregando contraste binário e inflação ("Não é apenas um investimento na X. É um investimento no futuro do país"). O slop se esconde no discurso direto, onde o leitor baixa a guarda.

**Correção:** fato, número, data. "Vamos abrir 2 escritórios e dobrar o time até 2027" vence qualquer compromisso reforçado.

## Suporte / atendimento (v2 — 10/2)

Empatia em fôrma, zero responsabilidade específica:

- "Lamentamos profundamente o ocorrido"
- "sinceras desculpas pelo transtorno causado"
- "Compreendemos perfeitamente a sua frustração"
- "situação que fugiu ao nosso controle"
- "Sua satisfação é a nossa maior prioridade"
- "tomar as devidas providências"
- "Permanecemos à disposição"
- Gerundismo de promessa: "estaremos aplicando", "estaremos enviando"

**Correção:** o que aconteceu, o que será feito, quando, e o que a pessoa precisa fazer. Uma desculpa específica vale dez profundas.

## Engajamento de plataforma — YouTube/thread (v2 — 26/10, o escape mais volumoso)

A IA reproduz a liturgia completa e na ordem canônica, sempre:

- "Fala, galera!" / "Salve, família"
- "já deixa o like" / "se inscreve no canal" / "ativa o sininho"
- "fica até o final porque" / "cola comigo até o final"
- "bora lá?"
- "Abre o fio 👇" / "segue o fio"
- "Salva essa thread 🔖" / "RT pra alcançar mais gente"
- Recapitulação final com ✅ por item

**Correção:** densidade é o tell — um canal real pede like uma vez, do seu jeito; a IA executa o ritual inteiro em cada peça. Corte para no máximo um pedido, com voz própria.

## Colecionismo / nicho (v2 — 13/3)

Reverência de catálogo (medido em vinil; o padrão generaliza para qualquer nicho de paixão):

- "presença obrigatória em qualquer coleção que se preze"
- "joia musical" / "verdadeira joia"
- "questão de completismo"
- "a versão definitiva"
- "icônica" / "lendário" / "cobiçada" em densidade
- "é também um investimento"

**Correção:** o detalhe que só quem conhece sabe (prensagem, selo, matriz, estado real) vale mais que toda a reverência.

---

## Artefatos de chat (decisivos quando encontrados)

Fragmentos da conversa com a IA colados no texto final:

- "Espero que ajude!"
- "Claro! Aqui está..."
- "Como modelo de linguagem..."
- "até a minha última atualização"
- "Fico à disposição para ajustes"
- strings perdidas tipo "turn0search0"

**Correção:** qualquer ocorrência é prova de publicação sem revisão. Corte e revise o texto inteiro.
