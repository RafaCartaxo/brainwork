---
title: Usuário Sogo
tags:
  - qa
  - conhecimento
  - sogov
  - usuario-sogo
tipo: modulo
revisado: 2026-10-14
fonte: https://app.notion.com/p/alfa-group/Usu-rio-Sogo-f32e8e606afa42509c12920e69f06d25
fonte_criado: 2024-09-17 (Alice Martins)
fonte_ultima_edicao: 2026-04-10 (Ivo Costa)
---
# Usuário Sogo

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-14 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria (campo `Task` vazio no Notion).

## Visão geral
- Usuários SOGO são os que têm acesso ao **Ambiente Sogo** e aos ambientes dos clientes, de acordo com as permissões do seu nível — ver [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]].

## Regras de negócio

### Níveis de usuário (cada nível herda as permissões do anterior)
- **Financeiro**: acessar a área de gerenciamento de clientes; visualizar e editar clientes cadastrados; cadastrar novos clientes; emitir documentos para o cliente; inadimplência.
- **Analista**: tudo do Financeiro, mais — acessar ambientes dos clientes vinculados ao seu cadastro, em modo **leitura**; acessar o ambiente técnico em modo leitura.
- **Suporte/Implantação**: tudo do Analista, mais — cadastrar e editar setores no organograma; cadastrar e editar serviços e assuntos; cadastrar e editar servidores; cadastrar e editar cidadãos; cadastrar e editar grupos de contato; acessar as mesas de todos os setores do cliente; visualizar os documentos das mesas.
- **Administrador**: tudo do Suporte, mais — **inativar cliente** (ver Dúvidas em aberto sobre duplicidade na lista deste nível no export).

### Dados de cadastro
- Campos: Nome completo; Email; Setor; Nível; Foto (opcional); Clientes vinculados (opcional).
- **Email**: não pode ser o mesmo já cadastrado como cidadão SoGov ou como servidor de alguma instância. Pode usar e-mail institucional de alguma instância (sem limitação); as notificações podem se misturar nesse caso, mas cabe ao usuário se organizar.
- **Clientes vinculados** (opcional): os únicos clientes cujos ambientes o usuário poderá acessar por esse vínculo — não impacta o acesso dele à visualização/edição de módulos desse ou de outros clientes, caso tenha nível de permissão pro ambiente técnico. **Não é necessário** para usuários Administrador e Financeiro (Financeiro não acessa ambiente de clientes; Administrador já acessa todos).
- Ao concluir o cadastro, uma senha de acesso **provisória** é enviada para o e-mail cadastrado.

### Listagem
- Colunas: Nome do usuário, Setor, Nível, Email, Status, menu kebab.
- Filtros/busca: input de busca por nome; filtro de Status, Setor e Nível; ordenação alfabética.

### Menu kebab
- Ativar/Inativar, Editar, Excluir.

### Editar
- Só **Administrador** edita colaboradores — inclusive a si próprio, **exceto o próprio nível** (nível só muda por outro administrador).
- Campos editáveis na edição: Nome, Email, Setor, Nível, Foto.

### Meu perfil
- O usuário edita todos os campos do próprio cadastro, **exceto o Nível** (só administrador edita).
- Também é onde o usuário troca a própria senha.

### Regras gerais
- Administrador é quem cadastra novos usuários SOGO.
- Acesso de usuário SOGO é via e-mail cadastrado.
- Níveis com acesso ao ambiente do cliente **não** podem interagir nos documentos (ver Dúvidas em aberto sobre o limite exato de "interagir").
- Excluir um usuário SOGO **preserva** o histórico de tudo que ele fez no sistema.
- Inativar a conta impede o acesso, mas **não** reseta os dados de acesso.
- Troca de senha exige confirmação com a senha atual.
- Troca de e-mail **não** precisa de confirmação por e-mail — é direta na plataforma.
- E-mail de login não pode já estar cadastrado no SoGov (evita misturar notificações).

### Atualização — Histórico e impressão de documentos (10/04/2026)
- Usuário Sogo ganha consulta ao **histórico** de documentos tramitados — cronologia completa de mudanças na abertura, quando existir.
- Ganha também permissão de **download** do documento, seguindo exatamente as mesmas regras já aplicadas ao perfil Servidor que já tem acesso ao documento.

### Atualização — Rastrear documento (10/04/2026)
- Funcionalidade de **Rastrear documento** liberada pro usuário Sogo, com adaptação na interface de busca: como ele não tem vínculo com setores internos, o radiobutton **"Buscar em meus setores participantes"** vem **desabilitado**.
- Por padrão, vem marcada a opção **"Buscar em setores que eu não participo"** — busca abrangente em todos os setores disponíveis, ao acessar a instância de qualquer cliente, sem precisar de ajuste manual do usuário.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] A lista de permissões do nível **Administrador** repete, palavra por palavra, duas permissões já listadas pro nível **Suporte/Implantação** ("Acessar as mesas de todos os setores do cliente" e "Visualizar os documentos das mesas") — provável erro de cópia no Notion. A única permissão claramente nova do Administrador é "Inativar cliente"; confirmar se não falta alguma permissão que deveria estar listada ali.
- [ ] A regra geral "níveis com acesso ao ambiente do cliente não poderão ter acesso para interagir nos documentos" não especifica o que conta como "interagir" (despachos? respostas?), nem se as permissões de histórico/download liberadas em 10/04/2026 contam como "interação" ou ficam de fora por serem só consulta. Confirmar o limite exato.
- [ ] Backlog do Notion cita 2 itens sem SGV: "[Melhoria] Usuário sogo pode imprimir e visualizar histórico dos documentos" e "[Melhoria] Permitir que usuários sogo também tenham acesso ao menu rastrear documento" — parecem ser a **origem** das duas atualizações de 10/04/2026 já documentadas acima. Confirmar se são o mesmo item (backlog desatualizado, deveria estar fechado) ou se falta algo além do que já foi entregue.
- [ ] Notion mostra "1 backlink" no topo da página, não identificado no export — alguma outra página do Notion referencia esta.
- [x] ~~Os exports de **Usuário Cidadão** e **Usuário Servidor**, baixados junto deste, vieram **vazios**~~ — reexportados e processados em 2026-10-14. Ver [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] e [[QA Workspace/04 Conhecimento/Módulos/Usuário Servidor|Usuário Servidor]].

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- Sem SGV vinculado — documentação de referência.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Ambientes SoGov|Ambientes SoGov]] — contexto do Ambiente SOGO onde esse tipo de usuário atua.
- [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] e [[QA Workspace/04 Conhecimento/Módulos/Usuário Servidor|Usuário Servidor]] — os outros dois tipos de usuário do sistema.
