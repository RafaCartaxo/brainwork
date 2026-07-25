---
tags:
  - qa
  - triagem
sprint: SP15
estagio: a-revisar
---
# 04 — A revisar

Cards que precisam de decisão antes de entrar em validação: revisar MR, definir critérios, investigar descarte, refinar.

---

## Revisar MR (dev entregou)

- [ ] **SGV-7337** — Impossibilidade de alterar serviço de um fluxo de trabalho
    - `Média` · Matheus Godoi · Squad 2 · também em SP16 · 🆕 (22/07)
- [ ] **SGV-6568** — Erro ao solicitar assinatura gera múltiplas assinaturas duplicadas e registros incorretos na timeline
    - `Média` · Washington Junior · API · em análise · PM Paulo Afonso · Squad 1
    - ⚠️ Saiu do impedimento → Revisar MR (22/07)
- [ ] **SGV-5245** — Nome do mês e ano incorretos no filtro de data da Mesa de Trabalho
    - `Média` · Lucas Lacerda · Squad 2
    - ⚠️ Backlog → Revisar MR (22/07)

## Refinar / definir critérios

- [x] **SGV-4873** — Assinaturas em anexos de documentos retificados não são canceladas corretamente
    - `Alta` · Matheus Godoi
    - ⚠️ Mesa de refinamento em andamento (`05 Refinar/SGV-4873.md`): conflito com regra de retificação
    - 🚨 ALERTA (24/07): Notion "Disponível para homologação" mas `fix/4873` NÃO mergeado em `development`. **NÃO TESTAR**.
- [x] **SGV-9036** — Mensagens de erro são exibidas quando é selecionado um signatário para assinatura ✅ 2026-07-17 → refinado, critérios no card (Notion)
    - `Altíssima` · Washington Junior · API · Squad 1
    - Sem card local — "no card" = task do Notion. Pendência de confirmação na fila.
    - ✅ Avançou: Revisar MR → Pronto pra teste em dev (Release, 24/07)
- [x] **SGV-7935** — Evento de emissão de documento não é exibido na timeline ao emitir pela toolbar ✅ 2026-07-24 → card criado em `02 Demandas/DEV/`, [MR !608](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/608) revisado
    - `Altíssima` · Diogo Sobreira · Squad 1 · também em SP16
- [x] **SGV-9633** — Assinatura em fluxo de trabalho não pode ser concluída ✅ 2026-07-23 → master; 🔴 reprovada em DEV (24/07)
    - `Alta` · João Rodrigo · CX · Squad 3
    - 🧭 3820 e 8574 duplicadas, consolidadas aqui. Aguardando nova correção.

## Investigar descarte (Não reproduzido)

- [ ] **SGV-6954** — Tela de posicionamento de assinatura em loading infinito com múltiplos anexos e signatários
    - `Média` · João Marcelo · Sanidade-006 · Squad 3
- [ ] **SGV-6256** — Demora para exibir lista de assinaturas após assinar documentos
    - `Média` · sem dev
- [ ] **SGV-6166** — Falha na exibição e conclusão de assinaturas
    - `Média` · João Rodrigo · PM Paulo Afonso · Squad 3
- [ ] **SGV-5970** — Documento impresso não exibe selo de todas as assinaturas realizadas em paralelo
    - `Média` · Diogo Sobreira · Squad 1
- [ ] **SGV-3786** — Exibição de erro 500 ao solicitar assinatura em documento sigiloso
    - `Média` · João Rodrigo · V2 · Squad 3
    - ⚠️ Notion: Em desenvolvimento → Não reproduzido (22/07)
- [x] **SGV-3413** — Erro ao assinar despacho de desassociação de documentos ✅ 2026-07-20 → descartado, não reproduz mais. Card em `99 Arquivo/`
    - `Média` · João Rodrigo · Squad 3

## A revisar (outros)

- [x] **SGV-8977** — Erro ao tentar editar regras de tramitação direto no organograma ✅ 2026-07-20 → refinado, card em `02 Demandas/DEV/`
    - `Baixa` · Washington Junior · CX · API
    - 🚨 ALERTA (24/07): Notion "Reaberto". Coincide com risco do card (timeout 10s sem teste de volume). Confirmar com Rafael/time.
- [x] **SGV-7829** — Anexos do despacho não carregados ao emitir e assinar como Cidadão ✅ reaberta, tratada no [[02-em-validacao|02 - Em validação]]
    - `Média` · João Marcelo · Squad 3
