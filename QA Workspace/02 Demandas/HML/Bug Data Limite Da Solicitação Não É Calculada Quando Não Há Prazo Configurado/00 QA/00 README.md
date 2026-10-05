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
# Bug — Data limite da solicitação não é calculada quando não há prazo configurado

> [!info]- Navegação QA/DEV
> **Bug:** [[Bug/01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> [!warning] Primeiro Bug do vault no modelo de pacote (00 QA/)
> Até 05/10/2026 todo Bug real do vault usava nota única (1 `.md` em `QA/`, CT-B0x embutido) — a doc (`SKILL_BUGS.md`) descreve pacote desde 24/09/2026, mas sem nenhum precedente aplicado. Rafael decidiu seguir a doc aqui. Sinalizar a divergência doc×prática continua pendente de reconciliação.

## Status do trabalho

| Etapa | Estado |
|---|---|
| Bug | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ (reprovado) |

**Próximo passo:** dev investigar e corrigir; QA retesta em homologação após o fix.

Pacote para este Bug, achado durante a validação da [[../../SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]] (sem SGV próprio ainda):

```text
Bug Data Limite Da Solicitação Não É Calculada Quando Não Há Prazo Configurado/
└── 00 QA/
    ├── 00 README.md
    ├── Bug/
    │   └── 01 - Bug.md
    ├── 03 - Casos de teste.md
    └── 04 - Validação dev.md
```

Sem `02 - Plano de teste.md` (bug simples, 1 critério) nem `05 - Preparação Qase.md` (prematuro — ainda não corrigido/validado).

## Histórico

- **2026-10-05:** 🐛 Bug confirmado (card criado) — achado comparando o retorno real da API e-SIC em homologação (cliente `prefeitura-de-cuite`) contra `novo-documentos.json` (Retornos esperados), durante a validação da SGV-10736.
