---
tags:
  - qa
  - qase
tipo: referencia
status: rascunho
tipo_card: casos-de-teste
projeto: "SGV-12272"
modulo: ""
qase_projeto: SGV
qase_suite_id: ""
demanda: "[[01 - Demanda]]"
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-12272

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (só depois de aprovados na validação) para os campos da API.

> [!warning] Pendência
> `qase_suite_id` ainda não confirmado — nunca assumir/criar suite sem perguntar (ver `Sistema/Skills/SKILL_SYNC_QASE.md`, GATE 2). Verificar suites existentes em `https://app.qase.io/project/SGV` antes do envio real. **Os 20 CTs já estão redigidos em `03 - Casos de teste.md`; a validação em `04 - Validação dev.md` ainda está pendente (execução real do Rafael) — esta preparação só avança depois dela concluída.**

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `<a confirmar>`
- **Origem:** [[03 - Casos de teste]] (20 CTs redigidos — CT-001 a CT-020; validação em `04 - Validação dev.md` ainda pendente)
- **Script/payload:** processo real descrito em `Sistema/Skills/SKILL_SYNC_QASE.md` — pasta `Sistema/Scripts/qase-sync/sgv-12272/` no vault (`sync.js` + `corrections.json` + `README.md`), a criar copiando a versão mais recente já usada. Não vive no repo de automação.

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | mantém o título humano do cenário; CTs de regressão levam o prefixo `[REGRESSÃO]` |
| Descrição + critério de aceite | `description` | nunca deixar vazio |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado |
| Pós-condição | `postconditions` | só quando agrega algo além do resultado esperado do último step |
| Tipo, severidade, automação | `type`/`severity`/`automation` | **inteiros reais na API**, não texto — usar só rótulos já confirmados contra a Qase real (`--inspect` num caso existente). Camada (UI/API/E2E) é só organização do vault, não é campo da Qase |

**Nunca inventar rótulo de enum.** Rótulos já confirmados em outras sincronizações: `severity: normal` (4), `type: acceptance` (7), `automation: is-not-automated` (0) — reconfirmar contra a Qase real antes de aplicar, conforme o gate do skill. Não existe `type` de "regressão" confirmado neste projeto — CTs de regressão usam `acceptance` mesmo, sinalizados pelo prefixo `[REGRESSÃO]` no título.

`priority` e `behavior` ficam de fora do payload por padrão.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: ID da demanda + módulo (ex. `SGV-12272`, `<módulo>`) — não criar uma tag por CT.

## Casos preparados

> Nenhum caso foi enviado ainda. Os `Qase ID` ficam em branco até o `--apply`. Os 20 CTs já estão redigidos (03), mas os blocos preenchidos abaixo só serão gerados depois da validação em `04 - Validação dev.md` (um por CT aprovado) — o bloco a seguir é o **modelo** a replicar, não um CT real.

### Modelo — CT-0NN — <título do cenário>

- **Qase ID:** `preencher após o envio`
- **Descrição:** <resumo do objetivo + critério coberto>
- **Pré-condições:** <estado necessário antes do teste>
- **Passo 1 — Ação:** <ação>
  **Resultado esperado:** <resultado>
- **Pós-condição:** <estado após o teste, se agregar algo além do resultado>
- **severity:** normal · **type:** acceptance · **automation:** is-not-automated
- **Tags Qase:** `SGV-12272`, `<módulo>`

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

## Checklist de envio

- [ ] Os 20 CTs estão redigidos em `03 - Casos de teste.md`.
- [ ] Os 20 CTs foram aprovados em `04 - Validação dev.md`.
- [ ] Projeto e suite confirmados (suite pré-existente ou criada com autorização explícita).
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados (`dry-run` rodado antes do `--apply`).
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
