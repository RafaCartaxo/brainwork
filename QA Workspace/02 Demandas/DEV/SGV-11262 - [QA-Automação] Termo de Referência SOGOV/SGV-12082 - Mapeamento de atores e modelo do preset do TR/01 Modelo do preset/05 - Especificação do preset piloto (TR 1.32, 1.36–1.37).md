---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: especificacao-preset
itens_tr: "1.32, 1.36–1.37"
status: aprovado
---
# 05 - Especificação do preset piloto (itens 1.32, 1.36–1.37)

> [!info]- Navegação
> **Matriz/índice:** [[01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../00 QA/01 - Demanda]] · **Mapa geral:** [[00 - Mapa geral]] · **Recorte-fonte:** [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)|06 - Atores externos e atendimento ao cidadão]] · **Fatias anteriores:** [[02 - Especificação do preset piloto (TR 1.24–1.27)|02]], [[03 - Especificação do preset piloto (TR 1.28–1.29)|03]], [[04 - Especificação do preset piloto (TR 1.30–1.31)|04]]

> [!info] Escopo desta fatia (09/10/2026)
> Quarta fatia da especificação do preset: liga o recorte 06 (Contato externo, Usuário externo, Central de atendimento, Demanda externa) ao que o seed Playwright atual já prepara. **Não é implementação de seed, não decompõe CTs, não propõe arquitetura nem formato novo de preset.** O recorte 06, a matriz e o mapa geral **não foram alterados**. Repositório consultado: `/home/sogov-rafael-cartaxo/Documentos/Sogov/sogov-automation-playwright`, commit `16c41e4` (branch principal). Leitura somente de código; nenhum teste foi executado nesta rodada.

> [!important] Restrição de ambiente confirmada por Rafael (09/10/2026)
> Cada QA terá ambiente próprio; o seed tem alto custo, é formado uma vez e permanece persistente; a implementação será feita por outro QA. Esta nota descreve **necessidades de dados por cenário** — não presume nova execução do seed nem escolhe mecanismo técnico.

## Como ler a tabela

- **Baseline reutilizável:** dado/estado que a população inicial do seed já carrega.
- **Preparação específica de cenário:** dado/estado que só alguns cenários precisam — não integra a população padrão; pode ser preparado uma única vez no ambiente persistente, sem presumir execução por teste.
- Estados de conhecimento: **Confirmado** (visto direto no TR, no código ou numa captura real de API/execução), **Inferido**, **A confirmar**.
- Esta nota **não** reabre as dúvidas já registradas no recorte 06 (Contato × Usuário externo; "entes externos"; estado da Demanda) — só confere se o código adiciona evidência nova a elas, deixando claro quando não adiciona.

