---
title: Usuário Servidor
tags:
  - qa
  - conhecimento
  - sogov
  - usuario-servidor
tipo: modulo
revisado: 2026-10-14
fonte: https://app.notion.com/p/alfa-group/Usu-rio-Servidor-156e5bf55ab4447d9cc101ad31384984
fonte_criado: 2024-09-17 (Alice Martins)
fonte_ultima_edicao: 2026-10-05 (Vinícius Sogo)
---
# Usuário Servidor

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-14 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria pro módulo em si (campo `Task` vazio no Notion); as atualizações datadas trazem SGV quando existe.

## Visão geral
- Servidores são usuários do tipo **CPF**, participantes das instâncias dos clientes, no **ambiente servidor** — pertencem a setores conforme a hierarquia de cada cliente.
- Usuário único entre ambientes (mesma regra documentada em [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]]): servidor ganha automaticamente um ambiente cidadão correspondente, com switch entre eles; cidadão que passa a trabalhar numa prefeitura (ou em mais de uma) recebe convite pro novo ambiente, mantendo o mesmo usuário e senha.

## Regras de negócio

### Permissões
- Níveis: **Administrador, Administrador Setorial, Nível 1, Nível 2, Nível 3**.
- O detalhe completo — o que cada nível pode em cada funcionalidade do sistema e da tramitação — vive numa página própria do Notion, **"Mapeamento de Permissões dos Servidores - Sistema e Tramitação"**, ainda **não importada** (ver Dúvidas em aberto).

### Cadastro — duas formas
- **Pré-cadastro interno**: feito por um admin/usuário com permissão, dentro do ambiente servidor; precisa ser concluído depois pelo próprio novo servidor.
- **Pré-cadastro externo**: feito pelo próprio usuário via link-convite gerado a partir de um setor do organograma; precisa de aprovação posterior de um admin/usuário com permissão.

#### Pré-cadastro interno
- Campos preenchidos por quem cadastra: CPF (API traz o nome, não editável), E-mail, Matrícula (opcional), Setor principal, Nível de acesso, Setores adicionais + níveis (opcional), Permissões do nível + extras (opcional).
- Permissões do nível do setor principal vêm preenchidas e **não podem ser retiradas**.
- **Regras**:
	- Setor adicional: nível de acesso só pode ser **igual ou menor** que o nível do setor principal.
	- CPF já cadastrado neste workspace → erro "Usuário já cadastrado neste ambiente. Insira um CPF diferente para um novo cadastro" (bloqueia).
	- CPF já com pré-cadastro neste workspace → erro "Este usuário já foi pré-cadastrado. Verifique as informações no gerenciador de pré-cadastros" (bloqueia).
	- CPF inválido → erro no campo, bloqueia avançar.
	- Integração com a API da Receita Federal: todo pré-cadastro valida o CPF e traz o nome completo (não editável).
	- Link do e-mail: validade de **7 dias**; expirado, precisa reenviar pela tela de gerenciamento de pré-cadastros.
	- CPF já cadastrado na base SoGov (cidadão ou outro ambiente) → e-mail de "aceitar convite para novo workspace" + aviso na aba de notificações, se já estiver em algum workspace.
	- CPF novo na base SoGov → e-mail de "Finalizar cadastro".
- **Conclusão pelo servidor convidado** (já tem conta SoGov): informa CPF, Senha da conta SoGov, Assinatura textual, Cargo de contrato, E-mail institucional, Matrícula (opcional), Cargos nos setores. Link valida o CPF específico (não aceita CPF de outro pré-cadastro); validade 7 dias corridos. Ao concluir, vai pra tela de login do cliente.
- **Conclusão pelo novo usuário** (sem conta SoGov): mesmos campos + E-mail pessoal, Data de nascimento (opcional), Sexo (opcional), Telefone celular (opcional), Criar e confirmar senha. Mesmas regras de link.

#### Pré-cadastro externo
- Link gerado a partir de um setor do organograma; **cada clique no menu gera um novo link**.
- Campos variam conforme o CPF já tem conta SoGov ou não (mesmos conjuntos do pré-cadastro interno).
- **Regras**:
	- Setor do link vira o **setor principal** de quem se cadastra por ele.
	- Validade: **7 dias**.
	- Usuário já cadastrado neste workspace **não pode** ser atribuído a um setor por esse link (link é só pra pré-cadastro).
	- CPF já cadastrado neste workspace → erro "Este CPF já está cadastrado neste ambiente, tente Acessar sua Conta" (bloqueia).
	- CPF já com pré-cadastro neste workspace → erro "Você já finalizou seu pré-cadastro. Em breve seu acesso será liberado!" (bloqueia).
	- CPF já cadastrado no SoGov em **outro** workspace/ambiente → pede a senha do usuário e segue um fluxo reduzido (4 passos, com o que já existe pré-preenchido — só pede o que for específico do novo workspace).
