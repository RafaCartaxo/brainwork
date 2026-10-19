---
prioridade: media
origem: "validação"
pontos_alocados: ""
---

# SGV-12272 — Casos de teste e publicação da Onda 1 de sanidade do TR

**Ticket de origem:** SGV-12272 (origem: Onda 1 aprovada na SGV-12200)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Origem (SGV-12200):** [[../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|Proposta da Onda 1 (20 cenários aprovados)]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** redigir os 20 CTs em `03 - Casos de teste.md` — nada foi redigido nem publicado ainda.

---

## Problema / contexto

A Onda 1 de 20 cenários candidatos de sanidade foi levantada e aprovada na SGV-12200 (19/10/2026) — mas a aprovação é só da seleção e do escopo: nenhum CT formal foi redigido, nenhum caso foi sincronizado na Qase, e o catálogo funcional correspondente ainda não existe no Notion (a subpágina "Cenários de sanidade" do hub segue placeholder).

## Objetivo

Transformar os 20 cenários já aprovados em artefatos formais e reutilizáveis: CTs em Gherkin, sincronizados na Qase após validação, e um catálogo funcional publicado na subpágina "Cenários de sanidade" do hub Notion, com rastreabilidade direta ao Termo de Referência.

### Entrega desta capacidade

- 20 CTs formais em Gherkin, um por cenário aprovado, com rastreabilidade ao TR.
- Plano de teste mapeando os 20 CTs aos cenários de origem.
- Validação dev dos 20 CTs pelo fluxo existente.
- Preparação e sincronização dos CTs aprovados na Qase.
- Catálogo funcional publicado na subpágina "Cenários de sanidade" do hub Notion, sem metadados internos de QA nem links inacessíveis.

---

## Decisões de produto

- A seleção e o escopo dos 20 cenários já estão aprovados (SGV-12200, 19/10/2026) — não são reabertos nem redecididos aqui.

---

## Escopo

- Produzir os 20 CTs em Gherkin, reutilizáveis, a partir dos 20 cenários aprovados.
- Plano de teste com rastreabilidade ao TR para cada CT.
- Validação dev dos CTs pelo fluxo já existente no vault.
- Sincronizar os CTs aprovados na Qase, usando o mecanismo vigente (`Sistema/Scripts/qase-sync/`), só depois da validação.
- Publicar na subpágina "Cenários de sanidade" do hub Notion o catálogo funcional com os 20 cenários e referências diretas ao TR.

---

## Fora de escopo

- Implementação ou execução de automação.
- Decisão de arquitetura do preset/seed/.env (passo 11 da SGV-12082).
- Propor a Onda 2 de cenários.
- Alterar os documentos canônicos (Transcrição, Modelo-alvo, Matriz) já publicados.
- Reabrir ou redecidir a seleção dos 20 cenários já aprovada na SGV-12200.

---

## Critérios de aceite

- C1. Os 20 CTs estão redigidos em Gherkin, cada um rastreável a um item exato do TR. ^c1
- C2. O plano de teste cobre os 20 CTs com rastreabilidade TR registrada. ^c2
- C3. Os 20 CTs passaram pelo fluxo de validação dev existente. ^c3
- C4. Os CTs aprovados estão sincronizados na Qase pelo mecanismo vigente. ^c4
- C5. O catálogo funcional dos 20 cenários está publicado na subpágina "Cenários de sanidade", sem metadados internos de QA nem links inacessíveis. ^c5

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Suite Qase ainda não confirmada — não assumir/criar suite sem autorização explícita (ver `Sistema/Skills/SKILL_SYNC_QASE.md`, GATE 2).
