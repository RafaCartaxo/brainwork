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
> Fonte: view `[SP15 - 2026] Engenharia (BUG'S)` do Notion, exportada em 17/07, **reconciliada com novo export de 22/07 13:25**. Sprint 14/07 → 28/07, em andamento (29,33%).
> **Como usar**: a linha do checkbox é curta de propósito — cole a decisão no fim dela, ex.: `→ já possui critérios`, `→ refinar (prioridade)`, `→ descartado: obsoleto`. Os detalhes (prioridade, dev, origem) ficam na sublinha. Card decidido como "refinar" → exportar o .md individual → mesa própria no `05 Refinar/` (fluxo 6).

> [!warning]- Export ainda incompleto: 53 de 75 cards
> O export de 22/07 continua cortando no "Load more" — captura 53 cards, mas o rodapé do Notion agora diz **Count 75** (antes o total estimado era 60). Faltam ~22 cards. Pra completar: rolar a lista até o fim no Notion e exportar de novo (eu mesclo, sem perder as marcações daqui). **11 cards que estavam na triagem antiga não vieram neste corte** (ver seção "Fora do export atual" no fim) — preservados, não apagados.

> [!tip] Progresso: **20/65** batidos (53 no export + 11 preservados fora do corte + SGV-8574 registrada na consolidação — atualizado 2026-07-23)
> Homologação `2/7` · Teste dev `5/10` · Testando HML `1/2` · Revisar MR `3/8` · Em dev `0/3` · Impedimento/CX `1/4` · Não reproduzido `1/6` · Backlog `0/2` · Aprovado no Dev `1/1` · Produção `2/11` · Fora do export `4/11`
> *Atualizar os contadores ao bater os cards (ou pedir numa sessão: "atualiza o progresso da triagem").*

## Disponível para homologação (7) — ação QA imediata

- [ ] **SGV-8870** — Toggle de abertura externa está setado na criação de Assunto e Serviço
    - `Altíssima` · Lucas Lacerda · Squad 2
    - ⚠️ Notion mudou de **Não reproduzido → Disponível para homologação** (22/07) — voltou a ser testável
- [ ] **SGV-7640** — Campo de busca de setor destinatário fica inutilizável após seleção inicial no ambiente do cidadão
    - `Alta` · Matheus Godoi · CX
- [ ] **SGV-4995** — Contagem de dias incorreta ao configurar prazos em etapas com prazo oficial pré-definido
    - `Alta` · Matheus Godoi
- [x] **[[QA Workspace/02 Demandas/Concluídas/9959 - Bug Inconsistência Status Drawer Evento Recusa Assinatura Sequencial|SGV-9959]]** — Inconsistência de status entre drawer de solicitação e evento de assinatura após recusa em assinatura sequencial ✅ 2026-07-23 → aprovada em HML, card criado enxuto em Concluídas/
    - `Média` · João Marcelo · Squad 3
    - Notion: Pronto pra teste em dev → Disponível para homologação (22/07) → aprovada por QA em homologação (23/07)
- [x] **[[QA Workspace/02 Demandas/Concluídas/9750 - Bug Assinatura Pendente Documento Encerrado|SGV-9750]]** — Pedido de assinatura permanece pendente mesmo com documento sendo encerrado ✅ 2026-07-17 → já refinado, critérios no card
    - `Média` · Washington Junior · CX · API · Squad 1
    - Card no vault com critérios prontos; [MR !583](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/583) revisado a nível de escopo em 2026-07-20 (6 cenários batem com os 5 critérios) — pendência de revisar cenários concluída na fila
    - ⚠️ Notion mudou de **Revisar MR → Disponível para homologação** (22/07) — pronto pra validar em HML
- [ ] **SGV-9690** — SGA: filtro de busca não localiza palavras com variações de caracteres especiais
    - `Média` · Lucas Cabral · CX · deadline 30/07
