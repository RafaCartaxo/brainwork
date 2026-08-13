---
tags:
  - bug
  - qa
  - etiquetas
task: "10833"
prioridade: media
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Opções das últimas etiquetas parcialmente ocultas no submenu "Etiquetas >" do meatball

### Descrição

Durante validação foi identificado que, ao acessar o submenu **"Etiquetas >"** pelo meatball, as etiquetas das últimas posições da lista aparecem **parcialmente ocultas**: clicando nas opções das etiquetas do fim da lista, elas ficam cortadas na borda do container — as opções não ficam totalmente visíveis nem acionáveis.

---

### Passo a passo para reproduzir

**Dado** que eu acesso o ambiente como Servidor
**E** verifico o meatball e clico em **"Etiquetas >"**
**Quando** clico nas opções das últimas etiquetas da lista
**Então** verifico que elas ficam **parcialmente ocultas**

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10833)

![[10833 - botão de opções de etiqueta esta ficando oculto.mp4]]


---

### Resultado Esperado

- As etiquetas do fim da lista — e as respectivas opções — ficam **totalmente visíveis e clicáveis**, sem serem cortadas ou cobertas na borda do container do submenu "Etiquetas >".

---

### Critérios de aceite

- [ ] As opções das etiquetas do fim da lista do submenu "Etiquetas >" ficam **totalmente visíveis e acionáveis**, sem ocultação parcial

---

### Casos de Teste Básicos

#### **CT-B01 Opções das últimas etiquetas totalmente visíveis e acionáveis**

**Dado** que eu acesso o ambiente como Servidor
**E** abri o submenu "Etiquetas >" pelo meatball
**Quando** clico nas opções das últimas etiquetas da lista
**Então** as opções ficam **totalmente visíveis e acionáveis**, sem ocultação parcial

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
    - ⚠️ Os subitens da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] estão em 87,50% e não vieram no export — este achado pode ser algo que **ainda não subiu**. Confirmar antes de tratar como bug fechado.
    - Sem evidência por enquanto — captura dedicada pendente.

- Histórico:
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10833; achado na validação da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])