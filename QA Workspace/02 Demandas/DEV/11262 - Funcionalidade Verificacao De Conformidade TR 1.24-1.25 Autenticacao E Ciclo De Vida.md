---
tags:
  - demanda
  - qa
  - funcionalidade
  - termo-de-referencia
  - autenticacao
task: "11262"
pai: ""
status: em andamento
prioridade: media
data_inicio: 2026-08-31
responsavel: Rafael
modulo: autenticacao
---
# Demanda: Verificação de Conformidade — TR 1.24-1.25 (Autenticação e ciclo de vida do usuário)

> [!info] Informações
> - **Tipo:** Funcionalidade (verificação de conformidade com Termo de Referência) — task **pai**, guarda-chuva das 4 partes abaixo
> - **Responsável QA:** Rafael
> - **Vault:** [[QA Workspace/07 Termo de Referência/1.24-1.25/1.24-1.25 - Handoff Geral|Handoff Geral]] (visão de conjunto) · [[QA Workspace/07 Termo de Referência/1.24-1.25/README|pasta do Termo]]
> - **Padrão reaproveitável:** [[Sistema/Templates/Verificação de Conformidade (Termo de Referência)|Template — Verificação de Conformidade]] (usar pro próximo Termo de Referência)

---

> [!abstract] Resumo

Verificação de conformidade do Sogov com os itens **1.24** e **1.25** do Termo de Referência (Autenticação e ciclo de vida do usuário — tipos de acesso, validação de credenciais, bloqueio por tentativas, ciclo de vida Ativo/Licença/Férias/Inativo/Suspenso). Decomposta em 4 partes sequenciais; por enquanto todas registradas aqui como seções — se alguma crescer o suficiente, vira task própria (SGV) depois, com esta como `pai:`.

---

## Partes

| Parte | O que cobre | Status |
|---|---|---|
| 1. Análise | Leitura do Termo original, extração dos itens 1.24/1.25, primeira formalização dos casos de teste | ✅ Concluída (histórica, anterior a esta task) |
| 2. Casos de teste | Consolidação de 3 versões divergentes numa fonte única no vault | ✅ Concluída (31/08) |
| 3. Sincronização com a Qase | Alinhamento dos 39 casos no projeto Qase via API | ✅ Concluída (31/08) |
| 4. Automação | Cobertura automatizada (Cypress) dos 38 CTs, validada contra homolog | 🔄 Em andamento — 25/38 confirmados, 12/38 já em MR |

---

## Parte 1 — Análise

Antes de existir uma fonte única de casos de teste, o Termo já tinha sido lido e transformado em CTs em **3 documentos separados e divergentes** (planilha original de Execução, uma versão "organizada para Qase", e uma versão em Gherkin no vault) — cada um capturando parte da informação, sem estarem sincronizados entre si. Essa divergência é o que a Parte 2 resolveu.

> Não há um registro detalhado de quando/como essa primeira leitura do Termo aconteceu (é anterior ao início do rastreamento desta task) — os 3 documentos-fonte são o artefato que sobrou dela.

---

## Parte 2 — Casos de teste

✅ Concluída em 31/08. As **3 versões divergentes** foram consolidadas em **1 arquivo canônico**: 38 CTs ativos (+ 3 extras fora de escopo), cada um com Dado/Quando/Então, Prioridade, Requisito e Citação do Termo (texto literal da regra, conferido contra o PDF original).

Correções de conteúdo feitas no caminho: precondição do CT-003 (cidadão PJ), granularidade do CT-018/019, e os nomes de nível de permissão do CT-020 (eram "Assistente/Auxiliar/Visualizador" — não existem no sistema; certo é **Especialista/Usuário básico/Somente leitura**, confirmado em 4 fontes: i18n da aplicação, migration do banco, docs de business-rules do QA, nota do vault).

Detalhe: [[QA Workspace/07 Termo de Referência/1.24-1.25/01 Casos de Teste/1.24-1.25 - Casos de Teste|Casos de Teste]].

---

## Parte 3 — Sincronização com a Qase

✅ Concluída em 31/08. A Qase (projeto `SGV`) estava desatualizada em relação ao vault: 23 casos vazios, 1 corrompido, 2 com regra já corrigida no vault mas não lá. Sincronizado via **API REST** (não CSV — duplica em vez de atualizar):

