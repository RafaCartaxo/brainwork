---
tags: [qa, bug]
task: "10736-CT-011"
pai: "10736"
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
# Bug — Ranking de solicitantes exibe "Sem Nome" para Pessoa Jurídica cadastrada

> [!info]- Navegação QA/DEV
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/04 - Validação dev]]

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

Pacote para este Bug, alocado dentro do próprio pacote da [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]] (sem SGV oficial ainda — numerado `10736-CT-011` pela melhoria de origem + o CT relacionado):

```text
10736-CT-011/
└── 00 QA/
    ├── 00 README.md
    ├── 01 - Bug.md
    ├── 03 - Casos de teste.md
    └── 04 - Validação dev.md
```

Sem `02 - Plano de teste.md` (bug simples, 1 critério) nem `05 - Preparação Qase.md` (prematuro — ainda não corrigido/validado).

## Histórico

- **2026-10-05:** 🐛 Bug confirmado (card criado) — achado cruzando o retorno real de estatísticas (`rankingRequesters`) com o retorno real da listagem para o mesmo `id`, durante a validação da SGV-10736.
- **2026-10-05:** 🔎 Confirmado em call com os responsáveis que o problema também afeta solicitante Anônimo, não só PJ. Correção agendada pelo time (grupo "Parte 2" da call) — segue aberto, aguardando dev.