- [ ] **SGV-6083** — Edição de documento não atualiza o conteúdo na assinatura ou download
    - `Média` · Matheus Godoi

## Pronto pra teste em dev (10)

- [x] **SGV-9458** — Nome do destinatário exibido como "Anônimo" ao responder despacho de cidadão PJ ✅ 2026-07-17 → já possui critérios
    - `Altíssima` · Matheus Godoi
    - ⚠️ Notion mudou de **Revisar MR → Pronto pra teste em dev** (22/07)
- [x] **SGV-9093** — Nome do solicitante exibido no evento de criação em solicitação sigilosa do cidadão ✅ 2026-07-17 → já possui critérios
    - `Altíssima` · Matheus Godoi · Squad 2
    - ⚠️ Notion mudou de **Revisar MR → Pronto pra teste em dev** (22/07)
- [x] **SGV-7074** — Ao alterar módulo de um assunto/serviço os modelos de documentos não são atualizados ✅ 2026-07-17
    - `Altíssima` · Matheus Godoi
    - ⚠️ Relação com o [[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]] é só de longe — é outra coisa. **Lucas Beninca** construindo os critérios
- [ ] **SGV-6427** — Possibilidade de um documento virar selo e aplicação num anexo PDF
    - `Alta` · Gabriel Alves (designer) · Funcionalidade · 🆕 card novo neste export (22/07)
- [ ] **SGV-8129** — Estado de hover ao arrastar selo não segue protótipo (decisão de design sobre o cursor)
    - `Baixa` · Lucas Lacerda · Squad 2 · 🆕 card novo neste export (22/07)
- [x] **SGV-5783** — Representante legal incorreto na assinatura após fazer alteração ✅ 2026-07-17 → já possui critérios
    - `Alta` · Diogo Sobreira · Squad 1
    - [MR !581](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/581) revisado a nível de escopo em 2026-07-20 (cenários de teste implementados batem com o problema) — falta validação manual do fluxo de reemissão de certificado
    - ⚠️ Notion mudou de **Revisar MR → Pronto pra teste em dev** (22/07)
- [ ] **[[QA Workspace/05 Refinar/SGV-4873|SGV-4873]]** — Assinaturas em anexos de documentos retificados não são canceladas corretamente
    - `Alta` · Matheus Godoi
    - ⚠️ Mesa de refinamento em andamento: possível conflito com regra nova de retificação — **não testar antes da decisão**
- [x] **SGV-6873** — Download de documento temporário não corresponde à versão editada ✅ 2026-07-17 → já possui critérios
    - `Média` · Matheus Godoi · Sanidade-004 · Squad 2
    - ⚠️ Notion mudou de **Revisar MR → Pronto pra teste em dev** (22/07)
- [ ] **SGV-6348** — Edição de documentos "Em elaboração" não é exibida ao baixar documento
    - `Média` · Matheus Godoi · Squad 2
    - ⚠️ Parece o mesmo caso da SGV-6873 — verificar com o dev como a solução foi aplicada
    - ⚠️ Notion mudou de **Revisar MR → Pronto pra teste em dev** (22/07)
- [ ] **SGV-6136** — [SOGOV+PM Conde] Divergência de logo e título na visualização do processo
    - `Média` · Matheus Godoi · Squad 2 · 🆕 card novo neste export (22/07)

## Testando em homologação (2)

- [x] **SGV-3820** — Erro ao criar despacho e assinar documento via workflow ✅ 2026-07-23 → **duplicada de SGV-9633**
    - `Altíssima` · Washington Junior · API
    - ⚠️ Notion mudou de **Disponível para homologação → Testando em homologação** (22/07)
    - 🧭 Decisão de triagem (23/07): mesmo problema da SGV-9633 → tratada lá. **Já tinha sido reaberta** anteriormente; agora consolidada como duplicada da master 9633
