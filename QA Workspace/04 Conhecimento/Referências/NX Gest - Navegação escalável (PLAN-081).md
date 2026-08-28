---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-08-28
---
# NX Gest - Navegação escalável (PLAN-081)

> [!info] Sobre esta nota
> Revisão do **PLAN-081** (📝 Planejado, não implementado) do repo pessoal `RafaCartaxo/nxgest` — **não é sistema Sogov**. Acervo pesquisável, na regra 2 de [[../README|04 Conhecimento]].
> Notas irmãs: [[NX Gest - Reposicionamento de identidade (PLAN-086)]] · [[NX Gest - Insights e gráficos (PLAN-080)]] · [[NX Gest - Contrato periodicidade alternada (PLAN-085)]].
> **Orquestração:** [[NX Gest - Handoff de execução]].

> [!warning] Numeração
> A **revisão deste plano foi aplicada no repo em 28/08** (organização: 4 correções + corte da sidebar). O `PLAN-081` **já existe** no repo com esse número. No repo o último plano é o **PLAN-085** (alternada, executado). Não pré-reservar número (de PLAN nem de BR).

## Visão geral

- **O quê:** revisão do plano de navegação escalável — tab bar mobile com aba "Mais", sidebar desktop colapsável, registro único `nav.ts`.
- **Por que importa:** é 100% frontend, era pré-requisito declarado do PLAN-080, e carrega uma decisão estrutural de UX (unificar nav mobile/desktop) que contamina toda tela futura se estiver torta.
- **Veredito:** plano **sólido**, premissa correta. 4 correções + 1 corte de escopo.
- **Estado:** revisão fechada em 25/08/2026. Nada implementado.

> [!important] Correção minha, registrada
> Suspeitei que a premissa do plano estivesse velha, porque a `BottomTabBar` já existe (entregue em 07/08 via o briefing Stitch / `PLAN-060`). **Estava errado.** O PLAN-081 é de **18/08**, posterior à entrega, e descreve o estado atual com precisão: tab bar com 5 abas, **sem** aba "Mais", sidebar fixa `w-64` **sem** colapso, e duplicação real de itens entre `AppLayout.tsx` e `BottomTabBar.tsx`.

## Regras de negócio

### O que o plano já acerta (manter)

- **D9 — a sheet "Mais" reusa o `Modal`**, que já é bottom-sheet no mobile. Sem componente novo.
- **D13 — registro resolve *nav*, guard resolve *acesso***. `RequireModule`/`AdminRoute`/`SuperAdminRoute` seguem intactos; não duplica proteção.
- **D11 — `/gastos` continua sem item de nav**, agregado ao Caixa, **documentado no registro para não ressuscitar**. É o tipo de decisão que se perde e volta.
- **D7 — itens do super_admin nunca são ocultados por whitelabel.** Correto: whitelabel é por empresa; super_admin é plataforma.
- **D4 tem precedente de persistência** — `ThemeProvider` já usa localStorage (`nxgest_palette`, `nxgest_mode`).
- A duplicação que o D5 quer matar **é real e verificada**: mudar ícone, rota ou chave i18n hoje exige editar dois arquivos.

### Correção 1 — as fases estão na ordem inversa do risco

O plano faz **Fase 1** = tab bar + "Mais", **Fase 2** = sidebar colapsável, **Fase 3** = registro único (`nav.ts`, D5).

Mas o `nav.ts` é a **correção da causa raiz**. Nessa ordem, a lógica de overflow é escrita na `BottomTabBar` contra as constantes hardcoded e depois movida para o registro — escrever duas vezes. O `nav.ts` é refactor puro, sem mudança de comportamento, testável isolado (`nav.test.ts` já está previsto). **Deve vir primeiro**, e a tab bar consumir ele.

### Correção 2 — a sidebar não é o problema de escala; D4 sai do escopo

O plano justifica o rail com "sidebar fixa `w-64` não escala". Mas **lista vertical escala**: 8 itens a ~40px cabem folgado em qualquer viewport de desktop. O que não escala é a barra **horizontal** do mobile. O rail resolve **largura de conteúdo** — motivação diferente e mais fraca — e é a peça com maior superfície (toggle, persistência, tooltips, colapso de header de seção).

Agrava: `06-UI-PATTERNS.md:439-444` é **normativo** — *"desktop expande informação, nunca muda fluxo"*. Um rail que esconde rótulos **reduz** informação no desktop.

**Decidido:** D4 e a Fase 2 saem do escopo → item de `BACKLOG.md`. Se voltarem, o plano precisa declarar que o motivo é área de conteúdo (não escala de nav) e justificar a exceção ao princípio.

### Correção 3 — `papel: "tenant"` (D12) não fecha com o código

