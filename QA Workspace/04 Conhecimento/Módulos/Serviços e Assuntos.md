---
title: Serviços e Assuntos
tags:
  - qa
  - conhecimento
  - sogov
  - servicos-e-assuntos
tipo: modulo
revisado: 2026-07-20
fonte: https://app.notion.com/p/alfa-group/Servi-os-e-Assuntos-9273202dadcb409697ba87231de464d4
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-05-11 (Vinícius)
---
# Serviços e Assuntos

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20. A página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste]].

## Visão geral

O gerenciador de Serviços e Assuntos organiza e gerencia categorias, subcategorias, serviços e assuntos. Funcionalidades: aplicação de filtros, busca, criação, edição e suspensão dos que não são mais necessários.

Permissões de criação, edição, exclusão e visualização estão centralizadas na página "Permissões Usuários SoGov" do Notion (não replicadas aqui — ver `fonte` relacionada).

A criação de um serviço/assunto pode ser feita de duas formas:
- **Criação Guiada**: obrigatória para usuários realizando a ação pela primeira vez / sem experiência — orientação passo a passo.
- **Criação Avançada**: para usuários experientes, sem suporte detalhado.

## Regras de negócio

### Criação guiada — etapas

**Seção 01: Informações do Serviço**
- Define nome, descrição e o módulo em que o serviço será disponibilizado.
- Todos os campos são obrigatórios; ausência ou excesso de caracteres exibe mensagens de erro específicas.
- Ao sair da seção: sem nada preenchido → confirmação avisando que nada será salvo; com algo preenchido → aviso permitindo salvar antes de sair.
- Ao selecionar um módulo, a pré-visualização atualiza automaticamente. Só módulos **completamente configurados** no gerenciador de módulos ficam disponíveis para seleção.

**Seção 02: Categorização do Serviço**
- Categoria é obrigatória (busca + listagem + opção de criar nova); tentar prosseguir sem selecionar exibe alerta.
- Criação de categoria: modal com nome e descrição; não pode repetir nome de categoria existente; limites de caracteres — 40 (nome) e 125 (descrição) — com erro se excedidos; campos obrigatórios.
- Subcategoria é opcional; deve pertencer à categoria selecionada; pode repetir nome de outra subcategoria desde que em categorias diferentes.
- Criar subcategoria em categoria diferente da selecionada **não é permitido no modo guiado**, mas é permitido no modo avançado.

**Seção 03: Natureza e Privacidade** — condicional, habilitada só se:
- o módulo vinculado ao serviço tiver um documento do tipo **Processo Administrativo** (se for "Comunicação Oficial" ou "Documento Oficial", a seção fica desabilitada); **e**
- o módulo estiver configurado para permitir abertura externa (essa configuração é replicada no serviço, com possibilidade de edição).
- Se qualquer condição não for atendida, a seção fica desabilitada e o usuário vai direto para Regras de Tramitação.
- Quando ativa: "Permite Abertura Externa" aparece habilitada; "Permite mostrar opções de privacidade" e "Permite despacho(s) sigiloso(s)" vêm configuradas conforme o módulo vinculado.
- "Permite mostrar opções de privacidade" só aparece se "Permite Abertura Externa" estiver habilitado.
- Desmarcar "Permite despacho(s) sigiloso(s)" → pré-visualização muda pra aba de tramitação.
- Desmarcar "Permite mostrar opções de privacidade" → remove o componente de seleção de privacidade do formulário na pré-visualização.
- Desmarcar "Permite Abertura Externa" → remove o componente "Solicitante" da aba de formulário na pré-visualização.

**Seção 04: Regras de Tramitação** — campos de setores:
- **Setores participantes** (obrigatório): vem preenchido por padrão com os setores da configuração de tramitação do módulo (seção 1); pode excluir. Excluído, o setor volta a ficar disponível para readicionar.
- Os campos seguintes só permitem selecionar setores dentro do conjunto de "Setores participantes":
  - **Somente este setor receberá automaticamente** (obrigatório): seleção única.
  - **Somente estes setores poderão criar** (obrigatório): múltipla.
  - **Somente estes setores estarão disponíveis para o cidadão enviar como setor destino**: exibido só se "Permite abertura externa" (seção 3) estiver habilitado.
  - **Somente estes setores poderão ver dados sigilosos** (obrigatório): múltipla; exibido só se "Permite mostrar opções de privacidade" estiver habilitado.
  - **Somente estes setores poderão interagir externamente** (obrigatório): herda automaticamente os setores de "Somente este setor receberá automaticamente" e "Somente estes setores estarão disponíveis para o cidadão enviar como setor destino", mais possibilidade de incluir outros setores participantes.
