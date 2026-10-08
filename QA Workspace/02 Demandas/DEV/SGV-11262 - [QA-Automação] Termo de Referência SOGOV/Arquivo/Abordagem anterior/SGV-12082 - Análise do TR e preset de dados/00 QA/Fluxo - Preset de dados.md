---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11262
tipo: fluxo
---

# Fluxo — Preset de dados (Playwright, Cypress e direção candidata)

> [!info]- Navegação
> **Índice/resumo:** [[Matriz - Análise do preset provável]] · **DISC-001 (arquitetura):** [[../01 Automação/01 - Plano de automação#DISC-001 — Auditoria do projeto, reconciliada com o código (07/10/2026)|Plano de automação]] · **DISC-002:** [[DISC-002 - Cobertura do TR e rastreabilidade dos CTs]] · **DISC-003:** [[DISC-003 - Dados, preparação e eixos]] · **DISC-004:** [[DISC-004 - Alternativas e recomendação]]

> [!warning] Nenhuma execução ou teste foi feito nesta análise
> Este fluxo é uma **síntese visual** do que DISC-001–004 já confirmaram por leitura de código (commits `16c41e4` e `bdf5e9a`) + do que o DISC-004 recomenda. Nenhum comando foi rodado, nenhuma configuração foi alterada, nenhuma instância foi criada ou selecionada pra produzir este diagrama. Linhas sólidas = confirmado/atual (DISC-001–003). Linhas tracejadas = candidato/futuro, ainda não implementado (DISC-004).

## Diagrama

```mermaid
flowchart TD
    subgraph PW["Playwright — fluxo atual (CONFIRMADO, commit 16c41e4)"]
        PW1["playwright.config.ts<br/>projects: infrastructure → seed → e2e/version/api"] --> PW2["Resolução da instância<br/>BASELINE.instance.name = 'E2E Automatic Test'<br/>(nome fixo, getInstanceOrCreate)"]
        PW2 --> PW3["Seed / reconciliação<br/>provisionBaseline: instância → setores → módulos →<br/>serviços → subsetores → servidores → cidadãos → workflows<br/>(idempotente por identidade natural)"]
        PW3 --> PW4["Manifesto por execução<br/>.runtime/&lt;runId&gt;/seed-manifest.json<br/>SEED_SCHEMA_VERSION = 12"]
        PW4 --> PW5["Pool por worker<br/>bindWorkerActors troca agents.agent/citizens.citizen<br/>pelo slot do parallelIndex"]
        PW5 --> PW6["13 CTs Playwright<br/>CT-001–012, CT-038"]
    end

    subgraph CY["Cypress — fluxo atual (CONFIRMADO, branch não mesclado bdf5e9a)"]
        CY1["cypress.env*.json + cypress/support/e2e.js"] --> CY2["Resolução da instância<br/>instanceName = 'E2E Automatic Test'<br/>(MESMO NOME FIXO do Playwright)"]
        CY2 --> CY3["Preparação por cenário<br/>createIsolatedTestAgent (agente dedicado)<br/>+ changePublicAgentWorkStatus (mutação de status)"]
        CY3 --> CY4["Manifesto fixo e único<br/>cypress.env.set.json<br/>(sobrescrito a cada run, sem isolamento por runId)"]
        CY4 --> CY5["25 CTs Cypress — Suítes 3/4<br/>CT-013–037 (22 com código; 016/017/037 sem código)"]
    end

    PW2 -.->|"mesmo NOME; identidade real do alvo NÃO comparada"| CY2

    subgraph FUT["Direção candidata — NÃO implementado (CANDIDATO/FUTURO, recomendação DISC-004)"]
        F1["Portar changePublicAgentWorkStatus +<br/>createIsolatedTestAgent pro Playwright<br/>(mantendo a instância fixa atual — Entregas 1–5)"]
        F2["Validação pelos próprios CTs portados<br/>(sem execução ainda nesta análise)"]
        F3["Trilha separada e posterior (Entrega 6):<br/>seleção segura da instância 225<br/>NÃO selecionada hoje por nenhum framework"]
    end

    CY3 -.->|"portar mecanismo já confirmado"| F1
    F1 -.-> F2
    F2 -.->|"trilha independente, não bloqueante"| F3
```

## Como ler

- **Subgraph `PW` (Playwright) e `CY` (Cypress)**: cada etapa e seta sólida corresponde a algo lido diretamente no código — ver [[DISC-002 - Cobertura do TR e rastreabilidade dos CTs|DISC-002]] (quais CTs, qual arquivo) e [[DISC-003 - Dados, preparação e eixos|DISC-003]] (dados/config por etapa).
- **Seta tracejada entre `PW2` e `CY2`**: os dois frameworks resolvem a instância pelo **mesmo nome fixo** (`"E2E Automatic Test"`), mas isso **não prova que é a mesma instância real** — a identidade do alvo (backend/registro) nunca foi comparada entre os dois `.env`/`cypress.env*.json` (achado do DISC-003). O nome igual é uma coincidência de código, não uma evidência de infraestrutura compartilhada.
- **Subgraph `FUT` (direção candidata)**: nada aqui existe hoje. É a recomendação do [[DISC-004 - Alternativas e recomendação|DISC-004]] — portar pro Playwright os mecanismos já confirmados em Cypress, mantendo a instância atual, em 6 entregas pequenas e sequenciadas. A seleção da instância 225 (`F3`) é **a última etapa, não a primeira**, e está desenhada aqui só como destino de uma trilha separada — **não como algo já selecionado ou em andamento**.
- Nenhuma caixa deste diagrama representa execução real nesta análise; todas as setas "confirmado" vêm de leitura de código, não de rodar o automação.
