---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: dev
versao: ""
status: execucao
responsavel: Rafael
resultado: aprovado_com_ressalvas
pontos: 0
ct_resultados:
  ct_001: "✅ Aprovado"
  ct_002: "✅ Aprovado"
  ct_002a: "⚪ Não executado"
  ct_002b: "⚪ Não executado"
  ct_002c: "✅ Aprovado"
  ct_003: "✅ Aprovado"
  ct_004: "✅ Aprovado"
  ct_005: "✅ Aprovado"
  ct_006: "⚪ Não executado"
  ct_007: "✅ Aprovado"
  ct_008: "✅ Aprovado"
  ct_008a: "✅ Aprovado"
  ct_009: "✅ Aprovado"
  ct_010: "⚪ Não executado"
  ct_011: "✅ Aprovado"
  ct_012: "⚪ Não executado"
  ct_012a: "❌ Falhou"
  ct_012b: "✅ Aprovado"
  ct_013: "✅ Aprovado"
  ct_014: "⚪ Não executado"
  ct_015: "✅ Aprovado"
  ct_016: "✅ Aprovado"
  ct_017: "✅ Aprovado"
  ct_018: "✅ Aprovado"
  ct_019: "✅ Aprovado"
  ct_020: "✅ Aprovado"
  ct_021: "✅ Aprovado"
  ct_022: "⚪ Não executado"
data_inicio: ""
data_fim: ""
---

# Validação — SGV-11184

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`. Validação real desde 03/09/2026 — 14/21 CTs aplicáveis aprovados na época, mais 6 aprovados em 02/10/2026 via aprovação geral da task em DEV (CT-003, 017-021 — não executados individualmente neste vault). **20/21 CTs aplicáveis aprovados**, 1 reprovado (CT-012a, defeito SGV-11338 ainda aberto); 7 marcados "Não executado" (fora de escopo real desta entrega, nível "participantes" não implementado — ver `01 - Demanda`). 2 defeitos já corrigidos e retestados (SGV-11312, SGV-11319).

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
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |  |  |  | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |  |  |  | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-002a\|CT-002a]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002a]` |  |  |  | `= choice(this.ct_resultados.ct_002a = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-002b\|CT-002b]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002b]` |  |  |  | `= choice(this.ct_resultados.ct_002b = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-002c\|CT-002c]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002c]` | ![[11312 - área de clique não respeitada.mp4]]<br>![[11312 - OK.mp4]] | Reprovado em 03/09, aprovado no reteste | [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma\|SGV-11312]] (resolvido) | `= choice(this.ct_resultados.ct_002c = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |  |  |  | `= choice(this.ct_resultados.ct_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |  |  |  | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |  |  |  | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |  |  |  | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |  |  |  | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-008a\|CT-008a]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008a]` | ![[11312 - OK.mp4]] | Reprovado em 03/09, aprovado no reteste | [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma\|SGV-11312]] (resolvido) | `= choice(this.ct_resultados.ct_008a = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-009\|CT-009]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` |  |  |  | `= choice(this.ct_resultados.ct_009 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-010\|CT-010]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` |  |  |  | `= choice(this.ct_resultados.ct_010 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-011\|CT-011]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_011]` |  |  |  | `= choice(this.ct_resultados.ct_011 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-012\|CT-012]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012]` |  |  |  | `= choice(this.ct_resultados.ct_012 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-012a\|CT-012a]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012a]` | ![[11338 - incorreto 1.png]]<br>![[11338 - incorreto 2.png]] | Defeito ainda aberto | [[Defeitos/SGV-11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo\|SGV-11338]] (aberto) | `= choice(this.ct_resultados.ct_012a = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-012b\|CT-012b]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012b]` | ![[11319 - Departamento não é persistido ao retificar despacho.mp4]]<br>![[11319 - OK.mp4]] | Formalizado a partir de defeito já corrigido | [[Defeitos/SGV-11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho\|SGV-11319]] (resolvido) | `= choice(this.ct_resultados.ct_012b = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-013\|CT-013]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_013]` |  |  |  | `= choice(this.ct_resultados.ct_013 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-014\|CT-014]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_014]` |  |  |  | `= choice(this.ct_resultados.ct_014 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-015\|CT-015]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_015]` |  |  |  | `= choice(this.ct_resultados.ct_015 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-016\|CT-016]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_016]` |  |  |  | `= choice(this.ct_resultados.ct_016 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-017\|CT-017]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_017]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_017 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-018\|CT-018]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_018]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_018 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-019\|CT-019]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_019]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_019 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-020\|CT-020]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_020]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_020 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-021\|CT-021]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_021]` |  | Aprovado via aprovação geral da task em DEV — execução individual não registrada neste vault (possivelmente testado por outro QA). |  | `= choice(this.ct_resultados.ct_021 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/03 - Casos de teste#^ct-022\|CT-022]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_022]` |  |  |  | `= choice(this.ct_resultados.ct_022 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

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

- **03/09/2026:** CT-002c reprovado — defeito [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] (área de clique do accordion não segue o Figma). Mesmo defeito confirmado no CT-008a.
- **03/09/2026:** [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] corrigido e aprovado em DEV — CT-002c e CT-008a revalidados e aprovados.
- **03/09/2026:** Defeito cadastrado (achado em teste exploratório): [[Defeitos/SGV-11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]] (departamento não persistido ao retificar despacho).
- **03/09/2026:** [[Defeitos/SGV-11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]] corrigido e aprovado em DEV — formalizado como CT-012b, já aprovado.
- **04/09/2026:** CT-012a reprovado — defeito cadastrado: [[Defeitos/SGV-11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]] (truncamento de destinatário com nome extenso). **Ainda aberto.**
- **02/10/2026:** Confirmado que a task já foi aprovada em DEV — CT-003, 017, 018, 019, 020 e 021 marcados aprovados via essa aprovação geral (execução individual não registrada neste vault). CT-012a/SGV-11338 segue aberto, sem alteração.

---

## Decisão

**Resultado geral:** aprovado com ressalvas — 20/21 CTs aplicáveis aprovados (6 via aprovação geral da task em DEV, 02/10/2026); falta corrigir SGV-11338 (CT-012a).

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [x] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [ ] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados.
- [x] Próximo passo registrado.
