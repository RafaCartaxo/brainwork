---
tags:
  - qa
  - conhecimento
---
# 04 Conhecimento

Base de conhecimento sobre o Sogov — comportamentos do sistema, regras de negócio aprendidas nas validações, documentação importada e referências técnicas. O objetivo é dar assertividade aos testes: antes de validar um módulo, conferir aqui o que já se sabe sobre ele.

## Estrutura

| Pasta | O que vai aqui |
|---|---|
| `Módulos/` | Uma nota por módulo/funcionalidade do Sogov (Documentos, Despachos, Assinatura, Notificações, Central de Atendimento…) com regras de negócio e comportamentos conhecidos |
| `Fluxos/` | Fluxos de negócio ponta a ponta que cruzam módulos (ex.: ciclo de vida de um documento, da abertura à conclusão) |
| `Referências/` | Material importado ou linkado de fora: docs do repositório, manuais, links externos, leis e normativas (ex.: TCE-PE) |
| `Tasks/<SGV>/` | Todo material de análise **específico de uma task** — refinamento arquivado, plano de automação, e o que mais vier daquela SGV. Um subdiretório por task, nomes de arquivo completos dentro (ver seção abaixo) |

A raiz não recebe nenhum arquivo — só este `README.md` e as quatro subpastas acima. Se não é conhecimento de módulo, fluxo cruzado, referência externa ou material de uma task específica, não pertence a `04 Conhecimento/`.

Notas de documentação usam o template [[../../Sistema/Templates/Conhecimento.md|Conhecimento.md]].

## Regras de uso

1. **Fonte da verdade**: o que está aqui é *conhecimento de QA* — observado em teste ou importado. Quando divergir do comportamento real do sistema, o sistema ganha e a nota se atualiza (anotar a data da revisão).
2. **Importar ≠ copiar tudo**: ao importar documentação, trazer só o que ajuda a testar (regras, restrições, perfis, estados possíveis). O resto vira link na seção Referências da nota.
3. **Aprendizado pontual em validação** continua nascendo na daily ou no card da demanda — sobe pra cá quando virar regra estável de um módulo, não coisa de um card só.
4. **Documentação do repositório de código** (`Sogov-application/docs/`): não duplicar — linkar o caminho e resumir o que interessa pra QA. Estrutura de lá: `contexto/` (api, web, fluxos, serviços externos) e `usecases/` (dispatch, document-event, document-object, download, notification, signature).

## Tasks/ — material específico de uma task

Objetivo: parar de espalhar o "acervo de análise" de uma mesma task por pastas diferentes só porque cada documento tem um *tipo* diferente (refinamento, plano de automação…). Tudo que é sobre a SGV-X vive em `Tasks/SGV-X/`, sem competir com o papel do card em `02 Demandas/` — o card continua sendo o artefato limpo pra QA testar; o que vai pra `Tasks/` é o material de apoio que **não entra no card**.

### Refinamento arquivado (primeiro tipo estruturado)

Quando um refinamento do [[../05 Refinar/README|05 Refinar]] é concluído ([[../../Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada|fluxo 6]]), o arquivo de mesa de trabalho ([[../../Sistema/Templates/Refinamento.md|Refinamento.md]]) é **arquivado em `Tasks/<SGV>/`** — com a análise completa (causa raiz, evidências, hipóteses descartadas, decisões dos pontos a definir):

- Caminho: `Tasks/<SGV>/<SGV> - Refinamento <título curto>.md` (nome de arquivo completo, mesmo dentro da subpasta — facilita busca/quick-switcher, mesmo padrão de `02 Demandas/`)
- `status: refinado` no frontmatter (era `em_refinamento` na fila)
- O card correspondente em `02 Demandas/` referencia este arquivo em **Observações** (wikilink), e este arquivo linka o card — rastro nos dois sentidos

A fonte de verdade externa da análise continua sendo a task no Notion (`📤`); a cópia daqui é o acervo local pesquisável — vale pra investigar bug parecido depois, sem depender de buscar no Notion.

### Outro material da mesma task

Plano de automação, handoff, ou qualquer outro documento específico daquela SGV entra na mesma subpasta (`Tasks/<SGV>/`), junto do refinamento (se existir). Não precisa de refinamento prévio pra a task ganhar uma subpasta em `Tasks/`.

> [!note] Auto-organizador
> O [[../../Sistema/Agentes/AGENTE_PROCESSAR_EXPORT|AGENTE_PROCESSAR_EXPORT]] roteia documentação automaticamente pra cá (modo C do [[../../Sistema/Skills/SKILL_LIMPEZA_EXPORT|SKILL_LIMPEZA_EXPORT]]). As pastas de documentação (`Módulos/`, `Fluxos/`, `Referências/`, `Tasks/`) também podem ser alimentadas manualmente (ou pedindo pra IA numa sessão).