- [ ] **[[QA Workspace/02 Demandas/HML/6906 - Bug Documentos Teste Implantacao Recebem Numeracao Ao Assinar|SGV-6906]]** — Não é possível assinar documento em instância Em Implantação
    - `Média` · Lucas Lacerda · Sanidade-005
    - 🔴 Reaberta em HML (22/07): impedimento de e-mail contornado; bug original resolvido (assinatura Em Implantação OK), mas documentos de teste ganham numeração e escapam da limpeza de "Sem numeração" da implantação — permanecem válidos na base. Card criado, aguardando dev corrigir — ver daily 22/07

## Revisar MR (8) — esteira dev, revisar cenários quando couber

- [ ] **SGV-10246** — Erro ao emitir e assinar despacho como cidadão
    - `Altíssima` · João Marcelo · Squad 3 · 🆕 card novo neste export (22/07)
- [x] **SGV-9036** — Mensagens de erro são exibidas quando é selecionado um signatário para assinatura ✅ 2026-07-17 → já refinado, critérios no card
    - `Altíssima` · Washington Junior · API · Squad 1
    - ⚠️ Sem wikilink — não há card em `02 Demandas/`; "no card" aqui provavelmente é a task do Notion, não o vault. Sem material/MR em mãos pra confirmar (2026-07-20) — pendência de confirmação criada na fila em vez de card inventado
    - ⚠️ Notion mudou de **Em desenvolvimento → Revisar MR** (22/07) — dev entregou, revisar cenários quando disponível
- [ ] **SGV-7935** — Evento de emissão de documento não é exibido na timeline ao emitir pela toolbar
    - `Altíssima` · Diogo Sobreira · Squad 1 · também em SP16 · 🆕 card novo neste export (22/07)
- [x] **SGV-9633** — Assinatura em fluxo de trabalho não pode ser concluída ✅ 2026-07-23 → **master, Pronto pra dev** (SGV-3820 e SGV-8574 são o mesmo problema, tratadas aqui)
    - `Alta` · João Rodrigo · CX · Squad 3
    - 🧭 Decisão de triagem (23/07, validada com o time): 9633/3820/8574 são o mesmo problema → **todas tratadas na 9633**. Esta é a master (Pronto pra dev); 3820 e 8574 marcadas como duplicadas. (Já possuía critérios desde 17/07)
- [x] **SGV-8574** — (mesmo problema da SGV-9633: assinatura em fluxo de trabalho) ✅ 2026-07-23 → **duplicada de SGV-9633**
    - `—` · API
    - 🧭 Decisão de triagem (23/07): consolidada na master 9633. ⚠️ Não estava neste export da triagem — adicionada aqui só para registrar a decisão (conferir no próximo export completo do Notion)
- [ ] **SGV-7337** — Impossibilidade de alterar serviço de um fluxo de trabalho
    - `Média` · Matheus Godoi · Squad 2 · também em SP16 · 🆕 card novo neste export (22/07)
- [ ] **SGV-6568** — Erro ao solicitar assinatura gera múltiplas assinaturas duplicadas e registros incorretos na timeline
    - `Média` · Washington Junior · API · em análise · PM Paulo Afonso · Squad 1
    - ⚠️ Notion mudou de **Em impedimento → Revisar MR** (22/07) — saiu do impedimento, dev entregou
- [ ] **SGV-5245** — Nome do mês e ano incorretos no filtro de data da Mesa de Trabalho
    - `Média` · Lucas Lacerda · Squad 2
    - ⚠️ Notion mudou de **Backlog → Revisar MR** (22/07) — entrou em desenvolvimento e dev entregou

## Em desenvolvimento / Em andamento (3)

- [ ] **SGV-9841** — Login autenticando usuário em conta de outro servidor
    - `Alta` · Matheus Godoi · CX
- [ ] **SGV-6094** — [API] Erro ao alterar o setor principal
    - `Média` · Washington Junior · CX · Squad 1 · também em SP16 · 🆕 card novo neste export (22/07)
