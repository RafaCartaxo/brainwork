---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-11177

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle dos casos de teste  
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis. CT-001 a CT-010 cobrem a tramitação para membro de departamento; CT-011 a CT-016 a assinatura para departamento; CT-017 a CT-022 a assinatura para membro; CT-023 a CT-031 o fluxo externo por CPF.

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

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- CT-001 · Busca de cidadão PJ retorna departamentos e membros
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
> **Descrição:** confirma que a busca em campo de cidadão PJ passa a retornar também membros de departamento.
>
> **Pré-condições:**  
> - Existe ao menos um departamento com membros cujo nome/documento casa com o termo de busca.
>
> **Dado** que um campo permita pesquisar cidadãos PJ  
> **Quando** o usuário realizar uma busca  
> **Então** o sistema lista, além dos departamentos correspondentes, os cidadãos membros desses departamentos que correspondam à busca
>
> **Resultado esperado:** resultado combinado de departamentos e membros, sem omitir nenhum dos dois tipos.
>
> **Pós-condição:** nenhuma alteração de estado — apenas exibição do resultado.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
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

> [!example]- CT-002 · Resultado da busca distingue departamento de membro
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
> **Descrição:** confirma a diferenciação visual entre um resultado de departamento e um resultado de membro.
>
> **Pré-condições:**  
> - Busca retornando ao menos um departamento e um membro (CT-001).
>
> **Dado** que a busca retorne departamentos e seus membros  
> **Quando** os resultados forem exibidos  
> **Então** o sistema permite distinguir visualmente um departamento de um membro, conforme o padrão definido no Figma
>
> **Resultado esperado:** usuário identifica sem ambiguidade qual resultado é departamento e qual é membro.
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
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Selecionar um membro adiciona à tramitação vinculado ao departamento
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
> **Descrição:** confirma que selecionar um membro no resultado da busca o vincula corretamente ao departamento na tramitação.
>
> **Pré-condições:**  
> - Um membro de departamento é exibido no resultado da busca (CT-001).
>
> **Dado** que um membro de departamento seja exibido no resultado da busca  
> **Quando** o usuário selecioná-lo  
> **Então** o sistema o adiciona à tramitação vinculado ao respectivo departamento
>
> **Resultado esperado:** membro presente na tramitação com o vínculo ao departamento visível.
>
> **Pós-condição:** tramitação com o membro adicionado, pronta para ser efetivada.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Membro adicionado à tramitação é notificado
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
> **Descrição:** confirma a notificação do membro (e-mail + interna) ao efetivar a tramitação.
>
> **Pré-condições:**  
> - Membro adicionado a uma tramitação (CT-003), ainda não efetivada.
>
> **Dado** que um membro de departamento seja adicionado a uma tramitação  
> **Quando** a tramitação for efetivada  
> **Então** o sistema notifica o membro por e-mail e por notificação interna
>
> **Resultado esperado:** as duas notificações (e-mail e interna) chegam ao membro.
>
> **Pós-condição:** tramitação efetivada; notificações registradas para o membro.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · E-mail do departamento continua recebendo a notificação
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
> **Descrição:** confirma que o e-mail do departamento não é substituído pelo do membro na notificação.
>
> **Pré-condições:**  
> - Tramitação efetivada com um membro de departamento adicionado (CT-004).
>
> **Dado** que um membro de departamento seja adicionado a uma tramitação  
> **Quando** as notificações forem enviadas  
> **Então** o e-mail do departamento também continua recebendo a notificação
>
> **Resultado esperado:** os dois destinos (membro e e-mail do departamento) recebem a notificação, sem substituição de um pelo outro.
>
> **Pós-condição:** notificação registrada também para o e-mail do departamento.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Conteúdo das notificações segue o padrão do Figma
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
> **Descrição:** confirma que o texto e a apresentação das notificações de tramitação para membro seguem o Figma.
>
> **Pré-condições:**  
> - Notificações geradas por uma tramitação destinada a um membro de departamento (CT-004/CT-005).
>
> **Dado** que a tramitação seja destinada a um membro de departamento  
> **Quando** as notificações forem geradas  
> **Então** seu conteúdo e sua apresentação seguem o padrão definido no Figma
>
> **Resultado esperado:** texto e layout da notificação conferem com a especificação — ver Pendências de decisão em `01 - Demanda` (ponto ainda sujeito a conferência fina no Figma).
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

