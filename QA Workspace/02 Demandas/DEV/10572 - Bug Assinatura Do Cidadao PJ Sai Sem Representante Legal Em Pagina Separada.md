---
tags:
  - bug
  - qa
  - assinatura
  - usuario-cidadao
task: "10572"
prioridade: media
status: aberto
data_inicio: 2026-08-03
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: DEV
---
# Assinatura do cidadão PJ sai sem o representante legal em documento com página de assinaturas separada

### Descrição

Durante validação foi identificado que, em documento cujo assunto/serviço está configurado com **página de assinaturas separada**, a assinatura realizada pelo **cidadão PJ** sai impressa **sem os dados do representante legal** — apenas com os dados da empresa. O responsável legal **estava preenchido no cadastro** do cidadão, ou seja, o dado existia e não foi levado para a página de assinaturas.

---

### Passo a passo para reproduzir

Dado que o assunto/serviço esteja configurado com "Documentos possuem página de assinaturas separada"
E exista um cidadão PJ com **nome e CPF do responsável legal preenchidos** no cadastro
E esse cidadão PJ tenha uma solicitação de assinatura em um documento desse assunto/serviço
Quando o cidadão PJ realizar a assinatura
E o documento for impresso ou baixado
Então verifico que a página de assinaturas traz apenas os dados da empresa, **sem o representante legal**

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10572)

![[10572 - assinatura da pj sai sem o representante legal.mp4]]


---

### Resultado Esperado

A página de assinaturas separada traz, na assinatura do cidadão PJ, **os dados da empresa e os do responsável legal**.

Isso está **respaldado por regra escrita** na doc de [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão#Regras gerais de e-mail e assinatura (PJ)|Usuário Cidadão § Regras gerais de e-mail e assinatura (PJ)]], que define para os dois tipos de assinatura:

> "**Assinatura SoGov**: fluxo padrão de senha de conta para autenticação; no documento, entram os dados da empresa **e** do responsável legal;
> **Assinatura ICP**: valida o token da PJ solicitante (autenticidade); no documento, entram os dados da empresa **e** do responsável legal."

E a página separada não é detalhe de exibição: pela doc de [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas § Página extra de assinaturas]], ela **"torna-se parte integrante do arquivo PDF"** e é o **fechamento oficial** do documento — então o dado ausente viaja no arquivo baixado e impresso.

---

### Critérios de aceite

- [ ] Com a **página de assinaturas separada ativada**, a assinatura do cidadão PJ sai com os dados da empresa **e** do responsável legal
- [ ] Com a página de assinaturas separada **desativada**, o comportamento é o mesmo — o responsável legal não depende dessa configuração
- [ ] Vale para **Assinatura SoGov** e **Assinatura ICP**, que a doc define com a mesma regra
- [ ] **Sem regressão**: assinatura de cidadão **PF** e de **servidor** seguem saindo como hoje

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura da PJ traz o representante legal na página separada**

**Dado** que o assunto/serviço esteja com a página de assinaturas separada ativada
**E** o cidadão PJ tenha o responsável legal preenchido no cadastro
**Quando** o cidadão PJ assinar o documento e o arquivo for baixado
**Então** a página de assinaturas exibe os dados da empresa e do responsável legal

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Mesmo comportamento com a página separada desativada**

**Dado** que o assunto/serviço esteja com a página de assinaturas separada **desativada**
**E** o cidadão PJ tenha o responsável legal preenchido no cadastro
**Quando** o cidadão PJ assinar o documento e o arquivo for baixado
**Então** a assinatura exibe os dados da empresa e do responsável legal

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Assinatura de cidadão PF e de servidor seguem normais (regressão)**

**Dado** que o assunto/serviço esteja com a página de assinaturas separada ativada
**Quando** um cidadão **PF** e um **servidor** assinarem o documento
**Então** as assinaturas saem completas, como já ocorria antes da correção

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento (posição na esteira de correção)

> [!info]- Origem: validado em todos os ambientes, considerar homologação
> Observado durante a execução dos CTs da melhoria de CNPJ ([[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]]) — é a **evidência 3** daquela bateria. O Rafael validou em todos os ambientes e definiu **homologação** como referência (03/08/2026).
>
> O card mora em `DEV/` com `ambiente: DEV` porque o campo reflete a **posição na esteira de correção**, não o último ambiente testado ([[Sistema/Contexto/PADROES_QA|PADROES_QA]] → Organização de Bugs).

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — encontrado **durante** a validação dela, mas **não é regressão** e **não é CT dela**: o Rafael confirmou que já existia **antes da implementação** do CNPJ alfanumérico. Nenhum critério da 9493 é afetado. Mesmo tratamento dado à [[QA Workspace/02 Demandas/DEV/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]], à [[QA Workspace/02 Demandas/DEV/10517 - Bug Busca Do Campo De Solicitante Nao Retorna Resultado Com Mascara|SGV-10517]] e à [[QA Workspace/02 Demandas/DEV/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]], todas achadas na mesma frente.

- **Relacionado**: [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]] e [[QA Workspace/02 Demandas/HML/10457 - Bug Espacamento Do Link Inferior E Paginacao Sobreposta Em Documento Assinado|SGV-10457]] — mesma superfície (a página de assinaturas separada), problemas diferentes: lá é posicionamento do link e do QR Code, aqui é **dado ausente** no bloco da assinatura.

- Observações:
    - **Gate de doc — DIVERGÊNCIA CONFIRMADA, não lacuna.** A regra citada no Resultado Esperado é explícita e vale para os **dois** tipos de assinatura. O comportamento observado contraria doc escrita, então o esperado não é interpretação da QA e o dev não tem como alegar que a regra não existe.
    - ✅ **O pré-requisito que separa bug de "não é bug" está confirmado**: o responsável legal **estava preenchido** no cadastro do cidadão PJ testado. Isso importa porque, no **cadastro interno feito por servidor**, o CPF do responsável legal é **opcional** ([[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão#1. Cadastro interno da pessoa jurídica (feito por um servidor)|doc do módulo]]) — sem ele não haveria o que imprimir, e o dev devolveria a task. Confirmado pelo Rafael em 03/08/2026; **manter esse dado preenchido ao revalidar**.
    - ⚠️ **Não confundir com a melhoria planejada** "*Permitir cadastro de cidadão Pessoa Jurídica sem vincular dados do responsável legal*", que está no backlog do módulo. São coisas distintas: a melhoria trata de PJ **sem** responsável legal; este bug é PJ **com** responsável legal cujo dado não é impresso.
    - **Cobertura de CT enxuta**: 3 CT-B para 4 critérios. O 3º critério (SoGov **e** ICP) não tem CT próprio — é uma dimensão a percorrer **dentro** do CT-B01 e do CT-B02, executando cada um com os dois tipos de assinatura. Não é lacuna esquecida.

- Histórico:
    - 2026-08-03 - 🐛 Bug confirmado (card criado)
    - 2026-08-03 - 🐛 Cadastrado no Notion como SGV-10572
