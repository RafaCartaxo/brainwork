---
tags: [qa]
task: "10735"
pai: "9657"
tipo: "funcionalidade"
status: concluido
ambiente: dev
prioridade: media
etapa_atual: "Concluído"
modulo: "integracoes-esic"
responsavel: Rafael
aguardando: ""
cadastrado_por: Rafael
data_inicio: 2026-10-05
data_fim: "2026-10-06"
pontos: ""
---
# SGV-10735 — Criação da feature de Integrações (API e-SIC)

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ |
| Plano de teste | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ **Aprovado** (06/10/2026) — 14/14 CTs aprovados |
| Preparação Qase | ⏳ Pendente de envio (falta confirmar `qase_suite_id`) |

**Próximo passo:** confirmar `qase_suite_id` e enviar os 14 CTs pra Qase.

Pacote para `SGV-10735`, parte de [[../Conhecimento/0 - SGV-9657 - Índice|SGV-9657 (epic)]]:

```text
SGV-10735 - Criação da feature de integrações/
└── 00 QA/
    ├── 00 README.md
    ├── 01 - Demanda.md
    ├── 02 - Plano de teste.md
    ├── 03 - Casos de teste.md
    ├── 04 - Validação dev.md
    └── 05 - Preparação Qase.md
```

Sem `01 Automação/` por enquanto (sem cobertura automatizada ainda).

## Histórico

- **2026-10-05:** card criado a partir da descrição da SGV-10735 no Notion, do doc "Gerenciamento de clientes SOGOV" (seção Integrações — API e-SIC) e da confirmação da call de 05/10/2026 de que o front-end é a próxima frente de trabalho. Demanda, critérios e CTs definidos; execução real ainda não iniciou (sem ambiente de teste disponível até o momento).
- **2026-10-05:** adicionado C14 (tipo do solicitante por extenso na listagem) — correção herdada da SGV-10736 (achado [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/00 README|10736-CT-002]]), confirmado na versão final da task no Notion. SGV-10736 aprovada com esse item explicitamente transferido pra cá.
- **2026-10-06:** ✅ Execução real concluída pelo Rafael — **14/14 CTs aprovados**, incluindo o CT-014 (reteste do achado da SGV-10736, confirmado corrigido: `requester.type` agora vem por extenso na listagem). Evidência em `Evidências/Desenvolvimento/10735 - integrações e-SIC aprovadas.mp4`.
