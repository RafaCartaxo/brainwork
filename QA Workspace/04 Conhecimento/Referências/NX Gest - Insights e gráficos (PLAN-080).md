---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-08-25
---
# NX Gest - Insights e gráficos (PLAN-080)

> [!info] Sobre esta nota
> Correção de direção para o **PLAN-080** (📝 Planejado, não implementado) do repo pessoal `RafaCartaxo/nxgest` — **não é sistema Sogov**. Acervo pesquisável, na regra 2 de [[../README|04 Conhecimento]].
> Notas irmãs: [[NX Gest - Reposicionamento de identidade (PLAN-085)]] · [[NX Gest - Navegação escalável (PLAN-081)]] · [[NX Gest - Contrato periodicidade alternada (PLAN-087)]].
> **Antes de executar:** [[NX Gest - Handoff de execução]] — ordem entre os planos, setup, baseline e colisões.

> [!tip] Desacoplado do PLAN-081
> A revisão do PLAN-081 decidiu que `insights` entra na aba **"Mais"** (a Rota fica primária). Como a Fase 1 daqui entrega `/insights` alcançável por URL **sem item de nav**, este plano **deixou de depender** do PLAN-081 para entregar — ele virou pré-requisito só de **descoberta**. Ver [[NX Gest - Navegação escalável (PLAN-081)]].

> [!warning] Numeração provisória
> `PLAN-085`, `PLAN-086` e `PLAN-087` são rótulos de trabalho — **no repo o último plano é o PLAN-084**. O número definitivo é atribuído quando cada plano for criado, na ordem em que efetivamente entrar. Não pré-reservar número (de PLAN nem de BR).

## Visão geral

- **O quê:** o PLAN-080 propõe um módulo whitelabel `insights` (read-only) com 5 gráficos em Recharts, página própria `/insights`, backend `src/modules/insights/`. Esta nota registra as correções de direção antes de alguém implementar.
- **Por que corrigir agora:** está **planejado, não implementado** — mudar custa zero. Executado como está, o custo apareceria em dois lugares caros: um gráfico que seria re-removido, e uma expansão de `dependsOn` que exigiria re-PATCH em todos os tenants.
- **Estado:** direção aprovada em 21/08/2026. Nada implementado.

## Visão geral do que o plano já acerta

Não é plano solto: D1..D11 com decisão justificada, registro no Module Manifest (W1/W2/W3), CTs de toggle, gating por `requireModule`, isolamento por `resolveScope`, e segue o padrão de agregação SQL do PLAN-083 (concluído). A dependência do PLAN-081 é real — a tab bar mobile satura em 5 abas e `insights` seria o 6º item.

## Regras de negócio

### Os três defeitos reais

**1. Ressuscita um gráfico já deletado, na fonte já julgada furada.**
`snapshots_atraso` é escrito **sob demanda** (`ListarHistoricoAtrasosUseCase.ts:10` chama `registrarSnapshotAtraso` ao abrir a view, upsert 1/dia) e **não existe scheduler no projeto** — a única menção a cron é um comentário dizendo "não por cron"; o cron do VPS é backup. A série só tem ponto nos dias em que alguém abriu a tela.

E já foi decidido antes — `docs/UPDATES.md:795`:

> **Removido**: o bloco "Histórico de atrasos" da view de atrasados (gráfico de evolução + tabela de `snapshots_atraso`) — o snapshot só era gravado ao abrir as Cobranças (sem job diário) → **dado esparso** […] O endpoint `historico-atrasos` permanece no backend (API-UC-022).

Agrava: é por `user_id`, não por empresa — para admin/sócio a série soma amostragens com buracos **diferentes por operador** (um dia em que 3 de 5 abriram a tela produz valor menor sem nada ter melhorado). E backfill é impossível por construção: o parâmetro `data?` existe mas nunca é passado, e a query recalcula o atraso **de hoje** a partir de `saldo_pendente`.

**2. A expansão do `dependsOn` (D10) é a única decisão irreversível — e quebra tenants.**
`validateModulos` (`modules.ts:128-148`) trata `dependsOn` como requisito duro (422, *"O módulo X requer: Y"*). Com a cadeia transitiva (`gastos → caixa`, `contratos → clientes`), a Fase 2 do D10 (`["contratos","caixa","gastos"]`) faria `insights` exigir **4 dos 7** módulos — empresa sem `gastos` não conseguiria ativar insights de jeito nenhum.

