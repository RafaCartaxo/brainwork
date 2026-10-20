---
tags: [qa]
task: "SGV-12272"
pai: ""
tipo: "casos-de-teste"
status: backlog
ambiente: dev
prioridade: media
etapa_atual: "QA · Triagem"
modulo: ""
responsavel: ""
aguardando: ""
cadastrado_por: ""
data_inicio: "19/10/2026"
data_fim: ""
pontos: ""
---
# SGV-12272 — Casos de teste e publicação da Onda 1 de sanidade do TR

> [!important] Origem: Onda 1 aprovada na SGV-12200 (19/10/2026)
> Esta demanda nasce da aprovação da Onda 1 de 20 cenários candidatos de sanidade, selecionados e aprovados por Rafael na [[../../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README|SGV-12200 — Levantamento da Onda 1 de cenários de sanidade]] (ver a [[../../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|Proposta da Onda 1]] e a página Notion da task). **A seleção dos 20 cenários não é reaberta aqui** — esta demanda transforma essa seleção já aprovada em artefatos formais.

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Origem (SGV-12200):** [[../../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README|SGV-12200 — Levantamento da Onda 1 de cenários de sanidade]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(QA · Preparação Qase),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ⏳ |
| Plano de teste | ⏳ |
| Casos de teste | ⏳ |
| Validação | ⏳ |
| Preparação Qase | ⏳ |
| Publicação no Notion | ⏳ |

**Próximo passo:** redigir os 20 CTs em `03 - Casos de teste.md`, a partir dos 20 cenários aprovados na Proposta da Onda 1 (SGV-12200). Nenhum CT foi redigido e nenhum conteúdo foi publicado no Notion ainda.

> [!tip]- Esforço e capacidade
> ```dataviewjs
> const raizDoPacote = dv.current().file.folder.split("/").slice(0, -1).join("/");
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + raizDoPacote + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos`);
> dv.table(["Artefato", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço total do pacote:** ${total} pontos`);
>
> const demanda = dv.pages('"' + raizDoPacote + '"').where(p => p.pontos_alocados !== undefined && p.pontos_alocados !== "").first();
> if (demanda) {
>   const alocado = Number(demanda.pontos_alocados || 0);
>   const diferenca = alocado - total;
>   dv.paragraph(`**Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> } else {
>   dv.paragraph("`pontos_alocados` ainda não preenchido em 01-Demanda — sem comparação de capacidade.");
> }
> ```

Pacote para `SGV-12272`:

```text
SGV-12272 - Casos de teste e publicação da Onda 1 de sanidade do TR/
└── 00 QA/
    ├── 00 README.md
    ├── 01 - Demanda.md
    ├── 02 - Plano de teste.md
    ├── 03 - Casos de teste.md
    ├── 04 - Validação dev.md
    └── 05 - Preparação Qase.md
```

Sem pasta `01 Automação/` — automação não faz parte do escopo desta demanda (ver `01 - Demanda.md`, Fora de escopo).

A numeração das pastas (`00 QA/`) é só pra ordem de leitura/execução no explorador de arquivos — nada no conteúdo ou nos links depende dela além do nome literal da pasta.

---
