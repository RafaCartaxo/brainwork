---
tags:
  - qa
  - conhecimento
tipo: referencia
revisado: 2026-07-17
---
# Docs do repositório Sogov

Mapa da documentação que já existe dentro do repo de código (`~/Documentos/Sogov/Sogov-application/docs/`) — fonte primária pra importar conhecimento pra cá sem duplicar.

## O que tem lá

| Caminho | Conteúdo | Interesse pra QA |
|---|---|---|
| `docs/contexto/api.md` | Contexto da API | Entender onde as regras vivem no backend |
| `docs/contexto/web.md` | Contexto do frontend | Mapear telas ↔ módulos |
| `docs/contexto/fluxos.md` | Fluxos do sistema | Base pras notas de `Fluxos/` daqui |
| `docs/contexto/servicos-externos.md` | Integrações externas | Riscos de teste que dependem de terceiros |
| `docs/usecases/dispatch/` | Casos de uso de despachos | Regras de despacho |
| `docs/usecases/document-event/` | Eventos de documento | Estados/transições de documento |
| `docs/usecases/document-object/` | Objeto documento | Estrutura e regras do documento |
| `docs/usecases/download/` | Download | Regras de download (relevante pra demanda TCE-PE) |
| `docs/usecases/notification/` | Notificações | Gatilhos de notificação |
| `docs/usecases/signature/` | Assinatura | Regras de assinatura |
| `docs/testes/` | Fluxo de correção de bug, mocks e factories | Processo dev de bugfix — útil pra entender o ciclo |

## Como importar

Ao estudar um desses arquivos, criar a nota do módulo/fluxo correspondente em [[../README|04 Conhecimento]] com o template Conhecimento.md, resumindo **só o que ajuda a testar** e linkando o caminho do arquivo aqui do repo como fonte.

## Dúvidas em aberto
- [ ] `docs/plan/` está vazio — confirmar se é usado pra algo
