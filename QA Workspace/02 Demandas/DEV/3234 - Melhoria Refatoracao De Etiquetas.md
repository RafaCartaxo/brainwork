---
tags:
  - demanda
  - melhoria
  - qa
  - etiquetas
task: "3234"
status: dev
prioridade: alta
mel: ""
data_inicio: 2026-08-12
data_fim: ""
responsavel: Rafael
modulo: etiquetas
---
# Demanda: *[Melhoria] Refatoração de etiquetas

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** DEV (Testando em Dev)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-3234 no Notion](https://app.notion.com/p/alfa-group/Melhoria-Refatora-o-de-etiqueta-2252aec67d30812cabccfd960a82e87b) · Figma — [Etiquetas / Handoff](https://www.figma.com/design/3KcRVaH0yYJqpiZ3VAGL9d/Etiquetas----Handoff?node-id=2314-1930) · [Etiquetas / Concepção](https://www.figma.com/design/JZajpqQJz3XDNm5Hj7DqX3/Etiquetas---Concep%C3%A7%C3%A3o?node-id=221-132429)
> - **Dev:** Lucas Cabral · **Revisores MR:** B. Luan, Marcos Vinicius (MR aprovado para testes em 11/08/2026)
> - **CX:** Edivaldo Lima · **Design:** Ivo Costa, Fernando Junior
> - **Cliente(s) afetado(s):** Todos · **Projeto:** Sustentação · **Funcionalidade:** Etiquetas
> - **Deadline firmado com cliente:** **31/08/2026** (Guamaré) · **Progresso de subitens:** 87,50%

---

> [!abstract] Resumo

Feedbacks do time de CX apontaram fricção na aplicação e criação de etiquetas dentro do documento. A entrega consolida esses pontos numa **refatoração da feature inteira**, especificada na *Documentação de Design — Refatoração de Etiquetas (07/05/2026)*.

O que muda, na prática: a etiqueta ganha **novo componente visual e menu contextual**; o **menu de aplicação** ganha criação direta, pesquisa e nova ordenação; um **drawer** passa a permitir criar e editar etiqueta/subetiqueta **sem sair do documento**; o **filtro da Mesa de Trabalho** ganha barra de pesquisa; e os **seletores de cor de fundo e de texto** passam a ser independentes.

Regras completas do módulo: [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]]. Análise e reconciliação de escopo: [[QA Workspace/05 Refinar/3234|mesa de refinamento]].

---

## Regras de negócio

*Fonte: a doc de design de 07/05/2026, importada em [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|04 Conhecimento/Módulos/Etiquetas]]. O card traz só o que vira asserção; a regra completa mora na doc.*

> [!important] Princípio de consistência
> Todos os fluxos de criação, edição e exclusão feitos **via drawer** usam **exatamente as mesmas regras, validações e diálogos** do fluxo principal da feature. As notificações do drawer são idênticas às do fluxo original.

- **Menu contextual** (ellipsis): Editar · Nova subetiqueta (só em etiqueta-pai) · Excluir — respeitando as permissões do usuário.
- **Drawer**: botão primário habilitado só com o nome preenchido; ao criar, **a etiqueta é aplicada automaticamente ao documento**; subetiqueta não exibe compartilhamento (herda do pai) e o preview mostra `Etiqueta-pai / Nome`.
- **"Urgente"**: não editável, não excluível, fixa no topo das compartilhadas, com prioridade de exibição e tooltip.
- **Pesquisa sem resultado** oferece `Criar etiqueta [termo]`, abrindo o drawer com nome pré-preenchido e botão já habilitado.
- **Cores**: fundo e texto **independentes**, cada um acionado pelo `+` do seu campo; **branco pré-selecionado** no texto.
- **Nome**: limite de **25 caracteres**, com contador `n/25`.

---

> [!warning] Pontos de atenção

