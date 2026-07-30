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

**Formato** — máscara passa de `00.000.000/0000-00` (só dígitos) para aceitar letras. Estrutura visual **inalterada**: `XX.XXX.XXX/XXXX-XX`, **14 caracteres úteis** e **18 com a formatação**. Letras de A a Z e números de 0 a 9, normalizadas para **maiúsculas**.

**Onde o alfanumérico vale e onde não** — as **12 primeiras** posições aceitam letra; os **2 últimos** caracteres são os **dígitos verificadores** e seguem **numéricos**. Na implementação a máscara é `SS.SSS.SSS/SSSS-99` (`S` alfanumérico, `9` numérico).

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

Os quatro primeiros saíram do **gate de doc** e do Figma, antes de escrever qualquer critério — cada um muda o que testar.

- 🔴 **Razão Social é preenchida por API e não é editável — se a API não aceitar CNPJ alfanumérico, o cadastro PJ trava sem workaround.** [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] é explícita: *"CNPJ → API retorna a **razão social** automaticamente (não editável)"* e Razão Social é **obrigatória**. O card não menciona a consulta externa em nenhum lugar — nem nas telas, nem nos endpoints. **Se a API de CNPJ ainda não devolve dados pro formato novo, não há como concluir o cadastro**, porque o campo obrigatório não pode ser digitado à mão. É o primeiro cenário a exercitar (CT-012); se falhar, é bloqueio de escopo, não bug de máscara.
- ⚠️ **Divergência Figma × implementação nos 2 últimos caracteres.** O Figma diz que a máscara nova *"utiliza X como coringa para indicar caractere alfanumérico, aceitando letras de A a Z e números de 0 a 9"* e mostra `XX.XXX.XXX/XXXX-XX` — o que, lido ao pé da letra, autoriza **letra também nos dígitos verificadores**. A implementação usa `SS.SSS.SSS/SSSS-99` (12 alfanuméricos + 2 numéricos), que é o que a regra da RFB manda e o que o próprio objetivo do card diz. **A implementação está certa; o Figma está impreciso.** Consequência prática: o **placeholder exibido ao usuário** (`XX.XXX.XXX/XXXX-XX`) informa que cabe letra nas duas últimas posições, e não cabe — **ajuste de copy a reportar**, não bug de validação. Não reprovar a máscara por causa disso.
- ⚠️ **Base legada com CNPJ inválido pode travar na edição.** A validação de DV **passou a ser real** (antes só comprimento), então qualquer PJ cadastrado com CNPJ numericamente inválido — que passou pela regra antiga — pode ficar **impossível de salvar** ao ser editado. Não está no escopo declarado e é o risco mais caro: atinge base existente, não cadastro novo. CT-024 cobre.
- ⚠️ **`Rastrear Documento` não está na lista de telas impactadas, mas busca por CNPJ.** A doc do módulo define: *"Input-search: busca ampla por CPF, **CNPJ**, nome…"* com **regra de máscara própria** — *"o campo deve suportar CPF/CNPJ com pontuação; o sistema preserva visualmente o que foi digitado, mas a busca funciona independente da presença de pontuação"*. Se a sanitização mudou, essa busca precisa achar PJ com CNPJ alfanumérico, com e sem pontuação. CT-025.
- **Unicidade × normalização de caixa**: a doc diz *"só existe **um** usuário por CNPJ"*, e o `sanitizeCnpj` normaliza para maiúsculas. Se a normalização falhar em algum ponto de entrada, `12abc…` e `12ABC…` podem virar **dois** usuários pro mesmo CNPJ. CT-013.
- **O Figma ilustra 1 das 11+ telas** (o modal "Cadastrar novo usuário" → Pessoa Jurídica). As outras seguem "a mesma regra", sem referência de design — a conferência de cada uma é por conta da QA.
- **Assinatura ICP e o match do certificado**: [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] registra que *"PJ com ICP: aceita certificados vinculados diretamente ao CNPJ ou ao responsável legal"*. Certificado de teste com CNPJ alfanumérico provavelmente não existe — se não houver massa, registrar como cobertura em aberto em vez de dar por testado.
- **Biblioteca**: o dev subiu `brazilian-values` de 0.12.0 → 0.14.0. O comentário de 23/06 (Marcos Vinicius) alertava que a lib estava defasada e sugeria trocar por `cpf-cnpj-validator` ou implementar internamente; a 0.14.0 resolveu. Vale saber que a validação vem de **dependência de terceiro**, não de código próprio — regressão pode vir de update de lib.
- **Anexo não veio no export**: `new-cnpj-report.pdf` (227,8 KiB), citado no comentário do dev como "principais anotações" do novo padrão. Se tiver detalhe de regra que não está aqui, vale importar.
- **Prazo confuso no Notion**: o campo "Data prevista de conclusão" traz **três** datas (25/08, 31/07 e 04/08). Confirmar qual vale.

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

