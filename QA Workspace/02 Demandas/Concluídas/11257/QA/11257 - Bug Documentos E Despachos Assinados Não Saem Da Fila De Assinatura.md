---
tags:
  - bug
  - qa
  - assinatura
task: "11257"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-02
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinaturas
ambiente: HML
---
# Documentos e despachos assinados não saem da fila de assinatura

### Descrição

Durante validação foi identificado que, ao solicitar assinatura de um documento com anexo e de um despacho com anexo (via toolbar, se selecionando como signatário) e assinar o combo do documento+anexo com sucesso, ao voltar para a fila esse combo já assinado não sai da fila — continua disponível pra assinar de novo, indefinidas vezes, mesmo já estando assinado.

---

### Passo a passo para reproduzir

Dado que crio um documento com anexo e realizo um despacho com anexo no mesmo documento
E solicito assinatura para todos (documento, anexos, despachos e seus anexos) via toolbar, me selecionando como signatário
Quando a tela de assinar carrega e assino o combo "documento + anexo" com sucesso
E, no modal de conclusão, clico em "Voltar para fila" pra assinar o combo "despacho + anexo"
Então verifico que o combo "documento + anexo", já assinado, não saiu da fila — continua lá, disponível pra assinar de novo indefinidas vezes

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11257)

![[11257 - Fila não é atualizada.mp4]]

---

### Resultado Esperado

- O combo já assinado com sucesso **sai da fila** de assinatura, permitindo que o usuário prossiga assinando o próximo combo pendente (ex.: despacho + anexo) normalmente, sem o combo já concluído continuar disponível pra assinar de novo

**Lastro documental** — [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Assinando uma solicitação não sequencial|Assinaturas → Regra do combo]]: documento+anexos e despacho+anexos são combos **separados** ("pode recusar o combo 'despacho + anexos' e assinar o combo 'documento + anexos'"), e o fluxo de fila descrito em [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Assinaturas em massa|Assinaturas em massa]] usa o mesmo princípio de fila que **esvazia** conforme os combos são concluídos ("vai pra fila de assinaturas (sai da listagem à esquerda)"). Um combo já assinado permanecer na fila, reassinável, é o oposto do que a doc descreve.

---

### Critérios de aceite

- [ ] Após assinar um combo com sucesso e escolher "Voltar para fila", o combo assinado **não aparece mais** na fila
- [ ] O usuário consegue seguir assinando os próximos combos pendentes (ex.: despacho + anexo) sem o combo já assinado bloquear ou poluir a lista
- [ ] O combo já assinado **não pode ser assinado novamente** pela fila

---

### Casos de Teste Básicos

#### **CT-B01 Combo assinado sai da fila e não pode ser reassinado**

**Dado** que solicito assinatura de um documento+anexo e de um despacho+anexo, via toolbar, me selecionando como signatário
**E** assino o combo do documento+anexo com sucesso
**Quando** volto para a fila (opção "Voltar para fila" no modal de conclusão)
**Então** o combo do documento+anexo **não aparece mais** na fila, e só o combo do despacho+anexo permanece pendente

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[11257 - Fila não é atualizada.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada:
- Observações: Gate de doc ([[Sistema/Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]): divergência confirmada contra [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] — ver Lastro documental acima. Não é regra de negócio nova, é a fila não refletindo o estado já assinado do combo.
- Histórico:
    - 2026-09-02 - 🐛 Bug cadastrado