- ⚠️ **A descrição consolidada da task subestima o escopo.** O detalhamento antigo lista 5 itens e a "Descrição da tarefa" consolida 3 — mas a spec cobre **4 dos 5**. O item *"não tem busca de filtro na mesa"* está especificado em §7.2 e **entra na validação**, apesar de fora dos 3 consolidados. Reconciliação completa na [[QA Workspace/05 Refinar/3234|mesa de refinamento]].
- ⚠️ **Um item ficou sem especificação**: *"modal de etiquetas não fecha ao aplicar na mesa"*. Está no grupo **H. Fora de execução** e depende de confirmação com produto/design.
- ⚠️ **Subitens em 87,50% e não vieram no export** — não se sabe o que da entrega já subiu. **Reexportar a task com os subitens expandidos antes de fechar a suíte**, sob risco de reprovar o que ainda não foi entregue.
- 🔎 **Escopo vizinho que NÃO é desta task**: *Histórico de etiquetas* (18/05) e *Seleção múltipla / etiquetas em massa* (22/05) têm tasks próprias no backlog. Estão documentados no módulo, mas não geram CT aqui.
- 📅 **Deadline com o cliente é 31/08/2026** e a demanda arrasta desde a **SP7/2025** — sete sprints e seis datas previstas de conclusão.

---

## Plano de teste

| Item | Definição |
|---|---|
| **Demanda** | SGV-3234 — Melhoria (refatoração da feature de Etiquetas) |
| **Responsável** | Rafael |
| **Ambiente** | Desenvolvimento |
| **Escopo** | Componente visual da etiqueta, menu contextual, menu de aplicação, pesquisa, drawer de criação/edição no documento, aplicação por contexto (toolbar, card, header), filtro da Mesa de Trabalho, página de criação e seus seletores de cor, estados, validações e toasts |
| **Fora de escopo** | Histórico de etiquetas (18/05) · Seleção múltipla e etiquetas em massa (22/05) — tasks próprias · Regras de negócio pré-existentes de compartilhamento e notificação, salvo onde a refatoração as toca |
| **Tipos de teste** | Funcional · Interface · Permissão · Negativo |
| **Dependências** | Documento acessível como Servidor · etiquetas pessoais e compartilhadas · ao menos uma etiqueta-pai com subetiquetas · mais de 10 etiquetas para exercitar a rolagem · a etiqueta "Urgente" · perfis com permissões distintas |

**Critérios de aceite**

*Derivados da doc do módulo. Escritos por **comportamento observável** — as medidas de handoff (px, hex, tipografia) estão em Informações adicionais como referência, não como critério ([[Sistema/Skills/SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]]).*

**A. Componente de etiqueta e menu contextual**

- [ ] **CA1** — A etiqueta usa o novo componente visual nos três contextos: página da feature, header do documento e card na Mesa de Trabalho
- [ ] **CA2** — O menu contextual da etiqueta oferece **Editar**, **Nova subetiqueta** e **Excluir**, exibidos conforme as permissões do usuário
- [ ] **CA3** — **"Nova subetiqueta" aparece apenas em etiquetas-pai**, e não em subetiquetas

**B. Menu de aplicação**

- [ ] **CA4** — O menu de aplicação exibe **"+ Nova etiqueta"** no header, e acioná-lo abre o drawer de criação
- [ ] **CA5** — O header do container é clicável em **toda a sua área** e apresenta estado de hover
- [ ] **CA6** — O container mantém o padrão de **10 etiquetas** e passa a exibir barra de rolagem ao ultrapassar a altura máxima
- [ ] **CA7** — Sem seleção, as etiquetas seguem a ordem de cadastro/edição; **com seleção, as selecionadas sobem**, sempre dentro do seu cluster
- [ ] **CA8** — A **"Urgente"** fica fixa no topo das compartilhadas, não pode ser editada nem excluída, e exibe tooltip no hover
- [ ] **CA9** — As subetiquetas são exibidas com ícone próprio e indentação que deixa a hierarquia clara

**C. Pesquisa no menu**

- [ ] **CA10** — Com resultados, a **contagem do cluster reflete o número encontrado** e o termo buscado é destacado
- [ ] **CA11** — Buscar por uma etiqueta que tem subetiquetas (ou pela própria pai) retorna o **cluster completo**
- [ ] **CA12** — Sem resultados, **"Criar etiqueta [termo]"** aparece como primeira opção; ao acioná-la o drawer abre com o **nome pré-preenchido** e o botão **já habilitado**

**D. Drawer**

