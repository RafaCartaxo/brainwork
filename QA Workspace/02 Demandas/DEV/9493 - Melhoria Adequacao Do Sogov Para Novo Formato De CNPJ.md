---
tags:
  - demanda
  - melhoria
  - qa
  - usuario-cidadao
task: "9493"
status: aberto
prioridade: ""
data_inicio: 2026-07-30
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: usuario-cidadao
ambiente: DEV
---
# Demanda: [Melhoria] Adequação do SOGOV para novo formato de CNPJ

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** DEV (Testando em Dev)
> - **Responsável QA:** Rafael — *campo vazio no Notion, preencher*
> - **Link:** [SGV-9493 no Notion](https://app.notion.com/p/alfa-group/Melhoria-Adequa-o-do-SOGOV-para-novo-formato-de-CNPJ-3832aec67d3080c4b219edf26c15e836) · [Figma — Tramitação/Handoff, página SGV-9493](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8988-5038)
> - **Dev:** Bruno Clementino · **Revisores MR:** Gabriel Desidério, Marcos Vinicius · **Design:** Ivo Costa, Vinícius, Edu
> - **MR:** [!657](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/657) — **aprovado para testes**
> - **Sprint:** SP17 - 2026 Engenharia (Melhorias) · Sprint SGA 24/07–31/07

---

> [!abstract] Resumo

A Receita Federal passou a emitir **CNPJ alfanumérico**: **12 caracteres alfanuméricos + 2 dígitos verificadores numéricos**. Esta entrega adequa o SOGOV para criar, logar, editar e exibir usuários PJ e órgãos com o novo formato, **sem quebrar os CNPJ numéricos já existentes**.

Não é mudança de fluxo — é mudança de **máscara, sanitização e validação** propagada por todo lugar que aceita ou exibe CNPJ. O valor do teste está na **abrangência**: 11 telas declaradas, mais geração de PDF, fluxo de assinatura e construtor de formulários.

---

## Regras de negócio

**Formato** — estrutura visual **inalterada**: `XX.XXX.XXX/XXXX-XX`, **14 caracteres úteis** e **18 com a formatação**, mesma pontuação. Letras de A a Z e números de 0 a 9, normalizadas para **maiúsculas**.

**Onde o alfanumérico vale e onde não** — as **12 primeiras** posições aceitam letra **e** número; os **2 últimos** são os **dígitos verificadores** e aceitam **somente número**. Máscara de aceitação: `SS.SSS.SSS/SSSS-99` (`S` alfanumérico ×12, `9` numérico ×2).

> [!important] A máscara nova é **superconjunto** da antiga — e é isso que faz a retrocompatibilidade funcionar
> Como as 12 primeiras posições também aceitam número, um CNPJ antigo (`12.345.678/0001-95`) encaixa **inteiro** na máscara nova. Não existe "modo antigo" e "modo novo": é o **mesmo campo, a mesma máscara**, aceitando os dois formatos.
>
> Consequência pro teste: o regressivo **não** é validar dois modos, é validar que o mesmo campo aceita as duas formas — o que também significa que uma quebra na máscara derruba os dois de uma vez.

> [!note] `placeholder` ≠ `máscara` — não reabrir isso como bug
> O **placeholder** exibido é `XX.XXX.XXX/XXXX-XX`, com `X` uniforme nas 14 posições. A **máscara de aceitação** é `SS.SSS.SSS/SSSS-99`. A diferença é **intencional**: placeholder é dica visual, máscara é regra de aceitação. **Validado com o time de design pelo Rafael em 30/07** — o placeholder fica assim.
>
> Registrado porque é armadilha: eu mesmo tratei isso como divergência Figma × implementação e como "ajuste de copy a reportar" antes de perguntar. **Não é defeito.** São dois critérios distintos e ambos válidos (CT-001 confere o placeholder, CT-002 e CT-003 conferem a aceitação).

**Validação de DV passou a ser real** — as mutations `citizenInternalRegister` e `finishCitizenRegistry` **rejeitam CNPJ com dígito verificador inválido**; antes só checavam o **comprimento**. É mudança de comportamento, não só de formato.

**Retrocompatibilidade** — CNPJ numérico existente continua válido e funcional em todas as telas.

### Telas declaradas impactadas (11)

| Rota | Tela |
|---|---|
| `/login/cidadao/{id}` | Login do cidadão (campo CPF/CNPJ) |
| `/cadastro/{instanceId}` | Cadastro público (Signup PJ) |
| `/finalizar-cadastro-cidadao` | Finalização de cadastro |
| `/cliente/{id}/cidadaos/criar` | Novo usuário PJ (admin) |
| `/cliente/{id}/cidadaos/editar/{citizenId}` | Edição de cidadão PJ (admin) |
| `/cliente/{id}/cidadaos` | Listagem de cidadãos (modal de visualização) |
| `/admin/instancias/criar` e `/admin/instancias/editar/{id}` | Cadastro/edição de órgão |
| `/cliente/{id}/solicitacao-assinatura/{moduleCode}/{eventId}` | Assinatura por código (CPF/CNPJ do signatário) |
| `/recuperar-acesso/{accessToken}` | Recuperação de acesso |
| `/cidadao/meu-perfil` | Meu perfil (cidadão PJ) |
| — | Campo de número com máscara CNPJ no **construtor de formulários** (módulo principal, módulo cliente, assunto/serviço) e em **despachos personalizados de fluxo de trabalho** |

### Superfícies não visuais impactadas

- **Geração de PDF** — despacho, capa de documento, modelo base (funções internas de formatação de CNPJ).
- **Fluxo de assinatura (Lacuna)** — anonimização/formatação do CNPJ do signatário.

Regras completas de PJ: [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]]. Onde o sistema exige CPF/CNPJ válido: [[QA Workspace/04 Conhecimento/Módulos/Login|Login]].

