---
prioridade: media
status: analise
tipo: funcionalidade
etapa_atual: "QA · Casos de teste"
modulo: servicos-pj
plano: ""
execucao: ""
ambiente: dev
origem: repo
projeto: ""
pai: ""
data_inicio: "2026-09-25"
data_fim: ""
responsavel: ""
pontos_alocados: ""
---

# SGV-11177 — Departamentos: Tramitação e assinaturas

**Ticket de origem:** SGV-11177 (Notion "[Parte 4] Departamentos: Tramitação e assinaturas", ID 9) · **Protótipo:** Figma referenciado no requisito de origem (6 pontos específicos ainda a confirmar — ver Pendências de decisão)

> [!info]- Navegação QA/DEV  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da demanda  
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual  
> **Próximo passo:** confirmar `projeto`/`pontos_alocados` antes de rotear para o DEV.

> [!info] Epic  
> **Parte 4** de quatro, irmã de [[QA Workspace/02 Demandas/Concluídas/11083/QA/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083 (Parte 1)]], [[QA Workspace/02 Demandas/Concluídas/11184/QA/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184 (Parte 2)]] e [[QA Workspace/02 Demandas/DEV/SGV-11176 - Departamentos Convites/01 - Demanda|SGV-11176 (Parte 3)]] — todas sob a epic [[QA Workspace/02 Demandas/Concluídas/9296/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]].
>
> Este requisito confirma o que o [[QA Workspace/02 Demandas/Concluídas/9296/Conhecimento/Complemento Figma - Departamento Destinatário E Signatário|Complemento Figma]] já tinha antecipado em 03/09/2026 como escopo futuro: seleção de membro de departamento como destinatário direto (aqui RF01-04) e departamento/membro como signatário de assinatura (aqui RF05-06), com a mesma string de exibição e a mesma regra de token bloqueado/liberado.

---

## Problema / contexto

Hoje a tramitação e a assinatura de documentos só reconhecem um departamento como unidade inteira (destinatário do encaminhamento, coberto pela SGV-11184) — não é possível direcionar uma tramitação ou uma solicitação de assinatura a uma **pessoa específica** dentro do departamento, nem solicitar assinatura ao departamento como um todo (qualquer membro apto assina). Além disso, pessoas que ainda não são membros do departamento, ou nem possuem cadastro no SOGOV, não têm caminho para assinar um documento que chega até elas por um convite de assinatura.

## Objetivo

Permitir a tramitação e a solicitação de assinatura direcionadas a um membro específico de um departamento (com identificação e notificação próprias) e ao departamento como um todo (qualquer membro apto assina), incluindo o fluxo de identificação e pré-cadastro para quem assina externamente sem vínculo ou cadastro prévio.

### Entrega desta capacidade

Busca e seleção de membro de departamento como destinatário de tramitação; notificações e exibição (tela e PDF) desse membro; solicitação de assinatura ao departamento inteiro (token bloqueado) e a um membro específico (token liberado); e o fluxo externo de assinatura por CPF, com pré-cadastro quando necessário.

---

## Decisões de produto

- Buscar por cidadão PJ passa a retornar, além dos departamentos correspondentes, os **cidadãos membros** desses departamentos — resultado de departamento e de membro precisam ser visualmente distinguíveis (padrão a confirmar no Figma).
- Selecionar um membro numa tramitação o adiciona **vinculado ao respectivo departamento** — não é um destinatário solto, sem contexto de departamento.
- Notificação de tramitação para um membro sempre soma dois destinos: o **membro** (e-mail + notificação interna) e o **e-mail do departamento**, que continua recebendo mesmo quando o alvo é uma pessoa específica.
- Identificação de membro de departamento (em tela e em PDF) segue sempre o padrão `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`.
- Assinatura solicitada ao **departamento inteiro**: qualquer membro apto pode assinar; validação por **token é bloqueada** nesse caso.
- Assinatura solicitada a um **membro específico** do departamento: validação por **token é liberada**.
- Notificação de solicitação de assinatura também soma dois destinos quando o alvo é um membro: o **membro** e o **e-mail do departamento**; quando o alvo é o departamento inteiro, só o **e-mail do departamento**.
- Fluxo de assinatura externa por CPF: pessoa cadastrada e já vinculada ao departamento assina só com senha; pessoa cadastrada mas **não vinculada** informa cargo e é vinculada antes de assinar; pessoa **sem cadastro** faz um pré-cadastro (CPF, e-mail, cargo, aceite de termos e declaração de maioridade), assina no mesmo fluxo e recebe depois um e-mail convidando a completar o cadastro no SOGOV.
- Nenhuma inconsistência de identificação/vínculo/pré-cadastro pode gerar vínculo ou cadastro duplicado — o sistema bloqueia a assinatura e mostra mensagem de erro adequada.

---

## Escopo

- Busca de cidadãos PJ retornando departamentos e membros, com distinção visual entre os dois tipos de resultado.
- Seleção de um membro de departamento como destinatário de tramitação, vinculado ao departamento.
- Notificações (membro + e-mail do departamento) e exibição padronizada do membro em tela e em PDF.
- Solicitação de assinatura ao departamento inteiro (token bloqueado, qualquer membro apto assina) e a um membro específico (token liberado).
- Header e eventos do componente de assinatura identificando corretamente departamento ou membro, conforme o alvo.
- Fluxo de assinatura externa por CPF: identificação, vínculo de pessoa cadastrada sem vínculo, pré-cadastro de pessoa sem cadastro (com termos e maioridade), assinatura no mesmo fluxo, e e-mail de convite para completar o cadastro.
- Tratamento de erro sem duplicar vínculo ou cadastro em qualquer etapa do fluxo externo.

---

