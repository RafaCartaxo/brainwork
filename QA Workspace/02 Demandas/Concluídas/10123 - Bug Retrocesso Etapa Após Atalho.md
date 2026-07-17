---
tags:
  - bug
  - qa
  - fluxo-de-trabalho
task: "10123"
prioridade: media
status: resolvido
data_inicio: 2026-07-16
data_fim: "2026-07-16"
responsavel: Rafael
cadastrado_por: ""
modulo: fluxo de trabalho
ambiente: HML
---
# Cluster de setor responsável não aparece ao retroceder etapa avançada por atalho

### Descrição

Durante validação da melhoria SGV-9112 em homologação foi identificado que, ao retroceder uma etapa de fluxo de trabalho que foi avançada por atalho para a última etapa, o cluster de seleção do setor responsável não é exibido e a etapa não retrocede.

---

### Passo a passo para reproduzir

Dado que exista um fluxo de trabalho com atalho entre etapas
E a etapa inicial esteja configurada com atalho para a última etapa
Quando o usuário avança da etapa inicial para a última etapa pelo atalho
E tenta retroceder a etapa
Então o cluster de seleção do setor responsável não aparece
E a etapa não retrocede

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10123)

![[10123 - cluster setor responsável não aparece ao retroceder etapa após atalho nOK.mp4]]

![[10123 - retrocesso de etapa após atalho aprovado em homologação.mp4]]

---

### Resultado Esperado

Ao retroceder uma etapa que foi avançada por atalho, o cluster de seleção do setor responsável deve ser exibido e o retrocesso deve ser concluído com sucesso.

---

### Critérios de aceite

- [ ] O cluster de seleção do setor responsável deve ser exibido ao retroceder etapa avançada por atalho
- [ ] O retrocesso da etapa deve ser concluído com sucesso após a seleção do setor responsável

---

### Casos de Teste Básicos

- **CT-B01 Retroceder etapa avançada por atalho exibindo cluster de setor responsável**
    Dado que exista um fluxo de trabalho com atalho da etapa inicial para a última etapa
    E o usuário tenha avançado para a última etapa pelo atalho
    Quando o usuário retroceder a etapa
    Então o cluster de seleção do setor responsável deve ser exibido e a etapa deve retroceder com sucesso

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes: ![[10123 - retrocesso de etapa após atalho aprovado em homologação.mp4]]

---

### Ambiente

- Versão:

- Ambiente: Homologação

- Navegador:

- Sistema Operacional:

---

### Informações adicionais

- Demanda relacionada: SGV-10123
- Observações: Bug aberto a partir da validação da melhoria SGV-9112 (reaberta em homologação por causa deste bug). Evidência compartilhada com a melhoria — mesmo vídeo, cópia renomeada (`9112 - Avanço de etapas de fluxo de trabalho, última etapa nOK.mp4`).
- Histórico:
    - 2026-07-16 - 🐛 Bug cadastrado
    - 2026-07-16 - ✅ Aprovada em homologação (cluster de setor responsável exibido e retrocesso concluído; evidência gravada)