Assimetria que define a ordem: mudar `dependsOn` de módulo já provisionado é **breaking change** (re-PATCH em todos os tenants, trade-off nomeado no ADR-006); um campo novo no manifest seria aditivo e indolor. Logo: decidir `dependsOn` agora, adiar campo novo indefinidamente.

**3. O critério de aceite de cor é vacuamente satisfeito.**
`audit-styles.mjs:26` tem `PALETTE = ["blue","indigo",…]` e o regex caça **classes Tailwind** (`bg-blue-500`). Recharts recebe cor por prop string: `fill="#3b82f6"` passa limpo. "Cores seguem o tema, `audit:styles` limpo" não prova nada para gráficos.

### Classificação de dado por gráfico — a espinha da correção

O plano deve declarar, **por gráfico**, a classe da fonte. CT deve falhar se gráfico de série apontar para classe 3 ou 4.

| Classe | Fontes | Propriedade | Uso permitido |
|---|---|---|---|
| **1. Evento** (append-only, data própria) | `pagamentos`, `pagamento_parcelas`, `movimentacoes_financeiras`, `gastos`, `historico_operacional` | completa, exata, retroativa | **série temporal** |
| **2. Cronograma imutável** | `parcelas.valor_previsto`, `parcelas.data_vencimento` | escritos na criação do contrato e **nunca atualizados** (verificado: zero `UPDATE` nessas colunas em todo o backend) | **série temporal** |
| **3. Estado mutável** | `parcelas.saldo_pendente`/`estado`/`data_quitacao`, `caixa_config` | válido só "agora", sem histórico | **snapshot do presente** — nunca série |
| **4. Snapshot amostrado** | `snapshots_atraso` | amostragem oportunista, buracos por operador | **nenhum gráfico** |

> [!warning] Armadilha de implementação
> Para valor histórico, `saldo_pendente` **não serve** (estado atual) e `data_quitacao` só é escrita na quitação **total** — pagamento parcial não deixa data em `parcelas`. Valor atrasado/recebido em D reconstrói-se do event log: `Σ parcelas.valor_previsto (data_vencimento ≤ D) − Σ pagamento_parcelas.valor JOIN pagamentos WHERE pagamentos.data ≤ D`, tratando `pagamentos.estornado_em` como evento datado (estorno posterior a D não reduz o valor em D) e respeitando os `deleted_at`. Sem essa frase no plano, quem implementar usa `saldo_pendente` e produz série lisa e errada.

### Decisões de produto fechadas

**"Performance: meta × real" → não existe meta; é "previsto × recebido".** Não há entidade de meta no schema. Mas como o cronograma é **classe 2** (imutável), "previsto no período" = `SUM(valor_previsto)` por `data_vencimento` e "recebido no período" vem do event log. Comparação factual e retroativa, cabe na Fase 1. **Renomear** — chamar de meta um número que o usuário nunca definiu é prometer o que não existe. Meta de verdade (admin define alvo) é entidade nova: tabela + CRUD + BR + tela; plano próprio, não ponta de gráfico.

**"Ranking de operadores" → "contribuição", sem placar.** Mostrar composição do total por operador em vez de ordenar do melhor ao pior: mesma informação de gestão, sem gamificar pessoas. Precedente no repo: `ContribuicaoModal` no admin. Fase 2.

### Resumo das mudanças no PLAN-080

| # | Mudança |
|---|---|
| D1, D9 | **Manter** — módulo único read-only, página própria, `widgets: []` |
| D10 | **Reescrever** — `dependsOn: []` permanente + degradação graciosa por gráfico + empty-states. Nunca expandir |
| D12 (novo) | Classe de dado por gráfico (4 classes) + veto a `snapshots_atraso`, citando `UPDATES.md:795` |
| D13 (novo) | Endpoint agregado único por fase (`/api/insights/resumo?periodo=`), padrão PLAN-083 |
| D14 (novo) | Regra de hex no `audit:styles` + sonda no `chartColors.ts` (ref. `favicon.ts:22`) |
| Fase 1 | Só classes 1 e 2. Sai tendência de atraso; "meta × real" vira "previsto × recebido" |
| Fase 2 | "Ranking" vira "contribuição" |
| PLAN-081 | Desacoplar — pré-requisito de **descoberta** (item de nav), não de **entrega** |

