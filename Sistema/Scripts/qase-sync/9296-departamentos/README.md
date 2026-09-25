# Sync Qase — SGV-9296 (Departamentos — Cadastrar Contato/Departamento sem CPF/CNPJ)

Sobe os casos de teste da epic SGV-9296 pro projeto `SGV` na Qase, suite **220**
("9296 - Possibilidade de Cadastrar Contato/Departamento sem CPF/CNPJ") — hoje
vazia (0 casos), sem sub-suites.

Fonte dos casos: vault do Obsidian, `QA Workspace/02 Demandas/DEV/`:
- `11083 - Funcionalidade Departamentos Para Cidadao PJ.md` (Parte 1)
- `11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos.md` (Parte 2)
- Defeitos filhos (`11312`, `11313`, `11273`, `11319`, em `02 Demandas/Concluídas/`), se entrarem no lote.

## Status atual

**Rodada 1 (04/09/2026)**: os 21 CTs aplicáveis da SGV-11184 (dos 28 do card, 7 excluídos
por estarem `Não se aplica`: CT-002a, CT-002b, CT-006, CT-010, CT-012, CT-014, CT-022)
foram criados na suite 220 — **ids 443 a 463**.

**Rodada 2 (04/09/2026) — enriquecimento**: os 21 casos vieram "crus" na rodada 1
(sem `description`/`postconditions`, sem shared steps pra mecânica repetida). Corrigido
via `--apply` de `updates` (não recriação):
- `description` + `postconditions` preenchidos nos 21 casos.
- 2 shared steps criados no projeto (`busca-3-caracteres`, `accordion-click-area`) e
  referenciados nos 4 casos que compartilham essa mecânica (ids 444/449 e 445/451).
- `sync.js` ganhou `createSharedStep`/`listSharedSteps`, resolução de
  `shared_step_key` → hash, e **idempotência real**: cada `create`/shared step
  aplicado grava seu `id`/`hash` de volta em `corrections.json` (persistido em disco
  ao fim do `--apply`), e uma entrada que já tem `id`/`hash` é **pulada, não
  recriada** — seguro rodar `--apply` de novo sem duplicar.
- Tudo verificado ao vivo contra a Qase real (`--inspect` nos casos alterados,
  `cases_count` dos shared steps), não só dry-run.

`corrections.json` deixou de ser só um log histórico do que foi enviado — agora é
**estado idempotente de verdade** (guarda `id`/`hash` reais e pode ser reaplicado com
segurança). Essa pasta é a **versão de referência** pra copiar em próximas
sincronizações — `qase-sync-1.24-1.25/` ficou congelada, sem esse fix, com aviso
no próprio `_readme` do seu `corrections.json` avisando pra não rodar `--apply` de
novo sem revisar.

Processo formalizado em `SKILL_SYNC_QASE` (Sistema/Skills/, vault) — mapeamento de
campos, mecânica de shared steps (atenção: campo de escrita `shared` × campo de
leitura `shared_step_hash`/`shared_step_nested_hash`, nomes diferentes na API) e o
próprio mecanismo de idempotência descritos lá.

Casos que carregam defeito aberto/corrigido, sinalizados com `_note` em cada entrada:
- CT-002c, CT-008a — defeito SGV-11312 (corrigido, aprovado em DEV)
- CT-012a — defeito SGV-11338 **ainda aberto**
- CT-012b — formalizado a partir do defeito SGV-11319 (corrigido, aprovado em DEV)

**Ainda não subiu**: os 33 CTs da SGV-11083 (Parte 1, nenhum executado ainda) e os
CTs próprios dos cards de defeito (`11312`/`11313`/`11319`/`11338`/`11273`, em
`Casos de Teste Básicos` de cada card) — decidir se entram num próximo lote.

## Como preencher um próximo lote

Cada entrada de `creates` segue o mesmo formato usado na sincronização anterior
(TR 1.24-1.25, ver `../qase-sync-1.24-1.25/corrections.json` como referência):

```json
{
  "title": "CT-001 Departamento só aparece com Pessoa Jurídica habilitada no campo",
  "description": "Dado que um campo pessoa está configurado pra aceitar Pessoa Jurídica...",
  "preconditions": "",
  "severity": "normal",
  "type": "acceptance",
  "automation": "is-not-automated",
  "steps": [
    { "action": "...", "data": "", "expected_result": "..." }
  ]
}
```

`suite_id` não vai dentro de cada entrada — já está fixo em `corrections.json` (220),
o script aplica pra todos os `creates` do lote.

**Rótulos de severity/type/automation**: `sync.js` só reconhece os rótulos já
mapeados em `ENUMS` (`severity: normal`, `type: acceptance`,
`automation: is-not-automated`) — confirmados contra a Qase real na sincronização
anterior. Se algum CT precisar de rótulo diferente (ex. `severity: critical`), tem
que **confirmar o valor inteiro real** (via `--inspect` num case existente que já
tenha esse rótulo) antes de adicionar a entrada no mapa — nunca adivinhar.

`priority` e `behavior` ficam de fora do payload por padrão, mesma decisão da
sincronização anterior — reavaliar só se o Rafael pedir explicitamente.

## Como rodar

```bash
# 1. Revisar o que seria feito (não chama a API)
node sync.js

# 2. Teste isolado de 1 caso de baixo risco antes do lote inteiro
node sync.js --apply --only=<id-fictício-não-se-aplica-a-creates>
# (nota: --only filtra updates por id; creates sempre rodam juntos hoje — se o lote
# de creates for grande, vale considerar dividir corrections.json em lotes menores
# antes do --apply, em vez de confiar só no --only)

# 3. Só depois de confirmar, aplicar o lote inteiro
node sync.js --apply
```

Precisa de `QASE_TESTOPS_API_TOKEN` no `.env` do repo (mesmo token do
`cypress-qase-reporter` — ver `docs/integrations/qase.md`). Token já testado e
autenticando (03/09/2026, `GET /v1/project/SGV` → 200).

## Depois de rodar

Conferir na Qase (https://app.qase.io/project/SGV?suite=220) se os casos batem com
o vault, e cruzar de volta pro card de origem (`11083`/`11184`) se fizer sentido
registrar o ID da Qase no card.
