---
tags:
  - qa
  - conhecimento
tipo: modulo
revisado: 2026-08-12
---
# Etiquetas

> [!info] Sobre esta nota
> Importada do Notion em 12/08/2026 (fluxo 8), a partir da página oficial **Etiquetas**. Cobre a base do módulo **mais três entregas distintas** — só a primeira é escopo da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]].

## Visão geral

Etiquetas organizam e filtram documentos nas mesas dos setores. São aplicadas ao documento e aparecem **no card do documento e na header ao acessá-lo**.

**Três contextos de uso:**

| Contexto | Para quê |
|---|---|
| Página da feature de Etiquetas | Gerenciamento centralizado (CRUD) |
| Header do documento | Botão fixo de aplicação |
| Mesa de Trabalho | Filtro por etiquetas e menu via card |

**Permissão:** todos os usuários podem criar, editar e excluir etiquetas.

---

## Regras de negócio

### Tipos

- **Pessoais** — uso individual, sem compartilhamento, só na mesa pessoal.
- **Compartilhadas** — criadas e compartilhadas pelo usuário, ou compartilhadas com setores dos quais ele faz parte, ou da mesma hierarquia.
- **"Urgente"** — etiqueta pré-definida, compartilhada com **todos os setores da instância**, visível a todos. **Não pode ser editada nem excluída**, fica **sempre fixa no topo** das compartilhadas, tem **prioridade de exibição** nas mesas e exibe tooltip no hover.

### Criação

- Obrigatório: **nome**. Opcional: cor e setores de compartilhamento.
- **Nomes iguais são permitidos** — a organização fica a critério do usuário.
- **Pré-visualização em tempo real** das alterações de nome e cor.
- Cor do texto **padrão branca**, alterável por color picker, **independente da cor de fundo**.
- **Limite do nome: 25 caracteres**, com contador `n/25`.

### Compartilhamento e notificação

- Etiqueta compartilhada vai para a seção de compartilhadas e **notifica os servidores dos setores** escolhidos.
- **Quem criou não é notificado**, mesmo pertencendo ao setor que recebeu.
- Clicar na notificação leva à listagem, com foco na etiqueta.

### Subetiquetas

- Criadas a partir da etiqueta-pai. **Herdam o contexto de compartilhamento** dela.
- Subetiqueta de etiqueta pessoal **não oferece setores** para compartilhar.
- Subetiqueta compartilhada é **automaticamente compartilhada com todos os setores da etiqueta-pai**, e todos são notificados.
- Na pré-visualização, o nome da etiqueta-pai aparece **antes** do nome da subetiqueta (hierarquia).
- Editar subetiqueta compartilhada **propaga para todos os setores vinculados à etiqueta-pai**.

### Edição

- Alterações de nome e cor são aplicadas **instantaneamente em todos os documentos** onde a etiqueta aparece.
- **Setor removido**: a etiqueta permanece nos documentos onde já foi aplicada, mas os usuários daquele setor **perdem o acesso** a ela.
- **Pessoal → compartilhada**: ao compartilhar, migra para a coluna de compartilhadas, e **todas as subetiquetas vão junto**.
- **Compartilhada não volta a ser pessoal**: o campo de compartilhamento é obrigatório, precisa de ao menos um setor, e salvar sem setor exibe erro.

### Exclusão

- Setores que tinham acesso **não podem mais aplicá-la** a novos documentos, mas **seguem podendo filtrar e visualizar** documentos que já a contêm.
- Documentos que já têm a etiqueta **não a perdem automaticamente** — só por remoção manual.

### Filtros, listagem e visualização

- Existe item de filtro **"Etiqueta"** nos filtros da mesa.
- A listagem exibe **apenas as etiquetas aplicadas na mesa atual**, em ordem cronológica (mais recente primeiro).
- **Visualização é restrita por permissão**: mesmo que o documento tenha várias etiquetas, cada usuário vê **apenas as compartilhadas com o seu setor**.

---

## Refatoração de Etiquetas (design de 07/05/2026) — escopo da SGV-3234

> [!important] Princípio de consistência
> Todos os fluxos de criação, edição e exclusão feitos **via drawer** usam **exatamente as mesmas regras, validações e diálogos** do fluxo principal da feature. As notificações geradas pelo drawer são idênticas às do fluxo original.

### Menu contextual da etiqueta (ellipsis)

Opções: **Editar** (abre drawer) · **Nova subetiqueta** (só em etiqueta-pai) · **Excluir** (abre diálogo). As opções respeitam as permissões do usuário.

### Menu de aplicação

- Botão **"+ Nova etiqueta"** no header do menu, abrindo o drawer de criação.
- Subetiquetas exibidas com ícone `arrow-turn-down-right`.
- Container mantém padrão de **10 etiquetas**; barra de rolagem ao ultrapassar a altura máxima.
- Header do container **inteiro clicável**, com estado de hover.
- **Ordenação**: sem seleção, por ordem de cadastro/edição; **com seleção, as selecionadas sobem**, respeitando o cluster.

### Pesquisa no menu

- **Com resultados**: a contagem `(n)` do cluster passa a refletir os encontrados; termo destacado; se o termo estiver numa etiqueta com subetiquetas (ou for a pai), retorna **o cluster completo**.
- **Sem resultados**: exibe **"Criar etiqueta [termo]"** como primeira opção → drawer abre com **nome pré-preenchido** e o botão **"Criar e aplicar" já habilitado**.

### Drawer

