---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "triagem-preset"
status: aprovado
---
# 03 - Triagem dos itens sem fatia (passo 8)

> [!info]- Navegação
> **Índice da iniciativa:** [[../../Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]] · **Roadmap:** [[../../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]] (passo 8) · **README do card:** [[../00 QA/00 README|README]] · **Visão consolidada:** [[02 - Visão consolidada do preset candidato]] · **Matriz:** [[01 - Matriz de atores e relações]] · **Mapa geral:** [[00 - Mapa geral]]

> [!important] Caminho-base aprovado para iniciar o modelo-alvo
> A triagem foi aprovada como **ordem de partida**, não como encerramento de requisitos. O modelo começa pelo caminho-base indicado por item; extensões e questões em aberto permanecem rastreadas para aprofundamento. Esta aprovação não transforma evidências técnicas em requisitos confirmados, não declara itens fora do preset e não exige abrir fatias 19+.

## 1. Propósito e limites

Registrar o caminho de partida aprovado para os requisitos do TR ainda sem fatia própria, usando o TR e a documentação do produto para identificar dados, atores, relações, configurações e estados necessários aos cenários de sanidade. **As extensões indicam ordem de aprofundamento, não exclusão do modelo-alvo. O seed atual e os testes são evidências sobre a automação de hoje, não limites do preset desejado.** Esta nota não implementa seed nem cria CTs; ausência de código/teste não significa ausência no produto. Não repete as fatias 02–18 nem os recortes `Seções do TR` — só cita e linka.

Cada linha classifica dois eixos, separadamente:
- **Caminho-base (ordem aprovada):** Base inicial / Extensão posterior / Questão em aberto — por sub-parte do item, quando se aplica. A aprovação define sequência de trabalho, não confirma evidências nem encerra dúvidas específicas.
- **Natureza do dado/estado:** configuração persistente do ambiente/módulo · dado de exemplo persistente · estado produzido em teste · ação/consulta de teste — um item pode ter mais de uma natureza.

**Origem de fornecimento ainda não definida:** tanto o `.env` individual de cada QA quanto o seed persistente podem fornecer dados. A natureza do dado necessária ao cenário não determina, por si só, qual canal a fornecerá. O mapeamento por campo entre `.env`, seed e estado criado durante o teste será feito no desenho do modelo do preset. O código/seed atual serve para consulta e reaproveitamento possível, não para limitar o modelo-alvo.

**Checagem contra "Limite de cobertura" da nota 02:** recorte 01 (1.1–1.23) já tem decisão registrada no [[00 - Mapa geral]] e recorte 09 (1.41) está coberto pela fatia 18, aprovada — nenhum dos dois entra aqui.

> Nas tabelas, links usam Markdown relativo (não wikilink) por renderização mais estável dentro de células; fora delas seguem como wikilinks.

## 2. Recorte 07 — Mesa de trabalho, etiquetas e tramitação

