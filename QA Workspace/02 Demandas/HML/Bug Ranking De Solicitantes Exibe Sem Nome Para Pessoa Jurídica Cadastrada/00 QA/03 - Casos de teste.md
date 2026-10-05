---
demanda: "[[Bug/01 - Bug]]"
plano: ""
validacao: "[[04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — Bug ranking "Sem Nome" para PJ

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[Bug/01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

> [!example]- CT-001 · Retornar a razão social do solicitante Pessoa Jurídica no ranking
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
> **Descrição:** confirma que o ranking de solicitantes das estatísticas exibe a razão social cadastrada de um solicitante Pessoa Jurídica, em vez de "Sem Nome".
>
> **Pré-condições:**
> - Existir solicitante Pessoa Jurídica com razão social cadastrada e solicitações suficientes para entrar no ranking.
>
> **Dado** que exista um solicitante Pessoa Jurídica com razão social cadastrada, presente no ranking
> **Quando** o endpoint de estatísticas for consultado
> **Então** `rankingRequesters[].name` deve trazer a razão social cadastrada, não "Sem Nome"
>
> **Resultado esperado:** `name` reflete `legalPerson.companyName`, mesmo valor usado na listagem de solicitações para o mesmo `id`.
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
> **Execução:** reprovado — `id: 9679` ("INSTITUTO NACIONAL DO SEGURO SOCIAL" na listagem) aparece como "Sem Nome" no ranking (ver [[04 - Validação dev]])

^ct-001