- [ ] **SGV-5360** — Assinatura de despacho customizado não aparece na tela de "Assinaturas pendentes" do servidor
    - `Média` · João Marcelo · Squad 3
    - ⚠️ Notion mudou de **Backlog → Em desenvolvimento** (22/07) — entrou em dev

## Em impedimento / Aguardando CX (4)

- [ ] **SGV-8095** — Ajuste de dados das Estatísticas > Aba Módulos
    - `Alta` · Ari Garcia · CX
- [ ] **SGV-9772** — Documento permanece com status "em aberto" e não abre ao clicar
    - `Alta` · Lucas Lacerda · CX · Squad 2 · status Notion: "Aguardando retorno do CX"
    - ⚠️ Notion mudou de **Em desenvolvimento → Aguardando retorno do CX** (22/07) — bloqueou aguardando CX
- [ ] **SGV-9807** — Cidadão PJ não consegue assinar documento
    - `Média` · sem dev · CX · aguardando retorno do CX
- [x] **SGV-7829** — Anexos do despacho não são carregados corretamente ao emitir e assinar como Cidadão ✅ 2026-07-17 → já possui critérios
    - `Média` · João Marcelo · Squad 3
    - ⚠️ Notion mudou de **Revisar MR → Em impedimento** (22/07) — retrocedeu pra impedimento (revisar motivo com o time)

## Não reproduzido (6) — validar descarte?

- [ ] **SGV-6954** — Tela de posicionamento de assinatura em loading infinito com múltiplos anexos e signatários
    - `Média` · João Marcelo · Sanidade-006 · Squad 3
- [ ] **SGV-6256** — Demora para exibir lista de assinaturas após assinar documentos
    - `Média` · sem dev
- [ ] **SGV-6166** — Falha na exibição e conclusão de assinaturas
    - `Média` · João Rodrigo · PM Paulo Afonso · Squad 3
- [ ] **SGV-5970** — Documento impresso não exibe selo de todas as assinaturas realizadas em paralelo
    - `Média` · Diogo Sobreira · Squad 1
- [ ] **SGV-3786** — Exibição de erro 500 ao solicitar assinatura em documento sigiloso
    - `Média` · João Rodrigo · V2 · Squad 3
    - ⚠️ Notion mudou de **Em desenvolvimento → Não reproduzido** (22/07)
- [x] **[[QA Workspace/99 Arquivo/Bug Assinatura Despacho Desassociacao|SGV-3413]]** — Erro ao assinar despacho de desassociação de documentos ✅ 2026-07-20 → descartado, não reproduz mais
    - `Média` · João Rodrigo · Squad 3
    - Verificado diretamente por Rafael (20/07) — card criado já como descartado em `99 Arquivo/`, sem material de causa raiz disponível
    - ✅ Notion agora bate com a decisão do vault (mudou de **Backlog → Não reproduzido** em 22/07)

## A fazer / Backlog (2)

- [ ] **[[QA Workspace/02 Demandas/DEV/9977 - Bug Nome Oculto Cópia Despacho|SGV-9977]]** — Nome do envolvido em cópia fica oculto no componente do despacho após emissão
    - `Baixa` · sem dev
    - ⚠️ Divergência: vault tem card **aberto em DEV**; Notion ainda diz Backlog
- [ ] **[[QA Workspace/02 Demandas/HML/9971 - Bug Assinatura Servidor Não Aprovado|SGV-9971]]** — Está sendo possível solicitar assinatura para servidor com cadastro "A aprovar"
    - `Baixa` · sem dev
    - ⚠️ Divergência: vault tem card **em validação em HML**; Notion ainda diz Backlog

## Aprovado no Dev (1) — segue pra HML

- [x] **[[QA Workspace/02 Demandas/HML/3412 - Bug Marcação Automática Checkbox Lista Solicitações Assinaturas|SGV-3412]]** — Marcação automática incorreta de checkbox na Lista de Solicitações de Assinaturas ✅ 2026-07-22 → **aprovada em DEV**, card criado em `02 Demandas/HML/` (segue pra validação em HML)
    - `Média` · João Rodrigo · Squad 3
    - ✅ Notion agora bate com a decisão do vault (mudou de **Backlog → [QA] Aprovado no Dev** em 22/07)

