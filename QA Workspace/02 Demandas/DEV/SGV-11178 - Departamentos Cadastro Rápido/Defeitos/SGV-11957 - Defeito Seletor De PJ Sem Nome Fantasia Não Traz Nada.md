---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11957"
pai: "SGV-11178"
prioridade: media
status: aberto
data_inicio: 2026-10-01
data_fim:
responsavel:
aguardando: dev
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Seletor de PJ sem Nome fantasia não traz nada

### Descrição

Durante a validação real da SGV-11178 (Parte 5 da epic [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]]), em 30/09/2026, foi identificado que, quando uma pessoa jurídica não possui Nome fantasia cadastrado, o seletor não traz nenhuma opção pra ela — em vez de cair no fallback esperado (Razão Social + CNPJ, conforme [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda#^c29|C29]]), a PJ simplesmente não aparece no resultado.

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
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11957 - Seletor sem Nome fantasia não traz nada, incorreto.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda|SGV-11178]]
- Observações: achado durante a validação da SGV-11178 — [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-029|CT-029]] (critério C29).
- Histórico:
    - 2026-10-01 - 🐛 Defeito cadastrado (seletor não traz nenhuma opção quando a PJ não tem Nome fantasia)
