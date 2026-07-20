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

> [!info]- Lista de acompanhamento — bater ponto a ponto com o time
> Fonte: view `[SP15 - 2026] Engenharia (BUG'S)` do Notion, exportada em 17/07. Sprint 14/07 → 28/07, em andamento (20%).
> **Como usar**: a linha do checkbox é curta de propósito — cole a decisão no fim dela, ex.: `→ já possui critérios`, `→ refinar (prioridade)`, `→ descartado: obsoleto`. Os detalhes (prioridade, dev, origem) ficam na sublinha. Card decidido como "refinar" → exportar o .md individual → mesa própria no `05 Refinar/` (fluxo 6).

> [!warning]- Export incompleto: 53 de 60 cards
> A view do Notion corta no "Load more" — faltam 7 cards. Pra completar: rolar a lista até o fim no Notion e exportar de novo (eu mesclo, sem perder as marcações daqui).

> [!tip] Progresso: **14/53** batidos (atualizado 2026-07-20)
> Homologação `1/9` · Teste dev `2/5` · Testando HML `0/1` · Revisar MR `9/11` · Em dev `1/4` · Impedimento `0/4` · Não reproduzido `0/5` · Backlog `1/7` · Produção `0/7`
> *Atualizar os contadores ao bater os cards (ou pedir numa sessão: "atualiza o progresso da triagem").*

## Disponível para homologação (9) — ação QA imediata

- [x] **[[QA Workspace/02 Demandas/Concluídas/5273 - Bug Login Senha Correta Apos Tentativas|SGV-5273]]** — Login com senha correta não funciona após tentativas incorretas ✅ 2026-07-20 → **aprovada em homologação**, card em Concluídas
    - `Altíssima` · Matheus Godoi
    - [MR !419](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/419) revisado (SKILL_REVISAO_ESCOPO_MR) — fix inverte a ordem senha↔tentativas, sem teste automatizado; card nasceu em `02 Demandas/HML/` (status real do Notion) e foi aprovado no mesmo dia — CT-B04 (Produção) segue em aberto como follow-up
- [ ] **SGV-3820** — Erro ao criar despacho e assinar documento via workflow
    - `Altíssima` · Washington Junior · API
- [ ] **SGV-7640** — Campo de busca de setor destinatário fica inutilizável após seleção inicial no ambiente do cidadão
    - `Alta` · Matheus Godoi · CX
- [ ] **SGV-4995** — Contagem de dias incorreta ao configurar prazos em etapas com prazo oficial pré-definido
    - `Alta` · Matheus Godoi
- [ ] **SGV-9690** — SGA: filtro de busca não localiza palavras com variações de caracteres especiais
    - `Média` · Lucas Cabral · CX
- [ ] **SGV-6975** — Erro 503 ao ativar clientes com status "Em implantação"
    - `Média` · Matheus Godoi · Sanidade-006
- [ ] **SGV-6083** — Edição de documento não atualiza o conteúdo na assinatura ou download
    - `Média` · Matheus Godoi
- [ ] **SGV-9808** — Documento, mesmo assinado, continua com status de "assinatura pendente"
    - `Baixa` · João Marcelo · CX · relacionado: 9809, 9870, 9842
- [ ] **SGV-8380** — Referência de resposta em despachos exibida incorretamente na cadeia de respostas
    - `Baixa` · Diogo Sobreira

## Pronto pra teste em dev (5)

- [ ] **[[QA Workspace/05 Refinar/SGV-4873|SGV-4873]]** — Assinaturas em anexos de documentos retificados não são canceladas corretamente
    - `Alta` · Matheus Godoi
    - ⚠️ Mesa de refinamento em andamento: possível conflito com regra nova de retificação — **não testar antes da decisão**
