---
tags:
  - bug
  - qa
task: "11226"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-01
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: HML
---
# Setores em cópia divergente do protótipo (exibe todos em vez da quantidade)

### Descrição

Durante validação foi identificado que a linha de setores em cópia está divergente do protótipo (Figma). O protótipo prevê `com cópia para ($qtd)` — texto com a **quantidade** de setores em cópia. O sistema hoje exibe **todos os setores em cópia** por extenso, em vez do texto com a quantidade.

Evidência (`11226 - divergência protótipo setores em cópia.mp4`) traz a comparação lado a lado: **print 02 → Figma 01 (protótipo)** mostrando `com cópia para ($qtd)`, e **01 → Sogov hoje 01** mostrando todos os setores listados em cópia — checar a parte grifada em cada print.

**Possível mesma família da [[QA Workspace/02 Demandas/DEV/10784 - Bug Destinatarios Em Copia De Despacho Divergente Do Prototipo|SGV-10784]]** (ainda aberta, em `DEV/`): aquele card já registra a linha de cópia do despacho divergente do protótipo no mesmo sentido — protótipo com quantidade, produto sem. A 10784 explicitamente descartou "criação de documento" do escopo na época ("foi conferida e não apresenta a divergência"), então se este achado for na criação de documento (não no despacho), pode ser uma regressão nova em área antes checada; se for no despacho, pode ser a mesma divergência da 10784 revalidada. Não linkei como duplicata — avaliar com o Rafael antes de fechar como a mesma coisa (ver Observações).

---

### Passo a passo para reproduzir

Dado que eu tenho setores em cópia num documento/despacho
Quando eu comparo a exibição com o protótipo (Figma)
Então verifico que o sistema mostra todos os setores em cópia por extenso, em vez do texto `com cópia para ($qtd)` previsto no protótipo

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11226)

![[11226 - divergência protótipo setores em cópia.mp4]]

---

### Resultado Esperado

- A linha de cópia exibe `com cópia para ($qtd)`, com a quantidade de setores em cópia, igual ao protótipo

---

### Critérios de aceite

- [ ] A linha de cópia informa a quantidade de setores em cópia, no formato `com cópia para ($qtd)`
- [ ] O comportamento bate com o protótipo (Figma) nos dois pontos comparados na evidência

---

### Casos de Teste Básicos

#### **CT-B01 Linha de cópia exibe a quantidade de setores, igual ao protótipo**

**Dado** que eu tenho setores em cópia num documento/despacho
**Quando** eu observo a linha de cópia
**Então** ela exibe `com cópia para ($qtd)`, igual ao protótipo (Figma)

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada:
- Observações: Confirmar com o Rafael se é a mesma divergência da [[QA Workspace/02 Demandas/DEV/10784 - Bug Destinatarios Em Copia De Despacho Divergente Do Prototipo|SGV-10784]] (mesmo padrão protótipo-com-quantidade × produto-sem) ou achado novo em tela diferente — a 10784 é especificamente do despacho e tinha descartado a criação de documento do escopo na época. `modulo: despacho` foi inferido por essa semelhança; corrigir se o achado for em outra tela.
- Histórico:
    - 2026-09-01 - 🐛 Bug cadastrado
