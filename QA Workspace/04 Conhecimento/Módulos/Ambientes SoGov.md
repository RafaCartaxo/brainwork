---
title: Ambientes SoGov
tags:
  - qa
  - conhecimento
  - sogov
  - ambiente
tipo: modulo
revisado: 2026-10-13
fonte: https://app.notion.com/p/alfa-group/Ambientes-SoGov-7fd019684daf4e08be69bde72e9c9438
fonte_criado: 2024-07-08 (Alice Martins)
fonte_ultima_edicao: 2026-07-23 (Ivo Costa)
---
# Ambientes SoGov

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-13 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria (campo `Task` vazio no Notion). **Não confundir** com [[QA Workspace/04 Conhecimento/Referências/Ambientes e Links de Trabalho|Ambientes e Links de Trabalho]] — aquela nota é o guia prático de URLs/acessos de DEV/HML/PROD do QA; esta aqui é a documentação conceitual de produto sobre os ambientes do sistema.

## Visão geral
- O SoGov é organizado em ambientes distintos, todos conectados entre si (usuários, funcionalidades e módulos se comunicam e trabalham juntos): **SOGO** (interno, com as sub-áreas Administrativo e Técnico) e **Externo** (com as sub-áreas Externo SOGO, Cliente e Externo Cidadão PF/PJ).

## Regras de negócio

### Permissões
- Ambiente SOGO tem um tipo de usuário próprio, diferente dos demais — permissões detalhadas na documentação do próprio ambiente (não vieram neste export, ver Dúvidas em aberto).
- Ambientes Cidadão e Servidor têm um único tipo de usuário cada, documentado nas respectivas docs.

### Administrativo SOGO
- Dedicado à gestão administrativa e financeira da SOGO: administração e controle de usuários e clientes.
- **Cadastro/gerenciamento de clientes** — campos: Tipo de cliente (Prefeitura, Câmara, Autarquia, outros), CNPJ, Razão social, Nome de exibição, Domínio, Licenças, Datas de início/término de contrato.
- **Cadastro/gerenciamento de colaboradores** — campos: Nome completo, E-mail, Setor, Nível do colaborador.

### Técnico SOGO
- Dedicado à criação, personalização e gerenciamento dos módulos — fundamental pra construir/ajustar módulos de tramitação alinhados ao contrato de cada cliente. Detalhe completo em [[QA Workspace/04 Conhecimento/Módulos/Construtor de Módulos|Construtor de Módulos]].
- Funcionalidades principais: criação e vinculação de módulos.

### Externo SOGO
- Funciona como o ambiente do cidadão, mas é feito pros colaboradores da SOGO — trocam informações e acompanham os documentos de comunicação entre a SOGO e os clientes.

### Cliente
- Espaço onde o cliente usa as soluções contratadas; cada cliente tem sua própria instância ("área de trabalho") com os módulos/soluções do contrato, mais as opções padrão e adicionais do sistema.
- **Funcionalidades padrão**: Cadastro e Gerenciamento de Usuários, Organograma (estrutura organizacional do cliente), Relatórios/Estatísticas, Módulos Disponibilizados, Etiquetas (organização por nível de prioridade).
- **Funcionalidades adicionais** (contratação à parte): Workflow (gestão/acompanhamento de fluxos de trabalho), Processos urbanísticos (ver [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]]).

### Externo Cidadão PF e PJ
- **Criação de Solicitações**: cidadão faz novas solicitações direto no sistema.
- **Acompanhamento de Solicitações**: cidadão monitora todas as interações/atualizações das próprias solicitações.

### Atualização — Backup completo de documentos para clientes em cancelamento (SGV-10028, 21/07/2026)
> Funcionalidade de uso **exclusivamente interno** — gerada pelo time SoGov, nunca pelo cliente final.

