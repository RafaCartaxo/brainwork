---
tags:
  - qa
  - qase
tipo: referencia
data_envio: 2026-09-04
---
# Casos enviados pra Qase: Departamentos — encaminhar documentos e despachos

Espelho legível do que foi enviado em 04/09/2026 (`sogov-automation-test/scripts/qase-sync-9296-departamentos/`) pro projeto `SGV` na Qase, suite **220** ("9296 - Possibilidade de Cadastrar Contato/Departamento sem CPF/CNPJ"). Fonte: [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]]. Cada caso abaixo já existe na Qase com o `id` indicado — confira em https://app.qase.io/project/SGV?suite=220.

21 dos 28 CTs do card (7 ficaram de fora, marcados "Não se aplica" — ver seção no fim).

---

## A. Selecionar departamento em campo pessoa de documento

### id 443 — CT-001 Departamento só aparece com Pessoa Jurídica habilitada no campo
- **Precondição:** Um campo pessoa está configurado pra aceitar Pessoa Jurídica.
- **Passo 1** — Ação: O servidor pesquisa um destinatário. Resultado esperado: A busca inclui departamentos ativos vinculados a cidadãos PJ; com a configuração desabilitada, nenhum departamento é exibido ou aceito.

### id 444 — CT-002 Busca de departamentos por nome ou razão social, só da mesma instância
- **Precondição:** A busca de departamentos está habilitada no campo.
- **Passo 1** — Ação: O servidor informa parte do nome do departamento ou a razão social da PJ, a partir de 3 caracteres digitados. Resultado esperado: O sistema retorna os departamentos correspondentes do mesmo cliente/instância, afunilando o resultado a cada caractere digitado, exibindo nome do departamento e razão social da PJ em cada resultado; com menos de 3 caracteres, nenhum resultado é retornado.

