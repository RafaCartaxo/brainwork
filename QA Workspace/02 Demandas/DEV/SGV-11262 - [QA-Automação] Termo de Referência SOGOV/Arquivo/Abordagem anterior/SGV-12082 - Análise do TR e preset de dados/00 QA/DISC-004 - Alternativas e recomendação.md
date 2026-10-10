---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11262
tipo: matriz-detalhe
parte_de: "[[Matriz - Análise do preset provável]]"
---

# DISC-004 — Comparação de alternativas e recomendação

> [!info]- Navegação
> **Índice/resumo:** [[Matriz - Análise do preset provável]] · **DISC-001 (arquitetura):** [[../01 Automação/01 - Plano de automação#DISC-001 — Auditoria do projeto, reconciliada com o código (07/10/2026)|Plano de automação]] · **DISC-002:** [[DISC-002 - Cobertura do TR e rastreabilidade dos CTs]] · **DISC-003:** [[DISC-003 - Dados, preparação e eixos]] · **Fluxo do preset:** [[Fluxo - Preset de dados]]

> [!info] Nota de extração (08/10/2026)
> Conteúdo movido sem alteração técnica do antigo corpo da Matriz pra esta nota própria, pra reduzir o tamanho do índice. Nenhuma alternativa, recomendação ou entrega foi reescrita — só reorganizado. Ver [[Matriz - Análise do preset provável]] pro propósito/legenda.

## DISC-004 — Comparação de alternativas e recomendação (07/10/2026)

> [!info] Natureza desta seção
> **Síntese/recomendação documental.** Nenhuma implementação, nenhuma execução, nenhuma pasta/demanda criada. Baseada só no que DISC-001–003 confirmaram — onde a base é fraca, digo isso explicitamente em vez de preencher com suposição.

### Alternativas comparadas

| Alternativa | O que seria | Prós | Contras / risco | Por que não é a recomendação agora |
|---|---|---|---|---|
| **A. Portar os mecanismos do Cypress pro Playwright, na instância fixa atual** | Trazer `changePublicAgentWorkStatus`/`WORK_STATUS` e o padrão `createIsolatedTestAgent` pra `src/api/services/users.ts`, sem mexer em seleção de instância | Reaproveita lógica **já confirmada** (não reinventa); escopo pequeno e isolado; não depende de resolver clienteId primeiro | Não avança a direção de "sanidade por cliente/instância" da iniciativa — fica só no alvo atual | — (**é a recomendação**, ver abaixo) |
| **B. Construir seleção paramétrica de cliente/instância primeiro** | Criar um mecanismo de `clienteId`/instância configurável antes de portar qualquer CT de estado | Ataca direto o objetivo final da iniciativa | Maior, mais arriscado: nenhum framework tem isso hoje; esbarra na regra D4 (não criar instância em execução normal) se envolver instância nova; a própria Entrega 01 já tentou uma versão disso e ficou só como histórico, sem seed ajustado | Prematuro — o Roadmap já lista "sanidade por cliente/instância" como a **última** etapa (passo 6 de 6), não a primeira; fazer isso antes de ter qualquer CT de estado portado não tem CT nenhum pra validar a seleção contra |
| **C. Não portar nada agora; só documentar e esperar** | Deixar Suítes 3/4 como estão, sem investir em porte | Zero risco de execução | Os 22 CTs ficam presos num branch não mesclado, cada vez mais desatualizados em relação ao `main` do Playwright | Desperdiça o achado mais barato desta análise (código já pronto, só precisa ser portado) |

### Recomendação

**Alternativa A** — portar os mecanismos de estado do Cypress pro Playwright, mantendo a instância fixa atual (sem seleção paramétrica ainda). Justificativa ligada aos achados:

- DISC-002 confirmou que 22 dos 25 CTs pendentes já têm lógica real e específica (`changePublicAgentWorkStatus`, `createIsolatedTestAgent`) — não é preciso desenhar nada novo, só portar.
- DISC-003 confirmou que nenhum framework resolve clienteId hoje — ou seja, resolver isso não é pré-requisito pra portar os CTs de estado; são preocupações independentes.
- A regra D4 e a ausência de API de exclusão de instância (achados de sessões anteriores) tornam qualquer trabalho de seleção de instância nova/225 mais delicado e mais lento de validar — não é o caminho de menor risco pra começar.

**Seleção segura da instância 225 fica como trilha separada, não bloqueante** — pode evoluir em paralelo (ex.: entender como apontar o seed pra ela com segurança), mas não precisa terminar antes da Alternativa A começar.

### Entregas pequenas e sequenciadas (recomendadas, não abertas como pasta/demanda)

> **São 6 entregas candidatas, não 5** — correção de contagem (07/10/2026): a antiga "3b" virou Entrega 4 própria, não subentrega. Os 3 CTs sem código (016/017/037) **não contam** nessa lista — ficam à parte, fora de escopo, sem numeração de entrega.

| Ordem | Entrega candidata | Objetivo | CTs no escopo | Dependências | Aceite/evidência | Riscos |
|---|---|---|---|---|---|---|
| 1 | Portar bloqueio por tentativas (parcial) | Portar `createIsolatedTestAgent` + contagem de tentativas pro Playwright | CT-013, 014, 018, 019 | Nenhuma nova — só ler o Cypress já confirmado (`bdf5e9a`) | 4 CTs passando em Playwright contra o ambiente atual, evidência de execução real (não só leitura de código) | Baixo — mecanismo já confirmado, só port |
| 2 | Resolver o achado do CT-015 antes de portar | Confirmar com produto se "conta bloqueada aceita login com senha correta" é bug ou comportamento esperado | CT-015 | Resposta de produto/dev | Decisão registrada; só depois disso portar o CT (a asserção depende da resposta) | Médio — pode revelar bug real de produto, fora do controle da automação |
| 3 | Portar ciclo de vida **sem nenhuma lacuna conhecida** | Portar `changePublicAgentWorkStatus`/`WORK_STATUS` + os CTs onde o código não registra nenhum achado/instabilidade | CT-020, 021, 023, 024, 026, 027, 031, 035 | Entrega 1 (reaproveita o padrão de agente isolado) | CTs passando em Playwright; e-mail de notificação (CT-026) confirmado via Gmail real | Baixo-médio — CT-026 depende de infra de e-mail, mais frágil que os outros |
| 4 | Portar ciclo de vida **com gate de instabilidade conhecida** (entrega própria, não bloqueante — é hipótese de flakiness de teste, não disputa de produto) | Portar os mesmos CTs, mas com salvaguarda explícita pras 2 instabilidades já documentadas no código: **busca por nome às vezes não encontra o agente recém-criado** (CT-022, CT-028 — sem causa raiz, agente existe de fato) e **atraso de propagação entre mudança de status e efeito** (CT-036 — mesma natureza do achado do CT-034, mas CT-036 usa agente próprio/`agentTransitions`, não depende da cadeia do CT-033). **Gate explícito exigido** (correção de 07/10/2026, revisão do Codex): timeout **máximo e explícito** por tentativa de verificação (ex.: retry curto com teto fixo — não retry ilimitado); se o teto for excedido, **o teste falha de verdade** — não mascarar com espera maior nem considerar "passou porque retentou". A causa segue **sem raiz confirmada**: isto é uma hipótese de instabilidade de teste a validar na execução real, não um fato assumido. Se, ao rodar, o limite for excedido de forma consistente (não só uma vez), **tratar como achado de produto/consistência** (mesma categoria do CT-033/CT-034), não como flakiness a ignorar | CT-022, 028, 036 | Entrega 1/3 (mesmo padrão de agente) | CTs passando com o gate de timeout explícito no código; registrar quantas vezes o retry foi necessário (não só se passou) | Médio — se o teto for excedido com frequência na execução real, deixa de ser flakiness e vira achado de produto a resolver fora da automação |
| 5 | Resolver achados de **produto** antes de portar (precisam de decisão externa, não só de teste) | CT-033 (mecanismo de revogação de token não confirmado) e **CT-025, que compartilha a mesma pergunta** (ação de escrita com token antigo, mesma nota do CT-033). **CT-032 e CT-034 dependem do mesmo agente/sequência do CT-033** (`agentAtivoInativo`, ordem CT-020→033→032→034 no arquivo) — não são portáveis isoladamente enquanto CT-033 estiver em disputa. **CT-029/030 têm discrepância entre fontes**: o código lido não registra achado nenhum (espelham CT-023/024), mas o placar histórico da SGV-11971 lista os três (015, 029, 030, 033) como "falha/achado" — não resolvi essa discrepância, fica registrada pro Rafael decidir qual fonte vale | CT-025, 029, 030, 032, 033, 034 | Resposta de produto sobre CT-025/033; Rafael decidir a divergência de fonte do CT-029/030 | Decisão registrada antes de portar | Médio-alto — risco de portar uma asserção errada se a fonte errada for seguida, ou de quebrar a sequência de agente compartilhado |
| 6 | Trilha separada — seleção segura da instância 225 | Entender/desenhar como apontar o seed pra uma instância existente (225) com validação explícita do alvo, sem tocar no seed de verdade ainda | Nenhum CT — é infraestrutura de teste | DISC-001–003 (já concluído) | Proposta técnica revisada, sem execução | Baixo enquanto for só design; alto se pular pra execução sem validação do alvo |
| — | **Fora do escopo, candidatos futuros, sem porte previsto (não é entrega numerada)** | CT-016, CT-017 (desbloqueio, mutation nunca capturada) e CT-037 (auditoria, endpoint nunca confirmado) — bloqueio de produto/backend, não de automação | CT-016, 017, 037 | Captura de API/endpoint pelo time de produto/backend | — | — |

> **Regra aplicada nesta correção**: nenhum CT com achado/instabilidade documentada no código fica implícito num grupo "limpo" — ou vai pra uma entrega própria com gate explícito (4, hipótese de flakiness de teste, com teto de timeout e falha preservada se exceder), ou pra uma entrega de resolução externa (5, disputa/achado de produto). A distinção entre as duas: a Entrega 4 é algo que a própria automação tenta resolver com um limite claro (e se não resolver, vira achado, não é escondida); a Entrega 5 depende de alguém fora da automação decidir antes mesmo de tentar portar.

### O que esta recomendação não é

- Não é uma decisão de implementar — é uma recomendação pro Rafael aprovar, ajustar ou rejeitar.
- Não presume que a Alternativa A vai passar de primeira contra o ambiente atual — "já confirmado em Cypress" é evidência histórica, não garantia.
- Não resolve a seleção de instância/clienteId de forma geral — só recomenda não deixar isso bloquear o que já está pronto pra portar.
- Não rotula nenhum CT com achado conhecido como "limpo" — ver regra acima.