- **Objetivo**: permitir que administradores internos gerem um pacote de backup com todos os documentos/anexos vinculados ao ambiente do cliente, antes da descontinuação do contrato.
- **O que contém**: a totalidade dos documentos e anexos do ambiente do cliente selecionado, consolidados num arquivo único pra download.
- **Quem pode gerar**: só usuários SoGov nível **Admin** veem a ação de backup — outros perfis não veem a opção.
- **Onde e quando aparece**: no Gerenciador de Clientes, menu de ações (ícone de reticências) de cada cliente — só exibido pra clientes com status **Inativo** ou **Ativo** (cancelamento em processo, ou em uso), junto de Editar/Emitir documento/Ativar.
- **Fluxo**:
	1. **Solicitação**: seleciona "Backup" → modal "Backup de cliente" com a mensagem "Deseja mesmo realizar o backup de todos os arquivos de [cliente]? Esta ação poderá demorar um pouco." — Confirmar inicia a geração, Cancelar encerra sem processar nada.
	2. **Preparação**: montagem em segundo plano (usuário segue usando a plataforma normalmente). Painel "Transferência de arquivo(s)" mostra notificação "Backup [cliente]" com "Preparando seu arquivo..." e barra de progresso percentual — avanço contínuo e suave, nunca parado mais de 2s, só chega a 100% na conclusão real. Dá pra cancelar direto pela notificação enquanto prepara.
	3. **Conclusão/download**: notificação vira "O arquivo está pronto para ser baixado" + botão "Baixar arquivo" (ícone do painel passa a indicar arquivo disponível). Usuário logado na conclusão → download automático. Usuário offline na conclusão → fica salvo no painel pra download posterior.
	4. **E-mail**: assim que pronto, e-mail automático aos administradores com botão de download direto, template padrão (título "O backup de [cliente] está pronto para baixar!").
- **Regras gerais**:
	- Arquivo fica em nuvem (S3), disponível por **até 7 dias**; qualquer alteração/evento no documento original depois do backup **invalida** essa garantia; passado o prazo, precisa gerar outro backup.
	- Download automático só se o solicitante estiver logado na conclusão; senão, fica no painel + e-mail como caminho alternativo.
	- Notificação sempre nomeada no padrão "Backup [cliente]" — facilita achar entre várias transferências em andamento/concluídas.
- **Termos usados na doc**: Gerenciador de Clientes (área onde clientes SoGov são cadastrados/visualizados/organizados); menu de ações (reticências no card do cliente); painel de Transferência de arquivo(s) (componente da barra superior que centraliza downloads); S3 (armazenamento em nuvem usado pra hospedar os arquivos temporariamente).

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] Comentário de Alice Martins (09/02/2024, sem resposta registrada no export, 1 reação ✅ de alguém) pediu pra detalhar melhor o cadastro de clientes/colaboradores, citando como exemplo faltante "quais clientes estão vinculados a um colaborador" — informação que a doc atual não cobre.
- [ ] Seção "Permissões" só diz que os níveis "estão descritos na documentação do ambiente" / "também está descrito em sua documentação", sem detalhar aqui — não ficou claro se existe uma doc própria de permissões do ambiente SOGO no Notion ainda não importada, ou se a info nunca foi escrita.
- [ ] Backlog do Notion cita 1 item sem SGV: "[FUNCIONALIDADE-CX] Exportação/Backup completo de documentos para clientes em processo de cancelamento" — parece ser a origem da própria atualização SGV-10028 já documentada acima; confirmar se é o mesmo item (backlog desatualizado, deveria estar fechado) ou se falta algo adicional além do que já foi entregue.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- SGV-10028 — Backup completo de documentos pra clientes em cancelamento (21/07/2026, ver seção própria).

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Construtor de Módulos|Construtor de Módulos]] — detalhe completo do Ambiente Técnico SOGO.
- [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]] — funcionalidade adicional do Ambiente Cliente.
- [[QA Workspace/04 Conhecimento/Módulos/Configurações da Instância|Configurações da Instância]] — tela do Ambiente Cliente onde dados cadastrais (visualização) e tema/marca (edição) ficam disponíveis.
