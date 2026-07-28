---
tags:
  - bug
  - qa
  - assinatura
task: ""
prioridade: ""
status: aberto
data_inicio: 2026-07-28
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: assinatura
ambiente: HML
---
# Download da versão com assinaturas autenticáveis ignora a configuração de página extra de assinaturas

### Descrição

Ao baixar um documento assinado pela opção **"versão com assinaturas autenticáveis"**, o arquivo vem como se a função de **assinatura em página extra** estivesse **desativada** — ou seja, o download não respeita a configuração ativa no cliente/documento.

As outras opções de download da mesma tela **vêm corretas**, respeitando a página extra: **personalizado** e **compactado**. O problema é específico da versão com assinaturas autenticáveis.

---

### Passo a passo para reproduzir

1. Ter um cliente/documento com a função de **assinatura em página extra ativada**
2. Assinar o documento
3. Baixar o documento pela opção **"versão com assinaturas autenticáveis"**
4. Observar que o arquivo vem **sem a página extra de assinaturas**, como se a função estivesse desativada
5. Para contraste, baixar o mesmo documento pelas opções **personalizado** e **compactado** — ambos vêm corretos, com a página extra

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/)

![[download versao assinaturas autenticaveis ignora pagina extra de assinaturas.mp4]]

---

### Resultado Esperado

**Todas** as opções de download respeitam a configuração de assinatura em página extra — inclusive a versão com assinaturas autenticáveis, que deve sair com a página extra igual ao personalizado e ao compactado.

---

### Critérios de aceite

- [ ] Download da "versão com assinaturas autenticáveis" respeita a configuração de assinatura em página extra
- [ ] Personalizado e compactado seguem corretos (sem regressão)

---

### Casos de Teste Básicos

- **CT-B01 Versão com assinaturas autenticáveis respeita a página extra**
    Dado um documento assinado, com a função de assinatura em página extra ativada
    Quando o usuário baixa pela opção "versão com assinaturas autenticáveis"
    Então o arquivo vem com a página extra de assinaturas

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [x] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[download versao assinaturas autenticaveis ignora pagina extra de assinaturas.mp4]]

- **CT-B02 Personalizado e compactado seguem corretos (sem regressão)**
    Dado o mesmo documento assinado com página extra ativada
    Quando o usuário baixa pelas opções "personalizado" e "compactado"
    Então ambos os arquivos vêm com a página extra de assinaturas

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[download versao assinaturas autenticaveis ignora pagina extra de assinaturas.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- ⚠️ **Card sem SGV ainda**: `task` vazio e arquivo nomeado sem prefixo numérico (é o primeiro card do vault nessa situação — todos os outros têm SGV ou MEL-NNNN). **Renomear pra `<SGV> - Bug ...` e preencher `task` quando o número existir** — pendência na fila.
- **Referência passada pelo Rafael** (28/07): [Árvore de processo (Notion)](https://app.notion.com/p/alfa-group/rvore-de-processo-17b4b88221184bdeac9d503e57b1c10e?source=copy_link#3502aec67d3080a7b864df708cd5c226) — link com âncora de bloco; **não dá pra extrair o SGV da URL**, então não inventei número.
- **Relacionado**: [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]] — mesma área (página extra/separada de assinaturas), problema diferente: lá era desalinhamento do link e QR Code **dentro** da página extra (aprovado em DEV hoje), aqui a página extra **nem é gerada** no download de autenticáveis.
- **Gate de doc** (2026-07-28, fluxo 8): [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] **não cobre as opções de download** (autenticáveis / personalizado / compactado) nem a página extra de assinaturas — esta só aparece listada em "Atualizações posteriores (conteúdo não veio no export)" (*"Atualização Página Extra de Assinaturas — 28/04/2026"*). Sem divergência de regra; **gap de doc**, mesmo candidato de importação levantado na SGV-9405.
- Histórico:
    - 2026-07-28 - 🐛 Bug confirmado em homologação (card criado; aguardando SGV)
