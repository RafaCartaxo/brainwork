---
tags:
  - bug
  - qa
task: "11151"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-28
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Documento não é criado com anexo no módulo e no assunto e serviço

### Descrição

Durante validação foi identificado que a criação de documento falha quando há arquivo anexado no campo de anexo do módulo e no campo de anexo do assunto e serviço — o sistema retorna erro em vez de criar o documento.

---

### Passo a passo para reproduzir

Dado que eu tento criar um documento
E preencho o campo de anexo do módulo com um arquivo
E preencho o campo de anexo do assunto e serviço com um arquivo
Quando eu confirmo a criação
Então verifico que o documento não é criado com sucesso e o sistema retorna erro

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11151)

![[11151 - erro ao criar documento com anexo no modulo e assunto.mp4]]

---

### Resultado Esperado

- Documento é criado com sucesso mesmo com arquivo anexado no campo de anexo do módulo e no campo de anexo do assunto e serviço

---

### Critérios de aceite

- [ ] Documento é criado com sucesso com anexo no campo do módulo
- [ ] Documento é criado com sucesso com anexo no campo de assunto e serviço
- [ ] Documento é criado com sucesso com os dois campos de anexo preenchidos ao mesmo tempo

---

### Casos de Teste Básicos

#### **CT-B01 Criar documento com anexo no módulo e no assunto e serviço**

**Dado** que eu tento criar um documento
**E** preencho o campo de anexo do módulo com um arquivo
**E** preencho o campo de anexo do assunto e serviço com um arquivo
**Quando** eu confirmo a criação
**Então** o documento é criado com sucesso, sem erro

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
- Observações: Achado testando criação/anexo de documento no novo ambiente de homologação (nova arquitetura). Não bate exatamente com nenhum CT já listado na SGV-8321 — CT-005 é "criar documento" sem anexo, CT-023 é "anexar arquivo em campo de texto longo" (contexto diferente dos campos de anexo do módulo/assunto e serviço). Não marquei nenhum CT da 8321 como reprovado por isso — avaliar se vale um CT novo lá.
- Histórico:
    - 2026-08-28 - 🐛 Bug cadastrado
