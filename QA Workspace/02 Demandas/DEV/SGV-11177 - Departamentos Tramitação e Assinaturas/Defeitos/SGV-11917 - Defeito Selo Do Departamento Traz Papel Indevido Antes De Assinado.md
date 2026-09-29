---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11917"
pai: "SGV-11177"
prioridade: media
status: aberto
data_inicio: 2026-09-29
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Selo do departamento traz papel indevido antes de assinado

### Descrição

Antes de assinado (a posicionar/posicionado), o selo de assinatura de um departamento traz o campo `$papel` com valor "signatario" — não deveria trazer `$papel` nesse caso, só razão social e nome do departamento. Depois de assinado já está correto.

---

### Passo a passo para reproduzir

**Dado** que a assinatura seja solicitada a um departamento
**Quando** o selo estiver no estado a posicionar ou posicionado (antes de assinado)
**Então** verifico que aparece o campo `$papel` com valor "signatario", quando não deveria aparecer

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11917)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

### Resultado Esperado

Selo mostra só razão social e nome do departamento, sem `$papel`, nos estados a posicionar/posicionado. Ver [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c34|C34]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-034|CT-034]].

---

### Critérios de aceite

- [ ] Selo do departamento, antes de assinado, não mostra `$papel`

---

### Casos de Teste Básicos

#### **CT-B01 Selo do departamento sem papel antes de assinado**

**Dado** que a assinatura seja solicitada a um departamento
**Quando** o selo estiver a posicionar ou posicionado
**Então** o selo mostra só razão social e nome do departamento, sem `$papel`

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

Pendência — nenhuma evidência anexada ainda.

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação da SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-034|CT-034]] (critério C34, criado a partir deste achado).
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
