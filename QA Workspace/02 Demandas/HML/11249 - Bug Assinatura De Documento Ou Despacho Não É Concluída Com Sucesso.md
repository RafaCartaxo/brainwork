---
tags:
  - bug
  - qa
task: "11249"
pai: ""
prioridade: media
status: resolvido
data_inicio: 2026-09-02
data_fim: "2026-09-04"
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Assinatura de documento ou despacho não é concluída com sucesso

### Descrição

Durante validação foi identificado que, ao criar um documento/despacho — com ou sem anexo — e solicitar a assinatura de um servidor, ao tentar assinar a assinatura não é concluída com sucesso. Achado no mesmo ambiente de homologação (nova arquitetura) da [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]].

**Vizinho da [[QA Workspace/02 Demandas/Concluídas/11215 - Bug Documento Não Carrega Para Realizar Assinatura|SGV-11215]], mas ponto de falha diferente**: na 11215 o documento não chega a carregar ao clicar pra assinar — a tentativa nem começa. Aqui o documento carrega e o fluxo de assinatura é iniciado, mas a assinatura em si não é concluída com sucesso.

```jsx
curl 'https://dev.sogov.net/api-dev/graphql' \ -H 'accept: */*' \ -H 'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \ -H 'auth-provider: dbAuth' \ -H 'authorization: Bearer 15769' \ -H 'content-type: application/json' \ -b '_ga=GA1.1.947450628.1787769532; accessType=public-agent; instanceId=1; session_8911=mNryd76d1dMqlR/XKgVDMIWErHIjaUYugS7zhRLKnX0C3RRy/RolcLgPmKEmPb1M5xmWxeriYu0LIovge5P1ertnohczHjOJv0/jvIVRXRHdz0uMlsUWX5DlRzNmQ2WVEkt0PZeVuWYmlWVzNZEv/g==|Vun78EWuK8P1QI0GGNtOgQ==; _ga_FEH338067G=GS2.1.s1788348492$o21$g1$t1788350241$j25$l0$h0' \ -H 'origin: https://dev.sogov.net' \ -H 'priority: u=1, i' \ -H 'referer: https://dev.sogov.net/cliente/1/documento/MTK0TXRN6L29FH1NRP?scrollTo=3800218' \ -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \ -H 'sec-ch-ua-mobile: ?0' \ -H 'sec-ch-ua-platform: "Linux"' \ -H 'sec-fetch-dest: empty' \ -H 'sec-fetch-mode: cors' \ -H 'sec-fetch-site: same-origin' \ -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36' \ -H 'x-renderer: /cliente/1/documento/MTK0TXRN6L29FH1NRP' \ -H 'x-tenant: 1' \ --data-raw $'{"operationName":"signatureLocations","variables":{"locationsId":[425683,425684]},"query":"query signatureLocations($locationsId: [Int\u0021]\u0021) {\\n signatureLocations(locationsId: $locationsId) {\\n signatureLocations {\\n id\\n status\\n documentObject {\\n id\\n __typename\\n }\\n attachment {\\n id\\n __typename\\n }\\n dispatch {\\n id\\n __typename\\n }\\n __typename\\n }\\n createEvent\\n __typename\\n }\\n}"}'
```
---

### Passo a passo para reproduzir

Dado que crio um documento/despacho, com ou sem anexo
E solicito a assinatura de um servidor
Quando tento assinar
Então verifico que a assinatura não é concluída com sucesso

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11249)

![[11249 - Erro ao assinar documento.mp4]]

> [!success]- Reteste em 04/09/2026 — aprovado
> ![[11249 - OK.mp4]]

---

### Resultado Esperado

- Assinatura é concluída com sucesso ao assinar o documento/despacho, com ou sem anexo

---

### Critérios de aceite

- [ ] Documento/despacho **sem anexo**: assinatura é concluída com sucesso
- [ ] Documento/despacho **com anexo**: assinatura é concluída com sucesso

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura é concluída sem anexo**

**Dado** que crio um documento/despacho sem anexo
**E** solicito a assinatura de um servidor
**Quando** tento assinar
**Então** a assinatura é concluída com sucesso

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B02 Assinatura é concluída com anexo**

**Dado** que crio um documento/despacho com anexo
**E** solicito a assinatura de um servidor
**Quando** tento assinar
**Então** a assinatura é concluída com sucesso

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
- Observações: Bate com o **CT-002** ("Assinar um documento continua funcionando") da SGV-8321 — já reprovado por [[QA Workspace/02 Demandas/Concluídas/11215 - Bug Documento Não Carrega Para Realizar Assinatura|SGV-11215]]. Este card documenta outra manifestação do mesmo fluxo quebrado: mesmo quando o documento carrega, a assinatura não conclui.
- Histórico:
    - 2026-09-02 - 🐛 Bug cadastrado
