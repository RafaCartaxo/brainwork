---
tags:
  - bug
  - qa
  - despacho
task: "8380"
prioridade: baixa
status: resolvido
data_inicio: 2026-07-22
data_fim: 2026-07-22
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: HML
---
# Referência de resposta em despacho exibida incorretamente na cadeia de respostas

### Descrição

Durante validação foi identificado que a referência de resposta de um despacho era exibida incorretamente na cadeia de respostas. Corrigido e aprovado em homologação.

---

### Passo a passo para reproduzir

Dado que um despacho tenha uma resposta associada
Quando a cadeia de respostas for exibida
Então a referência da resposta deve apontar corretamente para o despacho respondido

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://8380)

![[8380 - referencia resposta despacho cadeia respostas aprovado em homologacao.mp4]]

---

### Resultado Esperado

- A referência de resposta deve aparecer corretamente na cadeia de respostas, apontando para o despacho respondido.

---

### Critérios de aceite

- [x] A referência de resposta é exibida corretamente na cadeia de respostas

---

### Casos de Teste Básicos

- **CT-B01 Referência de resposta exibida corretamente na cadeia de respostas**
    Dado que um despacho tenha uma resposta associada
    Quando a cadeia de respostas for exibida
    Então a referência da resposta aponta corretamente para o despacho respondido

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes: ![[8380 - referencia resposta despacho cadeia respostas aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-8380
- Observações: Gate de doc (leve): o comportamento (referência de resposta correta na cadeia de respostas de despacho) não é coberto pelas docs de módulo de `04 Conhecimento/Módulos/` — nem [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]] (trata configuração/customização de despacho) nem [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]] descrevem a cadeia de respostas. Sem doc de módulo "despacho" dedicada — sem divergência a registrar; possível gap de doc (importar via fluxo 8), anotado na daily.
- Histórico:
    - 2026-07-22 - 🐛 Bug cadastrado
    - 2026-07-22 - ✅ Aprovada em homologação
