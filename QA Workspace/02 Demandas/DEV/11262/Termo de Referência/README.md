---
tags:
  - qa
  - termo-de-referencia
---
# Termo de Referência 1.24-1.25

Autenticação e ciclo de vida do usuário — itens 1.24 e 1.25 do Termo de Referência. Esta pasta reúne os casos de teste, a sincronização com a Qase e a automação (Cypress) desse escopo.

## Estrutura

| Pasta | O que tem | Quem usa |
|---|---|---|
| `01 Casos de Teste/` | [[1.24-1.25 - Casos de Teste]] — fonte única dos 38 CTs ativos (+ 3 extras fora de escopo): Dado/Quando/Então, Prioridade, Requisito e Citação do Termo | Ponto de partida pra qualquer trabalho neste Termo |
| `02 Sincronização Qase/` | [[1.24-1.25 - Sincronização com a Qase]] — registro do que foi sincronizado com o projeto `SGV`, achados sobre a API, e ponteiro pro script reutilizável | Quem for atualizar a Qase de novo |
| `03 Automação/` | [[1.24-1.25 - Plano de Automação]] (arquitetura) e [[1.24-1.25 - Handoff de execução]] (estado/handoff atual) | Agente/dev automatizando os casos |
| `Histórico/` | [[1.24-1.25 - Casos organizados para Qase]] e [[1.24-1.25: Execução]] — versões superadas, mantidas só pra rastro | Ninguém precisa entrar, a menos que queira contexto antigo |

`01` é a fonte de verdade. `02` e `03` **não são passos 2 e 3 de uma sequência** — são dois consumidores independentes de `01`, em paralelo: sincronizar com a Qase não depende da automação terminar, e vice-versa.

## Regras de uso

1. **Fonte única é sempre `01 Casos de Teste/`.** Nunca editar um CT só na Qase ou só num script — o vault é quem manda.
2. **Toda correção de conteúdo segue essa ordem**: atualizar `01` primeiro, depois refletir na Qase (documentado/aplicado via `02`).
3. **`Histórico/` nunca é editado** — é só arquivo morto, preservado pra contexto.
