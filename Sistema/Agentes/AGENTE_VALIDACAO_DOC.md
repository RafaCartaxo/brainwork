---
tags:
  - sistema
  - agentes
---
# AGENTE_VALIDACAO_DOC

Rede de segurança do **gate de verificação contra doc** ([[../Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]). Varre a daily/cards em busca de demandas marcadas como aprovadas **sem** o cruzamento contra a doc do módulo registrado, e levanta a pendência — pra não repetir o caso da SGV-9464 (aprovada e só depois descoberta a divergência com a doc).

Não faz integração externa nem roda por conta própria em background: dispara no gatilho **já existente** de organização da daily.

## Gatilho

| Gatilho | Quando |
|---|---|
| 🔄 Atualizar (Dashboard) / "organiza a daily" (IA) | junto do [[AGENTE_ORGANIZADOR]], na varredura da daily |

## Fonte

- Daily mais recente (Atividades → HML/DEV, fila) e cards em `QA Workspace/02 Demandas/` marcados `✅ aprovado` / movidos pra `Concluídas` recentemente.
- A doc do módulo em `QA Workspace/04 Conhecimento/Módulos/<Módulo>.md`.

## Regras

1. Para cada card **aprovado** (ou movido pra `Concluídas`) que ainda **não** tem registro do gate de doc — nem no card (Observações/Histórico), nem em `## Comportamentos observados em teste` da doc do módulo, nem anotação `[IA]` na daily — levantar pendência `⏳` na fila:
   `⚠️ SGV-XXXX × doc <Módulo> — cruzar contra a doc (gate pendente)`, e espelhar em **Travas** do Status—reunião.
2. Se a doc do módulo **não existe**, a pendência vira `Importar doc de <Módulo> (fluxo 8)` — não deixar lacuna silenciosa.
3. Se o gate **já** foi registrado (veredito ✅/⚠️/❓ presente), não repetir — só confirmar que divergências `⚠️` em aberto seguem com dono/decisão de Produto na fila.
4. Não decide nem edita a doc: apenas **sinaliza**. A resolução é humana/skill (ver [[../Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]] seções 4–5).

## Resultado

Pendências de gate registradas na fila + Travas, e uma linha no bloco recolhido `[!organizacao]- Auto-organização` da daily listando quais cards aprovados estavam sem o cruzamento contra a doc.
