---
title: Assinaturas
tags:
  - qa
  - conhecimento
  - sogov
  - assinaturas
tipo: modulo
revisado: 2026-07-17
fonte: https://app.notion.com/p/alfa-group/Assinaturas-3a34ab9f797643bbb1792b9a3d90cb8e
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-06-30 (Vinícius)
---
# Assinaturas

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-17 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. O export veio com ruído (imagens, âncoras) que foi limpo preservando todas as regras. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

## Definição geral

As assinaturas no SoGov servem para dar validade a um documento quando este precisa de uma camada a mais de segurança: documentos que passarão por auditoria ou fiscalização (prestações de conta para tribunais de contas e afins), que necessitam de autenticação externa (ofícios, alvarás, notas fiscais) ou que serão publicados em outros canais e precisam ter sua veracidade identificada.

Classificação geral:

- **Assinatura eletrônica** — qualquer tipo de validação de documentos por meios eletrônicos. Quando a validação ocorre por meio de certificados digitais, temos as assinaturas digitais.
- **Assinatura digital** — tipo de assinatura eletrônica em que o usuário utiliza um certificado digital validado pela ICP-Brasil para comprovar a sua identidade.

Tipos existentes no SoGov:

| Tipo | Descrição |
|---|---|
| **Eletrônica simples** | Eventos gerados na timeline que identificam os autores (nome, cargo e setor) das ações executadas |
| **Digital SoGov** | Realizada via API da Lacuna com certificados gerados pela própria Lacuna — padrão de certificado digital, mas não emitidos por autoridades vinculadas ao ICP-Brasil; ainda assim têm validade como assinatura digital em várias esferas públicas |
| **Digital ICP-Brasil** | Realizada via API da Lacuna com certificados próprios dos signatários, emitidos por autoridades certificadoras vinculadas ao ICP-Brasil |

## Solicitando assinaturas

O usuário aciona a opção de solicitar assinaturas **num despacho** ou **na toolbar do documento**. A solicitação pode ser para um ou mais signatários, sequencial ou não.

> [!note] O fluxo de solicitação de assinaturas independe do tipo do documento.

### Solicitação não sequencial

> Assinaturas não sequenciais são aquelas que não precisam seguir uma ordem específica para que os signatários assinem.

#### Solicitando de um servidor

O solicitante informa:

- **Signatário** — servidor que pertença a algum setor dentro das regras de tramitação do documento;
- **Setor** — a partir de qual setor o signatário deverá assinar;
- **Papel do signatário** — campo opcional; se em branco, por default assume o cargo do servidor no setor pelo qual assinou;
- **Tipo de assinatura** — SoGov (default) ou ICP;
- **Locais** — onde os signatários precisarão assinar. Uma vez definidos pelo solicitante, **não podem ser mudados pelo signatário** (ele só assina ou recusa). Opções exibidas dependem da origem:
	- **Via toolbar**: documento de abertura e seus anexos + todos os despachos emitidos e seus anexos (escolha múltipla);
	- **Via despacho**: apenas o próprio despacho e seus anexos (escolha múltipla).

#### Solicitando de um cidadão PF ou PJ

O solicitante informa:

- **Signatário** — contato externo (PF ou PJ) cadastrado como cidadão na base do cliente;
- **Papel do signatário** — opcional; se em branco, default é "Signatário";
- **Tipo de assinatura** — SoGov (default) ou ICP;
- **Locais** — mesmas regras do servidor (toolbar = tudo; despacho = só ele e anexos).

> [!note] Observações
> - Numa mesma solicitação o servidor pode definir vários signatários (cada um com as informações acima) e pode incluir a si próprio.
> - Ao fim do ciclo, notificação deve ser enviada ao(s) signatário(s) informando da solicitação.

### Solicitação sequencial

> Assinaturas sequenciais são aquelas em que deve ser seguida uma ordem específica em que os signatários devem assinar.

Além das informações da solicitação normal, define-se a **sequência**. A notificação do primeiro da lista é enviada e, só após ele assinar, a do próximo é disparada.

