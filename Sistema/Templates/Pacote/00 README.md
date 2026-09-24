---
tags: [qa]
task: "<ID>"
pai: ""
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
# <ID> — <título curto orientado ao resultado>

> [!info]- Navegação QA/DEV
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda/Bug | ⏳ |
| Plano de teste | ⏳ |
| Casos de teste | ⏳ |
| Validação | ⏳ |
| Preparação Qase | ⏳ |

**Próximo passo:** <registrar a próxima ação objetiva>.

> [!tip]- Esforço
> ```dataviewjs
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + dv.current().file.folder + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos`);
> dv.table(["Artefato", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço total do pacote:** ${total} pontos`);
> ```
>
> A busca por pasta (`dv.pages(file.folder)`) já inclui a subpasta `Defeitos/` automaticamente — não precisa de um bloco separado somando defeitos filhos (diferente do operating-vault, onde o pacote QA e o pacote DEV ficam em pastas irmãs distintas).

Pacote para `<ID>`:

```text
<ID> - <título>/
├── 00 README.md
├── 01 - Demanda.md          (ou 01 - Bug.md)
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
├── 05 - Preparação Qase.md
└── Defeitos/                (só se houver CT reprovado — ver Sistema/Skills/SKILL_BUGS.md)
```

---
