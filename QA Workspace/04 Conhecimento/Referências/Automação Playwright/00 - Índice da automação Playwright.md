---
tags: [qa, conhecimento, automacao]
tipo: indice
---
# Índice — Automação Playwright

> [!info]- Navegação
> **Fonte primária de comandos e configuração:** `~/Documentos/Sogov/sogov-automation-test/playwright/README.md` (versionado junto do código)
> **Proposta de skills de automação (pendente):** [[2026-10-01-skills-automacao-playwright]]

## Objetivo desta pasta

Reunir a referência de automação Playwright do SOGOV, independente de qual demanda a esteja usando. Esta pasta **não duplica** o `playwright/README.md` do repositório.

> [!important] Fonte primária: o README do repo
> Comandos, "Como rodar", setup, variáveis do `.env`, como uma execução funciona (launcher, projetos, seed, fixtures), regras para escrever testes (independência, paralelismo e atores, nomes e tags), lista de testes e pontos de atenção estão em `sogov-automation-test/playwright/README.md`. O próprio README diz: *"Se o código mudar, vale o código."* Em caso de divergência com esta pasta, vale o README (e, acima dele, o código).
>
> Aqui fica só o que é exclusivo do vault: histórico de decisão, achados de QA, mapeamento das variáveis antigas e registros de execução.

> [!danger] Achado de QA: não rodar a suíte inteira de uma vez
> Rodar `npm run test` (todos os projetos juntos) satura o gerador de PDF do backend e produz falhas que **não são bugs reais** (`system.messages.pdf-generator-attachment-error`). Ir por domínio, em lotes de 15–20 min; os specs de `signatures` são anormalmente lentos. Duas execuções simultâneas no mesmo ambiente também não são suportadas. Descoberto em 01/10/2026 e confirmado em [[2026-10-06 - Execução completa (399 casos)]]; o README do repo lista o comando `npm run test` sem esse aviso.

## Os documentos

| # | Documento | Papel |
|---|---|---|
| 1 | [[01 - Primeiros passos]] | Setup do zero, enxuto (instalar, browser, `test:infra`, `.env`). Comandos validados na máquina do Rafael. |
| 2 | [[02 - Migração Cypress → Playwright]] | Histórico e decisão: por que a nota existe, descarte do Cypress, commits da migração, equivalências Cypress → Playwright, lacunas e achados, mapeamento das variáveis antigas. |
| 3 | [[2026-10-06 - Execução completa (399 casos)]] | Registro de uma execução real (suíte inteira contra HML): falhas por domínio e hipóteses. Pasta `Execuções/` guarda os próximos. |

## Cadeia de referência

```text
Código do repo (fonte final: "se o código mudar, vale o código")
    ↓ documentado em
sogov-automation-test/playwright/README.md   (comandos, execução, regras, seed, lista de testes)
    ↓ complementado, no vault, por
01 - Primeiros passos                         (setup validado)
02 - Migração Cypress → Playwright            (histórico, decisões, variáveis antigas)
Execuções/AAAA-MM-DD - ...                    (registros de run)
```

## Origem e histórico

Esta pasta nasceu em 16/10/2026 da divisão da nota única `Automação Playwright.md` (criada em 01/10/2026, quando se descobriu que o repo tinha migrado para Playwright em setembro sem registro no vault) e da nota solta `Execução completa Playwright - 06-10-2026.md`. As seções de comandos, "Como rodar", convenção de escrita, fluxo do QA (diagramas) e a lista de arquitetura foram **removidas daqui de propósito**, porque o README do repo as cobre e duas fontes de verdade se desalinham. O conteúdo de comparação com Cypress que o README não tem foi preservado em [[02 - Migração Cypress → Playwright]].