- **Aprovação do pré-cadastro externo**: admin/usuário com permissão recebe as respostas com status "A aprovar"; pode verificar, aprovar, excluir ou remover.
	- Aprovar exige informar o **nível de acesso**.
	- Exclusão só é possível **antes** da aprovação (pré-cadastro ainda não aprovado).
	- Aprovado, o usuário já tem acesso conforme as permissões definidas.
	- Aprovação/exclusão gera notificação pro usuário; quem tem permissão de cadastrar é avisado sempre que um pré-cadastro chega ou é aprovado.
	- Fluxo de verificação: "Verificar" no menu meatball → 4 páginas de informação, cada uma com opção de reprovar; reprovar exige motivo, e o usuário reprovado é avisado e excluído da lista.

### Gerenciamento de servidor — filtro clusterizado (12/02/2026)
- Filtro de Nível de acesso na aba "Servidores" do gerenciamento, combinável com Status e com a busca por texto (nome, email, cargo, setor).
- Cluster de Nível de acesso lista: **Administrador, Administrador Setorial, Especialista, Usuário Básico e Somente Leitura** (ver Dúvidas em aberto sobre a divergência de nomes com a seção Permissões).
- Regras de retorno (vazio/erro) continuam as mesmas — só o conteúdo da listagem muda conforme os itens selecionados.
- UI: clusterização visual por grupo dentro do mesmo dropdown; placeholder vira "Filtrar por"; contador de filtros ativos ao fechar o seletor (ex.: "Filtros (3)"); shortcut de remover filtro quando algo está selecionado.

### Histórico de alterações em servidores (23/02/2026)
- Novo item **"Histórico"** no menu meatball — disponível pra servidores já cadastrados e pré-cadastrados (campos variam conforme a categoria).
- Modal: título dinâmico com o nome do servidor; cada registro traz data/hora da alteração; 5 itens por página; altura do modal acompanha o conteúdo até 674px (depois, rolagem); tag **"Você"** quando a alteração foi feita pelo próprio usuário logado.
- Accordion: nasce minimizado; só um aberto por vez (abrir um fecha o anterior).
- **Eventos mapeados**:
	- Pré-cadastro: realização, reenvio de e-mail, finalização.
	- Dados institucionais: Assinatura Textual (edição, não se aplica a pré-cadastrados), E-mail institucional (edição), Matrícula (edição).
	- Setores e cargos: Setor Principal (edição), Cargo (edição, não se aplica a pré-cadastrados), Nível do Setor (edição).
	- Setores adicionais: Setor Adicional (inclusão/edição/remoção), Cargo Adicional (edição, não se aplica a pré-cadastrados), Nível de Acesso (edição).
	- Permissões extras (inserção/remoção): log gerado pra 9 módulos — Organograma, Servidores, Cidadãos, Grupo de Contatos, Assuntos e Serviços, Mesa de Trabalho, Fluxo de Trabalho, Configurações de Órgãos, Estatísticas — cada ação específica (ex.: "Cadastrar setores", "Atualizar servidor") gera log de inserção **e** de remoção, com copy padronizada "Permissão extra de $permissão inserida/removida em $módulo".
- Fluxo: abre o meatball do servidor (cadastrado ou pré-cadastrado) → "Histórico" → modal com os logs filtrados por CPF/Matrícula.

### Permissão de mesas alheias (24/03/2026)
- Sai do cluster de permissões gerais e ganha controle **dedicado no Perfil do Servidor** — novo cluster "Configuração para mesas alheias", com toggle "Habilitar acesso à mesas alheias".
- Toggle desativado por padrão; ativado, expande dois campos; desativado de novo, os campos somem e os valores são **limpos** (evita submissão residual de permissão).
- **Campo 1 — "Setores que o servidor poderá ter acesso à mesa e aos documentos"**: obrigatório com o toggle ativo; lista todos os setores da organização; componente de chips, com overflow mostrando "+N" quando não cabe mais na largura do container.
- **Campo 2 — "Setores que o servidor poderá baixar documentos"**: opcional; **depende do campo 1** — só lista setores já selecionados ali (só pode baixar onde já tem acesso de visualização). Ambos os campos têm atalho "Limpar seleção".
- **Regra de negócio nova**: hoje só quem participa da tramitação pode baixar anexos. Com essa permissão, quem tem visualização da mesa de um setor **e** esse setor selecionado no campo 2 pode baixar anexos de despachos/aberturas **mesmo sem participar da tramitação**. Mas a permissão é **só visualização e download** — ações de toolbar (editar, tramitar, assinar) continuam vedadas pro "visualizador".
- Validação: toggle ativo sem nenhum setor selecionado no campo 1 → erro "Selecione ao menos um setor". Campo 2 vazio não bloqueia salvar.
- Usuários que **já tinham** a permissão antiga (do cluster geral) migram com todos os setores da organização já marcados nos dois campos (podem remover livremente); usuários **novos** configuram manualmente do zero.

