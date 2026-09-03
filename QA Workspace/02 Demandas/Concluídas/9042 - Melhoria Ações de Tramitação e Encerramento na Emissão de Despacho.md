---
tags:
  - demanda
  - melhoria
  - qa
  - tramitacao
task: "9042"
status: resolvido
prioridade: ""
data_inicio: 2026-07-29
data_fim: 2026-08-11
responsavel: Rafael
cadastrado_por: ""
modulo: tramitacao
ambiente: PROD
---
# Demanda: [Melhoria-CX] Ações de tramitação e encerramento na emissão de despacho

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** Concluída (entrega em produção; card encerrado em 11/08/2026)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-9042 no Notion](https://app.notion.com/p/alfa-group/MELHORIA-CX-Adicionar-tarefas-na-barra-de-ferramentas-na-cria-o-de-um-despacho-3722aec67d3081d8ba12d56fc6387c5b) · [Figma — Tramitação/Handoff](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8765-2765)
> - **Devs:** Gabriel Desidério, Lucas Cabral · **Design:** Ivo Costa, Edu, Vinícius
> - **Prazo de conclusão (Notion):** 31/07/2026
> - **Refinamento:** mesa arquivada em [[QA Workspace/04 Conhecimento/Tasks/SGV-9042/SGV-9042 - Refinamento Ações de Tramitação e Encerramento na Emissão de Despacho|04 Conhecimento/Tasks/SGV-9042]]

---

> [!abstract] Resumo

Na **emissão de despacho** passa a existir o contêiner **"Próximo passo do documento"**, que permite ao usuário definir o destino do documento no mesmo ato em que emite o despacho — em vez de emitir e tramitar em dois passos separados.

O contêiner oferece a escolha do **próximo passo do fluxo** (permanecer na etapa atual, avançar, retroceder ou usar um atalho configurado) e, de forma **independente**, o **comportamento de encerramento** do documento (continuar aberto, encerrar para mim ou encerrar para meu setor).

---

## Regras de negócio

**Elegibilidade** — o contêiner só existe em documento com fluxo de trabalho **configurado e já iniciado**. Fluxo **não iniciado** não pode ser movimentado nem encerrado: o contêiner não aparece e vale a toolbar de fluxo não iniciado. Documento **sem** workflow segue o layout padrão do despacho, sem o contêiner.

**Bloqueio por pendência** (regra central):

- Qualquer ação obrigatória pendente na etapa — **despacho customizado não emitido** ou **assinatura não concluída** — desabilita o select de movimentação, que fica fixo em **"Permanecer na etapa atual"** com tooltip informando a pendência.
- O bloqueio é **total**: inclui avançar, retroceder e **todos os atalhos, nas duas direções**. Não é permitido movimentar etapa com pendência **mesmo que a intenção seja retroceder**.
- Nesse estado, **retroceder ou encerrar segue possível pela toolbar do documento**.
- O select habilita quando **todas** as pendências forem cumpridas.

> [!info] Não confundir com a regra do Workflow
> O [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]] diz que com pendência *"só retroceder ou encerrar"* — isso é sobre o que é **permitido no documento**, e o caminho é a **toolbar**. O bloqueio total aqui é sobre o que **este contêiner oferece**. Retroceder é permitido; não por aqui. Conciliação detalhada em [[QA Workspace/04 Conhecimento/Módulos/Tramitação#Ações de destino na emissão de despacho (SGV-9042)|Tramitação]].

**Assinatura muda o número de cliques** — o split button mantém "Emitir / Emitir e Assinar", mas se o despacho exigir assinaturas o **avanço não se conclui no mesmo clique**: as solicitações são disparadas *após* a emissão.

**Movimentação × encerramento são independentes e combináveis** — dá pra "Avançar etapa" + "Encerrar para mim" na mesma emissão. As regras de continuar aberto / encerrar para mim / encerrar para meu setor seguem o que **já está implementado na plataforma**.

**Sigilo** — o grupo de sigilo só aparece quando o despacho tem opções de sigilo. Em despacho customizado de etapa, é herdado da configuração de **módulo/serviço/assunto**; o fluxo de trabalho **não** configura sigilo.

Regras completas do módulo: [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]].

---

> [!warning] Pontos de atenção

- ✅ **Nomenclatura definida (30/07)**: permanecem os rótulos do **Figma** — "Continuar aberto" / "Encerrar para mim" / "Encerrar para meu setor". A spec do Notion, que dizia "Encerrar no Setor" / "Encerrar na Mesa", está **desatualizada nesse ponto**. Decidido com o time; não é mais ponto aberto.
- **MR não identificado**: nem o export do Notion nem o Figma citam o MR da entrega. Confirmar com Gabriel Desidério / Lucas Cabral — sem isso não há revisão de escopo de MR ([[Sistema/Skills/SKILL_REVISAO_ESCOPO_MR|SKILL_REVISAO_ESCOPO_MR]]).
- **Risco de regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]]** (reaberta em DEV): aquele bug é "setores das Regras de tramitação não mantidos ao avançar/retroceder". Esta melhoria adiciona avançar/retroceder num **ponto de entrada novo** e pode herdar o mesmo defeito — está no registro do grupo G (adiado).
- **Typo de copy no tooltip**: o Figma traz "Esta ação só **esta** disponível..." (falta acento em "está"). Reportar como ajuste de copy.
- **Matriz de combinações**: o Figma garante que movimentação e encerramento são independentes, mas remete a "todas as regras já implementadas" sem listar os casos. CT-021 cobre uma combinação; a segunda direção ficou no registro do grupo G.
- ⚠️ **Ponto de entrada novo para um defeito já aberto**: a [[QA Workspace/02 Demandas/Concluídas/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]] (aberta em 29/07) é exatamente *"encerrar para mim documento com fluxo de trabalho → toolbar só com Reabrir documento, sem histórico nem baixar"*. Esta melhoria cria um **caminho novo pra disparar essa mesma ação, no mesmo tipo de documento**. Ao executar o CT-013, olhar a toolbar depois: se o defeito aparecer por aqui também, o escopo do fix da 10451 muda (não é a toolbar de um caminho, é a toolbar do estado). **Não virou CT** porque a toolbar não é escopo desta entrega — é observação a fazer de passagem.
- **"Encerrar para todos" no contêiner — pergunta aberta, não critério**: o Figma mostra **três** opções e a plataforma tem "Encerrar para todos" em outro lugar (toolbar; regra documentada na [[QA Workspace/02 Demandas/Concluídas/9750 - Bug Assinatura Pendente Documento Encerrado|SGV-9750]] — é a única que cancela assinaturas pendentes). **Confirmar com o time** se a ausência aqui é intencional. Eu havia escrito isso como CT ("só existem três opções") e **removi**: mockup com três opções não é regra de que uma quarta seja proibida, e como a lista de opções **depende de permissão** (CA16), "exatamente três" não é afirmável — o CT levaria a reprovar comportamento possivelmente correto.
- **Encerrar aqui é praticamente irreversível**: [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]] registra que documento encerrado com fluxo de trabalho **pode ser reaberto, mas o fluxo não volta a acontecer**. Ou seja, escolher "Encerrar para mim/para meu setor" no ato da emissão encerra o fluxo de vez — reabrir devolve o documento, não a esteira. Vale ter massa de teste separada pros CTs do grupo D, porque cada execução queima um documento.

