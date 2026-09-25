---
status: analise
demanda: SGV-11177
tipo: funcionalidade
etapa_atual: "QA · Casos de teste"
---
# SGV-11177 — Departamentos: Tramitação e assinaturas

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
| Casos de teste | ✅ Preparados (CT-001 a CT-031) |
| Validação | ⏳ Aguardando implementação do DEV |
| Preparação Qase | 📝 Rascunho (suite/projeto Qase ainda não confirmados) |

**Próximo passo:** confirmar `pontos_alocados` em `01 - Demanda` e rotear para o DEV.

> [!warning]- Escopo desta rodada  
> Cobre as 7 frentes do requisito de origem (Notion, Parte 4 da epic SGV-9296): tramitação para membro de departamento (busca, notificação, exibição em tela e em PDF), assinatura solicitada ao departamento inteiro, assinatura solicitada a um membro específico, e o fluxo de assinatura externa por CPF (com pré-cadastro). Este requisito **confirma e formaliza** o que o `Complemento Figma - Departamento Destinatário E Signatário` (arquivado em `Concluídas/9296/Conhecimento/`) já tinha antecipado como escopo futuro da epic em 03/09/2026.

Pacote QA para `SGV-11177`:

```text
SGV-11177 - Departamentos Tramitação e Assinaturas/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
└── 05 - Preparação Qase.md
```

---