> [!example]- CT-007 · Padrão de exibição do membro na tramitação
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
> **Descrição:** confirma a string de identificação do membro na tramitação.
>
> **Pré-condições:**  
> - Membro de departamento adicionado à tramitação (CT-003).
>
> **Dado** que um membro de departamento tenha sido adicionado à tramitação  
> **Quando** sua identificação for exibida  
> **Então** o sistema utiliza o padrão `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`
>
> **Resultado esperado:** string exibida exatamente no formato especificado, com os quatro dados corretos.
>
> **Pós-condição:** nenhuma.
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

> [!example]- CT-008 · Consistência da exibição entre componentes da tramitação
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
> **Descrição:** confirma que o padrão de exibição do membro (CT-007) se repete em todos os componentes previstos.
>
> **Pré-condições:**  
> - Membro de departamento aparece em mais de um componente da tramitação (ex.: lista de destinatários e detalhe da tramitação).
>
> **Dado** que o membro apareça em diferentes componentes da tramitação  
> **Quando** sua identificação for renderizada  
> **Então** o padrão é aplicado de forma consistente nos locais previstos no Figma
>
> **Resultado esperado:** nenhuma variação de formato entre os componentes.
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

> [!example]- CT-009 · Identificação do membro no PDF
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
> **Descrição:** confirma que o PDF gerado a partir da tramitação também aplica o padrão de identificação do membro.
>
> **Pré-condições:**  
> - Membro de departamento selecionado em uma tramitação (CT-003).
>
> **Dado** que um membro de departamento tenha sido selecionado em uma tramitação  
> **Quando** o PDF correspondente for gerado  
> **Então** sua identificação segue o padrão `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`
>
> **Resultado esperado:** string idêntica à exibida em tela (CT-007), agora no PDF.
>
> **Pós-condição:** PDF gerado disponível para conferência.
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI (PDF)  
> **Automação:** manual  
> **Execução:** planejado

^ct-009

> [!example]- CT-010 · Campo do tipo pessoa no PDF segue o mesmo padrão
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
> **Descrição:** confirma que qualquer campo do tipo pessoa preenchido com um membro de departamento também segue o padrão no PDF.
>
> **Pré-condições:**  
> - Documento com um campo do tipo pessoa preenchido com um membro de departamento.
>
> **Dado** que um campo do tipo pessoa esteja preenchido com um membro de departamento  
> **Quando** um PDF que contenha esse campo for gerado  
> **Então** o mesmo padrão de identificação é aplicado
>
> **Resultado esperado:** consistência entre o CT-009 (PDF da tramitação) e qualquer outro PDF que exiba o campo do tipo pessoa.
>
> **Pós-condição:** PDF gerado disponível para conferência.
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI (PDF)  
> **Automação:** manual  
> **Execução:** planejado

^ct-010

> [!example]- CT-011 · Selecionar departamento na assinatura o adiciona como signatário
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
> **Descrição:** confirma a adição de um departamento inteiro como signatário de uma solicitação de assinatura.
>
> **Pré-condições:**  
> - Usuário está configurando uma solicitação de assinatura.
>
> **Dado** que o usuário esteja configurando uma solicitação de assinatura  
> **Quando** pesquisar e selecionar um departamento  
> **Então** o departamento é adicionado como signatário
>
> **Resultado esperado:** departamento presente na lista de signatários da solicitação.
>
> **Pós-condição:** solicitação com o departamento como signatário, pronta para ser enviada.
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

