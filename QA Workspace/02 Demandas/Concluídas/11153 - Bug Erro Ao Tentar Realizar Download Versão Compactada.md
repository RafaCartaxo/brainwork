---
tags:
  - bug
  - qa
task: "11153"
pai: ""
prioridade: media
status: resolvido
data_inicio: 2026-08-28
data_fim: 2026-09-01
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
deploy: pendente_release
---
# Erro ao tentar realizar download versão compactada

### Descrição

Durante validação foi identificado que o download da versão compactada do documento retorna erro em vez de concluir. Já era um bug conhecido da rodada anterior de validação da nova arquitetura ([[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]] → tabela de Regressão, SGV-8660) e reapareceu nesta revalidação em homologação.

```jsx
curl 'https://dev.sogov.net/api-dev/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'auth-provider: dbAuth' \
  -H 'authorization: Bearer 15769' \
  -H 'content-type: application/json' \
  -b '_ga=GA1.1.947450628.1787769532; accessType=public-agent; instanceId=1; session_8911=gXWTAftY9W+DONiqFwFNwfQHqFPp3D73pICWKXLHnUbRTs+1HPGAUEPOMfU/xOEhkSPHawnukl7TkfuZyvceQP2nJa3Q01s6yn1uoRtAF7XMB5m+g9lI8JjFSMjEh7iz+IXVY6BYwlx2kNmSYF/O/w==|ny54ZPGtFG4Y1rwsCwWc4Q==; _ga_FEH338067G=GS2.1.s1787916452$o11$g1$t1787926062$j60$l0$h0' \
  -H 'origin: https://dev.sogov.net' \
  -H 'priority: u=1, i' \
  -H 'referer: https://dev.sogov.net/cliente/1/documento/MTD10FANPKYICZ3LNC' \
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36' \
  -H 'x-renderer: /cliente/1/documento/MTD10FANPKYICZ3LNC' \
  -H 'x-tenant: 1' \
  --data-raw $'{"operationName":"GetDownloadStatus","variables":{"hash":"instanceId_1_userId_15769_type_COMPRESSED_VERSION_documentObjectId_770940"},"query":"query GetDownloadStatus($hash: String!) {\\n  data: getDownloadStatus(hash: $hash) {\\n    status\\n    progress\\n    url\\n    fileName\\n    type\\n    subTitle\\n    __typename\\n  }\\n}"}'
```

---

### Passo a passo para reproduzir

Dado que eu tenho um documento
Quando eu solicito o download na versão compactada
Então verifico que o sistema retorna erro em vez de concluir o download

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11153)

![[11153 - erro ao baixar compactado.mp4]]
*Reprodução (28/08).*

![[11153 - OK.mp4]]
*Aprovado em homologação (01/09).*

---

### Resultado Esperado

- Download da versão compactada do documento conclui com sucesso, sem erro

---

### Critérios de aceite

- [x] Download da versão compactada do documento é concluído com sucesso

---

### Casos de Teste Básicos

#### **CT-B01 Baixar documento em versão compactada**

**Dado** que eu tenho um documento
**Quando** eu solicito o download na versão compactada
**Então** o download conclui com sucesso, sem erro

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[11153 - OK.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]]
- Observações: Corresponde à SGV-8660 da rodada anterior (tabela de Regressão da SGV-8321, "Erro ao tentar realizar download Versão compactada") — revalidação nesta rodada reproduziu o mesmo erro. A tabela correlacionava com CT-022, mas CT-022 é sobre expiração de link de download, tema diferente do erro de download em si — não bate exatamente, mesmo caso do que já foi observado na SGV-11151. **Gate de doc** ([[Sistema/Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]): confirmação de paridade pós-migração de arquitetura, não regra de negócio nova — resultado esperado é reproduzir o comportamento pré-migração, já confirmado na aprovação.
- Histórico:
    - 2026-08-28 - 🐛 Bug cadastrado
    - 2026-09-01 - ✅ Aprovada em homologação
