---
tags:
  - qa
  - conhecimento
tipo: indice
---
# Índice: Departamentos de cidadão PJ (SGV-9296)

Task guarda-chuva do Notion que agrupa as quatro partes da funcionalidade de departamentos vinculados a cidadãos Pessoa Jurídica. Sem card/CTs próprios — a validação acontece pelas partes.

## Partes

| Parte | SGV | O que é | Status |
|---|---|---|---|
| 1 | [[QA Workspace/02 Demandas/Concluídas/11083/QA/11083 - Funcionalidade Departamentos Para Cidadao PJ\|SGV-11083]] | Criação, edição, exclusão, suspensão e gerenciamento de membros do departamento | Refinada, aberta em DEV — 33 CTs, 1 ponto em aberto (contagem de participantes, aguardando Produto) |
| 2 | [[QA Workspace/02 Demandas/Concluídas/11184/QA/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos\|SGV-11184]] | Encaminhar documentos/despachos pro departamento, notificações e rastreabilidade de visualização externa | Refinada, aberta em DEV — 27 CTs, sem pontos em aberto no escopo atual |
| 3 | [[QA Workspace/02 Demandas/DEV/SGV-11176 - Departamentos Convites/01 - Demanda\|SGV-11176]] | Entrada em departamento por link de convite (permanente do departamento ou temporário gerado por servidor) e filtro de solicitações por perfil/departamento | Refinada, aberta em DEV (pacote novo) — 14 CTs, 1 pendência aberta (revogação de convite, não coberta pelo requisito de origem) |
| 4 | [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda\|SGV-11177]] | Tramitação e assinatura direcionadas a um membro específico de departamento, e assinatura pro departamento inteiro; fluxo externo de assinatura por CPF com pré-cadastro | Refinada, aberta em DEV (pacote novo) — 31 CTs, 6 pontos de conferência visual/textual fina no Figma ainda pendentes |

As Partes 3 e 4 confirmam o que o [[QA Workspace/02 Demandas/Concluídas/9296/Conhecimento/Complemento Figma - Departamento Destinatário E Signatário|Complemento Figma]] já tinha antecipado em 03/09/2026 como escopo futuro da epic (seleção de membro como destinatário direto e departamento/membro como signatário) — recebido do Notion como export bruto em 25/09/2026, com SGVs próprios (11176 e 11177) confirmados no mesmo dia.

## Dependência entre as partes

- A Parte 2 (11184) depende funcionalmente da Parte 1 (11083): precisa existir departamento (com participantes e status ativo/suspenso definidos) antes de testar encaminhamento.
- A Parte 3 (11176) depende da Parte 1 (11083): entrada por convite pressupõe que o departamento já existe.
- A Parte 4 (11177) depende das Partes 1 e 3 (11083, 11176): tramitação/assinatura para membro pressupõe que o membro já é participante do departamento (seja por vínculo manual da 11083, seja por convite da 11176).

Recomendado validar a 11083 primeiro; 11176 e 11184 podem seguir em paralelo depois dela; 11177 valida por último, com massa de dados compatível com as anteriores.

## Ordem de leitura sugerida (por parte)

Resumo → card (critérios + CTs) → mesa de refinamento (detalhe técnico), quando existir. As Partes 3 e 4 nasceram já no pacote (`00 README` + `01 - Demanda` + CTs) — sem mesa de refinamento própria, por decisão explícita (requisito já veio completo do Notion).

## Resumos em linguagem simples

- [[QA Workspace/02 Demandas/Concluídas/11083/Conhecimento/1 - SGV-11083 - Resumo|SGV-11083 - Resumo]]
- [[QA Workspace/02 Demandas/Concluídas/11184/Conhecimento/1 - SGV-11184 - Resumo|SGV-11184 - Resumo]]

## Mesas de refinamento

- [[QA Workspace/02 Demandas/Concluídas/11083/Conhecimento/2 - SGV-11083 - Refinamento Departamentos Para Cidadao PJ|SGV-11083 - Refinamento]]
- [[QA Workspace/02 Demandas/Concluídas/11184/Conhecimento/2 - SGV-11184 - Refinamento Departamentos Encaminhar Documentos E Despachos|SGV-11184 - Refinamento]]

## Contexto de apoio (não é fonte de critério de aceite)

Documento de produto consolidado do Notion ("Departamento CNPJ") cobre esta epic **e outras 3 tasks** (SGV-8883, 8884, 9898) numa visão única de produto — usado nas duas mesas só como esclarecimento de detalhe (limites de campo, fluxo de convite, formato de exibição), nunca como origem de critério.

[[QA Workspace/02 Demandas/Concluídas/9296/Conhecimento/Complemento Figma - Departamento Destinatário E Signatário|Complemento Figma — departamento como destinatário e signatário]] (recebido 03/09/2026): parte já incorporada à SGV-11184 (formato de exibição, regras de busca/exibição); os dois pontos antes registrados como "possível escopo futuro" — seleção de membro individual como destinatário direto e departamento como signatário de assinatura — foram confirmados em 25/09/2026 e viraram a SGV-11177 (Parte 4).