---

## Plano de teste

| Item | Definição |
|---|---|
| **Demanda** | SGV-9042 — Melhoria-CX |
| **Responsável** | Rafael |
| **Ambiente** | Homologação |
| **Escopo** | Contêiner "Próximo passo do documento" na emissão de despacho: exibição condicional, movimentação de etapa (avançar/retroceder/atalhos), encerramento (continuar aberto / para mim / para meu setor), bloqueio por pendência, sigilo |
| **Fora de escopo** | Regras de encerramento em si (já implementadas na plataforma) e configuração de fluxo de trabalho |
| **Tipos de teste** | Funcional · Regressão (SGV-6373) |
| **Dependências** | Fluxo de trabalho configurado e iniciado; despacho customizado de etapa; assinatura configurada; atalhos configurados numa etapa |

**Critérios de aceite**

*Agrupados na mesma ordem dos casos de teste. Um critério por comportamento verificável — estado que liga/desliga o defeito rende critério próprio ([[Sistema/Skills/SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]]).*

**A. Exibição do contêiner**

- [x] **CA1** — O contêiner "Próximo passo do documento" é exibido em documento com fluxo de trabalho **configurado e já iniciado**
- [x] **CA2** — Documento **sem** fluxo de trabalho segue o layout padrão do despacho, **sem** o contêiner

