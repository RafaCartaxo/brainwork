---
tags:
  - bug
  - qa
  - etiquetas
task: "10844"
prioridade: baixa
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Toasts de criação e edição de etiqueta com copy divergente da doc

### Descrição

Durante validação foi identificado que, ao criar ou editar uma etiqueta pelo drawer, os toasts exibem **"Etiqueta criada com sucesso!"** e **"Etiqueta editada com sucesso!"**, divergindo dos títulos e corpos previstos na doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]].

---

### Passo a passo para reproduzir

**Dado** que estou no drawer de criação de uma etiqueta
**E** preencho o nome e concluo a criação
**Então** verifico que o toast exibe **"Etiqueta criada com sucesso!"**, em vez do título previsto na doc

**E** quando edito uma etiqueta existente e salvo
**Então** verifico que o toast exibe **"Etiqueta editada com sucesso!"**, também divergente da copy especificada

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10844)


---

### Resultado Esperado

*Fonte: doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]] — tabela de toasts (copy literal).*

- **Criação**: `Etiqueta criada! A etiqueta foi criada e aplicada com sucesso`
- **Edição**: `Etiqueta editada! A etiqueta foi editada e aplicada com sucesso`

O toast de **exclusão** (`Etiqueta excluída com sucesso!`) já está correto e serve de referência para o padrão.

---

### Critérios de aceite

- [ ] Ao criar uma etiqueta pelo drawer, o toast exibe exatamente **"Etiqueta criada! A etiqueta foi criada e aplicada com sucesso"**
- [ ] Ao editar uma etiqueta pelo drawer, o toast exibe exatamente **"Etiqueta editada! A etiqueta foi editada e aplicada com sucesso"**

---

### Casos de Teste Básicos

#### **CT-B01 Toast de criação com a copy da doc**

**Dado** que estou no drawer de criação de uma etiqueta
**Quando** preencho o nome e concluo a criação
**Então** o toast exibe **"Etiqueta criada! A etiqueta foi criada e aplicada com sucesso"**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Toast de edição com a copy da doc**

**Dado** que abri o drawer de edição de uma etiqueta existente
**Quando** altero um campo e salvo
**Então** o toast exibe **"Etiqueta editada! A etiqueta foi editada e aplicada com sucesso"**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão: 12.38.39.2
- Ambiente: Desenvolvimento (`dev-lucas-cabral`)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — achado na validação da refatoração de etiquetas em DEV; corresponde ao **Defeito 5** do card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]], extraído para ticket próprio.

- Observações:
    - O modal de confirmação ao salvar edição foi verificado — comportamento **correto**; não faz parte deste bug.
    - ⚠️ Os subitens da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] estão em 87,50% e não vieram no export — este achado pode ser algo que **ainda não subiu**. Confirmar antes de tratar como bug fechado.
    - Sem evidência por enquanto — captura dedicada pendente.

- Histórico:
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10844; correspondente ao Defeito 5 do card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]])