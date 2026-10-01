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
data_inicio: "2026-09-30"
data_fim: ""
responsavel: ""
pontos_alocados: ""
---

# SGV-11178 — Departamentos: Cadastro rápido

**Ticket de origem:** SGV-11178 (Notion "[Parte 5] Departamentos: Cadastro rápido", ID 10) · **Protótipo:** Figma referenciado no requisito de origem (conferir ao iniciar o plano de execução)

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
> **Parte 5** de cinco, irmã de [[QA Workspace/02 Demandas/Concluídas/11083/QA/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083 (Parte 1)]], [[QA Workspace/02 Demandas/Concluídas/11184/QA/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184 (Parte 2)]], [[QA Workspace/02 Demandas/DEV/SGV-11176 - Departamentos Convites/01 - Demanda|SGV-11176 (Parte 3)]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177 (Parte 4)]] — todas sob a epic [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]].

---

## Problema / contexto

Hoje o cadastro de pessoa física, pessoa jurídica e departamento só acontece em telas dedicadas, fora do fluxo em que o servidor está trabalhando. Quando o servidor precisa referenciar alguém que ainda não existe no sistema — como solicitante, destinatário de despacho, signatário ou membro de departamento — ele precisa interromper o que está fazendo, ir cadastrar a pessoa/departamento em outro lugar e depois voltar para concluir a ação original. Isso já foi identificado como lacuna concreta em [[QA Workspace/02 Demandas/DEV/SGV-11926 - Bug Campo De Solicitante Desatualizado|SGV-11926]] (campo de solicitante na criação de documento usa componente antigo, sem esse atalho).

## Objetivo

Permitir que servidores realizem o cadastro rápido de cidadãos (PF e PJ) e de departamentos diretamente nos campos e componentes de seleção de pessoas, sem interromper o fluxo em andamento.

### Entrega desta capacidade

Um atalho de cadastro rápido disponível nos componentes de seleção de pessoa (campo solicitante, campo do tipo pessoa PF/PJ, destinatário de despacho, seleção de signatário), com um formulário único que alterna entre Pessoa Física, Pessoa Jurídica e Departamento por um seletor, preservando dados entre as trocas, com validação de CPF/CNPJ via API e seleção automática do registro criado no campo de origem.

---

## Decisões de produto

- O atalho de cadastro rápido é oferecido de forma **consistente** em todo componente de seleção de pessoa que já permita adicionar um cidadão — não é exclusivo de um fluxo específico.
- O formulário alterna entre **Pessoa Física, Pessoa Jurídica e Departamento** por um seletor do tipo radio button; só o formulário do tipo ativo é exibido, e os dados de cada tipo são preservados enquanto o cadastro rápido estiver aberto (mesmo trocando de tipo e voltando).
- **Pessoa Física:** CPF, Nome, E-mail e Telefone. Nome só é preenchido (automaticamente, via API) após CPF válido consultado — e fica desabilitado para edição. E-mail e Telefone são opcionais; quando o e-mail é informado, o cidadão recebe notificação para completar o cadastro.
- **Pessoa Jurídica:** CNPJ, Razão Social, Nome fantasia, Telefone, CPF e Nome do responsável legal. Razão Social e Nome fantasia só são preenchidos (via API) após CNPJ válido consultado. Razão Social fica desabilitada; Nome fantasia fica habilitado pra edição depois de preenchido. Telefone e CPF do responsável legal são opcionais; quando o CPF do responsável é informado, o Nome do responsável é validado e preenchido via API, desabilitado para edição.
- **Departamento:** seletor de Pessoa Jurídica (só PJs com cadastro completo), Nome do departamento e E-mail — todos obrigatórios. Nome ou e-mail duplicado na mesma PJ bloqueia a criação. Notificação de criação é a mesma já usada no fluxo atual de cadastro de departamento (fora desta capacidade).
- Ao concluir qualquer um dos três cadastros com sucesso, o **registro criado fica selecionado automaticamente** no campo de origem, desde que compatível com os parâmetros desse campo (ex.: campo parametrizado só para PF não seleciona um PJ recém-criado).
- Toda consulta de CPF/CNPJ é **validada no front antes de ir para a API** — API só é chamada com formato válido. Falha da API (documento não encontrado, indisponibilidade) impede a conclusão do cadastro e mostra erro, sem derrubar os dados já preenchidos.
- Cadastro duplicado (CPF/CNPJ já existente) é sempre bloqueado, com mensagem informando que o registro já existe — vale para os três tipos.

---

## Escopo