| Ref./necessidade | Caminho de trabalho (partida aprovada) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.35** — acesso às mesas conforme vínculo do servidor com setores | **Base inicial:** modelar Servidor↔Setor e as regras de tramitação por módulo e Assunto/Serviço. **Extensão:** cenário de permissão negativa/positiva conforme recorte do TR | Dados necessários: setores, servidores e relações de tramitação; a distribuição entre `.env` e seed fica para o desenho do modelo | TR: [recorte 07](<Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35).md>). [Regras de Tramitação](<../../../../../04 Conhecimento/Fluxos/Regras de Tramitação.md>) descreve módulo→A/S→setores: criação, recebimento/tramitação, setor dono, interação com cidadão e visualização de dados sigilosos; A/S restringe regras herdadas do módulo. Fonte reconstruída de diagrama, ainda não validada em teste. [Mesa de trabalho](<../../../../../04 Conhecimento/Módulos/Mesa de trabalho.md>) (acesso e switch de setores). Teste de negação não localizado |
| **1.35.1** — linha do tempo: (a) executor, (b) setor, (c) data/hora, (d) visualizações | **Base inicial:** consulta já funciona (`type` confirmado). **Extensão:** assegurar (b)/(c)/(d) por asserção direta | **Ação/consulta de teste** — consulta sobre eventos **já produzidos por outras ações** (despacho/assinatura/associação); não é timeline persistente própria desta linha, nem dado de exemplo dedicado | `getDocumentEvents`/`DocumentEvent` (`documents.ts:134-171`); A52-C01 confirma só `event.type`. `createdAt`/setor/visualizações: **A confirmar/não localizado** — ver nota |
| **1.35.2** — introdutório, prepara 1.35.2.1 | **Sem decisão autônoma** | — | TR: recorte 07 |
| **1.35.2.1** — status do Documento × estado individual da Mesa | **Base inicial:** status do Documento (fatia 06) como núcleo. **Extensão, explícita, não subsumida:** estado individual da Mesa — duas dimensões documentadas pelo produto, não equivalentes nem reduzíveis uma à outra. **Configuração de usuário relacionada:** preferência persistida para exibir Pausado/Encerrado | Status do Documento: **consulta/filtro já confirmado** (fatia 06, `getWorkboardDocuments`) — **não** é documento persistente comprovado no seed atual; um **dado de exemplo persistente** com status definido é **candidato/proposta** pro preset inicial, ainda não comprovado no seed; o estado também pode ser **produzido em cenário de teste**. Estado da Mesa = dimensão própria a validar, sem prova técnica de enum no código. Preferência de exibição = **configuração de produto documentada**, persistida na conta do usuário; seed/código não verificados nesta proposta. Busca em outras mesas vinculadas é contexto, sem necessidade adicional de massa identificada | [Mesa de trabalho](<../../../../../04 Conhecimento/Módulos/Mesa de trabalho.md>) (status do Documento e das Mesas; preferência persistida Pausado/Encerrado; busca em outras mesas). [fatia 06](<Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33).md>) confirma só consulta/filtro |
| **1.35.2.2** — introdutório, anuncia 1.35.2.2.1 ([fatia 08](<Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1).md>)) | **Sem decisão autônoma** | — | TR: recorte 07 |

**Nota — 1.35.1:** `DocumentEvent.createdAt` é tipado, `eventHistory` é `unknown`; nenhum teste localizado lê/assert esses campos (busca por `.createdAt` combinado com `getDocumentEvents`: zero resultado). Exceção parcial: autor/setor de um **despacho** são assertados via `getDocumentEventsWithAccessKey`, usada na fatia 18 para outro fim — não cobertura direta de 1.35.1.

## 3. Recorte 08 — Divulgação, exportação e assinaturas

| Ref./necessidade | Caminho de trabalho (partida aprovada) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.38** — canal (mural/externo), divulgar, acesso do cidadão | **Base inicial:** parâmetro do módulo habilitando divulgação + configuração do canal externo/Jornal Oficial e ato de divulgar (A23-C02). **Extensão:** mural interno (bug conhecido) e verificação automatizada do acesso público pelo cidadão | Parâmetro = **configuração persistente do módulo** enviada na criação (`provision.ts:69-72`), não reconciliada em reuso; mural e canal externo são **canais independentes** sob essa funcionalidade. Ato de divulgar no canal externo = **ação de teste confirmada**; acesso público sem login = **documentado no produto**, mas sem evidência de teste automatizado localizada. Mural interno = ação de teste com bug de produto confirmado | [Divulgar Documento](<../../../../../04 Conhecimento/Módulos/Divulgar Documento.md>) (um parâmetro, dois canais independentes; canal externo/Jornal Oficial público sem login). [Construtor de Módulos](<../../../../../04 Conhecimento/Módulos/Construtor de Módulos.md>) (configuração do parâmetro). `publish-document.spec.ts` A23-C01 (`test.fail()`/`pdf-generator-attachment-error`), A23-C02 (divulgação externa) |
| **1.39** — exportação de documento existente × árvore composta completa | **Base inicial:** exportar um documento existente simples (reaproveitado de outra fatia). **Extensão, sem inferir cobertura conjunta:** árvore composta (anexos+despachos+associação+assinaturas combinados) — nunca testada combinada | **Ação de teste** — exportação é sempre ação sobre entidade já existente; nenhum dado persistente novo para a base | `print.spec.ts` A22-C01–C04; `complete-document-attachment.spec.ts` E26-C01/C02; `authenticable-signature.spec.ts` E33-C01; zero menção a PAdES/ICP; zero setup em `provision.ts`/`baseline.ts` |
| **1.40.1** — autenticação, notificação, verificação de autenticidade | **Base do modelo-alvo:** representar o tipo de assinatura/autenticação exigido pelo TR e a verificação de autenticidade; a equivalência de `type:'SOGOV'` com as categorias do produto fica em aberto. **Extensão de configuração:** página extra de assinaturas/QR, ativada por CX no módulo filho e herdada por A/S com opção de desmarcar. Isso não é tratado como substituto do tipo de assinatura | `type:'SOGOV'` = **evidência do seed atual**, não escolha aprovada para o preset-alvo. Página extra = **configuração de produto documentada**, parte do PDF, sem cobertura confirmada no seed/teste atual. Solicitação de assinatura = **ação de cenário** | `seed.ts:327,372`; `workflow.ts:30-38`. [Assinaturas](<../../../../../04 Conhecimento/Módulos/Assinaturas.md>) (página adicional no PDF e QR). [Construtor de Módulos](<../../../../../04 Conhecimento/Módulos/Construtor de Módulos.md>) (ativação mestre por CX e herança para A/S). Taxonomia `SOGOV` segue não resolvida |
| **1.40.4** — editar tipo/papel do signatário, excluir signatário pendente | **Extensão posterior** — não é base inicial, mas **não descartado** | Se implementado: **ação de teste**. Hoje nenhuma função no código | `signatures.ts` (lido por completo) sem função de cancelar/editar. Assinaturas ("Gerenciar solicitação") |
| **1.40.5** — recusa simples × cascata em sequência | **Base inicial:** recusa simples, já ação de teste confirmada. **Extensão:** validar recusa sequencial conforme regra atual — só signatários posteriores ao recusante são cancelados; assinaturas anteriores concluídas são mantidas | Recusa simples = **ação de teste confirmada** (`refuseSignature`). Cascata sequencial = ação de teste a desenhar; pode usar pedido e signatários criados em tempo de teste, ou dado de exemplo persistente se isso for útil para reuso | `refuseSignature`, A30-C08. [Assinaturas](<../../../../../04 Conhecimento/Módulos/Assinaturas.md>) (regra atualizada em 15/09/2026); fatia 17 documenta cobertura sequencial, não essa regra de recusa |
| **1.40.6** — assinatura em massa | **Extensão posterior** — **não descartado**; separar do risco observado | Se implementado: **ação de teste** (assinar de fato) + possível **dado de exemplo persistente** (múltiplas pendências pré-seedadas). **O vazamento do E63-C01 é risco operacional, não massa útil para o preset** — as duas coisas não se confundem | `massive-signature-resize.spec.ts` E63-C01 (regressão, cria 1 pendência, não conclui nem limpa — vazamento admitido no próprio comentário). Assinaturas ("Assinaturas em massa") |

