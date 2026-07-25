---
tags:
  - qa
  - triagem
sprint: SP15
estagio: aguardando-deploy
---
# 03 — Aguardando deploy

Cards aprovados em um ambiente, aguardando o fix subir no próximo (DEV→HML ou HML→release). Não testar ainda — o ambiente não tem o fix.

---

## Aguardando subir pra HML

> Aprovado em DEV, fix ainda não deployado em homologação.

- [x] **SGV-9610** — Servidor não consegue associar documento na abertura de um novo documento ✅ 2026-07-17 → refinado, card em `02 Demandas/HML/`, aprovada em DEV (23/07)
    - `Baixa` · João Rodrigo · CX
    - ⏳ Aguardando MR !537 chegar em HML. Gate 2 da automação pendente.

## Aguardando release (produção)

> Aprovado em HML, aguardando janela de release.

- [x] **SGV-9959** — Inconsistência de status entre drawer de solicitação e evento de assinatura após recusa ✅ 2026-07-23 → aprovada em HML, card em Concluídas
    - `Média` · João Marcelo · Squad 3
- [x] **SGV-9750** — Pedido de assinatura permanece pendente mesmo com documento encerrado ✅ 2026-07-17 → refinado; aprovada em homologação (23/07), card em Concluídas
    - `Média` · Washington Junior · CX · API · Squad 1
- [x] **SGV-10246** — Erro ao emitir e assinar despacho como cidadão ✅ 2026-07-24 → aprovada em HML (1ª reprovada 23/07, corrigida e aprovada). Card em Concluídas
    - `Altíssima` · João Marcelo · Squad 3
- [x] **SGV-5269** — Botão de recuperar senha não redireciona para o fluxo de esqueci senha ✅ 2026-07-24 → aprovada em HML, card em Concluídas
    - `Altíssima` · Matheus Godoi
- [x] **SGV-6873** — Download de documento temporário não corresponde à versão editada ✅ resolvida por herança (fix mergeado em 6083). Card em Concluídas
    - `Média` · Matheus Godoi · Squad 2
