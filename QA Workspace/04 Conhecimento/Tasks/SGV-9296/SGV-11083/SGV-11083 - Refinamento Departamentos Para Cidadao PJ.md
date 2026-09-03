---
tags:
  - qa
  - refinamento
task: "11083"
status: refinado
data_inicio: 2026-09-02
responsavel: Rafael
modulo: servicos-pj
---
# Refinamento: Departamentos para cidadão Pessoa Jurídica

> [!info]- Mesa de trabalho — [[Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada|fluxo 6]]
> Análise e suposição vivem aqui — o card em `02 Demandas/` nasce do **Destilado**, limpo. Ao concluir: análise → Notion (`📤`), card criado (`📝`), este arquivo → `04 Conhecimento/` (`status: refinado`).

## O problema (task no Notion)

**Descrição** — [Parte 1] Departamentos: Criação, edição, exclusão, suspensão e gerenciamento de membros (SGV-11083, backlog "[Dev][Parte 1] Gerenciamento de departamentos").

**Objetivo** — Permitir que servidores gerenciem departamentos vinculados a cidadãos Pessoa Jurídica (PJ): criação, vínculo de participantes, notificações, histórico, exclusão e suspensão.

### RF01 — Criar departamento para cidadão PJ

Como servidor, quero criar departamentos para cidadãos PJ, pra organizar participantes vinculados a uma empresa e usar esses departamentos em fluxos posteriores do SoGov.

Cada departamento é vinculado a **um** cidadão PJ, tem nome e e-mail próprios (sem duplicidade dentro da mesma empresa), e pode ter participantes (cidadãos do mesmo cliente/instância), cada um com um cargo.

**Critérios de aceitação (CA01-CA08, doc original):**
- CA01 — Só permite criar se o cidadão selecionado for PJ (bloqueia PF)
- CA02 — Nome e e-mail são obrigatórios
- CA03 — Não permite dois departamentos com o mesmo nome pra mesma PJ
- CA04 — Não permite dois departamentos com o mesmo e-mail pra mesma PJ
- CA05 — Participantes só podem ser cidadãos do mesmo cliente/instância
- CA06 — Cargo do participante é obrigatório
- CA07 — Notificação por e-mail (template do Figma) após criação
- CA08 — Registro no histórico do cidadão PJ após criação

### RF02 — Vincular e desvincular participantes do departamento

Como servidor, quero vincular e desvincular participantes de um departamento, pra manter atualizada a composição do departamento.

**Critérios de aceitação (CA01-CA07):**
- CA01 — Vincular um cidadão como participante do departamento
- CA02 — Só permite vincular cidadãos do mesmo cliente/instância
- CA03 — Cargo é obrigatório no vínculo
- CA04 — Desvincular um participante existente
- CA05 — Vínculo/desvínculo gera notificação interna
- CA06 — Vínculo/desvínculo gera notificação por e-mail
- CA07 — Vínculo/desvínculo é registrado no histórico do cidadão PJ

### RF03 — Ajustar listagem e visualização de cidadãos PJ

Como servidor, quero ver departamentos e participantes na gestão de cidadãos PJ, pra identificar rápido a estrutura de departamentos de uma empresa.

**Critérios de aceitação (CA01-CA04):**
- CA01 — Coluna "Nome" da listagem de PJ vira "Razão Social"
- CA02 — Nova coluna "Participantes" com a quantidade de cidadãos participantes em departamentos da empresa
- CA03 — Visualização do cidadão PJ lista os departamentos vinculados
- CA04 — Edição do cidadão PJ permite criar novos departamentos

> [!warning] Ponto em aberto — contagem da coluna Participantes (CA02)
> Se o mesmo cidadão participa de mais de um departamento da mesma empresa, não está definido se a contagem soma **vínculos por departamento** ou **cidadãos únicos**. Ver "Pontos a definir" abaixo.

### RF04 — Excluir ou suspender departamento

Como servidor, quero excluir ou suspender departamentos conforme suas condições de uso, pra impedir alteração indevida em departamento que já tem vínculo, documento ou pendência.

**Critérios de aceitação — Exclusão (CA01-CA03):**
- CA01 — Exclusão permitida só quando não há participantes vinculados nem documentos tramitados
- CA02 — Bloqueia exclusão se há participantes vinculados (oferece suspensão)
- CA03 — Bloqueia exclusão se há documentos tramitados (oferece suspensão)

**Critérios de aceitação — Suspensão (CA04-CA06):**
- CA04 — Suspensão permitida quando não há pendências
- CA05 — Bloqueia suspensão se há pendências, com mensagem explicando o motivo
- CA06 — Departamento suspenso não aparece disponível em novas tramitações

Exclusão e suspensão são registradas no histórico do cidadão PJ.

---

## Análise

- **Fonte tripla**: 3 arquivos do Notion pra esta task — o requisito técnico completo (RF01-04 acima, com schema de banco e tarefas de dev removidos daqui por não serem QA), um documento de produto mais amplo ("Departamento CNPJ", que na verdade consolida **outras 3 tasks** — SGV-8883, 8884, 9898 — numa visão única) e um "Resumo da Task" que já condensa tudo em formato de cenário de QA, do jeito que o Rafael pediu.
- **Detalhes extraídos do documento de produto** (não inventados, preenchem lacuna do requisito técnico):
  - Nome do departamento: até 200 caracteres. Cargo do participante: até 28 caracteres.
  - Um participante pode estar em vários departamentos do **mesmo** CNPJ e de CNPJs **diferentes** — não há exclusividade.
  - Departamento **pode existir sem participantes**: nesse caso, a tramitação só permite responder (gera despacho), não assinar.
  - Departamento herda as **mesmas regras de visibilidade de módulo/assunto/serviço** que já valem pra PJ (não é uma regra nova de visibilidade).
  - Participar de um departamento não muda a vida da pessoa como cidadão comum — as demandas pessoais e as do departamento ficam separadas.
