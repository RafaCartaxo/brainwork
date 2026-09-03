---
tags:
  - demanda
  - funcionalidade
  - qa
  - servicos-pj
task: "11083"
pai: ""
status: aberto
ambiente: DEV
prioridade: media
data_inicio: 2026-09-02
data_fim: ""
responsavel: Rafael
aguardando: ""
pontos: ""
modulo: servicos-pj
---
# Demanda: [Funcionalidade] Departamentos para cidadão Pessoa Jurídica

> [!info] Informações
> - **Tipo:** Funcionalidade
> - **Responsável QA:** Rafael
> - **Link:** SGV-11083 no Notion ("[Parte 1] Departamentos: Criação, edição, exclusão, suspensão e gerenciamento de membros")
> - **Parte 1** de duas, irmã de [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184 (Parte 2)]] — ambas sob a epic [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-9296 - Índice|SGV-9296]]

---

> [!abstract] Resumo

Nova funcionalidade: departamentos vinculados a cidadãos Pessoa Jurídica (PJ). Um servidor cria departamentos (nome + e-mail únicos por empresa) e vincula participantes (cidadãos do mesmo cliente/instância, cada um com um cargo). A listagem e a visualização de PJ passam a exibir razão social, quantidade de participantes e os departamentos da empresa. Departamentos podem ser excluídos (só se não têm participante nem documento tramitado) ou suspensos (só se não têm pendência) — departamento suspenso não pode ser usado em novas tramitações. Toda ação relevante gera notificação (sistema + e-mail) e registro no histórico do cidadão PJ.

Nasce do refinamento de 3 documentos do Notion (requisito técnico completo, doc de produto consolidado, resumo em formato de QA) — mesa em [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11083/SGV-11083 - Refinamento Departamentos Para Cidadao PJ|04 Conhecimento/Tasks/SGV-11083]].

---

## Regras de negócio

- Departamento só existe vinculado a **um** cidadão PJ; uma mesma empresa pode ter vários.
- Nome (até 200 caracteres) e e-mail são obrigatórios e únicos dentro da mesma PJ — mesmo nome/e-mail pode existir em PJs diferentes.
- Participante é um cidadão (PF ou PJ) do mesmo cliente/instância; pode participar de vários departamentos, do mesmo CNPJ ou de CNPJs diferentes. Cargo (até 28 caracteres) é obrigatório por vínculo.
- Departamento pode existir sem participantes — nesse caso a tramitação só permite responder (despacho), não assinar.
- Departamento herda as mesmas regras de visibilidade de módulo/assunto/serviço que já valem para a PJ (não é regra de visibilidade nova).
- Exclusão só é permitida sem participante vinculado e sem documento tramitado; havendo qualquer um dos dois, a única ação disponível é suspender.
- Suspensão só é permitida sem pendência; departamento suspenso não pode ser selecionado em novas tramitações.
- Toda criação, vínculo, desvínculo, exclusão e suspensão gera notificação (sistema + e-mail) e é registrada no histórico do cidadão PJ.

---

> [!warning] Pontos de atenção
> - **Ponto em aberto — contagem da coluna "Participantes"**: se o mesmo cidadão participa de mais de um departamento da mesma empresa, não está definido se a contagem soma vínculos por departamento ou cidadãos únicos. **QA aguarda definição do Produto** antes de considerar o comportamento aprovado ou bug (CT-021 abaixo fica marcado como bloqueado até a decisão chegar).
> - Documento de produto consolidado ("Departamento CNPJ") cobre 3 tasks diferentes (SGV-8883, 8884, 9898), não só esta — usado aqui só como contexto de apoio, não como fonte de critério de aceite.
> - Ainda não existe seção de "Departamentos" em nenhuma doc de módulo (`04 Conhecimento/Módulos/`) — quando esta demanda for validada, abre pendência de criar/atualizar a doc (fluxo 8).

---

## Casos de teste

### A. Criação de departamento

#### **CT-001 Departamento só é criado para cidadão PJ** *(CA01)*

**Dado** que um servidor está cadastrando um departamento
**Quando** seleciona um cidadão do tipo Pessoa Física
**Então** o sistema não permite a criação do departamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Nome do departamento é obrigatório** *(CA02)*

**Dado** que um servidor está criando um departamento
**Quando** tenta salvar sem informar o nome
**Então** o sistema não permite salvar e sinaliza o campo obrigatório

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-003 E-mail do departamento é obrigatório** *(CA02)*

