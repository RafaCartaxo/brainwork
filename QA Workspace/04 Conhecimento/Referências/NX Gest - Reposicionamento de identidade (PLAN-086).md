---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-08-28
---
# NX Gest - Reposicionamento de identidade (PLAN-086)

> [!info] Sobre esta nota
> Plano **fechado e aprovado**, ainda **não executado** (mantido como **pendência** — será o **PLAN-086 do repo** quando entrar; o número real é atribuído na criação). Trata do repo pessoal `RafaCartaxo/nxgest` — **não é sistema Sogov**, então não vale como conhecimento de validação: está aqui como acervo pesquisável, no espírito da regra 2 de [[../README|04 Conhecimento]] (material de fora, resumido e linkado).
> Template: [[../../../Sistema/Templates/Conhecimento|Conhecimento.md]].
> Notas irmãs: [[NX Gest - Insights e gráficos (PLAN-080)]] · [[NX Gest - Navegação escalável (PLAN-081)]] · [[NX Gest - Contrato periodicidade alternada (PLAN-085)]].
> **Orquestração:** [[NX Gest - Handoff de execução]].

> [!warning] Numeração provisória
> O rótulo `PLAN-085` era provisório e **colidiu** com o plano de periodicidade alternada (que entrou como **PLAN-085**, executado em 27/08). Este plano de identidade será **PLAN-086** no repo; o plano de convite (anexo) será **PLAN-087**. Números atribuídos na criação, sem pré-reserva (de PLAN nem de BR): foi o erro corrigido em 25/08.

## Visão geral

- **O quê:** alinhar a documentação canônica do NX Gest ao que o produto já é — de "sistema de gestão de cobranças em campo" para **plataforma modular de gestão operacional**, tendo *crédito em campo* como primeiro vertical.
- **Natureza:** organização. Uma passada, escopo medido, docs-only (+3 strings user-facing). **Não é** rebrand, refatoração, migração de infra, nem antecipação de fase do roadmap.
- **Estado:** plano aprovado em 21/08/2026; **pendência registrada (28/08)** — será PLAN-086 no repo quando for executar. Repo clonado em `~/Documentos/Desenvolvimento/nxgestao`.
- **Origem:** o plano completo foi gerado em sessão de IA e vive em `~/.claude/plans/eu-tinha-te-deixado-shiny-hummingbird.md` (caminho volátil — esta nota é a cópia durável).

## Regras de negócio

### Intuito e teste de pronto

Fazer a doc canônica declarar o que o sistema já é, e travar para não driftar de novo. Três entregas, em ordem de importância:

1. **Acabar com a contradição interna** — o repo tem hoje duas verdades oficiais.
2. **Instalar a trava que a mudança exige** — subir para "plataforma" esvaziaria o "o que este sistema não é", que é a única defesa concreta da doc para recusar feature.
3. **Prevenir a reincidência** — linha nova na matriz de propagação da SKILL-009.

> [!important] Teste de pronto (falsificável)
> Um dev ou agente novo que leia o `00-NORTH-STAR.md` deve chegar à **mesma conclusão** sobre o que o produto é que alguém que leia o `ADR-006`, o roadmap e a tela de login. Hoje não chega. Se depois do plano ainda não chegar, o plano falhou.

### O diagnóstico: a doc está atrasada, não errada de origem

A doc de fundação é de 27/06/2026 (NORTH-STAR v1.0) e nunca foi revisada. O resto do repo já andou:

