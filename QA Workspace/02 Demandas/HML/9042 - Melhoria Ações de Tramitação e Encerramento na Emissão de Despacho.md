---
tags:
  - demanda
  - melhoria
  - qa
  - tramitacao
task: "9042"
mel: ""
status: aberto
prioridade: ""
data_inicio: 2026-07-29
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: tramitacao
ambiente: HML
---
# Demanda: [Melhoria-CX] Ações de tramitação e encerramento na emissão de despacho

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** HML (em validação)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-9042 no Notion](https://app.notion.com/p/alfa-group/MELHORIA-CX-Adicionar-tarefas-na-barra-de-ferramentas-na-cria-o-de-um-despacho-3722aec67d3081d8ba12d56fc6387c5b) · [Figma — Tramitação/Handoff](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8765-2765)
> - **Devs:** Gabriel Desidério, Lucas Cabral · **Design:** Ivo Costa, Edu, Vinícius
> - **Prazo de conclusão (Notion):** 31/07/2026

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

**Assinatura muda o número de cliques** — o split button mantém "Emitir / Emitir e Assinar", mas se o despacho exigir assinaturas o **avanço não se conclui no mesmo clique**: as solicitações são disparadas *após* a emissão.

**Movimentação × encerramento são independentes e combináveis** — dá pra "Avançar etapa" + "Encerrar para mim" na mesma emissão. As regras de continuar aberto / encerrar para mim / encerrar para meu setor seguem o que **já está implementado na plataforma**.

**Sigilo** — o grupo de sigilo só aparece quando o despacho tem opções de sigilo. Em despacho customizado de etapa, é herdado da configuração de **módulo/serviço/assunto**; o fluxo de trabalho **não** configura sigilo.

Regras completas do módulo: [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]].

---

> [!warning] Pontos de atenção

- **Nomenclatura a confirmar**: este card usa os rótulos do **Figma** — "Continuar aberto" / "Encerrar para mim" / "Encerrar para meu setor". A spec do Notion diz "Encerrar no Setor" / "Encerrar na Mesa". Confirmar o rótulo final com o time antes de reprovar por texto de botão.
- **MR não identificado**: nem o export do Notion nem o Figma citam o MR da entrega. Confirmar com Gabriel Desidério / Lucas Cabral — sem isso não há revisão de escopo de MR ([[Sistema/Skills/SKILL_REVISAO_ESCOPO_MR|SKILL_REVISAO_ESCOPO_MR]]).
- **Risco de regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]]** (reaberta em DEV): aquele bug é "setores das Regras de tramitação não mantidos ao avançar/retroceder". Esta melhoria adiciona avançar/retroceder num **ponto de entrada novo** e pode herdar o mesmo defeito — está no registro do grupo G (adiado).
- **Typo de copy no tooltip**: o Figma traz "Esta ação só **esta** disponível..." (falta acento em "está"). Reportar como ajuste de copy.
- **Matriz de combinações**: o Figma garante que movimentação e encerramento são independentes, mas remete a "todas as regras já implementadas" sem listar os casos. CT-022 cobre uma combinação; a segunda direção ficou no registro do grupo G.
- ⚠️ **Ponto de entrada novo para um defeito já aberto**: a [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]] (aberta em 29/07) é exatamente *"encerrar para mim documento com fluxo de trabalho → toolbar só com Reabrir documento, sem histórico nem baixar"*. Esta melhoria cria um **caminho novo pra disparar essa mesma ação, no mesmo tipo de documento**. Ao executar o CT-014, olhar a toolbar depois: se o defeito aparecer por aqui também, o escopo do fix da 10451 muda (não é a toolbar de um caminho, é a toolbar do estado). **Não virou CT** porque a toolbar não é escopo desta entrega — é observação a fazer de passagem.
- **"Encerrar para todos" no contêiner — pergunta aberta, não critério**: o Figma mostra **três** opções e a plataforma tem "Encerrar para todos" em outro lugar (toolbar; regra documentada na [[QA Workspace/02 Demandas/Concluídas/9750 - Bug Assinatura Pendente Documento Encerrado|SGV-9750]] — é a única que cancela assinaturas pendentes). **Confirmar com o time** se a ausência aqui é intencional. Eu havia escrito isso como CT ("só existem três opções") e **removi**: mockup com três opções não é regra de que uma quarta seja proibida, e como a lista de opções **depende de permissão** (CA17), "exatamente três" não é afirmável — o CT levaria a reprovar comportamento possivelmente correto.
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
- [ ] **CA3** — Documento com fluxo **não iniciado** não exibe o contêiner e não permite movimentar nem encerrar *(satisfeito por construção — ver CT-003)*