- [x] **SGV-7074** — Ao alterar módulo de um assunto/serviço os modelos de documentos não são atualizados ✅ 2026-07-17
    - `Altíssima` · Matheus Godoi
    - ⚠️ Relação com o [[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]] é só de longe — é outra coisa. **Lucas Beninca** construindo os critérios
- [x] **[[QA Workspace/02 Demandas/DEV/9610 - Bug Associar Documento Abertura Multi-Setor|SGV-9610]]** — Servidor não consegue associar documento na abertura de um novo documento ✅ 2026-07-17 → refinado, critérios de aceite no card, análise no Notion, mesa arquivada em 04 Conhecimento
    - `Baixa` · João Rodrigo · CX
    - Card no vault pronto pra validar em DEV (pendência na fila)
- [ ] **SGV-9548** — Campo de telefone no cadastro de instância não permite número fixo
    - `Baixa` · Matheus Godoi
- [ ] **SGV-9959** — Inconsistência de status entre drawer de solicitação e evento de assinatura após recusa em assinatura sequencial
    - `Média` · João Marcelo · status Notion: "Em ambiente teste/Dev"

## Testando em homologação (1)

- [ ] **SGV-6906** — Não é possível assinar documento em instância Em Implantação
    - `Média` · Lucas Lacerda · Sanidade-005

## Revisar MR (11) — esteira dev, revisar cenários quando couber

- [x] **SGV-9458** — Nome do destinatário exibido como "Anônimo" ao responder despacho de cidadão PJ ✅ 2026-07-17 → já possui critérios
    - `Altíssima` · Matheus Godoi
- [x] **SGV-9093** — Nome do solicitante exibido no evento de criação em solicitação sigilosa do cidadão ✅ 2026-07-17 → já possui critérios
    - `Altíssima` · Matheus Godoi
- [x] **SGV-9633** — Assinatura em fluxo de trabalho não pode ser concluída ✅ 2026-07-17 → já possui critérios
    - `Alta` · João Rodrigo · CX
- [x] **SGV-5783** — Representante legal incorreto na assinatura após fazer alteração ✅ 2026-07-17 → já possui critérios
    - `Alta` · Diogo Sobreira
    - [MR !581](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/581) revisado a nível de escopo em 2026-07-20 (cenários de teste implementados batem com o problema) — falta validação manual do fluxo de reemissão de certificado
- [x] **[[QA Workspace/02 Demandas/DEV/9750 - Bug Assinatura Pendente Documento Encerrado|SGV-9750]]** — Pedido de assinatura permanece pendente mesmo com documento sendo encerrado ✅ 2026-07-17 → já refinado, critérios no card
    - `Média` · Washington Junior · CX · API
    - Card no vault com critérios prontos; [MR !583](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/583) revisado a nível de escopo em 2026-07-20 (6 cenários batem com os 5 critérios) — pendência de revisar cenários concluída na fila
- [x] **SGV-7829** — Anexos do despacho não são carregados corretamente ao emitir e assinar como Cidadão ✅ 2026-07-17 → já possui critérios
    - `Média` · João Marcelo
- [x] **SGV-6873** — Download de documento temporário não corresponde à versão editada ✅ 2026-07-17 → já possui critérios
    - `Média` · Matheus Godoi · Sanidade-004
- [ ] **SGV-6348** — Edição de documentos "Em elaboração" não é exibida ao baixar documento
    - `Média` · Matheus Godoi
    - ⚠️ Parece o mesmo caso da SGV-6873 — verificar com o dev como a solução foi aplicada
- [x] **[[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]]** — Modelos automatizados perdem a referência dos campos dinâmicos (@) após alteração do módulo ✅ 2026-07-17 → já refinado, critérios no card
    - `Baixa` · Diogo Sobreira · CX
    - Card no vault com critérios prontos (esteira 3f)
