---
tags: [qa]
task: "Entrega 01"
pai: SGV-11971
tipo: melhoria
status: analise
ambiente: hml
prioridade: media
etapa_atual: "QA · Análise da demanda"
modulo: Automação
responsavel: ""
aguardando: "Confirmar backend da instância 225 e destino do CT-038"
cadastrado_por: ""
data_inicio: ""
data_fim: ""
pontos: ""
---
# Entrega 01 — Baseline de autenticação na instância 225

> [!info]- Navegação QA/DEV
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|SGV-11971]]
> **Roadmap:** [[../../../Roadmap - Automação TR|SGV-11262]]
> **Preparação Qase:** Não se aplica; os casos funcionais já pertencem à Qase da SGV-11971 e os casos de seed são técnicos.
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — quando a automação for planejada; antes de começar a codar)*

> [!settings]- Controle do card
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda/Bug | ✅ Escopo e critérios definidos; sem ID próprio no tracker |
| Plano de teste | ✅ Preparado para as quatro verificações do seed e os 13 CTs funcionais |
| Casos de teste | ✅ Quatro verificações técnicas; CTs funcionais referenciados da SGV-11971 |
| Validação | ⏳ Aguardando implementação e execução |
| Preparação Qase | — Não se aplica nesta entrega |
| Automação | 📋 Pacote `00–02` preparado; implementação pendente |

**Próximo passo:** confirmar o backend da instância 225 e resolver o destino do CT-038; em seguida, implementar a seleção explícita e segura da instância no seed.

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
>   dv.paragraph("`pontos_alocados` ainda não preenchido em 01-Demanda/01-Bug — sem comparação de capacidade.");
> }
> ```
>
> A busca sai de `00 QA/` (pasta deste arquivo) e sobe um nível até a raiz do pacote, pra incluir `01 Automação/` e `Defeitos/` automaticamente — não precisa de bloco separado somando cada subpasta. `pontos_alocados` fica só em `01-Demanda`/`01-Bug` (não duplicado aqui) — este bloco lê de lá pra calcular saldo/déficit.

Pacote para `Entrega 01`:

```text
Entrega 01 - Baseline de autenticação na instância 225/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de teste.md
│   ├── 03 - Casos de teste.md
│   └── 04 - Validação dev.md
├── 01 Automação/                (quando houver cobertura automatizada)
│   ├── 00 - Automação.md        entrada, configuração e próxima ação
│   ├── 01 - Plano de automação.md escopo, estratégia, dados e dependências
│   └── 02 - Validação automação.md placar atual por CT
└── Defeitos/                    (só se houver CT reprovado — ver Sistema/Skills/SKILL_BUGS.md; numerada por último de propósito — é exceção, não parte da sequência QA → Automação)
```

A nota `05 - Preparação Qase` não foi criada porque esta entrega não adiciona casos funcionais à Qase. Os CTs de autenticação são mantidos no pacote funcional arquivado da SGV-11971; aqui ficam apenas os critérios técnicos do seed.

A numeração das pastas (`00 QA/`, `01 Automação/`) indica a ordem de leitura: primeiro a demanda e seus testes, depois a automação.

---