**B. Bloqueio por pendência**

- [x] **CA4** — Com **despacho customizado não emitido** na etapa, o select fica desabilitado e fixo em "Permanecer na etapa atual"
- [x] **CA5** — Com **assinatura não concluída** na etapa, o select fica desabilitado e fixo em "Permanecer na etapa atual"
- [x] **CA6** — O bloqueio é **total**: impede avançar, retroceder **e todos os atalhos, nas duas direções**
- [x] **CA7** — No estado bloqueado, o ⓘ exibe o tooltip informando a pendência
- [x] **CA8** — Cumpridas **todas** as pendências da etapa, o select habilita
- [ ] **CA9** — No estado bloqueado, retroceder ou encerrar **continua possível pela toolbar do documento** — 🔴 **REPROVADO**, ver [[QA Workspace/02 Demandas/HML/10489 - Bug Toolbar Do Documento Nao Permite Retroceder Nem Encerrar Com Etapa Bloqueada|SGV-10489]]

**C. Movimentação de etapa pelo contêiner**

- [x] **CA10** — "Permanecer na etapa atual" emite o despacho **sem** movimentar a etapa
- [x] **CA11** — "Avançar etapa" move o documento para a etapa **seguinte** do fluxo
- [x] **CA12** — "Retroceder etapa" move o documento para a etapa **anterior** do fluxo
- [x] **CA13** — Atalho configurado leva o documento para a **etapa do atalho**, não para a adjacente

**D. Encerramento**

- [x] **CA14** — "Continuar aberto" mantém o documento **aberto** após a emissão
- [x] **CA15** — "Encerrar para mim" põe o documento em **Encerrado**, remove da fila de pendências gerais e arquiva na **mesa do usuário logado**
- [x] **CA16** — "Encerrar para meu setor" põe o documento em **Encerrado no setor**, e o documento **segue em tramitação nos demais setores envolvidos**
- [ ] **CA17** — Servidor **sem** permissão de encerrar na etapa **não recebe** a opção de encerrar para o setor *(pendente — exige segundo usuário)*
- [x] **CA18** — Encerrar **para mim** ou **para meu setor** pelo contêiner **não cancela** solicitações de assinatura pendentes

**E. Sigilo**

- [x] **CA19** — Despacho **com** opções de sigilo exibe o grupo de sigilo, herdado de módulo/serviço/assunto
- [x] **CA20** — Despacho **sem** opções de sigilo **não** exibe o grupo de sigilo
- [x] **CA21** — Emitido **com** sigilo, **somente os setores habilitados** veem o conteúdo e os dados do solicitante
- [x] **CA22** — Emitido **sem** sigilo, o conteúdo fica visível aos envolvidos normalmente

**F. Combinações**

- [x] **CA23** — Movimentação e encerramento são **independentes e combináveis** na mesma emissão

