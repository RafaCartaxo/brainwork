---
title: Login
tags:
  - qa
  - conhecimento
  - sogov
  - login
tipo: modulo
revisado: 2026-07-20
fonte: https://app.notion.com/p/alfa-group/Login-ok-a60a15f585a04718acd099232abbba1c
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2025-01-30 (Alice Martins)
---
# Login

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20. A página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

## Visão geral

Login permite que os usuários acessem o sistema autenticando credenciais (e-mail, CPF, CNPJ e senha). Após validar os dados, o sistema pode exigir etapas adicionais de segurança (CAPTCHA).

Dois esquemas de login separados:

| Tipo de usuário | Identificador | Observação |
|---|---|---|
| Cidadão ou servidor | CPF (PF) ou CNPJ (PJ) + senha | Login **único** no SoGov |
| SOGO | E-mail institucional + senha | Login **separado** dos demais |

## CAPTCHA

Em todas as telas de login (**LOGIN SERVIDOR, LOGIN CIDADÃO, LOGIN SOGO**), após inserir dados corretos e clicar em "ENTRAR", o CAPTCHA é exibido como etapa adicional de segurança. Também aparece em outros pontos sensíveis do fluxo:

| Ponto | Quando aparece o CAPTCHA |
|---|---|
| Esqueci minha senha ou acesso | Após confirmar e-mail válido pra recuperação |
| Verificação de autenticidade de assinaturas (cidadão) | Ao inserir código válido e iniciar a consulta de autenticidade; e ao inserir código válido pra acompanhamento de solicitação |
| Consulta de CPF/CNPJ — cadastro de cidadãos | Após confirmar CPF ou CNPJ válido, antes de ir pra tela de cadastro |
| Pré-cadastro externo de servidor | Após inserir e confirmar CPF válido |
| Conclusão de pré-cadastro de servidor | Após inserir CPF válido e confirmar a ação |
| Conclusão de cadastro interno do cidadão | Após inserir CPF ou CNPJ válido e confirmar a ação |

Em todos os casos, a correta inserção do CAPTCHA redireciona o usuário pra próxima tela do fluxo correspondente.

## Bloqueio de conta após múltiplas tentativas de login

Vale pra **todos os ambientes** do SoGov: errar a senha **5 vezes** bloqueia a conta.

Mensagem de erro exibida: o e-mail cadastrado do usuário, **anonimizado** — mostra só as duas primeiras letras e a última letra, com os caracteres intermediários substituídos por asteriscos (ex.: `ra***o@sogo.com.br`).

## Status do usuário servidor (limitações de acesso)

O usuário servidor tem as funcionalidades disponíveis conforme seu **nível de permissão**, mas o **status** impõe limitações adicionais. Quatro status possíveis:

| Status | Ambiente servidor | Ambiente cidadão |
|---|---|---|
| **Em Atividade** | Acesso completo, conforme o nível de permissão | Acesso completo |
| **Licença** | Login mostra aviso do período de licença; só funcionalidades do menu "Profile" | **Não alterado** |
| **Férias** | Login mostra aviso do período de férias; só funcionalidades do menu "Profile" | **Não alterado** |
| **Inativo** | **Sem acesso** ao workspace enquanto inativo; mensagem exibida ao tentar logar | Pode logar em **outros workspaces** (se status diferente lá) e no ambiente cidadão normalmente |

> [!note] Licença e Férias não afetam o ambiente cidadão
> Um servidor de licença ou férias continua com acesso total ao ambiente cidadão — a limitação é só no ambiente servidor, e mesmo lá só restringe a funcionalidades fora do "Profile" (não bloqueia o login em si, como o Inativo faz).

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] O CAPTCHA aparece "após o usuário inserir dados corretos" no login — o que acontece se os dados estiverem **incorretos**? CAPTCHA aparece antes, depois, ou só na tentativa correta? Não especificado
- [ ] Bloqueio por 5 tentativas: existe desbloqueio automático por tempo, ou só manual (suporte/admin)? Não especificado
- [ ] Servidor Inativo consegue logar em "outros workspaces" — como o sistema decide isso é o mesmo usuário/CPF vinculado a instâncias diferentes com status diferentes? Relaciona com [[Usuário Cidadão#Visão geral|usuário único entre ambientes]]

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- 
