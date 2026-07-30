---
tags:
  - qa
  - conhecimento
tipo: modulo
revisado: 2026-07-29
---
# Tramitação

## Visão geral

Regras que definem **quais setores podem criar, receber, tramitar e ver** um documento — configuradas em dois níveis: no **módulo** e, dentro dele, em cada **assunto/serviço**.

> [!important] Herança com sobrescrita
> "Serviços e assuntos herdam as mesmas regras do módulo. No entanto, caso sejam alteradas, elas **sobrescrevem ou somam-se** às regras do módulo, dependendo do cenário."
> Na prática, testar A&S sem olhar a config do módulo dá falso resultado: o que aparece no campo de setor destinatário depende da combinação dos dois níveis.

Duas variáveis atravessam quase toda regra e definem o comportamento esperado:

- **Abertura externa** (o cidadão abre) vs **apenas interna** — muda quais regras existem e quais são obrigatórias.
- **Setor dono** — em módulo com abertura externa é o setado como destinatário; em módulo só interno, é **quem cria**.

## Regras de negócio

### Nível MÓDULO

| Regra | Obrigatória? | Comportamento |
|---|---|---|
| **Setores que recebem e tramitam** | Sempre, independente do tipo de abertura | **Primeira** regra a definir. Escolhe entre todos os setores da organização, quantos quiser. É o universo de onde as outras regras são distribuídas. Se nada for definido em setores destino, **são estes que aparecem no campo de setor destinatário na abertura** |
| **Setores criadores** | Sempre | Exibe os setores de "recebem e tramitam". **Só os selecionados aqui podem criar** documentos do módulo |
| **Setores destino** | Opcional sem abertura externa; **com** abertura externa é obrigatório pelo menos um dos clusters | Dois clusters — ver tabela abaixo |
| **Interações externas** | Obrigatória, **só existe com abertura externa** | Exibe os de "recebem e tramitam". Os habilitados são **os únicos que podem interagir com o cidadão** — despachos, respostas e solicitações de assinatura |
| **Sigilos** | Obrigatória, só com abertura externa **+** parâmetro "permitir mostrar opções de privacidade" | Os selecionados são **os únicos que veem os dados do solicitante e o conteúdo** da abertura quando a demanda é sigilosa, e as demais interações sigilosas do cidadão. Mínimo um setor |

**Setores destino — os dois clusters e a combinação** (é aqui que mora a maior parte das pegadinhas de teste):

| Configuração | Onde vive o "dono" | O que aparece no campo destinatário na abertura |
|---|---|---|
| Só **recebimento automático** | O setor definido no recebimento automático | Setor dono **selecionado e travado** |
| Só **setores que o cidadão pode escolher** | O setor selecionado como destinatário na abertura | Os setores dessa regra — **independente de quem abriu** (cidadão direto, ou servidor em nome do cidadão) |
| **Os dois** | O do **recebimento automático** | Os setores da regra "cidadão pode selecionar" |

Regras gerais dos clusters: exibem os setores de "recebem e tramitam"; quando o campo de setor dono fica ativo é **obrigatório** escolher um; os dois campos só existem com abertura externa e, quando ambos existem, são opcionais mas **ao menos um deve ser configurado**; sem abertura externa existe só o recebimento automático, e aí ele é **inteiramente opcional**.

Pré-seleção do **sigilo**: vêm marcados os de "recebem automaticamente", o setor dono, e os de "disponíveis pro cidadão enviar como destino". Podem ser retirados — **exceto o setor dono**, quando configurado.

### Nível ASSUNTO/SERVIÇO

| Regra | Comportamento |
|---|---|
| **Setores que criam** | Exibe os "Setores Criadores" do módulo; podem ser desmarcados, mínimo um. No campo de assunto/serviço da abertura, **só aparecem os assuntos que o setor criador tem permissão de criar** |
| **Setores que recebem e tramitam** | Exibe os do módulo. Os que estão em "Setores que criam" do próprio A&S vêm marcados **e sem opção de desmarcar**. Desmarcar um (que não seja criador) o exclui da tramitação daquele A&S |
| **Setores responsáveis** | Equivalente ao "Setores Destino" do módulo. Sempre tem recebimento automático; com abertura externa também tem o cluster do cidadão. **Se nenhum setor for definido, valem os do módulo** |
| **Interação externa** | Só com abertura externa no módulo **e** no A&S. Vêm marcados os do recebimento automático e os disponíveis pro cidadão; podem ser desmarcados garantindo **ao menos um** |
| **Sigilo** | Obrigatória, mesmas condições do módulo. Mínimo um setor; o setor dono não pode ser retirado |