- [ ] **CA13** — É possível **criar e editar** etiqueta e subetiqueta a partir do próprio documento, sem ir à página da feature
- [ ] **CA14** — Ao criar pelo drawer, a etiqueta é **automaticamente aplicada ao documento**, sem retorno ao menu
- [ ] **CA15** — O drawer de subetiqueta **não exibe seção de compartilhamento** e a subetiqueta **herda os setores** da etiqueta-pai
- [ ] **CA16** — O preview da subetiqueta exibe a hierarquia **"Etiqueta-pai / Nome"**
- [ ] **CA17** — Com compartilhamento selecionado, aparecem seleção de setores **com pesquisa**, **chips removíveis** por setor e opção de **limpar todos**

**E. Aplicação por contexto**

- [ ] **CA18** — Os fluxos de drawer funcionam igualmente pela **toolbar** e pelo **card na Mesa de Trabalho**
- [ ] **CA19** — O botão de etiquetas no **header do documento** tem posição fixa: aparece **com ou sem etiquetas aplicadas** e fica **sempre no início do container**, com estados default e hover diferenciados

**F. Alterações em outros fluxos**

- [ ] **CA20** — Na **página da feature**, o menu contextual substitui a edição inline e a hierarquia etiqueta/subetiqueta é preservada
- [ ] **CA21** — O **filtro de etiquetas da Mesa de Trabalho** tem **barra de pesquisa**, subetiquetas indentadas, botões **"Cancelar"** e **"Filtrar"** ao final, e clusters com contagem e expansão/retração
- [ ] **CA22** — Na **página de criação**, os seletores de **cor da etiqueta** e **cor do texto** são **independentes**, cada um acionado pelo `+` do seu campo, com **branco pré-selecionado** no texto
- [ ] **CA23** — O **preview da página de criação** exibe nome, número do documento, setor responsável e última atividade, atualizando **em tempo real** conforme as cores mudam
- [ ] **CA24** — O texto do **accordion de subetiquetas no card da Mesa** está legível, resolvendo o relato de "muito pequeno"

**G. Estados, validações e feedback**

- [ ] **CA25** — **"Criar e aplicar"** permanece desabilitado até o nome ser preenchido; na criação por sugestão, já vem habilitado
- [ ] **CA26** — **"Salvar e aplicar"** permanece desabilitado até que alguma edição seja feita
- [ ] **CA27** — O nome da etiqueta é limitado a **25 caracteres**, com contador visível
- [ ] **CA28** — Os diálogos de confirmação (edição com mudança de compartilhamento e exclusão de compartilhada) exibem o checkbox **"Não quero receber este alerta novamente"**
- [ ] **CA29** — Os **toasts** de criação, edição e exclusão exibem as mensagens previstas na doc

---

## Casos de teste

*Formato em [[Sistema/Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]] — um CT por critério, agrupados por tema.*

### A. Componente de etiqueta e menu contextual

#### **CT-001 Novo componente visual nos três contextos** *(CA1)*

**Dado** que existem etiquetas aplicadas a um documento
**Quando** eu observo a etiqueta na página da feature, no header do documento e no card da Mesa de Trabalho
**Então** verifico que os três exibem o **mesmo componente novo**, com o padrão visual atualizado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Menu contextual respeita permissões** *(CA2)*

**Dado** que estou logado com um perfil que pode editar e excluir etiquetas, e depois com um que não pode
**Quando** eu aciono o ícone de opções da etiqueta em cada caso
**Então** verifico que as opções **Editar**, **Nova subetiqueta** e **Excluir** aparecem conforme a permissão de cada perfil

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-003 "Nova subetiqueta" só em etiqueta-pai** *(CA3)*

**Dado** que existe uma etiqueta-pai com subetiquetas
**Quando** eu abro o menu contextual da etiqueta-pai e depois o de uma subetiqueta
**Então** verifico que **"Nova subetiqueta" aparece apenas na etiqueta-pai**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Menu de aplicação

#### **CT-004 Botão "+ Nova etiqueta" abre o drawer** *(CA4)*

**Dado** que eu abri o menu de aplicação de etiquetas em um documento
**Quando** eu aciono **"+ Nova etiqueta"** no header do menu
**Então** verifico que o **drawer de criação** é aberto

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005 Header do container clicável em toda a área, com hover** *(CA5)*

**Dado** que o menu de aplicação está aberto
**Quando** eu passo o cursor sobre o header do container e clico em pontos diferentes dele (não apenas no ícone)
**Então** verifico que há **estado de hover** e que **qualquer ponto do header** expande/recolhe o container

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-006 Rolagem ao ultrapassar o padrão de 10 etiquetas** *(CA6)*

