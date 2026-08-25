---
tags:
  - bug
  - qa
  - fluxo-de-trabalho
task: "11079"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-25
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: fluxo de trabalho
ambiente: HML
---
# Notificação de fluxo de trabalho exibe "undefined undefined" ao retificar documento

### Descrição

Durante validação foi identificado que, ao retificar um documento com fluxo de trabalho, a retificação é concluída com sucesso, porém a notificação exibida mostra valores não interpolados: "Seu setor GP é o responsável pela etapa inicial de undefined undefined em seu fluxo de traballho." — além do "undefined undefined" no lugar do nome da etapa, o texto também tem o erro de digitação "traballho" (deveria ser "trabalho").

---

### Passo a passo para reproduzir

Dado que eu crio um documento com fluxo de trabalho
Quando eu retifico o documento com fluxo de trabalho
Então verifico que o documento é retificado com sucesso
E que a notificação mostra "Seu setor GP é o responsável pela etapa inicial de undefined undefined em seu fluxo de traballho."

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11079)

![[11079 - notificação com setor undefinied.mp4]]

---

### Resultado Esperado

A notificação exibida após a retificação mostra o nome real da etapa inicial do fluxo de trabalho, sem "undefined undefined", e o texto não contém o erro de digitação "traballho".

---

### Critérios de aceite

- [ ] A notificação de retificação de documento com fluxo de trabalho exibe o nome real da etapa, não "undefined undefined"
- [ ] O texto da notificação não contém o erro de digitação "traballho"

---

### Casos de Teste Básicos

#### **CT-B01 Notificação de retificação exibe a etapa corretamente, sem "undefined undefined"**

**Dado** que eu crio um documento com fluxo de trabalho
**Quando** eu retifico o documento com fluxo de trabalho
**Então** o documento é retificado com sucesso e a notificação exibe o nome real da etapa inicial, sem "undefined undefined" e sem o erro de digitação "traballho"

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[11079 - notificação com setor undefinied.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação (inferido — mesma área da SGV-8673, retificação de documento com fluxo de trabalho; confirmar se foi em outro ambiente)

---

### Informações adicionais

- Demanda relacionada: SGV-11079 (Notion)
- Observações:
    - Relacionado à área da [[QA Workspace/02 Demandas/Concluídas/8673 - Bug Retificacao De Despacho Com Fluxo De Trabalho Exibe Erro Mesmo Com Sucesso|SGV-8673]] (retificação de documento/despacho com fluxo de trabalho), mas defeito diferente: aqui é a notificação com valores não interpolados, não o erro falso de retificação.
- Histórico:
    - 2026-08-25 - 🐛 SGV-11079 - Bug cadastrado
