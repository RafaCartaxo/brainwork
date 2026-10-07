---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — Entrega 01

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|CTs da SGV-11971]]
> **Preparação Qase:** Não se aplica; os casos desta entrega são verificações técnicas do seed.
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[#^ct-seed-001\|SEED-001]] |
| [[01 - Demanda#^c2\|C2]] | [[#^ct-seed-002\|SEED-002]] |
| [[01 - Demanda#^c3\|C3]] | [[#^ct-seed-003\|SEED-003]] |
| [[01 - Demanda#^c4\|C4]] | [[#^ct-seed-004\|SEED-004]] |
| [[01 - Demanda#^c5\|C5]] | CT-001–012 e CT-038 da SGV-11971; resultados em [[../01 Automação/02 - Validação automação]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- SEED-001 · Selecionar a instância configurada
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
> **Descrição:** o seed usa a instância 225 quando recebe esse ID como configuração explícita.
>
> **Pré-condições:** backend configurado contém a instância 225; credencial administrativa pode consultá-la.
>
> **Dado** o ID 225 e o nome esperado “Termo De Referência - Sogov”
> **Quando** o seed resolve o alvo
> **Então** encontra a instância 225 e valida sua identidade antes de provisionar dados.
>
> **Resultado esperado:** manifesto registra o ID e o nome confirmados; nenhuma outra instância é criada.
>
> **Pós-condição:** o alvo efetivo da preparação é a instância dedicada 225.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** técnico
> **Camada:** seed/API
> **Automação:** planejada nesta entrega
> **Execução:** planejado

^ct-seed-001

---

> [!example]- SEED-002 · Interromper diante de alvo ausente ou divergente
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
> **Descrição:** um ID explícito inválido não pode levar o seed a criar ou preparar outro cliente.
>
> **Pré-condições:** testar o seletor isoladamente com ID inexistente ou nome divergente; não usar cliente de produção.
>
> **Dado** um ID explícito que não existe ou retorna nome inesperado
> **Quando** o seed tenta resolver o alvo
> **Então** encerra antes de qualquer chamada de provisionamento e não aciona fallback de criação.
>
> **Resultado esperado:** erro claro e nenhuma entidade criada ou alterada.
>
> **Pós-condição:** nenhum outro cliente recebeu dados do seed.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** técnico
> **Camada:** unidade/API
> **Automação:** planejada nesta entrega
> **Execução:** planejado

^ct-seed-002

---

> [!example]- SEED-003 · Preservar o alvo padrão sem configuração explícita
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
> **Descrição:** proteger as suítes atuais que não configuram um ID específico.
>
> **Pré-condições:** executar teste isolado do seletor; não apontar as suítes existentes à instância 225.
>
> **Dado** que `PW_INSTANCE_ID` não está definido
> **Quando** o seed resolve o alvo
> **Então** segue o comportamento padrão atual baseado no perfil `E2E Automatic Test`.
>
> **Resultado esperado:** o destino padrão e sua impressão digital continuam compatíveis com as execuções atuais.
>
> **Pós-condição:** suítes sem override continuam usando o alvo padrão.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão técnica
> **Camada:** unidade/API
> **Automação:** planejada nesta entrega
> **Execução:** planejado

^ct-seed-003

---

> [!example]- SEED-004 · Reconciliar a mesma instância na reexecução
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
> **Descrição:** confirmar que duas execuções usam a mesma instância e reconciliam os dados-base sem duplicação.
>
> **Pré-condições:** ID 225 validado; backend e permissões administrativas confirmados.
>
> **Dado** que o seed foi executado uma vez na instância 225
> **Quando** for executado novamente com a mesma configuração
> **Então** reutiliza o ID 225 e reconcilia as entidades necessárias.
>
> **Resultado esperado:** os dois manifestos registram a instância 225; a segunda execução não cria outra instância nem duplica atores-chave.
>
> **Pós-condição:** alvo e dados-base permanecem associados à mesma instância.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** técnico
> **Camada:** API
> **Automação:** planejada nesta entrega
> **Execução:** planejado

^ct-seed-004