> [!info]- Critérios fora desta rodada (registro)
> - **Assinatura muda o número de cliques** ("o avanço não se conclui no mesmo clique quando o despacho exige assinatura") — **inalcançável na prática**: enquanto a assinatura da etapa está pendente o select fica desabilitado (CA5/CT-005), então não existe o estado "avançar + emitir e assinar". Detalhe no registro dos casos de teste.
> - **Regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]]** (setores das Regras de tramitação mantidos ao navegar etapas) — **adiada** por decisão do Rafael em 30/07: o conjunto executado já cobre bem a entrega. A 6373 segue aberta em DEV e tem validação própria.
> - **"Encerrar para todos" não é oferecido no contêiner** — era o CA18 antigo, removido por não ter lastro (mockup com três opções não é regra de proibição, e a lista depende de permissão). Virou pergunta pro time em Pontos de atenção.

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

![[9042 - CT-001, CT-005, CT-007 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4]]

*Mesma gravação cobre CT-005 e CT-007.*

---

#### **CT-002 Documento sem fluxo de trabalho não exibe o contêiner** *(CA2)*

**Dado** que eu tenho um documento **sem** fluxo de trabalho configurado
**Quando** eu emito um despacho
**Então** verifico que o layout padrão do despacho é exibido, sem o contêiner

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-002 - documento sem fluxo nao exibe o conteiner.mp4]]

---

#### **CT-003 Fluxo não iniciado não movimenta nem encerra** *(CA3)*

**Dado** que eu tenho um documento com fluxo de trabalho configurado mas **não iniciado**
**Quando** eu acesso a emissão de despacho
**Então** verifico que o contêiner não é exibido e que vale a toolbar de fluxo não iniciado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [x] Não se aplica

> [!info]- Por que não se aplica
> Documento com fluxo **não iniciado não emite despacho** (Rafael, 30/07) — logo não existe a tela onde o contêiner apareceria. A pré-condição é inalcançável por esta via.
>
> O **CA3 segue válido como regra**: está satisfeito por construção, não por teste. Se o produto passar a permitir emitir com fluxo não iniciado, este CT volta a ser executável.

**Evidências de Testes:**

---

### B. Bloqueio por pendência

#### **CT-004 Despacho customizado não emitido bloqueia a movimentação** *(CA4, CA7)*

**Dado** que a etapa atual tem um despacho customizado **não emitido**
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que o select está desabilitado e fixo em "Permanecer na etapa atual", e que o ⓘ exibe o tooltip da pendência

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-004, CT-006 - despacho customizado nao emitido bloqueia inclusive atalhos.mp4]]

*Mesma gravação cobre CT-006.*

---

#### **CT-005 Assinatura não concluída bloqueia a movimentação** *(CA5, CA7)*

**Dado** que a etapa atual tem uma **assinatura não concluída**
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que o select está desabilitado e fixo em "Permanecer na etapa atual", e que o ⓘ exibe o tooltip da pendência

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-001, CT-005, CT-007 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4]]

*Mesma gravação cobre CT-001 e CT-007.*

---

#### **CT-006 Bloqueio por pendência cobre atalhos nas duas direções** *(CA6)*

**Dado** que a etapa atual tem atalhos configurados
**E** que existe ação obrigatória pendente na etapa
**Quando** eu tento selecionar avançar, retroceder ou qualquer atalho
**Então** verifico que **nenhuma** opção de movimentação está disponível, nas duas direções

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-004, CT-006 - despacho customizado nao emitido bloqueia inclusive atalhos.mp4]]

*Mesma gravação cobre CT-004.*

---

#### **CT-007 Select habilita quando as pendências são cumpridas** *(CA8)*

**Dado** que a etapa atual tinha ação obrigatória pendente e o select estava desabilitado
**Quando** eu concluo **todas** as ações obrigatórias da etapa
**Então** verifico que o select de movimentação habilita e permite escolher o próximo passo

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-001, CT-005, CT-007 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4]]

*Mesma gravação cobre CT-001 e CT-005.*

---

#### **CT-008 Toolbar do documento segue permitindo retroceder e encerrar no estado bloqueado** *(CA9)*

**Dado** que a etapa atual tem pendência e o select de movimentação está desabilitado
**Quando** eu uso a toolbar do documento
**Então** verifico que retroceder e encerrar seguem disponíveis por esse caminho

