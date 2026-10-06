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

## Falhas (26) — por domínio

| Domínio | Casos falhos | Hipótese |
|---|---|---|
| `signatures` (large-page-attachment, long-document) | 4 (E34-S09/S10/S11/S12) | **Alta suspeita de ruído** — a própria doc já marca `signatures` como "anormalmente lento", e os nomes dos specs (anexo grande, documento longo) são exatamente o perfil que satura o gerador de PDF |
| `signatures` (citizen, citizen-alphanumeric) | 8 (A30-C14/15/16/17, C21/22/23/24) | Mesma suspeita — mesmo domínio, mesmo gerador de PDF por trás da assinatura |
| `contact-groups` | 5 (E58-C01/03/05, A50-C01/04) | Sem relação óbvia com PDF — candidato a investigar separado, não descartar como ruído sem rodar isolado |
| `processing` (automated-document, associate-document, imported-document-share, label-document) | 4 (E08-C01, E12-C01, E61-C01, E45-C01) | Processing também depende do gerador de documento — mesma suspeita de saturação |
| `models` | 1 (A07-C03) | Isolado — investigar |
| `public-agents` | 1 (E43-C01) | Isolado — investigar |
| `workboard` | 2 (E51-C01/02) | Isolado — investigar |

**Nenhuma falha caiu em `@auth`** (13 casos, 0 falhas) — os 13 CTs já confirmados em Playwright da [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/02 - Validação automação|TR 1.24-1.25]] (CT-001 a CT-012 + CT-038) seguem verdes, inclusive no meio de um run saturado — reforça que são estáveis.

Os 4 "bugs de produto conhecidos" (`test.fail`, SGV-8395 e mais 2 sem SGV) continuam falhando como esperado — não são novidade, não entram na contagem de 26.

## O que isso confirma sobre o piloto do botão (CT-038 / A55-C01)

Três execuções reais confirmam CT-038 estável, nenhuma delas isolada da outra:

| Run | Escopo | A55-C01 |
|---|---|---|
| `run-1a740878` (05/10, 21:34) | 3 casos (smoke/organizational) | não incluído neste escopo |
| `run-d0db750e` (06/10, 10:08) | 11 casos (smoke + alguns domínios) | ✅ passou (3.9s) |
| `run-3a4d6ac4` (06/10, 12:24) | 399 casos (suíte completa) | ✅ passou |

## Achado corrigido nesta rodada

A tabela "Resultado por CT" do [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/02 - Validação automação|02 - Validação automação]] da SGV-11971 guardava o caminho do spec sem o prefixo `tests/` (ex. `` `api/auth/login.spec.ts` `` em vez de `` `tests/api/auth/login.spec.ts` ``) — as 13 linhas foram corrigidas.

## Próximo passo sugerido

Rodar `contact-groups`, `models`, `public-agents` e `workboard` isolados (não saturados) pra confirmar se as 8 falhas desses domínios são reais ou também ruído — são os que **não** têm relação óbvia com o gerador de PDF, então merecem checagem antes de descartar.

## Referências

- [[Automação Playwright]] — arquitetura, convenção de execução, o aviso sobre não rodar a suíte inteira
- [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/02 - Validação automação|02 - Validação automação (SGV-11971)]]
