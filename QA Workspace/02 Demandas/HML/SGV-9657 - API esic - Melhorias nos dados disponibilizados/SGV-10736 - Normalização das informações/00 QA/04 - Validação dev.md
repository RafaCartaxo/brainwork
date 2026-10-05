---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: hml
versao: ""
status: execucao
responsavel: Rafael
resultado: reprovado
pontos: 0
ct_resultados:
  ct_001: "✅ Aprovado"
  ct_002: "✅ Aprovado"
  ct_003: "✅ Aprovado"
  ct_004: "⏳ Aguardando"
  ct_005: "✅ Aprovado"
  ct_006: "⏳ Aguardando"
  ct_007: "❌ Falhou"
  ct_008: "⏳ Aguardando"
  ct_009: "⏳ Aguardando"
  ct_010: "❌ Falhou"
  ct_011: "✅ Aprovado"
  ct_012: "⏳ Aguardando"
  ct_013: "⏳ Aguardando"
  ct_014: "✅ Aprovado"
data_inicio: 2026-10-05
data_fim: ""
---

# Validação — SGV-10736

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da execução dos CTs e das evidências. Os cenários permanecem em `03 - Casos de teste.md`. Fluxo 3f (API) — sem esteira DEV, validação direta em homologação via Postman/curl/swagger.

---

## Contexto

- Ambiente: homologação, cliente `prefeitura-de-cuite`
- Versão/build: não informada

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-001\|CT-001]] | ✅ Aprovado | `rankingRequesters` com 3 ids "Sem Nome" distintos (8540, 14098, 9679) e listagem com ids distintos por solicitante | — | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-002\|CT-002]] | ✅ Aprovado (ressalva) | `requester.type: "PF"/"PJ"` nos 10 registros reais | Distinção funciona; nomenclatura diverge do documentado (ver Pendências de decisão em `01 - Demanda`) | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-003\|CT-003]] | ✅ Aprovado (ressalva) | `individualPerson.birthDate`/`gender` preenchidos nos 7 solicitantes PF da amostra | Mesma ressalva de nomenclatura do CT-002 | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-004\|CT-004]] | ⏳ Aguardando | — | Nenhum solicitante PF sem `birthDate`/`gender` na amostra de 10 — falta massa de dados pra testar a borda | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-005\|CT-005]] | ✅ Aprovado | `orderDate` presente nos 10 registros reais | — | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-006\|CT-006]] | ⏳ Aguardando | — | Nenhuma solicitação com prazo configurado na amostra — todas vieram com `orderDateDeadline: null` | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-007\|CT-007]] | ❌ Falhou | `orderDateDeadline: null` em 10/10 registros | Bloqueia C5 | [[../Bugs/10736-CT-007/00 QA/00 README\|Bug — data limite não calculada]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-008\|CT-008]] | ⏳ Aguardando | — | Nenhuma solicitação "Respondido" nas 24 do cliente (todas "Encerrado") | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-009\|CT-009]] | ⏳ Aguardando | — | Só "Encerrado" confirmado nos dados reais; falta massa com os outros 3 status | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-010\|CT-010]] | ❌ Falhou | `status` sem a chave `totalAnswered` | Bloqueia C7 | [[../Bugs/10736-CT-010/00 QA/00 README\|Bug — totalAnswered ausente]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-011\|CT-011]] | ✅ Aprovado | `id` distinto entre 3 "Sem Nome" do ranking | `name` do ranking tem bug à parte (PJ exibe "Sem Nome") — não invalida este CT (é sobre `id`), mas achado separado registrado | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/00 README\|Bug — ranking Sem Nome PJ]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-012\|CT-012]] | ⏳ Aguardando | — | 0 solicitações "timely" na amostra do cliente — sem caso pra confirmar a contagem | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-013\|CT-013]] | ⏳ Aguardando | — | 0 solicitações "delayed" na amostra do cliente — sem caso pra confirmar a contagem | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-014\|CT-014]] | ✅ Aprovado (ressalva) | `deadline.undefined: 24` bate com as 24 solicitações do cliente | Resultado tecnicamente correto, mas mascarado pelo Bug do CT-007 (tudo cai em "undefined" porque nada é calculado) — confirmar de novo quando o Bug for corrigido | [[../Bugs/10736-CT-007/00 QA/00 README\|Bug — data limite não calculada]] | |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

---

## Histórico de validação

- **2026-10-05:** primeira rodada de execução real em homologação (cliente `prefeitura-de-cuite`). 7 CTs aprovados (3 com ressalva de nomenclatura pendente), 2 reprovados (CT-007, CT-010 — viraram Bug), 5 aguardando massa de dados (CT-004, CT-006, CT-008, CT-009, CT-012, CT-013). Achado adicional fora da lista de CTs: `rankingRequesters` com nome errado pra PJ (ver CT-011).

---

## Decisão

**Resultado geral:** reprovado — 2 Bugs abertos (data limite não calculada, totalAnswered ausente) bloqueiam o fechamento de C5 e C7. Retestar após correção; completar CT-004/006/008/009/012/013 quando houver massa de dados compatível (solicitante PF sem cadastro completo, solicitação com prazo configurado, solicitação "Respondido", solicitações timely/delayed).

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada (5 aguardando massa de dados, justificativa na tabela acima).
- [x] Evidências e observações preenchidas quando necessário.
- [x] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [x] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados — aguardando correção dos 2 Bugs antes de fechar.
- [x] Próximo passo registrado.
