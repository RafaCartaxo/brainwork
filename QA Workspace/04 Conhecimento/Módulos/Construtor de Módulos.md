---
title: Construtor de Módulos
tags:
  - qa
  - conhecimento
  - sogov
  - construtor-modulos
tipo: modulo
revisado: 2026-10-13
fonte: https://app.notion.com/p/alfa-group/Construtor-de-M-dulos-29474b21e916499ca79d50bb387093c1
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-10-02 (Vinícius Sogo)
---
# Construtor de Módulos

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-13 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria pro módulo em si (campo `Task` vazio no Notion); as atualizações datadas trazem SGV quando existe. Duas seções do export ("Página Extra de Assinaturas" e os campos de zona/categoria de "Processos urbanísticos") são conteúdo que já mora, em detalhe completo, em outras docs do vault — aqui ficou só a referência cruzada, pra não duplicar.

## Visão geral
- Módulos são tipos de documento e/ou processo administrativo, com campos e características próprias, tramitáveis ou não (depende do tipo), usados pra comunicação interna e rotina administrativa de um órgão público. Exemplos-base: protocolos, processos administrativos, alvarás, memorandos, circulares.
- O **construtor de módulos** fica no Ambiente Técnico SOGO (menu "Módulos"), acessível só a usuários cadastrados como SOGO — ver [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]]. Facilita criar tipos de módulo pras instâncias dos clientes.
- **3 etapas**: (1) configuração dos parâmetros, (2) casca — onde se adicionam os campos do formulário de abertura, (3) visualização do que foi inserido.

## Regras de negócio

### Permissão
- Só usuários SOGO com nível **Administrador** podem criar, editar, vincular/desvincular, duplicar, publicar, ativar/inativar e excluir módulos.

### Configuração de parâmetros (etapa 1)

#### Descrição geral do módulo
- Nome do módulo (texto) e Descrição (texto).

#### Natureza e privacidade do documento
- **Tipo de documento** (select obrigatório, define regras de tramitação): **Documento oficial** / **Comunicação oficial** / **Processo administrativo**.
	- Documento oficial: interação é sempre informativa por padrão — a seção "Tipo de interação" é pulada no modo guiado e fica `disable` no avançado; libera o toggle "Permite publicação em canal de comunicação oficial".
	- Comunicação oficial: libera o mesmo toggle de publicação em canal.
	- Processo administrativo: libera "Permitir abertura externa" e "Permite despachos sigilosos".
- **Permite publicação em canal de comunicação oficial**: escolhe Canal interno (mural SoGov) e/ou Canal externo (jornal oficial) — detalhe completo em [[QA Workspace/04 Conhecimento/Módulos/Divulgar Documento|Divulgar Documento]].
- **Permite abertura externa** (só Processo administrativo): documento pode ser gerado externamente pelo cidadão; libera "Permite mostrar opções de privacidade" (condicionado a este parâmetro).
- **Permite mostrar opções de privacidade**: libera, na casca de abertura, as opções Com sigilo / Sem sigilo / Anônimo.
- **Permite despachos sigilosos** (só Processo administrativo): toda vez que for feito um despacho na tramitação, aparece a opção de marcá-lo como sigiloso.

#### Tipo de interação
- **Caráter informativo**: exibe, na casca de abertura, opção pra gerar documento sem necessidade de interação (só informativo pra quem recebe). Não aparece na versão externa do módulo — só na interna.
- Na abertura (visão do servidor), com o cluster "Tipo de interação" ativo: **Documento informativo** (não recebe interações) vs. **Documento interativo** (recebe interações). Informativo exibe a flag "Caráter informativo" no header; interativo não mostra sinalização na header.

#### Conexões
- **Vincula a assuntos e serviços**: define se o módulo aceita A/S vinculados; se marcado, a casca ganha campo de seleção dos A/S cadastrados no workspace.
- **Permite conexão com outro módulo**: ativa um botão "Gerar" na tramitação, que lista os módulos conectados como atalho pra gerar documento (fica registrado na timeline). Ativado, aparece busca pra escolher quais módulos poderão "gerar" documentos deste tipo.

