---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-08-25
---
# NX Gest - Contrato periodicidade alternada (PLAN-087)

> [!info] Sobre esta nota
> Plano fechado, **não executado**, para o repo pessoal `RafaCartaxo/nxgest` — **não é sistema Sogov**. Acervo pesquisável, na regra 2 de [[../README|04 Conhecimento]].
> Notas irmãs: [[NX Gest - Reposicionamento de identidade (PLAN-085)]] · [[NX Gest - Insights e gráficos (PLAN-080)]] · [[NX Gest - Navegação escalável (PLAN-081)]].
> **Antes de executar:** [[NX Gest - Handoff de execução]] — ordem entre os planos, setup, baseline e colisões.

> [!warning] Numeração provisória
> `PLAN-085`, `PLAN-086` e `PLAN-087` são rótulos de trabalho — **no repo o último plano é o PLAN-084**. O número definitivo é atribuído quando cada plano for criado, na ordem em que efetivamente entrar. Não pré-reservar número (de PLAN nem de BR).

## Visão geral

- **O quê:** adicionar um terceiro modelo de contrato — **pagar dia sim, dia não** — como valor novo de `periodicidade`, chamado `alternada`.
- **Regra:** intervalo de 2 dias. Fechou o contrato na segunda, começa quarta; fechou terça, começa quinta. Respeita domingo como os outros modelos.
- **Padrão comercial:** ~20 dias → **10 parcelas**.
- **Estado:** plano fechado em 25/08/2026. Nada implementado.
- **Origem:** modelo já em uso pelos clientes que o sistema não representava.

## Regras de negócio

### Os 2 modelos que já existem (PLAN-076, 14/08/2026)

| modelo | intervalo | regra de domingo | default de parcelas | span |
|---|---|---|---|---|
| `diaria` (default) | +1 dia | desliza domingo → segunda (BR-042) | 20 | ~20 dias |
| `semanal` | +7 dias | não aplica (dia da semana é fixo); **não pode iniciar em domingo** (BR-040-A) | 3 | ~21 dias |
| **`alternada`** (novo) | **+2 dias** | desliza domingo → segunda | **10** | ~20 dias nominais |

Os três convergem em ~20 dias — o **10** não é arbitrário, é o valor que mantém a duração do contrato alinhada aos outros dois.

### Por que é a mudança mais barata possível

A abstração atual é **intervalo em dias — um número**:

```ts
/** Intervalo em dias entre vencimentos — diária = 1, semanal = 7 (PLAN-076). */
export function intervaloDePeriodicidade(periodicidade: Periodicidade): number {
  return periodicidade === "semanal" ? 7 : 1
}
```

`alternada` é intervalo fixo → **encaixa sem tocar na abstração**. (Um modelo mensal, por contraste, exigiria trocar o retorno `number` por uma função que avança data, e supersederia a fórmula da BR-042-A por completo.)

Três consequências verificadas que **reduzem** o escopo:

1. **Zero migração.** A coluna é `periodicidade TEXT NOT NULL DEFAULT 'diaria'` (`database.ts:123, 444`), **sem CHECK constraint**. O valor novo passa a ser aceito sem `ALTER TABLE`.
2. **Zero validação nova.** A BR-040-A bloqueia `semanal` iniciando em domingo porque ali o dia da semana é fixo — todas as parcelas cairiam em domingo. No intervalo 2 o dia varia, então **não precisa de `superRefine`**.
3. **Zero mudança no loop.** `gerarParcelas` faz `setDate(+intervalo)` e `ajustarDomingo` **antes** de criar a parcela (`gerar-parcelas.ts:53-54`) — é isso que já produz "fechou segunda, começa quarta" com intervalo 2, sem caso especial.

### Decisões fechadas

- **Nome do valor:** `alternada` — segue o padrão dos atuais (adjetivo único, sem espaço). É valor **persistido**; renomear depois exigiria migração de dados.
- **i18n:** pt-BR "Alternada" · en "Every other day" · es "Día por medio".
- **Rótulo do botão:** só o nome, sem subtexto de intervalo — três palavras curtas cabem em `grid-cols-3` no mobile.
- **Default de parcelas:** **10**.

### BRs necessárias

BR é imutável e as atuais enumeram só 2 valores, então são **2 BRs novas** (números atribuídos no momento da escrita, sem pré-reserva):

