---
tags:
  - bug
  - qa
task: "11249"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-02
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Assinatura de documento ou despacho não é concluída com sucesso

### Descrição

Durante validação foi identificado que, ao criar um documento/despacho — com ou sem anexo — e solicitar a assinatura de um servidor, ao tentar assinar a assinatura não é concluída com sucesso. Achado no mesmo ambiente de homologação (nova arquitetura) da [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]].

**Vizinho da [[QA Workspace/02 Demandas/HML/11215 - Bug Documento Não Carrega Para Realizar Assinatura|SGV-11215]], mas ponto de falha diferente**: na 11215 o documento não chega a carregar ao clicar pra assinar — a tentativa nem começa. Aqui o documento carrega e o fluxo de assinatura é iniciado, mas a assinatura em si não é concluída com sucesso.

---

### Passo a passo para reproduzir

Dado que crio um documento/despacho, com ou sem anexo
E solicito a assinatura de um servidor
Quando tento assinar
Então verifico que a assinatura não é concluída com sucesso

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11249)

![[11249 - Erro ao assinar documento.mp4]]

---

### Resultado Esperado

- Assinatura é concluída com sucesso ao assinar o documento/despacho, com ou sem anexo

---

### Critérios de aceite

- [ ] Documento/despacho **sem anexo**: assinatura é concluída com sucesso
- [ ] Documento/despacho **com anexo**: assinatura é concluída com sucesso

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura é concluída sem anexo**

**Dado** que crio um documento/despacho sem anexo
**E** solicito a assinatura de um servidor
**Quando** tento assinar
**Então** a assinatura é concluída com sucesso

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B02 Assinatura é concluída com anexo**

**Dado** que crio um documento/despacho com anexo
**E** solicito a assinatura de um servidor
**Quando** tento assinar
**Então** a assinatura é concluída com sucesso

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]]
- Observações: Bate com o **CT-002** ("Assinar um documento continua funcionando") da SGV-8321 — já reprovado por [[QA Workspace/02 Demandas/HML/11215 - Bug Documento Não Carrega Para Realizar Assinatura|SGV-11215]]. Este card documenta outra manifestação do mesmo fluxo quebrado: mesmo quando o documento carrega, a assinatura não conclui.
- Histórico:
    - 2026-09-02 - 🐛 Bug cadastrado
