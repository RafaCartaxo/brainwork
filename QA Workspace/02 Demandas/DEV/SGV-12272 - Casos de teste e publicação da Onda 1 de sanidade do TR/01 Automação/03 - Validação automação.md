---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
framework: playwright
ambiente: hml
status: planejado
ct_resultados:
  ct_001: "⏳ Aguardando"
  ct_002: "🧩 Sem teste"
  ct_003: "🧩 Sem teste"
  ct_004: "🧩 Sem teste"
  ct_005: "🧩 Sem teste"
  ct_006: "🧩 Sem teste"
  ct_007: "🧩 Sem teste"
  ct_008: "🧩 Sem teste"
  ct_009: "🧩 Sem teste"
  ct_010: "🧩 Sem teste"
  ct_011: "🧩 Sem teste"
  ct_012: "🧩 Sem teste"
  ct_013: "🧩 Sem teste"
  ct_014: "🧩 Sem teste"
  ct_015: "🧩 Sem teste"
  ct_016: "🧩 Sem teste"
  ct_017: "🧩 Sem teste"
  ct_018: "🧩 Sem teste"
  ct_019: "🧩 Sem teste"
  ct_020: "🧩 Sem teste"
---

# Validação automação — SGV-12272 · Onda 1

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Automação:** [[00 - Automação]]
> **Análise:** [[01 - Análise]]
> **Plano de automação:** [[02 - Plano de automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Esta tabela é o **placar atual por CT**. Atualize o resultado existente quando o CT for executado de novo; não acrescente rodadas antigas. O plano fica em [[02 - Plano de automação]] e a próxima ação geral fica em [[00 - Automação]].

## Resumo da execução

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const valores = Object.values(resultados).map(String);
const total = valores.length;
const aprovados = valores.filter((r) => r.includes("Aprovado")).length;
const iniciados = valores.filter((r) => ["Aprovado", "Falhou", "Em andamento", "Bloqueado"].some((s) => r.includes(s))).length;
dv.list([
  `CTs aprovados: ${aprovados}/${total}`,
  `CTs iniciados: ${iniciados}/${total}`,
  `CTs sem teste: ${valores.filter((r) => r.includes("Sem teste")).length}/${total}`,
]);
```

## Resultado por CT

| CT | Teste no repo | Resultado atual | Última execução (data/build) | Observação |
|---|---|---|---|---|
| [[../00 QA/03 - Casos de teste#^ct-001\|CT-001]] | `A02-C01: tests/api/auth/login.spec.ts; CT-001: tests/e2e/public-agents/login.spec.ts` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_001]` | — | `E2E implementado; CT ainda não executado. Em 22/10, o seed falhou em DEV na confirmação de cidadãos, antes de iniciar o CT. Próxima tentativa em HML; abrir navegador visível para preencher eventual CAPTCHA.` |
| [[../00 QA/03 - Casos de teste#^ct-002\|CT-002]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_002]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-003\|CT-003]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_003]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-004\|CT-004]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_004]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-005\|CT-005]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_005]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-006\|CT-006]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_006]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-007\|CT-007]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_007]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-008\|CT-008]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_008]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-009\|CT-009]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_009]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-010\|CT-010]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_010]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-011\|CT-011]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_011]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-012\|CT-012]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_012]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-013\|CT-013]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_013]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-014\|CT-014]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_014]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-015\|CT-015]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_015]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-016\|CT-016]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_016]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-017\|CT-017]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_017]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-018\|CT-018]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_018]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-019\|CT-019]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_019]` | — | |
| [[../00 QA/03 - Casos de teste#^ct-020\|CT-020]] | `sem teste` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_020]` | — | |

**Estados:** `Sem teste` = código ainda não existe; `Aguardando` = há teste mapeado, mas ainda não foi executado; `Em andamento` = execução iniciada; `Aprovado` = passou; `Falhou` = falha observada ainda a triar; `Bloqueado` = não foi possível concluir por dependência/ambiente. Falha observada não significa, por si só, defeito confirmado no produto.

## Encerramento

- [ ] Todos os CTs do escopo têm resultado atual ou justificativa para estarem sem teste/bloqueados.
- [ ] Observações e links para defeitos/pendências foram registrados quando necessários.
- [ ] Campo **Automação** dos CTs foi sincronizado em `../00 QA/03 - Casos de teste`.
- [ ] Status da validação e próxima ação em [[00 - Automação]] foram atualizados.
