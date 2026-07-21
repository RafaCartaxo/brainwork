---
tags:
  - qa
  - refinamento
task: "9464"
status: refinado
data_inicio: 2026-07-21
data_fim: 2026-07-21
responsavel: Rafael
modulo: Rastrear Documento
---
# Refinamento: Ao realizar novo rastreio de documentos, filtros não são reiniciados

> [!info]- Mesa de trabalho — [[Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada (Notion → vault)|fluxo 6]]
> Análise e suposição vivem aqui — o card em `02 Demandas/` nasce do **Destilado**, limpo. Ao concluir: análise → Notion (`📤`), card criado (`📝`), este arquivo → `04 Conhecimento/` (`status: refinado`).

## O problema (task no Notion)

**Descrição** (Rafael Borges) — Ao utilizar a funcionalidade de rastreamento de documentos e aguardar o carregamento dos resultados, em seguida aplicar filtros na tela de resultados (como "Documentos pausados" e "Documentos encerrados") e realizar um novo rastreamento, verifica-se que ao término do carregamento da nova consulta os filtros aplicados anteriormente permanecem selecionados, não sendo reiniciados automaticamente pelo sistema.

**Saída esperada** — Ao iniciar um novo rastreio de documentos, os filtros aplicados na consulta anterior devem ser reiniciados automaticamente. *(Não veio explícita na task; extraída do título e da entrega do dev — confirmada pela validação em homologação: filtros reiniciam ao novo rastreio.)*

**Saída atual** — Após um novo rastreio, os filtros da busca anterior permanecem selecionados; o sistema não os reinicia ao fim do carregamento da nova consulta.

**Entrega do dev** (João Marcelo, 09/07 — [MR !553](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/553), aprovado pra teste; aprovado em DEV por Lucas Beninca em 15/07) — Ao detectar novo rastreio (`location.search` muda), zera `statusFilter` e `importedDocuments`. `searchItems` passa a aceitar overrides explícitos (status, imported) pra a busca inicial não depender do estado antigo. Ajuste de tipo: `statusFilter` de `[]` para `{}` (objeto), como já era usado no código. Arquivo: `web/src/components/ListTrackedDocuments/ListTrackedDocuments.tsx`. Tela impactada: `/cliente/clientId/documentos-rastreados`. Sem endpoint impactado.

---

## Análise

- **Causa raiz**: o estado dos filtros da tela de resultados (`statusFilter`, `importedDocuments`) não era reiniciado ao disparar um novo rastreio — a nova consulta herdava os filtros da consulta anterior. Correção do MR !553: ao mudar `location.search` (novo rastreio), zerar `statusFilter` e `importedDocuments`; `searchItems` passa a aceitar overrides explícitos pra a busca inicial não depender do estado antigo.
- **Evidências**: validação em homologação gravada — [[9464 - filtros reiniciados ao realizar novo rastreio aprovado em homologacao.mp4]] (Evidências/Homologação/). Descrição técnica no MR !553.
- **Hipóteses descartadas**: —

---

## Pontos a definir

- [x] ~~Critérios de aceite ausentes na task~~ → definidos e confirmados na validação: (1) ao iniciar novo rastreio, os filtros da consulta anterior voltam ao estado inicial; (2) o resultado exibido corresponde à nova consulta sem filtro residual.
- [x] ~~Resultado esperado ausente na task~~ → "reiniciar filtros" confirmado; escopo cobre `statusFilter` (pausados/encerrados) e `importedDocuments`, conforme MR !553.
- [x] ~~Sem evidência no export~~ → gravada validação em homologação (aprovada) e embedada no card.
- [x] ~~Escopo dos filtros~~ → o MR zera `statusFilter` e `importedDocuments`; validação em homologação aprovou o reinício dos filtros ao novo rastreio.

> [!warning] Divergência doc × bug (aberta — decisão de produto)
> A doc [[Módulos/Rastrear Documento|Rastrear Documento]] descreve "Novo rastreio" como "recomeça do zero **mantendo os resultados anteriores visíveis ao fundo**" e não menciona reinício de filtros. O bug SGV-9464 + MR !553 tratam a permanência dos filtros como defeito a corrigir. Com a aprovação do bug, o comportamento agora especificado é **reiniciar os filtros**. Confirmar com produto se a linha da doc está desatualizada (fonte Notion editada em 25/03; bug/MR de 09/07) e, se sim, atualizar a doc do módulo + registrar em "Comportamentos observados em teste". Não editado aqui: é decisão de produto, não suposição.

---

## Destilado (rascunho do card)

> [!abstract] Só o problema — o que vai pro card, quase copy-paste: Descrição objetiva, passo a passo, resultado esperado, critérios de aceite, CTs. Nada de análise ou suposição.

### Descrição

Após aplicar filtros na tela de resultados do rastreamento de documentos (ex.: "Documentos pausados", "Documentos encerrados") e realizar um novo rastreio, os filtros aplicados anteriormente permanecem selecionados, não sendo reiniciados automaticamente ao término do carregamento da nova consulta.

### Passo a passo para reproduzir

Dado que o usuário realizou um rastreamento e aplicou filtros na tela de resultados
Quando realiza um novo rastreamento
Então, ao término do carregamento, os filtros anteriores permanecem selecionados

### Resultado Esperado

Ao iniciar um novo rastreio, os filtros da consulta anterior são reiniciados automaticamente e o resultado corresponde à nova consulta sem filtro residual.

### Critérios de aceite

- [x] Ao iniciar novo rastreio, os filtros da consulta anterior voltam ao estado inicial
- [x] O resultado exibido corresponde à nova consulta, sem filtro residual

### Casos de Teste Básicos

- **CT-B01 Filtros são reiniciados ao realizar novo rastreio** — Dado filtros aplicados na consulta anterior, quando realiza novo rastreio, então os filtros voltam ao estado inicial e o resultado corresponde à nova consulta.

---

## Histórico do refinamento

- 2026-07-21 - Material recebido (export do Notion) e organizado na mesa. Task tem descrição e passo a passo claros e entrega do dev com MR aprovado em DEV, mas **sem** resultado esperado, critérios de aceite nem evidência — por isso entrou na mesa (modo A) em vez de card direto. 4 gaps mapeados em Pontos a definir.
- 2026-07-21 - 📝 Destilado fechado e card criado em [[../02 Demandas/Concluídas/9464 - Bug Filtros Nao Reiniciados Novo Rastreio|02 Demandas/Concluídas/9464]]. 4 Pontos a definir resolvidos pela validação em homologação (critérios, resultado esperado, escopo dos filtros e evidência confirmados). Demanda simples validada e aprovada direto em homologação.
- 2026-07-21 - ✅ Aprovada em homologação. Mesa arquivada em `04 Conhecimento/` (`status: refinado`). Ciclo do fluxo 6 concluído. Divergência doc × bug ("Novo rastreio" mantém estado vs. reinicia filtros) permanece aberta como decisão de produto.
