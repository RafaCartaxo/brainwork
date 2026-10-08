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

> [!info] Escopo desta pasta — segmentação aprovada, leitura por recorte em andamento
> Estrutura reorganizada em 08/10/2026 (autorização do Rafael). A abordagem anterior (investigação SGV-12082 original, ciclo SGV-11971, Roadmap e Mapa do seed) está arquivada para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]; links de navegação foram ajustados quando necessário. Esta pasta é a nova frente — mapeamento de atores e modelo do preset do TR. O TR completo (1.1–1.43) foi segmentado em **11 recortes temáticos, aprovados pelo Rafael** (ver [[../01 Modelo do preset/01 - Matriz de atores e relações#Recortes temáticos do TR|índice na matriz]]). A leitura começou pelo recorte 1 (itens 1.1–1.23) — ver resultado na própria nota; os recortes 2–11 ainda não foram lidos. **A análise não está completa.**

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | 📝 Preparada, aguardando revisão |
| Plano de análise | 📝 Preparado, aguardando revisão |
| Segmentação em recortes temáticos (`Seções do TR/`) | ✅ Aprovada pelo Rafael (11 recortes) |
| Recorte 1 — Infraestrutura técnica e operacional (1.1–1.23) | 🔵 Lido e classificado, aguardando revisão do Codex |
| Recortes 2–11 | ⏳ Não iniciados |
| Síntese visual (mapa geral) | ⏳ Não iniciado |
| Revisão da análise | ⏳ Não iniciado |

**Próximo passo:** revisão do Codex sobre o recorte 1; só depois dessa revisão o recorte 2 começa.

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
│   ├── 01 - Matriz de atores e relações.md  (índice dos recortes temáticos, sem duplicar seu conteúdo)
│   └── Seções do TR/                  (uma nota por recorte — cobertura, elementos, relações, dúvidas, fontes)
└── Fontes/
    └── Requisitos Sogov.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — casos de teste são trabalho separado, a ser decidido depois do mapeamento, e automação não está sendo implementada nesta frente.
