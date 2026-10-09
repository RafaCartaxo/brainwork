---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.33–1.35"
paginas_pdf: "p. 13–16"
status: aprovado
---
# 07 - Mesa de trabalho, etiquetas e tramitação (itens 1.33–1.35)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Itens do TR: **1.33–1.35**, cobertos recursivamente em todos os subitens numerados que o PDF apresenta (50 linhas na Cobertura). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Mapa de páginas: 1.33–1.33.3.5 (p. 13); 1.33.3.6–1.35 (p. 14); 1.35.1–1.35.2.7.a (p. 15); 1.35.2.7.b–1.35.5 (p. 16, antes de 1.36). Listas com letras dentro de um item numerado são conteúdo desse item, não subitens próprios do TR — exceto onde o próprio TR numera. Nesta rodada, a análise usou exclusivamente o texto do TR — Conhecimento > Módulos não foi consultado para este recorte.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.33 | Mapeado | Funcionalidade de mesa de trabalho: servidores gerenciam documentos/processos administrativos de forma integrada e dinâmica, com troca de informações entre setores. |
| 1.33.1 | Mapeado | Usuários alternam entre diferentes setores, visualizando/gerenciando documentos e processos de cada setor. |
| 1.33.2 | Mapeado | Na primeira tela de acesso, servidor vê resumo de todas as demandas que tem a fazer. |
| 1.33.2.1 | Mapeado | Tela de boas-vindas informa quantidade de documentos em: (a) Em aberto; (b) Em tramitação; (c) Concluído; (d) Assinaturas pendentes; (e) Demandas prestes a vencer/já vencidas. |
| 1.33.3 | Mapeado | Mesa de trabalho própria para cada servidor, com documentos/processos de suas atividades individuais e dos setores em que está vinculado. |
| 1.33.3.1 | Mapeado | Visualização padrão em formato Kanban (colunas). |
| 1.33.3.2 | Mapeado | Visualização alternativa em lista vertical. |
| 1.33.3.3 | Mapeado | Alertas de prazos, status de documentos e novas demandas, independente do setor ativo. |
| 1.33.3.4 | Mapeado | Alertas para documentos/processos com prazos próximos ao vencimento ou já vencidos. |
| 1.33.3.5 | Mapeado | Filtragem de documentos com prazos vencidos ou próximos ao vencimento. |
| 1.33.3.6 | Mapeado | Status de documentos **e das mesas de trabalho**: em aberto, em elaboração, em tramitação, pausado, encerrado. |
| 1.33.3.7 | Mapeado | Reabertura de documentos encerrados. |
| 1.33.4 | Mapeado | Filtros/buscas/ordenação em mesas pessoais e de setores, isolados ou combinados: (a) palavra-chave; (b) pessoas; (c) CPF; (d) CNPJ; (e) ordem alfabética; (f) pendente de assinatura; (g) pendente de revisão; (h) status; (i) módulo; (j) assunto ou serviço; (k) período. |
| 1.33.5 | Mapeado | Nos documentos das mesas, deve ser possível identificar os itens dos subitens a seguir. |
| 1.33.5.1 | Mapeado | Setor responsável pelo documento. |
| 1.33.5.2 | Mapeado | Data/hora da última atividade. |
| 1.33.5.3 | Mapeado | Notificações de novas interações diretas (solicitação de assinatura, envio de despacho, solicitação de revisão) direcionadas ao servidor/setor. |
| 1.33.6 | Mapeado | Ferramenta de rastreio/busca ampla por documentos em todo o escopo da organização (não só na mesa em visualização), respeitando a permissão do usuário consultante. |
| 1.34 | Mapeado | Funcionalidade de etiquetas para organização/categorização/filtragem/identificação de documentos nas mesas. |
| 1.34.1 | Mapeado | Tipos de etiqueta: (a) pessoais (uso individual, visíveis só na mesa pessoal do servidor); (b) compartilhadas (entre setores ou hierarquias de setores). |
| 1.34.1.2 | Mapeado | Etiqueta padrão "Urgente", visível/aplicável por todos os setores e usuários; não pode ser excluída. |
| 1.34.1.3 | Mapeado | Etiquetas usáveis como filtro na mesa de trabalho. |
| 1.34.1.4 | Mapeado | Visualização de etiquetas aplicadas é restrita conforme o setor do usuário — ver dúvida abaixo sobre escopo da regra. |
| 1.34.2 | Mapeado | Criação de novas etiquetas com nome/cor/setores de compartilhamento. |
| 1.34.2.1 | Mapeado | Etiquetas compartilhadas aparecem em seção própria, visível a todos os usuários do setor. |
| 1.34.2.2 | Mapeado | Subetiquetas ligadas a uma etiqueta principal. |
| 1.34.2.3 | Mapeado | Edição de nome/cor/setores de qualquer etiqueta. |
| 1.34.2.4 | Mapeado | Alterações de etiqueta se aplicam automaticamente às etiquetas já aplicadas em documentos. |
| 1.34.2.5 | Mapeado | Etiqueta excluída permanece aplicada/exibida nos documentos onde já estava, mas não pode ser adicionada a novos documentos. |
| 1.35 | Mapeado | Documentos/processos tramitam entre setores conforme organograma do órgão, respeitando limites de permissão por setor — servidor só acessa documentos/processos da tramitação das mesas dos setores a que pertence. |
| 1.35.1 | Mapeado | Linha do tempo da tramitação registra toda ação, com: (a) usuário executor; (b) setor do usuário (se executor foi servidor); (c) data/hora da ação; (d) registro de quem visualizou e quantas vezes, com data/hora da última visualização. |
| 1.35.2 | Mapeado | Documentos/processos precisam de "status" para classificação durante a tramitação. |
| 1.35.2.1 | Mapeado | Classificações de situação: (a) Em aberto; (b) Em elaboração; (c) Em tramitação; (d) Pausado; (e) Encerrado. |
| 1.35.2.2 | Mapeado | Funcionalidades adicionais variam conforme tipo de documento/processo gerado (introduz os subitens a seguir). |
| 1.35.2.2.1 | Mapeado | Após abertura de processo administrativo, setores envolvidos podem realizar despachos durante a tramitação. |
| 1.35.2.2.1.1 | Mapeado | Despacho: campo de livre preenchimento, com anexos e definição de destinatários (inclusive setores em cópia). |
| 1.35.2.2.1.2 | Mapeado | Despacho pode: (a) apensar outro documento da entidade à tramitação, com identificação no documento/processo e na impressão. |
| 1.35.2.2.1.3 | Mapeado | Despachos podem ser sigilosos ou não, conforme natureza do processo. |
| 1.35.2.2.1.4 | Mapeado | Despacho pode indicar prazo aos destinatários, respeitando prazos oficiais/do documento pré-existentes (não pode ultrapassá-los). |
| 1.35.2.2.1.5 | Mapeado | Assinar/solicitar assinaturas em despacho específico e anexos — assinatura nativa da plataforma ou ICP. |
| 1.35.2.2.1.6 | Mapeado | Possibilidade de imprimir despacho emitido, incluindo anexos e assinaturas. |
| 1.35.2.3 | Mapeado | Retificação do documento de abertura de processo administrativo, com histórico e justificativa legal. |
| 1.35.2.4 | Mapeado | Solicitação de revisão de documentos/comunicações oficiais ainda em estado pré-elaboração (antes da emissão oficial). |
| 1.35.2.5 | Mapeado | Edição do documento de abertura (documento/comunicação oficial) ainda em estado pré-elaboração, com histórico de cada edição. |
| 1.35.2.6 | Mapeado | Definição de prazos para documentos, aplicados hierarquicamente a setores/servidores envolvidos. |
| 1.35.2.7 | Mapeado | Prazos (a-d): prazo oficial, quando existente, torna-se o prazo do documento e não pode ser alterado (a); sem prazo oficial, define-se prazo do documento aplicado a todos os envolvidos (b); prazo de assinatura respeita o prazo do documento ou oficial, se houver (c); prazo individual respeita o prazo do documento ou oficial, se houver (d). |
| 1.35.3 | Mapeado | Encerramento flexível de tramitações, no mínimo: (a) individual por servidor (mantém tramitação normal nos demais); (b) por setor envolvido (encerra em massa nas mesas dos servidores do setor, mantendo tramitação normal nos demais setores); (c) total do documento (setor responsável encerra em todos os setores/servidores de uma vez). |
| 1.35.4 | Mapeado | Possibilidade de gerar documento de outro módulo e associá-lo automaticamente ao processo/documento em questão, conforme parametrização prévia. |
| 1.35.4.1 | Mapeado | Documento associado fica identificado no documento/processo que o associou, incluído também na impressão. |
| 1.35.5 | Mapeado | Possibilidade de visualizar histórico do documento/processo quando houver retificações ou edições. |

