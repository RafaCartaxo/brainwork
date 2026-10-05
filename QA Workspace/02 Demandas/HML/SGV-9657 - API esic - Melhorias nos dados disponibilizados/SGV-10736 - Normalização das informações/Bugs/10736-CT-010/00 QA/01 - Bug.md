---
prioridade: media
origem: validação
pontos_alocados: ""
---

# Bug — Total de solicitações respondidas ausente no retorno de estatísticas

> [!info]- Navegação QA/DEV
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/00 README|Abrir README do card]]
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/01 - Bug]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/04 - Validação dev]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que o endpoint de estatísticas (`GET /solicitacoes/listar-estatisticas`) não retorna o campo `status.totalAnswered` — o campo está ausente do JSON, não apenas zerado. A SGV-10736 pedia esse campo como nova informação para contabilizar solicitações com o novo status "Respondido" (C7 da demanda).

---

## Passo a passo para reproduzir

**Dado** que o cliente tenha solicitações cadastradas no módulo e-SIC
**Quando** o endpoint de estatísticas (`GET /solicitacoes/listar-estatisticas`) é consultado
**Então** verifico que `body.statistics.status` não contém a chave `totalAnswered` — só vêm `totalReceived`, `totalInProgress` e `totalClosed`

---

## Evidências [🔍](evidencia://bug-esic-totalanswered-ausente)

Retorno real em homologação, cliente `prefeitura-de-cuite`:

```json
GET https://homolog.sogov.com.br/api-dev/solicitacoes/listar-estatisticas

"status": {
    "totalReceived": 0,
    "totalInProgress": 0,
    "totalClosed": 24
}
```

Campo `totalAnswered` esperado (conforme `novo-estatistica.json`, Retornos esperados) não aparece em nenhum lugar do objeto `status`.

---

## Resultado Esperado

Conforme a Demanda (SGV-10736, critério C7) e o retorno esperado (`novo-estatistica.json`): `statistics.status.totalAnswered` deve estar presente, contando as solicitações com `orderStatus` "Respondido".

---

## Critérios de aceite

- [ ] `statistics.status.totalAnswered` está presente no retorno
- [ ] O valor de `totalAnswered` corresponde à quantidade real de solicitações respondidas
- [ ] Os demais contadores de status (`totalReceived`, `totalInProgress`, `totalClosed`) permanecem corretos após a correção

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

> **Pendência:** sem SGV cadastrado no Notion ainda — obter o número e renomear (card, evidência, wikilinks, daily) quando chegar.