- **Cidadão Interage Somente na Abertura do Processo** (checkbox): herda o status do módulo vinculado, editável na criação/edição; exibido só se "Permite abertura externa" estiver habilitado. (Efeitos na ótica do cidadão em [[Usuário Cidadão]].)
  - **Ativado**: cidadão só interage na abertura; depois perde a capacidade de responder despachos, criar despachos e anexar arquivos. Exceção — "crédito" de interação: recupera a capacidade quando um servidor o menciona diretamente num despacho (crédito pra despacho de resposta) ou solicita sua assinatura (pode executar a assinatura). Nessa configuração o cidadão só vê o conteúdo completo dos despachos direcionados a ele; os demais aparecem só como "Tramitação interna", sem conteúdo visível.
  - **Desativado**: cidadão interage durante toda a tramitação (responde, anexa, cria interações sem restrição); botões "Finalizar Solicitação" e "Reabrir Solicitação" ficam disponíveis; todos os despachos internos ficam totalmente transparentes/visíveis para ele.

> [!note] Atualização de 23/02/2026 — Abertura externa desmembrada
> Regra reformulada, separando **controle de peticionamento** de **controle de visibilidade** — permite que o cidadão acompanhe a tramitação interna mesmo quando sua interação for restrita à abertura. Configuração feita nos níveis de Serviço e Assunto; aplica-se obrigatoriamente a todos os documentos (existentes e novos) vinculados — não há configuração individual por documento.
>
> - **Toggle "Permite abertura externa"**: gatilho principal. Desativado → cidadão não abre mais processo, mas consegue consultar os seus e tramitar. Ativado → revela os checkboxes abaixo.
> - **Checkbox "Restringir cidadão para interação somente na abertura do processo"**: limita a atuação ao protocolo inicial; sozinho, ainda permite ao cidadão ver toda a tramitação e baixar anexos (respeitando sigilos).
> - **Checkbox "Bloquear conteúdos de despachos e anexos para o cidadão"**: ativa máscara de privacidade — conteúdo dos despachos exibe "Tramitação Interna".
> - **Checkbox "Permite mostrar opções de privacidade"**: habilita ferramentas de sigilo, condicionado à abertura externa estar ativa.
> - Migração: serviços/assuntos que já tinham "Cidadão interage somente na abertura do processo" marcado no banco recebem automaticamente Toggle ativado + Checkbox 1 marcado + Checkbox 2 marcado (mantém o comportamento anterior).
>
> Matriz de comportamento:
>
> | Configuração | Interação do cidadão | Visibilidade dos documentos |
> |---|---|---|
> | Toggle OFF | Nenhuma | Inacessível |
> | Toggle ON + Checkboxes OFF | Em todo o processo | Pública (conteúdo e anexos) |
> | Toggle ON + Checkbox 1 | Somente abertura | Pública (conteúdo e anexos) |
> | Toggle ON + Checkbox 1 + Checkbox 2 | Somente abertura | Oculta ("Tramitação Interna") |
> | Toggle ON + Checkbox 2 | Em todo o processo | Oculta ("Tramitação Interna") |

**Seção 05: Gerenciamento de Prazos**
- Prazo e prorrogações do módulo associado são replicados para o serviço/assunto, editáveis desde que o novo valor seja **igual ou menor** que o do módulo.
- Usuário define se o prazo é contado em dias úteis ou corridos.
- Prorrogações só são permitidas se habilitadas no módulo vinculado; o total combinado (prazo + prorrogações) não pode ultrapassar o limite do módulo.
- A prorrogação não pode ser maior que o prazo inicial; prorrogações subsequentes não podem exceder a anterior.
- Se o toggle "Permitir adicionar prazo oficial" for desativado e reativado, prazo/prorrogações do módulo são restaurados. Se esse toggle estiver desabilitado no módulo (prazo zerado), não é possível reabilitá-lo no serviço/assunto.

