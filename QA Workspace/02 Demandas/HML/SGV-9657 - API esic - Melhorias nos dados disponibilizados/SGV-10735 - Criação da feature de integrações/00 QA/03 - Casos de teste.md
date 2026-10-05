---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-10735

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis. Cenários em linguagem visual (tela), sem execução real ainda — sem ambiente de teste disponível até 05/10/2026.

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

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- CT-001 · Exibir "Integrações" desabilitada para cliente inativo
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
> **Descrição:** confirma que a opção "Integrações" aparece no menu de ações, mas fica desabilitada quando o cliente está inativo.
>
> **Pré-condições:**
> - Existir um cliente com status "Inativo".
>
> **Dado** que um cliente esteja com status "Inativo"
> **Quando** o menu de ações (kebab) desse cliente for aberto na listagem de clientes
> **Então** a opção "Integrações" aparece visível, porém desabilitada para clique
>
> **Resultado esperado:** opção visível e desabilitada, comunicando que o recurso existe mas não está disponível pra esse cliente agora.
>
> **Pós-condição:** nenhuma alteração de dado.
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

> [!example]- CT-002 · Exibir brasão e nome do cliente durante toda a navegação
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
> **Descrição:** confirma que a página de Integrações mantém o cliente identificado (brasão + nome) em qualquer etapa da navegação.
>
> **Pré-condições:**
> - Existir um cliente ativo, com brasão cadastrado.
>
> **Dado** que o usuário acesse a página de Integrações de um cliente ativo
> **Quando** navegar entre as seções da página (credenciais, módulos, histórico)
> **Então** o brasão e o nome do cliente permanecem visíveis em todas elas
>
> **Resultado esperado:** mesmo brasão/nome usado na listagem de clientes, sem trocar ou sumir ao navegar.
>
> **Pós-condição:** nenhuma alteração de dado.
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

> [!example]- CT-003 · Ativar a integração gera as duas credenciais com estado de carregamento
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
> **Descrição:** confirma que ativar a integração gera identificador do cliente e chave secreta, com efeito imediato.
>
> **Pré-condições:**
> - Cliente ativo, sem integração ativada ainda.
>
> **Dado** que o cliente não tenha a integração ativada
> **Quando** o usuário clicar em ativar a integração
> **Então** a página exibe um estado de carregamento e, em seguida, o identificador do cliente e a chave secreta preenchidos
>
> **Resultado esperado:** credenciais aparecem sem precisar de nenhum passo de salvamento adicional.
>
> **Pós-condição:** integração ativa, credenciais persistidas.
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

> [!example]- CT-004 · Credenciais são somente leitura e chave secreta vem mascarada
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
> **Descrição:** confirma que identificador e chave secreta não podem ser editados, e que a chave secreta aparece parcialmente mascarada.
>
> **Pré-condições:**
> - Cliente com integração já ativada.
>
> **Dado** que o cliente tenha a integração ativada
> **Quando** a página de Integrações for exibida
> **Então** o identificador do cliente e a chave secreta aparecem em campos somente leitura, e a chave secreta vem parcialmente mascarada
>
> **Resultado esperado:** nenhum dos dois campos aceita edição; chave secreta nunca aparece por extenso na tela.
>
> **Pós-condição:** nenhuma alteração de dado.
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

> [!example]- CT-005 · Copiar credencial sempre copia o valor real, com confirmação visual
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
> **Descrição:** confirma que copiar a chave secreta mascarada copia o valor real pra área de transferência, e que a cópia é confirmada visualmente.
>
> **Pré-condições:**
> - Cliente com integração ativada, chave secreta mascarada na tela.
>
> **Dado** que a chave secreta esteja mascarada na tela
> **Quando** o usuário clicar em copiar a chave secreta
> **E** colar o conteúdo copiado em outro campo
> **Então** o valor colado é o valor real (não a máscara), e a tela exibe uma confirmação visual de que a cópia foi feita
>
> **Resultado esperado:** mesmo comportamento se repete ao copiar o identificador do cliente.
>
> **Pós-condição:** nenhuma alteração de dado.
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

> [!example]- CT-006 · Reativar a integração preserva as credenciais, sem gerar novas
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
> **Descrição:** confirma que desativar e reativar a integração mantém as mesmas credenciais geradas originalmente.
>
> **Pré-condições:**
> - Cliente com integração ativada, credenciais já geradas e anotadas.
>
> **Dado** que o cliente tenha a integração ativada com credenciais conhecidas
> **Quando** o usuário desativar e, em seguida, reativar a integração
> **Então** o identificador do cliente e a chave secreta exibidos são os mesmos de antes da desativação
>
> **Resultado esperado:** nenhuma credencial nova é gerada na reativação.
>
> **Pós-condição:** integração ativa novamente, credenciais inalteradas.
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

