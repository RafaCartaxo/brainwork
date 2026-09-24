---
status: analise
demanda: SGV-9982
tipo: melhoria
etapa_atual: "QA · Casos de teste"
---
# SGV-9982 — Permanecer no documento após encerrar

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
| Demanda | ✅ Preparada (pendência RF11 em aberto) |
| Plano de teste | ✅ Preparado |
| Casos de teste | ✅ Preparados (CT-001 a CT-011) |
| Validação | ⏳ Aguardando implementação do DEV |
| Preparação Qase | 📝 Rascunho (suite/projeto Qase ainda não confirmados) |

**Próximo passo:** decidir a pendência do RF11 e confirmar `projeto`/`pontos_alocados` em `01 - Demanda`; depois rotear para o DEV.

> [!warning]- Escopo desta rodada  
> Cobre o núcleo funcional (CT-001 a CT-011): estado do checkbox, redirecionamento, persistência por usuário e entre sessões. Ficam para uma rodada seguinte: copy/estilo exato dos dialogs (C9), acessibilidade (RNF07), variante mobile (RNF08) e verificação de histórico (RNF05) — bem como o requisito condicional RF11.

Pacote QA para `SGV-9982`:

```text
SGV-9982 - Permanecer no documento após encerrar/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---
