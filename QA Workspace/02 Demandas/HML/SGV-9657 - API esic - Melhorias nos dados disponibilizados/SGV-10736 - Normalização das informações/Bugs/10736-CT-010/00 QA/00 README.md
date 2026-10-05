---
tags: [qa, bug]
task: "10736-CT-010"
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
# Bug — Total de solicitações respondidas ausente no retorno de estatísticas

> [!success] Fechado em 05/10/2026 — requisito retirado do contrato, não é mais um bug a corrigir
> Confirmado em call com os responsáveis: o sistema **não tem** status "Respondido" — `orderStatus` deriva do andamento interno do documento (tramitação), não do fato de já ter sido respondido ao cidadão. Marcos decidiu remover `totalAnswered`/"Respondido" do contrato da SGV-10736 (C7, e a parte de C6 que citava "Respondido"). O campo realmente não vem na API (o achado original estava correto) — só deixou de ser um defeito a corrigir, porque a exigência em si foi retirada.

> [!info]- Navegação QA/DEV
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/04 - Validação dev]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Bug | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ (requisito retirado) |

**Próximo passo:** nenhum — requisito retirado do contrato, nada a corrigir ou retestar.

Pacote para este Bug, alocado dentro do próprio pacote da [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]] (sem SGV oficial ainda — numerado `10736-CT-010` pela melhoria de origem + o CT relacionado):

```text
10736-CT-010/
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
- **2026-10-05:** 🗑️ Fechado como requisito retirado — call com os responsáveis confirmou que o sistema não tem status "Respondido" (decisão de Marcos). Não é mais critério de aceite da SGV-10736 (C7).
