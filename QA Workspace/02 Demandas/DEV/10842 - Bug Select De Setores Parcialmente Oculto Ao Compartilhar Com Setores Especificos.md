---
tags:
  - bug
  - qa
  - etiquetas
task: "10842"
prioridade: media
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Select de setores parcialmente oculto ao compartilhar a etiqueta com setores específicos

### Descrição

Durante validação foi identificado que, ao iniciar a criação de uma nova etiqueta e compartilhar com **setores específicos**, quando a lista de setores retorna um volume um pouco maior, o **select de setores fica parcialmente oculto** — parte da lista não fica totalmente visível, comprometendo a visualização e a seleção dos setores.

---

### Passo a passo para reproduzir

**Dado** que inicio a criação de uma nova etiqueta
**Quando** compartilho com **setores específicos**, de forma que a lista retorne um volume um pouco maior
**Então** verifico que o **select de setores fica parcialmente oculto**

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10842)

![[10842 - select setores parcialmente oculto.mp4]]


---

### Resultado Esperado

- A lista de setores do select abre **totalmente visível**, com todas as opções legíveis e selecionáveis — sem corte nem ocultação parcial, mesmo com uma lista de setores maior.

---

### Critérios de aceite

- [ ] A lista de setores do select fica **totalmente visível e selecionável** ao compartilhar com setores específicos, sem ocultação parcial mesmo com maior volume de setores

---

### Casos de Teste Básicos

#### **CT-B01 Lista de setores totalmente visível no compartilhamento**

**Dado** que inicio a criação de uma nova etiqueta
**E** seleciono a opção de compartilhar com setores específicos, com uma lista de setores maior
**Quando** abro o select de setores
**Então** a lista abre **totalmente visível**, com todas as opções legíveis e selecionáveis, sem ocultação parcial

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
    - Relacionado ao seletor de setores do drawer (o **Defeito 6** do card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]] cobre itens do mesmo campo — "Selecionados:", contador `+qtd` e limpar todos — mas a **ocultação por volume da lista** é um sintoma distinto).
    - ⚠️ Os subitens da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] estão em 87,50% e não vieram no export — este achado pode ser algo que **ainda não subiu**. Confirmar antes de tratar como bug fechado.
    - Sem evidência por enquanto — captura dedicada pendente.

- Histórico:
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10842; achado na validação da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])