> [!warning] Cascata de fallback do campo destinatário
> A regra que decide o que aparece no destinatário desce em cascata: **setores destino do A&S** → se vazio, **setores destino do módulo** → se vazio, **"recebem e tramitam" do A&S**. Testar cada degrau isolado.
>
> E uma sutileza do "setores responsáveis" do A&S: se algum setor for definido lá, "o encaminhamento para os setores definidos no nível do módulo **continuará sendo respeitado**, mas o setor dono passa a ser o selecionado no A&S, substituindo o do módulo".

### Encerramento no setor responsável (~15/06/2026)

Mudança **apenas de regra** (origem: SGV-8962): se o setor responsável já encerrou suas demandas no documento, ele pode **encerrar no seu setor sem encerrar a tramitação do documento como um todo** — passando a ter o mesmo comportamento de um setor participante. Objetivo é enxugar a quantidade de documentos em tramitação exibidos nas mesas.

### Ações de destino na emissão de despacho (SGV-9042)

> [!info] Procedência: **Figma — Tramitação/Handoff** (lido em 29/07/2026), fonte mais atual que o Notion
> A spec do Notion usa "Encerrar no Setor / Encerrar na Mesa"; o Figma usa **"Encerrar para meu setor" / "Encerrar para mim" / "Continuar aberto"**. **Nomenclatura final a confirmar com o time** — análise completa na [[QA Workspace/04 Conhecimento/9042 - Refinamento Ações de Tramitação e Encerramento na Emissão de Despacho|mesa de refinamento arquivada]].

Na emissão de despacho passa a existir o contêiner **"Próximo passo do documento"**, que permite definir o destino no mesmo ato da emissão.

**Elegibilidade** — o contêiner só existe em documento com fluxo de trabalho **configurado e já iniciado**. Fluxo **não iniciado** não pode ser movimentado nem encerrado: o contêiner não aparece e vale a toolbar de fluxo não iniciado. Documento **sem** workflow segue o layout padrão do despacho, sem o contêiner.

**Bloqueio por pendência** (regra central):

- Qualquer ação obrigatória pendente na etapa — **despacho customizado não emitido** ou **assinatura não concluída** — desabilita o select de movimentação, que fica fixo em **"Permanecer na etapa atual"** com tooltip informando a pendência.
- O bloqueio é **total**: inclui avançar, retroceder e **todos os atalhos, nas duas direções**. Não é permitido movimentar etapa com pendência **mesmo que a intenção seja retroceder**.
- Nesse estado, **retroceder ou encerrar só pela toolbar do documento**.
- O select habilita quando **todas** as pendências forem cumpridas.

> [!important] Isto **não** contradiz o Workflow — e a conciliação é o que engana
> A doc de [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]] diz que com ação obrigatória pendente *"a etapa só avança quando o despacho for emitido (**sem ele, só retroceder ou encerrar**)"*. Lido isolado, parece autorizar retroceder pelo contêiner.
>
> As duas regras falam de coisas diferentes:
>
> | Regra | Sobre o quê |
> |---|---|
> | **Workflow** — "sem ele, só retroceder ou encerrar" | O que é **possível no documento** nesse estado: retroceder e encerrar seguem permitidos |
> | **Tramitação/9042** — bloqueio total do select | O que o **contêiner de despacho oferece**: nada de movimentação. O caminho para retroceder/encerrar é a **toolbar** |
>
> Ou seja: retroceder **é permitido**, mas **não pelo contêiner**. Confirmado no Figma em 30/07 (duas leituras) e pelo time.
>
> Precedente de 30/07: eu tratei essa aparente contradição como defeito e cheguei a abrir bug (descartado). Antes de reprovar por aqui, separar **"a ação é permitida?"** de **"este ponto de entrada a oferece?"** — são perguntas diferentes com respostas diferentes.

**Assinatura muda o número de cliques**: o split button mantém "Emitir / Emitir e Assinar", mas se o despacho exigir assinaturas o **avanço não se conclui no mesmo clique** — as solicitações são disparadas *após* a emissão.

**Movimentação × encerramento são independentes e combináveis**: dá pra "Avançar etapa" + "Encerrar para mim" na mesma emissão. As regras de continuar aberto / encerrar para mim / encerrar para meu setor seguem o que **já está implementado na plataforma**.

