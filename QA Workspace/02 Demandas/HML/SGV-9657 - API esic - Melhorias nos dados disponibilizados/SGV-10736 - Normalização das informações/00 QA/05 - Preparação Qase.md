---
tags:
  - qa
  - qase
tipo: referencia
status: rascunho
tipo_card: melhoria
projeto: ""
modulo: integracoes-esic
qase_projeto: SGV
qase_suite_id: ""
demanda: "[[01 - Demanda]]"
casos_origem: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]"
validacao_origem: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]"
---
# Preparação Qase — SGV-10736

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (só depois de aprovados na validação) para os campos da API.

> [!warning] Pendência
> `qase_suite_id` ainda não confirmado — nunca assumir/criar suite sem perguntar (ver [[../../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]], GATE 2). Verificar suites existentes em `https://app.qase.io/project/SGV` antes do envio real. Envio só deve acontecer **depois** dos 14 CTs aprovados em `04 - Validação dev`.

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `<a confirmar>`
- **Origem:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]] (CT-001 a CT-014 — todos aplicáveis, nenhum "Não se aplica")
- **Script/payload:** processo real descrito em [[../../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]] — pasta `Sistema/Scripts/qase-sync/<contexto>/` no vault.

## Mapeamento dos campos

| Vault | Qase | Regra |
|---|---|---|
| Título do CT | `title` | mantém o título humano do cenário |
| Descrição + critério de aceite | `description` | nunca deixar vazio |
| Pré-condições | `preconditions` | copiar sem misturar com os passos |
| Dado/Quando/Então | `steps` | separar cada ação do resultado esperado |
| Pós-condição | `postconditions` | só quando agrega algo além do resultado esperado do último step |
| Tipo, severidade, automação | `type`/`severity`/`automation` | inteiros reais na API — usar só rótulos já confirmados contra a Qase real. Camada (API) é só organização do vault, não é campo da Qase |

**Nunca inventar rótulo de enum.** Rótulos confirmados até 24/09/2026: `severity: normal` (4), `type: acceptance` (7), `automation: is-not-automated` (0).

`priority` e `behavior` ficam de fora do payload por padrão — preencher manualmente na Qase depois, se fizer sentido.

Tags da nota: manter somente `qa` e `qase`. Tags enviadas ao Qase: `SGV-10736`, `integracoes-esic`.

## Casos preparados

> Nenhum caso foi enviado ainda — validação ainda em andamento. Os `Qase ID` ficam em branco até o `--apply`, que só deve rodar após os 14 CTs aprovados.

## Checklist de envio

- [ ] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados (suite pré-existente ou criada com autorização explícita).
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados (`dry-run` rodado antes do `--apply`).
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
