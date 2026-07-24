---
tags:
  - bug
  - qa
  - assinatura
task: "5360"
prioridade: media
status: aberto
data_inicio: 2026-07-24
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
---
# Assinatura de despacho customizado não aparece na tela de "Assinaturas pendentes" do servidor

### Descrição

Ao solicitar assinatura num **despacho customizado**, a solicitação pendente **não aparece** na tela de "Assinaturas pendentes" do servidor (tela inicial, CTA de solicitações pendentes) — diferente do comportamento esperado pra despachos normais. (Origem Notion SGV-5360, João Marcelo, Squad 3.)

---

### Resultado Esperado

Solicitação de assinatura em despacho customizado aparece normalmente na tela de "Assinaturas pendentes" do servidor, no mesmo fluxo que despachos regulares.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://5360)

![[5360 - assinatura despacho customizado aparece pendentes aprovado em dev.mp4]]

---

### Critérios de aceite

- [x] Solicitação de assinatura num despacho customizado aparece na tela de "Assinaturas pendentes" do servidor

---

### Casos de Teste Básicos

- **CT-B01 Assinatura de despacho customizado aparece nas pendências**
    Dado um despacho customizado com solicitação de assinatura pendente para um servidor
    Quando o servidor acessa a tela inicial / "Assinaturas pendentes"
    Então a solicitação do despacho customizado aparece normalmente na lista

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[5360 - assinatura despacho customizado aparece pendentes aprovado em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML (aprovada em DEV — segue pra homologação)

---

### Informações adicionais

- Demanda relacionada: SGV-5360 (origem Notion; Sprint SP15/SP16; João Marcelo, Squad 3). Notion mudou de Backlog → Em desenvolvimento em 22/07.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] descreve a entrada da tela inicial (CTA de solicitações pendentes) só pra assinatura em massa, e não distingue **despacho customizado** de despacho regular — sem divergência com o aprovado; gap de doc (fluxo 8).
- Histórico:
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa da validação; sem export completo)
    - 2026-07-24 - ✅ Aprovada em DEV — segue pra homologação (card criado direto em `02 Demandas/HML/`, `ambiente: HML`)