---

> [!warning] Pontos de atenção

Os três primeiros saíram do **gate de doc** e da leitura do MR, e cada um muda o que testar. Ordem = risco real.

- 🔴 **Razão Social vem de API, é obrigatória e não é editável — e a consulta externa não aparece no MR.** [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] é explícita: *"CNPJ → API retorna a **razão social** automaticamente (não editável)"*, e Razão Social é **obrigatória** (o Nome Fantasia tem fallback manual; a Razão Social **não**). No MR !657, os arquivos de backend tocados são **só geração de PDF e `api/src/shared/utils.ts`** — **nenhum arquivo de consulta externa de CNPJ**. Se o lookup precisava ser adaptado pro formato alfanumérico, **não foi neste MR**. Se a API não devolver dados, **o cadastro PJ não conclui e não há workaround**. É o teste de maior valor da entrega — **CT-008**, com o **CT-007** como controle.
    *Ressalva honesta*: o lookup pode viver em outro serviço/repo que a lista de arquivos não mostra — a evidência é forte, não é prova.
- ⚠️ **`Rastrear Documento` não está na lista de telas declaradas, mas busca por CNPJ.** Confirmado pelo Rafael em 30/07: a busca por CNPJ existe e retorna os documentos relacionados. A doc do módulo tem **regra de máscara própria** — *"o campo deve suportar CPF/CNPJ com pontuação; o sistema preserva visualmente o que foi digitado, mas a busca funciona independente da presença de pontuação"*. Se a sanitização mudou, essa busca precisa achar PJ com CNPJ alfanumérico, com e sem pontuação. **CT-027**.
- ⚠️ **Base legada com CNPJ inválido: risco rebaixado, mas não zerado.** A validação de DV passou a ser real (antes só comprimento), o que em teoria deixaria PJ legada impossível de salvar. **Na prática provavelmente não existe** — raciocínio do Rafael, que se sustenta: se a Razão Social vem de API e é obrigatória, um CNPJ inexistente nunca completou cadastro, independente de o campo validar DV ou não. **O que sobra**: o cadastro de **órgão/instância não tem doc nenhuma no vault**, então não se sabe se consulta API. Se não consultar, ali o campo só validava comprimento e o risco permanece. **CT-026** cobre, focado em instância.
- **Unicidade × normalização de caixa**: a doc diz *"só existe **um** usuário por CNPJ"*, e o `sanitizeCnpj` normaliza para maiúsculas. Se a normalização falhar em algum ponto de entrada, `12abc…` e `12ABC…` podem virar **dois** usuários pro mesmo CNPJ. **CT-013**.
- **O Figma ilustra 1 das 11+ telas** (o modal "Cadastrar novo usuário" → Pessoa Jurídica). As outras seguem "a mesma regra", sem referência de design — a conferência de cada uma é por conta da QA.
- **Assinatura ICP e o match do certificado**: [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] registra que *"PJ com ICP: aceita certificados vinculados diretamente ao CNPJ ou ao responsável legal"*. Certificado de teste com CNPJ alfanumérico provavelmente não existe — se não houver massa, registrar como **cobertura em aberto** em vez de dar por testado.
- **Validação vem de dependência de terceiro**: o dev subiu `brazilian-values` 0.12.0 → 0.14.0. O comentário de 23/06 (Marcos Vinicius) alertava que a lib estava defasada e sugeria trocar por `cpf-cnpj-validator` ou implementar internamente; a 0.14.0 resolveu. Regressão futura pode vir de update de lib, não de código próprio.
- **Anexo não veio no export**: `new-cnpj-report.pdf` (227,8 KiB), citado pelo dev como "principais anotações" do novo padrão. Se tiver detalhe de regra que não está aqui, vale importar.
- **Prazo confuso no Notion**: "Data prevista de conclusão" traz **três** datas (25/08, 31/07 e 04/08). Confirmar qual vale.
- **Dois gaps de doc descobertos ao escrever os CTs**: não existe doc de **órgão/instância** nem de **construtor de formulários** em `04 Conhecimento/Módulos/`. Por isso 5 CTs nascem provisórios — ver aviso na seção de casos de teste.

---

## Plano de teste

| Item | Definição |
|---|---|
| **Demanda** | SGV-9493 — Melhoria técnica de compatibilidade |
| **Responsável** | Rafael |
| **Ambiente** | DEV (status "Testando em Dev") |
| **Escopo** | Máscara, sanitização e validação de CNPJ alfanumérico nas 11 telas declaradas + geração de PDF + fluxo de assinatura + construtor de formulários, preservando CNPJ numérico |
| **Fora de escopo** | O algoritmo de validação em si (vem da lib `brazilian-values` 0.14.0) e a emissão de CNPJ pela Receita |
| **Tipos de teste** | Funcional · Regressão (retrocompatibilidade) · Exploratório nas superfícies não declaradas |
| **Dependências** | CNPJ alfanumérico **válido** para teste (com DV correto) · CNPJ alfanumérico **inválido** (DV errado) · PJ já cadastrada com CNPJ numérico · idealmente uma PJ com CNPJ numérico **inválido** na base · API de consulta de CNPJ respondendo |