- Atalho de cadastro rápido nos componentes de seleção de pessoa: campo solicitante, campo do tipo pessoa PF/PJ, destinatário de despacho, seleção de signatário.
- Formulário único com seletor de tipo (PF/PJ/Departamento), um tipo visível por vez, dados preservados entre trocas.
- Cadastro rápido de Pessoa Física: campos, validação de CPF, preenchimento automático de Nome, notificação por e-mail quando aplicável, tratamento de falha.
- Cadastro rápido de Pessoa Jurídica: campos, validação de CNPJ, preenchimento automático de Razão Social/Nome fantasia, validação do CPF do responsável legal, tratamento de falha.
- Cadastro rápido de Departamento: campos, obrigatoriedade, seletor de PJs com cadastro completo, identificação por Nome fantasia ou Razão Social, bloqueio de nome/e-mail duplicado, notificação existente.
- Validações transversais: bloqueio de confirmação com dados inválidos/pendentes/ausentes, bloqueio de duplicidade de CPF/CNPJ, tratamento de falha de comunicação preservando dados, confirmação e encerramento do formulário ao concluir.

---

## Fora de escopo

- Fluxo completo de cadastro dedicado (fora do atalho) para PF, PJ ou Departamento — este requisito cobre só o atalho embutido nos componentes de seleção.
- Regras de criação, edição, exclusão e suspensão de departamento além do cadastro em si (já cobertas por [[QA Workspace/02 Demandas/Concluídas/11083/QA/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083]]).
- Entrada em departamento por convite ([[QA Workspace/02 Demandas/DEV/SGV-11176 - Departamentos Convites/01 - Demanda|SGV-11176]]) e tramitação/assinatura direcionada a membro/departamento ([[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]).
- Revisão do componente legado apontado pela [[QA Workspace/02 Demandas/DEV/SGV-11926 - Bug Campo De Solicitante Desatualizado|SGV-11926]] além da adição do atalho em si (a SGV-11926 registra a lacuna; esta demanda entrega a capacidade que a fecha).
- Conteúdo exato dos e-mails de notificação (PF e Departamento) — usa o texto já existente/definido em outro lugar (ver Pendências de decisão).

---

## Critérios de aceite

### RF01 — Acesso ao cadastro rápido

- C1. Todo campo do tipo pessoa ou componente de seleção de usuário que permita adicionar um cidadão disponibiliza um atalho para o cadastro rápido. ^c1
- C2. O atalho é oferecido de forma consistente nos contextos: campo solicitante, campo do tipo pessoa parametrizado para PF ou PJ, destinatário de despacho e seleção de signatário. ^c2
- C3. Ao acionar o atalho, o formulário exibido permite escolher entre Pessoa Física, Pessoa Jurídica e Departamento. ^c3
- C4. Ao concluir o cadastro rápido com sucesso, o novo registro fica disponível e selecionado no campo de origem, desde que compatível com os parâmetros desse campo. ^c4

### RF02 — Navegação entre os formulários

- C5. O formulário de cadastro rápido apresenta um seletor do tipo radio button com as opções Pessoa Física, Pessoa Jurídica e Departamento. ^c5
- C6. Apenas o formulário do tipo selecionado é exibido por vez. ^c6
- C7. Dados preenchidos parcial ou totalmente em um formulário permanecem ao alternar para outro tipo e voltar, enquanto o cadastro rápido estiver aberto. ^c7

### RF03 — Cadastro rápido de pessoa física

- C8. O formulário de Pessoa Física apresenta os campos CPF, Nome, E-mail e Telefone. ^c8
- C9. Antes de consultar um CPF válido, o campo Nome permanece desabilitado e os campos E-mail e Telefone são opcionais. ^c9
- C10. O sistema valida o CPF informado antes de consultar a API. ^c10
- C11. Quando a API retorna os dados de um CPF válido, o Nome é preenchido automaticamente e permanece desabilitado para edição. ^c11
- C12. O cadastro de Pessoa Física é criado ao confirmar o formulário com CPF e Nome validados, independentemente do preenchimento de E-mail ou Telefone. ^c12
- C13. Quando um e-mail é informado, o cidadão recebe uma notificação por e-mail com instruções para completar o cadastro, ao concluir o cadastro rápido de pessoa física. ^c13
- C14. Quando o CPF é inválido ou a API não retorna os dados necessários, o sistema impede a conclusão do cadastro e apresenta mensagem de erro adequada. ^c14

### RF04 — Cadastro rápido de pessoa jurídica

- C15. O formulário de Pessoa Jurídica apresenta os campos CNPJ, Razão Social, Nome fantasia, Telefone, E-mail, CPF do responsável legal e Nome do responsável legal. ^c15
- C16. Antes de consultar um CNPJ válido, os campos Razão Social e Nome fantasia permanecem desabilitados. ^c16
- C17. O sistema valida o CNPJ informado antes de consultar a API. ^c17
- C18. Quando a API retorna os dados de um CNPJ válido, Razão Social e Nome fantasia são preenchidos automaticamente. ^c18
- C19. Após o preenchimento automático, o Nome fantasia fica habilitado para edição, enquanto a Razão Social permanece desabilitada. ^c19
- C20. O sistema permite concluir o cadastro de Pessoa Jurídica sem o preenchimento de Telefone ou CPF do responsável legal. ^c20
- C21. Quando o CPF do responsável legal é informado, o sistema valida o CPF e consulta o nome correspondente na API. ^c21
- C22. Quando a API retorna os dados do CPF válido do responsável legal, o Nome do responsável legal é preenchido automaticamente e permanece desabilitado para edição. ^c22
- C23. Quando o CPF do responsável legal é inválido ou a API não retorna o nome, o sistema impede a conclusão do cadastro e apresenta mensagem de erro adequada. ^c23
- C24. Quando o CNPJ é inválido ou a API não retorna os dados obrigatórios, o sistema impede a conclusão do cadastro e apresenta mensagem de erro adequada. ^c24
- C37. O campo CNPJ exibe o placeholder `XX.XXX.XXX/XXXX-XX`. *(achado durante validação real em 30/09/2026 — numeração fora de sequência pra não quebrar os anchors de C25 em diante.)* ^c37

### RF05 — Cadastro rápido de departamento

- C25. O formulário de Departamento apresenta o seletor de Pessoa Jurídica, o Nome do departamento e o E-mail. ^c25
- C26. O sistema exige o preenchimento de todos os campos do formulário de Departamento para concluir o cadastro. ^c26
- C27. O seletor de Pessoa Jurídica lista somente pessoas jurídicas com cadastro completo. ^c27
- C28. Quando a pessoa jurídica possui Nome fantasia cadastrado, a opção no seletor apresenta o Nome fantasia e o CNPJ. ^c28
- C29. Quando a pessoa jurídica não possui Nome fantasia, a opção no seletor apresenta a Razão Social e o CNPJ. ^c29
- C30. O sistema impede a criação de um departamento com o mesmo nome de outro já existente na mesma pessoa jurídica, informando a duplicidade. ^c30
- C31. O sistema impede a criação de um departamento com o mesmo e-mail de outro já existente na mesma pessoa jurídica, informando a duplicidade. ^c31
- C32. Ao criar o departamento com sucesso, o sistema envia ao e-mail do departamento a mesma notificação já utilizada no fluxo atual de cadastro de departamento. ^c32

### RF06 — Validações e consistência do cadastro rápido

- C33. O sistema impede a confirmação do cadastro quando existem campos inválidos, consultas pendentes ou dados obrigatórios ausentes, destacando os campos a corrigir. ^c33
- C34. O sistema impede um novo cadastro quando já existe cidadão com o CPF ou CNPJ informado, informando que o registro já existe. ^c34
- C35. Quando ocorre falha de comunicação com a API ou no processamento do cadastro, o sistema preserva os dados preenchidos e apresenta mensagem de erro adequada. ^c35
- C36. Ao criar o registro com sucesso, o sistema apresenta uma confirmação e encerra o formulário de cadastro rápido. ^c36

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Requisito de origem não traz o conteúdo exato do e-mail de conclusão de cadastro de Pessoa Física (CA06/C13) — confirmar texto/template antes da implementação.
- Confirmar no Figma (ver "Pontos para validação" do requisito de origem): localização/apresentação do atalho em cada componente, layout do formulário e do seletor, quais campos além de PF/PJ permitem cadastro rápido de Departamento, gatilho das consultas às APIs (saída do campo, ação manual ou tempo de espera), tratamento quando a API não retorna Nome/Razão Social/Nome fantasia, formato/validação de E-mail e Telefone, se a checagem de nome/e-mail duplicado de departamento ignora maiúsculas/acentos/espaços, e se o registro criado deve sempre ser selecionado automaticamente em todos os componentes de origem.
- Confirmar `projeto`, `prioridade` e `pontos_alocados` antes de rotear a demanda para o DEV.

> [!bug] Defeitos confirmados em validação real (30/09/2026)
> - **C37** (placeholder do campo CNPJ, criado a partir deste achado) — [[Defeitos/SGV-11951 - Defeito Placeholder Campo CNPJ Incorreto|SGV-11951]].
> - **C29** (seletor não traz nenhuma opção pra PJ sem Nome fantasia, em vez do fallback Razão Social + CNPJ) — [[Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]]. **Descartado em 01/10/2026** — diagnóstico errado: CT-029 já funcionava certo, o achado real era [[03 - Casos de teste#^ct-027|CT-027]] (cadastro incompleto).
> - **C15** (formulário de PJ ainda não coleta e-mail, exigido pelo critério atualizado em 01/10/2026) — [[Defeitos/SGV-11958 - Defeito Formulário De Pessoa Jurídica Não Coleta E-mail|SGV-11958]].
