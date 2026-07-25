---
tags:
  - qa
  - triagem
sprint: SP15
estagio: acao-imediata
---
# 01 — Ação imediata

Cards testáveis agora — fix está no ambiente (ou assumido recém-deployado em DEV). Ordenado: HML primeiro, depois DEV.

## 🔴 Validar em homologação

- [ ] **SGV-8870** — Toggle de abertura externa está setado na criação de Assunto e Serviço
    - `Altíssima` · Lucas Lacerda · Squad 2
    - ⚠️ Notion mudou de Não reproduzido → Disponível para homologação (22/07)
- [x] **SGV-9458** — Nome do destinatário exibido como "Anônimo" ao responder despacho de cidadão PJ ✅ 2026-07-17 → já possui critérios
    - `Altíssima` · Matheus Godoi
    - ⚠️ Avançou: Pronto pra teste em dev → Disponível para homologação (Release, 24/07)
- [x] **SGV-7074** — Ao alterar módulo de um assunto/serviço os modelos de documentos não são atualizados ✅ 2026-07-17
    - `Altíssima` · Matheus Godoi
    - ✅ Critérios prontos (Lucas Beninca). Avançou → Disponível para homologação (Release, 24/07)
- [x] **SGV-3412** — Marcação automática incorreta de checkbox na Lista de Solicitações de Assinaturas ✅ 2026-07-22 → aprovada em DEV, card criado em `02 Demandas/HML/`, segue pra HML
    - `Média` · João Rodrigo · Squad 3
- [ ] **SGV-10268** — Ajuste no fluxo de solicitação de revisão para eliminar cenário duplicado
    - `Baixa` · Lucas Lacerda · 🆕 novo (Release, 24/07)
- [ ] **SGV-8386** — Ordenação Z–A de clientes com ícone invertido e exibição incorreta da lista
    - `—` · Lucas Lacerda · 🆕 novo (Release, 24/07)
- [ ] **SGV-9548** — Campo de telefone no cadastro de instância não permite número fixo
    - `Baixa` · Matheus Godoi
    - ✅ Avançou: Pronto pra teste em dev → Disponível para homologação (Release, 24/07)

## 🟡 Validar em DEV

- [x] **SGV-9093** — Nome do solicitante exibido no evento de criação em solicitação sigilosa do cidadão ✅ 2026-07-17 → já possui critérios
    - `Altíssima` · Matheus Godoi · Squad 2
    - ⚠️ Notion: Revisar MR → Pronto pra teste em dev (22/07)
- [x] **SGV-5783** — Representante legal incorreto na assinatura após fazer alteração ✅ 2026-07-17 → já possui critérios
    - `Alta` · Diogo Sobreira · Squad 1
    - [MR !581](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/581) revisado a nível de escopo (20/07) — falta validação manual do fluxo de reemissão de certificado
    - ⚠️ Notion: Revisar MR → Pronto pra teste em dev (22/07)
- [ ] **SGV-5103** — Mensagem de erro exibida ao alternar para prefeitura na qual o servidor está de férias, apesar do funcionamento normal
    - `Alta` · Matheus Godoi · 🆕 novo (Release, 24/07)
- [x] **SGV-9963** — Modelos automatizados perdem a referência dos campos dinâmicos (@) após alteração do módulo ✅ 2026-07-17 → refinado, critérios no card
    - `Baixa` · Diogo Sobreira · CX
    - ✅ Fix chegou em HML! (Release, 24/07) — destrava pendência "aguardando disponibilização"
- [ ] **SGV-6427** — Possibilidade de um documento virar selo e aplicação num anexo PDF
    - `Alta` · Gabriel Alves (designer) · Funcionalidade · 🆕 (22/07)
- [ ] **SGV-8129** — Estado de hover ao arrastar selo não segue protótipo
    - `Baixa` · Lucas Lacerda · Squad 2 · 🆕 (22/07)
- [ ] **SGV-6136** — [SOGOV+PM Conde] Divergência de logo e título na visualização do processo
    - `Média` · Matheus Godoi · Squad 2 · 🆕 (22/07)
