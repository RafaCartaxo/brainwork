---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — SGV-11176

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle do plano de teste  
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar os dois caminhos de convite para entrada em departamento (link permanente do departamento e link temporário gerado por servidor), o fluxo de entrada pelo convite com e sem cadastro prévio, e o filtro de solicitações por perfil/departamento — sem regredir o vínculo manual já coberto pela SGV-11083.

---

## Riscos e escopo

- **Risco principal:** um link temporário aceitar mais de um cadastro ou não expirar de fato em 7 dias — quebraria a regra central de RF02.
- **Risco secundário:** o filtro de solicitações vazar dados entre departamentos diferentes, ou entre o perfil pessoal e um departamento.
- **Fora do escopo desta rodada:** revogação manual de convite (pendência em `01 - Demanda`), performance de geração de link em massa.

---

## Estratégia de teste

- **Unitário:** regra de expiração (7 dias) e de uso único do link temporário.
- **API/repositório:** persistência de quem gerou o convite e de quem se cadastrou por ele; filtro de solicitações por departamento.
- **UI/E2E:** geração dos dois tipos de link, cópia para área de transferência, fluxo de entrada com e sem cadastro, seletor de perfil.
- **Regressão:** vínculo manual de participante (SGV-11083) continua funcionando lado a lado com a entrada por convite.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-009\|CT-009]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-010\|CT-010]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-011\|CT-011]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-012\|CT-012]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-013\|CT-013]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-014\|CT-014]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** build com a funcionalidade "Departamentos: Convites" disponível em ambiente de dev/hml.
**Saída:** os 14 CTs executados e registrados em `04 - Validação dev`, com resultado geral definido (aprovado / reprovado / aprovado com ressalvas).
