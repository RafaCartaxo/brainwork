---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — SGV-9982

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do plano de teste  
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar que a preferência "Permanecer no documento após encerrar" funciona corretamente nos três dialogs de encerramento (documento inteiro, setor, participação própria), é persistida por usuário e não altera nenhuma regra de tramitação existente.

---

## Riscos e escopo

- **Risco principal:** regressão nas regras de encerramento (permissão, efeito por tipo, reabertura, histórico) — não são o alvo da mudança, mas podem ser afetadas por engano ao mexer no fluxo pós-confirmação.
- **Risco secundário:** a preferência ser tratada por sessão/dispositivo em vez de por usuário (quebraria C6/C7/RNF03/RNF04).
- **Fora do escopo desta rodada:** acessibilidade (RNF07), variante mobile (RNF08) e verificação de que a gravação não entra no histórico do documento (RNF05) — ficam para uma rodada seguinte, junto com o requisito condicional RF11 (pendência 1, ver `01 - Demanda`).

---

## Estratégia de teste

- **Unitário:** regra de gravação/leitura da preferência do usuário (uma preferência única, não por setor).
- **API/repositório:** persistência da preferência entre sessões e dispositivos.
- **UI/E2E:** comportamento dos três dialogs — estado do checkbox, confirmação, cancelamento, recarregamento do documento.
- **Regressão:** isolamento entre usuários do mesmo setor; nenhuma automação de regressão de tramitação nova é criada aqui — o plano assume a suíte de regressão existente para permissão/efeito/reabertura, que não é alterada por esta melhoria.

Camada não aplicável nesta rodada: acessibilidade e mobile dedicados (ficam para a rodada seguinte, junto com RNF05/RNF07/RNF08).

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Regressão | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Funcional | UI/E2E | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Funcional | UI/API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-009\|CT-009]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-010\|CT-010]] | Regressão | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-011\|CT-011]] | Regressão | API | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-012\|CT-012]] | Funcional | UI | Manual | [[04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** build com a feature "Permanecer no documento após encerrar" disponível em ambiente de dev/hml, para os três tipos de encerramento.
**Saída:** os 12 CTs executados e registrados em `04 - Validação dev`, com resultado geral definido (aprovado / reprovado / aprovado com ressalvas).
