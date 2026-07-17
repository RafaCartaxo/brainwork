---
title: Fluxo de trabalho (Workflow)
tags:
  - qa
  - conhecimento
  - sogov
  - workflow
tipo: modulo
revisado: 2026-07-17
fonte: https://app.notion.com/p/alfa-group/Fluxo-de-trabalho-Workflow-4773d79eb5dc457da4582f05b4527f51
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-07-08 (Fernando Junior)
---
# Fluxo de trabalho (Workflow)

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-17 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. O export veio com ruído (imagens, âncoras) que foi limpo preservando as regras; várias seções de atualização vieram **só como título** (ver [[#Dúvidas em aberto]]). Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

## Definição geral

Workflow é a funcionalidade para criar fluxos pré-definidos para módulos, serviços ou assuntos, em formato de **etapas**, virtualizando o ritual físico dos órgãos (ex.: solicitação de pagamento → finanças → nota fiscal do fornecedor → conferência → tesouraria empenha/liquida/paga). O fluxo pode retroceder etapas (ex.: NF com problema) e segue até a última etapa.

Nas etapas podem ser inseridas configurações específicas: despachos com campos personalizados, prazos, assinaturas obrigatórias etc.

> [!warning] Restrição de tipo
> Só é possível configurar workflow para a natureza/tipo de documento **Processo Administrativo**.

## Liberando uso de workflow para clientes

- A liberação é feita no **ambiente administrativo SOGO**, na edição do cliente (gerenciamento de clientes).
- A **primeira ativação** é feita no ambiente técnico SOGO (área de Gerenciamento de Workflow); depois dela o menu Workflow passa a aparecer no ambiente do cliente.
- No ambiente técnico existem **modelos de workflow** que podem ser vinculados a clientes (como módulos): customizáveis pontualmente na instância sem perder vínculo com o modelo principal.

### Ativar / desativar / suspender no cliente

| Ação | Efeito |
|---|---|
| **Ativar** | Escolhe quais módulos do cliente poderão configurar workflow; menu aparece pro cliente |
| **Desativar** | Pode ser feito a qualquer momento sem aviso; só impacta documentos novos (em tramitação seguem com suas etapas); módulos **perdem a configuração definitivamente** (não restaura); menu some |
| **Suspender** | Idem desativar, mas a configuração **não é perdida** — removendo a suspensão tudo volta ao estado anterior; menu some enquanto suspenso; cliente suspenso não tem opção de desativar (precisa remover a suspensão antes) |

Permissão: qualquer usuário SOGO com permissão de cadastrar/editar cliente.

## Criando e gerenciando workflows

Criação e gerenciamento podem ser feitos **na instância do cliente** ou **no ambiente técnico SOGO**.

### Usuários com permissão

| Ambiente | Quem | Escopo |
|---|---|---|
| Técnico SOGO | Adm SOGO | Todos os clientes |
| Técnico SOGO | Técnico SOGO | Clientes da sua carteira |
| Cliente | Adm SOGO / Técnico SOGO | Todos / carteira |
| Cliente | Adm Servidor | Todos os setores da instância |
| Cliente | Adm setorial | Só setores da sua hierarquia (listagem/edição e criação limitadas a módulos/assuntos/serviços da hierarquia) |

### Criando workflow (ambiente cliente)

Mínimo necessário: **Módulo** (obrigatório) + **Assunto ou serviço** (obrigatório*) + **no mínimo 2 etapas**.

> [!note] *Módulo sem serviço/assunto: workflow pode ser criado direto no módulo. Se o módulo **tem** assuntos/serviços, só é possível criar a nível de assunto/serviço. Se um módulo com workflow ganhar serviço/assunto no futuro, o usuário é avisado na criação de que o workflow do módulo será **desativado**.

## Etapas

Dois modos de inserção — simples e avançado.

### Modo avançado

- **Descrição geral**: nome (obrigatório) + descrição (opcional);
- **Regras de tramitação** (abaixo);
- **Despachos customizados** (opcional).

### Regras de tramitação da etapa

- **Setor responsável pela etapa** (obrigatório):
	- *Setor específico* — listado conforme regras de tramitação herdadas do módulo/serviço/assunto; ao avançar, não pede destinatário (vai automático);
	- *Setor especificado na hora de avançar* — na tramitação, só é possível setar **um** setor de encaminhamento (vira o responsável); esse setor pode envolver outros na demanda.
- **Setores que podem participar da etapa** (obrigatório) — default: todos da regra de tramitação do módulo/serviço/assunto (deselecionáveis, mínimo um). Na tramitação, só age na etapa quem está envolvido nela, e só podem ser envolvidos os setores desta regra.
- **Setores que podem apenas visualizar** (opcional) — subconjunto dos participantes; não podem ser destino de avanço, só envolvidos via despacho/comentário.
- **Setores que podem avançar ou retroceder** (obrigatório) — default: todos os participantes.
- **Setores que podem encerrar na etapa** (obrigatório) — encerram o fluxo inteiro mesmo sem ser a última etapa; default: todos os participantes. Refinável por **nível** (Administrador, Adm setorial, N1, N2) e por **servidores específicos** (opcionais).

> [!note] Herança e embutidos
> Sem serviço/assunto → regras herdadas do módulo; com serviço/assunto → herdadas dele. O **setor dono** do documento e o **setor responsável pela etapa** estão sempre "embutidos" nas regras, mesmo não selecionados.

### Modo simples

Só nome (obrigatório), descrição (opcional) e setor responsável (obrigatório, mesmas regras do avançado). Por debaixo dos panos, participar/avançar-retroceder/encerrar já vêm pré-configurados com a herança do módulo/serviço/assunto.

### Editando uma etapa

Tudo é editável (etapa simples pode ganhar configuração avançada na edição).

> [!warning] Edição durante tramitação em andamento
> Não é permitido editar os setores envolvidos na etapa atual (nem participantes, nem setores de ações personalizadas). **Regra geral: edição só vale pra documentos novos** — documentos em tramitação seguem as regras antigas. Se a edição afetar etapa anterior e o responsável dela sair das regras: o nome antigo continua exibido; se retrocederem pra ela, pede-se novo encaminhamento dentro da nova regra (ou vai automático, se a edição setou responsável específico).

## Despachos customizados

Artefatos que dão robustez à etapa: uma vez inseridos, **tornam-se obrigatórios** — a etapa só avança quando o despacho for emitido (sem ele, só retroceder ou encerrar).

Configuração obrigatória:

- **Nome do despacho** — exibido na criação durante a tramitação (como despacho de revogação/retificação);
- **Setores que podem emitir** — dentre os participantes da etapa (default: todos, incluindo o responsável). Retirar um setor envolvido numa ação personalizada "quebra" a configuração (deve ficar explícito).

Regras na tramitação:

- Com "Outros setores podem emitir este despacho": setor dono e responsável da etapa também podem emitir;
- Destinatários possíveis: só participantes da etapa;
- Com múltiplos despachos configurados, o botão da toolbar vira menu (despacho normal + customizados); emitidos saem da lista; evento da etapa atualiza;
- O despacho segue a numeração sequencial da timeline e a estética original (incluindo config de sigilo do módulo/serviço/assunto).

### Assinaturas no despacho customizado

Solicitadas **após a emissão** do despacho. Configuração:

- **Setor** (obrigatório) — específico (dos participantes) ou "setor que emitiu o despacho";
- **Nível de permissão** (opcional) — sem nível, segue a regra geral do SoGov;
- **Servidor** (opcional) — dos setores/níveis selecionados; sem nível definido, retorna todos os que podem assinar;
- **Papel do signatário** (opcional) e **Tipo de assinatura** (obrigatório) — padrão SoGov ([[Assinaturas]]);
- **Locais** (obrigatório) — Despacho, Anexos do despacho, campos tipo arquivo personalizados.

> [!note] Locais "Anexos do despacho": o signatário escolhe qualquer um/todos os anexos, mas assina **pelo menos um**. Sem essa opção, anexo ainda pode ser assinado avulso.

- Suporta múltiplas solicitações e estrutura **sequencial** (padrão SoGov);
- Se a assinatura configurada é do próprio emissor, ele já é remetido pra assinar logo após emitir;
- Solicitação para setor (sem servidor específico): CTA de assinar fica disponível pra qualquer servidor dentro das regras.

## Prazo para etapas

Define-se a **quantidade de dias** da etapa (disponível na listagem de etapas).

Regras principais:

- Módulo/assunto/serviço com prazo: a **soma dos prazos das etapas** deve caber no prazo total configurado;
- Documento sem prazo de módulo/assunto/serviço mas com prazos de etapa: prazo do documento deve respeitar o mínimo da soma das etapas **restantes** (ex.: 3 etapas restantes de 2 dias → mínimo 6 dias a partir da inserção);
- O prazo da etapa **conta a partir do início dela** e **pausa** ao avançar/retroceder; voltando à etapa, retoma de onde parou;
- Documento com prazo vencido entrando em etapa com prazo: o prazo da etapa é **substituído** pelo do documento, com sinalização;
- O prazo da etapa é o prazo do **setor responsável pela etapa**; se o setor já tinha prazo, a header mostra o mais próximo de vencer; resolvido um, o outro entra em vigor;
- Etapas concluídas: prazo não pode mais ser alterado/inserido;
- Documento **pausado** durante etapa com prazo → prazo da etapa pausa;
- Ao **retroceder**: prazos da etapa retrocedida não podem mais ser alterados; pode-se adicionar prazo pra etapas futuras; se a data já passou, fica **atrasada**;
- Na aba de prazos, dá pra adicionar/editar prazos de etapas sem prazo configurado (só etapa atual e próximas);
- **Prazo de assinatura da etapa**: um só, vale pra todas as assinaturas solicitadas na etapa atual.

Permissões de prazo:

| Ação | Quem |
|---|---|
| Adicionar | Setor dono: etapa atual e demais; Setor responsável: só a etapa atual dele (etapa e assinatura) |
| Editar | Prazo definido pelo dono → responsável pode editar; definido pelo responsável → dono pode editar |

## Gerenciamento de workflow

Menu com listagem de todos os workflows da instância: ordenação (default: mais recente criado/editado primeiro), filtros (módulo, serviço/assunto, status) e busca integrada aos filtros.

Item da listagem: módulo, serviço/assunto, status, data/hora da última atualização, menu de ações.

### Status e ações

Status possíveis: **Rascunho, Ativo e Inativo**.

| Status | Ações disponíveis |
|---|---|
| Rascunho | Ativar · Excluir · Duplicar · Editar · Histórico |
| Inativo | Ativar · Excluir · Duplicar · Editar · Histórico |
| Ativo | Inativar · Duplicar · Editar · Histórico |

### Impacto das ações

- **Inativar / Excluir / Editar**: documentos com fluxo não finalizado **não são impactados**; só documentos novos (deixam de seguir fluxo, ou seguem a versão editada);
- **Duplicar**: sem impacto no original (não pode existir mais de um fluxo por módulo/assunto/serviço).

### Duplicar fluxo de trabalho

- Precisa configurar módulo/serviço/assunto novo (só listam os **sem** fluxo configurado);
- Módulo pode reaparecer na lista se tiver assuntos/serviços ainda sem fluxo;
- Se nada do módulo original está livre, campo módulo vem vazio;
- **Herdado**: prazos (se o prazo do destino é o mesmo, ou se destino não tem prazo a respeitar; senão resetam), etapas (com sugestão de revisar regras de tramitação), regras de tramitação default;
- **Perdido**: despachos e assinaturas configurados — etapas que os tinham ficam sinalizadas como pendência;
- Duplicado entra no topo da listagem como **rascunho**; duplicar é possível em qualquer status.

### Histórico

Cada workflow tem histórico de modificações: quem editou, data/hora e lista do que foi editado (criação, reordenação/duplicação/adição/exclusão de etapa, mudança de status, edições de prazo e despachos).

### Editando um fluxo de trabalho

- Editável em qualquer status, mas **mudar módulo/assunto/serviço só em rascunho ou inativo**;
- Ao mudar módulo/assunto/serviço: regras de tramitação resetam pro padrão novo (perde personalização); prazos seguem a mesma regra da duplicação; despachos/assinaturas configurados se perdem (etapas sinalizadas);
- Salvar com pendências → vira **rascunho**; **só ativa sem pendências**.

## Fluxo de trabalho na tramitação

### Criação de documento

Documento com workflow **não tem** campos "setor destinatário" e "servidor responsável" — o encaminhamento é o início do fluxo (1ª etapa já define o responsável).

### Documento já criado

- O fluxo **não inicia automático** — usuário com permissão precisa iniciar; **somente o setor dono pode iniciar**;
- Etapas são exibidas dentro do documento (atual, faltantes, configurações); sinalização da etapa atual, setor responsável e prazo;
- Ações disponíveis só pra quem tem permissão e participa da etapa atual;
- Criador que não é dono (direcionamento automático) fica só como envolvido — toolbar diferente (igual pros setores "em cópia").

### Ações obrigatórias

- Sinalizadas no evento principal da etapa; precisam ser cumpridas pra avançar;
- Despachos específicos: botão vira menu; emitidos saem da lista; evento atualiza;
- Assinaturas de despachos customizados: CTA no evento pra quem pode assinar; evento atualiza ao assinar.

### Status do documento

- Encerrado com workflow pode ser **reaberto, mas o fluxo não volta a acontecer**;
- Em tramitação com fluxo não iniciado → toolbar diferente pro dono;
- **Pausado/Encerrado**: eventos da timeline sem comentar/responder (vale também pra docs sem workflow);
- Encaminhamento automático (não-dono): envolvidos o tempo inteiro, toolbar normal.

### Avançar e retroceder

- Retroceder gera **evento principal na timeline com justificativa**;
- Avançar/retroceder **só pela toolbar**;
- Só avança cumprindo todas as ações obrigatórias;
- **Setor dono sempre pode** avançar e retroceder;
- Retrocedendo, o que já foi feito nas ações obrigatórias **não se perde**;
- **Só retrocede uma vez** a partir de onde está (da 5 pra 4; na 4, só avança) — e depois de um retrocesso, ninguém mais retrocede.

### Prazos na tramitação

Documento com workflow **não tem** prazo de revisão nem de documento. Existem: prazo oficial (se configurado pro tipo), prazo das etapas (configurado antes → não editável; não configurado → pode adicionar na tramitação) e prazo de assinatura (só na etapa atual com solicitação pendente; único pra todas as assinaturas da etapa; não pode ser maior que o da etapa; se a etapa não tem prazo, o da assinatura vira o dela também). Permissões: as mesmas do drawer de prazos; só edita prazos não cumpridos.

### Filtros

Na mesa deve existir filtro por documentos que possuem fluxo de trabalho ([[Mesa de trabalho#Regras de filtros|filtros da Mesa]]).

## Outras regras

- **Só 1 workflow por assunto ou serviço**;
- **Retificação**: ~~documento com workflow só pode ser retificado na primeira etapa, e antes de concluí-la~~ **REGRA REVOGADA** em ~08/07/2026 — retificação passou a ser permitida **em qualquer etapa**, com reinício do fluxo. Ver [[#Retificação de documento em qualquer etapa (~08/07/2026)]];
- Workflow em edição: sinalizado na listagem; ao concluir, notificação pra usuários com permissão do cliente (o que mudou e em que etapa);
- **Setor dono não perde seus poderes** sobre o documento durante toda a tramitação, mesmo com responsáveis por etapa;
- Na header do documento o responsável exibido é sempre o **setor dono**; o responsável da etapa aparece só nos steps;
- **N2 do setor dono não pode mais encerrar tramitação — vale para todo o SoGov**.

## Permissões extras (funcionalidade)

8 permissões: **Visualizar** (menu + listagem sem ações), **Cadastrar** (botão novo fluxo), **Editar**, **Ativar**, **Inativar**, **Excluir**, **Duplicar**, **Histórico** (cada uma libera a respectiva opção no menu do item).

## Configurações do órgão

Uma permissão única — **Visualizar e editar**: libera no menu profile a opção de configurações do órgão (edição de cores e imagens).

## Perguntas ainda sem resposta (da própria doc)

- O que acontece se o módulo, serviço ou assunto de um flow for editado/inativado? → **parcialmente respondido** no e-mail 03/07/2024 (pergunta 8): inativar módulo do cliente não afeta o workflow; desvincular módulo → fluxos vão pra rascunho com popup + notificação aos admins; inativar assunto/serviço com fluxo → bloqueado até atribuir o fluxo a outro;
- E se um setor envolvido num flow for desativado? *(sem resposta; correlato: signatário de despacho customizado que sai do setor/é desativado → "continua pendente", e-mail 03/07/2024)*;
- Envolvidos em etapas anteriores poderão acompanhar as etapas seguintes (modo visualizar)?
- Com responsável = "setor selecionado na hora de avançar", como será essa seleção na tramitação?

## Atualizações pós-entrega

### E-mail 03/07/2024 (dúvidas Virtus × respostas SOGO)

Decisões que viraram regra:

- **Módulo não muda mais de tipo**: uma vez criado e ativado, módulo nunca mais tem o tipo de documento alterado (mesmo voltando pra rascunho) — parâmetros de tipo ficam `disabled` na edição (regra geral, inclusive processo urbanístico);
- **Desvincular módulo do cliente com workflows**: popup avisa → confirmando, fluxos vão pra **rascunho** + notificação aos administradores do cliente; campos módulo/serviço/assunto ficam vazios na edição; documentos em tramitação continuam normalmente;
- **Inativar assunto/serviço com fluxo**: bloqueado — popup informa que até atribuir o fluxo a outro serviço/assunto a inativação não pode ser feita;
- **Inativar módulo do cliente**: nada acontece com o workflow (só não cria mais documentos do módulo);
- **Suspensão da feature após editar configurações**: módulos adicionados permanecem; o que foi excluído permanece excluído mesmo suspendendo;
- **Ativar workflow pro cliente**: só na **edição** do cliente (não na criação); ao habilitar o toggle, é **obrigatório** associar módulos;
- **Tag de fluxo de trabalho** em serviços/assuntos: só aparece quando o fluxo está **ativo**;
- **Card da etapa**: não é todo clicável — edição só pelo meatball;
- **"Outros setores podem emitir este despacho"**: setores não vêm pré-selecionados, ficam disponíveis pra seleção;
- **"Setor que emitiu o despacho"** (assinaturas): não é item fixo de seleção — pesquisa-se como os demais setores;
- **Signatário de despacho customizado que sai do setor / é desativado**: a solicitação **continua pendente**;
- **Campos de despacho personalizado**: podem ter lógica; campo de arquivo pode requerer aprovação; campos de referência seguem as regras do formulário do documento;
- **Cidadão não visualiza as etapas** do fluxo;
- **Não é possível encerrar um fluxo sem ele ter sido iniciado**;
- **Iniciar o fluxo**: setor dono **e também o responsável da etapa**, quando já definido na configuração;
- **Layout "com cópia"**: vale pra todos os despachos, não só o customizado;
- **Retroceder não cancela eventos**: pendências da etapa continuam pendentes e só podem ser feitas quando avançar de novo pra ela;
- **Pessoa que encaixa em dois critérios de assinatura**: assina **uma vez** — prioridade: solicitação direta pra pessoa > pro setor;
- **Editar regras de tramitação do módulo/assunto/serviço retirando setor que é responsável de etapa ou tem ação obrigatória em workflow**: bloqueado com aviso — precisa antes retirar o setor das regras do workflow;
- **Permissões default**: Workflow → Administrador e Adm setorial (módulos/setores da hierarquia); Configurações do órgão → Administrador;
- **3 níveis de inadimplência** no filtro de clientes estão corretos (alerta + limitação N1 + limitação N2).

### Texto padrão no campo texto grande de despacho personalizado (04/02/2026)

- Configuração **exclusiva da etapa** onde o despacho foi inserido (sem herança de módulo/assunto/serviço);
- Componente de texto com posicionamento e grid iguais aos campos de formulário padrão;
- O texto padrão só aparece quando o processo atinge a etapa configurada;
- Configuração: cluster "Exemplo de Preenchimento" com botão pra cadastrar o conteúdo; tooltip contextualiza; texto salvo reflete no desenho do fluxo; botão Salvar inicia desabilitado (habilita ao alterar); exclusão exige popup de confirmação;
- Usuário final: campo já vem preenchido ao despachar; pode apagar/editar/complementar; a edição vale **só naquele processo** (não altera o modelo);
- Logs no histórico do fluxo: cadastro, edição e exclusão do texto base (indicando a etapa);
- **Restrições do campo texto grande** no despacho personalizado: obrigatório (não desmarca), sem repetição, sem exclusão, sem lógica.

### "Selecionar Todos" nas configurações de etapa (17/04/2026)

Checkbox de seleção global nos campos: setores que podem participar, avançar/retroceder, encerrar e apenas visualizar. Segue o padrão de "selecionar todos" já estabelecido no sistema.

### Atalhos de etapas (27/05/2026)

Quebra a tramitação estritamente linear: cada etapa pode ser configurada com **atalhos** pra saltar pra etapas futuras ou retornar a anteriores de forma não linear (ex.: 8 → 3, 2 → 5).

- **Configuração** (criação avançada e edição da etapa): select múltiplo "Permitir atalhos entre as seguintes etapas (opcional)", listando as etapas do serviço/assunto (a etapa atual vem desabilitada/oculta); exibe `$etapa - $nomeDaEtapa` com seleção em massa;
- **Direção livre**: atalho progressivo (avanço) e retroativo (recuo);
- **Escopo isolado por etapa**: atalho da etapa A pra C não vale pra B; sem atalhos configurados, vale o comportamento linear padrão;
- **Reposicionamento de etapas reseta atalhos**: as etapas reposicionadas perdem seus atalhos (reset de origem) e as que apontavam pra elas também (reset de destino), com alerta ao administrador antes de confirmar — previne atalhos obsoletos;
- Rastreabilidade via novos eventos de sistema.

> [!warning] Impacto nas regras base
> Os atalhos relativizam as regras "só retrocede uma vez" e "avançar/retroceder etapa por etapa" da doc original — em etapas com atalho configurado, o movimento é o do atalho. Regra antiga permanece pro caso sem atalhos.

### Retificação de documento em qualquer etapa (~08/07/2026)

> [!important] Regra anterior REVOGADA
> "Documento com workflow só pode ser retificado na primeira etapa e se ele não tiver concluído ela ainda" **deixa de existir**. A retificação passa a ser permitida em **qualquer etapa**, equiparando documentos com fluxo aos sem fluxo. Motivação: a necessidade de retificação raramente é identificada na 1ª etapa, sobretudo em documentos de abertura externa.

**Permissões** (mesmas da retificação geral): N1, Administrador ou Adm setorial do **setor dono**; N2 só retifica documentos criados por ele mesmo.

**Restrição por etapa (despachos)**: fora da etapa atual, "Retificar despacho" e "Cancelar despacho" ficam desabilitados no meatball (precisa estar na etapa). Distinta da retificação do documento, que é via toolbar.

**Comportamento central — reinício do fluxo**:

- Retificou em qualquer etapa → o fluxo **retorna integralmente pra 1ª etapa**;
- **Todos os eventos do fluxo anteriores à retificação são invalidados (anulados)** — os atos administrativos sobre a versão anterior perdem efeito e o ritual refaz sobre o documento corrigido.

**Fluxo do usuário**:

- *Via toolbar* ("Retificar documento"): popup de confirmação — *"Ao retificar este documento, ele retornará a sua primeira etapa e todas as ações realizadas nele serão desfeitas. Deseja mesmo continuar?"* → modo de edição dos campos + despacho de **justificativa obrigatória** → flash "Documento retificado!";
- *Via meatball do despacho* ("Retificar despacho"): confirmação análoga → retificação + justificativa. Permissão de retificar despacho continua **restrita ao criador original**; despachos gerados por ações sistêmicas (Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou, Retomou) **não são retificáveis**.

**Impactos na timeline**:

- Eventos anulados: perdem botões de ação, ganham tag **"Anulado"** (tooltip: *"Esta ação foi anulada devido à retificação realizada no documento."*);
- **Ações de etapa e assinaturas vinculadas aos eventos anulados passam a "Cancelado"** — independente do status anterior (ex.: "Emitido"/"Assinado" → "Cancelado");
- Eventos anulados ficam **ocultos por padrão** atrás de um separador (*"Eventos anteriores ocultados devido à retificação do documento e reinício de suas etapas."*) com toggle Exibir/Ocultar eventos;
- **Exceções à ocultação**: evento de criação do documento, eventos/despachos de retificação (registro do ato) e evento de reinício do fluxo permanecem visíveis.

**Evento de reinício do fluxo**: gerado após a retificação com os parâmetros da 1ª etapa, encaminhado ao setor responsável dela (*"Etapas do documento reiniciadas e encaminhado para o Setor Responsável: [Nome do setor] devido à retificação."*), com copy própria no título; reexibe as ações obrigatórias da 1ª etapa (despachos customizados, assinaturas etc.) todas em **"Pendente"**.

**Impactos no documento**: prazos de etapas e do documento **não são alterados** nem recalculados pela retificação; tag **"Retificado"** na header (padrão existente); anexos podem ser substituídos — anexo substituído que já estava aprovado **volta pra pendente de aprovação**.

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] Seção **"Repetição da etapa"** segue **vazia mesmo no export expandido** (2026-07-17) — a configuração nunca foi especificada no Notion? Confirmar com produto se a feature existe/foi descartada
- [ ] Perguntas da doc ainda de fato sem resposta: setor envolvido num flow desativado; acompanhamento (modo visualizar) de etapas seguintes pelos envolvidos de etapas anteriores; UX da seleção quando responsável = "setor na hora de avançar"
- [ ] **Retificação em qualquer etapa × assinaturas**: a update diz que assinaturas vinculadas a eventos do fluxo vão pra "Cancelado" no reinício. E as assinaturas **fora** dos eventos de etapa (abertura/anexos, solicitadas avulsas)? Cruzar com a decisão pendente da [[../../05 Refinar/SGV-4873|mesa SGV-4873]]
- [ ] Atalhos (27/05/2026) × regra "só retrocede uma vez": confirmar em teste como convivem (o texto diz que sem atalho vale o linear padrão, mas não explicita se usar atalho consome/reseta o direito de retroceder)

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- [[../../05 Refinar/SGV-4873|SGV-4873]] — retificação × cancelamento de assinaturas (a regra de retificação no workflow conversa direto com a análise da mesa)
- Backlog da página no Notion: melhoria "checkbox marcar/desmarcar todos os setores", "[Melhoria-CX] caminhos alternativos (etapas não obrigatórias)", "[MELHORIA-CX] Permissão de Retificar documento em qualquer etapa do fluxo de Trabalho"
