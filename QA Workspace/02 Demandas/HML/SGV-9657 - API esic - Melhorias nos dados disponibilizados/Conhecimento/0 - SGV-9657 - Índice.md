---
tags:
  - qa
  - conhecimento
tipo: indice
---
# Índice: API e-SIC — Melhorias nos dados disponibilizados (SGV-9657)

Task guarda-chuva do Notion ("[Melhoria-dev] API esic - Melhorias nos dados que são disponibilizados na API Adicionar ID para solicitante e ajustes na estrutura do json") que agrupa as duas partes da melhoria. Sem card/CTs próprios — a validação acontece pelas partes.

> [!info] Epic aberta — 1 de 2 partes em teste (HML), 1 impedida
> Esta pasta vive em `HML/` (não em `Concluídas/`) enquanto a epic como um todo não fechar. **Parte 1 (SGV-10736)** já com MR aprovado e em teste direto em homologação — fluxo 3f (API, sem esteira DEV), ver [[../../../../Sistema/Contexto/PADROES_QA#Tasks de API (fluxo 3f)|PADROES_QA#Tasks de API]]. **Parte 2 (SGV-10735)** impedida desde 15/09/2026, aguardando prototipação de UI (Figma) pelo time de UI/UX — sem pacote próprio ainda, fora de escopo nesta rodada de testes. Regra: só mover esta pasta-índice pra `Concluídas/` quando as duas partes fecharem o ciclo completo.
>
> **Estrutura:** as partes vivem fisicamente dentro desta pasta da epic (`SGV-9657 - .../SGV-<n> - <título>/`), junto com `Conhecimento/`. Cada parte mantém seu próprio status/ciclo de vida no frontmatter (`ambiente:`/`status:`) — o card de cada uma não se move de pasta ao fechar. A Dashboard lê o campo `ambiente:` do frontmatter antes do nome da pasta, então esse aninhamento não esconde os cards sem responsável.

## Partes

| Parte | SGV | O que é | Status |
|---|---|---|---|
| 1 | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda\|SGV-10736]] | Normalização das informações retornadas pela API — ID do solicitante, tipo PF/PJ, data de nascimento e gênero do solicitante, data de abertura/vencimento com cálculo de prazo, novo status "Respondido" | Testando em homologação (fluxo 3f — API) |
| 2 | SGV-10735 (sem pacote ainda) | Criação da feature de integrações — tela onde o time interno ativa a API e-SIC por cliente, gera credenciais, seleciona módulos expostos e consulta histórico de alterações | Impedida — aguardando prototipação de UI (desde 15/09/2026) |

## Dependência entre as partes

Nenhuma dependência funcional direta: a Parte 1 normaliza o JSON já retornado pela API existente; a Parte 2 cria a tela de ativação/gestão da integração sobre essa mesma API. Podem ser testadas de forma independente.

## Ordem de leitura sugerida

Card da Parte 1 (`00 QA/00 README` → `01 - Demanda`, critérios + CTs) → `04 - Validação dev` (execução) → `05 - Preparação Qase` (envio). A Parte 2 ganha o mesmo padrão de pacote quando destravar.

## Contexto de apoio (não é fonte de critério de aceite)

A documentação oficial "Gerenciamento de clientes SOGOV" no Notion cobre a seção "Integrações — API e-SIC" com o desenho funcional completo (ativação, credenciais, módulos, desativação, histórico) — referência pra entender o produto como um todo. Os critérios de aceite da Parte 1 vêm da descrição da própria SGV-9657/SGV-10736 e dos retornos esperados (novos) em JSON, não deste documento.
