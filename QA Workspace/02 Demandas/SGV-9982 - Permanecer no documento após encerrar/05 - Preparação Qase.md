---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: melhoria
projeto: ""
modulo: "Tramitação — Encerramento de documento"
qase_projeto: ""
qase_suite_id: ""
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-9982

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` para os campos da API.

> **Pendência:** `qase_projeto` e `qase_suite_id` ainda não foram confirmados para o módulo Tramitação — verificar suites existentes antes do envio real. Nenhum caso foi enviado à Qase nesta etapa.

## Configuração

- **Projeto Qase:** `<a confirmar>`
- **Suite Qase:** `<a confirmar>`
- **Origem:** [[03 - Casos de teste]] (CT-001 a CT-011)

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | manter o título humano do cenário |
| Descrição | `description` | resumir o objetivo do CT |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado |
| Pós-condição | `postconditions` | registrar somente o estado após o teste |
| Tipo, camada, automação | campos Qase | usar os valores normalizados abaixo |

Valores normalizados: `funcional`/`regressão`; camada `E2E`/`API`/`unit`; automação `manual`/`automatizado`/`ambos`.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: `SGV-9982`, `tramitação` — não criar uma tag por CT.

## Casos preparados

> Nenhum destes casos foi enviado à Qase. Os `Qase ID` ficam em branco até o envio real.

### CT-001 — Checkbox desmarcado por padrão sem preferência salva

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que o checkbox "Permanecer no documento após encerrar" aparece desmarcado para usuário sem preferência salva.
- **Pré-condições:** usuário não possui preferência salva; está em documento com tramitação ativa, prestes a abrir um dos três dialogs de encerramento.
- **Passo 1 — Ação:** abrir qualquer um dos três dialogs de encerramento.
  **Resultado esperado:** o checkbox "Permanecer no documento após encerrar" é exibido desmarcado.
- **Pós-condição:** nenhum dado alterado; dialog aberto aguardando decisão.
- **Tipo:** funcional. **Camada:** UI. **Automação:** manual. **Prioridade Qase:** média. **Severidade Qase:** normal. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-002 — Confirmar com checkbox desmarcado mantém o redirecionamento atual

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que, sem marcar o checkbox, o usuário continua sendo redirecionado para a mesa de trabalho.
- **Pré-condições:** checkbox desmarcado; documento com tramitação ativa.
- **Passo 1 — Ação:** confirmar o encerramento clicando em "Encerrar" com o checkbox desmarcado.
  **Resultado esperado:** usuário é redirecionado para a mesa de trabalho.
- **Pós-condição:** tramitação encerrada conforme o tipo escolhido; usuário na mesa de trabalho.
- **Tipo:** regressão. **Camada:** E2E. **Automação:** manual. **Prioridade Qase:** alta. **Severidade Qase:** crítica. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-003 — Confirmar marcado no encerramento do documento inteiro permanece no documento

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que marcar o checkbox no dialog "Encerrar tramitação" mantém o usuário no documento.
- **Pré-condições:** usuário com permissão para encerrar a tramitação do documento inteiro; dialog "Encerrar tramitação" aberto.
- **Passo 1 — Ação:** marcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** usuário permanece no documento, recarregado no estado pós-encerramento.
- **Pós-condição:** tramitação do documento encerrada para todos os setores; usuário permanece na tela do documento.
- **Tipo:** funcional. **Camada:** E2E. **Automação:** manual. **Prioridade Qase:** alta. **Severidade Qase:** normal. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-004 — Confirmar marcado no encerramento de setor permanece no documento

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que marcar o checkbox no dialog "Encerrar tramitação no setor" mantém o usuário no documento.
- **Pré-condições:** usuário com permissão para encerrar a participação do próprio setor; dialog "Encerrar tramitação no setor" aberto.
- **Passo 1 — Ação:** marcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** usuário permanece no documento, recarregado no estado pós-encerramento; participação do setor e colaboradores encerrada.
- **Pós-condição:** participação do setor e colaboradores encerrada; usuário permanece na tela do documento.
- **Tipo:** funcional. **Camada:** E2E. **Automação:** manual. **Prioridade Qase:** alta. **Severidade Qase:** normal. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-005 — Confirmar marcado no encerramento de participação própria permanece no documento

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que marcar o checkbox no dialog "Encerrar tramitação para mim" mantém o usuário no documento.
- **Pré-condições:** usuário participa do documento; dialog "Encerrar tramitação para mim" aberto.
- **Passo 1 — Ação:** marcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** usuário permanece no documento, recarregado no estado pós-encerramento; suas próprias ações ficam indisponíveis.
- **Pós-condição:** participação do próprio usuário encerrada; usuário permanece na tela do documento.
- **Tipo:** funcional. **Camada:** E2E. **Automação:** manual. **Prioridade Qase:** alta. **Severidade Qase:** normal. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-006 — Preferência marcada em um tipo de encerramento já reflete nos outros dois

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que a preferência é única por usuário, não por tipo de encerramento.
- **Pré-condições:** usuário marcou e confirmou o checkbox em um dos três dialogs anteriormente.
- **Passo 1 — Ação:** abrir outro dialog de encerramento (tipo diferente do já confirmado).
  **Resultado esperado:** checkbox já aparece marcado, sem precisar marcar novamente.
- **Pós-condição:** preferência do usuário permanece "permanecer" para qualquer tipo de encerramento.
- **Tipo:** funcional. **Camada:** API. **Automação:** manual. **Prioridade Qase:** média. **Severidade Qase:** normal. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-007 — Reabrir o dialog reflete o último valor salvo

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que o checkbox é pré-marcado conforme a última preferência salva.
- **Pré-condições:** usuário tem a preferência "permanecer" salva.
- **Passo 1 — Ação:** abrir novamente qualquer um dos três dialogs de encerramento.
  **Resultado esperado:** checkbox aparece pré-marcado.
- **Pós-condição:** nenhuma alteração até nova confirmação ou cancelamento.
- **Tipo:** funcional. **Camada:** API. **Automação:** manual. **Prioridade Qase:** média. **Severidade Qase:** normal. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-008 — Desmarcar e confirmar reverte a preferência

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que desmarcar o checkbox e confirmar reverte a preferência para "voltar à mesa".
- **Pré-condições:** usuário tem a preferência "permanecer" salva; checkbox aparece marcado.
- **Passo 1 — Ação:** desmarcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** preferência revertida; usuário redirecionado para a mesa de trabalho.
- **Pós-condição:** próxima abertura de qualquer dialog mostra o checkbox desmarcado.
- **Tipo:** funcional. **Camada:** API. **Automação:** manual. **Prioridade Qase:** média. **Severidade Qase:** normal. **Comportamento:** negativo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-009 — Cancelar não grava a preferência nem encerra a tramitação

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma que alterar o checkbox sem confirmar não grava nada.
- **Pré-condições:** dialog de encerramento aberto, em qualquer um dos três tipos.
- **Passo 1 — Ação:** alterar o estado do checkbox e clicar em "Cancelar" (ou fechar o dialog).
  **Resultado esperado:** nenhuma preferência gravada; nenhum encerramento ocorre.
- **Pós-condição:** preferência e tramitação permanecem como estavam antes da abertura do dialog.
- **Tipo:** funcional. **Camada:** UI. **Automação:** manual. **Prioridade Qase:** média. **Severidade Qase:** normal. **Comportamento:** negativo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-010 — Preferência é por usuário, não por setor

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma isolamento da preferência por usuário, mesmo entre usuários do mesmo setor.
- **Pré-condições:** dois usuários do mesmo setor, um com preferência salva e outro sem.
- **Passo 1 — Ação:** cada usuário confirma um encerramento a partir de sua própria preferência.
  **Resultado esperado:** cada usuário é direcionado conforme sua própria preferência, sem interferência do setor.
- **Pós-condição:** preferências individuais preservadas.
- **Tipo:** regressão. **Camada:** API. **Automação:** a definir. **Prioridade Qase:** baixa. **Severidade Qase:** menor. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-011 — Preferência sobrevive a logout e a novo dispositivo

- **Qase ID:** `preencher após o envio`
- **Descrição:** confirma persistência da preferência além da sessão atual.
- **Pré-condições:** usuário tem a preferência "permanecer" salva.
- **Passo 1 — Ação:** fazer logout e login novamente, ou acessar de outro dispositivo.
  **Resultado esperado:** preferência salva é aplicada normalmente.
- **Pós-condição:** comportamento do checkbox consistente com a preferência salva em qualquer sessão/dispositivo.
- **Tipo:** regressão. **Camada:** API. **Automação:** a definir. **Prioridade Qase:** baixa. **Severidade Qase:** menor. **Comportamento:** positivo.
- **Tags Qase:** `SGV-9982`, `tramitação`

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

## Checklist de envio

- [ ] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados.
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados.
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
