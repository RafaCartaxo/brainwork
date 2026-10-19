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
> `qase_suite_id` ainda não confirmado — nunca assumir/criar suite sem perguntar (ver `Sistema/Skills/SKILL_SYNC_QASE.md`, GATE 2). Verificar suites existentes em `https://app.qase.io/project/SGV` antes do envio real. **Nenhum CT foi redigido ainda — esta preparação só avança depois de `03 - Casos de teste.md` e `04 - Validação dev.md` estarem concluídos.**

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `<a confirmar>`
- **Origem:** [[03 - Casos de teste]] (20 CTs, a redigir — nenhum ainda)
- **Script/payload:** `Sistema/Scripts/qase-sync/sgv-12272/` (a criar, copiando a versão mais recente já usada — ver `Sistema/Skills/SKILL_SYNC_QASE.md`)

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | mantém o título humano do cenário |
| Descrição + critério de aceite | `description` | nunca deixar vazio |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado |
| Pós-condição | `postconditions` | só quando agrega algo além do resultado esperado do último step |
| Tipo, severidade, automação | `type`/`severity`/`automation` | inteiros reais na API — usar só rótulos já confirmados contra a Qase real |

**Nunca inventar rótulo de enum.** Rótulos já confirmados em outras sincronizações: `severity: normal` (4), `type: acceptance` (7), `automation: is-not-automated` (0) — reconfirmar contra a Qase real antes de aplicar, conforme o gate do skill.

`priority` e `behavior` ficam de fora do payload por padrão.

## Casos preparados

> Nenhum caso foi redigido nem enviado ainda — esta nota está preparada para quando os 20 CTs existirem e forem aprovados em `04 - Validação dev.md`.

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