| Sinal | Onde | O que já diz |
|---|---|---|
| Roadmap oficial | `docs/product/04-ROADMAP.md:603-607` (§5.10) | "um app, vários negócios (cobrança hoje, agendamentos/vendas amanhã)" · F4 = `tipo_negocio` |
| ADR de arquitetura | `docs/foundation/ADR-006-Module-Manifest.md:15` | "para o verdadeiro whitelabel (vários negócios plugáveis)…" |
| Tagline **em produção** | `frontend/src/i18n/locales/*.json:426` (`auth.tagline`, login) | "Gestão centralizada para o seu negócio" |
| 4 briefings | `Lovable-{NXGest,Admin,Avatar,Anexos}-NXGest.md` | 'NX Gest ("Nexus Gestão") — plataforma de gestão multi-negócio (whitelabel)' |
| Capacidades | `docs/plans/PLAN-059-*.md:68` | "capacidades já são desenhadas independentes de `tipo_negocio`" |
| Identidade visual | `Logo.tsx:128` · `favicon.ts:75` | "hub central (o Nexus)" |
| ⟶ Doc de fundação | `docs/foundation/00-NORTH-STAR.md:13` | "sistema de gestão de cobranças em campo" |

**Segundo desalinhamento:** "cobrança" é a *atividade do operador*, não o *tipo de produto*. O modelo de dados é de **crédito próprio** — `contratos` com `valorBase` + `percentualJuros` + `valorFinal` + `periodicidade` (diária/semanal), `parcelas` geradas na contratação, `caixa_config` por operador, `fechamentos_semanais`, BR-098 ("lucro realizado = `valorFinal − valorBase`"). É **microcrédito popular com recebimento em rota**, e o `01-DOMAIN.md:25` já usa o termo certo: "contratos de crediário".

### Desenho adotado: 3 níveis conceituais, 2 de prosa, 1 fonte executável

- **Nível 0 — Plataforma (NX Gest):** whitelabel modular multi-tenant. Escopo por **capacidades**, não por domínio.
- **Nível 1 — Vertical ("Crédito em campo"):** primeiro negócio. Herda o escopo e os "não é" de **domínio** e as BR-001..106.
- **Nível 2 — Módulo:** já existe e **não é prosa** — fonte é o Module Manifest (`src/modules/admin/domain/modules.ts` + espelho frontend), validado por `npm run audit:modules`.

Não é positioning vago porque o nível 1 é **enumerável**: `{clientes, contratos, cobrancas, rota, atendidos}`, com `caixa`/`gastos` genéricos e `central`/`auth`/`admin` como plataforma. Verificável por máquina. Os dois níveis já existem no código — o ADR só lhes dá nome.

### As três travas

1. **Critérios de admissão de vertical** (falsificáveis um a um): caber no manifest com tudo declarado · preservar isolamento `empresaId`/`userId` · rastreabilidade de toda movimentação com valor · UCs/CTs em `06`/`07` + linha em `08` · não exigir novo motor de persistência nem novo mecanismo de autorização · entregar os 3 idiomas.
2. **Regra de fronteira** (protege contra creep *dentro* do vertical, que a lista de "não é" não cobre): toda demanda mapeia para módulo existente ou justifica módulo novo. O que não mapeia é item de `BACKLOG.md`.
3. **Domicílio de BR:** arquivo único, numeração global contínua. **Dividir `02-BUSINESS-RULES.md` por nível é proibido** (rename ⇒ link quebrado ⇒ `audit:links`).

### Camada `tipo_negocio`: adiada = não antecipar o F4

Motivo técnico, não YAGNI genérico: **os 7 módulos não formam partição por negócio.** `clientes`, `caixa` (`dependsOn: []`) e `gastos` são genéricos — etiquetá-los como "crédito em campo" seria errado em **3 de 7**, e o `audit:modules` passaria a defender uma taxonomia falsa.

Gatilhos para promover o F4 a execução (**A, B ou C disparam sozinhos**):

- **A — Semântico:** dois negócios precisam do mesmo conceito com regra incompatível (colisão de `id`/`labelKey`/`dados`).
- **B — Configuração:** `DEFAULT_MODULOS` deixa de ter resposta única (tenant com default disjunto de outro). Sintoma: `PATCH /modulos` de desativação em massa logo após criar a empresa.
- **C — UX/escala:** `ALL_MODULES` passa de 12 entradas (hoje 7; o `insights` do PLAN-080 leva a 8).
- **D — Contexto (necessário, insuficiente):** 2º negócio com tenant comprometido **e** ≥3 módulos próprios não reaproveitáveis. Sozinho, D só autoriza módulos novos.

