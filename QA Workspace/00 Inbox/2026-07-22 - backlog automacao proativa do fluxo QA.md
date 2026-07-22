---
tags:
  - qa
  - inbox
  - backlog
data: 2026-07-22
---
# Backlog — automação proativa do fluxo QA (fora do escopo atual)

Levantado na auditoria de ponta-a-ponta do fluxo (22/07). A **costura da cadeia** (handoffs explícitos, gate de doc, `SKILL_REFINAMENTO`, `AGENTE_VALIDACAO_DOC`) foi feita. Estes itens são **infra proativa** — deixados pra depois por exigirem integração externa / cron / monitoramento, fora do "contexto atual":

- **Detecção automática de export novo** — hoje o `.md` do Notion fica no `~/Downloads` até alguém chamar o [[../../Sistema/Agentes/AGENTE_PROCESSAR_EXPORT|AGENTE_PROCESSAR_EXPORT]]. Um watcher/hook reduziria a latência.
- **`AGENTE_MR_MERGED`** — detectar MR mergeado (webhook/cron GitLab) e disparar revisão de escopo + preparar automação. Evita MRs ficarem "acompanhando" na fila por dias.
- **`AGENTE_HEALTH_AMBIENTE`** — rastrear qual build está em HML e alertar quando um card espera por fix que ainda não chegou (casos SGV-6906 / SGV-7371 / gate 2 da automação).
- **SLA/escalonamento de mesa de refinamento** — alerta intermediário (3–5 dias) antes do zumbi de 7d, pra mesa parada não sumir do radar.
- **Template obrigatório de "Plano de Automação"** — padronizar formato/localização (hoje é livre; a 9610 ficou em `04 Conhecimento/`).

Referência: auditoria e decisões em `~/.claude/plans/` (sessão 22/07) — escopo escolhido foi "costurar a cadeia + poucos skills/agentes, dentro do contexto atual".
