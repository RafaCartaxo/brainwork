---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
framework: playwright
ambiente: hml
status: planejado
ct_resultados:
  ct_001: "🧩 Sem teste"
---

# Validação automação — <ID>

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Automação:** [[Sistema/Templates/Pacote/01 Automação/00 - Automação]]
> **Plano de automação:** [[Sistema/Templates/Pacote/01 Automação/01 - Plano de automação]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Esta tabela é o **placar atual por CT**. Atualize o resultado existente quando o CT for executado de novo; não acrescente rodadas antigas. O plano fica em [[Sistema/Templates/Pacote/01 Automação/01 - Plano de automação]] e a próxima ação geral fica em [[Sistema/Templates/Pacote/01 Automação/00 - Automação]].

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
| [[../00 QA/03 - Casos de teste#^ct-001\|CT-001]] | <caminho + ID do teste; ou `sem teste`> | `INPUT[inlineSelect(option(🧩 Sem teste),option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado)):ct_resultados.ct_001]` | — | |

**Estados:** `Sem teste` = código ainda não existe; `Aguardando` = há teste mapeado, mas ainda não foi executado; `Em andamento` = execução iniciada; `Aprovado` = passou; `Falhou` = falha observada ainda a triar; `Bloqueado` = não foi possível concluir por dependência/ambiente. Falha observada não significa, por si só, defeito confirmado no produto.

## Encerramento

- [ ] Todos os CTs do escopo têm resultado atual ou justificativa para estarem sem teste/bloqueados.
- [ ] Observações e links para defeitos/pendências foram registrados quando necessários.
- [ ] Campo **Automação** dos CTs foi sincronizado em `../00 QA/03 - Casos de teste`.
- [ ] Status da validação e próxima ação em [[Sistema/Templates/Pacote/01 Automação/00 - Automação]] foram atualizados.
