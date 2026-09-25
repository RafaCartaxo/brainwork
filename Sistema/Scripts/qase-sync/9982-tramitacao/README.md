# Sync Qase — SGV-9982 (Permitir escolher permanecer no documento ou voltar à mesa ao encerrar)

Sobe os 12 casos de teste aplicáveis da melhoria SGV-9982 pro projeto `SGV` na Qase,
suite **358** ("9982 - Permitir escolher permanecer no documento ou voltar à mesa ao
encerrar"), criada em 24/09/2026 como filha da suite **125** (Melhorias/Funcionalidades)
— mesmo padrão das outras 5 suítes já existentes ali (220, 353, 354, 355, 357).

Fonte dos casos: vault Obsidian (BrainWork), `QA Workspace/04 Conhecimento/Tasks/
SGV-9982 - Permanecer no documento após encerrar/03 - Casos de teste.md`. Rascunho
legível com os campos já traduzidos pra Qase: `05 - Preparação Qase.md`, no mesmo
pacote. (Pacote movido de `02 Demandas/` pra `04 Conhecimento/Tasks/` em 24/09/2026
— convenção nativa do vault pra material de conhecimento/task.)

## Status atual

**Rodada 1 (24/09/2026)**: os 12 CTs do card (todos aplicáveis — nenhum marcado "Não
se aplica") foram aprovados na validação em DEV, incluindo os 2 que carregaram
defeito numa rodada anterior:
- CT-009 — defeito SGV-11815 (preferência gravada mesmo ao cancelar), corrigido e
  retestado.
- CT-012 — defeito SGV-11816 (cores do modal divergiam do Figma), corrigido e
  retestado.

Diferente da SGV-9296, `description`/`preconditions`/`postconditions` foram
preenchidos **desde a rodada 1** (evitando a necessidade de uma rodada 2 de
`updates` só pra enriquecer os casos).

**Sem shared steps**: CT-003/CT-004/CT-005 têm mecânica parecida (marcar o checkbox
e confirmar "Encerrar"), mas o resultado esperado específico difere por tipo de
encerramento (documento inteiro/setor/participação própria) — decidido com o Rafael
manter como 3 casos independentes em vez de generalizar num shared step.

## Como preencher um próximo lote

`suite_id` não vai dentro de cada entrada — já está fixo em `corrections.json` (358),
o script aplica pra todos os `creates` do lote.

**Rótulos de severity/type/automation**: `sync.js` só reconhece os rótulos já
mapeados em `ENUMS` (`severity: normal`, `type: acceptance`,
`automation: is-not-automated`). Confirmado por inspeção ao vivo (24/09/2026, suite
321) que casos com título `[REGRESSÃO]` no projeto usam `type=1` e não um enum
"regressão" dedicado — por isso os 3 CTs de regressão desta leva (CT-002, CT-010,
CT-011) usam `type: acceptance` (o único confirmado) com o prefixo `[REGRESSÃO]` no
título, em vez de arriscar um enum não confirmado.

## Como rodar

```bash
# 1. Revisar o que seria feito (não chama a API) — já rodado e conferido em 24/09/2026
node sync.js

# 2. Teste isolado antes do lote inteiro (opcional — este lote é só de creates,
#    --only filtra updates por id, não se aplica diretamente aqui)

# 3. Aplicar o lote inteiro, só depois do Rafael revisar o dry-run e o rascunho no vault
node sync.js --apply
```

Precisa de `QASE_TESTOPS_API_TOKEN` no `.env` do repo. Token já testado e
autenticando (24/09/2026, `GET /v1/project/SGV` → 200; suite 358 criada via
`POST /v1/suite/SGV` no mesmo dia).

## Depois de rodar

Conferir na Qase (https://app.qase.io/project/SGV?suite=358) se os 12 casos batem
com o vault, registrar os ids de volta em `05 - Preparação Qase.md` (`status:
enviado`), e registrar na daily (`📤`).

## Status atual (concluído, 24/09/2026)

`--apply` rodado com sucesso — 12 casos criados, ids **775 a 786**, gravados de volta
em `corrections.json` (idempotente). Conferido por amostragem (`--inspect=775` e
`--inspect=786`) direto contra a Qase real: `severity=4`, `type=7`, `automation=0`,
`suite_id=358`, steps corretos (CT-012 com os 3 steps, um por dialog).

**Correção pós-envio**: as tags `SGV-9982`/`tramitação` ficaram de fora do payload
original de `creates` (gap deste rascunho — o `sync.js` não monta `tags` a partir de
`creates`, só os campos padrão). Aplicadas via `PATCH /v1/case/SGV/{id}` direto nos
12 casos, fora do `sync.js` (não é um fluxo de update/idempotência coberto pelo
script hoje) — conferido via `--inspect=775` que a tag `SGV-9982` foi aplicada.
Se um próximo lote precisar de tags no `creates`, vale ensinar o `sync.js` a montar
o campo `tags` a partir da entrada, em vez de repetir o `PATCH` manual.