> [!tip] Massa de teste — preparar antes de começar
> Metade dos CTs depende de ter **quatro** CNPJs em mão: um alfanumérico válido, um alfanumérico com DV inválido, um numérico válido já cadastrado e (se existir) um numérico inválido legado. Sem o par válido/inválido não dá pra separar "aceita letra" de "valida DV", que são as duas metades da entrega.

**Critérios de aceite**

*Agrupados na mesma ordem dos casos de teste. `placeholder` e `máscara` são critérios **separados** — um é exibição, o outro é aceitação, e podem falhar independentemente.*

**A. Máscara e validação** — *locais: rodam com CNPJ gerado, não dependem de API*

- [ ] **CA1** — O campo **exibe** o placeholder `XX.XXX.XXX/XXXX-XX`
- [x] **CA2** — A máscara **aceita letras (A–Z)** nas 12 primeiras posições
- [ ] **CA3** — A máscara aceita **somente dígitos** nos 2 últimos caracteres (dígitos verificadores)
- [x] **CA4** — A estrutura visual se mantém: **14 caracteres úteis**, **18 com a formatação**, mesma pontuação
- [ ] **CA5** — Letra digitada em **minúscula** é normalizada para maiúscula *(**reprovado** — CT-019: converte só ao salvar, não no campo; bug [[QA Workspace/02 Demandas/HML/10511 - Bug CNPJ Alfanumerico Aceita Letra Minuscula Sem Normalizar No Campo|SGV-10511]])*
- [ ] **CA6** — CNPJ alfanumérico com **DV inválido** é rejeitado, com mensagem que permita entender o erro

**B. Cidadão PJ — cadastro, edição e exibição** — *dependem de CNPJ **real**, porque Razão Social é obrigatória e vem da API*

- [ ] **CA7** — **Controle**: CNPJ **numérico real** preenche a Razão Social pela API (prova que a consulta funciona no ambiente)
- [ ] **CA8** — CNPJ **alfanumérico real** preenche a Razão Social pela API, mantendo o campo não editável
- [x] **CA9** — Cadastro público (Signup PJ) conclui com CNPJ alfanumérico
- [ ] **CA10** — Finalização de cadastro do cidadão aceita CNPJ alfanumérico
- [x] **CA11** — Novo usuário PJ pelo admin conclui com CNPJ alfanumérico
- [ ] **CA12** — Edição de cidadão PJ preserva e aceita CNPJ alfanumérico *(satisfeito por construção — ver CT-006: CNPJ de cidadão já cadastrado não é editável)*
- [ ] **CA13** — Unicidade respeitada **independente de caixa**: CNPJ já cadastrado não aceita segundo usuário, nem digitado em minúscula
- [x] **CA14** — Modal de visualização da listagem exibe o CNPJ alfanumérico formatado
- [x] **CA15** — Meu perfil (cidadão PJ) exibe o CNPJ alfanumérico formatado

**C. Login e recuperação de acesso**

- [x] **CA16** — Login do cidadão autentica com CNPJ alfanumérico
- [x] **CA17** — Recuperação de acesso aceita CNPJ alfanumérico

**D. Órgão / instância**

- [x] **CA18** — Cadastro de órgão conclui com CNPJ alfanumérico
- [x] **CA19** — Edição de órgão preserva o CNPJ alfanumérico

**E. Saída em documento e assinatura**

- [ ] **CA20** — CNPJ alfanumérico sai **formatado corretamente** no PDF de despacho, na capa de documento e no modelo base *(parcial — CT-010/CT-011 aprovaram tela e impressão; falta o PDF nos três geradores, CT-025)*
- [x] **CA21** — Assinatura por código aceita o CNPJ alfanumérico do signatário
- [ ] **CA22** — O fluxo de assinatura formata/anonimiza o CNPJ alfanumérico **sem corromper o valor**

**F. Construtor de formulários**

- [ ] **CA23** — Campo com máscara CNPJ no construtor (módulo principal, módulo cliente, assunto/serviço) aceita alfanumérico
- [ ] **CA24** — Campo com máscara CNPJ em **despacho personalizado de fluxo de trabalho** aceita alfanumérico

**G. Retrocompatibilidade**

- [x] **CA25** — CNPJ **numérico** existente segue funcionando em login, edição, exibição e PDF
- [ ] **CA26** — Órgão/instância com CNPJ **inválido legado** tem comportamento definido na edição — não trava sem aviso nem perde o registro

**H. Superfícies fora da lista declarada**

- [ ] **CA27** — Busca por CNPJ no [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] encontra a PJ alfanumérica e seus documentos, **com e sem** pontuação
- [ ] **CA28** — Listagem/pesquisa de cidadãos exibe o CNPJ alfanumérico corretamente, inclusive na tag "Cadastro incompleto" *(**reprovado** — CT-016 do Waldemar, defeito da busca por CNPJ alfanumérico aberto no Notion)*

---

## Casos de teste

