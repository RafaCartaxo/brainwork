---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../../Arquivo/00 QA/03 - Casos de teste]]"
casos_entrega: "[[../00 QA/03 - Casos de teste]]"
framework: playwright
ambiente: hml
status: planejado
ct_resultados:
  ct_001: "⏳ Aguardando"
  ct_002: "⏳ Aguardando"
  ct_003: "⏳ Aguardando"
  ct_004: "⏳ Aguardando"
  ct_005: "⏳ Aguardando"
  ct_006: "⏳ Aguardando"
  ct_007: "⏳ Aguardando"
  ct_008: "⏳ Aguardando"
  ct_009: "⏳ Aguardando"
  ct_010: "⏳ Aguardando"
  ct_011: "⏳ Aguardando"
  ct_012: "⏳ Aguardando"
  ct_038: "🚫 Bloqueado"
---
# Validação automação — Entrega 01: Baseline na instância 225

> [!info]- Navegação QA
> **README:** [[../00 QA/00 README|Entrega 01]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|SGV-11971]]
> **Casos técnicos desta entrega:** [[../00 QA/03 - Casos de teste]]
> **Automação:** [[00 - Automação]]
> **Plano:** [[01 - Plano de automação]]
> **Mapa do seed:** [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa técnico]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Esta nota registra o resultado mais recente por CT funcional desta entrega. Os quatro casos técnicos de validação do seed ficam em [[../00 QA/04 - Validação dev]]. Ainda não houve implementação nem execução específica na instância 225.

## Resumo da execução

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const valores = Object.values(resultados).map(String);
const total = valores.length;
const aprovados = valores.filter((r) => r.includes("Aprovado")).length;
const iniciados = valores.filter((r) => ["Aprovado", "Falhou", "Em andamento", "Bloqueado"].some((s) => r.includes(s))).length;
dv.list([`CTs aprovados: ${aprovados}/${total}`, `CTs iniciados: ${iniciados}/${total}`, `CTs aguardando: ${valores.filter((r) => r.includes("Aguardando")).length}/${total}`]);
```

## Resultado por CT

| CT | Teste no repositório | Resultado atual | Última execução (data/build) | Observação |
|---|---|---|---|---|
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-001|CT-001]] | `tests/api/auth/login.spec.ts / A02-C01` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_001]` | — | Executar contra instância 225 |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-002|CT-002]] | `tests/api/auth/login.spec.ts / A02-C02` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_002]` | — | Usa CPF do servidor na rota de cidadão |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-003|CT-003]] | `tests/api/auth/login.spec.ts / A02-C03` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_003]` | — | Cidadão PJ do pool por worker |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-004|CT-004]] | `tests/api/auth/login.spec.ts / A02-C04` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_004]` | — | CNPJ do cidadão PJ no login de servidor |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-005|CT-005]] | `tests/api/auth/login.spec.ts / A02-C05` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_005]` | — | Usa CPF do servidor |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-006|CT-006]] | `tests/api/auth/login.spec.ts / A02-C06` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_006]` | — | Identificador inválido |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-007|CT-007]] | `tests/api/auth/login.spec.ts / A02-C07` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_007]` | — | Identificador inválido |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-008|CT-008]] | `tests/api/auth/login.spec.ts / A02-C08` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_008]` | — | Rejeição de cadastro duplicado |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-009|CT-009]] | `tests/api/auth/login.spec.ts / A02-C09` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_009]` | — | Usa CPF do servidor |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-010|CT-010]] | `tests/api/auth/credentials.spec.ts / A01-C01` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_010]` | — | Senha incorreta |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-011|CT-011]] | `tests/api/auth/credentials.spec.ts / A01-C02` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_011]` | — | CPF inexistente gerado pelo teste |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-012|CT-012]] | `tests/api/auth/credentials.spec.ts / A01-C03` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_012]` | — | Rejeição via API; não valida bloqueio na interface |
| [[../../Arquivo/00 QA/03 - Casos de teste#^ct-038|CT-038]] | `tests/api/auth/audit-sessions.spec.ts / A55-C01` | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_038]` | — | Arquivo em HEAD destacado (16c41e4), sem commit; resolver destino |

**Estados:** `Sem teste` = código ainda não existe; `Aguardando` = teste mapeado, sem execução nesta entrega; `Em andamento` = execução iniciada; `Aprovado` = passou; `Falhou` = falha observada ainda a triar; `Bloqueado` = dependência ou ambiente impede conclusão.

## Encerramento

- [ ] Todos os CTs do escopo têm resultado atual ou justificativa para bloqueio/ausência de teste.
- [ ] Ambiente e instância da execução foram registrados.
- [ ] Observações e links para defeitos/pendências foram registrados quando necessários.
- [ ] Campo **Automação** dos CTs foi sincronizado nos casos de origem, quando aplicável.
- [ ] Status e próxima ação em [[00 - Automação]] foram atualizados.