- [ ] **SGV-9692** — SGA: lentidão ao salvar configurações de tramitação na criação de setores
    - `Baixa` · Diogo Sobreira · CX
    - [MR !573](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/573) revisado a nível de escopo em 2026-07-20 (troca de chamada individual por lote — bate com a lentidão; testes cobrem a regra de negócio, não performance) — ainda não batido/decidido
    - ⚠️ Caso de lentidão — verificar situação; tem relação com a SGV-8977?
- [x] **[[QA Workspace/02 Demandas/DEV/8977 - Bug Timeout Edicao Regras Organograma|SGV-8977]]** — Erro ao tentar editar regras de tramitação direto no organograma ✅ 2026-07-20 → refinado, card criado
    - `Baixa` · Washington Junior · CX · API
    - [MR !505](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/505) revisado a nível de escopo em 2026-07-20 (mesmo padrão N+1→lote da SGV-9692, aplicado ao Organograma) — card criado com critérios reescritos (timeout entregue foi 10s, não os 30s pedidos); falta validação real de volume

## Em desenvolvimento / Em andamento (4)

- [x] **SGV-9036** — Mensagens de erro são exibidas quando é selecionado um signatário para assinatura ✅ 2026-07-17 → já refinado, critérios no card
    - `Altíssima` · Washington Junior · API
    - ⚠️ Sem wikilink — não há card em `02 Demandas/`; "no card" aqui provavelmente é a task do Notion, não o vault. Sem material/MR em mãos pra confirmar (2026-07-20) — pendência de confirmação criada na fila em vez de card inventado
- [ ] **SGV-9841** — Login autenticando usuário em conta de outro servidor
    - `Alta` · Matheus Godoi · CX
- [ ] **SGV-9772** — Documento permanece com status "em aberto" e não abre ao clicar
    - `Alta` · Lucas Lacerda · CX
- [ ] **SGV-3786** — Exibição de erro 500 ao solicitar assinatura em documento sigiloso
    - `Média` · João Rodrigo · V2

## Em impedimento / Aguardando CX (4)

- [ ] **SGV-8095** — Ajuste de dados das Estatísticas > Aba Módulos
    - `Alta` · Ari Garcia · CX
- [ ] **SGV-9430** — Ajustes de responsividade no modal de posicionamento de assinaturas
    - Lucas Cabral · LEGADO
- [ ] **SGV-6568** — Erro ao solicitar assinatura gera múltiplas assinaturas duplicadas e registros incorretos na timeline
    - `Média` · Washington Junior · API · em análise · PM Paulo Afonso
- [ ] **SGV-9807** — Cidadão PJ não consegue assinar documento
    - `Média` · sem dev · CX · aguardando retorno do CX

## Não reproduzido (5) — validar descarte?

- [ ] **SGV-8870** — Toggle de abertura externa está setado na criação de Assunto e Serviço
    - `Altíssima` · Lucas Lacerda
- [ ] **SGV-6954** — Tela de posicionamento de assinatura em loading infinito com múltiplos anexos e signatários
    - `Média` · João Marcelo · Sanidade-006
- [ ] **SGV-6256** — Demora para exibir lista de assinaturas após assinar documentos
    - `Média` · sem dev
- [ ] **SGV-6166** — Falha na exibição e conclusão de assinaturas
    - `Média` · João Rodrigo · PM Paulo Afonso
- [ ] **SGV-5970** — Documento impresso não exibe selo de todas as assinaturas realizadas em paralelo
    - `Média` · Diogo Sobreira

## A fazer / Backlog (7)

- [ ] **SGV-5360** — Assinatura de despacho customizado não aparece na tela de "Assinaturas pendentes" do servidor
    - `Média` · João Marcelo
- [x] **[[QA Workspace/99 Arquivo/Bug Assinatura Despacho Desassociacao|SGV-3413]]** — Erro ao assinar despacho de desassociação de documentos ✅ 2026-07-20 → descartado, não reproduz mais
    - `Média` · Squad 3
    - Verificado diretamente por Rafael (20/07) — card criado já como descartado em `99 Arquivo/`, sem material de causa raiz disponível
