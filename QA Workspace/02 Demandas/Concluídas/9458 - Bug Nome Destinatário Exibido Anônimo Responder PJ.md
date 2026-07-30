---
tags:
  - bug
  - qa
  - despacho
task: "9458"
prioridade: altíssima
status: resolvido
data_inicio: 2026-07-27
data_fim: 2026-07-27
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: HML
---
# Nome do destinatário exibido como "Anônimo" ao responder PJ

### Descrição

Ao responder uma Pessoa Jurídica (PJ), o nome do destinatário era exibido como "Anônimo" em vez do nome real. (Origem Notion SGV-9458, Matheus Godoi.)

---

### Resultado Esperado

Ao responder uma PJ, o nome do destinatário é exibido corretamente, sem cair no fallback "Anônimo".

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9458)

![[9458 - nome destinatario exibido corretamente resposta pj aprovado em homologacao.mp4]]

---

### Critérios de aceite

- [x] Nome do destinatário é exibido corretamente ao responder uma PJ

---

### Casos de Teste Básicos

#### **CT-B01 Nome do destinatário correto ao responder PJ**

**Dado** uma resposta destinada a uma Pessoa Jurídica
**Quando** o destinatário é exibido na tela
**Então** o nome real é mostrado, sem cair em "Anônimo"

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[9458 - nome destinatario exibido corretamente resposta pj aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: SGV-9458 (origem Notion; Triagem SP15, grupo "Pronto pra homologação"; critérios prontos desde 17/07; Matheus Godoi).
- Sem export completo — card criado direto a partir do ticket + validação em homologação.
- Histórico:
    - 2026-07-27 - ✅ Aprovada em homologação