> [!example]- CT-007 · Lista de módulos exibe só os contratados pelo cliente
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
> **Descrição:** confirma que o seletor de módulos da integração só lista os módulos contratados pelo cliente.
>
> **Pré-condições:**
> - Cliente com um subconjunto específico de módulos contratados (não todos os módulos existentes).
>
> **Dado** que o cliente tenha contratado apenas alguns módulos
> **Quando** o seletor de módulos da página de Integrações for aberto
> **Então** só aparecem como opção os módulos contratados por esse cliente
>
> **Resultado esperado:** nenhum módulo não-contratado aparece como opção selecionável.
>
> **Pós-condição:** nenhuma alteração de dado.
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

> [!example]- CT-008 · Manter integração ativa sem nenhum módulo selecionado
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
> **Descrição:** confirma que a integração pode ficar ativa mesmo sem módulo nenhum selecionado.
>
> **Pré-condições:**
> - Cliente com integração ativada, nenhum módulo selecionado ainda.
>
> **Dado** que a integração esteja ativa e sem módulos selecionados
> **Quando** o usuário sair da página sem selecionar nenhum módulo
> **Então** a integração continua ativa, sem exigir ao menos um módulo selecionado
>
> **Resultado esperado:** nenhum bloqueio ou erro por falta de seleção de módulo.
>
> **Pós-condição:** integração ativa, sem módulos expostos.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** borda
> **Camada:** UI
> **Automação:** manual
> **Execução:** planejado

^ct-008

> [!example]- CT-009 · Salvar seleção de módulos exige confirmação
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
> **Descrição:** confirma que alterar a seleção de módulos só tem efeito depois de confirmado o salvamento, e que esse salvamento pede confirmação.
>
> **Pré-condições:**
> - Cliente com integração ativada e ao menos um módulo já selecionado.
>
> **Dado** que o usuário altere a seleção de módulos (adicionar ou remover um módulo)
> **Quando** clicar em salvar
> **Então** a tela exibe um pedido de confirmação antes de aplicar a alteração
>
> **E** confirmar a ação
>
> **Então** a nova seleção passa a valer imediatamente para a integração
>
> **Resultado esperado:** sem a confirmação, a alteração não é efetivada.
>
> **Pós-condição:** seleção de módulos atualizada conforme confirmado.
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

> [!example]- CT-010 · Sair da página com alterações pendentes pede confirmação
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
> **Descrição:** confirma que tentar sair da página com alterações de módulo não salvas pede confirmação antes de descartar.
>
> **Pré-condições:**
> - Usuário altere a seleção de módulos sem salvar.
>
> **Dado** que exista alteração de módulo não salva na página
> **Quando** o usuário tentar sair da página de Integrações
> **Então** a tela pede confirmação antes de descartar a alteração pendente
>
> **Resultado esperado:** só sai sem salvar se o usuário confirmar o descarte.
>
> **Pós-condição:** alteração descartada (se confirmado) ou página permanece aberta (se cancelado).
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
> **Execução:** planejado

^ct-010

> [!example]- CT-011 · Desativar a integração exige confirmação e exibe mensagem específica
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
> **Descrição:** confirma que desativar a integração pede confirmação e, ao concluir, exibe a mensagem "API e-SIC desativada."
>
> **Pré-condições:**
> - Cliente com integração ativada.
>
> **Dado** que a integração esteja ativa
> **Quando** o usuário clicar em desativar, no botão do título do container
> **Então** a tela pede confirmação antes de desativar
>
> **E** confirmar a ação
>
> **Então** a tela exibe a mensagem "API e-SIC desativada."
>
> **Resultado esperado:** integração passa a "Inativa" só após a confirmação.
>
> **Pós-condição:** integração desativada, credenciais e módulos preservados.
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

> [!example]- CT-012 · Reativar a integração exibe mensagem específica
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
> **Descrição:** confirma que reativar a integração exibe a mensagem "API e-SIC reativada. Credenciais mantidas."
>
> **Pré-condições:**
> - Cliente com integração desativada previamente.
>
> **Dado** que a integração esteja desativada
> **Quando** o usuário clicar em reativar
> **Então** a tela exibe a mensagem "API e-SIC reativada. Credenciais mantidas."
>
> **Resultado esperado:** mensagem exata, sem variação de texto.
>
> **Pós-condição:** integração ativa novamente.
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

> [!example]- CT-013 · Histórico de alterações registra as ações e fica acessível mesmo desativado
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
> **Descrição:** confirma que o histórico registra ativação/desativação, inclusão/remoção de módulo e cópia de credencial, com responsável, data e hora, e continua acessível com a integração desativada.
>
> **Pré-condições:**
> - Cliente com histórico de ao menos uma ativação, uma alteração de módulo e uma cópia de credencial.
>
> **Dado** que o cliente tenha realizado ativação, alteração de módulo e cópia de credencial em momentos diferentes
> **Quando** o histórico de alterações for consultado
> **Então** cada ação aparece registrada com responsável, data e hora
>
> **E** a integração estiver desativada
> **Quando** o histórico for consultado novamente
> **Então** os registros anteriores continuam visíveis normalmente
>
> **Resultado esperado:** histórico nunca fica vazio ou inacessível por causa do estado atual da integração.
>
> **Pós-condição:** nenhuma alteração de dado.
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI
> **Automação:** manual
> **Execução:** planejado

^ct-013