**Regra crítica**: se um dos signatários da lista sequencial **recusar**, todas as demais assinaturas devem ser **canceladas — inclusive as já efetuadas**.

### Quem pode solicitar assinaturas?

> [!note] Apenas servidores podem solicitar assinaturas (sequenciais ou não). Cidadãos podem apenas assinar.

Níveis que podem solicitar (setor dono e setores envolvidos): **Adm, Adm setorial, N1, N2**.

## Gerenciar solicitação de assinaturas

Só é possível gerenciar solicitações **ainda não executadas**, pontualmente, direto no evento de solicitação. Únicos campos alteráveis:

- Tipo de assinatura;
- Papel do signatário.

É possível **excluir um signatário** da lista; ao confirmar:

- Um subevento é gerado na thread do evento de solicitação informando o cancelamento;
- A tag do signatário no evento principal é atualizada para **Cancelada**.

> [!note] Solicitações já executadas, recusadas ou excluídas não podem ser alteradas no gerenciamento.

### Quem pode gerenciar?

Níveis (setor dono e envolvidos): **Adm, Adm setorial, N1**.

> [!warning] Regra de escopo por setor
> Cada setor só gerencia as **próprias** solicitações, EXCETO o setor dono, que gerencia todas. O CTA de gerenciar só aparece nos eventos de solicitação do setor do usuário. Se o usuário faz parte de mais de um setor solicitante, vê todos os CTAs respectivos; ao acionar um CTA de setor diferente do switch atual, o **switch é trocado automaticamente**.

## Recusando uma solicitação

O signatário (cidadão ou servidor) entra no fluxo de assinatura e aciona **Recusar** → é **exigida justificativa** com o motivo → gera evento e notificação **apenas para o solicitante**.

## Assinando

Formas de assinar:

1. **Via CTA de uma solicitação** recebida — servidores e cidadãos;
2. **Emitindo um despacho e assinando junto** — servidores e cidadãos;
3. **Via toolbar** — escolhe livremente os locais entre todos os passíveis de assinatura no documento — **apenas servidores**;
4. **Via despacho pontual** — escolhe locais entre o despacho em questão e seus anexos — **apenas servidores**.

> [!note] Certificados ICP
> - Na seleção de certificado, só carregam os vinculados ao signatário em questão.
> - PJ com ICP: aceita certificados vinculados diretamente ao CNPJ **ou** ao responsável legal.

### Servidor assinando por conta própria (fluxos 2, 3 e 4)

Informações necessárias antes de confirmar:

- **Setor** — só os setores dele que podem ser envolvidos no documento pela regra de tramitação;
- **Papel do signatário** — opcional; default = cargo no setor pelo qual assinou;
- **Tipo de assinatura** — SoGov (default) ou ICP;
- **Locais** — toolbar = tudo (abertura + anexos + despachos + anexos); despacho = só ele e anexos.

Confirmação:

- **Com SoGov**: insere a senha de acesso ao SoGov → assinaturas realizadas;
- **Com ICP**: seleciona o certificado → insere a senha do SoGov → assinaturas realizadas.

Ações pós-assinatura:

- Notificações para os envolvidos no documento;
- Evento na timeline: ação via toolbar → evento principal; via despacho → evento na thread do despacho.

### Emitindo um despacho e assinando-o

Após preencher o despacho, no momento de "emitir e assinar":

**Para servidores** — Setor (só os envolvíveis pela tramitação), Papel (opcional, default = cargo), Tipo (SoGov default ou ICP), Locais (só o próprio despacho e anexos).

**Para cidadãos** — Tipo (SoGov default ou ICP), Locais (só o próprio despacho e anexos). O cidadão **não define papel** — default "Signatário".

Confirmação igual aos demais (senha SoGov; ICP = certificado + senha). Pós-assinatura: notificações aos envolvidos + evento na thread do despacho.

### Assinando uma solicitação não sequencial

#### Quando há apenas um local (ou combo único)