### Nenhuma BR nova

(1) Falha o escopo do próprio `02-BUSINESS-RULES.md` — "a plataforma é modular" não governa entidade, nenhum request a viola. (2) Falha o checklist SKILL-009 §4.4 ("toda BR tem ao menos um UC/CT?") — seria a primeira BR sem CT e, sendo BR imutável, dívida permanente. (3) BR-034 não se aplica: não há código de negócio novo.

> [!warning] Correção de 25/08 — não pré-reservar número de BR
> A versão anterior desta nota reservava o `BR-107` para a camada `tipo_negocio`. **Errado:** reservar número sem escrever a regra colide com a primeira BR nova que aparecer — e apareceu, no [[NX Gest - Contrato periodicidade alternada (PLAN-085)|PLAN-085]], que precisa de duas. Texto correto: a camada `tipo_negocio` **receberá um BR numerado no momento em que for escrita**, sem pré-reserva. Vale para números de PLAN também (ver nota de numeração provisória no topo).

### "Finanças pessoais" / "evolução pessoal" ficam fora da Visão

Não por conservadorismo — **é incompatível com o schema**: todo o isolamento pendura em `usuarios.empresaId` (BR-105/106) e finanças pessoais é B2C sem empresa. Escrever na Visão canônica criaria compromisso que a arquitetura não honra hoje, trocando um drift resolvido por um novo. Vai para o ADR-007 §"Escopos futuros não comprometidos" (com o custo declarado: exigiria ADR próprio sobre tenancy de pessoa física) + `BACKLOG.md`.

## Comportamentos observados em teste

### Baseline dos gates (medido no clone, não presumido)

```
audit:links   → 0 erro(s), 5 warn(s), 196 arquivos     ← CI passa (grep "0 erro(s)")
docs:audit    → Nenhuma divergência encontrada.         ← CI passa (grep "Nenhuma divergência")
                72 rotas ↔ 72 endpoints ↔ 72 UCs ↔ 72 requests · 28 rotas front ↔ 28 telas
audit:modules → manifest coerente (7 módulos, 13 widgets, 8 capacidades)
```

Baseline **verde** — qualquer quebra seria introduzida pelo trabalho. Os 5 warns são órfãos antigos, sem relação, e warn não quebra o gate.

**Risco de âncora: nulo (medido).** Existe **1** link com âncora em todo o repo: `docs/engineering/02-API.md:1483` → `](#módulo-admin-atualizado)`, interno a arquivo não tocado. Logo os headers dos docs de identidade são livres — mas a recomendação é não renomear os H1 "O que este sistema é / não é" e entrar com os níveis como `##` (diff aditivo).

**Headers congelados:** `# Módulo Admin (atualizado)` em `02-API.md` · todo `## BR-NNN` · headers `# GET|POST /rota` e tabelas de `05-MAPEAMENTO-TELAS.md` (parseados por `audit-docs.mjs`).

### Escopo provado

`docs/` tem **194 arquivos .md**; **10** contêm "cobranças em campo". Varredura com vocabulário alternativo ("crediário", "sistema de cobrança", "este sistema é") não achou nada novo além de `01-DOMAIN.md` — falso positivo, vocabulário legítimo.

**Verificados limpos:** `docs/templates/` (nenhum template embute a descrição, logo não se propaga para doc novo) · `.opencode/agents/` · `.github/` · `docs/skills/` · `docs/qa/02`–`09` · `docs/engineering/**` · topo do `04-ROADMAP` e do `STATUS.md`.

Superfície final: **16 arquivos**, 7 docs de identidade + 3 user-facing + 3 artefatos novos + anti-drift + rastreio + registro.

