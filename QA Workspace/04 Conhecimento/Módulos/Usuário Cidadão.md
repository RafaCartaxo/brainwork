---
title: Usuário Cidadão
tags:
  - qa
  - conhecimento
  - sogov
  - usuario-cidadao
tipo: modulo
revisado: 2026-10-14
fonte: https://app.notion.com/p/alfa-group/Usu-rio-Cidad-o-15050c52ecbf40eca2e35e5ca6576b65
fonte_criado: 2024-09-17 (Alice Martins)
fonte_ultima_edicao: 2026-09-16 (Edu)
---
# Usuário Cidadão

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. O export veio com ruído (imagens, propriedades do Notion) removido preservando as regras. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].
> **Atualizado em 2026-10-14** com reexport mais recente do Notion: a feature "Acesso via gov.br" (antes só título, agora completa) + quatro atualizações novas (requisitos de senha no reenvio, confirmação de e-mail na Central de Atendimento, autenticação de assinatura pós-retificação, download compactado SGV-10076). Conteúdo de Departamentos/PJ (SGV-8883/8884/9898, 14/07/2026) ficou documentado em [[QA Workspace/04 Conhecimento/Módulos/Usuário Servidor|Usuário Servidor]], que veio no mesmo lote — ver lá.

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

### Feature — Acesso do cidadão (Pessoa Física) via gov.br (02/07/2026)
> Permite que o cidadão PF entre no SoGov usando a conta gov.br, tanto pra se cadastrar (sem conta ainda) quanto pra acessar (já tem conta) — reduz o esforço do primeiro acesso aproveitando a identidade que o gov.br já confirma. Só PF (gov.br não cobre PJ).

**Regras gerais**
- Uma conta por CPF — o CPF decide o caminho: conta existente → login; sem conta → cadastro.
- Decisão automática no retorno do gov.br (login ou cadastro, só pelo CPF, sem o usuário escolher).
- Nome completo e CPF vêm confirmados do gov.br e **não são editáveis**.
- Senha é criada mesmo entrando pelo gov.br, e passa a valer como forma alternativa de acesso (CPF + senha).
- Conta só é criada ao **concluir** — cancelar/abandonar a tela de completar cadastro não deixa registro pela metade; numa próxima tentativa, reabre a mesma tela com os dados repreenchidos.

**Ponto de entrada**: botão gov.br na tela de login, na área "Ou acesse via" (abaixo do botão "Entrar") — desktop e mobile.

**Cenários**:
1. **Sem cadastro, primeiro acesso via gov.br**: autentica no gov.br → autoriza uso dos dados → volta sem conta no SoGov → abre "Complete seu cadastro" (dados confirmados + campos pré-preenchidos) → preenche senha, aceita termos, "Concluir e acessar plataforma" → tela de carregamento → e-mail de conta criada → entra já logado.
2. **Já tem conta no SoGov**: autentica no gov.br (primeira vez) → sistema vincula automaticamente pelo CPF, **sem tela de confirmação** → e-mail de aviso da vinculação (é o mecanismo de transparência do vínculo automático) → entra já logado. Acessos seguintes: direto, sem telas intermediárias.
3. **Alternativo — autorização negada**: cidadão clica "Negar" no gov.br → tela "Cadastro pelo gov.br não autorizado" → "Tentar novamente com o gov.br" ou "Fazer cadastro" (fluxo padrão).
4. **Exceção — erro de autenticação** (gov.br fora do ar ou erro 500): tela "Não foi possível concluir a autenticação" → "Tentar novamente" ou "Voltar para a tela de acesso".
5. **Alternativo — cancelamento**: em "Complete seu cadastro", clica "Cancelar" → modal "Ao cancelar, todas as informações inseridas serão descartadas. Deseja mesmo cancelar seu cadastro?" → confirma → nada é salvo, volta pro login.

**Tela "Complete seu cadastro"**:
- Não editável: Nome completo; CPF mascarado (asteriscos nos 3 primeiros e 2 últimos dígitos, ex. `*.275.714-**`).
- Pré-preenchido (editável): Nome de exibição (dois primeiros nomes do gov.br); E-mail (do gov.br — apagar mostra placeholder de exemplo).
- A preencher: Senha + confirmação (mesmos requisitos/componente do fluxo de recuperação de acesso); aceite de dados + maioridade (mesmos componentes do fluxo de assinatura por token/link — sem aceitar, alerta "Para continuar, você precisa aceitar os termos abaixo").

**Notificações**: e-mail "Conta criada com sucesso via gov.br" (boas-vindas, não confirmação — já vem verificado pelo gov.br); e-mail "Conta gov.br conectada a uma conta SoGov existente" (comunica o vínculo automático, já que não há tela de confirmação).