**A. Regra da máscara**

- [ ] **CA1** — O input de CNPJ aceita **letras de A a Z** nas 12 primeiras posições
- [ ] **CA2** — O input aceita **somente dígitos** nos 2 últimos caracteres (dígitos verificadores)
- [ ] **CA3** — A estrutura visual permanece `XX.XXX.XXX/XXXX-XX`: 14 caracteres úteis, 18 com formatação, mesma pontuação
- [ ] **CA4** — Letra digitada em **minúscula** é normalizada para maiúscula
- [ ] **CA5** — CNPJ alfanumérico com **DV inválido** é rejeitado, com mensagem que permita entender o erro

**B. Cadastro, edição e exibição de cidadão PJ**

- [ ] **CA6** — Cadastro público (Signup PJ) conclui com CNPJ alfanumérico
- [ ] **CA7** — Finalização de cadastro do cidadão aceita CNPJ alfanumérico
- [ ] **CA8** — Novo usuário PJ pelo admin conclui com CNPJ alfanumérico
- [ ] **CA9** — Edição de cidadão PJ preserva e aceita CNPJ alfanumérico
- [ ] **CA10** — Modal de visualização da listagem exibe o CNPJ alfanumérico formatado
- [ ] **CA11** — Meu perfil (cidadão PJ) exibe o CNPJ alfanumérico corretamente
- [ ] **CA12** — A **Razão Social** segue sendo preenchida pela API para CNPJ alfanumérico, mantendo o campo não editável
- [ ] **CA13** — Unicidade respeitada **independente de caixa**: CNPJ já cadastrado não aceita segundo usuário, nem digitado em minúscula

**C. Login e recuperação de acesso**

- [ ] **CA14** — Login do cidadão autentica com CNPJ alfanumérico
- [ ] **CA15** — Recuperação de acesso aceita CNPJ alfanumérico

**D. Órgão / instância**

- [ ] **CA16** — Cadastro de órgão conclui com CNPJ alfanumérico
- [ ] **CA17** — Edição de órgão preserva o CNPJ alfanumérico

**E. Saída em documento e assinatura**

- [ ] **CA18** — CNPJ alfanumérico sai **formatado corretamente** no PDF de despacho, na capa de documento e no modelo base
- [ ] **CA19** — Assinatura por código aceita o CNPJ alfanumérico do signatário
- [ ] **CA20** — O fluxo de assinatura formata/anonimiza o CNPJ alfanumérico sem corromper o valor

**F. Construtor de formulários**

- [ ] **CA21** — Campo com máscara CNPJ no construtor (módulo principal, módulo cliente, assunto/serviço) aceita alfanumérico
- [ ] **CA22** — Campo com máscara CNPJ em **despacho personalizado de fluxo de trabalho** aceita alfanumérico

**G. Retrocompatibilidade**

- [ ] **CA23** — CNPJ **numérico** existente segue funcionando em login, edição, exibição e PDF
- [ ] **CA24** — PJ com CNPJ numérico **inválido já na base** tem comportamento definido na edição — não trava sem aviso nem perde o registro

**H. Superfícies fora da lista declarada**

- [ ] **CA25** — Busca por CNPJ no [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] encontra PJ com CNPJ alfanumérico, **com e sem** pontuação
- [ ] **CA26** — Listagem/pesquisa de cidadãos exibe o CNPJ alfanumérico corretamente, inclusive na tag "Cadastro incompleto"

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
