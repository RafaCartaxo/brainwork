---
tags:
  - bug
  - qa
  - etiquetas
task: "10833"
prioridade: media
status: resolvido
data_inicio: 2026-08-13
data_fim: "2026-08-17"
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

![[10833 - pt2.mp4]]

![[10833 - botão de opções de etiqueta esta ficando oculto.mp4]]


---

### Resultado Esperado

- As etiquetas do fim da lista — e as respectivas opções — ficam **totalmente visíveis e clicáveis**, sem serem cortadas ou cobertas na borda do container do submenu "Etiquetas >".

---

### Critérios de aceite

- [x] As opções das etiquetas do fim da lista do submenu "Etiquetas >" ficam **totalmente visíveis e acionáveis**, sem ocultação parcial

---

### Casos de Teste Básicos

#### **CT-B01 Opções das últimas etiquetas totalmente visíveis e acionáveis**

**Dado** que eu acesso o ambiente como Servidor
**E** abri o submenu "Etiquetas >" pelo meatball
**Quando** clico nas opções das últimas etiquetas da lista
**Então** as opções ficam **totalmente visíveis e acionáveis**, sem ocultação parcial

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[10833 - reteste ok, opcoes das ultimas etiquetas visiveis no submenu.mp4]]

---

### Ambiente

- Versão: 12.38.39.2
- Ambiente: Desenvolvimento (`dev-lucas-cabral`)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — achado na validação da refatoração de etiquetas em DEV.
    
- Observações:
    - ✅ **Registrado como o Defeito 8** do card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]] (novo, não relacionado aos itens 1–7) e cruzado na tabela "Bugs encontrados" da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]].
    - ⚠️ Os subitens da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] estão em 87,50% e não vieram no export — este achado pode ser algo que **ainda não subiu**. Confirmar antes de tratar como bug fechado.

- Histórico:
    - 2026-08-17 - ✅ Aprovada em DEV (defeito corrigido, reteste OK) — card fechado **sem etapa de HML**: é defeito da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] e a validação em homologação acontece pela task principal (decisão do Rafael em 17/08)
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10833; achado na validação da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])