> [!info] Como esta lista está organizada
> **CT-001 a CT-016** são o plano que o **Waldemar** executou no Notion (`TC-712`), mantidos na ordem, na numeração e no texto dele — inclusive os sufixos `005a/b/c`. Os resultados vieram dele: **todos passaram**, exceto o **CT-006** (não se aplica) e o **CT-016** (reprovado, defeito aberto no Notion).
>
> **CT-017 em diante** é a cobertura que o cruzamento contra os 28 critérios de aceite mostrou faltando no plano dele — 11 cenários que ele não toca e 4 em que ele toca a superfície sem fazer a asserção. Estes **ainda não foram executados** e nascem em branco.
>
> A numeração dele foi preservada de propósito: os prints que ele anexou apontam pro `CT-NNN` dele, e **número de CT é identificador, não posição** (precedente 30/07, SGV-9042). A renumeração dos nossos foi possível porque a 9493 ainda não tinha nenhuma evidência nomeada por CT.

> [!tip] Ordem de execução importa em dois pontos
> **O grupo I é local** — máscara, DV e normalização não passam pela API, então rodam com CNPJ **gerado**. Comece por ele: se a máscara estiver quebrada, o resto não se sustenta.
>
> **O CT-021 vem antes do CT-022, de propósito.** O CT-021 usa CNPJ **numérico real** e prova que a consulta de Razão Social funciona no ambiente. Sem esse controle, uma Razão Social vazia no CT-022 tem duas causas indistinguíveis — "a API não suporta o formato novo" ou "esse CNPJ não existe na Receita" — e o resultado não conclui nada.

---

### A. Criação/edição de instâncias — *executado pelo Waldemar*

#### **CT-001 Criar instância utilizando CNPJ alfanumérico** *(CA18)*

**Dado** que a pessoa usuária possui permissão para criar uma instância
**Quando** informar um CNPJ válido no novo padrão
**Então** o sistema deve permitir a criação da instância
**E** os dados devem ser gravados corretamente

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Editar instância contendo CNPJ alfanumérico** *(CA19)*

**Dado** que existe uma instância cadastrada com CNPJ alfanumérico
**Quando** alterar informações da instância
**Então** o sistema deve manter o CNPJ corretamente
**E** deve salvar a edição com sucesso

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Login do cidadão — *executado pelo Waldemar*

#### **CT-003 Realizar login utilizando CNPJ alfanumérico** *(CA16)*

**Dado** que existe um cidadão Pessoa Jurídica cadastrado com CNPJ alfanumérico
**Quando** informar o CNPJ e senha válidos
**Então** o sistema deve autenticar o usuário
**E** deve direcioná-lo para a área autenticada

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*O card registra que o campo de login **rejeitava qualquer CNPJ com letra** por depender de uma checagem `isNaN` — este CT é a verificação direta daquele conserto.*

**Evidências de Testes:**

---

#### **CT-004 Impedir login com CNPJ inválido** *(cenário negativo — sem critério declarado)*

**Dado** que a tela de login está disponível
**Quando** informar um CNPJ inválido
**Então** o sistema deve impedir a autenticação
**E** deve apresentar mensagem de erro

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*Cobertura que o Waldemar somou — não havia critério de aceite pra rejeição no **login**. O CA6 cobre a rejeição de DV inválido no preenchimento do campo (CT-020), que é outra superfície. Mantido como cenário negativo legítimo.*

**Evidências de Testes:**

---

### C. Usuário cidadão PJ — *executado pelo Waldemar*

#### **CT-005a Cadastrar usuário cidadão PJ (internamente) com CNPJ alfanumérico** *(CA11)*

**Dado** que a pessoa usuária está cadastrando um cidadão Pessoa Jurídica internamente
**Quando** informar um CNPJ válido no novo padrão
**Então** o sistema deve permitir o cadastro
**E** os dados devem ser gravados corretamente

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005b Cadastrar usuário cidadão PJ (externamente) com CNPJ alfanumérico** *(CA9)*

**Dado** que cidadão PJ está se cadastrando externamente
**Quando** informar um CNPJ válido no novo padrão
**Então** o sistema deve permitir o cadastro
**E** os dados devem ser gravados corretamente

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005c Visualizar menu meu perfil com cidadão PJ com CNPJ alfanumérico** *(CA15)*

**Dado** que cidadão PJ está acessando seu ambiente
**Quando** clicar no menu meu perfil e visualizar o CNPJ
**Então** o sistema deve exibir o CNPJ no novo formato com sucesso

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-006 Editar usuário cidadão PJ com CNPJ alfanumérico** *(CA12)*

**Dado** que existe um cidadão Pessoa Jurídica cadastrado
**Quando** editar seus dados
**Então** o sistema deve manter o CNPJ corretamente
**E** deve salvar as alterações

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [x] Não se aplica

> [!info]- Por que não se aplica
> **O CNPJ de um cidadão já cadastrado não é editável** — a pré-condição do CT (alterar o CNPJ na edição) não existe na tela. O **CA12** segue válido como regra: está satisfeito **por construção**, não por teste — se o valor não pode ser alterado, ele não pode ser corrompido na edição.
>
> Se o produto passar a permitir edição de CNPJ, este CT volta a ser executável e o CA12 precisa de execução real.

**Evidências de Testes:**

---

#### **CT-007 Visualizar cidadão PJ com CNPJ alfanumérico** *(CA14)*

**Dado** que existe um cidadão Pessoa Jurídica cadastrado
**Quando** acessar sua tela de visualização
**Então** o sistema deve exibir o CNPJ utilizando a máscara `XX.XXX.XXX/XXXX-XX`
**E** o valor exibido deve corresponder ao cadastro

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:** print anexado no Notion (`TC-712` — *Visualizar cidadão PJ*)

