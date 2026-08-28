---
tags:
  - bug
  - qa
task: "11151"
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
# Documento não é criado com anexo no módulo e no assunto e serviço

### Descrição

Durante validação foi identificado que a criação de documento falha quando há arquivo anexado no campo de anexo do módulo e no campo de anexo do assunto e serviço — o sistema retorna erro em vez de criar o documento.

```jsx
curl '<https://dev.sogov.net/api-dev/graphql>' \
  -H 'accept: */*' \
  -H 'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'auth-provider: dbAuth' \
  -H 'authorization: Bearer 15769' \
  -H 'content-type: application/json' \
  -b '_ga=GA1.1.947450628.1787769532; accessType=public-agent; instanceId=1; session_8911=gXWTAftY9W+DONiqFwFNwfQHqFPp3D73pICWKXLHnUbRTs+1HPGAUEPOMfU/xOEhkSPHawnukl7TkfuZyvceQP2nJa3Q01s6yn1uoRtAF7XMB5m+g9lI8JjFSMjEh7iz+IXVY6BYwlx2kNmSYF/O/w==|ny54ZPGtFG4Y1rwsCwWc4Q==; _ga_FEH338067G=GS2.1.s1787916452$o11$g1$t1787925188$j47$l0$h0' \
  -H 'origin: <https://dev.sogov.net>' \
  -H 'priority: u=1, i' \
  -H 'referer: <https://dev.sogov.net/cliente/1/abrir-documento/373?matterServiceId=3939>' \
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36' \
  -H 'x-renderer: /cliente/1/abrir-documento/373' \
  -H 'x-tenant: 1' \
  --data-raw $'{"operationName":"documentProcess","variables":{"id":223057},"query":"query documentProcess($id: Int\u0021) {\\n  documentProcess(id: $id) {\\n    id\\n    status\\n    errorMessage\\n    trackerCode\\n    documentId\\n    attachments {\\n      id\\n      name\\n      __typename\\n    }\\n    __typename\\n  }\\n}"}'
```
---

### Passo a passo para reproduzir

Dado que eu tento criar um documento
E preencho o campo de anexo do módulo com um arquivo
E preencho o campo de anexo do assunto e serviço com um arquivo
Quando eu confirmo a criação
Então verifico que o documento não é criado com sucesso e o sistema retorna erro

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11151)

![[11151 - erro ao criar documento com anexo no modulo e assunto.mp4]]

---

### Resultado Esperado

- Documento é criado com sucesso mesmo com arquivo anexado no campo de anexo do módulo e no campo de anexo do assunto e serviço

---

### Critérios de aceite

- [ ] Documento é criado com sucesso com anexo no campo do módulo
- [ ] Documento é criado com sucesso com anexo no campo de assunto e serviço
- [ ] Documento é criado com sucesso com os dois campos de anexo preenchidos ao mesmo tempo

---

### Casos de Teste Básicos

#### **CT-B01 Criar documento com anexo no módulo e no assunto e serviço**

**Dado** que eu tento criar um documento
**E** preencho o campo de anexo do módulo com um arquivo
**E** preencho o campo de anexo do assunto e serviço com um arquivo
**Quando** eu confirmo a criação
**Então** o documento é criado com sucesso, sem erro

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
- Observações: Achado testando criação/anexo de documento no novo ambiente de homologação (nova arquitetura). Não bate exatamente com nenhum CT já listado na SGV-8321 — CT-005 é "criar documento" sem anexo, CT-023 é "anexar arquivo em campo de texto longo" (contexto diferente dos campos de anexo do módulo/assunto e serviço). Não marquei nenhum CT da 8321 como reprovado por isso — avaliar se vale um CT novo lá.
- Histórico:
    - 2026-08-28 - 🐛 Bug cadastrado
