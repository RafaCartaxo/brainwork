---
tags:
  - qa
  - conhecimento
tipo: indice
---
# Índice: [QA-Automação] Termo de Referência SOGOV (SGV-11262)

A SGV-11262 é a demanda pai da iniciativa de QA sobre o Termo de Referência do SOGOV; esta pasta funciona como **contêiner/índice** — os artefatos específicos (demanda, plano, CTs, validação) ficam nos pacotes filhos.

> [!info] Papéis distintos — Roadmap × Índice
> **Roadmap** ([[../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]]): direção, sequência macro e dependências da frente ativa. **Índice (este arquivo):** só localizar documentos e pacotes — não repete a sequência nem o plano do Roadmap.

## Referência permanente (independente de qualquer demanda)

[[Sanidade automatizada do SOGOV - Termo de Referência/00 - Índice da sanidade automatizada do TR|Sanidade automatizada do SOGOV — Termo de Referência]] — a transcrição integral do TR, o modelo-alvo de atores/dados/estados e a matriz de fornecimento dos dados, organizados como referência permanente (não subordinada a nenhuma onda de cenários específica). Inclui o link para o hub no Notion (em organização). Produzida a partir dos artefatos aprovados da SGV-12082 (ver abaixo).

## Trabalho ativo

[[../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README|SGV-12200 — Levantamento da Onda 1 de cenários de sanidade]] — proposta rastreável de um primeiro lote de 20 cenários candidatos de sanidade, usando a referência permanente acima como base. Pendente de aprovação do Rafael; não é seleção oficial, CT, automação nem execução.

## Trabalho concluído nesta frente

[[../SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README|SGV-12082 — Mapeamento de atores e modelo do preset do TR]] — modelo conceitual de atores, entidades, configurações, estados, relações e dependências a partir do **TR completo** (itens 1.1–1.43), seguido da especificação de um preset candidato por cruzamento com seed/testes reais e do modelo-alvo/matriz de fornecimento dos dados. Não inclui casos de teste, Qase nem implementação de preset.

**Estado factual (corrigido em 15/10/2026 — divergência anterior identificada em auditoria):** Fase 1 (modelo conceitual, 11 recortes) concluída — aprovada pelo Rafael (08/10/2026) e revisada pelo Codex. Fase 2 (especificação do preset candidato) **concluída** — 17 fatias aprovadas (notas 02–18) e consolidadas. Passo 8 (caminho-base) **concluído e aprovado**. Modelo-alvo (04) e matriz de fornecimento (05, C1–C6) **concluídos e aprovados pelo Rafael/Codex em 13/10/2026**. Com isso, **a SGV-12082 foi encerrada neste escopo em 15/10/2026** (decisão do Rafael) — passos 1–10 da Sequência macro do Roadmap. O **passo 11** (preparação técnica/arquitetura do preset) permanece futuro, numa trilha separada que não bloqueia este encerramento nem a SGV-12200. Sequência completa e gates: [[../Roadmap - Modelo de atores e preset do TR|Roadmap]].

## Material arquivado para consulta

Arquivado para consulta em `Arquivo/Abordagem anterior/` — conteúdo preservado, referência histórica, não fluxo ativo; links de navegação foram ajustados quando necessário por causa da mudança de pasta.

- [[../Arquivo/Abordagem anterior/SGV-12082 - Análise do TR e preset de dados/00 QA/00 README|SGV-12082 — Análise do TR e preset de dados]] 🗄️ histórico/arquivado — **mesmo número de ticket (SGV-12082) da frente atual, título e pasta diferentes**; investigou automação e cobertura de CTs a partir do TR completo (DISC-001–004 + recomendação).
- [[../Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/00 README|SGV-11971 — TR 1.24-1.25 Autenticação e Ciclo de Vida]] 🗄️ histórico/arquivado — ciclo de automação dos itens 1.24–1.25, incluindo a [[../Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/00 QA/00 README|Entrega 01 — Baseline na instância 225]].
- [[../Arquivo/Abordagem anterior/Roadmap - Automação TR|Roadmap — Automação TR (anterior)]] e [[../Arquivo/Abordagem anterior/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] 🗄️ histórico/arquivado.

## Estrutura atual

```text
SGV-11262 - [QA-Automação] Termo de Referência SOGOV/
├── Conhecimento/                                              ← este índice
│   └── Sanidade automatizada do SOGOV - Termo de Referência/   ← referência permanente (TR, modelo-alvo, matriz)
├── Roadmap - Modelo de atores e preset do TR.md                ← direção/sequência da frente ativa
├── Arquivo/
│   └── Abordagem anterior/                                     ← material histórico arquivado para consulta
├── SGV-12082 - Mapeamento de atores e modelo do preset do TR/   ← encerrada neste escopo (15/10/2026)
└── SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/  ← frente ativa
```
