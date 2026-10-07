---
tags:
  - qa
  - qase
tipo: referencia
status: enviado
tipo_card: funcionalidade
projeto: ""
modulo: servicos-pj
qase_projeto: SGV
qase_suite_id: 360
casos_origem: "[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste]]"
validacao_origem: "[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/04 - Validação dev]]"
---
# Preparação Qase — SGV-11177

> [!info]- Navegação QA  
> **Demanda:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda]]  
> **Plano de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/02 - Plano de teste]]  
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste]]  
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/04 - Validação dev]]  
> **Preparação Qase:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (só depois de aprovados na validação) para os campos da API.

> [!info] Suite confirmada
> `qase_suite_id: 360` — verificado via `GET /v1/suite/SGV/360` (30/09/2026): título "11177 - Departamentos: Tramitação e assinaturas" (bate com a demanda), `cases_count: 0` (vazia, sem risco de duplicar), `parent_id: 125` ("Melhorias/Funcionalidades" — hierarquia própria de Rafael, fora da suite 220 da epic 9296; reorganização de hierarquia fica pra depois).

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `360` — "11177 - Departamentos: Tramitação e assinaturas"
- **Origem:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste]] (CT-001 a CT-036 — CT-032 a CT-036 vieram de achados na validação real, fora da sequência original; todos os 36 aplicáveis, nenhum "Não se aplica")
- **Script/payload:** processo real descrito em [[../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]] — pasta `Sistema/Scripts/qase-sync/<contexto>/` no vault (`sync.js` + `corrections.json` + `README.md`), copiada da versão mais recente já usada. Não vive no repo de automação.

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | mantém o título humano do cenário |
| Descrição + critério de aceite | `description` | nunca deixar vazio |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado — um CT com múltiplos pares vira múltiplos steps |
| Pós-condição | `postconditions` | só quando agrega algo além do resultado esperado do último step |
| Tipo, severidade, automação | `type`/`severity`/`automation` | **inteiros reais na API**, não texto — usar só rótulos já confirmados contra a Qase real (`--inspect` num caso existente). Camada (UI/API/E2E) é só organização do vault, não é campo da Qase |

**Nunca inventar rótulo de enum.** Rótulos confirmados até 24/09/2026: `severity: normal` (4), `type: acceptance` (7), `automation: is-not-automated` (0).

`priority` e `behavior` ficam de fora do payload por padrão — preencher manualmente na Qase depois, se fizer sentido.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: ID da demanda + módulo (`SGV-11177`, `servicos-pj`) — não criar uma tag por CT.

## Shared steps (mecânicas repetidas entre CTs)

### `notificacao-membro-dupla` — Membro recebe notificação por e-mail e notificação interna
*(usado em: CT-004, CT-021)*
1. Ação: com o membro de departamento adicionado (à tramitação ou como signatário de assinatura) e a ação efetivada/solicitação criada | Resultado esperado: o membro recebe notificação por e-mail e por notificação interna
- Hash na Qase: `98dfb7555ba6371faf9884080bc36f233a65045c`

### `notificacao-departamento-mantida` — E-mail do departamento continua recebendo a notificação
*(usado em: CT-005, CT-022)*
1. Ação: com a notificação do membro já disparada (tramitação ou assinatura) | Resultado esperado: o e-mail do departamento também recebe a notificação, sem substituir a do membro
- Hash na Qase: `4c5d48c3d50a3dfb05ebfa12be523b76547a576f`

### `string-identificacao-membro` — String de identificação do membro segue o padrão do Figma
*(usado em: CT-007, CT-009, CT-010)*
1. Ação: consultar a identificação do membro de departamento renderizada (em tela ou em PDF) | Resultado esperado: segue o padrão `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`
- Hash na Qase: `b344fb966af25ac04db537425366a1cac3b371fb`

## Casos preparados

> Enviado em 30/09/2026 — 36 casos criados (ids 789-824) e 3 shared steps criados na suite SGV/360 via `node sync.js --apply` (`Sistema/Scripts/qase-sync/11177-tramitacao-assinaturas/`). Dry-run validado antes, sem erros nem duplicata.

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

