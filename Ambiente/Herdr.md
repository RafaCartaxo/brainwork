---
title: Herdr
tags:
  - ambiente
  - setup
date: 2026-08-27
---
# Herdr

> [!info] Isso não é convenção do QA
> Este arquivo vive em `Ambiente/`, fora de `Sistema/` e `QA Workspace/` de propósito: documenta uma ferramenta de **terminal/ambiente pessoal**, não um padrão de trabalho do QA. Não é lido por [[../Sistema/Contexto/REGRAS_IA|REGRAS_IA]] nem pelos fluxos do vault — é referência de setup de máquina, no mesmo espírito do [[../Sistema/Contexto/Plugins Instalados|Plugins Instalados]] (que é o equivalente pro Obsidian).

## O que é
[Herdr](https://herdr.dev) é um multiplexador de terminal feito pra agentes de IA de código — organiza terminais em workspaces/tabs/panes, reconhece o agente rodando em cada pane e expõe a sessão via CLI (`herdr agent`, `herdr pane`, `herdr workspace`, etc.). É quem dá a sessão persistente usada nas sessões de Claude Code deste ambiente.

- Binário: `~/.local/bin/herdr` (v0.8.2, canal `stable`)
- Config: `~/.config/herdr/config.toml`
- Não inicia sozinho — é preciso rodar `herdr` manualmente num terminal novo (o Ptyxis não está configurado pra abrir com ele por padrão)

## Setup atual
```toml
# ~/.config/herdr/config.toml
onboarding = false

[theme]
name = "solarized"
auto_switch = false

[ui]
agent_panel_sort = "spaces"
```

## Integração com Claude Code
A integração precisa ser instalada à parte — sem ela, o herdr não detecta corretamente se a sessão está `idle`/`working`/`blocked`/`done`:

```
herdr integration install claude
```

Isso cria `~/.claude/hooks/herdr-agent-state.sh` e adiciona um hook `SessionStart` em `~/.claude/settings.json` que chama esse script. Instalado em 2026-08-27 (estava faltando até então).

## Autocomplete no zsh
```bash
mkdir -p ~/.oh-my-zsh/custom/completions
herdr completion zsh > ~/.oh-my-zsh/custom/completions/_herdr
```
`$ZSH_CUSTOM/completions` já entra no `fpath` automaticamente pelo oh-my-zsh — não precisa mexer no `.zshrc`. Depois de criar o arquivo, abrir um terminal novo (ou `exec zsh`) pra recarregar.

## Setup do zero (outra máquina)
1. Instalar o `herdr` ([site oficial](https://herdr.dev))
2. Rodar `herdr integration install claude` (repetir pra outros agentes usados: `codex`, `cursor`, etc. — ver `herdr integration install --help`)
3. Gerar o autocomplete conforme a seção acima
4. `herdr` num terminal novo pra criar/anexar a sessão persistente