**Resultado do recorte:** 50/50 itens (incluindo subitens numerados) considerados; 50 Mapeados, 0 Não aplicáveis. Nenhum item pendente de leitura — pendências de detalhe (não de cobertura) registradas em Dúvidas/ambiguidades abaixo.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.33, 1.33.1, 1.33.3 | Mesa de trabalho | Entidade | Espaço de trabalho do servidor (pessoal) e do setor, reunindo documentos/processos relacionados | visualização (Kanban padrão / Lista — 1.33.3.1, 1.33.3.2); alertas de prazo/status/novas demandas (1.33.3.3, 1.33.3.4); filtros de prazo (1.33.3.5); filtros/buscas/ordenação (1.33.4, 11 critérios); resumo de demandas na tela de boas-vindas (1.33.2, 1.33.2.1); **status da própria mesa** (mesmo enum de 1.33.3.6 — ver linha "Status" abaixo) | Confirmado |
| 1.33.3.6, 1.35.2.1 | Status (Em aberto, Em elaboração, Em tramitação, Pausado, Encerrado) | Estado/enum | Enum único citado pelo TR duas vezes (1.33.3.6 e 1.35.2.1), aplicado explicitamente tanto a Documento/Processo quanto à Mesa de trabalho (1.33.3.6: "status dos documentos **e das mesas de trabalho**") | 5 valores: Em aberto, Em elaboração, Em tramitação, Pausado, Encerrado. TR não detalha regra de agregação (como o status da mesa se relaciona ao dos documentos nela) | Confirmado quanto ao enum e à dupla aplicação; regra de agregação — A confirmar |
| 1.33.3.6, 1.35.2, 1.35.2.1 | Documento/Processo | Entidade | Unidade central tramitada entre setores, com estado e histórico próprios | status (ver enum acima); setor responsável (1.33.5.1); data/hora da última atividade (1.33.5.2); notificações (1.33.5.3); prazo (ver Prazo abaixo); linha do tempo de tramitação (1.35.1); documento apensado via despacho (1.35.2.2.1.2.a) e/ou documento associado automaticamente (1.35.4) — mecanismos distintos, ver nota | Confirmado |
| 1.35.1 | Linha do tempo da tramitação | Entidade/registro | Auditoria de toda ação ocorrida durante a tramitação de um Documento/Processo | usuário executor; setor do usuário (se executor foi servidor); data/hora da ação; registro de visualizações (quem, quantas vezes, data/hora da última) | Confirmado |
| 1.35.2.2.1, 1.35.2.2.1.1–1.35.2.2.1.6 | Despacho | Entidade | Ação realizada por um setor envolvido durante a tramitação de um processo administrativo | campo de livre preenchimento; destinatário(s), inclusive setores em cópia (1.35.2.2.1.1); possibilidade de apensar outro documento (1.35.2.2.1.2.a); sigiloso ou não; prazo dirigido aos destinatários (respeita prazo oficial/do documento pré-existente — 1.35.2.2.1.4); assinatura (nativa ou ICP); impressão | Confirmado (atributos deste item); vínculo de identidade com o "Despacho" do recorte 05 (1.30.2) — **A confirmar**, ver dúvida abaixo |
| 1.34, 1.34.1 | Etiqueta | Entidade | Marcação usada para organizar/filtrar/identificar documentos nas mesas de trabalho | tipo (pessoal — só na mesa do próprio servidor / compartilhada — setores ou hierarquias de setores); nome; cor; setor(es) de compartilhamento; subetiqueta (vínculo a etiqueta principal — 1.34.2.2); etiqueta padrão "Urgente" (fixa, não excluível — 1.34.1.2) | Confirmado |
| 1.35.2.7 | Prazo | Atributo/conceito associado a Documento/Processo e a Despacho | 4 tipos: Prazo oficial (lei; quando existente, torna-se o prazo do documento e não pode ser alterado); Prazo do documento (quando não há oficial, aplicado a todos os envolvidos); Prazo de assinatura (respeita o prazo do documento ou oficial, se houver); Prazo individual (respeita o prazo do documento ou oficial, se houver) — o TR não declara relação direta entre assinatura e individual | Confirmado |
| 1.35.3 | Encerramento de tramitação | Conceito/ação sobre Documento/Processo | 3 modalidades: individual (por servidor, mesa própria); por setor (em massa, mesas dos servidores do setor); total (documento inteiro, todos os setores/servidores) | Confirmado |
| 1.35.2.2.1.2.a | Documento apensado (via despacho) | Entidade | Documento da entidade apensado à tramitação por meio de um despacho | identificado no documento/processo que o associou; incluído na impressão | Confirmado |
| 1.35.4, 1.35.4.1 | Documento associado (gerado automaticamente) | Entidade | Documento de outro módulo, gerado e associado automaticamente ao processo/documento em questão, conforme parametrização prévia; o TR descreve esse vínculo também com a palavra "apensado" (1.35.4.1) | documento associado deve estar identificado como apensado a outro documento/processo (1.35.4.1); na impressão do documento/processo que contém o documento associado, este também deve ser incluído (1.35.4.1) | Confirmado quanto ao mecanismo e existência; identidade conceitual com o "Documento apensado via despacho" (1.35.2.2.1.2.a) — mesmo objeto/mecanismo de dados ou só coincidência terminológica — **A confirmar** |
| 1.33.6 | Ferramenta de rastreio (busca global) | Entidade/Função | Busca ampla por documentos em todo o escopo da organização, não restrita à mesa em visualização | abrangência: toda a organização; acesso limitado à permissão do usuário consultante | Confirmado |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Mesa de trabalho | pertence a | Servidor (mesa pessoal) | 1.33.3 | Confirmado |
| Mesa de trabalho | pertence a | Setor (mesa do setor) | 1.33.1, 1.33.3 | Confirmado |
| Mesa de trabalho | contém | Documento/Processo | 1.33.3 | Confirmado |
| Documento/Processo | tem | Status (Em aberto \| Em elaboração \| Em tramitação \| Pausado \| Encerrado) | 1.33.3.6, 1.35.2.1 | Confirmado |
| Mesa de trabalho | tem | Status (mesmo enum: Em aberto \| Em elaboração \| Em tramitação \| Pausado \| Encerrado) | 1.33.3.6 | Confirmado — TR não detalha regra de agregação entre o status da mesa e o dos documentos nela |
| Documento/Processo | tem | Setor responsável | 1.33.5.1 | Confirmado |
| Documento/Processo | tem | Prazo oficial, do documento, de assinatura e/ou individual (ver Elemento Prazo — sem cadeia hierárquica estrita declarada entre os 4 tipos) | 1.35.2.7 | Confirmado |
| Documento/Processo | registrado em | Linha do tempo da tramitação | 1.35.1 | Confirmado |
| Documento/Processo | pode ter | Etiqueta (pessoal ou compartilhada) | 1.34, 1.34.1 | Confirmado |
| Documento/Processo (processo administrativo) | pode receber | Despacho | 1.35.2.2.1 | Confirmado |
| Despacho | tem | Destinatário(s), inclusive setores em cópia | 1.35.2.2.1.1 | Confirmado |
| Despacho | pode indicar | Prazo dirigido aos destinatários (respeita prazo oficial/do documento pré-existente) | 1.35.2.2.1.4 | Confirmado |
| Despacho | pode apensar | Documento apensado (via despacho) | 1.35.2.2.1.2.a | Confirmado |
| Documento/Processo | pode gerar e associar automaticamente | Documento associado (de outro módulo) | 1.35.4 | Confirmado quanto ao mecanismo; identidade com o "Documento apensado via despacho" — A confirmar, ver dúvida abaixo |
| Documento/Processo | pode ser encerrado | individualmente (servidor) / por setor (em massa) / totalmente (setor responsável) | 1.35.3 | Confirmado |
| Etiqueta compartilhada | compartilhada com | Setor(es) | 1.34.1.b, 1.34.2 | Confirmado |
| Etiqueta | pode ter | Subetiqueta | 1.34.2.2 | Confirmado |
| Servidor | pertence a | Setor | 1.33.1, 1.35 | Confirmado |
| Servidor | acessa | Mesa de trabalho (pessoal e dos setores vinculados) | 1.33.1, 1.33.3 | Confirmado |
| Servidor | só acessa (sujeito a permissões) | Documentos/Processos das mesas dos setores a que pertence | 1.35 | Confirmado |
| Ferramenta de rastreio (busca global) | abrange | Todo o escopo da organização (não só a mesa em visualização) | 1.33.6 | Confirmado — acesso limitado à permissão do usuário consultante |
| Documento/Processo | tramita entre | Setor (conforme organograma do órgão) | 1.35 | Confirmado quanto ao fato; Organograma em si não analisado neste recorte |
| Mesa de trabalho | reflete tramitação de | Etapa/Fluxo de trabalho (recorte 05, 1.30) | — | A confirmar — ver dúvida abaixo |
| Despacho (1.35.2.2.1, este recorte) | mesmo conceito que | Despacho (recorte 05, 1.30.2) | 1.30.2, 1.35.2.2.1 | A confirmar — mesmo termo, atributos compatíveis, mas o TR não declara identidade formal; ver dúvida abaixo |