#### Prazos
- **Adicionar prazo oficial**: define a quantidade de dias; libera "Aceita prorrogação de prazo oficial".
- **Aceita prorrogação de prazo oficial**: define a quantidade de prorrogações possíveis, cada uma com seu próprio campo de dias; libera o checkbox "Exige justificativa nas prorrogações".
- Regras de prorrogação:
	- Prazos de prorrogação **não podem ser maiores** que o prazo oficial.
	- Prorrogações seguintes **não podem ser maiores** que as anteriores (podem ser iguais ou menores).
	- A **soma** de todas as prorrogações não pode ultrapassar os dias do prazo oficial.
	- Quantidade máxima de prorrogações = dias do prazo oficial (ex.: prazo de 20 dias → no máximo 20 prorrogações de 1 dia cada).
	- Exemplo válido: prazo de 20 dias com 3 prorrogações de 15, 3 e 2 dias (sempre decrescente ou igual).

#### Numeração
- Segue as mesmas regras já especificadas pra criação guiada em serviços e assuntos. Ao avançar, tela de carregamento; se o módulo tem prazo configurado, mostra mensagem orientando o prazo de conclusão a partir da data de abertura.

#### Processos urbanísticos
- Ativando, os campos de zona e categoria de uso entram na casca como **obrigatórios** pra abrir o formulário — regras completas de zona/categoria (dependência entre os campos, sem lógica de exibição, só largura editável com mínimo de 60%) em [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]].

#### Finalização do módulo
- Status possíveis ao salvar: **Rascunho** (criado, não disponível pra uso) / **Ativo** (visível, mas não gera documentos) / **Publicado** (gera documentos).
- Por padrão nenhum status vem pré-selecionado; o módulo filho pode nascer em Rascunho mesmo com o módulo pai Ativo.
- Esse modal de status só aparece durante o processo de vinculação — depois disso, status só muda pelo menu meatball.

### Gerenciamento de módulos: listagem, edição e afins

#### Listagem de módulos
- Itens exibidos: Título, Descrição, Status, menu de opções (varia conforme status), botão "Novo Módulo", campo de busca, filtro por status.

#### Ações por status
| Status | Ações permitidas | Exclusão |
|---|---|---|
| Ativo | Editar, vincular, duplicar, inativar | só se **sem** clientes vinculados |
| Inativo | Editar, vincular, duplicar, ativar | só se **sem** clientes vinculados |
| Rascunho | Editar, duplicar, ativar, excluir | livre |

#### Vincular cliente
- Duas entradas: menu meatball na listagem do gerenciador de módulos, ou listagem interna de um módulo específico.
- **Módulo em Rascunho não pode ser vinculado a cliente.**
- Seleção de cliente: lista com busca (a partir de 3 caracteres) e paginação (10 por página); tentar avançar sem selecionar um cliente → alerta de erro.
- Após selecionar o cliente, configura as regras de tramitação: setores que recebem/tramitam, setores criadores, setores destino (automático e/ou opções pro cidadão escolher — só se o módulo permite abertura externa), interações externas (só com abertura externa), sigilo (setores que veem dados sigilosos, conforme privacidade/despacho sigiloso). Essas regras seguem o mesmo padrão já especificado pra criação guiada em serviços e assuntos.

