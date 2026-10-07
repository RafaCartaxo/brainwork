---
tags:
  - qa
  - conhecimento
tipo: indice
---
# Índice: [QA-Automação] Termo de Referência SOGOV (SGV-11262)

> **Direção e sequência da iniciativa:** [[../Roadmap - Automação TR|Roadmap — Automação TR]]. **Inventário técnico do seed atual:** [[Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]]. Este índice fica dedicado à navegação e à localização dos ciclos e documentos.

Guarda-chuva do trabalho de QA sobre o **Termo de Referência do SOGOV**: verificar, ciclo a ciclo, se a plataforma atende ao que o Termo exige, com cobertura automatizada e evidência reproduzível. Sem card nem CTs próprios — a validação acontece pelos ciclos.

> [!info] Guarda-chuva aberta — 1 ciclo em andamento
> **Reorganizada em 02/10/2026.** Antes, a SGV-11262 era uma pasta só, que misturava o processo de verificação de TR (reaproveitável) com o conteúdo do único Termo já trabalhado (1.24-1.25). O ciclo 1.24-1.25 virou pacote próprio com SGV próprio — **SGV-11971** — e esta pasta passou a ser só a guarda-chuva. O pacote funcional original foi movido para `SGV-11971/Arquivo/`; as entregas novas ficam diretamente dentro da pasta SGV-11971, cada uma com QA e automação próprios. Um Termo novo entra como pacote irmão da 11971, sem duplicar estrutura.
>
> **Estrutura:** cada ciclo vive fisicamente dentro desta pasta (`SGV-<n> - <título>/`), junto com este `Conhecimento/`. Cada ciclo mantém seu próprio status no frontmatter (`ambiente:`/`status:`) e **não muda de pasta ao fechar** — mesma exceção consciente que a epic [[../../SGV-9296 - Departamentos/Conhecimento/0 - SGV-9296 - Índice|SGV-9296]] adota. A Dashboard ("Sem dono") lê o campo `ambiente:` do frontmatter antes do nome da pasta, então o aninhamento não esconde os cards.
>
> **Reorganizado em 07/10/2026:** a investigação do preset (antes "Entrega 02", aninhada dentro da SGV-11971) virou pacote próprio e irmão — **SGV-12082**, direto sob a SGV-11262 — porque seu escopo real é o Termo completo (itens 1.1–1.43), não só o ciclo 1.24-1.25. Decisão do Codex (planejador desta rodada), executada pelo Claude. A análise ativa está lá; as próximas implementações só serão abertas após sua recomendação.

## Ciclos

| Ciclo | SGV | O que cobre | Status |
|---|---|---|---|
| 1.24-1.25 | [[../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/01 - Demanda\|SGV-11971]] | Autenticação e ciclo de vida do usuário — tipos de acesso, validação de credenciais, bloqueio por tentativas e os estados Ativo/Licença/Férias/Inativo/Suspenso (itens 1.24 e 1.25, mais os correlatos 1.13 e 1.27.x) | 🔄 Em andamento — 25/38 CTs aprovados no histórico: 13 em Playwright (CT-001–012, CT-038) e 12 ainda em Cypress; 4 falharam, 6 bloqueados, 3 aguardam. Histórico em [[../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/01 Automação/02 - Validação automação\|placar arquivado]] |

## Investigação da iniciativa

| Investigação | Referência | Escopo | Status |
|---|---|---|---|
| [[../SGV-12082 - Análise do TR e preset de dados/00 QA/00 README\|SGV-12082 — Análise do TR e preset de dados]] | Iniciativa SGV-11262; PDF completo do Termo (itens 1.1–1.43); 38 CTs da [[../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste\|SGV-11971]] como cobertura existente de 1.24–1.25 | Entender o projeto de automação, mapear cobertura do TR completo, dados/ambientes e propor preset provável | 🔄 Em análise; levantamento pendente |

## Entregas dentro do ciclo 1.24-1.25

| Entrega | Referência | Escopo | Status |
|---|---|---|---|
| [[../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/00 QA/00 README\|Entrega 01 — Baseline na instância 225]] | Iniciativa SGV-11262; CTs da [[../SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/03 - Casos de teste\|SGV-11971]] | Piloto de seleção da instância 225 pelo seed | 🗄️ Histórico da hipótese; não executada nem validada; decisão técnica reaberta pela SGV-12082 |

