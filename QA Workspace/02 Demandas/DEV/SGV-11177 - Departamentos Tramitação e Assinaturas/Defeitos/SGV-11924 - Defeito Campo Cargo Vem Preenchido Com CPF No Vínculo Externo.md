---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11924"
pai: "SGV-11177"
prioridade: media
status: aberto
data_inicio: 2026-09-29
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Campo cargo vem preenchido com CPF no vínculo externo

### Descrição

No fluxo externo de assinatura, quando uma pessoa já cadastrada mas sem vínculo com o departamento precisa informar o cargo pra ser vinculada, o campo cargo vem auto-preenchido com o CPF — impedindo o usuário de informar o cargo real que exerce no departamento.

---

### Passo a passo para reproduzir

**Dado** que o CPF informado pertence a uma pessoa cadastrada mas ainda não vinculada ao departamento destinatário
**Quando** o fluxo pede o cargo pra concluir o vínculo
**Então** verifico que o campo já vem preenchido com o CPF, e não é possível informar o cargo real

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11924)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

### Resultado Esperado

Campo cargo vazio e editável, pra o usuário informar o cargo que exerce no departamento. Ver [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c25|C25]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-025|CT-025]].

---

### Critérios de aceite

- [ ] Campo cargo vem vazio e editável no vínculo externo, sem preenchimento automático com o CPF

---

### Casos de Teste Básicos

#### **CT-B01 Campo cargo editável no vínculo externo**

**Dado** que o CPF informado pertence a uma pessoa cadastrada sem vínculo com o departamento
**Quando** o fluxo pede o cargo
**Então** o campo vem vazio, permitindo informar o cargo real

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

Pendência — nenhuma evidência anexada ainda.

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação da SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-025|CT-025]].
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
