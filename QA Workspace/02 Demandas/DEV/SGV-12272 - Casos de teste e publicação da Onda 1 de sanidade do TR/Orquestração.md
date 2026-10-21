---
demanda: SGV-12272
titulo: Casos de teste e publicação da Onda 1 de sanidade do TR
etapa: DEV
estado: travada            # em andamento | travada | concluída
atualizado_em: 2026-10-21T08:40:00-03:00
atualizado_por: coordenacao
frentes:
  - frente: tr
    orquestrador: tr-orquestrador
    executor: tr-executor
    estado: em andamento
  - frente: automacao
    orquestrador: automacao-orquestrador
    executor: automacao-executor
    estado: em andamento
aguarda_voce:
  - o_que: Validar os 20 CTs em DEV (vídeo e capturas para a automação)
    desde: 2026-10-20T14:30:00-03:00
    efeito: TR (sync Qase) e Automação (Plano e código) não avançam
    abrir: coordenacao
  - o_que: Confirmar massa de dados dev dos CT-004, 006, 007/008, 009, 010, 017 e 018
    desde: 2026-10-20T14:30:00-03:00
    efeito: Validação manual e Análise da automação
    abrir: coordenacao
  - o_que: Definir pontos da validação (04) e indicar qase_suite_id (05)
    desde: 2026-10-20T14:30:00-03:00
    efeito: Fechamento do pacote TR e sync Qase
    abrir: tr-orquestrador
  - o_que: Decisões da automação (CT-013 manual, ambiente da Onda 1, SEED_SCHEMA_VERSION, itens a conferir no homolog)
    desde: 2026-10-20T14:30:00-03:00
    efeito: Gate da Análise de automação
    abrir: automacao-orquestrador
dependencias:
  - frente: tr
    espera: automacao
    motivo: Linha do CT-019 na tabela de capturas do 04 (permissão extra de configuração de instância)
---

<!--
Ficha da demanda. Coordenação mantém identificação, pendências e decisões;
cada orquestrador atualiza o bloco da sua frente. O painel lê só o frontmatter.
-->

## Decisões já tomadas

- 20/10: critérios de aceite C1–C20 (um por CT) e C21–C24 de processo; publicados no Notion (Backlog).
- 20/10: CT-002 fica como está; o erro é do produto (bug SGV-12316 aberto). O passo "senha correta com conta bloqueada" não volta ao CT.
- 20/10: CT-019 cria uma 3ª instância na automação; no CT, positivo = administrador geral, negativo = Servidor sem administrador geral e sem a permissão extra de configuração de instância.
- 20/10: todos os CTs terão API e E2E na automação. Nada roda sem ordem do Rafael.
- 20/10: página "Modelo de demanda" do Notion já estava apagada.

## Bloco TR (tr-orquestrador)

_A preencher pelo orquestrador: estado, última entrega, próximo passo._

## Bloco Automação (automacao-orquestrador)

_A preencher pelo orquestrador: estado, última entrega, próximo passo._

## Notas

- Pacote QA: pasta `00 QA/`. Pacote de automação: pasta `01 Automação/`.
- A automação é frente paralela; a SGV-12272 em si é só CTs e publicação.