### Divergências de nome (`NX Gest` × `Nexus Gestão` × `nxgestao`)

| Eixo | Achado | Ação |
|---|---|---|
| **1. slug** | `nxgestao` tem ~60 ocorrências, quase todas infra: `/opt/nxgestao`, `nxgestao_data`/`_pgdata`, `nxgestao_net`, staging DuckDNS, `~/.config/nxgestao/` | **Nada.** PLAN-084:23-25 já fixou `nxgest` como canônico e proíbe renomear infra (migração com risco de perda de volume) |
| **2. marca** | "Nexus Gestão" aparece 6×, sempre glosa entre parênteses e **sempre em doc histórico**; nunca em produto | Fica registrada como **leitura oficial** no ADR-007, via tabela canônica de nomes. Nenhuma superfície muda |
| **3. string comercial** | `locales/*.json:851` (`lead.queroConhecerSubtitle`) diz "negócio **de cobranças**" / "**collection** business" / "negocio **de cobranzas**" — no formulário "Quero conhecer", contradizendo a `auth.tagline` da tela vizinha | Corrigir nos 3 idiomas + o artigo feminino ("a NX Gest" → "o NX Gest") |
| **4. descrições** | 3 concorrentes: a corrente (foundation) e 2 históricas (briefings Lovable/Stitch) | Históricos **não se reescrevem** (política PLAN-084) — são o rastro que prova que a intenção de plataforma é antiga |
| **5. terminologia** | O roadmap §5.10 F4 já batizou o conceito de `tipo_negocio`; "vertical" seria sinônimo concorrente | `tipo_negocio` = conceito de código; "vertical" = rótulo de doc. ADR-007 amarra os dois |

> [!warning] Artigo gramatical
> Canônico é **"o NX Gest"** (masculino, 11 ocorrências vs 2). Uma das 2 femininas era falso positivo: `templates.ts:28`, "acceder **a** NX Gest" — preposição espanhola.

### Legibilidade para o próximo agente (dois furos corrigidos)

1. **A investigação vive fora do repo.** O plano em `~/.claude/plans/` é invisível para um agente trabalhando no repo — tudo apurado evaporaria. Correção: o `PLAN-086` **no repo** carrega uma seção "Baseline e fatos apurados". Mesma lógica para o PLAN-087.
2. **Não existe caminho de leitura para "o que é este produto?"** A tabela "comece por aqui" do `AGENTS.md` tem 7 linhas e nenhuma responde a pergunta; a mais próxima aponta uma **pasta**. Correção: linha nova formulada como pergunta, com 3 saltos — `00-NORTH-STAR` (o que somos) → `ADR-007` (o que aceita entrar) → `08-UC-MODULOS` (como plugar).

### Coerência com convenções do repo (auditado)

| Convenção | Verificação |
|---|---|
| ADR é pareado com PLAN | ADR-005↔PLAN-043/044 · ADR-006↔PLAN-045 → o par ADR-007↔PLAN-086 segue o padrão |
| ADR pode ser de governança, não só de stack | ADR-005 = "por que o redesign deixou débito + guardrails anti-drift" — mesma forma do ADR-007 |
| Versionamento usa incremento **menor** | nenhum doc jamais foi a 2.0 (1.0→1.1→1.4→1.9). Corrigido: NORTH-STAR →1.1, PROJECT →1.2, PRD →1.1 |
| Histórico não se reescreve | PLAN-084; `plans/README.md:103-107` |

## Anexo — incidente do link de convite (PLAN-087)

Incidente real: operador recebeu link antigo de convite, clicou, mensagem incompreensível, **travou as duas pessoas**.

**Causa raiz.** `ConviteRepository.create()` (`convite.repository.impl.ts:31-35`) invalida o convite anterior ao reenviar (`PENDENTE → EXPIRADO`) — invariante N2 do PLAN-075, e está **correta**. O problema é a leitura: `AtivarContaUseCase.ts` tem **6 caminhos de falha colapsados em 2 erros**.

