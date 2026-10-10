---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "consolidacao-preset"
status: em levantamento
---
# 02 - Visão consolidada do preset candidato

> [!info]- Navegação
> **Índice da iniciativa:** [[../../Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]] · **Roadmap:** [[../../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]] (passo 7 da "Sequência macro") · **README do card:** [[../00 QA/00 README|README]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Matriz de atores e relações:** [[01 - Matriz de atores e relações]] · **Mapa geral:** [[00 - Mapa geral]]
> As 16 fatias-fonte não são listadas aqui — cada seção temática abaixo já linka para a sua fatia-fonte correspondente, no cabeçalho da seção e em cada linha das tabelas.

> [!important] Rascunho — aguardando revisão do Codex (passo 7 do Roadmap)
> Esta nota é um **rascunho**, ainda **não aprovado**. Nenhuma fatia 18+ deve ser aberta, nenhum item deve ser declarado não aplicável/fora do preset, e README/Roadmap só serão atualizados depois que o conteúdo aqui for revisado e aprovado. Até lá, o status desta nota permanece `em levantamento`.

> [!info] Escopo e limites desta consolidação
> Esta nota **resume as 16 fatias aprovadas** (notas 02–17 da pasta `01 Modelo do preset/Especificações do preset piloto/`), normalizando vocabulário e organizando por tema — **não duplica** o texto analítico delas (cada linha/grupo linka de volta à fatia-fonte, onde está a evidência completa) e **não introduz nenhuma inferência nova**. **Não especifica o TR inteiro** (só os itens que já têm fatia própria — ver "Limite de cobertura" abaixo) **nem declara o preset pronto/decidido**. Não implementa seed, não propõe arquitetura, não decide o que entra no preset nem declara item não aplicável — isso é o passo 8 do Roadmap, separado e posterior a esta consolidação. Repositório de referência de todas as 16 fatias: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4`.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler esta consolidação

- **Classe** normalizada em 5 valores (conforme Roadmap, passo 7): **Baseline persistente reutilizável** (dado/estado que a população inicial do seed já carrega); **Ação de teste/temporária** (mutation/payload/interação de UI criado em tempo de execução por um CT, não preparado de antemão); **Consulta** (função que só lê dados já existentes, não prepara estado); **Dependência observada** (aparece em comentário/shape de código/schema, sem teste real que a exercite); **Comportamento de tela quando aplicável** (interação de UI confirmada, não é dado de preset).
- Quando a fatia-fonte **não permite** decidir com segurança qual das 5 classes se aplica (ex.: achado de produto confirmado verbalmente por Rafael, não por código; ou mecanismo que simplesmente não existe no Playwright `main`), a coluna Classe traz **"A confirmar"** com uma nota curta do motivo — **não force-se nenhuma das 5 categorias** nesse caso.
- **Certeza**: Confirmado / Inferido / A confirmar — exatamente como registrado na fatia-fonte, nunca endurecido nem suavizado aqui.
- **Evidência/link**: aponta para a fatia-fonte (e, quando útil, a função/CT citada nela) — o texto completo da evidência vive só na fatia-fonte, não é repetido aqui.
- **Lacuna/decisão**: o que falta, exatamente como a fatia-fonte registrou — nenhuma lacuna é resolvida, nenhuma decisão de preset é tomada nesta nota.

## Limite de cobertura

**Itens do TR efetivamente cobertos pelas 16 fatias** (por `itens_tr` de cada nota-fonte):

| Fatia | itens_tr | Recorte-fonte (Fase 1) |
|---|---|---|
| [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|02]] | 1.24–1.27 | Recortes 02–03 |
| [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)\|03]] | 1.28–1.29 | Recorte 04 |
| [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|04]] | 1.30–1.31 | Recorte 05 |
| [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|05]] | 1.32, 1.36–1.37 | Recorte 06 |
| [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|06]] | 1.33 | Recorte 07 |
| [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|07]] | 1.34 | Recorte 07 |
| [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|08]] | 1.35.2.2.1 (+.1–.6) | Recorte 07 |
| [[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)\|09]] | 1.35.2.3 | Recorte 07 |
| [[Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)\|10]] | 1.35.2.4 | Recorte 07 |
| [[Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)\|11]] | 1.35.2.5 | Recorte 07 |
| [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|12]] | 1.35.2.6–1.35.2.7 | Recorte 07 |
| [[Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)\|13]] | 1.35.3 | Recorte 07 |
| [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|14]] | 1.35.4 (+1.35.4.1 no corpo) | Recorte 07 |
| [[Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)\|15]] | 1.35.5 | Recorte 07 |
| [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|16]] | 1.40.2–1.40.2.1 | Recorte 08 |
| [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|17]] | 1.40.3 | Recorte 08 |

**Precisão sobre o recorte 07 (1.33–1.35):** foi **mapeado conceitualmente por inteiro na Fase 1** (Matriz: ✅ revisado e aprovado; recorte-fonte: 50/50 itens "Mapeado") — isso vale para **todos** os itens citados a seguir, inclusive os sem fatia própria. Na Fase 2, porém, **só 10 das 16 fatias** pertencem a ele (06–15), e mesmo essas **não cobrem o recorte por inteiro**: os itens `1.35` (introdutório), **`1.35.1`** (linha do tempo geral da tramitação — **sem fatia própria de especificação do preset na Fase 2; já mapeado conceitualmente na Fase 1; citado como fronteira na fatia 15**), `1.35.2` (introdutório), `1.35.2.1` (enum de status — mapeado conceitualmente na Fase 1; na Fase 2, só tocado de forma incidental na fatia 06, por compartilhar o enum com 1.33.3.6; não é escopo próprio dela) e `1.35.2.2` (introdutório) **não têm fatia própria de especificação do preset**. Isso não os torna fora do preset nem "não analisados" — ficam pendentes para o passo 8 decidir se viram fatia futura ou são declarados não aplicáveis/fora do preset, com justificativa.

**Demais recortes:**
- **Recorte 01** (infraestrutura técnica, 1.1–1.23) — sem fatia; decisão já registrada no Mapa geral ("sem elementos de negócio no diagrama"), não uma omissão.
- **Recorte 08** (1.38–1.40) — só `1.40.2–1.40.2.1` e `1.40.3` têm fatia (16, 17); `1.38`, `1.39`, `1.40.1`, `1.40.4–1.40.6` ficam pendentes.
- **Recortes 09, 10, 11** (1.41 chaves de acesso; 1.42 personalização; 1.43 estatísticas) — sem nenhuma fatia ainda.

**Esta nota não declara nenhum desses itens como não aplicável nem decide o que entra no preset candidato** — isso é o passo 8 do Roadmap, posterior e separado desta consolidação.

## Dúvidas de negócio relevantes às linhas abaixo (abertas, não resolvidas aqui)

- **Despacho de etapa (1.30.2) × Despacho na tramitação (1.35.2.2.1)** — mesma dúvida dos recortes 05/07; as fatias 04 e 08 confirmam que não encontraram teste que ligue os dois, sem resolver a identidade.
- **Documento apensado via despacho (1.35.2.2.1.2.a) × Documento associado automaticamente (1.35.4)** — mesma dúvida do recorte 07; as fatias 08 e 14 preservam a dúvida sem resolvê-la.
- **"Contribuinte" (1.32/1.40.3.a) como ator distinto** — dúvida dos recortes 06/08; a fatia 17 confirma que não encontrou evidência de código, sem resolver.
- **Canal Oficial (1.38.1.b) × Jornal Oficial (1.38.3.1)** — dúvida de negócio do Mapa geral, trilha paralela (Roadmap); nenhuma das 16 fatias toca nela diretamente (1.38 não tem fatia própria ainda).

---

## 1. Autenticação, identidade e estrutura organizacional (recortes 02–03 · [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)|fatia 02]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.24.1 | Servidor Público — CPF + senha | Baseline persistente reutilizável | `BASELINE.agents` + pool; CT A02-C01 — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado | — |
| 1.24.2 | Cidadão Pessoa Física — CPF + senha | A confirmar (lacuna de baseline, não há classe aplicável — ator não existe próprio) | reaproveita CPF de servidor — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado (lacuna, não suposição) | Falta cidadão PF próprio no baseline |
| 1.24.3 | Empresa/entidade (PJ) — CNPJ + senha | Baseline persistente reutilizável | `BASELINE.citizens` + pools; CT A02-C03 — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado | — |
| 1.25.1 | Bloqueio por 5 tentativas malsucedidas | A confirmar (mecanismo não existe no Playwright `main`) | só em branch Cypress não mesclada — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado (gap) | Não portado para Playwright |
| 1.25.3.1–4 | 4 estados funcionais (Ativo/Licença/Férias/Inativo) | A confirmar (mecanismo não existe no Playwright `main`) | `WORK_STATUS`/`changePublicAgentWorkStatus` só em branch Cypress (captura HAR) — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado (gap) | Não portado; relação com enum de 1.27.10.1 não especificada pelo TR |
| 1.26 | Setor/Subsetor, hierarquia reparentável | Baseline persistente reutilizável | `BASELINE.sectors`/`subsectors` — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado | — |
| 1.27 | Servidor ↔ Setor (N:N) | Baseline persistente reutilizável (1 setor) + Ação de teste/temporária (2º setor) | `BASELINE.agents` (1 setor) + CT E64 (`editPublicAgent`, 2º setor) — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado | — |
| 1.27.2.1–5 | 5 níveis canônicos de acesso | Baseline persistente reutilizável | `accessLevel` 2–5 (`seqBasic`/`seqSpecialist`/`seqSectorAdmin`/`seqAdmin`) — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado (4 de 5 níveis) | Nível 1 ("Somente leitura") sem identidade própria |
| 1.27.4.4/5.4/6 | Permissão de visualizar/criar Assuntos e Serviços, por nível | A confirmar (confirmação verbal de produto por Rafael, não é dado de seed/código) | contexto de produto, recorte 03 — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado (produto); A confirmar (código) | Regra ainda não verificada no código/seed |
| 1.27.3–7.4 | Escopo de permissão por nível (4 áreas) | A confirmar (não investigado nesta fatia) | — | A confirmar | Fora do escopo da fatia 02 |
| 1.27.10.1/11.2 | Status de atividade (listagem) e presença online/offline | A confirmar (mecanismo não existe no Playwright `main`) | mesmo gap de `WORK_STATUS` acima — [[Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)\|fatia 02]] | Confirmado (gap) | Não portado |

## 2. Serviços, assuntos e categorias de documento (recorte 04 · [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)|fatia 03]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.28/1.28.1 | Serviço/Assunto (cadastro, categoria vinculada) | Baseline persistente reutilizável | `BASELINE.services` (12), `makeService` — [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)\|fatia 03]] | Confirmado | — |
| 1.28 / 1.27.8.2.o | Categoria/Subcategoria de A&S (lacuna (n) do mapa) | Baseline persistente reutilizável (campo existe, nunca exercitado) | `categoryId: null` sempre — [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)\|fatia 03]] | Confirmado (campo não usado) | Lacuna (n) não resolvida por isso |
| 1.28.1.2.1 | Tipos de campo personalizado | Ação de teste/temporária (parcial) | `file`, `bigText`, `informativeText-*` — [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)\|fatia 03]] | Confirmado (parcial) | Demais tipos do enum não verificados |
| 1.29.1 | Categoria-base de documento (3 valores) | Baseline persistente reutilizável | `makeModule`/DO/CO/PA, `documentType` — [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)\|fatia 03]] | Confirmado (uso no seed) | Limite do schema — A confirmar |
| 1.29.2–1.29.9 | 8 categorias específicas de documento | A confirmar (não encontrado) | — | A confirmar | Não localizado no código lido |
| 1.29.10 | Zoneamento/Processo urbanístico | Baseline persistente reutilizável (módulo `PU` específico) | `makeModule(PU, isUrbanisticProcess:true)` — [[Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)\|fatia 03]] | Confirmado (config. do seed) | Não é categoria-base própria no seed; limite do schema — A confirmar |
| 1.29.10.4 | Zona, Categoria de uso | A confirmar (não localizado) | — | A confirmar | — |

## 3. Fluxo de trabalho, Etapa, Despacho de etapa e Modelos de documento (recorte 05 · [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)|fatia 04]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.30 | Status do Fluxo de trabalho (ativo/inativo/rascunho) | Baseline persistente reutilizável (parcial) | `status: 'ACTIVE'` — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado (ACTIVE) | Demais valores não localizados |
| 1.30/1.30.1 | 3 configurações de Fluxo no baseline | Baseline persistente reutilizável | `workflow`/`workflowAttachment`/`workflowFiveSteps` — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado | — |
| 1.30.1 | Etapa — nome/setor responsável/regras de tramitação | Baseline persistente reutilizável | `makeWorkflowInput`, objeto `base` dos steps — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado | — |
| 1.30.2 | Despacho na etapa (customizado, assinatura opcional) | Baseline persistente reutilizável (workflow `workflow`) + Ação de teste/temporária (variante com anexo) | `dispatches`/`dispatchLocations` do step — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado | Identidade com despacho de tramitação (1.35.2.2.1) — ver dúvida acima |
| 1.30.3 | Regras de transição de etapa | A confirmar (não verificado) | — | A confirmar | Comportamento de tela/fluxo, não investigado |
| 1.31.1.1 | Modelo simples | Ação de teste/temporária | `makeDocumentModel`, `simple-model.spec.ts` — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado (valores vistos) | Demais valores de `inheritanceType`/`sharedType`; não integra baseline |
| 1.31.1.2 | Histórico de alterações do modelo | A confirmar (não verificado) | — | A confirmar | — |
| 1.31.2 | Documento automatizado — cadastro do modelo | Ação de teste/temporária | `makeAutomatedDocumentModel` — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado | Não integra baseline |
| 1.31.2.1.3 | Estilização de cabeçalho/rodapé | Ação de teste/temporária | `headerImage*`/`footer*` — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado | — |
| 1.31.2.1.3.1 | Conteúdo/herança de dados (@mentions) | Ação de teste/temporária | `getAllAutomatedDocumentMentionFields` — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado | — |
| 1.31.2.1.3.2 | Validade pré-definida | Ação de teste/temporária | `hasValidity: false` por padrão — [[Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)\|fatia 04]] | Confirmado (campos existem, desativados) | Validade não ativa na config. padrão |
| 1.31.3 | Edição/exclusão de modelos com histórico | A confirmar (não verificado) | — | A confirmar | — |

## 4. Atores externos e atendimento ao cidadão (recorte 06 · [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|fatia 05]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.32 | Contato externo PJ — nome/CNPJ | Baseline persistente reutilizável | `BASELINE.citizens` (5) + pools — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado | — |
| 1.32 | Contato externo PF | A confirmar (mesma lacuna da fatia 02, sem classe aplicável) | reaproveita CPF de servidor — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado (lacuna) | Mesma lacuna da fatia 02 |
| 1.32 | Cadastro único (rejeição de duplicata, PJ) | Ação de teste/temporária | `signup()`, `makeCitizenPJAutoRegistration`; A02-C08 — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado | — |
| 1.32 | Cadastro único/auto-registro PF | A confirmar (não encontrado) | só fábrica PJ existe — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | A confirmar | — |
| 1.32.1 | Confirmação de cadastro por e-mail | Baseline persistente reutilizável (condicional — só quando o cidadão ainda não existe) | `getCitizenOrCreate`, `provision.ts` L.480 — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado (fluxo completo, condicionado) | Não exercitado de novo em instância já provisionada |
| 1.36 | Abertura externa habilitada/desabilitada | Baseline persistente reutilizável | `isOpenExternal`, `services.openExternalDisabled`; A47 — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado | — |
| 1.36 | "Canais digitais do órgão" | A confirmar (não localizado) | — | A confirmar (sem mudança) | — |
| 1.36 | "Entes externos" (terceiro tipo de ator) | A confirmar (sem nova evidência de existência) | `BASELINE.citizens`/pools só têm 2 tipos — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | A confirmar | — |
| 1.37 | Demanda externa (solicitação aberta por cidadão) | Ação de teste/temporária | `makeExternalDocument`/`generateExternalDocument` — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado (mecanismo) | Equivalência com entidade "Demanda" própria — Inferido |
| 1.37 | Interação do cidadão limitada à abertura | Baseline persistente reutilizável | `services.citizenOpeningOnly` — [[Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)\|fatia 05]] | Confirmado | — |
| 1.37 | Usuário externo acompanha/assina/imprime | A confirmar (fora do escopo desta fatia) | coberto em outras fatias (04, 16/17) | A confirmar | — |
| 1.37 | Estado da Demanda (Pausada/Encerrada) | A confirmar (sem verificação nova) | ver recorte 06 | Sem mudança | — |

## 5. Mesa de trabalho (recorte 07, item 1.33 · [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)|fatia 06]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.33.3.1/3.2 | Visualização Kanban/Lista | Baseline persistente reutilizável (restrito ao pool de agentes) | `changeWorkboardViewMode`, laço `b.pools.agent` em `provision.ts` — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado (restrito ao pool) | Não vale para agentes nomeados fora do pool |
| 1.33.3.6/1.35.2.1 | Status de Documento e da Mesa (5 valores) | Consulta | `getWorkboardDocuments` (`includeDocumentContents`) — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado (status do Documento) | Status da Mesa como entidade própria — A confirmar |
| 1.33.3.7 | Reabertura de documentos encerrados | Ação de teste/temporária | `reopenDocumentInSector` — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado (mecanismo existe) | — |
| 1.33.1 | Alternar entre setores / mesas alheias | Baseline persistente reutilizável (restrito ao pool) + Baseline persistente reutilizável (`agentThird.othersWorkboard`) | `changeLastSectorAccessed` — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado | — |
| 1.33.3/3.3/3.4 | Alertas de prazo/status/novas demandas | Consulta | `getWorkboardDocuments` (toggles) — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado (filtros existem) | Equivalência com "alerta" — Inferido |
| 1.33.3.5 | Filtro de prazos vencidos/próximos | Consulta | `getWorkboardDocuments` (`deadline`) — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado | — |
| 1.33.4 | Filtros/busca/ordenação (11 critérios) | Consulta (parcial) | `getWorkboardDocuments` (`term`, `orderBy`, etc.) — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado (parte) | Restante dos critérios — A confirmar |
| 1.33.5.1–3 | Campos por documento na mesa | A confirmar (shape não confirmado) | `WorkboardItem` — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | A confirmar | — |
| 1.33.6 | Ferramenta de rastreio global | Consulta | `trackDocumentObjects` — [[Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)\|fatia 06]] | Confirmado | — |
| 1.33.2/2.1 | Resumo da tela de boas-vindas | A confirmar (não encontrado) | — | A confirmar | Possível reaproveitamento de `getWorkboardDocuments`, não confirmado |

## 6. Etiquetas (recorte 07, item 1.34 · [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)|fatia 07]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.34/1.34.2 | Etiqueta — criação (nome/cor) | Ação de teste/temporária | `createTag`/`makeTagInput`; A40-C01 — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado | Não integra baseline |
| 1.34.1.a | Etiqueta pessoal | Ação de teste/temporária | `sharedType:'NO_SHARE'` — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado (não compartilhada) | Visibilidade restrita à mesa pessoal — A confirmar |
| 1.34.1.b/2.1 | Etiqueta compartilhada entre setores | Ação de teste/temporária | `sharedType:'MY_SECTORS'`; A40-C05 — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado (dado) | Comportamento de tela — A confirmar |
| 1.34.1.2 | Etiqueta padrão "Urgente" | Dependência observada | `LABEL_ID=1` assumido pelo CT, não criado por `provision.ts` — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado (dependência existe) | Ambiente-alvo precisa tê-la pré-existente |
| 1.34.2.2 | Subetiqueta | Ação de teste/temporária | `makeSubTagInput` — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado (estrutura pai/filho) | Herança de compartilhamento — A confirmar |
| 1.34.2.3 | Edição de etiqueta/subetiqueta | Ação de teste/temporária | `updateTag`; A40-C03/C04 — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado | — |
| — | Histórico de etiqueta/subetiqueta | Ação de teste/temporária (gera) + Consulta (lê) | `getTagHistory`; A40-C08/09/10 — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado | — |
| 1.34.2.4 | Alteração reflete em documentos já etiquetados | A confirmar (não verificado) | — | A confirmar | — |
| 1.34.2.5 | Etiqueta excluída permanece em documentos antigos | A confirmar (não verificado) | — | A confirmar | — |
| 1.34.1.3 | Etiqueta como filtro na mesa | A confirmar (sem verificação nova) | `filter.tags` — ver seção 5 | A confirmar | — |
| — | Associação etiqueta ↔ documento | Ação de teste/temporária | `updateDocumentLabel`; A19-C01/C02 — [[Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)\|fatia 07]] | Confirmado | Depende da etiqueta "Urgente" (linha acima) |

## 7. Tramitação de processo administrativo (recorte 07, item 1.35 · fatias 08–15)

### 7.1 Despacho na tramitação ([[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)|fatia 08]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.2.2.1.1 | Despacho — texto livre, anexos, destinatários | Ação de teste/temporária | `makeDispatch`; A14-C01 — [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|fatia 08]] | Confirmado | — |
| 1.35.2.2.1.3 | Despacho sigiloso ou não | Ação de teste/temporária | `withConfidentiality`; A14-C01/C02 — [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|fatia 08]] | Confirmado | — |
| 1.35.2.2.1.4 | Prazo do despacho | Ação de teste/temporária | `makeDeadlineForDispatch`; A14-C03 — [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|fatia 08]] | Confirmado (dado existe) | Regra de não ultrapassar prazo pré-existente — A confirmar |
| 1.35.2.2.1.2.a | Apensar documento via despacho | Ação de teste/temporária | `documentsAssociated`; A14-C04 — [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|fatia 08]] | Confirmado (mecanismo) | Identidade com 1.35.4 — dúvida preservada (ver topo) |
| 1.35.2.2.1.5 | Assinar/solicitar assinatura no despacho | Comportamento de tela quando aplicável | `ui/dispatch.ts` helpers — [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|fatia 08]] | Confirmado (via UI) | Payload de API — A confirmar |
| 1.35.2.2.1.6 | Imprimir despacho emitido | Ação de teste/temporária + Consulta | `getDispatchPrintInfo`; A22-C04 — [[Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)\|fatia 08]] | Confirmado (download existe) | Inclusão de anexos/assinaturas no conteúdo — A confirmar |

### 7.2 Retificação do documento de abertura ([[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)|fatia 09]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.2.3 | Retificar documento de abertura | Ação de teste/temporária | `retifyDocument`; A18-C02/A25-C01 — [[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)\|fatia 09]] | Confirmado | — |
| 1.35.2.3 | Categoria do documento retificável | Ação de teste/temporária | exercitado em PA e DO — [[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)\|fatia 09]] | Confirmado (mecanismo) | Se o TR restringe só a PA — A confirmar |
| 1.35.2.3 | Justificativa legal | Ação de teste/temporária (só valor padrão) | parâmetro `justification` — [[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)\|fatia 09]] | Confirmado (campo existe/enviado) | Adequação legal, customização, validação — A confirmar |
| — | Anexos na retificação | Ação de teste/temporária (campo não exercitado com conteúdo) | parâmetro `attachments` — [[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)\|fatia 09]] | Confirmado (campo existe) | Uso com conteúdo real — A confirmar |
| 1.35.2.3 | Histórico da retificação | Consulta | `getDocumentForAgent`, `isRectified`, `values[]` — [[Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)\|fatia 09]] | Confirmado (versionamento) | Completude do histórico exigido pelo TR — A confirmar |

### 7.3 Solicitação de revisão ([[Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)|fatia 10]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.2.4 | Solicitar revisão (configurada na criação) | Ação de teste/temporária | `makeDocument({withReviews})`; A27-C01 — [[Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)\|fatia 10]] | Confirmado (na criação) | Solicitação posterior à criação — A confirmar |
| 1.35.2.4 | Revisor(es) designado(s) | Ação de teste/temporária | `reviewers[]` — [[Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)\|fatia 10]] | Confirmado (um revisor) | Múltiplos revisores — A confirmar |
| 1.35.2.4 | Aprovação da revisão | Ação de teste/temporária | `approveReview`; A27-C01 — [[Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)\|fatia 10]] | Confirmado (status → REVIEWED) | Mesmo evento ou novo — A confirmar |
| — | Rejeição da revisão | A confirmar (não encontrado) | — | A confirmar | Não presume ausência no produto |
| — | Status inicial do revisor | A confirmar (não verificado) | — | A confirmar | — |
| — | Justificativa do revisor | Dependência observada | shape `justification` — [[Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)\|fatia 10]] | A confirmar | — |
| 1.35.2.4 | Restrição a documentos em pré-elaboração | A confirmar (não verificado) | — | A confirmar | — |

### 7.4 Edição do documento de abertura ([[Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)|fatia 11]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.2.5 | Editar documento de abertura | Ação de teste/temporária | `editDocument`; A17-C01 — [[Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)\|fatia 11]] | Confirmado | — |
| 1.35.2.5 | Estado "pré-elaboração" (DRAFT) | A confirmar (único CT usa `mode:'SEND'`, não `DRAFT`) | — | A confirmar | Não exercitado em documento DRAFT |
| 1.35.2.5 | Edição ≠ retificação (mutations distintas) | Ação de teste/temporária | `editDocumentObject`/`retifyDocumentObject` — [[Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)\|fatia 11]] | Confirmado (mutations distintas) | Se edição gera `versionInfo.type:'edit'` — A confirmar |
| 1.35.2.5 | Histórico de cada edição (valor `'edit'`) | Dependência observada | comentário em `edit-document.spec.ts`, sem asserção — [[Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)\|fatia 11]] | A confirmar | Existência em execução e grafia do valor |

### 7.5 Prazos de documento ([[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|fatia 12]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.2.7.a | Serviço com prazo oficial configurado | Baseline persistente reutilizável (desigual entre os 2 serviços) | `officialPA` (só flag) / `officialPADeadline` (flag+dias+tipo) — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | Confirmado (ambos, níveis diferentes) | Ausência garantida de dias em `officialPA` — A confirmar |
| 1.35.2.7.a | Prazo oficial "torna-se" o prazo do documento | Ação de teste/temporária | `type:'DOCUMENT'` automático via cidadão — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | Confirmado (via cidadão) | Via servidor — A confirmar |
| 1.35.2.7.a | Imutabilidade do prazo oficial | A confirmar (não encontrado) | — | A confirmar | — |
| 1.35.2.7.b | Prazo do documento (manual) | Ação de teste/temporária (UI) | `addDeadlineByUI('document')`; E28-C02 — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | Confirmado (cenário exato) | Equivalência com "sem prazo oficial" do TR — A confirmar |
| 1.35.2.7.b | "Aplicado a todos os envolvidos" | A confirmar (não verificado) | — | A confirmar | — |
| 1.35.2.7.d | Prazo individual | Ação de teste/temporária (UI+API) | `addDeadlineByUI('individual')`, `updateDocumentDeadlines`; E28-C03/A41-C01 — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | Confirmado | — |
| 1.35.2.7.c | Prazo de assinatura | Dependência observada | comentário cita chave `signature` — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | A confirmar | — |
| — | Chave `review` (não mapeada a tipo do TR) | Dependência observada | comentário — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | A confirmar | — |
| 1.35.2.6 | Hierarquia do prazo por setor/servidor | A confirmar (não encontrado) | rótulo "Prazo do setor" só em comentário — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | A confirmar | — |
| — | Contagem de prazo (dias úteis/corridos) | Consulta (helper puro) | `calculateFinalDate` — [[Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)\|fatia 12]] | Confirmado (função) | Uso real de dias corridos — A confirmar |

### 7.6 Encerramento flexível de tramitações ([[Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)|fatia 13]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.3 | Mecanismo único por trás dos 3 alcances | Ação de teste/temporária | `endDocument`; A10/A37/E42 — [[Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)\|fatia 13]] | Confirmado | — |
| 1.35.3.a | Individual por servidor | Ação de teste/temporária | `{user:true}` — [[Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)\|fatia 13]] | Confirmado | "Mantém tramitação normal nos demais" — A confirmar |
| 1.35.3.b | Por setor envolvido | Ação de teste/temporária | `{onlySector:true}`, evento `SECTOR_ENDED` — [[Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)\|fatia 13]] | Confirmado (evento) | Efeito "em massa"/"custódia" como asserção própria — A confirmar |
| 1.35.3.c | Total do documento | Ação de teste/temporária | `endDocument()` sem opções, evento `ENDED` — [[Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)\|fatia 13]] | Confirmado (evento) | `documentStatus` → CLOSED neste caminho — A confirmar |

### 7.7 Documento associado gerado automaticamente ([[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)|fatia 14]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.4 | Gerar Documento automatizado, vínculo automático ao emissor | Ação de teste/temporária | `generateAutomatedDocument`; A07-C03/E08-C01 — [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|fatia 14]] | Confirmado | Não preparado por `provision.ts` |
| 1.35.4 | "De outro módulo" | A confirmar (não confirmado) | todos os testes usam o mesmo módulo nos 2 lados — [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|fatia 14]] | A confirmar | — |
| 1.35.4 | "Conforme parametrização prévia" | Ação de teste/temporária (parcial) | vínculo obrigatório modelo↔serviço — [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|fatia 14]] | Confirmado (vínculo) | Regra de filtragem na tela — A confirmar |
| 1.35.4.1 | Identificação reversa no documento emissor | Dependência observada | campo `generatorDocuments` no schema, não exposto no tipo TS — [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|fatia 14]] | A confirmar | — |
| 1.35.4.1 | Impressão do documento gerado (filho) | Ação de teste/temporária | PDF do filho, dados herdados — [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|fatia 14]] | Confirmado (direção do filho) | Direção literal do TR (associado na impressão do emissor) — A confirmar |
| 1.35.4.1 | Associado incluído na impressão do emissor | Dependência observada | `selectAllPrintMap`/`associatedDocuments` — [[Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)\|fatia 14]] | A confirmar | Direção literal do TR não exercitada por teste |

### 7.8 Histórico do documento/processo ([[Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)|fatia 15]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.35.5 | Geração das versões do histórico (criação/retificação) | Ação de teste/temporária | criação gera versão `'initial'` (A18-C01); retificação gera versão `'retification'` (A18-C02/A25-C01) — [[Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)\|fatia 15]] | Confirmado | — |
| 1.35.5 | Leitura do array de versões (`values[]`) — mesmo mecanismo para criação e retificação | Consulta (não prepara estado, só lê as versões já geradas) | `getDocumentForAgent(...).values` — [[Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)\|fatia 15]] | Confirmado | — |
| 1.35.5 | Histórico cobre também edições | A confirmar (mesma lacuna da fatia 11) | — | A confirmar | — |
| — | Histórico acumulado (3+ versões) | A confirmar (não testado) | — | A confirmar | — |
| — | Metadados por versão (autor/data) | A confirmar (não confirmado) | — | A confirmar | — |
| 1.35.5 | Botão "histórico" na tela do documento | Comportamento de tela quando aplicável | E18-C04, presença na toolbar — [[Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)\|fatia 15]] | Confirmado (presença) | Conteúdo da tela — A confirmar |
| — | Visibilidade condicional do botão | A confirmar (não conclusivo) | — | A confirmar | — |

## 8. Assinaturas — tipos e solicitação (recorte 08, itens 1.40.2–1.40.3 · fatias 16–17)

### 8.1 Tipos de assinatura ([[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|fatia 16]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.40.2 | Campo `type` no payload de assinatura | Ação de teste/temporária | `makeSignRequest`, `executeSignatures` — [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|fatia 16]] | Confirmado (campo existe, valor único exercitado) | — |
| 1.40.2.1.a | Eletrônica simples — canal UI | Ação de teste/temporária | `fillSignaturePassword`, 14 arquivos — [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|fatia 16]] | Confirmado | — |
| 1.40.2.1.a | Eletrônica simples — canal API | Ação de teste/temporária | `type:'SOGOV'` enviado — [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|fatia 16]] | Confirmado (valor enviado) | Mecanismo de autenticação; correspondência com a taxonomia do TR — A confirmar |
| 1.40.2.1.b/c | Avançada/qualificada (certificado ICP-Brasil) | A confirmar (nenhuma cobertura) | busca por `'ICP'` sem resultado — [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|fatia 16]] | A confirmar | — |
| — | `type:'SOGOV'` no workflow do baseline | Baseline persistente reutilizável (condicional) | `makeWorkflowInput`; `workflow`/`workflowAttachment` — [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|fatia 16]] | Confirmado (payload, 2 de 3) | Persistência quando workflow já preexiste — A confirmar |
| — | Modal "Assinaturas digitais" (seleção de tipo), citado em comentário de teste | Dependência observada | E37 — comentário do teste + 2 asserções **negativas** de ausência num fluxo específico (emitir e assinar, cidadão) — [[Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)\|fatia 16]] | Confirmado (referência/comentário no teste, e a ausência do modal nesse fluxo específico); A confirmar (se o modal é de fato renderizado/aberto em algum fluxo — nunca verificado por asserção positiva) | Conteúdo/seleção dentro dele, e sua existência em runtime fora do fluxo testado — nunca exercitados |

### 8.2 Solicitação de assinaturas ([[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)|fatia 17]])

| Ref. TR | Ator/entidade/dado/estado/relação | Classe | Evidência/link | Certeza | Lacuna/decisão |
|---|---|---|---|---|---|
| 1.40.3 | Quem solicita: servidor | Ação de teste/temporária | sempre `agent.api` — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado (o que é exercitado) | Restrição ativa contra cidadão solicitar — A confirmar |
| 1.40.3.a | Signatário interno (servidor) | Ação de teste/temporária | `organizationalComponentId:sector.id`; A30-C01–C08 — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado | — |
| 1.40.3.a | Signatário externo (cidadão) | Ação de teste/temporária | `organizationalComponentId:null`; A30-C12–C17 — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado | — |
| 1.40.3.a | "Contribuinte" como ator distinto | A confirmar (não encontrado) | — | A confirmar | Dúvida do recorte 08 preservada (ver topo) |
| — | Cidadão assinando anexo via sessão do servidor | Ação de teste/temporária (achado lateral) | A30-C14–C17 — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado (padrão repetido) | Se é exigência real de backend — A confirmar |
| 1.40.3.b | Sequencial — execução na ordem escolhida | Ação de teste/temporária + Baseline persistente reutilizável (identidades `seqBasic`–`seqAdmin`, `engineer`/`architect`/`manager`) | E40-C01, E34-S08 — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado (execução na ordem) | Se o sistema grava/aplica a ordem — A confirmar |
| 1.40.3.b | Bloqueio até a vez (enforcement) | A confirmar (não exercitado nem assertado) | — | A confirmar | — |
| 1.40.3.c | Permissões/regras de tramitação na seleção | A confirmar (não encontrado) | — | A confirmar | — |
| 1.40.3.d | Locais de assinatura (solicitar/executar) | Ação de teste/temporária | 4 tipos de local; A30-C01–C07/C12–C17 — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado | — |
| 1.40.3.d | Status `SIGNED` por local (multi-local) | Ação de teste/temporária (parcial) | só o 1º local lido em multi-local — [[Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)\|fatia 17]] | Confirmado (local único) | Locais adicionais — A confirmar |

---

## Fontes

Todas as linhas acima vêm exclusivamente das 16 fatias aprovadas (notas 02–17 em `01 Modelo do preset/Especificações do preset piloto/`), cada uma linkada por linha/grupo. Nenhuma evidência de código/teste foi relida ou reverificada nesta rodada — esta nota só reorganiza e normaliza vocabulário do que as fatias já registraram. Commit de referência citado por todas as fatias-fonte: `16c41e4` (repositório `sogov-automation-playwright`).
