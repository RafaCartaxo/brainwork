---
prioridade: media
origem: validação
pontos_alocados: ""
---

# Bug — Data limite da solicitação não é calculada quando não há prazo configurado

> [!info]- Navegação QA/DEV
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/00 README|Abrir README do card]]
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/04 - Validação dev]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que o campo `orderDateDeadline` da listagem de solicitações sempre retorna `null`, inclusive para solicitações sem prazo de atendimento configurado — cenário em que a SGV-10736 pedia explicitamente que a API calculasse e retornasse uma informação de prazo mesmo sem configuração (C5 da demanda).

---

## Passo a passo para reproduzir

**Dado** que exista uma solicitação sem prazo de atendimento configurado
**Quando** a listagem de solicitações (`GET /solicitacoes/listar-documentos`) é consultada
**Então** verifico que `orderDateDeadline` vem `null`, sem `date`/`days`/`type` calculados

---

## Evidências [🔍](evidencia://bug-esic-deadline-null)

Retorno real em homologação, cliente `prefeitura-de-cuite` (10/10 registros da primeira página, todos com o mesmo padrão):

```json
GET https://homolog.sogov.com.br/api-dev/solicitacoes/listar-documentos?page=1&itemsPerPage=10

"orderDateDeadline": null
```

Confirmado também pelas estatísticas do mesmo cliente (`GET /solicitacoes/listar-estatisticas`): `deadline.timely: 0, delayed: 0, undefined: 24` — as 24 solicitações do cliente caem inteiramente em "undefined", consistente com `orderDateDeadline` nunca calculado.

---

## Resultado Esperado

Conforme a Demanda (SGV-10736, critério C5) e o retorno esperado (`novo-documentos.json`): `orderDateDeadline` deve vir preenchido com `date`, `days` e `type`, calculados a partir de uma regra padrão, mesmo quando a solicitação não tiver prazo configurado — permitindo saber se está dentro ou fora do prazo independente de configuração.

> [!warning] Pendência confirmada em call (05/10/2026)
> O comportamento está confirmado como real pelo time. Falta decisão de produto: **qual valor usar quando não há prazo configurado** (data de referência, regra de cálculo) — responsabilidade do Marcos, em SGV-12019 (Parte 3, ainda vazia). Bug segue aberto até essa decisão vir e ser implementada.

---

## Critérios de aceite

- [ ] `orderDateDeadline` vem preenchido (não nulo) em toda solicitação, com ou sem prazo configurado
- [ ] O fluxo de solicitações com prazo configurado permanece íntegro após a correção

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

> **Pendência:** sem SGV cadastrado no Notion ainda — obter o número e renomear (card, evidência, wikilinks, daily) quando chegar.