---

### D. Recuperação de senha — *executado pelo Waldemar*

#### **CT-008 Recuperar senha utilizando CNPJ alfanumérico** *(CA17)*

**Dado** que existe um cidadão Pessoa Jurídica cadastrado
**Quando** solicitar recuperação de senha informando o CNPJ válido
**Então** o sistema deve localizar o cadastro
**E** deve iniciar o fluxo de recuperação de senha

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-009 Impedir recuperação de senha com CNPJ inválido** *(cenário negativo — sem critério declarado)*

**Dado** que a tela de recuperação de senha está disponível
**Quando** informar um CNPJ inválido
**Então** o sistema não deve iniciar o processo de recuperação
**E** deve apresentar mensagem de erro

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*Mesma natureza do CT-004: cobertura negativa somada pelo Waldemar, sem critério de aceite declarado.*

**Evidências de Testes:** print anexado no Notion (`TC-712` — *Recuperação com CNPJ inválido*)

---

### E. Visualização de documentos — *executado pelo Waldemar*

#### **CT-010 Criar/visualizar documento contendo cidadão PJ com CNPJ alfanumérico** *(CA20 — parcial)*

**Dado** que um servidor está criando um novo documento inserindo o CNPJ alfanumérico
**Quando** visualizar o documento depois de criado
**Então** o sistema deve exibir o CNPJ no novo padrão
**E** deve manter a máscara `XX.XXX.XXX/XXXX-XX`

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*Cobre o CNPJ **em tela**. O CA20 exige também a saída em **PDF** nos três geradores (despacho, capa de documento e modelo base) — isso é o CT-025, ainda em aberto.*

**Evidências de Testes:**

---

### F. Impressão de documentos — *executado pelo Waldemar*

#### **CT-011 Imprimir documento contendo cidadão PJ com CNPJ alfanumérico** *(CA20 — parcial)*

**Dado** que existe um documento contendo um cidadão Pessoa Jurídica
**Quando** realizar a impressão do documento
**Então** o CNPJ deve ser apresentado no novo padrão
**E** a formatação deve ser preservada na impressão

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### G. Assinatura — *executado pelo Waldemar*

#### **CT-012 Assinar documento contendo cidadão PJ com CNPJ alfanumérico** *(CA21)*

**Dado** que existe um documento pendente de assinatura
**E** que o cidadão Pessoa Jurídica possui CNPJ no novo padrão
**Quando** realizar a assinatura do documento
**Então** o processo de assinatura deve ser concluído com sucesso
**E** o CNPJ deve ser apresentado corretamente durante o fluxo

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*Cobre o CA21 (assinatura aceita o CNPJ). O CA22 — formatação/anonimização **sem corromper o valor** — é asserção distinta e fica no CT-026.*

**Evidências de Testes:**

---

### H. Casos de regressão importantes — *executado pelo Waldemar*

#### **CT-013 Manter compatibilidade com CNPJ exclusivamente numérico** *(CA25)*

**Dado** que existe um cadastro utilizando um CNPJ exclusivamente numérico
**Quando** acessar ou editar esse cadastro
**Então** o sistema deve continuar aceitando o CNPJ
**E** nenhuma informação deve ser alterada indevidamente

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*Regressivo central. Como a máscara nova é **superconjunto** da antiga (12 posições alfanuméricas aceitam número), é o **mesmo campo** servindo os dois formatos — uma quebra aqui derruba os dois de uma vez.*

**Evidências de Testes:**

---

#### **CT-014 Permitir utilização de letras maiúsculas e números no CNPJ** *(CA2)*

**Dado** que a pessoa usuária está preenchendo um campo de CNPJ
**Quando** informar caracteres alfanuméricos válidos
**Então** o sistema deve aceitar letras de A a Z
**E** deve aceitar números de 0 a 9
**E** deve impedir caracteres especiais não previstos

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*A restrição **posicional** (letra só nas 12 primeiras, dígito nos 2 últimos) não é asserção deste CT — está no CT-018.*

**Evidências de Testes:**

---

#### **CT-015 Validar limite máximo de caracteres do CNPJ** *(CA4)*

**Dado** que a pessoa usuária está preenchendo um campo de CNPJ
**Quando** tentar informar mais caracteres do que o permitido
**Então** o sistema deve limitar a entrada ao formato `XX.XXX.XXX/XXXX-XX`

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:** print anexado no Notion (`TC-712`)

---

#### **CT-016 Pesquisar Pessoa Jurídica utilizando CNPJ alfanumérico** *(CA28)*

**Dado** que existe uma Pessoa Jurídica cadastrada com CNPJ alfanumérico
**Quando** pesquisar utilizando o CNPJ completo
**Então** o sistema deve localizar corretamente o registro
**E** deve apresentar os dados da empresa

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

> [!danger]- Reprovado — defeito aberto pelo Waldemar
> **"Busca por CNPJ alfanumérico não retorna resultado (o item existe)"** — defeito registrado por ele no Notion, ainda sem SGV conhecido aqui no vault.
>
> Bate direto nos nossos **CT-030** (busca no Rastrear Documento, com e sem pontuação) e **CT-031** (listagem/pesquisa de cidadãos): quando a correção subir, os três se revalidam juntos. O **CA28 não é aprovado** enquanto isso.

**Evidências de Testes:**

---

### I. Máscara e validação — *cobertura que faltava*