### CT-001 Busca de cidadão PJ retorna departamentos e membros
- **Descrição:** cobre C1 — a busca em campo de cidadão PJ passa a retornar também os cidadãos membros de departamentos que casam com o termo buscado, além dos departamentos correspondentes. Parte da SGV-11177 (Parte 4 da epic SGV-9296, Departamentos).
- **Precondição:** existe ao menos um departamento com membros cujo nome/documento casa com o termo de busca.
- **Passos:** 1. Ação: realizar uma busca em campo de cidadão PJ | Resultado esperado: o sistema lista, além dos departamentos correspondentes, os cidadãos membros desses departamentos que correspondem à busca
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `789`

### CT-002 Resultado da busca distingue departamento de membro
- **Descrição:** cobre C2 — o resultado da busca permite distinguir visualmente um departamento de um membro, conforme o padrão definido no Figma.
- **Precondição:** busca retornando ao menos um departamento e um membro (CT-001).
- **Passos:** 1. Ação: exibir os resultados da busca | Resultado esperado: o sistema permite distinguir visualmente um departamento de um membro, conforme o padrão do Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `790`

### CT-003 Selecionar um membro adiciona à tramitação vinculado ao departamento
- **Descrição:** cobre C3 — selecionar um membro exibido no resultado da busca o adiciona à tramitação, vinculado ao respectivo departamento (não como destinatário solto).
- **Precondição:** um membro de departamento é exibido no resultado da busca (CT-001).
- **Passos:** 1. Ação: selecionar o membro exibido no resultado | Resultado esperado: o sistema o adiciona à tramitação vinculado ao respectivo departamento
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `791`

### CT-004 Membro adicionado à tramitação é notificado
- **Descrição:** cobre C4 — membro de departamento adicionado a uma tramitação é notificado (e-mail + interna) quando ela é efetivada.
- **Precondição:** membro adicionado a uma tramitação (CT-003), ainda não efetivada.
- **Passos:** usa o shared step `notificacao-membro-dupla` (ação: efetivar a tramitação)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `792`

### CT-005 E-mail do departamento continua recebendo a notificação
- **Descrição:** cobre C5 — o e-mail do departamento não é substituído pelo do membro na notificação de tramitação; os dois recebem.
- **Precondição:** tramitação efetivada com um membro de departamento adicionado (CT-004).
- **Passos:** usa o shared step `notificacao-departamento-mantida`
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `793`

### CT-006 Conteúdo das notificações segue o padrão do Figma
- **Descrição:** cobre C6 — texto e apresentação das notificações de tramitação para membro de departamento seguem o Figma. Ponto ainda sujeito a conferência fina no Figma (ver Pendências de decisão em `01 - Demanda`).
- **Precondição:** notificações geradas por uma tramitação destinada a um membro de departamento (CT-004/CT-005).
- **Passos:** 1. Ação: gerar as notificações da tramitação destinada a um membro | Resultado esperado: conteúdo e apresentação seguem o padrão definido no Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `794`

### CT-007 Padrão de exibição do membro na tramitação
- **Descrição:** cobre C7 — identificação do membro na tramitação segue a string `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`.
- **Precondição:** membro de departamento adicionado à tramitação (CT-003).
- **Passos:** usa o shared step `string-identificacao-membro` (exibição em tela, na tramitação)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `795`

### CT-008 Consistência da exibição entre componentes da tramitação
- **Descrição:** cobre C8 — o padrão de exibição do membro (CT-007) se repete de forma consistente em todos os componentes previstos da tramitação, sem variação de formato.
- **Precondição:** membro de departamento aparece em mais de um componente da tramitação (ex.: lista de destinatários e detalhe da tramitação).
- **Passos:** 1. Ação: renderizar a identificação do membro nos diferentes componentes da tramitação | Resultado esperado: o padrão é aplicado de forma consistente em todos os locais previstos no Figma, sem variação
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `796`

### CT-009 Identificação do membro no PDF
- **Descrição:** cobre C9 — PDF gerado a partir da tramitação também aplica o padrão de identificação do membro, igual à tela (CT-007).
- **Precondição:** membro de departamento selecionado em uma tramitação (CT-003).
- **Passos:** usa o shared step `string-identificacao-membro` (exibição no PDF gerado a partir da tramitação)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `797`

