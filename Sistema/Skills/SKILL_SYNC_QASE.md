---
tags:
  - qa
  - skill
---
# Skill: Sincronizar Casos de Teste com a Qase

Levar CTs **já escritos e refinados** num card do vault até casos de teste criados/atualizados no projeto `SGV` da Qase TestOps — decidindo *quais* CTs sobem, *como* ficam legíveis lá (descrição, pré/pós-condição, shared steps), e aplicando via API com segurança (sem duplicar, sem adivinhar campo). É o handoff downstream dos CTs, em paralelo à automação ([[SKILL_INICIAR_AUTOMACAO]]) — os dois partem do mesmo card validado, mas um vai pro Cypress e o outro pro repositório de casos da Qase.

## Contexto (leia antes — necessário pra qualquer IA/pessoa sem o setup na cabeça)

- **Vault QA (Obsidian)** — onde os CTs vivem: card em `QA Workspace/02 Demandas/<ambiente>/`, seção "Casos de teste"/"Casos de Teste Básicos", formato Dado/Quando/Então ([[SKILL_CASOS_DE_TESTE]]). **Esse formato não muda** por causa da Qase — ele é otimizado pra leitura humana e rastreio de defeito, não precisa espelhar o schema da API.
- **Ferramenta reutilizável** — vive no repositório de automação, não no vault: `sogov-automation-test/scripts/qase-sync-<contexto>/` (`sync.js` + `corrections.json` + `README.md`). Cada sincronização ganha sua própria pasta (nome do contexto, ex. `qase-sync-9296-departamentos`), copiada da **versão mais recente já usada** — hoje `qase-sync-9296-departamentos/sync.js`, não a `qase-sync-1.24-1.25/` antiga (mais simples, sem shared steps nem idempotência real).
- **Autenticação**: `QASE_TESTOPS_API_TOKEN` no `.env` do repo (mesmo token do `cypress-qase-reporter`, ver `docs/integrations/qase.md`). Validar antes de qualquer coisa: `node sync.js --inspect=<id de um case qualquer que já exista>` (só leitura) ou `curl -H "Token: $TOKEN" https://api.qase.io/v1/project/SGV` — token errado/expirado dá `401`.
- **O arquivo "Preparação Qase" — rascunho que vira registro**: um por card sincronizado, em `04 Conhecimento/Tasks/<epic>/<parte>/N - <SGV> - Preparação Qase.md` (mesma pasta e convenção de numeração do [[SKILL_REFINAMENTO]] — **nunca usar o número `3` se existir "Plano de Automação"**, esse slot é reservado; usar o próximo livre). Nasce com `status: rascunho`, todos os campos da Qase já preenchidos (não só Dado/Quando/Então) — Rafael revisa **antes** de qualquer POST/PATCH. Depois do `--apply`, o mesmo arquivo ganha os `id`/`hash` da Qase e vira `status: enviado` — **nunca é descartável**, é o registro definitivo de o que subiu e por quê.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| CTs prontos, pedido explícito de subir pra Qase | "sobe os CTs da SGV-XXXX pra Qase", "prepara os casos pra Qase" |
| Card com CTs marcados N/A que precisam ficar de fora do lote | mesmo gatilho acima, com filtro |

## Pré-requisitos (GATES)

1. **CTs já escritos no card**, no formato Dado/Quando/Então de [[SKILL_CASOS_DE_TESTE]] — a skill não escreve CT novo, só traduz o que já existe.
2. **Suite de destino confirmada** — nunca assumir/criar suite sem perguntar; conferir via `GET /v1/suite/SGV/<id>` (só leitura) se já existe e está vazia ou não.
3. **Token válido** (ver Contexto acima).

## Passo a passo

### 1. Decidir o que sobe (filtro, não renumeração)
Nunca renumerar CT do vault pra "ficar bonito" antes de subir — os CT-NNN são referenciados em Regras de negócio, outros CTs, evidências já nomeadas e defeitos filhos; renumerar quebra tudo isso pra ganho nenhum. **A numeração da Qase é independente**: cada caso ganha um `id` próprio da API, sem relação com CT-001...CT-NNN do vault — o `CT-NNN` só entra no **título** de cada caso, como referência de rastreio.