- [ ] **SGV-5245** — Nome do mês e ano incorretos no filtro de data da Mesa de Trabalho
    - `Média` · Lucas Lacerda
- [ ] **SGV-3412** — Marcação automática incorreta de checkbox na Lista de Solicitações de Assinaturas
    - `Média` · Squad 3
- [ ] **[[QA Workspace/02 Demandas/DEV/9977 - Bug Nome Oculto Cópia Despacho|SGV-9977]]** — Nome do envolvido em cópia fica oculto no componente do despacho após emissão
    - `Baixa` · sem dev
    - ⚠️ Divergência: vault tem card **aberto em DEV**; Notion diz Backlog
- [ ] **[[QA Workspace/02 Demandas/HML/9971 - Bug Assinatura Servidor Não Aprovado|SGV-9971]]** — Está sendo possível solicitar assinatura para servidor com cadastro "A aprovar"
    - `Baixa` · sem dev
    - ⚠️ Divergência: vault tem card **em validação em HML**; Notion diz Backlog
- [ ] **SGV-8395** — Comentários do evento de abertura não são incluídos ao baixar pelo download personalizado
    - `Baixa` · Matheus Godoi

## Em produção / Aprovado / Concluído (7) — conferir encerramento

- [ ] **[[QA Workspace/02 Demandas/Concluídas/9237 - Bug Download Tramitação Interna|SGV-9237]]** — Download realizado por cidadão inclui conteúdo de tramitação interna
    - `Alta` · Bruno Clementino
    - Vault: concluído ✓
- [ ] **SGV-8385** — Definição de caminhos alternativos no fluxo de trabalho (etapas não obrigatórias)
    - `Alta` · Marcos Vinicius · Melhoria · CX
- [ ] **SGV-9112** — Implementar o avanço até uma etapa específica a partir do split-button (parte 2)
    - Marcos Vinicius · Tarefa
    - Retestada e aprovada em homologação em 16/07
- [ ] **[[QA Workspace/02 Demandas/Concluídas/10123 - Bug Retrocesso Etapa Após Atalho|SGV-10123]]** — Cluster de setor responsável não aparece ao retroceder etapa avançada por atalho
    - `Média` · Marcos Vinicius
    - Vault: concluído ✓ (Notion: Aprovado por QA)
- [ ] **SGV-10075** — Problemas na visualização de conteúdo em processo em tramitação para Cidadão
    - `Média` · João Marcelo · CX · Notion: Concluído
- [ ] **SGV-5548** — Aprimorar posicionamento da assinatura em documentos
    - `Alta` · Lucas Cabral · Melhoria · CX
- [ ] **SGV-9474** — Diferença entre tela de rastrear documentos em prod e o Figma
    - `Baixa` · B. Luan

---

## Registro da triagem

- 2026-07-17 - Lista criada a partir do export da view SP15 (53/60 cards — 7 faltando por corte do "Load more")
- 2026-07-17 - Reformatada pra leitura: linha do checkbox só com ID + título; prioridade/dev/origem na sublinha
- 2026-07-17 - Primeira batida (10/53): 9458, 9093, 9633, 5783, 7829, 6873 → já possuem critérios; 9750, 9963, 8977, 9036 → já refinados, critérios no card. Investigações abertas: 6348 (mesmo caso da 6873?), 9692 (relação com 8977?), 7074 (critérios com Lucas Beninca)
- 2026-07-17 - Correção: SGV-9474 tinha ficado de fora da lista na montagem (erro de transcrição) — incluído em Em produção; grupo agora com 7
- 2026-07-17 - Segunda batida (12/53): **9610** → refinado de ponta a ponta (card no vault com CTs, análise no Notion, mesa arquivada em 04 Conhecimento); **7074** → critérios sendo construídos com Lucas Beninca. Painel de progresso adicionado no topo (contador geral + por grupo)
