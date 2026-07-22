---
tags:
  - sistema
  - skills
---
# Skills

Instruções de referência para atividades de QA. Diferente de [[../Agentes/README|Agentes]] (que disparam sozinhos), skills são consultados quando você ou a IA precisam executar uma tarefa específica.

## Skills ativos

| Skill | Quando usar |
|---|---|
| [[SKILL_BUGS]] | Criar, revisar e organizar bugs no padrão do vault |
| [[SKILL_CASOS_DE_TESTE]] | Criar casos de teste no formato Dado/Quando/Então |
| [[SKILL_PLANO_DE_TESTE]] | Criar planos de teste para melhorias e funcionalidades |
| [[SKILL_PADRONIZACAO]] | Revisar e padronizar documentos do vault |
| [[SKILL_INBOX]] | Como invocar o auto-organizador da daily |
| [[SKILL_LIMPEZA_EXPORT]] | Limpar .md bruto exportado do Notion (3 modos: mesa, card direto, documentação) |
| [[SKILL_REFINAMENTO]] | Conduzir a mesa de refinamento (05 Refinar) até o card destilado — gate de doc, CTs, encadeia pra validação/automação |
| [[SKILL_TRIAGEM_SPRINT]] | Processar view de sprint do Notion (agrupar por status, cruzar com vault) |
| [[SKILL_REVISAO_ESCOPO_MR]] | Revisar escopo de MR via git fetch, levantar cenários de teste |
| [[SKILL_REVISAO_AUTOMACAO_E2E]] | Revisar código de teste e2e (padrão + coerência de asserts) antes de subir |
| [[SKILL_VERIFICACAO_DOC]] | Cruzar bug/demanda contra a doc de módulo (04 Conhecimento) — confirma critério ou expõe divergência |
| [[SKILL_INICIAR_AUTOMACAO]] | Ir de um card validado ao início da automação — gates (validação + ambiente), onde escrever e o que reaproveitar |

> Onde as "avulsas" entram na cadeia: [[SKILL_TRIAGEM_SPRINT]] é a **entrada** de uma view de sprint (fluxo 9) e alimenta refinamento/fila; [[SKILL_PLANO_DE_TESTE]] roda **em paralelo** ao card, pra melhorias/funcionalidades/épicos (fluxo 4).
