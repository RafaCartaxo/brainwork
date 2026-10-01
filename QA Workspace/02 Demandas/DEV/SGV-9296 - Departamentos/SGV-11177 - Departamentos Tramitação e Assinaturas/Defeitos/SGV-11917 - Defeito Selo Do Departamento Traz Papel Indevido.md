---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11917"
pai: "SGV-11177"
prioridade: media
status: resolvido
data_inicio: 2026-09-29
data_fim: "2026-09-30"
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Selo do departamento traz papel indevido

### Descrição

Antes de assinado (a posicionar/posicionado), o selo de assinatura de um departamento traz o campo `$papel` com valor "signatario" — não deveria trazer `$papel` nesse caso, só razão social e nome do departamento. Depois de assinado também está incorreto.

---

### Passo a passo para reproduzir

**Dado** que a assinatura seja solicitada a um departamento
**Quando** o selo for exibido, em qualquer estado (a posicionar, posicionado ou assinado)
**Então** verifico que aparece o campo `$papel` com valor "signatario" em todos eles, quando não deveria aparecer em nenhum

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11917)

**Antes da correção:**
![[11917 - Selo departamento retornando $papel, incorreto.mp4]]

**Retestado e aprovado (30/09/2026):**
![[11917 - Selo do departamento sem papel indevido, ok.png]]

---

### Resultado Esperado

Selo mostra só razão social e nome do departamento, sem `$papel`, em nenhum estado (a posicionar, posicionado ou assinado). Ver [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c34|C34]] e [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-034|CT-034]].

---

### Critérios de aceite

- [x] Selo do departamento não mostra `$papel` em nenhum estado (a posicionar, posicionado, assinado)

---

### Casos de Teste Básicos

#### **CT-B01 Selo do departamento sem papel em nenhum estado**

**Dado** que a assinatura seja solicitada a um departamento
**Quando** o selo for exibido, em qualquer estado
**Então** o selo mostra só razão social e nome do departamento, sem `$papel`

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11917 - Selo do departamento sem papel indevido, ok.png]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação da SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-034|CT-034]] (critério C34, criado a partir deste achado).
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
    - 2026-09-30 - ✅ Retestado e aprovado — selo sem `$papel` em nenhum estado
