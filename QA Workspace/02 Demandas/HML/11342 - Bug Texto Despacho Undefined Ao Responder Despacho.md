---
tags:
  - bug
  - qa
  - despachos
task: "11342"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-04
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despachos
ambiente: HML
---
# Texto do despacho de resposta traz "despacho undefined" em vez do número do despacho respondido

### Descrição

Durante validação foi identificado que, ao responder um despacho, o texto do subdespacho de resposta traz **"despacho undefined"** em vez de referenciar o número do despacho original que está sendo respondido.

---

### Passo a passo para reproduzir

**Dado** que existe um despacho em tramitação
**Quando** respondo esse despacho
**Então** verifico que o texto do subdespacho de resposta exibe "despacho undefined" em vez do número do despacho respondido

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://11342)

![[11342 - despacho resposta traz texto despacho undefined.mp4]]

---

### Resultado Esperado

Doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] ("Referência de origem nos eventos"): o subdespacho de resposta deve informar **qual** despacho está sendo respondido (referência ao número do despacho original) — regra incrementada justamente porque antes mostrava só "neste despacho", sem dizer qual. "Despacho undefined" é essa referência quebrada, não um texto genérico faltando: o número do despacho respondido não está sendo resolvido.

Texto deve trazer o número real do despacho respondido, nunca "undefined".

---

### Critérios de aceite

- [ ] Ao responder um despacho, o texto do subdespacho de resposta traz o número do despacho original respondido, nunca "undefined"

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada:
- Observações:
    - Achado direto em homologação, sem CT de nenhuma task pai — relato rápido do Rafael com evidência.
    - Versão/ambiente exato (qual container `hml-*`) não informado — pendência preencher.
    - Doc: [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] confirma a regra de referência de origem no evento de resposta — gate de doc cumprido, sem divergência de definição (o defeito é de implementação, a regra em si está clara e documentada).
- Histórico:
    - 2026-09-04 - 🐛 Bug cadastrado (achado em homologação, evidência no vault)
