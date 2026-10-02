---
demanda: "[[01 - Demanda]]"
execucao: "suíte automatizada Cypress contra HML"
ambiente: dev
versao: ""
status: execucao
responsavel: Rafael
resultado: aguardando
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
  ct_015: ❌ Falhou
  ct_016: ⏳ Aguardando
  ct_017: ⏳ Aguardando
  ct_018: ✅ Aprovado
  ct_019: ✅ Aprovado
  ct_020: ✅ Aprovado
  ct_021: ✅ Aprovado
  ct_022: 🚫 Bloqueado
  ct_023: ✅ Aprovado
  ct_024: ✅ Aprovado
  ct_025: ✅ Aprovado
  ct_026: 🚫 Bloqueado
  ct_027: ✅ Aprovado
  ct_028: 🚫 Bloqueado
  ct_029: ❌ Falhou
  ct_030: ❌ Falhou
  ct_031: ✅ Aprovado
  ct_032: ✅ Aprovado
  ct_033: ❌ Falhou
  ct_034: 🚫 Bloqueado
  ct_035: 🚫 Bloqueado
  ct_036: 🚫 Bloqueado
  ct_037: ⏳ Aguardando
  ct_038: ✅ Aprovado
  ct_e01: ⚪ Não executado
  ct_e02: ⚪ Não executado
  ct_e03: ⚪ Não executado
data_inicio: "2026-08-31"
data_fim: ""
---

# Validação — SGV-11971 (TR 1.24-1.25)

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[../01 Automação/00 - Automação|Automação]]

