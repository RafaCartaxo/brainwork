---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.28–1.29"
paginas_pdf: "p. 7–11"
status: lido
---
# 04 - Serviços, assuntos e categorias de documentos (itens 1.28–1.29)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — lido em 08/10/2026, aguardando revisão do Codex
> Itens do TR: **1.28–1.29**, cobertos recursivamente em todos os subitens numerados que o PDF apresenta (28 linhas na Cobertura — 5 sob 1.28, 23 sob 1.29). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Mapa de páginas: 1.28–1.28.1 (p. 7–8); 1.28.1.2–1.29.1 (p. 8–9); 1.29.2–1.29.8 (p. 9–10); 1.29.9–1.29.10.4 (p. 10–11). Listas com letras dentro de um item numerado são conteúdo desse item, não subitens próprios do TR.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.28 | Mapeado | Gerenciamento de Serviços e Assuntos: CRUD de categorias/subcategorias, serviços e assuntos, com filtros e busca. |
| 1.28.1 | Mapeado | Campos mínimos do cadastro de serviço/assunto: nome, descrição, categoria de documento vinculada, abertura externa, setores de interação externa, sigilo (com/sem/anônimo), setores com acesso a dados sigilosos, setores que abrem/recebem processos, envio automático a setor, prazo oficial (dias úteis/corridos, prorrogação limitada e justificável), numeração oficial pré-existente (reinício anual ou sequência infinita). |
| 1.28.1.2 | Mapeado | Tipos de campo personalizável do formulário do serviço/assunto — enum detalhado abaixo. |
| 1.28.1.3 | Mapeado | Configuração por campo: título, visibilidade (servidor/cidadão/ambos), obrigatoriedade, repetição, sensibilidade (LGPD), uso como título do documento/mesa de trabalho. |
| 1.28.1.4 | Não aplicável | Reordenação visual dos campos no formulário — requisito de interface. |
| 1.29 | Mapeado | Categorias de documentos para geração de processos/comunicação oficial, com regras de tramitação pré-estabelecidas por categoria e módulo, sem limite de quantidade. |
| 1.29.1 | Mapeado | 3 categorias-base: Documento oficial (atos oficiais), Comunicação oficial (memorando/ofício/circular), Processo administrativo (ouvidoria/protocolo/processo administrativo). |
| 1.29.2 | Mapeado | Categoria "Memorando" — comunicação oficial entre setores/subsetores (de uma secretaria ou mais amplo). |
| 1.29.2.1 | Mapeado | Campos do Memorando: numeração única/contínua, origem, setor(es) destinatário(s) em cópia, assunto, texto livre + anexos. |
| 1.29.3 | Mapeado | Categoria "Circular" — comunicado em massa, para todos os setores ou alguns. |
| 1.29.3.1 | Mapeado | Campos da Circular: numeração, assunto, texto+anexos, e se o documento é respondível ou só informativo (definido pelo setor criador). |
| 1.29.4 | Mapeado | Categoria "Ofício" — comunicação oficial para contatos externos (PF/PJ/outras organizações). |
| 1.29.4.1 | Mapeado | Campos do Ofício: numeração, origem, destinatário externo, assunto, texto+anexos; exige confirmação de recebimento; destinatário recebe alerta de envio. |
| 1.29.5 | Mapeado | Categoria "Processo administrativo" (genérico) — atividade administrativa robusta, múltiplos setores, assuntos pré-definidos. |
| 1.29.5.1 | Mapeado | Campos: numeração (única ou por assunto), seleção de assunto (herda campos personalizados do serviço/assunto vinculado), origem, setor destinatário em cópia. |
| 1.29.6 | Mapeado | Categoria "Processo administrativo — solicitação externa" — entrada de requerimento/solicitação por usuário externo (contribuinte/fornecedor/empresa/população). |
| 1.29.6.1 | Mapeado | Campos: numeração, demandante (ator externo), setor destinatário (1ª tratativa), seleção de assunto/serviço (campos herdados), notificação em tempo real ao demandante, despacho sigiloso opcional. |
| 1.29.7 | Mapeado | Categoria "Processo administrativo — Ouvidoria" (Lei 13.460/2017) — denúncias/reclamações/sugestões/elogios. |
| 1.29.7.1 | Mapeado | Campos: numeração, demandante, opção anônima/sigilosa/não sigilosa, setor destinatário, assunto, texto+anexos, notificação, despacho sigiloso, restrição de setor para dados sigilosos, controle de prazo por lei. |
| 1.29.8 | Mapeado | Categoria "Processo administrativo — e-SIC" (Lei 12.527/2011) — solicitação de informação/dados públicos. |
| 1.29.8.1 | Mapeado | Campos: numeração, demandante, setor destinatário, assunto, texto+anexos, notificação, despacho sigiloso. |
| 1.29.9 | Mapeado | Categoria "Documento oficial" (Ato oficial) — leis, portarias, decretos, resoluções, instruções normativas. |
| 1.29.9.1 | Mapeado | Campos: numeração, setor emissor, setor(es) destinatário(s) em cópia, assunto, texto livre. |
| 1.29.10 | Mapeado | Categoria de transparência/zoneamento urbano (consulta/licenciamento) — ver dúvida sobre encaixe nas 3 categorias-base. |
| 1.29.10.1 | Mapeado | Reafirma o objetivo da funcionalidade de zoneamento, sem elemento novo além do já coberto em 1.29.10.4. |
| 1.29.10.2 | Mapeado | Ferramenta acessível a servidores e também a cidadãos/empresas (ator externo com acesso de consulta). |
| 1.29.10.3 | Mapeado | Servidores (com permissão) gerenciam zoneamentos e categorias de uso. |
| 1.29.10.4 | Mapeado | Entidades Zona e Categoria de uso, criação manual ou por upload de arquivo (.kmz), com histórico completo e publicação no portal de transparência — detalhado abaixo. |

