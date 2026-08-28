---
tags:
  - bug
  - qa
task: "11159"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-28
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Campo de mapa não carrega para seleção de localização

### Descrição

Durante validação foi identificado que, ao acessar um documento com campo de mapa configurado, o campo não carrega para seleção de localização. Já era um bug conhecido da rodada anterior de validação da nova arquitetura ([[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]] → tabela de Regressão, SGV-9074) e reapareceu nesta revalidação em homologação.

---

### Passo a passo para reproduzir

Dado que eu acesso um documento com campo de mapa configurado
Quando eu tento selecionar a localização nesse campo
Então verifico que o campo de mapa não é carregado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11159)

![[11159 - campo mapa nok.mp4]]

---

### Resultado Esperado

- Campo de mapa carrega normalmente e permite seleção de localização

---

### Critérios de aceite

- [ ] O campo de mapa carrega ao acessar um documento com esse campo configurado
- [ ] É possível selecionar a localização no campo de mapa

---

### Casos de Teste Básicos

#### **CT-B01 Campo de mapa carrega e permite seleção de localização**

**Dado** que eu acesso um documento com campo de mapa configurado
**Quando** eu tento selecionar a localização nesse campo
**Então** o campo de mapa carrega normalmente, sem erro

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]]
- Observações: Corresponde à SGV-9074 da rodada anterior (tabela de Regressão da SGV-8321, "Erro ao selecionar localização em campo do tipo mapa (POC1)") — revalidação nesta rodada reproduziu o mesmo erro. A rodada anterior marcava esse item como tag POC/ambiente "POC1", com nota pra confirmar se esse ambiente ainda existia no novo ambiente de homologação — esse achado confirma que o problema reproduz também fora do POC1, no ambiente atual.
- Histórico:
    - 2026-08-28 - 🐛 Bug cadastrado
