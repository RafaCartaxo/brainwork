---
prioridade: media
origem: repo
pontos_alocados: ""
---

# SGV-11083 — Departamentos para cidadão Pessoa Jurídica

**Ticket de origem:** SGV-11083 no Notion ("[Parte 1] Departamentos: Criação, edição, exclusão, suspensão e gerenciamento de membros")

> [!info]- Navegação QA/DEV
> **README do card:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** preparar os 33 CTs pra envio na Qase — task já aprovada em DEV (02/10/2026).

---

## Problema / contexto

Nova funcionalidade: departamentos vinculados a cidadãos Pessoa Jurídica (PJ). Um servidor cria departamentos (nome + e-mail únicos por empresa) e vincula participantes (cidadãos do mesmo cliente/instância, cada um com um cargo). A listagem e a visualização de PJ passam a exibir razão social, quantidade de participantes e os departamentos da empresa. Departamentos podem ser excluídos (só se não têm participante nem documento tramitado) ou suspensos (só se não têm pendência) — departamento suspenso não pode ser usado em novas tramitações. Toda ação relevante gera notificação (sistema + e-mail) e registro no histórico do cidadão PJ.

Nasce do refinamento de 3 documentos do Notion (requisito técnico completo, doc de produto consolidado, resumo em formato de QA).

## Objetivo

Servidor consegue criar, gerenciar participantes, consultar, excluir e suspender departamentos de uma Pessoa Jurídica, com todas as regras de obrigatoriedade/duplicidade/notificação/histórico aplicadas.

### Entrega desta capacidade

Grupos A-E abaixo (criação, gerenciamento de participantes, listagem/visualização, exclusão, suspensão). Edição formal de um departamento existente fica fora desta rodada (ver Fora de escopo).

---

## Decisões de produto

- Departamento só existe vinculado a **um** cidadão PJ; uma mesma empresa pode ter vários.
- Nome (até 200 caracteres) e e-mail são obrigatórios e únicos dentro da mesma PJ — mesmo nome/e-mail pode existir em PJs diferentes.
- Participante é um cidadão (PF ou PJ) do mesmo cliente/instância; pode participar de vários departamentos, do mesmo CNPJ ou de CNPJs diferentes. Cargo (até 28 caracteres) é obrigatório por vínculo.
- Departamento pode existir sem participantes — nesse caso a tramitação só permite responder (despacho), não assinar.
- Departamento herda as mesmas regras de visibilidade de módulo/assunto/serviço que já valem para a PJ (não é regra de visibilidade nova).
- Exclusão só é permitida sem participante vinculado e sem documento tramitado; havendo qualquer um dos dois, a única ação disponível é suspender.
- Suspensão só é permitida sem pendência; departamento suspenso não pode ser selecionado em novas tramitações.
- Toda criação, vínculo, desvínculo, exclusão e suspensão gera notificação (sistema + e-mail) e é registrada no histórico do cidadão PJ.

---

## Escopo

- Criação de departamento (grupo A).
- Gerenciamento de participantes — vincular/desvincular (grupo B).
- Listagem e visualização da PJ (razão social, coluna Participantes, departamentos vinculados) (grupo C).
- Exclusão de departamento (grupo D).
- Suspensão de departamento (grupo E).

---

## Fora de escopo

