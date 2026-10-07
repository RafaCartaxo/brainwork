---
demanda_pai: SGV-11262
ciclo_referencia: SGV-11971
casos_origem: "[[../../00 QA/03 - Casos de teste]]"
casos_entrega: "[[../00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
status: planejado
---

# Plano de automação — Baseline de autenticação na instância 225

> [!info]- Navegação
> **Hub:** [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/01 Automação/00 - Automação]]
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/01 Automação/02 - Validação automação]]
> **Roadmap:** [[../../../Roadmap - Automação TR|Roadmap da SGV-11262]]
> **Casos de origem:** [[../../00 QA/03 - Casos de teste|38 CTs da SGV-11971]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Objetivo e escopo

- **Objetivo:** executar o seed existente e os CTs de autenticação numa instância de teste dedicada já criada.
- **Instância:** ID 225 — “Termo De Referência - Sogov”.
- **CTs incluídos:** CT-001–012 e CT-038.
- **Fora do escopo:** demais CTs da SGV-11971, teste de criação de cliente por execução, implementação do Roteiro de Sanidade 01 como preset e ampliação do catálogo atual.

## Estratégia

| Grupo | Camada | Dados/estado inicial | Reuso ou mudança | Dependência/gate |
|---|---|---|---|---|
| CT-001–012, CT-038 | API | Instância 225 acessível; atores de servidor e cidadão provisionados pelo seed | Reusar specs, fixtures e pools atuais. Adicionar seleção explícita por PW_INSTANCE_ID (ou configuração equivalente), conferir identidade da instância e gravar o resultado no manifesto | Confirmar que as URLs configuradas apontam ao mesmo backend onde a 225 existe; confirmar disponibilidade do login no estado atual da instância; resolver CT-038 sem commit |
| Seed global do projeto API | API/setup | Baseline amplo atual do repositório | Preservar o caminho padrão das demais suítes. Quando ID explícito estiver configurado, não criar instância como fallback; interromper se a validação do ID/nome falhar | Execução dedicada apenas para esta fatia; reconhecer que o seed atual também provisiona outros recursos globais |

O parâmetro de instância deve ser opcional: sem ele, o comportamento padrão atual continua usando E2E Automatic Test. Com o alvo explícito, o seed deve buscar a instância pelo ID, validar o nome esperado e falhar sem criar outra instância caso não consiga confirmar o alvo. O manifesto deve registrar o ID e o nome efetivamente usados; sua impressão digital deve distinguir o alvo dedicado.

O seed atual prepara recursos globais de outras suítes além dos atores usados pelos 13 CTs. Esta entrega não os amplia nem afirma que os 13 CTs dependem deles. Uma eventual divisão do seed global é decisão técnica separada.

## Pronto para implementar quando

- [ ] Confirmado que o ambiente configurado corresponde ao backend onde a instância 225 foi criada.
- [ ] Confirmado que a instância está num estado em que os atores podem ser preparados e autenticar.
- [ ] Seleção explícita por ID e verificação do nome estão definidas sem fallback para criação.
- [ ] Fica preservado o comportamento padrão quando a configuração específica não é fornecida.
- [ ] Destino do código CT-038 foi definido ou o CT foi explicitamente bloqueado nesta rodada.

## Pronto para validar quando

- [ ] Alteração implementada no repositório e revisada.
- [ ] Seed executado duas vezes; ambas as execuções registram ID 225 e não criam cliente adicional.
- [ ] CT-001–012 e CT-038 executados na instância 225, com resultados em [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/01 Automação/02 - Validação automação]].
- [ ] O escopo de execução e os artefatos do run foram registrados.

## Execução

A primeira validação deve rodar somente o seed e os CTs deste escopo, com a opção de instância explícita habilitada. Não apontar a suíte completa para a 225 nesta entrega. A criação de cliente novo por execução deve ser tratada numa entrega separada, com política de unicidade e retenção dos clientes criados.
