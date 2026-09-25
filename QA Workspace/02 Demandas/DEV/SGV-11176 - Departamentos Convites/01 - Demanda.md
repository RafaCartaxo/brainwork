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

# SGV-11176 — Departamentos: Convites

**Ticket de origem:** SGV-11176 (Notion "[Parte 3] Departamentos: Convites", ID 6) · **Protótipo:** Figma referenciado no requisito de origem (conferir ao iniciar o plano de execução)

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
> **Parte 3** de quatro, irmã de [[QA Workspace/02 Demandas/Concluídas/11083/QA/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083 (Parte 1)]], [[QA Workspace/02 Demandas/Concluídas/11184/QA/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184 (Parte 2)]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177 (Parte 4)]] — todas sob a epic [[QA Workspace/02 Demandas/Concluídas/9296/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]].

---

## Problema / contexto

Hoje um departamento só ganha participantes por vínculo manual feito por um servidor, um a um, dentro do cadastro do cidadão PJ (fluxo coberto pela SGV-11083). Não existe forma de convidar alguém a entrar num departamento por conta própria, nem de filtrar a mesa de solicitações do cidadão pelo departamento em que ele atua — quem participa de vários departamentos vê tudo misturado com suas solicitações pessoais.

## Objetivo

Permitir a entrada de participantes em departamentos por link de convite (permanente, do próprio departamento, ou temporário, gerado por um servidor para uma pessoa específica) e permitir que o cidadão filtre suas solicitações por perfil (pessoal ou por departamento).

### Entrega desta capacidade

Um link permanente por departamento (gerado na criação), links temporários gerados por servidor (via lista de cidadãos ou edição do cidadão), o fluxo de entrada no departamento a partir do convite (com ou sem cadastro prévio) e o filtro de solicitações por perfil/departamento na mesa do cidadão.

---

## Decisões de produto

- O link **permanente** do departamento não expira e não tem limite de uso — é a via padrão de convite do próprio departamento, enviada automaticamente no e-mail de criação.
- O link **temporário** só pode ser gerado por um servidor (não pelo próprio departamento) e é sempre direcionado a uma pessoa: aceita **um único cadastro** e expira em **7 dias**, o que vier primeiro.
- Link já utilizado ou expirado nunca permite novo cadastro — a pessoa recebe mensagem informando que o convite não é mais válido.
- Todo convite (permanente ou temporário) persiste **quem gerou** (quando aplicável, o servidor) e, ao ser concluído, **quem se cadastrou** através dele.
- Quem entra por convite (com ou sem cadastro prévio no SOGOV) sempre informa sua **função** no departamento antes de confirmar a entrada — mesmo campo já usado no vínculo manual da SGV-11083.
- O filtro de solicitações abre sempre em **"Perfil pessoal"** por padrão — nunca abre já filtrado por um departamento.

---

## Escopo

- Geração automática do link permanente do departamento na criação, sem expiração nem limite de uso, incluído no e-mail de notificação.
- Geração de link temporário por um servidor, a partir da lista de cidadãos ou da edição de um cidadão, com cópia automática para a área de transferência.
- Validade do link temporário: um cadastro, expira em 7 dias; bloqueio e mensagem quando já usado ou expirado.
- Persistência de quem gerou o convite (servidor) e de quem se cadastrou por ele.
- Fluxo de entrada no departamento pelo convite, para pessoa com ou sem cadastro no SOGOV, informando função e virando participante do departamento.
- Seletor de perfil (pessoal/departamento) na tela de solicitações do cidadão, com filtro aplicado por departamento e valor padrão "Perfil pessoal".

---

## Fora de escopo

- Vínculo manual de participante feito diretamente pelo servidor no cadastro do cidadão PJ (já coberto pela SGV-11083).
- Regras de criação, edição, exclusão e suspensão de departamento (SGV-11083).
- Encaminhamento de documentos/despachos ao departamento (SGV-11184).
- Regras de tramitação/assinatura para membro de departamento como destinatário/signatário direto (SGV-11177).
- Revogação manual de um link já gerado (não mencionado no requisito de origem — ver Pendências de decisão).

---

## Critérios de aceite

- C1. Ao criar um departamento, o sistema gera um link de convite permanente, sem expiração e sem limite de uso. ^c1
- C2. O e-mail de notificação de criação do departamento contém o link permanente. ^c2
- C3. A partir da lista de cidadãos, selecionar "Convidar via link" no menu de um cidadão exige a escolha de um departamento ativo desse cidadão e gera o convite. ^c3
- C4. A partir da edição de um cidadão, selecionar "Convidar via link" em um departamento gera o convite para esse departamento. ^c4
- C5. Ao concluir a geração de um convite pelo servidor, o link é copiado automaticamente para a área de transferência. ^c5
- C6. O link gerado por um servidor aceita apenas um cadastro e expira após 7 dias. ^c6
- C7. Um link já utilizado ou expirado impede o cadastro e informa que o convite não é válido. ^c7
- C8. O convite gerado por um servidor persiste o servidor que o gerou; ao ser usado para concluir um cadastro, passa a persistir também o cidadão cadastrado. ^c8
- C9. Pessoa convidada que já possui cadastro no SOGOV realiza login, informa sua função e confirma a entrada no departamento, virando participante. ^c9
- C10. Pessoa convidada sem cadastro no SOGOV conclui o cadastro, informa sua função e confirma a entrada no departamento, virando participante. ^c10
- C11. O seletor de perfil na tela de solicitações do cidadão abre com o valor padrão "Perfil pessoal". ^c11
- C12. O seletor de perfil lista os CNPJs e os respectivos departamentos do cidadão, conforme o Figma. ^c12
- C13. Selecionar um departamento no seletor filtra a tela para exibir apenas as solicitações relacionadas a esse departamento. ^c13
- C14. Selecionar "Perfil pessoal" exibe todas as solicitações do cidadão. ^c14

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Requisito de origem não menciona revogação/desativação manual de um convite já gerado (nem permanente, nem temporário) — confirmar se fica fora de escopo mesmo ou se foi só omissão do documento.
- Confirmar `projeto`, `prioridade` e `pontos_alocados` antes de rotear a demanda para o DEV.
