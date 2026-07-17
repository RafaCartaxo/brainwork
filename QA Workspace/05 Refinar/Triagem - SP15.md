---
tags:
  - qa
  - triagem
sprint: SP15
status: em_andamento
data: 2026-07-17
responsavel: Rafael
---
# Triagem SP15 — Engenharia (BUG'S)

> [!info] Lista de acompanhamento — bater ponto a ponto com o time
> Fonte: view `[SP15 - 2026] Engenharia (BUG'S)` do Notion, exportada em 17/07. Sprint 14/07 → 28/07, em andamento (20%).
> **Como usar**: ao bater cada card, marcar o checkbox com a decisão entre parênteses — ex.: `(refinar — prioridade)`, `(validar em dev)`, `(descartado: obsoleto)`, `(já com dev, aguardar)`. Card decidido como "refinar" → exportar o .md individual dele → mesa própria aqui no `05 Refinar/` (fluxo 6).

> [!warning] Export incompleto: 53 de 60 cards
> A view do Notion corta no "Load more" — faltam 7 cards. Pra completar: rolar a lista até o fim no Notion e exportar de novo (eu mesclo, sem perder as marcações daqui).

## Disponível para homologação (9) — ação QA imediata

- [ ] SGV-5273 - [BUG] Login com senha correta não funciona após tentativas incorretas (Altíssima · Matheus Godoi)
- [ ] SGV-3820 - [BUG][API] Erro ao criar despacho e assinar documento via workflow (Altíssima · Washington Junior)
- [ ] SGV-7640 - [BUG-CX] Campo de busca de setor destinatário fica inutilizável após seleção inicial no ambiente do cidadão (Alta · Matheus Godoi)
- [ ] SGV-4995 - [BUG] Contagem de dias incorreta ao configurar prazos em etapas com prazo oficial pré-definido (Alta · Matheus Godoi)
- [ ] SGV-9690 - [BUG-CX] SGA - Filtro de busca não localiza palavras com variações de caracteres especiais (Média · Lucas Cabral)
- [ ] SGV-6975 - [BUG](Sanidade-006/2026) Erro 503 ao ativar clientes com status "Em implantação" (Média · Matheus Godoi)
- [ ] SGV-6083 - Edição de documento não está atualizando o conteúdo no momento da assinatura ou download (Média · Matheus Godoi)
- [ ] SGV-9808 - [BUG-CX] Documento, mesmo assinado, continua com status de "assinatura pendente" (relacionado: 9809, 9870, 9842) (Baixa · João Marcelo)
- [ ] SGV-8380 - [BUG] Referência de resposta em despachos exibida incorretamente na cadeia de respostas (Baixa · Diogo Sobreira)

## Pronto pra teste em dev (5)

- [ ] [[QA Workspace/05 Refinar/SGV-4873|SGV-4873]] - [BUG] Assinaturas em Anexos de Documentos Retificados não são Canceladas Corretamente (Alta · Matheus Godoi) — **mesa de refinamento em andamento: possível conflito com regra nova de retificação, não testar antes da decisão**
- [ ] SGV-7074 - [BUG] Ao alterar módulo de um assunto/serviço os modelos de documentos não são atualizados (Altíssima · Matheus Godoi) — parente do [[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]]?
- [ ] SGV-9610 - [BUG-CX] Servidor não consegue associar documento na abertura de um novo documento (Baixa · João Rodrigo)
- [ ] SGV-9548 - [BUG] Campo de telefone no cadastro de instância não permite número fixo (Baixa · Matheus Godoi)
- [ ] SGV-9959 - [BUG] Inconsistência de status entre drawer de solicitação e evento de assinatura após recusa em assinatura sequencial (Média · João Marcelo) — status Notion: "Em ambiente teste/Dev"

## Testando em homologação (1)

- [ ] SGV-6906 - [BUG](Sanidade-005/2026) Não é possível assinar documento em instância Em Implantação (Média · Lucas Lacerda)

## Revisar MR (11) — esteira dev, revisar cenários quando couber

- [x] SGV-9458 - [BUG] Nome do destinatário exibido como "Anônimo" ao responder despacho de cidadão PJ (Altíssima · Matheus Godoi) ✅ 2026-07-17
- [x] SGV-9093 - [BUG] Nome do solicitante exibido no evento de criação em solicitação sigilosa do cidadão (Altíssima · Matheus Godoi) ✅ 2026-07-17
- [x] SGV-9633 - [BUG-CX] Assinatura em fluxo de trabalho não pode ser concluída (Alta · João Rodrigo) ✅ 2026-07-17
- [ ] SGV-5783 - [BUG] Representante legal incorreto na assinatura após fazer alteração (Alta · Diogo Sobreira)
- [ ] [[QA Workspace/02 Demandas/DEV/9750 - Bug Assinatura Pendente Documento Encerrado|SGV-9750]] - [BUG-CX][API] Pedido de assinatura permanece pendente mesmo com documento sendo encerrado (Média · Washington Junior) — card no vault com critérios prontos; pendência de revisar cenários já na fila
- [ ] SGV-7829 - [BUG] Anexos do despacho não são carregados corretamente ao emitir e assinar como Cidadão (Média · João Marcelo)
- [ ] SGV-6873 - [BUG](Sanidade-004/2026) Download de documento temporário não corresponde à versão editada (Média · Matheus Godoi)
- [ ] SGV-6348 - [BUG] Edição de documentos com status de "Em elaboração" não são exibidos ao baixar documento (Média · Matheus Godoi)
- [ ] [[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]] - [BUG-CX] Modelos de documentos automatizados perdem a referência dos campos dinâmicos (@) após alteração do módulo (Baixa · Diogo Sobreira) — card no vault com critérios prontos (esteira 3f)
- [ ] SGV-9692 - [BUG-CX] SGA - Lentidão ao salvar configurações de tramitação na criação de setores (Baixa · Diogo Sobreira)
- [ ] SGV-8977 - [BUG-CX][API] Erro ao tentar editar regras de tramitação direto no organograma (Baixa · Washington Junior)