**Nota — 1.40.1, workflow do baseline:** `provision.ts` cria 3 workflows. Os 2 primeiros (`workflow`, linhas 324-327; `workflowAttachment`, linhas 345-349) usam `makeWorkflowInput`, configurando `type:'SOGOV'` na Etapa 02 (`seed.ts:327`). O 3º (`workflowFiveSteps`, linhas 367-371) usa `makeMultiStepDispatchWorkflowInput`, com `signers: []` vazio (`seed.ts:372`) — sem `type:'SOGOV'`. Enviado **só na criação**: `getWorkflowOrCreate` (`workflow.ts:30-38`) não chama `createWorkflow` nem reconcilia se o workflow já existe. Correspondência de `type:'SOGOV'` com a taxonomia do produto (Eletrônica simples/Digital SoGov/Digital ICP-Brasil) segue **não resolvida**.

## 4. Recorte 10 — Personalização e identidade visual do órgão

| Ref./necessidade | Caminho de trabalho (partida aprovada) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.42** — dados cadastrais + identidade visual | **Base do modelo-alvo:** representar a instância do Cliente e os atributos cadastrais/visuais pedidos pelo TR. **Questão em aberto:** origem de cada campo e ator/permissão para licenças, contrato e módulos. Processo Urbanístico é adicional/contratado, não padrão universal | O payload de criação do seed é **evidência do setup atual**, não decisão sobre a origem nem o canal do dado no preset-alvo. A edição de cores/imagens é requisito do TR; permissão Administrador consta na documentação, ainda sem teste. | [Ambientes SoGov](<../../../../../04 Conhecimento/Módulos/Ambientes SoGov.md>) (instância própria do cliente; licenças/contrato no cadastro administrativo). [Fluxo de trabalho](<../../../../../04 Conhecimento/Módulos/Fluxo de trabalho (Workflow).md>) — não responde ator/permissão para 1.42.1.a no ambiente Cliente. [Processos Urbanísticos](<../../../../../04 Conhecimento/Módulos/Processos Urbanísticos.md>) (funcionalidade adicional) |

