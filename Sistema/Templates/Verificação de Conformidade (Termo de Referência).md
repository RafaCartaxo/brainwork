---
tags:
  - demanda
  - qa
  - funcionalidade
  - termo-de-referencia
task: ""
pai: ""
status: em andamento
prioridade: media
data_inicio: <% tp.date.now("YYYY-MM-DD") %>
data_fim:
responsavel:
modulo:
---
# Demanda: Verificação de Conformidade — TR {{número}} ({{assunto curto}})

> [!info] Informações
> - **Tipo:** Funcionalidade (verificação de conformidade com Termo de Referência) — task **pai**, guarda-chuva das partes abaixo
> - **Responsável QA:**
> - **Vault:** link pro Handoff Geral do Termo (se existir) · link pra pasta do Termo

---

> [!abstract] Resumo

Verificação de conformidade do Sogov com o Termo de Referência {{número}} ({{assunto}}). Task pai, decomposta em partes sequenciais — cada parte pode virar uma task própria mais adiante (SGV separado); enquanto não vira, fica registrada aqui como seção.

---

## Partes

*Padrão reaproveitável pra qualquer Termo de Referência — ajustar/remover partes conforme o escopo real.*

| Parte | O que cobre | Status |
|---|---|---|
| 1. Análise | Leitura do Termo original, extração dos itens/requisitos, primeira formalização dos casos de teste (rascunho inicial, ainda não consolidado) | |
| 2. Casos de teste | Consolidação/padronização dos CTs numa fonte única no vault (Dado/Quando/Então + Prioridade + Requisito + Citação do Termo) | |
| 3. Sincronização com a Qase | Alinhar os CTs no projeto da Qase — criar/atualizar/excluir casos, mantendo o vault como fonte de verdade | |
| 4. Automação | Cobertura automatizada (Cypress, repo `sogov-automation-test`) dos CTs, validada contra HML | |

---

## Parte 1 — Análise

*O que foi lido/entendido do Termo antes de qualquer CT existir; de onde vieram os rascunhos originais.*

## Parte 2 — Casos de teste

*Resumo + link pra nota de detalhe, se existir uma dedicada.*

## Parte 3 — Sincronização com a Qase

*Resumo + link pra nota de detalhe, se existir uma dedicada.*

## Parte 4 — Automação

*Resumo + link pro handoff de execução e pro repo de automação, se essa parte já tiver o próprio detalhamento.*

---

> [!warning] Pontos de atenção

---

## Histórico

- DD/MM/AAAA - Parte 1 (Análise) concluída
- DD/MM/AAAA - Parte 2 (Casos de teste) concluída
- DD/MM/AAAA - Parte 3 (Sincronização Qase) concluída
- DD/MM/AAAA - Parte 4 (Automação) iniciada