## Contato externo e cadastro (TR 1.32)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.32 | Contato externo PJ — nome, CNPJ, cadastro único | Baseline | `BASELINE.citizens` (5 identidades nomeadas: `citizen`, `engineer`, `architect`, `manager`, `alphanumeric`) + `BASELINE.pools.citizen`/`pools.alphanumeric` (4 cada) | `playwright/src/data/seed/baseline.ts` | Confirmado |
| 1.32 | Contato externo PF — nome, CPF | — | **Mesma lacuna já registrada no piloto 1.24–1.27**: não há cidadão PF próprio no baseline; os testes reaproveitam o CPF de um servidor (`seed.agents.agent`) como identificador de cidadão PF (ex.: `citizen/list.spec.ts`, caso A03-C02). Não é uma entidade nova — confirmo que a lacuna persiste neste recorte também | `playwright/tests/api/citizen/list.spec.ts` | Confirmado (lacuna, não suposição) |
| 1.32 | Cadastro único — impede segundo cadastro com o mesmo CPF/CNPJ | Preparação específica de cenário | `signup()` (API pública de auto-cadastro) + `makeCitizenPJAutoRegistration` (payload completo: cnpj, nome, responsável legal, telefone, e-mail, senha). Exercitado pelo CT A02-C08: tentar cadastrar de novo um CNPJ já existente é **rejeitado** — confirma a regra de cadastro único, do lado da rejeição | `playwright/src/auth/auth-client.ts` (função `signup`); `playwright/src/data/factories/seed.ts` (`makeCitizenPJAutoRegistration`); `playwright/tests/api/auth/login.spec.ts` (A02-C08) | Confirmado |
| 1.32 | Cadastro único PF (auto-registro) | — | Não encontrei um `makeCitizenPFAutoRegistration` ou equivalente — só a fábrica de auto-cadastro PJ existe no código lido. Não presumo ausência de cadastro PF no produto, só não achei a fábrica de teste | — | A confirmar |
| 1.32.1 | E-mail de confirmação de cadastro | Baseline (quando o cidadão precisa ser criado) | **Confirmado no próprio seed, não só em CT**: `getCitizenOrCreate` (chamada por `provision.ts` para garantir o cidadão PJ do baseline) primeiro busca o cidadão por CNPJ; **se não existir**, chama `signup()` isolado, aguarda de verdade o token de confirmação chegar por e-mail (`mailbox.waitForRegistrationToken`) e então chama `confirmUser(userId, finishToken)` — o fluxo completo de cadastro + confirmação por e-mail do TR 1.32.1 é exercitado de ponta a ponta. **Limite confirmado**: isso só roda quando o cidadão ainda não existe na instância; numa instância já provisionada (cidadão reaproveitado), esse caminho **não é exercitado** de novo. O CT A02-C08 é um caminho **diferente** (rejeição de cadastro duplicado) e não usa essa confirmação | `playwright/src/api/services/users.ts`, função `getCitizenOrCreate` (chama `signup`, `mailbox.waitForRegistrationToken`, `confirmUser`); `provision.ts` L.480 (uso real no baseline) | Confirmado (fluxo completo, condicionado à criação) |

## Central de atendimento e acesso a serviços (TR 1.36)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.36 | Central de atendimento — cidadão acessa Serviços disponibilizados externamente | Baseline (campo) + preparação específica de cenário (consulta) | Cada Serviço tem `isOpenExternal` (booleano) — `true` por padrão em `makeService`, mas o baseline também cria `openExternalDisabled` (`Service PA Abertura Externa Desativada API`) especificamente com `isOpenExternal: false`. As duas queries reais usadas pelo cidadão pra selecionar serviço (`getModuleMatterServices`, `getMatterServicesByTerm` com `citizenMode: true`) **não retornam** serviços com abertura externa desativada — confirmado por CTs de regressão (A47-C01/C03) e seus controles positivos (A47-C02/C04) | `baseline.ts` (`services.openExternalDisabled`); `playwright/src/data/factories/seed.ts` (`makeService`, campo `isOpenExternal`); `playwright/tests/api/matters-services/citizen-open-external-selection.spec.ts` | Confirmado |
| 1.36 | "Canais digitais do órgão" — mecanismo exato | — | Não localizado no código lido nesta rodada — a leitura cobriu a seleção de serviço, não a camada de "canal". O recorte 06 já registra isso como "A confirmar"; não adiciono evidência nova | — | A confirmar (sem mudança) |
| 1.36 | "Entes externos" — terceiro tipo de ator além de PF/PJ | — | Não encontrei nenhum terceiro tipo de identidade externa no código (`BASELINE.citizens`/`pools` só têm PF-via-agente e PJ). Isso **não contradiz** a dúvida do recorte 06 — reforça que, pelo menos no seed atual, só os dois tipos existem | `baseline.ts` | A confirmar (sem nova evidência de existência de um terceiro tipo) |

## Usuário externo e Demanda externa (TR 1.37)

