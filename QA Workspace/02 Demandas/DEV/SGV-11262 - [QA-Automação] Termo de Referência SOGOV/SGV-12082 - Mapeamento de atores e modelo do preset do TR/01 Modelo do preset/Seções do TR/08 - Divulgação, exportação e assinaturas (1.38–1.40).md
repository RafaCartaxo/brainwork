---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.38–1.40"
paginas_pdf: "p. 16–18"
status: aprovado
---
# 08 - Divulgação, exportação e assinaturas (itens 1.38–1.40)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Itens do TR: **1.38–1.40**, cobertos recursivamente em todos os subitens numerados que o PDF apresenta (22 linhas na Cobertura). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Mapa de páginas: 1.38–1.38.2.a (p. 16); 1.38.2.b–1.39.6.1 (p. 17); 1.40–1.40.6 (p. 18, antes de 1.41, que pertence ao recorte 09 e não foi analisado aqui). Listas com letras dentro de um item numerado são conteúdo desse item, não subitens próprios do TR — exceto onde o próprio TR numera. Contexto de produto já confirmado por Rafael (níveis canônicos, visualizar/criar Assuntos e Serviços, status Ativo/Inativo, presença online/offline) **não aparece de forma literal neste recorte** — nenhum desses itens cita nível de acesso nomeado ou status funcional do servidor, então não foi aplicado por falta de pertinência textual. Nesta rodada, a análise usou exclusivamente o texto do TR — Conhecimento > Módulos não foi consultado para este recorte.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.38 | Mapeado | Funcionalidade de divulgação de documentos oficiais e comunicações internas, para uso interno e acesso público, visando conformidade legal. |
| 1.38.1 | Mapeado | Tipos de divulgação: (a) interna — mural de servidores (mural interno geral + mural particular por servidor); (b) externa — canal oficial, acessível sem login, incluindo leis/decretos/portarias/editais. |
| 1.38.2 | Mapeado | O sistema permite configurar a divulgação do documento **tanto enquanto ele está em elaboração quanto após ser emitido**, com opções para: (a) imediata; (b) agendada (data definida pelo usuário); (c) edição da configuração permitida enquanto não divulgado; (d) remoção da publicação já realizada. |
| 1.38.3 | Mapeado | Servidores, ao acessar documentos divulgados em seus murais, podem visualizar/interagir/tramitar conforme suas permissões de usuário no documento em questão. |
| 1.38.3.1 | Mapeado | Cidadãos acessam documentos divulgados no jornal oficial via interface pública, com busca e filtros. |
| 1.39 | Mapeado | Exportação/impressão de documentos e processos administrativos, gerando PDF para impressão ou compartilhamento digital. |
| 1.39.1 | Mapeado | Exportação de diferentes partes de documentos/processos conforme especificações técnicas dos subitens seguintes. |
| 1.39.2 | Mapeado | Exportação da árvore completa do processo em PDF, incluindo anexos, despachos, documentos apensados, assinaturas e afins. |
| 1.39.3 | Mapeado | Formatos de exportação da árvore: (a) básica (todas as partes); (b) personalizada (servidor escolhe partes); (c) PAdES (gerada a cada assinatura, conformidade legal, validável em sistemas como o ITI). |
| 1.39.4 | Mapeado | Exportação isolada de despacho, com anexos e documentos associados. |
| 1.39.5 | Mapeado | Documentos muito grandes exportados já zipados; partes assinadas em formato autenticável para validação das assinaturas. |
| 1.39.6 | Mapeado | Documentos de tamanho regular: download unificado, com opção de paginação. |
| 1.39.6.1 | Mapeado | Quando a paginação afeta a estrutura do documento (invalidando assinaturas), manter selos de assinatura visíveis com link de validação e verificação do conteúdo — exceto quando o documento é sigiloso. |
| 1.40 | Mapeado | Uso de assinaturas eletrônicas e digitais, relevante para auditoria/fiscalização/validação jurídica. |
| 1.40.1 | Mapeado | Requisitos técnicos: (a) autenticação segura (token, ICP-Brasil); (b) interface intuitiva; (c) notificações automáticas — **ao signatário, informando a solicitação de assinatura, e ao solicitante, conforme os signatários forem assinando**; (d) verificação da autenticidade das assinaturas realizadas, **em meio oficial do órgão**. |
| 1.40.2 | Mapeado | Diferentes tipos de assinatura conforme nível de segurança/validade jurídica, com base na Lei nº 14.063/2020 e MP nº 2.200-2/2001 (detalhado em 1.40.2.1). |
| 1.40.2.1 | Mapeado | Tipos: (a) eletrônica simples (login/senha ou credenciais corporativas); (b) eletrônica avançada (associação inequívoca ao documento, detecção de alteração posterior); (c) eletrônica qualificada (certificado digital ICP-Brasil, para contratos/documentos fiscais/auditados). |
| 1.40.3 | Mapeado | Solicitação de assinaturas por servidores: (a) rotulado "Assinaturas simples" no TR, mas significa possibilitar a solicitação de assinatura **de qualquer um dos tipos já definidos anteriormente (simples, avançada ou qualificada)** para qualquer servidor, cidadão ou contribuinte cadastrado no ambiente do órgão; (b) assinaturas sequenciais (ordem definida, bloqueio até a vez); (c) seleção de signatários internos/externos, **respeitando as permissões e regras de tramitação do documento**; (d) locais de assinatura no documento (ex.: documento de abertura, anexos, despachos e outros). |
| 1.40.4 | Mapeado | Gerenciamento de solicitações de assinatura: edição/cancelamento de assinaturas não realizadas. |
| 1.40.4.1 | Mapeado | Funcionalidades de gerenciamento: (a) alteração de tipo de assinatura e papel do signatário (se ainda não assinado); (b) exclusão de signatários pendentes, com registro automático no histórico. |
| 1.40.5 | Mapeado | Signatários (internos/externos) podem recusar assinatura, com justificativa registrada e notificada ao solicitante. |
| 1.40.6 | Mapeado | Assinatura em massa de múltiplos documentos/solicitações. |