**Execução Passou?**
- [ ] Sim
- [x] Não

> [!danger] Reprovado — bug aberto
> A toolbar do documento **não** permite retroceder nem encerrar enquanto a etapa está bloqueada por pendência. Contraria a regra do Figma registrada em Regras de negócio: *"Nesse estado, retroceder ou encerrar segue possível pela toolbar do documento"*.
> Bug: [[QA Workspace/02 Demandas/HML/10489 - Bug Toolbar Do Documento Nao Permite Retroceder Nem Encerrar Com Etapa Bloqueada|SGV-10489]]

**Evidências de Testes:**

![[9042 - CT-008, CT-010 - toolbar no estado bloqueado e avancar etapa.mp4]]

*Mesma gravação cobre CT-010.*

---

### C. Movimentação de etapa pelo contêiner

#### **CT-009 Permanecer na etapa atual emite sem movimentar** *(CA10)*

**Dado** que a etapa atual não tem pendências
**Quando** eu mantenho "Permanecer na etapa atual" e emito o despacho
**Então** verifico que o despacho é emitido e o documento **continua na mesma etapa**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-009 - permanecer na etapa atual emite sem movimentar.mp4]]

---

#### **CT-010 Avançar etapa pelo contêiner** *(CA11)*

**Dado** que a etapa atual não tem pendências e existe etapa seguinte no fluxo
**Quando** eu seleciono "Avançar etapa" e emito o despacho
**Então** verifico que o documento passa para a **etapa seguinte** e o evento aparece na timeline

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-008, CT-010 - toolbar no estado bloqueado e avancar etapa.mp4]]

*Mesma gravação cobre CT-008.*

---

#### **CT-011 Retroceder etapa pelo contêiner** *(CA12)*

**Dado** que a etapa atual não tem pendências e existe etapa anterior no fluxo
**Quando** eu seleciono "Retroceder etapa" e emito o despacho
**Então** verifico que o documento volta para a **etapa anterior** e o evento aparece na timeline

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-011 - retroceder etapa pelo conteiner.mp4]]

---

#### **CT-012 Atalho leva à etapa do atalho, não à adjacente** *(CA13)*

**Dado** que a etapa atual tem um atalho configurado para uma etapa não adjacente
**E** que a etapa não tem pendências
**Quando** eu seleciono o atalho e emito o despacho
**Então** verifico que o documento vai para a **etapa do atalho**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-012 - atalho leva a etapa do atalho.mp4]]

---

### D. Encerramento

#### **CT-013 Continuar aberto mantém o documento aberto** *(CA14)*

**Dado** que a etapa atual não tem pendências
**Quando** eu seleciono "Continuar aberto" e emito o despacho
**Então** verifico que o documento **segue aberto** após a emissão

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-013 - continuar aberto mantem o documento aberto.mp4]]

---

#### **CT-014 Encerrar para mim arquiva na mesa do usuário logado** *(CA15)*

**Dado** que a etapa atual não tem pendências
**Quando** eu seleciono "Encerrar para mim" e emito o despacho
**Então** verifico que o documento fica **Encerrado**, sai da fila de pendências gerais e é arquivado na **minha mesa**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-014 - encerrar para mim arquiva na mesa do usuario.mp4]]

---

#### **CT-015 Encerrar para meu setor mantém a tramitação nos demais setores** *(CA16)*

**Dado** que eu **tenho** permissão de encerrar na etapa
**E** que o documento tem outros setores envolvidos
**Quando** eu seleciono "Encerrar para meu setor" e emito o despacho
**Então** verifico que o documento fica **Encerrado no meu setor** e **segue em tramitação** nas mesas dos demais

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-015 - encerrar para meu setor mantem tramitacao nos demais.mp4]]

---

#### **CT-016 Servidor sem permissão de encerrar na etapa não recebe a opção** *(CA17)*