#### Edição de módulo
- Permite ajustar campos existentes, adicionar novos ou remover, num módulo principal ou vinculado.
- **Adicionar/remover campo no módulo pai** → replica a ação pra todos os módulos vinculados + notifica todos os clientes afetados. Ex.: campo "Escolha única/múltipla" adicionado → ao salvar, checklist com todas as alterações, agrupadas por tipo (cada uma com cor própria conforme o protótipo); mais de 8 alertas → ativa rolagem. Notifica administradores dos módulos vinculados + usuários com acesso ao ambiente técnico SOGO; mudanças em nível de cliente/servidor notificam administradores e servidores N1 (ou quem tem permissão extra) com acesso ao documento.
- **Regras de largura depois de vincular um cliente**:
	- Campo **sem** largura fixa no pai → não pode mudar a largura no pai, mas pode no módulo do cliente.
	- Campo **com** largura fixa no pai → editável no pai, mas **não** no módulo do cliente.
	- Editar um campo com largura fixa e salvar **sem** fixá-la → vira "sem largura fixa" de forma permanente — nunca mais editável no pai.
	- Posicionamento de campos novos (com cliente já vinculado): só acima ou abaixo das linhas existentes, exceto quando campos de largura fixa diminuíram e sobrou espaço na linha; um campo inserido no meio sempre fica acima **ou** abaixo de todos os existentes, nunca misturado.
	- Serviços/assuntos impactados pela edição do pai ou filho sobem (ancoram) pro topo da listagem, com tag/tooltip de "impactado"; notificação usa a copy "confira os afetados".
	- Regras de tramitação editadas são replicadas, herdando o que dá pra herdar; o que precisa ser feito manualmente é resetado — até resolver, não dá pra abrir o tipo do documento.
	- **Prazo do pai alterado**: se não conflita com o do filho (não é menor) → sem impacto, documentos novos já usam o prazo novo. Se é diminuído e conflita com o herdeiro → herdeiro herda o prazo novo + notifica. Se é excluído → notifica, mas não remove dos filhos. Numeração nunca muda por causa disso.
	- Campos do pai podem ser excluídos, **exceto** os ligados a parâmetros.
	- Editar campo existente no pai: é **opcional** se a edição afeta os filhos já existentes, ou só os que forem vinculados a partir dali.

#### Duplicar módulo
- Modal de confirmação; confirmado → flash de sucesso, módulo novo nasce em **Rascunho**, cor alternada (mantém o padrão zebrado da listagem), título ganha sufixo **"(cópia)"**.
- Duplicações sucessivas são enumeradas: "Memorando" → "Memorando (cópia 2)" → duplicar de novo → "Memorando (cópia 2) (cópia)".
- **A duplicação não herda os clientes vinculados.**

#### Inativar módulo
- Modal de confirmação; ao concluir, notifica no ambiente do servidor sobre a alteração.
- **Não afeta** documentos já criados (continuam tramitando livremente) — só impede a criação de **novos** documentos.
- A inativação é em massa e notifica clientes com módulo Ativo e/ou Publicado.
- Inativar o módulo pai **inativa os módulos clientes junto**; mas **reativar o pai não reativa os clientes automaticamente** — cada um precisa ser reativado individualmente.
- Ao reativar, o sistema restaura a **última versão** do módulo.

#### Ativar módulo
- Modal de confirmação simples; confirmado, o status volta pra Ativo.

#### Excluir módulo
- Sem clientes vinculados → exclui direto, com mensagem de sucesso.
- Com clientes vinculados → bloqueia a exclusão, avisa que é preciso desvincular todos os clientes antes.

### Lógica de campos (exibição condicional)
- Configuração opcional por campo, ao lado das configurações básicas. Ativa ao clicar em "adicionar grupo de regras" — se toda a lógica for apagada, o componente volta ao estado default. Um preview acompanha a configuração pra facilitar o entendimento.
- **Campos condicionantes** (definem se outro campo aparece ou não):
	- Renomear um condicionante atualiza automaticamente onde ele é referenciado na lógica.
	- Excluir um campo condicionante avisa e o remove da lógica; o grupo de regra que o usava como condicionante é excluído, os demais grupos se reorganizam, e quem foi impactado é avisado pra reformular a própria lógica.
	- Condicionante do tipo **Escolha** com alternativas resetadas/editadas → aparece um select de VALOR na configuração da lógica; o usuário é avisado do impacto e levado a ajustar. Adiar o ajuste deixa o campo em **estado de erro** até corrigir — só é possível salvar/finalizar a criação depois de resolver a lógica impactada.
	- Editar só o **nome** de uma alternativa não impacta a lógica — atualiza sozinho, sem aviso.

### Ações disponíveis por status do cliente (módulo vinculado)
| Status do cliente | Ações |
|---|---|
| Publicado | Editar formulário, Regras de tramitação, Desvincular, Inativar, Resetar |
| Rascunho | Ativar, Publicar, Editar formulário, Regras de tramitação, Desvincular, Resetar |
| Ativo | Publicar, Editar formulário, Regras de tramitação, Desvincular, Inativar, Resetar |
| Inativo | Ativar, Editar formulário, Regras de tramitação, Desvincular, Resetar |