- **Edição formal de um departamento existente** — a task inclui "edição" no título (Notion), mas nem o requisito refinado nem os CTs abaixo têm um grupo dedicado a editar um departamento já criado. Gap exposto pelo defeito [[QA Workspace/02 Demandas/Concluídas/11313/QA/11313 - Defeito Editar Nome Do Departamento Altera Despachos Ja Realizados|SGV-11313]] (corrigido e aprovado em 03/09/2026), por analogia com a edição de nome de **setor** ([[QA Workspace/04 Conhecimento/Módulos/Organograma#Edição de setor ou subsetor|Organograma]]) — segue em aberto decidir se vira grupo formal de CTs aqui.

---

## Critérios de aceite

### A. Criação de departamento
- C1. O sistema não permite criar um departamento para um cidadão do tipo Pessoa Física. ^c1
- C2. Nome do departamento é obrigatório na criação. ^c2
- C3. E-mail do departamento é obrigatório na criação. ^c3
- C4. Nome duplicado é bloqueado dentro da mesma PJ. ^c4
- C5. E-mail duplicado é bloqueado dentro da mesma PJ. ^c5
- C6. Mesmo nome/e-mail é permitido em PJs diferentes. ^c6
- C7. Participante só pode ser um cidadão da mesma instância/cliente. ^c7
- C8. Cargo do participante é obrigatório na criação do departamento. ^c8
- C9. Criação bem-sucedida envia notificação por e-mail com o template previsto no Figma. ^c9
- C10. Criação é registrada no histórico do cidadão PJ. ^c10

### B. Gerenciamento de participantes
- C11. É possível vincular um participante a um departamento existente. ^c11
- C12. Vínculo de participante de outra instância é bloqueado. ^c12
- C13. Cargo é obrigatório ao vincular um participante. ^c13
- C14. É possível desvincular um participante existente. ^c14
- C15. Vínculo gera notificação interna e por e-mail aos envolvidos. ^c15
- C16. Desvínculo gera notificação interna e por e-mail aos envolvidos. ^c16
- C17. Vínculo é registrado no histórico da PJ. ^c17
- C18. Desvínculo é registrado no histórico da PJ. ^c18

### C. Listagem e visualização da PJ
- C19. A coluna "Nome" vira "Razão Social" na listagem de cidadãos PJ. ^c19
- C20. Existe uma coluna "Participantes" na listagem de PJ. ^c20
- C21. A quantidade exibida na coluna "Participantes" reflete a regra definida pelo Produto. *(ponto em aberto — ver Pendências de decisão)* ^c21
- C22. A visualização da PJ lista os departamentos vinculados a ela. ^c22
- C23. A edição da PJ permite criar um novo departamento a partir da seção de departamentos. ^c23

### D. Exclusão de departamento
- C24. É possível excluir um departamento sem participantes vinculados e sem documentos tramitados. ^c24
- C25. Exclusão é bloqueada quando existem participantes vinculados, oferecendo a suspensão como alternativa. ^c25
- C26. Exclusão é bloqueada quando existem documentos tramitados, oferecendo a suspensão como alternativa. ^c26
- C27. A opção de suspensão aparece quando a exclusão é bloqueada. ^c27
- C28. Exclusão é registrada no histórico da PJ. ^c28

### E. Suspensão de departamento
- C29. É possível suspender um departamento sem pendências. ^c29
- C30. Suspensão é bloqueada quando existem pendências, com mensagem explicando o motivo. ^c30
- C31. O status do departamento muda para "Suspenso" após a suspensão. ^c31
- C32. Departamento suspenso não aparece disponível em novas tramitações. ^c32
- C33. Suspensão é registrada no histórico da PJ. ^c33

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- **C21 (contagem da coluna "Participantes")**: se o mesmo cidadão participa de mais de um departamento da mesma empresa, não está definido se a contagem soma vínculos por departamento ou cidadãos únicos. QA aguarda definição do Produto antes de considerar o comportamento aprovado ou bug — CT-021 fica bloqueado até a decisão chegar.
- Documento de produto consolidado ("Departamento CNPJ") cobre 3 tasks diferentes (SGV-8883, 8884, 9898), não só esta — usado aqui só como contexto de apoio, não como fonte de critério de aceite.
- Ainda não existe seção de "Departamentos" em nenhuma doc de módulo (`04 Conhecimento/Módulos/`) — quando esta demanda for validada, abre pendência de criar/atualizar a doc.
- Confirmar `prioridade` e `pontos_alocados` antes de rotear pro DEV.

> [!bug] Gaps de cobertura expostos por defeitos (achados fora de CT formal, já corrigidos)
> - [[QA Workspace/02 Demandas/Concluídas/11313/QA/11313 - Defeito Editar Nome Do Departamento Altera Despachos Ja Realizados|SGV-11313]] (corrigido e aprovado em 03/09/2026) — editar o nome do departamento alterava despachos já realizados; expõe a ausência de um grupo formal de CTs pra edição (ver Fora de escopo). O CT-B02 do próprio defeito (nome novo em despacho futuro) não teve retest explícito.
> - [[QA Workspace/02 Demandas/Concluídas/11273/QA/11273 - Defeito Empresa Vincula A Si Propria Como Participante Do Proprio Departamento|SGV-11273]] (corrigido e aprovado em 03/09/2026) — a própria PJ dona do departamento conseguia se vincular como participante dele mesma; nenhum CT do grupo B testava esse bloqueio de auto-vínculo (CT-012 cobre só instância diferente, regra distinta). Falta decidir se vira CT formal aqui.
