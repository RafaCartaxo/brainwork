---
tags:
  - bug
  - qa
task: ""
pai: ""
prioridade: alta
status: aberto
data_inicio: 2026-08-26
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: email
ambiente: HML
---
# E-mail de confirmação de cadastro não chega no novo ambiente de homologação

### Descrição

Durante a rodada de revalidação da [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]] (novo ambiente de homologação `dev.sogov.net`, nova arquitetura), a automação (`sogov-automation-test`) travou no setup inicial: a etapa de pré-cadastro de agente/servidor dispara um e-mail de confirmação de cadastro, mas ele nunca chegou na caixa de teste. A automação esperou 15 minutos (`cy.task('waitForGmailMessage')`, timeout de 900000ms) e desistiu.

Verificado manualmente por mim (Rafael) checando a caixa Gmail diretamente: **o e-mail realmente não chegou** — não é falha de busca/critério da automação, é ausência de entrega mesmo.

---

### Passo a passo para reproduzir

Dado que estou no novo ambiente de homologação (`dev.sogov.net`)
E inicio o pré-cadastro de um novo servidor/agente (fluxo que dispara e-mail de confirmação com link/token pra finalizar o cadastro)
Quando aguardo a chegada do e-mail de confirmação na caixa de entrada
Então verifico que o e-mail nunca chega

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://sem-numero)

Sem vídeo/print anexado ainda — confirmação foi feita checando a caixa Gmail diretamente durante a sessão. Log da automação com o timeout: run de 2026-08-26, specs `create.document.api.cy.js` e `sector.e2e.cy.js`, ambas falharam no `before all` hook no mesmo ponto.

---

### Resultado Esperado

O e-mail de confirmação de cadastro deve chegar na caixa de entrada em poucos minutos, permitindo concluir o fluxo de pré-cadastro normalmente — igual acontece hoje no ambiente de homologação antigo (`homolog.sogov.com.br`).

---

### Critérios de aceite

- [ ] E-mail de confirmação de cadastro de servidor/agente chega na caixa de entrada em tempo razoável (poucos minutos) no ambiente `dev.sogov.net`
- [ ] Conteúdo do e-mail (link/token de confirmação) funciona normalmente pra concluir o cadastro

---

### Casos de Teste Básicos

#### **CT-B01 E-mail de confirmação de cadastro é entregue**

**Dado** que eu inicio o pré-cadastro de um novo servidor/agente no ambiente `dev.sogov.net`
**Quando** eu aguardo a chegada do e-mail de confirmação
**Então** verifico que ele chega na caixa de entrada em poucos minutos, com link/token válido

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

---

### Ambiente

- Versão: nova arquitetura (migração Lambda → EKS)
- Ambiente: Homologação (`dev.sogov.net`, novo ambiente disponibilizado em 2026-08-26)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]] (CT-025 "E-mails do sistema chegam corretamente") — falha aqui bloqueia CT-025 e, por consequência, boa parte da automação (qualquer fluxo que precise de um agente/servidor novo passa por confirmação de e-mail no setup)
- Correlação com bugs da rodada anterior: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura#Regressão — bugs da rodada anterior|SGV-8446]] (erro ao enviar e-mail ao cadastrar) e SGV-8602 (logo não exibida no e-mail de finalização de cadastro) — os três apontam pro mesmo ponto de risco: pipeline de e-mail (migração SES v2→v3 + nodemailer) pode não estar funcional/configurado neste ambiente ainda
- Observações: causa raiz não investigada ainda — duas hipóteses em aberto, a confirmar com Dev/Infra: (1) SES do `dev.sogov.net` não está enviando e-mail de verdade (ex.: sandbox/allowlist de destinatário), ou (2) está enviando mas pra endereço/critério diferente do esperado. Sem acesso a logs de backend não dá pra distinguir as duas só pela QA.
- Histórico:
    - 2026-08-26 - 🐛 Bug confirmado (card criado) — verificado manualmente que o e-mail não chega, sem SGV ainda