### Refatoração de componentes de requisito de senha ao solicitar reenvio de senha (22/07/2026)
> Corrige o bug "Redefinição de senha não exibe mensagem de erro quando a senha não atende aos critérios de segurança" (PF, PJ e Servidor — desktop e mobile).

- Critérios de senha: 1 maiúscula, 1 minúscula, 1 número, 1 caractere especial (`! @ # $ % ^ & *`), mínimo 8 caracteres.
- Botão "Finalizar" só habilita com **todos** os critérios atendidos.
- Feedback em tempo real: requisito atendido vira verde com check; não atendido fica neutro com ícone close.
- Clicar em Finalizar com senha incompleta → requisitos não atendidos ficam **vermelhos**.
- Iconografia (check/close) além de cor — acessibilidade pra daltonismo.
- Cabeçalho identifica o usuário: PF mostra nome completo + CPF anonimizado; PJ mostra razão social + CNPJ + nome do responsável legal.
- Usuário sempre chega nesse fluxo pelo link de e-mail (recuperação); ao concluir (qualquer perfil), vai pra página de sucesso com contagem regressiva de redirecionamento.
- Link expirado → tela de aviso com botão "Reenviar solicitação" (gera novo link).
- Paridade total desktop/mobile em todos os fluxos (PF, PJ, sucesso, link expirado).

### Confirmação de e-mail — Central de Atendimento
> ⚠️ Esta seção aparece no Notion sob o título **"Mudança de e-mail servidor"**, mas o conteúdo é sobre a Central de Atendimento (ambiente cidadão) — provável erro de título/organização na página de origem. Mantive o conteúdo como veio, sinalizado em Dúvidas em aberto.

- Alert de e-mail pendente de confirmação, na Central de Atendimento, ganha **ação de reenvio direto no próprio componente** (antes só direcionava pra tela de confirmação, sem reenviar ali).
- Copy nova: "Atenção: Confirme seu e-mail para ter acesso completo aos serviços. Reenviar e-mail de confirmação".
- Clicou em reenviar → dispara o e-mail, alert muda pra estado **Temporizador**: "Aguarde 59s para um novo envio" (contagem regressiva por segundo); reenvio fica indisponível durante a contagem; ao zerar, volta ao estado Default.
- Flash message "✓ E-mail de confirmação enviado!" aparece junto com a transição pro Temporizador (feedback imediato; o temporizador reforça de forma persistente).
- E-mail transacional de confirmação: disparado tanto na **alteração** de e-mail (pro novo endereço) quanto no **primeiro cadastro**. Copy atualizada: título "Confirme seu novo e-mail de acesso!" (antes "Novo e-mail de acesso!"); parágrafo ajustado pra deixar claro que a confirmação é condição pro e-mail valer.

### Autenticação de assinatura (15/09/2026)
> Comportamento da verificação de autenticidade quando um documento assinado é retificado depois — via link do PDF ou via hash (consulta manual na página de verificação).

- **Regra 1 — retificação invalida assinaturas existentes**: documento retificado após já ter assinatura(s) → assinaturas anteriores perdem validade (vale pros dois tipos de acesso); verificação exibe mensagem (prototipada no Figma) avisando que não são mais válidas por causa da retificação.
- **Regra 2 — nova assinatura após retificação**: se o documento é assinado de novo após a retificação, a consulta de autenticidade mostra um indicativo **diferente** da Regra 1 — informa que o documento foi retificado no ambiente externo do cidadão (aparece nos dois fluxos: busca manual por hash e acesso direto pelo link).

### Disponibilidade de download da versão compactada para o cidadão (SGV-10076, 16/09/2026)
> [MELHORIA-CX] · Cliente: Prefeitura Municipal de Guarabira · Chamado #0726-000283 · Ambiente Cidadão · Componente: toolbar-cidadao → "Baixar documento". O download compactado (.zip, documento separado por partes) já existe e está consolidado no **ambiente servidor** — aqui a demanda é estender ao ambiente cidadão, mantendo o completo.

- "Baixar documento" na toolbar do cidadão vira um **menu com dropdown** de 2 opções, nessa ordem: "Baixar documento completo" (comportamento atual, arquivo único) e "Baixar documento compactado" (.zip, documento separado por partes — mesmo serviço de compactação do ambiente servidor, sem regra própria pro cidadão).
- O .zip respeita as permissões de visualização do cidadão — nada que ele não possa ver na tela entra no pacote.
- Única mudança na toolbar é esse menu — os demais itens (Histórico, Cancelar solicitação, Responder) seguem as regras de exibição/habilitação por status de tramitação já existentes, sem alteração.
- Ambos os downloads usam a **bolha de downloads** já existente no top-header — mesma interação, aviso de conclusão e persistência; sem tratamento próprio pro .zip.
- Falha ao gerar o .zip → informa o usuário, mantendo o documento acessível pelo download completo.
- Responsabilidade de escopo: o comportamento do compactado foi levantado/validado pelo CX junto ao cliente — a tradução da necessidade do contribuinte é responsabilidade do CX solicitante; o design entrega exatamente o que foi pedido.

