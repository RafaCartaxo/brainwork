---
tags:
  - bug
  - qa
  - organograma
  - tramitacao
task: "8977"
prioridade: baixa
status: aberto
data_inicio: 2026-07-20
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: organograma
ambiente: DEV
---
# Erro (timeout) ao editar regras de tramitação direto no Organograma em ambientes com muitos setores

### Descrição

Foi identificado um erro ao editar regras de tramitação diretamente pelo módulo de Organograma em ambientes que possuem um grande número de setores vinculados aos módulos do sistema.

**Comportamento observado**: ao editar regras de tramitação diretamente pelo Organograma, o sistema apresenta erro ao salvar as alterações; o problema ocorre em ambientes com grande quantidade de setores vinculados aos módulos; a operação aparenta exceder o tempo limite da requisição. Em ambientes com menor volume de setores, a funcionalidade opera normalmente.

**Entrega do dev** (Washington Junior — [MR !505](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/505)) — Substitui buscas individuais em loop (`findUnique`/`findMany` por id, N+1) por buscas em lote (`findMany` com `id: { in: [...] }`) em `updateOrganizationalComponent` e nas funções auxiliares `updateRulesSectorToModule`/`updateRulesSectorToMatterService`; adiciona índices (`@@index`) em `ModuleProceduralRule.organizationalComponentId`/`moduleDeploymentInstanceId` e `ProceduralRule.organizationalComponentId`/`mattersServicesId`; introduz constante dedicada `TIME_OUT_TRANSACTION_ORGANOGRAM = 10000` (10s) substituindo `TIME_OUT_TRANSACTION_SYNCHRONOUS` (30s) nessa transação. Histórico de commits mostra iteração no valor do timeout (aumento → ajuste ao limite do gateway/serverless → redução) antes de fechar em 10s.

---

### Passo a passo para reproduzir

Dado que exista um ambiente com grande quantidade de setores vinculados aos módulos do sistema
Quando acessar o módulo Organograma, selecionar um setor com regras de tramitação configuradas, editar as regras e salvar
Então o sistema deve concluir a edição com sucesso — sem erro nem timeout — independente da quantidade de setores/módulos existentes

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://8977)

- Evidência **na task do Notion**, sem cópia local: `Gravando 2026-05-28 111446 - editando regra de tramitação direto no organograma PM SGA.mp4`. Evidência local entra no fluxo normal na validação.

---

### Resultado Esperado

O sistema deve concluir a edição das regras de tramitação com sucesso, independentemente da quantidade de setores ou módulos existentes no ambiente. Caso o processamento demande mais tempo devido ao volume de dados, a aplicação deve suportar essa operação sem interromper a requisição, garantindo que as alterações sejam persistidas corretamente.

---

### Critérios de aceite

> [!warning] Critério de tempo atualizado conforme o que foi implementado
> O critério original pedia timeout compatível **"(30s)"**. O fix entregue reduziu o timeout dessa transação de 30s para **10s** (`TIME_OUT_TRANSACTION_ORGANOGRAM`) — não aumentou. A aposta do dev é que o ganho de performance (lote + índice) compensa a janela menor. **Isso não foi comprovado por teste automatizado** (os 2 testes do MR cobrem só correção funcional de CRUD, nenhum mede tempo/volume) — critérios abaixo ajustados pra refletir o que precisa ser validado manualmente.

- [ ] Editar e salvar regras de tramitação pelo Organograma conclui **sem erro** em ambiente com grande quantidade de setores/módulos (cenário original do bug — validar no ambiente de maior volume disponível)
- [ ] A operação conclui **dentro dos 10s** do novo timeout (`TIME_OUT_TRANSACTION_ORGANOGRAM`) mesmo no ambiente de maior volume disponível pra teste — **não** dos 30s do critério original, que não foi o valor entregue
- [ ] O sistema não apresenta timeout durante o salvamento das regras, no volume testado
- [ ] As alterações realizadas são persistidas corretamente após a conclusão da operação
- [ ] A correção não piora o desempenho da edição de regras em ambientes com menor volume de dados (comparar tempo antes/depois se possível)
- [ ] Sem regressão funcional: conceder `canCreate` cria regras de módulo e assunto/serviço; revogar preserva histórico com `canCreate=false` (coberto pelos testes automatizados do MR — conferir na revisão, não recriar)

---

### Casos de Teste Básicos

- **CT-B01 Editar regra de tramitação em ambiente de grande volume**
    Dado um ambiente com grande quantidade de setores vinculados aos módulos
    Quando editar e salvar as regras de tramitação de um setor pelo Organograma
    Então a operação deve concluir com sucesso, sem erro nem timeout

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Tempo de conclusão dentro do novo limite (10s)**
    Dado o mesmo ambiente de grande volume
    Quando salvar as regras de tramitação
    Então a operação deve concluir dentro de 10s (cronometrar) — se exceder, o critério original "(30s)" e o novo valor entregue estão ambos em risco

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Persistência das alterações**
    Dado que a edição de regras foi concluída sem erro
    Quando reabrir o setor no Organograma
    Então as regras salvas devem refletir exatamente o que foi configurado

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Regressão em ambiente de menor volume**
    Dado um ambiente com poucos setores/módulos
    Quando editar e salvar regras de tramitação pelo Organograma
    Então a operação deve continuar rápida e sem erro, sem piora perceptível em relação ao comportamento anterior

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento (posição na esteira — origem é relato/gravação, ver Descrição)

---

### Informações adicionais

- Demanda relacionada: [MR !505](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/505) (Washington Junior — squad API)
- Observações: **Esteira 3f** ([[Sistema/Contexto/FLUXOS|FLUXOS]]) — task de API, correção já implementada; próximo passo de QA é a validação real com volume alto de setores (item mais importante, pois nenhum teste automatizado mede isso). Relação levantada na triagem com a [[QA Workspace/05 Refinar/Triagem - SP15|SGV-9692]] (mesmo padrão de fix N+1→lote, módulo distinto).
- Histórico:
    - 2026-07-20 - 🐛 Bug cadastrado (a partir da revisão do MR !505 — escopo bate com o problema relatado, critérios de aceite atualizados conforme o que foi implementado, incluindo a divergência do timeout 30s→10s)