| Ref. TR | Ator/dado/estado necessário | Baseline × cenário | Cobertura atual do seed (Playwright, `main`) | Evidência/fonte | Estado |
|---|---|---|---|---|---|
| 1.37 | Demanda externa — solicitação aberta por usuário externo | Preparação específica de cenário | **Confirmado**: existe `makeExternalDocument`/`generateExternalDocument` — "Documento aberto por cidadão", com payload próprio (setor de destino, identidade do cidadão anexada como `person-1_P`, campos do formulário). É usado em mais de 10 specs reais (ex.: `cancel-citizen-request.spec.ts` — cancelar uma solicitação do cidadão; `citizen-dispatch-emit-and-sign.spec.ts`; `citizen-mention-dispatch.spec.ts`) — o código confirma esse mecanismo de criação de documento por cidadão. **O que isso não confirma**: se o produto trata essa criação como uma entidade de negócio própria chamada "Demanda" (nome e ciclo de vida distintos) ou só como um Documento/Processo comum com origem externa — a equivalência com a entidade "Demanda" do TR segue como inferência, não confirmada pelo código | `playwright/src/data/factories/documents.ts` (`makeExternalDocument`); `playwright/src/api/services/documents.ts` (`generateExternalDocument`); specs que a usam (ex.: `playwright/tests/e2e/processing/cancel-citizen-request.spec.ts`) | Confirmado (mecanismo de criação); Inferido (equivalência com a entidade "Demanda") |
| 1.37 | Interação do cidadão limitada a abertura (variante de configuração) | Baseline (módulo específico) | `BASELINE.services.citizenOpeningOnly` ("Service PA Interage Somente Abertura API") — comentário no código confirma: "o cidadão só interage na ABERTURA: depois disso o servidor precisa endereçá-lo num despacho pra ele poder responder". É uma variante de configuração do mesmo mecanismo de Serviço, não uma entidade nova | `baseline.ts` (comentário de `services.citizenOpeningOnly`) | Confirmado |
| 1.37 | Usuário externo acompanha/interage/assina/imprime | — | Não verifiquei nesta rodada os mecanismos de assinatura/impressão do lado do cidadão especificamente para este recorte — já cobertos de forma geral no piloto 1.30–1.31 (Documento automatizado) e no recorte 08 (Assinaturas), não reexplorados aqui | — | A confirmar (fora do escopo desta fatia) |
| 1.37 | Estado da Demanda (Pausada/Encerrada, já esclarecido no recorte 06 via Mesa de trabalho) | — | Não busquei evidência de código nova para esse ponto nesta fatia — o recorte 06 já tem contexto de produto registrado; não dupliquei a verificação | — | Sem mudança (ver recorte 06) |

## O que falta para este recorte virar preset executável (resumo)

- **Cidadão PF próprio** — mesma lacuna do piloto 1.24–1.27, reconfirmada aqui: nenhuma identidade PF independente, nem fábrica de auto-cadastro PF.
- **E-mail de confirmação de cadastro (1.32.1)** — confirmado como fluxo completo (`getCitizenOrCreate`), mas só roda quando o cidadão precisa ser criado; numa instância já provisionada, não é exercitado de novo.
- **"Demanda externa" como entidade de negócio própria** — confirmado o mecanismo de criação (`makeExternalDocument`/`generateExternalDocument`, usado em várias specs reais); segue como inferência se o produto trata isso como uma entidade "Demanda" separada ou só como Documento/Processo comum de origem externa.
- **"Entes externos" e canais digitais do órgão** — mencionados no TR, mas sem definição (já registrado no recorte 06); sem evidência adicional no código consultado nesta fatia.

## Fontes/evidências

- Recorte do TR (fonte do modelo conceitual, não alterado nesta rodada): [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)]].
- Código do repositório Playwright (`main`, commit `16c41e4`): `playwright/src/data/seed/baseline.ts`, `playwright/src/data/factories/seed.ts`, `playwright/src/auth/auth-client.ts`, `playwright/src/api/services/users.ts` (`getCitizenOrCreate`, `confirmUser`), `playwright/src/data/factories/documents.ts` (`makeExternalDocument`), `playwright/src/api/services/documents.ts` (`generateExternalDocument`), `playwright/src/data/seed/provision.ts`, `playwright/tests/api/auth/login.spec.ts`, `playwright/tests/api/citizen/list.spec.ts`, `playwright/tests/api/matters-services/citizen-open-external-selection.spec.ts`, `playwright/tests/e2e/processing/cancel-citizen-request.spec.ts`. Lido nesta sessão, só leitura — nenhum comando executado.
