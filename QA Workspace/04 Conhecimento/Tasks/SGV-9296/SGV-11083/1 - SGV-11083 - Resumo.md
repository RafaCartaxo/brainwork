---
tags:
  - qa
  - conhecimento
---
# Resumo: Departamentos para cidadão Pessoa Jurídica

> Parte 1 da epic [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/0 - SGV-9296 - Índice|SGV-9296]] — irmã da [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184 (Parte 2)]]. Detalhe técnico (RFs, critérios, CTs) fica no [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|card]] e na [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11083/2 - SGV-11083 - Refinamento Departamentos Para Cidadao PJ|mesa de refinamento]]. Esta nota é só o "o que é e por quê".

## O que é

Cria, dentro do cadastro de uma empresa (Pessoa Jurídica), a possibilidade de organizá-la em **departamentos** — um setor, uma área, um "Financeiro", um "Jurídico". Cada departamento tem nome e e-mail próprios, e pode ter participantes: pessoas vinculadas a ele, cada uma com um cargo.

Esta é a Parte 1 — só o **cadastro** (criar, editar, excluir, suspender departamento e seus participantes). Usar o departamento de fato na tramitação de documentos é a Parte 2 ([[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]]).

## Problema / Problemática

Hoje uma pessoa jurídica é só uma entidade única no sistema — sem estrutura interna. Se a prefeitura precisa falar especificamente com o setor Financeiro de uma empresa, não tem como: só existe "a empresa" (genérico) ou "o contato pessoal de alguém de lá" (que muda de função e derruba a comunicação). Departamento é a peça que falta pra representar essa estrutura interna — sem ele, a Parte 2 (encaminhar documento pro setor certo) não tem o que selecionar.

## Resultado esperado da entrega

- Servidor cria um departamento pra uma empresa, com nome e e-mail únicos dentro daquela empresa (o mesmo nome/e-mail pode existir em empresas diferentes, sem conflito).
- Servidor vincula e desvincula participantes ao departamento — sempre pessoas da mesma prefeitura/instância, cada uma com um cargo (ex.: "Gerente Financeiro").
- A listagem de empresas passa a mostrar a razão social e quantas pessoas participam de departamentos daquela empresa; a tela da empresa lista os departamentos que ela tem.
- Um departamento só pode ser **excluído** se estiver vazio (sem participante) e sem nenhum documento em andamento nele — caso contrário, a única opção é **suspender**, e suspender também só é permitido se não houver pendência aberta. Departamento suspenso some das opções pra novos documentos.
- Toda ação relevante (criar, vincular, desvincular, excluir, suspender) avisa por e-mail e fica registrada no histórico da empresa — dá pra saber depois quem fez o quê.

## Ponto em aberto

Quando a mesma pessoa participa de mais de um departamento da mesma empresa, ainda não está definido se a contagem de "quantos participantes" soma cada vínculo separadamente ou conta a pessoa uma vez só. **QA aguarda a definição do Produto** antes de considerar esse comportamento aprovado ou bug — não é pra decidir sozinho na validação.