- 25 casos atualizados, 2 excluídos (órfãos já absorvidos), 1 criado (equivalente ao CT-017, desbloqueio manual).
- Ferramenta reutilizável em `sogov-automation-test/scripts/qase-sync-1.24-1.25/` — serve de modelo pro próximo Termo de Referência.
- `priority` deixado de fora de propósito (preencher manualmente na Qase depois).

Detalhe: [[QA Workspace/07 Termo de Referência/1.24-1.25/02 Sincronização Qase/1.24-1.25 - Sincronização com a Qase|Sincronização com a Qase]].

---

## Parte 4 — Automação

🔄 Em andamento. Cypress, repo `sogov-automation-test`. **Rafael entra de férias em 04/09, volta 24/09 (quinta)** — ver [[QA Workspace/07 Termo de Referência/1.24-1.25/03 Automação/1.24-1.25 - Retomada (volta 24-09)|nota de retomada]] pra retomar rápido. Detalhe completo e atualizado a cada rodada: [[QA Workspace/07 Termo de Referência/1.24-1.25/03 Automação/1.24-1.25 - Handoff de execução|Handoff de execução]] · [[Sistema/Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]] (processo).

### Suítes e status atual

| Suíte | CTs | Status |
|---|---|---|
| 1. Tipos de acesso | CT-001 a 009 (9) | ✅ Confirmados — branch `tr-1.24-1.25-auth-suite-1-2` no ar, MR a criar/confirmar |
| 2. Validação de credenciais | CT-010 a 012 (3) | ✅ Confirmados — mesma branch |
| 3. Bloqueio por tentativas | CT-013, 014, 018, 019 (4) | ✅ Confirmados — não commitado ainda |
| 3. Bloqueio por tentativas | CT-015 | ⚠️ Em disputa — ver Achados |
| 3. Bloqueio por tentativas | CT-016, 017 | ❌ Sem código (falta captura de API) |
| 4. Ciclo de vida da identidade | CT-020, 021, 023, 024, 025, 027, 031, 032 (8) | ✅ Confirmados — não commitado ainda |
| 4. Ciclo de vida da identidade | CT-029, 030, 033 (3) | ⚠️ Achados reais — ver Achados |
| 4. Ciclo de vida da identidade | CT-022, 026, 028, 034, 035, 036 (6) | ❓ Falha sem causa raiz identificada |
| 5. Transversais e auditoria | CT-038 | ✅ Confirmado — não commitado ainda |
| 5. Transversais e auditoria | CT-037 | ❌ Sem código (falta captura de API) |

**25 de 38 CTs 100% prontos e verdes contra homolog — 12 deles (Suítes 1 e 2) já em MR aberto, aguardando review.**

**Pendente de decisão, código já pronto mas NÃO commitado**: os 5 agentes fixos da Suíte 4 foram renomeados (CPF cru tirado do nome, ex. `"Servidor Lifecycle Ativo Inativo"`) — mudança feita, mas nunca rodada de novo pra confirmar (fica pro dia 24). Também um fix de reaproveitamento de dado em `sector.e2e.cy.js` (fora do escopo da TR, feature de Organograma) — não commitado, decisão de quando subir é do Rafael.

### Achados reais de produto (não são bugs da automação)

- **CT-015** — depois de bloquear uma conta por 5 tentativas erradas (confirmado via log: a 5ª já retorna `"account-blocked"`), uma tentativa imediatamente seguinte com a senha correta autentica normalmente. **Em disputa**: o responsável testou manualmente (tela e API direto) e o bloqueio funcionou. Hipótese de condição de corrida/timing levantada, ainda não confirmada — 3 tentativas de experimento controlado falharam por instabilidade do ambiente (zero dado gerado ainda).
- **CT-029 / CT-030** — em Férias, escrita e leitura não ficam bloqueadas, diferente de Licença (CT-023/CT-024), que bloqueia corretamente. Inconsistência real entre os dois estados de quarentena — vale confirmar se é intencional.
- **CT-033** — uma sessão obtida antes da mudança de status para Inativo continua acessando o próprio perfil normalmente depois da mudança — sessão antiga não é revogada/checada.

