---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de análise — SGV-12082

> [!info]- Navegação QA
> **README:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano:** [[02 - Plano de teste]]
> **Validação:** [[04 - Validação dev]]
> **Matriz:** [[Matriz - Análise do preset provável]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]]

> Estes são critérios verificáveis da investigação, não CTs funcionais adicionais do Termo. Os CTs funcionais continuam na fonte da SGV-11971.

## Matriz de cobertura

| Critério | Verificação |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[#^ct-001\|DISC-001]] |
| [[01 - Demanda#^c2\|C2]] | [[#^ct-002\|DISC-002]] |
| [[01 - Demanda#^c3\|C3]] | [[#^ct-003\|DISC-003]] |
| [[01 - Demanda#^c4\|C4]] | [[#^ct-004\|DISC-004]] |
| [[01 - Demanda#^c5\|C5]] | [[#^ct-004\|DISC-004]] |

> [!example]- DISC-001 · Explicar a arquitetura e o fluxo de execução atual
>
> ## Cenário
>
> **Descrição:** confirmar que a nota identifica os componentes que iniciam os testes, preparam dados, distribuem fixtures e registram resultados.
>
> **Dado** o projeto Playwright atualmente usado pelo TR  
> **Quando** alguém seguir a configuração de execução até a preparação de dados e consumo pelas suítes  
> **Então** o mapa deve nomear os componentes e suas responsabilidades, ligar cada afirmação à fonte e apontar claramente o que não foi confirmado.
>
> **Resultado esperado:** uma pessoa nova consegue explicar o fluxo sem inferir detalhes ausentes.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> **Tipo:** análise técnica  
> **Camada:** repositório/documentos  
> **Automação:** não se aplica  
> **Execução:** planejado

^ct-001

> [!example]- DISC-002 · Cobrir os 38 CTs e registrar suas dependências
>
> ## Cenário
>
> **Descrição:** conferir a rastreabilidade integral da fonte funcional para a matriz de análise.
>
> **Dado** que a SGV-11971 contém CT-001–CT-038  
> **Quando** cada caso for comparado ao seu cenário, pré-condições e situação de automação conhecida  
> **Então** cada CT deve constar individualmente ou em grupo explicitamente justificado, com dependências e dúvidas registradas.
>
> **Resultado esperado:** nenhum CT desaparece por estar fora dos 13 já mapeados em Playwright.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> **Tipo:** análise de cobertura  
> **Camada:** casos + código  
> **Automação:** não se aplica  
> **Execução:** planejado

^ct-002

> [!example]- DISC-003 · Distinguir dados consumidos, preparação e variação de ambiente
>
> ## Cenário
>
> **Descrição:** verificar se a matriz descreve a massa necessária com proveniência suficiente para decidir reutilização.
>
> **Dado** cada CT/grupo e seus pré-requisitos  
> **Quando** forem comparados com seed, fixtures, criação no próprio teste e configuração ambiental  
> **Então** a matriz deve indicar ator/entidade/estado, preparação e ambiente relevante, marcando como “a confirmar” o que não tiver evidência.
>
> **Resultado esperado:** massa preparada globalmente não é apresentada como massa consumida sem comprovação.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> **Tipo:** análise de dados  
> **Camada:** código + configuração  
> **Automação:** não se aplica  
> **Execução:** planejado

^ct-003

> [!example]- DISC-004 · Recomendar preset e próximas fatias com base nos achados
>
> ## Cenário
>
> **Descrição:** avaliar se as opções propostas derivam da matriz e deixam explícitas as incertezas.
>
> **Dado** o mapa do projeto e a matriz dos CTs  
> **Quando** forem consolidadas as necessidades comuns, diferenças e lacunas  
> **Então** a recomendação deve delimitar um preset inicial provável, comparar alternativas técnicas sem decidir refatoração antecipadamente e ordenar entregas candidatas com CTs/resultado esperado.
>
> **Resultado esperado:** a equipe consegue escolher a primeira implementação seguinte sem abrir uma demanda ampla ou inventário geral.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]] · [[01 - Demanda#^c5|C5]]
>
> **Tipo:** síntese técnica  
> **Camada:** documentação  
> **Automação:** não se aplica  
> **Execução:** planejado

^ct-004
