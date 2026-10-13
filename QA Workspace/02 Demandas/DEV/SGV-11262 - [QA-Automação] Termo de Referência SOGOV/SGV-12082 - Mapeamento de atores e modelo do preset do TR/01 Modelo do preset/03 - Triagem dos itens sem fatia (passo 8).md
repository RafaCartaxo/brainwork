---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "triagem-preset"
status: em levantamento
---
# 03 - Triagem dos itens sem fatia (passo 8)

> [!info]- Navegação
> **Índice da iniciativa:** [[../../Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]] · **Roadmap:** [[../../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]] (passo 8) · **README do card:** [[../00 QA/00 README|README]] · **Visão consolidada:** [[02 - Visão consolidada do preset candidato]] · **Matriz:** [[01 - Matriz de atores e relações]] · **Mapa geral:** [[00 - Mapa geral]]

> [!important] Proposta de caminho-base — aguardando revisão do Rafael/Codex, sem decisão do passo 8 nem encerramento tomados
> Esta nota propõe, por item, um **caminho-base** (o mínimo sustentado pra iniciar o modelo do preset), **extensões posteriores** (não bloqueiam o início) e **questões em aberto**. **Não é decisão aprovada nem fechamento do passo 8.** Nenhum item foi declarado não aplicável/fora do preset, nenhuma fatia nova (19+) foi aberta.

## 1. Propósito e limites

