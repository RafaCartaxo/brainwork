---
tags: [qa]
task: "11958"
pai: ""
tipo: "melhoria"
status: backlog
ambiente: dev
prioridade: media
etapa_atual: "QA · Triagem"
modulo: servicos-pj
responsavel: ""
aguardando: ""
cadastrado_por: ""
data_inicio: 2026-10-01
data_fim: ""
pontos: ""
---
# SGV-11958 — Cadastro rápido de PJ passa a solicitar e-mail

> [!info]- Navegação QA/DEV
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | 🔵 Em análise (pendências de decisão em aberto) |
| Plano de teste | ⏳ |
| Casos de teste | ⏳ |
| Validação | ⏳ |
| Preparação Qase | ⏳ |
| Automação | ⏳ |

**Próximo passo:** confirmar com produto/DEV os detalhes do campo de e-mail (obrigatoriedade, validação, link do protótipo atualizado no Figma) antes de detalhar critérios e CTs.

> [!info]- Origem
> Nasceu do fechamento do defeito [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]] (CT-029/C29 da SGV-11178): em vez do fallback originalmente esperado (Razão Social + CNPJ) pra PJ sem Nome fantasia, produto decidiu redesenhar a identificação da PJ no cadastro rápido, acrescentando um campo de e-mail — protótipo já atualizado no Figma.

Pacote para `SGV-11958`:

```text
SGV-11958 - Departamentos Cadastro Rápido E-mail PJ/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---