> [!settings]- Controle da validação  
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`  
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da verificação de conformidade. Os cenários permanecem em `03 - Casos de teste.md`. **A execução aqui é a suíte automatizada rodando contra HML**, não execução manual — por isso a coluna Evidência fica vazia: o placar atual por CT da automação é [[../01 Automação/02 - Validação automação|02 - Validação automação]]; o detalhe de cada cenário de código é [[../01 Automação/04 - Documentação de entrega|Documentação de Entrega]].

---

## Contexto

- Ambiente: HML
- Framework: Cypress (repo `sogov-automation-test`) — **alvo migrou pra Playwright em 01/10/2026**, o código precisa ser portado antes de subir.
- Placar consolidado em **01/10/2026**, a partir do card guarda-chuva.

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-009\|CT-009]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_009 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-010\|CT-010]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_010 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-011\|CT-011]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_011]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_011 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-012\|CT-012]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_012 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-013\|CT-013]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_013]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_013 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-014\|CT-014]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_014]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_014 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-015\|CT-015]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_015]` |  | Achado real em disputa: via automação, após o bloqueio na 5ª tentativa (log retorna `account-blocked`), a tentativa seguinte com a senha correta autentica. Validação manual do Rafael (tela e API) não reproduziu. Hipótese de corrida/timing não confirmada — 3 experimentos falharam por instabilidade do ambiente. |  | `= choice(this.ct_resultados.ct_015 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-016\|CT-016]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_016]` |  | Sem código — aguarda captura de API do desbloqueio por link de e-mail. |  | `= choice(this.ct_resultados.ct_016 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-017\|CT-017]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_017]` |  | Sem código — aguarda captura de API do desbloqueio manual por servidor. |  | `= choice(this.ct_resultados.ct_017 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-018\|CT-018]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_018]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_018 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-019\|CT-019]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_019]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_019 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-020\|CT-020]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_020]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_020 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-021\|CT-021]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_021]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_021 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-022\|CT-022]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_022]` |  | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |  | `= choice(this.ct_resultados.ct_022 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-023\|CT-023]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_023]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_023 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-024\|CT-024]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_024]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_024 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-025\|CT-025]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_025]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_025 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-026\|CT-026]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_026]` |  | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |  | `= choice(this.ct_resultados.ct_026 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-027\|CT-027]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_027]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_027 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-028\|CT-028]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_028]` |  | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |  | `= choice(this.ct_resultados.ct_028 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-029\|CT-029]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_029]` |  | Achado real: em Férias a escrita não é bloqueada, diferente de Licença (CT-023), que bloqueia corretamente. Divergência entre os dois estados de quarentena — confirmar com produto se é intencional. |  | `= choice(this.ct_resultados.ct_029 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-030\|CT-030]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_030]` |  | Achado real: em Férias a leitura não é bloqueada, diferente de Licença (CT-024). Mesma divergência do CT-029. |  | `= choice(this.ct_resultados.ct_030 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-031\|CT-031]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_031]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_031 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-032\|CT-032]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_032]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_032 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-033\|CT-033]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_033]` |  | Achado real: sessão obtida antes da mudança para Inativo segue acessando o próprio perfil depois da mudança — a sessão antiga não é revogada nem revalidada. |  | `= choice(this.ct_resultados.ct_033 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-034\|CT-034]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_034]` |  | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |  | `= choice(this.ct_resultados.ct_034 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-035\|CT-035]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_035]` |  | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |  | `= choice(this.ct_resultados.ct_035 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-036\|CT-036]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_036]` |  | Falha na automação sem causa raiz identificada — investigar na mesma janela do CT-015. |  | `= choice(this.ct_resultados.ct_036 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-037\|CT-037]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_037]` |  | Sem código — aguarda captura do endpoint de auditoria. |  | `= choice(this.ct_resultados.ct_037 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-038\|CT-038]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_038]` |  | Confirmado contra HML pela suíte automatizada (31/08/2026). |  | `= choice(this.ct_resultados.ct_038 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-e01\|CT-E01]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_e01]` |  | Fora do escopo do Termo de Referência — não executado. |  | `= choice(this.ct_resultados.ct_e01 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-e02\|CT-E02]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_e02]` |  | Fora do escopo do Termo de Referência — não executado. |  | `= choice(this.ct_resultados.ct_e02 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-e03\|CT-E03]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_e03]` |  | Fora do escopo do Termo de Referência — não executado. |  | `= choice(this.ct_resultados.ct_e03 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

> **Pontos entregues:** a coluna é calculada automaticamente conforme o status de cada CT.

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const pontosEtapa = Number(pagina.pontos) || 0;
const chaves = Object.keys(resultados);
const totalCTs = chaves.length;
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
    const chave = chaves[indice];
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

- **2026-08-31 — rodada 1 (Suítes 1, 2 e 3).** 18 CTs codados e validados contra HML.
- **2026-08-31 — rodada 2 (Suíte 4).** Captura de API da troca de status localizada, desbloqueando os 17 CTs do ciclo de vida: 8 confirmados, 3 achados reais, 6 sem causa raiz.
- **2026-09-01 — CT-015 contestado.** A validação manual do Rafael (tela e API) não reproduziu o achado da automação. Experimento de timing tentado 3 vezes, inconclusivo por instabilidade do ambiente.
- **2026-10-01 — placar consolidado.** 25/38 confirmados. Descoberto que o repo migrou pra Playwright; o código Cypress não sobe mais, será portado.

> [!tip] Pistas de investigação (preservadas da nota de retomada, apagada em 02/10/2026)
> - **6 falhas sem causa raiz:** comparar o CT-031, que passa, contra CT-022/026/028/036, que falham — a diferença entre eles é a pista mais direta pra causa comum.
> - **CT-016/017/037:** falta capturar um HAR novo via DevTools (desbloqueio manual e endpoint de auditoria), do mesmo jeito que foi feito pra destravar a Suíte 4 em 31/08.
> - **CT-015:** o script do experimento de timing já está pronto — só depende de o ambiente HML estabilizar.

---

## Decisão

**Resultado geral:** aguardando — 25/38 CTs confirmados (01/10/2026). Faltam 4 achados reais de produto a confirmar, 6 falhas sem causa raiz a investigar e 3 CTs sem código.

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [ ] 4 achados reais confirmados com produto/backend (CT-015, CT-029, CT-030, CT-033).
- [ ] 6 falhas sem causa raiz investigadas (CT-022/026/028/034/035/036).
- [ ] 3 CTs sem código cobertos (CT-016/017/037 — dependem de captura de API).
- [ ] Suíte portada de Cypress pra Playwright.
- [ ] Resultado geral definido.

