---
tags:
  - qa
  - conhecimento
tipo: indice
---
# Índice: API e-SIC — Melhorias nos dados disponibilizados (SGV-9657)

Task guarda-chuva do Notion ("[Melhoria-dev] API esic - Melhorias nos dados que são disponibilizados na API Adicionar ID para solicitante e ajustes na estrutura do json") que agrupa as duas partes da melhoria. Sem card/CTs próprios — a validação acontece pelas partes.

> [!info] Epic aberta — Parte 1 em teste (HML), Parte 2 com pacote criado (DEV)
> Esta pasta vive em `HML/` (não em `Concluídas/`) enquanto a epic como um todo não fechar. **Parte 1 (SGV-10736)** em teste direto em homologação — fluxo 3f (API, sem esteira DEV), ver [[../../../../Sistema/Contexto/PADROES_QA#Tasks de API (fluxo 3f)|PADROES_QA#Tasks de API]]; 1 Bug aberto. **Parte 2 (SGV-10735)** destravou (backend de credenciais já com MR aprovado) — pacote criado em 05/10/2026, execução aguardando ambiente de teste/dev disponível. Regra: só mover esta pasta-índice pra `Concluídas/` quando as duas partes fecharem o ciclo completo.
>
> **Estrutura:** as partes vivem fisicamente dentro desta pasta da epic (`SGV-9657 - .../SGV-<n> - <título>/`), junto com `Conhecimento/`. Cada parte mantém seu próprio status/ciclo de vida no frontmatter (`ambiente:`/`status:`) — o card de cada uma não se move de pasta ao fechar. A Dashboard lê o campo `ambiente:` do frontmatter antes do nome da pasta, então esse aninhamento não esconde os cards sem responsável.

## Partes

| Parte | SGV | O que é | Status |
|---|---|---|---|
| 1 | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/01 - Demanda\|SGV-10736]] | Normalização das informações retornadas pela API — ID do solicitante, tipo PF/PJ, data de nascimento e gênero do solicitante, data de abertura/vencimento com cálculo de prazo | Testando em homologação (fluxo 3f — API), 1 Bug aberto |
| 2 | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda\|SGV-10735]] | Criação da feature de integrações — tela onde o time interno ativa a API e-SIC por cliente, gera credenciais, seleciona módulos expostos e consulta histórico de alterações | Pacote criado, aguardando ambiente de teste/dev pra iniciar execução |

## Dependência entre as partes

Nenhuma dependência funcional direta: a Parte 1 normaliza o JSON já retornado pela API existente; a Parte 2 cria a tela de ativação/gestão da integração sobre essa mesma API. Podem ser testadas de forma independente.

## Ordem de leitura sugerida

Card de cada parte (`00 QA/00 README` → `01 - Demanda`, critérios + CTs) → `04 - Validação dev` (execução) → `05 - Preparação Qase` (envio).

## Contexto de apoio (não é fonte de critério de aceite)

A documentação oficial "Gerenciamento de clientes SOGOV" no Notion cobre a seção "Integrações — API e-SIC" com o desenho funcional completo (ativação, credenciais, módulos, desativação, histórico) — base dos critérios de aceite da Parte 2. Os critérios de aceite da Parte 1 vêm da descrição da própria SGV-9657/SGV-10736 e dos retornos esperados (novos) em JSON.