> [!example]- CT-012 · Qualquer membro apto do departamento consegue assinar
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
> **Descrição:** confirma que a assinatura solicitada ao departamento fica disponível para qualquer membro apto.
>
> **Pré-condições:**  
> - Assinatura solicitada a um departamento com mais de um membro apto (CT-011).
>
> **Dado** que a assinatura tenha sido solicitada a um departamento  
> **Quando** um membro desse departamento acessar a solicitação  
> **Então** ele está apto a realizar a assinatura
>
> **Resultado esperado:** qualquer membro apto do departamento consegue assinar, não só um específico.
>
> **Pós-condição:** documento assinado pelo membro que acessou primeiro; solicitação encerrada para os demais.
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-012

> [!example]- CT-013 · Token bloqueado quando o signatário é um departamento
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
> **Descrição:** confirma que a validação por token não pode ser configurada quando o signatário é o departamento inteiro.
>
> **Pré-condições:**  
> - Departamento selecionado como signatário (CT-011).
>
> **Dado** que o signatário selecionado seja um departamento  
> **Quando** o solicitante configurar a assinatura  
> **Então** o sistema não permite a solicitação de assinatura via token
>
> **Resultado esperado:** opção de token indisponível ou bloqueada na configuração para esse signatário.
>
> **Pós-condição:** solicitação configurada sem token para o departamento.
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

> [!example]- CT-014 · Header do componente signatário para departamento
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
> **Descrição:** confirma o header do componente de signatário quando o alvo é o departamento inteiro.
>
> **Pré-condições:**  
> - Departamento adicionado como signatário (CT-011).
>
> **Dado** que um departamento tenha sido adicionado como signatário  
> **Quando** o componente signatário for exibido  
> **Então** seu header segue o padrão definido no Figma
>
> **Resultado esperado:** header visualmente diferente do de um signatário individual comum — ver Pendências de decisão (ponto sujeito a conferência fina no Figma).
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
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-014

> [!example]- CT-015 · Eventos de assinatura identificam o departamento
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
> **Descrição:** confirma a identificação do departamento no componente de eventos de assinatura.
>
> **Pré-condições:**  
> - Ao menos um evento de assinatura já ocorreu numa solicitação com departamento como signatário (ex.: envio, visualização).
>
> **Dado** que ocorram eventos relacionados à assinatura solicitada a um departamento  
> **Quando** esses eventos forem exibidos  
> **Então** o componente de eventos identifica corretamente o departamento conforme o Figma
>
> **Resultado esperado:** eventos mostram o departamento como o alvo, não um membro específico.
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
> **Execução:** planejado

^ct-015

