---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11905"
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
# Selo de assinatura não traz o departamento do membro signatário

### Descrição

Durante a validação real da SGV-11177 (Parte 4 da epic SGV-9296) foi identificado que o selo de assinatura aplicado no documento, quando o signatário é um cidadão membro de um departamento, não traz a copy definida no Figma — falta o contexto do departamento (razão social, nome do departamento, cargo no departamento e papel). Mesma causa de fundo do defeito nos eventos de assinatura, ver [[SGV-11904 - Defeito Eventos De Assinatura Não Identificam Departamento Do Membro Signatário|SGV-11904]] (defeito irmão).

---

### Passo a passo para reproduzir

**Dado** que um cidadão membro de um departamento assina um documento
**Quando** o servidor consulta o selo de assinatura aplicado no documento
**Então** verifico que o selo não contém razão social, nome do departamento, nome de exibição com o cargo no departamento e papel — conforme o Figma

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11905)

![[11905 - Selo representando dpt incorreto.mp4]]

---

### Resultado Esperado

O selo deve mostrar: razão social, nome do departamento, nome de exibição (com o cargo no departamento) e papel.

Ver [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c32|C32]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-032|CT-032]].

---

### Critérios de aceite

- [ ] O selo de assinatura de um membro de departamento mostra razão social, nome do departamento, nome de exibição (com o cargo no departamento) e papel

---

### Casos de Teste Básicos

#### **CT-B01 Selo de assinatura traz o contexto do departamento**

**Dado** que um cidadão membro de um departamento assina um documento
**Quando** o servidor consulta o selo aplicado
**Então** o selo mostra razão social, nome do departamento, nome de exibição (cargo no departamento) e papel

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11905 - Selo representando dpt incorreto.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação real do pacote QA de SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-032|CT-032]] (critério C32 criado a partir deste achado, fora de sequência).
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
