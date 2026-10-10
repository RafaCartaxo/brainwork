---
status: analise
demanda: SGV-11177
tipo: funcionalidade
ambiente: dev
etapa_atual: "QA · Casos de teste"
---
# SGV-11177 — Departamentos: Tramitação e assinaturas

> [!info]- Navegação QA/DEV  
> **Demanda:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda]]  
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/02 - Plano de teste]]  
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste]]  
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/04 - Validação dev]]  
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/05 - Preparação Qase]]
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
| Validação | ✅ 36/36 CTs aprovados (6 defeitos encontrados e corrigidos — ver `Defeitos/`) — restam 6 pendências de conferência fina no Figma |
| Preparação Qase | 📤 Enviado (36 casos + 3 shared steps na suite SGV/360, 30/09/2026) |

**Próximo passo:** conferência fina no Figma das 6 pendências pendentes.

> [!warning]- Escopo desta rodada  
> Cobre as 7 frentes do requisito de origem (Notion, Parte 4 da epic SGV-9296): tramitação para membro de departamento (busca, notificação, exibição em tela e em PDF), assinatura solicitada ao departamento inteiro, assinatura solicitada a um membro específico, e o fluxo de assinatura externa por CPF (com pré-cadastro). Este requisito **confirma e formaliza** o que o `Complemento Figma - Departamento Destinatário E Signatário` (arquivado em `DEV/SGV-9296 - Departamentos/Conhecimento/`) já tinha antecipado como escopo futuro da epic em 03/09/2026.

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