### CT-010 Campo do tipo pessoa no PDF segue o mesmo padrão
- **Descrição:** cobre C10 — qualquer campo do tipo pessoa preenchido com um membro de departamento também segue o padrão de identificação no PDF correspondente, não só o PDF da tramitação (CT-009).
- **Precondição:** documento com um campo do tipo pessoa preenchido com um membro de departamento.
- **Passos:** usa o shared step `string-identificacao-membro` (exibição no PDF do campo do tipo pessoa)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `798`

### CT-011 Selecionar departamento na assinatura o adiciona como signatário
- **Descrição:** cobre C11 — pesquisar e selecionar um departamento numa solicitação de assinatura o adiciona como signatário do documento.
- **Precondição:** usuário está configurando uma solicitação de assinatura.
- **Passos:** 1. Ação: pesquisar e selecionar um departamento | Resultado esperado: o departamento é adicionado como signatário
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `799`

### CT-012 Qualquer membro apto do departamento consegue assinar
- **Descrição:** cobre C12 — quando o signatário é um departamento, qualquer membro apto desse departamento consegue realizar a assinatura, não só um específico.
- **Precondição:** assinatura solicitada a um departamento com mais de um membro apto (CT-011).
- **Passos:** 1. Ação: um membro apto do departamento acessa a solicitação de assinatura | Resultado esperado: ele está apto a realizar a assinatura
- **Pós-condição:** documento assinado pelo membro que acessou primeiro; a solicitação é encerrada para os demais membros aptos.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `800`

### CT-013 Token bloqueado quando o signatário é um departamento
- **Descrição:** cobre C13 — quando o signatário selecionado é um departamento inteiro, o sistema não permite configurar a solicitação de assinatura via token (contraste com CT-018, membro específico).
- **Precondição:** departamento selecionado como signatário (CT-011).
- **Passos:** 1. Ação: configurar a solicitação de assinatura pro departamento | Resultado esperado: o sistema não permite a solicitação via token
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `801`

### CT-014 Header do componente signatário para departamento
- **Descrição:** cobre C14 — header do componente de signatário segue o padrão do Figma quando o alvo é o departamento inteiro. Ponto ainda sujeito a conferência fina no Figma (ver Pendências de decisão em `01 - Demanda`).
- **Precondição:** departamento adicionado como signatário (CT-011).
- **Passos:** 1. Ação: exibir o componente signatário do departamento | Resultado esperado: o header segue o padrão definido no Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `802`

### CT-015 Eventos de assinatura identificam o departamento
- **Descrição:** cobre C15 — componente de eventos de assinatura identifica corretamente o departamento (não um membro específico) quando ele é o signatário.
- **Precondição:** ao menos um evento de assinatura já ocorreu numa solicitação com departamento como signatário.
- **Passos:** 1. Ação: exibir os eventos relacionados à assinatura solicitada ao departamento | Resultado esperado: o componente de eventos identifica corretamente o departamento, conforme o Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `803`

### CT-016 Notificação do departamento ao solicitar assinatura
- **Descrição:** cobre C16 — assinatura solicitada a um departamento notifica o e-mail do departamento na criação da solicitação.
- **Precondição:** departamento selecionado como signatário (CT-011).
- **Passos:** 1. Ação: criar a solicitação de assinatura pro departamento | Resultado esperado: o sistema envia a notificação ao e-mail do departamento
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `804`

### CT-017 Selecionar membro na assinatura o adiciona vinculado ao departamento
- **Descrição:** cobre C17 — pesquisar e selecionar um membro de departamento numa solicitação de assinatura o adiciona como signatário, vinculado ao respectivo departamento.
- **Precondição:** usuário está configurando uma solicitação de assinatura.
- **Passos:** 1. Ação: pesquisar e selecionar um membro de departamento | Resultado esperado: o membro é adicionado como signatário, vinculado ao respectivo departamento
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `805`