## Fora de escopo

- Encaminhamento de documento/despacho ao departamento como destinatário único (já coberto pela SGV-11184).
- Entrada de participante no departamento por convite/link (SGV-11176) — aqui o membro já é participante existente do departamento.
- Regras de criação, edição, exclusão e suspensão de departamento (SGV-11083).
- Revogação de uma solicitação de assinatura já enviada (não mencionado no requisito de origem).
- Definição visual exata dos componentes (cores, ícones, espaçamento) — os CTs verificam o comportamento e a presença do padrão, não a medida de handoff (ver Pendências de decisão para os pontos que dependem de conferência direta no Figma).

---

## Critérios de aceite

### Tramitação para membro de departamento

- C1. Uma busca em campo de cidadão PJ lista, além dos departamentos correspondentes, os cidadãos membros desses departamentos que casam com a busca. ^c1
- C2. O resultado da busca permite distinguir visualmente um departamento de um membro, conforme o padrão do Figma. ^c2
- C3. Selecionar um membro exibido no resultado o adiciona à tramitação, vinculado ao respectivo departamento. ^c3
- C4. Um membro de departamento adicionado a uma tramitação é notificado por e-mail e por notificação interna quando a tramitação é efetivada. ^c4
- C5. O e-mail do departamento também recebe a notificação quando um membro seu é adicionado a uma tramitação. ^c5
- C6. O conteúdo e a apresentação das notificações de tramitação para membro de departamento seguem o padrão do Figma. ^c6
- C7. A identificação do membro de departamento na tramitação segue o padrão `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`. ^c7
- C8. O padrão de identificação do membro é aplicado de forma consistente em todos os componentes da tramitação onde ele aparece. ^c8
- C9. A identificação do membro de departamento em um PDF gerado a partir da tramitação segue o mesmo padrão de exibição. ^c9
- C10. Um campo do tipo pessoa preenchido com um membro de departamento aplica o mesmo padrão de identificação quando o PDF correspondente é gerado. ^c10

### Assinatura para departamento

- C11. Pesquisar e selecionar um departamento numa solicitação de assinatura o adiciona como signatário. ^c11
- C12. Quando o signatário é um departamento, qualquer membro apto desse departamento consegue realizar a assinatura. ^c12
- C13. Quando o signatário selecionado é um departamento, o sistema não permite configurar a solicitação de assinatura via token. ^c13
- C14. O header do componente signatário segue o padrão do Figma quando o signatário é um departamento. ^c14
- C15. O componente de eventos de assinatura identifica corretamente o departamento, conforme o Figma. ^c15
- C16. Uma assinatura solicitada a um departamento notifica o e-mail do departamento na criação da solicitação. ^c16

### Assinatura para membro de departamento

- C17. Pesquisar e selecionar um membro de departamento numa solicitação de assinatura o adiciona como signatário, vinculado ao respectivo departamento. ^c17
- C18. Quando o signatário selecionado é um membro de departamento, o sistema permite configurar a solicitação de assinatura via token. ^c18
- C19. O header do componente signatário identifica corretamente o membro e o departamento, conforme o Figma. ^c19
- C20. O componente de eventos de assinatura identifica corretamente o membro e o departamento, conforme o Figma. ^c20
- C21. Uma assinatura solicitada a um membro de departamento notifica esse membro por e-mail e por notificação interna. ^c21
- C22. O e-mail do departamento também recebe a notificação quando um membro seu é signatário de uma solicitação de assinatura. ^c22

### Fluxo de assinatura para usuário externo

- C23. O fluxo externo de identificação solicita o CPF e verifica se existe cadastro correspondente. ^c23
- C24. Pessoa com CPF já cadastrado e vinculado ao departamento destinatário informa a senha e realiza a assinatura. ^c24
- C25. Pessoa com CPF cadastrado mas ainda não vinculada ao departamento destinatário informa o cargo, é vinculada ao departamento e realiza a assinatura. ^c25
- C26. Pessoa sem cadastro para o CPF informado é levada ao pré-cadastro, informando CPF, e-mail e cargo. ^c26
- C27. No pré-cadastro, a pessoa precisa aceitar os termos aplicáveis e declarar ser maior de idade, no modal definido no Figma. ^c27
- C28. Ao confirmar dados válidos e os consentimentos obrigatórios, o sistema cria o pré-cadastro e vincula a pessoa ao departamento com o cargo informado. ^c28
- C29. Concluído o pré-cadastro e criado o vínculo, a pessoa realiza a assinatura no mesmo fluxo, sem etapa adicional. ^c29
- C30. Depois de assinar por meio de um pré-cadastro, a pessoa recebe um e-mail com instruções para completar o cadastro no SOGOV. ^c30
- C31. Qualquer inconsistência na identificação, autenticação, vinculação ou criação do pré-cadastro impede a assinatura e mostra mensagem de erro adequada, sem criar vínculos ou cadastros duplicados. ^c31

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

O requisito de origem lista 6 pontos que dependem de conferência direta no Figma antes de fechar o detalhe visual/textual exato (o comportamento funcional já está descrito e coberto pelos CTs; o que falta é o padrão visual/textual fino):

- Padrão visual dos resultados de busca de departamentos e membros (C2).
- Conteúdo e apresentação das notificações (C6, C16, C21, C22).
- Aplicação do padrão de identificação nas telas e nos PDFs (C7, C8, C9, C10).
- Headers dos componentes de signatário para departamento e membro (C14, C19).
- Apresentação dos eventos de assinatura (C15, C20).
- Modal de pré-cadastro, aceite dos termos e declaração de maioridade (C27).

Confirmar `projeto`, `prioridade` e `pontos_alocados` antes de rotear a demanda para o DEV.