## Em desenvolvimento / Em andamento (4)

- [ ] SGV-9036 - [BUG][API] Mensagens de erro são exibidas quando é selecionado um signatário para assinatura (Altíssima · Washington Junior)
- [ ] SGV-9841 - [BUG-CX] Login autenticando usuário em conta de outro servidor (Alta · Matheus Godoi)
- [ ] SGV-9772 - [BUG-CX] Documento permanece com status "em aberto" e não abre ao clicar (Alta · Lucas Lacerda)
- [ ] SGV-3786 - [BUG - V2] Exibição de erro 500 ao solicitar assinatura em documento sigiloso (Média · João Rodrigo)

## Em impedimento / Aguardando CX (4)

- [ ] SGV-8095 - [BUG-CX] Ajuste de dados das Estatísticas > Aba Módulos (Alta · Ari Garcia)
- [ ] SGV-9430 - [BUG][LEGADO] Ajustes de responsividade no modal de posicionamento de assinaturas (Lucas Cabral)
- [ ] SGV-6568 - [API][EM ANÁLISE] Erro ao solicitar assinatura gera múltiplas assinaturas duplicadas e registros incorretos na timeline — PM Paulo Afonso (Média · Washington Junior)
- [ ] SGV-9807 - [BUG-CX] Cidadão PJ não consegue assinar documento (Média · sem dev) — status: aguardando retorno do CX

## Não reproduzido (5) — validar descarte?

- [ ] SGV-8870 - [BUG] Toggle de abertura externa está setado na criação de Assunto e Serviço (Altíssima · Lucas Lacerda)
- [ ] SGV-6954 - [BUG](Sanidade-006/2026) Tela de posicionamento de assinatura em loading infinito com múltiplos anexos e signatários (Média · João Marcelo)
- [ ] SGV-6256 - [BUG] Demora para exibir lista de assinaturas após assinar documentos (Média · sem dev)
- [ ] SGV-6166 - [SOGOV + PM Paulo Afonso] Falha na Exibição e Conclusão de Assinaturas (Média · João Rodrigo)
- [ ] SGV-5970 - [BUG] Documento impresso não exibe selo de todas as assinaturas realizadas em paralelo (Média · Diogo Sobreira)

## A fazer / Backlog (7)

- [ ] SGV-5360 - [BUG] Assinatura de despacho customizado não aparece na tela de "Assinaturas pendentes" do servidor (Média · João Marcelo)
- [ ] SGV-3413 - [BUG] Erro ao assinar despacho de desassociação de documentos (Média · Squad 3)
- [ ] SGV-5245 - [BUG] Nome do mês e ano incorretos no filtro de data da Mesa de Trabalho (Média · Lucas Lacerda)
- [ ] SGV-3412 - Marcação automática incorreta de checkbox na Lista de Solicitações de Assinaturas (Média · Squad 3)
- [ ] [[QA Workspace/02 Demandas/DEV/9977 - Bug Nome Oculto Cópia Despacho|SGV-9977]] - [BUG] Nome do envolvido em cópia fica oculto no componente do despacho após emissão (Baixa) — **vault: card em DEV, aberto** (Notion diz Backlog)
- [ ] [[QA Workspace/02 Demandas/HML/9971 - Bug Assinatura Servidor Não Aprovado|SGV-9971]] - [BUG] Está sendo possível solicitar assinatura para servidor com cadastro "A aprovar" (Baixa) — **vault: card em HML, em validação** (Notion diz Backlog — divergência a alinhar)
- [ ] SGV-8395 - [BUG] Comentários do evento de abertura não são incluídos ao baixar pelo download personalizado (Baixa · Matheus Godoi)

## Em produção / Aprovado / Concluído (6) — conferir encerramento

- [ ] [[QA Workspace/02 Demandas/Concluídas/9237 - Bug Download Tramitação Interna|SGV-9237]] - [BUG] Download realizado por cidadão inclui conteúdo de tramitação interna (Alta · Bruno Clementino) — vault: concluído ✓
- [ ] SGV-8385 - [Melhoria-CX] Definição de caminhos alternativos no fluxo de trabalho (etapas não obrigatórias) (Alta · Marcos Vinicius)
- [ ] SGV-9112 - [DEV][PARTE 2] Implementar o avanço até uma etapa específica a partir do split-button (Tarefa · Marcos Vinicius) — retestada e aprovada em homologação em 16/07
- [ ] [[QA Workspace/02 Demandas/Concluídas/10123 - Bug Retrocesso Etapa Após Atalho|SGV-10123]] - [BUG] Cluster de setor responsável não aparece ao retroceder etapa avançada por atalho (Média · Marcos Vinicius) — vault: concluído ✓ (Notion: Aprovado por QA)
- [ ] SGV-10075 - [BUG-CX] Problemas na visualização de conteúdo em processo em tramitação para Cidadão (Média · João Marcelo) — Notion: Concluído
- [ ] SGV-5548 - [Melhoria-CX] Aprimorar posicionamento da assinatura em documentos (Alta · Lucas Cabral)

---

## Registro da triagem

- 2026-07-17 - Lista criada a partir do export da view SP15 (53/60 cards — 7 faltando por corte do "Load more")
