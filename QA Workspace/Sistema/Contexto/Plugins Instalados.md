---
title: Plugins Instalados
tags:
  - plugins
  - setup
date: 2026-07-13
---
# Setup do Vault

> [!info] Uso
> Esse arquivo documenta tudo que fica configurado dentro de `.obsidian/` (plugins, atalhos, ícones, cores) e que **não é copiado junto** se alguém migrar só o conteúdo do vault (a pasta `QA Workspace/`) para outro computador ou outra ferramenta. Se for configurar do zero — inclusive com outra IA — use este arquivo como checklist.

## Plugins Ativos

| Plugin                 |    ID                        | Descrição                                    |
| ----------------------- | ---------------------------- | --------------------------------------------- |
| Excalidraw              | `obsidian-excalidraw-plugin` | Diagramas e desenhos dentro do Obsidian       |
| Iconize                 | `obsidian-icon-folder`       | Ícones e cores personalizados por pasta/arquivo |
| Omnisearch               | `omnisearch`                 | Busca full-text/semântica avançada no vault (atalho: Ctrl+L) |
| Calendar                | `calendar`                   | Visualização calendário das notas diárias     |
| Tasks                   | `obsidian-tasks-plugin`      | Gerenciamento de tarefas/checklists            |
| Templater               | `templater-obsidian`         | Templates dinâmicos (ex.: data automática)    |
| Dataview                | `dataview`                   | Consultas e listagens dinâmicas sobre notas (usado na [[../../Dashboard/Dashboard|Dashboard]]) |
| Slides Extended         | `slides-extended`            | Apresentações a partir de notas               |
| Minimal Theme Settings  | `obsidian-minimal-settings`  | Configurações do tema Minimal                 |
| Editing Toolbar         | `editing-toolbar`            | Barra de formatação estilo Word no modo de edição |
| Homepage                | `homepage`                   | Abre a [[../../Dashboard/Dashboard\|Dashboard]] automaticamente ao abrir o vault; botão na ribbon + comando com atalho |
| Obsidian Git            | `obsidian-git`               | Versionamento/sincronização automática do vault (pull ao abrir; commit+push a cada 10 min) |

## Plugins Core (nativos) que precisam estar ligados
- **Bases** — necessário pros arquivos `.base` funcionarem ([[../../Dashboard/Bugs.base|Bugs.base]], [[../../Dashboard/Demandas.base|Demandas.base]], [[../../01 Daily/Índice Diário.base|Índice Diário.base]]). Em Settings → Core plugins.
- **Daily notes** — ver configuração específica abaixo.

## Daily Notes (configuração)
Em Settings → Daily notes:
- **Folder**: `QA Workspace/01 Daily`
- **Format**: `YYYY-MM/DD-MM`
- **Template**: `QA Workspace/Sistema/Templates/Daily Note.md`

> [!warning] Por que não é "Julho/13 de Julho"
> Esse Obsidian não tem o locale em português carregado pro moment.js — nomes de mês por extenso (`Julho`) só são gerados em inglês (`July`), quebrando a geração automática de notas. Por isso o formato é 100% numérico (`YYYY-MM/DD-MM`), o que também deixa os nós mais curtos no Graph View.

## Atalho customizado
- `Ctrl+L` → comando `omnisearch:show-modal` (busca full-text no vault). Configurado em Settings → Hotkeys.
- `Ctrl+H` → comando `homepage:open-homepage` (volta pra Dashboard de qualquer lugar). Configurado em Settings → Hotkeys.

## Modo leitura por padrão
Toda nota abre em **modo leitura** (Settings → Editor → "Default view for new tabs" = Reading view; no `app.json`: `defaultViewMode: preview`). Pra editar: **`Ctrl+E`** alterna leitura ↔ edição (atalho nativo do Obsidian, sem config). O Homepage também abre a Dashboard em Reading view (config própria do plugin).

## Acesso rápido à Dashboard
Três caminhos, sem navegar por pastas (config do Homepage: Settings → Homepage → "Main Homepage" apontando pra `QA Workspace/Dashboard/Dashboard`, "Open on startup" ligado, "Refresh Dataview" ligado):
1. **Ao abrir o vault** — o plugin Homepage abre a Dashboard sozinho.
2. **`Ctrl+H`** (ou o ícone de casa na ribbon) — volta pra ela de qualquer nota.
3. **Bookmark** — a Dashboard fica fixa no painel Bookmarks (core plugin) no topo da sidebar.

