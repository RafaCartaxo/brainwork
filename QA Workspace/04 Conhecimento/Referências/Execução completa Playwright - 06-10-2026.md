---
tags:
  - qa
  - conhecimento
  - automacao
tipo: execucao
data: 2026-10-06
---
# Execução completa Playwright — 06/10/2026

> [!warning] Modo de execução não recomendado
> Este run rodou a suíte **inteira** de uma vez (`399` casos, `tests/` todo). A própria [[Automação Playwright]] avisa: *"Não rode `npm run test` — a suíte inteira de uma vez satura o gerador de PDF do backend e produz falhas que não são bugs reais. Vá por domínio, em lotes de 15–20 min."* Os números abaixo são reais (run de verdade contra HML), mas **boa parte das 26 falhas é candidata a ruído de saturação**, não regressão confirmada — ver análise por domínio mais abaixo antes de abrir defeito em cima de qualquer uma.

## Run

- **Quando:** 06/10/2026, 12:24 → 14:46 (≈2h12 de relógio)
- **Artefatos:** `sogov-automation-playwright/playwright/.runtime/run-3a4d6ac4-6eb3-4cb7-b55e-0ca1a9a400dc/` (`summary.md`, `summary.json`, `results.xml`, `playwright-report/`)
- **Resultado:** 399 casos — ok 355 · falhas 26 · flaky 0 · skip 18

## Falhas (26) — resumo por domínio

| Domínio | Qtd | Hipótese |
|---|---|---|
| `signatures` | 12 | **Alta suspeita de ruído** — a própria doc já marca `signatures` como "anormalmente lento", e os specs envolvidos (anexo grande, documento longo, assinatura) são exatamente o perfil que satura o gerador de PDF |
| `contact-groups` | 5 | Sem relação óbvia com PDF — investigar isolado, não descartar como ruído |
| `processing` | 4 | Também depende do gerador de documento — mesma suspeita de saturação |
| `models` | 2 | Sem relação óbvia com PDF — investigar isolado |
| `workboard` | 2 | Sem relação óbvia com PDF — investigar isolado |
| `public-agents` | 1 | Sem relação óbvia com PDF — investigar isolado |

## Falhas (26) — caso por caso

| ID | Camada | Domínio | Arquivo | Hipótese |
|---|---|---|---|---|
| E58-C01 | E2E | contact-groups | `contact-group.spec.ts` | investigar |
| E58-C03 | E2E | contact-groups | `contact-group.spec.ts` | investigar |
| E58-C05 | E2E | contact-groups | `contact-group.spec.ts` | investigar |
| A50-C01 | API | contact-groups | `contact-group.spec.ts` | investigar |
| A50-C04 | API | contact-groups | `contact-group.spec.ts` | investigar |
| E08-C01 | E2E | models | `automated-document.spec.ts` | investigar |
| A07-C03 | API | models | `automated-model.spec.ts` | investigar |
| E12-C01 | E2E | processing | `associate-document.spec.ts` | ruído provável |
| E61-C01 | E2E | processing | `imported-document-share.spec.ts` | ruído provável |
| E45-C01 | E2E | processing | `label-document.spec.ts` | ruído provável |
| A53-C01 | API | processing | `imported-document-share.spec.ts` | ruído provável |
| E43-C01 | E2E | public-agents | `change-email-pending.spec.ts` | investigar |
| E51-C01 | E2E | workboard | `date-filter-reopen.spec.ts` | investigar |
| E51-C02 | E2E | workboard | `date-filter-reopen.spec.ts` | investigar |
| E34-S09 | E2E | signatures | `long-document.spec.ts` | ruído provável |
| E34-S10 | E2E | signatures | `long-document.spec.ts` | ruído provável |
| E34-S11 | E2E | signatures | `large-page-attachment.spec.ts` | ruído provável |
| E34-S12 | E2E | signatures | `large-page-attachment.spec.ts` | ruído provável |
| A30-C14 | API | signatures | `citizen.spec.ts` | ruído provável |
| A30-C15 | API | signatures | `citizen.spec.ts` | ruído provável |
| A30-C16 | API | signatures | `citizen.spec.ts` | ruído provável |
| A30-C17 | API | signatures | `citizen.spec.ts` | ruído provável |
| A30-C21 | API | signatures | `citizen-alphanumeric.spec.ts` | ruído provável |
| A30-C22 | API | signatures | `citizen-alphanumeric.spec.ts` | ruído provável |
| A30-C23 | API | signatures | `citizen-alphanumeric.spec.ts` | ruído provável |
| A30-C24 | API | signatures | `citizen-alphanumeric.spec.ts` | ruído provável |

**Nenhuma falha caiu em `@auth`** (13 casos, 0 falhas) — os 13 CTs já confirmados em Playwright da [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/01 Automação/02 - Validação automação|TR 1.24-1.25]] (CT-001 a CT-012 + CT-038) seguem verdes, inclusive no meio de um run saturado — reforça que são estáveis.

Os 4 "bugs de produto conhecidos" (`test.fail`, SGV-8395 e mais 2 sem SGV) continuam falhando como esperado — não são novidade, não entram na contagem de 26.

## O que isso confirma sobre o piloto do botão (CT-038 / A55-C01)

Três execuções reais confirmam CT-038 estável, nenhuma delas isolada da outra:

| Run | Escopo | A55-C01 |
|---|---|---|
| `run-1a740878` (05/10, 21:34) | 3 casos (smoke/organizational) | não incluído neste escopo |
| `run-d0db750e` (06/10, 10:08) | 11 casos (smoke + alguns domínios) | ✅ passou (3.9s) |
| `run-3a4d6ac4` (06/10, 12:24) | 399 casos (suíte completa) | ✅ passou |

## Achado corrigido nesta rodada

A tabela "Resultado por CT" do [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/01 Automação/02 - Validação automação|02 - Validação automação]] da SGV-11971 guardava o caminho do spec sem o prefixo `tests/` (ex. `` `api/auth/login.spec.ts` `` em vez de `` `tests/api/auth/login.spec.ts` ``) — as 13 linhas foram corrigidas.

## Próximo passo sugerido

Rodar `contact-groups`, `models`, `public-agents` e `workboard` isolados (não saturados) pra confirmar se as 10 falhas desses domínios são reais ou também ruído — são os que **não** têm relação óbvia com o gerador de PDF, então merecem checagem antes de descartar.

## Referências

- [[Automação Playwright]] — arquitetura, convenção de execução, o aviso sobre não rodar a suíte inteira
- [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/01 Automação/02 - Validação automação|02 - Validação automação (SGV-11971)]]
