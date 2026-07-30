---
tags:
  - bug
  - qa
  - servicos-e-assuntos
task: "6373"
prioridade: ""
status: aberto
data_inicio: 2026-07-27
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: servicos-e-assuntos
ambiente: DEV
---
# Setores das Regras de tramitação não são mantidos ao avançar/retroceder etapas na criação de A&S

### Descrição

Na criação de um Assunto e Serviço (A&S), os setores configurados nas Regras de tramitação não são mantidos quando o usuário avança ou retrocede entre as etapas do wizard de criação — os setores selecionados se perdem/resetam.

---

### Resultado Esperado

Ao avançar ou retroceder entre as etapas da criação de A&S, os setores configurados nas Regras de tramitação permanecem mantidos, sem perder a seleção.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://6373)

![[6373 - setores regras tramitacao nao mantidos avancar retroceder etapas criacao as reaberta em dev.mp4]]

---

### Critérios de aceite

- [ ] Setores das Regras de tramitação permanecem mantidos ao avançar/retroceder etapas na criação de A&S

---

### Casos de Teste Básicos

#### **CT-B01 Setores mantidos ao navegar entre etapas**

**Dado** a criação de A&S com setores configurados nas Regras de tramitação
**Quando** o usuário avança e depois retrocede entre as etapas do wizard
**Então** os setores configurados permanecem selecionados

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[6373 - setores regras tramitacao nao mantidos avancar retroceder etapas criacao as reaberta em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: DEV

---

### Informações adicionais

- Demanda relacionada: SGV-6373. Sem card/registro prévio no vault — primeira entrada aqui.
- Testado e **reaberto em DEV** — bug ainda reproduz, aguardando correção do dev.
- Histórico:
    - 2026-07-27 - 🔴 Reaberta em DEV
