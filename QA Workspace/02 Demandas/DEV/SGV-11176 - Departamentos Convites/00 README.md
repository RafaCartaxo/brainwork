---
status: analise
demanda: SGV-11176
tipo: funcionalidade
etapa_atual: "QA · Casos de teste"
---
# SGV-11176 — Departamentos: Convites

> [!info]- Navegação QA/DEV  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do card  
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Preparada |
| Plano de teste | ✅ Preparado |
| Casos de teste | ✅ Preparados (CT-001 a CT-014) |
| Validação | ⏳ Aguardando implementação do DEV |
| Preparação Qase | 📝 Rascunho (suite/projeto Qase ainda não confirmados) |

**Próximo passo:** confirmar `pontos_alocados` em `01 - Demanda` e rotear para o DEV.

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
