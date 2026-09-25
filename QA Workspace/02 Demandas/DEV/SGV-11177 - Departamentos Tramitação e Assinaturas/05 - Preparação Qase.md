---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: "funcionalidade"
projeto: ""
modulo: servicos-pj
qase_projeto: SGV
qase_suite_id: ""
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-11177

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (só depois de aprovados na validação) para os campos da API.

> [!warning] Pendência  
> `qase_suite_id` ainda não confirmado — nunca assumir/criar suite sem perguntar (ver [[../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]], GATE 2). Verificar suites existentes em `https://app.qase.io/project/SGV` antes do envio real.

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `<a confirmar>`
- **Origem:** [[03 - Casos de teste]] (CT-001 a CT-031 — todos aplicáveis, nenhum "Não se aplica")
- **Script/payload:** processo real descrito em [[../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]] — pasta `sogov-automation-test/scripts/qase-sync-<contexto>/` (`sync.js` + `corrections.json` + `README.md`), copiada da versão mais recente já usada.

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | mantém o título humano do cenário |
| Descrição + critério de aceite | `description` | nunca deixar vazio |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado — um CT com múltiplos pares vira múltiplos steps |
| Pós-condição | `postconditions` | só quando agrega algo além do resultado esperado do último step |
| Tipo, severidade, automação | `type`/`severity`/`automation` | **inteiros reais na API**, não texto — usar só rótulos já confirmados contra a Qase real (`--inspect` num caso existente). Camada (UI/API/E2E) é só organização do vault, não é campo da Qase |

**Nunca inventar rótulo de enum.** Rótulos confirmados até 24/09/2026: `severity: normal` (4), `type: acceptance` (7), `automation: is-not-automated` (0).

`priority` e `behavior` ficam de fora do payload por padrão — preencher manualmente na Qase depois, se fizer sentido.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: ID da demanda + módulo (`SGV-11177`, `servicos-pj`) — não criar uma tag por CT.

## Casos preparados

> Nenhum caso foi enviado ainda. Os `Qase ID` ficam em branco até o `--apply`.

> **Regra:** critérios, evidências, esforço e resultado da execução continuam no vault ou no Test Run; não duplicar esses dados no caso da Qase.

## Checklist de envio

- [ ] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados (suite pré-existente ou criada com autorização explícita).
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados (`dry-run` rodado antes do `--apply`).
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