Ao clicar no CTA: **Recusar** ou **Assinar** (SoGov = senha; ICP = certificado + senha).

> [!note] Servidores podem ainda alterar o tipo de assinatura nesse fluxo.

#### Quando há vários combos de locais

> **Combo** = solicitação de assinatura no documento + um ou mais de seus anexos, ou num despacho + um ou mais de seus anexos.

> [!warning] Regra do combo
> Solicitações que incluem anexos são um **combo único**: o signatário só pode assinar ou recusar o combo **inteiro**. Ex.: solicitaram assinatura no documento, seus anexos, num despacho e seus anexos → não dá pra recusar só o anexo e assinar o despacho. Mas pode recusar o combo "despacho + anexos" e assinar o combo "documento + anexos".

Ações com múltiplos combos:

- **Recusar um combo** — vai combo por combo recusando; ao final insere **justificativa única** para todas as recusas (vieram do mesmo evento);
- **Assinar um combo** — combo por combo, confirmando tudo ao final;
- **Assinar tudo** — sem passar por todos os locais; também pode ser usado após recusar algum combo (assina todo o restante).

Confirmação igual aos demais fluxos (SoGov = senha; ICP = certificado + senha).

> [!note] A recusa só é efetivamente enviada após a conclusão de todo o fluxo (recusando tudo ou recusando parcialmente e assinando o restante).

Pós-assinatura: notificações aos envolvidos + evento na thread do evento de solicitação; havendo recusa, notificações da recusa + subevento na thread da solicitação.

### Assinando uma solicitação sequencial

Mesmo fluxo da não sequencial, com as diferenças:

- Notificações enviadas **só na vez de cada um** (primeiro da lista assina → segundo é notificado, e assim por diante);
- **Recusa de qualquer signatário cancela todas as assinaturas da sequência, inclusive as já efetuadas.**

## Assinaturas em massa

> Possibilidade de um servidor assinar várias solicitações, de vários documentos diferentes, de uma só vez. **Apenas para servidores.**

- Entrada única: **tela inicial do servidor**, no CTA com a quantidade total de solicitações pendentes;
- Exibe, **por documento**, todas as solicitações pendentes dele;
- **Não é possível recusar** solicitações na assinatura em massa.

> [!warning] Conceito de combo na massa é mais abrangente
> Aqui, um combo = **todas** as solicitações de um documento, mesmo que tenham vindo de eventos diferentes. Não dá pra assinar só uma solicitação de um documento e deixar as outras.

Opções:

- **Assinar tudo** — modal:
	- SoGov: 2 steps (senha → "life" com progresso das assinaturas, ex. 3/10);
	- ICP: 3 steps (localizar/validar certificado na máquina → senha → "life");
	- ICP + SoGov misto: segue o fluxo ICP, mas cada solicitação é assinada com o tipo requerido.
	- Ao concluir: modal exibe as assinaturas realizadas em clusters, separadas por documento, com botão de voltar ao início.
- **Assinar por combo** — marca o checkbox do documento → vai pra fila de assinaturas (sai da listagem à esquerda) → na fila, "assinar" abre o modal (2 steps SoGov / 3 ICP). Após confirmação, todas as solicitações daquele usuário naquele documento são realizadas **independente do switch**, com sub-eventos criados em cada solicitação.
- **Assinar vários combos** — insere mais de um documento na fila e assina; mesmo comportamento.

## Fluxos de erro possíveis no momento da assinatura

Previstos em todos os fluxos:

| Erro | Tratamento |
|---|---|
| Senha incorreta | — |
| Senha não inserida | — |
| Ausência de certificado | Informar que nenhum certificado foi identificado na máquina + sugerir prosseguir com assinatura SoGov |
| Certificados inválidos | Informar que os certificados identificados estão inválidos + sugerir prosseguir com SoGov |
| Problema de conexão com a internet | Informar + opção de tentar novamente; se já houve assinatura no meio do processo e ele não quiser continuar, exibir as que foram efetuadas |
| Problema de conexão com a API | Idem acima |

