---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../../Arquivo/00 QA/03 - Casos de teste]]"
casos_entrega: "[[../00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
framework: playwright
ambiente: hml
status: planejado
---
# Automação — Entrega 01: Baseline na instância 225

> [!info]- Navegação QA
> **README:** [[../00 QA/00 README|Entrega 01]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos da entrega:** [[../00 QA/03 - Casos de teste]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|SGV-11971]]
> **Plano:** [[01 - Plano de automação]]
> **Validação:** [[02 - Validação automação]]
> **Roadmap:** [[../../../Roadmap - Automação TR|SGV-11262]]
> **Mapa do seed:** [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa técnico]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(bloqueado),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Entrada do pacote automatizado desta entrega. Os critérios técnicos do seed estão em QA; este placar cobre somente os CTs funcionais incluídos.

## Estado

- **Alvo:** instância dedicada ID 225 — “Termo De Referência - Sogov”.
- **CTs funcionais incluídos:** CT-001–012 e CT-038, originados na SGV-11971 e sem cópia nesta entrega.
- **Situação:** implementação e execução específica na instância 225 pendentes.
- **Bloqueio conhecido:** CT-038 está em worktree com `HEAD` destacado (`16c41e4`), sem commit; resolver o destino antes do encerramento.
- **Pré-condição de execução:** confirmar que a configuração aponta ao backend onde a instância 225 existe.

## Próxima ação

Implementar no seed a seleção segura da instância 225, conforme o plano; depois executar o seed duas vezes e validar apenas os CTs deste escopo.

## Repositório e entrega

- **Repositório:** `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`
- **Branch/MR:** ainda não iniciado.

## Checklist de encerramento

- [ ] Plano e escopo atualizados em [[01 - Plano de automação]].
- [ ] Resultado atual de cada CT registrado em [[02 - Validação automação]].
- [ ] Cobertura sincronizada nos CTs de origem quando aplicável.
- [ ] Revisão de código concluída no repositório/MR.
- [ ] Status e próxima ação atualizados.
