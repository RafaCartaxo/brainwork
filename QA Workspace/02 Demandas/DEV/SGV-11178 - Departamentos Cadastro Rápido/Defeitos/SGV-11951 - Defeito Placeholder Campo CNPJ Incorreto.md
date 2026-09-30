---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11951"
pai: "SGV-11178"
prioridade: media
status: aberto
data_inicio: 2026-09-30
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Placeholder do campo CNPJ incorreto

### Descrição

No formulário de cadastro rápido de Pessoa Jurídica, o campo CNPJ exibe placeholder incorreto — mostra `00.000...` em vez do padrão esperado `XX.XXX.XXX/XXXX-XX`.

---

### Passo a passo para reproduzir

**Dado** que o cadastro rápido esteja com a opção Pessoa Jurídica selecionada
**Quando** o campo CNPJ for exibido vazio
**Então** o placeholder mostra `00.000...` em vez de `XX.XXX.XXX/XXXX-XX`

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11951)

![[11951 - Placeholder divergente.png]]

---

### Resultado Esperado

Placeholder do campo CNPJ segue o padrão `XX.XXX.XXX/XXXX-XX`.

---

### Critérios de aceite

- [ ] Campo CNPJ do cadastro rápido de Pessoa Jurídica exibe o placeholder `XX.XXX.XXX/XXXX-XX`

---

### Casos de Teste Básicos

#### **CT-B01 Placeholder do campo CNPJ**

**Dado** que o cadastro rápido esteja com a opção Pessoa Jurídica selecionada
**Quando** o campo CNPJ estiver vazio
**Então** o placeholder exibido deve ser `XX.XXX.XXX/XXXX-XX`

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11951 - Placeholder divergente.png]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda|SGV-11178]]
- Observações: achado durante a validação da SGV-11178 — [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-037|CT-037]] (critério C37, criado a partir deste achado).
- Histórico:
    - 2026-09-30 - 🐛 Defeito cadastrado (placeholder do campo CNPJ incorreto)
