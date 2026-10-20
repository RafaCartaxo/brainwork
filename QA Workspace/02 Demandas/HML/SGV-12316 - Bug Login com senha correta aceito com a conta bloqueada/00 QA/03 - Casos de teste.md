---
demanda: "[[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/01 - Bug]]"
validacao: "[[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-12316

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/00 README|Abrir README do card]]
> **Bug:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/01 - Bug|01 - Bug]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/04 - Validação dev|04 - Validação dev]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Bug`; esta nota concentra os cenários executáveis.

---

## Matriz de cobertura

| Critério de aceite (`01 - Bug`) | CT |
|---|---|
| Conta bloqueada recusa a senha correta | [[#^ct-001\|CT-001]] |
| Desbloqueio pelo link do e-mail | [[#^ct-002\|CT-002]] |
| Desbloqueio interno por servidor | [[#^ct-003\|CT-003]] |
| Regressão SGV-5273 | [[#^ct-004\|CT-004]] |
| Regressão do bloqueio | [[#^ct-005\|CT-005]] |

---

> [!example]- CT-001 · Conta bloqueada recusa o login com a senha correta
>
> **Pré-condições:** usuário cadastrado e ativo, com a conta bloqueada por 5 tentativas incorretas.
>
> **Dado** que a conta do usuário esteja bloqueada
> **Quando** ele informar a senha correta
> **Então** o login é recusado e o sistema informa que a conta está bloqueada
>
> **Pós-condição:** conta segue bloqueada.
>
> **Tipo:** funcional · **Camada:** API/E2E · **Automação:** manual · **Execução:** planejado

^ct-001

> [!example]- CT-002 · Desbloqueio pelo link de reativação do e-mail
>
> **Pré-condições:** conta bloqueada; e-mail de reativação recebido.
>
> **Dado** que a conta do usuário esteja bloqueada
> **E** ele acesse o link de reativação recebido por e-mail
> **Quando** informar a senha correta
> **Então** o login é efetuado
>
> **Pós-condição:** conta desbloqueada, contador de tentativas zerado.
>
> **Tipo:** funcional · **Camada:** API/E2E · **Automação:** manual · **Execução:** planejado

^ct-002

> [!example]- CT-003 · Desbloqueio interno feito por servidor com permissão
>
> **Pré-condições:** conta bloqueada; servidor com permissão de desbloqueio na mesma instância.
>
> **Dado** que a conta do usuário esteja bloqueada
> **E** um servidor com permissão realize o desbloqueio pela tela interna
> **Quando** o usuário informar a senha correta
> **Então** o login é efetuado
>
> **Pós-condição:** conta desbloqueada, contador de tentativas zerado.
>
> **Tipo:** funcional · **Camada:** API/E2E · **Automação:** manual · **Execução:** planejado

^ct-003

> [!example]- CT-004 · Regressão SGV-5273 — senha correta na 5ª tentativa, conta não bloqueada
>
> **Pré-condições:** usuário cadastrado e ativo, sem bloqueio.
>
> **Dado** que o usuário tenha errado a senha 4 vezes
> **Quando** informar a senha correta na 5ª tentativa
> **Então** o login é efetuado
>
> **Pós-condição:** contador de tentativas zerado.
>
> **Tipo:** regressão · **Camada:** API/E2E · **Automação:** manual · **Execução:** planejado

^ct-004

> [!example]- CT-005 · Regressão do bloqueio — 5ª senha incorreta
>
> **Pré-condições:** usuário cadastrado e ativo, sem bloqueio.
>
> **Dado** que o usuário tenha errado a senha 4 vezes
> **Quando** errar a senha pela 5ª vez
> **Então** a conta é bloqueada, a mensagem de bloqueio é exibida e o e-mail de reativação é enviado
>
> **Pós-condição:** conta bloqueada.
>
> **Tipo:** regressão · **Camada:** API/E2E · **Automação:** manual · **Execução:** planejado

^ct-005
