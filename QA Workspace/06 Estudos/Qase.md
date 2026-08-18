---
tags:
  - qa
  - estudo
tipo: estudo
status: estudando
fonte: docs.qase.io, qase.io/pricing
criado: 2026-08-18
revisado: 2026-08-18
---
# Qase

> [!info] Sobre esta nota
> Estudo ad hoc (fonte externa: documentação oficial da Qase). `status`: `estudando` | `revisado`. Quando virar regra estável do fluxo de QA do Sogov, graduar pra [[../04 Conhecimento/README|04 Conhecimento]] (link nos dois sentidos).

## Resumo
- Qase é uma ferramenta de test management (repositório de casos, execução, defeitos) sendo avaliada como adoção pro time. Alternativa a TestRail/Zephyr.
- Hierarquia: **Projeto** → **Suites** (pastas) → **Casos de teste** → **Test Runs** (execução) → **Test Plans**/**Milestones** (agrupamento).

## Pontos-chave
- **Projeto**: workspace isolado por produto/time — repositório de casos, runs, defeitos e milestones próprios.
- **Suites**: árvore hierárquica de pastas dentro do projeto, organiza casos por feature/módulo. Três visualizações: árvore aninhada, pastas, mind map (beta).
- **Casos de teste**: título, pré-condição, passos (ação + dado + resultado esperado por passo), pós-condição, severidade, prioridade, campos customizados (pago). Dois layouts de passo: clássico (step-by-step) ou texto livre.
- **Shared Steps**: sequência de passos reutilizável entre casos. Nível de **projeto** funciona no Free; nível de **workspace** (compartilhado entre projetos diferentes) exige plano pago.
- **Test Designer (IA / AIDEN)**: gera casos manuais a partir de um requisito colado (texto livre ou issue do Jira/GitHub) — marca os casos gerados com tag "AI", exige revisão antes de salvar na suite. **Feature paga** (créditos AIDEN inclusos a partir do plano Startup).
- **Test Runs**: sessão de execução real, status por caso (passou/falhou/bloqueado/pulado) + evidência anexada.
- **Automação**: reporters oficiais (Cypress, Playwright, pytest, JUnit etc.) publicam resultado de execução automatizada direto num Test Run via **API pública** — isso **não** é a categoria "Integrações" (que é bloqueada no Free), então automação via reporter funciona mesmo no plano gratuito.

## Anotações

### Plano Free (permanente, sem prazo)
- 2 projetos, até 4 usuários
- 2 test runs concorrentes (abertos ao mesmo tempo, não por mês)
- Retenção de **30 dias** nos dados de test run — histórico mais antigo some
- Shared Steps: nível de projeto incluso; nível de workspace (cross-projeto) é pago
- Gestão de defeitos: completa
- API pública + Reporter Apps inclusos, teto de 5.000 resultados/mês
- 500MB de anexos

### O que exige plano pago (Teams/Business, ~US$30-36/user/mês)
- Integrações nativas (Jira, GitHub, GitLab e outras 35+)
- Dashboards & reports widgetizados
- Requirements Traceability Matrix
- Campos customizados
- Test Case Review (gate de aprovação de caso)
- RBAC (controle de acesso por papel)
- Test Designer / IA (AIDEN) — todos os recursos de IA

### Import de casos (CSV)
- Formato próprio "Qase.io CSV", em duas versões: V1 (`id`, deprecated) e V2 (`v2.id`)
- Colunas confirmadas: `title`, `description`, `preconditions`, `postconditions`, `tags`, `priority`, `severity`, `type`, `behavior`, `automation`, `steps_type`, `steps_actions`, `steps_data`, `steps_results`
- Todos os passos de **um mesmo caso** são consolidados numa única célula de `steps_actions` (e as correspondentes `steps_data`/`steps_results`), numerados linha a linha — não é uma linha de CSV por passo
- Suite é criada com uma linha própria (`suite_without_cases` = 1) e referenciada pelas linhas de caso — nome/coluna exata de vínculo **não confirmado verbatim** (ver Dúvidas em aberto)
- Import não faz merge por título — reimportar sobre casos já existentes tende a duplicar, não atualizar

## Dúvidas em aberto
- [ ] Cabeçalho completo e ordem exata das colunas do CSV V2 (especialmente a coluna que referencia a suite de destino) — a documentação da Qase usa exemplos em imagem/Google Drive, não texto puro, então não dá pra confirmar 100% sem abrir a tela de Import na conta real ou baixar o template de lá.
- [ ] Se o Test Plans é ou não uma feature disponível no Free (não apareceu na tabela de comparação oficial, nem como incluído nem como exigindo upgrade).
- [ ] Se worth avaliar o teto de 5.000 resultados/mês da API contra o volume real de execuções do `sogov-automation-test` antes de depender disso pra automação contínua.

## Aplicação no QA/Sogov
- **Automação**: o repo `sogov-automation-test` (Cypress) pode publicar resultados direto num Test Run da Qase via `cypress-qase-reporter`, taggeando specs com o ID do caso na Qase — sem precisar de plano pago, porque isso usa API/Reporter Apps (incluso no Free), não a categoria "Integrações".
- **Caso concreto em andamento**: os 39 casos de teste do Termo de Referência "1.24-1.25: Autenticação e ciclo de vida do usuário" (hoje só títulos na Qase) estão sendo reorganizados no formato nativo dela (step/data/expected result + shared steps) — ver arquivo de organização ao lado da planilha original em `~/Downloads/Termo de refência/`.
- **Limite prático do Free** (2 projetos) vira relevante se o Sogov tiver mais de 2 frentes de produto testadas simultaneamente — decisão de consolidar num projeto só ou orçar upgrade.

## Referências
- [Test suites | Qase Docs](https://docs.qase.io/general/get-started-with-the-qase-platform/create-a-test-suite)
- [Test cases | Qase Docs](https://docs.qase.io/general/get-started-with-the-qase-platform/test-cases)
- [Import test cases | Qase Docs](https://docs.qase.io/general/get-started-with-the-qase-platform/test-cases/import-test-cases)
- [AI Test Designer | Qase Help Center](https://docs.qase.io/en/articles/9653096-ai-test-designer)
- [Free Plan | Qase Help Center](https://docs.qase.io/en/articles/6639381-free-plan)
- [Pricing - Test Management Plans | Qase](https://www.qase.io/pricing/)
- [Cypress integration | Qase](https://www.qase.io/integrations/cypress/)
- [Cypress | Qase Docs](https://docs.qase.io/automation/reporters/javascript/cypress)
- [Shared Steps | Qase Help Center](https://docs.qase.io/en/articles/5563709-shared-steps)
