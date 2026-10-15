---
tags: [qa]
task: "SGV-12200"
pai: "SGV-11262"
tipo: "levantamento-cenarios"
status: rascunho
ambiente: dev
prioridade: media
etapa_atual: "QA · Proposta da Onda 1 (pendente de aprovação do Rafael)"
modulo: ""
responsavel: ""
aguardando: "Rafael"
cadastrado_por: ""
data_inicio: "15/10/2026"
data_fim: ""
pontos: ""
---
# SGV-12200 — Levantamento da Onda 1 de cenários de sanidade

> [!info]- Navegação QA
> **Índice da iniciativa:** [[../../Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]]
> **Roadmap da iniciativa:** [[../../Roadmap - Modelo de atores e preset do TR|Roadmap — Modelo de atores e preset do TR]]
> **Proposta da Onda 1:** [[01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]]
> **Frente de origem (encerrada, usada como referência):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README|SGV-12082 — Mapeamento de atores e modelo do preset do TR]]
> **Modelo-alvo dos dados do preset (04):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]]
> **Matriz de fornecimento dos dados (05):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]]
> **Fonte original da SGV-12200 (export Notion):** `Downloads/SGV-12200 - [Automação][Sanidade] -  3 | Notion.md` (fora do vault; cópia de referência, não duplicada aqui)

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(rascunho),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Proposta da Onda 1 (pendente de aprovação do Rafael)),option(QA · Onda 1 aprovada),option(QA · Preparação de CTs (futura)),option(Concluído)):etapa_atual]`

> [!important] Rascunho pendente de aprovação do Rafael — não é seleção oficial, CT, automação ou execução
> O export disponível da SGV-12200 (ver fonte acima) não lista os 20 testes nem seus critérios de seleção — só registra o objetivo ("levantar tudo que será necessário para criar os 20 testes iniciais específicos de sanidade") e a ação de falar com Alice sobre uma página no Notion. Diante dessa lacuna, Rafael decidiu (15/10/2026) que a frente **propõe** — em vez de esperar — uma primeira **Onda de 20 cenários candidatos de sanidade**, construída a partir do Termo de Referência e dos artefatos já aprovados da SGV-12082 (04/05), com ondas adicionais de 20 previstas para rodadas futuras. Esta é uma **proposta rastreável para validação**, não uma lista aprovada: cada linha cita sua referência exata do TR e sua razão de entrada na onda 1; nenhuma foi escolhida só por já existir um CT/automação correspondente.

## Escopo desta pasta

- Propor a Onda 1 (20 cenários candidatos), rastreável ao TR e aos artefatos 04/05 da SGV-12082 — ver [[01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|01 - Proposta da Onda 1]].
- Propor a organização do conteúdo da SGV-11262/SGV-12082 útil para uma futura página no Notion (TR normativo, 11 recortes, mapa geral, matriz de atores, 04 e 05) — sem despejar as 17 fatias de evidência técnica.
- Registrar a conversa com Alice (reservar página no Notion) como pendência operacional explícita.

## Fora de escopo nesta pasta

- Selecionar os 20 cenários como decisão final — a Onda 1 é proposta, pendente de aprovação do Rafael.
- Redigir CTs formais, implementar automação, executar ou validar qualquer cenário.
- Decidir a preparação técnica/arquitetura do preset (passo 11 da SGV-12082) — trilha futura e separada, não tratada aqui.
- Contatar Alice, criar página no Notion ou transferir/publicar qualquer conteúdo — não há conector de escrita disponível nesta sessão, e a ação depende de decisão humana.
- Reabrir ou alterar conteúdo já aprovado da SGV-12082 (TR, recortes, mapa, matriz de atores, 04, 05) — tudo usado só por referência/link.

## Pacote para `SGV-12200`

```text
SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/
└── 00 QA/
    ├── 00 README.md
    └── 01 - Proposta da Onda 1 (cenários candidatos e organização no Notion).md
```

Esta pasta não duplica o PDF do TR, os 11 recortes nem as 17 fatias da SGV-12082 — toda referência é por link relativo. Não tem `Fontes/` própria nem pasta de automação.
