---
tags:
  - demanda
  - qa
  - melhoria
  - servicos-e-assuntos
task: "10147"
status: aberto
prioridade: alta
data_inicio: 2026-08-17
data_fim: ""
responsavel: Rafael
modulo: servicos-e-assuntos
ambiente: HOTFIX
---
# Demanda: Permitir configurar múltiplos setores como destino automático

> [!info] Informações
> - **Tipo:** Melhoria (CX)
> - **Status:** Hotfix — aguardando validação em homologação (aprovada em DEV pelo dev em 17/08)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-10147 no Notion](https://app.notion.com/p/alfa-group/MELHORIA-CX-Permitir-configurar-m-ltiplos-setores-como-destino-autom-tico-PM-Guarabira-3a02aec67d308108a6c8ee6040f1b4e3) · Figma — Assuntos e Serviços/Handoff: [nó 2459-611](https://www.figma.com/design/QdlUzvG6molKptfwBTKC0b/Assuntos-e-Servi%C3%A7os---Handoff?node-id=2459-611)
> - **Dev:** João Marcelo · **Revisores MR:** Bruno Clementino, Marcos Vinicius
> - **CX responsável:** Elisa Alves · **Designer:** não atribuído
> - **Cliente afetado:** **Guarabira** · **Funcionalidade afetada:** Serviços e Assuntos
> - **Versão para deploy:** `Hotfix: SGV-10147 12.38.44.2.4`
> - **Progresso de subitens:** 14,29% · Sprints: SP15 (Product designer), SP17 (Engenharia — Melhorias)
> - **Prazo com o cliente:** **17/08/2026** (acordado por Ari Garcia com Bruno Clementino e Alice Martins)

---

> [!abstract] Resumo

Hoje o destino automático de um assunto ou serviço aceita **um único setor**. A melhoria permite configurar **múltiplos setores**, para que a demanda chegue a mais de um setor de uma vez e se evite tramitação manual em fluxos que exigem atuação conjunta.

O modelo entregue é **1 setor responsável + N setores em cópia**: o responsável mantém o comportamento atual (recebe e fica responsável direto), e os setores em cópia entram como **envolvidos** no documento na abertura, **sem** assumir responsabilidade.

Especificação completa (regras, copies e anatomia do evento) em [[QA Workspace/04 Conhecimento/Módulos/Serviços e Assuntos#Múltiplos setores de destino — 1 responsável + N cópias (importado em 17/08/2026)|Serviços e Assuntos → Múltiplos setores de destino]]. **É a única fonte de critério de aceite** — a task não tem designer atribuído nem campos de comportamento preenchidos.

---

## Regras de negócio

Destiladas da doc oficial do módulo (link acima). Resumo operacional:

| Papel | Quantidade | Comportamento |
|---|---|---|
| **Setor responsável** | 1 (único) | Recebe automaticamente e fica **responsável direto** — comportamento já existente |
| **Setores em cópia** | N | Entram como **envolvidos** na abertura, **sem** ficar responsáveis |

- **Pool de opções**: só aparece para cópia o setor que estiver em "Setores que recebem e tramitam".
- **Sem duplicidade**: o setor já escolhido como responsável não aparece na lista de cópia.
- **Opcional**: salvar sem nenhum setor em cópia é válido.
- **Aplicação (padrão SoGov)**: documentos **já criados** mantêm a configuração vigente na criação; **novos** recebem a nova.
- **Abrangência**: módulo, serviço e assunto, com copy contextual por tela.
- **Evento**: nenhum tipo novo — os eventos de criação (cidadão) e emissão (servidor) passam a listar responsável + cópias.

---

> [!warning] Pontos de atenção

- 🚨 **Progresso de subitens em 14,29%** (1 de 7) com status "Disponível para homologação" e 48 cenários aprovados em DEV. Ou o campo está desatualizado, ou **6 de 7 subitens não subiram** — risco de validar em HML o que não foi entregue e aprovar por engano. **Reexportar a task com os subitens expandidos antes de testar.**
- 🚨 **Prazo com o cliente Guarabira era 17/08** — hoje. E o campo oficial "Deadline firmado com cliente" está **vazio**: o prazo só existe no comentário do Ari Garcia de 13/08. Não confundir com o deadline da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]], que é Guamaré em 31/08.
- ⚠️ **Um cenário do dev ficou sem resultado.** Dos 48 itens que o Flávio Oliveira postou como aprovados em DEV, 47 terminam com `- ok`/`- OK`. Este está sem marcador nenhum: *"Selecionar setor em cópia por meio do Organograma expandido"* — justamente a ação **Expandir Organograma**, que a doc lista como parte do componente. Tratar como **não coberto** (CT-003 abaixo).
- ⚠️ **Buraco de cobertura em permissão**: nenhum dos 48 cenários testa se o setor em cópia entra na **herança automática** de "Somente estes setores poderão interagir externamente" — campo que hoje herda do setor destino automático e do setor-destino-do-cidadão. Se herdar, **o cidadão passa a poder interagir com setor que só deveria receber cópia**. É permissão, não layout. Está registrado como dúvida em aberto na doc do módulo e virou o CT-018 aqui.
- ⚠️ **Posição do campo indefinida**: a doc se contradiz entre *"logo abaixo do select de setor responsável"* (2ª posição) e *"3ª posição no cluster"*. O dev validou *"posicionamento — OK"* sem dizer qual. Resolver antes de fechar o CT-002.
- ℹ️ **Sem designer e sem prazo de protótipo** na task, mas **há link de Figma**. Confirmar se o handoff está atualizado para esta entrega antes de usá-lo como referência de layout.
- ℹ️ **Primeiro card em `02 Demandas/Hotfix/`.** A pasta e a regra existem no [[Sistema/Contexto/PADROES_QA#Organização de Bugs|PADROES_QA]] desde sempre, mas nunca tinham sido usadas. Card fica aqui com `ambiente: HOTFIX` durante a validação e vai pra `Concluídas/` quando aprovado; evidências em `Evidências/Hotfix/`.

---

## Casos de teste

Um CT por critério de aceite, derivados da doc do módulo. A lista de 48 cenários do dev foi usada como **cruzamento de cobertura**, não como fonte — os cenários dele que vão além da doc estão nos grupos F e G.

### A. Interface do cluster

#### **CT-001 Cluster renomeado com copy nova** *(CA1)*

**Dado** que estou em Editar serviço → Regras de tramitação
**Quando** localizo o cluster de setores de destino
**Então** verifico que o **title** é `Setores responsáveis` e o **subtitle** é `Selecione um setor do cliente que será responsável direto pelos documentos.`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Campo de cópia com label e posição corretos** *(CA2)*

**Dado** que o cluster "Setores responsáveis" está visível
**Quando** observo a ordem dos campos
**Então** verifico que existe o select com label `Setores que receberão os documentos de abertura deste serviço em cópia (opcional)` na posição definida do cluster

> [!warning]- Posição em disputa — resolver antes de assertar
> A doc diz "logo abaixo do select de setor responsável" (**2ª**) e também "3ª posição no cluster, logo após 'Somente estes setores estarão disponíveis para o cidadão enviar como setor destino'". O dev validou posicionamento como OK sem especificar. Confirmar com produto/dev qual é a correta.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-003 Componente do select: busca, contador e Expandir Organograma** *(CA3)*

**Dado** que abro o select de setores em cópia
**Quando** pesquiso um setor elegível pelo campo de busca, seleciono setores e aciono **Expandir Organograma**
**Então** verifico que a busca filtra, o contador exibe `(N) Setores selecionados` conforme a quantidade, e a seleção pelo organograma expandido funciona

> [!danger]- Cenário sem resultado na validação de DEV
> "Selecionar setor em cópia por meio do Organograma expandido" é o único dos 48 itens do dev **sem marcador de resultado**. Tratar como não coberto e executar com atenção.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-004 Setor responsável continua seleção única** *(CA4)*

**Dado** que estou no cluster "Setores responsáveis"
**Quando** tento selecionar mais de um setor no campo de responsável
**Então** verifico que só **um** setor pode ser escolhido — o comportamento anterior é preservado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Regras de seleção

#### **CT-005 Pool restrito a "Setores que recebem e tramitam"** *(CA5)*

**Dado** que existe um setor **fora** da seleção de "Setores que recebem e tramitam"
**Quando** abro o select de setores em cópia
**Então** verifico que esse setor **não aparece** como opção, e que os setores listados lá aparecem

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-006 Sem duplicidade com o responsável** *(CA6)*

**Dado** que defini um setor como responsável
**Quando** abro o select de setores em cópia
**Então** verifico que o setor responsável **não aparece** na listagem de cópia

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-007 Campo opcional** *(CA7)*

**Dado** que preenchi o cluster sem escolher nenhum setor em cópia
**Quando** salvo a configuração
**Então** verifico que o salvamento conclui sem erro nem obrigatoriedade

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-008 Seleção de múltiplos setores em cópia** *(CA7)*

**Dado** que o select de cópia está aberto
**Quando** seleciono vários setores elegíveis
**Então** verifico que todos são aceitos e o contador reflete a quantidade

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### C. Efeito na abertura

#### **CT-009 Setor em cópia entra como envolvido, não responsável** *(CA8)*

**Dado** que um serviço tem 1 responsável e N setores em cópia configurados
**Quando** um documento é aberto por esse serviço
**Então** verifico que os setores em cópia constam como **envolvidos** e que **nenhum deles** assume responsabilidade durante a tramitação inicial — o responsável direto segue sendo só o setor único

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-010 Documento anterior mantém a configuração vigente** *(CA9)*

**Dado** que existe documento criado **antes** da alteração do campo de cópia
**Quando** consulto seus envolvidos
**Então** verifico que ele mantém a configuração vigente no momento da criação, sem receber a nova regra

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-011 Documento novo recebe a configuração nova** *(CA9)*

**Dado** que alterei os setores em cópia e salvei
**Quando** abro um documento **depois** dessa alteração
**Então** verifico que ele recebe a configuração nova

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Abrangência

#### **CT-012 Mesmo comportamento em módulo, serviço e assunto, com copy contextual** *(CA10)*

**Dado** que a configuração existe nos três níveis
**Quando** abro o cluster em módulo, em serviço e em assunto
**Então** verifico que o campo existe nos três, com o mesmo comportamento, e que a **copy do label acompanha a tela** (não fica fixa em "deste serviço")

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Histórico

#### **CT-013 Histórico de adição com título e formato corretos** *(CA11)*

**Dado** que adicionei setores em cópia e salvei
**Quando** abro o histórico do assunto/serviço
**Então** verifico o bloco com o título `Adicionou estes setores à categoria de setores que recebem os documentos de abertura em cópia` e cada item no formato `$SIGLA/$SIGLA - $Nome_do_setor`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-014 Histórico de remoção com título e formato corretos** *(CA12)*

**Dado** que removi setores em cópia e salvei
**Quando** abro o histórico
**Então** verifico o bloco com o título `Removeu estes setores da categoria de setores que recebem os documentos de abertura em cópia` e os itens no mesmo formato

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-015 Adição e remoção na mesma alteração, e ator correto** *(CA13)*

**Dado** que numa única edição eu adiciono um setor e removo outro
**Quando** salvo e abro o histórico
**Então** verifico que os **dois blocos** aparecem e que o cabeçalho identifica corretamente o ator, nas variações Servidor / Usuário Sogov / Usuário logado ("Você")

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-016 Sem alteração, sem histórico** *(CA13)*

**Dado** que abro a configuração e salvo **sem mexer** no campo de cópia
**Quando** consulto o histórico
**Então** verifico que **nenhuma** entrada nova foi criada para esse campo

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### F. Evento de abertura

#### **CT-017 Evento de criação e de emissão listam responsável + cópias** *(CA14, CA15)*

**Dado** que o serviço tem responsável e setores em cópia
**Quando** um **cidadão cria** e, noutro caso, um **servidor emite** um documento
**Então** verifico as copies `($cargo) $SIGLA` **criou e encaminhou** / **emitiu e encaminhou** `este documento para o(s) seguinte(s) destinatário(s)`, com **todos** os destinatários listados (responsável + cópias)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-018 Anatomia do evento e tipo reaproveitado** *(CA16)*

**Dado** que o evento de abertura foi gerado
**Quando** o inspeciono
**Então** verifico ícone + `$assinatura_textual`, lista de destinatários **expansível** pelo chevron, data e hora, ações **Comentar** e **Responder**, toggle "Ver N interações" — e que **nenhum tipo novo de evento** foi criado, é o existente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-019 Evento sem setores em cópia** *(CA16)*

**Dado** que o serviço **não** tem setores em cópia configurados
**Quando** um documento é aberto
**Então** verifico que o evento se comporta como antes, listando só o responsável

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### G. Transições e regressão

#### **CT-020 Setor em cópia removido de "Setores que recebem e tramitam"** *(CA5)*

**Dado** que um setor já foi selecionado como cópia
**Quando** ele é **removido** da lista de "Setores que recebem e tramitam"
**Então** verifico o que acontece com a seleção de cópia — se cai, se permanece, ou se bloqueia o salvamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-021 Troca do setor responsável reflete na disponibilidade para cópia** *(CA6)*

**Dado** que troquei o setor responsável
**Quando** reabro o select de cópia
**Então** verifico que o **novo** responsável sai da lista de cópia e o **antigo** volta a ficar disponível

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-022 Setor já selecionado como cópia vira responsável** *(CA6)*

**Dado** que um setor está selecionado como cópia
**Quando** eu o defino como **responsável**
**Então** verifico o tratamento da duplicidade — se ele é removido da cópia automaticamente, se o sistema impede, ou se fica nos dois papéis

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-023 Herança em "Somente estes setores poderão interagir externamente"** *(sem CA — comportamento não especificado)*

**Dado** que configurei setores em cópia
**Quando** abro o campo "Somente estes setores poderão interagir externamente"
**Então** verifico **se os setores em cópia foram herdados automaticamente**, como já acontece com o setor destino automático e o setor-destino-do-cidadão

> [!danger]- CT de maior valor da entrega — e sem critério definido
> A doc **não diz** se a cópia entra nessa herança, e **nenhum** dos 48 cenários do dev cobre isso. Se herdar, o cidadão passa a poder interagir com setor que deveria só receber cópia: é **escopo de permissão**, não layout. Qualquer resultado aqui precisa virar decisão de produto e voltar pra doc do módulo.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-024 Não regressão do cluster e da tela** *(CA17)*

**Dado** que só o cluster "Setores responsáveis" deveria mudar
**Quando** percorro os demais campos do cluster e da tela de Regras de tramitação
**Então** verifico que nada mais foi alterado — em especial "Setores participantes", "Somente estes setores poderão criar", "setor destino do cidadão" e "ver dados sigilosos"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

> [!danger] Bugs encontrados

*Nenhum até agora — validação em homologação ainda não iniciada.*

---

## Evidências

*A gravar na validação em homologação. Padrão: `10147 - EV-NN - CT-NNN - <descrição>.mp4`, em `Evidências/Hotfix/`.*

---

> [!tip] Observações

**Validação em DEV (não minha)**: o dev **Flávio Oliveira** postou na task, em 17/08, uma lista de **48 cenários** marcados como aprovados em DEV. Usei essa lista como cruzamento de cobertura contra a doc do módulo, não como fonte dos CTs. O resultado do cruzamento está em **Pontos de atenção**: um cenário sem resultado (Organograma expandido) e um buraco de permissão que a lista não cobre (herança de interação externa).

Cinco cenários dele **vão além** do que a doc descreve e viraram os CTs do grupo G — são transições e casos negativos sem regra escrita. Se passarem, vale levar o comportamento observado de volta pra doc do módulo.

**Registro anterior no vault**: a daily de 10/08 traz `✅ SGV-10147 - Aprovada em homologação`, o que não fecha com a linha do tempo da task (MR só aprovado em 14/08, DEV em 17/08). Por decisão do Rafael em 17/08, esse registro antigo foi desconsiderado e este card representa o ciclo atual, começando em 17/08.

---

## Histórico

- 2026-08-17 - Card criado no vault a partir do export da task, para a validação em homologação (hotfix `12.38.44.2.4`)
