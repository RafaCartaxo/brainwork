---
demanda: "[[01 - Demanda]]"
status: executado
responsavel: Rafael
pontos: ""
---

# Plano de teste — SGV-11971 (TR 1.24-1.25)

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[Automação/Plano de Automação|Plano]] · [[Automação/Handoff de execução|Handoff de execução]] · [[Automação/Documentação de Entrega|Documentação de Entrega]]

## Objetivo

Verificar, com cobertura automatizada e reproduzível, que o SOGOV atende aos 16 itens do Termo de Referência listados em [[01 - Demanda#Critérios de aceite]] — e registrar cada divergência encontrada como achado rastreável até o texto literal da regra.

## Riscos e escopo

- **Risco principal:** divergência entre o que a automação observa e o que a validação manual observa — já materializado no CT-015, ainda não resolvido.
- **Risco secundário:** instabilidade do ambiente HML, que já impediu 3 tentativas de experimento controlado e é a causa provável de parte das 6 falhas sem causa raiz.
- **Risco terciário:** o Termo tem itens de redação ambígua (1.25.3 × 1.27.10/1.27.11.2) — resolvidos por confirmação direta com o Rafael em 18/08/2026, registradas em [[01 - Demanda#Decisões de produto]].
- **Fora do escopo desta rodada:** acesso de servidor afastado no contexto de cidadão (CT-E01–E03).

## Estratégia de teste

- **API:** camada principal. As 5 suites são specs `*.api.cy.js` — autenticação, validação de credenciais, bloqueio, ciclo de vida e auditoria são todos verificáveis no contrato, sem depender de tela.
- **E2E:** um smoke de login só para garantir que o caminho pela interface não diverge do contrato.
- **Manual:** usado para contestar/confirmar achado da automação — foi o que expôs a divergência do CT-015.
- **Regressão:** a suíte inteira roda contra HML a cada rodada; nenhuma suíte é dada por boa sem validação manual prévia do cenário.

## Matriz de cobertura

A matriz critério ↔ CT vive em [[03 - Casos de teste#Matriz de cobertura]], gerada a partir do item do Termo que cada caso cita. São 16 critérios cobertos por 38 casos ativos.

## Entrada e saída

- **Entrada:** Termo de Referência do SOGOV (PDF original, itens até 1.26) e o backlog de casos herdado das 3 versões divergentes consolidadas em 31/08/2026.
- **Saída:** 38 casos ativos na Qase (projeto SGV, suite 4), suíte automatizada no repo `sogov-automation-test` e o registro de conformidade em [[04 - Validação dev]].