| Situação | Linha | Erro | Código |
|---|---|---|---|
| Token inexistente | l.20 | `TokenInvalidoError` | `TOKEN_INVALID` |
| Revogado **ou já usado** | l.21 | `TokenInvalidoError` | `TOKEN_INVALID` |
| **Link substituído por reenvio** | l.30 | `TokenInvalidoError` | `TOKEN_INVALID` |
| Usuário inexistente | l.40 | `TokenInvalidoError` | `TOKEN_INVALID` |
| E-mail ≠ `emailAlvo` | l.43 | `TokenInvalidoError` | `TOKEN_INVALID` |
| Vencimento real (7 dias) | l.29/36 | `TokenExpiradoError` | `TOKEN_EXPIRED` |

As quatro situações mais prováveis produzem a **mesma** mensagem: `auth.error.ts:47`, "Token inválido ou já utilizado."

> [!tip] O achado que muda o custo: não falta copy, falta fiação
> `locales/*.json:457-464` tem **8 chaves nos 3 idiomas**. Só `conviteExpirado`/`Detail` são usadas (em `AtivarPage.tsx`). **6 são código morto** — `conviteRevogado`, `conviteJaUsado`, `conviteEmailNaoConfere` e seus `Detail` têm **zero** referências. Alguém já escreveu a mensagem didática para exatamente esses casos e ela nunca chega à tela, porque `AtivarPage.tsx:32` só ramifica em `TOKEN_EXPIRED`.

Débitos adjacentes: **PLAN-065 AC-07** pedia "erro + 'reenviar convite'" e a tela é um `ErrorBanner` sem ação de saída (critério não cumprido em plano concluído); e o e-mail de convite é o **único** dos 4 templates sem prazo concreto — `reset` diz "30 minutos", `verificarEmail` "24 horas", `convite` diz "validade limitada" quando o TTL real é **7 dias** (`auth-token.service.ts:5`).

**Divisão decidida (revisada em 28/08).** A copy preventiva do e-mail (string pura, 3 idiomas, zero backend: prazo real de 7 dias + "use sempre o último convite") e todo o resto (códigos de erro distintos, ramificação no `AtivarPage`, ativação das 6 chaves órfãs, par novo "Convite substituído", ação de saída da AC-07, BR-109, UC/CT) foram **executados no PLAN-087 (28/08)**. Este plano de identidade fica com a doc canônica + as 3 strings + ADR-007, **sem** o e-mail de convite (já entregue).

---

## Checklist de execução

> [!important] Como usar
> Ordem obrigatória: **F0 → F7**. Os vetos valem em toda a execução. O baseline (F0) já foi medido e está na seção "Baseline dos gates" acima — a comparação final (F7) tem que dar idêntico.

### Vetos permanentes (conferir antes de commitar)

- [ ] `git diff --name-status` tem **somente `M` e `A`** — nenhum `R` (rename) nem `D` (delete). Rename de `.md` quebra o `audit:links`
- [ ] Nenhuma ocorrência de `nxgestao` foi renomeada (infra: `/opt/nxgestao`, volumes, rede Docker, staging DuckDNS, `~/.config/nxgestao/`)
- [ ] `docs/plans/Lovable-*.md` e `Stitch-*.md` **intocados** (histórico, política do PLAN-084)
- [ ] `src/modules/admin/domain/modules.ts` e o espelho frontend **intocados** — `audit:modules` idêntico ao baseline
- [ ] `docs/product/02-BUSINESS-RULES.md` intocado; **não** foi dividido por nível
- [ ] Nenhuma BR nova criada por este plano (e **nenhum número de BR pré-reservado** — ver correção de 25/08)
- [ ] Nenhuma chave de i18n além de `lead.queroConhecerSubtitle`; `auth.tagline` intacta
- [ ] Headers `# O que este sistema é` / `# O que este sistema não é` **não** renomeados (níveis entram como `##` dentro deles)
- [ ] "Finanças pessoais" / "evolução pessoal" **não** entraram na Visão canônica

