---
tags: [qa, qase]
tipo: referencia
status: rascunho
tipo_card: "funcionalidade"
projeto: ""
modulo: "integracoes-esic"
qase_projeto: SGV
qase_suite_id: ""
demanda: "[[01 - Demanda]]"
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-10735

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

Esta nota transforma os CTs refinados do vault em casos da Qase. Não cria CT novo: apenas traduz os casos já existentes em `03 - Casos de teste` (só depois de aprovados na validação) para os campos da API.

> [!warning] Pendência
> Os 14 CTs já estão executados e aprovados (06/10/2026) — falta só confirmar `qase_suite_id` antes do envio. Nunca assumir/criar suite sem perguntar (ver [[../../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]], GATE 2).

## Configuração

- **Projeto Qase:** `SGV`
- **Suite Qase:** `<a confirmar>`
- **Origem:** [[03 - Casos de teste]] (CT-001 a CT-014 — todos aplicáveis, nenhum "Não se aplica")

## Casos preparados

> Nenhum caso foi enviado ainda — aguardando confirmação do `qase_suite_id`.

## Checklist de envio

- [ ] Todos os CTs candidatos têm descrição, pré-condições e passos.
- [ ] Projeto e suite confirmados (suite pré-existente ou criada com autorização explícita).
- [ ] Campos normalizados e passos separados.
- [ ] Tags limitadas ao ID da demanda e ao módulo.
- [ ] Campos da API validados (`dry-run` rodado antes do `--apply`).
- [ ] Envio realizado sem duplicação.
- [ ] IDs da Qase registrados nesta nota.
- [ ] Status alterado para `enviado`.
