---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11273"
pai: "11083"
prioridade: media
status: resolvido
data_inicio: 2026-09-02
data_fim: "2026-09-03"
responsavel: Rafael
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Empresa consegue se vincular como participante do próprio departamento

### Descrição

Durante validação foi identificado que o sistema permite que uma empresa (cidadão PJ) vincule **a si própria** como participante de um departamento que ela mesma possui.

---

### Passo a passo para reproduzir

**Dado** que estou editando um cidadão PJ e acesso a configuração de um departamento dele
**Quando** busco por participante pra vincular ao departamento e localizo a própria empresa (a mesma PJ dona do departamento) na lista de opções
**E** seleciono e confirmo a vinculação
**Então** verifico que o sistema permite a vinculação — a própria empresa é aceita como participante do seu próprio departamento

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://11273)

![[11273 - OK.mp4]]

> [!info]- Evidência original da reprodução não trazida pro vault
> Referenciada como `2026-09-02 17-26-11.mkv` na descrição recebida — arquivo não está em `Evidências/`.

---

### Resultado Esperado

A própria empresa responsável pelo departamento **não deve estar disponível para vinculação ao próprio departamento** — deve ficar de fora da lista de participantes selecionáveis daquele departamento.

---

### Critérios de aceite

- [x] A própria PJ dona do departamento não aparece na lista de participantes disponíveis pra vincular ao próprio departamento

---

### Casos de Teste Básicos

#### **CT-B01 Empresa não pode se vincular como participante do próprio departamento**

**Dado** que estou configurando um departamento de uma PJ
**Quando** busco por participante pra vincular
**Então** a própria PJ dona do departamento não aparece na lista de opções

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!success]- Reprovado em 02/09, aprovado no reteste de 03/09
> Corrigido e reteste passou — gravação da execução abaixo.

**Evidências de Testes:**

![[11273 - OK.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083]] — defeito do grupo B (Gerenciamento de participantes); nenhum CT hoje cobria bloqueio de auto-vínculo (CT-012 bloqueia participante de **outra instância**, regra diferente) — gap de cobertura exposto por este defeito.
- Observações:
    - Versão/ambiente exato (qual container `dev-*`) não informado — pendência preencher.
- Histórico:
    - 2026-09-02 - 🐛 Defeito identificado (achado na validação da SGV-11083)
    - 2026-09-03 - ✅ Aprovado em DEV (corrigido, reteste OK) — cadastrado e fechado já resolvido; card fica sem etapa de HML, validação em homologação acontece pela task principal