### F0 — baseline

- [ ] `npm run audit:links` → `0 erro(s)` (esperado: `0 erro(s), 5 warn(s), 196 arquivos`)
- [ ] `npm run docs:audit` → `Nenhuma divergência encontrada.`
- [ ] `npm run audit:modules` → `manifest coerente`
- [ ] `npm run audit:ui` · `npm run audit:styles` · `npm test` — saídas registradas

### F1 — decisão (ADR-007)

- [ ] `docs/foundation/ADR-007-Identidade-Plataforma.md` criado, no formato do ADR-006 (Status/Versão/Data/Relacionados · Contexto · Decisão · Consequências · Referências)
- [ ] Contém a frase "3 níveis conceituais, 2 de prosa, 1 fonte executável"
- [ ] Contém a **tabela canônica de nomes** (marca, leitura, design system, artigo, slug, domínios, infra legada)
- [ ] Contém os **6 critérios de admissão** de vertical
- [ ] Contém a **regra de fronteira** (demanda mapeia para módulo existente ou justifica módulo novo)
- [ ] Contém a amarração `tipo_negocio` (código, roadmap F4) × "vertical" (rótulo de doc)
- [ ] Contém os **gatilhos A/B/C/D** para reabrir a camada de tipo de negócio
- [ ] Contém §"Escopos futuros não comprometidos" com o custo de tenancy de pessoa física declarado
- [ ] Diz que a camada `tipo_negocio` receberá um BR **numerado quando for escrita** — sem pré-reservar número
- [ ] Registrado em `docs/foundation/README.md` (tabela + ordem de leitura)
- [ ] Registrado em `docs/decisions/ADR-INDEX.md`
- [ ] Registrado em `docs/INDEX.md` §Foundation — **e ADR-005/ADR-006 adicionados** (hoje a lista para no ADR-004)

### F2 — canônicos

- [ ] `00-NORTH-STAR.md`: Objetivo · Missão · Visão · "é" em 2 níveis · "não é" em 2 níveis + Regra de fronteira · Regra de Ouro (original preservada palavra por palavra) · versão **1.0 → 1.1** + data
- [ ] `00-PROJECT.md`: Objetivo · Visão do Produto · Público-Alvo · Escopo → ponteiro ao manifest · Fora do Escopo em 2 níveis · Critérios de Sucesso · versão **1.1 → 1.2** + data
- [ ] `03-PRD.md`: Objetivo · Público-Alvo · **bullets duplicados removidos (l.33-35)** · versão **1.0 → 1.1** + data
- [ ] Nenhuma versão foi para 2.0 (o repo nunca usou; padrão é incremento menor)

### F3 — secundários

- [ ] `README.md:3` · `docs/README.md:3` · `docs/qa/01-VISAO-GERAL.md:9` + linha `| Produto |` (l.13)
- [ ] `AGENTS.md:7` (stack/PostgreSQL/PLAN-070 preservados na mesma linha)
- [ ] **Linha nova na tabela "Documentação — comece por aqui" do `AGENTS.md`** — caminho de leitura em 3 saltos: NORTH-STAR → ADR-007 → 08-UC-MODULOS

### F4 — módulos/doc

- [ ] Nota "Escopo e verticais" em `docs/product/08-UC-MODULOS.md`, acima de "Como validar um novo negócio", com link ao ADR-007

### F5 — user-facing

