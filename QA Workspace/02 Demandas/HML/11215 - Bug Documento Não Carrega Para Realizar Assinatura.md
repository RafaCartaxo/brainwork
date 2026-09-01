---
tags:
  - bug
  - qa
task: "11215"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-01
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Documento não carrega para realizar assinatura

### Descrição

Durante validação foi identificado que, ao solicitar a assinatura de um servidor num documento/despacho/anexo e clicar pra assinar, o documento não é carregado com sucesso — a assinatura não pode ser concluída. Achado no mesmo ambiente de homologação (nova arquitetura) da [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]].

**Vizinho da [[QA Workspace/02 Demandas/HML/11158 - Bug Prévia De Documento Não Carrega Para Solicitação De Assinatura|SGV-11158]], mas ponto de falha diferente**: na 11158 a tela de **solicitar** assinatura é que não carregava a prévia. Aqui a tela de solicitar funcionou normal — é o documento não carregando na hora de **assinar em si**, depois que a solicitação já foi feita.

---

### Passo a passo para reproduzir

Dado que solicito a assinatura de um servidor em um documento/despacho/anexo
Quando clico para assinar
Então verifico que o documento não é carregado com sucesso

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11215)

![[11215 - Erro ao carregar documento para realizar assinatura.mp4]]

---

### Resultado Esperado

- Documento carrega normalmente na hora de assinar, permitindo concluir a assinatura

---

### Critérios de aceite

- [ ] Ao clicar para assinar, o documento/despacho/anexo carrega com sucesso
- [ ] A assinatura pode ser concluída normalmente após o documento carregar

---

### Casos de Teste Básicos

#### **CT-B01 Documento carrega ao assinar**

**Dado** que solicito a assinatura de um servidor em um documento/despacho/anexo
**Quando** clico para assinar
**Então** o documento carrega com sucesso e a assinatura pode ser concluída

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
- Observações: Bate direto com o **CT-002** ("Assinar um documento continua funcionando") da SGV-8321 — o cenário do CT é exatamente ter um documento pronto pra assinatura → assinar → confirmar que fica assinado, e é isso que está falhando (documento nem carrega). Marcado como reprovado lá.
- Histórico:
    - 2026-09-01 - 🐛 Bug cadastrado
