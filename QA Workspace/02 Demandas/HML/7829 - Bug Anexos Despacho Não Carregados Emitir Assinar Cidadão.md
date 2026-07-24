---
tags:
  - bug
  - qa
  - assinatura
task: "7829"
prioridade: media
status: aberto
data_inicio: 2026-07-24
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
---
# Anexos do despacho não são carregados corretamente ao emitir e assinar como Cidadão

### Descrição

Ao emitir e assinar um despacho como cidadão, os **anexos não carregam corretamente**. Validação em homologação (24/07) constatou **atendimento parcial**: anexos do tipo **PDF carregam normalmente**, mas anexos do tipo **imagem (IMG) não carregam**. (Origem Notion SGV-7829, João Marcelo, Squad 3.)

---

### Resultado Esperado

Ao emitir e assinar um despacho como cidadão, todos os anexos — independente do tipo (PDF, imagem, etc.) — carregam corretamente.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://7829)

![[7829 - anexos despacho pdf ok imagem nao carrega reaberta em homologacao.mp4]]

---

### Critérios de aceite

- [x] Anexos do tipo PDF carregam corretamente ao emitir e assinar como cidadão
- [ ] Anexos do tipo imagem (IMG) carregam corretamente ao emitir e assinar como cidadão

---

### Casos de Teste Básicos

- **CT-B01 Anexo PDF carrega corretamente**
    Dado um despacho com anexo em PDF
    Quando o cidadão emitir e assinar o despacho
    Então o anexo PDF carrega corretamente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[7829 - anexos despacho pdf ok imagem nao carrega reaberta em homologacao.mp4]]

- **CT-B02 Anexo do tipo imagem carrega corretamente**
    Dado um despacho com anexo em imagem (ex.: JPG/PNG)
    Quando o cidadão emitir e assinar o despacho
    Então o anexo de imagem carrega corretamente

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [x] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[7829 - anexos despacho pdf ok imagem nao carrega reaberta em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML (validado 24/07 — atendimento parcial, reaberta)

---

### Informações adicionais

- Demanda relacionada: SGV-7829 (origem Notion; Sprint SP15/SP16; João Marcelo, Squad 3). Notion: Revisar MR → Em impedimento (22/07) → Disponível para homologação (Release homolog, 24/07).
- **Reabertura parcial, sem bloqueio de publicação**: o fix resolveu o caso mais comum (PDF), mas não cobre anexos de imagem. Rafael optou por **não impedir a publicação do código** (o ganho já é real) — o card segue **reaberto** pra cobrir o caso de imagem numa próxima iteração do dev.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] documenta o fluxo de anexos em solicitação/emissão de despacho, mas não distingue comportamento por **tipo de arquivo** do anexo (PDF vs imagem) — sem divergência de regra; é bug de implementação específico de imagem, não gap de documentação de negócio.
- Histórico:
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa da validação; sem export completo)
    - 2026-07-24 - 🔴 Reaberta em homologação (atendimento parcial: PDF ok, imagem não carrega) — sem bloqueio de publicação do código
