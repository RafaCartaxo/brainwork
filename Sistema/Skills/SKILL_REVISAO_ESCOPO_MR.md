---
tags:
  - qa
  - skill
---
# Skill: Revisão de Escopo de MR

Acessar um Merge Request do GitLab, confirmar que a correção implementada bate com o problema relatado (SGV/card), e levantar os cenários de teste automatizados implementados — sem análise profunda de código, só o suficiente pra decidir se a QA pode seguir pra validação real.

## Gatilhos

| Gatilho | Exemplo |
|---|---|
| Link de MR colado no chat | "verifica esse MR: `https://gitlab.sogo.com.br/.../merge_requests/N`" |
| Pedido explícito | "revisa o escopo do MR N", "confere se o MR bate com o problema" |

Junto com o link, Rafael frequentemente cola o problema original (descrição, passo a passo, critérios) — quando vier, é o material pra comparar contra a implementação, e pode virar card direto (ver "Card não existe" abaixo).

## 1. Acesso ao MR (sem precisar de token de API)

```bash
git fetch origin "+refs/merge-requests/<N>/head:mr-<N>"
```

Funciona com o remote git normal do repositório — não depende de PAT com escopo `api` (o token salvo no `git credential store` costuma ter só escopo de repositório) nem de sessão de navegador logada. Cria a ref local `mr-<N>` com o HEAD do MR.

## 2. Isolar o diff certo (cuidado com `origin/development` desatualizado)

`origin/development` local costuma estar dias/semanas atrás do real. Diffar direto contra ele traz ruído de MRs não relacionadas já mergeadas remotamente. Passo:

1. `git log mr-<N> --oneline` — achar os commits com `fix(SGV-XXXX)` ou `feat(SGV-XXXX)` no início do log (de trás pra frente, são os mais antigos da branch)
2. Achar o **pai** do commit mais antigo do SGV: `git log --oneline -1 <hash-do-commit-mais-antigo>^`
3. Usar esse pai como base: `git diff --stat <pai> mr-<N>` — isso isola só o que a branch de fato mudou, mesmo se `development` local estiver desatualizado

Se o pai já for um commit reconhecível de outro SGV (merge de branch), a base está certa.

## 3. Identificar o SGV e cruzar com o vault

O SGV vem no commit (`fix(SGV-XXXX): ...`). Buscar no vault:

- Existe card em `02 Demandas/`? → **Card existe** (seção 4)
- Existe só na Triagem de sprint, sem link real pro card? → **Card não existe** (seção 5) — não confiar na palavra da Triagem sem confirmar o arquivo
- Não existe em nenhum lugar? → idem, seção 5

## 4. Levantar os cenários de teste implementados

Nos arquivos `.test.ts` tocados pelo diff:

```bash
git show mr-<N>:<caminho/do/arquivo.test.ts> | grep -B1 -A2 "scenario(\|describe(\|it("
```

Listar os títulos em português dos `describe`/`scenario`/`it` novos ou alterados — isso é o que vai pro registro, não o código em si.

## 5. Checar escopo (sem profundidade)

Perguntas de sanidade, não auditoria de código:

- O nome da função/arquivo tocado tem relação óbvia com o problema relatado (ex.: `checkIfRemoveAnyInvalidSectorsBatch` bate com "lentidão")?
- Os cenários de teste cobrem o **sintoma relatado** (não só um mecanismo interno)?
- Existe algum valor/constante/comportamento entregue que **diverge** do que o critério de aceite pede? (ex.: timeout virou 10s quando o critério pedia 30s) — não deduzir se está certo ou errado, só **registrar a divergência**.
- Os testes medem o que o bug realmente é (ex.: performance/timeout) ou só a correção funcional ao redor? Sinalizar quando for só o segundo caso — não é falha do MR, é lacuna de cobertura automatizada que a validação manual precisa cobrir.

## 6. Dois caminhos de saída

### Card já existe

1. Comparar os cenários de teste com os critérios de aceite do card, um a um
2. Se bate: marcar a pendência correspondente na fila como `[x]`, com o resultado entre parênteses
3. Registrar no **Histórico** do card: `- YYYY-MM-DD - 🔎 Cenários de teste do MR revisados a nível de escopo (MR !N) — <resultado curto>`
4. Se achar algo fora do escopo original mas coberto pelo fix (ex.: revogação além de encerramento), registrar como achado — não é bloqueio, é possível gap de cobertura de CT pra próxima rodada

### Card não existe (mesmo que a Triagem diga que existe — confirmar sempre o arquivo)

Se o material recebido (colado no chat ou já conhecido) tem descrição, passo a passo e critérios completos → **modo B direto** ([[SKILL_LIMPEZA_EXPORT#B — Card direto (task completa)|SKILL_LIMPEZA_EXPORT]]), sem mesa de refinamento. Critérios de aceite do card **não são copiados verbatim** — são **reescritos conforme o que foi de fato implementado**:

- Critério que a implementação atende → mantém
- Critério que a implementação diverge (ex.: valor numérico diferente do pedido) → reescreve com o valor real entregue + callout `[!warning]` explicando a divergência e por que não foi simplesmente copiado
- Critério que a implementação não teve cobertura automatizada pra provar (ex.: comportamento sob volume/performance) → mantém como critério, mas marca que a prova é manual, não automatizada — normalmente isso é o CT mais importante do card

Se a Triagem de sprint tinha uma entrada desatualizada dizendo "já refinado/critérios no card" sem o card existir: corrigir a linha da Triagem (adicionar o link real, corrigir a data de conclusão) — é uma inconsistência de registro, não um erro de julgamento de quem triou.

## 7. Registro (igual nos dois caminhos)

- **Planejamento** da daily: `🔎 SGV-XXXX - Análise ([MR !N](link) — <resultado curto>)`, com callout de Detalhes explicando o fix e os achados
- **Auto-organização**: uma linha citando como o MR foi acessado (`git fetch` da ref) e o que resultou
- Card criado do zero: seguir também o registro do [[SKILL_LIMPEZA_EXPORT#Resultado Esperado|SKILL_LIMPEZA_EXPORT modo B]] (pendência de levar pro Notion, linha em Bugs encontrados)

## Exemplos reais (dia 20/07/2026 — 4 casos na mesma sessão)

| SGV | MR | Card | Achado |
|---|---|---|---|
| 9692 | !573 | Só na Triagem | N+1→lote; testes cobrem regra de negócio, não performance |
| 5783 | !581 | Só na Triagem | Fix pontual; 1 dos 4 testes reproduz o sintoma direto (raro e bom sinal) |
| 9750 | !583 | Existia (`02 Demandas/DEV/`) | Melhor cobertura dos 4 — bateu ponto a ponto com os 5 critérios |
| 8977 | !505 | Triagem dizia que existia, **não existia** | Card criado direto; timeout entregue (10s) diverge do critério pedido (30s) — critério reescrito com callout |

## Resultado Esperado

Decisão rápida — "dá pra seguir pra validação real" ou "achei algo que muda o critério" — sem virar code review completo. Rastro na daily e no card/Triagem sempre atualizado com a fonte real (link do MR), nunca só "revisado" sem contexto.
