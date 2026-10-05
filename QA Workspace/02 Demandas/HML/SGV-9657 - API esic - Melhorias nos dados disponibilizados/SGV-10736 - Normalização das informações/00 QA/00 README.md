---
tags: [qa]
task: "10736"
pai: "9657"
tipo: "melhoria"
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
# SGV-10736 — Normalizar os campos retornados pela API e-SIC

> [!info]- Navegação QA/DEV
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda/Bug | ✅ |
| Plano de teste | ✅ |
| Casos de teste | ✅ |
| Validação | ✅ **Aprovado** (com ressalvas) |
| Preparação Qase | ⏳ |

**Próximo passo:** SGV-10736 aprovada no Notion (05/10/2026). C2 (tipo abreviado) corrigido como critério C14 da [[../../SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda|SGV-10735]] — Bug [[../Bugs/10736-CT-002/00 QA/00 README|10736-CT-002]] encerrado por transferência. C5 (data limite sem prazo configurado) segue pendente de decisão do Marcos em SGV-12019 (Parte 3, ainda vazia) — Bug [[../Bugs/10736-CT-007/00 QA/00 README|10736-CT-007]] continua aberto. Bug de paginação reportado como já corrigido pelo dev — pendente reverificar.

Pacote para `SGV-10736`, parte de [[../../Conhecimento/0 - SGV-9657 - Índice|SGV-9657 (epic)]]:

```text
SGV-10736 - Normalização das informações/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de teste.md
│   ├── 03 - Casos de teste.md
│   ├── 04 - Validação dev.md
│   └── 05 - Preparação Qase.md
└── Bugs/                        (achados em homologação, sem SGV ainda — numerados <melhoria>-CT-<NN> pelo CT de origem)
    ├── 10736-CT-002/00 QA/...   (tipo do solicitante abreviado na listagem — fechado, transferido pra SGV-10735 C14)
    ├── 10736-CT-007/00 QA/...   (orderDateDeadline não calculada sem prazo — aberto)
    ├── 10736-CT-010/00 QA/...   (totalAnswered ausente — fechado 05/10/2026, requisito retirado)
    └── 10736-CT-011/00 QA/...   (ranking exibe Sem Nome para PJ e Anônimo — aberto, correção agendada)
```

Sem `01 Automação/` por enquanto. `Bugs/` aqui cumpre o papel que `Defeitos/` cumpriria numa Melhoria com esteira DEV — como a SGV-10736 valida direto em HML (fluxo 3f), o achado é tecnicamente Bug, não Defeito, mas fica alocado dentro do próprio pacote por decisão do Rafael (05/10/2026), não solto em `02 Demandas/HML/`.

## Histórico

- **2026-10-05:** card criado a partir da descrição da SGV-9657/SGV-10736 no Notion e dos retornos esperados (novos) já fornecidos (`novo-documentos.json`, `novo-estatistica.json`). CTs definidos e prontos para execução em homologação.
- **2026-10-05:** ✅ SGV-10736 aprovada no Notion. C2 corrigido na Parte 2 (SGV-10735, C14); C5 pendente de decisão do Marcos em SGV-12019 (Parte 3, ainda vazia).
