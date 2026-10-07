---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: hml
versao: ""
status: execucao
responsavel: ""
resultado: aguardando
pontos: 0
data_inicio: ""
data_fim: ""
ct_resultados:
  seed_001: ⏳ Aguardando
  seed_002: ⏳ Aguardando
  seed_003: ⏳ Aguardando
  seed_004: ⏳ Aguardando
---

# Validação QA/DEV — Entrega 01

> [!info]- Navegação
> **README:** [[00 README]]
> **Demanda:** [[01 - Demanda]]
> **Plano:** [[02 - Plano de teste]]
> **Casos:** [[03 - Casos de teste]]
> **Automação:** [[../01 Automação/00 - Automação|Pacote de automação]]
> **Validação dos 13 CTs funcionais:** [[../01 Automação/02 - Validação automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Esta validação cobre os quatro casos técnicos do seed. Os CTs funcionais da autenticação têm placar separado na validação de automação. Ainda não houve implementação nem execução desta entrega.

## Contexto

- **Backend/ambiente:** confirmar antes do primeiro run; precisa conter a instância 225.
- **Instância:** ID 225 — “Termo De Referência - Sogov”.
- **Build/commit:** preencher após implementação.

## Resultado dos casos de teste

| Caso | Resultado | Evidência | Observação |
|---|---|---|---|
| [[03 - Casos de teste#^ct-seed-001|SEED-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_001]` | — | Resolve e confere a instância 225 |
| [[03 - Casos de teste#^ct-seed-002|SEED-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_002]` | — | ID/nome inválido interrompe sem criar |
| [[03 - Casos de teste#^ct-seed-003|SEED-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_003]` | — | Sem configuração, alvo padrão permanece |
| [[03 - Casos de teste#^ct-seed-004|SEED-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_004]` | — | Duas execuções reutilizam a 225 |

## Encerramento

- [ ] Todos os quatro casos técnicos executados ou bloqueios justificados.
- [ ] Evidências e build/commit registrados.
- [ ] Os resultados dos CTs funcionais estão atualizados separadamente em [[../01 Automação/02 - Validação automação]].
- [ ] Resultado geral e próxima ação definidos.

