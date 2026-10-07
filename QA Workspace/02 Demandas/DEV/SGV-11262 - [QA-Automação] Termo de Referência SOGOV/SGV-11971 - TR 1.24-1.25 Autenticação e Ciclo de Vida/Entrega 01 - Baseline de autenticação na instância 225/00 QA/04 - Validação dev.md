---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: hml
versao: ""
status: execucao
responsavel: ""
resultado: aguardando
pontos: 0
ct_resultados:
  seed_001: "⏳ Aguardando"
  seed_002: "⏳ Aguardando"
  seed_003: "⏳ Aguardando"
  seed_004: "⏳ Aguardando"
data_inicio: ""
data_fim: ""
---

# Validação QA/DEV — Entrega 01

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|CTs da SGV-11971]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** Não se aplica nesta entrega.
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da execução dos quatro casos técnicos e das evidências. Os cenários permanecem em [[03 - Casos de teste]]. Os resultados dos CTs funcionais ficam em [[../01 Automação/02 - Validação automação]].

---

## Contexto

- **Ambiente/backend:** confirmar antes da execução que contém a instância 225.
- **Instância:** ID 225 — “Termo De Referência - Sogov”.
- **Versão/build:** preencher após implementação.

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
| [[03 - Casos de teste#^ct-seed-001\|SEED-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_001]` | — | Resolver e validar identidade da instância 225 | — | `= choice(this.ct_resultados.seed_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-seed-002\|SEED-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_002]` | — | ID inexistente/nome divergente interrompe sem criar | — | `= choice(this.ct_resultados.seed_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-seed-003\|SEED-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_003]` | — | Sem configuração, o alvo padrão permanece | — | `= choice(this.ct_resultados.seed_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-seed-004\|SEED-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.seed_004]` | — | Duas execuções usam a mesma instância sem duplicação | — | `= choice(this.ct_resultados.seed_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

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
    const chave = `seed_${String(indice + 1).padStart(3, "0")}`;
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

**Resultado geral:** aguardando implementação e execução.

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [ ] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [ ] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados.
- [ ] Próximo passo registrado.