- [ ] `templates.ts:56-58` — `rodape[*].marca` nos 3 idiomas
- [x] `templates.ts:26-28` — `convite[*].seguro` nos 3 idiomas (prazo de 7 dias + aviso de que reenvio invalida o anterior) — **feito no PLAN-087 (28/08)**, saiu deste plano
- [ ] Assuntos, corpos, botões e cores dos e-mails **intocados**
- [ ] `frontend/public/manifest.webmanifest:5` — só `description`
- [ ] `locales/{pt-BR,en,es}.json:851` — só `lead.queroConhecerSubtitle` (sai "de cobranças"; pt-BR passa a "o NX Gest")
- [ ] `npx tsc --noEmit` · `npm run build` · `node scripts/check-dist.mjs` · `npm test` (`mailers.test.ts`)
- [ ] Render manual dos 3 e-mails conferido

### F6 — anti-drift e rastreio

- [ ] Linha nova na matriz de propagação da `docs/skills/SKILL-009-documentation-sync.md` §3 (**o entregável que impede a reincidência**)
- [ ] `docs/plans/PLAN-071-email-deliverability.md:69` — anotação de **uma linha** de que o rodapé foi atualizado pelo PLAN-086. Plano **não** reescrito
- [ ] `docs/plans/PLAN-087-mensagens-falha-convite.md` criado como 📝 Planejado, com a investigação do incidente embutida
- [ ] `PLAN-086` e `PLAN-087` registrados em `docs/plans/README.md`
- [ ] `PLAN-086` contém a seção "Baseline e fatos apurados" (os fatos ficam no repo, não só na sessão)

### F7 — registro e fechamento

- [ ] `docs/UPDATES.md` com a entrega
- [ ] `docs/STATUS.md` atualizado
- [ ] Status do `PLAN-086` atualizado
- [ ] **Re-rodar os 6 gates e comparar com F0** — `audit:links` `0 erro(s)`, `docs:audit` `Nenhuma divergência`, `audit:modules` idêntico
- [ ] Leitura corrida do `00-NORTH-STAR.md` conferindo que os dois níveis não se contradizem
- [ ] **Teste de pronto:** um leitor do NORTH-STAR chega à mesma conclusão de quem lê o ADR-006 + roadmap + tela de login

## Dúvidas em aberto

- [ ] Onde clonar o repo, nome da branch (sugestão `docs/reposicionamento-plataforma`), e se fica commit local ou PR (`gh` não instalado na máquina)
- [ ] Contagens estagnadas do `04-ROADMAP` §Estado Atual (diz 18 telas / 15 shared components; `docs:audit` mede 28 telas) — dívida pré-existente, fora do escopo do PLAN-086, registrar no `BACKLOG.md`
- [ ] PLAN-071 está `⏳ Em execução` e a l.69 especifica o rodapé de e-mail que o PLAN-086 muda — a anotação de rastreio resolve, mas o PLAN-071 também documenta cor primária `#0520ae` enquanto o código usa `#3571eb`: conferir se foi mudança legítima de tema

## Cards relacionados

- Nenhum. Produto próprio, fora do escopo Sogov.

## Referências

- Plano completo da sessão: `~/.claude/plans/eu-tinha-te-deixado-shiny-hummingbird.md`
- Repo: `https://github.com/RafaCartaxo/nxgest` · produção `nxgest.com.br` · staging `nxgestao.duckdns.org`
- Docs do repo citadas: `docs/foundation/00-NORTH-STAR.md` · `docs/foundation/ADR-006-Module-Manifest.md` · `docs/product/{00-PROJECT,03-PRD,04-ROADMAP,08-UC-MODULOS}.md` · `docs/plans/{PLAN-065,PLAN-071,PLAN-075,PLAN-084}.md` · `docs/skills/SKILL-009-documentation-sync.md`
- Código citado: `src/modules/admin/domain/modules.ts` · `src/modules/auth/application/use-cases/AtivarConta/AtivarContaUseCase.ts` · `src/shared/email/templates.ts` · `frontend/src/i18n/locales/*.json`
- Convenções do vault seguidas: [[../../../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] (regra de data resolvida do ambiente; commit por arquivo com identidade fixada) · [[../README|04 Conhecimento]] regra 2 (importar ≠ copiar tudo)
