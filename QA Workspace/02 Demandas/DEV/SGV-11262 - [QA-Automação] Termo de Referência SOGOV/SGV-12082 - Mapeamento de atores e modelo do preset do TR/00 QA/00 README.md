---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "melhoria"
status: backlog
ambiente: dev
prioridade: media
etapa_atual: "QA · Triagem"
modulo: ""
responsavel: ""
aguardando: ""
cadastrado_por: ""
data_inicio: ""
data_fim: ""
pontos: ""
---
# SGV-12082 — Mapeamento de atores e modelo do preset do TR

> [!info]- Navegação QA
> **Índice da iniciativa:** [[../../Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]]
> **Roadmap da iniciativa:** [[../../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]]
> **Demanda:** [[01 - Demanda]]
> **Plano de análise:** [[02 - Plano de análise]]
> **Revisão da análise:** [[04 - Revisão da análise]]
> **Mapa geral:** [[../01 Modelo do preset/00 - Mapa geral]]
> **Matriz de atores e relações:** [[../01 Modelo do preset/01 - Matriz de atores e relações]]
> **Fontes:** [[../Fontes/Requisitos Sogov.pdf|Requisitos Sogov.pdf]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de análise),option(QA · Mapeamento no TR),option(QA · Síntese visual),option(QA · Revisão da análise),option(Concluído)):etapa_atual]`

> [!info] Escopo desta pasta — estrutura pronta para revisão, mapeamento do TR ainda não iniciado
> Estrutura reorganizada em 08/10/2026 (autorização do Rafael). A abordagem anterior (investigação SGV-12082 original, ciclo SGV-11971, Roadmap e Mapa do seed) está arquivada para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]; links de navegação foram ajustados quando necessário. Esta pasta é a nova frente — mapeamento de atores e modelo do preset do TR. Demanda e plano já têm escopo/método estruturados, aguardando revisão; o conteúdo do TR ainda não foi lido/mapeado — nenhum ator, entidade ou achado do TR foi registrado ainda.

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | 📝 Preparada, aguardando revisão |
| Plano de análise | 📝 Preparado, aguardando revisão |
| Mapeamento na matriz (atores/entidades/relações) | ⏳ Não iniciado |
| Síntese visual (mapa geral) | ⏳ Não iniciado |
| Revisão da análise | ⏳ Não iniciado |

**Próximo passo:** revisão/aprovação do escopo ([[01 - Demanda]]) e do plano ([[02 - Plano de análise]]) — só depois disso iniciar a leitura/mapeamento do TR por blocos temáticos.

Pacote para `SGV-12082`:

```text
SGV-12082 - Mapeamento de atores e modelo do preset do TR/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de análise.md
│   └── 04 - Revisão da análise.md
├── 01 Modelo do preset/
│   ├── 00 - Mapa geral.md              (esqueleto Mermaid, sem conteúdo de domínio)
│   └── 01 - Matriz de atores e relações.md  (cabeçalho/colunas, sem linhas preenchidas)
└── Fontes/
    └── Requisitos Sogov.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — casos de teste são trabalho separado, a ser decidido depois do mapeamento, e automação não está sendo implementada nesta frente.
