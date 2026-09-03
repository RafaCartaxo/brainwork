---
tags:
  - qa
  - conhecimento
tipo: indice
---
# SGV-9296 — Departamentos de cidadão PJ (epic)

Task guarda-chuva do Notion que agrupa as duas partes da funcionalidade de departamentos vinculados a cidadãos Pessoa Jurídica. Sem card/CTs próprios — a validação acontece pelas partes.

## Partes

| Parte | SGV | O que é | Status |
|---|---|---|---|
| 1 | [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ\|SGV-11083]] | Criação, edição, exclusão, suspensão e gerenciamento de membros do departamento | Refinada, aberta em DEV — 33 CTs, 1 ponto em aberto (contagem de participantes, aguardando Produto) |
| 2 | [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos\|SGV-11184]] | Encaminhar documentos/despachos pro departamento, notificações e rastreabilidade de visualização externa | Refinada, aberta em DEV — 22 CTs, sem pontos em aberto |

## Dependência entre as partes

A Parte 2 (11184) depende funcionalmente da Parte 1 (11083): precisa existir departamento (com participantes e status ativo/suspenso definidos) antes de testar encaminhamento. Recomendado validar a 11083 primeiro, ou em paralelo com massa de dados compatível.

## Mesas de refinamento

- [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11083/SGV-11083 - Refinamento Departamentos Para Cidadao PJ|SGV-11083 - Refinamento]]
- [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11184/SGV-11184 - Refinamento Departamentos Encaminhar Documentos E Despachos|SGV-11184 - Refinamento]]

## Contexto de apoio (não é fonte de critério de aceite)

Documento de produto consolidado do Notion ("Departamento CNPJ") cobre esta epic **e outras 3 tasks** (SGV-8883, 8884, 9898) numa visão única de produto — usado nas duas mesas só como esclarecimento de detalhe (limites de campo, fluxo de convite, formato de exibição), nunca como origem de critério.
