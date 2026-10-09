---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.35.3"
status: aprovado
---
# 13 - Especificação do preset piloto (item 1.35.3)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|07 - Mesa de trabalho, etiquetas e tramitação]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]], [[05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05]], [[06 - Especificação do preset piloto (TR 1.33)|06]], [[07 - Especificação do preset piloto (TR 1.34)|07]], [[08 - Especificação do preset piloto (TR 1.35.2.2.1)|08]], [[09 - Especificação do preset piloto (TR 1.35.2.3)|09]], [[10 - Especificação do preset piloto (TR 1.35.2.4)|10]], [[11 - Especificação do preset piloto (TR 1.35.2.5)|11]], [[12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12]]

> [!info] Escopo desta fatia (09/10/2026)
> Décima segunda fatia da especificação do preset: liga **só o item 1.35.3** do recorte 07 — "Encerramento flexível de tramitações, no mínimo: (a) individual por servidor; (b) por setor envolvido; (c) total do documento" — ao que o seed Playwright atual já prepara. Prazos (1.35.2.6–1.35.2.7, já mapeados na fatia 12), associação automática (1.35.4) e histórico geral (1.35.5) ficam **fora desta fatia**. **Reabertura de documentos encerrados (1.33.3.7) já foi mapeada na fatia 06 e não é repetida aqui** — citada só como fronteira. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 07, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Ação de teste (cria em tempo de execução):** mutation chamada por um CT especificamente para validar o cenário — não é algo que o baseline deixa pronto de antemão.
- **Consulta (não prepara estado):** função que só lê dados já existentes.
- **Dependência observada (não confirmado que o seed prepare):** aparece em comentário/shape de código, sem teste real que a exercite.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.

## Encerramento flexível de tramitações (TR 1.35.3)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.35.3 | Mecanismo único por trás dos 3 alcances | Ação de teste | **Confirmado que é uma única mutation parametrizada**: `endDocument(api, documentId, sectorId, {user?, onlySector?})` — os 3 alcances do TR são 3 combinações diferentes dos mesmos dois parâmetros booleanos, não 3 mutations distintas. A mesma função é exercitada tanto no fluxo genérico "Encerrar documento" (CT A10, `close-document.spec.ts`) quanto no painel pós-emissão de despacho "Após emitir, o documento deve:" (CT A37/E42, documento **sem** fluxo de trabalho) | `playwright/src/api/services/documents.ts` (`endDocument`, interface `EndDocumentOptions`); `playwright/tests/api/processing/close-document.spec.ts` (A10); `playwright/tests/api/processing/after-issuing-dispatch.spec.ts` (A37); `playwright/tests/e2e/processing/after-issuing-dispatch.spec.ts` (E42) | Confirmado |
| 1.35.3.a | Individual por servidor | Ação de teste | `endDocument(..., {user: true})` — **confirmado por releitura do documento** que `userStatus` passa a `'CLOSED'` e que `documentStatus` **continua** `'PROCESSING'` (não muda para o próprio agente que fechou). Exercitado nos dois contextos: fluxo genérico (A10-C02) e pós-emissão de despacho (A37-C03/C04, E42-C03/C04) — mesmo comportamento nos dois | `documents.ts` (`endDocument`); `close-document.spec.ts` (A10-C02); `after-issuing-dispatch.spec.ts` (A37-C03/C04); `e2e/processing/after-issuing-dispatch.spec.ts` (E42-C03/C04) | Confirmado |
| 1.35.3.a | "Mantém tramitação normal nos demais" (outros servidores envolvidos) | — | **Não verificado nesta fatia**: todos os CTs citados releem o documento pelo mesmo agente que executou o encerramento individual — não encontrei teste que confirme, pela ótica de **outro** servidor envolvido no mesmo documento, que a tramitação de fato continua normal para ele | — | A confirmar |
| 1.35.3.b | Por setor envolvido | Ação de teste | `endDocument(..., {onlySector: true})` — **confirmado por evento na timeline**: gera `SECTOR_ENDED` (assíncrono, verificado via `expect.poll`). Um comentário no código descreve o efeito como "mantém a custódia no setor" — isso **não foi verificado por asserção própria** nesta cobertura, só a existência do evento. **Só exercitado no contexto pós-emissão de despacho** (A37-C01/C02, E42-C01/C02) — `close-document.spec.ts` (fluxo genérico de encerrar) não testa `onlySector` | `documents.ts` (`endDocument`); `after-issuing-dispatch.spec.ts` (A37-C01/C02); `e2e/processing/after-issuing-dispatch.spec.ts` (E42-C01/C02) | Confirmado (evento `SECTOR_ENDED` existe); A confirmar (efeito "custódia no setor" como asserção própria; exercício fora do contexto pós-despacho) |
| 1.35.3.b | "Encerra em massa nas mesas dos servidores do setor" | — | **Não encontrei teste que verifique o efeito em massa**: nenhum CT lido consulta a mesa de trabalho de um **segundo** servidor do mesmo setor após o `SECTOR_ENDED`, nem o campo `sectorStatus` do documento é asserido diretamente em nenhum teste (só citado em comentário) | `documents.ts`, campo `sectorStatus: unknown` (nunca lido por asserção nos testes encontrados) | A confirmar |
| 1.35.3.c | Total do documento | Ação de teste | `endDocument(...)` **sem opções** (`user`/`onlySector` ambos no padrão) — **confirmado só por evento**: gera `'ENDED'` na timeline (A10-C01). **Não encontrei** nenhum teste que, para essa chamada específica (sem opções), releia o documento e confirme `documentStatus === 'CLOSED'` diretamente — a única asserção de `documentStatus: 'CLOSED'` encontrada no código vem de um mecanismo **diferente** (ver fronteira "revogar" abaixo), não deste caminho. Também não exercitado no contexto pós-emissão de despacho (A37/E42 só testam `user`/`onlySector`, nunca a chamada sem opções) | `documents.ts` (`endDocument`); `close-document.spec.ts` (A10-C01) | Confirmado (evento `'ENDED'` existe); A confirmar (se `documentStatus` muda para `'CLOSED'` neste caminho; efeito "em todos os setores/servidores de uma vez") |