### CT-018 Token liberado quando o signatário é um membro de departamento
- **Descrição:** cobre C18 — quando o signatário selecionado é um membro específico, o sistema permite configurar a solicitação de assinatura via token (contraste direto com CT-013, departamento inteiro).
- **Precondição:** membro de departamento selecionado como signatário (CT-017).
- **Passos:** 1. Ação: configurar a solicitação de assinatura pro membro | Resultado esperado: o sistema permite a solicitação via token
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `806`

### CT-019 Header do componente signatário identifica membro e departamento
- **Descrição:** cobre C19 — header do componente de signatário identifica corretamente o membro e o departamento quando o alvo é um membro específico. Ponto ainda sujeito a conferência fina no Figma (ver Pendências de decisão em `01 - Demanda`).
- **Precondição:** membro de departamento adicionado como signatário (CT-017).
- **Passos:** 1. Ação: exibir o componente signatário do membro | Resultado esperado: o header identifica corretamente o membro e o departamento, conforme o Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `807`

### CT-020 Eventos de assinatura identificam membro e departamento
- **Descrição:** cobre C20 — componente de eventos de assinatura identifica corretamente o membro e o departamento ao qual pertence. Retestado e aprovado em 30/09/2026 após correção do defeito SGV-11904 (evento mostrava só o cidadão, sem cargo nem departamento).
- **Precondição:** ao menos um evento de assinatura já ocorreu numa solicitação com membro como signatário.
- **Passos:** 1. Ação: exibir os eventos relacionados à assinatura solicitada a um membro | Resultado esperado: o componente identifica corretamente o membro e o departamento, conforme o Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `808`

### CT-021 Notificação do membro signatário
- **Descrição:** cobre C21 — membro de departamento é notificado (e-mail + interna) ao ser adicionado como signatário de uma solicitação de assinatura.
- **Precondição:** membro de departamento selecionado como signatário (CT-017).
- **Passos:** usa o shared step `notificacao-membro-dupla` (ação: criar a solicitação de assinatura)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `809`

### CT-022 E-mail do departamento continua recebendo notificação de assinatura
- **Descrição:** cobre C22 — e-mail do departamento não é substituído pelo do membro na notificação de assinatura; os dois recebem.
- **Precondição:** solicitação de assinatura criada com um membro como signatário (CT-021).
- **Passos:** usa o shared step `notificacao-departamento-mantida`
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `810`

### CT-023 Identificação externa solicita e verifica o CPF
- **Descrição:** cobre C23 — primeiro passo do fluxo externo de assinatura: o sistema solicita o CPF e verifica se existe cadastro correspondente, direcionando pro sub-fluxo certo.
- **Precondição:** pessoa acessa externamente uma solicitação de assinatura destinada a um departamento ou membro.
- **Passos:** 1. Ação: iniciar a identificação externa informando o CPF | Resultado esperado: o sistema verifica se existe cadastro correspondente e direciona pro sub-fluxo certo (CT-024, CT-025 ou CT-026)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `811`

### CT-024 Pessoa cadastrada e vinculada assina com senha
- **Descrição:** cobre C24 — caminho mais direto do fluxo externo: pessoa já cadastrada e já vinculada ao departamento destinatário assina só com a senha.
- **Precondição:** CPF informado (CT-023) pertence a uma pessoa cadastrada e já vinculada ao departamento destinatário.
- **Passos:** 1. Ação: informar a senha após a identificação | Resultado esperado: a pessoa realiza a assinatura sem etapa adicional de vínculo ou cadastro
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `812`

### CT-025 Pessoa cadastrada sem vínculo informa cargo, vincula e assina
- **Descrição:** cobre C25 — caminho intermediário: pessoa já cadastrada no SOGOV, mas ainda não membro do departamento destinatário, informa o cargo, é vinculada e assina no mesmo fluxo.
- **Precondição:** CPF informado (CT-023) pertence a uma pessoa cadastrada, mas sem vínculo com o departamento destinatário.
- **Passos:** 1. Ação: informar o cargo solicitado | Resultado esperado: a pessoa é vinculada ao departamento com o cargo informado e realiza a assinatura no mesmo fluxo
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `813`

