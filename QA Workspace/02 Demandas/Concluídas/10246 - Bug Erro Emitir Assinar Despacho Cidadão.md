---
tags:
  - bug
  - qa
  - assinatura
task: "10246"
prioridade: altíssima
status: resolvido
data_inicio: 2026-07-24
data_fim: 2026-07-24
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
---
# Erro ao emitir e assinar despacho como cidadão

### Descrição

Ao emitir um despacho e assinar junto (fluxo "emitir e assinar"), o cidadão recebia um **erro** — a ação não era concluída com sucesso. (Origem Notion SGV-10246, João Marcelo, Squad 3.)

---

### Resultado Esperado

O cidadão consegue emitir um despacho e assiná-lo no mesmo fluxo ("emitir e assinar"), sem erros.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10246)

![[10246 - assinatura emitir e assinar cidadao aprovado em homologacao.mp4]]

**Histórico de tentativas**: 1ª validação (23/07) **reprovada** — vídeo `10246 - primeira validação nok.mp4` (mantido na raiz de Evidências, não movido — ver anotação). Correção aplicada, retestada e **aprovada** hoje (24/07).

---

### Critérios de aceite

- [x] Cidadão emite despacho e assina junto ("emitir e assinar") sem erros

---

### Casos de Teste Básicos

- **CT-B01 Cidadão emite e assina despacho com sucesso**
    Dado um cidadão com permissão de assinatura num despacho
    Quando ele emitir o despacho e assinar no mesmo fluxo ("emitir e assinar")
    Então a ação é concluída sem erros, com o despacho emitido e a assinatura realizada

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[10246 - assinatura emitir e assinar cidadao aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML (reprovada em 1ª validação 23/07; retestada e aprovada em homologação 24/07)

---

### Informações adicionais

- Demanda relacionada: SGV-10246 (origem Notion; Sprint SP15/SP16; João Marcelo, Squad 3). Notion avançou Revisar MR → Disponível para homologação (Release homolog, 24/07) → aprovada por QA (24/07).
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] já documenta o fluxo "emitindo um despacho e assinando junto" para cidadãos (seção "Emitindo um despacho e assinando-o") — o bug era falha de implementação num fluxo já documentado, não regra de negócio nova. Sem divergência, sem gap de doc.
- Histórico:
    - 2026-07-23 - 🔴 1ª validação em homologação reprovada (erro ao emitir e assinar como cidadão)
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa; sem export completo)
    - 2026-07-24 - 🔁 Retestada e aprovada em homologação
