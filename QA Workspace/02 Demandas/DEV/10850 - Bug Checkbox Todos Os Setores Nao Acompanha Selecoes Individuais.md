---
tags:
  - bug
  - qa
  - etiquetas
task: "10850"
prioridade: media
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Checkbox "Todos os setores" não acompanha o estado das seleções individuais de setores

### Descrição

Durante validação foi identificado que, ao compartilhar uma etiqueta com **setores específicos**, o checkbox mestre **"Todos os setores"** do seletor não reflete o estado das seleções individuais: clicar nele não marca corretamente todos os setores da lista, e selecionar/desselecionar setores individualmente não atualiza o mestre para os estados esperados (todos marcados → cheio; alguns marcados → parcial/indeterminado; nenhum → vazio).

---

### Passo a passo para reproduzir

**Dado** que inicio a criação/edição de uma etiqueta e escolho **compartilhar com setores específicos**
**Quando** eu clico no checkbox **"Todos os setores"** e, em seguida, seleciono e desseleciono setores individualmente
**Então** verifico que o checkbox mestre **não acompanha** as seleções — não marca todos ao ser acionado, nem transita para os estados cheio/parcial/vazio conforme as seleções individuais

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10850)

![[10850 - checkbox nok.mp4]]

*Sem evidência por enquanto.*

---

### Resultado Esperado

- Clicar em **"Todos os setores"** seleciona **todos** os setores da lista (todos marcados/verdes), e um novo clique desseleciona todos.
- Ao selecionar/desselecionar setores individualmente, o checkbox mestre **sincroniza**: **cheio** quando todos estão marcados, **parcial/indeterminado** quando alguns estão, e **vazio** quando nenhum está.

---

### Critérios de aceite

- [ ] O checkbox **"Todos os setores"** seleciona e desseleciona todos os setores da lista ao ser acionado
- [ ] As seleções individuais atualizam o checkbox mestre para **cheio**, **parcial/indeterminado** ou **vazio**, conforme o estado da lista

---

### Casos de Teste Básicos

#### **CT-B01 Estado do checkbox mestre acompanha as seleções de setores**

**Dado** que escolhi compartilhar com setores específicos
**E** que o seletor de setores está aberto
**Quando** eu aciono "Todos os setores" e, depois, seleciono e desseleciono setores individualmente
**Então** o checkbox mestre marca todos ao ser acionado e reflete os estados cheio/parcial/vazio conforme as seleções

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

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — achado na validação da refatoração de etiquetas em DEV.

- Observações:
    - Relacionado ao seletor de setores do drawer — nota de **vizinhança** (não duplicata) adicionada no card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]]: o **Defeito 6** cobre a ausência de "Selecionados:", contador `+qtd` e limpar todos; a [[QA Workspace/02 Demandas/Concluídas/10842 - Bug Select De Setores Parcialmente Oculto Ao Compartilhar Com Setores Especificos|SGV-10842]] cobre a ocultação do select por volume; este card cobre a **sincronização do checkbox mestre "Todos os setores"** com as seleções individuais — sintomas distintos do mesmo campo.
    - ⚠️ Os subitens da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] estão em 87,50% e não vieram no export — este achado pode ser algo que **ainda não subiu**. Confirmar antes de tratar como bug fechado.

- Histórico:
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10850; achado na validação da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])
