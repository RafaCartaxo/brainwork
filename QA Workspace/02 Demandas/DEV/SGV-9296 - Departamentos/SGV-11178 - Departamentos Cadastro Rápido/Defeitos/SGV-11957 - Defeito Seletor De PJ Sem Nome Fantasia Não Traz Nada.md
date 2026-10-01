---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11957"
pai: "SGV-11178"
prioridade: media
status: descartado
data_inicio: 2026-10-01
data_fim: 2026-10-01
responsavel:
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Seletor de PJ sem Nome fantasia não traz nada

### Descrição

Durante a validação real da SGV-11178 (Parte 5 da epic [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]]), em 30/09/2026, foi identificado que, quando uma pessoa jurídica não possui Nome fantasia cadastrado, o seletor não traz nenhuma opção pra ela — em vez de cair no fallback esperado (Razão Social + CNPJ, conforme [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda#^c29|C29]]), a PJ simplesmente não aparece no resultado.

---

### Passo a passo para reproduzir

**Dado** que uma pessoa jurídica sem Nome fantasia cadastrado esteja disponível no seletor
**Quando** ela for buscada/exibida no seletor
**Então** nenhuma opção aparece pra essa PJ (esperado: aparecer como "Razão Social — CNPJ")

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11957)

**Reprodução (30/09/2026):** Verificar a partir do minuto 6.
![[11957 - Seletor sem Nome fantasia não traz nada, incorreto.mp4]]

---

### Resultado Esperado

Pessoa jurídica sem Nome fantasia aparece no seletor como "Razão Social — CNPJ", igual ao padrão de quando tem Nome fantasia (só troca o rótulo).

---

### Critérios de aceite

- [ ] Pessoa jurídica sem Nome fantasia aparece no seletor, exibida como "Razão Social — CNPJ"

---

### Casos de Teste Básicos

#### **CT-B01 Seletor exibe PJ sem Nome fantasia**

**Dado** que uma pessoa jurídica sem Nome fantasia esteja disponível no seletor
**Quando** ela for buscada/exibida
**Então** a opção deve aparecer como "Razão Social — CNPJ"

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11957 - Seletor sem Nome fantasia não traz nada, incorreto.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda|SGV-11178]]
- Observações: **Descartado em 01/10/2026** — diagnóstico original estava errado. O CT-029 (fallback Razão Social + CNPJ pra PJ sem Nome fantasia) já funcionava corretamente; a PJ da gravação tinha **cadastro incompleto** e foi corretamente ocultada do seletor pelo [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-027|CT-027]] (critério C27). Decisão de produto: formulário de cadastro rápido de PJ passa a coletar e-mail também (ver [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-015|CT-015]]), reduzindo cadastros incompletos.
- Histórico:
    - 2026-10-01 - 🐛 Defeito cadastrado (seletor não traz nenhuma opção quando a PJ não tem Nome fantasia)
    - 2026-10-01 - 🗑️ Descartado — diagnóstico errado, CT-029 já funcionava certo; achado real foi [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-027|CT-027]] (cadastro incompleto). Campo E-mail agora exigido em C15, ver [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/Defeitos/SGV-11958 - Defeito Formulário De Pessoa Jurídica Não Coleta E-mail|SGV-11958]]
