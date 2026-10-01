---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-11176

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle dos casos de teste  
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c9\|C9]] | [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c10\|C10]] | [[03 - Casos de teste#^ct-010\|CT-010]] |
| [[01 - Demanda#^c11\|C11]] | [[03 - Casos de teste#^ct-011\|CT-011]] |
| [[01 - Demanda#^c12\|C12]] | [[03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c13\|C13]] | [[03 - Casos de teste#^ct-013\|CT-013]] |
| [[01 - Demanda#^c14\|C14]] | [[03 - Casos de teste#^ct-014\|CT-014]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- CT-001 · Departamento novo gera link permanente sem expiração nem limite de uso
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
> **Descrição:** confirma que a criação de um departamento já gera um link de convite permanente.
>
> **Pré-condições:**  
> - Servidor está criando um novo departamento para um cidadão PJ.
>
> **Dado** que um departamento seja criado  
> **Quando** a criação for concluída  
> **Então** o sistema gera um link de convite permanente, sem expiração e sem limite de uso
>
> **Resultado esperado:** link gerado automaticamente, acessível a qualquer momento, sem contagem de usos.
>
> **Pós-condição:** link permanente disponível para uso em qualquer momento futuro.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · E-mail de notificação de criação contém o link permanente
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
> **Descrição:** confirma que o e-mail de criação do departamento carrega o link permanente.
>
> **Pré-condições:**  
> - Departamento acabou de ser criado (CT-001).
>
> **Dado** que o departamento tenha sido criado  
> **Quando** o e-mail de notificação for enviado ao departamento  
> **Então** a mensagem contém o link permanente de convite
>
> **Resultado esperado:** link presente e funcional no corpo do e-mail.
>
> **Pós-condição:** nenhuma alteração de estado além do envio do e-mail.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Gerar link temporário a partir da lista de cidadãos
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
> **Descrição:** confirma a geração de convite temporário a partir do menu de opções da lista de cidadãos.
>
> **Pré-condições:**  
> - Servidor está na lista de cidadãos.  
> - Cidadão possui ao menos um departamento ativo.
>
> **Dado** que o servidor esteja na lista de cidadãos  
> **Quando** selecionar "Convidar via link" no menu de opções de um cidadão  
> **Então** o sistema exige a escolha de um departamento ativo desse cidadão e gera o convite
>
> **Resultado esperado:** convite temporário gerado para o departamento escolhido.
>
> **Pós-condição:** convite ativo, ainda não utilizado.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Gerar link temporário a partir da edição do cidadão
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
> **Descrição:** confirma a geração de convite temporário a partir da tela de edição do cidadão.
>
> **Pré-condições:**  
> - Servidor está editando um cidadão com ao menos um departamento.
>
> **Dado** que o servidor esteja editando um cidadão  
> **Quando** selecionar "Convidar via link" em um departamento  
> **Então** o sistema gera o convite para esse departamento
>
> **Resultado esperado:** mesmo comportamento de CT-003, disparado por outro ponto de entrada.
>
> **Pós-condição:** convite ativo, ainda não utilizado.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Link copiado automaticamente para a área de transferência
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
> **Descrição:** confirma que o link gerado pelo servidor é copiado automaticamente ao ser criado.
>
> **Pré-condições:**  
> - Servidor concluiu a geração de um convite (CT-003 ou CT-004).
>
> **Dado** que o convite seja gerado  
> **Quando** a operação for concluída  
> **Então** o link é copiado automaticamente para a área de transferência
>
> **Resultado esperado:** colar (Ctrl+V) logo em seguida reproduz o link gerado.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Link temporário aceita um único cadastro e expira em 7 dias
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
> **Descrição:** confirma a regra central de validade do link temporário — uso único e expiração em 7 dias.
>
> **Pré-condições:**  
> - Convite temporário gerado por um servidor.
>
> **Dado** que o link tenha sido gerado por um servidor  
> **Quando** for utilizado  
> **Então** aceita apenas um cadastro e expira após 7 dias
>
> **Resultado esperado:** segundo uso (mesmo dentro dos 7 dias) ou uso após o 7º dia é bloqueado.
>
> **Pós-condição:** convite marcado como usado ou expirado, conforme o caso testado.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Link já utilizado ou expirado bloqueia novo cadastro
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
> **Descrição:** confirma que um convite inválido nunca permite novo cadastro.
>
> **Pré-condições:**  
> - Link já utilizado uma vez, ou gerado há mais de 7 dias.
>
> **Dado** que o link já tenha sido utilizado ou esteja expirado  
> **Quando** alguém tentar acessá-lo  
> **Então** o sistema impede o cadastro e informa que o convite não é válido
>
> **Resultado esperado:** mensagem clara de convite inválido, sem opção de prosseguir.
>
> **Pós-condição:** nenhum vínculo ou cadastro criado.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-007

> [!example]- CT-008 · Convite persiste quem gerou e quem se cadastrou por ele
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
> **Descrição:** confirma a rastreabilidade do convite — servidor que gerou e cidadão que se cadastrou.
>
> **Pré-condições:**  
> - Convite gerado por um servidor (CT-003/CT-004) e depois utilizado por um cidadão (CT-009/CT-010).
>
> **Dado** que um convite seja gerado por um servidor  
> **Quando** o convite for criado  
> **Então** o sistema persiste o servidor que gerou o link  
> **E dado** que o link seja utilizado para concluir um cadastro  
> **Quando** o cidadão concluir o cadastro  
> **Então** o sistema persiste no convite o cidadão cadastrado
>
> **Resultado esperado:** os dois dados (servidor gerador e cidadão cadastrado) ficam disponíveis para consulta no convite.
>
> **Pós-condição:** registro do convite completo com as duas pontas.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-008

> [!example]- CT-009 · Pessoa com cadastro entra no departamento pelo convite
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
> **Descrição:** confirma o fluxo de entrada por convite para quem já tem cadastro no SOGOV.
>
> **Pré-condições:**  
> - Convite válido (permanente ou temporário).  
> - Pessoa convidada já possui cadastro no SOGOV.
>
> **Dado** que a pessoa convidada já possua cadastro no SOGOV  
> **Quando** acessar um convite válido  
> **Então** realiza login, informa sua função e confirma a entrada no departamento, sendo adicionada como participante
>
> **Resultado esperado:** pessoa vira participante do departamento com a função informada.
>
> **Pós-condição:** participante listado no departamento (mesma listagem coberta pela SGV-11083).
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-009

> [!example]- CT-010 · Pessoa sem cadastro completa o cadastro e entra no departamento pelo convite
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
> **Descrição:** confirma o fluxo de entrada por convite para quem ainda não tem cadastro no SOGOV.
>
> **Pré-condições:**  
> - Convite válido (permanente ou temporário).  
> - Pessoa convidada não possui cadastro no SOGOV.
>
> **Dado** que a pessoa convidada não possua cadastro no SOGOV  
> **Quando** acessar um convite válido  
> **Então** conclui o cadastro, informa sua função e confirma a entrada no departamento, sendo adicionada como participante
>
> **Resultado esperado:** cadastro criado e pessoa já entra como participante no mesmo fluxo.
>
> **Pós-condição:** participante listado no departamento; cadastro novo ativo no SOGOV.
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-010

> [!example]- CT-011 · Seletor de perfil abre com "Perfil pessoal" como padrão
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
> **Descrição:** confirma o valor padrão do seletor de perfil na tela de solicitações.
>
> **Pré-condições:**  
> - Cidadão participa de ao menos um departamento.
>
> **Dado** que o cidadão acesse a tela de solicitações  
> **Quando** o seletor de perfil for exibido  
> **Então** o valor padrão é "Perfil pessoal"
>
> **Resultado esperado:** nenhuma solicitação de departamento aparece pré-filtrada sem ação do cidadão.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-011

> [!example]- CT-012 · Seletor lista CNPJs e departamentos do cidadão
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
> **Descrição:** confirma o conteúdo do seletor de perfil quando o cidadão participa de departamentos.
>
> **Pré-condições:**  
> - Cidadão participa de departamentos de um ou mais CNPJs.
>
> **Dado** que o cidadão participe de departamentos  
> **Quando** abrir o seletor  
> **Então** são listados os CNPJs e seus respectivos departamentos conforme o Figma
>
> **Resultado esperado:** hierarquia CNPJ → departamentos exibida corretamente, sem departamento de outro cidadão.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-012

> [!example]- CT-013 · Selecionar um departamento filtra as solicitações
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
> **Descrição:** confirma que selecionar um departamento restringe a listagem de solicitações.
>
> **Pré-condições:**  
> - Cidadão participa de ao menos um departamento com solicitações registradas.
>
> **Dado** que o cidadão selecione um departamento  
> **Quando** a seleção for aplicada  
> **Então** a tela exibe somente as solicitações relacionadas ao departamento escolhido
>
> **Resultado esperado:** solicitações pessoais e de outros departamentos ficam ocultas.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-013

> [!example]- CT-014 · Selecionar "Perfil pessoal" exibe todas as solicitações do cidadão
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
> **Descrição:** confirma que voltar para "Perfil pessoal" remove qualquer filtro de departamento.
>
> **Pré-condições:**  
> - Cidadão tinha um departamento selecionado no filtro.
>
> **Dado** que o cidadão selecione "Perfil pessoal"  
> **Quando** a seleção for aplicada  
> **Então** a tela exibe todas as suas solicitações
>
> **Resultado esperado:** nenhuma solicitação pessoal fica oculta pelo filtro anterior.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c14|C14]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-014