**Resultado do recorte:** 28/28 itens (incluindo subitens numerados) considerados; 27 Mapeados, 1 Não aplicável (1.28.1.4 — interface). Nenhum item pendente de leitura.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.28.1 | Serviço/Assunto | Entidade | Unidade configurável de tramitação, vinculada a uma categoria de documento | nome, descrição, categoria de documento, abertura externa (sim/não), setores de interação externa, sigilo (com sigilo/sem sigilo/anônimo), setores com acesso a dados sigilosos, setores que abrem/recebem processos, envio automático a setor, prazo oficial (dias úteis/corridos + regras de prorrogação com limite e justificativa), numeração oficial pré-existente (reinício anual ou sequência infinita) | Confirmado |
| 1.28.1.2 | Campo personalizado (tipo) | Configuração (enum) | Tipo de campo do formulário de um serviço/assunto | Texto curto; Texto grande (com texto pré-definido); Número (subtipos: simples, porcentagem, moeda BR, telefone, celular, CPF, CNPJ, m², m³); E-mail; Mapa; Link; Arquivo; Data e hora; Escolha única/múltipla; Grupo de campos (aninhável); Texto informativo (não preenchível); Seleção de referência (Pessoas — cidadãos/empresas/servidores — ou Setores) | Confirmado |
| 1.28.1.3 | Configuração do campo | Configuração | Parâmetros aplicáveis a qualquer campo personalizado | título, visibilidade (servidor/cidadão/ambos), descrição, dica, obrigatório (sim/não), repetível (sim/não), sensível/LGPD (protegido e não exibido externamente), é título do documento/mesa de trabalho | Confirmado |
| 1.29.1 | Categoria de documento (base) | Entidade (enum, 3 valores-base) | Classificação macro de todo documento gerado | Documento oficial; Comunicação oficial; Processo administrativo | Confirmado |
| 1.29.2, 1.29.3, 1.29.4, 1.29.5, 1.29.6, 1.29.7, 1.29.8, 1.29.9 | Categoria de documento (específica) | Entidade (enum, 8 valores) | Subtipo de documento, cada um com campos próprios | Memorando; Circular; Ofício; Processo administrativo (genérico); Processo administrativo – solicitação externa; Ouvidoria; e-SIC; Ato oficial | Confirmado |
| 1.29.2.1, 1.29.3.1, 1.29.4.1, 1.29.5.1, 1.29.6.1, 1.29.7.1, 1.29.8.1, 1.29.9.1 | Campos por categoria específica | Dado/atributo | Cada categoria define seu próprio conjunto de campos obrigatórios (ver Cobertura acima, item a item) | numeração, setor de origem/destinatário, assunto, texto+anexos, e variações específicas (demandante externo, sigilo, notificação, prazo legal) conforme a categoria | Confirmado |
| 1.29.6, 1.29.7, 1.29.8 | Demandante (ator externo) | Ator | Quem solicita um processo administrativo externamente (contribuinte, fornecedor, cidadão, empresa) | identificação do solicitante; pode ser anônimo (só na Ouvidoria, 1.29.7.1) | Confirmado |
| 1.29.9 | Ato oficial (subtipo) | Dado/atributo (enum) | Tipos de ato dentro da categoria Documento oficial | Lei; Portaria; Decreto; Resolução; Instrução normativa | Confirmado |
| 1.29.10.4 | Zona | Entidade | Unidade de zoneamento urbano | nome, descrição, bairros/localidades, categorias de uso associadas; histórico completo de criação/edição/associações | Confirmado |
| 1.29.10.4 | Categoria de uso | Entidade | Uso permitido associável a uma Zona | nome, descrição, parâmetros (unidade de medida + valor); histórico completo | Confirmado |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Serviço/Assunto | tem (1:N) | Campo personalizado | 1.28.1.2 | Confirmado |
| Serviço/Assunto | vinculado a | Categoria de documento | 1.28.1 | Confirmado |
| Processo administrativo (1.29.5) / Solicitação externa (1.29.6) | herda campos personalizados de | Serviço/Assunto selecionado | 1.29.5.1, 1.29.6.1 | Confirmado |
| Categoria de documento específica | é subtipo de | Categoria de documento (base, 1.29.1) | 1.29.2–1.29.9 | Confirmado para Memorando/Circular/Ofício/Processo administrativo/Ouvidoria/e-SIC/Ato oficial |
| Categoria "Zoneamento" (1.29.10) | é subtipo de | Categoria de documento (base, 1.29.1) | 1.29.1, 1.29.10 | **A confirmar — ver dúvida abaixo** |
| Zona | associada a (N:N) | Categoria de uso | 1.29.10.4 | Confirmado |
| Upload de arquivo de zoneamento (.kmz) | sobrescreve | Zonas já existentes | 1.29.10.4.b | Confirmado |

## Dúvidas/ambiguidades

- **Zoneamento (1.29.10) não é explicitamente enquadrado numa das 3 categorias-base de 1.29.1** (Documento oficial, Comunicação oficial, Processo administrativo). O texto não afirma a qual pertence, nem que seja uma 4ª categoria-base. **A confirmar.**

## Fontes/evidências

- PDF: `Fontes/Requisitos Sogov.pdf`, p. 7–11 (ver mapa de páginas no Escopo acima). Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
