---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11948"
pai: "SGV-11177"
prioridade: media
status: resolvido
data_inicio: 2026-09-30
data_fim: "2026-09-30"
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Solicitação de assinatura não aparece na lista do departamento

### Descrição

Durante a validação real da SGV-11177 (Parte 4 da epic [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]]) foi identificado que, ao solicitar assinatura — tanto pro cidadão membro alocado num departamento quanto pro departamento como um todo — a nova solicitação não carrega na lista de demandas do departamento.

---

### Passo a passo para reproduzir

**Dado** que uma assinatura é solicitada a um cidadão membro de um departamento, ou ao departamento como um todo
**Quando** o servidor consulta a lista de demandas do departamento
**Então** verifico que a nova solicitação não aparece nessa lista

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11948)

**Antes da correção:**
![[11948 - Solicitação de assinatura não aparece na lista do departamento, incorreto.mp4]]

**Retestado e aprovado (30/09/2026):**
![[11948 - OK.mp4]]

---

### Resultado Esperado

Solicitação de assinatura ao membro ou ao departamento inteiro carrega normalmente na lista de demandas do departamento.

---

### Critérios de aceite

- [x] Solicitação de assinatura a um membro de departamento aparece na lista de demandas do departamento
- [x] Solicitação de assinatura ao departamento inteiro aparece na lista de demandas do departamento

---

### Casos de Teste Básicos

#### **CT-B01 Solicitação de assinatura carrega na lista do departamento**

**Dado** que uma assinatura é solicitada a um cidadão membro de um departamento, ou ao departamento inteiro
**Quando** o servidor consulta a lista de demandas do departamento
**Então** a nova solicitação aparece na lista

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11948 - OK.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação da SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-036|CT-036]] (critério C36, criado a partir deste achado). Distinto da [[SGV-11924 - Defeito Assinatura Bloqueada Entre Departamentos Diferentes Do Mesmo Cidadão PJ|SGV-11924]] (que é sobre a API bloquear a solicitação) — aqui a solicitação é aceita, só não aparece na lista certa.
- Histórico:
    - 2026-09-30 - 🐛 Defeito cadastrado
    - 2026-09-30 - ✅ Retestado e aprovado — solicitação aparece na lista de demandas do departamento (membro e departamento inteiro)
