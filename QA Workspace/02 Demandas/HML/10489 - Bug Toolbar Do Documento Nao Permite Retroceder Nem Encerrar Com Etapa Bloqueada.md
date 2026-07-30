---
tags:
  - bug
  - qa
  - tramitacao
task: "10489"
prioridade: ""
status: aberto
data_inicio: 2026-07-30
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: tramitacao
ambiente: HML
---
# Toolbar do documento não permite retroceder nem encerrar quando a etapa está bloqueada por pendência

### Descrição

Quando a etapa atual tem ação obrigatória pendente (despacho customizado não emitido ou assinatura não concluída), o select de movimentação do contêiner "Próximo passo do documento" fica desabilitado — **isso é o comportamento esperado**. O problema é a saída: a **toolbar do documento também não oferece retroceder nem encerrar**.

A regra diz o contrário. Nesse estado, a toolbar é justamente a **válvula de escape** — o único caminho para retroceder ou encerrar enquanto a pendência existe.

Sem ela, o documento fica **preso na etapa**: as duas vias de movimentação estão fechadas ao mesmo tempo, e a única forma de destravar é cumprir a pendência. Se a pendência não puder ser cumprida por quem está ali (assinatura de outro servidor, despacho que deveria ter sido emitido em outra etapa), não há saída pela interface.

---

### Passo a passo para reproduzir

**Dado** que eu tenho um documento com fluxo de trabalho configurado e iniciado
**E** que a etapa atual tem ação obrigatória pendente (despacho customizado não emitido)
**Quando** eu abro a emissão de despacho e vejo o select de movimentação desabilitado
**E** recorro à toolbar do documento para retroceder ou encerrar
**Então** verifico que a toolbar **também não oferece** retroceder nem encerrar, e o documento fica sem saída da etapa

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10489)

![[10489 - toolbar nao permite retroceder nem encerrar com etapa bloqueada.mp4]]

*Evidência compartilhada com a [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] — mesmo vídeo, cópia renomeada. Lá é a gravação do CT-008 (reprovado) e do CT-010.*

---

### Resultado Esperado

Com a etapa bloqueada por pendência, a **toolbar do documento continua oferecendo retroceder e encerrar**, funcionando como a via alternativa de movimentação — o bloqueio vale para o select do contêiner, não para a toolbar.

---

### Critérios de aceite

- [ ] Com etapa bloqueada por **despacho customizado não emitido**, a toolbar do documento oferece **retroceder**
- [ ] Com etapa bloqueada por **despacho customizado não emitido**, a toolbar do documento oferece **encerrar**
- [ ] O mesmo vale quando o bloqueio vem de **assinatura não concluída**
- [ ] O select de movimentação do contêiner **continua desabilitado** nesse estado (não regredir o bloqueio, que é o comportamento correto)
- [ ] Em etapa **sem** pendência, a toolbar segue funcionando como hoje

---

### Casos de Teste Básicos

#### **CT-B01 Toolbar com etapa bloqueada por despacho customizado não emitido**

**Dado** que a etapa atual tem um despacho customizado **não emitido**
**E** que o select de movimentação do contêiner está desabilitado
**Quando** eu abro a toolbar do documento
**Então** verifico que retroceder e encerrar estão disponíveis por esse caminho

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10489 - toolbar nao permite retroceder nem encerrar com etapa bloqueada.mp4]]

---

#### **CT-B02 Toolbar com etapa bloqueada por assinatura não concluída**

**Dado** que a etapa atual tem uma **assinatura não concluída**
**E** que o select de movimentação do contêiner está desabilitado
**Quando** eu abro a toolbar do documento
**Então** verifico que retroceder e encerrar estão disponíveis por esse caminho

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 Controle — toolbar em etapa sem pendência**

**Dado** que a etapa atual **não** tem pendências
**Quando** eu abro a toolbar do documento
**Então** verifico que retroceder e encerrar estão disponíveis normalmente

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

- Demanda relacionada: **SGV-10489** (número informado pelo Rafael em 30/07).
- **Origem**: reprovação do **CT-008** da [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] na validação em homologação. O CA9 daquele card está marcado como reprovado e aponta pra cá.
- **Prioridade não definida** — não foi declarada. Vale considerar na triagem que o efeito é **documento preso na etapa**, sem saída pela interface quando a pendência não pode ser cumprida por quem está ali.
- **Gate de doc** (2026-07-30, fluxo 8): **divergência confirmada**, não gap. [[QA Workspace/04 Conhecimento/Módulos/Tramitação#Ações de destino na emissão de despacho (SGV-9042)|Tramitação § Ações de destino na emissão de despacho]] registra literalmente:

    > "Nesse estado, **retroceder ou encerrar só pela toolbar do documento**."

    A palavra "só" é o ponto: a doc não apresenta a toolbar como alternativa conveniente, e sim como **a única** via nesse estado. Se ela não oferece as ações, a regra não tem como ser cumprida por caminho nenhum. Regra escrita e contrariada — o card aponta a doc, não interpretação da QA.
- **A confirmar no diagnóstico**: o defeito depende do **tipo de pendência**? O CT-B01 cobre despacho customizado não emitido (o que foi reprovado) e o **CT-B02** cobre assinatura não concluída. Se só um dos dois falha, o fix é pontual; se os dois, é o estado bloqueado que apaga as ações da toolbar. O **CT-B03** é controle: confirma que a toolbar funciona normalmente sem pendência, isolando o defeito no estado e não na toolbar em geral.
- **Vizinhança**: é o **terceiro** bug de toolbar em dois dias, junto com a [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]] (toolbar de documento encerrado sem histórico nem baixar). Os dois são "a toolbar não mostra a ação que deveria, num estado específico do documento" — e a [[QA Workspace/04 Conhecimento/Módulos/Tramitação|doc de Tramitação]] registra como **dúvida em aberto** que o comportamento da toolbar por estado **nunca foi descrito em texto**, só no protótipo. Vale tratar como sintoma da mesma lacuna: a **tabela de permissões/ações da toolbar por estado** (pendente de exportação) fecharia os dois.
- Histórico:
    - 2026-07-30 - 🐛 SGV-10489 - Bug cadastrado (reprovação do CT-008 da SGV-9042; divergência confirmada contra a regra "retroceder ou encerrar só pela toolbar do documento")