## Como um ciclo é organizado

O pacote funcional original de cada ciclo segue `Sistema/Templates/Pacote/`. Entregas menores dentro do ciclo também seguem o mesmo padrão, mas cada uma é uma pasta filha própria com `00 QA/` e `01 Automação/`.

```text
SGV-<n> - TR <ciclo> <assunto>/
├── 00 QA/
│   ├── 00 README.md            ← estado do trabalho e próximo passo
│   ├── 01 - Demanda.md         ← itens do Termo viram critérios de aceite (C1..Cn)
│   ├── 02 - Plano de teste.md
│   ├── 03 - Casos de teste.md  ← fonte única dos CTs deste Termo
│   ├── 04 - Validação dev.md   ← conformidade por CT
│   └── 05 - Preparação Qase.md
└── 01 Automação/
    ├── 00 - Automação.md        ← estado resumido e navegação
    ├── 01 - Plano de automação.md
    └── 02 - Validação automação.md ← placar por CT
```

Os documentos antigos de SGV-11971 estão preservados em `Arquivo/` e podem ser consultados quando agregarem contexto. As entregas novas usam os templates atuais; handoff e documentação duplicada não são criados por padrão.

As pastas são numeradas (`00 QA/`, `01 Automação/`) só pra ordem de leitura/execução no explorador de arquivos — QA vem antes porque é o que se faz primeiro; automação é consequência, quando houver.

### Entregas menores dentro de um ciclo

Quando um ciclo específico (ex. 1.24-1.25) precisar de execução em fatias, cada entrega fica dentro da pasta do ciclo pai. O pai mantém os requisitos e CTs funcionais de origem; cada filha mantém o escopo, os critérios técnicos e a validação QA próprios, além do plano e placar de automação limitados aos CTs incluídos. Assim, a Entrega 01 pode validar quatro verificações do seed e automatizar CT-001–012 e CT-038 sem duplicar os casos funcionais da SGV-11971.

```text
SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/
├── Arquivo/                ← pacote funcional original e histórico preservados
│   ├── 00 QA/              ← fonte dos 38 CTs do ciclo
│   └── 01 Automação/       ← evidências e documentos anteriores
└── Entrega 01 - Baseline de autenticação na instância 225/
    ├── 00 QA/              ← escopo e quatro verificações técnicas do seed
    └── 01 Automação/       ← plano e placar de CT-001–012 e CT-038
```

**Investigações da iniciativa inteira** (escopo maior que um único ciclo, ex. o Termo completo) **não** ficam aninhadas dentro de um ciclo — vivem como pacote irmão, direto sob a SGV-11262:

```text
SGV-11262 - [QA-Automação] Termo de Referência SOGOV/
├── Conhecimento/
├── Roadmap - Automação TR.md
├── SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/   ← ciclo 1.24-1.25
└── SGV-12082 - Análise do TR e preset de dados/              ← investigação do Termo completo (1.1-1.43)
    ├── 00 QA/              ← demanda, matriz do preset, PDF fonte em Fontes/
    └── 01 Automação/        ← leitura técnica e placar da investigação
```

**O que é específico de um Termo/ciclo** (itens citados, CTs, placar, ids da Qase) vive no pacote do ciclo. **O que é da iniciativa inteira** (investigação, roadmap, preset) vive em pacotes irmãos sob a SGV-11262. **O que vale pra qualquer Termo** (o processo) vive fora, nas skills — não é duplicado aqui.

## Regras de uso (valem pra qualquer ciclo)

1. **A fonte dos CTs funcionais do ciclo atual permanece em `Arquivo/00 QA/03 - Casos de teste.md`; CTs técnicos específicos de uma entrega ficam no `03 - Casos de teste.md` da própria entrega.** Nunca editar um CT só na Qase ou só num script — o vault é quem manda.
2. **Toda correção de conteúdo segue a ordem:** atualizar o `03` primeiro, depois refletir na Qase (registrado no `05`).
3. **O `05` e a pasta `01 Automação/` não são passos 2 e 3 de uma sequência** — são dois consumidores independentes do `03`, em paralelo. Sincronizar com a Qase não depende da automação terminar, e vice-versa.
4. **Cada item do Termo vira um critério** no `01 - Demanda.md`, com o texto literal da regra e âncora `^cN`, para que todo CT seja rastreável até a redação original.

