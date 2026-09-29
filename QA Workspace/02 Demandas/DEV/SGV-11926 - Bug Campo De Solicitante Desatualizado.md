---
tags:
  - bug
  - qa
  - servicos-e-assuntos
task: "11926"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-29
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-e-assuntos
ambiente: DEV
---
# Campo de solicitante desatualizado — sem atalho de criação rápida

### Descrição

O componente do campo de solicitante, herdado de outro módulo e usado na construção do formulário (aba de formulário de Serviços e Assuntos), está desatualizado em relação a uma regra nova: "Qualquer campo do tipo pessoa ou componente de seleção de usuário no qual seja possível adicionar um cidadão deve, agora, conter um atalho para a criação rápida deste, seja ele pessoa física ou jurídica." Isso impacta diretamente a demanda de cadastro rápido, que depende desse atalho estar presente em todo campo de seleção de pessoa/usuário.

---

### Passo a passo para reproduzir

**Dado** que o usuário está na construção de um formulário com campo de solicitante
**Quando** ele abre o componente de seleção de pessoa nesse campo
**Então** verifico que não existe o atalho de criação rápida de cidadão (pessoa física ou jurídica), diferente do que a regra exige agora

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11926)

![[11926 - Campo solicitante do formulário com componente desatualziado.mp4]]

---

### Resultado Esperado

Campo de solicitante (e qualquer outro campo do tipo pessoa/componente de seleção de usuário onde seja possível adicionar um cidadão) contém o atalho de criação rápida, para pessoa física ou jurídica.

---

### Critérios de aceite

- [ ] Campo de solicitante na construção do formulário exibe o atalho de criação rápida de cidadão (PF ou PJ)
- [ ] O componente atualizado não regride nenhum comportamento existente de seleção/busca de solicitante

---

### Casos de Teste Básicos

#### **CT-B01 Atalho de criação rápida no campo de solicitante**

**Dado** que o usuário está construindo um formulário com campo de solicitante
**Quando** ele abre o componente de seleção de pessoa desse campo
**Então** o atalho de criação rápida (PF ou PJ) está disponível

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11926 - Campo solicitante do formulário com componente desatualziado.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Observações: componente compartilhado/herdado de outro módulo — vale checar se outros campos do tipo pessoa que usam o mesmo componente têm o mesmo problema, além do campo de solicitante.
- Histórico:
    - 2026-09-29 - 🐛 Bug cadastrado