#### **CT-017 Placeholder do campo de CNPJ** *(CA1)*

**Dado** que eu estou numa tela com campo de CNPJ (ex.: novo usuário PJ)
**Quando** o campo está vazio
**Então** verifico que o placeholder exibido é `XX.XXX.XXX/XXXX-XX`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Comportamento aprovado pelo design em 30/07 — o `X` uniforme é intencional e **não** indica que o DV aceita letra. Ver a nota `placeholder ≠ máscara` em Regras de negócio.*

**Evidências de Testes:**

---

#### **CT-018 Máscara aceita somente dígitos nos 2 últimos caracteres** *(CA3)*

**Dado** que eu estou num campo de CNPJ com as 12 primeiras posições preenchidas
**Quando** eu tento digitar uma **letra** em qualquer um dos 2 últimos caracteres
**Então** verifico que a letra **não é aceita**, e que dígitos de 0 a 9 são

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*O CT-014 do Waldemar provou que letra é aceita e caractere especial não; nenhum CT dele testa **onde** a letra é aceita. Esta é a metade que falta da máscara.*

**Evidências de Testes:**

---

#### **CT-019 Letra minúscula é normalizada para maiúscula** *(CA5)*

**Dado** que eu estou num campo de CNPJ
**Quando** eu digito as letras em **minúsculas**
**Então** verifico que são convertidas para **maiúsculas** no campo, e que o valor salvo também está em maiúsculas

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

> [!danger]- Reprovado em DEV — bug [[QA Workspace/02 Demandas/HML/10511 - Bug CNPJ Alfanumerico Aceita Letra Minuscula Sem Normalizar No Campo|SGV-10511]] aberto
> **A segunda metade do `Então` passa, a primeira não.** O valor salvo fica em maiúsculas, mas o campo **não converte durante a digitação** — a normalização só acontece ao finalizar o cadastro.
>
> Encontrado em execução exploratória (31/07) em três superfícies: cadastro de cidadão PJ pelo servidor, cadastro público (signup) e **campo com máscara CNPJ do construtor de formulários**. Neste último é pior — não há normalização em camada nenhuma e o valor fica **exibido em minúsculas** depois de gravado, o que também respinga no **CT-027** (ainda não executado).
>
> O **CA5 não é aprovado** enquanto o fix não subir.

**Evidências de Testes:**

![[9493 - EV-01 - CT-019 - letra minuscula nao normalizada no campo de cadastro.mp4]]

*Evidência compartilhada com [[QA Workspace/02 Demandas/HML/10511 - Bug CNPJ Alfanumerico Aceita Letra Minuscula Sem Normalizar No Campo|SGV-10511]] — mesmo vídeo do **cenário 1** daquele card, cópia renomeada. Os cenários 2 e 3 do bug estão só lá: o 3 (construtor de formulários) falha também na segunda metade do `Então` deste CT e é assunto do **CT-027**, ainda não executado.*

---

#### **CT-020 CNPJ alfanumérico com DV inválido é rejeitado** *(CA6)*

**Dado** que eu tenho um CNPJ alfanumérico com **dígito verificador incorreto**
**Quando** eu preencho o campo e tento avançar
**Então** verifico que o valor é rejeitado, com mensagem que permita entender que o problema é o dígito verificador

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Os CT-004 e CT-009 do Waldemar rejeitam CNPJ inválido no **login** e na **recuperação**. Este testa a rejeição no **preenchimento**, que é onde o CA6 mora — e é o que separa "aceita letra" de "valida DV".*

**Evidências de Testes:**

---

### J. Cidadão PJ — Razão Social, cadastro e unicidade — *cobertura que faltava*

#### **CT-021 Controle — CNPJ numérico real preenche a Razão Social** *(CA7)*

**Dado** que eu estou no cadastro de novo usuário PJ
**Quando** eu informo um CNPJ **numérico de empresa real** (que existe na base da Receita)
**Então** verifico que a **Razão Social é preenchida automaticamente** pela API e fica não editável

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Este é o **controle** do CT-022. Se ele falhar, a consulta está indisponível no ambiente e o CT-022 não pode ser interpretado — resolver isto antes de seguir.*

**Evidências de Testes:**

---

#### **CT-022 Razão Social preenchida com CNPJ alfanumérico real** *(CA8)*

**Dado** que o CT-021 passou (a consulta funciona no ambiente)
**E** que eu tenho um CNPJ **alfanumérico de empresa real**
**Quando** eu informo esse CNPJ no cadastro de novo usuário PJ
**Então** verifico que a **Razão Social é preenchida automaticamente** e o campo segue não editável

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*⚠️ **Teste de maior valor da entrega, e nenhum CT do Waldemar o cobre.** Nenhum arquivo de consulta externa de CNPJ aparece no MR !657 — se a Razão Social não vier, o cadastro PJ **não conclui e não há workaround**, porque o campo é obrigatório e não editável. Nesse caso é **bloqueio de escopo**, não bug de máscara. Os CT-005a/005b dele passaram, mas o `Então` deles para em "os dados devem ser gravados corretamente" e não afirma nada sobre a Razão Social.*

**Evidências de Testes:**

---

#### **CT-023 Finalização de cadastro do cidadão** *(CA10)*

**Dado** que existe um cidadão PJ com cadastro pendente de conclusão
**Quando** eu concluo o cadastro em `/finalizar-cadastro-cidadao` informando o CNPJ alfanumérico
**Então** verifico que a conclusão é aceita e o CNPJ é gravado corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-024 Unicidade independente de caixa** *(CA13)*