## Em produção / Aprovado / Concluído (11) — conferir encerramento

- [x] **[[QA Workspace/02 Demandas/Concluídas/5273 - Bug Login Senha Correta Apos Tentativas|SGV-5273]]** — Login com senha correta não funciona após tentativas incorretas ✅ 2026-07-20 → **aprovada em homologação**, card em Concluídas
    - `Altíssima` · Matheus Godoi
    - [MR !419](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/419) revisado (SKILL_REVISAO_ESCOPO_MR) — fix inverte a ordem senha↔tentativas, sem teste automatizado; card nasceu em `02 Demandas/HML/` (status real do Notion) e foi aprovado no mesmo dia — CT-B04 (Produção) segue em aberto como follow-up
    - ✅ Notion agora bate com o vault (mudou de **Disponível para homologação → Aprovado por QA** em 22/07)
- [x] **[[QA Workspace/02 Demandas/Concluídas/6975 - Bug Erro 503 Ativar Cliente Em Implantação|SGV-6975]]** — Erro 503 ao ativar clientes com status "Em implantação" ✅ 2026-07-21 → **aprovada em homologação**, card em Concluídas
    - `Média` · Matheus Godoi · Sanidade-006
    - ✅ Notion agora bate com o vault (mudou de **Disponível para homologação → Aprovado por QA** em 22/07)
- [ ] **[[QA Workspace/02 Demandas/Concluídas/10123 - Bug Retrocesso Etapa Após Atalho|SGV-10123]]** — Cluster de setor responsável não aparece ao retroceder etapa avançada por atalho
    - `Média` · Marcos Vinicius
    - Vault: concluído ✓ (Notion: Aprovado por QA)
- [ ] **SGV-10231** — Botão "Gerar documento" aparece após os demais botões da toolbar no módulo Análise de Projetos
    - `Altíssima` · Diogo Sobreira · CX · 🆕 card novo neste export (22/07) · Notion: Em produção
- [ ] **SGV-10193** — Botão "Gerar Documento" não é exibido em Memorandos e Processos Administrativos
    - `Alta` · Diogo Sobreira · CX · 🆕 card novo neste export (22/07) · Notion: Em produção
- [ ] **[[QA Workspace/02 Demandas/Concluídas/9237 - Bug Download Tramitação Interna|SGV-9237]]** — Download realizado por cidadão inclui conteúdo de tramitação interna
    - `Alta` · Bruno Clementino
    - Vault: concluído ✓
- [ ] **SGV-8385** — Definição de caminhos alternativos no fluxo de trabalho (etapas não obrigatórias)
    - `Alta` · Marcos Vinicius · Melhoria · CX
- [ ] **SGV-9112** — Implementar o avanço até uma etapa específica a partir do split-button (parte 2)
    - Marcos Vinicius · Tarefa
    - Retestada e aprovada em homologação em 16/07
- [ ] **SGV-10166** — Servidores não conseguem acessar os memorandos após ativação/desativação do novo módulo - PM Guarabira
    - `Média` · João Marcelo · CX · Squad 3 · 🆕 card novo neste export (22/07) · Notion: Em produção
- [ ] **SGV-10143** — Anexos de documento associado não são exibidos para setores envolvidos no documento principal
    - `Média` · João Marcelo · CX · Squad 3 · deadline 15/08 · 🆕 card novo neste export (22/07) · Notion: Em produção
- [ ] **SGV-10075** — Problemas na visualização de conteúdo em processo em tramitação para Cidadão
    - `Média` · João Marcelo · CX · Squad 3 · Notion: Concluído

## Fora do export atual (11) — preservados, saíram do corte de 22/07

