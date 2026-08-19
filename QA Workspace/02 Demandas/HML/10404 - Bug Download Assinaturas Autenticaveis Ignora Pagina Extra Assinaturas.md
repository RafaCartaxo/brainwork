---
tags:
  - bug
  - qa
  - assinatura
task: "10404"
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

Dado que eu tenho um cliente com documento com a função de assinatura em página extra ativada
E Assino o documento
Quando baixo o documento pela opção "versão com assinaturas autenticáveis"
Então verifico que o arquivo vem sem a página extra de assinaturas, como se a função estivesse desativada

Para contraste, baixando o mesmo documento pelas opções **personalizado** e **compactado**, ambos vêm corretos, com a página extra.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10404)

![[10404 - download versao assinaturas autenticaveis ignora pagina extra de assinaturas.mp4]]

![[10404 - pagina assinaturas separadas - impedido - não assina no ambiente.mp4]]

---

### Resultado Esperado

**Todas** as opções de download respeitam a configuração de assinatura em página extra — inclusive a versão com assinaturas autenticáveis, que deve sair com a página extra igual ao personalizado e ao compactado.

---

### Critérios de aceite

- [ ] Download da "versão com assinaturas autenticáveis" respeita a configuração de assinatura em página extra
- [ ] Personalizado e compactado seguem corretos (sem regressão)

---

### Casos de Teste Básicos

#### **CT-B01 Versão com assinaturas autenticáveis respeita a página extra**

**Dado** que eu tenho um cliente com documento com a função de assinatura em página extra ativada
**E** Assino o documento
**Quando** baixo o documento pela opção "versão com assinaturas autenticáveis"
**Então** verifico que o arquivo vem com a página extra de assinaturas

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10404 - download versao assinaturas autenticaveis ignora pagina extra de assinaturas.mp4]]

---

#### **CT-B02 Personalizado e compactado seguem corretos (sem regressão)**

**Dado** que eu tenho um cliente com documento com a função de assinatura em página extra ativada
**E** Assino o documento
**Quando** baixo o documento pelas opções "personalizado" e "compactado"
**Então** verifico que ambos os arquivos vêm com a página extra de assinaturas

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10404 - download versao assinaturas autenticaveis ignora pagina extra de assinaturas.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-10404** (Rafael, 28/07). Referência no Notion: [Árvore de processo](https://app.notion.com/p/alfa-group/rvore-de-processo-17b4b88221184bdeac9d503e57b1c10e?source=copy_link#3502aec67d3080a7b864df708cd5c226).
- **Relacionado**: [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]] — mesma área (página extra/separada de assinaturas), problema diferente: lá era desalinhamento do link e QR Code **dentro** da página extra (aprovado em DEV hoje), aqui a página extra **nem é gerada** no download de autenticáveis.
- **Gate de doc — reclassificado em 2026-07-29: de "gap" para DIVERGÊNCIA CONFIRMADA.** Com a importação da doc, [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas § Página extra de assinaturas]] define explicitamente, nas Regras de download e impressão:

    > "A página extra **não é apenas visual; ela se torna parte integrante do arquivo PDF**."

    E complementa que a paginação inclui as páginas de assinatura, e que mesmo com comentários no despacho "a página de assinaturas [continua] como o **fechamento oficial**".

    Ou seja: o comportamento observado (download de "versão com assinaturas autenticáveis" trazendo o PDF **sem** a página extra) **contraria regra documentada** — não é lacuna de especificação. Isso fortalece o card: há regra escrita pra apontar, e o esperado não é interpretação da QA.
- ⚠️ **Ponto pra confirmar com o dev**: a doc diz que, com o parâmetro ativo, a página extra é parte do PDF **em todos os modelos de assinatura** (direta, sequencial, solicitada) e que o editor de posicionamento manual nem aparece. Vale checar se o gerador da versão "autenticáveis" usa um caminho de renderização próprio que não passa pela regra da página extra — seria a explicação técnica de personalizado/compactado saírem certos e só esse não.
- Histórico:
    - 2026-07-28 - 🐛 SGV-10404 - Bug cadastrado (confirmado em homologação; card criado)
    - 2026-08-19 - ⏳ Impedida (tentativa de acompanhamento em homologação — ambiente não permite assinar o documento, precondição do CT-B01 inalcançável; ver evidência)