**Sigilo**: o grupo de sigilo só aparece quando o despacho tem opções de sigilo. Em despacho customizado de etapa, é **herdado da configuração do módulo/serviço/assunto** — **o fluxo de trabalho não configura sigilo**.

### Modal de revisão pré-emissão (~16/03/2026)

As regras do sistema **não exigem mais o crivo da revisão** pra seguir com emissão ou tramitação — então as copies dos modais que orientavam o usuário ficaram desalinhadas da realidade. A entrega é **só atualização de copy**, sem mudança visual. Combinações de situação que têm esse ponto de interação: `Revisão → Assinaturas → Emissão → Publicação`, `Revisão → Assinaturas → Emissão`, `Revisão → Emissão`, `Assinaturas → Emissão`, `Revisão → Emissão → Publicação`, `Assinaturas → Emissão → Publicação`, `Emissão → Publicação`.

### Exibição de conteúdo completo de despachos

Anexos do despacho passam a ser **exibidos mesmo com o conteúdo recolhido** — não é mais necessário clicar em "Exibir detalhes" pra ver anexo. O botão de expansão foi reposicionado e ganhou ajuste estético; o comportamento dele segue o mesmo, **exceto** pelos anexos.

### Regras que moram em outro módulo (não duplicar aqui)

| Assunto | Doc canônica |
|---|---|
| Retificação em qualquer etapa, reinício do fluxo e anulação de eventos (~08/07/2026) | [[Fluxo de trabalho (Workflow)#Retificação de documento em qualquer etapa (~08/07/2026)]] |
| Menção de servidores via "@" em processos (~13/05/2026) | [[Mesa de trabalho]] |
| Tag "Férias" em seletores e solicitações (~22/01/2026) | [[Login]] (cadastro/status do servidor) |
| Regras de A&S do ponto de vista do cadastro | [[Serviços e Assuntos]] |

## Comportamentos observados em teste

- **SGV-6373** (reaberta em DEV, 27/07): os setores das Regras de tramitação **não são mantidos** ao avançar/retroceder etapas na criação de A&S — ver [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|card]].
- **SGV-10451** (aberta em HML, 29/07): ao **encerrar para mim** um documento com fluxo de trabalho, a toolbar exibe só "Reabrir documento" — sem histórico nem baixar documento, obrigando a reabrir o documento pra consultá-lo — ver [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|card]].

## Dúvidas em aberto

- **Documento sem abertura externa pode envolver o cidadão?** Resposta do time em 18/07/2024: "deve ser possível envolver o cidadão, e os setores que podem interagir com ele são todos aqueles que fazem parte do documento". Vale confirmar se segue válido depois das atualizações de 2026 — a regra de "interações externas" só existe com abertura externa, o que aparenta conflitar.
- **Encerramento no setor responsável**: a doc manda "averiguar design no protótipo para visualizar nova toolbar para setores dono" — o comportamento da toolbar não está descrito em texto. **Essa lacuna já produziu bug**: a [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]] (29/07) é exatamente uma toolbar de documento encerrado sem as ações esperadas, e não há regra escrita pra apontar. A fonte que fecharia isso é a **tabela de permissões de encerramento** que o Rafael tem — exportação pendente.

## Cards relacionados

- [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]] — setores das regras de tramitação não mantidos ao navegar etapas na criação de A&S
- [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] — ações de tramitação e encerramento na emissão de despacho (refinada 29/07, em validação em homologação)
- [[QA Workspace/02 Demandas/HML/10451 - Bug Toolbar De Documento Encerrado Para Mim Nao Exibe Historico Nem Baixar|SGV-10451]] — toolbar de documento encerrado "para mim" sem histórico nem baixar documento. Vizinho da 9042 (mesma família "Encerrar para mim / para meu setor"), mas coisa distinta: a 9042 é o **ato** de encerrar na emissão de despacho, a 10451 é o **estado** da toolbar depois de encerrado. Se um fix mexer no outro, vale reteste cruzado

## Referências

- [Tramitação (Notion)](https://app.notion.com/p/alfa-group/Tramita-o-48e0035660f54aa893c246ef91be572a) — página-mãe; esta doc traz só o que serve pra testar. Cenários testados detalhados, protótipos e histórico completo ficam lá.
- Origem desta importação: export `(9+)-tramitação-notion.md` (29/07/2026, 1270 linhas).
