---
tags:
  - qa
  - inbox
---
# 00 Inbox

Backlog de melhorias do **próprio vault/ferramenta** (QA Workspace). Não é lugar de captura do dia a dia — anotações, bugs e ideias entram na **daily do dia**, e o auto-organizador roteia depois (ver fluxograma na [[Dashboard]] e lógica em [[Sistema/Skills/SKILL_INBOX|SKILL_INBOX]]).

> [!note] Capturas legadas
> Arquivos de captura soltos que ainda existirem nesta pasta (formato antigo, com `status: pendente`) continuam sendo processados pelo auto-organizador até zerarem. Não criar capturas novas aqui.

## Próximos passos — Roadmap de melhorias do vault

Ideia: uma central de operações única, onde dá pra trabalhar a partir de um local só (página inicial), criar bugs e anotações que se organizem automaticamente com as referências corretas. O ato de testar continua manual por enquanto — atenção a esse ponto.

### ✅ Concluído
- [x] Dashboard central com KPIs e navegação — ver [[Dashboard]]
- [x] Auto-organização das anotações soltas nas referências corretas — implementado em 14/07: a daily virou o lugar único de escrita e o organizador roteia de lá (ver [[Sistema/Skills/SKILL_INBOX|SKILL_INBOX]] e [[Sistema/Specs/2026-07-14-inbox-auto-organizacao-design|spec]])
- [x] Esteira prática por etapa da demanda (o que fazer em DEV, o que fazer em HML etc.), disparável a partir da Dashboard — implementado em 14/07 como passo a passo em [[Sistema/Contexto/FLUXOS|FLUXOS]], linkado na navegação e na regra de bolso da Dashboard

### 🔴 Agora
- [x] Criar `opencode.json` como índice de contexto do vault (sem duplicar agentes/skills — o vault é a fonte única de verdade)
- [x] Mapear [[Sistema/Agentes/AGENTE_ORGANIZADOR|AGENTE_ORGANIZADOR]] como comando `/organiza-daily` no opencode (junto com `/processa-export` e `/status-reuniao`)

### 🟡 Em breve
- [x] [[Sistema/Skills/SKILL_MELHORIA|SKILL_MELHORIA]] — ciclo completo do fluxo 4 (checklist → refinar → card → Notion → esteira normal)
- [x] Expandir [[Sistema/Agentes/AGENTE_VALIDACAO_DOC|AGENTE_VALIDACAO_DOC]] — detecção automática de módulo e integração com Travas do Status — reunião
- [x] Agentes reconhecerem "aguardando deploy" (Fase 2) — AGENTE_MIGRACAO_CARDS, AGENTE_ORGANIZADOR e AGENTE_FILA
- [ ] Avaliar viabilidade de MCP Notion pra sincronização bidirecional (hoje tudo manual: cadastrar, renomear, atualizar)

### 🟢 Um dia
- [ ] Graduação automática Estudos → Conhecimento — agente que detecta maturidade, move o arquivo e cria cross-links
- [ ] Documentar procedimento de recovery pra falha na migração atômica de cards ([[Sistema/Agentes/AGENTE_MIGRACAO_CARDS|AGENTE_MIGRACAO_CARDS]])
- [ ] Diff incremental no [[Sistema/Agentes/AGENTE_STATUS_REUNIAO|AGENTE_STATUS_REUNIAO]] — cache da última geração pra destacar mudanças na reunião
- [ ] Template + skill de Sanidade — precisa mapear roteiros de execução reais e ser pensado pra automação, não é só um template solto. Vai exigir mais tempo/planejamento.

### ⏸️ Congelado (sem necessidade atual)
- [ ] Organizar vídeos de evidência soltos/inconsistentes: gravações cruas do OBS sem pasta/nome padrão na raiz de `Evidências/` (atualmente `2026-07-15 13-46-02.mp4` e `2026-07-15 14-12-11.mp4`) pilha de 4 vídeos com nomes inconsistentes pro SGV-9237 em `Evidências/Homologação/`, e vídeos sem descrição/sem card conhecido em `Evidências/Desenvolvimento/` (`5016.mp4`, `7640 - nOK.mp4`)