A daily de hoje se acessa pelo botão "✏️ Escrever na daily de hoje" da própria Dashboard, ou pelo Calendar.

## Versionamento (git + Obsidian Git)
O vault inteiro (`BrainWork/`, incluindo `.obsidian/` com plugins, scripts e snippets) é um repositório git — **clonar em outra máquina traz o ambiente completo**, não só as notas. Remoto: repositório **privado pessoal** no GitHub (o vault é método de trabalho/insights do QA; código do projeto é da empresa e não entra aqui).

- **Fora do git**: `QA Workspace/Evidências/` (vídeos, 600MB+ — ficam locais por máquina; o registro oficial da evidência é a task do Notion) e `workspace.json` (layout volátil).
- **Sincronização**: Obsidian Git com pull ao abrir o vault, commit+push automáticos a cada 10 min, pull antes de push (merge). Mensagens `vault: <timestamp>`.
- **Nova máquina**: `git clone <repo>` → abrir a pasta como vault no Obsidian → ativar community plugins quando perguntado → configurar credencial GitHub (HTTPS + token) → recriar só o que é do SO (esquema `evidencia://`, ver seção própria).

## Botão "🔄 Atualizar" da Dashboard (script local, sem plugin)
O botão na seção **Hoje** da [[../../Dashboard/Dashboard|Dashboard]] roda o script `.obsidian/scripts/qa-atualiza.py` (Python 3 puro, sem dependências, offline — **não usa IA nem Claude CLI**). Ele executa a parte mecânica do ciclo do [[../Skills/SKILL_INBOX|SKILL_INBOX]]: cria a daily de hoje se não existir, carrega pendências de ontem sem duplicar, e completa pendências concluídas com resultado anotado entre parênteses (frases padrão, cards atualizados/movidos/renomeados, Histórico). O disparo é feito pelo bloco `dataviewjs` da própria Dashboard via `child_process` — funciona só no desktop (requer `python3` no sistema). Idempotente: pode clicar quantas vezes quiser.

## CSS snippet (`qa-workspace.css`)
Arquivo em `.obsidian/snippets/qa-workspace.css`, habilitado em Settings → Appearance → CSS snippets. Estiliza só as notas que declaram as classes no frontmatter (`cssclasses`):
- **`qa-dashboard`** (usada na [[../../Dashboard/Dashboard|Dashboard]]): título com sublinhado teal, seções em rótulo caixa-alta, faixa de KPIs em cards (classes `qa-kpis`/`qa-kpi`, geradas pelo bloco `dataviewjs` do Resumo de Bugs), botão da daily de hoje (classe `qa-today`), fluxograma centralizado.
- **`qa-daily`** (usada no template [[../Templates/Daily Note.md|Daily Note.md]] e nas dailies): barra lateral colorida por seção no modo leitura, usando as mesmas cores das pastas/status (Atividades teal, Bugs vermelho, Melhorias âmbar, Pendências violeta, DEV/HML/POCs nas cores das subpastas de `02 Demandas`).

As cores derivam da tabela de ícones/cores por pasta abaixo — se mudar uma cor lá, mudar no snippet também. Sem o snippet habilitado, as notas continuam 100% funcionais, só perdem o estilo.

## Ícones e cores por pasta (Iconize)
Cada pasta tem um ícone Lucide + cor própria, escolhidos pra remeter ao que a pasta representa. Nenhuma cor se repete entre pastas irmãs (mesmo nível).

**Regra didática de ambiente**: o mesmo ambiente usa o mesmo ícone+cor em todo lugar — a pasta de cards (`02 Demandas/<ambiente>`) e a pasta de vídeos (`Evidências/<ambiente>`) são visualmente idênticas (DEV = code-2 verde, Homologação = clipboard-check laranja, Hotfix = flame vermelho).

