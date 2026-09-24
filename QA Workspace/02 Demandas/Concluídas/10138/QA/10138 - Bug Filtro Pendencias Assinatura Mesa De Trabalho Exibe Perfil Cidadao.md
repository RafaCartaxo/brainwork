---
tags:
  - bug
  - qa
  - mesa-de-trabalho
task: "10138"
prioridade: media
status: resolvido
data_inicio: 2026-08-12
data_fim: 2026-08-12
responsavel: Rafael
cadastrado_por: ""
modulo: mesa de trabalho
ambiente: HML
---
# [BUG] Filtro de pendências de assinatura na Mesa de Trabalho exibe solicitações do perfil Cidadão indevidamente

### Descrição

Durante validação foi identificado que o **filtro de pendências de assinatura** da Mesa de Trabalho exibia tanto as solicitações do perfil **Servidor** quanto as do perfil **Cidadão** do mesmo usuário, misturando pendências de contextos distintos.

Validado em homologação em 12/08/2026: o filtro passou a considerar **apenas o perfil Servidor**.

---

### Passo a passo para reproduzir

Dado que eu acesso a Mesa de Trabalho com um usuário que possui perfis de **Servidor e Cidadão**
Quando eu seleciono o filtro de **pendências de assinatura** e aguardo o carregamento da lista
Então verifico que são exibidas solicitações de assinatura dos **dois perfis**, com as pendências do Cidadão aparecendo junto das do Servidor

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://10138)

![[10138 - pendencias de assinatura ok, não considera mais meu cidadão na minha mesa de trabalho, perfil servidor.mp4]]

---

### Resultado Esperado

- O filtro de pendências de assinatura da Mesa de Trabalho exibe **exclusivamente** as solicitações do perfil **Servidor**
- Solicitações vinculadas ao perfil **Cidadão** não são consideradas nesse contexto
- A listagem respeita o **perfil ativo** e o contexto funcional da Mesa de Trabalho

---

### Critérios de aceite

- [x] O filtro de pendências de assinatura exibe apenas solicitações relacionadas ao perfil **Servidor**
- [x] Solicitações vinculadas ao perfil **Cidadão** não são exibidas na Mesa de Trabalho
- [x] A consulta considera corretamente o **perfil ativo** do usuário
- [x] A correção **não impacta os demais filtros** da Mesa de Trabalho
- [x] O comportamento permanece **consistente após atualização da página** e novas consultas

---

### Casos de Teste Básicos

#### **CT-B01 Filtro de pendências exibe apenas o perfil Servidor**

**Dado** que eu acesso a Mesa de Trabalho com usuário que possui perfis de Servidor e Cidadão
**E** existem solicitações de assinatura pendentes nos dois perfis
**Quando** eu seleciono o filtro de pendências de assinatura
**Então** verifico que **apenas** as solicitações do perfil Servidor são listadas, e nenhuma do perfil Cidadão

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10138 - pendencias de assinatura ok, não considera mais meu cidadão na minha mesa de trabalho, perfil servidor.mp4]]

---

#### **CT-B02 Correção não impacta os demais filtros e se mantém após recarregar**

**Dado** que o filtro de pendências de assinatura está corrigido
**Quando** eu uso os demais filtros da Mesa de Trabalho, atualizo a página e refaço as consultas
**Então** verifico que os outros filtros seguem funcionando e que o comportamento do filtro de pendências se mantém consistente

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10138 - pendencias de assinatura ok, não considera mais meu cidadão na minha mesa de trabalho, perfil servidor.mp4]]
*Mesma gravação do CT-B01.*

---

### Ambiente

- Versão: **12.39.44.2** (Homolog, deploy de 11/08/2026)
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada:
- Observações:
    - **Card criado no dia da aprovação** (12/08/2026). A demanda não existia no vault — descrição, passos, resultado esperado e critérios vieram do **export da task**, não de reconstrução.
    - **Causa raiz (do MR):** *"meu usuário servidor também possui cidadão, então coloco o filtro que precisa ter um setor envolvido"*. A correção adicionou **filtro por setor** quando a query filtrava apenas por usuário. Endpoints afetados: `documentObjectsForWorkboard`, `documentObjectsCountForWorkboard`, `documentObjectsByAllStatus`, `documentObjectsCountByAllStatus`. [MR !723](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/723) — dev Diogo Sobreira, revisores Washington Junior e Gabriel Desidério.
    - **Por que o bug era inevitável**: a doc de [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] registra que *"se cadastrado como servidor, um ambiente cidadão correspondente já é criado automaticamente"* — ou seja, **todo servidor tem um perfil cidadão**, então qualquer consulta que filtre só por usuário traz os dois contextos.
    - **QA Responsável na task é Flávio Oliveira**; a validação em homologação de 12/08 foi feita pelo Rafael.
- Histórico:
    - 2026-08-12 - 🔎 Gate de doc: **doc respalda** o resultado esperado — [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]] define a mesa como área do servidor ("cada servidor terá acesso à sua mesa individual e às mesas dos setores a que está vinculado"), então pendência do perfil Cidadão não pertence ao contexto. **Lacuna**: a doc não escreve isso como regra explícita do filtro de pendências, nem registra o recorte por setor que a correção introduziu.
    - 2026-08-12 - ✅ Aprovada em homologação (5 de 5 critérios e 2 de 2 CTs; versão 12.39.44.2)
