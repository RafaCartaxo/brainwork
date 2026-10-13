---
title: Chaves de Acesso
tags:
  - qa
  - conhecimento
  - sogov
  - chave-acesso
tipo: modulo
revisado: 2026-10-13
fonte: https://app.notion.com/p/alfa-group/Chaves-de-Acesso-a05fadd0c5f847c8b28576a739dc21ec
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-07-27 (Vinícius Sogo)
---
# Chaves de Acesso

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-13 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria pro módulo em si (campo `Task` vazio no Notion); a atualização de 27/07/2026 já vem com SGV (ver seção própria).

## Visão geral
- Chaves de acesso permitem que outros servidores gerem documentos (e, após a atualização de 27/07/2026, também despachos) **em nome de outro usuário**, de forma segura, sem precisar compartilhar login e senha.

## Regras de negócio

### Permissões
- Podem **criar** chaves de acesso: Administrador, Administrador setorial, N1 e N2.
- **N3** só pode **receber** chaves — nunca criar.

### Criando um novo documento com chave de acesso
- Ao criar novo documento, as opções exibidas consideram as chaves de acesso disponíveis pro usuário no setor do switch ativo.
- Acesso restrito a **uma única chave** → ao escolher o tipo de documento, vai direto pro formulário já identificado com a chave.
- Acesso restrito ao **próprio nome** do usuário no setor ativo → formulário abre normalmente, sem chave.
- Acesso possível por **mais de uma permissão** (chave(s) + permissão pessoal) → modal pra escolher o usuário responsável pela criação; a tag identificadora destaca o próprio usuário (se ele tiver acesso) e lista os demais usuários dos setores que concederam chave.

### Notificações e eventos
- **Criação de documento** via chave de acesso → dono da chave é notificado, com link de redirecionamento pro documento.
- **Geração de documento** via **contrassenha** → dono da contrassenha é notificado, com link de redirecionamento (ver Dúvidas em aberto sobre o termo).

### Recebimento de chave em setor que o usuário já faz parte
- Usuário fica **completamente envolvido**: documento aparece na mesa pessoal **e** na mesa do setor; interage conforme seu nível.
- Encerrada a chave, tramitação e visualização continuam normais pra ele — não perde acesso.

### Recebimento de chave em setor que o usuário **não** tem acesso
- Documento aparece na mesa de trabalho, mas o envolvimento é **parcial**: só visualiza, não interage.
- Documento continua visível mesmo com a chave já encerrada.
- Se o setor do usuário **se tornar** envolvido no documento por outro motivo, ele passa a tramitar na mesa do setor e pode interagir conforme seu nível.

### Encerramento automático da chave
| Gatilho | Efeito |
|---|---|
| Quem concedeu a chave sai do setor | Chave encerrada automaticamente; notificação pra quem concedeu e quem recebeu |
| Quem concedeu a chave vira N3 | Todas as chaves concedidas por ele são encerradas (histórico mantido); notificação aos envolvidos |
| Setor de quem concedeu é removido das regras de criação do documento | Chave encerrada automaticamente; notificação aos envolvidos |

### Listagem de chaves
- Duas abas: **Chaves Criadas** e **Chaves Recebidas**.
- Paginação a partir de 11 itens, 10 por página.
- Filtro por status em ambas as abas.
- Busca: em Criadas, pelo nome do servidor com quem a chave foi compartilhada; em Recebidas, pelo nome do servidor que concedeu.
- **Chaves Criadas** mostra: total criadas, total ativas (das criadas), total de documentos gerados por elas.
- **Chaves Recebidas** mostra: total concedidas, total ativas, total de documentos gerados por elas.

### Status e ações (menu meatball)
| Status | Ações (Chaves Criadas) |
|---|---|
| Ativa | Editar, Encerrar (encerrada manualmente ou por esgotar os usos antes do prazo → data final = data de encerramento); Excluir disponível **enquanto não houver documento criado** |
| Encerrada | Visualizar |
| Agendada | Editar, Ativar (ativada antes da data agendada → data inicial = data de ativação); Encerrar (encerrada manualmente enquanto agendada → data inicial **e** final = data de encerramento); Excluir |

- Em **Chaves Recebidas**, mesmos status, mas **sem** menu meatball — só visualizar.

