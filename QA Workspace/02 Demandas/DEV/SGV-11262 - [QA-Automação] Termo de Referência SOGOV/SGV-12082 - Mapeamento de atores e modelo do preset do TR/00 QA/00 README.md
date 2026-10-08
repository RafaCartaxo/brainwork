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
> **Fontes:** [[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de análise),option(QA · Mapeamento no TR),option(QA · Síntese visual),option(QA · Revisão da análise),option(Concluído)):etapa_atual]`

> [!info] Escopo desta pasta — recortes 1–3 aprovados, recorte 4 aprovado pelo Codex
> Estrutura reorganizada em 08/10/2026 (autorização do Rafael). A abordagem anterior (investigação SGV-12082 original, ciclo SGV-11971, Roadmap e Mapa do seed) está arquivada para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]; links de navegação foram ajustados quando necessário. Esta pasta é a nova frente — mapeamento de atores e modelo do preset do TR. O TR completo (1.1–1.43) foi segmentado em **11 recortes temáticos, aprovados pelo Rafael** (ver [[../01 Modelo do preset/01 - Matriz de atores e relações#Recortes temáticos do TR|índice na matriz]]). Recortes 1–3 (itens 1.1–1.27) revisados e aprovados pelo Codex; recorte 4 (itens 1.28–1.29) revisado e aprovado pelo Codex; recortes 5–11 ainda não iniciados. **A análise não está completa.**

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | 📝 Preparada, aguardando revisão |
| Plano de análise | 📝 Preparado, aguardando revisão |
| Segmentação em recortes temáticos (`Seções do TR/`) | ✅ Aprovada pelo Rafael (11 recortes) |
| Recorte 1 — Infraestrutura técnica e operacional (1.1–1.23) | ✅ Revisado e aprovado pelo Codex |
| Recorte 2 — Autenticação e ciclo de vida da identidade (1.24–1.25) | ✅ Revisado e aprovado pelo Codex |
| Recorte 3 — Estrutura organizacional e cadastro de servidores (1.26–1.27) | ✅ Revisado e aprovado pelo Codex |
| Recorte 4 — Serviços, assuntos e categorias de documentos (1.28–1.29) | ✅ Revisado e aprovado pelo Codex |
| Recortes 5–11 | ⏳ Não iniciados |
| Síntese visual (mapa geral) | ⏳ Não iniciado |
| Revisão da análise | ⏳ Não iniciado |

**Próximo passo:** iniciar a leitura do recorte 5 (itens 1.30–1.31) e submetê-lo à revisão do Codex antes de avançar.

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
    └── Termo de Referência SOGOV.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — casos de teste são trabalho separado, a ser decidido depois do mapeamento, e automação não está sendo implementada nesta frente.
