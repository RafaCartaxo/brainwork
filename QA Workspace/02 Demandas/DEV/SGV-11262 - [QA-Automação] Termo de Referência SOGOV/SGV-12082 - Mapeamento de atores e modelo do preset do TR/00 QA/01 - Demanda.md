---
prioridade: media
origem: conversa
pontos_alocados: ""
---

# SGV-12082 — Mapeamento de atores e modelo do preset do TR

**Ticket de origem:** SGV-12082 · **Demanda pai:** SGV-11262

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Plano de análise:** [[02 - Plano de análise]]
> **Revisão da análise:** [[04 - Revisão da análise]]
> **Mapa geral:** [[../01 Modelo do preset/00 - Mapa geral]]
> **Matriz de atores e relações:** [[../01 Modelo do preset/01 - Matriz de atores e relações]]
> **Fontes:** [[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual — demanda encerrada neste escopo (15/10/2026, decisão do Rafael)
> A **Fase 1 — modelo conceitual do TR completo — está concluída**, o **caminho-base (passo 8) foi aprovado**, o **modelo-alvo dos dados do preset ([[../01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04]]) está aprovado**, e a **matriz de fornecimento dos dados ([[../01 Modelo do preset/05 - Matriz de fornecimento dos dados|05]], C1–C6) está aprovada**. As 17 fatias e a consolidação são evidência sobre a automação atual, não limite do modelo. Com isso, os passos 1–10 da Sequência macro do Roadmap estão concluídos e **esta demanda está encerrada no escopo atingido** — sem reabrir TR, recortes, 04 ou 05. A arquitetura/preparação técnica do preset (**passo 11**) continua **futura, fora do escopo atual e numa trilha separada que não bloqueia este encerramento**; sequência e gates estão no [[../../Roadmap - Modelo de atores e preset do TR|Roadmap]]. O levantamento da Onda 1 de cenários de sanidade da SGV-12200 já foi iniciado como pacote irmão (demanda independente desde 16/10/2026), usando 04/05 como referência.

> [!note] Abordagem anterior preservada
> A investigação original da SGV-12082 (matriz do preset, DISC-001–004), o ciclo SGV-11971 e o Roadmap anterior estão arquivados para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]] — referência histórica, não fonte de critério desta nova frente.

---

## Problema / contexto

O Termo de Referência do SOGOV (itens 1.1–1.43) precisava de um modelo conceitual explícito de atores, entidades, configurações, estados, relações e dependências, rastreável item a item. A abordagem anterior (preservada em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]) inclui o ciclo de automação dos itens 1.24–1.25 (SGV-11971) **e** uma investigação mais ampla do TR sob a ótica de CTs (SGV-12082 anterior, DISC-001–004). Esta frente já concluiu o modelo conceitual e agora deriva dele, com apoio da documentação de produto, o **modelo-alvo dos dados necessários aos cenários de sanidade** — sem decidir casos de teste nem preset executável.

## Objetivo

Produzir um modelo rastreável do TR completo que identifique atores, entidades, dados/atributos, configurações, estados e relações/dependências e, a partir dele e da documentação de produto, derive os dados necessários aos cenários de sanidade. Cada elemento mantém referência de origem e estado de conhecimento (Confirmado/Inferido/A confirmar). A matriz indexa os recortes; notas temáticas e mapa geral sustentam a rastreabilidade. Primeiro se define a necessidade lógica; depois se mapeia o fornecimento pelo `.env` individual, pelo seed persistente ou durante o cenário.

### Entrega desta capacidade

- Notas temáticas (por recorte do TR, ver `01 Modelo do preset/Seções do TR/`) cobrindo o TR completo, com cada item mapeado, marcado como não aplicável (sem elemento relevante para este modelo, com justificativa) ou registrado como pendente; a matriz central indexa os recortes, sem duplicar elementos/relações.
- Mapa geral (Mermaid) como síntese visual consistente das notas temáticas — nunca uma fonte própria de fato.
- Modelo-alvo do preset, derivado do TR e da documentação de produto, que relaciona os dados, atores, estados, configurações e dependências necessários aos cenários de sanidade ([[../01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04]], aprovado).
- Matriz de fornecimento dos dados ([[../01 Modelo do preset/05 - Matriz de fornecimento dos dados|05]], aprovada, C1–C6): pra cada dado já definido no modelo-alvo, um **canal candidato** (`.env` individual, seed persistente, cenário de teste, ou combinação) — hipótese, não decisão final de arquitetura.
- Lacunas e ambiguidades encontradas registradas para revisão, não resolvidas por suposição.

---

## Decisões de método e escopo

- O TR completo (itens 1.1–1.43) é a fonte de escopo desta análise. Contexto externo pode esclarecer, mas não vira requisito sem identificação da fonte e validação.
- Os 11 recortes temáticos usados para percorrer o TR (nomes, quantidade e fronteiras) foram **aprovados pelo Rafael em 08/10/2026** — a segmentação não é mais definida durante a leitura. O que resta é analisar o conteúdo de cada recorte contra o PDF, um de cada vez, com pausa para revisão entre eles.
- Esta demanda produz o modelo conceitual e o modelo-alvo dos dados necessários; não implementa seed/preset, automação, testes funcionais nem sincronização com a Qase.

---

## Escopo