O filtro é por **aplicabilidade**, não por status de execução: sobe todo CT que **não** está marcado "Não se aplica" (inclui `Sim`, `Não` — reprovado ou já corrigido — e não-executado). CT marcado N/A representa um cenário fora do escopo real da entrega; criar um caso de teste pra ele na Qase testaria comportamento que não existe no produto.

### 2. Identificar shared steps (mecânica repetida entre CTs)
Antes de escrever o rascunho, varrer os CTs candidatos procurando a **mesma mecânica testada em mais de um lugar** (ex.: a mesma regra de busca testada no campo pessoa e no despacho; a mesma regra de accordion testada nos dois componentes). Cada mecânica repetida vira **um shared step**, referenciado pelos CTs que o usam — sem duplicar o texto do passo em cada caso.

### 3. Escrever o rascunho "Preparação Qase"
Um arquivo por card, no template abaixo. Cada CT vira uma seção com todos os campos que a Qase usa:

```markdown
---
tags: [qa, qase]
tipo: referencia
status: rascunho  # rascunho | enviado
suite_id: <id da suite>
---
# Preparação Qase: <Título da demanda>

## Shared steps (mecânicas repetidas entre CTs)

### `<chave-curta>` — <título do shared step>
*(usado em: CT-XXX, CT-YYY)*
1. Ação: ... | Resultado esperado: ...
- Hash na Qase: `<preenchido depois do --apply>`

## Casos

### CT-NNN <título>
- **Descrição:** <CA + contexto da demanda — não deixar em branco>
- **Precondição:** <o Dado do CT>
- **Passos:** <o Quando/Então do CT, ou "usa o shared step `<chave>`">
- **Pós-condição:** <opcional — só quando agregar algo além do resultado esperado do último passo, ex. "registro X persistido no banco">
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado (ajustar se o CT pedir outro rótulo — ver ressalva de ENUMS abaixo)
- **Qase id:** `<preenchido depois do --apply>`
```

Mapeamento de campos, resumido:

| Campo Qase | Vem de |
|---|---|
| `title` | `CT-NNN <título do cabeçalho>` |
| `description` | CA (já anotado no CT) + contexto curto da demanda — nunca deixar vazio |
| `preconditions` | O `Dado` do CT |
| `steps` (ação/resultado esperado) | O `Quando`/`Então` do CT — um step por par; CT com múltiplos `Quando`/`Então` vira múltiplos steps |
| `postconditions` | Só quando o CT implica um estado final que vale registrar além do resultado do último step (nem todo CT precisa) |
| `severity` / `type` / `automation` | Ver ENUMS abaixo — nunca inventar rótulo novo sem confirmar |

Rafael revisa o rascunho antes do próximo passo.

### 4. Gerar o `corrections.json` a partir do rascunho
Tradução mecânica, não interpretação livre — o rascunho já decidiu o conteúdo. Formato:

```json
{
  "project_code": "SGV",
  "suite_id": <id>,
  "shared_steps": [
    { "key": "<chave-curta>", "title": "...", "steps": [ { "action": "...", "data": "", "expected_result": "..." } ] }
  ],
  "updates": [ { "id": <id existente>, "description": "...", "postconditions": "...", "steps": [ { "shared_step_key": "<chave>" } ] } ],
  "delete": [],
  "creates": [
    {
      "title": "CT-NNN ...", "description": "...", "preconditions": "...",
      "severity": "normal", "type": "acceptance", "automation": "is-not-automated", "behavior": "undefined",
      "steps_type": "classic",
      "steps": [ { "action": "...", "data": "", "expected_result": "..." } ]
    }
  ]
}
```

Step com `"shared_step_key": "<chave>"` (em vez de `action`/`data`/`expected_result`) referencia o shared step correspondente — o script resolve pro hash real na hora de montar o payload.

### 5. Rodar — dry-run → lote pequeno/isolado → apply
```bash
node sync.js                    # dry-run: só imprime, não chama a API
node sync.js --apply --only=<id>  # teste isolado de 1 update de baixo risco
node sync.js --apply             # lote completo (shared_steps → updates → deletes → creates, nessa ordem)
```
Depois de cada `--apply`, o script **reescreve o `corrections.json`** com os `id`/`hash` resultantes — é assim que o arquivo vira estado idempotente (ver "Por que a idempotência importa" abaixo). Conferir por amostragem com `node sync.js --inspect=<id>` (só leitura).