### Correções feitas no código do repositório (impactam código já existente, não só testes novos)

- **Vazamento de cookie de sessão entre testes**: `cy.apiRequest`/`cy.request` sempre envia o cookie jar atual, independente do body da requisição — uma tentativa de login que deveria falhar podia "passar" por causa de um login bem-sucedido anterior no mesmo spec. Corrigido com `cy.clearCookies()` embutido nos commands de login "cru".
- **Bug pré-existente em `finishAgentRegistry`** (`user.api.commands.js`) — faltava um `return` na chamada da API, nunca detectado porque nenhum teste anterior exercitava o caminho de "criar agente do zero" repetidamente.
- Fix de nome de agente de teste isolado (limite de tamanho de campo no backend).

### Pendências (ordem de prioridade combinada)

1. **CT-015** — repetir o experimento de timing (script pronto) assim que o ambiente HML estabilizar.
2. **6 CTs da Suíte 4 sem causa raiz** (CT-022/026/028/034/035/036) — mesma janela de investigação do item 1.
3. **CT-029/030/033** — confirmação rápida com produto/backend se a divergência Licença × Férias é intencional.
4. **CT-016/017/037** — aguardam captura de API nova (desbloqueio manual e endpoint de auditoria), depende do responsável capturar via DevTools/HAR.
5. **Subida do código**: Suítes 1 e 2 (12 CTs, sem achado nem pendência) já commitadas e em branch/MR (`tr-1.24-1.25-auth-suite-1-2`) — confirmar review/merge no dia 24. Suítes 3/4/5 continuam sem commit, aguardando resolver os itens 1-4 acima.

---

> [!warning] Pontos de atenção

- Esta task cobre o TR **inteiro** desde 02/09 — antes disso (31/08 a 01/09) ela só registrava a Parte 4 (automação). Ver Histórico.
- `priority` dos 39 casos na Qase ficou pendente de preenchimento manual (decisão consciente, não esquecimento) — Parte 3.
- A Parte 4 só fecha depois de resolver os 3 achados reais em disputa/confirmação (CT-015, CT-029/030, CT-033).

---

## Histórico

- 2026-08-31 - Casos de teste padronizados numa fonte única no vault (Parte 2)
- 2026-08-31 - 39 casos sincronizados com a Qase — 25 atualizados, 2 excluídos, 1 criado (Parte 3)
- 2026-08-31 - Automação iniciada (Parte 4), Suítes 1/2/3 (18 CTs) — sem card vinculado ainda
- 2026-08-31 - Captura de API da troca de status localizada (Downloads do responsável) — desbloqueou e permitiu codar a Suíte 4 inteira (17 CTs)
- 2026-08-31 - Suíte 4 validada contra HML: 8/17 confirmados, 3 achados reais, 6 sem causa raiz
- 2026-09-01 - CT-015 questionado pelo responsável (validação manual diverge do achado automatizado) — investigação de timing tentada, inconclusiva por instabilidade do ambiente
- 2026-09-02 - Card criado (retroativo, só cobria a Parte 4/automação nesse momento), skill [[Sistema/Skills/SKILL_AUTOMACAO_TERMO_REFERENCIA|SKILL_AUTOMACAO_TERMO_REFERENCIA]] registrada no vault
- 2026-09-02 - Reestruturada pra virar a task **pai** do TR inteiro (4 partes), usando o novo template [[Sistema/Templates/Verificação de Conformidade (Termo de Referência)|Verificação de Conformidade]] — decisão do Rafael de não abrir SGVs separados por parte "por enquanto"
- 2026-09-04 - Suítes 1 e 2 (12 CTs) commitadas e enviadas em branch própria (`tr-1.24-1.25-auth-suite-1-2`, a partir do `origin/main` atualizado, sem conflito) — MR a criar/confirmar. Suíte 4 renomeada (CPF cru tirado do nome dos 5 agentes fixos) — pronta, não commitada, não re-rodada ainda. Rafael entra de férias, volta 24/09 — [[QA Workspace/07 Termo de Referência/1.24-1.25/03 Automação/1.24-1.25 - Retomada (volta 24-09)|nota de retomada]] criada
