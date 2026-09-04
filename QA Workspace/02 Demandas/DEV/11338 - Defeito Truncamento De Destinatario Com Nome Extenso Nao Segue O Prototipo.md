---
tags:
  - defeito
  - qa
  - despachos
task: "11338"
pai: "11184"
prioridade: media
status: aberto
data_inicio: 2026-09-04
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despachos
ambiente: DEV
---
# Truncamento de destinatário com nome extenso não segue o protótipo (campo de busca sem limite; despacho trunca na 1ª linha)

### Descrição

Durante validação foi identificado que, ao selecionar um destinatário (cidadão) com nome extremamente longo num despacho, o truncamento não segue o especificado no protótipo do Figma em nenhuma das duas superfícies observadas:

1. **Campo "Busque e selecione destinatários"**: o texto do nome extenso não trunca — o campo cresce sem limite, ocupando múltiplas linhas dentro da própria caixa de busca.
2. **Exibição do despacho já emitido**: o texto trunca, mas aparenta truncar já na **1ª linha**, e não sempre na **2ª linha** como especifica o protótipo ("sempre será truncada na segunda linha").

Mesmo mecanismo de truncamento já registrado como CT-012a na [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]] e como CT-B06 (regra geral) / CT-B03 (departamento, mesma família de dropdown) na [[QA Workspace/02 Demandas/DEV/11333 - Bug Exibicao Do Dropdown De Destinatarios Nao Segue O Prototipo Do Figma|SGV-11333]].

---

### Passo a passo para reproduzir

**Dado** que um Departamento está cadastrado com um nome extremamente longo (ex.: string repetida muitas vezes, "Teste nome gigante...")
**Quando** esse Departamento é selecionado no campo "Busque e selecione destinatários" de um despacho
**Então** verifico que o campo de busca cresce sem limite, ocupando múltiplas linhas, sem aplicar truncamento

**Dado** que um despacho foi emitido (ou retificado) com esse destinatário de nome extenso
**Quando** o despacho é exibido na tela
**Então** verifico que o texto trunca já na 1ª linha, e não sempre na 2ª linha como especifica o protótipo

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://11338)

![[11338 - incorreto 1.png]]
![[11338 - incorreto 2.png]]

---

### Resultado Esperado

Mesma regra já especificada no protótipo do Figma (ver [[QA Workspace/02 Demandas/DEV/11333 - Bug Exibicao Do Dropdown De Destinatarios Nao Segue O Prototipo Do Figma|SGV-11333]], seção Resultado Esperado, e CT-012a da SGV-11184):

- O campo de busca/seleção de destinatário não cresce sem limite — aplica o mesmo tratamento de truncate que as demais superfícies.
- Texto extenso de qualquer destinatário **sempre** trunca na **2ª linha**, mantendo a mesma sequência de string até o ponto de corte — nunca trunca já na 1ª linha.

---

### Critérios de aceite

- [ ] Campo "Busque e selecione destinatários" não cresce sem limite com nome extenso — aplica truncamento
- [ ] Despacho exibido com destinatário de nome extenso trunca sempre na 2ª linha, nunca na 1ª

---

### Casos de Teste Básicos

#### **CT-B01 Campo de busca de destinatário não cresce sem limite com nome extenso**

**Dado** que um cidadão tem nome extremamente longo cadastrado
**Quando** é selecionado no campo "Busque e selecione destinatários"
**Então** o campo aplica truncamento, sem crescer sem limite pra múltiplas linhas

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11338 - incorreto 1.png]]

---

#### **CT-B02 Despacho com destinatário de nome extenso trunca sempre na 2ª linha**

**Dado** que um despacho foi emitido/retificado com um destinatário de nome extenso
**Quando** o despacho é exibido
**Então** o texto trunca sempre na 2ª linha, nunca já na 1ª

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11338 - incorreto 2.png]]

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]] — defeito do CT-012a (nunca executado antes deste achado, ver o próprio CT). Relacionado também à [[QA Workspace/02 Demandas/DEV/11333 - Bug Exibicao Do Dropdown De Destinatarios Nao Segue O Prototipo Do Figma|SGV-11333]] (CT-B03/CT-B06) — mesma família de bug de truncamento no dropdown/exibição de destinatário, achada com cidadão nesta rodada.
- Observações:
    - Rafael se referiu a este caso como "truncamento do setor" — as duas evidências mostram um **cidadão** (PF) com nome extenso, não um setor. Registrado como achado com cidadão; se houver também um caso específico de setor não reproduzido aqui, avisar que é um caso adicional.
    - Versão/ambiente exato (qual container `dev-*`) não informado — pendência preencher.
- Histórico:
    - 2026-09-04 - 🐛 Defeito cadastrado (CT-012a da SGV-11184 reprovado; evidência já no vault)
