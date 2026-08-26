---
tags:
  - bug
  - qa
  - documento
task: "10958"
pai: ""
prioridade: media
status: resolvido
data_inicio: 2026-08-26
data_fim: 2026-08-26
responsavel: Rafael
cadastrado_por: Rafael
modulo: documento
ambiente: HML
---
# Mensagem exibida corretamente ao revogar documento

> [!info] Card criado já aprovado — título inferido
> Sem descrição detalhada; título e escopo inferidos a partir do nome da evidência (`10958 - revogar documento mensagem ok.mp4`).

### Descrição

Durante validação foi confirmado que a mensagem exibida ao revogar um documento está correta.

---

### Passo a passo para reproduzir

Dado que eu tenho um documento
Quando eu revogo esse documento
Então verifico que a mensagem exibida está correta

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10958)

![[10958 - revogar documento mensagem ok.mp4]]

---

### Resultado Esperado

A mensagem exibida ao revogar um documento reflete corretamente a ação realizada.

---

### Critérios de aceite

- [x] A mensagem exibida ao revogar o documento está correta

---

### Casos de Teste Básicos

#### **CT-B01 Mensagem correta ao revogar documento**

**Dado** que eu tenho um documento
**Quando** eu revogo esse documento
**Então** a mensagem exibida está correta

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10958 - revogar documento mensagem ok.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação (inferido)

---

### Informações adicionais

- Demanda relacionada: SGV-10958 (Notion)
- Observações:
    - Sem descrição original do problema — completar se precisar de mais contexto (qual era a mensagem incorreta antes da correção).
- Histórico:
    - 2026-08-26 - 🐛✅ SGV-10958 - Bug cadastrado e já aprovado em homologação