### Impactos na edição de módulos
- Iniciar a edição de um **módulo cliente** bloqueia a edição do módulo pai e dos A/S vinculados a esse módulo.
- Iniciar a edição do **módulo pai** bloqueia a edição de todos os módulos clientes vinculados a ele e de seus respectivos A/S.
- Durante a edição (pai ou cliente), notifica os clientes vinculados que o módulo está em manutenção e que a abertura de documentos está temporariamente suspensa; concluída a edição, notifica detalhando as mudanças.
- Alterações que afetam as regras de tramitação desativam e sinalizam automaticamente os A/S impactados, pros administradores dos clientes fazerem os ajustes necessários.

### Visualização do cluster central na edição de módulos
- Campos inseridos no cluster central (na configuração de hierarquias) têm o espaço reservado pra evitar conflito — visualização específica criada pra isso.
- Só é ativada no módulo **pai** quando já existem clientes vinculados; no módulo **cliente/filho**, só se há serviços ou assuntos vinculados.
- O espaço reservado aparece como "não vago" na edição — só dá pra adicionar campos acima ou abaixo dele, nunca ao lado.
- Hierarquia do módulo pai = módulos clientes + serviços/assuntos vinculados a esses clientes. Hierarquia do módulo cliente/filho = serviços e assuntos do próprio módulo.

### Campo de Texto Informativo (28/01/2026, atualizado em 22/07/2026)
- Campo **não interativo** do Construtor de Formulários — exibe texto, orientação ou conteúdo institucional ao usuário (Servidor e/ou Cidadão) durante o preenchimento, **sem coletar dado**. Só aparece na abertura do documento; some depois de criado e na impressão.
- Largura fixa 100% (não configurável); não recebe foco/input/validação do usuário final; pode receber lógica de exibição aplicada a ele, mas **não pode ser campo condicionante** (não tem interação).
- Inserido pela Sidebar do Construtor de Formulário, categoria **Conteúdo → Texto informativo**. Estado inicial (vazio): rótulo "TEXTO INFORMATIVO", mensagem "Ainda não há conteúdo cadastrado.", borda padrão serrilhada.
- **Parâmetros**: Conteúdo (obrigatório); Exibição do campo (Servidor e Cidadão / Apenas Servidor / Apenas Cidadão); botões Editar conteúdo, Excluir (fluxo padrão dos demais campos), Resetar (idem).
- Modal "Cadastrar conteúdo de texto informativo" — editor de texto rico (mesmas opções dos Modelos de Documento); botões Salvar, Cancelar, Fechar (X).
- **Cancelar/Fechar com alterações pendentes**: sem alteração → retorna direto; com alteração → alerta `danger` ("ATENÇÃO! Ao cancelar, todo o conteúdo criado e definido para este campo será perdido. Deseja mesmo descartá-lo?") com **Cancelar** (volta ao modal preservando o conteúdo) ou **Descartar alterações** (perde tudo).
- **Validação**: conteúdo é obrigatório — tentar finalizar o formulário ou inserir um novo campo sem preencher → campo entra em erro, pré-visualização não mostra conteúdo, mensagem "Insira o conteúdo para o campo", borda vermelha sólida.
- Não aparece após a criação do documento nem na impressão; não permite mudar largura; não pode ser condicionante; **sem** restrição de posição no primeiro/penúltimo container mesmo que já tenham duas linhas de campos (por ser só informativo, não entra na contagem normal de restrição de posição).