- Altura proporcional à tela; botões de ação fixos no rodapé.
- Botão primário **habilitado só após preencher o nome**.
- **Ao criar, a etiqueta é automaticamente aplicada ao documento** — sem voltar ao menu.
- Variações: Nova etiqueta · Nova subetiqueta (pessoal/compartilhada, **sem seção de compartilhamento** — herda do pai) · Editar etiqueta (pessoal/compartilhada) · Editar subetiqueta.
- Preview de subetiqueta exibe **"Etiqueta-pai / Nome"**.
- Compartilhamento selecionado abre: seleção de setores com pesquisa, **chips removíveis** (`$sigla ×`) e botão de limpar todos.

### Aplicação por contexto

- **Toolbar** e **card na Mesa de Trabalho**: todos os fluxos de drawer se aplicam igualmente.
- **Header do documento**: botão redesenhado, **posição fixa** (aparece com ou sem etiquetas aplicadas), **sempre no início do container** (não mais ao final das etiquetas), com estados Default e Hover diferenciados.

### Alterações em outros fluxos

- **Página da feature**: novo componente visual; menu contextual substitui a edição inline.
- **Filtro na Mesa de Trabalho**: redesign completo, **barra de pesquisa adicionada**, subetiquetas indentadas com ícone, botões **"Cancelar"** e **"Filtrar"** ao final, clusters com contagem e expansão/retração.
- **Página de criação**: preview atualizado (nome, número do documento, setor responsável, última atividade); **seletores de cor de fundo e de texto agora separados**, cada um pelo `+` do seu campo, **independentes**, com branco pré-selecionado.

### Estados, validações e feedback

| Botão | Regra |
|---|---|
| Criar e aplicar | Desabilitado por padrão; habilita ao preencher o nome |
| Salvar e aplicar | Desabilitado por padrão; habilita ao realizar qualquer edição |
| Criar e aplicar (sugestão) | **Já habilitado** ao abrir, pois o nome vem pré-preenchido |

- **Diálogos de confirmação**: edição com mudança de compartilhamento → "Confirmar edição de etiqueta"; exclusão de compartilhada → "Excluir etiqueta compartilhada" (com aviso de impacto). Todos têm checkbox **"Não quero receber este alerta novamente"**.
- **Toasts** (copy literal, serve para asserção):

| Ação | Mensagem |
|---|---|
| Criação | "Etiqueta criada! A etiqueta foi criada e aplicada com sucesso" |
| Edição | "Etiqueta editada! A etiqueta foi editada e aplicada com sucesso" |
| Exclusão | "Etiqueta excluída com sucesso!" |

---

## Histórico de etiquetas (18/05/2026) — **escopo de outra task**

*Backlog: "[Melhoria-CX] Implementar histórico de alterações no gerenciador de etiquetas". Não é escopo da SGV-3234.*

- Acionado **exclusivamente pelo menu contextual** de etiquetas do container **"Etiquetas Compartilhadas"**; o item é **omitido para a "Urgente"** (padrão do SoGov).
- Modal com linha do tempo cronológica: avatar do autor, nome (substituído por **"Você"** quando é o usuário logado, ou com badge **"SOGOV"** para colaboradores internos), string de ação parametrizada, data e hora.
- A doc traz a **tabela completa de strings parametrizadas** por evento (criação, alteração de nome/cor/cor do texto/compartilhamento, inclusão e remoção de setores em única e múltipla, ciclo de vida de subetiqueta) — consultar no Notion ao validar aquela task.

## Seleção múltipla e etiquetas em massa (22/05/2026) — **escopo de outra task**

*Backlog: "[Melhoria-CX] Aplicação e remoção de etiquetas em massa na mesa de trabalho". Não é escopo da SGV-3234.*

- Modo de seleção múltipla na Mesa de Trabalho, **nos modos Painel e Lista**, ativado por icon-button na barra de pesquisa.
- Cards ficam selecionáveis (checkbox, estados pre-selected/hover/selected); surge **toolbar no rodapé** com contador, "Limpar seleção" e botão "Etiquetas"; algumas funções da página ficam restritas até sair do modo.
- **Drawer com abas "Aplicar etiquetas" e "Remover etiquetas"**.
- **Permissões**: nenhuma regra nova — reaplica exatamente a regra já existente por card.
- Dialog **"Sair do modo de seleção"** com matriz de gatilhos.

---

## Comportamentos observados em teste

- *(a preencher durante a validação da SGV-3234)*

---

## Dúvidas em aberto

- [ ] **"Modal de etiquetas não fecha ao aplicar na mesa"** — relatado no detalhamento original da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]], mas **não há especificação** na doc de design de 07/05. Confirmar com produto/design se entrou na entrega.
- [ ] A doc não define o que acontece ao **exceder 25 caracteres** no nome (bloqueia a digitação ou exibe erro?).
- [ ] O checkbox "Não quero receber este alerta novamente" é **por usuário, por diálogo, ou global**? E onde se desfaz essa escolha?

---

## Cards relacionados

- [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — Refatoração de etiquetas (em validação em DEV)
- SGV-5416 — Teste de usabilidade (backlog), relacionado à 3234 na task

---

## Referências

- Página oficial no Notion: **Etiquetas** (`d7a71ec546714247b09aba146e6a999d`)
- Figma — [Etiquetas / Handoff](https://www.figma.com/design/3KcRVaH0yYJqpiZ3VAGL9d/Etiquetas----Handoff?node-id=2314-1930) · [Etiquetas / Concepção](https://www.figma.com/design/JZajpqQJz3XDNm5Hj7DqX3/Etiquetas---Concep%C3%A7%C3%A3o?node-id=221-132429)
- Mesa de refinamento: [[QA Workspace/04 Conhecimento/SGV-3234 - Refinamento Refatoracao De Etiquetas|SGV-3234 - Refinamento]] *(após arquivamento)*
- Módulo vizinho: [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]]
