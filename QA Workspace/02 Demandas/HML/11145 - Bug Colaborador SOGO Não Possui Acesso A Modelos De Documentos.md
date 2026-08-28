---
tags:
  - bug
  - qa
task: "11145"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-28
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: Modelos de Documentos
ambiente: HML
---
# Colaborador SOGO não possui acesso a modelos de documentos

### Descrição

Durante validação foi identificado que o colaborador SOGO não consegue visualizar os modelos de documento de um cliente ao qual está vinculado — o sistema retorna erro de permissão em vez de exibir a listagem.

---

### Passo a passo para reproduzir

Dado que acesso o ambiente como colaborador SOGO
E seleciono e entro em um cliente
Quando clico em "Modelos de documento"
Então verifico a mensagem `Error: You don't have access to do that`

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11145)

![[11145 - Colaborador SOGO não possui acesso a modelos de documentos.mp4]]

---

### Resultado Esperado

- Colaborador SOGO consegue visualizar a listagem de modelos de documento do cliente normalmente, sem mensagem de erro

---

### Critérios de aceite

- [ ] Colaborador SOGO acessa "Modelos de documento" dentro de um cliente sem receber erro de permissão
- [ ] A listagem de modelos é exibida corretamente pro colaborador SOGO

---

### Casos de Teste Básicos

#### **CT-B01 Colaborador SOGO acessa modelos de documento sem erro**

**Dado** que acesso o ambiente como colaborador SOGO
**E** seleciono e entro em um cliente
**Quando** clico em "Modelos de documento"
**Então** visualizo a listagem de modelos normalmente, sem mensagem de erro

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

- Demanda relacionada:
- Observações:
- Histórico:
    - 2026-08-28 - 🐛 Bug cadastrado