### Status no pré-cadastro — data de expiração (18/05/2026)
- Motivado por necessidade de licitação (POC-Natal): listagem de pré-cadastros ganha, no status **"Expirado"**, a **data e hora** em que o convite expirou (reforço — o aviso de validade já existe no momento do envio).
- Tooltips adicionados ao componente de status, exibidos no hover.

### Refatoração de usuários CNPJ — Departamentos (SGV-8883, SGV-8884, SGV-9898, 14/07/2026)
> Doc unificada cobrindo 3 tasks: cadastro rápido de usuário/departamentos (SGV-8883), refatoração externa de usuários CNPJ (SGV-8884) e contato/departamento sem CPF/CNPJ (SGV-9898). Conteúdo primariamente sobre **Usuário Cidadão PJ** — ver também [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]]; aqui ficam as pontas que tocam o lado servidor (gestão de departamentos, tramitação).

- **Problema**: hoje só dá pra mandar demanda pro CNPJ "raiz" (genérico demais) ou pro contato pessoal (se perde quando a pessoa muda de função) — empurra parte da comunicação pra fora da plataforma.
- **Solução — Departamento**: unidade dentro de uma PJ, com nome (obrigatório, até 200 caracteres) e e-mail próprio (obrigatório, canal de comunicação); pertence sempre a um CNPJ (uma PJ pode ter vários); **não tem "responsável"**, só participantes; pode existir **sem participantes** (aí só recebe respostas, sem poder assinar); herda as mesmas regras de visibilidade de módulo/assunto/serviço da PJ.
- **Participante**: usuário externo (PF ou PJ) já cadastrado, vinculado a um departamento; pode participar de vários departamentos (do mesmo CNPJ ou de CNPJs diferentes); cada vínculo tem cargo (até 28 caracteres, aparece na assinatura) + e-mail opcional. Participar de um departamento não muda a vida do cidadão como pessoa física comum (contextos separados, com alternância no ambiente cidadão).
- **3 ações possíveis sobre um documento**: Visualizar (sem identificação) → vê tudo, não dá direito de assinar; Responder (sem identificação) → tramitação de verdade, gera despacho; Assinar (exige identificação completa) → gera selo com CNPJ + departamento + participante responsável.
- **Rastreabilidade**: acesso anônimo pelo e-mail do departamento registra a interação (origem e-mail) + IP; usuário logado reaproveita o evento de visualização já existente (sem duplicar registro); histórico do cidadão PJ ganha eventos de criação/edição/exclusão de departamento e entrada/saída de participante.
- **Gestão no ambiente servidor**:
	- Listagem de cidadãos PJ: primeira coluna passa a exibir a Razão Social; nova coluna de Participantes (soma de todos os departamentos do CNPJ); menu meatball reordenado: Visualizar → Editar → Histórico → Criar departamento (novo) → Convidar via link (novo, só aparece se o CNPJ já tem ≥1 departamento).
	- Criar departamento: pela listagem (meatball) ou durante a edição do CNPJ. Campos: Nome (obrigatório), Email do departamento (obrigatório), Participantes (opcional — seletor só com usuários externos já cadastrados, agrupados PF/PJ com busca, cada um com cargo + e-mail opcional).
	- Convidar participantes: link válido por **7 dias**, gerado via meatball ("Convidar via link" → escolhe o departamento → "Copiar link" só habilita depois da escolha) ou direto no card do departamento (ícone de link copia sem diálogo). Confirmação em ambos: "Link de convite copiado com sucesso! Este convite possui validade de 7 dias".
	- Excluir departamento: bloqueado se tiver pendência (envolvido em documento tramitando — despacho, solicitação de assinatura etc.); sem pendência, exclui livre.
