---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
casos_funcionais_origem: "[[../../Arquivo/00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
framework: playwright
ambiente: hml
status: planejado
---
# Automação — Entrega 01: Baseline na instância 225

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos técnicos da entrega:** [[../00 QA/03 - Casos de teste]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|CTs da SGV-11971]]
> **Plano de automação:** [[01 - Plano de automação]]
> **Validação automação:** [[02 - Validação automação]]

> [!settings]- Controle da automação
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(bloqueado),option(concluido)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(cypress_legado),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Ponto de entrada da cobertura automatizada. O escopo e a estratégia ficam em [[01 - Plano de automação]]; os resultados atuais por CT ficam em [[02 - Validação automação]]. Os casos técnicos desta entrega estão em `00 QA/`; a cobertura funcional é definida na SGV-11971 e referenciada aqui.

> [!warning] Escopo histórico
> O piloto na instância 225 não foi executado nem validado. A análise ativa está na [[../../Entrega 02 - Análise do projeto e preset do TR/00 QA/00 README|SGV-12082]]; aguardar sua recomendação antes de implementar ou executar o seed.

## Próxima ação

- Confirmar o backend da instância 225 e resolver o destino de CT-038; depois implementar a seleção segura da instância no seed.

## Repositório e entrega

- **Repositório:** `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`
- **Branch/MR:** ainda não iniciado.

## Pendências gerais

- Confirmar que o ambiente configurado contém a instância 225.
- Resolver o arquivo de CT-038, hoje em `HEAD` destacado (`16c41e4`) e sem commit.

## Checklist de encerramento

- [ ] Plano e escopo atualizados em [[01 - Plano de automação]].
- [ ] Resultado mais recente de cada CT registrado em [[02 - Validação automação]].
- [ ] Cobertura técnica e funcional sincronizada nas respectivas notas de casos.
- [ ] Revisão de código concluída no repositório/MR.
- [ ] Status e próxima ação atualizados.
