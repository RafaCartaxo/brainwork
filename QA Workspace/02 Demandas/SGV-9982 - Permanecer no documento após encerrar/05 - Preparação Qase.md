---
tags: [qa, qase]
tipo: referencia
status: enviado
tipo_card: melhoria
projeto: ""
modulo: "Tramitação — Encerramento de documento"
qase_projeto: SGV
qase_suite_id: 358
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-9982

> [!info]- Navegação QA
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (todos aprovados na validação, incluindo CT-009 e CT-012, corrigidos após defeito) para os campos da API.

> [!success] Status: enviado — 12 casos criados na Qase (24/09/2026)
> Suite **358** ("9982 - Permitir escolher permanecer no documento ou voltar à mesa ao encerrar"), filha de **125** (Melhorias/Funcionalidades). `node sync.js --apply` rodado com sucesso — ids **775 a 786**, gravados de volta em `corrections.json` (idempotente — rodar de novo não duplica) e nesta nota. Conferido por amostragem (`--inspect` em 775 e 786) direto contra a Qase real: campos batendo com o esperado (`severity=4`, `type=7`, `automation=0`, `suite_id=358`, steps corretos). Uma correção pós-envio: as tags `SGV-9982`/`tramitação` tinham ficado de fora do payload original de criação (gap desta nota, não do script) — aplicadas via `PATCH` direto nos 12 casos logo em seguida e conferidas.

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `358` — [9982 - Permitir escolher permanecer no documento ou voltar à mesa ao encerrar](https://app.qase.io/project/SGV?suite=358), filha de `125` (Melhorias/Funcionalidades)
- **Origem:** [[03 - Casos de teste]] (CT-001 a CT-012 — todos aplicáveis, nenhum "Não se aplica")
- **Script/payload:** `sogov-automation-test/scripts/qase-sync-9982-tramitacao/` (`sync.js` + `corrections.json` + `README.md`)

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | mantém o título humano do cenário; CTs de regressão levam o prefixo `[REGRESSÃO]` |
| Descrição + critério de aceite | `description` | nunca deixar vazio |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado — CT-012 tem 3 steps (um por dialog) |
| Pós-condição | `postconditions` | só quando agrega algo além do resultado esperado do último step |
| Tipo, severidade, automação | `type`/`severity`/`automation` | **inteiros reais na API**, não texto — usar só rótulos já confirmados contra a Qase real (ver abaixo). Camada (UI/API/E2E) é só organização do vault, não é campo da Qase |

**Rótulos confirmados e usados nos 12 (nenhum inventado):** `severity: normal` (4), `type: acceptance` (7), `automation: is-not-automated` (0). Não existe um `type` de "regressão" confirmado neste projeto — inspecionei casos `[REGRESSÃO]` já existentes na Qase (suite 321) e eles usam `type=1` (não mapeado no script); por isso os CTs de regressão desta leva (CT-002, CT-010, CT-011) usam o mesmo `acceptance` confirmado, sinalizados pelo prefixo `[REGRESSÃO]` no título em vez de um enum não confirmado.

`priority` e `behavior` ficam de fora do payload por padrão (mesma decisão da sincronização anterior, SGV-9296) — preencher manualmente na Qase depois, se fizer sentido.

Tags da nota: manter somente `qa` e `qase`. Este lote não usa shared steps (CT-003/CT-004/CT-005 têm mecânica parecida, mas resultado esperado específico por tipo de encerramento — decidido manter os 3 casos independentes).

## Casos preparados

> Conteúdo idêntico ao `corrections.json` real (não um exemplo) — nenhum caso foi enviado ainda. Os `Qase ID` ficam em branco até o `--apply`.

### CT-001 — Checkbox desmarcado por padrão sem preferência salva

- **Qase ID:** [775](https://app.qase.io/case/SGV-775)
- **Descrição:** confirma o critério C1/C2 (RF02) da SGV-9982 — o checkbox "Permanecer no documento após encerrar" aparece desmarcado quando o usuário nunca marcou a preferência.
- **Pré-condições:** usuário não possui preferência salva; está em documento com tramitação ativa, prestes a abrir um dos três dialogs de encerramento.
- **Passo 1 — Ação:** abrir qualquer um dos três dialogs de encerramento.
  **Resultado esperado:** o checkbox "Permanecer no documento após encerrar" é exibido desmarcado.
- **Pós-condição:** nenhum dado alterado; dialog aberto aguardando decisão.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-002 — [REGRESSÃO] Confirmar com checkbox desmarcado mantém o redirecionamento atual

- **Qase ID:** [776](https://app.qase.io/case/SGV-776)
- **Descrição:** confirma o critério C3 — sem marcar o checkbox, o usuário continua sendo redirecionado para a mesa de trabalho.
- **Pré-condições:** checkbox desmarcado; documento com tramitação ativa.
- **Passo 1 — Ação:** confirmar o encerramento clicando em "Encerrar" com o checkbox desmarcado.
  **Resultado esperado:** usuário é redirecionado para a mesa de trabalho.
- **Pós-condição:** tramitação encerrada conforme o tipo escolhido; usuário na mesa de trabalho.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-003 — Confirmar marcado no encerramento do documento inteiro permanece no documento

- **Qase ID:** [777](https://app.qase.io/case/SGV-777)
- **Descrição:** confirma os critérios C1 e C4 — marcar o checkbox no dialog "Encerrar tramitação" mantém o usuário no documento.
- **Pré-condições:** usuário com permissão para encerrar a tramitação do documento inteiro; dialog "Encerrar tramitação" aberto.
- **Passo 1 — Ação:** marcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** usuário permanece no documento, recarregado no estado pós-encerramento com as ações indisponíveis já refletidas.
- **Pós-condição:** tramitação do documento encerrada para todos os setores; usuário permanece na tela do documento.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-004 — Confirmar marcado no encerramento de setor permanece no documento

- **Qase ID:** [778](https://app.qase.io/case/SGV-778)
- **Descrição:** confirma os critérios C1 e C4 — marcar o checkbox no dialog "Encerrar tramitação no setor" mantém o usuário no documento.
- **Pré-condições:** usuário com permissão para encerrar a participação do próprio setor; dialog "Encerrar tramitação no setor" aberto.
- **Passo 1 — Ação:** marcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** usuário permanece no documento, recarregado no estado pós-encerramento; participação do setor e colaboradores encerrada.
- **Pós-condição:** participação do setor e colaboradores encerrada; usuário permanece na tela do documento.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-005 — Confirmar marcado no encerramento de participação própria permanece no documento

- **Qase ID:** [779](https://app.qase.io/case/SGV-779)
- **Descrição:** confirma os critérios C1 e C4 — marcar o checkbox no dialog "Encerrar tramitação para mim" mantém o usuário no documento.
- **Pré-condições:** usuário participa do documento; dialog "Encerrar tramitação para mim" aberto.
- **Passo 1 — Ação:** marcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** usuário permanece no documento, recarregado no estado pós-encerramento; suas próprias ações ficam indisponíveis.
- **Pós-condição:** participação do próprio usuário encerrada; usuário permanece na tela do documento.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-006 — Preferência marcada em um tipo de encerramento já reflete nos outros dois

- **Qase ID:** [780](https://app.qase.io/case/SGV-780)
- **Descrição:** confirma o critério C6 — a preferência é única por usuário, não por tipo de encerramento.
- **Pré-condições:** usuário marcou e confirmou o checkbox em um dos três dialogs anteriormente.
- **Passo 1 — Ação:** abrir outro dialog de encerramento (tipo diferente do já confirmado).
  **Resultado esperado:** checkbox já aparece marcado, sem precisar marcar novamente.
- **Pós-condição:** preferência do usuário permanece "permanecer" para qualquer tipo de encerramento.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-007 — Reabrir o dialog reflete o último valor salvo

- **Qase ID:** [781](https://app.qase.io/case/SGV-781)
- **Descrição:** confirma o critério C7 — o checkbox é pré-marcado conforme a última preferência salva.
- **Pré-condições:** usuário tem a preferência "permanecer" salva.
- **Passo 1 — Ação:** abrir novamente qualquer um dos três dialogs de encerramento.
  **Resultado esperado:** checkbox aparece pré-marcado.
- **Pós-condição:** nenhuma alteração até nova confirmação ou cancelamento.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-008 — Desmarcar e confirmar reverte a preferência

- **Qase ID:** [782](https://app.qase.io/case/SGV-782)
- **Descrição:** confirma o critério C8 — desmarcar o checkbox e confirmar reverte a preferência para "voltar à mesa".
- **Pré-condições:** usuário tem a preferência "permanecer" salva; checkbox aparece marcado.
- **Passo 1 — Ação:** desmarcar o checkbox e confirmar clicando em "Encerrar".
  **Resultado esperado:** preferência revertida; usuário redirecionado para a mesa de trabalho.
- **Pós-condição:** próxima abertura de qualquer dialog mostra o checkbox desmarcado.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-009 — Cancelar não grava a preferência nem encerra a tramitação

- **Qase ID:** [783](https://app.qase.io/case/SGV-783)
- **Descrição:** confirma o critério C5 — a preferência só é gravada na confirmação; Cancelar/fechar não altera nada. Defeito [[Defeitos/SGV-11815 - Defeito Preferência De Permanecer É Gravada Ao Cancelar O Encerramento|SGV-11815]] corrigido e aprovado em DEV.
- **Pré-condições:** dialog de encerramento aberto, em qualquer um dos três tipos.
- **Passo 1 — Ação:** alterar o estado do checkbox e clicar em "Cancelar" (ou fechar o dialog).
  **Resultado esperado:** nenhuma preferência gravada; nenhum encerramento ocorre.
- **Pós-condição:** preferência e tramitação permanecem como estavam antes da abertura do dialog.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-010 — [REGRESSÃO] Preferência é por usuário, não por setor

- **Qase ID:** [784](https://app.qase.io/case/SGV-784)
- **Descrição:** confirma o requisito não funcional RNF03 — isolamento da preferência por usuário, mesmo entre usuários do mesmo setor.
- **Pré-condições:** dois usuários do mesmo setor, um com preferência salva e outro sem.
- **Passo 1 — Ação:** cada usuário confirma um encerramento a partir de sua própria preferência.
  **Resultado esperado:** cada usuário é direcionado conforme sua própria preferência, sem interferência do setor.
- **Pós-condição:** preferências individuais preservadas.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-011 — [REGRESSÃO] Preferência sobrevive a logout e a novo dispositivo

- **Qase ID:** [785](https://app.qase.io/case/SGV-785)
- **Descrição:** confirma o requisito não funcional RNF04 — persistência da preferência além da sessão atual.
- **Pré-condições:** usuário tem a preferência "permanecer" salva.
- **Passo 1 — Ação:** fazer logout e login novamente, ou acessar de outro dispositivo.
  **Resultado esperado:** preferência salva é aplicada normalmente.
- **Pós-condição:** comportamento do checkbox consistente com a preferência salva em qualquer sessão/dispositivo.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

### CT-012 — Os três dialogs seguem o modal de alerta com CTAs e copy padronizados

- **Qase ID:** [786](https://app.qase.io/case/SGV-786)
- **Descrição:** confirma o critério C9 — os três dialogs de encerramento usam o formato de alerta (`modal Type=Alert`), CTAs padronizados e a copy exata de cada tipo, incluindo as cores do protótipo Figma. Defeito [[Defeitos/SGV-11816 - Defeito Cores Do Modal De Encerramento Divergem Do Protótipo Figma|SGV-11816]] (cores divergentes do Figma) corrigido e aprovado em DEV.
- **Pré-condições:** usuário tem permissão para abrir qualquer um dos três dialogs de encerramento.
- **Passo 1 — Ação:** abrir o dialog "Encerrar tramitação" (documento inteiro).
  **Resultado esperado:** `modal Type=Alert` com as cores do protótipo Figma, CTA primário "Encerrar", CTA secundário "Cancelar", título "Encerrar tramitação" e corpo com o texto exato definido (incluindo $sigla/$nome-setor).
- **Passo 2 — Ação:** abrir o dialog "Encerrar tramitação no setor".
  **Resultado esperado:** `modal Type=Alert` com as cores do protótipo Figma, CTA primário "Encerrar", CTA secundário "Cancelar", título "Encerrar tramitação no setor" e corpo com o texto exato definido (incluindo $sigla/$nome-setor).
- **Passo 3 — Ação:** abrir o dialog "Encerrar tramitação para mim".
  **Resultado esperado:** `modal Type=Alert` com as cores do protótipo Figma, CTA primário "Encerrar", CTA secundário "Cancelar", título "Encerrar tramitação para mim" e corpo com o texto exato definido.
- **Pós-condição:** nenhuma alteração de estado; validação apenas visual/textual.
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-9982`, `tramitação`

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

## Checklist de envio

- [x] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [x] Projeto e suite confirmados (SGV / 358).
- [x] Campos normalizados e passos separados.
- [x] Tags limitadas ao ID da demanda e ao módulo.
- [x] Campos da API validados (`dry-run` rodado, `severity`/`type`/`automation` conferidos contra rótulos já confirmados na Qase real).
- [x] Envio realizado sem duplicação (`node sync.js --apply`, 24/09/2026 — 12 casos criados, ids 775-786, conferidos por amostragem via `--inspect`).
- [x] IDs da Qase registrados nesta nota.
- [x] Status alterado para `enviado`.
