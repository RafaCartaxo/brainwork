---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: "funcionalidade"
projeto: ""
modulo: servicos-pj
qase_projeto: SGV
qase_suite_id: 361
demanda: "[[01 - Demanda]]"
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-11178

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (só depois de aprovados na validação) para os campos da API.

> [!info] Suite confirmada  
> `qase_suite_id: 361` — criada via `POST /v1/suite/SGV` em 01/10/2026, com autorização explícita do Rafael (GATE 2 cumprido — suite não existia ainda pra essa demanda). Título "11178 - Departamentos: Cadastro rápido", `parent_id: 125` ("Melhorias/Funcionalidades", mesmo pai da suite 360 da SGV-11177), `cases_count: 0` (vazia, sem risco de duplicar).

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `361` — "11178 - Departamentos: Cadastro rápido"
- **Origem:** [[03 - Casos de teste]] (CT-001 a CT-037 — todos aplicáveis, nenhum "Não se aplica". CT-038 fica de fora por enquanto: defeito [[Defeitos/SGV-11962 - Defeito Modal De Cadastro Rápido Sem Responsividade|SGV-11962]] ainda aberto, aguardando DEV)
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

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: ID da demanda + módulo (`SGV-11178`, `servicos-pj`) — não criar uma tag por CT.

## Casos preparados

> Nenhum caso foi enviado ainda. Os `Qase ID` ficam em branco até o `--apply`.

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