**Resultado do recorte:** 22/22 itens (incluindo subitens numerados) considerados; 22 Mapeados, 0 Não aplicáveis. Nenhum item pendente de leitura — pendências de identidade entre recortes registradas em Dúvidas/ambiguidades abaixo.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.38, 1.38.1, 1.38.2 | Divulgação | Entidade/Funcionalidade | Publicação de um documento oficial/comunicação, interna ou externa | tipo (interna/externa); **configurável tanto com o documento em elaboração quanto após emitido** (1.38.2); timing (imediata/agendada — data definida pelo usuário); editável enquanto não divulgado; removível (despublicação) após divulgado | Confirmado |
| 1.38.1.a.i, 1.38.1.a.ii | Mural | Entidade | Local de exibição de divulgações internas | mural interno geral (visível a todos os servidores cadastrados); mural particular por servidor (divulgações vinculadas a ele) | Confirmado |
| 1.38.1.b | Canal Oficial | Entidade/Canal | Canal de divulgação externa de documentos oficiais, acessível sem login | documentos: leis, decretos, portarias, editais; disponível na Central de atendimento (recorte 06, 1.36) | Confirmado |
| 1.38.3.1 | Jornal Oficial | Entidade/Canal | Onde o cidadão acessa os documentos divulgados, via interface pública | interface pública; busca e filtros | Confirmado quanto à existência e ao acesso do cidadão; identidade com o Canal Oficial (1.38.1.b) — **A confirmar**, ver dúvida abaixo |
| 1.39, 1.39.2, 1.39.3 | Exportação (árvore do processo) | Entidade/Funcionalidade | Geração de PDF com o conteúdo de um Documento/Processo para impressão ou compartilhamento | formatos: básica (todas as partes), personalizada (partes escolhidas pelo servidor), PAdES (gerada a cada assinatura); conteúdo: anexos, despachos, documentos apensados, assinaturas; regras de tamanho (1.39.5, 1.39.6, 1.39.6.1) | Confirmado |
| 1.40, 1.40.1, 1.40.2, 1.40.2.1 | Assinatura | Entidade | Assinatura eletrônica ou digital aplicada a documentos/processos/despachos | tipo (simples, avançada, qualificada — base legal: Lei nº 14.063/2020, MP nº 2.200-2/2001); requisitos técnicos: autenticação segura (token, ICP-Brasil); interface intuitiva; **notificação automática ao signatário na solicitação e ao solicitante conforme os signatários vão assinando** (1.40.1.c); **verificação de autenticidade em meio oficial do órgão** (1.40.1.d) | Confirmado |
| 1.40.3, 1.40.4, 1.40.4.1, 1.40.5, 1.40.6 | Solicitação de assinatura | Entidade | Pedido de assinatura feito por um servidor, dirigido a um ou mais signatários | ordem sequencial (opcional); local de assinatura no documento; seleção de signatários **respeitando permissões e regras de tramitação do documento** (1.40.3.c); editável/cancelável enquanto não realizada; signatário excluível (se pendente, com histórico); recusável (com justificativa, notificada ao solicitante); assinatura em massa | Confirmado |
| 1.40.3.c | Signatário | Ator | Pessoa que assina um documento/processo, interna (servidor) ou externa | interno: servidor; externo: pessoa física ou jurídica — TR também cita "cidadão ou contribuinte cadastrado no ambiente do órgão" (1.40.3.a); seleção sujeita a permissões e regras de tramitação do documento (1.40.3.c); identidade com Contato externo/Usuário externo (recorte 06) — não declarada | Confirmado quanto à existência dos dois tipos (interno/externo) e à restrição de permissões/tramitação; identidade do signatário externo com os atores do recorte 06 — **A confirmar**, ver dúvida abaixo |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Divulgação (interna) | publicada em | Mural interno (geral) | 1.38.1.a.i | Confirmado |
| Divulgação (interna) | publicada em | Mural particular do servidor | 1.38.1.a.ii | Confirmado |
| Divulgação (externa) | publicada em | Canal Oficial | 1.38.1.b | Confirmado |
| Canal Oficial | disponível em | Central de atendimento (recorte 06, 1.36) | 1.38.1.b.i | Confirmado — o próprio TR declara explicitamente que o canal oficial fica "disponível na central de atendimento" |
| Servidor | acessa (conforme permissão no documento) | Documento divulgado (mural) | 1.38.3 | Confirmado |
| Cidadão | acessa | Documento divulgado (Jornal Oficial) | 1.38.3.1 | Confirmado |
| Canal Oficial (1.38.1.b) | mesmo elemento que — **não declarado pelo TR** | Jornal Oficial (1.38.3.1) | 1.38.1.b, 1.38.3.1 | A confirmar — ver dúvida abaixo |
| Documento/Processo | é exportável como | Árvore do processo (básica, personalizada ou PAdES) | 1.39.2, 1.39.3 | Confirmado |
| Despacho | é exportável isoladamente como | Despacho exportado (com anexos/documentos associados) | 1.39.4 | Confirmado |
| Assinatura | associa dados do signatário a | Documento, Processo, Despacho ou afins | 1.40.2.1.a | Confirmado |
| Assinatura | tem | Tipo (simples, avançada ou qualificada) | 1.40.2.1 | Confirmado |
| Assinatura | gera notificação automática para | Signatário (ao ser solicitada a assinatura) | 1.40.1.c | Confirmado |
| Assinatura | gera notificação automática para | Solicitante (conforme os signatários vão assinando) | 1.40.1.c | Confirmado |
| Assinatura | é verificável quanto à autenticidade em | Meio oficial do órgão | 1.40.1.d | Confirmado |
| Solicitação de assinatura | feita por | Servidor | 1.40.3 | Confirmado |
| Solicitação de assinatura | dirigida a | Signatário (interno ou externo), respeitando permissões e regras de tramitação do documento | 1.40.3.c | Confirmado |
| Signatário | pode recusar | Solicitação de assinatura (com justificativa) | 1.40.5 | Confirmado |
| Assinaturas sequenciais | seguem | ordem definida na configuração da Solicitação | 1.40.3.b | Confirmado |
| Signatário externo (1.40.3.c) | mesma população de — **não declarado pelo TR** | Contato externo / Usuário externo (recorte 06, 1.32/1.37) | 1.40.3.a, 1.40.3.c | A confirmar — ver dúvida abaixo |

