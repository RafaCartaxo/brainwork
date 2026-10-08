---
title: Gestão de Desbloqueio de Acessos
tags:
  - qa
  - conhecimento
  - sogov
  - desbloqueio
tipo: modulo
revisado: 2026-10-08
fonte: https://app.notion.com/p/alfa-group/Gest-o-de-Desbloqueio-de-acessos-Servidor-e-Cidad-o-33d2aec67d30808aae4de3eb04e30d09
fonte_criado: 2026-04-09 (Edu)
fonte_ultima_edicao: 2026-07-20 (Ivo Costa)
---
# Gestão de Desbloqueio de Acessos

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-08 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Export sem SGV vinculado (feature ainda em especificação, campo `Task` vazio no Notion); Figma (handoff) já existe — ver Referências.

## Visão geral
- Fluxo de desbloqueio de acesso para usuários (Servidor e Cidadão PF/PJ) que excederam o limite de tentativas de login, permitindo que o Admin intervenha e o usuário tenha um fluxo de recuperação seguro.

## Regras de negócio

### Permissões
- Por padrão, níveis **Admin** e perfis **SOGO (Análise CX)** — exceto **Financeiro** — têm as permissões de desbloqueio:
	- **Permissão A** — Resetar e-mail de Servidor (cluster de permissões Servidores).
	- **Permissão B** — Resetar e-mail de Cidadão (cluster de permissões Cidadãos).
- Essas permissões podem ser estendidas como extras a outros níveis, respeitando a hierarquia de permissões já estabelecida no sistema.

### Interface — Listagem de Servidores
- Novo status **Bloqueado** na tag de status da listagem de usuários.
- Opção **Bloqueado** incluída no componente de filtro global (exclusivo da listagem de servidores).

### Interface — Listagem de Cidadãos (PF e PJ)
- Menu meatball (ações): estado padrão tem **Visualizar** e **Alterar E-mail**; estado **Bloqueado** adiciona dinamicamente **Desbloquear Acesso**.
- Interface SOGO: analistas CX veem as ações agrupadas no próprio meatball.

### Fluxo de desbloqueio e sincronização
- **Regra crítica**: quando o Admin desbloqueia um usuário alterando o e-mail pessoal, o sistema invalida automaticamente qualquer pendência de confirmação de e-mail anterior — o novo e-mail já nasce validado no ato da ação.
- Ao finalizar o fluxo de redefinição (manual ou sistêmico), o ID do usuário é removido da lista de bloqueios por tentativas excedidas.
- Após o desbloqueio, o usuário retorna ao status de origem anterior ao bloqueio (ex.: Ativo).
- Novos inputs de senha usam o medidor de força já implementado no sistema.

### Fluxo de recuperação (experiência do usuário)
- **Validação de acesso**: usuário insere o código enviado por e-mail; botão "Reenviar código" fica desabilitado por 60s com contador regressivo.
- **Redefinição de senha**: requisitos de senha mudam para verde conforme atendidos (validação real-time); clicar em "Redefinir" sem preencher mostra erro "Campo Obrigatório" e requisitos não atendidos ficam vermelhos após o clique.
- **Finalização**: tela de sucesso com redirecionamento automático após 3s, ou link manual para a tela de login.

### Histórico e auditoria (logs)
| Contexto | Ação | Texto do log |
|---|---|---|
| Cidadão PF/PJ | Alterar e-mail | Mudou o $e-mail-pessoal de $nome-cidadão para $e-mail |
| Cidadão PF/PJ | Reset senha | Enviou uma redefinição de senha para $cidadão via e-mail |
| Servidor | Alterar e-mail | Mudou o $e-mail-pessoal de $assinatura_textual para $e-mail |
| Servidor | Reset senha | Enviou uma redefinição de senha para $assinatura_textual via e-mail |

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — feature em especificação, sem card/SGV cadastrado.

## Dúvidas em aberto
- [ ] Revisão de Ivo Costa (20/07) ficou registrada só como "revisado com ponderações", sem detalhar o quê — confirmar com Edu/Ivo o que mudou após essa revisão.
- [ ] Quais níveis, além de Admin e SOGO (Análise CX, exceto Financeiro), podem receber as permissões extras de desbloqueio, e sob qual critério — a doc só diz que isso "respeita a hierarquia já estabelecida", sem listar os perfis.
- [ ] Notion lista um item de backlog vinculado ("[UX/UI] Criar opção de desbloqueio de usuário para administradores") sem detalhar escopo — confirmar se é a mesma entrega ou um recorte à parte.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- Nenhum ainda — feature em especificação (campo `Task` vazio no Notion), sem SGV cadastrado.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- Figma (handoff): https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=1650-4112&t=u7jWEVlf6ASoHdsE-1