**Seção 06: Numeração**
- Cada documento é identificado por numeração composta: geral do módulo + específica do tipo de serviço/assunto dentro do módulo.
- Antes da emissão do primeiro documento: é possível definir/ajustar a numeração inicial; se nada for configurado, o padrão inicia em 1.
- Após a emissão do primeiro documento: **não é mais permitido** alterar ou desativar a configuração de numeração inicial (garante integridade da sequência e evita duplicidades).
- Sistema valida automaticamente para impedir dois documentos com a mesma combinação de sequência + numeração inicial dentro do mesmo Assunto/Serviço.
- Pode-se habilitar numeração sequencial contínua entre anos (não reinicia a cada virada de ano).

### Filtros da listagem
- **Ordenar por**: data de criação ou ordem alfabética.
- **Filtrar por status**: ativos, inativos ou em rascunho.
- **Filtrar por módulo**: exibe só os módulos associados aos serviços/assuntos em exibição (não a listagem completa do sistema).
- Sem filtro aplicado, exibição segue ordem de criação/modificação.

### Restruturação da listagem (v2)
- Funcionalidades anteriores mantidas.
- Opção "Excluir" passou a ficar diretamente no menu meatball nos status "Inativo" e "Rascunho" (antes ficava fora do menu).
- Listagem dividida em duas abas: "assuntos e serviços" e "categorias e subcategorias".
- Filtros unificados.

### Regras de tramitação — seleção de setores (atualização de 30/10/2025)
- Objetivo: separar visualmente setores já selecionados dos ainda disponíveis (antes, todos ficavam na mesma posição da árvore hierárquica, dificultando visualização).
- Afeta as regras: setores criadores, setores que recebem e tramitam, setor destino, interações externas.
- Mudanças em todas as exibições de regras de tramitação: sigla do setor na listagem no padrão `$SIGLA $NOME_DO_SETOR`; placeholder atualizado no campo de busca; filtro com opções "Selecionados"/"Não selecionados"; componente abaixo da lista mostrando os já selecionados; reposicionamento da flash message pós-salvamento.

### Texto padrão em nível de Assunto/Serviço (atualização de 04/02/2026)
- Configuração de texto padrão (default) só é permitida **se não existir** cadastro de texto padrão em nível de Módulo.
- Se não houver configuração no módulo, o texto se aplica só aos documentos gerados a partir deste Serviço/Assunto (não afeta outros do mesmo módulo).
- Precedência: se um texto for adicionado ao Módulo posteriormente, a configuração deste nível é ignorada/sobrescrita pela regra do Módulo.
- Interface: cluster "Exemplo de Preenchimento" com botão para habilitar o cadastro; tooltip "Todos os documentos abertos neste serviço ou assunto terão este conteúdo cadastrado previamente, mas ainda podendo ser editado livremente."; texto salvo no pop-up reflete no campo da tela de configuração; botão "Salvar" do modal inicia desabilitado, só habilita após alguma alteração; exclusão de um modelo exige pop-up de confirmação.
- Experiência do usuário: documento abre com o texto do Assunto/Serviço (ou do módulo, se existir) já preenchido; usuário pode apagar/editar livremente; se aplicar um "Modelo de Texto", o texto do modelo é inserido **após** o texto padrão — o modelo não substitui o padrão a menos que o usuário apague o padrão manualmente antes.
- Logs devem ser gerados no histórico do Assunto/Serviço para: cadastro, edição e exclusão do texto base.

### Página extra de assinaturas com QR-code (atualização de 28/04/2026)
- Funcionalidade controlável em múltiplos níveis:
  - **Nível Módulo**: precisa ser ativada pelo time de CX (parâmetro técnico), na criação/edição do módulo. Uma vez ativo, todos os serviços/assuntos do módulo herdam por padrão a configuração de "Página Extra".
  - **Nível Assunto/Serviço**: administrador pode manter o padrão do módulo ou alterar especificamente. Etapa renomeada para "Numeração e Assinaturas". Se o módulo pai estiver com a função ligada, o checkbox aparece marcado por padrão, mas pode ser desmarcado manualmente. Copy do checkbox: "Documentos possuem página de assinaturas separada".
