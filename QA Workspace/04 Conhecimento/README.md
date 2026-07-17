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
| (raiz) | Análises de refinamento arquivadas (ver seção abaixo) |

Notas de documentação usam o template [[../Sistema/Templates/Conhecimento.md|Conhecimento.md]].

## Regras de uso

1. **Fonte da verdade**: o que está aqui é *conhecimento de QA* — observado em teste ou importado. Quando divergir do comportamento real do sistema, o sistema ganha e a nota se atualiza (anotar a data da revisão).
2. **Importar ≠ copiar tudo**: ao importar documentação, trazer só o que ajuda a testar (regras, restrições, perfis, estados possíveis). O resto vira link na seção Referências da nota.
3. **Aprendizado pontual em validação** continua nascendo na daily ou no card da demanda — sobe pra cá quando virar regra estável de um módulo, não coisa de um card só.
4. **Documentação do repositório de código** (`Sogov-application/docs/`): não duplicar — linkar o caminho e resumir o que interessa pra QA. Estrutura de lá: `contexto/` (api, web, fluxos, serviços externos) e `usecases/` (dispatch, document-event, document-object, download, notification, signature).

## Análises de refinamento (primeiro tipo estruturado)

Quando um refinamento do [[../05 Refinar/README|05 Refinar]] é concluído ([[../Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada (Notion → vault)|fluxo 6]]), o arquivo de mesa de trabalho ([[../Sistema/Templates/Refinamento.md|Refinamento.md]]) é **arquivado aqui** — com a análise completa (causa raiz, evidências, hipóteses descartadas, decisões dos pontos a definir) que **não entra no card**:

- Nome do arquivo: `<SGV> - Refinamento <título curto>.md` (mesmo título curto do card, prefixado por "Refinamento")
- `status: refinado` no frontmatter (era `em_refinamento` na fila)
- O card correspondente em `02 Demandas/` referencia este arquivo em **Observações** (wikilink), e este arquivo linka o card — rastro nos dois sentidos

A fonte de verdade externa da análise continua sendo a task no Notion (`📤`); a cópia daqui é o acervo local pesquisável — vale pra investigar bug parecido depois, sem depender de buscar no Notion.

> [!note] Auto-organizador
> O [[../Sistema/Skills/SKILL_INBOX|SKILL_INBOX]] só roteia pra cá as análises de refinamento (fluxo 6); as pastas de documentação (`Módulos/`, `Fluxos/`, `Referências/`) são alimentadas manualmente (ou pedindo pra IA numa sessão). Quando o uso estabilizar, atualizar o skill com regras de roteamento pra elas.
