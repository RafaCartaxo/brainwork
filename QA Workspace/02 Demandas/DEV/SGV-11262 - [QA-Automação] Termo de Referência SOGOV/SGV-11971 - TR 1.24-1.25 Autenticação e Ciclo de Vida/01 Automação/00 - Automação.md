---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
framework: playwright
status: execucao
pontos: ""
---
# Automação — SGV-11971 (TR 1.24–1.25)

> [!info] Objetivo
> Registrar o estado e a estratégia de automação deste ciclo. O placar por CT fica somente em `02 - Validação automação`; decisões e arquitetura deste ciclo ficam em `01 - Plano de automação`.

## Navegação

- [[../00 QA/00 README|README da SGV-11971]] — estado do ciclo de QA.
- [[../00 QA/03 - Casos de teste|Casos de teste]] — fonte única dos 38 CTs.
- [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/01 - Plano de automação|01 — Plano de automação]] — escopo, abordagem e preparação.
- [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/02 - Validação automação|02 — Validação automação]] — resultado atual por CT.
- [[../../Roadmap - Automação TR|Roadmap da iniciativa SGV-11262]] — direção e sequência das entregas.
- [[../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed atual]] — dados e estados consumidos pelos 13 CTs Playwright.

## Estado atual

- Escopo funcional do ciclo: **38 CTs**.
- Placar histórico: **25 aprovados**, 4 falharam, 6 bloqueados e 3 aguardam implementação ou evidência.
- Framework atual: **Playwright**. CT-001–012 e CT-038 estão identificados no código Playwright; os 12 outros CTs aprovados ainda estão associados à suíte Cypress legada.
- Os 13 CTs Playwright não falharam no run amplo registrado em 06/10/2026. Ainda falta demonstrar execução reproduzível em uma instância dedicada.
- Instância dedicada de teste criada: **ID 225 — “Termo De Referência - Sogov”**. O seed atual ainda procura o nome fixo `E2E Automatic Test` e pode criar outra instância; ajustar o alvo antes de executá-lo.
- CT-038 consta como verde no registro disponível, mas seu código está em worktree com `HEAD` destacado (`16c41e4`) e sem commit na verificação de 07/10. Definir branch e commit antes de encerrar qualquer entrega que o inclua.

## Próxima ação

Preparar a primeira entrega candidata de estabilização, com pacote próprio `00–02` para CT-001–012 e CT-038. Primeiro, fazer o seed selecionar a instância 225 no mesmo backend e impedir a criação involuntária de outro cliente. Depois, validar a preparação e os CTs nessa instância. Antes de encerrar a entrega, resolver o destino do código ainda sem branch/commit do CT-038.

## Documentos deste pacote

| Documento | Responsabilidade |
|---|---|
| `00 - Automação.md` | Estado resumido e navegação deste pacote |
| `01 - Plano de automação.md` | Escopo, arquitetura, preparação e critérios da entrega |
| `02 - Validação automação.md` | Placar atual, exclusivamente por CT |

Os arquivos `03 - Handoff de execução.md` e `04 - Documentação de entrega.md` pertencem ao pacote antigo e não são parte do padrão atualizado. Permanecem preservados enquanto suas informações forem reconciliadas.