O código tem quatro papéis (`operator | admin | socio | super_admin`) e derivações que **se sobrepõem**: `isTenant = operator || admin || socio` e `isAdminSocio = admin || socio` (`BottomTabBar.tsx:49-51`). Um campo `papel` escalar não expressa isso — um admin é "tenant" **e** "admin" ao mesmo tempo.

**Correção:** `papeis: Role[]` (lista), que casa com o `excluirPapel: Role[]` do próprio D8. Campo escalar aqui gera bug de gating silencioso.

### Correção 4 — D3 invertido: a Rota fica primária, `insights` vai para o "Mais"

O D3 aloca `insights` como aba primária e rebaixa a **Rota** ao overflow. Mas a Rota entrou no nav justamente porque o briefing que originou esta navegação registra: *"Falta o atalho da **Rota** (a ação diária mais importante do operador)"*.

Rebaixá-la para abrir espaço a uma página de gráficos read-only inverte a prioridade de quem usa o produto em campo — e `insights` interessa mais a admin/sócio, que **não têm** Rota (é delegada, `BottomTabBar.tsx:53`).

**Decidido:** Rota permanece primária; `insights` entra no "Mais".

**Consequência boa:** reforça o desacoplamento decidido em [[NX Gest - Insights e gráficos (PLAN-080)]]. Como a Fase 1 do PLAN-080 entrega `/insights` alcançável por URL **sem item de nav**, o PLAN-080 deixa de depender do PLAN-081 para **entregar** — este vira pré-requisito só de **descoberta**.

## Comportamentos observados em teste

### Estado atual verificado

| Papel | Tab bar hoje | Total |
|---|---|---|
| operator | Central · Clientes · Contratos · Caixa · Rota | 5 |
| admin/sócio | Central · Clientes · Contratos · Caixa · Painel Admin (Rota é delegada, sai) | 5 |
| super_admin | Central · Board · Empresas · Leads | 4 |

Desktop: sidebar fixa `w-64`, `hidden lg:flex`, sem colapso. Breakpoint único relevante: `lg` (1024px).

### O cap 5 não existe em código

`BottomTabBar.tsx:57-59` monta `visiveis` e renderiza tudo com `flex-1`. **Com 6 itens nada quebra** — as abas apenas apertam (label `text-[11px]` com `truncate` dentro de `max-w-lg`). O cap é premissa de design herdada do briefing Stitch, não regra implementada.

O plano diz "cap 5 primários" mas **não nomeia o mecanismo**. Especificar: o cap e o `isOverflowRoute` (D10) vivem **no `nav.ts`**, derivados da mesma lista ordenada — se o corte ficar na `BottomTabBar` e a rota de overflow for calculada em outro lugar, os dois discordam sobre o que é primário.

**Consequência:** o PLAN-081 é **trava de qualidade, não bloqueador**.

### Telas órfãs de navegação (confirmado)

`Cobranças`, `Atendidos` e `Gastos` não têm item de nav — só widget na Central. A `Rota` **saiu** dessa lista no PLAN-060. O D11 mantém `/gastos` fora de propósito.

### Travas de governança de UI

- **`role="tab"` fora do componente `Tabs` quebra o `audit:ui`** (`audit-ui.mjs:80`). A `BottomTabBar` acerta hoje com `role="navigation"` + `NavLink` (l.63). O `Tabs` é para conteúdo dentro de tela, **não** navegação estrutural.
- **`pb-safe` obrigatório** em elemento fixo na base (`index.css:342-344`, home bar do iPhone). Já presente em `BottomTabBar.tsx:65`.
- **"Scroll horizontal" é anti-pattern declarado** (`06-UI-PATTERNS.md:468`) — o que **justifica** a aba de overflow: rolar a barra lateralmente está proibido por doc.
- **`Modal` sem `title` quebra o gate** (`audit-ui.mjs:90`). A sheet "Mais" precisa de `title`.
- **`test/setup.ts` não tem mock de `matchMedia`** — teste que exercite breakpoint precisa adicioná-lo (hoje só stuba canvas).
- **Rota nova exige entrada no `05-MAPEAMENTO-TELAS.md`** ou o `docs:audit` quebra.

---

## Checklist de execução

> [!important] Como usar
> Ordem: **F0 → F3**. Os vetos valem em toda a execução. A Fase 1 é refactor puro — o teste dela é que **nada muda na tela**.

### Vetos permanentes

- [ ] **Nenhum `role="tab"`** fora do componente `Tabs` — a aba "Mais" usa `NavLink`/`button` com `role="navigation"` no container
- [ ] **Não reintroduzir o rail** da sidebar (D4/Fase 2 estão fora de escopo — está no BACKLOG)
- [ ] **Não rebaixar a Rota** do conjunto primário
- [ ] O cap e o `isOverflowRoute` moram **no `nav.ts`**, derivados da mesma lista ordenada — nunca em dois lugares
- [ ] `papeis` é **lista** (`Role[]`), nunca campo escalar
- [ ] `/gastos` **continua** sem item de nav
- [ ] Itens do super_admin (Board/Empresas/Leads) **nunca** ocultados por whitelabel
- [ ] O registro **não** duplica os guards de acesso (`RequireModule`/`AdminRoute`/`SuperAdminRoute` intactos)
- [ ] `pb-safe` preservado na `BottomTabBar`
- [ ] `Modal` da sheet "Mais" **com `title`**

