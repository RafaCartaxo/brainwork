---
demanda_pai: SGV-11262
ciclo_referencia: SGV-11971
casos_origem: "[[../../00 QA/03 - Casos de teste]]"
casos_entrega: "[[../00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
framework: playwright
ambiente: hml
status: planejado
---

# Automação — Baseline de autenticação na instância 225

> [!info] Propósito desta entrega
> Tornar seguro e reproduzível o uso da instância dedicada **ID 225 — “Termo De Referência - Sogov”** pelo seed existente e validar nela os 13 CTs de autenticação da SGV-11971. Esta entrega é vinculada à iniciativa SGV-11262 e usa os CTs da SGV-11971 como escopo de validação.

## Navegação

- [[01 - Plano de automação|01 — Plano de automação]]
- [[02 - Validação automação|02 — Validação automação]]
- [[../../../Roadmap - Automação TR|Roadmap da iniciativa]]
- [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed e da instância 225]]
- [[../../00 QA/03 - Casos de teste|Casos de teste da SGV-11971]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(bloqueado),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

## Estado

- **Instância alvo:** ID 225 — “Termo De Referência - Sogov”.
- **Rastreio no tracker:** pacote local de planejamento; ainda sem ID de demanda filha.
- **Comportamento atual do seed:** procura E2E Automatic Test pelo nome e pode criar outra instância. Ainda não seleciona a 225.
- **Escopo CT:** CT-001–012 e CT-038.
- **Decisão:** selecionar a 225 explicitamente e validar sua identidade; se o ID não existir ou o nome não corresponder, interromper sem criar outro cliente.
- **Execução:** ainda não iniciada. Confirmar que o ambiente configurado no run é o mesmo backend onde a 225 foi criada.

## Próxima ação

Implementar a seleção explícita e segura da instância 225 no seed, preservando o alvo padrão atual quando a configuração específica não for fornecida. Depois, rodar o seed duas vezes e validar o escopo definido no plano.

## Repositório e entrega

- **Repositório:** /home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright
- **Branch/MR:** ainda não iniciado.
- **CT-038:** consta no worktree com HEAD destacado (16c41e4) e sem commit; resolver sua inclusão antes da validação final desta entrega.

## Fora do escopo

- Criar uma instância nova em cada execução; essa possibilidade fica como teste separado.
- Replicar integralmente o Roteiro de Sanidade 01.
- Expandir o seed além dos dados que ele já provisiona e dos atores necessários à cobertura atual.
- Mudar o destino padrão das demais suítes Playwright.

## Critério de encerramento

- [ ] Seed aponta à instância 225 e confere o nome esperado.
- [ ] ID 225 ausente ou identidade divergente causa interrupção, sem fallback de criação.
- [ ] Duas execuções do seed mantêm o mesmo ID 225 e não criam outra instância.
- [ ] CT-001–012 e CT-038 são executados e registrados em [[02 - Validação automação]].
- [ ] Status, evidências e próxima ação atualizados.
