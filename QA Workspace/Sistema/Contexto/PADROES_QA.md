---
tags:
  - qa
  - contexto
---
# Padrões de QA

## Estrutura de Pastas
```
QA Workspace/
├── README.md
├── Dashboard/
│   ├── Dashboard.md
│   ├── Bugs.base
│   └── Demandas.base
├── 00 Inbox/
│   └── README.md (backlog do próprio vault/ferramenta — não é captura do dia a dia, ver [[QA Workspace/Sistema/Skills/SKILL_INBOX.md|SKILL_INBOX.md]])
├── 01 Daily/
│   ├── README.md
│   ├── Índice Diário.base
│   └── 2026-07/
│       └── DD-MM.md (uma por dia)
├── 02 Demandas/
│   ├── README.md
│   ├── DEV/
│   ├── HML/
│   ├── Hotfix/
│   ├── POCs/
│   └── Concluídas/
├── 03 Sanidades/
│   └── README.md (sem estrutura ainda — template/skill de Sanidade no backlog do vault)
├── 04 Conhecimento/
│   └── README.md (sem estrutura ainda)
├── 05 Refinar/
│   └── README.md (fila de material bruto — exports do Notion etc. — aguardando refinamento; apagado após virar card)
├── 99 Arquivo/
│   └── README.md (cards descartados — bugs/suspeitas que não ocorrem, melhorias descartadas)
├── Evidências/
│   ├── README.md (convenção de nomes e regras de organização das gravações)
│   └── Desenvolvimento|Homologação|Produção|Hotfix|Arquitetura|Cadastrar/ (vídeos de validação — não versionado, ver .gitignore)
└── Sistema/
    ├── README.md
    ├── Contexto/
    │   ├── COMO_EU_TRABALHO.md
    │   ├── FLUXOS.md
    │   ├── PADROES_QA.md
    │   └── Plugins Instalados.md
    ├── Skills/
    │   ├── SKILL_BUGS.md
    │   ├── SKILL_CASOS_DE_TESTE.md
    │   ├── SKILL_INBOX.md
    │   ├── SKILL_PADRONIZACAO.md
    │   └── SKILL_PLANO_DE_TESTE.md
    ├── Specs/
    │   └── YYYY-MM-DD-<tópico>-design.md (documentos de design/spec de melhorias do próprio vault)
    └── Templates/
        ├── Bug Report.md
        ├── Casos de teste.md
        ├── Daily Note.md
        └── Demanda.md
```

## Templates
| Template | Uso |
|----------|-----|
| [[QA Workspace/Sistema/Templates/Bug Report.md\|Bug Report.md]] | Reportar bugs com estrutura padronizada |
| [[QA Workspace/Sistema/Templates/Casos de teste.md\|Casos de teste.md]] | Criar casos de teste no formato Dado/Quando/Então |
| [[QA Workspace/Sistema/Templates/Demanda.md\|Demanda.md]] | Estruturar nota principal de uma demanda (hub) |
| [[QA Workspace/Sistema/Templates/Daily Note.md\|Daily Note.md]] | Registro diário de atividades — lugar único de escrita do dia a dia |

## Skills
| Arquivo | Finalidade |
|---------|------------|
| [[QA Workspace/Sistema/Skills/SKILL_BUGS.md\|SKILL_BUGS.md]] | Estrutura e checklist para reportar bugs |
| [[QA Workspace/Sistema/Skills/SKILL_CASOS_DE_TESTE.md\|SKILL_CASOS_DE_TESTE.md]] | Estrutura e boas práticas de casos de teste |
| [[QA Workspace/Sistema/Skills/SKILL_PLANO_DE_TESTE.md\|SKILL_PLANO_DE_TESTE.md]] | Estrutura e template de plano de teste |
| [[QA Workspace/Sistema/Skills/SKILL_PADRONIZACAO.md\|SKILL_PADRONIZACAO.md]] | Diretrizes de escrita e consistência visual |
| [[QA Workspace/Sistema/Skills/SKILL_INBOX.md\|SKILL_INBOX.md]] | Auto-organização da daily: classificação e roteamento dos registros crus (+ capturas legadas do Inbox) |

