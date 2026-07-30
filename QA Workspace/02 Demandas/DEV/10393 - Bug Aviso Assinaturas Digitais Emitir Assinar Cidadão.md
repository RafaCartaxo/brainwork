---
tags:
  - bug
  - qa
  - assinatura
  - despacho
task: "10393"
prioridade: media
status: aberto
data_inicio: 2026-07-28
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: DEV
---
# Aviso de assinaturas digitais é exibido ao emitir e assinar despacho como cidadão

### Descrição

Durante validação foi identificado que, ao selecionar **"Emitir e assinar"** na criação de um despacho como **cidadão**, o sistema exibe o aviso de confirmação **"Assinaturas digitais"** ("Deseja utilizar outro tipo de assinatura digital?", com os botões "Voltar" e "Sim") antes de prosseguir. O aviso não deveria ser exibido — a ação deve levar direto para a tela de **"Realização de assinaturas"**.

---

### Passo a passo para reproduzir

Dado que o usuário acesse o ambiente como cidadão
E abra um documento em que precise responder uma solicitação
E crie um novo despacho, preenchendo a descrição (com ou sem anexos)
Quando acionar a seta ao lado do botão "Emitir" e selecionar "Emitir e assinar"
Então é exibido o aviso "Assinaturas digitais" com a pergunta "Deseja utilizar outro tipo de assinatura digital?", em vez de seguir direto para a tela de "Realização de assinaturas"

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10393)

![[10393 - aviso assinaturas digitais exibido ao emitir e assinar como cidadao.mp4]]

---

### Resultado Esperado

Ao selecionar "Emitir e assinar" como cidadão, nenhum aviso de confirmação é exibido: o despacho é emitido e o usuário segue direto para a tela de "Realização de assinaturas", com os locais de assinatura do despacho e seus anexos — mesmo comportamento do fluxo de servidor.

---

### Critérios de aceite

- [ ] "Emitir e assinar" como cidadão não exibe o aviso "Assinaturas digitais"
- [ ] Ao selecionar "Emitir e assinar" como cidadão, o usuário é levado direto para a tela de "Realização de assinaturas", com os locais do despacho e seus anexos
- [ ] O despacho é emitido e a assinatura pode ser concluída normalmente (tipo SoGov como default, ICP disponível no seletor)
- [ ] Sem regressão no "Emitir" simples como cidadão (segue sem aviso e sem tela de assinatura)
- [ ] Sem regressão no "Emitir e assinar" como servidor (segue direto para a tela de assinaturas)

---

### Casos de Teste Básicos

#### **CT-B01 Emitir e assinar como cidadão não exibe aviso de confirmação**

**Dado** que o usuário esteja logado como cidadão
**E** crie um novo despacho com descrição preenchida
**Quando** selecionar "Emitir e assinar"
**Então** nenhum aviso de confirmação é exibido e a tela de "Realização de assinaturas" é aberta

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B02 Assinatura do despacho é concluída pelo cidadão**

**Dado** que o cidadão tenha selecionado "Emitir e assinar" em um despacho com anexo
**E** esteja na tela de "Realização de assinaturas"
**Quando** escolher o tipo de assinatura e confirmar em "Assinar"
**Então** a assinatura é realizada no despacho e nos anexos selecionados

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 Emitir simples como cidadão segue sem aviso (regressão)**

**Dado** que o usuário esteja logado como cidadão
**E** crie um novo despacho com descrição preenchida
**Quando** selecionar "Emitir"
**Então** o despacho é emitido sem aviso de confirmação e sem abrir a tela de assinaturas

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B04 Emitir e assinar como servidor segue sem aviso (regressão)**

**Dado** que o usuário esteja logado como servidor
**E** crie um novo despacho com descrição preenchida
**Quando** selecionar "Emitir e assinar"
**Então** nenhum aviso de confirmação é exibido e a tela de "Realização de assinaturas" é aberta

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento (ambiente de branch `dev-diogo-nobrega`, portal do cidadão)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/7829 - Bug Anexos Despacho Não Carregados Emitir Assinar Cidadão|SGV-7829]] — mesma tela ("emitir e assinar" como cidadão), problema diferente (anexos que não carregam)

- Observações:
    - **Gate de doc**: a doc do módulo ([[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Emitindo um despacho e assinando-o|Assinaturas — Emitindo um despacho e assinando-o]]) descreve o fluxo do cidadão como Tipo de assinatura + Locais, seguido da confirmação por senha; **não prevê nenhum aviso/confirmação intermediário**. Resultado esperado respaldado pela doc, sem divergência a registrar.
    - Fluxo reproduzido na resposta a uma solicitação, com anexo em PDF ("Proc Adm - Serviço 2 000036/000008/2026"). Ao responder "Sim" no aviso, o sistema segue normalmente para a tela de assinaturas com "Assinatura SoGov" selecionada — ou seja, o aviso não muda nada no fluxo, só adiciona um passo.

- Histórico:
    - 2026-07-28 - 🐛 Bug cadastrado
