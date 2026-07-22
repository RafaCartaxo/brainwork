---
tags:
  - qa
  - estudo
  - ferramentas
tipo: estudo
status: estudando
fonte: chat com Rafael (2026-07-22)
criado: 2026-07-22
revisado: 2026-07-22
---
# Ferramentas e Recursos (IA · dev · QA)

> [!info] Sobre esta nota
> Catálogo **acumulável** de ferramentas/recursos pra avaliar e, se valer, adotar. Nível-título: o que é + por que útil pra gente. Ferramenta adotada vira nota própria ou gradua pra [[../04 Conhecimento/README|04 Conhecimento]]. Novas ferramentas entram aqui embaixo, na categoria certa.

## Resumo
- Lista de tools que apareceram pra estudar/organizar o fluxo de QA/dev com IA. `status` por item: 🔎 avaliar · 🧪 testando · ✅ em uso · ❌ descartado.

## Ferramentas

### Automação & extração
- **[Browser MCP](https://browsermcp.io/)** ([repo](https://github.com/browsermcp/mcp)) — 🔎 avaliar
  MCP server + extensão Chrome que deixa a IA (Claude/Cursor/VS Code) automatizar o **seu navegador já logado**, localmente (rápido, privado, dribla detecção de bot por usar seu perfil real). Adaptado do Playwright MCP.
  **Útil pra nós:** dirigir o Sogov já logado pra reproduzir bug, preencher formulário e extrair dado sem subir browser novo; apoio a E2E dirigido por IA, complementa o repo Cypress.
- **[PageMarkdown](https://pagemarkdown.com/)** — 🔎 avaliar
  Extensão de navegador que converte página web em Markdown limpo (+ PDF/DOCX/EPUB/HTML…), por elemento (CSS selector), página ou site inteiro em ZIP. Refinamento opcional via IA.
  **Útil pra nós:** puxar documentação (Notion, manuais, docs externas) pra Markdown e jogar direto no vault — alimenta `04 Conhecimento/Referências` e esta pasta sem copiar/colar na mão.

### Skills de agente
- **[to-prd](https://www.skills.sh/mattpocock/skills/to-prd)** (mattpocock/skills) — 🔎 avaliar
  Gera um PRD estruturado a partir do contexto da conversa + codebase e publica como issue "ready-for-agent" no tracker.
  **Útil pra nós:** transformar discussão de feature/bug em requisito acionável.
  ⚠️ O CLAUDE.md do repo Sogov dizia que `to-prd` **não existia** no `mattpocock/skills` — mas o skills.sh lista. Conferir/reinstalar.
- **[handoff](https://www.skills.sh/mattpocock/skills/handoff)** (mattpocock/skills) — ✅ em uso (instalada no repo Sogov)
  Compacta o contexto da conversa num documento de handoff pra outro agente continuar sem reler tudo.
  **Útil pra nós:** continuidade entre sessões/agentes sem perder contexto.
- **[brainstorming](https://www.skills.sh/obra/superpowers/brainstorming)** (obra/superpowers) — ✅ em uso (instalada no repo Sogov)
  Força um processo de design/validação em 9 passos antes de codar (mesmo em coisa "simples").
  **Útil pra nós:** explorar requisitos/intenção antes de implementar — inclusive melhorias do próprio vault.

### Aprendizado
- **[Engram](https://github.com/nagisanzenin/engram)** — 🔎 avaliar
  "Evidence-based learning engine": transforma explicação de IA em conhecimento **retido** via tutoria estruturada + avaliação cega + revisão espaçada (algoritmo FSRS-4.5). Comandos `/learn`, `/review`, `/coach`. 100% local.
  **Útil pra nós:** estudar retendo, não só ler — casa direto com o fluxo `06 Estudos → 04 Conhecimento`; aprender conceitos de QA e domínio Sogov com repetição espaçada.

### Interface de agente de código
- **[OpenChamber](https://github.com/openchamber/openchamber)** — 🔎 avaliar
  Interface desktop/web/mobile pro agente **OpenCode**: timeline de chat com branch/undo, integração Git (commits/PRs/branches), multi-agente com worktrees isolados, voice mode, terminal integrado, PWA mobile, temas. Open-source (MIT).
  **Útil pra nós:** GUI multiplataforma pra tocar agentes de código com sessão contínua entre dispositivos; alternativa/complemento ao fluxo CLI.

## Dúvidas em aberto
- [ ] Testar **Browser MCP** logado no Sogov (DEV/HML) — reproduz bug e extrai dado de tela?
- [ ] Conferir/reinstalar **to-prd** do `mattpocock/skills` (CLAUDE.md dizia que não existia).
- [ ] Decidir se **Engram** entra oficialmente no fluxo de estudo (é o mais alinhado com esta pasta).
- [ ] **PageMarkdown** vs. captura manual — vale como pipeline padrão de import pro vault?

## Aplicação no QA / Sogov
- **Vault (este):** PageMarkdown alimenta `04 Conhecimento/Referências`; Engram sistematiza o estudo daqui.
- **Repo de automação (Cypress, `~/Documentos/Sogov/sogov-automation-test`):** Browser MCP como apoio exploratório/E2E dirigido por IA.
- **Claude Code / agentes:** to-prd, handoff, brainstorming no fluxo de refinamento→implementação; OpenChamber como GUI alternativa.

## Referências
- Browser MCP — https://browsermcp.io/ · https://github.com/browsermcp/mcp
- PageMarkdown — https://pagemarkdown.com/
- to-prd — https://www.skills.sh/mattpocock/skills/to-prd
- handoff — https://www.skills.sh/mattpocock/skills/handoff
- brainstorming — https://www.skills.sh/obra/superpowers/brainstorming
- Engram — https://github.com/nagisanzenin/engram
- OpenChamber — https://github.com/openchamber/openchamber