> [!note]- Estavam na triagem antiga mas não vieram neste export
> O export de 22/07 cortou em 53 (de 75). Estes 11 cards não apareceram no corte — **provavelmente por causa do "Load more", não porque saíram da sprint**. Trabalho do vault preservado; reconferir no próximo export completo. Não apagados.

- [x] **[[QA Workspace/02 Demandas/HML/9610 - Bug Associar Documento Abertura Multi-Setor|SGV-9610]]** — Servidor não consegue associar documento na abertura de um novo documento ✅ 2026-07-17 → refinado, critérios de aceite no card, análise no Notion, mesa arquivada em 04 Conhecimento
    - `Baixa` · João Rodrigo · CX · era **Pronto pra teste em dev**
    - **Aprovada em DEV (23/07)** — 6 CTs e 5 critérios atendidos, gate de doc ok (Associar/Desassociar respalda); card movido pra `02 Demandas/HML/`, segue pra homologação.
- [x] **[[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]]** — Modelos automatizados perdem a referência dos campos dinâmicos (@) após alteração do módulo ✅ 2026-07-17 → já refinado, critérios no card
    - `Baixa` · Diogo Sobreira · CX · era **Revisar MR**
    - Card no vault com critérios prontos (esteira 3f)
- [x] **[[QA Workspace/02 Demandas/DEV/8977 - Bug Timeout Edicao Regras Organograma|SGV-8977]]** — Erro ao tentar editar regras de tramitação direto no organograma ✅ 2026-07-20 → refinado, card criado
    - `Baixa` · Washington Junior · CX · API · era **Revisar MR**
    - [MR !505](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/505) revisado a nível de escopo em 2026-07-20 (mesmo padrão N+1→lote da SGV-9692, aplicado ao Organograma) — card criado com critérios reescritos (timeout entregue foi 10s, não os 30s pedidos); falta validação real de volume
- [ ] **SGV-9692** — SGA: lentidão ao salvar configurações de tramitação na criação de setores
    - `Baixa` · Diogo Sobreira · CX · era **Revisar MR**
    - [MR !573](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/573) revisado a nível de escopo em 2026-07-20 (troca de chamada individual por lote — bate com a lentidão; testes cobrem a regra de negócio, não performance) — ainda não batido/decidido
    - ⚠️ Caso de lentidão — verificar situação; tem relação com a SGV-8977?
- [ ] **SGV-9548** — Campo de telefone no cadastro de instância não permite número fixo
    - `Baixa` · Matheus Godoi · era **Pronto pra teste em dev**
- [ ] **SGV-9808** — Documento, mesmo assinado, continua com status de "assinatura pendente"
    - `Baixa` · João Marcelo · CX · relacionado: 9809, 9870, 9842 · era **Disponível para homologação**
- [x] **[[QA Workspace/02 Demandas/Concluídas/8380 - Bug Referencia Resposta Despacho Cadeia Respostas|SGV-8380]]** — Referência de resposta em despachos exibida incorretamente na cadeia de respostas ✅ 2026-07-22 → aprovada em HML
    - `Baixa` · Diogo Sobreira · era **Disponível para homologação**
- [ ] **SGV-8395** — Comentários do evento de abertura não são incluídos ao baixar pelo download personalizado
    - `Baixa` · Matheus Godoi · era **Backlog**
- [ ] **SGV-9430** — Ajustes de responsividade no modal de posicionamento de assinaturas
    - Lucas Cabral · LEGADO · era **Impedimento**
- [ ] **SGV-5548** — Aprimorar posicionamento da assinatura em documentos
    - `Alta` · Lucas Cabral · Melhoria · CX · era **Produção**
- [ ] **SGV-9474** — Diferença entre tela de rastrear documentos em prod e o Figma
    - `Baixa` · B. Luan · era **Produção**

---

## Registro da triagem