**Dado** que existem **mais de 10 etiquetas** disponíveis no cluster
**Quando** eu abro o menu de aplicação
**Então** verifico que o container mantém o padrão de 10 e exibe **barra de rolagem** para as demais

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-007 Ordenação muda com a seleção** *(CA7)*

**Dado** que o menu de aplicação está aberto, sem nenhuma etiqueta selecionada
**Quando** eu observo a ordem, seleciono etiquetas de clusters diferentes e observo de novo
**Então** verifico que sem seleção vale a ordem de cadastro/edição e que, **com seleção, as selecionadas sobem dentro do seu cluster**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-008 Etiqueta "Urgente" fixa, imutável e com tooltip** *(CA8)*

**Dado** que a etiqueta **"Urgente"** existe na instância
**Quando** eu observo sua posição no cluster de compartilhadas, abro seu menu contextual e passo o cursor sobre ela
**Então** verifico que ela está **fixa no topo**, que **não oferece editar nem excluir**, e que exibe **tooltip** no hover

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-009 Subetiquetas exibidas com hierarquia clara** *(CA9)*

**Dado** que existe uma etiqueta-pai com subetiquetas
**Quando** eu expando a etiqueta-pai no menu de aplicação
**Então** verifico que as subetiquetas aparecem com **ícone próprio e indentação**, deixando a hierarquia evidente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### C. Pesquisa no menu

#### **CT-010 Pesquisa com resultados atualiza contagem e destaca o termo** *(CA10)*

**Dado** que o menu de aplicação está aberto
**Quando** eu digito um termo que corresponde a etiquetas existentes
**Então** verifico que a **contagem do cluster passa a refletir o número encontrado** e que o termo aparece **destacado** no resultado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-011 Busca em etiqueta com subetiquetas retorna o cluster completo** *(CA11)*

**Dado** que existe uma etiqueta-pai com subetiquetas
**Quando** eu pesquiso pelo nome da etiqueta-pai e, em seguida, por um termo contido em uma subetiqueta
**Então** verifico que nos dois casos o resultado traz o **cluster completo**, com a pai e suas subetiquetas

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-012 Pesquisa sem resultado oferece criação por sugestão** *(CA12)*

**Dado** que o menu de aplicação está aberto
**Quando** eu digito um termo que **não corresponde a nenhuma etiqueta** e aciono a opção oferecida
**Então** verifico que **"Criar etiqueta [termo]"** aparece como **primeira opção**, que o drawer abre com o **nome já preenchido** e que o botão de criar **já está habilitado**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Drawer

#### **CT-013 Criar e editar etiqueta sem sair do documento** *(CA13)*

**Dado** que estou em um documento
**Quando** eu crio uma etiqueta pelo drawer e, em seguida, edito uma etiqueta existente pelo mesmo caminho
**Então** verifico que as duas ações se completam **sem navegar para a página da feature**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-014 Etiqueta criada é aplicada automaticamente ao documento** *(CA14)*

**Dado** que estou com o drawer de criação aberto a partir de um documento
**Quando** eu preencho o nome e concluo a criação
**Então** verifico que a etiqueta **já aparece aplicada ao documento**, sem que eu precise voltar ao menu e selecioná-la

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-015 Subetiqueta não oferece compartilhamento e herda os setores da pai** *(CA15)*

**Dado** que existe uma etiqueta-pai **compartilhada com setores específicos**
**Quando** eu crio uma subetiqueta a partir dela pelo drawer
**Então** verifico que **não há seção de compartilhamento** no drawer e que a subetiqueta nasce **compartilhada com os mesmos setores da pai**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-016 Preview da subetiqueta exibe a hierarquia** *(CA16)*

**Dado** que estou criando uma subetiqueta pelo drawer
**Quando** eu preencho o nome e observo o preview
**Então** verifico que ele exibe **"Etiqueta-pai / Nome"**, na ordem hierárquica

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-017 Seleção de setores com pesquisa, chips e limpar todos** *(CA17)*

**Dado** que estou criando uma etiqueta pelo drawer
**Quando** eu seleciono a opção de compartilhamento, pesquiso e adiciono setores, removo um pelo chip e aciono limpar todos
**Então** verifico que há **pesquisa de setores**, que cada setor vira um **chip removível** e que **limpar todos** esvazia a seleção

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Aplicação por contexto

