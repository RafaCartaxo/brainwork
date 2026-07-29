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
- **Risco de regressão da [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]]** (reaberta em DEV): aquele bug é "setores das Regras de tramitação não mantidos ao avançar/retroceder". Esta melhoria adiciona avançar/retroceder num **ponto de entrada novo** e pode herdar o mesmo defeito — CT-012 cobre.
- **Typo de copy no tooltip**: o Figma traz "Esta ação só **esta** disponível..." (falta acento em "está"). Reportar como ajuste de copy.
- **Matriz de combinações**: o Figma garante que movimentação e encerramento são independentes, mas remete a "todas as regras já implementadas" sem listar os casos. Mapear as combinações válidas durante a validação.

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

- [ ] **CA1** — O contêiner "Próximo passo do documento" é exibido em documento com fluxo de trabalho **configurado e já iniciado**
- [ ] **CA2** — Documento **sem** fluxo de trabalho segue o layout padrão do despacho, **sem** o contêiner
- [ ] **CA3** — Documento com fluxo **não iniciado** não exibe o contêiner e não permite movimentar nem encerrar
- [ ] **CA4** — Com **despacho customizado não emitido** na etapa, o select fica desabilitado e fixo em "Permanecer na etapa atual"
- [ ] **CA5** — Com **assinatura não concluída** na etapa, o select fica desabilitado e fixo em "Permanecer na etapa atual"
- [ ] **CA6** — O bloqueio por pendência é **total**: impede avançar, retroceder **e todos os atalhos, nas duas direções**
- [ ] **CA7** — No estado bloqueado, o ⓘ exibe o tooltip da pendência
- [ ] **CA8** — Cumpridas **todas** as pendências da etapa, o select habilita
- [ ] **CA9** — No estado bloqueado, retroceder ou encerrar **continua possível pela toolbar do documento**
- [ ] **CA10** — Movimentação e encerramento são **independentes e combináveis** na mesma emissão
- [ ] **CA11** — Quando o despacho **exige assinatura**, o avanço **não se conclui no mesmo clique**
- [ ] **CA12** — O grupo de sigilo aparece somente com opções de sigilo, herdadas de módulo/serviço/assunto
- [ ] **CA13** — Sem regressão na SGV-6373: setores das Regras de tramitação **mantidos** ao avançar/retroceder

---

## Casos de teste

- **CT-001 Contêiner exibido em documento com fluxo configurado e iniciado** *(CA1)*
    Dado que eu tenho um documento com fluxo de trabalho configurado e com o fluxo já iniciado
    Quando eu emito um despacho
    Então verifico que o contêiner "Próximo passo do documento" é exibido

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-002 Documento sem fluxo de trabalho não exibe o contêiner** *(CA2)*
    Dado que eu tenho um documento **sem** fluxo de trabalho configurado
    Quando eu emito um despacho
    Então verifico que o layout padrão do despacho é exibido, sem o contêiner "Próximo passo do documento"

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-003 Fluxo não iniciado não movimenta nem encerra** *(CA3)*
    Dado que eu tenho um documento com fluxo de trabalho configurado mas **não iniciado**
    Quando eu acesso a emissão de despacho
    Então verifico que o contêiner não é exibido e que vale a toolbar de fluxo não iniciado, sem opção de movimentar ou encerrar

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-004 Despacho customizado não emitido bloqueia a movimentação** *(CA4, CA7)*
    Dado que a etapa atual tem um despacho customizado **não emitido**
    Quando eu abro o contêiner "Próximo passo do documento"
    Então verifico que o select está desabilitado e fixo em "Permanecer na etapa atual", e que o ⓘ exibe o tooltip da pendência

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-005 Assinatura não concluída bloqueia a movimentação** *(CA5, CA7)*
    Dado que a etapa atual tem uma **assinatura não concluída**
    Quando eu abro o contêiner "Próximo passo do documento"
    Então verifico que o select está desabilitado e fixo em "Permanecer na etapa atual", e que o ⓘ exibe o tooltip da pendência

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-006 Bloqueio por pendência cobre atalhos nas duas direções** *(CA6)*
    Dado que a etapa atual tem atalhos configurados
    E que existe ação obrigatória pendente na etapa
    Quando eu tento selecionar avançar, retroceder ou qualquer atalho
    Então verifico que **nenhuma** opção de movimentação está disponível, nas duas direções

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-007 Select habilita quando as pendências são cumpridas** *(CA8)*
    Dado que a etapa atual tinha ação obrigatória pendente e o select estava desabilitado
    Quando eu concluo **todas** as ações obrigatórias da etapa
    Então verifico que o select de movimentação habilita e permite escolher o próximo passo

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-008 Toolbar do documento continua permitindo retroceder/encerrar no estado bloqueado** *(CA9)*
    Dado que a etapa atual tem pendência e o select de movimentação está desabilitado
    Quando eu uso a toolbar do documento
    Então verifico que retroceder e encerrar seguem disponíveis por esse caminho

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-009 Movimentação e encerramento combinados na mesma emissão** *(CA10)*
    Dado que a etapa atual não tem pendências
    Quando eu seleciono "Avançar etapa" e "Encerrar para mim" na mesma emissão
    Então verifico que as duas decisões são aplicadas, de forma independente

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-010 Despacho que exige assinatura não conclui o avanço no mesmo clique** *(CA11)*
    Dado que o despacho exige assinaturas
    Quando eu escolho avançar etapa e clico em "Emitir e Assinar"
    Então verifico que o avanço **não** se conclui no mesmo clique, porque as solicitações de assinatura são disparadas após a emissão

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-011 Grupo de sigilo só aparece quando o despacho tem opções de sigilo** *(CA12)*
    Dado que o módulo/serviço/assunto tem opções de privacidade configuradas
    Quando eu emito um despacho customizado de etapa
    Então verifico que o grupo de sigilo é exibido, herdado dessa configuração — e que num despacho sem opções de sigilo o grupo não aparece

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-012 Regressão SGV-6373 — setores mantidos ao navegar etapas** *(CA13)*
    Dado que eu tenho um assunto/serviço com setores configurados nas Regras de tramitação
    Quando eu avanço e retrocedo etapas pelo contêiner "Próximo passo do documento"
    Então verifico que os setores configurados permanecem mantidos

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

> [!danger] Bugs encontrados

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9042)

---

> [!tip] Observações

Análise completa (rodadas de refinamento, gate de doc, regras extraídas do Figma e divergências com o Notion) na mesa arquivada: [[QA Workspace/04 Conhecimento/9042 - Refinamento Ações de Tramitação e Encerramento na Emissão de Despacho|9042 - Refinamento]].

**Gate de doc** (2026-07-29): cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]]. As regras desta melhoria foram **incorporadas à doc de Tramitação** na mesma data — a doc respalda os critérios acima.

**Vizinhança com a [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]]** (aberta em 29/07): mesma família de ações ("Encerrar para mim" / "Encerrar para meu setor"), e esta melhoria declara que essas regras seguem o que **já está implementado na plataforma**. São coisas distintas — aqui é o **ato** de encerrar na emissão de despacho, lá é o **estado** da toolbar depois de encerrado — mas se o fix de um tocar o outro vale **reteste cruzado**.

---

## Histórico

- 2026-07-29 - 📝 Melhoria refinada (critérios de aceite prontos; card destilado da mesa em `05 Refinar/`)
- 2026-07-29 - ℹ️ Contexto: **aprovada em DEV por outro QA** (não pelo Rafael) — por isso não há registro de validação em DEV na daily dele. Validação em homologação em andamento.
