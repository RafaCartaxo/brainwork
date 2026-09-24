---
tags:
  - bug
  - qa
  - clientes
task: "8386"
prioridade: ""
status: resolvido
data_inicio: 2026-07-27
data_fim: 2026-07-27
responsavel: Rafael
cadastrado_por: ""
modulo: clientes
ambiente: HML
---
# Ordenação Z-A de clientes com ícone invertido

### Descrição

Na listagem de clientes, ao ordenar por ordem decrescente (Z-A), o ícone exibido ficava invertido (indicando o sentido oposto ao aplicado). (Origem Notion SGV-8386, Lucas Lacerda.)

---

### Resultado Esperado

Ao ordenar a listagem de clientes em Z-A, o ícone exibido reflete corretamente o sentido de ordenação aplicado.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://8386)

![[8386 - ordenacao za clientes icone corrigido aprovado em homologacao.mp4]]

---

### Critérios de aceite

- [x] Ícone de ordenação Z-A da listagem de clientes reflete o sentido correto

---

### Casos de Teste Básicos

#### **CT-B01 Ordenação Z-A exibe ícone correto**

**Dado** a listagem de clientes
**Quando** o usuário ordena por Z-A
**Então** o ícone exibido corresponde ao sentido de ordenação decrescente

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[8386 - ordenacao za clientes icone corrigido aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: SGV-8386 (origem Notion; item novo trazido pela reconciliação com o Release homolog de 24/07; Triagem SP15, grupo "Pronto pra homologação"; Lucas Lacerda).
- Sem export completo — card criado direto a partir do ticket + validação em homologação.
- Prioridade não informada no Notion (`—`).
- Histórico:
    - 2026-07-27 - ✅ Aprovada em homologação