### CT-026 Pessoa sem cadastro é levada ao pré-cadastro
- **Descrição:** cobre C26 — caminho mais longo: CPF sem cadastro correspondente no SOGOV é levado ao pré-cadastro (CPF, e-mail, cargo), sem pular nenhum campo.
- **Precondição:** CPF informado (CT-023) não corresponde a nenhum cadastro existente.
- **Passos:** 1. Ação: prosseguir com a assinatura sem cadastro existente | Resultado esperado: o sistema solicita CPF, e-mail e cargo para o pré-cadastro
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `814`

### CT-027 Termos e declaração de maioridade no pré-cadastro
- **Descrição:** cobre C27 — pré-cadastro exige aceite dos termos aplicáveis e declaração de maioridade, no modal definido no Figma, antes de prosseguir. Ponto ainda sujeito a conferência fina no Figma (ver Pendências de decisão em `01 - Demanda`).
- **Precondição:** pessoa preenchendo o pré-cadastro (CT-026).
- **Passos:** 1. Ação: confirmar os dados do pré-cadastro | Resultado esperado: a confirmação fica bloqueada até o aceite dos termos e a declaração de maioridade, no modal do Figma
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `815`

### CT-028 Criação do pré-cadastro e vínculo com o departamento
- **Descrição:** cobre C28 — com dados válidos e consentimentos completos, o sistema cria o pré-cadastro e vincula a pessoa ao departamento com o cargo informado.
- **Precondição:** dados válidos informados e consentimentos aceitos no pré-cadastro (CT-026, CT-027).
- **Passos:** 1. Ação: confirmar o pré-cadastro com dados válidos e consentimentos completos | Resultado esperado: o sistema cria o pré-cadastro e vincula a pessoa ao departamento com o cargo informado
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `816`

### CT-029 Assinatura no mesmo fluxo após o pré-cadastro
- **Descrição:** cobre C29 — concluído o pré-cadastro e o vínculo, a pessoa assina na mesma sessão, sem precisar reiniciar o fluxo.
- **Precondição:** pré-cadastro e vínculo com o departamento concluídos (CT-028).
- **Passos:** 1. Ação: prosseguir após a conclusão do pré-cadastro e do vínculo | Resultado esperado: a pessoa realiza a assinatura na mesma sessão, sem novo login ou navegação
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `817`

### CT-030 Convite por e-mail para completar o cadastro
- **Descrição:** cobre C30 — depois de assinar via pré-cadastro, a pessoa recebe um e-mail com instruções pra completar o cadastro no SOGOV.
- **Precondição:** pessoa assinou o documento por meio de um pré-cadastro (CT-029).
- **Passos:** 1. Ação: concluir a assinatura via pré-cadastro | Resultado esperado: o sistema envia um e-mail com instruções pra completar o cadastro no SOGOV
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `818`

### CT-031 Inconsistência no fluxo externo não cria vínculo ou cadastro duplicado
- **Descrição:** cobre C31 — qualquer inconsistência na identificação, autenticação, vinculação ou pré-cadastro impede a assinatura e mostra mensagem de erro adequada, sem deixar vínculo ou cadastro parcial.
- **Precondição:** uma inconsistência é provocada deliberadamente em cada uma das quatro etapas do fluxo externo (ex.: senha errada, cargo inválido, e-mail já usado, sessão expirada no meio do fluxo).
- **Passos:** 1. Ação: provocar uma inconsistência na identificação, autenticação, vinculação ou pré-cadastro | Resultado esperado: o sistema impede a assinatura, mostra mensagem de erro adequada específica pra etapa, e não cria vínculo ou cadastro duplicado
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `819`

### CT-032 Selo de assinatura do membro traz o contexto do departamento
- **Descrição:** cobre C32 — selo aplicado no documento assinado por um membro de departamento traz razão social, nome do departamento, nome de exibição (com cargo) e papel — mesmo padrão já cobrado no header (CT-019) e nos eventos (CT-020), não só o cidadão isolado. Achado de validação real (29/09/2026); retestado e aprovado em 30/09/2026 após correção do defeito SGV-11905.
- **Precondição:** um cidadão membro de um departamento foi selecionado como signatário (CT-017) e concluiu a assinatura.
- **Passos:** 1. Ação: consultar o selo de assinatura aplicado no documento | Resultado esperado: o selo mostra razão social, nome do departamento, nome de exibição (com o cargo no departamento) e papel
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `820`

