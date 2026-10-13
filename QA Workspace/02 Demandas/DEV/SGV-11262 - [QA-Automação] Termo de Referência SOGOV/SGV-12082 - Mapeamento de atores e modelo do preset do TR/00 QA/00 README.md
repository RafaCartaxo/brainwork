---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "melhoria"
status: validacao
ambiente: dev
prioridade: media
etapa_atual: "QA · Preparação técnica (Fase 5, futura)"
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
> **Visão consolidada do preset candidato:** [[../01 Modelo do preset/02 - Visão consolidada do preset candidato]]
> **Triagem dos itens sem fatia (passo 8):** [[../01 Modelo do preset/03 - Triagem dos itens sem fatia (passo 8)]]
> **Modelo-alvo dos dados do preset (passo 9):** [[../01 Modelo do preset/04 - Modelo-alvo dos dados do preset]]
> **Matriz de fornecimento dos dados (passo 10):** [[../01 Modelo do preset/05 - Matriz de fornecimento dos dados]]
> **Especificação do preset piloto:** [[../01 Modelo do preset/Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto (TR 1.24–1.27)]], [[../01 Modelo do preset/Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)|03 - Especificação do preset piloto (TR 1.28–1.29)]], [[../01 Modelo do preset/Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)|04 - Especificação do preset piloto (TR 1.30–1.31)]], [[../01 Modelo do preset/Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)]], [[../01 Modelo do preset/Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)|06 - Especificação do preset piloto (TR 1.33)]], [[../01 Modelo do preset/Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto (TR 1.34)]], [[../01 Modelo do preset/Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)|08 - Especificação do preset piloto (TR 1.35.2.2.1)]], [[../01 Modelo do preset/Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)|09 - Especificação do preset piloto (TR 1.35.2.3)]], [[../01 Modelo do preset/Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)|10 - Especificação do preset piloto (TR 1.35.2.4)]], [[../01 Modelo do preset/Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)|11 - Especificação do preset piloto (TR 1.35.2.5)]], [[../01 Modelo do preset/Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)]], [[../01 Modelo do preset/Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)|13 - Especificação do preset piloto (TR 1.35.3)]], [[../01 Modelo do preset/Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)|14 - Especificação do preset piloto (TR 1.35.4)]], [[../01 Modelo do preset/Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)|15 - Especificação do preset piloto (TR 1.35.5)]], [[../01 Modelo do preset/Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)]], [[../01 Modelo do preset/Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)|17 - Especificação do preset piloto (TR 1.40.3)]], [[../01 Modelo do preset/Especificações do preset piloto/18 - Especificação do preset piloto (TR 1.41)|18 - Especificação do preset piloto (TR 1.41)]]
> **Fontes:** [[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem do caminho inicial),option(QA · Análise da demanda),option(QA · Plano de análise),option(QA · Mapeamento no TR),option(QA · Síntese visual),option(QA · Revisão da análise),option(QA · Especificação do preset (Fase 2)),option(QA · Modelo-alvo do preset (Fase 3)),option(QA · Mapeamento de fornecimento (Fase 4)),option(QA · Preparação técnica (Fase 5, futura)),option(Concluído)):etapa_atual]`

> [!info] Escopo desta pasta — Fase 1 e evidências atuais concluídas; caminho-base aprovado; modelo-alvo dos dados do preset aprovado; mapeamento de fornecimento concluído e aprovado
> Estrutura reorganizada em 08/10/2026 (autorização do Rafael). A abordagem anterior (investigação SGV-12082 original, ciclo SGV-11971, Roadmap e Mapa do seed) está arquivada para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]. **Fase 1:** esta frente mapeou atores, entidades, dados, estados e relações do TR completo — os 11 recortes foram aprovados pelo Rafael e revisados item a item contra o PDF (1.1–1.43); a revisão documental está registrada em [[04 - Revisão da análise]]. **Evidência atual:** as 17 fatias e a consolidação registram o que seed/testes Playwright demonstram hoje; isso informa possíveis reaproveitamentos, mas não limita o modelo-alvo. **Modelo-alvo:** [[../01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]] foi revisado e aprovado pelo Rafael/Codex (13/10/2026) — entidades, atributos, estados e relações necessários aos cenários de sanidade, com síntese visual Mermaid por grupo. **Mapeamento de fornecimento:** [[../01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]] foi revisada e aprovada pelo Rafael/Codex (13/10/2026) — canal candidato (`.env` individual, seed persistente ou cenário de teste) campo a campo, cobrindo C1–C6. **Próxima etapa, ainda futura:** decidir a preparação técnica/arquitetura por ambiente ou instância a partir dessas hipóteses — nenhuma arquitetura ou implementação foi iniciada. Dúvidas seguem explícitas e podem ser aprofundadas sem bloquear o restante (ver [[../01 Modelo do preset/00 - Mapa geral#Lacunas registradas (arestas tracejadas)|lacunas no mapa]]).

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
| Especificação do preset piloto (TR 1.24–1.27) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.28–1.29) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)|03 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.30–1.31) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)|04 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.32, 1.36–1.37) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.33) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)|06 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.34) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.2.1) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)|08 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.3) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)|09 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.4) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)|10 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.5) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)|11 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.2.6–1.35.2.7) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.3) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)|13 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.4) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)|14 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.35.5) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)|15 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.40.2–1.40.2.1) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|16 - Especificação do preset piloto]] |
| Especificação do preset piloto (TR 1.40.3) | ✅ Revisado e aprovado pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)|17 - Especificação do preset piloto]] |
| Consolidação da especificação do preset (Fase 2, passo 7 do Roadmap) | ✅ Revisada e aprovada pelo Codex — ver [[../01 Modelo do preset/02 - Visão consolidada do preset candidato|02 - Visão consolidada do preset candidato]] |
| Especificação do preset piloto (TR 1.41) | ✅ Revisada e aprovada pelo Codex — ver [[../01 Modelo do preset/Especificações do preset piloto/18 - Especificação do preset piloto (TR 1.41)|18 - Especificação do preset piloto]] |
| Triagem do caminho inicial do modelo-alvo (passo 8 do Roadmap) | ✅ Caminho-base aprovado para iniciar; extensões e dúvidas permanecem rastreadas em [[../01 Modelo do preset/03 - Triagem dos itens sem fatia (passo 8)|03 - Triagem dos itens sem fatia]] |
| Modelo-alvo dos dados do preset (Fase 3) | ✅ Revisado e aprovado pelo Rafael/Codex — ver [[../01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]] |
| Matriz de fornecimento dos dados (Fase 4, passo 10) | ✅ Revisada e aprovada pelo Rafael/Codex — ver [[../01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]] (C1–C6) |

**Próximo passo:** passo 11 — decidir a preparação técnica/arquitetura por ambiente/instância a partir das hipóteses de canal da matriz 05. Ainda futuro, não iniciado: nenhuma arquitetura ou implementação começou. As 17 fatias aprovadas e a [[../01 Modelo do preset/02 - Visão consolidada do preset candidato|visão consolidada]] continuam evidência técnica de referência. Não abrir fatias 19+ para repetir essa evidência.

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
│   ├── 02 - Visão consolidada do preset candidato.md  (evidências consolidadas das 17 fatias; não é o modelo-alvo)
│   ├── 03 - Triagem dos itens sem fatia (passo 8).md  (caminho-base aprovado; extensões e dúvidas permanecem abertas)
│   ├── 04 - Modelo-alvo dos dados do preset.md  (revisado e aprovado — Fase 3 concluída)
│   ├── 05 - Matriz de fornecimento dos dados.md  (artefato do passo 10, revisado e aprovado — escopo C1–C6 completo)
│   ├── Especificações do preset piloto/  (17 fatias aprovadas — evidência TR × seed/testes atuais)
│   └── Seções do TR/                  (uma nota por recorte — cobertura, elementos, relações, dúvidas, fontes — Fase 1)
└── Fontes/
    └── Termo de Referência SOGOV.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — esta frente não produz casos de teste nem preparação de Qase. O modelo-alvo (04) e a matriz de fornecimento (05, passo 10) estão aprovados; o próximo entregável é a decisão de preparação técnica do preset por ambiente/instância (passo 11), ainda futura e sem arquitetura/implementação iniciada.
