# Entrevista de briefing: a especificidade nasce antes do texto

Texto genérico não é (só) defeito de escrita — é defeito de insumo. A IA preenche o que não sabe com a média do corpus; a entrevista existe para substituir a média por matéria-prima real. **Cada pergunta alimenta uma regra da skill**: sem resposta, a regra opera no vazio.

## Como conduzir

- Pergunte **só o que o briefing não respondeu**. Releia o pedido antes: entrevista que repete o briefing é slop de processo.
- **Máximo 5 perguntas, numa rodada só**, as de maior impacto primeiro. Não é formulário — é conversa de redator.
- **Toda pergunta oferece explicitamente a opção de pular.** Em ferramenta interativa de perguntas, inclua uma opção "Pular" (ou equivalente) em cada uma; em texto corrido, diga de saída que qualquer pergunta pode ser pulada. Pergunta pulada = placeholder `[CONFIRMAR]` ou slot pendente no lugar da resposta, sem insistir e sem reperguntar.
- Registre as respostas no topo do rascunho (bloco "Briefing") para a revisão poder auditar claims contra elas.

## Banco de perguntas → regra que alimenta

| # | Pergunta | Alimenta |
|---|---|---|
| 1 | **Qual é a ação ou decisão esperada de quem lê/assiste?** (comprar, agendar reunião, aprovar verba, mudar de opinião sobre o quê?) | O fio do deck e o CTA — sem isso, títulos viram categoria e o fecho vira exortação genérica |
| 2 | **Quem exatamente é o público?** (cargo, contexto, o que já sabe, o que resiste) — "todos os perfis" não é resposta | Registro certo × público, correlações de abrangência universal, juridiquês/tecniquês indevido |
| 3 | **Que ativos reais existem?** Números com fonte, casos, clientes nomeáveis, depoimentos autorizados, restrições reais de oferta (prazo, vagas, data) | Regra inegociável de claims (SKILL.md) — transforma `[CONFIRMAR]` em fato antes de nascer; urgência só entra com número e data |
| 4 | **O que só essa marca/produto pode dizer?** (ativo próprio, história, inimigo declarado, ponto de vista assumido, detalhe que só quem faz sabe) | Teste de intercambialidade — a resposta é a headline em estado bruto |
| 5 | **Existe guia de voz / tom da marca?** Expressões obrigatórias, proibidas, fórmulas deliberadas. *(Em revisão, acrescente: o que deste texto é fato de briefing e o que é herança de rascunho?)* | Exceções da skill (voz da marca vence regra), calibragem de anglicismos; em revisão, evita deslopar fato real |

Uma boa rodada tem as 3–4 mais relevantes para a peça, não as cinco por obrigação.

## Sinais de que a entrevista foi pulada indevidamente

- Texto entregue com 5+ `[CONFIRMAR]` sem que nenhuma pergunta tenha sido feita ao usuário presente e disponível.
- Headline que falha o teste do logo trocado quando a pergunta 4 nunca foi feita.
- Público descrito no texto como "empresas de todos os portes" / "para todos os perfis".

## Enriquecimento futuro (ganchos)

Esta seção é o ponto de extensão planejado — ao evoluir a skill, plugar aqui sem mexer no fluxo:

Arquivos `references/voz-*.md` e `references/dados-*.md` são **locais e proprietários** (fora do repo público, via `.gitignore`). Antes da entrevista, verifique se existem no diretório da skill — se existirem, leia-os primeiro:

- **Tom de voz proprietário:** havendo um `references/voz-*.md` aplicável, a pergunta 5 deixa de ser pergunta e vira leitura obrigatória do arquivo antes de gerar.
- **Dados proprietários:** benchmarks, pesquisas e números recorrentes em `references/dados-*.md` alimentam a pergunta 3 — consulte antes de pedir ao usuário e use como fonte legítima (não é dado inventado; é dado com procedência registrada).
- **Histórico de respostas:** respostas de briefing recorrentes (mesmo cliente/marca) podem ser promovidas a arquivo de referência para não reperguntar.
