---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11312"
pai: "11184"
prioridade: media
status: resolvido
data_inicio: 2026-09-03
data_fim: "2026-09-03"
responsavel: Rafael
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Área de clique do accordion de departamento não segue o padrão do Figma

### Descrição

Durante a validação do CT-002c da [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]] foi identificado que a área de clique do accordion do departamento não respeita o padrão definido no Figma — a distinção entre clicar no ícone de chevron (expandir/recolher os participantes) e clicar na linha do departamento (selecioná-lo como destinatário) não está sendo aplicada como especificado. Comportamento exato observado, ver gravação em Evidências.

---

### Passo a passo para reproduzir

**Dado** que um departamento é exibido como accordion no resultado de busca (campo pessoa de documento ou destinatário de despacho)
**Quando** o servidor clica no ícone de chevron para expandir/recolher, ou clica em qualquer outro ponto da linha do departamento para selecioná-lo
**Então** verifico que a área de clique não segue a regra do Figma — chevron e seleção não se comportam como dois alvos de clique independentes

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://11312)

![[11312 - área de clique não respeitada.mp4]]

---

### Resultado Esperado

- Área de clique do accordion (expandir/recolher) restrita a área de seleção.
- Selecionar o departamento como destinatário usa a linha inteira, do início do nome ao fim do container, com a mesma estética de hover de seleção já implementada.
- As duas ações não interferem entre si.

---

### Critérios de aceite

- [ ] Clicar no ícone de chevron e em sua aréa de seleção expande ou recolhe o accordion, sem selecionar o departamento
- [ ] Clicar em qualquer outro ponto da linha do departamento seleciona-o como destinatário, sem expandir/recolher o accordion

---

### Casos de Teste Básicos

#### **CT-B01 Área de clique do accordion respeita a distinção chevron × linha**

**Dado** que um departamento é exibido como accordion no resultado de busca
**Quando** o servidor clica no ícone de chevron
**Então** o accordion expande/recolhe, sem selecionar o departamento
**E quando** clica em qualquer outro ponto da linha
**Então** o departamento é selecionado como destinatário, sem expandir/recolher o accordion

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!success]- Reprovado em 03/09, aprovado no reteste de 03/09
> Corrigido e reteste passou — gravação da execução abaixo, junto com a evidência que registrou o problema original.

**Evidências de Testes:**

![[11312 - área de clique não respeitada.mp4]]
![[11312 - OK.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]] — defeito do CT-002c, achado na validação em DEV.
- Observações:
    - Versão/ambiente exato (qual container `dev-*`) não informado — pendência preencher.
- Histórico:
    - 2026-09-03 - 🐛 Defeito cadastrado (CT-002c da SGV-11184 reprovado)
    - 2026-09-03 - ✅ Aprovado em DEV (corrigido, reteste OK) — card fechado sem etapa de HML: é defeito da [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]], validação em homologação acontece pela task principal
