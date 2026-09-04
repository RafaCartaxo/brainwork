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
# Campo de despacho resposta com texto "undefined" ao responder despacho

### Descrição

Durante validação foi identificado que, ao responder um despacho, aparece um campo que não deveria aparecer nesse fluxo. **O problema não é o texto errado em si — é o campo existir.** Além de indevido, o campo está com defeito visual: fundo do modal quase branco e o texto também branco, ficando como uma "sombra" quase ilegível (mas o texto segue selecionável, confirmando que o conteúdo está lá, só não é visível). O conteúdo desse campo é o texto incorreto "undefined".

---

### Passo a passo para reproduzir

**Dado** que existe um despacho em tramitação
**Quando** respondo esse despacho
**Então** verifico que aparece um campo que não deveria aparecer nesse fluxo — quase invisível (fundo e texto do modal em branco, texto ainda selecionável) e com o conteúdo "undefined"

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://11342)

![[11342 - despacho resposta traz texto despacho undefined.mp4]]

---

### Resultado Esperado

O campo **não deve aparecer** nesse fluxo de resposta ao despacho. Não é uma questão de corrigir o texto exibido (trocar "undefined" por outra coisa) nem de corrigir a legibilidade/contraste — o campo em si é indevido nesse ponto do fluxo e sua correção é deixar de renderizar.

---

### Critérios de aceite

- [ ] Ao responder um despacho, o campo com o texto "undefined" não aparece

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
    - Doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] não documenta esse campo — não é a mesma regra de "referência de origem nos eventos" (essa fica na timeline, não num campo do modal de resposta). Sem gate de doc aplicável aqui; card corrigido em 04/09 depois de esclarecimento do Rafael sobre a causa real (campo indevido, não texto errado).
- Histórico:
    - 2026-09-04 - 🐛 Bug cadastrado (achado em homologação, evidência no vault)
    - 2026-09-04 - 🔧 Corrigido com Rafael: o defeito é o campo aparecer (quase invisível, fundo/texto branco, selecionável), não o texto "undefined" em si — card reescrito (Descrição, Passo a passo, Resultado Esperado, Critérios de aceite)