## Dúvidas/ambiguidades

- **Mesa de trabalho (1.33, este recorte) × Etapa/Fluxo de trabalho (1.30, recorte 05):** o TR não declara explicitamente, neste recorte, que os documentos/processos exibidos na mesa de trabalho do servidor correspondem a etapas de um Fluxo de trabalho configurado (recorte 05). É plausível que sim (a mesa parece ser a visão consolidada do que está em tramitação), mas essa é uma suposição estrutural, não um fato declarado em nenhum dos dois recortes — não concluo a partir da plausibilidade. **Pergunta objetiva para Rafael:** os itens que aparecem na mesa de trabalho do servidor (1.33) são necessariamente etapas de algum Fluxo de trabalho (1.30), ou a mesa pode conter documentos/processos fora desse modelo?
- **Escopo da restrição de etiquetas por setor (1.34.1.4):** o texto diz que a visualização de etiquetas aplicadas deve ser restrita conforme o setor do usuário. Não fica claro se essa regra se aplica também às etiquetas **pessoais** (1.34.1.a — já restritas por definição ao próprio servidor, não a um setor) ou só às **compartilhadas** (1.34.1.b). **Pergunta objetiva para Rafael:** a restrição de 1.34.1.4 vale só para etiquetas compartilhadas, ou também reinterpreta a visibilidade das etiquetas pessoais?
- **Despacho (1.35.2.2.1) × Despacho (recorte 05, 1.30.2):** o TR usa o mesmo termo "despacho" nos dois recortes, com atributos compatíveis (formulário/anexos, assinatura, sigilo), mas **não declara formalmente que se trata da mesma entidade de negócio** — a coincidência terminológica/compatibilidade de atributos não é, por si, evidência de identidade (mesma régua aplicada às demais dúvidas deste recorte). Mantido como **A confirmar** nos Elementos e Relações, sem alterar o recorte 05. **Pergunta objetiva para Rafael:** o "despacho" de 1.30.2 (dentro de uma Etapa de Fluxo de trabalho) e o "despacho" de 1.35.2.2.1 (durante a tramitação geral de um processo administrativo) são a mesma funcionalidade, ou duas funcionalidades distintas que compartilham o nome?
- **Documento apensado via despacho (1.35.2.2.1.2.a) × Documento associado gerado automaticamente (1.35.4/1.35.4.1):** ambos os mecanismos são descritos pelo TR usando a palavra "apensado", mas são acionados de formas diferentes (manual, durante um despacho específico vs. automático, por parametrização prévia ao gerar documento de outro módulo). O TR não declara se resultam no mesmo tipo de vínculo/objeto de dados ou se são mecanismos de associação de documentos totalmente independentes. Mantido como dois Elementos distintos, com identidade **A confirmar**. **Pergunta objetiva para Rafael:** esses dois mecanismos de "apensar"/associar documentos usam a mesma estrutura de dados (ex.: mesma lista de documentos apensados num processo), ou são funcionalidades separadas?

