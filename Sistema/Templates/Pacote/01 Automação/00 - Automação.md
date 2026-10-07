---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-test"
framework: playwright
ambiente: hml
status: planejado
---

# Automação — <ID>

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Plano de automação:** [[01 - Plano de automação]]
> **Validação automação:** [[02 - Validação automação]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(bloqueado),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Ponto de entrada da cobertura automatizada. O escopo e a estratégia ficam em [[01 - Plano de automação|01 - Plano de automação]]; os resultados atuais, por CT, ficam em [[02 - Validação automação|02 - Validação automação]]. A demanda e os CTs de `00 QA/` continuam sendo a fonte do comportamento esperado.

## Próxima ação

- <ação concreta, com responsável se necessário>

## Repositório e entrega

- **Repo / instruções:** <link para o repo e seu README>
- **Branch/MR:** <link quando existir>

## Pendências gerais

- Nenhuma pendência geral registrada.

## Checklist de encerramento

- [ ] Plano e escopo atualizados em [[01 - Plano de automação]].
- [ ] Resultado mais recente de cada CT registrado em [[02 - Validação automação]].
- [ ] Cobertura sincronizada no campo **Automação** dos CTs em `../00 QA/03 - Casos de teste`.
- [ ] Revisão de código concluída no repositório/MR.
- [ ] Status e próxima ação atualizados.