**Dado** que eu estou logado como servidor **sem** permissão de encerrar na etapa (regra "Setores que podem encerrar na etapa" do fluxo)
**Quando** eu abro o contêiner na emissão de despacho
**Então** verifico que a opção de encerrar para o setor **não é oferecida**

**Execução Passou?**
- [ ] Sim
- [ ] Não

> [!warning] Não executado — falta evidência
> Único CT ativo sem execução. Exige **segundo usuário**, sem a permissão de encerrar na etapa — não dá pra cobrir com o mesmo login. É o cenário negativo da permissão; sem ele, a regra do fluxo fica verificada só pelo lado positivo (CT-015).

**Evidências de Testes:**

---

#### **CT-017 Regressão SGV-9750 — encerrar para mim ou para meu setor não cancela assinatura pendente** *(CA18)*

**Dado** que o documento tem uma solicitação de assinatura pendente num despacho vinculado
**Quando** eu encerro "para mim" ou "para meu setor" pelo contêiner
**Então** verifico que a solicitação **permanece pendente** — o cancelamento só ocorre no encerramento para todos

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-017 - regressao 9750 encerrar para mim nao cancela assinatura pendente.mp4]]

---

### E. Sigilo

#### **CT-018 Grupo de sigilo exibido em despacho com opções de sigilo** *(CA19)*

**Dado** que o módulo/serviço/assunto tem opções de privacidade configuradas
**Quando** eu emito um despacho customizado de etapa
**Então** verifico que o grupo de sigilo é exibido, herdado dessa configuração

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-018, CT-020 - grupo de sigilo exibido e despacho emitido com sigilo restringe visualizacao.mp4]]

*Mesma gravação cobre CT-020.*

---

#### **CT-019 Grupo de sigilo ausente em despacho sem opções de sigilo** *(CA20)*

**Dado** que o módulo/serviço/assunto **não** tem opções de privacidade configuradas
**Quando** eu emito um despacho customizado de etapa
**Então** verifico que o grupo de sigilo **não** é exibido

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-019, CT-021 - grupo de sigilo ausente e despacho emitido sem sigilo.mp4]]

*Mesma gravação cobre CT-021.*

---

#### **CT-020 Despacho emitido com sigilo restringe a visualização** *(CA21)*

**Dado** que o despacho tem opções de sigilo e eu marco o despacho como **sigiloso**
**Quando** eu emito o despacho pelo contêiner
**Então** verifico que **somente os setores habilitados** veem o conteúdo e os dados do solicitante

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-018, CT-020 - grupo de sigilo exibido e despacho emitido com sigilo restringe visualizacao.mp4]]

*Mesma gravação cobre CT-018.*

---

#### **CT-021 Despacho emitido sem sigilo fica visível aos envolvidos** *(CA22)*

**Dado** que o despacho tem opções de sigilo e eu **não** marco o despacho como sigiloso
**Quando** eu emito o despacho pelo contêiner
**Então** verifico que o conteúdo fica visível normalmente para os setores e servidores envolvidos

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-019, CT-021 - grupo de sigilo ausente e despacho emitido sem sigilo.mp4]]

*Mesma gravação cobre CT-019.*

---

### F. Combinações

#### **CT-022 Avançar etapa combinado com encerrar para mim** *(CA23)*

**Dado** que a etapa atual não tem pendências
**Quando** eu seleciono "Avançar etapa" **e** "Encerrar para mim" na mesma emissão
**Então** verifico que as duas decisões são aplicadas de forma independente: o fluxo avança **e** o documento é encerrado na minha mesa

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9042 - CT-022 - avancar etapa combinado com encerrar para mim.mp4]]

---

### G. Fora de execução — registro

*Casos considerados e deliberadamente não executados nesta rodada. Ficam aqui pra não sumirem do histórico e pra não abrirem buraco na numeração dos ativos.*

