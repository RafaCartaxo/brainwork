---
title: Configurações da Instância
tags:
  - qa
  - conhecimento
  - sogov
  - configuracoes-instancia
tipo: modulo
revisado: 2026-10-20
fonte: https://app.notion.com/p/alfa-group/Configura-es-da-Inst-ncia-ok-c8d4c4a2e50644c7b5bab7928c19f9a2
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2025-01-30 (Alice Martins)
---
# Configurações da Instância

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-20 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria (campo `Task` vazio). Título da página no Notion é "Configurações da Instância **ok**" — o sufixo "ok" parece anotação informal de revisão, não faz parte do nome da feature (removido aqui).

## Visão geral
- Todo cliente cadastrado no SoGov é tratado como uma **instância**. "Configurações da Instância" é a tela, dentro do ambiente do próprio cliente, onde usuários com permissão visualizam dados cadastrais do órgão, consultam os módulos disponíveis e personalizam a aparência do ambiente (tema e marca).

## Regras de negócio

### O que a tela permite
- Visualizar as **informações cadastrais** do órgão.
- Consultar os **módulos disponíveis** pra essa instância e a quantidade de módulos **ativos**.
- Personalizar **temas**, incluindo cores.
- Gerenciar as **imagens da marca** do órgão, usadas no sistema.

### Permissão
- Disponível pra usuários com permissão de **administrador geral**, ou que tenham a permissão extra "configuração de instância" ativa.

### Edição das configurações
- Só **tema (personalização de cores)** e **imagens da marca** são editáveis direto nesta página.
- As demais informações (dados cadastrais, módulos disponíveis) são **somente visualização** — pra alterar, precisa ser via usuário **SOGO**, no gerenciamento do cadastro do cliente (ver [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]] → Administrativo SOGO).

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] Export é curto e genérico — não detalha quais são exatamente as "informações cadastrais do órgão" exibidas aqui (prováveis candidatas, pelo que já está documentado em [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]]: tipo de cliente, CNPJ, razão social, domínio, licenças, datas de contrato — mas não confirmado nesta página).
- [ ] Não detalha o que de fato pode ser personalizado em "temas" além de "cores" (paleta completa? logo tem seção própria, já que "imagens da marca" é item separado?).
- [ ] Página não foi editada desde 30/01/2025 (mais de um ano antes das demais docs importadas nesta sessão) — vale confirmar se o conteúdo ainda reflete o comportamento atual do sistema, já que outras docs do mesmo período já passaram por várias atualizações.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- Sem SGV vinculado — documentação de referência.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]] — Ambiente Cliente (onde esta tela vive) e Administrativo SOGO (onde os dados somente-visualização são de fato editados).
- [[QA Workspace/04 Conhecimento/Módulos/Construtor de Módulos|Construtor de Módulos]] — os módulos cuja contagem/disponibilidade aparece aqui.
