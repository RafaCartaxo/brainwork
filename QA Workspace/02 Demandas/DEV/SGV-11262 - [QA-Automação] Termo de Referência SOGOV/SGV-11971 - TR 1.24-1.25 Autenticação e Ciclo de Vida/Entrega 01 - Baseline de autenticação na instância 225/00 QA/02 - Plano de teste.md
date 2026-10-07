---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — Entrega 01

> [!info]- Navegação QA
> **README:** [[00 README]]
> **Demanda:** [[01 - Demanda]]
> **Casos:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Automação:** [[../01 Automação/00 - Automação|Pacote de automação]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

## Objetivo

Verificar que o seed seleciona com segurança a instância 225 quando configurado, mantém o comportamento padrão sem override e prepara os atores de autenticação de forma repetível.

## Riscos e escopo

- **Risco principal:** o seed atual pode criar E2E Automatic Test em vez de usar a 225.
- **Risco adicional:** a configuração local pode apontar para outro backend; o ID 225 pode existir noutro ambiente ou estar indisponível para autenticação.
- **Fora do escopo:** validar a implantação completa do cliente, os módulos do roteiro e os 25 CTs restantes da SGV-11971.

## Estratégia de teste

- Revisão/unitário do seletor de alvo: ID ausente, ID encontrado e nome divergente.
- Integração com a API do ambiente: confirmar que ID 225 resolve para o nome esperado antes de provisionar.
- Reexecução do seed: duas rodadas no mesmo backend; comparar ID de instância, identidade dos atores e manifesto.
- Regressão limitada: sem override, preservar o caminho padrão do seed. Não executar a suíte completa apontada à 225.
- Validação funcional: executar apenas CT-001–012 e CT-038 contra a instância 225 depois da preparação.
- Não alterar nem limpar dados da instância 225 manualmente durante a validação; registrar os efeitos do seed.

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-seed-001|SEED-001]] | Configuração do alvo | Unidade/API | Planejada | [[04 - Validação dev]] |
| [[03 - Casos de teste#^ct-seed-002|SEED-002]] | Fail-closed | Unidade/API | Planejada | [[04 - Validação dev]] |
| [[03 - Casos de teste#^ct-seed-003|SEED-003]] | Regressão do padrão atual | Unidade/API | Planejada | [[04 - Validação dev]] |
| [[03 - Casos de teste#^ct-seed-004|SEED-004]] | Idempotência/manifesta | API | Planejada | [[04 - Validação dev]] |
| CT-001–012, CT-038 da SGV-11971 | Funcional | API | Playwright existente | [[../01 Automação/02 - Validação automação]] |

## Entrada e saída

**Entrada:** alteração revisada; URL de ambiente confirmada; instância 225 acessível; destino do código CT-038 resolvido ou marcado como bloqueio explícito.

**Saída:** evidência de seleção correta, proteção contra alvo incorreto, preservação do padrão, idempotência e resultados por CT da cobertura funcional.

