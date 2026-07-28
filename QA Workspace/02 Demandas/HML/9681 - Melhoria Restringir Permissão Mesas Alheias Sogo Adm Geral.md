---
tags:
  - melhoria
  - qa
  - mesa-de-trabalho
  - cx
task: "9681"
prioridade: ""
status: aberto
data_inicio: 2026-07-27
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: mesa-de-trabalho
ambiente: HML
deploy: pendente_hml
---
# [Melhoria-CX] Restringir concessão da permissão "Mesas Alheias" para apenas usuários SOGO e Adm geral

### Descrição

A concessão da permissão "Mesas Alheias" (SGA) deve ser restrita apenas a usuários SOGO e Administrador geral — hoje qualquer perfil com acesso ao gerenciamento de permissões consegue concedê-la.

**Quem pode conceder** (regra confirmada com o Rafael, 28/07):

| Perfil | Onde vive | Pode conceder "Mesas Alheias"? |
|---|---|---|
| **Adm SOGO** | colaborador da SOGO | Sim |
| **Adm geral** | dentro da prefeitura / do cliente | Sim |
| Demais níveis de acesso | — | Não |

Quem tem o nível de acesso consegue conceder; quem não tem, não consegue — e a UI precisa deixar isso claro em vez de só falhar: **quem tem permissão vê o toggle de setores**; **quem não tem vê uma tag informativa / tooltip** explicando o motivo (conforme Figma).

Contexto de produto (Ivo Costa, 23/07): a permissão foi refatorada visualmente mas não nas regras. Doc de referência: [Usuário Servidor - Atualização permissão de mesas alheias](https://app.notion.com/p/Atualiza-o-permiss-o-de-mesas-alheias-156e5bf55ab4447d9cc101ad31384984). Tarefas relacionadas: [Permitir download de documentos para usuários com permissão "Mesas alheias"](https://app.notion.com/p/Permitir-o-download-de-documentos-para-usu-rios-que-possuam-a-permiss-o-Mesas-alheias-e-dar-op-o--2fe2aec67d308150925bd9176acfc127) e [Acessar mesas alheias de todos os setores](https://app.notion.com/p/Acessar-mesas-alheias-de-todos-os-setores-fff2aec67d30813d895ae756aee3b60e).

---

### Resultado Esperado

Ao gerenciar permissões, a concessão de "Mesas Alheias" só é possível para usuários SOGO ou Adm geral; demais perfis não conseguem concedê-la.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9681)

![[9681 - restringir permissao mesas alheias aprovado em dev.mp4]]

Histórico da reabertura (27/07, mantida como registro):

![[9681 - restringir permissao mesas alheias sogo adm geral reaberta em dev.mp4]]

---

### Critérios de aceite

- [x] Concessão da permissão "Mesas Alheias" restrita a adm SOGO e adm geral
- [x] Usuário sem permissão vê indicação visual de que a configuração está bloqueada (tag informativa / tooltip com o motivo; toggle de setores visível só pra quem tem permissão) — [Figma](https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=2952-49436)

---

### Casos de Teste Básicos

- **CT-B01 Adm SOGO e adm geral conseguem conceder "Mesas Alheias"**
    Dado a tela de gerenciamento de permissões
    Quando o usuário logado é adm SOGO ou adm geral
    Então consegue conceder a permissão "Mesas Alheias" e vê o toggle de setores

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9681 - restringir permissao mesas alheias aprovado em dev.mp4]]

- **CT-B02 Perfil sem nível de acesso não consegue conceder**
    Dado a tela de gerenciamento de permissões
    Quando o usuário logado não é adm SOGO nem adm geral
    Então a concessão de "Mesas Alheias" é bloqueada

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9681 - restringir permissao mesas alheias aprovado em dev.mp4]]

- **CT-B03 Indicação visual pra quem não tem permissão**
    Dado o usuário sem nível de acesso pra conceder "Mesas Alheias"
    Quando ele abre a configuração de permissões
    Então em vez do toggle de setores ele vê a tag informativa / tooltip explicando por que a configuração está bloqueada

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9681 - restringir permissao mesas alheias aprovado em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: DEV (aprovada — segue pra homologação)

---

### Informações adicionais

- Demanda relacionada: SGV-9681 (Melhoria-CX, já cadastrada no Notion). Sem card/registro prévio no vault — primeira entrada aqui.
- **Entrega do dev (MR aprovado 26/07)**:
    - Backend: `updatePublicAgent` compara configuração atual de `othersWorkboard` com a enviada — se houver alteração e o usuário não for gestor geral nem SOGO, bloqueia com mensagem de erro de permissão
    - Frontend: `OthersWorkboardConfig` verifica nível de acesso e tipo de usuário para desabilitar toggle + seletores; `MultiSelectSectors` e `CompactChipRenderer` receberam prop `disabled`; `EditSectors` ajustado pra inicializar valores do setor principal
    - Arquivos: `api/src/services/publicAgents/publicAgents.ts`, `web/public/locales/pt-BR/translation.json`, `EditPublicAgent.tsx`, `EditSectors.tsx`, `OthersWorkboardConfig.tsx`, `MultiSelectSectors.tsx`, `CompactChipRenderer.tsx`
- **Pendência de UX** (Rafael Borges, 27/07) — **atendida**: a indicação visual pro usuário sem permissão (tag informativa / tooltip com o motivo, em vez do toggle de setores) foi verificada na validação de 28/07. [Figma](https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=2952-49436)
- Trilha: reaberta em DEV em 27/07 (restrição não funcionava) → correção do dev → **retestada e aprovada em DEV** em 28/07, cobrindo backend, frontend e a indicação de UX. Segue pra validação em homologação.
- Histórico:
    - 2026-07-27 - 🔴 Melhoria reaberta em DEV
    - 2026-07-28 - 📝 Melhoria refinada (export processado; escopo do MR mapeado, critério de indicação visual de UX adicionado)
    - 2026-07-28 - 🔁 Melhoria retestada e aprovada em DEV (2 critérios + 3 CTs; segue pra homologação)
