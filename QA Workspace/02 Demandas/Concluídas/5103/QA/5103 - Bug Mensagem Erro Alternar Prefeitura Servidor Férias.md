---
tags:
  - bug
  - qa
  - organograma
task: "5103"
prioridade: alta
status: aberto
data_inicio: 2026-07-27
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: organograma
ambiente: DEV
---
# Mensagem de erro ao alternar para prefeitura onde servidor está de férias

### Descrição

Ao alternar para uma prefeitura onde o servidor logado está de férias, o sistema exibe uma mensagem de erro em vez de tratar o cenário corretamente. (Origem Notion SGV-5103, Matheus Godoi.)

---

### Resultado Esperado

Ao alternar para uma prefeitura onde o servidor está de férias, o sistema trata o cenário sem exibir mensagem de erro.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://5103)

![[5103 - mensagem erro alternar prefeitura servidor ferias reaberta em dev.mp4]]

---

### Critérios de aceite

- [ ] Alternar para prefeitura com servidor de férias não exibe mensagem de erro

---

### Casos de Teste Básicos

#### **CT-B01 Alternância de prefeitura com servidor de férias não gera erro**

**Dado** um servidor de férias com acesso a múltiplas prefeituras
**Quando** o usuário alterna para a prefeitura onde esse servidor está de férias
**Então** o sistema não exibe mensagem de erro

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[5103 - mensagem erro alternar prefeitura servidor ferias reaberta em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: DEV

---

### Informações adicionais

- Demanda relacionada: SGV-5103 (origem Notion; item novo trazido pela reconciliação com o Release homolog de 24/07; Triagem SP15, grupo "Pronto pra teste em dev"; Matheus Godoi).
- Sem card/registro prévio no vault — primeira entrada aqui. Testado e **reaberto em DEV** — bug reproduz, aguardando correção do dev.
- Histórico:
    - 2026-07-27 - 🔴 Reaberta em DEV