- **Entrada do participante** (aceite do convite): informa CPF/CNPJ no link ou pelo e-mail do departamento → sem cadastro, vai pro fluxo padrão de cadastro do SoGov e volta pra concluir a participação; com cadastro, confirma identidade por senha e confirma a participação.
- **Ambiente cidadão**: home ganha seletor de perfil — demandas pessoais + (se houver) os CNPJs/departamentos vinculados.
- **Na tramitação**:
	- Abertura de documento: campo Pessoa habilitado pra PJ mostra a árvore completa (Cidadãos PF/PJ com departamentos e participantes + Servidores); pode escolher o departamento em si ou um participante lotado nele; emissão não dispara notificação/e-mail (igual hoje).
	- Condição de exibição: departamento só aparece se o campo Pessoa do formulário tiver o checkbox **Pessoa Jurídica** ativo (herda a visibilidade da PJ).
	- Despachos: pode escolher departamento ou usuário do departamento como destinatário; exibe contexto (departamento — empresa); gera notificação pros envolvidos.
	- Assinaturas: lista de signatários busca por departamento ou por usuário lotado; selo informa CNPJ principal + departamento + participante responsável.
	- Notificações/e-mails: templates pra entrada no departamento, remoção, pós-criação pedindo cadastro de participantes, solicitação de assinatura pro departamento, chegada de despacho no e-mail do departamento, apoio ao pré-cadastro na assinatura; fallback de nome em todos: sem nome fantasia → razão social.

### Pré-cadastro rápido de cidadão — PF/PJ/Depto (22/07/2026)
- Atalho **"Novo Cadastro"** em qualquer componente de seleção de usuário/pessoa (solicitante, destinatário de despacho, signatário) — **só no ambiente Servidor**.
- Aparece fixo na base do dropdown ao focar/clicar na busca; com muitos resultados, fica acoplado — só a lista de resultados ganha rolagem.
- Modal com 3 modos: Pessoa Física, Pessoa Jurídica, Departamentos — PF nasce marcado por padrão.
- Campos seguem exatamente o padrão de cadastro já existente (obrigatoriedade detalhada no protótipo).
- **Retenção de dados ao trocar o tipo** (PF↔PJ↔Depto): dados já digitados **não somem** na hora — ficam em memória, só são limpos quando o usuário começa a digitar no novo formulário escolhido.
- Departamento no cadastro rápido segue as mesmas regras de criação da listagem/edição do cliente, **exceto** que não dá pra adicionar participantes nesse modal (só depois, por fora dele).
- Pós-cadastro: flash message de sucesso ("Cidadão cadastrado com sucesso!" / "Departamento cadastrado com sucesso!"); o cidadão recém-criado é selecionado automaticamente no campo de origem; se o e-mail foi preenchido, dispara a notificação padrão de pré-cadastro pra criar senha/finalizar perfil.
- **Exceção pra Signatários**: cidadão cadastrado rápido pode ser criado normalmente, mas só pode ser **vinculado pra assinatura** depois que ele mesmo acessar o e-mail e finalizar o próprio cadastro.

### Rodapé de despachos — assinatura automática personalizada (SGV-10351)
> Chamado #0726-000415, solicitado por servidora de São Gonçalo do Amarante. Referência de comportamento: assinatura de e-mail (Outlook/Gmail).

- Novo card **"Rodapé de despachos"** em Minha conta → Preferências da conta (abaixo dos cards já existentes: telefone no organograma, 2FA, notificações por e-mail).
- Editor de texto rico, mas **só com formatação** (tamanho, estilo, negrito/itálico/sublinhado, listas, alinhamento) — sem link, imagem, menção ou tabela.
- Placeholder dinâmico (campo vazio): monta com os dados do usuário logado, em linhas separadas ("Exemplo: / Atenciosamente, / $Assinatura_textual / $Cargo" — sem cargo, a linha some). É só ilustrativo — nunca é salvo.
- Salvar: persiste + flash de sucesso; salvar vazio **remove** o rodapé (sem mensagem de erro). Cancelar: descarta e restaura o último conteúdo salvo.
- **Aplicação**: ao abrir a criação de despacho, o rodapé salvo já aparece inserido no final do corpo; cursor começa **no topo**, acima do rodapé (como num e-mail — o servidor digita a mensagem antes da assinatura); editável/removível **só naquele documento**, sem alterar o cadastro nas preferências; editor do despacho em si **mantém** todos os recursos (link, imagem, tabela) — a restrição de formatação vale só pro editor das Preferências.
- **Regras**: rodapé único por servidor (aplica a todos os despachos, de qualquer setor/lotação); conteúdo 100% estático (sem variáveis dinâmicas tipo [Nome]/[Cargo]); sem limite de caracteres; alterações valem só pra despachos **novos** (documentos já emitidos não mudam); aplica só a despachos, nenhum outro tipo de documento recebe o conteúdo; não substitui a assinatura eletrônica (nome/cargo) já existente — é conteúdo complementar no corpo.
- **Fora de escopo**: variáveis dinâmicas/preenchimento automático, imagens/links/tabelas no rodapé, múltiplos rodapés por entidade/lotação, mudanças na assinatura eletrônica existente, aplicação em outros tipos de documento.

