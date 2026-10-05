---
tags: [qa, bug]
task: ""
pai: ""
tipo: "bug"
status: analise
ambiente: hml
prioridade: media
etapa_atual: "DEV · Análise técnica"
modulo: "integracoes-esic"
responsavel: Rafael
aguardando: "dev"
cadastrado_por: Rafael
data_inicio: 2026-10-05
data_fim: ""
pontos: ""
---
# Bug — Total de solicitações respondidas ausente no retorno de estatísticas

> [!info]- Navegação QA/DEV
> **Bug:** [[Bug/01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Bug | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ (reprovado) |

**Próximo passo:** dev investigar e corrigir; QA retesta em homologação após o fix.

Pacote para este Bug, achado durante a validação da [[../../SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]] (sem SGV próprio ainda):

```text
Bug Total De Solicitações Respondidas Ausente No Retorno De Estatísticas/
└── 00 QA/
    ├── 00 README.md
    ├── Bug/
    │   └── 01 - Bug.md
    ├── 03 - Casos de teste.md
    └── 04 - Validação dev.md
```

Sem `02 - Plano de teste.md` (bug simples, 1 critério) nem `05 - Preparação Qase.md` (prematuro — ainda não corrigido/validado).

## Histórico

- **2026-10-05:** 🐛 Bug confirmado (card criado) — achado comparando o retorno real da API e-SIC em homologação (cliente `prefeitura-de-cuite`) contra `novo-estatistica.json` (Retornos esperados), durante a validação da SGV-10736.
