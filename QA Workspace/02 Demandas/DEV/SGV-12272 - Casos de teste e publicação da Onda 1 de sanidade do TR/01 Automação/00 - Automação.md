---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-test"
framework: playwright
ambiente: hml
status: planejado
---

# Automação — SGV-12272

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Análise:** [[01 - Análise]]
> **Plano de automação:** [[02 - Plano de automação]]
> **Validação automação:** [[03 - Validação automação]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(bloqueado),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Ponto de entrada da cobertura automatizada. A abordagem, o escopo da onda e a massa de dados ficam em [[01 - Análise|01 - Análise]]; a estratégia por suíte fica em [[02 - Plano de automação|02 - Plano de automação]]; os resultados atuais, por CT, ficam em [[03 - Validação automação|03 - Validação automação]]. A demanda e os CTs de `00 QA/` continuam sendo a fonte do comportamento esperado.

## Próxima ação

- Validação manual dos 20 CTs (gate da Análise) e decisões pendentes do Rafael — ver [[01 - Análise#Pendências de decisão|Pendências de decisão]].

## Repositório e entrega

- **Repo / instruções:** `~/Documentos/Sogov/sogov-automation-test/playwright` — `README.md`, `ENVIRONMENTS.md` e [[00 - Índice da automação Playwright|índice no vault]].
- **Branch/MR:** nenhum ainda (gate da Análise aberto).

## Pendências gerais

- Nenhuma pendência geral registrada.

## Checklist de encerramento

- [ ] Análise da onda concluída em [[01 - Análise]] (decisões fechadas e tabela **Massa desta entrega** preenchida).
- [ ] Plano e escopo atualizados em [[02 - Plano de automação]].
- [ ] Resultado mais recente de cada CT registrado em [[03 - Validação automação]].
- [ ] Cobertura sincronizada no campo **Automação** dos CTs em `../00 QA/03 - Casos de teste`.
- [ ] Revisão de código concluída no repositório/MR.
- [ ] Status e próxima ação atualizados.
