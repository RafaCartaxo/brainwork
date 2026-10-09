---
title: Processos Urbanísticos
tags:
  - qa
  - conhecimento
  - sogov
  - urbanistico
  - zoneamento
tipo: modulo
revisado: 2026-10-09
fonte: https://app.notion.com/p/alfa-group/M-dulos-verticais-Processos-Urban-sticos-142012e90eb64b96b0645fd4d4e2dd7c
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-08-19 (Vinícius Sogo)
---
# Processos Urbanísticos

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-09 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Módulo vertical sem task própria (campo `Task` vazio no Notion), documentação de referência desde 2024. Notion marca um **sub-item "Documentação V2"** vinculado a esta página — pode existir versão mais atual não coberta por este export (ver Dúvidas em aberto).

## Visão geral
- Módulo vertical que permite a municípios exibirem informações de zoneamento urbano (zonas + categorias de uso permitidas em cada uma) para consulta prévia de cidadãos e empresas, antes de comprar um terreno ou solicitar um alvará de construção. Facilita o cadastro e a utilização dessas informações para servidores e cidadãos.

## Regras de negócio

### Permissões
- Apenas usuários nível **Administrador** gerenciam zoneamento urbano por padrão.
- Permissão extra pode ser atribuída a servidores de outros níveis, dando acesso total ao gerenciamento da feature no ambiente do cliente.

### Liberando processos urbanísticos para o cliente
- Contratação adicional (como fluxos de trabalho/workflow), habilitada só na **edição** do cliente — não existe na criação.
- Vinculado, aparece a opção de selecionar módulos de processos urbanísticos pro ambiente.
- Só é possível **retirar** o módulo da configuração enquanto o ícone de remoção estiver disponível: antes de salvar a adição, ou quando, após salvar e reabrir pra editar, o módulo ainda não foi vinculado no ambiente técnico.
- Ao vincular, aparece novo item **"Zoneamentos urbanos"** na sidebar do cliente, pra configurar zonas e categorias de uso.
- Processos urbanísticos e fluxos de trabalho são **independentes** entre si — módulos urbanísticos podem ter workflow configurado.

### Criando módulos de processos urbanísticos
- Na criação de módulo, quando o tipo de documento é **processo administrativo**, aparece parâmetro extra pra marcar característica urbanística.
- Ativado, o módulo herda: revisão de todos os PDFs inseridos na tramitação; dois campos dependentes (zona → categoria de uso) que podem ser adicionados à casca na vinculação do módulo ao cliente.

### Gerenciamento e vinculação
- Gerenciamento de módulos urbanísticos segue as mesmas regras/opções dos demais módulos — sem diferença.
- Só é possível vincular módulo urbanístico a clientes com a funcionalidade habilitada.
- Na vinculação, um parâmetro define se os campos zona/categoria entram na casca do formulário; ativado, viram obrigatórios pra abrir o formulário.
- Campos zona/categoria: **dependentes** (categoria só após escolher zona); sem configuração de lógica de exibição; só a largura é editável (mínimo 60%); **opcionais** (pode não ativar).

### Desvincular
- Desvincular o módulo do cliente: notificação enviada; documento perde os campos zona/categoria; módulo some de filtros/listagens por característica urbanística; documentos já abertos **mantêm** as características que tinham.
- Desativar processos urbanísticos no cadastro do cliente: menu "Zoneamento urbanístico" some do ambiente; mapa some; consulta prévia de viabilidade deixa de existir; documentos já abertos **não são impactados**.

### Criação de zoneamentos e categorias de uso
- Zoneamentos: **manual** ou **upload de arquivo `.kmz`** com os dados do município; criado manualmente, dá pra inserir mapa depois.
- Listagem de zonas em ordem alfabética; item recém-criado aparece no topo até a próxima atualização da ordenação.

#### Criação manual
- Campos: nome, descrição, localidade (bairros — vêm da cidade cadastrada no endereço do cliente; sem bairro na lista, cadastra manualmente), categorias de uso (só disponível com ao menos uma categoria já cadastrada).
- Localidade e categorias são **opcionais**, podem ser preenchidas depois.
- Mesmo inserindo mapa depois, a listagem manual é preservada pra quando o usuário quiser voltar a ela.

#### Criação automática (upload do mapa)
- Upload de `.kmz` **sobrescreve** zonas manuais existentes (aviso prévio ao usuário) — reversível, dá pra voltar às zonas manuais depois.
- Vínculos com categorias precisam ser **refeitos**.
- Com mapa, a listagem ganha alternância lista/mapa; o menu da tab ganha publicar/despublicar zoneamento, excluir e substituir mapa.
- Mesmo vindo do mapa, dá pra editar nome, descrição, cor e associar/desassociar categorias das zonas.