**Nota — 1.42, alcance exato por campo:**
- **Enviado na criação** (só se a instância ainda não existir): `licenses`, `startContract`/`endContract`, `contractedModules` (inicial vazio), `primaryColor`/`secondaryColor`, `cnpj`/`companyName`/`name`/`domain` — `provision.ts:48-50`.
- **Reconciliado no reuso**: só `contractedModules`/`workflowModules`, quando o módulo específico está ausente — `enableWorkflowFeatureOnInstance`.
- **Só lido/preservado, nunca alterado**: `theme`, `brasao`, `brasaoToDarkBackground`, `bannerUrl`, `logoUrl`, `logoUrlToDarkBackground`, `phone`, `address`.
- **Sem reconciliação alguma** em instância já existente: `getInstanceOrCreate` (`instance.ts:121-129`) retorna só `{id, created:false}`.
- **Questão em aberto:** ator de 1.42.1.a (licenças/contrato/módulos) — permanece sem resposta em qualquer fonte.

## 5. Recorte 11 — Estatísticas e indicadores

| Ref./necessidade | Caminho de trabalho (partida aprovada) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.43** — relatórios de setores/módulos/servidores/consumo | **Base do modelo-alvo:** incluir as dimensões de relatório explicitamente pedidas pelo TR e a necessidade de dados que as alimentem. **A aprofundar:** catálogo de relatórios, regras de cálculo e papéis autorizados; não bloqueiam representar essa necessidade inicial | [Ambientes SoGov](<../../../../../04 Conhecimento/Módulos/Ambientes SoGov.md>) confirma Relatórios/Estatísticas como função padrão do Cliente. Corpus, papéis e cobertura técnica seguem sem confirmação; fonte de dados fica para mapeamento posterior entre `.env`, seed e cenário | TR: [recorte 11](<Seções do TR/11 - Estatísticas e indicadores (1.43).md>). [Ambientes SoGov](<../../../../../04 Conhecimento/Módulos/Ambientes SoGov.md>). Código/teste ainda não localizados nesta análise. [Organograma](<../../../../../04 Conhecimento/Módulos/Organograma.md>) tem contador tangencial, não equivalente |

## 6. Dependências entre linhas

- 1.35.1 depende de eventos já gerados por despacho/assinatura/associação — fatias 08, 13, 14, 16, 17 (não reabertas).
- 1.35.2.1 depende do status do Documento já mapeado na fatia 06.
- 1.40.4/1.40.5/1.40.6 dependem da entidade "Solicitação de assinatura" já mapeada na fatia 17.
- 1.38 depende das flags de serviço/módulo já mapeadas na fatia 03.
- **1.41 (fatia 18, aprovada) não é reaberto aqui.** [[QA Workspace/04 Conhecimento/Módulos/Chaves de Acesso|Chaves de Acesso]] segue só como contexto de produto já registrado na fatia 18.

## 7. Questões em aberto para extensões/decisões futuras

Sem resposta ainda em nenhuma fonte — mas **não bloqueiam** seguir pelo caminho-base aprovado nas seções 2–5; ficam para quando as respectivas extensões forem avaliadas.

- **1.40.1** — `type:'SOGOV'` (código) corresponde a qual categoria exata da documentação ("Eletrônica simples" ou "Digital SoGov")?
- **1.42.1.a** — qual nível de acesso vê/edita licenças, contrato e módulos contratados? Não respondido por nenhuma fonte.
- **1.43** — "administradores e usuários autorizados" (texto do TR) corresponde a quais níveis canônicos exatos? Não nomeado pelo TR nem por produto.
- **Referência cruzada, não reaberta:** N1 = Especialista e N2 = Usuário básico já confirmados (legenda em [[QA Workspace/04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]]); só a correspondência de N3 com "Somente Leitura"/"Visualizador" segue em aberto — pendência registrada na fatia 18.

## 8. Decisão de partida

O Rafael autorizou seguir pelo caminho-base registrado. O passo 8 fica concluído como **seleção do ponto de partida**, não como decisão item a item de excluir ou encerrar requisitos. O modelo-alvo deriva necessidades do TR e da documentação de produto; somente depois atribui cada dado ao `.env` individual, ao seed persistente ou ao estado criado durante o cenário. As classificações técnicas e dúvidas das tabelas continuam com o grau de evidência registrado em cada linha; esta aprovação não as converte em fatos confirmados.

## Fontes

Repositório Playwright consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Documentação de produto citada por item nas tabelas acima. Notas-fonte do TR: [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]], [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]], [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]]. Fatias aprovadas citadas: 03, 06, 08, 16, 17, 18.
