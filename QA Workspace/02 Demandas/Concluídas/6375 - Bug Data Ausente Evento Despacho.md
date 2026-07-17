---
tags:
  - bug
  - qa
  - despacho
task: "6375"
prioridade: alta
status: resolvido
data_inicio: 2026-07-14
data_fim: 2026-07-14
responsavel: Rafael
modulo: despacho
ambiente: HML
---
# Data não aparece nos eventos de despacho

### Descrição

Durante validação foi identificado que a data não estava sendo exibida nos eventos de despacho. Corrigido e aprovado em homologação.

---

### Passo a passo para reproduzir

Dado que um despacho seja realizado
Quando o evento do despacho for exibido
Então a data do evento deve ser exibida corretamente

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://6375)

![[6375 - data ausente no evento de despacho corrigida.mp4]]

---

### Resultado Esperado

A data deve ser exibida corretamente em todos os eventos de despacho.

---

### Critérios de aceite

- [x] O evento de despacho deve exibir a data corretamente
- [x] Não deve haver casos onde a data apareça em branco/ausente

---

### Casos de Teste Básicos

- **CT-B01 Exibir data corretamente no evento de despacho**
    Dado que um despacho seja realizado
    Quando o evento do despacho for exibido
    Então a data do evento deve ser exibida corretamente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-6375
- Observações:
- Histórico:
    - 2026-07-14 - ✅ Aprovada em homologação