**Dado** que existe um cidadão PJ cadastrado com CNPJ alfanumérico (letras em maiúsculas)
**Quando** eu tento cadastrar outro usuário com o **mesmo** CNPJ, digitando as letras em **minúsculas**
**Então** verifico que o sistema **impede** o cadastro por duplicidade — a normalização de caixa não permite dois usuários pro mesmo CNPJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*A doc de [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] é explícita: "só existe **um** usuário por CNPJ".*

**Evidências de Testes:**

---

### K. Saída em documento e assinatura — *cobertura parcial dele, asserção que falta*

#### **CT-025 CNPJ alfanumérico no PDF gerado** *(CA20)*

**Dado** que existe um documento de uma PJ com CNPJ alfanumérico
**Quando** eu gero o PDF (despacho, capa de documento e modelo base)
**Então** verifico que o CNPJ aparece **formatado corretamente** em cada um, com letras em maiúsculas e a pontuação certa

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Os CT-010 e CT-011 dele cobrem exibição em tela e impressão. O CA20 nomeia **três geradores** — despacho, capa e modelo base — e é isso que falta conferir um a um.*

> [!warning]- Provisório — refinar após a primeira observação
> O `Então` está no nível de precisão possível **sem doc e sem ter visto a tela**: o card cita "funções internas de formatação de CNPJ" nos três geradores, mas **não diz onde** o CNPJ aparece em cada saída — falta identificar a posição exata no despacho, na capa e no modelo base. Ao rodar, ajustar o texto pro comportamento real.
>
> **A partir daqui o número deste CT não muda** — renumerar depois que existe evidência nomeada quebra o vínculo `CT-NNN` ↔ arquivo (precedente de 30/07 na SGV-9042).

**Evidências de Testes:**

---

#### **CT-026 Formatação e anonimização no fluxo de assinatura** *(CA22)*

**Dado** que uma PJ com CNPJ alfanumérico assinou um documento
**Quando** eu confiro o registro da assinatura e o documento assinado
**Então** verifico que o CNPJ aparece formatado e **sem corrupção do valor** (nenhuma letra trocada, removida ou substituída)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*A [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|doc de Assinaturas]] registra que "PJ com ICP aceita certificados vinculados diretamente ao CNPJ ou ao responsável legal". Se **não houver certificado de teste** com CNPJ alfanumérico, registrar como **cobertura em aberto** em vez de dar por testado.*

**Evidências de Testes:**

---

### L. Construtor de formulários — *cobertura que faltava*

#### **CT-027 Campo com máscara CNPJ no construtor de formulários** *(CA23)*

**Dado** que eu configuro um campo de número com máscara CNPJ no construtor (módulo principal, módulo cliente e assunto/serviço)
**Quando** um usuário preenche esse campo com CNPJ alfanumérico
**Então** verifico que o valor é aceito, mascarado e salvo corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

> [!warning]- Provisório — refinar após a primeira observação
> O `Então` está no nível de precisão possível **sem doc e sem ter visto a tela**: não existe doc do **construtor de formulários** em `04 Conhecimento/Módulos/`, então não se sabe como o campo com máscara CNPJ é configurado nem onde o valor é exibido depois. Ao rodar, ajustar o texto pro comportamento real.
>
> **A partir daqui o número deste CT não muda** — renumerar depois que existe evidência nomeada quebra o vínculo `CT-NNN` ↔ arquivo (precedente de 30/07 na SGV-9042).

**Evidências de Testes:**

---

#### **CT-028 Campo com máscara CNPJ em despacho personalizado de workflow** *(CA24)*

**Dado** que existe um despacho personalizado de etapa com campo de máscara CNPJ
**Quando** eu preencho esse campo com CNPJ alfanumérico e emito o despacho
**Então** verifico que o valor é aceito e aparece correto no despacho emitido

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

> [!warning]- Provisório — refinar após a primeira observação
> O `Então` está no nível de precisão possível **sem doc e sem ter visto a tela**: mesma razão do CT-027, e ainda depende de saber como o campo se comporta dentro do fluxo de trabalho. Ao rodar, ajustar o texto pro comportamento real.
>
> **A partir daqui o número deste CT não muda** — renumerar depois que existe evidência nomeada quebra o vínculo `CT-NNN` ↔ arquivo (precedente de 30/07 na SGV-9042).

**Evidências de Testes:**

---

### M. Retrocompatibilidade — *cobertura que faltava*

#### **CT-029 Órgão com CNPJ inválido legado na edição** *(CA26)*

**Dado** que existe um órgão/instância cadastrado com CNPJ numérico **inválido** (aceito pela regra antiga, que só checava comprimento)
**Quando** eu abro a edição desse órgão e tento salvar
**Então** verifico que há comportamento definido — mensagem clara ou permissão de salvar — sem travar sem aviso nem perder o registro

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Risco **rebaixado**: para **cidadão PJ** a Razão Social vem de API obrigatória, então CNPJ inexistente nunca completou cadastro. Sobra a instância, que não tem doc e pode não consultar API. **Se não houver órgão inválido na base, marcar como não se aplica** em vez de forçar o cenário.*

**Evidências de Testes:**

---

### N. Superfícies fora da lista declarada — *cobertura parcial dele, asserção que falta*

