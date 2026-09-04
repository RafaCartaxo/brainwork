---
tags:
  - qa
  - qase
tipo: referencia
status: enviado
suite_id: 220
---
# Preparação Qase: Departamentos — encaminhar documentos e despachos

> [!info] Como usar este arquivo
> Nasce **rascunho** pra revisão antes de qualquer POST/PATCH real na Qase. Depois do `--apply`, os ids/hashes entram aqui e o arquivo vira o **registro definitivo** — nunca é descartado. Este aqui já passou pela 1ª rodada (criação dos 21 casos, 04/09/2026) e está na 2ª (enriquecimento: description/postconditions + shared steps).

Fonte: [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]]. Ferramenta: `sogov-automation-test/scripts/qase-sync-9296-departamentos/`. Suite: **220** ("9296 - Possibilidade de Cadastrar Contato/Departamento sem CPF/CNPJ"), projeto `SGV`.

21 dos 28 CTs do card (7 ficaram de fora, marcados "Não se aplica" — ver seção no fim).

---

## Shared steps (mecânicas repetidas entre CTs)

### `busca-3-caracteres` — Busca de departamento com filtro progressivo a partir de 3 caracteres
*(usado em: CT-002/id 444, CT-007/id 449)*
1. Ação: O servidor informa parte do nome do departamento ou a razão social da PJ, a partir de 3 caracteres digitados. Resultado esperado: O sistema retorna os departamentos correspondentes do mesmo cliente/instância, afunilando o resultado a cada caractere digitado; com menos de 3 caracteres, nenhum resultado é retornado.
- Hash na Qase: `0437ba49056fc231f29ff1dd4743a4a5bcb143dc`

### `accordion-click-area` — Área de clique do accordion restrita ao chevron; seleção usa a linha inteira
*(usado em: CT-002c/id 445, CT-008a/id 451)*
1. Ação: O servidor clica no ícone de chevron. Resultado esperado: O accordion expande ou recolhe, mostrando/ocultando os participantes.
2. Ação: O servidor clica em qualquer outro ponto da linha do departamento (do início do nome ao fim do container). Resultado esperado: O departamento é selecionado como destinatário, com a mesma estética de hover de seleção já existente — a expansão do accordion não interfere na seleção, e vice-versa.
- Hash na Qase: `def9e4d06f3622f906ad6781b07cc06ab02f291a`

---

## A. Selecionar departamento em campo pessoa de documento

### CT-001 Departamento só aparece com Pessoa Jurídica habilitada no campo
- **Descrição:** CA01 — SGV-11184, grupo A (campo pessoa configurado pra Pessoa Jurídica).
- **Precondição:** Um campo pessoa está configurado pra aceitar Pessoa Jurídica.
- **Passos:** 1. Ação: O servidor pesquisa um destinatário → Resultado esperado: A busca inclui departamentos ativos vinculados a cidadãos PJ; com a configuração desabilitada, nenhum departamento é exibido ou aceito.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `443`

### CT-002 Busca de departamentos por nome ou razão social, só da mesma instância
- **Descrição:** CA02 — SGV-11184, grupo A.
- **Precondição:** A busca de departamentos está habilitada no campo.
- **Passos:** usa o shared step `busca-3-caracteres`, exibindo nome do departamento e razão social da PJ em cada resultado.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `444`

