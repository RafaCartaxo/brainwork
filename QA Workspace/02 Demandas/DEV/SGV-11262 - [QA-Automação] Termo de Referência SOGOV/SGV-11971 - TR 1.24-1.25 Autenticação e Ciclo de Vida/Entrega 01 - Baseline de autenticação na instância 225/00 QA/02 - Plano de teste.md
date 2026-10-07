---
demanda: "[[01 - Demanda]]"
status: planejado
responsavel: ""
pontos: ""
---

# Plano de teste — Entrega 01

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** Não se aplica nesta entrega.
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Verificar a seleção segura da instância 225 pelo seed, a preservação do padrão existente quando não há override, a idempotência e a execução dos CTs funcionais incluídos na entrega.

## Riscos e escopo

- **Risco principal:** com o comportamento atual, o seed pode usar o perfil fixo `E2E Automatic Test` ou criar outra instância em vez de selecionar a 225.
- **Risco adicional:** a configuração pode apontar para um backend diferente daquele em que a instância 225 foi criada.
- **Fora do escopo desta rodada:** validar a implantação completa do cliente, reproduzir todos os módulos do roteiro e executar os 25 CTs funcionais restantes.

---

## Estratégia de teste

- Testar isoladamente a resolução do alvo: sem ID, ID existente e ID/nome divergente.
- Confirmar pela API que o ID 225 pertence ao backend configurado e tem o nome esperado antes de provisionar dados.
- Executar o seed duas vezes no mesmo backend e comparar instância, atores-chave e manifesto.
- Sem override, verificar que o caminho padrão das demais suítes continua preservado.
- Após a preparação, validar somente CT-001–012 e CT-038 na instância 225.
- Não limpar dados manualmente na 225 durante a validação; registrar os efeitos do seed.


---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-seed-001|SEED-001]] | Configuração do alvo | Seed/API | Prevista | [[04 - Validação dev]] |
| [[03 - Casos de teste#^ct-seed-002|SEED-002]] | Fail-closed | Unidade/API | Prevista | [[04 - Validação dev]] |
| [[03 - Casos de teste#^ct-seed-003|SEED-003]] | Regressão do alvo padrão | Unidade/API | Prevista | [[04 - Validação dev]] |
| [[03 - Casos de teste#^ct-seed-004|SEED-004]] | Idempotência e manifesto | API | Prevista | [[04 - Validação dev]] |
| CT-001–012 e CT-038 da SGV-11971 | Autenticação | API | Playwright existente | [[../01 Automação/02 - Validação automação]] |

> Replique a linha para cada CT do pacote.

---

## Entrada e saída

**Entrada:** backend confirmado; instância 225 acessível; implementação revisada; destino de CT-038 definido ou registrado como bloqueio.
**Saída:** resultados e evidências dos quatro casos técnicos e placar atualizado dos CT-001–012 e CT-038.
