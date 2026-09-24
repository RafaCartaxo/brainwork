---
tags:
  - bug
  - qa
task: "11158"
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
# Prévia de documento não carrega para solicitação de assinatura

### Descrição

Durante validação foi identificado que a prévia do documento não carrega na tela de solicitação de assinatura — o sistema não exibe o preview do arquivo, impedindo conferir o documento antes/durante o fluxo de assinatura. Achado no mesmo ambiente de homologação (nova arquitetura) da [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]].

curl1 — busca as informações do artefato/documento (metadados, URLs do arquivo) pro fluxo de assinatura:

```jsx
curl 'https://dev.sogov.net/api-dev/graphql' \
  -H 'accept: */*' \
  -H 'accept-language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'auth-provider: dbAuth' \
  -H 'authorization: Bearer 15769' \
  -H 'content-type: application/json' \
  -b '_ga=GA1.1.947450628.1787769532; accessType=public-agent; instanceId=1; session_8911=gXWTAftY9W+DONiqFwFNwfQHqFPp3D73pICWKXLHnUbRTs+1HPGAUEPOMfU/xOEhkSPHawnukl7TkfuZyvceQP2nJa3Q01s6yn1uoRtAF7XMB5m+g9lI8JjFSMjEh7iz+IXVY6BYwlx2kNmSYF/O/w==|ny54ZPGtFG4Y1rwsCwWc4Q==; _ga_FEH338067G=GS2.1.s1787916452$o11$g1$t1787927320$j23$l0$h0' \
  -H 'origin: https://dev.sogov.net' \
  -H 'priority: u=1, i' \
  -H 'referer: https://dev.sogov.net/cliente/1/documento/MTD1REGG3R4TGN7Q4C' \
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36' \
  -H 'x-renderer: /cliente/1/documento/MTD1REGG3R4TGN7Q4C' \
  -H 'x-tenant: 1' \
  --data-raw $'{"operationName":"findInformationsByArtifacts","variables":{"artifacts":[{"location":"DOCUMENT","documentId":770941,"count":1,"signers":[{"signer":{"type":"public_agent","id":15769,"mainSectorId":15,"name":"Ursula Lidia Cartaxo Borges","profilePicture":null,"publicAgentId":5308,"userId":15769},"type":"SOGOV","organizationalComponentId":15,"role":"","authenticateType":"DEFAULT","location":["DOCUMENT"],"isIssuer":false}]}],"eventId":null},"query":"query findInformationsByArtifacts($artifacts: [CustomLocationInput!]!, $eventId: Int) {\\n  findInformationsByArtifacts(artifacts: $artifacts, eventId: $eventId) {\\n    document {\\n      id\\n      signedDocumentUrl\\n      originalDocumentUrl\\n      module {\\n        module {\\n          name\\n          __typename\\n        }\\n        __typename\\n      }\\n      mattersServices {\\n        name\\n        __typename\\n      }\\n      documentCode\\n      __typename\\n    }\\n    attachment {\\n      id\\n      name\\n      url\\n      contentType\\n      signedDocumentUrl\\n      revisedDocumentUrl\\n      printUrl\\n      dispatch {\\n        id\\n        number\\n        __typename\\n      }\\n      __typename\\n    }\\n    dispatch {\\n      id\\n      number\\n      signedDispatchUrl\\n      originalDispatchUrl\\n      __typename\\n    }\\n    signatureLocations {\\n      id\\n      x\\n      y\\n      page\\n      status\\n      signature {\\n        organizationalComponentId\\n        __typename\\n      }\\n      __typename\\n    }\\n    signatures {\\n      id\\n      __typename\\n    }\\n    signaturesToPosition {\\n      id\\n      isIssuer\\n      location\\n      organizationalComponentId\\n      role\\n      type\\n      position {\\n        xCm\\n        x\\n        yCm\\n        y\\n        page\\n        relativePage\\n        __typename\\n      }\\n      signer {\\n        iamSigner\\n        id\\n        mainSectorId\\n        name\\n        profilePicture\\n        type\\n        userId\\n        sectorInitials\\n        publicAgentId\\n        role\\n        __typename\\n      }\\n      __typename\\n    }\\n    count\\n    __typename\\n  }\\n}"}'
```

curl2 — busca direta do PDF no S3 (a URL retornada pela query acima), que é onde a prévia efetivamente falha em carregar:

```jsx
curl 'https://sogov-dev-app.s3.us-east-2.amazonaws.com/dev/instances/1/documents/f2fd17da-e2a7-4601-965c-f4db91decc97/f2fd17da-e2a7-4601-965c-f4db91decc97.pdf' \
  -H 'Accept: */*' \
  -H 'Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7' \
  -H 'Connection: keep-alive' \
  -H 'Origin: https://dev.sogov.net' \
  -H 'Referer: https://dev.sogov.net/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36' \
  -H 'sec-ch-ua: "Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Linux"'
```

---

### Passo a passo para reproduzir

Dado que eu tenho um documento pronto pra solicitação de assinatura
Quando eu abro a tela de solicitação de assinatura
Então verifico que a prévia do documento não carrega

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11158)

![[11158 - documento não carrega para realizar assinatura.mp4]]
*Reprodução (28/08).*

![[11158 - OK.mp4]]
*Aprovado em homologação (01/09).*

---

### Resultado Esperado

- Prévia do documento carrega normalmente na tela de solicitação de assinatura

---

### Critérios de aceite

- [x] A prévia do documento é exibida corretamente na tela de solicitação de assinatura

---

### Casos de Teste Básicos

#### **CT-B01 Prévia de documento carrega na solicitação de assinatura**

**Dado** que eu tenho um documento pronto pra solicitação de assinatura
**Quando** eu abro a tela de solicitação de assinatura
**Então** a prévia do documento carrega normalmente

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[11158 - OK.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]]
- Observações: Achado na mesma revalidação da nova arquitetura. Não encontrei CT nem item da tabela de Regressão que bata exatamente — o mais próximo é a SGV-8661 ("Documentos e despachos não carregam ao baixar documento personalizado", CT-029/CT-030), mas aquele é sobre download de documento personalizado, não prévia no fluxo de assinatura — temas parecidos, não a mesma coisa, então não linkei os dois. curl2 (fetch direto do PDF no S3) era onde a falha aparecia na prática. **Gate de doc** ([[Sistema/Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]): confirmação de paridade pós-migração de arquitetura, não regra de negócio nova — resultado esperado é reproduzir o comportamento pré-migração, já confirmado na aprovação.
- Histórico:
    - 2026-08-28 - 🐛 Bug cadastrado
    - 2026-09-01 - ✅ Aprovada em homologação
