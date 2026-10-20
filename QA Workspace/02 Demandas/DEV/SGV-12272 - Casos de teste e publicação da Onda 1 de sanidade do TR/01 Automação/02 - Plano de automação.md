---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-test"
status: planejado
---

# Plano de automação — SGV-12272 · Onda 1

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Automação:** [[00 - Automação]]
> **Análise:** [[01 - Análise]]
> **Validação automação:** [[03 - Validação automação]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> [!warning] Aguardando o gate da Análise
> O plano **não foi preenchido**: a validação manual dos 20 CTs ainda não foi feita (ver [[../00 QA/04 - Validação dev]]) e a [[01 - Análise|Análise]] tem pendências de decisão abertas. Preencher só depois do gate **"pronto para planejar"** da Análise.

> Este plano registra o escopo, a estratégia e as dependências antes da implementação. Mantenha as decisões curtas e ligadas aos CTs; o andamento geral fica em [[00 - Automação]] e os resultados executados ficam em [[03 - Validação automação]].

## Objetivo e escopo

- **Objetivo:** <comportamento que a automação vai cobrir>
- **CTs incluídos:** <suítes/CTs vinculados à nota de casos de teste; o recorte da onda está na [[01 - Análise|Análise]]>
- **Fora do escopo:** <exclusões importantes ou “nenhum”>

## Estratégia por suíte

| Suíte / CTs | Camada | Dados e estado inicial | Reuso / mudança necessária | Dependência ou gate |
|---|---|---|---|---|
| <suíte e links aos CTs> | <API / E2E> | <ver tabela **Massa desta entrega** em [[01 - Análise#Massa desta entrega\|01 - Análise]]: recurso e dono; aqui só a preparação e a limpeza específicas do teste> | <código existente a reutilizar ou mudança necessária> | <captura, acesso, fix no ambiente ou nenhuma> |

> Uma linha por suíte ou grupo de CTs com a mesma estratégia. Não replique aqui os passos e asserts dos casos de teste.

## Pronto para codar quando

- [ ] CTs e comportamento esperado estão definidos em `../00 QA/03 - Casos de teste`.
- [ ] Validação manual e disponibilidade do comportamento no ambiente-alvo foram confirmadas, conforme aplicável.
- [ ] Dados, estado inicial e forma de isolamento/preparação estão definidos e registrados na tabela **Massa desta entrega** da [[01 - Análise|Análise]].
- [ ] Dependências que impedem a implementação foram resolvidas ou os CTs afetados foram explicitamente retirados do escopo desta rodada.

## Pronto para validar quando

- [ ] Implementação concluída e CTs mapeados aos testes no repo.
- [ ] Ambiente e instruções de execução confirmados.

---

**Execução direta:** se não houver escolha técnica ou preparação especial, preencher a tabela com a camada escolhida, reuso disponível e “nenhuma” dependência. O plano continua sendo criado; não precisa crescer para justificar sua existência.