### CT-033 Selecionar o cidadão PJ funciona igual, independente do caminho de busca
- **Descrição:** cobre C33 — solicitar assinatura pro cidadão PJ dá o mesmo resultado independente de ele ter sido localizado direto ou via hierarquia `Cidadão PJ > Departamento > Membro`. Achado de validação real (29/09/2026, efeito colateral da busca nova sobre capacidade pré-existente); retestado e aprovado em 30/09/2026 após correção do defeito SGV-11910.
- **Precondição:** cidadão PJ com ao menos um departamento cadastrado.
- **Passos:** 1. Ação: pesquisar diretamente pelo cidadão PJ e solicitar a assinatura dele | Resultado esperado: a solicitação é aceita normalmente. 2. Ação: repetir a mesma solicitação pesquisando pelo nome de um departamento ou membro desse cidadão PJ, selecionando o mesmo cidadão PJ a partir da linha `Cidadão PJ > Departamento > Membro` | Resultado esperado: o mesmo comportamento do passo 1 — solicitação aceita, sem tag de cadastro incompleto
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `821`

### CT-034 Selo do departamento não traz papel em nenhum estado
- **Descrição:** cobre C34 — selo de um departamento signatário mostra só razão social e nome do departamento, sem o campo papel, em nenhum dos três estados (a posicionar, posicionado, assinado). Achado de validação real (29/09/2026); retestado e aprovado em 30/09/2026 após correção do defeito SGV-11917.
- **Precondição:** assinatura solicitada a um departamento (CT-011).
- **Passos:** 1. Ação: exibir o selo em cada um dos três estados (a posicionar, posicionado, assinado) | Resultado esperado: o selo mostra só razão social e nome do departamento, sem o campo papel, nos três estados
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `822`

### CT-035 Assinatura a departamentos diferentes do mesmo cidadão PJ
- **Descrição:** cobre C35 — solicitar assinatura a um segundo departamento diferente do mesmo cidadão PJ não é bloqueado (mesma regra de múltiplos departamentos por documento já válida pra destinatário de tramitação, SGV-11184, estendida à assinatura). Achado de validação real (29/09/2026); retestado e aprovado em 30/09/2026 após correção do defeito SGV-11924.
- **Precondição:** assinatura já solicitada a um departamento de um cidadão PJ (CT-011).
- **Passos:** 1. Ação: configurar uma nova solicitação de assinatura a um departamento diferente do mesmo cidadão PJ | Resultado esperado: o sistema aceita a solicitação normalmente, sem o erro `you-have-already-been-asked-once-with-sogov`
- **Pós-condição:** os dois departamentos ficam como signatários pendentes, cada um com sua própria solicitação.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `823`

### CT-036 Solicitação de assinatura aparece na lista de demandas do departamento
- **Descrição:** cobre C36 — solicitação de assinatura, seja a um membro de departamento ou ao departamento inteiro, aparece na lista de demandas do departamento. Achado de validação real (30/09/2026); retestado e aprovado no mesmo dia após correção do defeito SGV-11948.
- **Precondição:** assinatura solicitada a um membro de departamento (CT-017) ou ao departamento inteiro (CT-011).
- **Passos:** 1. Ação: consultar a lista de demandas do departamento após a solicitação | Resultado esperado: a nova solicitação aparece na lista, nos dois casos (membro e departamento inteiro)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `824`

## Checklist de envio

- [x] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [x] Projeto e suite confirmados (suite pré-existente ou criada com autorização explícita).
- [x] Campos normalizados e passos separados.
- [x] Tags limitadas ao ID da demanda e ao módulo.
- [x] Campos da API validados (`dry-run` rodado antes do `--apply`).
- [x] Envio realizado sem duplicação.
- [x] IDs da Qase registrados nesta nota.
- [x] Status alterado para `enviado`.

> [!note] Pendência combinada com Rafael (30/09/2026)
> Depois deste envio, ainda vêm ajustes no template de preparação e em como os CTs são transcritos pra Qase — a aplicar na próxima rodada (SGV-11178 ou outra), não retroativo a este envio já aplicado.
