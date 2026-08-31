---
tags:
  - bug
  - qa
task: "11185"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-31
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Documento não abre na área de solicitações realizadas do cidadão

### Descrição

Durante validação foi identificado que, ao acessar um documento como cidadão na área de solicitações realizadas, o documento não abre — clicar nele diversas vezes não tem efeito nenhum.

---

### Passo a passo para reproduzir

Dado que acesso o sistema como cidadão
E vou até a área de solicitações realizadas
Quando clico em um documento pra abrir
Então verifico que, mesmo clicando diversas vezes, o documento não abre

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11185)

*Capturada pelo celular (iPhone/Safari) — ainda não está no vault. Adicionar aqui quando o Rafael passar o arquivo.*

---

### Resultado Esperado

- Documento abre normalmente ao clicar, na área de solicitações realizadas do cidadão

---

### Critérios de aceite

- [ ] O documento abre ao clicar, na área de solicitações realizadas do cidadão

---

### Casos de Teste Básicos

#### **CT-B01 Documento abre na área de solicitações realizadas do cidadão**

**Dado** que acesso o sistema como cidadão
**E** vou até a área de solicitações realizadas
**Quando** clico em um documento pra abrir
**Então** o documento abre normalmente

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Homologação
- Dispositivo: iPhone, Safari (mobile)

---

### Informações adicionais

- Demanda relacionada:
- Observações: Reproduzido em mobile (iPhone/Safari) — vale confirmar se também reproduz em desktop antes de considerar o critério de aceite fechado só pelo recorte mobile.
- Histórico:
    - 2026-08-31 - 🐛 Bug cadastrado