## Dúvidas/ambiguidades

- **Canal Oficial (1.38.1.b) × Jornal Oficial (1.38.3.1):** os dois termos aparecem em itens diferentes do TR — Canal Oficial é citado como o canal de divulgação externa, disponível na Central de atendimento; Jornal Oficial é citado como onde o cidadão acessa os documentos divulgados, via interface pública com busca e filtros. **O TR não declara literalmente que são o mesmo elemento.** Mantidos como dois Elementos distintos; Confirmado apenas que (i) o Canal Oficial fica disponível na Central de atendimento (1.38.1.b.i) e (ii) o cidadão acessa documentos divulgados no Jornal Oficial (1.38.3.1) — não concluo por semelhança de contexto que sejam a mesma entidade. **Pergunta objetiva para Rafael:** Canal Oficial e Jornal Oficial são o mesmo canal (dois nomes para a mesma coisa), ou são elementos distintos no produto?
- **Signatário externo (1.40) × Contato externo / Usuário externo (recorte 06):** o TR descreve o signatário externo como "pessoa física ou jurídica" (1.40.3.c) e também cita "cidadão ou contribuinte cadastrado no ambiente do órgão" (1.40.3.a) — vocabulário semelhante ao de Contato externo (1.32, cidadão/empresa) e Usuário externo (1.37), mas **não há declaração explícita de identidade** entre esses atores nos dois recortes. Mesma régua já aplicada às dúvidas equivalentes do recorte 06 — não concluo por semelhança de vocabulário. **Pergunta objetiva para Rafael:** o signatário externo de uma assinatura é o mesmo contato/usuário externo cadastrado em 1.32/1.37, ou um conceito à parte?
- **"Contribuinte" (1.40.3.a):** termo novo, não usado nos recortes anteriores (que usam cidadão/empresa/ente externo). O TR não define se "contribuinte" é um tipo adicional de ator externo ou um sinônimo contextual de cidadão/empresa. **Pergunta objetiva para Rafael:** "contribuinte", neste contexto, é um tipo de ator externo distinto, ou apenas outro nome para cidadão/empresa já cadastrado?
- **Recorrência do termo "apensado"/"documentos apensados" (1.39.2, 1.39.3.a):** a exportação da árvore do processo cita "documentos apensados" como parte do conteúdo exportável — o mesmo termo usado no recorte 07 para os dois mecanismos de associação de documentos (despacho, 1.35.2.2.1.2.a; geração automática, 1.35.4) ainda não resolvidos como idênticos ou distintos. Esta ocorrência não resolve essa dúvida já aberta — apenas reforça a recorrência do termo no TR; **não tento resolvê-la aqui**.

