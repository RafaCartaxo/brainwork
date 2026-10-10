---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "melhoria"
status: validacao
ambiente: dev
prioridade: media
etapa_atual: "QA · Especificação do preset (Fase 2)"
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
> **Especificação do preset piloto:** [[../01 Modelo do preset/02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto (TR 1.24–1.27)]], [[../01 Modelo do preset/03 - Especificação do preset piloto (TR 1.28–1.29)|03 - Especificação do preset piloto (TR 1.28–1.29)]], [[../01 Modelo do preset/04 - Especificação do preset piloto (TR 1.30–1.31)|04 - Especificação do preset piloto (TR 1.30–1.31)]], [[../01 Modelo do preset/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)]], [[../01 Modelo do preset/06 - Especificação do preset piloto (TR 1.33)|06 - Especificação do preset piloto (TR 1.33)]], [[../01 Modelo do preset/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto (TR 1.34)]], [[../01 Modelo do preset/08 - Especificação do preset piloto (TR 1.35.2.2.1)|08 - Especificação do preset piloto (TR 1.35.2.2.1)]], [[../01 Modelo do preset/09 - Especificação do preset piloto (TR 1.35.2.3)|09 - Especificação do preset piloto (TR 1.35.2.3)]], [[../01 Modelo do preset/10 - Especificação do preset piloto (TR 1.35.2.4)|10 - Especificação do preset piloto (TR 1.35.2.4)]], [[../01 Modelo do preset/11 - Especificação do preset piloto (TR 1.35.2.5)|11 - Especificação do preset piloto (TR 1.35.2.5)]], [[../01 Modelo do preset/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)]], [[../01 Modelo do preset/13 - Especificação do preset piloto (TR 1.35.3)|13 - Especificação do preset piloto (TR 1.35.3)]], [[../01 Modelo do preset/14 - Especificação do preset piloto (TR 1.35.4)|14 - Especificação do preset piloto (TR 1.35.4)]], [[../01 Modelo do preset/15 - Especificação do preset piloto (TR 1.35.5)|15 - Especificação do preset piloto (TR 1.35.5)]], [[../01 Modelo do preset/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)]], [[../01 Modelo do preset/17 - Especificação do preset piloto (TR 1.40.3)|17 - Especificação do preset piloto (TR 1.40.3)]]
> **Fontes:** [[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de análise),option(QA · Mapeamento no TR),option(QA · Síntese visual),option(QA · Revisão da análise),option(QA · Especificação do preset (Fase 2)),option(Concluído)):etapa_atual]`

> [!info] Escopo desta pasta — Fase 1 concluída (11 recortes); Fase 2 em andamento (16 fatias); consolidação é o próximo passo
> Estrutura reorganizada em 08/10/2026 (autorização do Rafael). A abordagem anterior (investigação SGV-12082 original, ciclo SGV-11971, Roadmap e Mapa do seed) está arquivada para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]. **Fase 1:** esta frente mapeou atores, entidades, dados, estados e relações do TR completo — os 11 recortes foram aprovados pelo Rafael e revisados item a item contra o PDF (1.1–1.43); a revisão documental está registrada em [[04 - Revisão da análise]]. **Fase 2 (em andamento):** especificação do preset candidato por cruzamento de cada item do TR com o que o seed/testes Playwright reais confirmam — ver "Status do trabalho" abaixo e o [[../../Roadmap - Modelo de atores e preset do TR|Roadmap]] para a sequência completa e os gates. Permanecem dúvidas de negócio explícitas a esclarecer com Rafael, numa trilha paralela que não bloqueia a Fase 2 (ver [[../01 Modelo do preset/00 - Mapa geral#Lacunas registradas (arestas tracejadas)|lacunas no mapa]]).

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
| Especificação do preset piloto (TR 1.34) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.2.1) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/08 - Especificação do preset piloto (TR 1.35.2.2.1)|08 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.3) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/09 - Especificação do preset piloto (TR 1.35.2.3)|09 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.4) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/10 - Especificação do preset piloto (TR 1.35.2.4)|10 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.5) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/11 - Especificação do preset piloto (TR 1.35.2.5)|11 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.6–1.35.2.7) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.3) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/13 - Especificação do preset piloto (TR 1.35.3)|13 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.4) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/14 - Especificação do preset piloto (TR 1.35.4)|14 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.5) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/15 - Especificação do preset piloto (TR 1.35.5)|15 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.40.2–1.40.2.1) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|16 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.40.3) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/17 - Especificação do preset piloto (TR 1.40.3)|17 - Especificação do preset piloto]] |
| Consolidação da especificação do preset (Fase 2, passo 7 do Roadmap) | ⏳ Próximo passo único — nenhuma fatia nova (18+) abre antes desta consolidação ser revisada |

**Próximo passo:** consolidar as 16 fatias aprovadas (02–17) numa visão-resumo rastreável, sem duplicar as notas-fonte (detalhe das colunas/classes no passo 7 da "Sequência macro" do [[../../Roadmap - Modelo de atores e preset do TR|Roadmap]]). **Nenhuma fatia nova (18+) abre antes dessa consolidação ser revisada.** Em paralelo, seguem abertas as dúvidas de negócio do mapeamento — a primeira é se Canal Oficial (1.38.1.b) e Jornal Oficial (1.38.3.1) continuam como elementos distintos ou são o mesmo no produto — trilha não bloqueante, exceto quando uma linha da especificação depender diretamente dela.

Pacote para `SGV-12082`:

```text
SGV-12082 - Mapeamento de atores e modelo do preset do TR/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de análise.md
│   └── 04 - Revisão da análise.md
├── 01 Modelo do preset/
│   ├── 00 - Mapa geral.md              (síntese Mermaid vertical, derivada dos recortes — Fase 1)
│   ├── 01 - Matriz de atores e relações.md  (índice dos recortes temáticos, sem duplicar seu conteúdo — Fase 1)
│   ├── 02–17 - Especificação do preset piloto (*.md)  (16 fatias aprovadas da Fase 2 — TR × seed/testes reais; lista completa e atualizada na tabela "Status do trabalho" acima, não repetida aqui para não ficar obsoleta a cada fatia nova)
│   └── Seções do TR/                  (uma nota por recorte — cobertura, elementos, relações, dúvidas, fontes — Fase 1)
└── Fontes/
    └── Termo de Referência SOGOV.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — esta frente não produz casos de teste nem preparação de Qase; uma eventual frente para isso seria definida à parte, sem fase atribuída por enquanto. Automação/implementação de preset também não acontece aqui (nem na Fase 1, nem na Fase 2) — a Fase 3 do Roadmap trata só da decisão/desenho do preset persistente, não de CTs/Qase.