## Fronteiras com itens vizinhos (fora desta fatia)

- **Revogar documento** (`revokeDocument`/`makeRevoke`, CT A29-C01, `revoke-document.spec.ts`) é um mecanismo **diferente** do encerramento tratado nesta fatia: produz `documentStatus: 'CLOSED'` **e** `isRevoked: true` numa mutation própria (`revokeDispatch`, reaproveitada tanto para "cancelar" quanto para "revogar", conforme já registrado na fatia 10). **Não presumo identidade** entre "revogar" e "encerramento total" (1.35.3.c) só porque os dois citam `documentStatus: 'CLOSED'` — são mutations e semânticas distintas no código, e o TR trata encerramento e revogação como conceitos separados (revogação não está em 1.35.3). É a única evidência encontrada de `documentStatus: 'CLOSED'` confirmado por asserção direta no código lido.
- **Reabertura de documentos encerrados** (1.33.3.7) já foi mapeada na fatia 06 ([[06 - Especificação do preset piloto (TR 1.33)|piloto 06]]) — `reopenDocumentInSector`, evento `RESUME` (CT A10-C03, sobre um documento fechado pelo caminho "total"/sem opções). Não revisitado aqui, só referenciado.
- **Pausar documento** (`changeDocumentStatus`, `newStatus: 'PAUSED'`/`'OPEN'`, parâmetro `type` default `'NO_DEADLINE'`) é um mecanismo **diferente** de pausa/reabertura de status geral — não é um dos 3 alcances de encerramento do TR 1.35.3, não analisado nesta fatia.
- **Prazos** (1.35.2.6–1.35.2.7) já foram mapeados na fatia 12 ([[12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|piloto 12]]) — não revisitados aqui.
- **Associação automática** (1.35.4) e **histórico geral** (1.35.5) seguem como fatias futuras, não analisadas aqui.

## O que falta para este recorte virar preset executável (resumo)

- **Efeito "em massa" do encerramento por setor (1.35.3.b)** — confirmado só o evento `SECTOR_ENDED`; nenhum teste verifica a mesa de outro servidor do mesmo setor nem o campo `sectorStatus` diretamente.
- **`documentStatus` no encerramento total (1.35.3.c)** — confirmado só o evento `'ENDED'`; nenhum teste releu o documento para confirmar `documentStatus === 'CLOSED'` neste caminho específico (a única asserção desse tipo encontrada pertence a um mecanismo diferente, "revogar").
- **Efeito "mantém tramitação normal nos demais" (1.35.3.a e 1.35.3.b)** — não verificado pela ótica de outros servidores/setores envolvidos; todos os CTs releem pelo mesmo agente que executou a ação.
- **Encerramento por setor (`onlySector`) fora do contexto pós-emissão de despacho** — só exercitado nos CTs A37/E42 (painel "Após emitir"); não encontrei teste que use essa opção no fluxo genérico de "Encerrar documento".
- **Encerramento total (sem opções) fora do fluxo genérico** — só exercitado em A10-C01 (`close-document.spec.ts`); não exercitado no contexto pós-emissão de despacho.
- **Nenhum encerramento integra o baseline persistente** — todos os CTs citados (A10, A37, E42) criam seu próprio documento e o encerram em tempo de execução.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] — só o item 1.35.3 foi usado nesta fatia.
- Piloto anterior (referência, não repetida como requisito aqui): [[06 - Especificação do preset piloto (TR 1.33)]] (reabertura, 1.33.3.7); [[10 - Especificação do preset piloto (TR 1.35.2.4)]] (origem da observação sobre `revokeDispatch` reaproveitada).
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/api/services/documents.ts` (`endDocument`, interface `EndDocumentOptions`, `reopenDocumentInSector`, `revokeDocument`, `changeDocumentStatus`, campos `userStatus`/`sectorStatus`/`documentStatus` da interface `DocumentForAgent`), `playwright/src/data/factories/documents.ts` (`makeRevoke`), `playwright/tests/api/processing/close-document.spec.ts` (A10-C01–C03), `playwright/tests/api/processing/after-issuing-dispatch.spec.ts` (A37-C01–C04), `playwright/tests/e2e/processing/after-issuing-dispatch.spec.ts` (E42-C01–C04), `playwright/tests/api/processing/revoke-document.spec.ts` (A29-C01, citado só como fronteira). Lido nesta sessão, só leitura — nenhum comando executado.