### Campo de Texto Grande — texto padrão no nível de módulo (03/02/2026)
- Texto padrão (default) cadastrado no **módulo** (nível "Pai") sobrescreve e **bloqueia** qualquer configuração equivalente nos níveis inferiores — todos os A/S vinculados herdam automaticamente, se a configuração existir.
- Com texto cadastrado no módulo, o cluster "Exemplo de preenchimento" **não aparece** pra configurar nos assuntos/serviços (eles herdam a regra do módulo).
- Tooltip do cluster: *"Todos os documentos abertos neste módulo terão este conteúdo cadastrado previamente, mas ainda podendo ser editado livremente."*
- Botão "Salvar" do modal nasce **desabilitado**, só habilita após alguma alteração (input); excluir um modelo exige pop-up de confirmação obrigatório.
- Documento abre com o texto do módulo já preenchido; usuário pode apagar/editar livremente. Aplicar um "Modelo de Texto" pessoal **insere depois** do texto padrão do módulo — não o substitui, a menos que o usuário apague o padrão manualmente antes.

### Configuração de conteúdo sensível (09/03/2026)
- Camada de proteção seletiva de dados — permite que o cidadão acompanhe a demanda externamente por número de protocolo **sem exigir login**, mantendo mascarados os campos marcados como sensíveis. Só se aplica ao tipo **Processo administrativo**, em qualquer campo onde exista construção de formulário.
- **Mudança de paradigma**: substitui a exigência de login pra todo acesso externo por uma regra granular de ocultação de dado por campo.
- No construtor, todo tipo de campo ganha um checkbox "Sensível". O mascaramento afeta só a **visualização externa** — o dado real fica íntegro na base interna.
- **Matriz de visibilidade**:

| Perfil de acesso | Condição | Comportamento do dado |
|---|---|---|
| Externo (não logado) | Acesso via protocolo | Mascarado (se marcado como sensível) |
| Logado e envolvido | Faz parte do fluxo | Visualização plena |
| Logado e não envolvido | Sem vínculo direto | Mascarado (se marcado como sensível) |

- Campos **não** marcados como sensíveis continuam visíveis externamente (ex.: dados públicos de alvará).
- **Herança módulo pai → filho**: se o pai tem o campo marcado como sensível, o filho pode alterar a configuração. Mantendo sensível no filho → documentos criados nesse filho (com ou sem A/S) **têm** o dado como sensível. Desmarcando no filho → documentos criados nesse filho **não têm**. Se o **filho** já define a configuração, o A/S (serviço/assunto) **não pode alterar**.
- **Campo removido do "sensível" depois de já existirem documentos criados com ele**: os documentos anteriores **não são impactados** — mantêm o dado como sensível.
- **Configuração do campo alterada** (passou a ser sensível, ou deixou de ser) depois de já existirem documentos: os documentos anteriores **são impactados** e passam a seguir a nova regra, nos dois sentidos.

### Formatos de anexo KMZ e KML (11/05/2026)
- Adicionados ao seletor "Formato(s) suportado(s)", categoria Documentos. Aplica-se tanto a nível de módulo quanto de serviço/assunto.

### Página extra de assinaturas — ativação mestre (28/04/2026)
> Conteúdo completo (configuração, herança, regras de download/impressão, QR Code) já documentado em [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas]] — aqui fica só a ponta que pertence ao Construtor.

- A **ativação mestre** da funcionalidade é um parâmetro técnico do **módulo filho**, ativado pelo time de **CX** na criação/edição do módulo — sem essa ativação prévia, as opções de "Página Extra" nem aparecem na edição dos assuntos/serviços vinculados.

