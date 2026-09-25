# Sync Qase — TR 1.24-1.25 (Autenticação e ciclo de vida do usuário)

Corrige os 39 casos do projeto `SGV` na Qase (suite id 4) para bater com o conteúdo
validado no vault (fonte única desde 31/08):
`Obsidian/BrainWork/QA Workspace/06 Estudos/Termo de Referência 1.24-1.25/1.24-1.25 - Casos de Teste (Dado-Quando-Então).md`

## Por que via API, e não CSV

O import de CSV da Qase não faz merge por título — reimportar sobre casos já
existentes duplica, não atualiza (ver nota `Qase.md` do vault). Como os 39 casos já
existem lá, a correção precisa ser update in-place via API REST.

## O que o script faz

- `corrections.json` — payload com o estado final desejado de cada caso: **25**
  `updates` (preenche os 21 que estavam vazios, corrige o card `id 5` corrompido,
  corrige `id 24`/`id 30` sobre acesso de leitura em Licença/Férias — os outros 12
  casos que só precisavam de `priority` saíram da lista, ver abaixo), 2 `deprecate`
  (ids 13 e 33, órfãos já absorvidos no vault — marcados como `deprecated`, **não
  deletados**), e 1 `creates` (card novo, equivalente ao CT-017 — desbloqueio manual
  pelo servidor — que nunca existiu na Qase).
- `sync.js` — lê `corrections.json` e chama a API da Qase.

## `priority` foi deixado de fora, de propósito

Decisão do Rafael em 31/08: `priority` não é enviado em nenhum caso (nem updates,
nem o create do CT-017) — fica como está na Qase (`undefined`), pra ser preenchido
manualmente lá depois. Motivo: nenhum dos 39 casos originais tinha prioridade
definida, então não havia como confirmar empiricamente o mapeamento 1/2/3
(low/medium/high) antes de escrever. Como consequência, os 12 casos que só
precisavam desse campo (ids 4, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17) saíram de
`corrections.json["updates"]` — não sobrou nada pra corrigir neles.

## Comportamento da API — importante

O endpoint usado (`PATCH /v1/case/{code}/{id}`) faz update **parcial de verdade**:
campo que o `corrections.json` não envia não é tocado (confirmado na doc oficial:
*"only fields present in the payload are validated; required fields not included
are not enforced"*).

## Campos numéricos — severity/type/automation/status

Confirmado em 31/08 via `node sync.js --inspect=1` contra a Qase real: esses campos
são **inteiros** na API (não texto — o export usa texto, a API não). O
`corrections.json` continua com rótulos legíveis (`"deprecated"` etc.); `sync.js`
traduz pro inteiro certo através dos mapas `ENUMS` no topo do arquivo antes de cada
chamada.

O que já foi confirmado contra um case real (id 1): `severity:4`, `type:7`,
`automation:0`, `status:0` — batendo com os rótulos `normal`/`acceptance`/
`is-not-automated`/`actual` do export. O campo `behavior` teve um valor (`1`) que
não bateu com o padrão esperado pro rótulo `undefined` do export — hipótese mais
provável é que o export tenha um bug de rotulagem nesse campo específico (o case 1
é um cenário de sucesso, e `behavior:1` bate com "positive" no enum padrão da Qase).
De qualquer forma, **nunca enviamos esse campo** — não vale o risco.

**Ainda em aberto:** `status: deprecated` (2) — só o valor `0` (actual) foi visto
num case real (id 1). Os ids 13/33 (`deprecate`) são o primeiro teste real desse
valor. Por isso `sync.js` recusa rodar o **lote completo** (`--apply` sem `--only`)
até isso ser testado isoladamente — ver passo 2 abaixo. Um `--apply --only=13`
isolado passa direto (é o próprio teste).

## Como rodar

```bash
# 1. Revisar o que seria feito (não chama a API)
node sync.js

# 2. Teste real e isolado do status:deprecated — id 13 (órfão, baixo risco)
node sync.js --apply --only=13
node sync.js --inspect=13   # confirma que voltou status:2
# e dá uma olhada na tela da Qase: o card 13 deve aparecer como depreciado/arquivado,
# com o título prefixado "[ABSORVIDO — NÃO EXECUTAR]".
# se bater, marcar STATUS_DEPRECATED_CONFIRMED = true no topo de sync.js.

# 3. Só depois de confirmar, aplicar o lote inteiro
node sync.js --apply
```

Precisa de `QASE_TESTOPS_API_TOKEN` no `.env` do repo (mesmo token já usado pelo
`cypress-qase-reporter` — ver `docs/integrations/qase.md`). Sem esse `.env`,
`node sync.js` (dry-run) roda normalmente; `--inspect` e `--apply` exigem o token
(`--inspect` só lê, não escreve nada).

## Depois de rodar

Conferir no projeto SGV (https://app.qase.io/project/SGV) se os 39 casos batem
com o vault, e revisar manualmente os 2 cards marcados `[ABSORVIDO — NÃO EXECUTAR]`
(ids 13 e 33) — decidir se ficam só depreciados ou se algum dia são de fato excluídos.
