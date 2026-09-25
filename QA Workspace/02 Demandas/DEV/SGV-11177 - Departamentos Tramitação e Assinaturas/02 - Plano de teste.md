---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — SGV-11177

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

Validar a tramitação e a solicitação de assinatura direcionadas a um membro específico de departamento e ao departamento como um todo, incluindo a regra de token bloqueado/liberado, as notificações duplas (pessoa + departamento), a exibição padronizada em tela e PDF, e o fluxo completo de assinatura externa por CPF (com e sem cadastro/vínculo prévio).

---

## Riscos e escopo

- **Risco principal:** a regra de token (bloqueado para departamento, liberado para membro) ser invertida ou aplicada de forma inconsistente entre os dois fluxos de assinatura.
- **Risco secundário:** o fluxo de pré-cadastro externo criar vínculo ou cadastro duplicado em caso de erro/reentrada — é o único ponto do requisito com criação de conta fora do fluxo tradicional.
- **Risco terciário:** a notificação dupla (membro + e-mail do departamento) perder um dos dois destinos em qualquer um dos dois fluxos de assinatura ou na tramitação.
- **Fora do escopo desta rodada:** os 6 pontos de conferência visual/textual fina do Figma (ver Pendências de decisão em `01 - Demanda`) — os CTs cobrem o comportamento funcional descrito; a validação pixel-a-pixel fica para quando o Figma for confirmado.

---

## Estratégia de teste

- **Unitário:** regra de token por tipo de signatário (departamento vs. membro); regra de vínculo único por pré-cadastro.
- **API/repositório:** persistência do vínculo tramitação↔membro↔departamento; disparo das notificações duplas; criação do pré-cadastro e do vínculo.
- **UI/E2E:** busca e seleção de membro/departamento, configuração de assinatura, os três sub-fluxos do acesso externo por CPF (vinculado, não vinculado, sem cadastro).
- **Regressão:** solicitação de assinatura para um signatário individual comum (fora de departamento) e encaminhamento de tramitação ao departamento inteiro (SGV-11184) continuam funcionando lado a lado com os novos fluxos.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-009\|CT-009]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-010\|CT-010]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-011\|CT-011]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-012\|CT-012]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-013\|CT-013]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-014\|CT-014]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-015\|CT-015]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-016\|CT-016]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-017\|CT-017]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-018\|CT-018]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-019\|CT-019]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-020\|CT-020]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-021\|CT-021]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-022\|CT-022]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-023\|CT-023]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-024\|CT-024]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-025\|CT-025]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-026\|CT-026]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-027\|CT-027]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-028\|CT-028]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-029\|CT-029]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-030\|CT-030]] | Funcional | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-031\|CT-031]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** build com a funcionalidade "Departamentos: Tramitação e assinaturas" disponível em ambiente de dev/hml, incluindo o fluxo externo de assinatura por CPF.
**Saída:** os 31 CTs executados e registrados em `04 - Validação dev`, com resultado geral definido (aprovado / reprovado / aprovado com ressalvas).
