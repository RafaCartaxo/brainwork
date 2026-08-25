---
tags:
  - bug
  - qa
  - organograma
task: "11052"
pai: ""
prioridade: media
status: resolvido
data_inicio: 2026-08-25
data_fim: 2026-08-25
responsavel: Rafael
cadastrado_por: Rafael
modulo: organograma
ambiente: HML
---
# Renomear setor reflete corretamente no evento do documento

> [!info] Card criado e já aprovado na mesma sessão
> Título e escopo inferidos a partir do nome da evidência (`11052 - editar nome setor evento ok.mp4`) e da regra documentada em [[QA Workspace/04 Conhecimento/Módulos/Organograma#Edição de setor ou subsetor|Organograma § Edição de setor ou subsetor]]. Sem passo a passo detalhado do Rafael — completar se precisar de mais contexto.

### Descrição

Durante validação foi confirmado que, ao renomear um setor, o nome exibido no evento/histórico do documento respeita a regra documentada: documentos já tramitados no setor mantêm o nome antigo, e documentos gerados após a mudança já saem com o nome atualizado.

---

### Passo a passo para reproduzir

Dado que existe um setor com documentos já tramitados nele
Quando eu renomeio esse setor
Então verifico que os documentos já tramitados mantêm o nome antigo do setor no evento
E que documentos novos, gerados após a mudança, já saem com o nome atualizado do setor

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11052)

![[11052 - editar nome setor evento ok.mp4]]

---

### Resultado Esperado

- Documentos já tramitados no setor **antes** da renomeação mantêm o nome antigo do setor no evento
- Documentos gerados/tramitados **depois** da renomeação já saem com o nome novo do setor

> [!note] Gate de doc: confirmado
> [[QA Workspace/04 Conhecimento/Módulos/Organograma#Edição de setor ou subsetor|Organograma § Edição de setor ou subsetor]] documenta exatamente essa regra ("os documentos permanecerão com o nome do setor antigo" / "a partir da data/horário da mudança de nome em diante, documentos novos já saem com o nome do setor novo"). O comportamento validado bate com a doc.

---

### Critérios de aceite

- [x] Documentos já tramitados no setor mantêm o nome antigo no evento após a renomeação
- [x] Documentos novos, gerados após a renomeação, exibem o nome atualizado do setor no evento

---

### Casos de Teste Básicos

#### **CT-B01 Renomear setor reflete corretamente no evento do documento**

**Dado** que existe um setor com documentos já tramitados nele
**Quando** eu renomeio esse setor
**Então** os documentos já tramitados mantêm o nome antigo no evento, e documentos novos exibem o nome atualizado

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[11052 - editar nome setor evento ok.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-11052 (Notion)
- Observações:
    - Card nasce já aprovado, sem rodada de reprovação anterior registrada no vault.
- Histórico:
    - 2026-08-25 - ✅ Aprovada em homologação (renomear setor reflete corretamente o nome antigo/novo no evento do documento, conforme regra documentada em Organograma)
