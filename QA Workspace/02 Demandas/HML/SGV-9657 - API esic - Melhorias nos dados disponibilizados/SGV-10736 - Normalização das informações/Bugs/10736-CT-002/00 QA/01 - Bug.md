---
prioridade: media
origem: validação
pontos_alocados: ""
---

# Bug — Tipo do solicitante não vem por extenso na listagem

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[01 - Bug]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que o endpoint de listagem (`GET /solicitacoes/listar-documentos`) retorna `requester.type` abreviado (`"PF"`/`"PJ"`), enquanto o endpoint de estatísticas (`GET /solicitacoes/listar-estatisticas`) retorna o mesmo conceito por extenso (`"Pessoa Física"`/`"Pessoa Jurídica"`) em `rankingRequesters[].type`. O retorno esperado atualizado (`novo-estatistica-atualizado.txt`) confirma o padrão por extenso como o esperado.

---

## Passo a passo para reproduzir

**Dado** que exista uma solicitação de um solicitante Pessoa Física ou Jurídica
**Quando** a listagem de solicitações (`GET /solicitacoes/listar-documentos`) é consultada
**Então** verifico que `requester.type` vem abreviado (`"PF"`/`"PJ"`), diferente do padrão por extenso usado pelas estatísticas

---

## Evidências [🔍](evidencia://bug-esic-tipo-abreviado-listagem)

Retorno real em homologação, cliente `prefeitura-de-cuite`:

```json
GET https://homolog.sogov.com.br/api-dev/solicitacoes/listar-documentos?page=1&itemsPerPage=10
"requester": { "id": 36060, "type": "PF", ... }
"requester": { "id": 9679, "type": "PJ", ... }
```

```json
GET https://homolog.sogov.com.br/api-dev/solicitacoes/listar-estatisticas
"rankingRequesters": [{ "id": 9679, "name": "Sem Nome", "type": "Pessoa Jurídica", ... }]
```

Retorno esperado atualizado (`Retornos esperados (novos)/novo-estatistica-atualizado.txt`), recebido em 05/10/2026, confirma o padrão por extenso: `"type": "Pessoa Física"` em `rankingRequesters`. O retorno esperado da listagem (`novo-documentos-atualizado.txt`) não tem exemplo preenchido de `type` (só o caso anônimo, `type: null`) — não dá pra confirmar diretamente por lá, mas o padrão das estatísticas e a confirmação do Rafael indicam que a listagem deve seguir o mesmo formato.

---

## Resultado Esperado

`requester.type` na listagem retorna por extenso (`"Pessoa Física"`/`"Pessoa Jurídica"`), no mesmo padrão já usado pelo endpoint de estatísticas.

---

## Critérios de aceite

- [ ] `requester.type` na listagem vem por extenso, igual ao padrão das estatísticas
- [ ] Nenhuma regressão no restante do bloco `data` (`individualPerson`/`legalPerson`) associado ao solicitante

---

## Checklist de entrega ao DEV

- [x] Sintoma, ambiente e passos de reprodução estão claros.
- [x] Resultado esperado está definido.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

> **Fechado por transferência (05/10/2026):** a correção virou o critério C14 da SGV-10735 (Parte 2) — reteste acontece por lá, não aqui. Sem SGV próprio necessário.