## Contexto
| Arquivo | Finalidade |
|---------|------------|
| [[QA Workspace/Sistema/Contexto/COMO_EU_TRABALHO.md\|COMO_EU_TRABALHO.md]] | Fluxo de trabalho pessoal, ambientes e tipos de demanda |
| [[QA Workspace/Sistema/Contexto/FLUXOS.md\|FLUXOS.md]] | Passo a passo prático de cada fluxo (dia, bug, melhoria, evidência) — linkado na Dashboard |
| [[QA Workspace/Sistema/Contexto/PADROES_QA.md\|PADROES_QA.md]] | Este arquivo — padrões técnicos e de documentação |
| [[QA Workspace/Sistema/Contexto/Plugins Instalados.md\|Plugins Instalados.md]] | Setup completo do vault: plugins, atalhos, ícones/cores, Daily Notes, Graph View — necessário pra replicar em outro computador ou com outra IA |

## Organização de Bugs
- Todo bug usa o [[QA Workspace/Sistema/Templates/Bug Report.md|Bug Report.md]] como estrutura única (sem tag `demanda`, sem callouts) — ver [[QA Workspace/Sistema/Skills/SKILL_BUGS.md|SKILL_BUGS.md]].
- `status` reflete o ciclo de vida do bug: `aberto` (ainda com problema) → `em_validacao` → `resolvido`. Não usar `dev`/`hml`/`prod` nesse campo — isso é o que o campo `ambiente` já representa.
- `ambiente` reflete o último ambiente testado (DEV/HML/HOTFIX/PROD), usado para localizar o card em `02 Demandas/`.
- **Hotfix**: correção urgente é validada num ambiente de homologação que carrega a versão de produção + a hotfix. O card vive em `02 Demandas/Hotfix/` durante a validação (`ambiente: HOTFIX`) e, aprovado, vai pra `Concluídas/` como qualquer bug. Evidências na subpasta `Evidências/Hotfix/`.
- **Bug de produção em sustentação** (relatado/analisado em produção, correção **não urgente** — se urgente, é Hotfix acima): não existe pasta `Produção/` em `02 Demandas/` de propósito — o card nasce em `DEV/` com `ambiente: DEV`, representando a **posição na esteira de correção**, e a origem/análise em produção fica registrada na Descrição e no Histórico. Daí segue a esteira normal (ou a variação 3f, se for task de API). Precedentes: SGV-9963, SGV-9750.
- `cadastrado_por` (opcional): quem cadastrou o card, quando não foi o próprio responsável pela validação. Se tem a informação, preenche; se não, deixa vazio — não inventar.
- Ao mudar de ambiente ou ser concluído, mover o arquivo fisicamente de pasta (`DEV` → `HML` → `Concluídas`), atualizando `ambiente` e `status` no frontmatter e um novo item em Histórico (dentro de Informações adicionais), no formato `- YYYY-MM-DD - <frase padrão com emoji>` — mesma frase da daily (ver [[QA Workspace/01 Daily/README|tabela de padronização]]). **Movendo fora do Obsidian** (script, IA, terminal): atualizar também os wikilinks pro caminho novo em todo o vault — o Obsidian só reescreve links sozinho quando a movimentação é feita dentro dele.

## Descarte de bug/suspeita (99 Arquivo)
Quando um bug ou suspeita de bug (achado via análise de código, CX, ou qualquer outra origem) é investigado e confirmado que **não ocorre** (cenário impossível, premissa errada, ou já coberto por outro comportamento):
- `status` vira `descartado` (novo valor, ao lado de `aberto`/`em_validacao`/`resolvido`)
- Move-se o arquivo fisicamente pra `99 Arquivo/` (mesma lógica de mover por mudança de status já usada entre `DEV`/`HML`/`Concluídas`)
- O(s) Caso(s) de Teste Básico(s) relacionado(s) são marcados como "Sim" (comportamento esperado se confirma — não há bug)
- `Observações` explica o motivo do descarte (por que o cenário não se aplica ou não reproduz)
- Registra-se em Atividades da daily do dia com a frase padrão: `🗑️ Bug/SGV XXXX - Descartado (não reproduz: <motivo curto>)`

## Frontmatter
Todas as notas seguem frontmatter YAML com ao menos a tag `qa`:
```yaml
---
tags:
  - qa
  - [tag-específica]
---
```