### Atualização — "Permitir solicitar ações de cidadãos" (14/09/2026)
- **Objetivo**: tornar configurável, por módulo (herdado pelos A/S vinculados), se cidadãos (pessoas físicas) podem ser selecionados em ações do documento — destino, resposta, assinatura. Hoje esse comportamento é fixo.
- **Onde fica**: etapa 2 (Natureza e privacidade do documento) da Criação Guiada, logo abaixo do toggle "Permite publicação em canal de comunicação oficial" — checkbox com texto de apoio. No nível de A/S, o mesmo componente aparece no container Natureza e Privacidade, respeitando as mesmas regras.
- **Regras de negócio**:
	- Parâmetro ativo → seleção de cidadãos disponível tanto na abertura quanto na tramitação, respeitando as regras já existentes.
	- Parâmetro inativo → nenhum componente de seleção de usuário exibe cidadãos/pessoas físicas — só servidores (vale pra documento em abertura e já em tramitação).
	- A/S criado vinculando um módulo já nasce com o parâmetro ativo/inativo conforme a configuração do módulo.
	- **Caso de borda**: natureza = Processo administrativo **e** Abertura externa ativa → o parâmetro vem **habilitado e bloqueado** (`checked + disabled`) — única exceção; fora dela, é sempre editável. Reavaliado sempre que natureza ou Abertura externa mudam na mesma sessão.
	- **Regra não retroativa**: vínculos de cidadão já existentes em documentos (destinatário, revisor, signatário, resposta) permanecem válidos depois de desativar o parâmetro — a regra vale só pras seleções novas, feitas a partir da mudança.
	- Filtragem precisa ser aplicada no **backend**, não só ocultada na interface — tentativa de vincular cidadão via API com o parâmetro inativo é rejeitada.
	- Alteração do parâmetro gera entrada no histórico do módulo.
	- Copy do tooltip (caso de borda): *"Esta opção é automaticamente acionada ao ativar permissão de abertura externa."*
	- Valor padrão pra módulos novos e já existentes: mantém o comportamento atual (ativo); mudar é manual, feito por quem configura o módulo/A/S.

### Atualização — Comunicação oficial com sigilo por usuário (SGV-11889, 02/10/2026)
> Memorando para destinatário específico — sigilo **por usuário**, independente do sigilo por setor já existente (doc relacionada: "Documentos e despachos Com Sigilo", consolidado 10/11/2025 — ver Dúvidas em aberto).

- **Contexto**: Comunicações Oficiais hoje tramitam por setor (todos os servidores do setor acessam); alguns clientes precisam restringir o acesso a um único servidor específico, sem recorrer a meios externos ao sistema.
- **Escopo**: parâmetro só em **módulos filhos** de Comunicação oficial — nunca no módulo pai (SOGO). Não altera a regra de sigilo por setor já existente, nem a transferência automática de documentos por inativação.
- **Configuração do módulo**:
	- Parâmetro **"Permitir documentos de comunicação oficial sigilosos"** — só em filhos, só pro tipo Comunicação oficial, desmarcado por padrão (sem ele, tramitação segue por setor como hoje).
	- Marcar o parâmetro **desliga e desabilita** "Permite publicação em canal de comunicação oficial" e "Permitir solicitar ações de cidadãos" (se algum estiver ativo no momento, é desligado automaticamente antes de ficar desabilitado). Desmarcar devolve os dois habilitados, no estado desligado.
- **Emissão do memorando**:
	- Parâmetro ativo → emissão ganha o checkbox **"Documento de comunicação sigilosa"** (desmarcado por padrão), abaixo dos campos de destino.
	- Marcado → **Setor destinatário** e **Servidor responsável** viram obrigatórios (troca "(opcional)" por "*"); Servidor responsável aceita um único servidor, só do setor selecionado, fica `disabled` até escolher o setor; trocar o setor limpa o servidor selecionado.
	- Validação ao clicar em Criar: campo vazio → estado Error "Campo obrigatório para comunicação sigilosa", documento não é criado. Sem setor selecionado, o erro aparece só no Setor destinatário; ao selecioná-lo, o erro some e o servidor é habilitado.
	- Desmarcar o checkbox remove todos os erros e devolve os campos ao estado opcional, **mantendo os valores já preenchidos**.
	- Com o checkbox marcado: "Adicionar setores em cópia" e "Solicitar revisão" ficam `disabled` (com tooltip explicando o motivo); "Assinaturas" segue habilitado.
	- **O sigilo não pode ser removido nem alterado depois da emissão.**
- **Acesso e interações**:
	- Só acessam o conteúdo: remetente, servidor destinatário único, e signatários incluídos por solicitação de assinatura (enquanto durar a solicitação, ou pra sempre após assinar). A permissão setorial "Visualizar sigilo de documentos" **não concede acesso**; mesas alheias e hierarquia setorial (admin setorial) também não.
	- Demais servidores dos setores de origem e destino veem só o card **"Documento sigiloso"** (sem conteúdo, anexos, respostas, timeline ou nome do destinatário).
	- Única interação possível entre os envolvidos: **Responder** — não dá pra tramitar pra outros setores nem incluir novos servidores nas respostas.
	- Qualquer envolvido pode solicitar assinatura a qualquer servidor do órgão; ao receber, o signatário ganha o mesmo acesso dos demais envolvidos. Solicitação cancelada/recusada → acesso removido; assinatura executada → acesso permanente.
	- Download, impressão e "Compartilhar link" só disponíveis pra quem tem acesso ao conteúdo.
	- Toda concessão/remoção de acesso, e a própria aplicação do sigilo, são registradas no histórico.