- Toda alteração dessa configuração é registrada no histórico do módulo/serviço/assunto (eventos: "Ativou a funcionalidade de página extra para assinaturas" / "Desativou...").
- Regras de download/impressão: se houver muitos signatários e não couberem numa única folha extra, o sistema cria páginas subsequentes automaticamente; em arquivos ≤ 2GB paginados, a numeração segue o fluxo lógico incluindo as páginas de assinatura; comentários no despacho são inseridos após o documento, mantendo a página de assinaturas como fechamento oficial.
- Se o parâmetro estiver ativo, o editor de posicionamento manual de assinaturas nunca aparece (aplica-se a todos os modelos de assinatura: direta, sequencial, solicitada). Sem a ativação prévia via CX, as opções não aparecem na edição do módulo.
- Cabeçalho de cada página extra referencia explicitamente o item assinado (ex.: "Página de Assinaturas - Despacho nº 123/2026", "Página de Assinaturas - Anexo: Contrato_Social.pdf"); se os signatários excederem a área útil, o cabeçalho é replicado na página seguinte.
- QR Code: proporção 20px x 20px; margens de 8px da borda inferior e 8px da borda esquerda; espaçamento interno de 8px entre o código e o texto indicativo; acompanhado do texto padrão da plataforma para verificação de autenticidade.
- Regra transversal (global update): a inclusão do QR Code e texto de autenticidade no rodapé também se aplica aos fluxos de posicionamento manual de assinatura, independente de a assinatura ter sido posicionada manualmente ou gerada automaticamente na página extra.

### Novos formatos de anexo — KMZ e KML (atualização de 11/05/2026)
- No seletor "Formato(s) suportado(s)", categoria Documentos ampliada com KMZ (dados de mapas compactados) e KML (anotações geográficas e vetores).
- Alteração aplicada tanto em nível de módulo quanto em nível de serviço/assunto.

## Comportamentos observados em teste
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] Item de backlog do export ("[Melhoria] Adicionar novo parâmetro em serviços e assuntos para que possa ser definido se as tramitações internas estarão disponíveis para os cidadãos ou não") — parece já resolvido pela atualização de abertura externa de 23/02/2026 (checkbox "Bloquear conteúdos de despachos e anexos para o cidadão"), mas não há confirmação explícita no export. Validar status real no Notion.
- [ ] "Selos de assinaturas em página extra com qr-code" aparecia como item separado de backlog no board do Notion, mas o export também traz uma seção detalhada "Atualização Página Extra de Assinaturas @April 28, 2026" — não fica claro se o backlog já foi implementado integralmente ou se ainda há partes pendentes.
- [ ] Seção 03 (Natureza e Privacidade): o export não detalha o que muda especificamente se o módulo permitir abertura externa mas o tipo de documento não for "Processo Administrativo" (ou vice-versa) — só afirma que ambas condições precisam ser satisfeitas. Comportamento de borda não descrito.
- [ ] Não há, no export, uma definição explícita da diferença conceitual entre "Serviço" e "Assunto" (o documento trata os dois quase sempre em conjunto/como sinônimos operacionais) — confirmar se há distinção de regra de negócio entre os dois tipos ou se é só nomenclatura conforme o módulo.
- [ ] "Configuração para Abertura Externa" (Seção 03) menciona que a config do módulo "deve ser replicada no serviço em criação, com possibilidade de edição" — não fica claro se há alguma restrição de "igual ou mais restritivo que o módulo" (como existe explicitamente para prazos na Seção 05) ou se a edição é livre em qualquer direção.

## Referências
<!-- Docs do repo (caminho), cards relacionados ([[SGV-XXXX]]), links externos, leis -->
- `packages/e2e/tests/10-ServicosEAssuntos/` (repo Sogov-application) — suíte de testes e2e do módulo (categorias/subcategorias, criação/edição/duplicação de assuntos, listagens, permissões)
- `packages/e2e/pageobject/matterService.elements.ts` (repo Sogov-application) — no código o conceito aparece como "matter service" / "matterService"
- [[Fluxo de trabalho (Workflow)]] — módulo relacionado (regras de tramitação, prazos, prorrogações herdadas/configuradas a nível de módulo)
