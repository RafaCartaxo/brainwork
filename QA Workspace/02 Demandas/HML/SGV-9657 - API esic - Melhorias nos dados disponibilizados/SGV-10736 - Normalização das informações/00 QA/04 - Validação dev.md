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
  ct_002: "❌ Falhou"
  ct_003: "✅ Aprovado"
  ct_004: "⏳ Aguardando"
  ct_005: "✅ Aprovado"
  ct_006: "⏳ Aguardando"
  ct_007: "❌ Falhou"
  ct_008: "✅ Aprovado"
  ct_009: "✅ Aprovado"
  ct_010: "⏳ Aguardando"
  ct_011: "⏳ Aguardando"
  ct_012: "✅ Aprovado"
  ct_013: "⏳ Aguardando"
  ct_014: "⏳ Aguardando"
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

> [!info]- Renumeração de 05/10/2026 (call com os responsáveis)
> CT-008/CT-010 antigos (status "Respondido"/totalAnswered) saíram da rodada — ver `03 - Casos de teste#G. Fora de execução`. A tabela abaixo já usa a numeração atual (CT-008 a CT-012 renumerados; CT-013/CT-014 são novos, ainda sem execução).

---

## Contexto

- Ambiente: homologação, cliente `prefeitura-de-cuite`
- Versão/build: não informada

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-001\|CT-001]] | ✅ Aprovado | `requester.id` distinto entre solicitantes, inclusive "Sem Nome" repetidos (8540, 14098, 9679) | — | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-002\|CT-002]] | ❌ Falhou | `requester.type: "PF"/"PJ"` (abreviado) nos 10 registros reais; `novo-estatistica-atualizado.txt` confirma padrão por extenso | Correção já confirmada/agendada (grupo "Parte 2") | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/00 README\|Bug — tipo abreviado na listagem]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-003\|CT-003]] | ✅ Aprovado | `individualPerson.birthDate`/`gender` preenchidos nos 7 solicitantes PF da amostra | Nomenclatura de chave confirmada (ver `01 - Demanda`) | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-004\|CT-004]] | ⏳ Aguardando | — | Nenhum solicitante PF sem `birthDate`/`gender` na amostra de 10 — falta massa de dados pra testar a borda | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-005\|CT-005]] | ✅ Aprovado | `orderDate` presente nos 10 registros reais | — | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-006\|CT-006]] | ⏳ Aguardando | — | Nenhuma solicitação com prazo configurado na amostra — todas vieram com `orderDateDeadline: null` | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-007\|CT-007]] | ❌ Falhou | `orderDateDeadline: null` em 10/10 registros | Bloqueia C5. Confirmado real na call de 05/10/2026 — valor esperado sem prazo configurado é decisão pendente do Marcos | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/00 README\|Bug — data limite não calculada]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-008\|CT-008]] | ✅ Aprovado (ressalva) | "Encerrado" confirmado em 10/10 registros reais | CT reescrito em 05/10/2026 — não cobre mais "Respondido" (status inexistente, ver G. Fora de execução). "Recebido"/"Em Andamento" ainda sem exemplo cruzado | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-009\|CT-009]] | ✅ Aprovado | `id` distinto entre 3 "Sem Nome" do ranking | `name` do ranking tem bug à parte (PJ e Anônimo exibem "Sem Nome", confirmado na call) — não invalida este CT (é sobre `id`) | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/00 README\|Bug — ranking Sem Nome PJ]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-010\|CT-010]] | ⏳ Aguardando | — | 0 solicitações "timely" na amostra do cliente — sem caso pra confirmar a contagem | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-011\|CT-011]] | ⏳ Aguardando | — | 0 solicitações "delayed" na amostra do cliente — sem caso pra confirmar a contagem | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-012\|CT-012]] | ✅ Aprovado (ressalva) | `deadline.undefined: 24` bate com as 24 solicitações do cliente | Resultado tecnicamente correto, mas mascarado pelo Bug do CT-007 (tudo cai em "undefined" porque nada é calculado) — confirmar de novo quando o Bug for corrigido | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/00 README\|Bug — data limite não calculada]] | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-013\|CT-013]] | ⏳ Aguardando | — | Item novo (call 05/10/2026) — cenário de erro ainda não definido/executado | — | |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-014\|CT-014]] | ⏳ Aguardando | — | Item novo (call 05/10/2026) — cenário de erro ainda não definido/executado | — | |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

---

## Histórico de validação

- **2026-10-05:** primeira rodada de execução real em homologação (cliente `prefeitura-de-cuite`). 7 CTs aprovados (3 com ressalva de nomenclatura pendente), 1 reprovado (CT-007 — virou Bug), 4 aguardando massa de dados (CT-004, CT-006, CT-010, CT-011). Achado adicional fora da lista de CTs: `rankingRequesters` com nome errado pra PJ (CT-009).
- **2026-10-05 (call com os responsáveis):** confirmado que o status "Respondido" não existe no sistema — CT-008/CT-010 antigos saíram de escopo (ver `03 - Casos de teste#G. Fora de execução`); CT-009 antigo reescrito como novo CT-008 (sem "Respondido"). Confirmado que o Bug do ranking (agora CT-009) também afeta solicitante Anônimo, correção agendada. Trazidos 2 critérios/CTs novos de padronização de erro (CT-013, CT-014), ainda sem execução. Bug de paginação (500 em page=1+itemsPerPage=1000) reportado pelo dev como já corrigido — pendente reverificar.
- **2026-10-05 (Retornos esperados atualizados):** `novo-estatistica-atualizado.txt` confirma `requester.type` por extenso como padrão — a listagem real retorna abreviado (`PF`/`PJ`), CT-002 reprovado e virou Bug ([[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/00 README|10736-CT-002]]), correção já agendada no mesmo grupo "Parte 2".

---

## Decisão

**Resultado geral:** reprovado — 2 Bugs abertos (data limite não calculada, bloqueia C5; tipo do solicitante abreviado, bloqueia C2 — ambos com correção já confirmada/agendada) impedem o fechamento total. CT-010/CT-011 (timely/delayed) e CT-004/CT-006 (bordas de cadastro/prazo) aguardam massa de dados compatível. CT-013/CT-014 (erro) ainda não têm cenário de execução definido.

---

## Checklist de encerramento QA

- [x] Todos os CTs executados ou com justificativa registrada (4 aguardando massa de dados, 2 novos ainda sem cenário — justificativa na tabela acima).
- [x] Evidências e observações preenchidas quando necessário.
- [x] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [x] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados — aguardando correção do Bug de data limite antes de fechar.
- [x] Próximo passo registrado.
