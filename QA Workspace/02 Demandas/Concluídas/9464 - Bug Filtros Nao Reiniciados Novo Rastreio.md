---
tags:
  - bug
  - qa
task: "SGV-9464"
prioridade: media
status: resolvido
data_inicio: 2026-07-21
data_fim: 2026-07-21
responsavel: Rafael
cadastrado_por: ""
modulo: Rastrear Documento
ambiente: HML
---
# Ao realizar novo rastreio de documentos, filtros não são reiniciados

### Descrição

Durante validação foi identificado que, após aplicar filtros na tela de resultados do rastreamento de documentos (como "Documentos pausados" e "Documentos encerrados") e realizar um novo rastreio, ao término do carregamento da nova consulta os filtros aplicados anteriormente permaneciam selecionados, não sendo reiniciados automaticamente pelo sistema.

---

### Passo a passo para reproduzir

Dado que o usuário realizou um rastreamento de documentos e aguardou o carregamento dos resultados
E aplicou filtros na tela de resultados (ex.: "Documentos pausados", "Documentos encerrados")
Quando realiza um novo rastreamento
Então, ao término do carregamento da nova consulta, os filtros aplicados anteriormente permanecem selecionados, não sendo reiniciados automaticamente

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9464)

![[9464 - filtros reiniciados ao realizar novo rastreio aprovado em homologacao.mp4]]

---

### Resultado Esperado

- Ao iniciar um novo rastreio de documentos, os filtros aplicados na consulta anterior são reiniciados automaticamente, e o resultado exibido corresponde à nova consulta sem filtro residual.

---

### Critérios de aceite

- [x] Ao iniciar um novo rastreio, os filtros da consulta anterior voltam ao estado inicial
- [x] O resultado exibido corresponde à nova consulta, sem filtro residual

---

### Casos de Teste Básicos

- **CT-B01 Filtros são reiniciados ao realizar novo rastreio**
    Dado que o usuário realizou um rastreamento e aplicou filtros na tela de resultados
    Quando realiza um novo rastreamento
    Então, ao término do carregamento, os filtros voltam ao estado inicial e o resultado corresponde à nova consulta sem filtro residual

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes: ![[9464 - filtros reiniciados ao realizar novo rastreio aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-9464
- Observações: Refinada em [[QA Workspace/04 Conhecimento/SGV-9464 - Refinamento Filtros Novo Rastreio|SGV-9464 - Refinamento Filtros Novo Rastreio]]. Correção pelo MR !553 (João Marcelo): ao detectar novo rastreio (`location.search` muda), zera `statusFilter` e `importedDocuments`; `searchItems` passa a aceitar overrides explícitos pra a busca inicial não depender do estado antigo. Aprovado em DEV por Lucas Beninca (15/07). Card criado retroativamente no momento do registro da validação (aprovada em homologação).
- Histórico:
    - 2026-07-21 - Análise de causa raiz (mesa 05 Refinar): filtros residuais (`statusFilter`, `importedDocuments`) não zeravam ao mudar `location.search`; MR !553 corrige
    - 2026-07-21 - ✅ Aprovada em homologação