## Contexto de produto verificado em documentação (09/10/2026)

> Esta seção registra contexto de produto (Conhecimento > Módulos) — não é requisito literal do TR e não substitui nem resolve as dúvidas acima, que permanecem registradas tal como estão.

- **Mesa de trabalho (1.33) × Etapa/Fluxo de trabalho (1.30, recorte 05):** [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]] documentam que Mesa de trabalho e Fluxo de trabalho são conceitos distintos no produto: o fluxo só pode ser configurado para documentos do tipo Processo Administrativo, e um documento sem fluxo configurado "segue o layout padrão do despacho, sem o contêiner" de movimentação de etapa, permanecendo normalmente na mesa. **Esclarecido no produto** que a mesa pode conter documentos fora do modelo de Fluxo de trabalho — sem afirmar que a mesa "reflita etapas" em geral, nem que essa seja a única relação possível entre os dois conceitos. O TR não declara essa relação explicitamente; a dúvida acima permanece registrada.
- **Alcance da restrição de etiquetas por setor (1.34.1.4):** [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]] documenta que etiquetas **pessoais** são de uso individual, visíveis só na mesa pessoal do servidor, e que a restrição de visualização por setor se aplica às **compartilhadas** ("cada usuário vê apenas as compartilhadas com o seu setor"). **Ponto resolvido no produto.**
- **Despacho (1.30.2, Etapa) × Despacho (1.35.2.2.1, tramitação):** [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] documenta que "despacho é a forma de comunicação usada para tramitar documentos... todas [as variações] seguem o modelo do despacho padrão", e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]] descreve o despacho customizado de etapa como variação configurável sobre esse mesmo padrão. Isso esclarece que, no produto, são a **mesma família/modelo funcional de Despacho** — **parcialmente esclarecido**: não há evidência documental de que sejam a mesma estrutura persistida; a identidade estrutural segue sem confirmação.
- **Documento apensado via despacho (1.35.2.2.1.2.a) × Documento associado gerado automaticamente (1.35.4):** [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] documenta que "o documento gerado é tratado como documento associado ao gerador", herdando a mesma regra de visibilidade de [[QA Workspace/04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]]. Isso esclarece que as duas vias convergem para o mesmo **conceito/regra de visibilidade de documento associado**, com gatilhos diferentes (manual via despacho; automático via Gerar Documento) — **parcialmente esclarecido**: não afirma mesma estrutura de banco de dados, e a distinção entre as duas vias/gatilhos permanece.

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf`, p. 13–16 (ver mapa de páginas no Escopo acima). Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
- Conhecimento > Módulos: não consultado nesta rodada (análise restrita ao texto do TR).
