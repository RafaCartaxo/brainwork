---
tags:
  - qa
  - inbox
---
# 00 Inbox

Backlog de melhorias do **próprio vault/ferramenta** (QA Workspace). Não é lugar de captura do dia a dia — anotações, bugs e ideias entram na **daily do dia**, e o auto-organizador roteia depois (ver fluxograma na [[Dashboard]] e lógica em [[QA Workspace/Sistema/Skills/SKILL_INBOX|SKILL_INBOX]]).

> [!note] Capturas legadas
> Arquivos de captura soltos que ainda existirem nesta pasta (formato antigo, com `status: pendente`) continuam sendo processados pelo auto-organizador até zerarem. Não criar capturas novas aqui.

## Próximos passos — Central de Operações

Ideia: uma central de operações única, onde dá pra trabalhar a partir de um local só (página inicial), criar bugs e anotações que se organizem automaticamente com as referências corretas. O ato de testar continua manual por enquanto — atenção a esse ponto.

- [x] Dashboard central com KPIs e navegação — ver [[Dashboard]]
- [x] Auto-organização das anotações soltas nas referências corretas — implementado em 14/07: a daily virou o lugar único de escrita e o organizador roteia de lá (ver [[QA Workspace/Sistema/Skills/SKILL_INBOX|SKILL_INBOX]] e [[QA Workspace/Sistema/Specs/2026-07-14-inbox-auto-organizacao-design|spec]])
- [x] Esteira prática por etapa da demanda (o que fazer em DEV, o que fazer em HML etc.), disparável a partir da Dashboard — implementado em 14/07 como passo a passo em [[QA Workspace/Sistema/Contexto/FLUXOS|FLUXOS]], linkado na navegação e na regra de bolso da Dashboard
- [ ] Template + skill de Sanidade — precisa mapear roteiros de execução reais e ser pensado pra automação, não é só um template solto. Vai exigir mais tempo/planejamento.
- [ ] Organizar vídeos de evidência soltos/inconsistentes: gravações cruas do OBS sem pasta/nome padrão na raiz de `Evidências/` (atualmente `2026-07-15 13-46-02.mp4` e `2026-07-15 14-12-11.mp4`) pilha de 4 vídeos com nomes inconsistentes pro SGV-9237 em `Evidências/Homologação/`, e vídeos sem descrição/sem card conhecido em `Evidências/Desenvolvimento/` (`5016.mp4`, `7640 - nOK.mp4`)