## Achados técnicos da Qase (valem pra qualquer sincronização futura)

Levantados na rodada de 31/08/2026 do ciclo 1.24-1.25:

- Import via CSV **não faz merge** — duplica casos existentes em vez de atualizar. Usar sempre a API REST.
- A API faz update parcial de verdade — **campo não enviado não é tocado**.
- `severity` / `type` / `automation` / `status` são **números** na API real, mesmo que o export mostre texto. Sempre confirmar contra um `GET` real (`--inspect`) antes de escrever.
- Exclusão via `DELETE` é definitiva, sem lixeira documentada — tratar como irreversível.
- A Qase tem shared steps nativos (`GET /v1/shared_step/{code}`) — conferir se já existem antes de escrever conteúdo novo.

Processo passo a passo e o script: [[../../../../../Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]] e `Sistema/Scripts/qase-sync/`. Pra um ciclo novo, copiar o `sync.js` da versão mais recente (`9296-departamentos/`), **não** da `11971-tr-1-24-1-25/`, que é mais simples e está congelada.

## Processo de automação

Não é duplicado aqui — está em [[../../../../../Sistema/Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]], que é a destilação do que foi aprendido no ciclo 1.24-1.25 (criar o card cedo, triagem de cada falha, nunca dar suíte por boa sem validação manual prévia, docs só por acréscimo).

> [!warning] A skill ainda descreve Cypress
> O repo `sogov-automation-test` migrou pra Playwright em setembro/2026 e **Playwright é o padrão** — teste novo só se escreve nele. A `SKILL_AUTOMACAO_TERMO_REFERENCIA` ainda precisa ser reconciliada com esse fluxo. Estado atual e convenção nova em [[../../../../04 Conhecimento/Referências/Automação Playwright|Automação Playwright]].

## Padrão reaproveitável

O template [[../../../../../Sistema/Templates/Verificação de Conformidade (Termo de Referência)|Verificação de Conformidade (Termo de Referência)]] descreve as 4 fases do trabalho de QA sobre um Termo — Análise → Casos de teste → Sincronização Qase → Automação. Essas fases **não** são subdivisões do requisito: elas mapeiam nos arquivos do pacote (`01` ← Análise, `03` ← Casos de teste, `05` ← Sincronização, `01 Automação/` ← Automação). A subdivisão do requisito é outra coisa — são as suites temáticas dentro do `03`.

## Histórico

- 2026-08-31 - Ciclo 1.24-1.25: casos de teste consolidados numa fonte única no vault, a partir de 3 versões divergentes
- 2026-08-31 - Ciclo 1.24-1.25: 39 casos sincronizados com a Qase (25 atualizados, 2 excluídos, 1 criado)
- 2026-08-31 - Ciclo 1.24-1.25: automação iniciada; captura de API da troca de status localizada, desbloqueando a Suíte 4 inteira
- 2026-09-01 - CT-015 contestado — validação manual do Rafael diverge do achado da automação; investigação de timing inconclusiva por instabilidade do ambiente
- 2026-09-02 - Card SGV-11262 criado (retroativo) e reestruturado como task pai do TR inteiro, com o template de Verificação de Conformidade; skill de automação de TR registrada
- 2026-09-25 - Scripts `qase-sync` movidos do repo `sogov-automation-test` pra `Sistema/Scripts/qase-sync/` no vault
- 2026-10-01 - Descoberto que o repo migrou pra Playwright (merge `1d78bf9`) sem registro no vault — nota [[../../../../04 Conhecimento/Referências/Automação Playwright|Automação Playwright]] criada. Suítes 3/4/5 (13 CTs) commitadas localmente (`bdf5e9a`); não sobem em Cypress, serão portadas
- 2026-10-02 - SGV-11262 vira guarda-chuva de automação de Termo de Referência; o ciclo 1.24-1.25 ganha SGV próprio (SGV-11971) e vira pacote no padrão da epic SGV-9296
- 2026-10-07 - Índice atualizado: 13 CTs Playwright (CT-001–012 e CT-038); 12 aprovados seguem associados ao Cypress. A análise SGV-12082 foi definida como próximo passo; o piloto da instância 225 fica histórico até a recomendação baseada no levantamento.
