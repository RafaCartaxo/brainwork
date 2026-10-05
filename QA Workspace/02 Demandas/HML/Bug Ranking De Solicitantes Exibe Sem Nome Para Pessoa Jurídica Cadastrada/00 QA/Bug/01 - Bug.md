---
prioridade: media
origem: validação
pontos_alocados: ""
---

# Bug — Ranking de solicitantes exibe "Sem Nome" para Pessoa Jurídica cadastrada

> [!info]- Navegação QA/DEV
> **README do card:** [[../00 README|Abrir README do card]]
> **Bug:** [[01 - Bug]]
> **Casos de teste:** [[../03 - Casos de teste]]
> **Validação:** [[../04 - Validação dev]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que o endpoint de estatísticas (`GET /solicitacoes/listar-estatisticas`) exibe `"name": "Sem Nome"` em `rankingRequesters` para um solicitante Pessoa Jurídica que tem razão social cadastrada — confirmado ao cruzar o `id` do ranking com o mesmo `id` na listagem de solicitações, que retorna o nome correto. O `id` em si bate entre os dois endpoints (correto), só o nome não é resolvido pra PJ.

---

## Passo a passo para reproduzir

**Dado** que exista um solicitante Pessoa Jurídica com razão social cadastrada, com solicitações suficientes para aparecer no ranking
**Quando** o endpoint de estatísticas (`GET /solicitacoes/listar-estatisticas`) é consultado
**Então** verifico que `rankingRequesters` traz esse solicitante com `"name": "Sem Nome"`, apesar de ter razão social cadastrada (confirmável pelo mesmo `id` na listagem de solicitações)

---

## Evidências [🔍](evidencia://bug-esic-ranking-sem-nome-pj)

Retorno real em homologação, cliente `prefeitura-de-cuite`:

```json
GET https://homolog.sogov.com.br/api-dev/solicitacoes/listar-estatisticas
"rankingRequesters": [
  { "id": 9679, "name": "Sem Nome", "type": "Pessoa Jurídica", "ordersPerPage": 1 }
]
```

```json
GET https://homolog.sogov.com.br/api-dev/solicitacoes/listar-documentos?page=1&itemsPerPage=10
{
  "requester": { "id": 9679, "type": "PJ", "data": { "legalPerson": { "companyName": "INSTITUTO NACIONAL DO SEGURO SOCIAL" } } },
  "protocolNumber": "000015/2026"
}
```

Mesmo `id` (9679), mesma quantidade de solicitações (1, batendo `ordersPerPage` com a solicitação da listagem) — só o `name` do ranking não reflete a razão social cadastrada.

Outros 2 solicitantes do ranking também aparecem como "Sem Nome" com `type: "Pessoa Jurídica"` (ids 8540 e 14098) — suspeita de que o problema afete todo solicitante PJ no ranking, não só este caso, mas só confirmado para o `id: 9679` (único cruzado com a listagem até agora).

---

## Resultado Esperado

`rankingRequesters[].name` deve trazer a razão social cadastrada do solicitante Pessoa Jurídica, no mesmo padrão já usado na listagem de solicitações (`legalPerson.companyName`) — não "Sem Nome" quando há cadastro.

---

## Critérios de aceite

- [ ] `rankingRequesters[].name` traz a razão social para solicitante Pessoa Jurídica com cadastro completo
- [ ] `rankingRequesters[].name` continua trazendo o nome completo para solicitante Pessoa Física (sem regressão)
- [ ] "Sem Nome" continua aparecendo apenas quando o solicitante realmente não tem nome/razão social cadastrado (ex.: solicitação anônima)

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

> **Pendência:** sem SGV cadastrado no Notion ainda — obter o número e renomear (card, evidência, wikilinks, daily) quando chegar. Confirmar também se os outros 2 "Sem Nome" do ranking (ids 8540, 14098) são o mesmo bug, cruzando com a listagem completa (ainda só vimos a 1ª página de 10).
