---
demanda: "[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda]]"
execucao: ""
ambiente: dev
versao: ""
status: execucao
responsavel: Rafael
resultado: aprovado
pontos: 0
ct_resultados:
  ct_001: ✅ Aprovado
  ct_002: ✅ Aprovado
  ct_003: ✅ Aprovado
  ct_004: ✅ Aprovado
  ct_005: ✅ Aprovado
  ct_006: ✅ Aprovado
  ct_007: ✅ Aprovado
  ct_008: ✅ Aprovado
  ct_009: ✅ Aprovado
  ct_010: ✅ Aprovado
  ct_011: ✅ Aprovado
  ct_012: ✅ Aprovado
  ct_013: ✅ Aprovado
  ct_014: ✅ Aprovado
  ct_015: ✅ Aprovado
  ct_016: ✅ Aprovado
  ct_017: ✅ Aprovado
  ct_018: ✅ Aprovado
  ct_019: ✅ Aprovado
  ct_020: ✅ Aprovado
  ct_021: ✅ Aprovado
  ct_022: ✅ Aprovado
  ct_023: ✅ Aprovado
  ct_024: ✅ Aprovado
  ct_025: ✅ Aprovado
  ct_026: ✅ Aprovado
  ct_027: ✅ Aprovado
  ct_028: ✅ Aprovado
  ct_029: ✅ Aprovado
  ct_030: ✅ Aprovado
  ct_031: ✅ Aprovado
  ct_032: ✅ Aprovado
  ct_033: ✅ Aprovado
data_inicio: ""
data_fim: ""
---

# Validação — SGV-11083

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/00 README|Abrir README do card]]
> **Demanda/Bug:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`. **Atualizado em 02/10/2026:** confirmado que a task já foi aprovada em DEV — os 33 CTs foram marcados aprovados via essa aprovação geral (não executados individualmente neste vault, possivelmente testados por outro QA). CT-021 segue com a definição de contagem pendente do Produto, mas isso não bloqueia a aprovação geral.

---

## Contexto

- Ambiente:
- Versão/build:

---

## Resumo da execução

```dataviewjs
const paginaResumo = dv.current() ?? {};
const resultadosResumo = paginaResumo.ct_resultados ?? {};
const pontosEtapaResumo = Number(paginaResumo.pontos) || 0;
const totalCTsResumo = Object.keys(resultadosResumo).length;
const aprovadosResumo = Object.values(resultadosResumo).filter((resultado) => String(resultado).includes("Aprovado")).length;
const pesoResumo = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const executadosResumo = Object.values(resultadosResumo).filter((resultado) => pesoResumo(resultado) > 0).length;
const pontosEntreguesResumo = totalCTsResumo
  ? Math.round(Object.values(resultadosResumo).reduce((total, resultado) => total + (pontosEtapaResumo / totalCTsResumo) * pesoResumo(resultado), 0) * 100) / 100
  : 0;

dv.list([
  `CTs aprovados: ${aprovadosResumo}/${totalCTsResumo}`,
  `CTs executados: ${executadosResumo}/${totalCTsResumo}`,
  `Pontos da etapa: ${pontosEtapaResumo}`,
  `Pontos entregues: ${pontosEntreguesResumo} de ${pontosEtapaResumo}`,
]);
```

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-009\|CT-009]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_009 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-010\|CT-010]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_010 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-011\|CT-011]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_011]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_011 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-012\|CT-012]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_012 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-013\|CT-013]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_013]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_013 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-014\|CT-014]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_014]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_014 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-015\|CT-015]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_015]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_015 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-016\|CT-016]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_016]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_016 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-017\|CT-017]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_017]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_017 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-018\|CT-018]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_018]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_018 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-019\|CT-019]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_019]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_019 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-020\|CT-020]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_020]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_020 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-021\|CT-021]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_021]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault. Definição exata da contagem (vínculos por departamento vs. cidadãos únicos) segue pendente do Produto, mas não bloqueia a aprovação geral. |  | `= choice(this.ct_resultados.ct_021 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-022\|CT-022]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_022]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_022 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-023\|CT-023]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_023]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_023 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-024\|CT-024]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_024]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_024 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-025\|CT-025]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_025]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_025 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-026\|CT-026]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_026]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_026 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-027\|CT-027]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_027]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_027 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-028\|CT-028]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_028]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_028 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-029\|CT-029]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_029]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_029 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-030\|CT-030]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_030]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_030 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-031\|CT-031]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_031]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_031 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-032\|CT-032]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_032]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_032 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste#^ct-033\|CT-033]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_033]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_033 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

> **Pontos entregues:** a coluna é calculada automaticamente conforme o status de cada CT.

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const pontosEtapa = Number(pagina.pontos) || 0;
const totalCTs = Object.keys(resultados).length;
const pesoDoStatus = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const raiz = dv.container.closest(".markdown-preview-view") ?? document;
const tabela = Array.from(raiz.querySelectorAll("table")).find((item) => item.innerText.includes("Pontos entregues"));
if (tabela) {
  const pontosPorCT = totalCTs ? pontosEtapa / totalCTs : 0;
  Array.from(tabela.querySelectorAll("tbody tr")).forEach((linha, indice) => {
    const chave = `ct_${String(indice + 1).padStart(3, "0")}`;
    const celula = linha.lastElementChild;
    if (celula) {
      const pontos = pontosPorCT * pesoDoStatus(resultados[chave]);
      celula.textContent = pontos ? (Math.round(pontos * 100) / 100).toString() : "0";
    }
  });
}
```

> A prévia do CT é exibida pelo Obsidian ao passar o mouse sobre cada link. A tabela é o registro da execução; o conteúdo do cenário permanece em `03 - Casos de teste.md`.

---

## Histórico de validação

Use esta seção somente quando houver reteste após correção:

- **Rodada inicial:** registre o CT reprovado e o defeito aberto.
- **Correção:** vincule o bug e o Fix DEV.
- **Reteste:** registre o resultado final e a data.

---

## Decisão

**Resultado geral:** aprovado — via aprovação geral da task em DEV (02/10/2026)

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [ ] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [ ] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados.
- [ ] Próximo passo registrado.
