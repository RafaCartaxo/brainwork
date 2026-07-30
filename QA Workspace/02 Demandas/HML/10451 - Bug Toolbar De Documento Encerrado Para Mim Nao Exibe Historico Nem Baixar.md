---
tags:
  - bug
  - qa
  - tramitacao
task: "10451"
prioridade: ""
status: aberto
data_inicio: 2026-07-29
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: tramitacao
ambiente: HML
---
# Toolbar de documento encerrado "para mim" não exibe histórico nem baixar documento

### Descrição

Ao encerrar **para mim** um documento que possui **fluxo de trabalho**, a toolbar de encerramento passa a exibir **apenas "Reabrir documento"**.

Faltam as ações de **histórico** e de **baixar documento**, que deveriam continuar disponíveis — encerrar o documento remove a capacidade de tramitar, não a de consultar e obter o que já foi produzido. Do jeito que está, para simplesmente ver o histórico ou baixar o arquivo o usuário é obrigado a **reabrir o documento**, alterando o status de algo que ele só queria consultar.

---

### Passo a passo para reproduzir

Dado que eu tenho um documento que possui fluxo de trabalho configurado e iniciado
E que eu tenho permissão de encerramento nesse documento
Quando eu encerro o documento para mim
Então verifico que a toolbar de encerramento exibe apenas "Reabrir documento", sem as ações de histórico e de baixar documento

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10451)

![[10451 - toolbar de documento encerrado para mim mostra so reabrir sem historico e baixar.mp4]]

---

### Resultado Esperado

A toolbar de um documento encerrado "para mim" exibe, além de **Reabrir documento**, as ações de **histórico** e de **baixar documento** — permitindo consultar e obter o documento **sem precisar reabri-lo**.

---

### Critérios de aceite

- [ ] Documento com fluxo de trabalho encerrado "para mim" exibe a ação de **histórico** na toolbar
- [ ] Documento com fluxo de trabalho encerrado "para mim" exibe a ação de **baixar documento** na toolbar
- [ ] A ação **Reabrir documento** continua sendo exibida
- [ ] Consultar histórico e baixar documento **não exigem reabrir** o documento
- [ ] As ações exibidas respeitam a tabela de permissões de encerramento (ver Informações adicionais)

---

### Casos de Teste Básicos

#### **CT-B01 Toolbar após encerrar para mim, documento com fluxo de trabalho**

**Dado** que eu tenho um documento com fluxo de trabalho configurado e iniciado
**Quando** eu encerro o documento para mim
**Então** verifico que a toolbar exibe Reabrir documento, histórico e baixar documento

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10451 - toolbar de documento encerrado para mim mostra so reabrir sem historico e baixar.mp4]]

---

#### **CT-B02 Toolbar após encerrar para mim, documento sem fluxo de trabalho**

**Dado** que eu tenho um documento **sem** fluxo de trabalho
**Quando** eu encerro o documento para mim
**Então** verifico que a toolbar exibe Reabrir documento, histórico e baixar documento

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 Toolbar após encerrar para meu setor**

**Dado** que eu tenho um documento com fluxo de trabalho configurado e iniciado
**Quando** eu encerro o documento para meu setor
**Então** verifico que a toolbar exibe as ações de consulta esperadas (histórico e baixar documento), além de Reabrir documento

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-10451** — número **inferido do nome da gravação** (`10451.mp4`, 29/07 15:25), conforme a convenção de nomear a evidência com o número do card. ⚠️ **Confirmar**: foi o único card de hoje cujo número não veio dito na mensagem.
- ⚠️ **Ambiente inferido como homologação** — é onde o Rafael está validando hoje e onde a gravação foi feita. Corrigir se foi em DEV.
- **Prioridade não definida** — não foi declarada como impeditiva. Há workaround (reabrir o documento), mas o workaround **altera o status** de um documento que o usuário só queria consultar, o que é efeito colateral indesejado. Definir na triagem.
- **Gate de doc** (2026-07-29, fluxo 8): **gap de documentação**, não divergência. Nenhuma doc descreve quais ações a toolbar exibe num documento encerrado:
    - [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]] cobre os **status** e diz que sair de **Encerrado** só acontece via Reabrir/Retomar documento — o que explica o "Reabrir documento" aparecer, mas nada afirma sobre histórico e download.
    - A doc de Mesa de trabalho só descreve toolbar para o status **Pausado**: *"Quando um documento é colocado em pausa no setor dono, possui todas as funcionalidades de tramitação na toolbar"*. Encerrado não tem equivalente escrito.
    - [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] já registra isso como **dúvida em aberto**: a doc de origem manda *"averiguar design no protótipo para visualizar nova toolbar para setores dono"* — ou seja, o comportamento da toolbar **nunca foi descrito em texto**, ficou só no protótipo. Este bug é a materialização dessa lacuna.
- **Fonte que fecharia o gap**: o Rafael tem uma **tabela com as permissões possíveis** de encerramento. Exportação **postergada por decisão dele em 29/07** (prioridade era agilidade). Quando entrar, ela resolve o critério de aceite em aberto e alimenta [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]].
- **A confirmar no diagnóstico** (o que os CTs isolam): o defeito depende do **fluxo de trabalho** (CT-B02, documento sem workflow) ou vale para todo documento encerrado? E replica em **encerrar para meu setor** (CT-B03)? A resposta define o escopo do fix.
- **Vizinhança com a [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]]** — mesma família de ações ("Encerrar para mim" / "Encerrar para meu setor"), e a 9042 afirma que essas regras seguem o que **já está implementado na plataforma**. São coisas diferentes (a 9042 é o *ato* de encerrar na emissão de despacho; este bug é o *estado* da toolbar depois de encerrado), mas se o fix de um mexer no outro vale reteste cruzado.
- Histórico:
    - 2026-07-29 - 🐛 SGV-10451 - Bug cadastrado (gap de doc: toolbar de documento encerrado não descrita em nenhuma doc; tabela de permissões postergada)