**B. Bloqueio por pendência**

- [x] **CA3** — Com **despacho customizado não emitido** na etapa, o select fica desabilitado e fixo em "Permanecer na etapa atual"
- [x] **CA4** — Com **assinatura não concluída** na etapa, o select fica desabilitado e fixo em "Permanecer na etapa atual"
- [x] **CA5** — O bloqueio é **total**: impede avançar, retroceder **e todos os atalhos, nas duas direções**
- [x] **CA6** — No estado bloqueado, o ⓘ exibe o tooltip informando a pendência
- [x] **CA7** — Cumpridas **todas** as pendências da etapa, o select habilita
- [x] **CA8** — No estado bloqueado, retroceder ou encerrar **continua possível pela toolbar do documento**

**C. Movimentação de etapa pelo contêiner**

- [x] **CA9** — "Permanecer na etapa atual" emite o despacho **sem** movimentar a etapa
- [x] **CA10** — "Avançar etapa" move o documento para a etapa **seguinte** do fluxo
- [x] **CA11** — "Retroceder etapa" move o documento para a etapa **anterior** do fluxo
- [x] **CA12** — Atalho configurado leva o documento para a **etapa do atalho**, não para a adjacente

**D. Encerramento**

- [x] **CA13** — "Continuar aberto" mantém o documento **aberto** após a emissão
- [x] **CA14** — "Encerrar para mim" põe o documento em **Encerrado**, remove da fila de pendências gerais e arquiva na **mesa do usuário logado**
- [x] **CA15** — "Encerrar para meu setor" põe o documento em **Encerrado no setor**, e o documento **segue em tramitação nos demais setores envolvidos**
- [x] **CA16** — Servidor **sem** permissão de encerrar na etapa **não recebe** a opção de encerrar para o setor
- [x] **CA17** — Encerrar **para mim** ou **para meu setor** pelo contêiner **não cancela** solicitações de assinatura pendentes

**E. Sigilo**

- [x] **CA18** — Despacho **com** opções de sigilo exibe o grupo de sigilo, herdado de módulo/serviço/assunto
- [x] **CA19** — Despacho **sem** opções de sigilo **não** exibe o grupo de sigilo
- [x] **CA20** — Emitido **com** sigilo, **somente os setores habilitados** veem o conteúdo e os dados do solicitante
- [x] **CA21** — Emitido **sem** sigilo, o conteúdo fica visível aos envolvidos normalmente

**F. Combinações**

- [x] **CA22** — Movimentação e encerramento são **independentes e combináveis** na mesma emissão

> [!info]- Critérios fora desta rodada (registro)
> - **Assinatura muda o número de cliques** ("o avanço não se conclui no mesmo clique quando o despacho exige assinatura") — **inalcançável na prática**: enquanto a assinatura da etapa está pendente o select fica desabilitado (CA4/CT-004), então não existe o estado "avançar + emitir e assinar". Detalhe no registro dos casos de teste.
> - **Regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]]** (setores das Regras de tramitação mantidos ao navegar etapas) — **adiada** por decisão do Rafael em 30/07: o conjunto executado já cobre bem a entrega. A 6373 segue aberta em DEV e tem validação própria.
> - **"Encerrar para todos" não é oferecido no contêiner** — era o CA17 antigo, removido por não ter lastro (mockup com três opções não é regra de proibição, e a lista depende de permissão). Virou pergunta pro time em Pontos de atenção.

---

## Casos de teste

### A. Exibição do contêiner

#### **CT-001 Contêiner exibido em documento com fluxo configurado e iniciado** *(CA1)*

**Dado** que eu tenho um documento com fluxo de trabalho configurado e com o fluxo já iniciado
**Quando** eu emito um despacho
**Então** verifico que o contêiner "Próximo passo do documento" é exibido

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-01 - CT-001, CT-004, CT-006 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4]]

*Mesma gravação cobre CT-004 e CT-006.*

---

#### **CT-002 Documento sem fluxo de trabalho não exibe o contêiner** *(CA2)*

**Dado** que eu tenho um documento **sem** fluxo de trabalho configurado
**Quando** eu emito um despacho
**Então** verifico que o layout padrão do despacho é exibido, sem o contêiner

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-02 - CT-002 - documento sem fluxo nao exibe o conteiner.mp4]]