### 6. Atualizar o rascunho pro estado final
Copiar os `id`/`hash` gravados no `corrections.json` de volta pro arquivo "Preparação Qase" no vault (`status: enviado`), e linkar esse arquivo no Resumo/Histórico do card de origem. Registrar na daily (`📤` na fila/Atividades, copy do [[../../QA Workspace/01 Daily/README|01 Daily/README]]).

## Por que a idempotência importa
Sem o `id`/`hash` gravado de volta, rodar `--apply` duas vezes por engano **recria caso duplicado** (a API não tem dedup por título). Com o campo gravado, o script pula qualquer `creates`/`shared_steps` que já tenha `id`/`hash` (log de aviso, não erro) — o `corrections.json` vira o estado atual de verdade, não só um log do que foi feito uma vez. **Só os `updates` são seguros de rerodar por natureza** (PATCH sobrescreve, não duplica) — mas mesmo assim, gravar o resultado de volta documenta o estado real.

## Shared Steps — mecânica da API (confirmado contra a doc oficial, 04/09/2026)

- **Criar**: `POST /v1/shared_step/{code}` — body `title` + `steps: [{action, expected_result, data}]` (campos no nível raiz do payload existem mas são *deprecated*, sempre usar `steps`).
- **Listar/checar duplicata antes de criar**: `GET /v1/shared_step/{code}?search=<título>` — a API **não faz dedup automático por título**, o script precisa checar antes.
- **Assimetria real entre escrita e leitura** — não é erro, é como a API funciona: ao **escrever** um step que referencia um shared step (criar/atualizar caso), o campo é **`shared`** = hash do shared step. Ao **ler** (GET) um caso já salvo, a API devolve **`shared_step_hash`**/`shared_step_nested_hash` no lugar. Nomes diferentes pra escrita e leitura.
- **Plano Free**: shared step **de projeto** está incluso (fonte: artigo oficial do Free Plan da Qase — a tabela de pricing comparativa não cita isso e pode parecer pago numa leitura rápida dela; só o nível **workspace/global** é pago).
- **Editar um shared step propaga imediatamente** pra todo caso que o usa — inclusive execuções já feitas com aquela definição. Cuidado ao editar um shared step em uso.
- **`DELETE` via API**: comportamento não documentado (a UI oferece excluir de vez ou converter pra step local antes; não confirmado se a API oferece a mesma escolha) — **não implementar exclusão de shared step até confirmar isso na prática**, tratar como território desconhecido.

## Cuidado com ENUMS (severity/type/automation)
Esses três campos são **inteiros** na API real, mesmo que o export/UI mostrem texto. O script só reconhece os rótulos já confirmados contra um `--inspect` real (`severity: normal`, `type: acceptance`, `automation: is-not-automated`). Se um CT precisar de rótulo diferente (ex. `severity: critical`), **confirmar o valor inteiro real** via `--inspect` num caso existente que já tenha esse rótulo antes de adicionar a entrada no mapa `ENUMS` do script — nunca adivinhar. `priority` e `behavior` ficam de fora do payload por padrão (decisão de longa data: mais simples preencher/confirmar manualmente na Qase do que arriscar mapeamento não confirmado).

## Handoff (pra onde vai depois)

Casos criados/atualizados na Qase, arquivo "Preparação Qase" com `status: enviado` e os ids — pronto pra quem for executar puxar da Qase diretamente. Card do vault segue sendo a fonte de verdade pra qualquer mudança de regra; próxima sincronização (novo lote, ou correção) parte de um novo rascunho no mesmo arquivo ou um novo arquivo, nunca editando a Qase por fora do script.

## Resultado Esperado

Casos na Qase legíveis por quem não conhece o vault (descrição, pré/pós-condição, shared step em vez de passo repetido), sem duplicata em reruns, sem campo adivinhado, e com um registro no vault que sobrevive — o "Preparação Qase" — linkando de volta pro card de origem.