### F0 — baseline

- [ ] `npm test` · `npm run audit:ui` · `npm run audit:styles` · `npm run docs:audit` · `npx tsc --noEmit` — saídas registradas
- [ ] Print/anotação da tab bar atual **nos 3 papéis** (operator, admin/sócio, super_admin) — é a referência de "nada mudou" da Fase 1

### F1 — registro único `nav.ts` (refactor puro, zero mudança visível)

- [ ] `frontend/src/shared/navigation/nav.ts` — registro com `papeis: Role[]`, `modulo?`, `excluirPapel?: Role[]`, ordem, cap de primários e `isOverflowRoute`
- [ ] `frontend/src/shared/navigation/nav.test.ts` — gating por módulo, gating por papel, `excluirPapel` (Rota para admin/sócio), cálculo de primários vs overflow, cap
- [ ] `AppLayout.tsx` — `useNavItems`/`useAdminNavItems` passam a derivar do registro
- [ ] `BottomTabBar.tsx` — constantes `ABAS`/`ADMIN_ABAS`/`SUPER_ABAS` removidas; consome o registro
- [ ] Ícones e chaves i18n declarados **uma vez** (hoje importados nos dois arquivos)
- [ ] **Conferir contra o baseline F0:** os 3 papéis mostram exatamente os mesmos itens, na mesma ordem
- [ ] Gates: `npm test` · `audit:ui` · `audit:styles` · `tsc`

### F2 — aba "Mais" (overflow)

- [ ] Cap aplicado no consumo, a partir da lista ordenada do registro
- [ ] Aba "Mais" na `BottomTabBar`, abrindo `Modal` (bottom-sheet no mobile) **com `title`**
- [ ] Estado ativo: "Mais" acende quando a rota atual está no conjunto de overflow (`isOverflowRoute`)
- [ ] `insights` entra no overflow quando existir (não como primário)
- [ ] i18n `nav.mais` nos 3 idiomas, com paridade de chaves
- [ ] Acessibilidade: foco gerenciado, `Escape` fecha, foco volta para a aba "Mais"
- [ ] Módulo desligado → item some da lista **sem deixar buraco** na barra
- [ ] `docs/engineering/design/04-UI-COMPONENTS.md` e `UI-COVERAGE.md` atualizados
- [ ] UCs de navegação em `docs/product/06-CASOS-DE-USO.md`

### F3 — verificação

- [ ] `npm test` · `npm run audit:ui` · `npm run audit:styles` · `npm run docs:audit` · `npx tsc --noEmit && npm run build`
- [ ] **Manual, por papel** (operator · admin/sócio · super_admin): itens corretos; módulo off sem buraco; rota de overflow deixa "Mais" aceso; `Escape` fecha a sheet e devolve o foco
- [ ] Se algum teste exercitar breakpoint, `matchMedia` mockado em `frontend/src/test/setup.ts`

## Dúvidas em aberto

- [ ] A sidebar colapsável volta algum dia? Se sim, o gatilho é área de conteúdo apertada no desktop — não número de itens de nav. Precisaria justificar a exceção ao `06-UI-PATTERNS`
- [ ] `Cobranças` e `Atendidos` seguem sem item de nav (só widget da Central). É intencional ou dívida? O D11 documenta só o caso de `/gastos`
- [ ] Com o cap vivendo no `nav.ts`, vale um teste que falhe se o número de primários passar de 5 — travando a premissa de design em código

## Cards relacionados

- Nenhum. Produto próprio, fora do escopo Sogov.

## Referências

- Plano completo da sessão: `~/.claude/plans/eu-tinha-te-deixado-shiny-hummingbird.md` (Parte 4)
- Plano revisado: `docs/plans/PLAN-081-navegacao-escalavel.md` (📝 Planejado)
- Origem da navegação atual: `docs/plans/Stitch-Nav-AppFirst-NXGest.md` (✅ Concluído 07/08/2026, PLAN-060)
- Normativo de UI: `docs/foundation/ADR-005-UI-Governance.md` · `docs/engineering/design/06-UI-PATTERNS.md` · `UI-COVERAGE.md`
- Código citado: `frontend/src/shared/layout/{AppLayout,BottomTabBar,UserMenu}.tsx` · `frontend/src/shared/theme/ThemeProvider.tsx` · `frontend/src/shared/auth/RequireModule.tsx` · `scripts/audit-ui.mjs` · `frontend/src/index.css`
- Convenções do vault: [[../../../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] · [[../README|04 Conhecimento]] regra 2