---

### B. Bloqueio por pendência

#### **CT-003 Despacho customizado não emitido bloqueia a movimentação** *(CA3, CA6)*

**Dado** que a etapa atual tem um despacho customizado **não emitido**
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que o select está desabilitado e fixo em "Permanecer na etapa atual", e que o ⓘ exibe o tooltip da pendência

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-03 - CT-003, CT-005 - despacho customizado nao emitido bloqueia inclusive atalhos.mp4]]

*Mesma gravação cobre CT-005.*

---

#### **CT-004 Assinatura não concluída bloqueia a movimentação** *(CA4, CA6)*

**Dado** que a etapa atual tem uma **assinatura não concluída**
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que o select está desabilitado e fixo em "Permanecer na etapa atual", e que o ⓘ exibe o tooltip da pendência

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-01 - CT-001, CT-004, CT-006 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4]]

*Mesma gravação cobre CT-001 e CT-006.*

---

#### **CT-005 Bloqueio por pendência cobre atalhos nas duas direções** *(CA5)*

**Dado** que a etapa atual tem atalhos configurados
**E** que existe ação obrigatória pendente na etapa
**Quando** eu tento selecionar avançar, retroceder ou qualquer atalho
**Então** verifico que **nenhuma** opção de movimentação está disponível, nas duas direções

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-03 - CT-003, CT-005 - despacho customizado nao emitido bloqueia inclusive atalhos.mp4]]

*Mesma gravação cobre CT-003.*

---

#### **CT-006 Select habilita quando as pendências são cumpridas** *(CA7)*

**Dado** que a etapa atual tinha ação obrigatória pendente e o select estava desabilitado
**Quando** eu concluo **todas** as ações obrigatórias da etapa
**Então** verifico que o select de movimentação habilita e permite escolher o próximo passo

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-01 - CT-001, CT-004, CT-006 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4]]

*Mesma gravação cobre CT-001 e CT-004.*

---

#### **CT-007 Toolbar do documento segue permitindo retroceder e encerrar no estado bloqueado** *(CA8)*

**Dado** que a etapa atual tem pendência e o select de movimentação está desabilitado
**Quando** eu uso a toolbar do documento
**Então** verifico que retroceder e encerrar seguem disponíveis por esse caminho

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-04 - CT-007, CT-009 - toolbar no estado bloqueado e avancar etapa.mp4]]

*Mesma gravação cobre CT-009.*

---

### C. Movimentação de etapa pelo contêiner

#### **CT-008 Permanecer na etapa atual emite sem movimentar** *(CA9)*

**Dado** que a etapa atual não tem pendências
**Quando** eu mantenho "Permanecer na etapa atual" e emito o despacho
**Então** verifico que o despacho é emitido e o documento **continua na mesma etapa**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-05 - CT-008 - permanecer na etapa atual emite sem movimentar.mp4]]

---

#### **CT-009 Avançar etapa pelo contêiner** *(CA10)*

**Dado** que a etapa atual não tem pendências e existe etapa seguinte no fluxo
**Quando** eu seleciono "Avançar etapa" e emito o despacho
**Então** verifico que o documento passa para a **etapa seguinte** e o evento aparece na timeline

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-04 - CT-007, CT-009 - toolbar no estado bloqueado e avancar etapa.mp4]]

*Mesma gravação cobre CT-007.*

---

#### **CT-010 Retroceder etapa pelo contêiner** *(CA11)*

**Dado** que a etapa atual não tem pendências e existe etapa anterior no fluxo
**Quando** eu seleciono "Retroceder etapa" e emito o despacho
**Então** verifico que o documento volta para a **etapa anterior** e o evento aparece na timeline

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-06 - CT-010 - retroceder etapa pelo conteiner.mp4]]

---

#### **CT-011 Atalho leva à etapa do atalho, não à adjacente** *(CA12)*

**Dado** que a etapa atual tem um atalho configurado para uma etapa não adjacente
**E** que a etapa não tem pendências
**Quando** eu seleciono o atalho e emito o despacho
**Então** verifico que o documento vai para a **etapa do atalho**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-07 - CT-011 - atalho leva a etapa do atalho.mp4]]

---

### D. Encerramento

