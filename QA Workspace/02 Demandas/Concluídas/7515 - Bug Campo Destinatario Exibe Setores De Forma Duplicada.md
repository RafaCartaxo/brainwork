---
tags:
  - bug
  - qa
  - despacho
task: "7515"
prioridade: media
status: resolvido
data_inicio: 2026-08-11
data_fim: 2026-08-11
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: HML
---
# Campo destinatário exibe setores de forma duplicada

### Descrição

Durante validação foi identificado que o campo **Destinatário** exibia os **setores de forma duplicada** na lista de opções.

Validado em homologação em 11/08/2026: o campo passou a listar os setores **sem repetição**.

---

### Passo a passo para reproduzir

Dado que estou emitindo um despacho
Quando abro o campo **Destinatário** e percorro a lista de setores
Então verifico que os setores aparecem duplicados na lista

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://7515)

![[7515 - campo destinatário ok - sem opções repetidas.mp4]]

---

### Resultado Esperado

- O campo **Destinatário** lista cada setor **uma única vez**, sem repetição de opções

---

### Critérios de aceite

- [x] O campo Destinatário não apresenta setores duplicados na lista de opções

---

### Casos de Teste Básicos

#### **CT-B01 Campo Destinatário lista cada setor uma única vez**

**Dado** que estou emitindo um despacho
**Quando** abro o campo **Destinatário** e percorro a lista de setores
**Então** verifico que cada setor aparece **uma única vez**, sem opções repetidas

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[7515 - campo destinatário ok - sem opções repetidas.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada:
- Observações:
    - **Card criado no dia da aprovação** (11/08/2026). A demanda não existia no vault até aqui — nem card, nem menção em daily anterior —, então o registro de descrição e passo a passo foi reconstruído a partir da evidência e não do histórico da validação original.
    - **Módulo inferido** como `despacho` pelo campo Destinatário; conferir se a task aponta outro.
    - ⚠️ **Divergência com o Notion**: lá a demanda ficou marcada como **"não reproduzido"**; aqui foi registrada como **aprovada em homologação**, conforme decisão do Rafael em 11/08. As duas leituras têm consequências diferentes no vault — `⚪ não reproduzido` deixaria o card em limbo, sem arquivar ([[QA Workspace/01 Daily/README|01 Daily/README]]).
- Histórico:
    - 2026-08-11 - ✅ Aprovada em homologação (campo destinatário sem opções repetidas) — primeira validação, sem reabertura anterior