> [!example]- CT-016 · Notificação do departamento ao solicitar assinatura
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
> **Descrição:** confirma o envio da notificação ao e-mail do departamento na criação da solicitação de assinatura.
>
> **Pré-condições:**  
> - Departamento selecionado como signatário (CT-011).
>
> **Dado** que uma assinatura seja solicitada a um departamento  
> **Quando** a solicitação for criada  
> **Então** o sistema envia a notificação ao e-mail do departamento
>
> **Resultado esperado:** e-mail do departamento recebe a notificação de nova solicitação.
>
> **Pós-condição:** notificação registrada para o e-mail do departamento.
>
> **Critérios cobertos:** [[01 - Demanda#^c16|C16]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-016

> [!example]- CT-017 · Selecionar membro na assinatura o adiciona vinculado ao departamento
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
> **Descrição:** confirma a adição de um membro específico como signatário, vinculado ao seu departamento.
>
> **Pré-condições:**  
> - Usuário está configurando uma solicitação de assinatura.
>
> **Dado** que o usuário esteja configurando uma solicitação de assinatura  
> **Quando** pesquisar e selecionar um membro de departamento  
> **Então** o membro é adicionado como signatário, vinculado ao respectivo departamento
>
> **Resultado esperado:** membro presente na lista de signatários, com o departamento visível no vínculo.
>
> **Pós-condição:** solicitação com o membro como signatário, pronta para ser enviada.
>
> **Critérios cobertos:** [[01 - Demanda#^c17|C17]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-017

> [!example]- CT-018 · Token liberado quando o signatário é um membro de departamento
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
> **Descrição:** confirma que a validação por token continua disponível quando o signatário é um membro específico (contraste direto com CT-013).
>
> **Pré-condições:**  
> - Membro de departamento selecionado como signatário (CT-017).
>
> **Dado** que o signatário selecionado seja um membro de departamento  
> **Quando** o solicitante configurar a assinatura  
> **Então** o sistema permite a solicitação de assinatura via token
>
> **Resultado esperado:** opção de token disponível e configurável para esse signatário.
>
> **Pós-condição:** solicitação configurada com token para o membro, se o solicitante optar por isso.
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

> [!example]- CT-019 · Header do componente signatário identifica membro e departamento
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
> **Descrição:** confirma o header do componente de signatário quando o alvo é um membro específico.
>
> **Pré-condições:**  
> - Membro de departamento adicionado como signatário (CT-017).
>
> **Dado** que um membro de departamento tenha sido adicionado como signatário  
> **Quando** o componente signatário for exibido  
> **Então** seu header identifica corretamente o membro e o departamento conforme o Figma
>
> **Resultado esperado:** header mostra tanto o membro quanto o departamento — ver Pendências de decisão (ponto sujeito a conferência fina no Figma).
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

> [!example]- CT-020 · Eventos de assinatura identificam membro e departamento
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
> **Descrição:** confirma a identificação do membro e do departamento no componente de eventos de assinatura.
>
> **Pré-condições:**  
> - Ao menos um evento de assinatura já ocorreu numa solicitação com membro como signatário.
>
> **Dado** que ocorram eventos relacionados à assinatura solicitada a um membro  
> **Quando** esses eventos forem exibidos  
> **Então** o componente de eventos identifica corretamente o membro e o departamento conforme o Figma
>
> **Resultado esperado:** eventos mostram tanto o membro quanto o departamento ao qual pertence.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c20|C20]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-020

> [!example]- CT-021 · Notificação do membro signatário
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
> **Descrição:** confirma a notificação do membro (e-mail + interna) ao ser adicionado como signatário.
>
> **Pré-condições:**  
> - Membro de departamento selecionado como signatário (CT-017).
>
> **Dado** que uma assinatura seja solicitada a um membro de departamento  
> **Quando** a solicitação for criada  
> **Então** o sistema notifica o membro por e-mail e por notificação interna
>
> **Resultado esperado:** as duas notificações (e-mail e interna) chegam ao membro.
>
> **Pós-condição:** notificações registradas para o membro.
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

> [!example]- CT-022 · E-mail do departamento continua recebendo notificação de assinatura
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
> **Descrição:** confirma que o e-mail do departamento não é substituído pelo do membro na notificação de assinatura.
>
> **Pré-condições:**  
> - Solicitação de assinatura criada com um membro como signatário (CT-021).
>
> **Dado** que uma assinatura seja solicitada a um membro de departamento  
> **Quando** as notificações forem enviadas  
> **Então** o e-mail do departamento também continua recebendo a notificação
>
> **Resultado esperado:** os dois destinos (membro e e-mail do departamento) recebem a notificação.
>
> **Pós-condição:** notificação registrada também para o e-mail do departamento.
>
> **Critérios cobertos:** [[01 - Demanda#^c22|C22]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** manual  
> **Execução:** planejado

^ct-022

> [!example]- CT-023 · Identificação externa solicita e verifica o CPF
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
> **Descrição:** confirma o primeiro passo do fluxo externo de assinatura — identificação por CPF.
>
> **Pré-condições:**  
> - Pessoa acessa externamente uma solicitação de assinatura destinada a um departamento ou membro.
>
> **Dado** que uma pessoa acesse externamente o fluxo de assinatura  
> **Quando** iniciar sua identificação  
> **Então** o sistema solicita o CPF e verifica se existe cadastro correspondente
>
> **Resultado esperado:** sistema direciona para um dos três sub-fluxos (CT-024, CT-025 ou CT-026) conforme o resultado da verificação.
>
> **Pós-condição:** nenhuma alteração de estado — apenas verificação.
>
> **Critérios cobertos:** [[01 - Demanda#^c23|C23]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-023

> [!example]- CT-024 · Pessoa cadastrada e vinculada assina com senha
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
> **Descrição:** confirma o caminho mais direto do fluxo externo — pessoa já cadastrada e já vinculada ao departamento.
>
> **Pré-condições:**  
> - CPF informado (CT-023) pertence a uma pessoa cadastrada e já vinculada ao departamento destinatário.
>
> **Dado** que o CPF pertença a uma pessoa cadastrada e já vinculada ao departamento destinatário  
> **Quando** a identificação for concluída  
> **Então** a pessoa informa sua senha e pode realizar a assinatura
>
> **Resultado esperado:** assinatura concluída sem etapa adicional de vínculo ou cadastro.
>
> **Pós-condição:** documento assinado; nenhum vínculo novo criado (já existia).
>
> **Critérios cobertos:** [[01 - Demanda#^c24|C24]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-024

> [!example]- CT-025 · Pessoa cadastrada sem vínculo informa cargo, vincula e assina
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
> **Descrição:** confirma o caminho intermediário — pessoa já tem cadastro no SOGOV, mas ainda não é membro do departamento destinatário.
>
> **Pré-condições:**  
> - CPF informado (CT-023) pertence a uma pessoa cadastrada, mas sem vínculo com o departamento destinatário.
>
> **Dado** que o CPF pertença a uma pessoa cadastrada, mas ainda não vinculada ao departamento destinatário  
> **Quando** prosseguir com a assinatura  
> **Então** a pessoa informa seu cargo, é vinculada ao departamento e pode realizar a assinatura
>
> **Resultado esperado:** vínculo criado com o cargo informado, seguido da assinatura no mesmo fluxo.
>
> **Pós-condição:** pessoa passa a constar como participante do departamento; documento assinado.
>
> **Critérios cobertos:** [[01 - Demanda#^c25|C25]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-025

> [!example]- CT-026 · Pessoa sem cadastro é levada ao pré-cadastro
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
> **Descrição:** confirma o caminho mais longo — CPF sem nenhum cadastro correspondente no SOGOV.
>
> **Pré-condições:**  
> - CPF informado (CT-023) não corresponde a nenhum cadastro existente.
>
> **Dado** que não exista cadastro para o CPF informado  
> **Quando** a pessoa prosseguir com a assinatura  
> **Então** o sistema solicita CPF, e-mail e cargo para realizar o pré-cadastro
>
> **Resultado esperado:** formulário de pré-cadastro exibido com os três campos, sem pular nenhum.
>
> **Pós-condição:** nenhum cadastro criado ainda — dados apenas coletados.
>
> **Critérios cobertos:** [[01 - Demanda#^c26|C26]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-026

> [!example]- CT-027 · Termos e declaração de maioridade no pré-cadastro
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
> **Descrição:** confirma a exigência de aceite dos termos e declaração de maioridade antes de concluir o pré-cadastro.
>
> **Pré-condições:**  
> - Pessoa preenchendo o pré-cadastro (CT-026).
>
> **Dado** que a pessoa esteja realizando o pré-cadastro  
> **Quando** confirmar seus dados  
> **Então** deve aceitar os termos aplicáveis e declarar ser maior de idade no modal definido no Figma
>
> **Resultado esperado:** confirmação bloqueada até o aceite dos termos e a declaração de maioridade — ver Pendências de decisão (modal sujeito a conferência fina no Figma).
>
> **Pós-condição:** nenhum cadastro criado ainda — consentimentos coletados.
>
> **Critérios cobertos:** [[01 - Demanda#^c27|C27]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI  
> **Automação:** manual  
> **Execução:** planejado

^ct-027

> [!example]- CT-028 · Criação do pré-cadastro e vínculo com o departamento
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
> **Descrição:** confirma a criação efetiva do pré-cadastro e do vínculo, uma vez que todos os dados e consentimentos estão completos.
>
> **Pré-condições:**  
> - Dados válidos informados e consentimentos aceitos no pré-cadastro (CT-026, CT-027).
>
> **Dado** que a pessoa sem cadastro informe dados válidos e forneça os consentimentos obrigatórios  
> **Quando** confirmar o pré-cadastro  
> **Então** o sistema cria o pré-cadastro e a vincula ao departamento com o cargo informado
>
> **Resultado esperado:** pré-cadastro criado e pessoa já constando como participante do departamento com o cargo informado.
>
> **Pós-condição:** pessoa vinculada ao departamento, pronta para assinar.
>
> **Critérios cobertos:** [[01 - Demanda#^c28|C28]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-028

> [!example]- CT-029 · Assinatura no mesmo fluxo após o pré-cadastro
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
> **Descrição:** confirma que a pessoa não precisa reiniciar o fluxo para assinar depois de concluir o pré-cadastro.
>
> **Pré-condições:**  
> - Pré-cadastro e vínculo com o departamento concluídos (CT-028).
>
> **Dado** que o pré-cadastro tenha sido concluído com sucesso  
> **Quando** o vínculo com o departamento for criado  
> **Então** a pessoa pode realizar a assinatura no mesmo fluxo
>
> **Resultado esperado:** assinatura concluída na mesma sessão, sem exigir novo login ou nova navegação.
>
> **Pós-condição:** documento assinado; pessoa já constando como participante do departamento.
>
> **Critérios cobertos:** [[01 - Demanda#^c29|C29]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-029

> [!example]- CT-030 · Convite por e-mail para completar o cadastro
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
> **Descrição:** confirma o e-mail enviado após uma assinatura concluída via pré-cadastro.
>
> **Pré-condições:**  
> - Pessoa assinou o documento por meio de um pré-cadastro (CT-029).
>
> **Dado** que a pessoa tenha assinado por meio de um pré-cadastro  
> **Quando** a assinatura for concluída  
> **Então** o sistema envia um e-mail com instruções para completar o cadastro no SOGOV
>
> **Resultado esperado:** e-mail recebido com instruções claras de como finalizar o cadastro (ex.: definir senha).
>
> **Pós-condição:** convite de finalização de cadastro registrado/enviado.
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

> [!example]- CT-031 · Inconsistência no fluxo externo não cria vínculo ou cadastro duplicado
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
> **Descrição:** confirma o tratamento de erro em qualquer ponto do fluxo externo (identificação, autenticação, vinculação ou pré-cadastro), sem deixar rastro duplicado.
>
> **Pré-condições:**  
> - Uma inconsistência é provocada deliberadamente em cada uma das quatro etapas (ex.: senha errada, cargo inválido, e-mail já usado em outro pré-cadastro, sessão expirada no meio do fluxo).
>
> **Dado** que ocorra uma inconsistência na identificação, autenticação, vinculação ou criação do pré-cadastro  
> **Quando** não for possível prosseguir  
> **Então** o sistema impede a assinatura e apresenta uma mensagem de erro adequada, sem criar vínculos ou cadastros duplicados
>
> **Resultado esperado:** mensagem de erro específica para cada etapa, sem nenhum vínculo ou cadastro parcial deixado no sistema.
>
> **Pós-condição:** nenhum vínculo, cadastro ou assinatura criado a partir da tentativa malsucedida.
>
> **Critérios cobertos:** [[01 - Demanda#^c31|C31]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional (negativo)  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-031
