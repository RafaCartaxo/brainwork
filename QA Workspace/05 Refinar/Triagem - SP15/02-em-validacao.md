---
tags:
  - qa
  - triagem
sprint: SP15
estagio: em-validacao
---
# 02 — Em validação

Cards com QA ativa — CTs sendo executados, validação em curso (DEV ou HML). Card local existe em `02 Demandas/`.

---

- [x] **SGV-7829** — Anexos do despacho não são carregados corretamente ao emitir e assinar como Cidadão ✅ 2026-07-17 → já possui critérios; 🔴 reaberta em HML (24/07): PDF ok, imagem não
    - `Média` · João Marcelo · Squad 3
    - Card em `02 Demandas/HML/`. Rafael optou por não bloquear publicação; card reaberto pra imagem numa próxima iteração
- [ ] **SGV-6906** — Não é possível assinar documento em instância Em Implantação
    - `Média` · Lucas Lacerda · Sanidade-005
    - 🔴 Reaberta em HML (22/07): bug original resolvido (assinatura OK), mas documentos de teste escapam da limpeza. Card em `02 Demandas/HML/`, aguardando dev
- [x] **SGV-5360** — Assinatura de despacho customizado não aparece na tela de "Assinaturas pendentes" do servidor ✅ 2026-07-24 → aprovada em DEV, card em `02 Demandas/HML/`, segue pra homologação
    - `Média` · João Marcelo · Squad 3
- [x] **SGV-6083** — Edição de documento não atualiza o conteúdo na assinatura ou download ✅ 2026-07-24 → aprovada em HML (reabriu na 1ª validação; fix da 6873 mergeado, reaprovou). Card em Concluídas
    - `Média` · Matheus Godoi
    - 🧭 Raiz comum com 6873 e 6348
- [x] **SGV-6348** — Edição de documentos "Em elaboração" não é exibida ao baixar documento ✅ 2026-07-24 → resolvida por decisão de QA (sintoma coberto pela correção comum). Card em Concluídas
    - `Média` · Matheus Godoi · Squad 2
