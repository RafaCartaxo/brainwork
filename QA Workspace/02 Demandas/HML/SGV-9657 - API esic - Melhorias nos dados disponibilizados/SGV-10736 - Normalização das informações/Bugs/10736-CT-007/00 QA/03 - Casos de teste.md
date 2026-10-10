---
demanda: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/01 - Bug]]"
plano: ""
validacao: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/04 - Validação dev]]"
status: concluido
pontos: ""
---

# Casos de teste — Bug data limite não calculada

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/00 README|Abrir README do card]]
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/04 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

> [!example]- CT-001 · Calcular a data limite mesmo sem prazo configurado
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
> **Descrição:** confirma que a listagem calcula e retorna a data limite mesmo quando a solicitação não tem prazo configurado.
>
> **Pré-condições:**
> - Existir solicitação sem prazo de atendimento configurado.
>
> **Dado** que exista uma solicitação sem prazo de atendimento configurado
> **Quando** a listagem de solicitações for consultada
> **Então** `orderDateDeadline` deve vir preenchido (`date`/`days`/`type`), nunca `null`
>
> **Resultado esperado:** `orderDateDeadline` presente e coerente, independente de configuração de prazo.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** critério único do bug (ver [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/01 - Bug]]).
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** reprovado — `orderDateDeadline` veio `null` em 10/10 registros testados (ver [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/04 - Validação dev]])

^ct-001