| Caso | Decisão | Motivo |
|---|---|---|
| Retroceder etapa combinado com encerrar para meu setor | **Retirado** (Rafael, 30/07) | Segunda combinação da matriz. O CT-022 já prova a independência entre movimentação e encerramento; a segunda direção não agrega risco novo o suficiente pra custar mais uma massa de teste |
| Despacho que exige assinatura não conclui o avanço no mesmo clique | **Retirado — cenário inalcançável** (Rafael, 30/07) | Enquanto a assinatura da etapa está pendente, o select de movimentação fica **desabilitado** (CT-005). Não existe o estado "escolher avançar + Emitir e Assinar", então a regra do Figma sobre o split button não é observável por esta via. Mesma natureza do CT-003 |
| Regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS\|SGV-6373]] — setores mantidos ao navegar etapas | **Adiado** (Rafael, 30/07) | O conjunto executado já cobre bem a entrega. A 6373 segue **aberta em DEV** com validação própria; quando o fix dela subir, vale exercitar o caminho do contêiner |
| Contêiner não oferece "Encerrar para todos" | **Removido por falta de lastro** (30/07) | Mockup com três opções não é regra de que uma quarta seja proibida, e a lista de opções depende de permissão (CA17) — "exatamente três" não é afirmável. Virou pergunta pro time em Pontos de atenção |

---

> [!danger] Bugs encontrados

- 🐛 [[QA Workspace/02 Demandas/HML/10489 - Bug Toolbar Do Documento Nao Permite Retroceder Nem Encerrar Com Etapa Bloqueada|SGV-10489]] — **reprovação do CT-008**: com a etapa bloqueada por pendência, a toolbar do documento **também** não permite retroceder nem encerrar. Divergência confirmada contra a regra *"nesse estado, retroceder ou encerrar só pela toolbar do documento"* — as duas vias fecham juntas e o documento fica preso na etapa.

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9042)

As gravações desta validação estão **embedadas em cada CT** (seção Casos de teste), no padrão `9042 - CT-NNN[, CT-NNN] - <descrição>.mp4`. Gravação que cobre mais de um caso é **um arquivo só**, referenciado em cada CT com nota de compartilhamento — convenção em [[QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]].

---

> [!tip] Observações

Análise completa (rodadas de refinamento, gate de doc, regras extraídas do Figma e divergências com o Notion) na mesa arquivada: [[QA Workspace/04 Conhecimento/9042 - Refinamento Ações de Tramitação e Encerramento na Emissão de Despacho|9042 - Refinamento]].

**Gate de doc** (2026-07-29): cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]]. As regras desta melhoria foram **incorporadas à doc de Tramitação** na mesma data — a doc respalda os critérios acima.

**Vizinhança com a [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]]** (aberta em 29/07): mesma família de ações ("Encerrar para mim" / "Encerrar para meu setor"), e esta melhoria declara que essas regras seguem o que **já está implementado na plataforma**. São coisas distintas — aqui é o **ato** de encerrar na emissão de despacho, lá é o **estado** da toolbar depois de encerrado — mas se o fix de um tocar o outro vale **reteste cruzado**.

---

## Histórico

- 2026-07-29 - 📝 Melhoria refinada (critérios de aceite prontos; card destilado da mesa em `05 Refinar/`)
- 2026-07-30 - 🔁 Validada em homologação: **20 de 23 critérios aprovados**, 19 CTs aprovados, 1 reprovado (CT-008 → [[QA Workspace/02 Demandas/HML/10489 - Bug Toolbar Do Documento Nao Permite Retroceder Nem Encerrar Com Etapa Bloqueada|SGV-10489]]), 1 não se aplica (CT-003), 1 pendente de segundo usuário (CT-016). 3 casos movidos pro registro por decisão do Rafael.
- 2026-07-29 - ℹ️ Contexto: **aprovada em DEV por outro QA** (não pelo Rafael) — por isso não há registro de validação em DEV na daily dele. Validação em homologação em andamento.