#### **CT-018 Fluxos de drawer iguais pela toolbar e pelo card da Mesa** *(CA18)*

**Dado** que eu tenho um documento acessível pela toolbar e pelo card na Mesa de Trabalho
**Quando** eu executo criação e edição de etiqueta pelos dois caminhos
**Então** verifico que os fluxos de drawer se comportam **igualmente** nos dois contextos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-019 Botão de etiquetas fixo no início do header do documento** *(CA19)*

**Dado** que tenho um documento **sem nenhuma etiqueta** e outro **com várias etiquetas aplicadas**
**Quando** eu abro os dois e observo o header
**Então** verifico que o botão de etiquetas **aparece nos dois casos**, **sempre no início do container** (não ao final das etiquetas), com estados default e hover distintos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### F. Alterações em outros fluxos

#### **CT-020 Página da feature usa menu contextual no lugar da edição inline** *(CA20)*

**Dado** que eu acesso a página de gerenciamento de etiquetas
**Quando** eu observo as etiquetas e aciono o ícone de opções
**Então** verifico que a **edição inline foi substituída pelo menu contextual** e que a hierarquia etiqueta/subetiqueta segue preservada

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-021 Filtro de etiquetas da Mesa com pesquisa, clusters e ações** *(CA21)*

**Dado** que eu estou na Mesa de Trabalho
**Quando** eu abro o filtro de etiquetas, pesquiso um termo, expando e retraio um cluster e observo o rodapé do componente
**Então** verifico que existe **barra de pesquisa**, que as subetiquetas aparecem indentadas, que os clusters têm **contagem e expansão/retração** e que há os botões **"Cancelar"** e **"Filtrar"**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

> [!info]- Este CT cobre o item que sumiu da descrição consolidada
> *"Não tem busca de filtro na mesa"* estava no detalhamento original da task e ficou fora dos 3 ajustes consolidados — mas a doc de design especifica a barra de pesquisa em §7.2. Por isso entra na suíte.

**Evidências de Testes:**

---

#### **CT-022 Seletores de cor de fundo e de texto independentes** *(CA22)*

**Dado** que eu estou na página de criação de etiquetas
**Quando** eu observo os campos de cor e altero primeiro a cor da etiqueta e depois a cor do texto
**Então** verifico que os dois seletores são **independentes**, cada um acionado pelo `+` do seu campo, e que a **cor branca já vem pré-selecionada** no texto

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-023 Preview da criação atualiza em tempo real** *(CA23)*

**Dado** que eu estou na página de criação de etiquetas
**Quando** eu preencho o nome e altero as cores
**Então** verifico que o preview exibe **nome, número do documento, setor responsável e última atividade**, e que ele **acompanha as mudanças em tempo real**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-024 Texto do accordion de subetiquetas legível no card da Mesa** *(CA24)*

**Dado** que um documento na Mesa de Trabalho tem etiqueta-pai com subetiquetas aplicadas
**Quando** eu expando o accordion de subetiquetas no card
**Então** verifico que o texto está **legível**, sem a redução que motivou o relato

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### G. Estados, validações e feedback

#### **CT-025 "Criar e aplicar" só habilita com nome preenchido** *(CA25)*

**Dado** que o drawer de criação está aberto com o campo de nome **vazio**
**Quando** eu observo o botão, digito um nome e observo de novo; e depois repito abrindo pela **criação por sugestão**
**Então** verifico que o botão está **desabilitado com o campo vazio**, **habilita ao digitar**, e que na criação por sugestão **já vem habilitado**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-026 "Salvar e aplicar" só habilita após alguma edição** *(CA26)*

**Dado** que abri o drawer de edição de uma etiqueta existente, sem alterar nada
**Quando** eu observo o botão de salvar e, em seguida, altero um campo qualquer
**Então** verifico que ele estava **desabilitado** e **habilita após a primeira edição**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-027 Limite de 25 caracteres com contador** *(CA27)*

**Dado** que estou no campo de nome da etiqueta
**Quando** eu digito progressivamente até passar de 25 caracteres
**Então** verifico que existe **contador visível** e que o campo **respeita o limite de 25**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

