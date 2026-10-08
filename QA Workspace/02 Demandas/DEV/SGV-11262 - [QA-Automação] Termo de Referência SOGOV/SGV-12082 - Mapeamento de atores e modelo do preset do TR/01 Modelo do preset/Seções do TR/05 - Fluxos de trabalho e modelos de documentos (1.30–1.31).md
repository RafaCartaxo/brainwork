---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.30–1.31"
paginas_pdf: "p. 11–13"
status: lido
---
# 05 - Fluxos de trabalho e modelos de documentos (itens 1.30–1.31)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — lido em 08/10/2026, aguardando revisão do Codex
> Itens do TR: **1.30–1.31**, cobertos recursivamente em todos os subitens numerados que o PDF apresenta (18 linhas na Cobertura — 4 sob 1.30, 14 sob 1.31). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Mapa de páginas: 1.30–1.30.1(intro) (p. 11); 1.30.1(configurações)–1.31.1.2 (p. 12); 1.31.1.3–1.31.3 (p. 13). Listas com letras dentro de um item numerado são conteúdo desse item, não subitens próprios do TR — exceto onde o próprio TR numera (ex.: 1.31.2.1.1–1.31.2.1.3.2, que são subitens numerados de verdade, cobertos como tal).

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.30 | Mapeado | Criação/gerenciamento de Fluxo de trabalho, aplicável a qualquer processo administrativo, com etapas configuráveis e ações obrigatórias. |
| 1.30.1 | Mapeado | Configurações de Etapa (nome, setor responsável, regras de tramitação) e do Fluxo como um todo (listagem com filtros, ativar/inativar/duplicar/editar/excluir, histórico, controle de acesso) — detalhado abaixo. |
| 1.30.2 | Mapeado | Etapa pode incluir despacho customizado (formulário próprio) e exigir assinatura obrigatória antes de avançar. |
| 1.30.3 | Mapeado | Regras de transição: etapa só avança após ações obrigatórias concluídas; retrocesso de uma única etapa, com justificativa; checklist de requisitos exibido e registrado de forma transparente ao iniciar a etapa. |
| 1.31 | Mapeado | Modelos de documentos, em 2 categorias ("Modelos Simples" e "Documentos Automatizados"), com herança de dados de um formulário preenchido. |
| 1.31.1 | Mapeado | Modelo simples: integrado ao campo Texto grande/editores de texto dos despachos. |
| 1.31.1.1 | Mapeado | Atributos do Modelo simples: nome, herança de dados (sim/não), categoria/serviço/assunto vinculado (se houver herança), corpo do modelo, exclusividade (próprio servidor ou compartilhado). |
| 1.31.1.2 | Mapeado | Histórico de alterações do modelo (criação/edição/duplicação) para auditoria — data, hora, ação, usuário responsável. |
| 1.31.1.3 | Mapeado | Na tramitação, oferece a opção de inserir um modelo onde houver campo de texto grande/editor. |
| 1.31.1.4 | Mapeado | Só modelos compatíveis com a categoria/serviço/assunto selecionado são exibidos ao usuário. |
| 1.31.2 | Mapeado | Documento automatizado: modelo com herança de dados que gera um documento **independente**, com tramitação própria — distinto do Modelo simples (ver dúvida/achado abaixo). |
| 1.31.2.1 | Mapeado | Introduz os atributos do Documento automatizado, detalhados nos subitens numerados a seguir. |
| 1.31.2.1.1 | Mapeado | Nome do modelo. |
| 1.31.2.1.2 | Mapeado | Categoria de documento, serviço ou assunto ao qual o modelo fica vinculado. |
| 1.31.2.1.3 | Mapeado | Estilização de cabeçalho e rodapé. |
| 1.31.2.1.3.1 | Mapeado | Conteúdo do escopo do modelo, incluindo a herança de dados. |
| 1.31.2.1.3.2 | Mapeado | Validade pré-definida para o documento, contada a partir da emissão. |
| 1.31.3 | Mapeado | Modelos (ambos os tipos) podem ser editados/excluídos conforme permissão, com histórico de alterações. |

**Resultado do recorte:** 18/18 itens (incluindo subitens numerados) considerados; 18 Mapeados, 0 Não aplicáveis. Nenhum item pendente de leitura.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.30 | Fluxo de trabalho | Entidade | Sequência configurável de etapas para tramitação de um processo administrativo | status (ativo, inativo, rascunho — 1.30.1.f.i); histórico de alterações (1.30.1.f.iii) | Confirmado |
| 1.30.1 | Etapa | Entidade | Unidade de um Fluxo de trabalho | nome, setor responsável, regras de tramitação (setores que podem visualizar/participar/retroceder-avançar; setores que podem encerrar/interromper mesmo não sendo a última etapa) | Confirmado |
| 1.30.1, 1.30.2 | Despacho | Entidade | Ação dentro de uma Etapa | obrigatório (sim/não); formulário personalizado (opcional); assinatura obrigatória (opcional, bloqueia avanço até ser realizada) | Confirmado |
| 1.31.1.1 | Modelo simples | Entidade | Texto reutilizável inserido num campo de texto grande/editor durante a tramitação; não gera documento próprio | nome, herança de dados (sim/não), categoria/serviço/assunto vinculado (se herança=sim), corpo (texto), exclusividade (próprio servidor ou compartilhado com setores) | Confirmado |
| 1.31.2, 1.31.2.1.1–1.31.2.1.3.2 | Documento automatizado | Entidade | Modelo que gera um documento **independente**, com tramitação própria — usado para Alvarás, Licenças e documentos semelhantes | nome, categoria/serviço/assunto vinculado, cabeçalho/rodapé estilizado, conteúdo+herança de dados, validade pré-definida (contada da emissão) | Confirmado |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Fluxo de trabalho | tem (sequência ordenada de) | Etapa | 1.30, 1.30.1 | Confirmado |
| Etapa | pode exigir | Despacho | 1.30.1, 1.30.2 | Confirmado |
| Despacho | pode exigir | Assinatura (bloqueante ao avanço) | 1.30.2.b | Confirmado |
| Fluxo de trabalho | filtrável/associado por | Categoria de documento, Serviço ou Assunto | 1.30.1.f.i | Confirmado que o filtro existe; mecanismo exato do vínculo não detalhado |
| Modelo simples | vinculado a (quando há herança de dados) | Categoria de documento, Serviço ou Assunto | 1.31.1.1.b | Confirmado |
| Modelo simples | exibição condicionada a | Categoria/Serviço/Assunto selecionado no documento em tramitação | 1.31.1.4 | Confirmado |
| Documento automatizado | vinculado a | Categoria de documento, Serviço ou Assunto | 1.31.2.1.2 | Confirmado |
| Documento automatizado | gera | Documento independente (tramitação própria) | 1.31.2 | Confirmado |

## Dúvidas/ambiguidades

- Nenhuma ambiguidade de conteúdo identificada neste recorte — as regras de Fluxo/Etapa/Despacho e a distinção Modelo simples × Documento automatizado estão descritas de forma direta no texto.

## Fontes/evidências

- PDF: `Fontes/Requisitos Sogov.pdf`, p. 11–13 (ver mapa de páginas no Escopo acima). Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
