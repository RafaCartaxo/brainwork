---
title: Organograma
tags:
  - qa
  - conhecimento
  - sogov
  - organograma
  - setores
tipo: modulo
revisado: 2026-07-20
fonte: https://app.notion.com/p/alfa-group/Organograma-96c5fd1b1bb341b983e5299ec4773cb0
fonte_criado: 2024-07-08 (Alice Martins)
fonte_ultima_edicao: 2026-05-11 (Ivo Costa)
---
# Organograma

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20. A página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Os prints/protótipos do Figma citados no export não vieram no export em si — consultar o Notion/Figma pra referência visual. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste]].

## Visão geral

O organograma é a representação hierárquica da organização funcional do cliente. É onde se cadastram todos os setores da organização, com seus usuários, respeitando a estrutura administrativa individual de cada cliente. No sistema, o organograma representa também a origem e destino de documentos/processos e seus despachos.

**Permissão de acesso**: todos os usuários cadastrados na plataforma SoGov podem acessar a página de organograma e visualizar as informações de cada setor (a visualização é livre; ações de edição/cadastro exigem permissão — ver [[#Regras de negócio]]).

**Hierarquia**: setor pai → subsetores (um setor pai pode ter múltiplos subsetores em sequência).

Em ambiente de cliente novo, é exibido o organograma base vindo das cargas iniciais. Em cliente já ativo, exibe o organograma conforme configurado.

## Regras de negócio

### Funcionalidades gerais do organograma

- **Visualização expandida**: usuários podem expandir a visualização para ver toda a estrutura de setores e subsetores;
- **Cadastro ilimitado**: não há limite para o número de setores e subsetores cadastráveis;
- **Cadastro restrito**: o cadastro de novos setores e subsetores é restrito a usuários com permissões específicas;
- **Usuários online**: no topo da página, é exibido o total de usuários online junto com a quantidade de setores (ex.: "100 usuários online em 53 setores");
- **Estatísticas**: exibe quantidade total de setores e usuários cadastrados no sistema;
- **Retração/expansão**: cada setor e subsetor tem botão para retrair ou expandir seus subsetores;
- **Visualizar setor**: cada setor tem botão "Visualizar setor", que abre página com nome do setor e informações dos usuários atribuídos (nome, cargo, data de cadastro, data do último acesso online, telefone); o usuário online no momento é destacado na lista.

### Cadastro de setores principais

Campos do cadastro:

| Campo | Descrição |
|---|---|
| Nome do setor | Identificação no organograma, no topo de documentos gerados e nos processos |
| Sigla do setor | Abreviação exibida antes do nome no organograma |
| Descrição do setor | Texto resumido; aparece no organograma e na caixa de seleção de setor como destino de documento |
| Setor Pai | Setor hierarquicamente acima no organograma |
| ID Setor | Atribuído automaticamente pelo sistema ao criar o setor |
| Tipo de Setor | Ver tabela abaixo |

Tipos de setor:

| Tipo | Regra |
|---|---|
| **Setor** | Padrão do organograma, envio/recebimento de documentos sem regras/restrições por default |
| **Gabinete** | Mesma finalidade de setor, mas com poder de restrição: o sistema deve possibilitar que o Gabinete receba documentos apenas de outros Gabinetes |
| **Grupo de trabalho** | Usado para comissões especiais e grupos de trabalho. Visível no organograma **apenas** para o seu setor pai; **não pode ter subsetor**; aceita função "setor soberano" (não atende regras de acesso de setor e documentos por hierarquia de organograma) |

### Cadastro de subsetores

- CTA de cadastro de novo subsetor disponível em qualquer setor do organograma, **exceto** em setores do tipo "Grupo de Trabalho";
- Única diferença do modal de cadastro de subsetor em relação ao de setor: o select "Setor pai" vem **preenchido automaticamente e travado** (não editável) com o setor a partir do qual o CTA foi acionado;
- **Sigla do subsetor**: ao criar, o nome vem com duas siglas — a sigla do setor principal mais acima na hierarquia + a sigla do próprio subsetor. Exemplo do export: SEPLAN é subsetor de Controladoria Interna, mas o setor principal (topo da hierarquia) é o Gabinete do Prefeito — mesmo o setor pai direto sendo Controladoria, a sigla usada é a do Gabinete.

### Ações nos setores e subsetores

Disponíveis no menu meatball: **Editar**, **Adicionar usuário ao setor/subsetor**, **Suspensão**.

### Edição de setor ou subsetor

Ao acionar "Editar" no meatball, é possível: editar informações básicas, gerenciar usuários vinculados, suspender o setor, reativar (se inativo), editar o setor pai (para subsetores, mudando a posição na hierarquia) e editar as regras de tramitação do setor.

Regras:
- CTAs de edição ficam indisponíveis para usuários sem permissão adequada (por nível/perfil ou por permissão adicional de sistema — feature de [Usuários e gerenciamento de permissões](https://app.notion.com/p/Usu-rios-e-gerenciamento-de-permiss-es-1eeb22fe245143b4a412209763906be7));
- Quem tem permissão pode editar todas as informações, **exceto ID de setor**;
- O CTA de visualização fica disponível para todos os usuários.

**Efeito de renomear um setor/subsetor sobre documentos já tramitados**:
- Se existem documentos já tramitados no setor: é exibido um alerta informando que esses documentos permanecerão com o nome do setor antigo;
- A partir da data/horário da mudança de nome em diante, documentos novos já saem com o nome do setor novo;
- Se o setor **não** tem nenhum documento gerado/tramitado nele, a mudança de nome se aplica normalmente (os documentos gerados/tramitados depois adquirem o nome novo, sem ressalva);
- Mudar o setor pai também muda a sigla do setor, o que se enquadra nessa mesma regra de renomeação.

### Gerenciar usuários do setor/subsetor

- Listagem de todos os usuários do setor;
- Usuários que têm o setor em questão como setor **principal** e também estão em outros setores exibem uma tag indicando o setor principal; **não é possível excluir** esse usuário da listagem quando esse é o seu setor principal;
- Botão para ordenar em ordem alfabética;
- Remoção de usuário do setor — se mais de um usuário for selecionado, a remoção pode ser em massa;
- Busca de usuários: feita entre todos os usuários do organograma. Se o usuário buscado não está atribuído ao setor em questão, a exibição muda para permitir incluí-lo e definir a permissão dele ali mesmo;
- CTA "Adicionar usuário ao setor": abre tela de busca por nome → seleciona o usuário → usuário vai para lista abaixo da busca, onde se escolhe o nível de permissão dele no setor → ao confirmar, exibe flash message de sucesso e retorna à listagem de usuários do setor.

### Suspensão de setor/subsetor

Um setor **não pode ser excluído** — só suspenso por tempo indeterminado. A suspensão:
- Faz o setor deixar de ser exibido no organograma;
- Torna o setor indisponível, não permitindo que documentos passem por ele;
- Muda o status do setor para inativo.

Ao clicar para suspender (menu meatball), o sistema verifica configurações de módulos, fluxos e sistema antes de permitir. Cenários:

| Caso | Condição | Resultado |
|---|---|---|
| 1 | Sem nenhuma pendência | Exibe modal de confirmação; suspensão é feita com sucesso |
| 2 | Documentos pendentes de tramitação/assinatura no setor | Exibe quais documentos têm pendência (dentro de um select); **não permite** suspensão |
| 3 | Configurações de workflow no setor | Exibe qual configuração é (dentro de um select); **não permite** suspensão |
| 4 | Setores filhos e/ou netos | Exibe quais são esses setores (dentro de um select); **não permite** suspensão |
| 5 | Usuários cadastrados com esse setor como principal | Exibe lista dos usuários (dentro de um select); **não permite** suspensão |
| 6 | Configuração de módulos diretamente relacionada ao setor | Exibe lista dessas configurações (dentro de um select); **não permite** suspensão |
| 7 | Combinação de várias pendências acima | Todas exibidas em lista; **não permite** suspensão |

Após suspenso, o setor/subsetor só fica visível para o administrador — só o administrador pode reativar um setor inativo.

### Reativar setor

Administradores usam filtros/busca para listar setores inativos. A listagem exibe: sigla e nome completo, ID do setor, data de cadastro, data de inativação e log de ação (quem suspendeu). Administradores podem reativar direto da lista.

Ao reativar, **todos os documentos voltam a ficar disponíveis no inbox do setor**.

### Visualização de servidores por setor

O contador de servidores de cada setor (antes estático) funciona como gatilho para abrir um modal com a listagem completa dos membros do setor, com busca e status de atividade.

- **Gatilho**: hover no contador muda o cursor para pointer com indicação visual de interatividade; clique abre o modal "Listagem de Servidores"; fecha pelo ícone "X" ou tecla ESC;
- **Header do modal**: título com nome completo do setor (ex.: "(IPREV) Instituto de Previdência do Município"), subtítulo com contagem total (ex.: "32 servidores");
- **Busca**: reativa, inicia a filtragem a partir de 3+ caracteres digitados; filtra por nome do servidor; lista se atualiza em tempo real e a altura do container se adapta; "X" no campo limpa a busca e retorna ao estado padrão; sem resultado exibe "Nenhum resultado encontrado para sua busca: Verifique se digitou sua busca corretamente";
- **Listagem**: ordenação alfabética padrão por nome; linhas zebradas; até 10 servidores a altura se ajusta ao conteúdo (sem scroll); acima de 10, altura máxima de 704px com scroll vertical (lazy loading com skeleton screen ao carregar);
- **Item da lista**: avatar padrão, nome completo em destaque, cargo em menor destaque, e indicador de status:
  - 🟢 Online: sessão ativa na plataforma;
  - ⚪ Pré-cadastrado: nunca acessou — exibe "Cadastro em: DD/MM/AAAA";
  - ⚫ Offline: já acessou mas não está online agora — exibe "Último acesso: DD/MM/AAAA".
- **Casos de borda**: setor com 0 servidores — o contador perde o status de clicável e o modal não abre; falha ao carregar — flash message de erro no topo ("Houve um problema ao carregar - Verifique sua conexão ou tente novamente").

> [!warning] Comentário no Notion (Edu, 29/10/2025) marca esta seção como desatualizada, apontando pra uma versão mais atual da regra na própria página do Notion. O export trazido aqui não contém essa versão revisada — ver [[#Dúvidas em aberto]].

### Edição de regras de tramitação de setores (fluxo de aprovação de permissão)

Funcionalidade que formaliza um fluxo de governança pra edição de regras de tramitação: usuários designados (Adm Setorial e N1/Especialistas) solicitam permissão de edição de forma controlada, com justificativa obrigatória e aprovação centralizada — pra rastreabilidade e segurança sobre alterações críticas nos fluxos de trabalho.

**Ponto de controle único**: aprovar/reprovar uma solicitação acontece exclusivamente na tela de Gerenciamento de Servidores. Notificações por e-mail e alertas na plataforma são apenas atalhos pra esse ponto de decisão.

**Quem pode aprovar**:
- Ambiente cliente: Administradores, Administradores Setoriais, N1 (Especialistas);
- Ambiente SOGO: Administradores SOGO, Analistas, Suporte.

**Onde solicitar**: na tela de edição do setor, acessada via organograma.

**Jornada do solicitante**:
1. Usuário navega até o organograma, localiza o setor, aciona meatball ("••") → "Editar";
2. Dentro do container de editar tramitação (bloqueado por padrão), clica em "Solicitar Permissão";
3. Modal "Solicitação de permissão adicional" com campo de justificativa obrigatório (placeholder de exemplo, limite de 400 caracteres, erro se enviado vazio) e botões "Cancelar"/"Solicitar";
4. Ao solicitar: flash message de sucesso ("Permissão solicitada com sucesso!"), notificação por e-mail e alerta na plataforma são enviados aos responsáveis; o container de regras permanece bloqueado até decisão.

**Jornada do aprovador**:
1. Acessa Gerenciamento de Servidores → aba "Solicitações" (também acessível via link no e-mail/notificação, chegando com foco/destaque na solicitação específica);
2. Aba tem filtros (Pendente, Aprovada, Recusada) e tabela com colunas: Solicitante, Edição do setor (sigla), Data, Status;
3. Ações por status: Pendente → botão "Avaliar"; Aprovada → meatball com "Remover permissão" e "Histórico"; Recusada → meatball com "Ver histórico";
4. Avaliação: modal "Avaliação de permissão adicional" mostra nome do solicitante, setor e justificativa, com botões "Aprovar"/"Recusar":
   - Aprovar → flash message "Permissão aprovada com sucesso!", status muda pra Aprovada, solicitante é notificado;
   - Recusar → flash message "Permissão recusada!", status muda pra Recusada, solicitante é notificado, container de regras volta ao estado default (permite nova solicitação).
5. Remover permissão (item Aprovada): meatball → "Remover permissão" → dialog de confirmação ("Deseja mesmo remover a permissão de $Assinatura_textual para editar as regras de tramitação?") → "Remover" → flash message "Permissão removida com sucesso!", status muda pra **Recusada**, usuário que perdeu a permissão é notificado.

**Histórico da solicitação**: acessado pelo meatball ("•••"), log simplificado. Textos padrão:
- Aprovação: "[Nome do Aprovador] aprovou permissão de edição de regras de tramitação para $Assinatura_textual em [Data]";
- Recusa: "[Nome do Aprovador] recusou permissão de edição de regras de tramitação para $Assinatura_textual em [Data]";
- Remoção pós-aprovação: "[Nome do Aprovador] removeu a permissão de edição de regras de tramitação para $Assinatura_textual em [Data]".

**Permissões e visualização por perfil** (nomenclatura de níveis: `N1 (Especialista)`, `N2 (Usuário básico, exibido como "Básico")` e `Somente Leitura` — nível à parte, abaixo do N2; ver legenda canônica em [[Associar e Desassociar#Permissões e visibilidade]]):
- ADMs: visualização **global** de todas as solicitações e edições; por default, checkbox "Regras de tramitação" vem marcado no container de Permissões Globais, com poder de conceder a permissão a Adms Setoriais e N1 (Especialistas);
- ADMs Setoriais e N1 (Especialistas): visualização restrita aos setores em que **tiverem essa permissão especificamente** (exemplo do export: um N1 lotado em 5 setores, com a permissão em apenas 2, só visualiza/aprova/recusa nesses 2). Checkbox vem **desmarcado** por default nesses níveis; pode ser concedido por outros ADMs/ADMs Setoriais/N1 que tenham permissão para tal;
- Usuários de nível **N2 (Básico) e Somente Leitura não visualizam** essa permissão/funcionalidade.

### Limite de caracteres em siglas

Após solicitações recorrentes de usuários (necessidade de representar nomes de setores complexos/compostos), o limite de caracteres da sigla de setor/organização foi ampliado em 12 caracteres, passando de um valor anterior não especificado no export para **15 caracteres** no total.

- Aplica-se tanto à edição de setores já existentes quanto à criação de novos setores;
- Áreas potencialmente afetadas: campos de busca, documentos, e-mails e outros componentes que exibem siglas de setores — esses elementos podem sofrer desconfiguração visual por causa do novo limite;
- O comportamento dos componentes não muda — só a regra de limite de caracteres é atualizada.

> [!note] O export registra a mudança como indo "contra os princípios organizacionais originais da plataforma", mas concedida pra atender demandas práticas dos usuários.

### Histórico de organograma (auditoria)

Objetivo: rastreabilidade completa de ações no organograma.

**Regra de espelhamento**: todo evento envolvendo módulos, realizado por usuário da instância ou no ambiente técnico, deve ser espelhado no histórico do setor correspondente. Alterações feitas no perfil do servidor que envolvam informações do setor também devem ser obrigatoriamente espelhadas no histórico do setor.

**Padrão de exibição**: `[Evento] — [Pessoa que realizou] • [Horário]`. Empty state exibido quando não há registros (incluindo espelhados), conforme Figma.

Eventos registrados (lista literal do export), agrupados em três blocos:

**1. Dados do setor/subsetor**: criação de setor/subsetor; alteração de nome, sigla, setor pai (subsetor), observações (adição/remoção/alteração) e telefone (adição/remoção/alteração) — cada ação com sua variação para setor e para subsetor.

**2. Regras de tramitação** (aplicável a operações no ambiente Sogov ou módulos específicos): adição/remoção de módulo e de assunto/serviço nas regras de Criação de Documentos, Recebimento e Tramitação de Documentos, Interação com o Cidadão, Visualização de Dados Sigilosos e Disponibilidade para Recebimento de Documentos — cada uma com variação setor/subsetor. (Essas mesmas categorias de regra são configuradas por serviço em [[Serviços e Assuntos]] e por etapa em [[Fluxo de trabalho (Workflow)]].)

**3. Demais regras e status** (espelhados inclusive se alterados via Perfil do Servidor): adicionar/remover usuário do setor/subsetor; alterar cargo do usuário no setor/subsetor; alterar nível de permissão do usuário no setor/subsetor; modificar setor para subsetor (e vice-versa); suspender/reativar setor ou subsetor.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- 

## Dúvidas em aberto
- [ ] Seção "Visualização de servidores por setor": um comentário do Notion (Edu, 29/10/2025) marca essa regra como desatualizada e aponta pra uma versão revisada na própria página — o export capturado aqui não trouxe essa versão nova. Confirmar se a especificação atual do modal ainda é essa ou se mudou.
- [ ] Limite de caracteres em siglas: o export diz "acréscimo de 12 caracteres, passando o limite total para 15" mas não informa qual era o limite anterior (seria 3 caracteres?). Confirmar valor original.
- [ ] Não há detalhamento de quem pode ver/editar setores do tipo "Grupo de trabalho" além da regra "visível apenas para o setor pai" — confirmar se outras permissões de setor comum (edição, suspensão etc.) se aplicam igual.
- [ ] Regra de "setor soberano" (Grupo de trabalho) descrita apenas como "não atende regras de acesso de setor e documentos por hierarquia de organograma" — sem mais detalhe de como isso se comporta na prática (ex.: quem consegue enviar documentos pra ele).
- [ ] Não fica claro no export se a remoção de permissão de edição de regras de tramitação (status muda pra "Recusada") é reversível ou se o setor precisa passar por nova solicitação do zero.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- [[../../02 Demandas/DEV/8977 - Bug Timeout Edicao Regras Organograma|SGV-8977 - Timeout na edição de regras do Organograma]]

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Módulos relacionados: [[Serviços e Assuntos]] e [[Fluxo de trabalho (Workflow)]] — consomem as regras de tramitação por setor definidas aqui
- Feature de permissões referenciada no export: [Usuários e gerenciamento de permissões](https://app.notion.com/p/Usu-rios-e-gerenciamento-de-permiss-es-1eeb22fe245143b4a412209763906be7)
- Protótipo Figma (Visualização de servidores por setor): https://www.figma.com/design/oFhUaElUXOBns9E400kswH/Organograma---Handoff?node-id=383-1625
