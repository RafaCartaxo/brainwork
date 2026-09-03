---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11319"
pai: "11184"
prioridade: alta
status: aberto
data_inicio: 2026-09-03
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Departamento não é persistido ao retificar despacho (tela mostra o cidadão PJ/empresa)

### Descrição

Durante validação foi identificado que, ao emitir um despacho com um **departamento** como destinatário e em seguida retificar esse despacho, a tela de retificação mostra selecionado o **cidadão PJ/empresa**, e não o departamento efetivamente solicitado.

---

### Passo a passo para reproduzir

**Dado** que um despacho foi emitido com um departamento como destinatário
**Quando** o despacho é retificado
**Então** verifico que a tela de retificação mostra o cidadão PJ/empresa selecionado no campo de destinatário, em vez do departamento que foi de fato solicitado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://11319)

![[11319 - Departamento não é persistido ao retificar despacho.mp4]]

---

### Resultado Esperado

[[QA Workspace/04 Conhecimento/Módulos/Despachos#Retificar despacho|Despachos.md]] documenta que a tela de retificação tem **"Campos editáveis: destinatários..."** — o fluxo existe pra corrigir erros de preenchimento, o que exige que o campo mostre o valor **atual real** antes de qualquer edição. Departamento é um destinatário válido desde a [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]]:

- A tela de retificação deve mostrar **o departamento** selecionado no campo de destinatário, exatamente como foi solicitado no despacho original.
- Não deve reverter/substituir pelo cidadão PJ/empresa ao qual o departamento pertence.

---

### Critérios de aceite

- [ ] Despacho emitido com departamento como destinatário mantém o departamento selecionado ao abrir a tela de retificação
- [ ] O cidadão PJ/empresa não aparece como selecionado no lugar do departamento

---

### Casos de Teste Básicos

#### **CT-B01 Retificação preserva o departamento selecionado como destinatário**

**Dado** que um despacho foi emitido com um departamento como destinatário
**Quando** o servidor abre a tela de retificação desse despacho
**Então** o departamento aparece selecionado no campo de destinatário, sem ser substituído pelo cidadão PJ/empresa

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11319 - Departamento não é persistido ao retificar despacho.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]] — defeito achado em teste exploratório, não em CT formal (a 11184 ainda não tem grupo de CT pra retificação de despacho, ver nota em Pontos de atenção do card).
- Observações:
    - Risco funcional além do visual: se o servidor não perceber a troca e salvar a retificação assim, o destinatário real do despacho pode mudar de departamento pra PJ/empresa sem intenção — daí a prioridade alta.
    - Versão/ambiente exato (qual container `dev-*`) não informado — pendência preencher.
- Histórico:
    - 2026-09-03 - 🐛 Defeito cadastrado (achado na validação da SGV-11184, evidência já no vault)
