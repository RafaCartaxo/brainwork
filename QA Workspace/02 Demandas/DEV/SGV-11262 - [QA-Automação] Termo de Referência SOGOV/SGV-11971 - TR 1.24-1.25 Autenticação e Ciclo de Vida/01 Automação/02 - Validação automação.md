---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
framework_atual: playwright
ambiente: hml
status: execucao
resultado: aguardando
ct_resultados:
  ct_001: "✅ Aprovado"
  ct_002: "✅ Aprovado"
  ct_003: "✅ Aprovado"
  ct_004: "✅ Aprovado"
  ct_005: "✅ Aprovado"
  ct_006: "✅ Aprovado"
  ct_007: "✅ Aprovado"
  ct_008: "✅ Aprovado"
  ct_009: "✅ Aprovado"
  ct_010: "✅ Aprovado"
  ct_011: "✅ Aprovado"
  ct_012: "✅ Aprovado"
  ct_013: "✅ Aprovado"
  ct_014: "✅ Aprovado"
  ct_015: "❌ Falhou"
  ct_016: "⏳ Aguardando"
  ct_017: "⏳ Aguardando"
  ct_018: "✅ Aprovado"
  ct_019: "✅ Aprovado"
  ct_020: "✅ Aprovado"
  ct_021: "✅ Aprovado"
  ct_022: "🚫 Bloqueado"
  ct_023: "✅ Aprovado"
  ct_024: "✅ Aprovado"
  ct_025: "✅ Aprovado"
  ct_026: "🚫 Bloqueado"
  ct_027: "✅ Aprovado"
  ct_028: "🚫 Bloqueado"
  ct_029: "❌ Falhou"
  ct_030: "❌ Falhou"
  ct_031: "✅ Aprovado"
  ct_032: "✅ Aprovado"
  ct_033: "❌ Falhou"
  ct_034: "🚫 Bloqueado"
  ct_035: "🚫 Bloqueado"
  ct_036: "🚫 Bloqueado"
  ct_037: "⏳ Aguardando"
  ct_038: "✅ Aprovado"
data_inicio: "2026-08-26"
data_fim: ""
---

