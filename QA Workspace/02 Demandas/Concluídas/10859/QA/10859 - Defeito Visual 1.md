---
tags:
  - defeito
  - qa
  - mesa-de-trabalho
task: "10859"
pai: "10363"
prioridade: baixa
status: resolvido
data_inicio: 2026-08-18
data_fim: "2026-08-18"
responsavel: Rafael
cadastrado_por: ""
modulo: mesa de trabalho
ambiente: DEV
---
# Defeito visual 1 — layout da mesa de trabalho mobile

> [!info] Defeito da [[QA Workspace/02 Demandas/HML/10363 - Melhoria Layout Mesa De Trabalho Mobile|SGV-10363]]
> Problema **visual básico** encontrado na validação em DEV da melhoria de layout da mesa de trabalho mobile (parte 5). Corrigido e retestado no mesmo dia.
>
> **Numeração `1` é só identificação** — segue a ordem crescente de SGV entre os 4 defeitos da task, não prioridade nem ordem de descoberta.

### Descrição

Ajuste visual no layout mobile da mesa de trabalho. **A descrição detalhada e a evidência vivem na task do Notion** — este card existe pra rastreabilidade da esteira, não como especificação.

Registrado assim por decisão: a task pai é visual e foi validada de forma exploratória, sem casos de teste ([[Sistema/Contexto/PADROES_QA#Por que o defeito fecha em DEV|PADROES_QA]]).

---

### Evidências

> [!important] No Notion, não no vault
> Gravada pelo celular durante a validação e anexada na task. **Não há arquivo local** em `Evidências/` — por isso o 🔄 não avisa nada sobre este card.

---

### Ambiente

- Ambiente: Desenvolvimento
- Versão: *(não apurada — validação exploratória)*

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/10363 - Melhoria Layout Mesa De Trabalho Mobile|SGV-10363]] — task pai, parte 5 da melhoria de layout da mesa de trabalho mobile

- Observações:
    - Fecha em `Concluídas/` com **`ambiente: DEV`**: é o marcador da exceção da esteira do defeito. Card concluído pela esteira normal termina com `ambiente: HML` — ver [[Sistema/Contexto/PADROES_QA#Defeito × Bug|Defeito × Bug]].
    - **Não será retestado em homologação**: quem valida em HML é a task pai.

- Histórico:
    - 2026-08-18 - 🐛 Defeito cadastrado (da [[QA Workspace/02 Demandas/HML/10363 - Melhoria Layout Mesa De Trabalho Mobile|SGV-10363]]; problema visual encontrado na validação em DEV)
    - 2026-08-18 - ✅ Defeito corrigido e retestado em DEV — card fechado **sem etapa de HML**: é defeito da [[QA Workspace/02 Demandas/HML/10363 - Melhoria Layout Mesa De Trabalho Mobile|SGV-10363]] e a validação em homologação acontece pela task principal
