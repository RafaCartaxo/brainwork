---
tags:
  - qa
  - agente
---
# Agente: Processar Export do Notion

Recebe .md bruto exportado do Notion e executa o pipeline completo de classificação → limpeza → roteamento → registro, sem intervenção.

## Por que existe

Exportar do Notion e processar é um fluxo que acontece quase todo dia. Hoje, cada export exige que Rafael saiba qual caminho seguir (modo A, B ou C? mesa ou card direto? triagem ou documentação?). O agente decide sozinho — Rafael só dropa o arquivo e diz "processa".

## Gatilhos

| Gatilho | Quando dispara |
|---|---|
| **Comando explícito** | "processa o material novo", "processa o export SGV-XXXX", "processa os exports na pasta Downloads" |
| **Arquivo novo em 05 Refinar/** | Detecta .md bruto recém-chegado e oferece processar |
| **Sessão interativa** | Rafael cola o conteúdo do export no chat e pede pra processar |

## Pipeline

```
.md bruto (export Notion)
        │
        ▼
┌───────────────────┐
│ 1. CLASSIFICAR    │  ← O que é isso?
└───┬───────┬───────┘
    │       │       │
  task   triagem   doc
  única  sprint
    │       │       │
    ▼       ▼       ▼
┌──────┐ ┌──────┐ ┌───────────┐
│LIMPAR│ │LIMPAR│ │LIMPAR     │
│A ou B│ │+agrup│ │(modo C)   │
└──┬───┘ └──┬───┘ └─────┬─────┘
   │        │            │
   ▼        ▼            ▼
┌──────┐ ┌──────┐ ┌──────────┐
│mesa  │ │05 Ref│ │04 Conhec │
│OU    │ │Triag │ │/subpasta │
│card  │ │-SP X │ │          │
└──────┘ └──────┘ └──────────┘
```

## Como classificar

| Se o export tem... | Tipo | Skill usado |
|---|---|---|
| 1 card, SGV identificável, descrição de problema | **Task única** | [[../Skills/SKILL_LIMPEZA_EXPORT\|SKILL_LIMPEZA_EXPORT]] modo A ou B |
| Vários cards, colunas de status do Notion (board view) | **Triagem de sprint** | [[../Skills/SKILL_TRIAGEM_SPRINT\|SKILL_TRIAGEM_SPRINT]] |
| Sem SGV, conteúdo descritivo/referência | **Documentação** | [[../Skills/SKILL_LIMPEZA_EXPORT\|SKILL_LIMPEZA_EXPORT]] modo C |

### Task única — completude

Após limpar, o agente avalia se a task está completa o suficiente pra card direto:

- ✅ Descrição clara do problema
- ✅ Passo a passo pra reproduzir
- ✅ Critérios de aceite definidos
- ✅ Ambiente especificado

**4/4?** → Modo B: card direto em `02 Demandas/<ambiente>/`.
**Falta algo?** → Modo A: envelopar no [[../Templates/Refinamento.md\|Refinamento.md]] em `05 Refinar/`.

## O que o agente sempre faz (qualquer tipo)

- ✅ Remove lixo de export (metadados, campos vazios, artefatos)
- ✅ Identifica e registra lacunas (vira item em Pontos a definir)
- ✅ Registra na daily com a frase padrão do catálogo ([[../../../QA Workspace/01 Daily/README\|01 Daily/README]])
- ✅ Cria pendências na fila (fila viva — [[AGENTE_ORGANIZADOR\|AGENTE_ORGANIZADOR]])
- ✅ Remove arquivo original do Downloads (se aplicável)
- ✅ Registra tudo no bloco `### Auto-organização`
- ✅ Se for documentação e a estrutura de `04 Conhecimento/` não existir, cria

## Relação com outros agentes

| Agente | Quando é chamado |
|---|---|
| **AGENTE_ORGANIZADOR** | Após processar: cria pendências, reconcilia Atividades, mantém fila viva |
| **AGENTE_MIGRACAO_CARDS** | Se o processamento gerar card que precisa ser movido na esteira |
| **AGENTE_STATUS_REUNIAO** | Cards/documentos processados hoje aparecem no Fiz |

## Exemplos reais (das dailies)

### Task única → mesa (SGV-4873, dia 17/07)
```
Export SGV-4873.md (Downloads) → classificada como task única,
incompleta → modo A → envelopada no Refinamento.md →
05 Refinar/SGV-4873 → pendência "Refinar" na fila
```

### Triagem de sprint (SP15, dia 17/07)
```
Export sprint-15.md (Downloads, 53 cards) → classificada como
triagem → SKILL_TRIAGEM_SPRINT → 05 Refinar/Triagem - SP15 →
53 cards agrupados, 7 com link pro vault, 2 divergências anotadas
```

### Documentação (Assinaturas, dia 17/07)
```
Export Assinaturas.md → classificada como documentação →
modo C → template Conhecimento.md → 04 Conhecimento/Módulos/
```

## Resultado Esperado

Export processado, classificado, limpo e roteado pro destino correto — com rastro completo na daily e pendências na fila. Rafael não precisa decidir nada: o agente encontra o caminho.