# Validação automação — SGV-11971 (TR 1.24-1.25)

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Plano de teste:** [[../00 QA/02 - Plano de teste]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Validação:** [[../00 QA/04 - Validação dev]]
> **Preparação Qase:** [[../00 QA/05 - Preparação Qase]]
> **Automação:** [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/00 - Automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Placar atual por CT da automação — representa o estado registrado, não um log. Quando o estado mudar, sobrescreva a linha. Os arquivos `03 - Handoff de execução` e `04 - Documentação de entrega` são registros do pacote antigo e não são fontes de status. Os 3 CTs extras (CT-E01–E03) estão fora do escopo do Termo e não entram neste placar.

---

## Resumo da execução

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const total = Object.keys(resultados).length;
const aprovados = Object.values(resultados).filter((r) => String(r).includes("Aprovado")).length;
const pesoDoStatus = (r) => {
  const status = String(r);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const executados = Object.values(resultados).filter((r) => pesoDoStatus(r) > 0).length;
dv.list([
  `CTs aprovados: ${aprovados}/${total}`,
  `CTs executados: ${executados}/${total}`,
]);
```

---

## Resultado por CT

| CT | Framework | Rótulo / Arquivo | Resultado | Observação |
|---|---|---|---|---|
| [[../00 QA/03 - Casos de teste#^ct-001\|CT-001]] | playwright | `A02-C01` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |  |
| [[../00 QA/03 - Casos de teste#^ct-002\|CT-002]] | playwright | `A02-C02` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |  |
| [[../00 QA/03 - Casos de teste#^ct-003\|CT-003]] | playwright | `A02-C03` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |  |
| [[../00 QA/03 - Casos de teste#^ct-004\|CT-004]] | playwright | `A02-C04` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |  |
| [[../00 QA/03 - Casos de teste#^ct-005\|CT-005]] | playwright | `A02-C05` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |  |
| [[../00 QA/03 - Casos de teste#^ct-006\|CT-006]] | playwright | `A02-C06` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |  |
| [[../00 QA/03 - Casos de teste#^ct-007\|CT-007]] | playwright | `A02-C07` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |  |
| [[../00 QA/03 - Casos de teste#^ct-008\|CT-008]] | playwright | `A02-C08` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |  |
| [[../00 QA/03 - Casos de teste#^ct-009\|CT-009]] | playwright | `A02-C09` / `tests/api/auth/login.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` |  |
| [[../00 QA/03 - Casos de teste#^ct-010\|CT-010]] | playwright | `A01-C01` / `tests/api/auth/credentials.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` |  |
| [[../00 QA/03 - Casos de teste#^ct-011\|CT-011]] | playwright | `A01-C02` / `tests/api/auth/credentials.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_011]` |  |
| [[../00 QA/03 - Casos de teste#^ct-012\|CT-012]] | playwright | `A01-C03` / `tests/api/auth/credentials.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012]` |  |
| [[../00 QA/03 - Casos de teste#^ct-013\|CT-013]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_013]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-014\|CT-014]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_014]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-015\|CT-015]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_015]` | falha registrada; triagem funcional antes do porte |
| [[../00 QA/03 - Casos de teste#^ct-016\|CT-016]] | — | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_016]` | sem código — aguarda captura API |
| [[../00 QA/03 - Casos de teste#^ct-017\|CT-017]] | — | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_017]` | sem código — aguarda captura API |
| [[../00 QA/03 - Casos de teste#^ct-018\|CT-018]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_018]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-019\|CT-019]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_019]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-020\|CT-020]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_020]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-021\|CT-021]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_021]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-022\|CT-022]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_022]` | bloqueado; investigar causa raiz antes de definir porte |
| [[../00 QA/03 - Casos de teste#^ct-023\|CT-023]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_023]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-024\|CT-024]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_024]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-025\|CT-025]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_025]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-026\|CT-026]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_026]` | bloqueado; investigar causa raiz antes de definir porte |
| [[../00 QA/03 - Casos de teste#^ct-027\|CT-027]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_027]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-028\|CT-028]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_028]` | bloqueado; investigar causa raiz antes de definir porte |
| [[../00 QA/03 - Casos de teste#^ct-029\|CT-029]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_029]` | falha registrada; triagem funcional antes do porte |
| [[../00 QA/03 - Casos de teste#^ct-030\|CT-030]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_030]` | falha registrada; triagem funcional antes do porte |
| [[../00 QA/03 - Casos de teste#^ct-031\|CT-031]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_031]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-032\|CT-032]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_032]` | código legado; porte depende de escopo e estado do CT |
| [[../00 QA/03 - Casos de teste#^ct-033\|CT-033]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_033]` | falha registrada; triagem funcional antes do porte |
| [[../00 QA/03 - Casos de teste#^ct-034\|CT-034]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_034]` | bloqueado; investigar causa raiz antes de definir porte |
| [[../00 QA/03 - Casos de teste#^ct-035\|CT-035]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_035]` | bloqueado; investigar causa raiz antes de definir porte |
| [[../00 QA/03 - Casos de teste#^ct-036\|CT-036]] | cypress (legado) | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_036]` | bloqueado; investigar causa raiz antes de definir porte |
| [[../00 QA/03 - Casos de teste#^ct-037\|CT-037]] | — | — | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_037]` | sem código — aguarda captura API |
| [[../00 QA/03 - Casos de teste#^ct-038\|CT-038]] | playwright | `A55-C01` / `tests/api/auth/audit-sessions.spec.ts` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_038]` |  |

> Legenda do Framework: `playwright` = alvo atual, confirmado; `cypress (legado)` = existe na suíte antiga; porte para Playwright depende de prioridade e condição do CT; `—` = sem código em nenhum framework.

---

## Decisão

**Resultado geral:** aguardando — 25/38 CTs aprovados no histórico (13 identificados em Playwright; 12 aprovados ainda associados ao Cypress). Há 4 falhas/achados, 6 CTs bloqueados e 3 aguardando código ou evidência. O porte dos CTs restantes será definido por fatias, considerando estado e dependências.