- **Ponto do documento de produto que NÃO entra neste refinamento**: há uma pendência "❓ a confirmar" sobre o CNPJ principal receber todas as notificações dos departamentos — mas essa página cobre 3 tasks diferentes, e não há indicação de que essa pendência seja desta SGV-11083 especificamente (parece pertencer ao escopo mais amplo de tramitação/notificação das outras tasks). Não trago pro Destilado por falta de confirmação de que é escopo daqui.

---

## Pontos a definir

- [ ] **Contagem da coluna "Participantes" (CA02 de RF03)**: vínculos por departamento (um cidadão em 2 departamentos da mesma empresa conta 2x) ou cidadãos únicos (conta 1x, independente de quantos departamentos)? O próprio "Resumo da Task" já registra isso como pendente e instrui: **QA aguarda definição do Produto antes de considerar o comportamento aprovado ou bug** — não decidir no CT, só observar e reportar o comportamento real.

---

## Destilado (rascunho do card)

### Descrição

Nova funcionalidade: departamentos vinculados a cidadãos Pessoa Jurídica (PJ). Um servidor cria departamentos (nome + e-mail únicos por empresa) e vincula participantes (cidadãos do mesmo cliente/instância, cada um com um cargo). A listagem e a visualização de PJ passam a exibir razão social, quantidade de participantes e os departamentos da empresa. Departamentos podem ser excluídos (só se não têm participante nem documento tramitado) ou suspensos (só se não têm pendência) — e um departamento suspenso não pode ser usado em novas tramitações. Toda ação relevante gera notificação (sistema + e-mail) e registro no histórico do cidadão PJ.

### Resultado Esperado

- Departamento só é criado pra cidadão PJ, com nome e e-mail obrigatórios e únicos por empresa.
- Participantes só podem ser cidadãos do mesmo cliente/instância, sempre com cargo informado.
- Toda criação/vínculo/desvínculo/exclusão/suspensão gera a notificação e o registro de histórico correspondente.
- Listagem de PJ mostra razão social e quantidade de participantes; visualização de PJ lista os departamentos.
- Exclusão só é permitida sem participante e sem documento tramitado; suspensão só sem pendência; departamento suspenso some das novas tramitações.

### Critérios de aceite

#### A. Criação de departamento
- [ ] Departamento só é criado se o cidadão selecionado for Pessoa Jurídica
- [ ] Nome do departamento é obrigatório
- [ ] E-mail do departamento é obrigatório
- [ ] Não permite dois departamentos com o mesmo nome na mesma PJ
- [ ] Não permite dois departamentos com o mesmo e-mail na mesma PJ
- [ ] Mesmo nome/e-mail pode existir em PJs diferentes
- [ ] Participante só pode ser cidadão do mesmo cliente/instância da PJ
- [ ] Cargo do participante é obrigatório na criação
- [ ] Notificação por e-mail é enviada após a criação do departamento
- [ ] Criação do departamento é registrada no histórico do cidadão PJ

#### B. Gerenciamento de participantes
- [ ] Vincular um cidadão como participante do departamento
- [ ] Bloquear vínculo de cidadão de outra instância
- [ ] Cargo é obrigatório ao vincular participante
- [ ] Desvincular um participante existente
- [ ] Vínculo gera notificação interna e por e-mail
- [ ] Desvínculo gera notificação interna e por e-mail
- [ ] Vínculo é registrado no histórico do cidadão PJ
- [ ] Desvínculo é registrado no histórico do cidadão PJ

#### C. Listagem e visualização da PJ
- [ ] Coluna "Nome" da listagem de PJ é exibida como "Razão Social"
- [ ] Existe a coluna "Participantes" na listagem de PJ
- [ ] ⚠️ Quantidade da coluna "Participantes" bate com a regra definida pelo Produto (vínculos × cidadãos únicos — **aguardando definição**, ver Pontos a definir)
- [ ] Visualização do cidadão PJ lista os departamentos vinculados
- [ ] Edição do cidadão PJ permite criar novo departamento

#### D. Exclusão de departamento
- [ ] Exclui departamento sem participantes e sem documentos tramitados
- [ ] Bloqueia exclusão quando há participantes vinculados (oferece suspensão)
- [ ] Bloqueia exclusão quando há documentos tramitados (oferece suspensão)
- [ ] Opção de suspensão aparece no lugar da exclusão bloqueada
- [ ] Exclusão é registrada no histórico do cidadão PJ

#### E. Suspensão de departamento
- [ ] Suspende departamento sem pendências
- [ ] Bloqueia suspensão quando há pendências, com mensagem explicando o motivo
- [ ] Status do departamento é atualizado pra suspenso
- [ ] Departamento suspenso não aparece disponível em novas tramitações
- [ ] Suspensão é registrada no histórico do cidadão PJ

### Casos de Teste Básicos

Ver seção "## Casos de teste" do card — CTs completos com Dado/Quando/Então, um por critério acima.

---

## Histórico do refinamento

- 2026-09-02 - Material recebido (3 arquivos do Notion: requisito técnico completo, doc de produto consolidado, resumo já em formato de QA)
- 2026-09-02 - Destilado escrito a partir dos 3 documentos cruzados; 1 ponto em aberto identificado (contagem de participantes) e mantido como pendência explícita, não decidido
- 2026-09-02 - 📝 Card criado em [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|02 Demandas/DEV/11083]], com 33 CTs (5 grupos) derivados do Destilado
