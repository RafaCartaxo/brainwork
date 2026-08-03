---
title: Usuário Cidadão
tags:
  - qa
  - conhecimento
  - sogov
  - usuario-cidadao
tipo: modulo
revisado: 2026-07-20
fonte: https://app.notion.com/p/alfa-group/Usu-rio-Cidad-o-15050c52ecbf40eca2e35e5ca6576b65
fonte_criado: 2024-09-17 (Alice Martins)
fonte_ultima_edicao: 2026-07-02 (Fernando Junior)
---
# Usuário Cidadão

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. O export veio com ruído (imagens, propriedades do Notion) removido preservando as regras. A seção "Feature — Acesso via gov.br" (02/07/2026) veio **só com o título**, sem conteúdo — ver [[#Dúvidas em aberto]]. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

## Visão geral

Usuários cidadãos são de dois tipos:

| Tipo | Identificador | Regra de unicidade |
|---|---|---|
| Pessoa Física | CPF | Só existe **um** usuário por CPF |
| Pessoa Jurídica | CNPJ | Só existe **um** usuário por CNPJ |

Independente do tipo, o cidadão acessa um ambiente próprio onde faz solicitações e acompanha o andamento delas.

> [!note] Usuário único entre ambientes
> Um usuário SoGov (cidadão **ou** servidor) é único: se cadastrado como servidor, um ambiente cidadão correspondente já é criado automaticamente, e é possível fazer **switch** entre eles. Da mesma forma, um cidadão que passa a trabalhar numa prefeitura (ou em mais de uma) recebe um convite para se cadastrar no novo ambiente, **mantendo o mesmo usuário e senha**.

## Regras de negócio

### Permissões do cidadão

Um usuário cidadão pode:

- Fazer solicitações na central de atendimento;
- Alterar informações do seu cadastro (meu perfil);
- Fazer switch de ambientes (caso seja servidor também);
- Interagir nos documentos que tem acesso (solicitações ou envolvimentos);
- Assinar;
- Fazer despachos;
- Imprimir;
- **Cancelar solicitação** — só se foi ele quem abriu o documento.

### Cadastro (fluxo original)

Feito pelo **portal do cidadão SoGov**, com link disponibilizado pelo cliente. Campos variam por tipo:

**Pessoa Física (CPF)**
- CPF → API retorna o **nome completo** automaticamente (não editável);
- Obrigatórios/demais campos: nome de exibição (exibido no sistema e documentos), e-mail, senha + confirmação, aceite de privacidade e termos;
- Opcionais: data de nascimento, sexo, telefone celular, telefone fixo.

**Pessoa Jurídica (CNPJ)**
- CNPJ → API retorna a **razão social** automaticamente (não editável);
- Obrigatórios/demais campos: nome fantasia (exibido no sistema e documentos), nome do responsável legal, CPF do responsável legal, e-mail, senha + confirmação, aceite de privacidade e termos;
- Opcionais: telefone celular, telefone fixo, ramal.

Após o cadastro, o usuário (PF ou PJ) recebe **e-mail de boas-vindas** e precisa clicar em confirmar antes de conseguir logar.

### Atualizações de cadastro PJ (21/11/2025)

O cadastro de servidor externo PJ afeta três fluxos distintos:

#### 1. Cadastro interno da pessoa jurídica (feito por um servidor)

| Campo | Regra |
|---|---|
| CNPJ | Obrigatório; consulta API preenche **Razão Social** automaticamente |
| Razão Social | Preenchido automaticamente, **não editável** |
| Nome Fantasia | Opcional; API pode preencher automaticamente, senão digitação manual a qualquer momento |
| E-mail institucional | Obrigatório; recebe o convite de conclusão do cadastro externo; **único no sistema** (mesma regra de não-duplicidade do e-mail pessoal da PF) |
| Telefone | Opcional |
| CPF do responsável legal | Opcional; ao informar, API busca e preenche **Nome do responsável legal** automaticamente |

#### 2. Conclusão do cadastro externo após pré-cadastro (PJ já cadastrada internamente por um servidor)

- **Nome Fantasia**: se não veio do cadastro interno, passa a ser **obrigatório** aqui; se já veio, fica disponível só pra visualização;
- **CPF do responsável legal**: se não veio do cadastro interno, **obrigatório** aqui; se já existe, pode ser alterado — alterando, a API é consultada novamente e o Nome do responsável legal é atualizado;
- **Nome do responsável legal**: sempre atualizado automaticamente a partir do CPF informado;
- **Telefone**: opcional; se veio pré-cadastrado, aparece preenchido e pode ser alterado livremente.

#### 3. Cadastro externo sem pré-cadastro interno (PJ direto pela plataforma)

- **Nome Fantasia**: passa a ser **obrigatório**;
- Telefone celular, telefone fixo e ramal: opcionais, com a informação exposta na label do campo;
- Ajustes de copy: placeholder da etapa de e-mail e label da etapa de senha (clareza quanto ao uso da senha em operações de assinatura digital) — *conferir protótipos pras mudanças exatas de copy*.

### Regras gerais de e-mail e assinatura (PJ)

- **E-mail institucional** da PJ é equivalente ao e-mail pessoal da PF — mesma regra de restrição de duplicidade;
- **Assinatura da PJ** é enviada para o e-mail institucional cadastrado;
- **Assinatura SoGov**: fluxo padrão de senha de conta para autenticação; no documento, entram os dados da empresa **e** do responsável legal;
- **Assinatura ICP**: valida o token da PJ solicitante (autenticidade); no documento, entram os dados da empresa **e** do responsável legal.

### Integrações técnicas (resumo)

| Consulta | Preenche automaticamente |
|---|---|
| CNPJ via API | Razão Social |
| CPF via API | Nome do responsável legal |

## Backlog da página (Notion)

- [Melhoria] Permitir cadastro de cidadão Pessoa Jurídica sem vincular dados do responsável legal;
- *Permitir login cidadão utilizando conta Gov.br — mesmo tema da seção "Feature — Acesso do cidadão via gov.br" abaixo, que veio sem conteúdo no export.

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] **Feature "Acesso do cidadão (Pessoa Física) via gov.br"** (~02/07/2026, autoria da última edição da página): veio **só o título** no export — buscar o conteúdo completo no Notion antes de qualquer teste envolvendo login via gov.br. É a mesma pauta do item de backlog "Permitir login cidadão utilizando conta Gov.br" — confirmar se já foi implementada ou ainda é planejamento
- [ ] Regra de "usuário único entre ambientes" (switch cidadão↔servidor): confirmar o comportamento de convite quando o cidadão já tem conta e passa a atuar em mais de uma prefeitura — o texto descreve o fluxo mas não os detalhes de tela/validação
- [ ] Ajustes de copy da etapa de e-mail/senha (cadastro externo sem pré-cadastro) remetem a "verificar protótipos" no Figma — não conferido aqui
- [ ] **Edição de cadastro pelo servidor não está documentada.** A seção "Cadastro interno da pessoa jurídica (feito por um servidor)" acima cobre os **campos de criação**, mas não a **edição de um cadastro já existente** — em especial a **confirmação por senha do usuário atual** que o sistema pede pra alterar o e-mail, e qual o retorno esperado quando essa senha está incorreta. Lacuna encontrada no gate de doc da [[QA Workspace/02 Demandas/DEV/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]] (03/08/2026, servidor editando cidadão PJ, reproduz em DEV e homologação). Respaldo hoje é **analogia** com o [[QA Workspace/04 Conhecimento/Módulos/Login|Login]], que documenta mensagem de erro pra credencial inválida — não regra escrita pra esta tela
- [ ] **A tentativa de senha na edição de cadastro conta pro bloqueio por 5 erros?** O [[QA Workspace/04 Conhecimento/Módulos/Login|Login]] registra que 5 senhas erradas bloqueiam a conta em todos os ambientes. A senha pedida nessa tela é a do **próprio servidor**, então, se contar, ele bloqueia a **conta de trabalho** sem receber aviso nenhum (ver [[QA Workspace/02 Demandas/DEV/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]]). Decisão de produto pendente — documentar a regra quando vier
- [ ] **O mesmo silêncio acontece nas superfícies vizinhas?** Só foi observado o servidor editando um cidadão **PJ**. Faltam: servidor editando um cidadão **PF**, e o **cidadão alterando o próprio e-mail** (meu perfil). Se acontecer nas três, o defeito é da **etapa de confirmação por senha**, não do fluxo PJ
- [ ] **A validação de e-mail duplicado nessa tela dá feedback?** O e-mail institucional é **único no sistema** (regra acima). Se a tela engole o erro de senha, vale confirmar se engole também o de duplicidade — seriam sintomas do mesmo tratamento de erro, não duas falhas

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- 