## Backlog da página (Notion)

- [Melhoria] Permitir cadastro de cidadão Pessoa Jurídica sem vincular dados do responsável legal;
- ~~*Permitir login cidadão utilizando conta Gov.br~~ — **implementado**, ver seção "Feature — Acesso via gov.br" acima;
- ~~[BUG-CX] Redefinição de senha não exibe mensagem de erro quando a senha não atende aos critérios de segurança~~ — **corrigido**, ver seção "Refatoração de componentes de requisito de senha" acima;
- [Melhoria] Fluxo para contornar situação de e-mail incorreto cadastrado do cidadão — sem SGV, pode relacionar com o gap de edição de e-mail já registrado em Dúvidas em aberto ([[QA Workspace/02 Demandas/Concluídas/10549/QA/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]]);
- Export mostra só 4 itens + "2 more…" — os demais não foram vistos.

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] Regra de "usuário único entre ambientes" (switch cidadão↔servidor): confirmar o comportamento de convite quando o cidadão já tem conta e passa a atuar em mais de uma prefeitura — o texto descreve o fluxo mas não os detalhes de tela/validação
- [ ] A seção "Confirmação de e-mail — Central de Atendimento" está sob o título **"Mudança de e-mail servidor"** no Notion — título e conteúdo não batem (conteúdo é claramente do ambiente cidadão/Central de Atendimento). Confirmar com quem escreveu se foi erro de organização da página ou se há conteúdo de servidor que deveria estar ali e se perdeu.
- [ ] Sub-item do Notion ligado a esta página, não importado: "[USUÁRIO CIDADÃO] Gerenciamento de cidadãos vinculados a um workspace: listagem, visualização e afins".
- [ ] Ajustes de copy da etapa de e-mail/senha (cadastro externo sem pré-cadastro) remetem a "verificar protótipos" no Figma — não conferido aqui
- [ ] **Edição de cadastro pelo servidor não está documentada.** A seção "Cadastro interno da pessoa jurídica (feito por um servidor)" acima cobre os **campos de criação**, mas não a **edição de um cadastro já existente** — em especial o fato de que, pra alterar o e-mail, o sistema pede **primeiro a senha do usuário atual (o servidor)** e só **depois** libera o campo de e-mail. A senha é **porta de entrada** do fluxo, não confirmação no final; e o retorno esperado quando ela está incorreta não está definido em lugar nenhum. Lacuna encontrada no gate de doc da [[QA Workspace/02 Demandas/Concluídas/10549/QA/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]] (03/08/2026, servidor editando cidadão PJ, reproduz em DEV e homologação). Respaldo hoje é **analogia** com o [[QA Workspace/04 Conhecimento/Módulos/Login|Login]], que documenta mensagem de erro pra credencial inválida — não regra escrita pra esta tela
- [ ] **A tentativa de senha na edição de cadastro conta pro bloqueio por 5 erros?** O [[QA Workspace/04 Conhecimento/Módulos/Login|Login]] registra que 5 senhas erradas bloqueiam a conta em todos os ambientes. A senha pedida nessa tela é a do **próprio servidor**, então, se contar, ele bloqueia a **conta de trabalho** sem receber aviso nenhum (ver [[QA Workspace/02 Demandas/Concluídas/10549/QA/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]]). Decisão de produto pendente — documentar a regra quando vier
- [ ] **O mesmo silêncio acontece nas superfícies vizinhas?** Só foi observado o servidor editando um cidadão **PJ**. Faltam: servidor editando um cidadão **PF**, e o **cidadão alterando o próprio e-mail** (meu perfil). Se acontecer nas três, o defeito é da **etapa de confirmação por senha**, não do fluxo PJ
- [ ] **A validação de e-mail duplicado nessa tela dá feedback?** O e-mail institucional é **único no sistema** (regra acima), e essa é a validação do passo **seguinte** — depois que a senha libera o campo. Se a tela engole o erro de senha, vale confirmar se engole também o de duplicidade: seriam sintomas do mesmo tratamento de erro, não duas falhas

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- **SGV-10076** — download compactado pro cidadão (16/09/2026, ver seção própria).
- [[QA Workspace/02 Demandas/Concluídas/10549/QA/10549 - Bug Senha Incorreta Nao Retorna Feedback Na Alteracao De E-mail Do Cidadao PJ|SGV-10549]] — já citado em Dúvidas em aberto.

## Referências
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Usuário Servidor|Usuário Servidor]] — Departamentos/PJ (SGV-8883/8884/9898, 14/07/2026) e a regra de usuário único entre ambientes, pelo lado servidor.
- [[QA Workspace/04 Conhecimento/Módulos/Usuário Sogo|Usuário Sogo]] — o terceiro tipo de usuário do sistema.
