---
demanda: "[[01 - Bug]]"
plano: ""
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — Bug tipo do solicitante abreviado

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

> [!example]- CT-001 · Retornar o tipo do solicitante por extenso na listagem
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
> **Descrição:** confirma que a listagem retorna o tipo do solicitante por extenso, no mesmo padrão já usado pelas estatísticas.
>
> **Pré-condições:**
> - Existir solicitação de solicitante Pessoa Física e de Pessoa Jurídica.
>
> **Dado** que existam solicitações de um solicitante Pessoa Física e de um solicitante Pessoa Jurídica
> **Quando** a listagem de solicitações for consultada
> **Então** `requester.type` deve vir por extenso ("Pessoa Física"/"Pessoa Jurídica"), não abreviado
>
> **Resultado esperado:** mesmo padrão de valor já usado em `rankingRequesters[].type` nas estatísticas.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** critério único do bug (ver [[01 - Bug]]).
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** reprovado — `requester.type` veio `"PF"`/`"PJ"` (abreviado) em 10/10 registros reais (ver [[04 - Validação dev]]); correção já agendada

^ct-001