### Tempo de inatividade da sessão (SGV-9149, 05/10/2026)
> Origem: reunião de 24/09 (ata no Google Docs) — esta task cobre só o componente de seleção do tempo; os demais pontos da reunião (instância única ativa + banner, rota de logout sem captcha, limpeza de cache) ficam na especificação técnica, **fora do escopo** aqui.

- Novo card **"Tempo de inatividade da sessão"** em Minha conta → Preferências da conta — a grade de preferências passa de 3 colunas pra **2×2** (esse card ocupa a 4ª posição, ao lado de "Notificações por e-mail"; é o único card com select, os demais têm toggle).
- Select: 15 min / 30 min (padrão) / 1h / 2h / 4h / 6h (teto). Opções acima do teto não aparecem na lista.
- **Regras**:
	- Preferência é **individual** por usuário, vale em qualquer setor onde ele atue.
	- Teto = **50% da validade do token** de autenticação (hoje, token de 12h → teto de 6h); a lista se recalcula se a validade do token mudar.
	- Tempo padrão da plataforma sobe de 20 pra **30 minutos** (quem nunca mexeu na preferência fica em 30).
	- Salvar grava e aplica **na hora**, sem precisar novo login; Cancelar descarta a alteração.
	- Contagem de inatividade reinicia a cada interação do usuário; esgotado o tempo sem interação, encerra a sessão e manda pro login.
	- Validação do teto também no **backend**, não só na lista do frontend — e o teto deve ser derivado da validade do token configurada (sem valor fixo em código).
- Sem impacto nas demais preferências (telefone no organograma, 2FA, notificações por e-mail, rodapé de despachos) nem no fluxo de login.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] **"Mapeamento de Permissões dos Servidores - Sistema e Tramitação"** é citada como a fonte **completa** dos 5 níveis (Administrador, Administrador Setorial, N1, N2, N3), mas é uma página separada no Notion, **não importada**. Sem ela, não dá pra detalhar o que cada nível realmente pode em cada funcionalidade.
- [ ] O filtro clusterizado de 12/02/2026 lista o "Cluster de Nível de acesso" com os rótulos **Administrador, Administrador Setorial, Especialista, Usuário Básico e Somente Leitura** — nomes diferentes dos 5 níveis citados na seção Permissões (N1/N2/N3 em vez de Especialista/Usuário Básico/Somente Leitura). Confirmar se são sinônimos (rótulos de UI diferentes dos nomes internos) ou se são coisas distintas.
- [ ] Na Refatoração de usuários CNPJ (14/07/2026), o próprio Notion marca como "a confirmar" se o CNPJ principal recebe todas as notificações das demandas dos próprios departamentos — "previsto no escopo original", sem confirmação registrada no export.
- [ ] Backlog do Notion cita itens sem SGV que parecem já cobertos pelas atualizações acima — confirmar se são resíduos desatualizados: "Adicionar filtro por tipo de permissão na listagem de servidores" (parece = atualização de 12/02), "[UI/UX] Implementar histórico de alterações feitas no cadastro do servidor" + par "*Implementar histórico..." (parecem = atualização de 23/02), "*Permitir o download de documentos para usuários que possuam a permissão 'Mesas alheias'..." (parece = atualização de 24/03). Export mostra só 3 itens + "5 more…" — os demais não foram vistos.
- [ ] As atualizações de Gerenciamento de servidor (12/02), Histórico de alterações (23/02), Mesas alheias (24/03) e Status no pré-cadastro (18/05) vieram só com título/data, **sem número de SGV/task**.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- **SGV-8883, SGV-8884, SGV-9898** — Refatoração de usuários CNPJ / Departamentos (14/07/2026).
- **SGV-10351** — Rodapé de despachos, assinatura automática personalizada.
- **SGV-9149** — Tempo de inatividade da sessão (05/10/2026).

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] — regra de usuário único entre ambientes; o conteúdo de Departamentos/PJ é primariamente documentado lá.
- [[QA Workspace/04 Conhecimento/Módulos/Usuário Sogo|Usuário Sogo]] — o terceiro tipo de usuário do sistema.
- "Mapeamento de Permissões dos Servidores - Sistema e Tramitação" (Notion, ainda não importada) — detalha as permissões de cada nível por funcionalidade.