- **Desvinculação e inativação**:
	- Envolvido desvinculado do setor → documento continua na mesa dele, acesso mantido.
	- Inativar um envolvido não muda o acesso dos demais que seguem ativos.
	- Destinatário inativado → remetente pode emitir novo memorando sigiloso pra outro servidor e vincular o original via "Associar documentos".
	- Documentos sigilosos **nunca** são transferidos automaticamente por inativação.
	- Todos os envolvidos inativados → documento permanece preservado, sigilo mantido; acesso é restabelecido se algum envolvido for reativado.
	- Inativar servidor **não** exibe modal nem aviso relacionado a comunicações sigilosas.
- **Nota pra QA**: há 3 exceções identificadas à doc de sigilo vigente ("Documentos e despachos Com Sigilo", consolidado 10/11/2025) que precisam ser registradas lá também, com link pra esta task: (1) despacho sem sigilo não fica visível pra quem só vê o card "Documento sigiloso"; (2) incluir um signatário **amplia** o acesso, em vez de a lista mostrar só quem já tinha; (3) desvincular do setor **não** remove o acesso.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado.

## Dúvidas em aberto
- [ ] "Finalização do módulo" não deixa claro se existe transição direta **Rascunho → Publicado** sem passar por Ativo, ou se o caminho é sempre sequencial.
- [ ] Backlog do Notion ainda lista **"[Melhoria] Configuração de 'conteúdo sensível'... com mascaramento em acesso externo sem login"** como pendente, mas a seção "Configuração de conteúdo sensível" (09/03/2026) parece já cobrir exatamente isso — confirmar se o item do backlog está desatualizado ou se falta algo.
- [ ] Backlog também cita **"[SOLICITAÇÃO-CX] Estender o mascaramento dos dados sensíveis aos documentos gerados antes da implementação da melhoria"** — ou seja, documentos criados **antes** de 09/03/2026 podem não ter o mascaramento aplicado retroativamente. A doc atual não cobre esse caso (ela só define o comportamento pra quando a config de um campo muda depois de já existirem documentos, não pra quando a própria feature de mascaramento ainda não existia). Confirmar status dessa solicitação.
- [ ] Export mostra só 5 itens do backlog + **"8 more…"** — os demais não foram vistos.
- [ ] Tabela de "Decisões registradas" da atualização de 02/10 lista decisões já **revogadas** (DC07, DC11) junto das vigentes, sem marcação visual — só a coluna "Origem" avisa ("Revogada pelo CX", "Revogada (DC07)"). Mantido como veio do Notion; atenção ao ler a tabela.
- [ ] A "doc relacionada" citada na atualização de 02/10 — **"Documentos e despachos Com Sigilo" (Consolidado 10/11/2025)** — ainda não foi importada pro vault; ela é quem recebe as 3 exceções anotadas na nota acima.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- **SGV-11889** — Memorando sigiloso por usuário (02/10/2026, ver seção própria).
- SGV-11558 — citado na decisão DC24 como referência da regra de abertura externa × ações de cidadãos (não detalhado neste export).
- Sem SGV pro módulo em si, nem pras demais atualizações datadas (documentação de referência, sem task própria no Notion).

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Divulgar Documento|Divulgar Documento]] — detalha o parâmetro "Permite publicação em canal de comunicação oficial" citado aqui.
- [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]] — detalha os campos de zona/categoria de uso citados na seção "Processos urbanísticos".
- [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] — detalhe completo da "Página extra de assinaturas", cuja ativação mestre é configurada aqui.
- [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]] — onde o Ambiente Técnico SOGO (que hospeda este construtor) está descrito.
