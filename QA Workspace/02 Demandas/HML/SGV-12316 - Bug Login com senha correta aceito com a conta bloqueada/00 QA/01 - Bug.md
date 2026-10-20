---
prioridade: alta
origem: validação
pontos_alocados: ""
---

# SGV-12316 — Bug Login com senha correta aceito com a conta bloqueada

> [!info]- Navegação QA/DEV
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/00 README|Abrir README do card]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/03 - Casos de teste|03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/04 - Validação dev|04 - Validação dev]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que, depois de a conta ser bloqueada por 5 tentativas de login com senha incorreta, o login com a **senha correta continua sendo aceito**. O bloqueio exibe a mensagem e envia o e-mail de reativação, mas não impede o acesso.

A conta bloqueada só deveria voltar a autenticar depois de desbloqueada — pelo link enviado por e-mail ou por ação interna de um servidor com permissão.

---

## Passo a passo para reproduzir

**Dado** que um usuário esteja cadastrado e ativo
**E** realize 5 tentativas de login com senha incorreta
**E** receba a mensagem de conta bloqueada e o e-mail de reativação
**Quando** informar a senha correta, sem desbloquear a conta
**Então** verifico que o login é efetuado normalmente, mesmo com a conta bloqueada

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://12316)

![[12316 - login com senha correta aceito com a conta bloqueada.mp4]]

---

## Resultado Esperado

Com a conta bloqueada, o login com a senha correta é **recusado**, informando que a conta está bloqueada, até que ela seja desbloqueada pelo link de reativação enviado por e-mail ou por ação interna de um servidor com permissão.

O cenário corrigido no SGV-5273 continua valendo: com 4 tentativas incorretas (conta ainda **não** bloqueada), a senha correta na 5ª tentativa autentica.

---

## Critérios de aceite

- [ ] Conta bloqueada recusa o login com a senha correta e informa que está bloqueada.
- [ ] Depois do desbloqueio pelo link de reativação do e-mail, o login com a senha correta é efetuado.
- [ ] Depois do desbloqueio interno feito por um servidor com permissão, o login com a senha correta é efetuado.
- [ ] Regressão do SGV-5273: com 4 tentativas incorretas e a senha correta na 5ª (conta não bloqueada), o login é efetuado.
- [ ] Regressão do bloqueio: a 5ª senha incorreta bloqueia a conta e envia o e-mail de reativação.

---

## Requisito do Termo de Referência

Descumpre o **TR §1.25.1 — PDF p. 2 — transcrição §1.25**: "Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada". Uma conta bloqueada que continua autenticando com a senha correta não está bloqueada.

Texto integral: [[QA Workspace/04 Conhecimento/Referências/Sanidade automatizada do SOGOV - Termo de Referência/01 - Termo de Referência SOGOV - Transcrição integral#1.25 (p. 2)|transcrição do TR, §1.25]]. Coberto pelo CT-002 da Onda 1 de sanidade ([[QA Workspace/02 Demandas/DEV/SGV-12272 - Casos de teste e publicação da Onda 1 de sanidade do TR/00 QA/03 - Casos de teste#^ct-002|SGV-12272]]).

---

## Ambiente

- Ambiente: Homologação
- Versão: a preencher

---

## Informações adicionais

- Notion: [SGV-12316 no Backlog](https://app.notion.com/p/3ff72f8c89908125ab07fd8971b8cce2) (versão enxuta, relacionada à SGV-12272)
- Demanda relacionada: [[QA Workspace/02 Demandas/Concluídas/5273/QA/5273 - Bug Login Senha Correta Apos Tentativas|SGV-5273]] (origem provável) · CT-002 da [[QA Workspace/02 Demandas/DEV/SGV-12272 - Casos de teste e publicação da Onda 1 de sanidade do TR/00 QA/03 - Casos de teste#^ct-002|SGV-12272]] (bloqueio após 5 tentativas)
- Observações:
  - **Origem provável:** a correção do SGV-5273 (MR !419) inverteu a ordem da autenticação — a senha passou a ser verificada antes do limite de tentativas e, se correta, o login é concluído ignorando o contador. Isso vale também quando a conta **já está bloqueada**. O SGV-5273 tratava outro cenário (senha correta na 5ª tentativa, conta ainda não bloqueada); o resultado esperado registrado lá ("mesmo após ter esgotado as tentativas máximas, efetuar o login") ampliou o escopo e provavelmente foi lido como "senha correta sempre entra".
  - A leitura do código do produto (checkout local, branch `development`) indica a mesma coisa: no bloqueio, o contador é reposto e a senha correta ainda autentica. Confirmar com o dev.
  - Relacionado: SGV-5428 (Notion, despriorizado) — e-mail de recuperação para usuário bloqueado, mesmo fluxo.
- Histórico:
    - 2026-10-20 - 🐛 Bug cadastrado (reproduzido em homologação)
