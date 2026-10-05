---
demanda: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/01 - Bug]]"
plano: ""
validacao: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — Bug totalAnswered ausente

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/00 README|Abrir README do card]]
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/04 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

> [!example]- CT-001 · Retornar o total de solicitações respondidas nas estatísticas
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o endpoint de estatísticas retorna o campo `totalAnswered` com a contagem de solicitações respondidas.
>
> **Pré-condições:**
> - Existir ao menos uma solicitação com status "Respondido".
>
> **Dado** que exista uma quantidade conhecida de solicitações respondidas
> **Quando** o endpoint de estatísticas for consultado
> **Então** `statistics.status.totalAnswered` deve estar presente e corresponder à quantidade real de solicitações respondidas
>
> **Resultado esperado:** campo presente com valor correto, sem afetar os demais contadores de status.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** critério único do bug (ver [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/01 - Bug]]).
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** não se aplica — ver nota abaixo
>
> > [!info]- Por que não se aplica
> > A pré-condição ("existir solicitação com status Respondido") é inalcançável: o sistema não tem esse status — `orderStatus` deriva do andamento interno do documento (tramitação), não do fato de já ter sido respondido ao cidadão. Confirmado em call com os responsáveis em 05/10/2026 (Marcos). O requisito foi retirado do contrato da SGV-10736 (C7), não é mais critério a satisfazer. Se o produto um dia introduzir um status "Respondido" de verdade, este CT volta a ser executável.

^ct-001
