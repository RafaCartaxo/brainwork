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
ambiente: DEV
---
# [Melhoria-CX] Restringir concessão da permissão "Mesas Alheias" para apenas usuários SOGO e Adm geral

### Descrição

A concessão da permissão "Mesas Alheias" (SGA) deve ser restrita apenas a usuários SOGO e Administrador geral — hoje qualquer perfil com acesso ao gerenciamento de permissões consegue concedê-la.

Contexto de produto (Ivo Costa, 23/07): a permissão foi refatorada visualmente mas não nas regras. Doc de referência: [Usuário Servidor - Atualização permissão de mesas alheias](https://app.notion.com/p/Atualiza-o-permiss-o-de-mesas-alheias-156e5bf55ab4447d9cc101ad31384984). Tarefas relacionadas: [Permitir download de documentos para usuários com permissão "Mesas alheias"](https://app.notion.com/p/Permitir-o-download-de-documentos-para-usu-rios-que-possuam-a-permiss-o-Mesas-alheias-e-dar-op-o--2fe2aec67d308150925bd9176acfc127) e [Acessar mesas alheias de todos os setores](https://app.notion.com/p/Acessar-mesas-alheias-de-todos-os-setores-fff2aec67d30813d895ae756aee3b60e).

---

### Resultado Esperado

Ao gerenciar permissões, a concessão de "Mesas Alheias" só é possível para usuários SOGO ou Adm geral; demais perfis não conseguem concedê-la.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9681)

![[9681 - restringir permissao mesas alheias sogo adm geral reaberta em dev.mp4]]

---

### Critérios de aceite

- [ ] Concessão da permissão "Mesas Alheias" restrita a usuários SOGO e Adm geral
- [ ] Usuário sem permissão vê indicação visual de que a configuração está bloqueada (toggle/seletores desabilitados + informação do motivo) — [Figma](https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=2952-49436)

---

### Casos de Teste Básicos

- **CT-B01 Restrição da concessão de "Mesas Alheias"**
    Dado a tela de gerenciamento de permissões
    Quando um usuário sem perfil SOGO ou Adm geral tenta conceder a permissão "Mesas Alheias"
    Então a concessão deve ser bloqueada/restrita

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [x] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9681 - restringir permissao mesas alheias sogo adm geral reaberta em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: DEV

---

### Informações adicionais

- Demanda relacionada: SGV-9681 (Melhoria-CX, já cadastrada no Notion). Sem card/registro prévio no vault — primeira entrada aqui.
- **Entrega do dev (MR aprovado 26/07)**:
    - Backend: `updatePublicAgent` compara configuração atual de `othersWorkboard` com a enviada — se houver alteração e o usuário não for gestor geral nem SOGO, bloqueia com mensagem de erro de permissão
    - Frontend: `OthersWorkboardConfig` verifica nível de acesso e tipo de usuário para desabilitar toggle + seletores; `MultiSelectSectors` e `CompactChipRenderer` receberam prop `disabled`; `EditSectors` ajustado pra inicializar valores do setor principal
    - Arquivos: `api/src/services/publicAgents/publicAgents.ts`, `web/public/locales/pt-BR/translation.json`, `EditPublicAgent.tsx`, `EditSectors.tsx`, `OthersWorkboardConfig.tsx`, `MultiSelectSectors.tsx`, `CompactChipRenderer.tsx`
- **Pendência de UX** (Rafael Borges, 27/07): necessário mostrar indicação visual para o usuário quando ele não possui permissão — [Figma](https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=2952-49436)
- Testada e **reaberta em DEV** — restrição ainda não funciona como esperado, aguardando correção do dev (contemplar backend + frontend + indicação UX).
- Histórico:
    - 2026-07-27 - 🔴 Melhoria reaberta em DEV
    - 2026-07-28 - Export processado, card atualizado com detalhes do MR e feedback de UX
