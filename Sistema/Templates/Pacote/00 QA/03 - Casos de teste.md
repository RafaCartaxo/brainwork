---
demanda: "[[Sistema/Templates/Pacote/00 QA/Melhoria/01 - Demanda]]"
plano: "[[Sistema/Templates/Pacote/00 QA/02 - Plano de teste]]"
validacao: "[[Sistema/Templates/Pacote/00 QA/04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — <ID>

> [!info]- Navegação QA
> **README do card:** [[Sistema/Templates/Pacote/00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[Sistema/Templates/Pacote/00 QA/Melhoria/01 - Demanda]]
> **Plano de teste:** [[Sistema/Templates/Pacote/00 QA/02 - Plano de teste]]
> **Casos de teste:** [[Sistema/Templates/Pacote/00 QA/03 - Casos de teste]]
> **Validação:** [[Sistema/Templates/Pacote/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[Sistema/Templates/Pacote/00 QA/05 - Preparação Qase]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[Sistema/Templates/Pacote/00 QA/Melhoria/01 - Demanda#^c1\|C1]] | [[Sistema/Templates/Pacote/00 QA/03 - Casos de teste#^ct-001\|CT-001]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- CT-001 · Título claro do cenário
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
> **Descrição:** explique em uma frase o que este caso confirma.
>
> **Pré-condições:**
> - Informe o que precisa estar preparado antes do teste.
>
> **Dado** que ...
> **Quando** ...
> **Então** ...
>
> **Resultado esperado:** descreva o comportamento observado em linguagem direta.
>
> **Pós-condição:** registre como o sistema deve ficar depois do teste.
>
> **Critérios cobertos:** [[Sistema/Templates/Pacote/00 QA/Melhoria/01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-001
