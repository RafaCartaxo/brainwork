---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "melhoria"
status: validacao
ambiente: dev
prioridade: media
etapa_atual: "QA · Revisão da análise"
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
> **Especificação do preset piloto:** [[../01 Modelo do preset/02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto (TR 1.24–1.27)]], [[../01 Modelo do preset/03 - Especificação do preset piloto (TR 1.28–1.29)|03 - Especificação do preset piloto (TR 1.28–1.29)]], [[../01 Modelo do preset/04 - Especificação do preset piloto (TR 1.30–1.31)|04 - Especificação do preset piloto (TR 1.30–1.31)]], [[../01 Modelo do preset/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)]], [[../01 Modelo do preset/06 - Especificação do preset piloto (TR 1.33)|06 - Especificação do preset piloto (TR 1.33)]], [[../01 Modelo do preset/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto (TR 1.34)]]
> **Fontes:** [[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de análise),option(QA · Mapeamento no TR),option(QA · Síntese visual),option(QA · Revisão da análise),option(Concluído)):etapa_atual]`

> [!info] Escopo desta pasta — 11 recortes revisados; dúvidas de negócio seguem abertas
> Estrutura reorganizada em 08/10/2026 (autorização do Rafael). A abordagem anterior (investigação SGV-12082 original, ciclo SGV-11971, Roadmap e Mapa do seed) está arquivada para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]. Esta frente mapeia atores, entidades, dados, estados e relações do TR completo. Os 11 recortes foram aprovados pelo Rafael e revisados item a item contra o PDF (1.1–1.43); a revisão documental está registrada em [[04 - Revisão da análise]]. Permanecem dúvidas explícitas a esclarecer com Rafael, sem equivalências presumidas (ver [[../01 Modelo do preset/00 - Mapa geral#Lacunas registradas (arestas tracejadas)|lacunas no mapa]]).

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Escopo aplicado à nova frente de mapeamento do TR completo |
| Plano de análise | ✅ Método aplicado: recorte a recorte, fonte PDF, proveniência explícita |
| Segmentação em recortes temáticos (`Seções do TR/`) | ✅ Aprovada pelo Rafael (11 recortes) |
| Recorte 1 — Infraestrutura técnica e operacional (1.1–1.23) | ✅ Revisado e aprovado pelo Codex |
| Recorte 2 — Autenticação e ciclo de vida da identidade (1.24–1.25) | ✅ Revisado e aprovado pelo Codex |
| Recorte 3 — Estrutura organizacional e cadastro de servidores (1.26–1.27) | ✅ Revisado e aprovado pelo Codex |
| Recorte 4 — Serviços, assuntos e categorias de documentos (1.28–1.29) | ✅ Revisado e aprovado pelo Codex |
| Recortes 5–11 | ✅ Revisados e aprovados |
| Síntese visual (mapa geral) | ✅ Atualizada para leitura vertical e alinhada às notas |
| Revisão da análise | ✅ Cobertura/rastreabilidade revisadas; dúvidas de negócio preservadas |
| Especificação do preset piloto (TR 1.24–1.27) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.28–1.29) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/03 - Especificação do preset piloto (TR 1.28–1.29)|03 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.30–1.31) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/04 - Especificação do preset piloto (TR 1.30–1.31)|04 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.32, 1.36–1.37) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.33) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/06 - Especificação do preset piloto (TR 1.33)|06 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.34) | 🔵 Em levantamento — ver [[../01 Modelo do preset/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto]] |

**Próximo passo:** revisão do Codex sobre a especificação do preset para o item 1.34 ([[../01 Modelo do preset/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto]]). Em paralelo, seguem abertas as dúvidas de negócio do mapeamento — a primeira é se Canal Oficial (1.38.1.b) e Jornal Oficial (1.38.3.1) continuam como elementos distintos ou são o mesmo no produto — sem travar nem depender da especificação do preset.

Pacote para `SGV-12082`:

```text
SGV-12082 - Mapeamento de atores e modelo do preset do TR/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de análise.md
│   └── 04 - Revisão da análise.md
├── 01 Modelo do preset/
│   ├── 00 - Mapa geral.md              (síntese Mermaid vertical, derivada dos recortes)
│   ├── 01 - Matriz de atores e relações.md  (índice dos recortes temáticos, sem duplicar seu conteúdo)
│   ├── 02 - Especificação do preset piloto (TR 1.24–1.27).md  (recortes 02/03 × seed de automação atual)
│   ├── 03 - Especificação do preset piloto (TR 1.28–1.29).md  (recorte 04 × seed de automação atual)
│   ├── 04 - Especificação do preset piloto (TR 1.30–1.31).md  (recorte 05 × seed de automação atual)
│   └── Seções do TR/                  (uma nota por recorte — cobertura, elementos, relações, dúvidas, fontes)
└── Fontes/
    └── Termo de Referência SOGOV.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — casos de teste são trabalho separado, a ser decidido depois do mapeamento, e automação não está sendo implementada nesta frente.