## Comportamentos observados em teste

### Reuso: o que dá e o que não dá

**Para série, não há reuso.** Verificado: `getFluxoConsolidado` (`caixa.repository.impl.ts:209-247`) retorna **escalares** via scan com `SUM(...) FILTER` — sem `date_trunc`, sem `GROUP BY`. `/api/gastos` retorna `totalPeriodo` escalar e **não existe nenhum `GROUP BY categoria` no repo**. `/api/operacoes/cobrancas` dá indicadores do dia.

- **Sem endpoint novo:** só gráficos de "estado do presente" montáveis de escalares.
- **Endpoint novo inevitável:** toda série (`date_trunc` + `GROUP BY`), donut por categoria, contribuição por operador. Nenhum endpoint atual tem dimensão temporal na saída.
- **Não reusar `/api/operacoes/historico-atrasos`** — é o único que *parece* servir e o único que não serve.

### Riscos técnicos

- **`chartColors.ts` precisa da técnica de sonda.** Tokens são compostos (`--color-success-hover: color-mix(in oklab, …)`, `index.css:150`), então `getComputedStyle(el).getPropertyValue("--x")` devolve **o texto do token**, não a cor — passar isso para `fill` de um `<path>` deixa o gráfico invisível. Precedente correto: `shared/theme/favicon.ts:22` (elemento sonda com `color: var(--…)`, leitura da propriedade resolvida).
- **Troca de tema em runtime:** cor resolvida uma vez no render não reage a dark, aos 5 temas (`index.css:53-54`) nem a `--tenant-primary`.
- **jsdom não resolve `color-mix()` nem `var()` sem CSS:** `getComputedStyle` devolve `""`. Precisa de fallback determinístico, e o CT deve asserir **o fallback** — teste de cor em jsdom valida o mock, não o produto.
- **Pool PG:** `max: 10` para o processo inteiro (`database.ts:33`); o PLAN-077 já registra ~13 queries ao montar Dashboard + Caixa. Página com 5 React Query em agregação `GROUP BY` satura. Mitigar em ordem: (1) endpoint único (D13); (2) `staleTime` longo, sem `refetchOnWindowFocus`; (3) só então medir `PG_POOL_MAX` contra o `max_connections` do Postgres.
- **Landmine do gate:** o regex de `audit-modules.mjs:44` espera exatamente `{ id, labelKey, descricaoKey, dependsOn, … }`. Propriedade inserida **antes** de `dependsOn` nas entradas de `MODULES` faz o parse voltar vazio e o gate falhar com "MODULES não parseado" — mensagem que não aponta para a causa.

### Proposta descartada (registrada para não voltar)

Cogitei inverter o D1 e criar um campo `graficos` no manifest, para cada módulo declarar os seus e a página compor — "igual o ADR-006 fez com a Central". **Derrubada por três fatos:**

1. **O padrão não existe.** `OperacoesDashboard.tsx:29-33` são cinco booleanos escritos à mão (`contratosAtivo`, `gastosAtivo`…). `isWidgetActive` alimenta flags; `MODULE_WIDGETS` é tabela de nomes, não registro de componentes. A "Central composável" do ADR-006 é aspiracional — o `04-ROADMAP.md:606` lista "dashboard que compõe qualquer conjunto de módulos" como **F4**.
2. **"1 dono" não modela gráfico.** Widget = 1 KPI = 1 tabela = 1 módulo. Gráfico = 1..N fontes: o cartão de fluxo usa `gastos.categoria` (dono `gastos`) **e** `movimentacoes_financeiras` (dono `caixa`).
3. **O "ganho presente" era falso.** Na Fase 1 o `dependsOn` é `["contratos"]`; `gastos` não entra. Empresa sem `gastos` tem insights hoje.

Nota de fundo: `audit-modules.mjs` valida `MODULE_WIDGETS` do **frontend**; o campo `widgets` do backend **nunca é comparado com nada** — é documentação inerte.

---

## Checklist de execução

