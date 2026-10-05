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

# Validação — Bug totalAnswered ausente

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
| [[03 - Casos de teste#^ct-001\|CT-001]] | ❌ Falhou | `GET /solicitacoes/listar-estatisticas` — `status` sem a chave `totalAnswered` | 24/24 solicitações do cliente são "Encerrado" (`totalClosed`); impossível confirmar se o valor em si seria correto, já que o campo nem existe | este próprio Bug | 0 |

---

## Decisão

**Resultado geral:** reprovado — bloqueia o fechamento do critério C7 da [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]].

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug** — não se aplica (este já é o Bug).
- [x] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados — aguardando correção do dev.
- [x] Próximo passo registrado.