## Regra de alteração de status

Documento/comunicação oficial **Em elaboração**: ao ser assinado, é **imediatamente emitido** e vai para **Em tramitação** na mesa do setor e do servidor em questão. Nas demais mesas:

| Status anterior | Novo status |
|---|---|
| Em aberto | permanece Em aberto |
| Em elaboração | vai para Em tramitação |
| Em tramitação | permanece Em tramitação |
| Pausado | segue as regras de alteração de status do documento pausado (doc "Pausar documento" no Notion) |

Relaciona com [[Mesa de trabalho#Regras de status|regras de status da Mesa de trabalho]].

## Tratamento de anexos inválidos para assinatura

**Problema**: a plataforma permitia solicitar assinatura em anexos tecnicamente inválidos (protegidos por senha etc.), resultando em erro inesperado.

**Solução**: verificação proativa — anexos inválidos ficam **não selecionáveis** nos fluxos de seleção de locais:

- Solicitação via toolbar (seletor de Locais);
- Solicitação via despacho (seletor de Locais).

Especificações de UI:

- **Checkbox `disabled`** nos itens inválidos — sem clique e sem hover de clicabilidade;
- **Tag "Inválido"** ao lado do nome do anexo, com tooltip: *"Este anexo pode estar restringido ou protegido para assinaturas."*

Relacionada à task "Carregar documentos" (Notion).

## Decisões/anotações pós-entrega

- Num despacho emitido via "emitir e assinar": o despacho **é emitido mesmo que haja problema com a assinatura**; se o usuário não assinar e voltar, o despacho permanece emitido.

### Dúvidas Galileu (15/05/2024) — esclarecimentos de conceito

- **Combo**: existe quando há mais de um local de uma mesma parte do documento (ex.: despacho + anexo). Um local só não caracteriza combo.
- **Clusters na UI**: solicitação de assinatura de anexo de despacho → exibe o cluster do despacho contendo só o que foi solicitado. Assinando pela toolbar: cada parte do documento é um cluster (abertura com título do documento; cada despacho um cluster individual).
- **Por conta própria** (sem solicitação): conceito de combo **não se aplica** — o usuário escolhe livremente o que assinar; não há recusa.
- **Novo documento**: após criado, usuário vai direto pra tela de assinatura com apenas o cluster da abertura.
- **Massa com solicitações repetidas**: duas solicitações para a mesma parte com tipos diferentes → o cluster da parte é duplicado, um pra cada tipo (serão duas assinaturas).
- **Info de assinaturas**: avulsas e sequenciais listadas na ordem em que foram solicitadas/aconteceram; sequenciais sempre agrupadas.

### Ajustes na página PAdES (29/05/2024, e-mail Virtus)

Removido background da página PAdES e bordas dos selos; hash abaixo da identificação do documento ao lado do QR code; paginação removida; rodapé removido (infos no cabeçalho); nome do signatário sem bold; selos menores (até 3 por linha); margens da folha PAdES ajustadas; imagem do selo SoGov modificada. Figma: [Handoff Virtus 7](https://www.figma.com/design/EyAXgFj9QWOTxMZBy5syIR/Handoff-Virtus-7?node-id=6144-220).

### Atualizações posteriores (conteúdo não veio no export)

- Atualização Página Extra de Assinaturas — 28/04/2026
- Reposicionamento de selos de assinatura — 28/05/2026
- Tratativa para assinatura de documentos por cidadão PJ sem responsável legal vinculado — 30/06/2026

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] As três atualizações de 2026 (Página Extra, Reposicionamento de selos, PJ sem responsável legal) vieram só como título no export — buscar o conteúdo no Notion e completar aqui
- [ ] Regras do documento Pausado × assinatura dependem do doc "Pausar documento" do Notion — importar também?

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- Bug em refinamento: assinaturas em anexos de documentos retificados não são canceladas corretamente (export em `~/Downloads`, candidato ao fluxo 6 — 05 Refinar)
