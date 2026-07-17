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

## Disponível para homologação (9) — ação QA imediata

- [ ] **SGV-5273** — Login com senha correta não funciona após tentativas incorretas
    - `Altíssima` · Matheus Godoi
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
- [ ] **SGV-7074** — Ao alterar módulo de um assunto/serviço os modelos de documentos não são atualizados
    - `Altíssima` · Matheus Godoi
    - ⚠️ Parente do [[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]]? (mais ou menos, é outra coisa) Lucas Beninca construindo os criterios
- [ ] **SGV-9610** — Servidor não consegue associar documento na abertura de um novo documento
    - `Baixa` · João Rodrigo · CX
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
- [x] **SGV-5783** — Representante legal incorreto na assinatura após fazer alteração ✅ 2026-07-17 (já possui critérios)
    - `Alta` · Diogo Sobreira
- [x] **[[QA Workspace/02 Demandas/DEV/9750 - Bug Assinatura Pendente Documento Encerrado|SGV-9750]]** — Pedido de assinatura permanece pendente mesmo com documento sendo encerrado ✅ 2026-07-17 (já refinado e possui critérios)
    - `Média` · Washington Junior · CX · API
    - Card no vault com critérios prontos; pendência de revisar cenários já na fila
- [x] **SGV-7829** — Anexos do despacho não são carregados corretamente ao emitir e assinar como Cidadão ✅ 2026-07-17(já possui critérios)
    - `Média` · João Marcelo
- [ ] **SGV-6873** — Download de documento temporário não corresponde à versão editada
    - `Média` · Matheus Godoi · Sanidade-004
- [ ] **SGV-6348** — Edição de documentos "Em elaboração" não é exibida ao baixar documento
    - `Média` · Matheus Godoi
- [ ] **[[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]]** — Modelos automatizados perdem a referência dos campos dinâmicos (@) após alteração do módulo
    - `Baixa` · Diogo Sobreira · CX
    - Card no vault com critérios prontos (esteira 3f)
- [ ] **SGV-9692** — SGA: lentidão ao salvar configurações de tramitação na criação de setores
    - `Baixa` · Diogo Sobreira · CX
- [ ] **SGV-8977** — Erro ao tentar editar regras de tramitação direto no organograma
    - `Baixa` · Washington Junior · CX · API

## Em desenvolvimento / Em andamento (4)

- [ ] **SGV-9036** — Mensagens de erro são exibidas quando é selecionado um signatário para assinatura
    - `Altíssima` · Washington Junior · API
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
- [ ] **SGV-3413** — Erro ao assinar despacho de desassociação de documentos
    - `Média` · Squad 3
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

## Em produção / Aprovado / Concluído (6) — conferir encerramento

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

---

## Registro da triagem

- 2026-07-17 - Lista criada a partir do export da view SP15 (53/60 cards — 7 faltando por corte do "Load more")
- 2026-07-17 - Reformatada pra leitura: linha do checkbox só com ID + título; prioridade/dev/origem na sublinha
