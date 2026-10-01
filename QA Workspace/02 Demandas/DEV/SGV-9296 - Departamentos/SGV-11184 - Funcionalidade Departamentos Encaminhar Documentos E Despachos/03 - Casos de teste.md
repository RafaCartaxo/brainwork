---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: execucao
pontos: ""
---

# Casos de teste — SGV-11184

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
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
| [[01 - Demanda#^c2a\|C2a]] | [[03 - Casos de teste#^ct-002a\|CT-002a]] |
| [[01 - Demanda#^c2b\|C2b]] | [[03 - Casos de teste#^ct-002b\|CT-002b]] |
| [[01 - Demanda#^c2c\|C2c]] | [[03 - Casos de teste#^ct-002c\|CT-002c]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c8a\|C8a]] | [[03 - Casos de teste#^ct-008a\|CT-008a]] |
| [[01 - Demanda#^c9\|C9]] | [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c10\|C10]] | [[03 - Casos de teste#^ct-010\|CT-010]] |
| [[01 - Demanda#^c11\|C11]] | [[03 - Casos de teste#^ct-011\|CT-011]] |
| [[01 - Demanda#^c12\|C12]] | [[03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c12a\|C12a]] | [[03 - Casos de teste#^ct-012a\|CT-012a]] |
| [[01 - Demanda#^c12b\|C12b]] | [[03 - Casos de teste#^ct-012b\|CT-012b]] |
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

---

### A. Selecionar departamento em campo pessoa de documento

> [!example]- CT-001 · Departamento só aparece com Pessoa Jurídica habilitada no campo
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
> **Descrição:** confirma que departamentos só aparecem como destinatário quando o campo pessoa aceita Pessoa Jurídica.
>
> **Pré-condições:**
> - Um campo pessoa está configurado pra aceitar Pessoa Jurídica.
>
> **Dado** que um campo pessoa está configurado pra aceitar Pessoa Jurídica
> **Quando** o servidor pesquisa um destinatário
> **Então** a busca inclui departamentos ativos vinculados a cidadãos PJ; com a configuração desabilitada, nenhum departamento é exibido ou aceito
>
> **Resultado esperado:** departamento só disponível com a configuração habilitada.
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
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** aprovado

^ct-001


> [!example]- CT-002 · Busca de departamentos por nome ou razão social, só da mesma instância
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
> **Descrição:** confirma a busca progressiva de departamentos por nome/razão social, limitada à mesma instância.
>
> **Pré-condições:**
> - A busca de departamentos está habilitada no campo.
>
> **Dado** que a busca de departamentos está habilitada no campo
> **Quando** o servidor informa parte do nome do departamento ou a razão social da PJ, a partir de 3 caracteres digitados
> **Então** o sistema retorna os departamentos correspondentes do mesmo cliente/instância, afunilando o resultado a cada caractere digitado, exibindo nome do departamento e razão social da PJ em cada resultado; com menos de 3 caracteres, nenhum resultado é retornado
>
> **Resultado esperado:** busca progressiva, só da mesma instância.
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
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** aprovado

^ct-002


> [!example]- CT-002a · Resultado do match já vem expandido, com cluster aninhado sob a PJ
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
> **Descrição:** confirma a exibição expandida do departamento no resultado da busca, com participantes lotados.
>
> **Pré-condições:**
> - A busca deu match com um departamento.
>
> **Dado** que a busca deu match com um departamento
> **Quando** o resultado é exibido
> **Então** o departamento já aparece expandido, mostrando os participantes lotados nele, e o cluster do departamento aparece aninhado visualmente sob a pessoa jurídica à qual pertence
>
> **Resultado esperado:** resultado expandido com participantes.
>
> **Pós-condição:** nenhuma.
>
> > [!info] Não se aplica — nível "participantes" não implementado nesta entrega
> > Confirmado por Rafael (03/09/2026): a entrega cobre só o departamento em si; exibir participantes lotados depende de um nível ("Cidadão > PJ > Departamento > participantes") que não existe nesta entrega.
>
> **Critérios cobertos:** [[01 - Demanda#^c2a|C2a]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** não se aplica — fora de escopo desta entrega (03/09/2026)

^ct-002a


> [!example]- CT-002b · CPF de pessoa física lotada no departamento é anonimizado
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
> **Descrição:** confirma a anonimização do CPF de participante exibido no resultado expandido.
>
> **Pré-condições:**
> - Um departamento com participantes pessoa física é exibido no resultado expandido da busca.
>
> **Dado** que um departamento com participantes pessoa física é exibido no resultado expandido da busca
> **Quando** o CPF do participante aparece na listagem
> **Então** o CPF é exibido de forma anonimizada, nunca completo
>
> **Resultado esperado:** CPF anonimizado.
>
> **Pós-condição:** nenhuma.
>
> > [!info] Não se aplica — mesmo motivo do CT-002a
> > Sem exibição de participantes nesta entrega, não há CPF de participante a anonimizar.
>
> **Critérios cobertos:** [[01 - Demanda#^c2b|C2b]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** não se aplica — fora de escopo desta entrega (03/09/2026)

^ct-002b


> [!example]- CT-002c · Área de clique do accordion vs. seleção do departamento
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
> **Descrição:** confirma que a área de clique do accordion (campo pessoa) distingue expandir/recolher de selecionar o departamento.
>
> **Pré-condições:**
> - O departamento é exibido como accordion no resultado da busca.
>
> **Dado** que o departamento é exibido como accordion no resultado da busca
> **Quando** o servidor clica no ícone de chevron
> **Então** o accordion expande ou recolhe, mostrando/ocultando os participantes
>
> **Quando** o servidor clica em qualquer outro ponto da linha do departamento (do início do nome ao fim do container)
> **Então** o departamento é selecionado como destinatário, com a mesma estética de hover de seleção já existente — a expansão do accordion não interfere na seleção, e vice-versa
>
> **Resultado esperado:** clique no chevron expande/recolhe; clique na linha seleciona.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c2c|C2c]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** retestado e aprovado — [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]]

^ct-002c


> [!example]- CT-003 · Vínculo é persistido e revalidado pela API
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
> **Descrição:** confirma a persistência do vínculo documento↔campo↔departamento, revalidado pela API.
>
> **Pré-condições:**
> - O servidor selecionou um departamento válido no campo pessoa.
>
> **Dado** que o servidor selecionou um departamento válido no campo pessoa
> **Quando** salva o documento
> **Então** o vínculo entre documento, campo pessoa e departamento é persistido, e a API revalida a configuração do campo, o status do departamento e a instância, independente da validação da interface
>
> **Resultado esperado:** vínculo persistido e revalidado pela API.
>
> **Pós-condição:** vínculo documento↔campo↔departamento persistido no banco, revalidado pela API.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-003


> [!example]- CT-004 · Multiplicidade do campo é respeitada e duplicidade é bloqueada
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
> **Descrição:** confirma que a multiplicidade do campo é respeitada e a repetição do mesmo departamento é bloqueada.
>
> **Pré-condições:**
> - Um campo pessoa de seleção única ou múltipla.
>
> **Dado** um campo pessoa de seleção única ou múltipla
> **Quando** o servidor seleciona departamentos
> **Então** o sistema respeita a multiplicidade configurada e impede repetir o mesmo departamento
>
> **Resultado esperado:** multiplicidade respeitada, duplicidade bloqueada.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** aprovado

^ct-004


> [!example]- CT-005 · Representação do departamento no PDF do documento
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
> **Descrição:** confirma o formato de exibição do departamento no PDF do documento.
>
> **Pré-condições:**
> - O documento tem um departamento num campo pessoa.
>
> **Dado** que o documento tem um departamento num campo pessoa
> **Quando** o PDF é gerado ou regenerado
> **Então** o valor aparece no formato "Nome do departamento (Razão social da PJ)", com parênteses (formato confirmado no Figma)
>
> **Resultado esperado:** formato "Nome (Razão Social)".
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
> **Execução:** aprovado

^ct-005


> [!example]- CT-006 · Departamento invalidado antes do salvamento bloqueia a operação
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
> **Descrição:** confirma o bloqueio total da operação quando o departamento é invalidado entre a seleção e o salvamento.
>
> **Pré-condições:**
> - Um departamento selecionado foi suspenso, excluído ou movido pra condição inválida antes da confirmação.
>
> **Dado** que um departamento selecionado foi suspenso, excluído ou movido pra condição inválida antes da confirmação
> **Quando** o documento é salvo
> **Então** a operação é recusada por inteiro, com aviso de que o departamento não está mais disponível, sem salvar parcialmente
>
> **Resultado esperado:** operação recusada por inteiro.
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
> **Camada:** API
> **Automação:** manual
> **Execução:** não se aplica — cenário de corrida não reproduzido nesta rodada

^ct-006


### B. Selecionar departamento como destinatário de despacho

> [!example]- CT-007 · Busca no campo de destinatário do despacho
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
> **Descrição:** confirma a busca progressiva de departamentos no campo de destinatário do despacho.
>
> **Pré-condições:**
> - Um servidor está criando ou editando um despacho.
>
> **Dado** que um servidor está criando ou editando um despacho
> **Quando** pesquisa no campo de destinatário informando ao menos 3 caracteres
> **Então** o sistema retorna departamentos ativos do mesmo cliente/instância, por nome ou razão social da PJ, afunilando o resultado a cada caractere digitado; com menos de 3 caracteres, nenhum resultado é retornado
>
> **Resultado esperado:** busca progressiva, só da mesma instância.
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
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** aprovado

^ct-007


> [!example]- CT-008 · Apresentação do resultado no componente
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
> **Descrição:** confirma a apresentação do resultado da busca de destinatário do despacho.
>
> **Pré-condições:**
> - Um departamento é retornado na busca de destinatário do despacho.
>
> **Dado** que um departamento é retornado na busca de destinatário do despacho
> **Quando** o resultado é exibido
> **Então** o componente mostra o nome do departamento e a razão social da PJ, com o cluster aninhado sob a PJ à qual pertence
>
> **Resultado esperado:** nome + razão social, cluster aninhado.
>
> **Pós-condição:** nenhuma.
>
> > [!info] CT reescrito (03/09/2026)
> > Redação original também cobria "já expandido com participantes lotados... CPF anonimizado" — removido por não se aplicar a esta entrega (nível "participantes" não implementado, mesma decisão do CT-002a/CT-002b). O que sobrou (nome + razão social) foi retestado do zero.
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
> **Execução:** aprovado

^ct-008


> [!example]- CT-008a · Área de clique do accordion vs. seleção do departamento no despacho
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
> **Descrição:** confirma que a área de clique do accordion (destinatário de despacho) distingue expandir/recolher de selecionar, mesma regra do CT-002c.
>
> **Pré-condições:**
> - O departamento é exibido como accordion no resultado da busca de destinatário do despacho.
>
> **Dado** que o departamento é exibido como accordion no resultado da busca de destinatário do despacho
> **Quando** o servidor clica no ícone de chevron
> **Então** o accordion expande ou recolhe os participantes
>
> **Quando** clica em qualquer outro ponto da linha do departamento
> **Então** o departamento é selecionado como destinatário, com a mesma estética de hover de seleção já existente
>
> **Resultado esperado:** clique no chevron expande/recolhe; clique na linha seleciona.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c8a|C8a]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** retestado e aprovado — [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]]

^ct-008a


> [!example]- CT-009 · Departamento é persistido como destinatário
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
> **Descrição:** confirma a persistência do departamento como destinatário do despacho.
>
> **Pré-condições:**
> - Um departamento válido está selecionado no despacho.
>
> **Dado** que um departamento válido está selecionado no despacho
> **Quando** o despacho é salvo ou enviado
> **Então** o departamento é persistido como destinatário
>
> **Resultado esperado:** departamento persistido.
>
> **Pós-condição:** departamento persistido como destinatário do despacho no banco.
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** aprovado

^ct-009


> [!example]- CT-010 · Membros do departamento não são selecionáveis individualmente
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
> **Descrição:** confirma que membros do departamento não são selecionáveis individualmente no destinatário de despacho.
>
> **Pré-condições:**
> - Um departamento com membros é selecionado no destinatário do despacho.
>
> **Dado** que um departamento com membros é selecionado no destinatário do despacho
> **Quando** o servidor abre a busca ou seleciona o departamento
> **Então** os membros não são expandidos, sugeridos nem adicionados como destinatários individuais
>
> **Resultado esperado:** membros não selecionáveis individualmente.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** não se aplica — fora de escopo desta entrega (mesmo motivo do CT-002a)

^ct-010


> [!example]- CT-011 · Representação do departamento no PDF do despacho
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
> **Descrição:** confirma o formato de exibição do departamento no PDF do despacho, mesmo formato do CT-005.
>
> **Pré-condições:**
> - Um despacho tem um departamento como destinatário.
>
> **Dado** que um despacho tem um departamento como destinatário
> **Quando** o PDF do documento/despacho é gerado
> **Então** o destinatário é representado no mesmo formato definido pro campo pessoa (CT-005)
>
> **Resultado esperado:** formato "Nome (Razão Social)".
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
> **Execução:** aprovado

^ct-011


> [!example]- CT-012 · Departamento invalidado após seleção bloqueia o envio
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
> **Descrição:** confirma o bloqueio total do envio do despacho quando o departamento se torna inválido após a seleção.
>
> **Pré-condições:**
> - O departamento selecionado no despacho se tornou inválido após a seleção.
>
> **Dado** que o departamento selecionado no despacho se tornou inválido após a seleção
> **Quando** o servidor envia o despacho
> **Então** o envio é bloqueado por inteiro e nenhuma notificação é disparada
>
> **Resultado esperado:** envio bloqueado por inteiro.
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
> **Camada:** API
> **Automação:** manual
> **Execução:** não se aplica — cenário de corrida não reproduzido nesta rodada

^ct-012


> [!example]- CT-012a · Truncamento da linha do evento com múltiplos destinatários
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
> **Descrição:** confirma o truncamento da linha do evento de emissão com destinatário de nome extenso.
>
> **Pré-condições:**
> - A linha do evento de emissão (remetente + destinatários) tem um ou mais departamentos entre os destinatários.
>
> **Dado** que a linha do evento de emissão (remetente + destinatários) tem um ou mais departamentos entre os destinatários
> **Quando** a linha se aproxima de ~16px da data de emissão
> **Então** o componente recebe status de truncate; em listas longas de destinatário (múltiplos departamentos ou usuários lotados), o texto sempre trunca na 2ª linha, mantendo a mesma sequência de string até o ponto de corte
>
> **Resultado esperado:** sempre trunca na 2ª linha.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c12a|C12a]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** reprovado — [[Defeitos/SGV-11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]]

^ct-012a


> [!example]- CT-012b · Retificação preserva o departamento selecionado como destinatário
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
> **Descrição:** confirma que a retificação de despacho preserva o departamento já selecionado como destinatário.
>
> **Pré-condições:**
> - Um despacho foi emitido com um departamento como destinatário.
>
> **Dado** que um despacho foi emitido com um departamento como destinatário
> **Quando** o servidor abre a tela de retificação desse despacho
> **Então** o departamento aparece selecionado no campo de destinatário, sem ser substituído pelo cidadão PJ/empresa
>
> **Resultado esperado:** departamento preservado na retificação.
>
> **Pós-condição:** nenhuma.
>
> **Critérios cobertos:** [[01 - Demanda#^c12b|C12b]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** aprovado — formalizado a partir do defeito [[Defeitos/SGV-11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]]

^ct-012b


### C. Notificações

> [!example]- CT-013 · E-mail enviado ao endereço do departamento
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
> **Descrição:** confirma o envio de notificação por e-mail ao endereço do departamento.
>
> **Pré-condições:**
> - Um documento ou despacho foi efetivamente encaminhado a um departamento.
>
> **Dado** que um documento ou despacho foi efetivamente encaminhado a um departamento
> **Quando** a operação é concluída
> **Então** uma notificação por e-mail é enviada ao endereço do departamento
>
> **Resultado esperado:** e-mail enviado.
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
> **Camada:** API
> **Automação:** manual
> **Execução:** aprovado

^ct-013


> [!example]- CT-014 · Deduplicação de e-mail por endereço normalizado
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
> **Descrição:** confirma que departamento e membro com o mesmo endereço recebem um único e-mail, não dois.
>
> **Pré-condições:**
> - O endereço do departamento é o mesmo de um cidadão já cadastrado como membro dele.
>
> **Dado** que o endereço do departamento é o mesmo de um cidadão já cadastrado como membro dele
> **Quando** os destinatários de e-mail são montados
> **Então** é enviado apenas um e-mail por endereço normalizado (sem diferenciar maiúsculas/minúsculas) — não dois, um pelo departamento e outro pelo membro; a notificação interna continua sendo criada uma vez por membro elegível
>
> **Resultado esperado:** um único e-mail por endereço normalizado.
>
> **Pós-condição:** nenhuma.
>
> > [!info] Cenário de dois membros com o mesmo e-mail removido (03/09/2026)
> > Confirmado pelo Rafael: cidadão tem e-mail único no sistema ([[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] — "e-mail institucional... único no sistema"), então dois membros nunca compartilham endereço. O único cenário real de sobreposição é **departamento × membro** (o departamento tem seu próprio campo de e-mail, sem essa mesma trava de unicidade contra os cidadãos).
>
> **Critérios cobertos:** [[01 - Demanda#^c14|C14]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** não se aplica — cenário não reproduzido nesta rodada

^ct-014


> [!example]- CT-015 · Reprocessar o mesmo encaminhamento não duplica a notificação
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
> **Descrição:** confirma que reprocessar o mesmo encaminhamento não duplica a notificação.
>
> **Pré-condições:**
> - Um encaminhamento ao departamento já foi processado e a notificação (e-mail e interna) já foi enviada.
>
> **Dado** que um encaminhamento ao departamento já foi processado e a notificação (e-mail e interna) já foi enviada
> **Quando** esse mesmo encaminhamento é processado de novo por retentativa do sistema (não uma nova ação do usuário)
> **Então** o e-mail e a notificação interna não são enviados de novo pra quem já recebeu
>
> **Resultado esperado:** sem duplicação.
>
> **Pós-condição:** nenhum e-mail/notificação duplicado persistido pra mesma combinação evento+canal+destinatário.
>
> **Critérios cobertos:** [[01 - Demanda#^c15|C15]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** aprovado

^ct-015


> [!example]- CT-016 · Conteúdo e link do e-mail
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
> **Descrição:** confirma o conteúdo e o link do e-mail de encaminhamento ao departamento.
>
> **Pré-condições:**
> - Um documento/despacho foi encaminhado a um departamento.
>
> **Dado** que um documento/despacho foi encaminhado a um departamento
> **Quando** o e-mail é enviado
> **Então** ele reutiliza o template do evento e inclui identificação do documento, indicação de encaminhamento ao departamento, nome do departamento + razão social da PJ, remetente/resumo já previstos, e URL externa com `departmentId={publicIdentifier}`
>
> **Resultado esperado:** template reutilizado, URL com `publicIdentifier`.
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
> **Camada:** API
> **Automação:** manual
> **Execução:** aprovado

^ct-016


### D. Registro de visualização externa (rastreabilidade)

> [!example]- CT-017 · Departamento sempre tem publicIdentifier
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
> **Descrição:** confirma que todo departamento tem `publicIdentifier` único e imutável.
>
> **Pré-condições:**
> - Um departamento novo ou existente.
>
> **Dado** um departamento novo ou existente
> **Quando** seus dados são persistidos ou migrados
> **Então** ele possui um `publicIdentifier` UUID v4, único, imutável e não nulo
>
> **Resultado esperado:** `publicIdentifier` sempre presente.
>
> **Pós-condição:** `publicIdentifier` gravado no registro do departamento.
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


> [!example]- CT-018 · URL externa carrega o publicIdentifier, nunca o ID interno
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
> **Descrição:** confirma que a URL externa carrega sempre o `publicIdentifier`, nunca o ID interno.
>
> **Pré-condições:**
> - Uma notificação por e-mail é enviada ao departamento.
>
> **Dado** que uma notificação por e-mail é enviada ao departamento
> **Quando** a URL externa é gerada
> **Então** ela contém `departmentId={publicIdentifier}` — o nome do parâmetro é mantido por compatibilidade, mas o valor é sempre o identificador público, nunca o ID numérico interno
>
> **Resultado esperado:** URL sempre com `publicIdentifier`.
>
> **Pós-condição:** nenhuma.
>
> > [!info] "ou seus membros" removido do Dado (03/09/2026)
> > A redação original citava "departamento ou seus membros" recebendo a notificação com URL externa — mas isso não está no requisito (RF04). O e-mail com URL externa vai só pro endereço do **departamento**; a notificação **interna** por membro elegível (CT-014 da SGV-11083) é um canal separado, sem essa URL de rastreamento externo associada.
>
> **Critérios cobertos:** [[01 - Demanda#^c18|C18]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-018


> [!example]- CT-019 · Validação completa do vínculo antes de qualquer registro
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
> **Descrição:** confirma a validação completa (formato, instância, vínculo, permissões) antes de registrar qualquer interação.
>
> **Pré-condições:**
> - A URL contém um `departmentId`.
>
> **Dado** que a URL contém um `departmentId`
> **Quando** o usuário abre o documento
> **Então** o backend valida o formato UUID, localiza o departamento por `publicIdentifier`, confirma que pertence à mesma instância do documento, confirma o vínculo real com o documento (campo pessoa ou destinatário de despacho) e aplica as permissões externas já existentes — só então registra a interação
>
> **Resultado esperado:** todas as validações antes do registro.
>
> **Pós-condição:** nenhum registro de interação até todas as validações passarem.
>
> **Critérios cobertos:** [[01 - Demanda#^c19|C19]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-019


> [!example]- CT-020 · Interação registrada só após carregamento válido do conteúdo
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
> **Descrição:** confirma que a `DocumentInteraction` só é criada após carregamento válido do conteúdo.
>
> **Pré-condições:**
> - Todas as validações foram aprovadas e o conteúdo principal do documento carregou com sucesso.
>
> **Dado** que todas as validações foram aprovadas e o conteúdo principal do documento carregou com sucesso
> **Quando** a visualização ocorre
> **Então** é criada uma `DocumentInteraction` (referência ao documento, tipo visualização, `departmentId` interno resolvido, IP normalizado, demais metadados do modelo atual); requisições de assets, prévias, health checks e validações de URL não geram interação
>
> **Resultado esperado:** `DocumentInteraction` criada só após carregamento válido.
>
> **Pós-condição:** registro `DocumentInteraction` persistido no banco.
>
> **Critérios cobertos:** [[01 - Demanda#^c20|C20]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-020


> [!example]- CT-021 · Parâmetro ausente ou inválido não gera interação nem revela existência
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
> **Descrição:** confirma que parâmetro ausente/inválido não gera interação nem revela a existência do departamento/documento.
>
> **Pré-condições:**
> - O parâmetro está ausente, malformado, sem correspondência ou sem vínculo com o documento.
>
> **Dado** que o parâmetro está ausente, malformado, sem correspondência ou sem vínculo com o documento
> **Quando** a URL é acessada (ou o documento é acessado por outro fluxo válido, no caso de ausência)
> **Então** o sistema não registra interação de departamento; se o parâmetro for malformado/sem vínculo, retorna a mesma resposta genérica de recurso indisponível, sem revelar a existência do departamento ou do documento
>
> **Resultado esperado:** sem interação, sem revelar existência.
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


> [!example]- CT-022 · Suspensão após encaminhamento não invalida o link histórico
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
> **Descrição:** confirma que a suspensão do departamento depois de um encaminhamento não invalida o link já enviado.
>
> **Pré-condições:**
> - O departamento foi suspenso depois de receber o documento.
>
> **Dado** que o departamento foi suspenso depois de receber o documento
> **Quando** uma URL anteriormente enviada é acessada
> **Então** o vínculo histórico continua válido para visualização e registro da interação — a suspensão impede apenas novos encaminhamentos
>
> **Resultado esperado:** link histórico continua válido.
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
> **Camada:** API
> **Automação:** manual
> **Execução:** não se aplica — depende do grupo D, ainda não testado

^ct-022
