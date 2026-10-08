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

## Trabalho ativo

[[../SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README|SGV-12082 — Mapeamento de atores e modelo do preset do TR]] — modelo conceitual de atores, entidades, configurações, estados, relações e dependências a partir do **TR completo** (itens 1.1–1.43). Não inclui casos de teste, Qase nem automação nesta demanda.

**Estado factual:** documentação/estrutura (demanda, plano de análise, matriz, mapa geral) preparada para revisão; o mapeamento do conteúdo do TR ainda não começou.

## Material arquivado para consulta

Arquivado para consulta em `Arquivo/Abordagem anterior/` — conteúdo preservado, referência histórica, não fluxo ativo; links de navegação foram ajustados quando necessário por causa da mudança de pasta.

- [[../Arquivo/Abordagem anterior/SGV-12082 - Análise do TR e preset de dados/00 QA/00 README|SGV-12082 — Análise do TR e preset de dados]] 🗄️ histórico/arquivado — **mesmo número de ticket (SGV-12082) da frente atual, título e pasta diferentes**; investigou automação e cobertura de CTs a partir do TR completo (DISC-001–004 + recomendação).
- [[../Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/00 README|SGV-11971 — TR 1.24-1.25 Autenticação e Ciclo de Vida]] 🗄️ histórico/arquivado — ciclo de automação dos itens 1.24–1.25, incluindo a [[../Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/00 QA/00 README|Entrega 01 — Baseline na instância 225]].
- [[../Arquivo/Abordagem anterior/Roadmap - Automação TR|Roadmap — Automação TR (anterior)]] e [[../Arquivo/Abordagem anterior/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] 🗄️ histórico/arquivado.

## Estrutura atual

```text
SGV-11262 - [QA-Automação] Termo de Referência SOGOV/
├── Conhecimento/                                              ← este índice
├── Roadmap - Modelo de atores e preset do TR.md                ← direção/sequência da frente ativa
├── Arquivo/
│   └── Abordagem anterior/                                     ← material histórico arquivado para consulta
└── SGV-12082 - Mapeamento de atores e modelo do preset do TR/   ← frente ativa
```