**Dado** que um servidor está criando um departamento
**Quando** tenta salvar sem informar o e-mail
**Então** o sistema não permite salvar e sinaliza o campo obrigatório

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-004 Nome duplicado é bloqueado na mesma PJ** *(CA03)*

**Dado** que já existe um departamento com um nome numa PJ
**Quando** o servidor tenta criar outro departamento com o mesmo nome para a mesma PJ
**Então** o sistema não permite a criação e exibe mensagem informando o nome já em uso

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005 E-mail duplicado é bloqueado na mesma PJ** *(CA04)*

**Dado** que já existe um departamento com um e-mail numa PJ
**Quando** o servidor tenta criar outro departamento com o mesmo e-mail para a mesma PJ
**Então** o sistema não permite a criação e exibe mensagem informando o e-mail já em uso

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-006 Mesmo nome/e-mail é permitido em PJs diferentes**

**Dado** que existe um departamento com nome e e-mail X numa PJ
**Quando** o servidor cria um departamento com o mesmo nome e e-mail X em outra PJ
**Então** o sistema permite a criação normalmente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-007 Participante só pode ser da mesma instância** *(CA05)*

**Dado** que um servidor está criando um departamento
**Quando** tenta adicionar como participante um cidadão de outro cliente/instância
**Então** o sistema não permite a seleção

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-008 Cargo do participante é obrigatório na criação** *(CA06)*

**Dado** que um servidor está criando um departamento com participante
**Quando** tenta salvar sem informar o cargo do participante
**Então** o sistema não permite salvar e sinaliza o campo obrigatório

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-009 Notificação por e-mail após criação** *(CA07)*

**Dado** que um departamento foi criado com sucesso
**Quando** o cadastro é concluído
**Então** o sistema envia notificação por e-mail com o template previsto no Figma

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-010 Criação registrada no histórico da PJ** *(CA08)*

**Dado** que um departamento foi criado
**Quando** o cadastro é concluído
**Então** a ação é registrada no histórico do cidadão PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Gerenciamento de participantes

#### **CT-011 Vincular participante ao departamento** *(CA01)*

**Dado** que existe um departamento cadastrado
**Quando** o servidor vincula um cidadão como participante
**Então** o vínculo é criado com sucesso

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-012 Bloquear vínculo de participante de outra instância** *(CA02)*

**Dado** que o servidor está vinculando um participante a um departamento existente
**Quando** tenta buscar/selecionar um cidadão de outro cliente/instância
**Então** o sistema não permite o vínculo

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-013 Cargo é obrigatório ao vincular participante** *(CA03)*

**Dado** que o servidor está vinculando um cidadão a um departamento
**Quando** tenta confirmar o vínculo sem informar o cargo
**Então** o sistema não permite e sinaliza o campo obrigatório

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-014 Desvincular participante existente** *(CA04)*

**Dado** que existe um cidadão vinculado a um departamento
**Quando** o servidor desvincula esse cidadão
**Então** o vínculo é removido com sucesso

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-015 Vínculo gera notificação interna e por e-mail** *(CA05, CA06)*

**Dado** que um participante foi vinculado a um departamento
**Quando** a ação é concluída
**Então** o sistema gera notificação interna e envia e-mail aos envolvidos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-016 Desvínculo gera notificação interna e por e-mail** *(CA05, CA06)*

**Dado** que um participante foi desvinculado de um departamento
**Quando** a ação é concluída
**Então** o sistema gera notificação interna e envia e-mail aos envolvidos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-017 Vínculo registrado no histórico da PJ** *(CA07)*

**Dado** que um participante foi vinculado a um departamento
**Quando** a ação é concluída
**Então** o vínculo é registrado no histórico do cidadão PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-018 Desvínculo registrado no histórico da PJ** *(CA07)*

**Dado** que um participante foi desvinculado de um departamento
**Quando** a ação é concluída
**Então** o desvínculo é registrado no histórico do cidadão PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### C. Listagem e visualização da PJ

#### **CT-019 Coluna "Nome" vira "Razão Social" na listagem de PJ** *(CA01)*

**Dado** que o servidor está visualizando a listagem de cidadãos PJ
**Quando** a listagem carrega
**Então** a coluna antes chamada "Nome" é exibida como "Razão Social"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-020 Coluna "Participantes" existe na listagem de PJ** *(CA02)*

**Dado** que o servidor está visualizando a listagem de cidadãos PJ
**Quando** a listagem carrega
**Então** existe uma coluna "Participantes"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-021 Quantidade da coluna "Participantes" reflete a regra do Produto** *(CA02)*

