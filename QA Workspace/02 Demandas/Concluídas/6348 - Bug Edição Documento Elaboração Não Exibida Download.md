---
tags:
  - bug
  - qa
  - documento
task: "6348"
prioridade: media
status: resolvido
data_inicio: 2026-07-24
data_fim: 2026-07-24
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Edição de documentos "Em elaboração" não é exibida ao baixar documento

### Descrição

Documentos **"Em elaboração"** editados não refletiam a edição ao serem baixados — o mesmo **problema em comum** de [[QA Workspace/02 Demandas/Concluídas/6083 - Bug Edição Documento Não Atualiza Download Assinatura|SGV-6083]] e [[QA Workspace/02 Demandas/Concluídas/6873 - Bug Download Documento Temporário Não Reflete Edição|SGV-6873]] (edição não refletida no download). (Origem Notion SGV-6348, Matheus Godoi, Squad 2.)

---

### Resultado Esperado

Editar um documento "Em elaboração" e baixá-lo reflete o conteúdo atualizado.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://6348)

- Sem cópia local — resolvida via a correção comum (ver Histórico), sem validação funcional independente do próprio fix.

---

### Critérios de aceite

- [x] Editar um documento "Em elaboração" e baixá-lo reflete a última edição — coberto pela correção comum (ver ressalva no Histórico)

---

### Casos de Teste Básicos

- **CT-B01 Download de documento "Em elaboração" reflete a edição**
    Dado um documento "Em elaboração" editado
    Quando o servidor faz o download
    Então o arquivo baixado reflete a última edição

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span> (coberto pela correção comum de 6083/6873 — ver ressalva)
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: SGV-6348 (Matheus Godoi, Squad 2). Raiz comum com SGV-6083 e SGV-6873.
- **Rastreio da resolução (IMPORTANTE — leia antes de reabrir ou cobrar teste)**:
    - SGV-6348 tinha um fix **próprio** (`fix/6348`, commits `f8d1cb4e` "evita carregar dados desnecessários da instância na regeneração do pdf" + `a8df3485` "corrige download de documentos e loga erro em caso de falha"), tocando o mesmo arquivo (`api/src/services/documentObjects/documentObjects.ts`) da correção comum de 6083/6873, mas **em commit separado**.
    - **O branch `fix/6348` nunca foi mergeado** — nem dentro do `fix/6083`, nem em `development`. Ou seja, **o código específico da 6348 não está em produção/homologação**.
    - Rafael decidiu **fechar a ticket e a MR do 6348 sem mergear o fix próprio** — considerando o sintoma coberto pela correção comum já aprovada em homologação (6083/6873), tornando o fix isolado da 6348 desnecessário/redundante.
    - **Isso NÃO é uma validação funcional do fix da 6348** (que nem chegou a subir) — é uma decisão de QA/Produto de que o sintoma já está resolvido pela raiz comum. Se o comportamento específico "Em elaboração" reaparecer, **não presumir que o fix da 6348 resolveria** — ele nunca foi testado nem mergeado.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] não cobre "download refletir a edição" — sem divergência; gap de doc (fluxo 8, junto com 6083/6873).
- Histórico:
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa; sem export completo)
    - 2026-07-24 - 🔎 Analisado: fix próprio (`fix/6348`) separado do fix comum de 6083/6873, mesmo arquivo — branch nunca mergeado
    - 2026-07-24 - ✅ Resolvida **por decisão de QA** (sintoma coberto pela correção comum 6083/6873) — **sem validação funcional do fix próprio, que não foi mergeado**
    - 2026-07-24 - 🔒 MR fechada no GitLab **sem merge** (fix próprio considerado desnecessário/redundante)