> [!important] Como usar
> Ordem obrigatória: **Fase 0 → 0.5 → 1 → 1.5 → 2**. Os vetos valem em todas as fases. Cada item de gate tem o comando que o prova.

### Vetos permanentes (conferir em toda entrega)

- [ ] Nenhum gráfico tem `snapshots_atraso` como fonte (classe 4)
- [ ] Nenhum gráfico de **série** usa fonte classe 3 (`saldo_pendente`, `estado`, `data_quitacao`, `caixa_config`)
- [ ] `insights.dependsOn` continua `[]` — **não** foi expandido para `caixa`/`gastos`
- [ ] Nenhum literal `#rrggbb` / `rgb(` / `hsl(` em arquivo de gráfico
- [ ] `/api/operacoes/historico-atrasos` **não** é consumido pelo insights
- [ ] Nenhuma propriedade nova inserida **antes** de `dependsOn` nas entradas de `MODULES`

### Fase 0 — base, sem módulo e sem nav (desbloqueia o PLAN-082 em paralelo)

- [ ] `recharts` adicionado ao `frontend/package.json`
- [ ] `frontend/src/shared/components/ChartCard/ChartCard.tsx` criado, só com tokens
- [ ] `frontend/src/shared/utils/chartColors.ts` com **técnica de sonda** (referência: `shared/theme/favicon.ts:22`) — não ler custom property direto
- [ ] `resolveChartColor` re-resolve na troca de tema (dark + 5 paletas + `--tenant-primary`)
- [ ] Fallback determinístico para jsdom; CT assere **o fallback**, não cor real
- [ ] Mock de `ResizeObserver` em `frontend/src/test/setup.ts` (compartilhado com PLAN-082)
- [ ] Regra de hex adicionada ao `scripts/audit-styles.mjs` para `modules/insights/**` e `ChartCard/**` (D14)
- [ ] `docs/engineering/design/UI-COVERAGE.md` atualizado com o `ChartCard`
- [ ] Gates: `npm run audit:styles` · `npm run audit:ui` · `npm test` · `npm run build`

### Fase 0.5 — decisões irreversíveis, tomadas uma vez (custo ~zero, é doc)

- [ ] PLAN-080 atualizado: **D10 reescrito** para `dependsOn: []` permanente
- [ ] PLAN-080 atualizado: **D12** (classe de dado por gráfico) com a tabela das 4 classes
- [ ] PLAN-080 atualizado: veto a `snapshots_atraso` citando `docs/UPDATES.md:795`
- [ ] PLAN-080 atualizado: **D13** (endpoint agregado único) e **D14** (hex + sonda)
- [ ] PLAN-080 atualizado: "meta × real" renomeado para "previsto × recebido"; meta real remetida a plano próprio
- [ ] PLAN-080 atualizado: "ranking" trocado por "contribuição"
- [ ] PLAN-080 atualizado: Fase 1 sem tendência de atraso e sem nav
- [ ] Depreciação do `snapshots_atraso` registrada com gatilho ("quando existir job agendado, ou quando o último consumidor sair")
- [ ] Registrado que o endpoint `historico-atrasos` permanece por compatibilidade (API-UC-022 / BR-086)

### Fase 1 — backend + página, só classes 1 e 2

