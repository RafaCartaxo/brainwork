---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11971
tipo: matriz-analise
status: em levantamento
---
# Matriz — análise do preset provável para o TR

> [!info] Propósito
> Esta matriz vai da regra/caso aos dados e ao mecanismo atual de preparação. Ela deve orientar a recomendação do preset inicial; não é um catálogo geral do SOGOV nem uma especificação aprovada de seed.
>
> **Fonte funcional:** [[../../Arquivo/00 QA/03 - Casos de teste|38 CTs da SGV-11971]] · **Demanda:** [[01 - Demanda]] · **Plano:** [[02 - Plano de teste]] · **Roadmap:** [[../../../Roadmap - Automação TR|Automação TR]]

## Como preencher

- Use uma linha por CT quando as pré-condições ou dados diferirem; agrupe apenas quando ator, estado e preparação forem iguais.
- Para cada afirmação, registre a fonte (caso, arquivo, configuração ou execução existente).
- Use **Confirmado**, **Inferido** ou **A confirmar**. Não transforme lacuna em fato.
- Não copiar valores secretos. Registre apenas nomes de variáveis/chaves e onde a configuração deve ser verificada.

## Legenda de estado do conhecimento

| Estado | Significado |
|---|---|
| Confirmado | Visível diretamente no CT/código/documento ou em execução já registrada |
| Inferido | Interpretação provável que ainda precisa de validação |
| A confirmar | Evidência ausente, ambiente inacessível ou comportamento não verificado |

## Matriz de cobertura e dados

| CT(s) | Requisito/fluxo | Framework/situação conhecida | Ator, entidade e estado inicial | O que o caso consome/altera | Preparação atual e origem da massa | Ambiente/portabilidade | Evidência e confiança | Lacuna / candidato de preset |
|---|---|---|---|---|---|---|---|---|
| CT-001–012, CT-038 | Autenticação, credenciais e sessões concorrentes | Playwright; último run registrado: 13 aprovados; execução atual não repetida nesta análise | Servidor por worker; cidadão PJ por worker em casos pertinentes; instância no manifesto; estados de login válidos/inválidos conforme CT | Credenciais válidas ou negativas; CT-038 abre duas sessões API; casos não alteram estado de conta conforme mapa técnico | Seed global + pools/fixtures; detalhes conhecidos no [[../../../Conhecimento/Mapa do seed Playwright atual - SGV-11971\|mapa atual do seed]] | Reuso depende do backend/URLs/credenciais configurados; seleção de alvo é atualmente perfil fixo. Portabilidade não demonstrada | Confirmado pelo mapa e código anteriormente inspecionado; revalidar referências nesta entrega | Separar dependências realmente comuns; decidir se um perfil dedicado/configurável basta ou se há necessidade de refatorar seed. **A confirmar** após revisar estrutura e ambientes atuais. |
| CT-013–019 | Bloqueio e desbloqueio por tentativas | CT-013–019 estão entre os 25 históricos aprovados/estado da automação a reconciliar; framework atual por CT a mapear | A preencher por CT a partir da fonte | A preencher por CT: tentativas, bloqueio, desbloqueio, tempo/estado | A verificar: seed, preparação manual/API e possível criação no próprio teste | A comparar entre ambientes | A confirmar | Identificar identidades isoladas por CT, reset/limpeza e estado bloqueado reproduzível |
| CT-020–026 | Estado Ativo/Licença | Estado individual a reconciliar com o placar atual | A preencher por CT a partir da fonte | A preencher por CT | A verificar nos testes e preparação | A comparar entre ambientes | A confirmar | Identificar datas/relógio, permissões e transições necessárias |
| CT-027–031 | Estado Férias | Estado individual a reconciliar com o placar atual | A preencher por CT a partir da fonte | A preencher por CT | A verificar nos testes e preparação | A comparar entre ambientes | A confirmar | Identificar datas/relógio, permissões e reset necessário |
| CT-032–038 | Estado Inativo/Suspenso e sessões relacionadas | CT-038 Playwright; demais status por CT a reconciliar | A preencher por CT a partir da fonte | A preencher por CT | A verificar nos testes e preparação | A comparar entre ambientes | A confirmar | Separar dependências de sessão/estado e atores; decidir se pertencem ao preset inicial ou a fatia própria |

> Agrupamentos provisórios acima servem apenas para orientar o levantamento. **Não substituem a leitura caso a caso**: a aceitação exige que todos os CT-001–038 sejam explicitamente cobertos e que grupos sejam desmembrados quando seus dados/preparação diferirem.

## Catálogo mínimo candidato

Preencher somente após cruzar os CTs com código e fontes de dados. Manter cada entrada ligada aos CTs que a exigem.

| Dado/estado candidato | CTs que justificam | Preparação existente | Reuso entre ambientes | Ação candidata | Evidência/pendência |
|---|---|---|---|---|---|
| Instância-alvo e configuração de endpoint | CTs que executam contra a instância | Perfil fixo no baseline; URLs fornecidas pelo ambiente | Não demonstrado para seleção de instância diferente | Avaliar parametrização segura com validação explícita do alvo | Confirmar ambientes e proteção contra criação acidental |
| Atores de servidor/cidadão e credenciais de teste | CTs de autenticação/estado | Pools por worker e credenciais ambientais no baseline Playwright | Reuso de atores no mesmo backend existe; entre ambientes a confirmar | Documentar pré-condições, ownership e reset por ambiente | Validar estado real e política de credenciais de teste |
| Estados de conta (bloqueio, licença, férias, inativo/suspenso) | CTs correspondentes após mapeamento individual | A verificar por CT | A confirmar | Determinar se são provisionados, alterados em teste ou preparados por API | Registrar operação inversa/limpeza e isolamento |
| Módulo/serviço/permissões | Somente CTs que comprovarem dependência | Seed declara catálogo mais amplo; consumo de cada CT a verificar | A confirmar | Incluir apenas dependências rastreadas | Cruzar passos/precondições e código dos testes |

## Decisões ao concluir

- **Forma recomendada do preset:** a preencher com comparação fundamentada (perfil/configuração, seed reconciliador, preparação específica por suíte ou combinação).
- **Escopo mínimo inicial:** CTs, atores, entidades e estados que a matriz comprovar necessários.
- **Diferenças por ambiente:** endpoint, credenciais, disponibilidade de entidades, permissões e limpeza.
- **Riscos de isolamento e concorrência:** a preencher.
- **Primeiras entregas sugeridas:** a preencher com escopo pequeno, dependências e aceite próprio.