| Pasta | Ícone (Lucide) | Cor |
|---|---|---|
| `QA Workspace` | beaker | `#0d9488` |
| `Dashboard/` (pasta e nota) | layout-dashboard | `#eab308` |
| `00 Inbox` | list-todo | `#2563eb` |
| `01 Daily` | calendar-days | `#d97706` |
| `01 Daily/2026-07` (dar ícone igual à pasta de cada mês novo) | calendar | `#d97706` |
| `02 Demandas` | clipboard-list | `#7c3aed` |
| `02 Demandas/DEV` | code-2 | `#059669` |
| `02 Demandas/HML` | clipboard-check | `#ea580c` |
| `02 Demandas/Hotfix` | flame | `#dc2626` |
| `02 Demandas/POCs` | flask-conical | `#c026d3` |
| `02 Demandas/Concluídas` | badge-check | `#ca8a04` |
| `03 Sanidades` | shield-check | `#0891b2` |
| `04 Conhecimento` | book-open | `#e11d48` |
| `99 Arquivo` | archive | `#78350f` |
| `Evidências` | video | `#16a34a` |
| `Evidências/Desenvolvimento` | code-2 | `#059669` |
| `Evidências/Homologação` | clipboard-check | `#ea580c` |
| `Evidências/Hotfix` | flame | `#dc2626` |
| `Evidências/Produção` | globe | `#2563eb` |
| `Evidências/Arquitetura` | network | `#4338ca` |
| `Evidências/Cadastrar` | file-plus-2 | `#ca8a04` |
| `Sistema` | settings | `#475569` |
| `Sistema/Contexto` | compass | `#4338ca` |
| `Sistema/Skills` | wrench | `#dc2626` |
| `Sistema/Specs` | pencil-ruler | `#0284c7` |
| `Sistema/Templates` | layout-template | `#0d9488` |

## Graph View — grupos de cor
Em Settings → Graph View (ou no ícone de grafo), os seguintes grupos por query, usando as mesmas cores da tabela de ícones onde faz sentido:

| Query | Cor |
|---|---|
| `path:"QA Workspace/01 Daily"` | `#d97706` |
| `tag:#bug` | `#7c3aed` |
| `path:"QA Workspace/Sistema"` | `#475569` |
| `path:"QA Workspace/Dashboard"` | `#eab308` |
| `path:"QA Workspace/00 Inbox"` | `#2563eb` |

## Esquema de URI `evidencia://` (fora do Obsidian, específico desta máquina)
Os cards de bug têm um link `[🔍](evidencia://<número>)` no título da seção Evidências, que abre o Nautilus já em modo de busca filtrado pelo número do card (usa o mesmo mecanismo de busca do GNOME Shell, `org.gnome.Shell.SearchProvider2.LaunchSearch`). Isso é config do **sistema operacional**, não do Obsidian — some se migrar só a pasta do vault. Pra recriar:

1. Script executável em `~/.local/bin/abrir-evidencia`:
```bash
#!/bin/bash
URI="$1"
TERM="${URI#evidencia://}"
TERM="${TERM%/}"
[ -z "$TERM" ] && exit 1
gdbus call --session --dest org.gnome.Nautilus \
  --object-path /org/gnome/Nautilus/SearchProvider \
  --method org.gnome.Shell.SearchProvider2.LaunchSearch "['$TERM']" 0
```
2. `chmod +x ~/.local/bin/abrir-evidencia`
3. Arquivo `~/.local/share/applications/abrir-evidencia.desktop`:
```
[Desktop Entry]
Type=Application
Name=Abrir Evidência QA
Exec=/home/<usuario>/.local/bin/abrir-evidencia %u
NoDisplay=true
MimeType=x-scheme-handler/evidencia;
```
4. `update-desktop-database ~/.local/share/applications/`
5. `xdg-mime default abrir-evidencia.desktop x-scheme-handler/evidencia`

Só funciona em Linux/GNOME/Nautilus. Em outro ambiente (macOS, Windows, outro DE), precisa de um equivalente diferente — ou cair de volta pro link simples `file:///caminho/da/pasta/` (sem filtro, só abre a pasta).

## Setup Rápido (do zero)

1. Abrir **Settings → Community plugins**, desativar **Safe mode**
2. Procurar e instalar cada plugin da tabela acima pelo ID, ativar todos
3. Habilitar os core plugins **Bases** e **Daily notes** (Settings → Core plugins)
4. Configurar Daily Notes conforme a seção acima
5. Configurar o atalho `Ctrl+L` pro Omnisearch (Settings → Hotkeys → buscar "Omnisearch")
6. Recriar os ícones/cores por pasta (Iconize) e os grupos de cor do Graph View conforme as tabelas acima
7. Copiar o snippet `qa-workspace.css` pra `.obsidian/snippets/` e habilitar em Settings → Appearance → CSS snippets (ver seção acima)
8. Copiar o script `.obsidian/scripts/qa-atualiza.py` (botão Atualizar da Dashboard — requer `python3` no sistema)
9. Recriar o esquema de URI `evidencia://` conforme a seção acima (fora do Obsidian, no sistema operacional)
