---
tags: [qa, automacao]
task: "Entrega 01"
pai: SGV-11971
tipo: melhoria
status: backlog
ambiente: hml
prioridade: media
etapa_atual: "QA · Análise da demanda"
modulo: Automação
responsavel: ""
aguardando: "Confirmar backend da instância 225 e destino do CT-038"
cadastrado_por: ""
data_inicio: ""
data_fim: ""
---

# Entrega 01 — Baseline de autenticação na instância 225

> [!info]- Navegação QA/DEV
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos desta entrega:** [[03 - Casos de teste]]
> **Validação QA:** [[04 - Validação dev]]
> **Automação:** [[../01 Automação/00 - Automação|Pacote de automação]]
> **SGV-11971 — casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste]]
> **Roadmap da iniciativa:** [[../../../Roadmap - Automação TR|Roadmap SGV-11262]]

> [!settings]- Controle da entrega
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Escopo e critérios registrados |
| Plano de teste | ✅ Preparado |
| Casos desta entrega | ✅ Quatro verificações técnicas; CTs funcionais permanecem na SGV-11971 |
| Validação QA | ⏳ Aguardando implementação e execução |
| Preparação Qase | — Não se aplica: não duplicar os CTs funcionais já existentes na Qase |
| Automação | 📋 Pacote próprio 00–02 preparado |

**Próximo passo:** ajustar o seed para selecionar a instância 225 com validação de identidade e sem fallback de criação. Antes de executar, confirmar que a configuração aponta ao backend onde a instância foi criada.

A SGV-11971 continua sendo a demanda-pai deste ciclo. Esta entrega trata somente da preparação do baseline de autenticação na instância 225. Os 13 CTs funcionais são referenciados da SGV-11971, sem cópia ou renumeração. As verificações específicas do seed estão nesta entrega.

O pacote ainda não tem ID de demanda filha no tracker. Não foi criado nem presumido um novo número SGV.

> [!tip]- Esforço e capacidade
> ```dataviewjs
> const raizDoPacote = dv.current().file.folder.split("/").slice(0, -1).join("/");
> const atual = dv.current().pontos;
> const paginas = dv.pages('"' + raizDoPacote + '"').where(p => typeof p.pontos === "number");
> const total = paginas.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);
> dv.paragraph(`**Esforço desta etapa:** ${typeof atual === "number" ? atual : "a definir"} pontos`);
> dv.table(["Artefato", "Pontos"], paginas.sort(p => p.file.name).map(p => [p.file.link, p.pontos]));
> dv.paragraph(`**Esforço total do pacote:** ${total} pontos`);
> const demanda = dv.pages('"' + raizDoPacote + '"').where(p => p.pontos_alocados !== undefined && p.pontos_alocados !== "").first();
> if (demanda) {
>   const alocado = Number(demanda.pontos_alocados || 0);
>   const diferenca = alocado - total;
>   dv.paragraph(`**Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);
> } else {
>   dv.paragraph("`pontos_alocados` ainda não preenchido na Demanda — sem comparação de capacidade.");
> }
> ```
> A consulta parte de `00 QA/` e sobe até a raiz da entrega para incluir também `01 Automação/`.

## Estrutura desta entrega

```text
Entrega 01 - Baseline de autenticação na instância 225/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de teste.md
│   ├── 03 - Casos de teste.md
│   └── 04 - Validação dev.md
└── 01 Automação/
    ├── 00 - Automação.md
    ├── 01 - Plano de automação.md
    └── 02 - Validação automação.md
```

A nota `05 - Preparação Qase` não se aplica nesta entrega: os CTs funcionais já pertencem à Qase da SGV-11971, e as quatro verificações do seed são critérios técnicos internos. Criar `05` somente em entregas com casos próprios que precisem ser sincronizados.

