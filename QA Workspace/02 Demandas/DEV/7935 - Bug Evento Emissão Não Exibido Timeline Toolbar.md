---
tags:
  - bug
  - qa
  - documento
task: "7935"
prioridade: altíssima
status: aberto
data_inicio: 2026-07-24
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: DEV
---
# Evento de emissão de documento não é exibido na timeline ao emitir pela toolbar

### Descrição

Ao clicar em "Emitir" pela toolbar do documento, o **evento de emissão não é exibido na timeline**. Reproduzido ao criar um documento oficial em elaboração e emitir: o documento é emitido, mas nenhum evento de emissão é registrado/exibido. (Origem: Notion SGV-7935, dev Diogo Sobreira, Squad 1; correção no [MR !608](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/608).)

---

### Passo a passo para reproduzir

Dado que estou logado como servidor
E crio um documento oficial
E salvo com status "Em elaboração"
Quando clico em "Emitir" (pela toolbar)
Então o documento é emitido, porém **não exibe o evento de emissão** na timeline

---

### Resultado Esperado

Ao emitir pela toolbar, o evento de emissão é registrado com sucesso e **exibido corretamente na timeline** do documento. Referência de layout: [Figma Tramitação — Handoff](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=6040-6280).

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://7935)

- Evidência local entra no fluxo normal quando houver validação em homologação.

---

### Critérios de aceite

- [ ] Ao clicar em "Emitir" pela toolbar, o evento de emissão é **registrado** com sucesso
- [ ] O evento de emissão é **exibido corretamente na timeline** do documento

---

### Casos de Teste Básicos

- **CT-B01 Emitir pela toolbar registra o evento de emissão**
    Dado um documento oficial "Em elaboração"
    Quando o servidor emite pela toolbar (status vai de rascunho para emitido)
    Então um evento de emissão é criado no documento (com autor, setor e assinatura textual do emissor)

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Evento de emissão aparece na timeline**
    Dado um documento emitido pela toolbar
    Quando o servidor abre a timeline do documento
    Então o evento de emissão é exibido corretamente (card do evento renderizado)

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Não duplicar/registrar emissão indevida**
    Dado um documento que não passou por emissão pela toolbar (ou já emitido)
    Quando a mudança de status não é a emissão inicial
    Então nenhum evento de emissão indevido é criado

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão: 12.4.11.2
- Ambiente: validação direto em homologação (task de sustentação; correção já em revisão de MR — sem etapa de validação em DEV)

---

### Informações adicionais

- Demanda relacionada: SGV-7935 (origem Notion; Sprint SP15/SP16; dev Diogo Sobreira, Squad 1 - Rogue One; revisor Washington Junior; prioridade **Altíssima** conforme Triagem SP15). Relacionada a SGV-7963.
- **Escopo do MR !608** (revisão de 2026-07-24): o fix cria um evento `ISSUED` ao mudar o status do documento de DRAFT→OPEN (emissão), com `eventHistory` (setor dono, cargo, iniciais, assinatura textual, nível de acesso); migration adiciona o tipo de evento `ISSUED`; o lado web (`DocumentEventCard.tsx` + tradução) passa a renderizar o card do evento na timeline.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] descreve eventos de **geração** (documento gerado a partir de outro), mas **não cobre o evento de emissão** (DRAFT→OPEN) na timeline — sem divergência com o aprovado; gap de doc registrado (fluxo 8).
- Histórico:
    - 2026-07-24 - 📝 Bug importado do Notion (modo B, card direto do export) — descrição, passo a passo e 2 critérios de aceite já vinham completos
    - 2026-07-24 - 👍 [MR !608](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/608) **aprovado pela QA** no code review (nível de cenários — escopo bate, liberado). Não é validação funcional: o "exibido na timeline" (critério 2) segue pra validação manual em HML. Card segue `aberto`.
    - 2026-07-24 - 🔎 Cenários de teste do [MR !608](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/608) (commit `294596c9`) revisados a nível de escopo — 3 cenários em `documentObjects.test.ts` ("changeDocumentStatus - evento de emissão pela toolbar (SGV-7935)"): (1) emissão pela toolbar cria o evento (autor=emissor, setor, `eventHistory`, `isIssued=true`, código real ≠ provisório); (2) caso negativo → nenhum evento criado; (3) caso de erro → rejeita e não cria evento. **Cruzamento**: critério 1 (evento registrado) ✅ coberto pela cenário 1. **Achado**: critério 2 (exibido na timeline) é **renderização web** (`DocumentEventCard`), **não coberto** pelos cenários de API — a exibição precisa de validação manual em HML. Cobertura é API/unit. Seguir pra validação real.
