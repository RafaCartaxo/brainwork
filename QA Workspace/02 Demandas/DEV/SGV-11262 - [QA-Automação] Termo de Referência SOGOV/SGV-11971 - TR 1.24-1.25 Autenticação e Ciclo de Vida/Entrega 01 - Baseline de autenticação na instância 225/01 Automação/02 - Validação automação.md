---
demanda_pai: SGV-11262
ciclo_referencia: SGV-11971
casos_origem: "[[../../00 QA/03 - Casos de teste]]"
casos_entrega: "[[../00 QA/03 - Casos de teste]]"
framework: playwright
ambiente: hml
status: planejado
ct_resultados:
  ct_001: ⏳ Aguardando
  ct_002: ⏳ Aguardando
  ct_003: ⏳ Aguardando
  ct_004: ⏳ Aguardando
  ct_005: ⏳ Aguardando
  ct_006: ⏳ Aguardando
  ct_007: ⏳ Aguardando
  ct_008: ⏳ Aguardando
  ct_009: ⏳ Aguardando
  ct_010: ⏳ Aguardando
  ct_011: ⏳ Aguardando
  ct_012: ⏳ Aguardando
  ct_038: 🚫 Bloqueado
---

# Validação automação — Baseline de autenticação na instância 225

> [!info]- Navegação
> **Hub:** [[00 - Automação]]
> **Plano:** [[01 - Plano de automação]]
> **Casos de origem:** [[../../00 QA/03 - Casos de teste|Casos da SGV-11971]]
> **Mapa do seed:** [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa técnico]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Esta nota registra somente a validação desta entrega. Os 13 CTs estão no escopo, mas seus resultados anteriores em HML não equivalem a uma execução na instância 225. Não houve execução do seed ou dos testes nesta entrega ainda.

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
  `CTs aguardando: ${valores.filter((r) => r.includes("Aguardando")).length}/${total}`,
]);
```

## Critérios de validação do seed

| Verificação | Resultado atual | Evidência |
|---|---|---|
| Ambiente configurado corresponde ao backend em que foi criada a instância 225 | ⏳ Aguardando | — |
| ID 225 resolve para “Termo De Referência - Sogov” | ⏳ Aguardando | — |
| ID ou nome divergente interrompe a preparação e não cria outro cliente | ⏳ Aguardando | — |
| Duas execuções consecutivas reutilizam ID 225 | ⏳ Aguardando | — |
| Manifesto registra ID 225 e nome esperado | ⏳ Aguardando | — |

## Resultado por CT

| CT | Teste no repositório | Resultado atual | Última execução | Observação |
|---|---|---|---|---|
| CT-001 | tests/api/auth/login.spec.ts / A02-C01 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_001]` | — | Executar contra instância 225 |
| CT-002 | tests/api/auth/login.spec.ts / A02-C02 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_002]` | — | Usa CPF do servidor na rota de cidadão |
| CT-003 | tests/api/auth/login.spec.ts / A02-C03 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_003]` | — | Cidadão PJ do pool por worker |
| CT-004 | tests/api/auth/login.spec.ts / A02-C04 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_004]` | — | CNPJ do cidadão PJ no login de servidor |
| CT-005 | tests/api/auth/login.spec.ts / A02-C05 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_005]` | — | Usa CPF do servidor |
| CT-006 | tests/api/auth/login.spec.ts / A02-C06 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_006]` | — | Identificador inválido |
| CT-007 | tests/api/auth/login.spec.ts / A02-C07 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_007]` | — | Identificador inválido |
| CT-008 | tests/api/auth/login.spec.ts / A02-C08 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_008]` | — | Rejeição de cadastro duplicado |
| CT-009 | tests/api/auth/login.spec.ts / A02-C09 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_009]` | — | Usa CPF do servidor |
| CT-010 | tests/api/auth/credentials.spec.ts / A01-C01 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_010]` | — | Senha incorreta |
| CT-011 | tests/api/auth/credentials.spec.ts / A01-C02 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_011]` | — | CPF inexistente gerado pelo teste |
| CT-012 | tests/api/auth/credentials.spec.ts / A01-C03 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_012]` | — | Rejeição via API; não valida bloqueio de envio na interface |
| CT-038 | tests/api/auth/audit-sessions.spec.ts / A55-C01 | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_038]` | — | Arquivo ainda sem commit em HEAD destacado (16c41e4); resolver antes da validação final |

## Encerramento

- [ ] Todas as verificações de preparação têm resultado e evidência.
- [ ] Cada CT do escopo foi executado ou tem bloqueio justificado.
- [ ] Resultados correspondem ao ambiente e à instância 225.
- [ ] Status e próxima ação atualizados em [[00 - Automação]].