#### **CT-012 Continuar aberto mantém o documento aberto** *(CA13)*

**Dado** que a etapa atual não tem pendências
**Quando** eu seleciono "Continuar aberto" e emito o despacho
**Então** verifico que o documento **segue aberto** após a emissão

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-08 - CT-012 - continuar aberto mantem o documento aberto.mp4]]

---

#### **CT-013 Encerrar para mim arquiva na mesa do usuário logado** *(CA14)*

**Dado** que a etapa atual não tem pendências
**Quando** eu seleciono "Encerrar para mim" e emito o despacho
**Então** verifico que o documento fica **Encerrado**, sai da fila de pendências gerais e é arquivado na **minha mesa**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-09 - CT-013 - encerrar para mim arquiva na mesa do usuario.mp4]]

---

#### **CT-014 Encerrar para meu setor mantém a tramitação nos demais setores** *(CA15)*

**Dado** que eu **tenho** permissão de encerrar na etapa
**E** que o documento tem outros setores envolvidos
**Quando** eu seleciono "Encerrar para meu setor" e emito o despacho
**Então** verifico que o documento fica **Encerrado no meu setor** e **segue em tramitação** nas mesas dos demais

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-10 - CT-014 - encerrar para meu setor mantem tramitacao nos demais.mp4]]

---

#### **CT-015 Servidor sem permissão de encerrar na etapa não recebe a opção** *(CA16)*

**Dado** que eu estou logado como servidor **sem** permissão de encerrar na etapa (regra "Setores que podem encerrar na etapa" do fluxo)
**Quando** eu abro o contêiner na emissão de despacho
**Então** verifico que a opção de encerrar para o setor **não é oferecida**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-11 - CT-015 - servidor sem permissao de encerrar na etapa nao recebe a opcao.mp4]]

---

#### **CT-016 Regressão SGV-9750 — encerrar para mim ou para meu setor não cancela assinatura pendente** *(CA17)*

**Dado** que o documento tem uma solicitação de assinatura pendente num despacho vinculado
**Quando** eu encerro "para mim" ou "para meu setor" pelo contêiner
**Então** verifico que a solicitação **permanece pendente** — o cancelamento só ocorre no encerramento para todos

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-12 - CT-016 - regressao 9750 encerrar para mim nao cancela assinatura pendente.mp4]]

---

### E. Sigilo

#### **CT-017 Grupo de sigilo exibido em despacho com opções de sigilo** *(CA18)*

**Dado** que o módulo/serviço/assunto tem opções de privacidade configuradas
**Quando** eu emito um despacho customizado de etapa
**Então** verifico que o grupo de sigilo é exibido, herdado dessa configuração

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-13 - CT-017, CT-019 - grupo de sigilo exibido e despacho emitido com sigilo restringe visualizacao.mp4]]

*Mesma gravação cobre CT-019.*

---

#### **CT-018 Grupo de sigilo ausente em despacho sem opções de sigilo** *(CA19)*

**Dado** que o módulo/serviço/assunto **não** tem opções de privacidade configuradas
**Quando** eu emito um despacho customizado de etapa
**Então** verifico que o grupo de sigilo **não** é exibido

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-14 - CT-018, CT-020 - grupo de sigilo ausente e despacho emitido sem sigilo.mp4]]

*Mesma gravação cobre CT-020.*

---

#### **CT-019 Despacho emitido com sigilo restringe a visualização** *(CA20)*

**Dado** que o despacho tem opções de sigilo e eu marco o despacho como **sigiloso**
**Quando** eu emito o despacho pelo contêiner
**Então** verifico que **somente os setores habilitados** veem o conteúdo e os dados do solicitante

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-13 - CT-017, CT-019 - grupo de sigilo exibido e despacho emitido com sigilo restringe visualizacao.mp4]]

*Mesma gravação cobre CT-017.*

---

#### **CT-020 Despacho emitido sem sigilo fica visível aos envolvidos** *(CA21)*

**Dado** que o despacho tem opções de sigilo e eu **não** marco o despacho como sigiloso
**Quando** eu emito o despacho pelo contêiner
**Então** verifico que o conteúdo fica visível normalmente para os setores e servidores envolvidos

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-14 - CT-018, CT-020 - grupo de sigilo ausente e despacho emitido sem sigilo.mp4]]

*Mesma gravação cobre CT-018.*

---

