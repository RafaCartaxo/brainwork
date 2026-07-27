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

---

### Resultado Esperado

Ao gerenciar permissões, a concessão de "Mesas Alheias" só é possível para usuários SOGO ou Adm geral; demais perfis não conseguem concedê-la.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9681)

![[9681 - restringir permissao mesas alheias sogo adm geral reaberta em dev.mp4]]

---

### Critérios de aceite

- [ ] Concessão da permissão "Mesas Alheias" restrita a usuários SOGO e Adm geral

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
- Testada e **reaberta em DEV** — restrição ainda não funciona como esperado, aguardando correção do dev.
- Histórico:
    - 2026-07-27 - 🔴 Melhoria reaberta em DEV