## Contexto de produto verificado em documentação (09/10/2026)

> Esta seção registra contexto de produto (Conhecimento > Módulos) — não é requisito literal do TR e não substitui nem resolve as dúvidas acima, que permanecem registradas tal como estão.

- **Signatário externo (1.40) × Contato externo / Usuário externo (recorte 06):** [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] documenta que, ao solicitar assinatura "de um cidadão PF ou PJ", o signatário é um "contato externo (PF ou PJ) cadastrado como cidadão na base do cliente". Isso **confirma, para o produto atual**, a relação entre signatário externo e Contato externo/Usuário Cidadão (ver recorte 06). **Confirmado no produto** quanto a esse vínculo.
- **"Contribuinte" (1.40.3.a):** segue sem definição na documentação consultada — não há evidência de que seja sinônimo de cidadão/empresa ou um tipo à parte. **Segue sem evidência.**
- **Canal Oficial (1.38.1.b) × Jornal Oficial (1.38.3.1):** nenhum módulo de Conhecimento documenta "Divulgação" ou "Jornal Oficial". **Segue sem evidência** — dúvida mantida em aberto.

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf`, p. 16–18 (ver mapa de páginas no Escopo acima). Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
- Conhecimento > Módulos: não consultado nesta rodada (análise restrita ao texto do TR).