### id 445 — CT-002c Área de clique do accordion vs. seleção do departamento
- **Precondição:** O departamento é exibido como accordion no resultado da busca.
- **Passo 1** — Ação: O servidor clica no ícone de chevron. Resultado esperado: O accordion expande ou recolhe, mostrando/ocultando os participantes.
- **Passo 2** — Ação: O servidor clica em qualquer outro ponto da linha do departamento (do início do nome ao fim do container). Resultado esperado: O departamento é selecionado como destinatário, com a mesma estética de hover de seleção já existente — a expansão do accordion não interfere na seleção, e vice-versa.
- ⚠️ *Nota: defeito [[QA Workspace/02 Demandas/Concluídas/11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] (corrigido, aprovado em DEV em 03/09/2026).*

### id 446 — CT-003 Vínculo é persistido e revalidado pela API
- **Precondição:** O servidor selecionou um departamento válido no campo pessoa.
- **Passo 1** — Ação: Salva o documento. Resultado esperado: O vínculo entre documento, campo pessoa e departamento é persistido, e a API revalida a configuração do campo, o status do departamento e a instância, independente da validação da interface.

### id 447 — CT-004 Multiplicidade do campo é respeitada e duplicidade é bloqueada
- **Precondição:** Um campo pessoa de seleção única ou múltipla.
- **Passo 1** — Ação: O servidor seleciona departamentos. Resultado esperado: O sistema respeita a multiplicidade configurada e impede repetir o mesmo departamento.

### id 448 — CT-005 Representação do departamento no PDF do documento
- **Precondição:** O documento tem um departamento num campo pessoa.
- **Passo 1** — Ação: O PDF é gerado ou regenerado. Resultado esperado: O valor aparece no formato "Nome do departamento (Razão social da PJ)", com parênteses (formato confirmado no Figma).

---

## B. Selecionar departamento como destinatário de despacho

### id 449 — CT-007 Busca no campo de destinatário do despacho
- **Precondição:** Um servidor está criando ou editando um despacho.
- **Passo 1** — Ação: Pesquisa no campo de destinatário informando ao menos 3 caracteres. Resultado esperado: O sistema retorna departamentos ativos do mesmo cliente/instância, por nome ou razão social da PJ, afunilando o resultado a cada caractere digitado; com menos de 3 caracteres, nenhum resultado é retornado.

### id 450 — CT-008 Apresentação do resultado no componente
- **Precondição:** Um departamento é retornado na busca de destinatário do despacho.
- **Passo 1** — Ação: O resultado é exibido. Resultado esperado: O componente mostra o nome do departamento e a razão social da PJ, com o cluster aninhado sob a PJ à qual pertence.

### id 451 — CT-008a Área de clique do accordion vs. seleção do departamento no despacho
- **Precondição:** O departamento é exibido como accordion no resultado da busca de destinatário do despacho.
- **Passo 1** — Ação: O servidor clica no ícone de chevron. Resultado esperado: O accordion expande ou recolhe os participantes.
- **Passo 2** — Ação: Clica em qualquer outro ponto da linha do departamento. Resultado esperado: O departamento é selecionado como destinatário, com a mesma estética de hover de seleção já existente.
- ⚠️ *Nota: defeito [[QA Workspace/02 Demandas/Concluídas/11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] (corrigido, aprovado em DEV em 03/09/2026).*

### id 452 — CT-009 Departamento é persistido como destinatário
- **Precondição:** Um departamento válido está selecionado no despacho.
- **Passo 1** — Ação: O despacho é salvo ou enviado. Resultado esperado: O departamento é persistido como destinatário.

### id 453 — CT-011 Representação do departamento no PDF do despacho
- **Precondição:** Um despacho tem um departamento como destinatário.
- **Passo 1** — Ação: O PDF do documento/despacho é gerado. Resultado esperado: O destinatário é representado no mesmo formato definido pro campo pessoa (CT-005).

### id 454 — CT-012a Truncamento da linha do evento com múltiplos destinatários
- **Precondição:** A linha do evento de emissão (remetente + destinatários) tem um ou mais departamentos entre os destinatários.
- **Passo 1** — Ação: A linha se aproxima de ~16px da data de emissão. Resultado esperado: O componente recebe status de truncate; em listas longas de destinatário (múltiplos departamentos ou usuários lotados), o texto sempre trunca na 2ª linha, mantendo a mesma sequência de string até o ponto de corte.
- 🔴 *Nota: reprovado — defeito [[QA Workspace/02 Demandas/DEV/11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]] **ainda aberto** (departamento de nome extenso: campo de busca cresce sem limite; despacho trunca já na 1ª linha, não na 2ª).*

### id 455 — CT-012b Retificação preserva o departamento selecionado como destinatário
- **Precondição:** Um despacho foi emitido com um departamento como destinatário.
- **Passo 1** — Ação: O servidor abre a tela de retificação desse despacho. Resultado esperado: O departamento aparece selecionado no campo de destinatário, sem ser substituído pelo cidadão PJ/empresa.
- ⚠️ *Nota: formalizado a partir do defeito [[QA Workspace/02 Demandas/Concluídas/11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]] (corrigido, aprovado em DEV em 03/09/2026).*

---

## C. Notificações

### id 456 — CT-013 E-mail enviado ao endereço do departamento
- **Precondição:** Um documento ou despacho foi efetivamente encaminhado a um departamento.
- **Passo 1** — Ação: A operação é concluída. Resultado esperado: Uma notificação por e-mail é enviada ao endereço do departamento.

### id 457 — CT-015 Reprocessar o mesmo encaminhamento não duplica a notificação
- **Precondição:** Um encaminhamento ao departamento já foi processado e a notificação (e-mail e interna) já foi enviada.
- **Passo 1** — Ação: Esse mesmo encaminhamento é processado de novo por retentativa do sistema (não uma nova ação do usuário). Resultado esperado: O e-mail e a notificação interna não são enviados de novo pra quem já recebeu.

### id 458 — CT-016 Conteúdo e link do e-mail
- **Precondição:** Um documento/despacho foi encaminhado a um departamento.
- **Passo 1** — Ação: O e-mail é enviado. Resultado esperado: Reutiliza o template do evento e inclui identificação do documento, indicação de encaminhamento ao departamento, nome do departamento + razão social da PJ, remetente/resumo já previstos, e URL externa com `departmentId={publicIdentifier}`.

---

## D. Registro de visualização externa (rastreabilidade)

### id 459 — CT-017 Departamento sempre tem publicIdentifier
- **Precondição:** Um departamento novo ou existente.
- **Passo 1** — Ação: Seus dados são persistidos ou migrados. Resultado esperado: Ele possui um `publicIdentifier` UUID v4, único, imutável e não nulo.

### id 460 — CT-018 URL externa carrega o publicIdentifier, nunca o ID interno
- **Precondição:** Uma notificação por e-mail é enviada ao departamento.
- **Passo 1** — Ação: A URL externa é gerada. Resultado esperado: Contém `departmentId={publicIdentifier}` — o nome do parâmetro é mantido por compatibilidade, mas o valor é sempre o identificador público, nunca o ID numérico interno.

### id 461 — CT-019 Validação completa do vínculo antes de qualquer registro
- **Precondição:** A URL contém um `departmentId`.
- **Passo 1** — Ação: O usuário abre o documento. Resultado esperado: O backend valida o formato UUID, localiza o departamento por `publicIdentifier`, confirma que pertence à mesma instância do documento, confirma o vínculo real com o documento (campo pessoa ou destinatário de despacho) e aplica as permissões externas já existentes — só então registra a interação.

### id 462 — CT-020 Interação registrada só após carregamento válido do conteúdo
- **Precondição:** Todas as validações foram aprovadas e o conteúdo principal do documento carregou com sucesso.
- **Passo 1** — Ação: A visualização ocorre. Resultado esperado: É criada uma `DocumentInteraction` (referência ao documento, tipo visualização, `departmentId` interno resolvido, IP normalizado, demais metadados do modelo atual); requisições de assets, prévias, health checks e validações de URL não geram interação.

### id 463 — CT-021 Parâmetro ausente ou inválido não gera interação nem revela existência
- **Precondição:** O parâmetro está ausente, malformado, sem correspondência ou sem vínculo com o documento.
- **Passo 1** — Ação: A URL é acessada (ou o documento é acessado por outro fluxo válido, no caso de ausência). Resultado esperado: O sistema não registra interação de departamento; se o parâmetro for malformado/sem vínculo, retorna a mesma resposta genérica de recurso indisponível, sem revelar a existência do departamento ou do documento.

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

## Referência técnica

Payload/script: `sogov-automation-test/scripts/qase-sync-9296-departamentos/` (`corrections.json`, `sync.js`, `README.md`) — repositório separado do vault.