### Criação de categoria de uso
- Nome e descrição obrigatórios; associar zoneamento é opcional.
- Parâmetros (detalhamento da categoria), sem limite de quantidade: nome, unidade de medida, valor, observações — só observações é opcional.
- Unidades de medida (mesmas do campo número do construtor de módulos/serviços/assuntos) e símbolo exibido: número simples (sem símbolo), porcentagem (`%`), metros (`m`), metros quadrados (`m²`), quilômetros (`km`), metros cúbicos (`m³`), fórmula matemática (símbolo antes do valor, ex. `ƒ: ALFR = ALFI + [n-4] x 0,20`).
- Zonas publicadas exibem os parâmetros das categorias com valor + símbolo.

### Gerenciamento de zonas e usos

#### Editar zona
- **Sem mapa**: edita tudo (nome, cor, descrição, localidade, categoria); vínculo com categoria é **bilateral** (editar aqui reflete lá).
- **Com mapa**: edita nome, cor, descrição e categoria; localidade **não** é editável (vem do mapa); vínculo com categoria também bilateral.

#### Duplicar zona
- Cópia nasce com nome "Cópia", herdando nome, cor, descrição, categorias e localidades; nomes duplicados são permitidos.
- **Com mapa, zona não pode ser excluída nem duplicada.**

### Publicar/despublicar zoneamento
- Com zonas cadastradas (manual ou mapa), dá pra publicar/despublicar na central de atendimento do cidadão (confirmação via pop-up nos dois sentidos).
- Substituir mapa, voltar pra zonas sem mapa ou excluir mapa **despublica automaticamente** o zoneamento, se estava publicado.

### Mapa
- Gerenciável após inserido: substituir, voltar pra zonas sem mapa, excluir — ações no menu meatball da tab de zonas.
- **Substituir mapa**: exclui permanentemente as zonas atuais e os vínculos de categoria (aviso prévio); exige novo upload `.kmz`.
- **Voltar pra zonas sem mapa**: só existe se havia zonas cadastradas antes do upload; restaura o cadastro anterior substituindo as atuais; despublica o zoneamento (se publicado), que precisa ser publicado de novo.
- **Excluir mapa**:
	- Sem zonas anteriores ao mapa: aviso de perda total → confirma → listagem volta vazia.
	- Com zonas anteriores, três opções:
		- *Excluir mapa e manter zonas atuais*: mantém config (categorias, nome, descrição, localidades); se a API conseguir manter as localidades do mapa, elas continuam na config/contagem e, na edição, só essas aparecem no seletor de bairros (cadastro manual de mais localidades continua disponível); se a API não conseguir, localidades vêm zeradas e o usuário adiciona manualmente.
		- *Excluir e voltar pra versão sem mapa*: restaura zonas e configs anteriores ao upload.
		- *Excluir tudo*: remove mapa, zonas dele e as zonas anteriores a ele (se existirem).

### Histórico de uma zona
- Registra: criação, edição (nome, descrição), localidade (adicionar/excluir), categorias de uso (adicionar/excluir).
- "Criou esta zona" distingue 3 origens: menu, importação do mapa, duplicação.

### Excluir zona
- Processo simples mesmo publicada: confirma pop-up → remove da listagem e da central (se publicada).
- Só é possível excluir zona **sem mapa**.

### Categoria de uso — editar, duplicar, histórico, excluir
- **Editar**: qualquer campo é editável, tudo registrado no histórico.
- **Duplicar**: nasce com o padrão de nomenclatura de cópia do sistema; herda nome, descrição, zonas e parâmetros; nomes duplicados são permitidos.
- **Histórico**: registra todas as ações, agrupadas por seção de edição.
- **Excluir**: remove a categoria e o vínculo nas zonas associadas (pop-up distinto conforme tenha ou não zona vinculada, avisando do impacto quando tem).

### Central de atendimento — Processos Urbanísticos
- Existindo módulos urbanísticos de abertura externa, aparece CTA pra página exclusiva listando esses módulos.
- Com zonas publicadas, aparece CTA pra página de zoneamento (lista todas as zonas do cliente, em modo lista ou mapa).
- Cada zona tem página própria de detalhes (localidades, descrição, categorias de uso e parâmetros); a partir dela, o cidadão pode abrir diretamente um processo urbanístico por um módulo que usa aquela zona/categoria.

