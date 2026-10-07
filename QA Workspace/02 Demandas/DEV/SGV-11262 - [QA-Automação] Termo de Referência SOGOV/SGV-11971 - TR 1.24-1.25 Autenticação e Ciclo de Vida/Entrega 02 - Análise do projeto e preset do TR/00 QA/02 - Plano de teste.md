---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — SGV-12082

> [!info]- Navegação QA
> **README:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Casos:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Matriz:** [[Matriz - Análise do preset provável]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Objetivo

Verificar por inspeção documentada que a análise cobre os requisitos 1.1–1.43 do PDF, identifica o tipo de evidência aplicável, mapeia a automação e os dados existentes (incluindo os 38 CTs de 1.24–1.25) e fundamenta as opções de preparação/reuso.

## Riscos e escopo

- **Risco principal:** confundir dados preparados pelo seed global com dados realmente consumidos por cada CT, ou tratar configuração de ambiente como prova de portabilidade.
- **Fora do escopo desta rodada:** executar testes/seed contra ambientes, alterar código ou validar comportamento funcional do produto.

## Estratégia de teste

- Revisar a PDF fonte completo e a fonte de casos da SGV-11971; conferir a cobertura do TR e rastrear CT-001–038 como casos existentes de 1.24–1.25.
- Inspecionar código/configuração/documentação do projeto Playwright em modo somente leitura; registrar caminho/trecho como evidência.
- Para cada requisito, identificar se a validação requer teste funcional, dados/estado, evidência operacional/técnica ou documentação; para CTs automatizados, comparar pré-condições com fixtures, seed, dados próprios do teste e limpeza.
- Separar cada achado em confirmado por código/documento, confirmado por execução já registrada, inferência ou pendente de confirmação.
- Revisar se a recomendação de preset contém somente dados e estados necessários ao escopo e lista dependências ambientais.

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|DISC-001]] | Análise técnica | Repositório/documentos | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-002\|DISC-002]] | Análise de cobertura | Casos + código | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-003\|DISC-003]] | Análise de dados/ambientes | Código + configuração | Manual | [[04 - Validação dev\|Registrar resultado]] |
| [[03 - Casos de teste#^ct-004\|DISC-004]] | Síntese/recomendação | Matriz + evidências | Manual | [[04 - Validação dev\|Registrar resultado]] |

## Entrada e saída

**Entrada:** [[Fontes/Requisitos Sogov.pdf|PDF completo do TR]], casos da SGV-11971, mapa do seed atual, repositório Playwright e configuração/documentação de ambientes acessível sem segredos.

**Saída:** mapa do projeto; matriz de cobertura dos requisitos do TR; rastreabilidade dos 38 CTs existentes de 1.24–1.25; recomendação fundamentada do preset provável e sequência de entregas candidatas.
