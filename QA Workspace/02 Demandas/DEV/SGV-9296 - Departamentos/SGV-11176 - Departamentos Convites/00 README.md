---
status: analise
demanda: SGV-11176
tipo: funcionalidade
ambiente: dev
etapa_atual: "QA · Casos de teste"
---
# SGV-11176 — Departamentos: Convites

> [!info]- Navegação QA/DEV  
> **Demanda:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11176 - Departamentos Convites/01 - Demanda]]  
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11176 - Departamentos Convites/02 - Plano de teste]]  
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11176 - Departamentos Convites/03 - Casos de teste]]  
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11176 - Departamentos Convites/04 - Validação dev]]  
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11176 - Departamentos Convites/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do card  
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Preparada |
| Plano de teste | ✅ Preparado |
| Casos de teste | ✅ Preparados (CT-001 a CT-014) |
| Validação | ✅ 14/14 CTs aprovados — aprovação geral da task em DEV (02/10/2026), execução individual não registrada neste vault |
| Preparação Qase | 📝 Rascunho (suite/projeto Qase ainda não confirmados) |

**Próximo passo:** preparar os 14 CTs pra envio na Qase. Pendência aberta (revogação de convite, não coberta pelo requisito de origem) segue sem decisão, sem bloquear a aprovação geral.

> [!warning]- Escopo desta rodada  
> Cobre as 4 frentes do requisito de origem (Notion, Parte 3 da epic SGV-9296): link permanente do departamento, link temporário gerado por servidor, entrada no departamento pelo convite (com ou sem cadastro prévio) e filtro de solicitações por perfil/departamento.

Pacote QA para `SGV-11176`:

```text
SGV-11176 - Departamentos Convites/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---