Propor, item a item, um caminho-base para os requisitos do TR que a [[02 - Visão consolidada do preset candidato|Visão consolidada]] lista como **sem fatia própria** na Fase 2 — para revisão do Rafael/Codex antes de qualquer decisão do passo 8. **Não implementa seed, não cria cenário de teste completo e não declara ausência de código como ausência no produto.** Não repete o texto analítico das fatias 02–18 nem dos recortes `Seções do TR/` — só cita e linka. Repositório de referência: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4`.

Cada linha classifica dois eixos, separadamente:
- **Caminho-base (proposta):** Base inicial / Extensão posterior / Questão em aberto — por sub-parte do item, quando se aplica.
- **Natureza do dado/estado:** configuração persistente do ambiente/módulo · dado de exemplo persistente · estado produzido em teste · ação/consulta de teste — um item pode ter mais de uma natureza.

**Checagem contra "Limite de cobertura" da nota 02:** recorte 01 (1.1–1.23) já tem decisão registrada no [[00 - Mapa geral]] e recorte 09 (1.41) está coberto pela fatia 18, aprovada — nenhum dos dois entra aqui.

> Nas tabelas, links usam Markdown relativo (não wikilink) por renderização mais estável dentro de células; fora delas seguem como wikilinks.

## 2. Recorte 07 — Mesa de trabalho, etiquetas e tramitação

| Ref./necessidade | Caminho-base (proposta) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.35** — acesso restrito às mesas dos setores a que o servidor pertence | **Base inicial:** nenhuma ação nova, já implícito em Servidor/Setor. **Extensão:** teste de permissão negativa | Nenhuma nova — reutiliza config já existente (fatias 02–04) | TR: [recorte 07](<Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35).md>). [Mesa de trabalho](<../../../../../04 Conhecimento/Módulos/Mesa de trabalho.md>) ("Switch de setores"). Zero teste de negação localizado |
| **1.35.1** — linha do tempo: (a) executor, (b) setor, (c) data/hora, (d) visualizações | **Base inicial:** consulta já funciona (`type` confirmado). **Extensão:** assegurar (b)/(c)/(d) por asserção direta | **Ação/consulta de teste** — consulta sobre eventos **já produzidos por outras ações** (despacho/assinatura/associação); não é timeline persistente própria desta linha, nem dado de exemplo dedicado | `getDocumentEvents`/`DocumentEvent` (`documents.ts:134-171`); A52-C01 confirma só `event.type`. `createdAt`/setor/visualizações: **A confirmar/não localizado** — ver nota |
| **1.35.2** — introdutório, prepara 1.35.2.1 | **Sem decisão autônoma** | — | TR: recorte 07 |
| **1.35.2.1** — status do Documento × estado individual da Mesa | **Base inicial:** status do Documento (fatia 06) como núcleo. **Extensão, explícita, não subsumida:** estado individual da Mesa — duas dimensões documentadas pelo produto, não equivalentes nem reduzíveis uma à outra | Status do Documento: **consulta/filtro já confirmado** (fatia 06, `getWorkboardDocuments`) — **não** é documento persistente comprovado no seed atual; um **dado de exemplo persistente** com status definido é **candidato/proposta** pro preset inicial, ainda não comprovado no seed; o estado também pode ser **produzido em cenário de teste** (documento criado e levado a um status). Estado da Mesa = **estado a validar**, dimensão própria, sem prova técnica de enum no código — não equivalente ao status do Documento | [Mesa de trabalho](<../../../../../04 Conhecimento/Módulos/Mesa de trabalho.md>) ("Status de um documento", "Status nas mesas", "Regras de status" — duas dimensões com regras de interação). [fatia 06](<Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33).md>) confirma só a consulta/filtro |
| **1.35.2.2** — introdutório, anuncia 1.35.2.2.1 ([fatia 08](<Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1).md>)) | **Sem decisão autônoma** | — | TR: recorte 07 |

**Nota — 1.35.1:** `DocumentEvent.createdAt` é tipado, `eventHistory` é `unknown`; nenhum teste localizado lê/assert esses campos (busca por `.createdAt` combinado com `getDocumentEvents`: zero resultado). Exceção parcial: autor/setor de um **despacho** são assertados via `getDocumentEventsWithAccessKey`, usada na fatia 18 para outro fim — não cobertura direta de 1.35.1.

## 3. Recorte 08 — Divulgação, exportação e assinaturas

| Ref./necessidade | Caminho-base (proposta) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.38** — canal (mural/externo), divulgar, acesso do cidadão | **Base inicial:** config de canal externo (módulo DO/CO) + ato de divulgar via canal externo (A23-C02, funcional). **Extensão, sem afirmar cobertura:** mural interno (bug de produto) e acesso cidadão/Jornal Oficial | Flags de canal = **configuração persistente do ambiente/módulo**, enviada na criação (`provision.ts:69-72`), não reconciliada em reuso. Ato de divulgar (canal externo) = **ação de teste** confirmada. Mural interno = ação de teste com **bug de produto confirmado**. Acesso cidadão = sem evidência | [Divulgar Documento](<../../../../../04 Conhecimento/Módulos/Divulgar Documento.md>). `seed.ts` flags `isInternalOfficialChannel`/`isExternalOfficialChannel`/`isPublicationOfficialChannel: true`. `publish-document.spec.ts` A23-C01 (`test.fail()`/`pdf-generator-attachment-error`), A23-C02 (sucesso) |
| **1.39** — exportação de documento existente × árvore composta completa | **Base inicial:** exportar um documento existente simples (reaproveitado de outra fatia). **Extensão, sem inferir cobertura conjunta:** árvore composta (anexos+despachos+associação+assinaturas combinados) — nunca testada combinada | **Ação de teste** — exportação é sempre ação sobre entidade já existente; nenhum dado persistente novo para a base | `print.spec.ts` A22-C01–C04; `complete-document-attachment.spec.ts` E26-C01/C02; `authenticable-signature.spec.ts` E33-C01; zero menção a PAdES/ICP; zero setup em `provision.ts`/`baseline.ts` |
| **1.40.1** — autenticação, notificação, verificação de autenticidade | **Base inicial:** `type:'SOGOV'` como **configuração de workflow já enviada no seed** em 2 de 3 workflows — registrado só como isso, **não como equivalência resolvida** com categoria do produto. **Extensão:** ICP-Brasil, notificação, "página extra"/QR Code | `type:'SOGOV'` no workflow = **configuração persistente do ambiente/módulo**, só na criação — **pode não ser reconciliada** em ambiente preexistente (workflow já existente não é recriado). Mutation de solicitação executada pelo teste = **ação de teste** separada, sem dado persistente | `seed.ts:327` (`makeWorkflowInput`, 2 workflows); `seed.ts:372` (`makeMultiStepDispatchWorkflowInput`, 3º workflow, `signers: []`); `workflow.ts:30-38` (`getWorkflowOrCreate` não reconcilia existente). [Assinaturas](<../../../../../04 Conhecimento/Módulos/Assinaturas.md>) (tipos, sem mapeamento resolvido) |
| **1.40.4** — editar tipo/papel do signatário, excluir signatário pendente | **Extensão posterior** — não é base inicial, mas **não descartado** | Se implementado: **ação de teste**. Hoje nenhuma função no código | `signatures.ts` (lido por completo) sem função de cancelar/editar. Assinaturas ("Gerenciar solicitação") |
| **1.40.5** — recusa simples × cascata em sequência | **Base inicial:** recusa simples, já ação de teste confirmada. **Extensão, separada da ação:** cascata de recusa em sequência — pode exigir um estado de solicitação sequencial pendente pré-criada | Recusa simples = **ação de teste confirmada** (`refuseSignature`). Cascata = ação de teste a desenhar + possível **dado de exemplo persistente** (solicitação pendente), se quiser evitar reconstruir tudo a cada teste | `refuseSignature`, 3 arquivos, A30-C08. Assinaturas — regra crítica de cascata, não testada pelos CTs sequenciais (fatia 17) |
| **1.40.6** — assinatura em massa | **Extensão posterior** — **não descartado**; separar do risco observado | Se implementado: **ação de teste** (assinar de fato) + possível **dado de exemplo persistente** (múltiplas pendências pré-seedadas). **O vazamento do E63-C01 é risco operacional, não massa útil para o preset** — as duas coisas não se confundem | `massive-signature-resize.spec.ts` E63-C01 (regressão, cria 1 pendência, não conclui nem limpa — vazamento admitido no próprio comentário). Assinaturas ("Assinaturas em massa") |

**Nota — 1.40.1, workflow do baseline:** `provision.ts` cria 3 workflows. Os 2 primeiros (`workflow`, linhas 324-327; `workflowAttachment`, linhas 345-349) usam `makeWorkflowInput`, configurando `type:'SOGOV'` na Etapa 02 (`seed.ts:327`). O 3º (`workflowFiveSteps`, linhas 367-371) usa `makeMultiStepDispatchWorkflowInput`, com `signers: []` vazio (`seed.ts:372`) — sem `type:'SOGOV'`. Enviado **só na criação**: `getWorkflowOrCreate` (`workflow.ts:30-38`) não chama `createWorkflow` nem reconcilia se o workflow já existe. Correspondência de `type:'SOGOV'` com a taxonomia do produto (Eletrônica simples/Digital SoGov/Digital ICP-Brasil) segue **não resolvida**.

## 4. Recorte 10 — Personalização e identidade visual do órgão

| Ref./necessidade | Caminho-base (proposta) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.42** — dados cadastrais + identidade visual | **Base inicial:** dados cadastrais da instância como já existem hoje (payload de criação). **Extensão:** feature de edição de cores/imagens (1.42.1.b/c, permissão Administrador confirmada no produto, sem teste) | Ver nota — 4 alcances distintos por campo, não "baseline garantido" único | [Fluxo de trabalho](<../../../../../04 Conhecimento/Módulos/Fluxo de trabalho (Workflow).md>) — Administrador só p/ cores/imagens, **não cobre 1.42.1.a**. `makeInstance` (`seed.ts:9-34`) |

**Nota — 1.42, alcance exato por campo:**
- **Enviado na criação** (só se a instância ainda não existir): `licenses`, `startContract`/`endContract`, `contractedModules` (inicial vazio), `primaryColor`/`secondaryColor`, `cnpj`/`companyName`/`name`/`domain` — `provision.ts:48-50`.
- **Reconciliado no reuso**: só `contractedModules`/`workflowModules`, quando o módulo específico está ausente — `enableWorkflowFeatureOnInstance`.
- **Só lido/preservado, nunca alterado**: `theme`, `brasao`, `brasaoToDarkBackground`, `bannerUrl`, `logoUrl`, `logoUrlToDarkBackground`, `phone`, `address`.
- **Sem reconciliação alguma** em instância já existente: `getInstanceOrCreate` (`instance.ts:121-129`) retorna só `{id, created:false}`.
- **Questão em aberto:** ator de 1.42.1.a (licenças/contrato/módulos) — permanece sem resposta em qualquer fonte.

## 5. Recorte 11 — Estatísticas e indicadores

| Ref./necessidade | Caminho-base (proposta) | Natureza do dado/estado | Evidência (resumo) |
|---|---|---|---|
| **1.43** — relatórios de setores/módulos/servidores/consumo | **Extensão posterior** — segue parte do escopo do TR, **não encerrada como fora do objetivo** por falta de evidência. Sub-passo antes de decidir: descobrir fonte/funcionalidade no produto/código; só depois decidir corpus controlado + consultas | Hoje nada. Se avançado: **dado de exemplo persistente** (corpus controlado) + **ação/consulta de teste** (relatórios) | TR: [recorte 11](<Seções do TR/11 - Estatísticas e indicadores (1.43).md>). Zero código (`statistic`/`estatistic`/`relatorio`). [Organograma](<../../../../../04 Conhecimento/Módulos/Organograma.md>) — achado tangencial, não equivalente. **Questão em aberto:** ator ("administradores e usuários autorizados") não nomeado; zero evidência **não localizada** ≠ ausência no produto |

## 6. Dependências entre linhas

- 1.35.1 depende de eventos já gerados por despacho/assinatura/associação — fatias 08, 13, 14, 16, 17 (não reabertas).
- 1.35.2.1 depende do status do Documento já mapeado na fatia 06.
- 1.40.4/1.40.5/1.40.6 dependem da entidade "Solicitação de assinatura" já mapeada na fatia 17.
- 1.38 depende das flags de serviço/módulo já mapeadas na fatia 03.
- **1.41 (fatia 18, aprovada) não é reaberto aqui.** [[QA Workspace/04 Conhecimento/Módulos/Chaves de Acesso|Chaves de Acesso]] segue só como contexto de produto já registrado na fatia 18.

## 7. Questões em aberto para extensões/decisões futuras

Sem resposta ainda em nenhuma fonte — mas **não bloqueiam** registrar o caminho-base proposto nas seções 2–5; ficam para quando as respectivas extensões forem avaliadas.

- **1.40.1** — `type:'SOGOV'` (código) corresponde a qual categoria exata da documentação ("Eletrônica simples" ou "Digital SoGov")?
- **1.42.1.a** — qual nível de acesso vê/edita licenças, contrato e módulos contratados? Não respondido por nenhuma fonte.
- **1.43** — "administradores e usuários autorizados" (texto do TR) corresponde a quais níveis canônicos exatos? Não nomeado pelo TR nem por produto.
- **Referência cruzada, não reaberta:** N1 = Especialista e N2 = Usuário básico já confirmados (legenda em [[QA Workspace/04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]]); só a correspondência de N3 com "Somente Leitura"/"Visualizador" segue em aberto — pendência registrada na fatia 18.

## 8. Próximo passo após revisão do Rafael/Codex

Com esta proposta de caminho-base revisada, o Rafael/Codex decidem se cada "Base inicial" proposta é aceita, se alguma "Extensão" deve virar fatia já, e quais "Questões em aberto" (seção 7) precisam de resposta antes de avançar — só depois disso o Roadmap e o README são atualizados e o passo 8 é formalmente fechado. Nenhuma dessas decisões foi tomada nesta nota.

## Fontes

Repositório Playwright consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Documentação de produto citada por item nas tabelas acima. Notas-fonte do TR: [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]], [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]], [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]]. Fatias aprovadas citadas: 03, 06, 08, 16, 17, 18.
