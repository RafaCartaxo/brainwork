---
tags:
  - demanda
  - qa
  - funcionalidade
  - termo-de-referencia
  - autenticacao
task: ""
status: em andamento
prioridade: media
data_inicio: 2026-08-31
responsavel: Rafael
modulo: autenticacao
---
# Demanda: Verificação de Conformidade — TR 1.24-1.25 (Autenticação e ciclo de vida do usuário)

> [!warning] Rascunho — falta o número da task (SGV)
> Criado retroativamente pra virar a task **pai** do trabalho já feito. Precisa ser cadastrado na ferramenta externa (Notion) pra ganhar um SGV de verdade — depois disso, preencher `task:` aqui, renomear o arquivo pra `<SGV> - ...`, e atualizar o `pai:` do [[11262 - Funcionalidade Automacao TR 1.24-1.25 Autenticacao E Ciclo De Vida|SGV-11262]] pra apontar pra cá.

> [!info] Informações
> - **Tipo:** Funcionalidade (verificação de conformidade com Termo de Referência)
> - **Responsável QA:** Rafael
> - **Vault:** [[../../07 Termo de Referência/1.24-1.25/1.24-1.25 - Handoff Geral|Handoff Geral]] (visão de conjunto das 3 frentes) · [[../../07 Termo de Referência/1.24-1.25/README|pasta do Termo]]

---

> [!abstract] Resumo

Verificação de conformidade do Sogov com os itens **1.24** e **1.25** do Termo de Referência (Autenticação e ciclo de vida do usuário). Cobre 3 frentes — casos de teste, sincronização com a Qase e automação — não é só a automação, que é uma **subtarefa** desta (ver Subtarefas abaixo).

---

## Subtarefas

| Frente | Task | Status |
|---|---|---|
| 1. Casos de teste (padronização no vault) | sem SGV — trabalho de vault, não demanda tradicional | ✅ Concluída (31/08) |
| 2. Sincronização com a Qase (projeto SGV) | sem SGV — trabalho de vault/ferramenta | ✅ Concluída (31/08) |
| 3. Automação (Cypress) | [[11262 - Funcionalidade Automacao TR 1.24-1.25 Autenticacao E Ciclo De Vida\|SGV-11262]] | 🔄 Em andamento — 25/38 CTs confirmados |

---

## Regras de negócio

Ver os 38 CTs em [[../../07 Termo de Referência/1.24-1.25/01 Casos de Teste/1.24-1.25 - Casos de Teste|Casos de Teste]] — cada um já cita o item exato do Termo (`Requisito:`) e o texto literal da regra (`Citação do Termo:`).

---

> [!warning] Pontos de atenção

- A automação (11262) tem 3 achados reais de produto ainda não resolvidos (CT-015 em disputa, CT-029/030, CT-033) — esta task pai só fecha depois que a 11262 fechar.
- `priority` dos 39 casos na Qase ficou pendente de preenchimento manual (decisão consciente, não esquecimento).

---

## Histórico

- 2026-08-31 - Casos de teste padronizados numa fonte única no vault (frente 1)
- 2026-08-31 - 39 casos sincronizados com a Qase — 25 atualizados, 2 excluídos, 1 criado (frente 2)
- 2026-08-31 - Automação iniciada (frente 3, sem card vinculado ainda)
- 2026-09-02 - Card [[11262 - Funcionalidade Automacao TR 1.24-1.25 Autenticacao E Ciclo De Vida|SGV-11262]] criado, cobrindo só a frente 3
- 2026-09-02 - Esta task pai rascunhada, pra agrupar as 3 frentes — aguardando cadastro externo (SGV)
