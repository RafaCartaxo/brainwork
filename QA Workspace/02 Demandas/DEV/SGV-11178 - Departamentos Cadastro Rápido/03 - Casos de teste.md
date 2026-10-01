---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-11178

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
| [[01 - Demanda#^c15\|C15]] | [[03 - Casos de teste#^ct-015\|CT-015]] |
| [[01 - Demanda#^c16\|C16]] | [[03 - Casos de teste#^ct-016\|CT-016]] |
| [[01 - Demanda#^c17\|C17]] | [[03 - Casos de teste#^ct-017\|CT-017]] |
| [[01 - Demanda#^c18\|C18]] | [[03 - Casos de teste#^ct-018\|CT-018]] |
| [[01 - Demanda#^c19\|C19]] | [[03 - Casos de teste#^ct-019\|CT-019]] |
| [[01 - Demanda#^c20\|C20]] | [[03 - Casos de teste#^ct-020\|CT-020]] |
| [[01 - Demanda#^c21\|C21]] | [[03 - Casos de teste#^ct-021\|CT-021]] |
| [[01 - Demanda#^c22\|C22]] | [[03 - Casos de teste#^ct-022\|CT-022]] |
| [[01 - Demanda#^c23\|C23]] | [[03 - Casos de teste#^ct-023\|CT-023]] |
| [[01 - Demanda#^c24\|C24]] | [[03 - Casos de teste#^ct-024\|CT-024]] |
| [[01 - Demanda#^c25\|C25]] | [[03 - Casos de teste#^ct-025\|CT-025]] |
| [[01 - Demanda#^c26\|C26]] | [[03 - Casos de teste#^ct-026\|CT-026]] |
| [[01 - Demanda#^c27\|C27]] | [[03 - Casos de teste#^ct-027\|CT-027]] |
| [[01 - Demanda#^c28\|C28]] | [[03 - Casos de teste#^ct-028\|CT-028]] |
| [[01 - Demanda#^c29\|C29]] | [[03 - Casos de teste#^ct-029\|CT-029]] |
| [[01 - Demanda#^c30\|C30]] | [[03 - Casos de teste#^ct-030\|CT-030]] |
| [[01 - Demanda#^c31\|C31]] | [[03 - Casos de teste#^ct-031\|CT-031]] |
| [[01 - Demanda#^c32\|C32]] | [[03 - Casos de teste#^ct-032\|CT-032]] |
| [[01 - Demanda#^c33\|C33]] | [[03 - Casos de teste#^ct-033\|CT-033]] |
| [[01 - Demanda#^c34\|C34]] | [[03 - Casos de teste#^ct-034\|CT-034]] |
| [[01 - Demanda#^c35\|C35]] | [[03 - Casos de teste#^ct-035\|CT-035]] |
| [[01 - Demanda#^c36\|C36]] | [[03 - Casos de teste#^ct-036\|CT-036]] |
| [[01 - Demanda#^c37\|C37]] | [[03 - Casos de teste#^ct-037\|CT-037]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---


> [!example]- CT-001 · Atalho de cadastro rápido disponível no componente de seleção
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
> **Descrição:** confirma que um componente de seleção de pessoa que permite adicionar cidadão disponibiliza o atalho de cadastro rápido.
>
> **Pré-condições:**  
> - Servidor está em um campo do tipo pessoa ou componente de seleção de usuário que permite adicionar cidadão.
>
> **Dado** que o servidor esteja em um componente de seleção que permita adicionar um cidadão  
> **Quando** o componente for exibido  
> **Então** o sistema disponibiliza um atalho para o cadastro rápido
>
> **Resultado esperado:** atalho visível e acionável no componente.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-001


> [!example]- CT-002 · Atalho consistente entre os contextos de uso
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
> **Descrição:** confirma que o atalho aparece de forma consistente nos quatro contextos previstos.
>
> **Pré-condições:**  
> - Servidor tem acesso aos quatro contextos: campo solicitante, campo tipo pessoa PF/PJ, destinatário de despacho, seleção de signatário.
>
> **Dado** que o servidor acesse cada um dos contextos (campo solicitante, campo do tipo pessoa PF/PJ, destinatário de despacho, seleção de signatário)  
> **Quando** o componente de seleção for exibido em cada um  
> **Então** o atalho de cadastro rápido é oferecido da mesma forma em todos
>
> **Resultado esperado:** comportamento idêntico do atalho nos 4 contextos, sem variação de disponibilidade.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002


> [!example]- CT-003 · Escolha entre Pessoa Física, Pessoa Jurídica e Departamento
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
> **Descrição:** confirma que acionar o atalho exibe a opção de escolher entre os 3 tipos de cadastro.
>
> **Pré-condições:**  
> - Atalho de cadastro rápido disponível (CT-001).
>
> **Dado** que o servidor acione o atalho  
> **Quando** o formulário for exibido  
> **Então** é possível escolher entre Pessoa Física, Pessoa Jurídica e Departamento
>
> **Resultado esperado:** as 3 opções aparecem disponíveis para seleção.
>
> **Pós-condição:** nenhuma.
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


> [!example]- CT-004 · Seleção automática do registro criado no campo de origem
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
> **Descrição:** confirma que, ao concluir o cadastro rápido com sucesso, o registro criado é selecionado automaticamente no campo de origem.
>
> **Pré-condições:**  
> - Cadastro rápido concluído com sucesso (qualquer tipo) a partir de um campo compatível.
>
> **Dado** que o cadastro rápido seja concluído com sucesso  
> **Quando** o sistema retornar ao componente de origem  
> **Então** o novo registro fica disponível e selecionado no campo, desde que compatível com os parâmetros desse campo
>
> **Resultado esperado:** campo de origem já exibe o registro recém-criado selecionado, sem busca manual.
>
> **Pós-condição:** registro criado e vinculado ao campo de origem.
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


> [!example]- CT-005 · Seletor radio button com as três opções
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
> **Descrição:** confirma a apresentação do seletor de tipo do formulário de cadastro rápido.
>
> **Pré-condições:**  
> - Formulário de cadastro rápido aberto.
>
> **Dado** que o formulário de cadastro rápido esteja aberto  
> **Quando** o servidor visualizar as opções  
> **Então** o sistema apresenta um seletor do tipo radio button com as opções Pessoa Física, Pessoa Jurídica e Departamento
>
> **Resultado esperado:** as 3 opções aparecem como radio button, mutuamente exclusivas.
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


> [!example]- CT-006 · Apenas um formulário exibido por vez
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
> **Descrição:** confirma que somente o formulário do tipo selecionado é exibido.
>
> **Pré-condições:**  
> - Formulário de cadastro rápido aberto, um tipo selecionado.
>
> **Dado** que um tipo de cadastro esteja selecionado  
> **Quando** sua opção estiver ativa  
> **Então** somente o formulário correspondente é exibido
>
> **Resultado esperado:** campos dos outros dois tipos ficam ocultos, não só desabilitados.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-006


> [!example]- CT-007 · Preservação de dados ao alternar entre tipos
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
> **Descrição:** confirma que dados preenchidos num tipo não se perdem ao alternar para outro e voltar.
>
> **Pré-condições:**  
> - Servidor preencheu parcial ou totalmente um formulário (ex.: Pessoa Física).
>
> **Dado** que o servidor tenha preenchido parcial ou totalmente um formulário  
> **Quando** alternar para outro tipo e retornar ao anterior  
> **Então** os dados informados anteriormente permanecem preenchidos enquanto o cadastro rápido estiver aberto
>
> **Resultado esperado:** nenhum campo já preenchido é limpo pela troca de tipo.
>
> **Pós-condição:** nenhuma, enquanto o formulário permanecer aberto.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-007


> [!example]- CT-008 · Campos do formulário de Pessoa Física
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
> **Descrição:** confirma os campos apresentados no formulário de Pessoa Física.
>
> **Pré-condições:**  
> - Opção Pessoa Física selecionada.
>
> **Dado** que a opção Pessoa Física esteja selecionada  
> **Quando** o formulário for exibido  
> **Então** são apresentados os campos CPF, Nome, E-mail e Telefone
>
> **Resultado esperado:** os 4 campos aparecem, sem campo adicional não previsto.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-008


> [!example]- CT-009 · Estado inicial dos campos de Pessoa Física
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
> **Descrição:** confirma o estado inicial do formulário antes de qualquer CPF válido consultado.
>
> **Pré-condições:**  
> - Formulário de Pessoa Física aberto, nenhum CPF consultado ainda.
>
> **Dado** que o formulário de Pessoa Física tenha sido aberto  
> **Quando** nenhum CPF válido tiver sido consultado  
> **Então** o campo Nome permanece desabilitado, e os campos E-mail e Telefone são opcionais
>
> **Resultado esperado:** Nome não editável; formulário não bloqueia confirmação por E-mail/Telefone vazios nesse estado.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-009


> [!example]- CT-010 · Validação do CPF antes da consulta à API
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
> **Descrição:** confirma que o CPF é validado no front antes de qualquer chamada à API.
>
> **Pré-condições:**  
> - Formulário de Pessoa Física aberto.
>
> **Dado** que o servidor informe um CPF  
> **Quando** o valor for submetido à consulta  
> **Então** o sistema valida o CPF antes de consultar a API
>
> **Resultado esperado:** CPF com formato/dígito verificador inválido não dispara chamada à API.
>
> **Pós-condição:** nenhuma consulta realizada para CPF inválido.
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-010


> [!example]- CT-011 · Preenchimento automático do Nome via API
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
> **Descrição:** confirma o preenchimento automático do Nome quando a API retorna dados de um CPF válido.
>
> **Pré-condições:**  
> - CPF válido informado e submetido à consulta.
>
> **Dado** que um CPF válido tenha sido informado  
> **Quando** a API retornar os dados correspondentes  
> **Então** o sistema preenche automaticamente o Nome, mantendo o campo desabilitado para edição
>
> **Resultado esperado:** Nome preenchido e não editável.
>
> **Pós-condição:** formulário pronto para conclusão (Nome preenchido).
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-011


> [!example]- CT-012 · Conclusão do cadastro de Pessoa Física
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
> **Descrição:** confirma que o cadastro é criado mesmo sem E-mail/Telefone, desde que CPF e Nome estejam validados.
>
> **Pré-condições:**  
> - CPF e Nome validados (CT-010/CT-011).
>
> **Dado** que o CPF e o Nome tenham sido validados  
> **Quando** o servidor confirmar o formulário  
> **Então** o sistema cria o cadastro da pessoa física, independentemente do preenchimento de E-mail ou Telefone
>
> **Resultado esperado:** cadastro criado com sucesso mesmo com E-mail/Telefone vazios.
>
> **Pós-condição:** pessoa física cadastrada no sistema.
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-012


> [!example]- CT-013 · Notificação por e-mail ao concluir cadastro com e-mail informado
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
> **Descrição:** confirma o envio de notificação ao cidadão quando um e-mail é informado no cadastro rápido de Pessoa Física.
>
> **Pré-condições:**  
> - Cadastro rápido de Pessoa Física concluído com e-mail preenchido.
>
> **Dado** que o servidor tenha informado um e-mail  
> **Quando** o cadastro da pessoa física for concluído  
> **Então** o cidadão recebe uma notificação por e-mail com as instruções para completar seu cadastro
>
> **Resultado esperado:** e-mail de notificação enviado ao endereço informado.
>
> **Pós-condição:** notificação registrada/enviada.
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-013


> [!example]- CT-014 · Falha na consulta de CPF
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
> **Descrição:** confirma o tratamento de erro quando o CPF é inválido ou a API não retorna os dados necessários.
>
> **Pré-condições:**  
> - CPF inválido informado, ou API indisponível/sem retorno.
>
> **Dado** que o CPF seja inválido ou que a API não retorne os dados necessários  
> **Quando** a consulta for processada  
> **Então** o sistema impede a conclusão do cadastro e apresenta uma mensagem de erro adequada
>
> **Resultado esperado:** cadastro não é criado; mensagem de erro clara exibida.
>
> **Pós-condição:** nenhum cadastro criado; dados preenchidos preservados no formulário.
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


> [!example]- CT-015 · Campos do formulário de Pessoa Jurídica
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
> **Descrição:** confirma os campos apresentados no formulário de Pessoa Jurídica.
>
> **Pré-condições:**  
> - Opção Pessoa Jurídica selecionada.
>
> **Dado** que a opção Pessoa Jurídica esteja selecionada  
> **Quando** o formulário for exibido  
> **Então** são apresentados os campos CNPJ, Razão Social, Nome fantasia, Telefone, E-mail, CPF do responsável legal e Nome do responsável legal
>
> **Resultado esperado:** os 7 campos aparecem, sem campo adicional não previsto.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c15|C15]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** reprovado — [[Defeitos/SGV-11958 - Defeito Formulário De Pessoa Jurídica Não Coleta E-mail|SGV-11958]]

^ct-015


> [!example]- CT-016 · Estado inicial dos campos de Pessoa Jurídica
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
> **Descrição:** confirma o estado inicial do formulário antes de qualquer CNPJ válido consultado.
>
> **Pré-condições:**  
> - Formulário de Pessoa Jurídica aberto, nenhum CNPJ consultado ainda.
>
> **Dado** que o formulário de Pessoa Jurídica tenha sido aberto  
> **Quando** nenhum CNPJ válido tiver sido consultado  
> **Então** os campos Razão Social e Nome fantasia permanecem desabilitados
>
> **Resultado esperado:** Razão Social e Nome fantasia não editáveis nesse estado.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c16|C16]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-016


> [!example]- CT-017 · Validação do CNPJ antes da consulta à API
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
> **Descrição:** confirma que o CNPJ é validado no front antes de qualquer chamada à API.
>
> **Pré-condições:**  
> - Formulário de Pessoa Jurídica aberto.
>
> **Dado** que o servidor informe um CNPJ  
> **Quando** o valor for submetido à consulta  
> **Então** o sistema valida o CNPJ antes de consultar a API
>
> **Resultado esperado:** CNPJ com formato/dígito verificador inválido não dispara chamada à API.
>
> **Pós-condição:** nenhuma consulta realizada para CNPJ inválido.
>
> **Critérios cobertos:** [[01 - Demanda#^c17|C17]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-017


> [!example]- CT-018 · Preenchimento automático de Razão Social e Nome fantasia
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
> **Descrição:** confirma o preenchimento automático quando a API retorna dados de um CNPJ válido.
>
> **Pré-condições:**  
> - CNPJ válido informado e submetido à consulta.
>
> **Dado** que um CNPJ válido tenha sido informado  
> **Quando** a API retornar os dados correspondentes  
> **Então** o sistema preenche automaticamente a Razão Social e o Nome fantasia
>
> **Resultado esperado:** os dois campos preenchidos com os dados retornados.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c18|C18]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-018


> [!example]- CT-019 · Habilitação do Nome fantasia para edição
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
> **Descrição:** confirma que, após o preenchimento automático, o Nome fantasia fica editável enquanto a Razão Social permanece bloqueada.
>
> **Pré-condições:**  
> - Razão Social e Nome fantasia preenchidos automaticamente (CT-018).
>
> **Dado** que a API tenha retornado os dados da pessoa jurídica  
> **Quando** o Nome fantasia for preenchido  
> **Então** o campo fica habilitado para edição, enquanto a Razão Social permanece desabilitada
>
> **Resultado esperado:** servidor consegue editar o Nome fantasia, mas não a Razão Social.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c19|C19]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-019


> [!example]- CT-020 · Conclusão do cadastro de Pessoa Jurídica sem campos opcionais
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
> **Descrição:** confirma que o cadastro é concluído sem Telefone ou CPF do responsável legal.
>
> **Pré-condições:**  
> - CNPJ válido consultado, Razão Social/Nome fantasia preenchidos.
>
> **Dado** que o servidor esteja preenchendo o formulário  
> **Quando** optar por não informar Telefone ou CPF do responsável legal  
> **Então** o sistema permite a conclusão do cadastro sem esses dados
>
> **Resultado esperado:** cadastro criado com sucesso mesmo com os dois campos opcionais vazios.
>
> **Pós-condição:** pessoa jurídica cadastrada no sistema.
>
> **Critérios cobertos:** [[01 - Demanda#^c20|C20]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-020


> [!example]- CT-021 · Validação do CPF do responsável legal
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
> **Descrição:** confirma a validação e consulta do CPF do responsável legal.
>
> **Pré-condições:**  
> - Formulário de Pessoa Jurídica aberto, CNPJ já validado.
>
> **Dado** que o servidor informe o CPF do responsável legal  
> **Quando** o campo for validado  
> **Então** o sistema valida o CPF e consulta o nome correspondente na API
>
> **Resultado esperado:** CPF validado antes da consulta, mesma regra do CPF de Pessoa Física.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c21|C21]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-021


> [!example]- CT-022 · Preenchimento automático do Nome do responsável legal
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
> **Descrição:** confirma o preenchimento automático do nome do responsável legal via API.
>
> **Pré-condições:**  
> - CPF válido do responsável legal consultado (CT-021).
>
> **Dado** que o CPF válido do responsável legal tenha sido consultado  
> **Quando** a API retornar os dados  
> **Então** o sistema preenche automaticamente o Nome do responsável legal, mantendo o campo desabilitado para edição
>
> **Resultado esperado:** Nome do responsável preenchido e não editável.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c22|C22]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-022


> [!example]- CT-023 · Falha na consulta do CPF do responsável legal
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
> **Descrição:** confirma o tratamento de erro quando o CPF do responsável legal é inválido ou a API não retorna o nome.
>
> **Pré-condições:**  
> - CPF do responsável legal informado.
>
> **Dado** que o CPF do responsável legal tenha sido informado  
> **Quando** o CPF for inválido ou a API não retornar o nome  
> **Então** o sistema impede a conclusão do cadastro e apresenta uma mensagem de erro adequada
>
> **Resultado esperado:** cadastro não é criado; mensagem de erro específica ao campo do responsável legal.
>
> **Pós-condição:** nenhum cadastro criado; dados preenchidos preservados.
>
> **Critérios cobertos:** [[01 - Demanda#^c23|C23]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-023


> [!example]- CT-024 · Falha na consulta do CNPJ
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
> **Descrição:** confirma o tratamento de erro quando o CNPJ é inválido ou a API não retorna os dados obrigatórios.
>
> **Pré-condições:**  
> - CNPJ inválido informado, ou API indisponível/sem retorno.
>
> **Dado** que o CNPJ seja inválido ou que a API não retorne os dados obrigatórios  
> **Quando** a consulta for processada  
> **Então** o sistema impede a conclusão do cadastro e apresenta uma mensagem de erro adequada
>
> **Resultado esperado:** cadastro não é criado; mensagem de erro clara exibida.
>
> **Pós-condição:** nenhum cadastro criado; dados preenchidos preservados.
>
> **Critérios cobertos:** [[01 - Demanda#^c24|C24]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-024


> [!example]- CT-025 · Campos do formulário de Departamento
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
> **Descrição:** confirma os campos apresentados no formulário de Departamento.
>
> **Pré-condições:**  
> - Opção Departamento selecionada.
>
> **Dado** que a opção Departamento esteja selecionada  
> **Quando** o formulário for exibido  
> **Então** são apresentados o seletor de Pessoa Jurídica, o Nome do departamento e o E-mail
>
> **Resultado esperado:** os 3 campos aparecem, sem campo adicional não previsto.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c25|C25]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-025


> [!example]- CT-026 · Obrigatoriedade dos campos de Departamento
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
> **Descrição:** confirma que todos os campos do formulário de Departamento são obrigatórios.
>
> **Pré-condições:**  
> - Formulário de Departamento aberto.
>
> **Dado** que o servidor esteja preenchendo o formulário de Departamento  
> **Quando** tentar concluir o cadastro com algum campo vazio  
> **Então** o sistema exige o preenchimento de todos os campos
>
> **Resultado esperado:** confirmação bloqueada até todos os campos serem preenchidos.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c26|C26]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-026


> [!example]- CT-027 · Seletor de PJ lista somente cadastro completo
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
> **Descrição:** confirma que o seletor de Pessoa Jurídica só lista PJs com cadastro completo.
>
> **Pré-condições:**  
> - Existem PJs com cadastro completo e incompleto no sistema.
>
> **Dado** que o servidor abra o seletor de Pessoa Jurídica  
> **Quando** as opções forem carregadas  
> **Então** o sistema lista somente pessoas jurídicas com cadastro completo
>
> **Resultado esperado:** PJ com cadastro incompleto não aparece na lista.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c27|C27]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-027


> [!example]- CT-028 · Identificação da PJ com Nome fantasia no seletor
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
> **Descrição:** confirma a apresentação da PJ no seletor quando ela possui Nome fantasia.
>
> **Pré-condições:**  
> - PJ com Nome fantasia cadastrado, disponível no seletor.
>
> **Dado** que uma pessoa jurídica seja exibida no seletor  
> **Quando** houver Nome fantasia cadastrado  
> **Então** a opção apresenta o Nome fantasia e o CNPJ
>
> **Resultado esperado:** opção exibida como "Nome fantasia — CNPJ" (ou equivalente do Figma).
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c28|C28]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-028


> [!example]- CT-029 · Identificação da PJ sem Nome fantasia no seletor
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
> **Descrição:** confirma a apresentação da PJ no seletor quando ela não possui Nome fantasia.
>
> **Pré-condições:**  
> - PJ sem Nome fantasia cadastrado, disponível no seletor.
>
> **Dado** que uma pessoa jurídica não possua Nome fantasia  
> **Quando** ela for exibida no seletor  
> **Então** a opção apresenta a Razão Social e o CNPJ
>
> **Resultado esperado:** opção exibida como "Razão Social — CNPJ" (ou equivalente do Figma).
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c29|C29]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** aprovado — comportamento sempre esteve correto (fallback Razão Social + CNPJ funciona); o achado da validação real era [[03 - Casos de teste#^ct-027|CT-027]] (cadastro incompleto), não este CT. Defeito [[Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]] descartado em 01/10/2026

^ct-029


> [!example]- CT-030 · Bloqueio de departamento com nome duplicado
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
> **Descrição:** confirma o bloqueio de criação de departamento com nome já existente na mesma pessoa jurídica.
>
> **Pré-condições:**  
> - Pessoa jurídica selecionada já possui um departamento com determinado nome.
>
> **Dado** que a pessoa jurídica selecionada já possua um departamento com o mesmo nome informado  
> **Quando** o servidor tentar concluir o cadastro  
> **Então** o sistema impede a criação e informa a duplicidade
>
> **Resultado esperado:** criação bloqueada; mensagem específica de nome duplicado.
>
> **Pós-condição:** nenhum departamento criado.
>
> **Critérios cobertos:** [[01 - Demanda#^c30|C30]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-030


> [!example]- CT-031 · Bloqueio de departamento com e-mail duplicado
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
> **Descrição:** confirma o bloqueio de criação de departamento com e-mail já existente na mesma pessoa jurídica.
>
> **Pré-condições:**  
> - Pessoa jurídica selecionada já possui um departamento com determinado e-mail.
>
> **Dado** que a pessoa jurídica selecionada já possua um departamento com o mesmo e-mail informado  
> **Quando** o servidor tentar concluir o cadastro  
> **Então** o sistema impede a criação e informa a duplicidade
>
> **Resultado esperado:** criação bloqueada; mensagem específica de e-mail duplicado.
>
> **Pós-condição:** nenhum departamento criado.
>
> **Critérios cobertos:** [[01 - Demanda#^c31|C31]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-031


> [!example]- CT-032 · Notificação de criação do departamento
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
> **Descrição:** confirma o envio da notificação já usada no fluxo atual de cadastro de departamento.
>
> **Pré-condições:**  
> - Departamento criado com sucesso pelo cadastro rápido.
>
> **Dado** que o departamento seja criado com sucesso  
> **Quando** o cadastro for concluído  
> **Então** o sistema envia ao e-mail do departamento a mesma notificação utilizada no fluxo atual de cadastro de departamento
>
> **Resultado esperado:** notificação recebida, com o mesmo conteúdo do fluxo dedicado (fora do escopo desta demanda).
>
> **Pós-condição:** notificação enviada.
>
> **Critérios cobertos:** [[01 - Demanda#^c32|C32]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-032


> [!example]- CT-033 · Bloqueio de confirmação com dados inválidos, pendentes ou ausentes
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
> **Descrição:** confirma o bloqueio transversal de confirmação quando há campo inválido, consulta pendente ou dado obrigatório ausente, em qualquer um dos 3 tipos.
>
> **Pré-condições:**  
> - Formulário de cadastro rápido (qualquer tipo) com campo inválido, consulta ainda em andamento, ou campo obrigatório vazio.
>
> **Dado** que existam campos inválidos, consultas pendentes ou dados obrigatórios ausentes  
> **Quando** o servidor tentar confirmar o cadastro  
> **Então** o sistema impede a criação e destaca os campos que precisam de correção
>
> **Resultado esperado:** confirmação bloqueada; campos problemáticos destacados visualmente.
>
> **Pós-condição:** nenhum cadastro criado.
>
> **Critérios cobertos:** [[01 - Demanda#^c33|C33]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-033


> [!example]- CT-034 · Bloqueio de cadastro duplicado por CPF ou CNPJ
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
> **Descrição:** confirma o bloqueio transversal de duplicidade de CPF (Pessoa Física) ou CNPJ (Pessoa Jurídica) já existente no sistema.
>
> **Pré-condições:**  
> - Já existe cidadão cadastrado com o CPF ou CNPJ que será informado.
>
> **Dado** que já exista um cidadão com o CPF ou CNPJ informado  
> **Quando** o servidor tentar realizar um novo cadastro  
> **Então** o sistema impede a duplicidade e informa que o registro já existe
>
> **Resultado esperado:** cadastro bloqueado; mensagem informando registro existente (vale para PF e PJ).
>
> **Pós-condição:** nenhum cadastro duplicado criado.
>
> **Critérios cobertos:** [[01 - Demanda#^c34|C34]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-034


> [!example]- CT-035 · Falha de comunicação preserva dados preenchidos
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
> **Descrição:** confirma que uma falha de comunicação com a API ou no processamento não descarta os dados já preenchidos.
>
> **Pré-condições:**  
> - Formulário de cadastro rápido (qualquer tipo) preenchido, falha simulada na API/processamento.
>
> **Dado** que ocorra uma falha de comunicação com a API ou no processamento do cadastro  
> **Quando** não for possível concluir a operação  
> **Então** o sistema preserva os dados preenchidos e apresenta uma mensagem de erro adequada
>
> **Resultado esperado:** dados permanecem no formulário após o erro, sem exigir redigitação.
>
> **Pós-condição:** nenhum cadastro criado; dados preservados no formulário.
>
> **Critérios cobertos:** [[01 - Demanda#^c35|C35]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-035


> [!example]- CT-036 · Confirmação e encerramento do formulário ao concluir
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
> **Descrição:** confirma que o sistema apresenta confirmação e encerra o formulário ao concluir o cadastro com sucesso.
>
> **Pré-condições:**  
> - Cadastro rápido (qualquer tipo) concluído com sucesso.
>
> **Dado** que o registro seja criado com sucesso  
> **Quando** a operação for finalizada  
> **Então** o sistema apresenta uma confirmação e encerra o formulário de cadastro rápido
>
> **Resultado esperado:** mensagem de sucesso exibida; formulário fechado automaticamente.
>
> **Pós-condição:** formulário de cadastro rápido fechado; registro disponível no campo de origem (ver CT-004).
>
> **Critérios cobertos:** [[01 - Demanda#^c36|C36]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-036

> [!example]- CT-037 · Placeholder do campo CNPJ
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
> **Descrição:** confirma que o campo CNPJ exibe o placeholder no padrão correto.
>
> **Pré-condições:**  
> - Opção Pessoa Jurídica selecionada.
>
> **Dado** que a opção Pessoa Jurídica esteja selecionada  
> **Quando** o campo CNPJ for exibido vazio  
> **Então** o placeholder exibido é `XX.XXX.XXX/XXXX-XX`
>
> **Resultado esperado:** placeholder no padrão `XX.XXX.XXX/XXXX-XX`.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c37|C37]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** retestado e aprovado — [[Defeitos/SGV-11951 - Defeito Placeholder Campo CNPJ Incorreto|SGV-11951]]

^ct-037
