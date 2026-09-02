---
tags:
  - qa
  - conhecimento
  - setup
tipo: referencia
revisado: 2026-09-02
---
# Ambientes e Links de Trabalho

> [!info] Origem e uso
> Importado do `favoritos.txt` (03/08/2026), sincronizado com os favoritos reais do Chrome em 02/09/2026 — a coleção de favoritos do navegador do Rafael. Esta nota é a **fonte legível**; o arquivo importável no navegador está ao lado: [`favoritos-sogov.html`](favoritos-sogov.html).
>
> **Pra levar pra outra máquina**: importar o `.html` no navegador (não o `.txt` — navegador não importa lista de texto). Chrome/Edge: `⋮` → Favoritos → Importar favoritos e configurações → Arquivo HTML de favoritos. Firefox: `Ctrl+Shift+O` → Importar e Backup → Importar favoritos de HTML.

## Padrão de URL dos ambientes

O que a lista crua esconde: **todo ambiente tem os mesmos pontos de entrada**, e é isso que dá pra decorar em vez de guardar link por link.

| Caminho | Pra que serve |
|---|---|
| `/login` | Entrada padrão |
| `/login/servidor/1` | Login direto como **servidor** |
| `/login/cidadao/1` | Login direto como **cidadão** (portal externo) |
| `/admin` | Área administrativa |

O `1` no fim é o identificador da instância/prefeitura — trocar pra alternar de cliente.

## Desenvolvimento (ambientes por dev)

Cada dev tem seu ambiente de branch em `*.d10fnl6gn002xw.amplifyapp.com`, no padrão `dev-<nome>`. É por aqui que a validação em DEV acontece — e é o que aparece na seção **Ambiente** dos cards (ex.: o card da [[QA Workspace/02 Demandas/DEV/10393 - Bug Aviso Assinaturas Digitais Emitir Assinar Cidadão|SGV-10393]] registra "ambiente de branch `dev-diogo-nobrega`").

| Dev | Subdomínio |
|---|---|
| B. Clementino | `dev-bruno-clementino` |
| B. Luan | `dev-bruno-silva` |
| Diogo | `dev-diogo-nobrega` |
| J. Marcelo | `dev-joao-vieira` |
| J. Rodrigo | `dev-joao-rodrigo` |
| Marcos | `dev-marcos-santos` |
| Matheus Godoi | `dev-matheus-godoi` |

Monta-se a URL assim: `https://<subdomínio>.d10fnl6gn002xw.amplifyapp.com/login/servidor/1`

> [!tip] O nome do subdomínio é o nome da branch
> Sabendo em qual branch o dev subiu o fix, o ambiente sai direto — e o inverso também: o card diz a branch, e daí vem a URL de validação.

## Homologação e produção

| Ambiente | Base |
|---|---|
| Homolog | `https://homolog.sogov.com.br` |
| Test | `https://test.sogov.com.br` |
| Produção | `https://www.sogov.com.br` |

Os três aceitam os mesmos caminhos da tabela de padrão acima. **Atenção ao par Homolog × Test**: são dois ambientes distintos de homologação, e a copy da daily usa `homologação` — quando o teste for no `test`, vale registrar qual dos dois foi ([[QA Workspace/01 Daily/README|01 Daily/README]] define `homologação` e `hotfix` como ambientes possíveis, não distingue esses dois).

## Notion e design

| Link | O que é |
|---|---|
| [Devs workspace](https://app.notion.com/p/alfa-group/Devs-workspace-2252aec67d308049aceacf5634a3d9ce) | Página das views de sprint — é a fonte dos exports de triagem (fluxo 9) |
| [SGV-0000](https://www.notion.so/alfa-group/SGV-0000) | **Atalho de busca**: trocar `0000` pelo número da task pra abrir direto |
| [Quadro `1a42aec6`](https://app.notion.com/p/alfa-group/1a42aec67d308030aad1e9cc9eefebc9?v=1b92aec67d3080cbaf14000c58963d47) | View do Notion — *conteúdo não identificado no import, renomear quando souber* |
| [Quadro `2232aec6`](https://app.notion.com/p/alfa-group/2232aec67d30809bae01d910d89165b4?v=2aa2aec67d30802699a9000cfa65fd89) | View do Notion — *conteúdo não identificado no import, renomear quando souber* |
| [Quadro `23b72f8c`](https://app.notion.com/p/23b72f8c8990802e8048df45655c23ad?v=23b72f8c8990808d8ed1000c2c445f6a) | View que fica na barra de favoritos — *conteúdo não identificado no import* |
| [Figma — PROCESSOS SOGOV](https://www.figma.com/board/2gwBACFvRe5YYbObFsJ1m3/PROCESSOS-SOGOV?node-id=3-7342) | Board de processos |
| [Google Calendar](https://calendar.google.com/calendar/u/0/r) | Agenda |

## Referências
- Arquivo importável no navegador: [`favoritos-sogov.html`](favoritos-sogov.html) (mesma pasta)
- [[Sistema/Contexto/Ferramentas do dia a dia|Ferramentas do dia a dia]] — lista viva de ferramentas e acessos; a seção "Acessos rápidos" aponta pra cá
- [[QA Workspace/04 Conhecimento/Referências/Docs do repositório Sogov|Docs do repositório Sogov]]