- Periodicidade `alternada`: intervalo 2, primeiro vencimento em `dataInicio+2`, sem restrição de dia de início — com nota de que **estende a BR-039** (que diz "diárias OU semanais").
- `dataFinal` com intervalo `1 | 2 | 7` — com nota de **revogação da BR-042-A**, cuja fórmula `dataInicio + quantidadeParcelas × intervalo` enumera só 1 e 7.

## Comportamentos observados em teste

### Traçado do comportamento (não presumido)

Com intervalo 2 + deslize de domingo, o padrão **converge para segunda/quarta/sexta**:

- **Início segunda:** qua · sex · `dom→seg` · qua · sex · `dom→seg` · qua · sex · `dom→seg` · qua
- **Início terça:** qui · sáb · seg · qua · sex · `dom→seg` · qua · sex · `dom→seg` · qua

Ritmo estável de 3 visitas por semana — propriedade desejável para quem roda rota, **não** efeito colateral a corrigir.

**Nunca gera parcela duplicada nem em dias consecutivos:** se cai sábado, a próxima é segunda (+2); se cai sexta, a próxima é `domingo→segunda`. Sem colisão.

> [!important] O span real é 22-23 dias, não 20
> Os 2-3 deslizes de domingo somam dias. Isso **já acontece hoje na `diaria`** (20 parcelas de +1 dia também terminam em ~23 dias), então é consistente com o comportamento existente. Registrar para que "padrão de 20 dias" não seja lido como garantia — e para ninguém "corrigir" isso depois achando que é bug.

### 🚨 O risco real: a lógica de intervalo existe duas vezes

```
src/modules/contrato/domain/services/gerar-parcelas.ts:6-8      (backend)
frontend/src/modules/contrato/utils/calcularDataFinal.ts:5-7    (frontend — cópia literal, mesmo comentário)
```

Duas implementações independentes da mesma regra. Se `alternada` entrar em só uma, **o formulário mostra uma `dataFinal` e o backend grava outra** — sem erro, sem teste falhando, sem gate reclamando. O `audit:modules` protege o espelho do Module Manifest; **nada protege este**.

Mitigação obrigatória: teste-espelho com a mesma matriz de casos nos dois lados, e linha na matriz de propagação da SKILL-009 registrando que os dois arquivos mudam juntos. Sem isso, a próxima periodicidade repete o problema.

### Ponto de atenção no formulário

O default de parcelas é um **ternário duplicado**, e três modelos não caberão nele:

```
ContratoForm.tsx:52    quantidadeParcelas: initial?.quantidadeParcelas ?? (periodicidadeInicial === "semanal" ? "3" : "20")
ContratoForm.tsx:122   form.setValue("quantidadeParcelas", p === "semanal" ? "3" : "20")
```

Vira lookup (`{diaria:"20", alternada:"10", semanal:"3"}`) — **nos dois lugares, ou divergem**. O grid dos botões é `grid-cols-2` fixo (l.114) e vai para 3.

---

## Checklist de execução

> [!important] Como usar
> Ordem: **F0 → F4**. Os vetos valem em toda a execução.

### Vetos permanentes

- [ ] `alternada` **não** é renomeado depois — é valor persistido; renomear exigiria migração de dados
- [ ] **Nenhum** `ALTER TABLE` / mudança em `src/database.ts` (a coluna é TEXT sem CHECK)
- [ ] **Nenhum** `superRefine` novo (o bloqueio de domingo é exclusivo do `semanal`)
- [ ] Nenhuma BR existente reescrita — BR é imutável; as 2 novas citam BR-039 e BR-042-A por nota
- [ ] **Nenhum número de BR ou PLAN pré-reservado** — atribuir no momento da criação
- [ ] O espelho `intervaloDePeriodicidade` é atualizado **nos dois lados** (backend e frontend)
- [ ] O lookup de default de parcelas é atualizado **nos dois pontos** do `ContratoForm.tsx` (l.52 e l.122)

### F0 — baseline

- [ ] `npx tsc --noEmit` · `npm test` · `npm run docs:audit` · `npm run audit:ui` · `npm run audit:styles` — saídas registradas

### F1 — domínio (backend)

- [ ] `src/modules/contrato/domain/contrato.entity.ts:5` — type `Periodicidade` ganha `"alternada"`
- [ ] `src/modules/contrato/domain/periodicidade.ts:4` — `PERIODICIDADES` ganha `"alternada"` (`isPeriodicidade` deriva daí, não precisa mexer)
- [ ] `src/modules/contrato/domain/services/gerar-parcelas.ts:6-8` — `intervaloDePeriodicidade` retorna `2` para `alternada`
- [ ] `.../CreateContrato/CreateContratoInput.ts:12-14` — enum zod
- [ ] `.../UpdateContrato/UpdateContratoInput.ts` — enum zod
- [ ] `gerar-parcelas.test.ts` — casos de `alternada`: início em cada dia da semana, deslize de domingo, residual da última parcela, e **span de 22-23 dias** (assertar o valor real, não 20)

