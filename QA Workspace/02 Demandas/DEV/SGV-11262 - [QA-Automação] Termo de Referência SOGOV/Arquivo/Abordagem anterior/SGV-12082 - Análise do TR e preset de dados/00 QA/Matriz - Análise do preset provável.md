---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11262
tipo: matriz-analise
status: em levantamento
---
# Matriz — análise do preset provável para o TR

> [!info] Propósito
> Esta matriz vai da regra/caso aos dados e ao mecanismo atual de preparação. Ela deve orientar a recomendação do preset inicial; não é um catálogo geral do SOGOV nem uma especificação aprovada de seed.
>
> **Fonte funcional:** [[../../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste|38 CTs da SGV-11971]] · **Demanda:** [[01 - Demanda]] · **Plano:** [[02 - Plano de teste]] · **Roadmap:** [[../../Roadmap - Automação TR|Automação TR]]

> [!tip] Esta nota é um índice (reorganizado em 08/10/2026)
> O conteúdo detalhado das verificações DISC-001–004 foi movido pra notas próprias, pra manter esta página curta. Nenhum conteúdo, evidência ou achado foi alterado — só reorganizado. Ver "Análises detalhadas" abaixo.

## Como preencher

- Use uma linha por CT quando as pré-condições ou dados diferirem; agrupe apenas quando ator, estado e preparação forem iguais.
- Para cada afirmação, registre a fonte (caso, arquivo, configuração ou execução existente).
- Use **Confirmado**, **Inferido** ou **A confirmar**. Não transforme lacuna em fato.
- Não copiar valores secretos. Registre apenas nomes de variáveis/chaves e onde a configuração deve ser verificada.

## Legenda de estado do conhecimento

| Estado | Significado |
|---|---|
| Confirmado | Visível diretamente no CT/código/documento ou em execução já registrada |
| Inferido | Interpretação provável que ainda precisa de validação |
| A confirmar | Evidência ausente, ambiente inacessível ou comportamento não verificado |

## Visão rápida

| Verificação | O que cobre | Situação | Onde está o detalhe |
|---|---|---|---|
| DISC-001 — Arquitetura | Auditoria do projeto Playwright (config, seed, manifesto, fixtures/pools), reconciliada contra o commit `16c41e4` | Concluído, 0 divergências contra o mapa existente | Seção própria em [[../01 Automação/01 - Plano de automação#DISC-001 — Auditoria do projeto, reconciliada com o código (07/10/2026)\|01 - Plano de automação]] |
| DISC-002 — Cobertura do TR e dos 38 CTs | TR completo (1.1–1.43) classificado; 38/38 CTs rastreados (13 Playwright, 22 Cypress em branch não mesclado, 3 sem código) | Concluído | [[DISC-002 - Cobertura do TR e rastreabilidade dos CTs]] |
| DISC-003 — Dados, preparação e eixos | Mapa de reuso por dado/estado; eixos ambiente×instância separados; pressupostos e perguntas em aberto | Concluído | [[DISC-003 - Dados, preparação e eixos]] |
| DISC-004 — Alternativas e recomendação | Comparação de alternativas, recomendação e 6 entregas candidatas sequenciadas | Concluído — aguardando revisão final do Rafael | [[DISC-004 - Alternativas e recomendação]] |
| Fluxo do preset | Diagrama Mermaid do fluxo atual (Playwright/Cypress) e da direção candidata | Novo (08/10/2026) | [[Fluxo - Preset de dados]] |

**Achado-resumo mais importante** (ver detalhe no DISC-003): Playwright e Cypress resolvem a instância pelo **mesmo nome fixo** (`"E2E Automatic Test"`), mas a **identidade real do alvo nunca foi comparada** entre os dois `.env`/`cypress.env*.json` — nome igual não é prova de instância real igual. Nenhum dos dois frameworks tem hoje parâmetro de `clienteId`/instância alternativa.

**Recomendação em uma frase** (ver detalhe no DISC-004): portar pro Playwright os mecanismos de estado já confirmados em Cypress (`changePublicAgentWorkStatus`, `createIsolatedTestAgent`), mantendo a instância fixa atual, em 6 entregas pequenas e sequenciadas; seleção segura da instância 225 fica como trilha separada e posterior, não bloqueante.

## Análises detalhadas

- **DISC-001 — Auditoria do projeto:** permanece como seção própria em [[../01 Automação/01 - Plano de automação#DISC-001 — Auditoria do projeto, reconciliada com o código (07/10/2026)|01 - Plano de automação]] (não foi extraída pra esta pasta — é a mesma camada do Plano, não da Matriz).
- **DISC-002 — Cobertura do TR completo (1.1–1.43) e rastreabilidade dos 38 CTs:** [[DISC-002 - Cobertura do TR e rastreabilidade dos CTs]].
- **DISC-003 — Dois eixos (ambiente×instância), dados reutilizáveis, pressupostos e perguntas em aberto:** [[DISC-003 - Dados, preparação e eixos]].
- **DISC-004 — Alternativas comparadas, recomendação e as 6 entregas candidatas:** [[DISC-004 - Alternativas e recomendação]].
- **Fluxo visual (Mermaid) do preset atual e da direção candidata:** [[Fluxo - Preset de dados]].
