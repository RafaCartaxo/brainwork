---
tags:
  - bug
  - qa
  - despacho
task: "10740"
prioridade: media
status: resolvido
data_inicio: 2026-08-11
data_fim: "2026-08-14"
responsavel: Rafael
cadastrado_por: Rafael
modulo: despacho
ambiente: HML
---
# Divergências de protótipo na exibição do despacho

### Descrição

Durante validação foi identificado que a exibição do despacho diverge do protótipo em **três pontos**: a posição do horário do despacho, o botão de "Exibir detalhes" e o alinhamento de "Ver interações".

Encontrado durante a validação da [[QA Workspace/02 Demandas/Concluídas/9011 - Melhoria Exibicao Conteudo Completo Despachos|SGV-9011]], que por isso foi reaberta em DEV.

---

### Passo a passo para reproduzir

Dado que estou na visualização de um documento
Quando crio despacho com cópia
Então verifico as 3 divergências em relação ao protótipo

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10740)

![[10740 - divergencias de prototipo na exibicao do despacho.png]]
*Mesma evidência cobre CT-B01, CT-B02 e CT-B03 — as setas apontam os três pontos.*

---

### Resultado Esperado

- O **horário do despacho** é exibido na posição prevista no protótipo
- O botão **"Exibir detalhes"** segue o protótipo
- O **"Ver interações"** segue o alinhamento previsto no protótipo

Referência de protótipo: Figma **Tramitação — Handoff**, nó [`8601-2511`](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8601-2511).

---

### Critérios de aceite

- [x] O horário do despacho aparece na posição definida no protótipo
- [x] O botão "Exibir detalhes" aparece conforme o protótipo
- [x] O "Ver interações" aparece alinhado conforme o protótipo

---

### Casos de Teste Básicos

#### **CT-B01 Posição do horário do despacho**

**Dado** que estou na visualização de um documento
**Quando** crio despacho com cópia
**Então** verifico que o horário do despacho aparece na posição prevista no protótipo

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10740 - divergencias de prototipo na exibicao do despacho.png]]

---

#### **CT-B02 Botão "Exibir detalhes"**

**Dado** que estou na visualização de um documento
**Quando** crio despacho com cópia
**Então** verifico que o botão "Exibir detalhes" segue o protótipo

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10740 - divergencias de prototipo na exibicao do despacho.png]]
*Mesma evidência do CT-B01.*

---

#### **CT-B03 Alinhamento de "Ver interações"**

**Dado** que estou na visualização de um documento
**Quando** crio despacho com cópia
**Então** verifico que o "Ver interações" segue o alinhamento previsto no protótipo

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10740 - divergencias de prototipo na exibicao do despacho.png]]
*Mesma evidência do CT-B01.*

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/Concluídas/9011 - Melhoria Exibicao Conteudo Completo Despachos|SGV-9011]] — a melhoria foi **reaberta em DEV** por conta deste defeito (fluxo [[Sistema/Contexto/FLUXOS#3g. Reprovação com bug novo (SGV próprio)|3g]])
- Observações:
    - Defeito **visual//de layout**, sem perda de função — os três pontos são divergência de posicionamento e alinhamento contra o protótipo.
    - As três divergências foram cadastradas como **um defeito só** no Notion, com uma evidência única. Um CT por divergência mantém a rastreabilidade individual sem quebrar isso.
    - O protótipo (Figma `8601-2511`) não foi lido nesta sessão — o resultado esperado remete a ele em vez de reproduzir medidas, conforme a regra de que **medida de handoff não é critério de aceite** ([[Sistema/Skills/SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]]).
- Histórico:
    - 2026-08-11 - 🐛 Bug cadastrado
    - 2026-08-14 - ✅ Aprovada em homologação