### F. Combinações

#### **CT-021 Avançar etapa combinado com encerrar para mim** *(CA22)*

**Dado** que a etapa atual não tem pendências
**Quando** eu seleciono "Avançar etapa" **e** "Encerrar para mim" na mesma emissão
**Então** verifico que as duas decisões são aplicadas de forma independente: o fluxo avança **e** o documento é encerrado na minha mesa

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - EV-15 - CT-021 - avancar etapa combinado com encerrar para mim.mp4]]

---

### G. Fora de execução — registro

*Casos considerados e deliberadamente não executados nesta rodada. Ficam aqui pra não sumirem do histórico e pra não abrirem buraco na numeração dos ativos.*

| Caso | Decisão | Motivo |
|---|---|---|
| Retroceder etapa combinado com encerrar para meu setor | **Retirado** (Rafael, 30/07) | Segunda combinação da matriz. O CT-021 já prova a independência entre movimentação e encerramento; a segunda direção não agrega risco novo o suficiente pra custar mais uma massa de teste |
| Despacho que exige assinatura não conclui o avanço no mesmo clique | **Retirado — cenário inalcançável** (Rafael, 30/07) | Enquanto a assinatura da etapa está pendente, o select de movimentação fica **desabilitado** (CT-004). Não existe o estado "escolher avançar + Emitir e Assinar", então a regra do Figma sobre o split button não é observável por esta via. Mesma natureza do CT-003 |
| Regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS\|SGV-6373]] — setores mantidos ao navegar etapas | **Adiado** (Rafael, 30/07) | O conjunto executado já cobre bem a entrega. A 6373 segue **aberta em DEV** com validação própria; quando o fix dela subir, vale exercitar o caminho do contêiner |
| Fluxo não iniciado não movimenta nem encerra *(era CT-003 / CA3)* | **Removido — não se aplica** (Rafael, 30/07) | Documento com fluxo **não iniciado não emite despacho**: não existe a tela onde o contêiner apareceria, a pré-condição é inalcançável por esta via. A regra segue válida e **satisfeita por construção**. Se o produto passar a permitir emitir com fluxo não iniciado, o caso volta a ser executável |
| Contêiner não oferece "Encerrar para todos" | **Removido por falta de lastro** (30/07) | Mockup com três opções não é regra de que uma quarta seja proibida, e a lista de opções depende de permissão (CA16) — "exatamente três" não é afirmável. Virou pergunta pro time em Pontos de atenção |

---

> [!danger] Bugs encontrados

Nenhum. A única reprovação da rodada (CT-005) foi revista: o bloqueio total é comportamento intencional, confirmado no Figma e com o time em 30/07 — o card aberto na hora ([[QA Workspace/99 Arquivo/10489 - Bug Conteiner De Despacho Nao Permite Retroceder Etapa Com Acao Obrigatoria Pendente|SGV-10489]]) foi **descartado**.

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9042)

As gravações estão **embedadas em cada CT** (seção Casos de teste), no padrão `9042 - EV-NN - CT-NNN[, CT-NNN] - <descrição>.mp4`. Gravação que cobre mais de um caso é **um arquivo só**, referenciado em cada CT com nota de compartilhamento — convenção em [[QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]].
**Índice de evidências** — 21 CTs em **15 gravações**, porque uma gravação pode cobrir mais de um caso. Por isso a evidência tem numeração própria (`EV-NN`), **contígua e sem buraco**: dá pra percorrer EV-01 → EV-15 sem procurar arquivo nem pular número.

| CT | Gravação |
|---|---|
| CT-001 | EV-01 |
| CT-002 | EV-02 |
| CT-003 | EV-03 |
| CT-004 | EV-01 |
| CT-005 | EV-03 |
| CT-006 | EV-01 |
| CT-007 | EV-04 |
| CT-008 | EV-05 |
| CT-009 | EV-04 |
| CT-010 | EV-06 |
| CT-011 | EV-07 |
| CT-012 | EV-08 |
| CT-013 | EV-09 |
| CT-014 | EV-10 |
| CT-015 | EV-11 |
| CT-016 | EV-12 |
| CT-017 | EV-13 |
| CT-018 | EV-14 |
| CT-019 | EV-13 |
| CT-020 | EV-14 |
| CT-021 | EV-15 |

<details><summary>Ordem de arrasto (EV-01 → EV-15)</summary>