### F2 — frontend

- [ ] `frontend/src/modules/contrato/services/contrato.service.ts` — type `Periodicidade`
- [ ] `frontend/src/modules/contrato/utils/calcularDataFinal.ts:5-7` — espelho do intervalo
- [ ] **Teste novo** para `calcularDataFinal` com a **mesma matriz** do teste de backend (é o que pega a divergência do espelho)
- [ ] `frontend/src/modules/contrato/schemas/contrato.schema.ts:19` — enum zod
- [ ] `ContratoForm.tsx:114` — `grid-cols-2` → `grid-cols-3` e o array `["diaria","semanal"]` ganha `"alternada"`
- [ ] `ContratoForm.tsx:52` e `:122` — ternário → lookup `{diaria:"20", alternada:"10", semanal:"3"}`
- [ ] `frontend/src/i18n/locales/{pt-BR,en,es}.json` — `contrato.periodicidadeOpcoes.alternada`, com paridade de chaves nos 3
- [ ] Conferir que o badge do `ContratoCard` sai automático (renderiza a chave i18n — não deve precisar de mudança)

### F3 — docs e regras

- [ ] `docs/product/02-BUSINESS-RULES.md` — as 2 BRs novas, cada uma com a nota de extensão/revogação
- [ ] `docs/engineering/02-API.md` + `npm run docs:collection`
- [ ] `docs/product/06-CASOS-DE-USO.md` (UC) e `07-CASOS-DE-USO-API.md` (CT de `POST /api/contratos` com `alternada`)
- [ ] `docs/product/01-DOMAIN.md` — hoje **não menciona periodicidade**; incluir na descrição de Contrato
- [ ] `docs/plans/PLAN-0XX-contrato-periodicidade-alternada.md` + linha em `docs/plans/README.md`
- [ ] `docs/skills/SKILL-009-documentation-sync.md` §3 — linha do espelho `intervaloDePeriodicidade` backend↔frontend
- [ ] `docs/UPDATES.md` · `docs/STATUS.md`

### F4 — verificação

- [ ] `npx tsc --noEmit && npm run build`
- [ ] `npm test` (backend + o teste novo do frontend)
- [ ] `npm run docs:audit` · `npm run smoke:api` · `npm run audit:ui` · `npm run audit:styles`
- [ ] **Manual:** criar contrato `alternada` fechando em cada dia da semana; conferir que a 1ª parcela cai em `dataInicio+2`, que nenhum vencimento cai em domingo, e que a `dataFinal` **exibida no formulário é idêntica à persistida** — é este o teste que pega a divergência do espelho

## Dúvidas em aberto

- [ ] Se depois vier um 4º modelo de intervalo fixo (decendial, quinzenal), vale trocar a enumeração por um campo de intervalo em dias? Generalizaria os quatro, mas tira a validação por enum e abre espaço para entrada absurda (0, 999)
- [ ] Um modelo **mensal** continua fora: quebraria a abstração `intervalo: number` e exigiria decidir "mesmo dia do mês ou +30 dias" e "dia 31 em fevereiro"

## Cards relacionados

- Nenhum. Produto próprio, fora do escopo Sogov.

## Referências

- Plano completo da sessão: `~/.claude/plans/eu-tinha-te-deixado-shiny-hummingbird.md` (Parte 3)
- Plano de origem dos 2 modelos atuais: `docs/plans/PLAN-076-contrato-periodicidade.md`
- BRs relevantes: BR-039 (diária ou semanal) · BR-040 (configurável, sem retroatividade) · BR-040-A (semanal não inicia em domingo) · BR-042 (nunca vence em domingo) · BR-042-A (fórmula da `dataFinal`)
- Código citado: `src/modules/contrato/domain/{contrato.entity,periodicidade}.ts` · `src/modules/contrato/domain/services/gerar-parcelas.ts` · `frontend/src/modules/contrato/utils/calcularDataFinal.ts` · `frontend/src/modules/contrato/components/ContratoForm.tsx` · `src/database.ts:123,444`
- Convenções do vault: [[../../../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] · [[../README|04 Conhecimento]] regra 2
