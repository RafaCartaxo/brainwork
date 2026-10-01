---
status: analise
demanda: SGV-11178
tipo: funcionalidade
etapa_atual: "QA · Casos de teste"
---
# SGV-11178 — Departamentos: Cadastro rápido

> [!info]- Navegação QA/DEV  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do card  
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Preparada |
| Plano de teste | ✅ Preparado |
| Casos de teste | ✅ Preparados (CT-001 a CT-036) |
| Validação | 🔵 Em andamento — 28/37 CTs aprovados (CT-029 fechado por decisão de produto — ver `Defeitos/SGV-11957`, descartado) e 9 aguardando execução |
| Preparação Qase | 📝 Rascunho (suite/projeto Qase ainda não confirmados) |

**Próximo passo:** confirmar `pontos_alocados` em `01 - Demanda` e rotear para o DEV.

> [!warning]- Escopo desta rodada  
> Cobre o atalho de cadastro rápido (PF, PJ e Departamento) embutido nos componentes de seleção de pessoa (requisito de origem, Parte 5 da epic SGV-9296) — não cobre os fluxos de cadastro dedicados, nem as regras de departamento fora do cadastro em si (SGV-11083), convite (SGV-11176) ou tramitação/assinatura (SGV-11177).

Pacote QA para `SGV-11178`:

```text
SGV-11178 - Departamentos Cadastro Rápido/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---
