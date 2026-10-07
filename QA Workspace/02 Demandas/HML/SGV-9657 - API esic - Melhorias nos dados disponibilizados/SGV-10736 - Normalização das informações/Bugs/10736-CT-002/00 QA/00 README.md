---
tags: [qa, bug]
task: "10736-CT-002"
pai: "10736"
tipo: "bug"
status: concluido
ambiente: hml
prioridade: media
etapa_atual: "Concluído"
modulo: "integracoes-esic"
responsavel: Rafael
aguardando: ""
cadastrado_por: Rafael
data_inicio: 2026-10-05
data_fim: ""
pontos: ""
---
# Bug — Tipo do solicitante não vem por extenso na listagem

> [!success] Fechado em 05/10/2026 — transferido pra Parte 2
> A SGV-10736 foi aprovada no Notion com este item explicitamente fora do ciclo: a correção virou o critério C14 da [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda|SGV-10735]] (Parte 2). O achado continua válido (campo realmente vem abreviado) — só a responsabilidade de correção/reteste migrou pra lá. Acompanhamento segue em [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda#^c14|C14]].

> [!info]- Navegação QA/DEV
> **Bug:** [[01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/04 - Validação dev]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Bug | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ (transferido pra Parte 2) |

**Próximo passo:** nenhum aqui — acompanhar pelo critério C14 da SGV-10735.

Pacote para este Bug, alocado dentro do próprio pacote da [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]] (sem SGV oficial ainda — numerado `10736-CT-002` pela melhoria de origem + o CT relacionado):

```text
10736-CT-002/
└── 00 QA/
    ├── 00 README.md
    ├── 01 - Bug.md
    ├── 03 - Casos de teste.md
    └── 04 - Validação dev.md
```

Sem `02 - Plano de teste.md` (bug simples, 1 critério) nem `05 - Preparação Qase.md` (prematuro — ainda não retestado).

## Histórico

- **2026-10-05:** 🐛 Bug confirmado (card criado) — achado comparando o retorno real da listagem (`"type": "PF"/"PJ"`) com o retorno real das estatísticas (`rankingRequesters[].type: "Pessoa Jurídica"`) e com o `novo-estatistica-atualizado.txt` (Retornos esperados atualizados), que usa o tipo por extenso.
- **2026-10-05:** 🔎 Confirmado pelo Rafael que a correção (listagem passar a retornar por extenso, igual às estatísticas) já está agendada no grupo "Parte 2" da call com os responsáveis.
- **2026-10-05:** 🔁 Fechado por transferência — SGV-10736 aprovada no Notion, correção virou critério C14 da SGV-10735.
