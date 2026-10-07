---
demanda: "[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — SGV-11178

> [!info]- Navegação QA  
> **Demanda:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda]]  
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/02 - Plano de teste]]  
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste]]  
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev]]  
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do plano de teste  
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar o atalho de cadastro rápido (PF, PJ e Departamento) nos componentes de seleção de pessoa, a navegação entre os três formulários sem perda de dados, as validações de CPF/CNPJ via API em cada tipo, e as regras transversais de duplicidade/falha/confirmação — sem regredir os fluxos de cadastro dedicados já existentes.

---

## Riscos e escopo

- **Risco principal:** o atalho selecionar/criar um registro incompatível com os parâmetros do campo de origem (ex.: campo só-PF aceitando um PJ recém-criado), ou não selecionar nada, forçando o servidor a buscar manualmente depois.
- **Risco secundário:** perda de dados preenchidos ao alternar entre os tipos de formulário (PF/PJ/Departamento) antes de confirmar; duplicidade de CPF/CNPJ/nome de departamento não bloqueada por diferença de maiúsculas/acentos/espaços (ponto em aberto no requisito de origem).
- **Fora do escopo desta rodada:** fluxo de cadastro dedicado (fora do atalho); regras de departamento além do cadastro em si (SGV-11083); conteúdo exato dos e-mails de notificação (pendência em `01 - Demanda`).

---

## Estratégia de teste

- **Unitário:** validação de formato de CPF/CNPJ antes da consulta à API; regra de campos obrigatórios por tipo de cadastro.
- **API/repositório:** consulta de CPF/CNPJ (preenchimento automático, falha, dado ausente), bloqueio de duplicidade (CPF/CNPJ/nome-e-mail de departamento), notificação por e-mail (PF e Departamento).
- **UI/E2E:** atalho disponível e consistente nos componentes de seleção, seletor de tipo (radio button), preservação de dados entre trocas, seleção automática do registro criado no campo de origem.
- **Regressão:** fluxos de cadastro dedicados de PF, PJ e Departamento (fora do atalho) continuam funcionando lado a lado com o cadastro rápido.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-002\|CT-002]] | Funcional | UI/E2E | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-004\|CT-004]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-005\|CT-005]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-006\|CT-006]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-007\|CT-007]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-008\|CT-008]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-009\|CT-009]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-010\|CT-010]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-011\|CT-011]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-012\|CT-012]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-013\|CT-013]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-014\|CT-014]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-015\|CT-015]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-016\|CT-016]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-017\|CT-017]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-018\|CT-018]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-019\|CT-019]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-020\|CT-020]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-021\|CT-021]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-022\|CT-022]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-023\|CT-023]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-024\|CT-024]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-025\|CT-025]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-026\|CT-026]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-027\|CT-027]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-028\|CT-028]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-029\|CT-029]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-030\|CT-030]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-031\|CT-031]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-032\|CT-032]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-033\|CT-033]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-034\|CT-034]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-035\|CT-035]] | Funcional | UI/API | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-036\|CT-036]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** build com a funcionalidade "Departamentos: Cadastro rápido" disponível em ambiente de dev/hml.
**Saída:** os 36 CTs executados e registrados em `04 - Validação dev`, com resultado geral definido (aprovado / reprovado / aprovado com ressalvas).