| EV | Cobre | Arquivo |
|---|---|---|
| EV-01 | CT-001, CT-004, CT-006 | `9042 - EV-01 - CT-001, CT-004, CT-006 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4` |
| EV-02 | CT-002 | `9042 - EV-02 - CT-002 - documento sem fluxo nao exibe o conteiner.mp4` |
| EV-03 | CT-003, CT-005 | `9042 - EV-03 - CT-003, CT-005 - despacho customizado nao emitido bloqueia inclusive atalhos.mp4` |
| EV-04 | CT-007, CT-009 | `9042 - EV-04 - CT-007, CT-009 - toolbar no estado bloqueado e avancar etapa.mp4` |
| EV-05 | CT-008 | `9042 - EV-05 - CT-008 - permanecer na etapa atual emite sem movimentar.mp4` |
| EV-06 | CT-010 | `9042 - EV-06 - CT-010 - retroceder etapa pelo conteiner.mp4` |
| EV-07 | CT-011 | `9042 - EV-07 - CT-011 - atalho leva a etapa do atalho.mp4` |
| EV-08 | CT-012 | `9042 - EV-08 - CT-012 - continuar aberto mantem o documento aberto.mp4` |
| EV-09 | CT-013 | `9042 - EV-09 - CT-013 - encerrar para mim arquiva na mesa do usuario.mp4` |
| EV-10 | CT-014 | `9042 - EV-10 - CT-014 - encerrar para meu setor mantem tramitacao nos demais.mp4` |
| EV-11 | CT-015 | `9042 - EV-11 - CT-015 - servidor sem permissao de encerrar na etapa nao recebe a opcao.mp4` |
| EV-12 | CT-016 | `9042 - EV-12 - CT-016 - regressao 9750 encerrar para mim nao cancela assinatura pendente.mp4` |
| EV-13 | CT-017, CT-019 | `9042 - EV-13 - CT-017, CT-019 - grupo de sigilo exibido e despacho emitido com sigilo restringe visualizacao.mp4` |
| EV-14 | CT-018, CT-020 | `9042 - EV-14 - CT-018, CT-020 - grupo de sigilo ausente e despacho emitido sem sigilo.mp4` |
| EV-15 | CT-021 | `9042 - EV-15 - CT-021 - avancar etapa combinado com encerrar para mim.mp4` |

</details>


---

> [!tip] Observações

Análise completa (rodadas de refinamento, gate de doc, regras extraídas do Figma e divergências com o Notion) na mesa arquivada: [[QA Workspace/04 Conhecimento/Tasks/SGV-9042/SGV-9042 - Refinamento Ações de Tramitação e Encerramento na Emissão de Despacho|9042 - Refinamento]].

**Gate de doc** (2026-07-29): cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]]. As regras desta melhoria foram **incorporadas à doc de Tramitação** na mesma data — a doc respalda os critérios acima.

**Vizinhança com a [[QA Workspace/02 Demandas/Concluídas/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]]** (aberta em 29/07): mesma família de ações ("Encerrar para mim" / "Encerrar para meu setor"), e esta melhoria declara que essas regras seguem o que **já está implementado na plataforma**. São coisas distintas — aqui é o **ato** de encerrar na emissão de despacho, lá é o **estado** da toolbar depois de encerrado — mas se o fix de um tocar o outro vale **reteste cruzado**.

---

## Histórico

- 2026-07-29 - 📝 Melhoria refinada (critérios de aceite prontos; card destilado da mesa em `05 Refinar/`)
- 2026-07-30 - 🔁 Validada em homologação: **22 de 22 critérios e 21 de 21 CTs aprovados — nenhum reprovado**. Nomenclatura dos botões definida (rótulos do Figma permanecem). 4 casos no registro do grupo G. Aberto só o **MR da entrega**, não identificado.
- 2026-07-29 - ℹ️ Contexto: **aprovada em DEV por outro QA** (não pelo Rafael) — por isso não há registro de validação em DEV na daily dele. Validação em homologação em andamento.
- 2026-08-11 - ✅ Entrega confirmada em produção; card encerrado (validação de homologação em 30/07: 22/22 critérios e 21/21 CTs, nenhum reprovado). O **MR da entrega nunca foi identificado** — encerrado assim mesmo, por decisão de 11/08.