- [ ] `insights` adicionado à union `ModuleId` em `src/modules/admin/domain/modules.ts` (W1)
- [ ] Entrada no `MODULE_MANIFEST` com `widgets: []`, `capacidades: []`, `dependsOn: []`
- [ ] Espelho em `frontend/src/shared/modules/modules.ts` + `MODULE_WIDGETS.insights = []`
- [ ] `npm run audit:modules` limpo (IDs, espelho, grafo sem ciclo, widget com 1 dono)
- [ ] Endpoint **único** `/api/insights/resumo?periodo=` (D13), não 5 rotas
- [ ] Montado com `authMiddleware` + `userRateLimit` + `requireModule("insights")`
- [ ] Agregação em SQL no padrão PLAN-083 (`date_trunc` + `GROUP BY`, sem N+1)
- [ ] Isolamento por `resolveScope`/`resolveUsuarioAlvo` (operador = próprio; admin/sócio = subárvore)
- [ ] Gráfico "tendência de recebimentos" — fonte classe 1 (`pagamentos`/`movimentacoes_financeiras`)
- [ ] Gráfico "previsto × recebido" — previsto de classe 2 (`valor_previsto` por `data_vencimento`), recebido de classe 1 reconstruído do event log (ver armadilha acima)
- [ ] Cada bloco gated por `hasModule(<dono>)` com **empty-state próprio**
- [ ] **Empty-state da página** ("nenhum insight disponível para os módulos ativos") — sem ele, tenant sem `contratos` vê página vazia, pior que 403
- [ ] Declarado no plano que a perda da cascata W2 é **intencional** (read-only, sem estado órfão)
- [ ] Rota `/insights` no `App.tsx` (lazy, `RequireModule`) — **sem item de nav**
- [ ] i18n `insights.*` + `modules.insights*` nos 3 idiomas, com paridade de chaves
- [ ] `docs/engineering/02-API.md` atualizado + `npm run docs:collection`
- [ ] UCs em `06-CASOS-DE-USO.md` + CTs em `07-CASOS-DE-USO-API.md` + linha em `08-UC-MODULOS.md`
- [ ] CT: `GET /api/insights/*` com módulo off → `403 MODULE_DISABLED`, sem vazar dado
- [ ] CT: nova empresa nasce com `insights` on; desligar sem `force` → `200` (read-only)
- [ ] CT: gráfico de série aponta para fonte classe 1 ou 2 — **falha** se apontar 3 ou 4
- [ ] `staleTime` longo no React Query, sem `refetchOnWindowFocus`
- [ ] Gates: `npm test` · `audit:modules` · `audit:ui` · `audit:styles` · `docs:audit` · `smoke:api`

### Fase 1.5 — navegação

- [ ] PLAN-081 concluído (tab bar com aba "Mais", sidebar colapsável, registro `nav.ts`)
- [ ] Item de nav do `insights` adicionado **só agora**, via `hasModule`
- [ ] Verificado que a tab bar não estourou (cap de 5 primários)

### Fase 2 — classe 3 e agregações caras

- [ ] Carteira / envelhecimento como **snapshot do presente** (classe 3), nunca série
- [ ] Gastos por categoria (`GROUP BY categoria` — não existe hoje no repo)
- [ ] **Contribuição** por operador (não ranking) — composição do total, sem ordenar pessoas
- [ ] `dependsOn` **continua** `[]`; granularidade por gráfico via `hasModule` do dono
- [ ] Reavaliar se vale usar `CAPABILITY_MANIFEST` (já existe e já é auditado) para granularidade fina por empresa
- [ ] Medido o impacto no pool PG antes de liberar (5 gráficos + Central + Caixa simultâneos)

## Dúvidas em aberto

- [ ] Meta de verdade (admin define alvo por operador/período) — vale plano próprio? Depende de decisão de negócio
- [ ] `snapshots_atraso` fica redundante para gráfico; vale planejar remoção da tabela, ou manter só por compatibilidade indefinidamente?
- [ ] Se um job agendado for introduzido no futuro (hoje não existe scheduler no projeto), a classe 4 vira classe 1 e a tendência de atraso volta a ser viável — registrar como gatilho

## Cards relacionados

- Nenhum. Produto próprio, fora do escopo Sogov.

## Referências

- Plano completo da sessão: `~/.claude/plans/eu-tinha-te-deixado-shiny-hummingbird.md` (Parte 2)
- Nota par: [[NX Gest - Reposicionamento de identidade (PLAN-085)]]
- Planos do repo: `docs/plans/PLAN-080-insights-dashboard.md` (📝 Planejado) · `PLAN-081-navegacao-escalavel.md` (📝) · `PLAN-082-devboard-recharts.md` (📝) · `PLAN-083-otimizacao-consultas-busca.md` (✅ Concluído) · `PLAN-077` (performance)
- Código citado: `src/modules/admin/domain/modules.ts` · `src/modules/operacoes/application/use-cases/ListarHistoricoAtrasos/` · `src/modules/caixa/infrastructure/repositories/caixa.repository.impl.ts` · `frontend/src/modules/operacoes/pages/OperacoesDashboard.tsx` · `frontend/src/shared/theme/favicon.ts` · `scripts/audit-modules.mjs` · `scripts/audit-styles.mjs`
- Convenções do vault: [[../../../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] · [[../README|04 Conhecimento]] regra 2
