---
demanda: "[[01 - Bug]]"
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

# Validação — Bug tipo do solicitante abreviado

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/00 README|Abrir README do card]]
> **Bug:** [[01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/04 - Validação dev]]

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
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/03 - Casos de teste#^ct-001\|CT-001]] | ❌ Falhou | `requester.type: "PF"`/`"PJ"` em 10/10 registros reais; `novo-estatistica-atualizado.txt` confirma padrão por extenso | Correção já confirmada/agendada pelo dev (grupo "Parte 2" da call de 05/10/2026) | este próprio Bug | 0 |

---

## Decisão

**Resultado geral:** reprovado — bloqueia o fechamento do critério C2 da [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda|SGV-10736]] até o retestar. Correção já confirmada/agendada, não é achado novo em aberto.

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada.
- [x] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug** — não se aplica (este já é o Bug).
- [x] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados — aguardando ambiente de teste pra reteste.
- [x] Próximo passo registrado.