### CT-001 Atalho de cadastro rápido disponível no componente de seleção
- **Descrição:** cobre C1 — confirma que um componente de seleção de pessoa que permite adicionar cidadão disponibiliza o atalho de cadastro rápido. Parte da SGV-11178 (Departamentos — Cadastro rápido).
- **Precondição:** servidor está em um campo do tipo pessoa ou componente de seleção de usuário que permite adicionar cidadão.
- **Passos:** 1. Ação: exibir o componente de seleção | Resultado esperado: o sistema disponibiliza um atalho para o cadastro rápido, visível e acionável
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-002 Atalho consistente entre os contextos de uso
- **Descrição:** cobre C2 — confirma que o atalho aparece de forma consistente nos quatro contextos previstos (campo solicitante, campo tipo pessoa PF/PJ, destinatário de despacho, seleção de signatário).
- **Precondição:** servidor tem acesso aos quatro contextos: campo solicitante, campo tipo pessoa PF/PJ, destinatário de despacho, seleção de signatário.
- **Passos:** 1. Ação: exibir o componente de seleção em cada um dos quatro contextos | Resultado esperado: o atalho de cadastro rápido é oferecido da mesma forma em todos, sem variação de disponibilidade
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-003 Escolha entre Pessoa Física, Pessoa Jurídica e Departamento
- **Descrição:** cobre C3 — confirma que acionar o atalho exibe a opção de escolher entre os 3 tipos de cadastro.
- **Precondição:** atalho de cadastro rápido disponível (CT-001).
- **Passos:** 1. Ação: acionar o atalho | Resultado esperado: o formulário exibido permite escolher entre Pessoa Física, Pessoa Jurídica e Departamento
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-004 Seleção automática do registro criado no campo de origem
- **Descrição:** cobre C4 — confirma que, ao concluir o cadastro rápido com sucesso, o registro criado é selecionado automaticamente no campo de origem.
- **Precondição:** cadastro rápido concluído com sucesso (qualquer tipo) a partir de um campo compatível.
- **Passos:** 1. Ação: o sistema retornar ao componente de origem após a conclusão | Resultado esperado: o novo registro fica disponível e selecionado no campo, desde que compatível com os parâmetros desse campo
- **Pós-condição:** registro criado e vinculado ao campo de origem.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-005 Seletor radio button com as três opções
- **Descrição:** cobre C5 — confirma a apresentação do seletor de tipo do formulário de cadastro rápido.
- **Precondição:** formulário de cadastro rápido aberto.
- **Passos:** 1. Ação: visualizar as opções do formulário | Resultado esperado: o sistema apresenta um seletor do tipo radio button com as opções Pessoa Física, Pessoa Jurídica e Departamento, mutuamente exclusivas
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-006 Apenas um formulário exibido por vez
- **Descrição:** cobre C6 — confirma que somente o formulário do tipo selecionado é exibido.
- **Precondição:** formulário de cadastro rápido aberto, um tipo selecionado.
- **Passos:** 1. Ação: selecionar um tipo de cadastro | Resultado esperado: somente o formulário correspondente é exibido; campos dos outros dois tipos ficam ocultos, não só desabilitados
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-007 Preservação de dados ao alternar entre tipos
- **Descrição:** cobre C7 — confirma que dados preenchidos num tipo não se perdem ao alternar para outro e voltar.
- **Precondição:** servidor preencheu parcial ou totalmente um formulário (ex.: Pessoa Física).
- **Passos:** 1. Ação: alternar para outro tipo e retornar ao anterior | Resultado esperado: os dados informados anteriormente permanecem preenchidos enquanto o cadastro rápido estiver aberto, sem nenhum campo limpo pela troca
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-008 Campos do formulário de Pessoa Física
- **Descrição:** cobre C8 — confirma os campos apresentados no formulário de Pessoa Física.
- **Precondição:** opção Pessoa Física selecionada.
- **Passos:** 1. Ação: exibir o formulário | Resultado esperado: são apresentados os campos CPF, Nome, E-mail e Telefone, sem campo adicional não previsto
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-009 Estado inicial dos campos de Pessoa Física
- **Descrição:** cobre C9 — confirma o estado inicial do formulário antes de qualquer CPF válido consultado.
- **Precondição:** formulário de Pessoa Física aberto, nenhum CPF consultado ainda.
- **Passos:** 1. Ação: abrir o formulário sem consultar um CPF válido | Resultado esperado: o campo Nome permanece desabilitado, e os campos E-mail e Telefone são opcionais (não bloqueiam a confirmação se vazios)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-010 Validação do CPF antes da consulta à API
- **Descrição:** cobre C10 — confirma que o CPF é validado no front antes de qualquer chamada à API.
- **Precondição:** formulário de Pessoa Física aberto.
- **Passos:** 1. Ação: informar um CPF e submeter à consulta | Resultado esperado: o sistema valida o CPF antes de consultar a API; CPF com formato/dígito verificador inválido não dispara chamada à API
- **Pós-condição:** nenhuma consulta realizada para CPF inválido.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-011 Preenchimento automático do Nome via API
- **Descrição:** cobre C11 — confirma o preenchimento automático do Nome quando a API retorna dados de um CPF válido.
- **Precondição:** CPF válido informado e submetido à consulta.
- **Passos:** 1. Ação: a API retornar os dados correspondentes | Resultado esperado: o sistema preenche automaticamente o Nome, mantendo o campo desabilitado para edição
- **Pós-condição:** formulário pronto para conclusão (Nome preenchido).
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-012 Conclusão do cadastro de Pessoa Física
- **Descrição:** cobre C12 — confirma que o cadastro é criado mesmo sem E-mail/Telefone, desde que CPF e Nome estejam validados.
- **Precondição:** CPF e Nome validados (CT-010/CT-011).
- **Passos:** 1. Ação: confirmar o formulário | Resultado esperado: o sistema cria o cadastro da pessoa física com sucesso, independentemente do preenchimento de E-mail ou Telefone
- **Pós-condição:** pessoa física cadastrada no sistema.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-013 Notificação por e-mail ao concluir cadastro com e-mail informado
- **Descrição:** cobre C13 — confirma o envio de notificação ao cidadão quando um e-mail é informado no cadastro rápido de Pessoa Física.
- **Precondição:** cadastro rápido de Pessoa Física concluído com e-mail preenchido.
- **Passos:** 1. Ação: concluir o cadastro da pessoa física com e-mail informado | Resultado esperado: o cidadão recebe uma notificação por e-mail com as instruções para completar seu cadastro
- **Pós-condição:** notificação registrada/enviada.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-014 Falha na consulta de CPF
- **Descrição:** cobre C14 — confirma o tratamento de erro quando o CPF é inválido ou a API não retorna os dados necessários.
- **Precondição:** CPF inválido informado, ou API indisponível/sem retorno.
- **Passos:** 1. Ação: processar a consulta | Resultado esperado: o sistema impede a conclusão do cadastro e apresenta uma mensagem de erro adequada
- **Pós-condição:** nenhum cadastro criado; dados preenchidos preservados no formulário.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-015 Campos do formulário de Pessoa Jurídica
- **Descrição:** cobre C15 — confirma os campos apresentados no formulário de Pessoa Jurídica, incluindo o campo E-mail (adicionado em 01/10/2026, ver SGV-11958).
- **Precondição:** opção Pessoa Jurídica selecionada.
- **Passos:** 1. Ação: exibir o formulário | Resultado esperado: são apresentados os campos CNPJ, Razão Social, Nome fantasia, Telefone, E-mail, CPF do responsável legal e Nome do responsável legal (7 campos), sem campo adicional não previsto
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-016 Estado inicial dos campos de Pessoa Jurídica
- **Descrição:** cobre C16 — confirma o estado inicial do formulário antes de qualquer CNPJ válido consultado.
- **Precondição:** formulário de Pessoa Jurídica aberto, nenhum CNPJ consultado ainda.
- **Passos:** 1. Ação: abrir o formulário sem consultar um CNPJ válido | Resultado esperado: os campos Razão Social e Nome fantasia permanecem desabilitados
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-017 Validação do CNPJ antes da consulta à API
- **Descrição:** cobre C17 — confirma que o CNPJ é validado no front antes de qualquer chamada à API.
- **Precondição:** formulário de Pessoa Jurídica aberto.
- **Passos:** 1. Ação: informar um CNPJ e submeter à consulta | Resultado esperado: o sistema valida o CNPJ antes de consultar a API; CNPJ com formato/dígito verificador inválido não dispara chamada à API
- **Pós-condição:** nenhuma consulta realizada para CNPJ inválido.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-018 Preenchimento automático de Razão Social e Nome fantasia
- **Descrição:** cobre C18 — confirma o preenchimento automático quando a API retorna dados de um CNPJ válido.
- **Precondição:** CNPJ válido informado e submetido à consulta.
- **Passos:** 1. Ação: a API retornar os dados correspondentes | Resultado esperado: o sistema preenche automaticamente a Razão Social e o Nome fantasia com os dados retornados
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-019 Habilitação do Nome fantasia para edição
- **Descrição:** cobre C19 — confirma que, após o preenchimento automático, o Nome fantasia fica editável enquanto a Razão Social permanece bloqueada.
- **Precondição:** Razão Social e Nome fantasia preenchidos automaticamente (CT-018).
- **Passos:** 1. Ação: o Nome fantasia é preenchido | Resultado esperado: o campo fica habilitado para edição, enquanto a Razão Social permanece desabilitada
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-020 Conclusão do cadastro de Pessoa Jurídica sem campos opcionais
- **Descrição:** cobre C20 — confirma que o cadastro é concluído sem Telefone ou CPF do responsável legal.
- **Precondição:** CNPJ válido consultado, Razão Social/Nome fantasia preenchidos.
- **Passos:** 1. Ação: concluir o formulário sem informar Telefone ou CPF do responsável legal | Resultado esperado: o sistema permite a conclusão do cadastro com sucesso mesmo com os dois campos opcionais vazios
- **Pós-condição:** pessoa jurídica cadastrada no sistema.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-021 Validação do CPF do responsável legal
- **Descrição:** cobre C21 — confirma a validação e consulta do CPF do responsável legal.
- **Precondição:** formulário de Pessoa Jurídica aberto, CNPJ já validado.
- **Passos:** 1. Ação: informar o CPF do responsável legal | Resultado esperado: o sistema valida o CPF e consulta o nome correspondente na API, mesma regra do CPF de Pessoa Física
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-022 Preenchimento automático do Nome do responsável legal
- **Descrição:** cobre C22 — confirma o preenchimento automático do nome do responsável legal via API.
- **Precondição:** CPF válido do responsável legal consultado (CT-021).
- **Passos:** 1. Ação: a API retornar os dados | Resultado esperado: o sistema preenche automaticamente o Nome do responsável legal, mantendo o campo desabilitado para edição
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-023 Falha na consulta do CPF do responsável legal
- **Descrição:** cobre C23 — confirma o tratamento de erro quando o CPF do responsável legal é inválido ou a API não retorna o nome.
- **Precondição:** CPF do responsável legal informado.
- **Passos:** 1. Ação: processar a consulta (CPF inválido ou API sem retorno do nome) | Resultado esperado: o sistema impede a conclusão do cadastro e apresenta uma mensagem de erro específica ao campo do responsável legal
- **Pós-condição:** nenhum cadastro criado; dados preenchidos preservados.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-024 Falha na consulta do CNPJ
- **Descrição:** cobre C24 — confirma o tratamento de erro quando o CNPJ é inválido ou a API não retorna os dados obrigatórios.
- **Precondição:** CNPJ inválido informado, ou API indisponível/sem retorno.
- **Passos:** 1. Ação: processar a consulta | Resultado esperado: o sistema impede a conclusão do cadastro e apresenta uma mensagem de erro adequada
- **Pós-condição:** nenhum cadastro criado; dados preenchidos preservados.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-025 Campos do formulário de Departamento
- **Descrição:** cobre C25 — confirma os campos apresentados no formulário de Departamento.
- **Precondição:** opção Departamento selecionada.
- **Passos:** 1. Ação: exibir o formulário | Resultado esperado: são apresentados o seletor de Pessoa Jurídica, o Nome do departamento e o E-mail (3 campos), sem campo adicional não previsto
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-026 Obrigatoriedade dos campos de Departamento
- **Descrição:** cobre C26 — confirma que todos os campos do formulário de Departamento são obrigatórios.
- **Precondição:** formulário de Departamento aberto.
- **Passos:** 1. Ação: tentar concluir o cadastro com algum campo vazio | Resultado esperado: o sistema exige o preenchimento de todos os campos, bloqueando a confirmação até estarem completos
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-027 Seletor de PJ lista somente cadastro completo
- **Descrição:** cobre C27 — confirma que o seletor de Pessoa Jurídica só lista PJs com cadastro completo.
- **Precondição:** existem PJs com cadastro completo e incompleto no sistema.
- **Passos:** 1. Ação: abrir o seletor de Pessoa Jurídica | Resultado esperado: o sistema lista somente pessoas jurídicas com cadastro completo; PJ com cadastro incompleto não aparece na lista
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-028 Identificação da PJ com Nome fantasia no seletor
- **Descrição:** cobre C28 — confirma a apresentação da PJ no seletor quando ela possui Nome fantasia.
- **Precondição:** PJ com Nome fantasia cadastrado, disponível no seletor.
- **Passos:** 1. Ação: exibir a PJ no seletor | Resultado esperado: a opção apresenta o Nome fantasia e o CNPJ ("Nome fantasia — CNPJ", conforme o Figma)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-029 Identificação da PJ sem Nome fantasia no seletor
- **Descrição:** cobre C29 — confirma a apresentação da PJ no seletor quando ela não possui Nome fantasia. Comportamento confirmado correto em 01/10/2026 (achado de validação real era [[../SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-027|CT-027]], cadastro incompleto — ver SGV-11957, descartado).
- **Precondição:** PJ sem Nome fantasia cadastrado, disponível no seletor.
- **Passos:** 1. Ação: exibir a PJ no seletor | Resultado esperado: a opção apresenta a Razão Social e o CNPJ ("Razão Social — CNPJ", conforme o Figma)
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-030 Bloqueio de departamento com nome duplicado
- **Descrição:** cobre C30 — confirma o bloqueio de criação de departamento com nome já existente na mesma pessoa jurídica.
- **Precondição:** pessoa jurídica selecionada já possui um departamento com determinado nome.
- **Passos:** 1. Ação: tentar concluir o cadastro com o mesmo nome já existente | Resultado esperado: o sistema impede a criação e informa a duplicidade de nome
- **Pós-condição:** nenhum departamento criado.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-031 Bloqueio de departamento com e-mail duplicado
- **Descrição:** cobre C31 — confirma o bloqueio de criação de departamento com e-mail já existente na mesma pessoa jurídica.
- **Precondição:** pessoa jurídica selecionada já possui um departamento com determinado e-mail.
- **Passos:** 1. Ação: tentar concluir o cadastro com o mesmo e-mail já existente | Resultado esperado: o sistema impede a criação e informa a duplicidade de e-mail
- **Pós-condição:** nenhum departamento criado.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-032 Notificação de criação do departamento
- **Descrição:** cobre C32 — confirma o envio da notificação já usada no fluxo atual de cadastro de departamento.
- **Precondição:** departamento criado com sucesso pelo cadastro rápido.
- **Passos:** 1. Ação: concluir o cadastro | Resultado esperado: o sistema envia ao e-mail do departamento a mesma notificação utilizada no fluxo atual de cadastro de departamento (conteúdo fora do escopo desta demanda)
- **Pós-condição:** notificação enviada.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-033 Bloqueio de confirmação com dados inválidos, pendentes ou ausentes
- **Descrição:** cobre C33 — confirma o bloqueio transversal de confirmação quando há campo inválido, consulta pendente ou dado obrigatório ausente, em qualquer um dos 3 tipos.
- **Precondição:** formulário de cadastro rápido (qualquer tipo) com campo inválido, consulta ainda em andamento, ou campo obrigatório vazio.
- **Passos:** 1. Ação: tentar confirmar o cadastro | Resultado esperado: o sistema impede a criação e destaca visualmente os campos que precisam de correção
- **Pós-condição:** nenhum cadastro criado.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-034 Bloqueio de cadastro duplicado por CPF ou CNPJ
- **Descrição:** cobre C34 — confirma o bloqueio transversal de duplicidade de CPF (Pessoa Física) ou CNPJ (Pessoa Jurídica) já existente no sistema.
- **Precondição:** já existe cidadão cadastrado com o CPF ou CNPJ que será informado.
- **Passos:** 1. Ação: tentar realizar um novo cadastro com CPF ou CNPJ já existente | Resultado esperado: o sistema impede a duplicidade e informa que o registro já existe (vale para PF e PJ)
- **Pós-condição:** nenhum cadastro duplicado criado.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-035 Falha de comunicação preserva dados preenchidos
- **Descrição:** cobre C35 — confirma que uma falha de comunicação com a API ou no processamento não descarta os dados já preenchidos.
- **Precondição:** formulário de cadastro rápido (qualquer tipo) preenchido, falha simulada na API/processamento.
- **Passos:** 1. Ação: provocar uma falha de comunicação com a API ou no processamento do cadastro | Resultado esperado: o sistema preserva os dados preenchidos e apresenta uma mensagem de erro adequada, sem exigir redigitação
- **Pós-condição:** nenhum cadastro criado; dados preservados no formulário.
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-036 Confirmação e encerramento do formulário ao concluir
- **Descrição:** cobre C36 — confirma que o sistema apresenta confirmação e encerra o formulário ao concluir o cadastro com sucesso.
- **Precondição:** cadastro rápido (qualquer tipo) concluído com sucesso.
- **Passos:** 1. Ação: finalizar a operação com o registro criado com sucesso | Resultado esperado: o sistema apresenta uma mensagem de sucesso e encerra o formulário de cadastro rápido automaticamente
- **Pós-condição:** formulário de cadastro rápido fechado; registro disponível no campo de origem (ver CT-004).
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

### CT-037 Placeholder do campo CNPJ
- **Descrição:** cobre C37 — confirma que o campo CNPJ exibe o placeholder no padrão correto. Achado de validação real (30/09/2026); retestado e aprovado no mesmo dia após correção do defeito SGV-11951.
- **Precondição:** opção Pessoa Jurídica selecionada.
- **Passos:** 1. Ação: exibir o campo CNPJ vazio | Resultado esperado: o placeholder exibido é `XX.XXX.XXX/XXXX-XX`
- **Severidade / Tipo / Automação:** normal / acceptance / is-not-automated
- **Qase id:** `<preenchido depois do --apply>`

## Checklist de envio

- [x] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [x] Projeto e suite confirmados (suite pré-existente ou criada com autorização explícita).
- [x] Campos normalizados e passos separados.
- [x] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados (`dry-run` rodado antes do `--apply`).
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