- Percorrer o TR completo (1.1–1.43), de forma progressiva, pelos recortes temáticos (`01 Modelo do preset/Seções do TR/`).
- Registrar, na nota temática de cada recorte, todo ator/entidade/configuração/estado identificado, com papel/descrição, dados/atributos relevantes, relações/dependências, referência ao item do TR e estado de conhecimento.
- Sintetizar o mapa geral (Mermaid) a partir do que estiver confirmado nas notas temáticas.
- Derivar o modelo-alvo dos dados de preset necessários a partir do TR e da documentação de produto, sem limitar o alvo ao seed/testes atuais.
- Após definir a necessidade de cada dado, registrar sua origem de fornecimento entre `.env` individual, seed persistente e estado criado durante o cenário, quando sustentado.
- Revisar cobertura (todo item do TR mapeado, não aplicável ou pendente) e consistência entre as notas temáticas e o mapa.

---

## Fora de escopo

- Casos de teste (CTs) e qualquer sincronização com a Qase.
- Automação, execução ou alteração de seed/preset.
- Implementar seed/preset, automatizar sua execução ou definir arquitetura de persistência e reconciliação.
- Criar ou sincronizar CTs/Qase; esses casos são trabalho separado, derivado do modelo.

---

## Critérios de aceite

- C1. Todo item do TR completo (1.1–1.43) foi considerado; cada item está rastreável como mapeado, não aplicável (sem elemento relevante para este modelo, com justificativa) ou pendente. ^c1
- C2. Cada elemento mapeado na nota temática correspondente aponta a referência/item do TR e seu estado de conhecimento (Confirmado/Inferido/A confirmar). ^c2
- C3. Os elementos e as relações/dependências entre eles estão representados nas notas temáticas correspondentes; a matriz central indexa os recortes (intervalo de itens/páginas, status, link), sem duplicá-los. ^c3
- C4. O mapa geral (Mermaid) é uma síntese consistente do que está registrado nas notas temáticas, sem conteúdo que elas não sustentem. ^c4
- C5. Lacunas e ambiguidades encontradas durante o mapeamento estão registradas explicitamente para revisão, não resolvidas por suposição. ^c5
- C6. O modelo-alvo identifica dados e estados necessários aos cenários de sanidade com rastreabilidade ao TR/produto; o que não está confirmado permanece aberto. ^c6
- C7. O canal de fornecimento não é presumido pela natureza do dado: `.env`, seed e cenário são avaliados depois de definir a necessidade. ^c7

---

## Checklist de fechamento da análise

- [x] Todo item do TR (1.1–1.43) está mapeado, não aplicável (com justificativa) ou pendente.
- [x] Cada elemento/relação, registrado na nota temática correspondente, aponta a referência do item do TR.
- [x] Notas temáticas e mapa geral (Mermaid) estão consistentes entre si.
- [x] Lacunas e ambiguidades encontradas estão registradas para revisão.
- [x] A [[04 - Revisão da análise|revisão da análise]] foi concluída.

---

## Pendências de decisão

O mapeamento conceitual da Fase 1 está concluído; o modelo-alvo (04) e a matriz de fornecimento (05) também estão concluídos e aprovados. Nenhuma decisão de arquitetura foi tomada, e dúvidas específicas continuam abertas sem bloquear o que já foi aprovado:

- A segmentação do TR em 11 recortes temáticos foi **aprovada pelo Rafael** (08/10/2026). Os 11 recortes foram revisados contra o PDF; a cobertura e a rastreabilidade estão registradas em [[04 - Revisão da análise]]. A fonte de autoridade permanece exclusivamente o PDF (`Fontes/Termo de Referência SOGOV.pdf`) — nunca as notas temáticas, a matriz ou material arquivado.
- As 17 fatias e a consolidação registram evidências do seed/testes atuais; não definem os requisitos do modelo-alvo.
- O caminho-base (passo 8) foi **aprovado** pelo Rafael/Codex para orientar o modelo-alvo. Dúvidas específicas de ator, regra, corpus ou implementação continuam abertas e rastreáveis por item — não bloqueiam o modelo aprovado, e são aprofundadas quando afetarem um elemento específico.
- CTs, Qase e implementação do preset continuam fora desta demanda. A preparação técnica é decidida depois de revisar o modelo-alvo e a matriz de fornecimento.

### Checklist de fechamento desta capacidade

- [x] C6 — Modelo-alvo aprovado, com rastreabilidade ao TR/produto: [[../01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]]
- [x] C7 — Canal de fornecimento mapeado como hipótese candidata, não decisão de arquitetura: [[../01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]] (C1–C6)

---

## Encerramento (15/10/2026)

Rafael autorizou encerrar esta demanda no escopo concluído: Fases 1–4 e passos 1–10 da Sequência macro do Roadmap (segmentação, leitura por recorte, consolidação, mapa geral, revisão da análise, evidências da automação atual, caminho-base, modelo-alvo 04 e matriz de fornecimento 05). Nenhum conteúdo aprovado do TR, dos recortes, do 04 ou do 05 foi reaberto para este encerramento.

O **passo 11** (preparação técnica/arquitetura do preset por ambiente/instância) permanece **futuro, fora do escopo desta demanda e numa trilha própria** — este encerramento não o transforma em bloqueio e não cria nenhuma nova task técnica para tratá-lo.

O levantamento da Onda 1 de cenários de sanidade da SGV-12200 foi iniciado como pacote irmão sob esta mesma SGV-11262 (até 16/10/2026, quando passou a demanda independente), usando os artefatos 04/05 já aprovados como referência, sem depender da conclusão do passo 11 nem de reabrir esta demanda.
