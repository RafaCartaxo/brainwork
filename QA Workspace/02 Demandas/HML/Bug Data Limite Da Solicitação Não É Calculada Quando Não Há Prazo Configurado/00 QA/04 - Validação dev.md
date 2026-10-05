---
demanda: "[[Bug/01 - Bug]]"
execucao: ""
ambiente: hml
versao: ""
status: execucao
responsavel: Rafael
resultado: reprovado
pontos: 0
ct_resultados:
  ct_001: "❌ Falhou"
data_inicio: 2026-10-05
data_fim: ""
---

# Validação — Bug data limite não calculada

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[Bug/01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

---

## Contexto

- Ambiente: homologação, cliente `prefeitura-de-cuite`
- Versão/build: não informada

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[03 - Casos de teste#^ct-001\|CT-001]] | ❌ Falhou | `GET /solicitacoes/listar-documentos?page=1&itemsPerPage=10` — 10/10 registros com `orderDateDeadline: null` | Confirmado também por `deadline.undefined: 24` (todas as 24 solicitações do cliente) nas estatísticas | este próprio Bug | 0 |

---

## Decisão

**Resultado geral:** reprovado — bloqueia o fechamento do critério C5 da [[../../SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]].

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug** — não se aplica (este já é o Bug).
- [x] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados — aguardando correção do dev.
- [x] Próximo passo registrado.
