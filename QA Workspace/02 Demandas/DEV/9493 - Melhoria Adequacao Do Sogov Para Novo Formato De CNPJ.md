---
tags:
  - demanda
  - melhoria
  - qa
  - usuario-cidadao
task: "9493"
mel: ""
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
- [ ] **CA2** — A máscara **aceita letras (A–Z)** nas 12 primeiras posições
- [ ] **CA3** — A máscara aceita **somente dígitos** nos 2 últimos caracteres (dígitos verificadores)
- [ ] **CA4** — A estrutura visual se mantém: **14 caracteres úteis**, **18 com a formatação**, mesma pontuação
- [ ] **CA5** — Letra digitada em **minúscula** é normalizada para maiúscula
- [ ] **CA6** — CNPJ alfanumérico com **DV inválido** é rejeitado, com mensagem que permita entender o erro

**B. Cidadão PJ — cadastro, edição e exibição** — *dependem de CNPJ **real**, porque Razão Social é obrigatória e vem da API*

- [ ] **CA7** — **Controle**: CNPJ **numérico real** preenche a Razão Social pela API (prova que a consulta funciona no ambiente)
- [ ] **CA8** — CNPJ **alfanumérico real** preenche a Razão Social pela API, mantendo o campo não editável
- [ ] **CA9** — Cadastro público (Signup PJ) conclui com CNPJ alfanumérico
- [ ] **CA10** — Finalização de cadastro do cidadão aceita CNPJ alfanumérico
- [ ] **CA11** — Novo usuário PJ pelo admin conclui com CNPJ alfanumérico
- [ ] **CA12** — Edição de cidadão PJ preserva e aceita CNPJ alfanumérico
- [ ] **CA13** — Unicidade respeitada **independente de caixa**: CNPJ já cadastrado não aceita segundo usuário, nem digitado em minúscula
- [ ] **CA14** — Modal de visualização da listagem exibe o CNPJ alfanumérico formatado
- [ ] **CA15** — Meu perfil (cidadão PJ) exibe o CNPJ alfanumérico formatado

**C. Login e recuperação de acesso**

- [ ] **CA16** — Login do cidadão autentica com CNPJ alfanumérico
- [ ] **CA17** — Recuperação de acesso aceita CNPJ alfanumérico

**D. Órgão / instância**

- [ ] **CA18** — Cadastro de órgão conclui com CNPJ alfanumérico
- [ ] **CA19** — Edição de órgão preserva o CNPJ alfanumérico

**E. Saída em documento e assinatura**

- [ ] **CA20** — CNPJ alfanumérico sai **formatado corretamente** no PDF de despacho, na capa de documento e no modelo base
- [ ] **CA21** — Assinatura por código aceita o CNPJ alfanumérico do signatário
- [ ] **CA22** — O fluxo de assinatura formata/anonimiza o CNPJ alfanumérico **sem corromper o valor**

**F. Construtor de formulários**

- [ ] **CA23** — Campo com máscara CNPJ no construtor (módulo principal, módulo cliente, assunto/serviço) aceita alfanumérico
- [ ] **CA24** — Campo com máscara CNPJ em **despacho personalizado de fluxo de trabalho** aceita alfanumérico

**G. Retrocompatibilidade**

- [ ] **CA25** — CNPJ **numérico** existente segue funcionando em login, edição, exibição e PDF
- [ ] **CA26** — Órgão/instância com CNPJ **inválido legado** tem comportamento definido na edição — não trava sem aviso nem perde o registro

**H. Superfícies fora da lista declarada**

- [ ] **CA27** — Busca por CNPJ no [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] encontra a PJ alfanumérica e seus documentos, **com e sem** pontuação
- [ ] **CA28** — Listagem/pesquisa de cidadãos exibe o CNPJ alfanumérico corretamente, inclusive na tag "Cadastro incompleto"

---

## Casos de teste

*A escrever após a preparação da massa. A ordem segue os grupos dos critérios; a numeração das evidências é independente (`EV-NN`), conforme [[QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]].*

---

> [!danger] Bugs encontrados

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9493)

---

> [!tip] Observações

**Gate de doc** (2026-07-30, fluxo 8): cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]], [[QA Workspace/04 Conhecimento/Módulos/Login|Login]], [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] e [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]]. As regras de PJ, de exigência de "CPF ou CNPJ válido" e de busca por CNPJ **já estão documentadas** e sustentam os critérios — o que a doc **não** cobre é o formato do CNPJ em si (nenhum módulo descreve a máscara). Quando esta entrega for aprovada, vale levar a regra do formato pra doc de Usuário Cidadão (fluxo 8).

**Figma lido em 30/07** — página `[SGV-9493]` da Tramitação/Handoff, com 3 cards de especificação e 1 tela de exemplo. Página inteira capturada; não há outras seções.

**Card criado direto, sem mesa de refinamento**: a spec do Notion está completa (objetivo, telas, endpoints, alterações, arquivos, MR) e não declara regra pendente de validação — diferente da [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]], que precisou de mesa porque a spec listava 4 regras sem conteúdo.

---

## Histórico

- 2026-07-30 - 📝 Melhoria refinada (export do Notion + Figma processados; 26 critérios de aceite, 4 riscos levantados no gate de doc)
