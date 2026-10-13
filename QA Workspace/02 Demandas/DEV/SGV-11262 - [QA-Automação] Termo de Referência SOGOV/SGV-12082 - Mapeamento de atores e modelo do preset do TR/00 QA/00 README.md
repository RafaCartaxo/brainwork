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
> **Visão consolidada do preset candidato:** [[../01 Modelo do preset/02 - Visão consolidada do preset candidato]]
> **Triagem dos itens sem fatia (passo 8):** [[../01 Modelo do preset/03 - Triagem dos itens sem fatia (passo 8)]]
> **Especificação do preset piloto:** [[../01 Modelo do preset/Especificações do preset piloto/02 - Especificação do preset piloto (TR 1.24–1.27)|02 - Especificação do preset piloto (TR 1.24–1.27)]], [[../01 Modelo do preset/Especificações do preset piloto/03 - Especificação do preset piloto (TR 1.28–1.29)|03 - Especificação do preset piloto (TR 1.28–1.29)]], [[../01 Modelo do preset/Especificações do preset piloto/04 - Especificação do preset piloto (TR 1.30–1.31)|04 - Especificação do preset piloto (TR 1.30–1.31)]], [[../01 Modelo do preset/Especificações do preset piloto/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)]], [[../01 Modelo do preset/Especificações do preset piloto/06 - Especificação do preset piloto (TR 1.33)|06 - Especificação do preset piloto (TR 1.33)]], [[../01 Modelo do preset/Especificações do preset piloto/07 - Especificação do preset piloto (TR 1.34)|07 - Especificação do preset piloto (TR 1.34)]], [[../01 Modelo do preset/Especificações do preset piloto/08 - Especificação do preset piloto (TR 1.35.2.2.1)|08 - Especificação do preset piloto (TR 1.35.2.2.1)]], [[../01 Modelo do preset/Especificações do preset piloto/09 - Especificação do preset piloto (TR 1.35.2.3)|09 - Especificação do preset piloto (TR 1.35.2.3)]], [[../01 Modelo do preset/Especificações do preset piloto/10 - Especificação do preset piloto (TR 1.35.2.4)|10 - Especificação do preset piloto (TR 1.35.2.4)]], [[../01 Modelo do preset/Especificações do preset piloto/11 - Especificação do preset piloto (TR 1.35.2.5)|11 - Especificação do preset piloto (TR 1.35.2.5)]], [[../01 Modelo do preset/Especificações do preset piloto/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)]], [[../01 Modelo do preset/Especificações do preset piloto/13 - Especificação do preset piloto (TR 1.35.3)|13 - Especificação do preset piloto (TR 1.35.3)]], [[../01 Modelo do preset/Especificações do preset piloto/14 - Especificação do preset piloto (TR 1.35.4)|14 - Especificação do preset piloto (TR 1.35.4)]], [[../01 Modelo do preset/Especificações do preset piloto/15 - Especificação do preset piloto (TR 1.35.5)|15 - Especificação do preset piloto (TR 1.35.5)]], [[../01 Modelo do preset/Especificações do preset piloto/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)]], [[../01 Modelo do preset/Especificações do preset piloto/17 - Especificação do preset piloto (TR 1.40.3)|17 - Especificação do preset piloto (TR 1.40.3)]], [[../01 Modelo do preset/Especificações do preset piloto/18 - Especificação do preset piloto (TR 1.41)|18 - Especificação do preset piloto (TR 1.41)]]
> **Fontes:** [[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de análise),option(QA · Mapeamento no TR),option(QA · Síntese visual),option(QA · Revisão da análise),option(QA · Especificação do preset (Fase 2)),option(Concluído)):etapa_atual]`

> [!info] Escopo desta pasta — Fase 1 concluída (11 recortes); Fase 2 em andamento (17 fatias + consolidação revisada e aprovada); próximo passo é concluir a triagem (passo 8 do Roadmap)
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
| Triagem de pendências do TR sem fatia própria (Fase 2, passo 8 do Roadmap) | 🔵 Em andamento — recorte 07 (cluster 1.35, parcial), recorte 08 (1.38–1.40, parcial), recorte 10 (1.42) e recorte 11 (1.43) aguardam decisão item a item; levantamento em [[../01 Modelo do preset/03 - Triagem dos itens sem fatia (passo 8)|03 - Triagem dos itens sem fatia]], em revisão do Codex |

**Próximo passo:** concluir a triagem item a item dos requisitos ainda sem fatia própria — recorte 07 (1.35, 1.35.1, 1.35.2.1; 1.35.2 e 1.35.2.2 são introdutórios, sem decisão autônoma), recorte 08 (1.38, 1.39, 1.40.1, 1.40.4–1.40.6), recorte 10 (1.42) e recorte 11 (1.43). Para cada item, registrar evidência consultada e decidir se requer uma fatia de especificação do preset ou se fica fora/não aplicável, com justificativa. Levantamento consolidado em [[../01 Modelo do preset/03 - Triagem dos itens sem fatia (passo 8)|03 - Triagem dos itens sem fatia]] — ainda **proposta em revisão do Codex, não decisão final do passo 8**. Lista completa das fatias e a régua de classes seguem em [[../01 Modelo do preset/02 - Visão consolidada do preset candidato|02 - Visão consolidada do preset candidato]] e no passo 8 do [[../../Roadmap - Modelo de atores e preset do TR|Roadmap]]. **Não abrir fatia 19 ou posterior antes de concluir essa triagem.** A dúvida de negócio sobre Canal Oficial (1.38.1.b) e Jornal Oficial (1.38.3.1) foi esclarecida no contexto do produto atual (mesmo fluxo de divulgação externa — ver [[../01 Modelo do preset/Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)#Contexto de produto verificado em documentação|recorte 08]]); demais dúvidas de negócio seguem no [[../01 Modelo do preset/00 - Mapa geral#Lacunas registradas (arestas tracejadas)|mapa geral]], sem bloquear itens que não dependam delas.

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
│   ├── 02 - Visão consolidada do preset candidato.md  (consolidação das 17 fatias aprovadas — Fase 2, passo 7 do Roadmap)
│   ├── 03 - Triagem dos itens sem fatia (passo 8).md  (levantamento dos itens sem fatia própria — Fase 2, passo 8, em revisão do Codex)
│   ├── Especificações do preset piloto/  (17 fatias aprovadas — TR × seed/testes reais; lista completa e navegável na tabela "Status do trabalho" acima)
│   └── Seções do TR/                  (uma nota por recorte — cobertura, elementos, relações, dúvidas, fontes — Fase 1)
└── Fontes/
    └── Termo de Referência SOGOV.pdf             (cópia de trabalho; original preservado no Arquivo)
```

Esta pasta não tem `03 - Casos de teste`, `05 - Preparação Qase` nem `01 Automação/` — esta frente não produz casos de teste nem preparação de Qase; uma eventual frente para isso seria definida à parte, sem fase atribuída por enquanto. Automação/implementação de preset também não acontece aqui (nem na Fase 1, nem na Fase 2) — a Fase 3 do Roadmap trata só da decisão/desenho do preset persistente, não de CTs/Qase.
