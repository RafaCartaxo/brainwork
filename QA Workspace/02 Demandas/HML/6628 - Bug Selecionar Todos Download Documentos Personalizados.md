---
tags:
  - bug
  - qa
  - documento
task: "6628"
prioridade: ""
status: aberto
data_inicio: 2026-07-27
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Selecionar Todos (Download de documentos personalizados)

### Descrição

Na tela de download de documentos personalizados, a opção "Selecionar todos" não refletia corretamente o estado da seleção (desmarcado/parcial/marcado) nem selecionava/desmarcava todos os documentos e despachos disponíveis ao ser clicada.

---

### Resultado Esperado

A opção "Selecionar todos" reflete corretamente o estado da seleção (desmarcado quando nada selecionado, parcial quando parte selecionada, marcado quando tudo selecionado) e seleciona/desmarca todos os documentos e despachos disponíveis ao ser clicada.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://6628)

![[6628 - selecionar todos download documentos personalizados aprovado em dev.mp4]]

---

### Critérios de aceite

- [x] "Selecionar todos" exibido desmarcado quando nenhum documento estiver selecionado
- [x] "Selecionar todos" exibido em estado parcial quando parte dos documentos estiver selecionada
- [x] "Selecionar todos" exibido marcado quando todos os documentos estiverem selecionados
- [x] Clicar em "Selecionar todos" seleciona/desmarca todos os documentos e despachos disponíveis

---

### Casos de Teste Básicos

#### **CT-B01 Exibir "Selecionar todos" desmarcado quando nenhum documento estiver selecionado**

**Dado** que eu acesse a tela de download de documentos personalizados
**Quando** nenhum documento estiver selecionado
**Então** a opção "Selecionar todos" deve ser exibida em estado desmarcado

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[6628 - selecionar todos download documentos personalizados aprovado em dev.mp4]]

---

#### **CT-B02 Exibir "Selecionar todos" em estado parcial quando parte dos documentos estiver selecionada**

**Dado** que eu acesse a tela de download de documentos personalizados
**Quando** eu selecionar apenas parte dos documentos e despachos disponíveis
**Então** a opção "Selecionar todos" deve ser exibida em estado parcial (indeterminado)

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[6628 - selecionar todos download documentos personalizados aprovado em dev.mp4]]

---

#### **CT-B03 Exibir "Selecionar todos" marcado quando todos os documentos estiverem selecionados**

**Dado** que eu acesse a tela de download de documentos personalizados
**Quando** eu selecionar manualmente todos os documentos e despachos disponíveis
**Então** a opção "Selecionar todos" deve ser exibida em estado marcado

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[6628 - selecionar todos download documentos personalizados aprovado em dev.mp4]]

---

#### **CT-B04 Selecionar e desmarcar todos os documentos ao clicar em "Selecionar todos"**

**Dado** que eu acesse a tela de download de documentos personalizados
**Quando** eu clicar na opção "Selecionar todos"
**Então** todos os documentos e despachos disponíveis devem ser selecionados, e ao clicar novamente, todos devem ser desmarcados

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[6628 - selecionar todos download documentos personalizados aprovado em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: DEV (aprovada — segue pra homologação)

---

### Informações adicionais

- Demanda relacionada: SGV-6628. Sem card prévio no vault — primeira vez que ganha um card formal, apesar de já ter histórico de teste desde 10/07 (CTs originalmente descritos direto na daily daquele dia, sem card).
- **Histórico anterior (antes deste card existir)**: reaberta em homologação em 10/07 (1 critério pendente, evidência antiga em `Evidências/Homologação/6628 - botão selecionar todos criterios de aceite 1 pendente.mp4` — mantida, não apagada); retestada em 13/07 (validada por outro QA, sem detalhe registrado do resultado). Correção adicional do dev entregue depois — hoje (27/07) retestada e **aprovada em DEV**; segue pra validação em homologação.
- Histórico:
    - 2026-07-10 - 🔴 Reaberta em homologação (1 critério pendente)
    - 2026-07-13 - 🔁 Retestada (validado por outro QA)
    - 2026-07-27 - 🔁 Retestada e aprovada em DEV