### Criando uma nova chave
- **Seleção de servidor**: só aparecem servidores com permissão pra criar documentos; seleção única.
- **Quantidade de usos**: opcional; se preenchida, limita quantas vezes a chave pode ser usada no período enquanto estiver ativa.
- **Definição de permissões**: escolhe quais documentos a chave libera; checkbox pai marca todos os filhos automaticamente; dá pra desmarcar filhos individualmente, desde que **ao menos um** permaneça marcado enquanto o pai estiver marcado.
- **Período de ativação**: final ≥ inicial; início não pode ser anterior à data atual; intervalo máximo de **365 dias** (limite de performance).
- **Agendamento**: três notificações possíveis — criação da chave agendada (imediata), ativação da chave (no dia da ativação, automática ou manual via meatball) e aviso ao **criador** quando uma chave agendada é ativada.

### Histórico
- Na tela de visualização/edição da chave: quantidade de documentos criados + link pro histórico completo.
- Histórico lista os documentos gerados pela chave, com a mesma ordenação/status da mesa de trabalho; abrir um card mostra o documento como na mesa.

### Atualização — Despachos via chave de acesso (SGV-10322, 27/07/2026)
> Objetivo: permitir que o usuário com chave de acesso elabore e emita despachos em nome de quem concedeu a chave, em documentos novos ou existentes.

- **Pontos de atenção de design**: reforçar visualmente de qual usuário é a sessão ativa (fluxo sensível — documento oficial em nome de terceiro); prever estado de chave sem permissão pra emitir despacho; alinhar ao fluxo de despacho já existente, mudando o mínimo além do contexto de autoria; estados vazio/sucesso/erro-sem-permissão.
- **Visualização de chaves de acesso**: quem recebe a chave passa a poder criar despachos nos módulos de Assunto/Serviço selecionados (regras de servidor, vigência, usos e módulos continuam as mesmas); card "Documentos criados" passa a contar documentos **e** despachos criados via chave; copies de tooltip atualizadas.
- **Nova chave de acesso**: subtítulo atualizado — *"Disponibilize chaves de acesso restritas exclusivamente à criação de documentos e despachos para que outros servidores possam gerá-los em seu nome."*
- **Histórico de documentos**: subtítulo atualizado; quando há despachos criados via chave, o item ganha accordion **"Despachos criados (N)"** (default aberto no protótipo) listando a numeração de cada despacho (ex.: Despacho 1, 4, 8, 26); clicar abre o documento ancorado no evento do despacho correspondente.
- **Árvore de processo**: impacto só informativo — todas as regras de despacho já existentes continuam valendo. Evento ganha linha de autoria: *"Aberto através de chave de acesso por: $Assinatura_textual, $Cargo, em $Setor"*.
- **Fluxo de criação** (toolbar ou "Responder" num evento): seleciona o usuário → emite o despacho.
	- **Emissão direta (toolbar)**: mesmas regras de seleção da criação de documento via chave (modal com reestruturação visual); despacho emitido ganha tag **"Via chave de acesso"** ao lado da data, com tooltip *"Criado por $assinatura_textual em nome de $assinatura_textual."* (ver Dúvidas em aberto sobre a variável repetida).
	- **Despacho - Resposta**: mantém a estrutura já existente ("Em resposta ao despacho $Nome_nro_desp"); também ganha a tag + tooltip de autoria via chave.
	- **Restrições da composição** (toolbar e resposta): só **Anexar arquivos**, **Associar documento** e **Emitir** — sem prazo, solicitação de assinaturas, ou emitir e assinar.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] O export cita notificação "Geração de Documento... utilizando uma **contrassenha**" logo depois de "Criação de Documento... utilizando uma **chave de acesso**" — o termo "contrassenha" não é definido em nenhum outro trecho da doc; confirmar se é sinônimo de chave de acesso num contexto específico ou um mecanismo à parte.
- [ ] No tooltip do despacho via chave, a frase é "Criado por $assinatura_textual em nome de $assinatura_textual" — a mesma variável aparece duas vezes; o esperado seria o segundo campo ser o nome de quem **concedeu** a chave, não repetir quem criou. Confirmar no Notion/Figma se é erro de cópia do export ou comportamento real.
- [ ] Backlog do Notion lista dois itens com título **idêntico** ("Permitir elaboração e emissão de despachos via chave de acesso"), um marcado **[UI/UX]** e outro **[MELHORIA-CX]** — mesmo padrão visto em outras docs importadas (ex.: Processos Urbanísticos, SGV-10677 com origem SGV-9980): provável que o item UI/UX seja a própria **SGV-10322** e o MELHORIA-CX seja a origem/pedido que gerou a task, mas o export não traz o SGV da origem. Confirmar no Notion.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- **SGV-10322** — [UI/UX] Permitir elaboração e emissão de despachos via chave de acesso — atualização de 27/07/2026, ver seção acima.
- Sem outro SGV vinculado ao módulo em si (documentação de referência desde 08/07/2024, sem task própria no Notion).

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
