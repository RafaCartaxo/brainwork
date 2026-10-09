---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.42"
paginas_pdf: "p. 19"
status: aprovado
---
# 10 - Personalização e identidade visual do órgão (item 1.42)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Item do TR: **1.42**, coberto recursivamente em todos os subitens numerados que o PDF apresenta (2 linhas na Cobertura: 1.42, 1.42.1). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Página do PDF: **p. 19**, entre 1.41.2.f (recorte 09, já analisado) e 1.43 (recorte 11, não analisado aqui). Listas com letras dentro de um item numerado são conteúdo desse item, não subitens próprios do TR — exceto onde o próprio TR numera. Contexto de produto já confirmado por Rafael (níveis canônicos, visualizar/criar Assuntos e Serviços, status Ativo/Inativo, presença online/offline) **não aparece de forma literal neste recorte** — o TR não nomeia nenhum nível de acesso neste item (diferente do recorte 09, que citou "Visualizador" explicitamente), então não foi aplicado por falta de pertinência textual. Nesta rodada, a análise usou exclusivamente o texto do TR — Conhecimento > Módulos não foi consultado para este recorte.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.42 | Mapeado | Área de personalização de informações relacionadas ao cadastro e à identidade visual do órgão. |
| 1.42.1 | Mapeado | Ações permitidas: (a) acesso a informações cadastrais do órgão — quantidade de licenças, período de contrato, módulos contratados (**o TR não qualifica o modo de acesso — não diz "somente visualização" nem proíbe edição**); (b) edição das cores temáticas da interface do menu principal; (c) upload e gerenciamento das imagens institucionais do órgão, exibidas em todo o sistema. |

**Resultado do recorte:** 2/2 itens (incluindo subitem numerado) considerados; 2 Mapeados, 0 Não aplicáveis. Nenhum item pendente de leitura — pendência de ator registrada em Dúvidas/ambiguidades abaixo.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.42, 1.42.1 | Órgão | Entidade/Ator organizacional | Entidade cujas informações cadastrais e identidade visual são personalizáveis no sistema | quantidade de licenças; período de contrato; módulos contratados; cores temáticas (menu principal); imagens institucionais (exibidas em todo o sistema) | Confirmado |
| 1.42.1.a | Informações cadastrais do órgão | Entidade/Atributo | Dados de cadastro do órgão, acessíveis nesta área — o TR usa "acesso", sem qualificar se é somente visualização ou também edição | quantidade de licenças; período de contrato; módulos contratados | Confirmado quanto à existência do acesso a esses dados; modo de acesso (visualizar somente ou também editar) — **A confirmar** |
| 1.42.1.b, 1.42.1.c | Identidade visual do órgão | Entidade/Configuração | Elementos visuais do sistema, editáveis/gerenciáveis nesta área | cores temáticas (interface do menu principal); imagens institucionais (upload e gerenciamento) | Confirmado |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Órgão | tem | Informações cadastrais (quantidade de licenças, período de contrato, módulos contratados) | 1.42.1.a | Confirmado quanto à existência do acesso; modo de acesso (visualizar somente ou também editar) — **A confirmar**, TR usa apenas "acesso", sem qualificar |
| Órgão | tem (editável) | Identidade visual (cores temáticas, imagens institucionais) | 1.42.1.b, 1.42.1.c | Confirmado |
| Cores temáticas | aplicadas em | Menu principal do sistema | 1.42.1.b | Confirmado |
| Imagens institucionais | exibidas em | Todo o sistema | 1.42.1.c | Confirmado |
| Área de personalização (1.42) | acessível a | Ator não especificado pelo TR neste item | — | A confirmar — ver dúvida abaixo |

## Dúvidas/ambiguidades

- **Ator com acesso à área de personalização (1.42):** o TR descreve a existência da área e as ações permitidas, mas **não especifica qual nível de usuário tem acesso a ela** — diferente do recorte 09 (1.41.1.a), que citou explicitamente o nível "Visualizador". Não apliquei aqui o contexto já confirmado por Rafael sobre criação de Assuntos e Serviços (Administrador/Administrador Setorial), pois é uma regra de outro domínio e não há menção literal de nível neste item — não extrapolo por analogia. Adicionalmente, para as informações cadastrais do órgão (1.42.1.a), o TR usa apenas o verbo "acesso", **sem qualificar se é somente visualização ou se também permite edição** — diferente de (b) e (c), que usam explicitamente "editar" e "upload e gerenciamento". **Pergunta objetiva para Rafael:** (1) qual(is) nível(is) de acesso (Administrador, Administrador Setorial, Especialista, Usuário básico, Somente leitura) tem acesso à área de personalização de cadastro/identidade visual do órgão? (2) o acesso às informações cadastrais (quantidade de licenças, período de contrato, módulos contratados) é somente leitura, ou também permite edição?

## Contexto de produto verificado em documentação (09/10/2026)

> Esta seção registra contexto de produto (Conhecimento > Módulos) — não é requisito literal do TR e não substitui nem resolve a dúvida acima, que permanece registrada tal como está.

- **Nível de acesso à identidade visual do órgão (1.42.1.b/c):** [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]] documenta, na seção "Configurações do órgão", uma permissão única "Visualizar e editar" que "libera no menu profile a opção de configurações do órgão (edição de cores e imagens)", e a tabela de permissões default associa essa funcionalidade ao nível **Administrador**. **Confirmado no produto** — mas só para cores/imagens (1.42.1.b/c). Não se estende a 1.42.1.a (quantidade de licenças, período de contrato, módulos contratados): ambiente e permissão dessa tela específica seguem sem evidência.

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf`, p. 19. Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
- Conhecimento > Módulos: não consultado nesta rodada (análise restrita ao texto do TR).
