---
tags:
  - qa
  - triagem
sprint: SP15
estagio: acompanhamento
---
# 06 — Acompanhamento

Cards sem ação pendente de Rafael: em produção, aprovados por outro QA, decididos (descartados/duplicados), ou órfãos do export. Observar, sem ação.

---

## Em produção / Concluído

- [x] **SGV-5273** — Login com senha correta não funciona após tentativas incorretas ✅ 2026-07-20 → aprovada em HML, card em Concluídas
    - `Altíssima` · Matheus Godoi
- [x] **SGV-6975** — Erro 503 ao ativar clientes com status "Em implantação" ✅ 2026-07-21 → aprovada em HML, card em Concluídas
    - `Média` · Matheus Godoi · Sanidade-006
- [ ] **SGV-10123** — Cluster de setor responsável não aparece ao retroceder etapa avançada por atalho
    - `Média` · Marcos Vinicius · Vault: concluído ✓ (Notion: Aprovado por QA)
- [ ] **SGV-10231** — Botão "Gerar documento" aparece após os demais botões da toolbar no módulo Análise de Projetos
    - `Altíssima` · Diogo Sobreira · CX · 🆕 (22/07) · Notion: Em produção
- [ ] **SGV-10193** — Botão "Gerar Documento" não é exibido em Memorandos e Processos Administrativos
    - `Alta` · Diogo Sobreira · CX · 🆕 (22/07) · Notion: Em produção
- [ ] **SGV-9237** — Download realizado por cidadão inclui conteúdo de tramitação interna
    - `Alta` · Bruno Clementino · Vault: concluído ✓
- [x] **SGV-8385** — Definição de caminhos alternativos no fluxo de trabalho ✅ 2026-07-24 → confirmado Em produção
    - `Alta` · Marcos Vinicius · Melhoria · CX
- [ ] **SGV-9112** — Implementar o avanço até uma etapa específica a partir do split-button (parte 2)
    - Marcos Vinicius · Tarefa · Retestada e aprovada em HML em 16/07
- [ ] **SGV-10166** — Servidores não conseguem acessar os memorandos após ativação/desativação do novo módulo
    - `Média` · João Marcelo · CX · Squad 3 · 🆕 (22/07) · Notion: Em produção
- [ ] **SGV-10143** — Anexos de documento associado não são exibidos para setores envolvidos no documento principal
    - `Média` · João Marcelo · CX · Squad 3 · 🆕 (22/07) · Notion: Em produção
- [ ] **SGV-10075** — Problemas na visualização de conteúdo em processo em tramitação para Cidadão
    - `Média` · João Marcelo · CX · Squad 3 · Notion: Concluído

## Aprovado por outro QA (sem card local)

> Validação feita por outro QA do time. Rafael não testou, não tem card. Registrado pra visibilidade da sprint.

- [x] **SGV-7640** — Campo de busca de setor destinatário fica inutilizável após seleção inicial ✅ 2026-07-24 → Aprovado por QA no Notion
    - `Alta` · Matheus Godoi · CX
- [x] **SGV-4995** — Contagem de dias incorreta ao configurar prazos ✅ 2026-07-24 → Aprovado por QA
    - `Alta` · Matheus Godoi
- [x] **SGV-9690** — SGA: filtro de busca não localiza palavras com variações de caracteres especiais ✅ 2026-07-24 → Aprovado por QA
    - `Média` · Lucas Cabral · CX
- [x] **SGV-9808** — Documento, mesmo assinado, continua com status de "assinatura pendente" ✅ 2026-07-24 → Aprovado por QA
    - `Baixa` · João Marcelo · CX
- [x] **SGV-9961** — Lentidão no carregamento dos documentos da mesa de trabalho ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Alta` · Gabriel Desidério
- [x] **SGV-9953** — Busca por setores que não participo trava o seletor de setores ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Média` · João Rodrigo
- [x] **SGV-9886** — Número de documentos em abertos não é igual ao exibido na tela inicial ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `—` · B. Luan
- [x] **SGV-9693** — SGA - Filtro de busca das regras de tramitação também pesquisar pela sigla dos setores ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Baixíssima` · Melhoria · Marcos Vinicius
- [x] **SGV-9386** — Pendência de assinatura permanece ativa após cancelamento do processo ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Baixíssima` · João Rodrigo
- [x] **SGV-7168** — Alterar copy que descreve ação de documentos com solicitação de revisão configurada ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Média` · Melhoria · Lucas Lacerda
- [x] **SGV-7162** — PM Nísia - Erro ao alterar setor do usuário ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Baixa` · Diogo Sobreira
- [x] **SGV-6198** — Prazo do despacho não é exibido na tela do servidor destinatário ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Alta` · Matheus Godoi
- [x] **SGV-5430** — Visualização de anexo está sendo contabilizada como download ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Média` · Matheus Godoi
- [x] **SGV-5242** — Setor criador incorreto no histórico da versão inicial do documento ✅ 2026-07-24 (Release) → Aprovado por QA 🆕
    - `Baixa` · Diogo Sobreira

## Backlog (sem ação)

- [ ] **SGV-9977** — Nome do envolvido em cópia fica oculto no componente do despacho após emissão
    - `Baixa` · sem dev
    - ⚠️ Divergência: vault tem card aberto em DEV; Notion diz Backlog
- [ ] **SGV-9971** — Está sendo possível solicitar assinatura para servidor com cadastro "A aprovar"
    - `Baixa` · sem dev
    - ⚠️ Divergência: vault tem card em validação em HML; Notion diz Backlog

## Decididos / descartados / duplicados

> Já tiveram decisão. Nada pendente.

- [x] **SGV-3820** — Duplicada de SGV-9633 ✅ 2026-07-23
- [x] **SGV-8574** — Duplicada de SGV-9633 ✅ 2026-07-23
- [x] **SGV-3413** — Descartado, não reproduz mais ✅ 2026-07-20

## Órfãos do export (saíram do corte de 22/07)

> Estavam na triagem antiga, não vieram no último export. Preservados, não apagados. Reconferir no próximo export completo.

- [ ] **SGV-8395** — Comentários do evento de abertura não são incluídos ao baixar pelo download personalizado
    - `Baixa` · Matheus Godoi · era Backlog
- [ ] **SGV-9430** — Ajustes de responsividade no modal de posicionamento de assinaturas
    - Lucas Cabral · LEGADO · era Impedimento
- [ ] **SGV-5548** — Aprimorar posicionamento da assinatura em documentos
    - `Alta` · Lucas Cabral · Melhoria · CX · era Produção
- [ ] **SGV-9474** — Diferença entre tela de rastrear documentos em prod e o Figma
    - `Baixa` · B. Luan · era Produção

## Concluídos com card (Rafael)

> Já aprovados, card em Concluídas. Registro encerrado.

- [x] **SGV-9959** — Inconsistência status drawer ✅ 2026-07-23
- [x] **SGV-9750** — Assinatura pendente documento encerrado ✅ 2026-07-23
- [x] **SGV-8380** — Referência resposta despacho ✅ 2026-07-22
    - `Baixa` · Diogo Sobreira
- [x] **SGV-9464** — Filtros não reiniciados Novo Rastreio ✅ (Release, 24/07)
    - `Baixíssima` · João Marcelo
- [x] **SGV-7371** — URL validação assinatura não expor código ✅ (Release, 24/07)
    - `Altíssima` · Melhoria · B. Luan
- [x] **SGV-7631** — Filtro de solicitações de assinaturas enviadas por mim ✅ 2026-07-24 (Release) → Em produção 🆕
    - `Altíssima` · Melhoria · Gabriel Desidério
