---
demanda: "QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/01 - Bug"
validacao: "QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/04 - Validação dev"
status: planejado
pontos: ""
---

# Casos de teste — SGV-12379

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/00 README|Abrir README do card]]
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/01 - Bug|01 - Bug]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/04 - Validação dev|04 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Bug`; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério de aceite (`01 - Bug`) | CT |
|---|---|
| Após trocar de setor, o scroll carrega mais documentos sem F5 | [[#^ct-001\|CT-001]] |
| Regressão: sem trocar de setor, o scroll segue carregando | [[#^ct-002\|CT-002]] |
| Regressão: trocar de setor em sequência mantém o scroll | [[#^ct-003\|CT-003]] |

---

> [!example]- CT-001 · Scroll carrega mais documentos após trocar de setor
>
> **Pré-condições:** servidor vinculado a mais de um setor (A e B); os setores A e B têm documentos suficientes na mesa para o scroll carregar mais.
>
> **Dado** que o servidor esteja na mesa de trabalho no setor A
> **Quando** trocar para o setor B, a mesa for carregada e ele fizer scroll para carregar mais documentos
> **Então** mais documentos do setor B são carregados, sem precisar atualizar a página (F5)
>
> **Pós-condição:** mesa do setor B exibindo documentos adicionais carregados pelo scroll.
>
> **Tipo:** funcional · **Camada:** E2E · **Automação:** manual · **Execução:** planejado

^ct-001

> [!example]- CT-002 · Regressão — scroll carrega no setor da abertura, sem trocar de setor
>
> **Pré-condições:** servidor com a mesa do setor aberto e documentos suficientes para o scroll carregar mais.
>
> **Dado** que o servidor abra a mesa de trabalho e permaneça no mesmo setor
> **Quando** fizer scroll na mesa para carregar mais documentos
> **Então** mais documentos do setor são carregados
>
> **Pós-condição:** mesa exibindo documentos adicionais carregados pelo scroll.
>
> **Tipo:** regressão · **Camada:** E2E · **Automação:** manual · **Execução:** planejado

^ct-002

> [!example]- CT-003 · Regressão — trocar de setor em sequência mantém o scroll funcionando
>
> **Pré-condições:** servidor vinculado a mais de um setor (A e B, no mínimo); os setores têm documentos suficientes na mesa para o scroll carregar mais.
>
> **Dado** que o servidor esteja na mesa de trabalho e troque de setor mais de uma vez em sequência (por exemplo A → B → A)
> **Quando** a mesa for carregada após cada troca e ele fizer scroll para carregar mais documentos
> **Então** o scroll carrega mais documentos em todos os setores visitados, sem precisar atualizar a página (F5)
>
> **Pós-condição:** mesa de cada setor visitado exibindo documentos carregados pelo scroll.
>
> **Tipo:** regressão · **Camada:** E2E · **Automação:** manual · **Execução:** planejado

^ct-003