> [!warning]- Comportamento no estouro não está especificado
> A doc define o limite e o contador, mas **não diz** se a digitação é bloqueada ou se aparece mensagem de erro ao exceder. Registrar o que o produto fizer, sem reprovar por isso — está em Dúvidas em aberto na doc do módulo.

**Evidências de Testes:**

---

#### **CT-028 Diálogos de confirmação com checkbox de não repetir alerta** *(CA28)*

**Dado** que eu edito uma etiqueta alterando o compartilhamento e, em outro momento, excluo uma etiqueta compartilhada
**Quando** os diálogos de confirmação são exibidos
**Então** verifico que ambos apresentam o checkbox **"Não quero receber este alerta novamente"** e os botões de cancelar e confirmar/excluir

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-029 Toasts de criação, edição e exclusão** *(CA29)*

**Dado** que eu executo a criação, a edição e a exclusão de uma etiqueta
**Quando** cada ação é concluída
**Então** verifico que os toasts exibem as mensagens previstas: **"Etiqueta criada! A etiqueta foi criada e aplicada com sucesso"**, **"Etiqueta editada! A etiqueta foi editada e aplicada com sucesso"** e **"Etiqueta excluída com sucesso!"**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### H. Fora de execução — registro

*Caso × decisão × motivo.*

| Caso | Decisão | Motivo |
|---|---|---|
| **Modal de etiquetas fecha ao aplicar na mesa** — *Dado que abri o menu de etiquetas pelo card na Mesa, Quando aplico uma etiqueta, Então o modal se fecha sem que eu precise clicar no ícone* | **Não executado nesta rodada** | Relatado no detalhamento original da task, mas **sem especificação** na doc de design de 07/05/2026. Pendência aberta para confirmar com produto/design se entrou na entrega. Só então vira CT executável |

---

> [!danger] Bugs encontrados

Nenhum registrado ainda — validação em DEV começando em 12/08/2026.

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://3234)

As gravações vão **embedadas em cada CT**, no padrão `3234 - EV-NN - CT-NNN[, CT-NNN] - <descrição>.mp4`. Gravação que cobre mais de um caso é **um arquivo só**, referenciado em cada CT com nota de compartilhamento — convenção em [[QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]]. O índice CT × EV entra aqui ao fim da execução.

---

> [!tip] Observações

**Medidas de handoff — referência, não critério.** A doc de design traz especificação visual detalhada. Elas ficam aqui para **localizar o ajuste** e sustentar a conversa com o dev, mas não viram critério de aceite (regra da [[Sistema/Skills/SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]], precedente SGV-10457):

| Elemento | Referência |
|---|---|
| Etiqueta (tag) | Altura 20px · padding lateral 12px · Inter Bold 11px · texto branco `#FFFFFF` pré-selecionado |
| Etiqueta editável | Fundo `#EDF0F8` (default) → `#DFE4F2` (hover) · ícone ellipsis 16px, `#42454D` → `#354984` |
| Título do menu / header do container | Inter 18px regular · ícone 18px · container 40px |
| Subetiquetas | Ícone `arrow-turn-down-right`, Inter Bold 20px, `#A1C2E9` |
| Botão de expansão de subetiquetas | Área clicável = container completo (85px × 36px) |
| Hover do botão de sugestão | Cursor pointer · fundo `#F2F8FD` |

**Análise e reconciliação de escopo** vivem na mesa de refinamento: [[QA Workspace/05 Refinar/3234|05 Refinar/3234]].

---

## Histórico

- 2026-08-12 - 📚 Documentação de Etiquetas importada para [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|04 Conhecimento/Módulos]] (fluxo 8)
- 2026-08-12 - 🔎 Análise (1ª — escopo reconciliado: a spec cobre 4 dos 5 itens do detalhamento original; a descrição consolidada subestimava o escopo)
- 2026-08-12 - 🔎 Gate de doc: **doc respalda** — os critérios derivam da doc de design de 07/05, agora importada como doc do módulo. Lacunas registradas em Dúvidas em aberto (comportamento ao exceder 25 caracteres; alcance do checkbox "não receber este alerta"; e o "modal não fecha", sem spec)
- 2026-08-12 - 📝 Melhoria refinada (critérios de aceite prontos; 29 critérios e 29 CTs, mais 1 caso em registro)
