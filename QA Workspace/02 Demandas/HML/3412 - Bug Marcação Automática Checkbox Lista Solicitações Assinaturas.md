---
tags:
  - bug
  - qa
  - assinatura
task: "3412"
prioridade: media
status: aberto
data: 2026-07-22
data_inicio: 2026-07-22
responsavel: Rafael
modulo: assinaturas
ambiente: HML
---
# Marcação automática incorreta de checkbox na Lista de Solicitações de Assinaturas

### Descrição

Durante validação foi identificado que, na Lista de Solicitações de Assinaturas, um checkbox é marcado automaticamente de forma indevida, sem ação do usuário.

---

### Passo a passo para reproduzir

Dado que o usuário acesse a Lista de Solicitações de Assinaturas
Quando a lista for exibida
Então um checkbox aparece marcado automaticamente, sem que o usuário o tenha selecionado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://3412)

![[3412 - marcacao automatica checkbox lista solicitacoes assinaturas aprovado em dev.mp4]]

---

### Resultado Esperado

Nenhum checkbox da Lista de Solicitações de Assinaturas deve ser marcado automaticamente. A seleção deve ocorrer apenas por ação explícita do usuário.

---

### Critérios de aceite

- [x] Ao abrir a Lista de Solicitações de Assinaturas, nenhum checkbox deve estar marcado sem ação do usuário

---

### Casos de Teste Básicos

- **CT-B01 Checkbox não deve ser marcado automaticamente na Lista de Solicitações de Assinaturas**
    Dado que o usuário acesse a Lista de Solicitações de Assinaturas
    Quando a lista for exibida
    Então nenhum checkbox deve estar marcado sem ação do usuário

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes: ![[3412 - marcacao automatica checkbox lista solicitacoes assinaturas aprovado em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-3412
- Observações: Card criado em modo enxuto (relato rápido) — descrição destilada do título, sem passo a passo técnico detalhado disponível. Gate de doc: [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|doc de Assinaturas]] conferida — não descreve marcação automática de checkbox na lista de solicitações; sem divergência com o comportamento aprovado (checkbox não deve marcar sozinho).
- Histórico:
    - 2026-07-22 - 🐛 Bug cadastrado
    - 2026-07-22 - ✅ Aprovada em DEV (Rafael)
