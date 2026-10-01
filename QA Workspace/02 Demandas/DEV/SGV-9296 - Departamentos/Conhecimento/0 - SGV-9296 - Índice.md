---
tags:
  - qa
  - conhecimento
tipo: indice
---
# Índice: Departamentos de cidadão PJ (SGV-9296)

Task guarda-chuva do Notion que agrupa as cinco partes da funcionalidade de departamentos vinculados a cidadãos Pessoa Jurídica. Sem card/CTs próprios — a validação acontece pelas partes.

> [!info] Epic aberta — 2 de 5 partes concluídas
> Esta pasta vive em `DEV/` (não em `Concluídas/`) enquanto a epic como um todo não fechar — mesmo com Partes 1 e 2 já concluídas individualmente. Regra: só mover esta pasta-índice pra `Concluídas/` quando a última parte em aberto (hoje: 3, 4 e 5) também estiver concluída.
>
> **Estrutura (01/10/2026):** as 5 Partes vivem fisicamente dentro desta pasta da epic (`SGV-9296 - Departamentos/SGV-<n> - <título>/`), junto com `Conhecimento/`. Cada parte mantém seu próprio status/ciclo de vida no frontmatter (`ambiente:`/`status:`) — o card de cada uma não se move de pasta ao fechar (diferente da convenção normal de `DEV → HML → Concluídas`, que vale pra demandas fora de uma epic). A Dashboard ("Sem dono") lê o campo `ambiente:` do frontmatter antes do nome da pasta, então esse aninhamento não esconde os cards sem responsável.

## Partes

| Parte | SGV | O que é | Status |
|---|---|---|---|
| 1 | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/01 - Demanda\|SGV-11083]] | Criação, edição, exclusão, suspensão e gerenciamento de membros do departamento | Refinada, aberta em DEV — 33 CTs, 1 ponto em aberto (contagem de participantes, aguardando Produto) |
| 2 | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/01 - Demanda\|SGV-11184]] | Encaminhar documentos/despachos pro departamento, notificações e rastreabilidade de visualização externa | Refinada, aberta em DEV — 27 CTs, sem pontos em aberto no escopo atual |
| 3 | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11176 - Departamentos Convites/01 - Demanda\|SGV-11176]] | Entrada em departamento por link de convite (permanente do departamento ou temporário gerado por servidor) e filtro de solicitações por perfil/departamento | Refinada, aberta em DEV (pacote novo) — 14 CTs, 1 pendência aberta (revogação de convite, não coberta pelo requisito de origem) |
| 4 | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda\|SGV-11177]] | Tramitação e assinatura direcionadas a um membro específico de departamento, e assinatura pro departamento inteiro; fluxo externo de assinatura por CPF com pré-cadastro | Validada — 36/36 CTs aprovados (6 defeitos encontrados e corrigidos), enviada pra Qase (suite 360) — restam 6 pontos de conferência visual/textual fina no Figma |
| 5 | [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda\|SGV-11178]] | Atalho de cadastro rápido de Pessoa Física, Pessoa Jurídica e Departamento embutido nos componentes de seleção de pessoa (campo solicitante, campo PF/PJ, destinatário de despacho, seleção de signatário) | Validação quase concluída — 37/38 CTs aprovados, enviados pra Qase (suite 361) — 1 CT (responsividade do modal de cadastro rápido, defeito SGV-11962) aguardando DEV |

As Partes 3 e 4 confirmam o que o [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/Complemento Figma - Departamento Destinatário E Signatário|Complemento Figma]] já tinha antecipado em 03/09/2026 como escopo futuro da epic (seleção de membro como destinatário direto e departamento/membro como signatário) — recebido do Notion como export bruto em 25/09/2026, com SGVs próprios (11176 e 11177) confirmados no mesmo dia. A Parte 5 (11178) chegou depois, em 30/09/2026, também como export bruto do Notion, com SGV próprio (11178) já confirmado.

## Dependência entre as partes

- A Parte 2 (11184) depende funcionalmente da Parte 1 (11083): precisa existir departamento (com participantes e status ativo/suspenso definidos) antes de testar encaminhamento.
- A Parte 3 (11176) depende da Parte 1 (11083): entrada por convite pressupõe que o departamento já existe.
- A Parte 4 (11177) depende das Partes 1 e 3 (11083, 11176): tramitação/assinatura para membro pressupõe que o membro já é participante do departamento (seja por vínculo manual da 11083, seja por convite da 11176).
- A Parte 5 (11178) é a mais independente das cinco: o atalho de cadastro rápido de PF/PJ não pressupõe departamento nenhum; só o cadastro rápido de Departamento em si depende de já existir ao menos uma PJ com cadastro completo (mesma pré-condição da Parte 1).

Recomendado validar a 11083 primeiro; 11176 e 11184 podem seguir em paralelo depois dela; 11177 valida por último, com massa de dados compatível com as anteriores. A 11178 pode ser validada em paralelo a qualquer uma das outras — só o bloco de cadastro rápido de Departamento se beneficia de já ter PJs completas cadastradas.

## Ordem de leitura sugerida (por parte)

Resumo → card (critérios + CTs) → mesa de refinamento (detalhe técnico), quando existir. As Partes 3, 4 e 5 nasceram já no pacote (`00 README` + `01 - Demanda` + CTs) — sem mesa de refinamento própria, por decisão explícita (requisito já veio completo do Notion).

## Resumos em linguagem simples

- [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/Conhecimento/1 - SGV-11083 - Resumo|SGV-11083 - Resumo]]
- [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/Conhecimento/1 - SGV-11184 - Resumo|SGV-11184 - Resumo]]

## Mesas de refinamento

- [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11083 - Funcionalidade Departamentos Para Cidadão PJ/Conhecimento/2 - SGV-11083 - Refinamento Departamentos Para Cidadao PJ|SGV-11083 - Refinamento]]
- [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/SGV-11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos/Conhecimento/2 - SGV-11184 - Refinamento Departamentos Encaminhar Documentos E Despachos|SGV-11184 - Refinamento]]

## Contexto de apoio (não é fonte de critério de aceite)

Documento de produto consolidado do Notion ("Departamento CNPJ") cobre esta epic **e outras 3 tasks** (SGV-8883, 8884, 9898) numa visão única de produto — usado nas duas mesas só como esclarecimento de detalhe (limites de campo, fluxo de convite, formato de exibição), nunca como origem de critério.

[[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/Complemento Figma - Departamento Destinatário E Signatário|Complemento Figma — departamento como destinatário e signatário]] (recebido 03/09/2026): parte já incorporada à SGV-11184 (formato de exibição, regras de busca/exibição); os dois pontos antes registrados como "possível escopo futuro" — seleção de membro individual como destinatário direto e departamento como signatário de assinatura — foram confirmados em 25/09/2026 e viraram a SGV-11177 (Parte 4).
