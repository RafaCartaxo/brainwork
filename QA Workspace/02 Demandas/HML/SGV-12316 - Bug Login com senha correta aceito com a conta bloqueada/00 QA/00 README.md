---
tags: [qa, bug]
task: "12316"
pai: ""
tipo: "bug"
status: backlog
ambiente: hml
prioridade: alta
etapa_atual: "DEV · Análise técnica"
modulo: "login"
responsavel: Rafael
aguardando: "dev"
cadastrado_por: Rafael
data_inicio: 2026-10-20
data_fim: ""
pontos: ""
---
# SGV-12316 — Bug Login com senha correta aceito com a conta bloqueada

> [!info]- Navegação QA/DEV
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/01 - Bug|01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/03 - Casos de teste|03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/04 - Validação dev|04 - Validação dev]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Bug | ✅ |
| Casos de teste | ✅ |
| Validação | ⏳ aguardando correção |

**Próximo passo:** aguardar correção do dev; depois executar os 5 CTs em DEV e HML.

Pacote para `SGV-12316`:

```text
SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/
└── 00 QA/
    ├── 00 README.md
    ├── 01 - Bug.md
    ├── 03 - Casos de teste.md
    └── 04 - Validação dev.md
```

Sem `02 - Plano de teste.md` (bug com critérios diretos) nem `05 - Preparação Qase.md` (prematuro — ainda não retestado).

## Histórico

- 2026-10-20 - 🐛 Bug cadastrado (reproduzido em homologação)
