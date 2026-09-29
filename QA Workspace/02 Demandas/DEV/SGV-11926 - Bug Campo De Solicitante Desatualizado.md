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
# Campo de solicitante desatualizado — bloqueia fluxos novos

### Descrição

O componente do campo de solicitante, herdado de outro módulo e usado na criação de documento (busca do destinatário/solicitante), está desatualizado — impede a visualização padronizada e bloqueia fluxos que dependem desse componente estar em dia: seleção de departamento na abertura de documento e o atalho de criação rápida de cidadão exigido pela regra nova ("Qualquer campo do tipo pessoa ou componente de seleção de usuário no qual seja possível adicionar um cidadão deve, agora, conter um atalho para a criação rápida deste, seja ele pessoa física ou jurídica.") — cadastro rápido é a SGV-11178.

---

### Passo a passo para reproduzir

**Dado** que o usuário está na criação de um documento com campo de solicitante herdado do módulo
**Quando** ele digita a pesquisa pelo usuário destinatário
**Então** verifico que o componente está desatualizado, impedindo a visualização padronizadas
**E** impedindo possíveis fluxos, como seleção de departamento na abertura e Cadastro rápido (SGV-11178)

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11926)

![[11926 - Campo solicitante do formulário com componente desatualziado.mp4]]

---

### Resultado Esperado

Campo de solicitante atualizado, com visualização padronizada e habilitando os fluxos que dependem dele: seleção de departamento na abertura do documento e o atalho de criação rápida de cidadão (PF ou PJ, SGV-11178).

---

### Critérios de aceite

- [ ] Campo de solicitante exibe a visualização padronizada do componente atual
- [ ] Campo de solicitante permite seleção de departamento na abertura de documento
- [ ] Campo de solicitante exibe o atalho de criação rápida de cidadão (PF ou PJ)
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
