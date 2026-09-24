---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-9982

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle dos casos de teste  
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis. Escopo desta rodada: CT-001 a CT-011 (núcleo funcional). C9 e os requisitos não-funcionais de copy/histórico/acessibilidade/mobile ficam para uma rodada seguinte — ver `01 - Demanda` e `02 - Plano de teste`.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |
| RNF03 (isolamento por usuário) | [[03 - Casos de teste#^ct-010\|CT-010]] |
| RNF04 (persistência entre sessões) | [[03 - Casos de teste#^ct-011\|CT-011]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- CT-001 · Checkbox desmarcado por padrão sem preferência salva
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
> **Descrição:** confirma que o checkbox aparece desmarcado quando o usuário nunca marcou a preferência.
>
> **Pré-condições:**  
> - Usuário não possui preferência de "Permanecer no documento após encerrar" salva.  
> - Usuário está em um documento com tramitação ativa, prestes a abrir um dos três dialogs de encerramento.
>
> **Dado** que o usuário não possui preferência de permanência salva  
> **Quando** ele abre qualquer um dos três dialogs de encerramento (documento inteiro, setor ou participação própria)  
> **Então** o checkbox "Permanecer no documento após encerrar" é exibido desmarcado
>
> **Resultado esperado:** o checkbox inicia desmarcado, sem pré-marcação indevida.
>
> **Pós-condição:** nenhum dado é alterado; o dialog permanece aberto aguardando a decisão do usuário.
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

^ct-001

> [!example]- CT-002 · Confirmar com checkbox desmarcado mantém o redirecionamento atual
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
> **Descrição:** confirma que, sem marcar o checkbox, o comportamento de produção (redirecionar para a mesa) é preservado.
>
> **Pré-condições:**  
> - O checkbox "Permanecer no documento após encerrar" está desmarcado.  
> - O documento tem tramitação ativa passível de encerramento.
>
> **Dado** que o checkbox "Permanecer no documento após encerrar" está desmarcado  
> **Quando** o usuário confirma o encerramento clicando em "Encerrar"  
> **Então** ele é redirecionado para a mesa de trabalho
>
> **Resultado esperado:** comportamento idêntico ao atual de produção.
>
> **Pós-condição:** tramitação encerrada conforme o tipo escolhido; usuário na mesa de trabalho.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Confirmar marcado no encerramento do documento inteiro permanece no documento
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
> **Descrição:** confirma que marcar o checkbox no dialog "Encerrar tramitação" mantém o usuário no documento.
>
> **Pré-condições:**  
> - Usuário tem permissão para encerrar a tramitação do documento inteiro.  
> - Dialog "Encerrar tramitação" está aberto.
>
> **Dado** que o usuário abriu o dialog "Encerrar tramitação" e marcou o checkbox "Permanecer no documento após encerrar"  
> **Quando** ele confirma o encerramento clicando em "Encerrar"  
> **Então** ele permanece no documento, que é recarregado no estado pós-encerramento com as ações indisponíveis já refletidas
>
> **Resultado esperado:** sem redirecionamento para a mesa; documento atualizado sem ação adicional do usuário.
>
> **Pós-condição:** tramitação do documento encerrada para todos os setores envolvidos; usuário permanece na tela do documento.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Confirmar marcado no encerramento de setor permanece no documento
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
> **Descrição:** confirma que marcar o checkbox no dialog "Encerrar tramitação no setor" mantém o usuário no documento.
>
> **Pré-condições:**  
> - Usuário tem permissão para encerrar a participação do próprio setor.  
> - Dialog "Encerrar tramitação no setor" está aberto.
>
> **Dado** que o usuário abriu o dialog "Encerrar tramitação no setor" e marcou o checkbox "Permanecer no documento após encerrar"  
> **Quando** ele confirma o encerramento clicando em "Encerrar"  
> **Então** ele permanece no documento, que é recarregado no estado pós-encerramento, com a participação do setor e de seus colaboradores encerrada
>
> **Resultado esperado:** sem redirecionamento para a mesa; documento atualizado sem ação adicional do usuário.
>
> **Pós-condição:** participação do setor e dos colaboradores encerrada; usuário permanece na tela do documento.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Confirmar marcado no encerramento de participação própria permanece no documento
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
> **Descrição:** confirma que marcar o checkbox no dialog "Encerrar tramitação para mim" mantém o usuário no documento.
>
> **Pré-condições:**  
> - Usuário participa do documento e pode encerrar sua própria participação.  
> - Dialog "Encerrar tramitação para mim" está aberto.
>
> **Dado** que o usuário abriu o dialog "Encerrar tramitação para mim" e marcou o checkbox "Permanecer no documento após encerrar"  
> **Quando** ele confirma o encerramento clicando em "Encerrar"  
> **Então** ele permanece no documento, que é recarregado no estado pós-encerramento, com suas próprias ações indisponíveis
>
> **Resultado esperado:** sem redirecionamento para a mesa; documento atualizado sem ação adicional do usuário.
>
> **Pós-condição:** participação do próprio usuário encerrada; usuário permanece na tela do documento.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]], [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/E2E  
> **Automação:** manual  
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Preferência marcada em um tipo de encerramento já reflete nos outros dois
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
> **Descrição:** confirma que a preferência é única por usuário, não por tipo de encerramento.
>
> **Pré-condições:**  
> - Usuário marcou e confirmou o checkbox em um dos três dialogs (ex.: encerramento de setor) anteriormente.
>
> **Dado** que o usuário marcou e confirmou "Permanecer no documento após encerrar" no encerramento de setor  
> **Quando** ele abre o dialog de encerramento de documento inteiro ou de participação própria em outra tramitação  
> **Então** o checkbox já aparece marcado, sem precisar marcar novamente
>
> **Resultado esperado:** a preferência única é aplicada aos três tipos de encerramento.
>
> **Pós-condição:** a preferência do usuário permanece "permanecer" independentemente do tipo de encerramento.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Reabrir o dialog reflete o último valor salvo
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
> **Descrição:** confirma que o checkbox é pré-marcado conforme a última preferência salva pelo usuário.
>
> **Pré-condições:**  
> - Usuário tem a preferência "permanecer" salva de uma confirmação anterior.
>
> **Dado** que o usuário tem a preferência "permanecer" salva  
> **Quando** ele abre novamente qualquer um dos três dialogs de encerramento  
> **Então** o checkbox aparece pré-marcado
>
> **Resultado esperado:** o estado do checkbox reflete corretamente o último valor salvo.
>
> **Pós-condição:** nenhuma alteração ocorre até que o usuário confirme ou cancele.
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

> [!example]- CT-008 · Desmarcar e confirmar reverte a preferência
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
> **Descrição:** confirma que desmarcar o checkbox e confirmar reverte a preferência do usuário para "voltar à mesa".
>
> **Pré-condições:**  
> - Usuário tem a preferência "permanecer" salva; o checkbox aparece marcado ao abrir o dialog.
>
> **Dado** que o usuário tem a preferência "permanecer" salva e o checkbox aparece marcado  
> **Quando** ele desmarca o checkbox e confirma o encerramento clicando em "Encerrar"  
> **Então** a preferência é revertida e ele é redirecionado para a mesa de trabalho
>
> **Resultado esperado:** a preferência passa a ser "voltar para a mesa" a partir dessa confirmação.
>
> **Pós-condição:** na próxima abertura de qualquer um dos três dialogs, o checkbox aparece desmarcado.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional  
> **Camada:** UI/API  
> **Automação:** manual  
> **Execução:** planejado

^ct-008

> [!example]- CT-009 · Cancelar não grava a preferência nem encerra a tramitação
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
> **Descrição:** confirma que alterar o checkbox sem confirmar o encerramento não grava nada.
>
> **Pré-condições:**  
> - Dialog de encerramento aberto, em qualquer um dos três tipos.
>
> **Dado** que o usuário altera o estado do checkbox (marca ou desmarca)  
> **Quando** ele clica em "Cancelar" ou fecha o dialog sem confirmar  
> **Então** nenhuma preferência é gravada e nenhum encerramento ocorre
>
> **Resultado esperado:** a preferência do usuário e o estado da tramitação permanecem exatamente como estavam antes da abertura do dialog.
>
> **Pós-condição:** próxima abertura do dialog reflete a preferência anterior à tentativa, não a alteração descartada.
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

^ct-009

> [!example]- CT-010 · Preferência é por usuário, não por setor
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
> **Descrição:** confirma que a preferência é isolada por usuário, mesmo entre usuários do mesmo setor.
>
> **Pré-condições:**  
> - Dois usuários do mesmo setor: um com a preferência "permanecer" salva, outro sem preferência salva.
>
> **Dado** dois usuários do mesmo setor, um com a preferência "permanecer" salva e outro sem preferência salva  
> **Quando** cada um confirma um encerramento a partir de sua própria preferência  
> **Então** cada usuário é direcionado conforme a sua própria preferência, independentemente do setor
>
> **Resultado esperado:** nenhuma interferência entre as preferências de usuários do mesmo setor.
>
> **Pós-condição:** preferências individuais preservadas para futuros encerramentos.
>
> **Critérios cobertos:** RNF03 (isolamento por usuário — não vinculado a `^cN` na Demanda)
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** API  
> **Automação:** manual (a definir)  
> **Execução:** planejado

^ct-010

> [!example]- CT-011 · Preferência sobrevive a logout e a novo dispositivo
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
> **Descrição:** confirma que a preferência do usuário é persistida além da sessão atual.
>
> **Pré-condições:**  
> - Usuário tem a preferência "permanecer" salva.
>
> **Dado** que o usuário tem a preferência "permanecer" salva  
> **Quando** ele faz logout e login novamente, ou acessa a plataforma em outro dispositivo  
> **Então** a preferência salva é aplicada normalmente, sem precisar marcar o checkbox de novo
>
> **Resultado esperado:** a preferência é recuperada corretamente em qualquer sessão ou dispositivo do mesmo usuário.
>
> **Pós-condição:** comportamento do checkbox consistente com a preferência salva, independentemente de sessão/dispositivo.
>
> **Critérios cobertos:** RNF04 (persistência — não vinculado a `^cN` na Demanda)
>
> ---
>
> **Informações do CT**
>
> **Tipo:** regressão  
> **Camada:** API  
> **Automação:** manual (a definir)  
> **Execução:** planejado

^ct-011
