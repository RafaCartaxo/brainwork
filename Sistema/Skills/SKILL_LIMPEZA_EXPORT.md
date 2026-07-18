---
tags:
  - qa
  - skill
---
# Skill: Limpeza de Export do Notion

Transformar .md bruto exportado do Notion em conteúdo limpo, pronto pra envelopar no [[../Templates/Refinamento.md|Refinamento.md]] ou criar card direto.

## O que remover (lixo de export)

- Metadados de sprint, revisores, datas de workflow, progresso, prioridade
- Campos vazios herdados do template do Notion (ex.: "Responsável:", "Data de início:", listas de propriedades sem valor)
- Artefatos de export (timestamps, IDs internos do Notion, headers de coluna de board)
- Status/progresso da task no Notion (não importa no card do vault)
- Listas de campos preenchidos automaticamente (data de criação, última modificação)

## O que manter (conteúdo útil pro QA)

- **Descrição da task** — com autoria quando disponível ("Fulano em DD/MM/AAAA:")
- **Saída esperada** — comportamento correto
- **Saída atual** — comportamento incorreto observado
- **Entrega do dev** — autor, data, link do MR, status de review, arquivos tocados (se houver)
- **Passo a passo, evidências, critérios de aceite, ambiente** — se existirem no export

## O que identificar como lacuna (vira item em Pontos a definir)

- Task sem passo a passo → `- [ ] Passo a passo ausente — definir como reproduzir`
- Task sem evidência → `- [ ] Sem evidência no export — solicitar ou reproduzir`
- Regra de negócio ambígua → `- [ ] Regra X ambígua — confirmar com dev/produto`
- Sem ambiente definido → assumir DEV e anotar
- Task sem critérios de aceite → `- [ ] Critérios de aceite ausentes — definir a partir das regras`

## Modos de saída

### A — Envelopar no Refinamento.md (task incompleta/ambígua)

Quando a task **não** está pronta pra virar card direto — falta informação, regras ambíguas, precisa de análise.

O conteúdo limpo é distribuído nas seções do [[../Templates/Refinamento.md|Refinamento.md]]:
- Descrição + Saída esperada + Saída atual → `## O problema`
- Entrega do dev → `## O problema` (seção "Entrega do dev")
- Lacunas identificadas → `## Pontos a definir`
- Análise e Destilado ficam vazios — preenchidos em rodadas seguintes

O arquivo envelopado fica em `05 Refinar/` com `status: em_refinamento`.

### B — Card direto (task completa)

Quando a task já vem **completa** do Notion: descrição clara, passo a passo, critérios de aceite, ambiente definido. **Pular a mesa.**

- Bug → criar card em `02 Demandas/<ambiente>/` via [[SKILL_BUGS\|SKILL_BUGS]]
- Melhoria/Funcionalidade/POC → criar card via [[../Templates/Demanda.md\|Demanda.md]]

Na daily: `📝 SGV-XXXX - <Tipo> refinado(a) (card criado direto do export)`.

### C — Documentação (não é task)

Quando o export é documentação de referência do sistema — não tem SGV, não descreve um problema. 

Classificar o tipo:
- Módulo do sistema → `04 Conhecimento/Módulos/`
- Fluxo ponta a ponta → `04 Conhecimento/Fluxos/`
- Referência externa (repo, lei, manual) → `04 Conhecimento/Referências/`

Template: [[../Templates/Conhecimento.md\|Conhecimento.md]].

Na daily: `📚 <Doc> - Documentação importada (<escopo curto>)` em Planejamento.

## Resultado Esperado

Conteúdo limpo e classificado, pronto pro próximo passo (mesa, card ou base de conhecimento), sem lixo de export e com lacunas explicitamente identificadas.