### CT-002c Área de clique do accordion vs. seleção do departamento
- **Descrição:** CA02 — SGV-11184, grupo A. Defeito [[QA Workspace/02 Demandas/Concluídas/11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] (corrigido, aprovado em DEV em 03/09/2026).
- **Precondição:** O departamento é exibido como accordion no resultado da busca.
- **Passos:** usa o shared step `accordion-click-area`.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `445`

### CT-003 Vínculo é persistido e revalidado pela API
- **Descrição:** CA03 — SGV-11184, grupo A.
- **Precondição:** O servidor selecionou um departamento válido no campo pessoa.
- **Passos:** 1. Ação: Salva o documento → Resultado esperado: O vínculo entre documento, campo pessoa e departamento é persistido, e a API revalida a configuração do campo, o status do departamento e a instância, independente da validação da interface.
- **Pós-condição:** Vínculo documento↔campo↔departamento persistido no banco, revalidado pela API.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `446`

### CT-004 Multiplicidade do campo é respeitada e duplicidade é bloqueada
- **Descrição:** CA04 — SGV-11184, grupo A.
- **Precondição:** Um campo pessoa de seleção única ou múltipla.
- **Passos:** 1. Ação: O servidor seleciona departamentos → Resultado esperado: O sistema respeita a multiplicidade configurada e impede repetir o mesmo departamento.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `447`

### CT-005 Representação do departamento no PDF do documento
- **Descrição:** CA05 — SGV-11184, grupo A. Formato confirmado no complemento do Figma (03/09/2026): parênteses, não travessão.
- **Precondição:** O documento tem um departamento num campo pessoa.
- **Passos:** 1. Ação: O PDF é gerado ou regenerado → Resultado esperado: O valor aparece no formato "Nome do departamento (Razão social da PJ)".
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `448`

---

## B. Selecionar departamento como destinatário de despacho

### CT-007 Busca no campo de destinatário do despacho
- **Descrição:** CA01 — SGV-11184, grupo B.
- **Precondição:** Um servidor está criando ou editando um despacho.
- **Passos:** usa o shared step `busca-3-caracteres`.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `449`

### CT-008 Apresentação do resultado no componente
- **Descrição:** CA02 — SGV-11184, grupo B.
- **Precondição:** Um departamento é retornado na busca de destinatário do despacho.
- **Passos:** 1. Ação: O resultado é exibido → Resultado esperado: O componente mostra o nome do departamento e a razão social da PJ, com o cluster aninhado sob a PJ à qual pertence.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `450`

### CT-008a Área de clique do accordion vs. seleção do departamento no despacho
- **Descrição:** CA02 — SGV-11184, grupo B. Defeito [[QA Workspace/02 Demandas/Concluídas/11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] (corrigido, aprovado em DEV em 03/09/2026).
- **Precondição:** O departamento é exibido como accordion no resultado da busca de destinatário do despacho.
- **Passos:** usa o shared step `accordion-click-area`.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `451`

### CT-009 Departamento é persistido como destinatário
- **Descrição:** CA03 — SGV-11184, grupo B.
- **Precondição:** Um departamento válido está selecionado no despacho.
- **Passos:** 1. Ação: O despacho é salvo ou enviado → Resultado esperado: O departamento é persistido como destinatário.
- **Pós-condição:** Departamento persistido como destinatário do despacho no banco.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `452`

### CT-011 Representação do departamento no PDF do despacho
- **Descrição:** CA05 — SGV-11184, grupo B. Mesmo formato do CT-005.
- **Precondição:** Um despacho tem um departamento como destinatário.
- **Passos:** 1. Ação: O PDF do documento/despacho é gerado → Resultado esperado: O destinatário é representado no mesmo formato definido pro campo pessoa (CT-005).
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `453`

### CT-012a Truncamento da linha do evento com múltiplos destinatários
- **Descrição:** CA05 — SGV-11184, grupo B. 🔴 Defeito [[QA Workspace/02 Demandas/DEV/11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]] **ainda aberto**.
- **Precondição:** A linha do evento de emissão (remetente + destinatários) tem um ou mais departamentos entre os destinatários.
- **Passos:** 1. Ação: A linha se aproxima de ~16px da data de emissão → Resultado esperado: O componente recebe status de truncate; em listas longas de destinatário, o texto sempre trunca na 2ª linha, mantendo a mesma sequência de string até o ponto de corte.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `454`

### CT-012b Retificação preserva o departamento selecionado como destinatário
- **Descrição:** CA05 — SGV-11184, grupo B. Formalizado a partir do defeito [[QA Workspace/02 Demandas/Concluídas/11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]] (corrigido, aprovado em DEV em 03/09/2026).
- **Precondição:** Um despacho foi emitido com um departamento como destinatário.
- **Passos:** 1. Ação: O servidor abre a tela de retificação desse despacho → Resultado esperado: O departamento aparece selecionado no campo de destinatário, sem ser substituído pelo cidadão PJ/empresa.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `455`

---

## C. Notificações

### CT-013 E-mail enviado ao endereço do departamento
- **Descrição:** CA01 — SGV-11184, grupo C.
- **Precondição:** Um documento ou despacho foi efetivamente encaminhado a um departamento.
- **Passos:** 1. Ação: A operação é concluída → Resultado esperado: Uma notificação por e-mail é enviada ao endereço do departamento.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `456`

### CT-015 Reprocessar o mesmo encaminhamento não duplica a notificação
- **Descrição:** CA03 — SGV-11184, grupo C.
- **Precondição:** Um encaminhamento ao departamento já foi processado e a notificação (e-mail e interna) já foi enviada.
- **Passos:** 1. Ação: Esse mesmo encaminhamento é processado de novo por retentativa do sistema (não uma nova ação do usuário) → Resultado esperado: O e-mail e a notificação interna não são enviados de novo pra quem já recebeu.
- **Pós-condição:** Nenhum e-mail/notificação duplicado persistido pra mesma combinação evento+canal+destinatário.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `457`

### CT-016 Conteúdo e link do e-mail
- **Descrição:** CA04 — SGV-11184, grupo C.
- **Precondição:** Um documento/despacho foi encaminhado a um departamento.
- **Passos:** 1. Ação: O e-mail é enviado → Resultado esperado: Reutiliza o template do evento e inclui identificação do documento, indicação de encaminhamento ao departamento, nome do departamento + razão social da PJ, remetente/resumo já previstos, e URL externa com `departmentId={publicIdentifier}`.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `458`

---

## D. Registro de visualização externa (rastreabilidade)

### CT-017 Departamento sempre tem publicIdentifier
- **Descrição:** CA01 — SGV-11184, grupo D (RF04).
- **Precondição:** Um departamento novo ou existente.
- **Passos:** 1. Ação: Seus dados são persistidos ou migrados → Resultado esperado: Ele possui um `publicIdentifier` UUID v4, único, imutável e não nulo.
- **Pós-condição:** `publicIdentifier` gravado no registro do departamento.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `459`

### CT-018 URL externa carrega o publicIdentifier, nunca o ID interno
- **Descrição:** CA02 — SGV-11184, grupo D. Nota: escopo é só o e-mail ao endereço do departamento (RF03 CA01) — "ou seus membros" foi removido do CT no vault por não ter base no requisito.
- **Precondição:** Uma notificação por e-mail é enviada ao departamento.
- **Passos:** 1. Ação: A URL externa é gerada → Resultado esperado: Contém `departmentId={publicIdentifier}` — nome do parâmetro mantido por compatibilidade, valor sempre o identificador público, nunca o ID numérico interno.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `460`

### CT-019 Validação completa do vínculo antes de qualquer registro
- **Descrição:** CA03 — SGV-11184, grupo D.
- **Precondição:** A URL contém um `departmentId`.
- **Passos:** 1. Ação: O usuário abre o documento → Resultado esperado: O backend valida o formato UUID, localiza o departamento por `publicIdentifier`, confirma instância, confirma o vínculo real com o documento (campo pessoa ou destinatário de despacho) e aplica as permissões externas já existentes — só então registra a interação.
- **Pós-condição:** Nenhum registro de interação até todas as validações passarem.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `461`

### CT-020 Interação registrada só após carregamento válido do conteúdo
- **Descrição:** CA04 — SGV-11184, grupo D.
- **Precondição:** Todas as validações foram aprovadas e o conteúdo principal do documento carregou com sucesso.
- **Passos:** 1. Ação: A visualização ocorre → Resultado esperado: É criada uma `DocumentInteraction` (referência ao documento, tipo visualização, `departmentId` interno resolvido, IP normalizado, demais metadados do modelo atual); requisições de assets, prévias, health checks e validações de URL não geram interação.
- **Pós-condição:** Registro `DocumentInteraction` persistido no banco.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `462`

### CT-021 Parâmetro ausente ou inválido não gera interação nem revela existência
- **Descrição:** CA05 — SGV-11184, grupo D.
- **Precondição:** O parâmetro está ausente, malformado, sem correspondência ou sem vínculo com o documento.
- **Passos:** 1. Ação: A URL é acessada (ou o documento é acessado por outro fluxo válido, no caso de ausência) → Resultado esperado: O sistema não registra interação de departamento; se malformado/sem vínculo, retorna a mesma resposta genérica de recurso indisponível, sem revelar a existência do departamento ou do documento.
- **Severidade / Tipo / Automação:** normal / acceptance / não automatizado
- **Qase id:** `463`

---

## Fora deste lote — marcados "Não se aplica" no vault, não criados na Qase

| CT | Motivo |
|---|---|
| CT-002a | Resultado do match já vem expandido, com cluster aninhado sob a PJ — depende do nível "participantes", não implementado nesta entrega |
| CT-002b | CPF de pessoa física lotada no departamento é anonimizado — mesmo motivo |
| CT-006 | Departamento invalidado antes do salvamento bloqueia a operação — cenário de corrida não reproduzido |
| CT-010 | Membros do departamento não são selecionáveis individualmente — depende do nível "participantes" |
| CT-012 | Departamento invalidado após seleção bloqueia o envio — cenário de corrida não reproduzido |
| CT-014 | Deduplicação de e-mail por endereço normalizado — cenário não reproduzido nesta rodada |
| CT-022 | Suspensão após encaminhamento não invalida o link histórico — depende do grupo D, ainda não testado |

## Ainda não subiu (fora de escopo deste lote)

- Os 33 CTs da [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083]] (Parte 1) — nenhum executado ainda.
- Os CTs próprios dos cards de defeito (SGV-11312, 11313, 11319, 11338, 11273) — hoje só existem como "Casos de Teste Básicos" dentro de cada card de defeito, não replicados aqui.

## Histórico desta preparação

- 2026-09-04 - 📤 21 casos criados na Qase (ids 443-463), sem `description`/`postconditions`, sem shared steps — Rafael sinalizou que ficou "cru".
- 2026-09-04 - 🔎 Desenhado o formato "rascunho→registro" e a skill [[Sistema/Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]] pra formalizar. Este arquivo reescrito no novo template, com `description`/`postconditions` preenchidos e 2 shared steps identificados (`busca-3-caracteres`, `accordion-click-area`) — próximo passo: aplicar via `update` na Qase.
- 2026-09-04 - ✅ Aplicado: 2 shared steps criados (hashes acima, confirmados via `--inspect`), `description`/`postconditions` aplicados nos 21 casos, e os 4 casos que compartilhavam mecânica (CT-002/CT-007, CT-002c/CT-008a) passaram a referenciar o shared step correspondente (`shared_step_hash` confirmado via `--inspect=444`). `corrections.json` agora guarda `id`/`hash` em cada entrada — reruns não duplicam. `status: enviado`.