### Revisar anexos — API (revisão de documentos)
- Todos os anexos de documentos com característica urbanística podem (não obrigatório) passar por revisão via API específica de processos urbanísticos — vale pra campos de upload e anexos de despacho (customizado ou simples).
- Mesmo upload sem aprovação obrigatória pode ser revisado; o servidor escolhe aprovar, reprovar ou só visualizar.
- Upload que **exige** aprovação: o servidor não precisa decidir na hora — pode sair e voltar ao fluxo de revisão quantas vezes precisar, até concluir e acionar aprovar/reprovar.
- Revisão usa API externa ([PSPDFKit](https://pspdfkit.com/)) com ferramentas de desenho, comentário e escrita pra apontar/destacar situações no arquivo.

### Atualização — Melhoria do visualizador/zoom (SGV-10677, 19/08/2026)
> Origem: SGV-9980 — [MELHORIA-CX] Melhoria do Visualizador/Zoom. Feedback: chegar a 400% exigia ~30 cliques (zoom de 10 em 10% nas lupas +/−); pedido pra digitar o valor ou crescimento geométrico.

- **Solução**: o indicador de zoom vira campo de input editável (inteiros de 1 a 400); as lupas +/− continuam funcionando — o input é caminho adicional, não substituição.
- **Escopo — dois leitores de PDF distintos**:
	- **Leitor 1 — Visualizador interno (SOGOV)**: componente próprio, usado em documentos normais, assinaturas (posicionamento) e visualização geral.
	- **Leitor 2 — Leitor externo**: componente de terceiros, usado na validação de anexos e aplicação de selos em processos urbanísticos.
- **Estados do input de zoom**: Default (mostra valor atual, ex. 100%) → Focus (em edição) → Filled (valor digitado, ex. 400%) → Applied (valor validado e aplicado).
- **Regras de validação — Leitor 1 (interno)**:
	- Digitar `0` → ajusta automaticamente pro piso mínimo de 0,67%.
	- Digitar acima de 400% (ex. 1000%) → ajusta automaticamente pro teto de 400%.
	- Validação/ajuste disparado na confirmação (Enter) ou perda de foco (blur).
	- Campo vazio ou não numérico, ao confirmar → restaura o último valor válido aplicado.
	- **Regras de validação — Leitor 2 (externo)**: não vieram no export (tabela cortada) — ver Dúvidas em aberto.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] Notion lista um sub-item **"Documentação V2"** vinculado a esta página — pode existir versão mais atualizada da documentação, não coberta por este export. Confirmar no Notion.
- [ ] Seção "Criação de zoneamentos e categorias de uso" trouxe no export a nota do próprio autor "(colocar aqui uma explicação do que são as zonas e os usos)" — conceito de zona/categoria de uso não tem definição própria no texto, só é usado operacionalmente. Confirmar definição com Rafael/produto.
- [ ] "Gerenciamento de zonas e usos" trouxe só dois bullets soltos no export ("publicar e despublicar mapa"; "quando não tem mapa, como serão exibidas as zonas na listagem da central de atendimento") sem desenvolver — a segunda pergunta (zonas sem mapa na central) não é respondida em nenhum outro trecho da doc.
- [ ] "Desvincular" lista "ver o que acontece com a tela onde consulta os usos" como anotação solta do autor, sem resposta no texto — comportamento da tela de consulta de usos após desativar processos urbanísticos do cliente fica indefinido.
- [ ] Export cortado no meio da tabela de regras de validação do zoom pro **Leitor 2 (externo)** — só vieram as regras do Leitor 1 (interno). Buscar o restante no Notion (SGV-10677).
- [ ] "Revisar anexos - API": trecho no export tem erro de formatação ("TODOS OS ANEXOSterão", sem espaço) — mantido o sentido (todos os anexos terão possibilidade de revisão), mas confirmar se não falta texto ali.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- **SGV-10677** — [UI/UX] Melhoria do visualizador/zoom (origem SGV-9980) — atualização de 19/08/2026, ver seção acima.
- Sem outro SGV vinculado ao módulo em si (documentação de referência desde 08/07/2024, sem task própria no Notion).
- Possível relação com [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/01 - Demanda|SGV-12082]] — a análise do Termo de Referência está travada aguardando a definição da categoria-base do processo urbanístico do Zoneamento; esta doc pode ser o material de referência que falta pra destravar.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- Leitor externo de PDF usado na revisão de anexos: [PSPDFKit](https://pspdfkit.com/)
