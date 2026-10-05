---
demanda: "[[Bug/01 - Bug]]"
plano: ""
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — Bug totalAnswered ausente

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[Bug/01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

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
> **Critérios cobertos:** critério único do bug (ver [[Bug/01 - Bug]]).
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** reprovado — campo `totalAnswered` ausente do retorno (ver [[04 - Validação dev]])

^ct-001
