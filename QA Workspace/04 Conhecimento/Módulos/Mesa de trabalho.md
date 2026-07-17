---
title: Mesa de trabalho
tags:
  - qa
  - conhecimento
  - sogov
  - mesa-de-trabalho
tipo: modulo
revisado: 2026-07-17
task: SGV-9044
fonte: https://app.notion.com/p/alfa-group/Mesa-de-trabalho-826bd0f556a841b694116d26a19a5bab
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-07-15 (Fernando Junior)
---

# Mesa de trabalho

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-17 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

> [!info] Sumário
> - [[#Definição geral]]
> - [[#Permissões]]
> - [[#Status de um documento]]
> - [[#Status nas mesas]]
> - [[#Modo de visualização listagem]]
> - [[#Regras de ordenação]]
> - [[#Regras de status]]
> - [[#Regras de prazo]]
> - [[#Regras de filtros]]
> - [[#Demais regras]]
> - [[#Switch de setores]]
> - [[#Alerts]]
> - [[#Histórico de atualizações]]

## Definição geral

A mesa de trabalho é uma área na plataforma SoGov onde os usuários podem acessar, gerenciar e realizar tarefas relacionadas a documentos e processos.

Cada servidor terá acesso tanto à sua mesa individual quanto às mesas dos setores a que ele está vinculado.

A mesa terá dois modos de visualização:

- **Lista**
- **Painel — kanban** (visualização padrão)

Através da mesa os servidores poderão administrar os processos e documentos que estão vinculados a eles e aos seus respectivos setores.

Cada tipo de visualização terá suas particularidades quanto às informações que serão exibidas e filtros, mas respeitarão os status definidos previamente.

## Permissões

A visualização da mesa de setores é exibida para todos os servidores cadastrados no SoGov. A realização do switch de setores só é possível para os servidores que estão participando de mais de um setor.

## Status de um documento

O documento pode possuir os seguintes status:

| Status | Tipo do doc | Situação |
| --- | --- | --- |
| Em aberto | Documento oficial · Comunicação oficial · Processo adm | Quando um documento chega em uma mesa específica e ainda não foi visualizado |
| Em elaboração | Documento oficial · Comunicação oficial | Quando um documento ainda não está emitido, ou seja, ainda não é um documento oficial e está em fase de elaboração |
| Em tramitação | Documento oficial · Comunicação oficial · Processo adm | Quando um processo adm ou documento já está emitido e tramitando entre os setores |
| Pausado (aguardando retorno) | Documento oficial · Comunicação oficial · Processo adm | Quando um documento é colocado em pausa, mas ainda não está com sua tramitação encerrada. Possui todas as funcionalidades de tramitação na toolbar, mas os prazos que possui são todos pausados |
| Encerrado | Documento oficial · Comunicação oficial · Processo adm | Quando um documento possui a sua tramitação encerrada |

## Status nas mesas

As mesas envolvidas na tramitação do documento podem possuir os seguintes status:

| Status | Tipo do doc | Situação |
| --- | --- | --- |
| Em aberto | Documento oficial · Comunicação oficial · Processo adm | Quando um documento chega na mesa e ainda não foi visualizado |
| Em elaboração | Documento oficial · Comunicação oficial | Quando um documento ainda não está emitido, ou seja, ainda não é um documento oficial e está em fase de elaboração |
| Em tramitação | Documento oficial · Comunicação oficial · Processo adm | Quando um processo adm ou documento/comunicação oficial já está emitido e tramitando entre os setores |
| Pausado (aguardando retorno) | Documento oficial · Comunicação oficial · Processo adm | Quando um documento ou processo foi interrompido, temporariamente, por estar esperando um retorno de usuários ou órgãos externos, ou por necessidade de pausa em seu prazo |
| Encerrado | Documento oficial · Comunicação oficial · Processo adm | Quando um documento é colocado em Encerrado só na mesa em questão, os prazos da mesa em questão ficam pausados |

> [!warning]
> A mesa do setor dono reflete o status do documento. No entanto, NEM SEMPRE a mesa dos servidores do setor dono reflete esse status, mesmo que façam parte do setor dono. Todas as regras sobre esse e outros pontos estão descritas no item [[#Regras de status]], adiante.

## Modo de visualização listagem

No modo de visualização listagem os itens são exibidos um abaixo do outro, respeitando as [[#Regras de ordenação]] definidas adiante. As informações necessárias para cada item da listagem serão:

- Nome do módulo
- Numeração
- Nome do assunto ou serviço (quando houver)
- **Quem abriu**
  - Quando for demanda de abertura externa:
    - Solicitante → Primeiro e segundo nome
    - Aberto por (quando houver) → Primeiro e segundo nome, cargo, SIGLA
  - Quando for demanda aberta internamente:
    - Aberto/criado por → Primeiro e segundo nome, cargo, SIGLA
- **Setor responsável** (setor dono) → SIGLA
- **Prazo**
  - Na visualização da mesa do setor, mostrar o prazo do setor
  - Na visualização da mesa do servidor, mostrar o prazo mais próximo de vencer do servidor
- **Status do documento** no setor responsável
- **Status na mesa**
  - Na visualização da mesa do setor, mostrar o status em que se encontra na mesa do setor
  - Na visualização da mesa do servidor, mostrar o status em que se encontra na mesa do servidor

## Regras de ordenação

No modo de visualização lista, a listagem será dividida em duas seções:

- **Não acessados** → onde ficarão todos os documentos que ainda não foram abertos na mesa em questão. Critério de ordenação:
  - Abertura mais antiga para mais recente
- **Todos os demais** → onde ficarão todos os demais documentos que já foram abertos na mesa em questão, respeitando a seguinte hierarquia de ordenação:
  1. Prazo mais próximo de vencer — cada mesa possui o seu prazo, assim, respeita-se esse prazo
  2. Demandas que tiveram geração de notificação para a mesa em questão
  3. Abertura mais antiga para a mais recente
  4. Ordem alfabética

## Regras de status

O status de cada mesa, na visualização de Lista (do setor e do servidor), precisa ser editável para que o servidor possa mudar o status na sua respectiva mesa.

### Mudança de status

> [!note] Anexo
> `Mudanca_de_colunas_na_mesa_do_setor_board_Respondido_por_Alice (1).txt` (2.2 KB)

- No modo de visualização de listagem, a mudança será diretamente na tag do status.
- No modo de visualização painel, a mudança será arrastando de uma coluna para outra.

A mudança entre os status pode ser feita livremente para todos os envolvidos. As exceções serão:

- Um documento do tipo Processo administrativo nunca pode ir para o status de **Em elaboração**.
- Um documento que está **Em elaboração** não pode ter seu status alterado manualmente para **Em tramitação**; para avançar para esse status ele precisa ser emitido, o que automaticamente já o colocaria **Em tramitação**.
- Uma vez que um documento/comunicação oficial é emitido, saindo do status de **Em elaboração** para **Em tramitação**, nunca mais poderá voltar para o status de **Em elaboração**.
- Uma vez que o documento está **Encerrado** no setor dono, a única possibilidade de mudar o status dele para algum outro será manualmente na funcionalidade [Reabrir/Retomar documento](https://app.notion.com/p/Reabrir-Retomar-documento-c67b703bcd564db1a6d92ef5a5215219), diretamente no documento.

Existem duas formas de tirar o documento do status de **Pausado**:

- **Mudando manualmente o status para:**
  - Em aberto (o prazo volta a contar)
  - Em tramitação (o prazo volta a contar)
  - Encerrado (aqui se aplica a regra de servidores que tiverem itens pendentes no checklist)
- **Assim que recebe uma interação**, já sai do status de Pausado e assume o status de **Em tramitação**. Nas mesas dos setores (inclusive o dono) e servidores envolvidos, obedecem às seguintes regras:
  - Se a interação veio de um usuário externo, o documento vai para as mesas de todos os envolvidos na coluna **Em aberto** e a contagem dos prazos é retomada.
  - Se a interação veio de um usuário de um setor envolvido ou do setor dono, na mesa do setor e do servidor que interagiu vai para o status de **Em tramitação**; na mesa dos demais setores e servidores o documento vai para a coluna **Em aberto**.

Outras regras:

- Ao acessar um documento que está na coluna **Em aberto**, caso não haja nenhum servidor do respectivo setor atribuído ainda, o servidor é automaticamente atribuído.
- Ao acessar um documento que está na coluna **Em aberto**, o status é alterado automaticamente para **Em tramitação** na respectiva mesa.
- Uma vez que um documento é mudado para o status **Encerrado**, no modo de visualização listagem ele é jogado para o fim da listagem dos itens dos demais status, obedecendo a ordem de fechamento mais recente para mais antigo.
- Quando uma solicitação externa estiver como **Pausado**, o cidadão pode ainda interagir; mas quando estiver **Encerrado** ele não reabre mais, só interage caso um servidor reabra a demanda.
- Quando um documento é colocado em pausa no setor dono, possui todas as funcionalidades de tramitação na toolbar, mas os prazos que possui são todos pausados.

> [!warning]
> O setor dono, ao alterar o status do setor, implica diretamente no status do documento e vice-versa: se o documento sofre alteração automática no seu status, isso reflete no status do setor dono.

É possível ainda que o documento esteja nos [[#Status de um documento]] definidos anteriormente, mas nas mesas dos setores e servidores envolvidos o status seja outro, pois o status da mesa de cada servidor e setor é individual, para que eles possam organizar suas demandas de acordo com os seus processos. No entanto, existem situações em que o status do documento precisa ser minimamente obedecido pelos status das mesas envolvidas, são elas:

- Quando um documento possui o status de **Em elaboração**, setores e servidores envolvidos não podem colocá-lo, em suas respectivas mesas, para o status de **Em tramitação**. No entanto, podem mudar para os demais status — lembrando que essa alteração aplica-se apenas à mesa do servidor ou setor envolvido, ou seja, não se aplica ao status do documento e do seu setor dono.
- Quando um documento possui o status de **Encerrado**, setores e servidores envolvidos até podem mudar o status dele, mas não de forma direta; para isso precisarão utilizar a funcionalidade [Reabrir/Retomar documento](https://app.notion.com/p/Reabrir-Retomar-documento-c67b703bcd564db1a6d92ef5a5215219).

## Regras de prazo

- Caso o servidor não possua prazo atribuído a ele, é exibido o prazo do setor dele.
- Caso o setor não possua prazo atribuído, é exibido o prazo do documento.
- Caso o documento não possua prazo atribuído, nada é exibido.

## Regras de filtros

Serão disponibilizados dois tipos de filtros:

### Ordenação

- Ordem alfabética (ignora todas as outras regras e ordena unicamente por ordem alfabética)
- Pendente de assinatura
- Pendente de revisão

### Filtro completo

Nesse filtro será possível escolher:

- **Status** (disponível apenas no modo lista) e a ordenação; se não tiver sido combinada com o filtro de "Ordenar por", assume a [[#Regras de ordenação|regra de ordenação]] padrão.
- **Módulo** (para que a busca combine diretamente com ele)
- **Assuntos e Serviços** (dependente de módulo, só fica disponível depois que ele estiver selecionado; é uma escolha múltipla)
- **Data inicial**
- **Data final**
- **Prazos vencidos**
- **"Incluir conteúdo do documento na busca"** (checkbox aninhado a módulos)
  - Ao ativado, permite que tudo o que for digitado no campo de busca seja filtrado nos campos do formulário de abertura dos módulos e serviços/assuntos selecionados no filtro.

#### Regras por tipo de campo

| Tipo de campo | Regra de busca |
| --- | --- |
| Texto pequeno | Considera valor na íntegra |
| Texto grande | Considera valor na íntegra. Desconsiderar tags HTML |
| Número | Considera valor na íntegra |
| E-mail | Considera valor na íntegra |
| Mapa | Considera endereço na íntegra |
| Link | Considera valor na íntegra |
| Arquivo (livre) | Pesquisar por nome |
| Arquivo (identificado) | Pesquisar por nome e label |
| Data e hora | Quando houver duas entradas, considerar ambas; deve considerar igualdade; quando for do tipo Hora, considerar hora e minuto |
| Escolha única/múltipla | Buscar pelos itens selecionados |
| Pessoa | Buscar somente pelo nome da pessoa |
| Setor | Buscar pelo nome e sigla do setor |
| Grupo de campos | Só serão considerados os campos contidos nele |

> [!note] Observações
> - O filtro considerará somente o conteúdo do campo e não o título.
> - Quanto mais campos/dados forem considerados na busca, maior será a quantidade de documentos retornados.
> - Deve ser considerado somente o conteúdo da abertura do documento; despachos, comentários, eventos e documentos relacionados **não** serão considerados na busca.

## Demais regras

- Uma demanda cancelada fica na coluna de **Encerrado** do board, com status de cancelada.
- Quando o documento é reaberto, o status do documento vai direto para **Em tramitação**. No board do setor e do servidor que realizaram a ação de retomar a demanda, também já entra na coluna **Em tramitação**. No board dos demais servidores e setores envolvidos, a demanda vai na coluna **Em aberto**.
- Um documento só pode ser suspenso caso esteja **Em tramitação**. E só terão permissão para realizar essa ação os servidores N1 do setor dono do documento.

## Switch de setores

O switch de setores é uma funcionalidade que permite ao usuário alternar entre diferentes setores dentro da plataforma SoGov.

### Realização do switch

O switch de setores deve ser realizado através de um menu suspenso (select) que lista os setores aos quais o servidor pertence.

### Configuração inicial

No primeiro acesso ao SoGov, o switch deve estar selecionado no setor principal do servidor. Após o primeiro login, o setor selecionado deve ser fixado para a próxima sessão, lembrando o setor no momento do logout.

### Visualização de mesas

Ao acessar as mesas de setores aos quais o servidor pertence, o switch não deve ser alterado. O usuário pode visualizar a listagem de documentos de outros setores sem modificar o setor do switch.

### Mudança de setor

Quando o usuário clicar para mudar o setor, deve ser exibido um carregamento (load) e o usuário deve ser direcionado para a mesa do setor selecionado. Se o usuário mudar para um setor não envolvido no documento atual, um carregamento de 5 segundos deve ser exibido antes de redirecionar para a mesa do novo setor. Se o setor de destino também estiver envolvido no documento, o usuário deve permanecer na visualização do documento após o carregamento.

### Acesso a documentos de setores diferentes

Se o usuário acessar um documento de um setor diferente do setor ativo e o setor ativo não estiver envolvido, o switch deve ser automaticamente ajustado para o setor envolvido no documento. Caso o usuário participe de múltiplos setores envolvidos, o switch será ajustado para o último setor mencionado.

### Documentos pertencentes ao setor atual

Quando o documento pertence ao setor atual do switch e a outros setores, o switch deve permanecer no setor atual, pois ele também está envolvido no documento.

## Alerts

Exibição dos alertas na mesa de trabalho.

- A exibição do alert é independente de switch: se estou acessando a mesa individual ou a mesa dos setores, os alerts são referentes a eles, independentemente do switch.
- Na minha mesa individual, os alerts exibidos nos documentos são referentes ao que me foi solicitado ou mencionado, independentemente do meu setor envolvido nele.
- Na minha mesa, caso num documento eu tenha solicitações de dois setores dos quais faço parte, o alert deve contar as duas solicitações.
- Na mesa dos setores, os alerts exibidos são referentes ao setor: se houver solicitações de assinatura para qualquer usuário do setor, o alert existe.
- Também na mesa do setor, se há menções para usuários do setor no documento (seja em despachos ou comentários), o alert existe e só sai quando cada menção for visualizada. Ou seja, se há 3 menções de usuários, abri o documento e só vi a primeira, ele ainda tem o alert para 2 menções.
- Na visualização de menções em despachos ou comentários dentro do documento, deve ser levado em consideração o switch do setor. Ou seja, se estou vendo o documento do setor A com o switch no setor A, tudo o que eu vir de menções para os servidores do setor A vai sair do alert. O alert também é de cada servidor: se eu vi a menção, o alert some para mim, mas para os demais servidores do setor o alert permanece até que eles vejam.
- A contabilização das visualizações fica a critério de discussão e alinhamento entre Virtus e Sogo, chegando a um resultado que seja viável para ambos.

### Demandas vencidas

Um documento possui tags para sinalizar o vencimento do prazo. Foram feitos os seguintes ajustes:

- A tag "Vence amanhã" foi renomeada para **"Prazo: dd/mm/aa — vence amanhã"**.
- Uma nova tag foi criada para indicar prazos vencidos: **"Prazo: dd/mm/aa — vencido"**.
- Um filtro para demandas vencidas foi adicionado na mesa de trabalho.
- Além disso, a visualização da tela inicial e a visualização interna do documento foram ajustadas.

## Histórico de atualizações

### Atualização na mesa de trabalho — 6 abr 2026

### Copiar dados da mesa — 30 abr 2026

### Salvar conjunto de filtros da mesa de trabalho — 20 mai 2026

# Melhoria no layout da mesa de trabalho

> [!abstract] 🖥️ Evolução da experiência: Nova Mesa de Trabalho
> A Mesa de Trabalho passou por uma reformulação estratégica para simplificar a rotina do usuário, reduzir o cansaço visual e tornar a busca por documentos muito mais ágil. Foram removidos excessos da tela inicial e trazidas ferramentas que dão controle personalizado para o dia a dia do servidor.

#### 1. Separação de contextos: Header e abas

**O que mudou:** o que antes alternávamos entre mesas através de somente um componente, agora é dividido claramente em duas abas principais na barra superior: **"Meus Documentos"** e **"Documentos do Setor"**.

- **Aba Meus Documentos:** terá o mesmo comportamento que hoje já existe em "Minha mesa", porém sem o componente de select — este reservado somente à aba de "Documentos do setor".
- **Aba Documentos do setor:** terá o comportamento que já temos na visualização de documentos de um setor. Este componente também acompanhará um seletor do setor que estará visualizando.

> [!note]
> Mesmo que o usuário alterne de "Documentos do setor" para "Meus documentos", será mantido o setor previamente selecionado.

**Impacto na experiência:** essa divisão aplica o princípio da clareza contextual. O usuário agora escolhe se quer focar exclusivamente nas suas tarefas individuais ou olhar o panorama geral da sua lotação (ex.: GAPRE), eliminando a confusão de ver processos de terceiros misturados aos seus.

#### 2. Filtros rápidos dinâmicos e inteligentes (Filter Buttons)

**O que mudou:** foram introduzidos botões de filtragem rápida logo ao lado do container de busca.

- **Botão "Criados por mim":** filtra na Mesa de trabalho todos os documentos criados por este usuário. Só estará visível durante a visualização de "Meus documentos".
- **Botão "Criados pelo setor":** filtra todos os documentos criados pelo setor que o usuário estiver ativo. Só estará visível durante a visualização de "Documentos do setor".
- **Botão "Favoritos":** disponível em ambas as visualizações. Filtra todos os documentos favoritados pelo usuário. Os documentos favoritados são exclusivos deste usuário — favoritar um documento no setor diz respeito à categorização somente para aquele usuário que clicou, não aplicando aos demais usuários do setor. Esse botão também pode ser usado por usuários que tenham a opção de visualização de mesas alheias.

**Impacto na experiência:** o SoGov agora "pensa" pelo usuário. Se ele está na aba individual, o botão se chama "Criados por mim"; se muda para a aba do setor, o mesmo botão se transforma em "Criados pelo setor". Isso evita erros de interpretação e economiza cliques. Além disso, o filtro de "Favoritos" exibe um contador com o total de itens marcados, servindo como atalho direto para os documentos mais importantes.

#### 3. Simplificação visual da barra de ferramentas

**O que mudou:** os antigos botões de Ordenação e Filtro Avançado, que ocupavam muito espaço com textos explicativos, foram transformados em botões de ícone (Icon Buttons). O botão de ordenação também não mostra mais o texto da opção selecionada diretamente na barra.

**Impacto na experiência:** menos texto significa menos ruído visual. Ao transformar essas ações em ícones limpos e padronizados, abrimos respiro no layout. Quando o usuário clica no botão de Ordenação, uma lista suspensa é exibida, mostrando qual opção está ativa.

#### 4. Layout focado e expansivo (visualização Kanban)

**O que mudou:** a tela inicial foi limpa de forma drástica. As colunas de documentos **Pausados** e **Encerrados** saíram da visualização padrão. Agora o usuário vê apenas 3 colunas: **Em elaboração**, **Aberto** e **Em tramitação**. Com menos colunas na tela, os cards laterais se expandiram para preencher todo o espaço horizontal disponível.

**Impacto na experiência:** foi limitada a quantidade de informações simultâneas para que o usuário foque no que realmente importa: os processos ativos e em andamento. Os cards maiores facilitam a leitura de títulos longos. Para quem ainda precisa gerenciar processos Pausados ou Encerrados, eles não sumiram — basta ativá-los novamente através do painel de Filtros Avançados, e o layout se reorganiza para abrir espaço para eles.

#### 5. Interação direta no card: atalho de favoritos e hover

**O que mudou:** agora é possível favoritar um documento diretamente pelo card através de um ícone de estrela, sem a necessidade de abrir o processo. Além disso, foi resgatado o comportamento visual de hover sobre o card.

**Impacto na experiência:** essa mudança traz agilidade operacional e sensação de controle. O usuário consegue marcar seus documentos prioritários "na mosca" enquanto rola a página, e a resposta visual imediata do card ao passar o mouse valida que aquele elemento é clicável e interativo, tornando a navegação mais viva e intuitiva.

#### 6. Atualização dos Filtros Avançados

**O que mudou:** toda a área interna do painel de Filtros Avançados foi repaginada. Os textos de agrupamento (clusters) e as opções de escolha foram reescritos para termos mais amigáveis e diretos.

**Impacto na experiência:** o filtro avançado deixa de ser uma ferramenta complexa e passa a ser uma extensão natural da busca.

- **Adição do filtro "Exibir documentos pausados e encerrados":** a nova visualização padrão esconderá as colunas de documentos pausados e encerrados; só serão exibidas com esta nova funcionalidade para habilitar a exibição das mesmas.
- **Ajustes de copys:** atenção às atualizações textuais em toda a seção de Filtros Avançados. As copys dos clusters (agrupamentos de filtros) e das opções individuais foram alteradas e revisadas para melhor clareza conceitual.
- **Componentização:** os estados de componentes, interações periféricas e a ação global de "Limpar Filtros" mantêm-se inalterados, preservando os comportamentos e padrões visuais vigentes no ecossistema da plataforma.

> [!quote] Comentário
> **Vinícius** (Jul 6): @Ivo Costa Doc da melhoria de mesa

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] 

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- SGV-9044 (task de origem desta doc)
- SGV-9953 — busca por setores que não participo travava o seletor de setores (relaciona com [[#Switch de setores]])
