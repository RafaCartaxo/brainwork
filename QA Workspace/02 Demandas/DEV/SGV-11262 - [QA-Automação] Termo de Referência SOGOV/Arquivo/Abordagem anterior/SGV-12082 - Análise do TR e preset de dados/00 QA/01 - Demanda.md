---
prioridade: media
origem: conversa
pontos_alocados: ""
---

# SGV-12082 — Entender a automação do TR e propor o preset de dados

**Ticket de origem:** SGV-12082 · **Demanda pai:** SGV-11262 · **Ciclo de referência (fonte dos 38 CTs):** SGV-11971

> [!info]- Navegação QA/DEV
> **README:** [[00 README|Abrir README do card]]
> **Plano:** [[02 - Plano de teste]]
> **Casos:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Matriz do preset:** [[Matriz - Análise do preset provável]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]]

> [!info] Status atual
> **Próximo passo:** classificar os requisitos 1.1–1.43 do PDF fonte e mapear os 38 CTs existentes de 1.24–1.25 com evidência rastreável.

---

## Problema / contexto

O [[Fontes/Requisitos Sogov.pdf|PDF de requisitos SOGOV]] contém o TR completo, dos itens 1.1 a 1.43. A cobertura funcional organizada disponível na SGV-11971 contém 38 CTs focados nos itens 1.24 e 1.25; ela não representa a cobertura integral do TR. Também existe automação Playwright e um seed global, mas ainda falta uma visão que relacione requisitos do documento, automações existentes, dados necessários, mecanismos de preparação e diferenças entre ambientes. Sem essa visão, não há base para recomendar um preset nem dividir a evolução em entregas pequenas.

A Entrega 01, voltada ao piloto na instância 225, fica preservada como histórico enquanto esta análise redefine o próximo passo. Refatorar o seed é uma hipótese a avaliar, não uma decisão de escopo.

## Objetivo

Produzir uma leitura clara e verificável do projeto de automação e uma matriz do TR que relacione CTs, fluxos, atores/dados/estados, preparação existente e variações por ambiente. A análise deve identificar o que funciona hoje, o que pode ser reaproveitado, lacunas e as primeiras entregas pequenas recomendadas.

### Entrega desta capacidade

- Mapa legível dos componentes e do fluxo atual de execução/preparação.
- Matriz de cobertura do TR completo (itens 1.1–1.43), relacionando requisitos, automação/testes existentes, tipo de evidência e situação; agrupar subitens somente quando a regra e a validação forem comuns.
- Mapeamento detalhado dos 38 CTs existentes de 1.24–1.25, além de localizar automações/dados existentes para outros requisitos quando houver.
- Visão das diferenças de configuração e disponibilidade de massa entre ambientes, distinguindo evidência de suposição.
- Recomendação de preset provável, limitada aos dados e estados exigidos pelos escopos automatizáveis identificados; requisitos de infraestrutura/documentação devem indicar a evidência apropriada, sem forçá-los a virar dados de seed.
- Proposta de próximas fatias implementáveis, cada uma com CTs próprios e critérios de aceite sugeridos.

## Decisões de produto

- A sanidade reproduzível por cliente/instância e ambiente continua sendo direção da iniciativa, evoluindo em etapas.
- A análise começa pelo TR e pela massa já usada; não é um inventário completo de todas as entidades/configurações do SOGOV.
- Preset significa, nesta análise, uma descrição reproduzível dos dados, estados e pré-condições necessários a um escopo de CTs. A forma técnica final permanece em aberto.
- A instância 225 e o piloto da Entrega 01 ficam como referência histórica até a recomendação desta investigação.

## Escopo

- Entender a estrutura do projeto Playwright, seus pontos de entrada, configuração de ambiente, seed, fixtures, manifesto e isolamento por worker.
- Analisar todos os requisitos do PDF do TR (1.1–1.43) e distinguir o que pode ser coberto por automação funcional/dados de teste e o que exige evidência de infraestrutura, segurança, operação ou documentação.
- Mapear individualmente CT-001–CT-038 da SGV-11971 como cobertura existente dos itens 1.24–1.25, incluindo framework/estado conhecido e dependências.
- Localizar cobertura automatizada e dados existentes para outros requisitos sem presumir que todo o catálogo do seed é necessário.
- Identificar atores, entidades, módulo/serviço, permissões, estado inicial, operações de preparação e limpeza exigidas por cada CT/grupo.
- Comparar como a preparação e a configuração se relacionam com os ambientes atualmente usados, sem executar preparação destrutiva.
- Registrar fatos com caminho de código/documento ou execução existente; marcar explicitamente o que ainda precisa ser confirmado.
- Recomendar entregas seguintes; não abrir demandas ou pastas futuras nesta etapa.

## Fora de escopo

- Refatorar, executar ou alterar o seed.
- Criar/alterar instâncias ou dados em ambientes.
- Catalogar todas as entidades e configurações do SOGOV.
- Portar CTs, implementar cobertura funcional ou corrigir defeitos do produto.
- Declarar que o preset funciona em múltiplos ambientes sem evidência de execução.

## Critérios de aceite

- C1. O mapa do projeto explica os componentes relevantes e o caminho de uma execução Playwright até os dados preparados, com referências verificáveis. ^c1
- C2. Os requisitos do TR completo (itens 1.1–1.43 e subitens aplicáveis) estão representados na [[Matriz - Análise do preset provável]], individualmente ou em grupos justificados, com situação de cobertura e tipo de evidência; os 38 CTs existentes de 1.24–1.25 estão rastreados sem serem apresentados como cobertura total do TR. ^c2
- C3. A matriz distingue dados/estados consumidos, mecanismo atual de preparação e variação por ambiente; afirmações sem evidência estão marcadas como “a confirmar”. ^c3
- C4. O preset provável e suas lacunas estão descritos sem pressupor refatoração; as alternativas e recomendação têm justificativa ligada aos CTs. ^c4
- C5. As primeiras entregas candidatas estão ordenadas por dependência e cada uma indica CTs/resultado esperado; nenhuma demanda futura é criada nesta entrega. ^c5

## Checklist de entrega ao DEV

- [ ] Mapa técnico e matriz foram revisados contra as fontes atuais.
- [ ] Escopo, lacunas e hipóteses estão separados com clareza.
- [ ] Critérios e verificações estão vinculados.
- [ ] `pontos_alocados` foi preenchido no tracker, se aplicável.

## Pendências de decisão

- Confirmar quais ambientes/repositórios serão considerados “em uso” nesta rodada e obter evidência/configuração sem expor segredos.
- Distinguir, no TR completo, requisitos validáveis por dados/testes funcionais daqueles que dependem de evidência técnica ou operacional.
- Determinar, com base na matriz, se a próxima fatia requer alteração de seed, configuração por ambiente, isolamento/preparação por CT ou apenas documentação.
