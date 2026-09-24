---
tags:
  - defeito
  - qa
  - tramitacao
task: "11816"
pai: "SGV-9982"
prioridade: media
status: aberto
data_inicio: 2026-09-24
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: tramitacao
ambiente: DEV
---
# Cores do modal de encerramento divergem do protótipo Figma

### Descrição

Durante a validação do CT-012 do pacote QA de SGV-9982 foi identificado que as cores dos três dialogs de encerramento (modal de alerta) estão divergentes do protótipo Figma. O Figma deve ser respeitado como referência de estilo.

---

### Passo a passo para reproduzir

**Dado** que o usuário abre qualquer um dos três dialogs de encerramento de tramitação (documento inteiro, setor ou participação própria)
**Quando** ele observa o estilo do modal exibido (ícone, cor de destaque, borda superior do `modal Type=Alert`)
**Então** verifico que as cores não correspondem às definidas no protótipo Figma

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11816)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

### Resultado Esperado

Protótipo: [Figma — Tramitação - Concepção → Section "Dialogs"](https://www.figma.com/design/LAe926PuW2psDGd3XT45lX/Tramita%C3%A7%C3%A3o---Concep%C3%A7%C3%A3o?node-id=6164-6993)

As cores dos três dialogs (ícone, cor de destaque, borda superior do `modal Type=Alert`) devem corresponder exatamente ao definido no protótipo Figma — ver [[QA Workspace/02 Demandas/SGV-9982 - Permanecer no documento após encerrar/01 - Demanda#^c9|C9]] e [[QA Workspace/02 Demandas/SGV-9982 - Permanecer no documento após encerrar/03 - Casos de teste#^ct-012|CT-012]].

---

### Critérios de aceite

- [x] As cores do modal (ícone, cor de destaque, borda superior do Alert) correspondem exatamente ao protótipo Figma nos três dialogs de encerramento

---

### Casos de Teste Básicos

#### **CT-B01 Cores do modal de encerramento seguem o protótipo Figma**

**Dado** que o usuário abre qualquer um dos três dialogs de encerramento
**Quando** ele observa o estilo do modal (ícone, cor de destaque, borda superior)
**Então** as cores correspondem exatamente ao protótipo Figma definido para o `modal Type=Alert`

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

- Demanda relacionada: [[QA Workspace/02 Demandas/SGV-9982 - Permanecer no documento após encerrar/01 - Demanda|SGV-9982]]
- Observações: achado durante a validação do pacote QA de SGV-9982 — [[QA Workspace/02 Demandas/SGV-9982 - Permanecer no documento após encerrar/03 - Casos de teste#^ct-012|CT-012]].
- Histórico:
    - 2026-09-24 - 🐛 Defeito cadastrado (da SGV-9982)