**Dado** que um cidadão participa de mais de um departamento da mesma PJ
**Quando** o servidor confere a coluna "Participantes" da listagem
**Então** verifico a quantidade exibida e reporto o comportamento observado (vínculos por departamento ou cidadãos únicos)

> [!warning]- Bloqueado — aguardando definição do Produto
> Não decidir se o comportamento observado é aprovado ou bug: registrar o número exibido e o cenário, e aguardar a definição do Produto antes de fechar este CT (ver Pontos de atenção do card e [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11083/SGV-11083 - Refinamento Departamentos Para Cidadao PJ|mesa de refinamento]]).

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-022 Visualização da PJ lista os departamentos vinculados** *(CA03)*

**Dado** que o servidor está visualizando os detalhes de um cidadão PJ
**Quando** a tela carrega
**Então** o sistema lista os departamentos vinculados a esse cidadão PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-023 Edição da PJ permite criar novo departamento** *(CA04)*

**Dado** que o servidor está editando um cidadão PJ
**Quando** acessa a seção de departamentos
**Então** é possível criar um novo departamento a partir dali

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Exclusão de departamento

#### **CT-024 Excluir departamento sem participantes e sem documentos** *(CA01)*

**Dado** que existe um departamento sem participantes vinculados e sem documentos tramitados
**Quando** o servidor solicita sua exclusão
**Então** o sistema permite excluir o departamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-025 Bloquear exclusão com participantes vinculados** *(CA02)*

**Dado** que existe um departamento com um ou mais participantes vinculados
**Quando** o servidor tenta excluí-lo
**Então** o sistema não permite a exclusão e oferece a suspensão como alternativa

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-026 Bloquear exclusão com documentos tramitados** *(CA03)*

**Dado** que existe um departamento com um ou mais documentos tramitados
**Quando** o servidor tenta excluí-lo
**Então** o sistema não permite a exclusão e oferece a suspensão como alternativa

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-027 Opção de suspensão aparece quando exclusão é bloqueada**

**Dado** que a exclusão de um departamento foi bloqueada (participante ou documento)
**Quando** o servidor confere as ações disponíveis
**Então** a única ação oferecida é suspender

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-028 Exclusão registrada no histórico da PJ**

**Dado** que um departamento foi excluído
**Quando** a exclusão é concluída
**Então** a ação é registrada no histórico do cidadão PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Suspensão de departamento

#### **CT-029 Suspender departamento sem pendências** *(CA04)*

**Dado** que existe um departamento sem pendências
**Quando** o servidor solicita sua suspensão
**Então** o sistema suspende o departamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-030 Bloquear suspensão com pendências** *(CA05)*

**Dado** que existe um departamento com pendências
**Quando** o servidor tenta suspendê-lo
**Então** o sistema não permite a suspensão e exibe mensagem explicando o motivo

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-031 Status do departamento muda para suspenso**

**Dado** que um departamento foi suspenso com sucesso
**Quando** o servidor confere o status do departamento
**Então** o status exibido é "Suspenso"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-032 Departamento suspenso não aparece em novas tramitações** *(CA06)*

**Dado** que um departamento está suspenso
**Quando** o servidor inicia uma nova tramitação e busca o destinatário
**Então** o departamento suspenso não está disponível para seleção

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-033 Suspensão registrada no histórico da PJ**

**Dado** que um departamento foi suspenso
**Quando** a suspensão é concluída
**Então** a ação é registrada no histórico do cidadão PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### F. Fora de execução — registro

*Só preencher quando algum CT acima for retirado/adiado desta rodada.*

| Caso | Decisão | Motivo |
|---|---|---|
|  |  |  |

---

> [!danger] Bugs encontrados

---

## Evidências

Nenhuma anexada ainda — funcionalidade ainda não implementada (backlog no Notion).

---

> [!tip] Observações

- Refinado a partir de 3 documentos do Notion — análise completa em [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11083/SGV-11083 - Refinamento Departamentos Para Cidadao PJ|04 Conhecimento/Tasks/SGV-11083]].
- Ponto em aberto (contagem da coluna Participantes) não é regra de negócio em disputa por falta de doc — é decisão de Produto ainda não tomada. Ver Pontos de atenção acima.
- Gate de doc: não existe seção de "Departamentos" em `04 Conhecimento/Módulos/` ainda — importar quando esta demanda for validada (fluxo 8).

---

## Histórico

- 2026-09-02 - 📝 Funcionalidade refinada (critérios de aceite prontos) — refinamento de 3 documentos do Notion, 1 ponto em aberto (contagem de participantes) registrado como pendência explícita
