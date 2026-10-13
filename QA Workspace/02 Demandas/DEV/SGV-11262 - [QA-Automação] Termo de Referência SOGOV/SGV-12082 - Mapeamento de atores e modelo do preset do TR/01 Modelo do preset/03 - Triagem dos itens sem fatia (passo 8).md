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

> [!important] Rascunho — aguardando revisão do Codex, sem decisão do passo 8 ainda tomada
> Esta nota é um **levantamento**, não uma decisão. Nenhum item aqui foi declarado não aplicável/fora do preset, nenhuma fatia nova (19+) foi aberta.

## 1. Propósito e limites

Reunir, item a item, os requisitos do TR que a [[02 - Visão consolidada do preset candidato|Visão consolidada]] já lista como **sem fatia própria** na Fase 2, para apoiar a decisão do passo 8 sobre relevância para o modelo do preset. **Não implementa seed, não cria cenário de teste completo e não declara ausência de código como ausência no produto.** Não repete o texto analítico das fatias 02–18 nem dos recortes `Seções do TR/` — só cita e linka. Repositório de referência: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4`.

**Checagem contra "Limite de cobertura" da nota 02:** recorte 01 (1.1–1.23) já tem decisão registrada no [[00 - Mapa geral]] ("sem elementos de negócio no diagrama") e recorte 09 (1.41) está coberto pela fatia 18, aprovada — nenhum dos dois entra aqui. Os demais itens (cluster 1.35 do recorte 07; 1.38/1.39/1.40.1/1.40.4–1.40.6 do recorte 08; 1.42 do recorte 10; 1.43 do recorte 11) estão todos cobertos abaixo.

> Nas tabelas a seguir, links usam Markdown relativo (não wikilink) por renderização mais estável dentro de células; fora das tabelas seguem como wikilinks.

## 2. Recorte 07 — Mesa de trabalho, etiquetas e tramitação

| Ref./necessidade | Evidência essencial | Estado persistente atual | Papel/encaminhamento |
|---|---|---|---|
| **1.35** — acesso restrito às mesas dos setores a que o servidor pertence | TR: [recorte 07](<Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35).md>). Produto: [Mesa de trabalho](<../../../../../04 Conhecimento/Módulos/Mesa de trabalho.md>) ("Switch de setores" — restrito ao setor ativo, salvo mesas alheias). Código: zero teste de negação localizado em `tests/api/workboard/`, `tests/api/processing/` | Nenhum dado novo — reaproveita Servidor/Setor (fatias 02–04) | Cenário de execução (teste de permissão negativa). Pendente — ausência não localizada ≠ prova de ausência da restrição |
| **1.35.1** — linha do tempo: (a) executor, (b) setor do executor, (c) data/hora, (d) visualizações | TR: recorte 07. Código: `getDocumentEvents`/`DocumentEvent` (`documents.ts:134-171`), usado em 12 arquivos de teste. `tests/api/processing/issue-draft-timeline-event.spec.ts` (A52-C01) assert só `event.type` (`.toContain('ISSUED')`) — **nenhuma asserção lida confirma `createdAt`, setor do executor ou visualizações** | Nenhum — é consulta sobre eventos já gerados (despacho/assinatura/associação, fatias 08/13/14/16/17) | Reutilizar a consulta (só `type` confirmado) + candidato a estado-config (timeline representativa). (b)/(c)/(d): **A confirmar/não localizado** — ver nota abaixo |
| **1.35.2** — introdutório, prepara 1.35.2.1 | TR: recorte 07 | — | **Sem decisão autônoma** — introdutório puro |
| **1.35.2.1** — status do Documento × status individual da Mesa | TR: recorte 07 (1.35.2.1, 1.33.3.6). Produto: [Mesa de trabalho](<../../../../../04 Conhecimento/Módulos/Mesa de trabalho.md>) ("Status de um documento", "Status nas mesas", "Regras de status") — descreve **dois conceitos/dimensões de status**, com regras de interação (ex.: "a mesa do setor dono reflete o status do documento... NO ENTANTO NEM SEMPRE a mesa dos servidores... reflete"). Código: [fatia 06](<Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33).md>) confirma só consulta/status do **Documento** (`getWorkboardDocuments`) | Status do Documento já é dado conhecido (fatia 06) | Reutilizar (fatia 06, Documento) + complemento de produto — **não** abrir fatia isolada. Sem prova de enum técnico próprio para a Mesa no código; não chamar de "dois enums" |
| **1.35.2.2** — introdutório, anuncia 1.35.2.2.1 ([fatia 08](<Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1).md>)) | TR: recorte 07 | — | **Sem decisão autônoma** — conteúdo já coberto |

**Nota — 1.35.1:** a interface `DocumentEvent` tem campo `createdAt` tipado e `eventHistory: unknown`, mas nenhum teste localizado lê/assert esses campos diretamente (busca por `.createdAt` em eventos e por `getDocumentEvents(...)` combinado com `createdAt`: zero resultado). Exceção parcial: autor/setor de um **despacho** especificamente são assertados (`event?.dispatch?.createdBy`/`createdBySector`) — mas via a variante `getDocumentEventsWithAccessKey`, usada na fatia 18 (TR 1.41) para outro fim, não como cobertura direta de 1.35.1.

## 3. Recorte 08 — Divulgação, exportação e assinaturas

| Ref./necessidade | Evidência essencial | Estado persistente atual | Papel/encaminhamento |
|---|---|---|---|
| **1.38** — canal (mural/externo), ato de divulgar, acesso do cidadão ao Jornal Oficial | TR: [recorte 08](<Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40).md>). Produto: [Divulgar Documento](<../../../../../04 Conhecimento/Módulos/Divulgar Documento.md>). Código: `provision.ts:69-72` cria módulos DO/CO via `makeModuleDO`/`makeModuleCO` com `isInternalOfficialChannel`/`isExternalOfficialChannel`/`isPublicationOfficialChannel: true`; `publish-document.spec.ts` A23-C01 (mural interno — **bug confirmado**, `test.fail()`/`pdf-generator-attachment-error`) e A23-C02 (canal externo, sucesso); zero teste do lado cidadão/Jornal Oficial | Flags de canal enviadas **na criação** dos módulos DO/CO (payload da fábrica; não reconciliadas em reuso — ver 1.42 para o mesmo padrão) | Candidato a estado-config (flags) + cenário de execução (ato de divulgar). Candidato a fatia — registrar bug do mural e ausência de evidência cidadã como limites |
| **1.39** — exportar/consultar × possível documento-base persistente (árvore: anexos+despachos+associação+assinaturas) | TR: recorte 08. Código: `print.spec.ts` A22-C01–C04 (ZIP/PDF documento e despacho); `complete-document-attachment.spec.ts` E26-C01/C02; `authenticable-signature.spec.ts` E33-C01; `long-document.spec.ts` E34-S09/S10; bugs confirmados em `custom-document-comment.spec.ts` E25-C01 e `citizen-reply-in-print.spec.ts` E39; zero menção a PAdES/ICP; zero setup em `provision.ts`/`baseline.ts`. Produto: nenhum doc dedicado localizado | Nenhum dado de export em si | Cenário de execução (ato de exportar) + **candidato a estado-config** (processo-base combinado, nunca montado hoje). Não é "sem candidato de dado" só por exportar ser ação |
| **1.40.1** — autenticação (SoGov/ICP), notificação, verificação de autenticidade | TR: recorte 08. Produto: [Assinaturas](<../../../../../04 Conhecimento/Módulos/Assinaturas.md>) (tipos; "Página extra de assinaturas" com QR Code — 3 bugs reais: SGV-10267, SGV-10457, SGV-9405). Código: solicitação executada por teste usa só senha SoGov; zero "notif" ligado a assinatura; `verificationCode` no schema, nunca lido | Ver nota abaixo — **separar mutation de solicitação (sem dado persistente) de workflow do baseline (parcialmente persistente)** | Pendente/candidato — ver nota. `type:'SOGOV'` ↔ categoria do produto **não resolvido**; "página extra" candidata, não equivalência confirmada |
| **1.40.4** — editar tipo/papel do signatário, excluir signatário pendente | TR: recorte 08. Produto: Assinaturas ("Gerenciar solicitação" — só não-executadas; tipo+papel editáveis; exclusão gera subevento+tag "Cancelada"; permissão Adm/Adm setorial/N1). Código: `signatures.ts` (lido por completo) sem função de cancelar/editar | Nada | Pendente — se testado, seria cenário de execução. Ausência de função não é prova de ausência no produto |
| **1.40.5** — recusa simples (confirmada) + cascata em sequência (não testada) | TR: recorte 08. Código: `refuseSignature` em 3 arquivos (A30-C08 `agent.spec.ts`, `citizen.spec.ts`, `citizen-alphanumeric.spec.ts`), asserção real. Produto: Assinaturas — recusa numa sequência cancela **todas** as assinaturas, inclusive já efetuadas; não testada pelos CTs sequenciais ([fatia 17](<Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3).md>), E40-C01/E34-S08) | Nada — sempre criado em teste | Reutilizar (recusa simples, confirmada) + candidato a estado-config (solicitação sequencial pendente pré-criada, só se decidido testar a cascata) |
| **1.40.6** — assinatura em massa (vários documentos de uma vez) | TR: recorte 08. Código: único teste `massive-signature-resize.spec.ts` E63-C01 (regressão de resize) — cria 1 pendência e **não conclui nem limpa**; comentário do próprio teste admite risco de vazamento. Produto: Assinaturas ("Assinaturas em massa" — agrupado por documento, impossível recusar, 3 variantes) | Nada — o residual do E63-C01 é efeito colateral indesejado, **não dado de preset** | Pendente/candidato a estado-config (múltiplas pendências pré-seedadas, só se decidido testar conclusão real). **O vazamento do E63-C01 é risco de contaminação do ambiente, não evidência de preset necessário** |

**Nota — 1.40.1, workflow do baseline:** `provision.ts` cria 3 workflows no baseline. Os 2 primeiros (`workflow`, linhas 324-327; `workflowAttachment`, linhas 345-349) usam `makeWorkflowInput`, que configura `signatures: { isSequential: false, signers: [{ ..., type: 'SOGOV', ... }] }` na Etapa 02 (`seed.ts:327`). O 3º (`workflowFiveSteps`, linhas 367-371) usa `makeMultiStepDispatchWorkflowInput`, com `signers: []` **vazio** (`seed.ts:372`) — sem `type:'SOGOV'`. Isso é **enviado só na criação**: `getWorkflowOrCreate` (`workflow.ts:30-38`), se o workflow já existe, retorna sem chamar `createWorkflow` — **não reconcilia workflow preexistente**. Mantém-se sem resolver a correspondência de `type:'SOGOV'` com a taxonomia do produto (Eletrônica simples/Digital SoGov/Digital ICP-Brasil).

## 4. Recorte 10 — Personalização e identidade visual do órgão

| Ref./necessidade | Evidência essencial | Estado persistente atual | Papel/encaminhamento |
|---|---|---|---|
| **1.42** — dados cadastrais (licenças/contrato/módulos) + identidade visual (cores/imagens) | TR: [recorte 10](<Seções do TR/10 - Personalização e identidade visual do órgão (1.42).md>). Produto: [Fluxo de trabalho](<../../../../../04 Conhecimento/Módulos/Fluxo de trabalho (Workflow).md>) — permissão "Visualizar e editar" = Administrador, **só para cores/imagens (1.42.1.b/c)**; **não cobre 1.42.1.a**. Código: `makeInstance` (`seed.ts:9-34`) define `licenses`, `startContract`/`endContract`, `contractedModules: []`, `primaryColor`/`secondaryColor: ''`; **não define** `theme`/`brasao`/`logoUrl`/`bannerUrl` em lugar nenhum | Ver nota abaixo — 4 categorias distintas, não "baseline garantido" único | Candidato a estado-config (dados cadastrais existem por ambiente, sem garantia pós-reuso); não exige massa própria para a *feature de edição* (sem teste). 1.42.1.a **sem ator confirmado** |

**Nota — 1.42, alcance exato por campo:**
- **Enviado na criação** (só se a instância ainda não existir no ambiente): `licenses`, `startContract`/`endContract`, `contractedModules` (inicial vazio), `primaryColor`/`secondaryColor` (vazios), `cnpj`/`companyName`/`name`/`domain` — `provision.ts:48-50`, `getInstanceOrCreate(..., makeInstance({cnpj, companyName, name, domain}))`.
- **Reconciliado no reuso**: só `contractedModules`/`workflowModules`, e só quando o módulo específico está ausente — via `enableWorkflowFeatureOnInstance`.
- **Só lido/preservado, nunca alterado**: `theme`, `brasao`, `brasaoToDarkBackground`, `bannerUrl`, `logoUrl`, `logoUrlToDarkBackground`, `phone`, `address` — repassados como `current.X`.
- **Sem reconciliação alguma**: em instância já existente, `getInstanceOrCreate` (`instance.ts:121-129`) retorna só `{id, created:false}`, sem tocar em nenhum campo.

## 5. Recorte 11 — Estatísticas e indicadores

| Ref./necessidade | Evidência essencial | Estado persistente atual | Papel/encaminhamento |
|---|---|---|---|
| **1.43** — relatórios de setores/módulos/servidores/consumo | TR: [recorte 11](<Seções do TR/11 - Estatísticas e indicadores (1.43).md>). Produto: nenhum doc dedicado nos 17 arquivos de `Conhecimento > Módulos`; achado tangencial em [Organograma](<../../../../../04 Conhecimento/Módulos/Organograma.md>) (contador simples de setores/usuários online — **não equivale** ao módulo do TR). Código: zero ocorrência de "statistic"/"estatistic"/"relatorio" em `playwright/src`/`playwright/tests` | Nada | Candidato a estado-config (volume controlado, só se decidido). Zero evidência **não localizada nesta busca** — não prova ausência no produto |

## 6. Dependências entre linhas

- 1.35.1 depende de eventos já gerados por despacho/assinatura/associação — fatias 08, 13, 14, 16, 17 (não reabertas).
- 1.35.2.1 depende do status do Documento já mapeado na fatia 06.
- 1.40.4/1.40.5/1.40.6 dependem da entidade "Solicitação de assinatura" já mapeada na fatia 17.
- 1.38 depende das flags de serviço/módulo já mapeadas na fatia 03.
- **1.41 (fatia 18, aprovada) não é reaberto aqui.** [[QA Workspace/04 Conhecimento/Módulos/Chaves de Acesso|Chaves de Acesso]] segue só como contexto de produto já registrado na fatia 18 — se a doc mudar a interpretação de relevância de algum estado, isso se resolve lá.

## 7. Pendências de negócio que impedem classificar uma linha

- **1.40.1** — `type:'SOGOV'` (código) corresponde a qual categoria exata da documentação ("Eletrônica simples" ou "Digital SoGov")? Sem essa resposta, a linha de autenticação não avança.
- **1.42.1.a** — qual nível de acesso vê/edita licenças, contrato e módulos contratados? Não respondido por nenhuma fonte.
- **1.43** — "administradores e usuários autorizados" (texto do TR) corresponde a quais níveis canônicos exatos? Não nomeado pelo TR nem por produto.
- **Referência cruzada, não reaberta:** N1 = Especialista e N2 = Usuário básico já confirmados (legenda em [[QA Workspace/04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]]); só a correspondência de N3 com "Somente Leitura"/"Visualizador" segue em aberto — pendência registrada na fatia 18.

## 8. Próximo passo após revisão do Codex

Com esta triagem revisada, o passo 8 decide, linha a linha, se cada item vira fatia futura, é registrado como "sem necessidade de massa própria" (com justificativa) ou fica pendente de resposta de negócio (seção 7) — só depois disso o Roadmap e o README são atualizados. Nenhuma dessas decisões foi tomada nesta nota.

## Fontes

Repositório Playwright consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Documentação de produto citada por item nas tabelas acima. Notas-fonte do TR: [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]], [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]], [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]]. Fatias aprovadas citadas: 03, 06, 08, 16, 17, 18.