- 2026-07-17 - Lista criada a partir do export da view SP15 (53/60 cards — 7 faltando por corte do "Load more")
- 2026-07-17 - Reformatada pra leitura: linha do checkbox só com ID + título; prioridade/dev/origem na sublinha
- 2026-07-17 - Primeira batida (10/53): 9458, 9093, 9633, 5783, 7829, 6873 → já possuem critérios; 9750, 9963, 8977, 9036 → já refinados, critérios no card. Investigações abertas: 6348 (mesmo caso da 6873?), 9692 (relação com 8977?), 7074 (critérios com Lucas Beninca)
- 2026-07-17 - Correção: SGV-9474 tinha ficado de fora da lista na montagem (erro de transcrição) — incluído em Em produção; grupo agora com 7
- 2026-07-17 - Segunda batida (12/53): **9610** → refinado de ponta a ponta (card no vault com CTs, análise no Notion, mesa arquivada em 04 Conhecimento); **7074** → critérios sendo construídos com Lucas Beninca. Painel de progresso adicionado no topo (contador geral + por grupo)
- 2026-07-22 - Batida (16/53): **3412** (Backlog) → aprovada em DEV, card criado em modo enxuto em `02 Demandas/HML/` (segue pra validação em HML). Backlog 1→2/7
- 2026-07-22 - Batida (17/64): **8380** (Fora do export atual) → aprovada em HML, card criado em modo enxuto em `02 Demandas/Concluídas/`. Fora do export 3→4/11
- 2026-07-22 - **Reconciliação com novo export (22/07 13:25)**. Export ainda incompleto: 53 cards, mas Notion agora diz Count 75 (antes ~60). **11 cards novos** entraram: 10246, 10231, 10193, 10166, 10143 (produção/revisar/dev), 7935, 7337, 6427, 6136, 6094, 8129. **20 mudanças de status** aplicadas (Notion → grupo da triagem), preservando marcações e decisões do vault: 9458/9093/5783/6873/6348 (Revisar MR→Teste dev), 9036 (Em dev→Revisar MR), 6568 (Impedimento→Revisar MR), 5245 (Backlog→Revisar MR), 5360 (Backlog→Em dev), 8870 (Não reproduzido→Homologação), 3820 (Homologação→Testando HML), 9772 (Em dev→Aguardando CX), 7829 (Revisar MR→Impedimento), 9959 (Teste dev→Homologação), 9750 (Revisar MR→Homologação), 3786 (Em dev→Não reproduzido), 3413 (Backlog→Não reproduzido, bate com descarte do vault), 3412 (Backlog→[QA] Aprovado no Dev, bate com o vault), 5273/6975 (Homologação→Aprovado por QA, batem com o vault). **11 cards saíram do corte** (9610, 9963, 8977, 9692, 9548, 9808, 8380, 8395, 9430, 5548, 9474) → movidos pra seção "Fora do export atual", trabalho preservado (não apagados). Contadores recontados por grupo.
- 2026-07-23 - Batida (18/64): **9959** (Disponível para homologação) → aprovada por QA em homologação, card criado em modo enxuto em `02 Demandas/Concluídas/`. (No mesmo dia, a **9750** — já com card — foi aprovada em HML e movida pra Concluídas.)
- 2026-07-23 - **Consolidação 9633/3820/8574** (decisão de triagem validada com o time): as três são o mesmo problema (assinatura em fluxo de trabalho não pode ser concluída) → **todas tratadas na SGV-9633**. **9633** = master, marcada como **Pronto pra dev** (Revisar MR); **3820** (Testando HML, já havia sido reaberta antes) e **8574** marcadas `[x]` como **duplicadas de 9633**. 8574 não estava neste corte do export — adicionada no grupo Revisar MR (junto da master) só pra registrar a decisão; conferir no próximo export completo. Nenhum dos três tem card em `02 Demandas/` — decisão registrada só na triagem (não criar card do zero). Contadores: Homologação 1→2, Testando HML 0→1, Revisar MR 2/7→3/8 (8574 somada ao grupo). Progresso 18/64 → 20/65.
