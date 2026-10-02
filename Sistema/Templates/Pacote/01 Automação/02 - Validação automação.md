---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
framework_atual: ""
ambiente: dev
status: execucao
resultado: aguardando
ct_resultados:
  ct_001: "⏳ Aguardando"
data_inicio: ""
data_fim: ""
---

# Validação automação — <ID>

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Plano de teste:** [[../00 QA/02 - Plano de teste]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Validação:** [[../00 QA/04 - Validação dev]]
> **Preparação Qase:** [[../00 QA/05 - Preparação Qase]]
> **Automação:** [[00 - Automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Esta nota é o **placar atual por CT** da automação — sempre representa o estado de agora, nunca um log. Quando o estado muda, **sobrescreve** a linha; não acrescenta um novo registro embaixo. Histórico de como se chegou aqui (achado, correção, investigação) vive em [[03 - Handoff de execução|03 - Handoff de execução]] — linka de lá pra cá quando fizer sentido, não copia o texto.

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
| [[../00 QA/03 - Casos de teste#^ct-001\|CT-001]] | `<cypress \| playwright>` | `<rótulo ou caminho do spec>` | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` | |

> **Observação curta, sempre** — "achado real em disputa, ver Handoff", não a narrativa inteira. A narrativa completa mora só em [[03 - Handoff de execução]].

---

## Decisão

**Resultado geral:** aguardando / aprovado / reprovado / aprovado com ressalvas — `<X/Y CTs confirmados no framework atual>`