#### **CT-030 Busca por CNPJ no Rastrear Documento** *(CA27)*

**Dado** que existe uma PJ com CNPJ alfanumérico que tem documentos no sistema
**Quando** eu busco por esse CNPJ no input-search do Rastrear Documento, **com** e **sem** pontuação
**Então** verifico que a PJ e seus documentos são retornados nas duas formas

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Tela **não declarada** na lista de impactos do card, mas confirmada pelo Rafael. A doc do módulo tem regra própria: "o campo deve suportar CPF/CNPJ com pontuação; a busca funciona independente da presença de pontuação".*
*⚠️ **O CT-016 do Waldemar já reprovou a busca** por CNPJ alfanumérico. Este CT provavelmente reprova junto — rodar só depois que a correção do defeito dele subir, e conferir as duas formas (com e sem pontuação), que é o que o CT dele não separa.*

**Evidências de Testes:**

---

#### **CT-031 Listagem e pesquisa de cidadãos** *(CA28)*

**Dado** que existe uma PJ com CNPJ alfanumérico, inclusive alguma com cadastro incompleto
**Quando** eu pesquiso e listo cidadãos
**Então** verifico que o CNPJ alfanumérico é exibido corretamente, inclusive na linha com a tag "Cadastro incompleto"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Complementa o CT-016 dele (reprovado): ele testa a **pesquisa**; este acrescenta a **exibição na listagem** e o caso da tag "Cadastro incompleto".*

**Evidências de Testes:**

---

> [!danger] Bugs encontrados
> - [[QA Workspace/02 Demandas/HML/10511 - Bug CNPJ Alfanumerico Aceita Letra Minuscula Sem Normalizar No Campo|SGV-10511]] — **CNPJ alfanumérico aceita letra minúscula sem normalizar no campo**, reprovando o **CT-019** (CA5). Achado em execução exploratória em DEV (31/07), em três superfícies: cadastro pelo servidor, cadastro público e campo do construtor de formulários. Nas duas primeiras o dado final fica certo e a falha é de digitação; na terceira **não há normalização em camada nenhuma** e o valor fica exibido em minúsculas — o que também respinga no **CT-027** (CA23), ainda não executado.
> - **Busca por CNPJ alfanumérico não retorna resultado (o item existe)** — encontrado pelo **Waldemar** na execução do `TC-712` (CT-016), reprovando o CA28. Defeito **já aberto por ele no Notion**; o SGV ainda não é conhecido aqui no vault, então segue sem card próprio.
>     > [!note]- Alcance do defeito
>     > Atinge as três superfícies de busca por CNPJ do escopo: a **pesquisa de cidadãos** (CT-016, reprovado), a **listagem** com a tag "Cadastro incompleto" (CT-031, não executado) e a busca no **Rastrear Documento** com e sem pontuação (CT-030, não executado).
>     >
>     > O CT-030 e o CT-031 **não devem ser executados antes da correção subir** — reprovariam pelo mesmo motivo e gerariam registro duplicado do mesmo defeito. Quando o fix chegar, os três se revalidam juntos.

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9493)

![[9493 - 2.mp4]]

---

> [!tip] Observações

**Gate de doc** (2026-07-30, fluxo 8): cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]], [[QA Workspace/04 Conhecimento/Módulos/Login|Login]], [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] e [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]]. As regras de PJ, de exigência de "CPF ou CNPJ válido" e de busca por CNPJ **já estão documentadas** e sustentam os critérios — o que a doc **não** cobre é o formato do CNPJ em si (nenhum módulo descreve a máscara). Quando esta entrega for aprovada, vale levar a regra do formato pra doc de Usuário Cidadão (fluxo 8).

**Figma lido em 30/07** — página `[SGV-9493]` da Tramitação/Handoff, com 3 cards de especificação e 1 tela de exemplo. Página inteira capturada; não há outras seções.

**Card criado direto, sem mesa de refinamento** — rota do [[Sistema/Skills/SKILL_LIMPEZA_EXPORT#B — Card direto (task completa)|SKILL_LIMPEZA_EXPORT modo B]], autorizada pela regra "quando PULAR a mesa" da [[Sistema/Skills/SKILL_REFINAMENTO|SKILL_REFINAMENTO]]: a spec do Notion está completa (objetivo, telas, endpoints, alterações, arquivos, MR) e não declara regra pendente de validação — diferente da [[QA Workspace/02 Demandas/Concluídas/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]], que precisou de mesa porque a spec listava 4 regras sem conteúdo.

---

## Histórico

- 2026-07-30 - 📝 Melhoria refinada (export do Notion + Figma processados; 26 critérios de aceite, 4 riscos levantados no gate de doc)
- 2026-07-31 - 🔴 Reaberta em DEV (CT-019 reprovado: o campo não normaliza a letra minúscula durante a digitação — bug [[QA Workspace/02 Demandas/HML/10511 - Bug CNPJ Alfanumerico Aceita Letra Minuscula Sem Normalizar No Campo|SGV-10511]] aberto). Evidência compartilhada com o card do bug — mesmo vídeo, cópia renomeada
- 2026-07-31 - 🔎 Análise (o plano que o Waldemar executou foi cruzado com os nossos casos: os 16 dele viraram a primeira parte da lista, com os resultados dele; os 15 que faltavam entraram depois. 12 critérios já aprovados, 1 não se aplica, 1 reprovado pelo defeito da busca, 13 ainda por testar)
