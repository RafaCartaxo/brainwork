---
prioridade: media
origem: repo
pontos_alocados: ""
---

# SGV-11184 — Departamentos: encaminhar documentos e despachos

**Ticket de origem:** SGV-11184 no Notion ("[Parte 2] Departamentos: Encaminhar documentos/despachos para o departamento")

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** DEV corrigir o defeito SGV-11338; executar os CTs ainda aguardando.

---

## Problema / contexto

Departamentos (SGV-11083) passam a poder ser selecionados como destinatários em documentos e despachos — no campo pessoa configurado pra Pessoa Jurídica, e no campo de destinatário de despacho. Ao serem efetivamente encaminhados, o departamento recebe notificação por e-mail (com deduplicação e idempotência), e o acesso externo ao documento via essa notificação é registrado com rastreabilidade (`publicIdentifier` UUID, validado contra o vínculo real com o documento) — sem nunca expor o ID interno nem autorizar responder/assinar pela URL.

Nasce do refinamento do requisito técnico do Notion.

## Objetivo

Departamento passa a ser selecionável como destinatário em documentos e despachos, com notificação por e-mail e rastreabilidade de visualização externa.

### Entrega desta capacidade

Grupos A-D abaixo (campo pessoa, destinatário de despacho, notificações, registro de visualização externa). Seleção de membro individual do departamento e departamento como signatário de assinatura ficam fora desta rodada (ver Fora de escopo).

---

## Decisões de produto

- Departamento só é selecionável como destinatário se estiver **ativo** e da **mesma instância** do documento/despacho; suspenso, excluído ou de outra instância não aparece na busca nem é aceito pela API.
- Seleção é sempre no nível do departamento — membros não aparecem nem são selecionáveis individualmente a partir dele (nem no campo pessoa, nem no destinatário de despacho).
- Um documento pode ter mais de um departamento (respeitando a multiplicidade já configurada no campo pessoa); o mesmo departamento não pode se repetir no mesmo campo/lista de destinatários.
- Toda persistência é revalidada pela API (configuração do campo, status, instância), independente da validação de interface; departamento invalidado entre a seleção e o salvamento/envio bloqueia a operação por inteiro, sem salvar/enviar parcialmente.
- PDF exibe o departamento como `Nome do departamento (Razão social da PJ)`, em documento e despacho (formato confirmado no Figma, complemento de 03/09/2026).
- Busca por departamento (campo pessoa e destinatário de despacho) só retorna resultado a partir de **3 caracteres digitados**, afunilando progressivamente conforme o servidor continua digitando.
- No accordion do departamento: a área de clique pra expandir/recolher é restrita ao ícone de chevron; selecionar o departamento como destinatário usa a linha inteira, do início do nome ao fim do container (mesma estética do hover de seleção já existente).
- Truncamento: se a linha do evento (remetente + destinatários) se aproximar de ~16px da data de emissão, o componente recebe status de truncate; em listas de destinatário longas (múltiplos departamentos/usuários), o texto sempre trunca na 2ª linha.
- E-mail é enviado ao endereço do departamento a cada encaminhamento efetivo, com deduplicação por endereço normalizado (case-insensitive) e idempotência por evento — reprocessar não duplica.
- Todo departamento tem `publicIdentifier` (UUID v4, único, imutável) — a URL externa da notificação carrega esse identificador, nunca o ID interno.
- Visualização externa via link do departamento é **somente leitura**: a presença do identificador na URL não autoriza responder, assinar ou qualquer ação protegida. Registro de interação só acontece depois de validar formato, instância, vínculo real com o documento e as permissões externas já existentes.
- Departamento suspenso **depois** de um encaminhamento não invalida o link já enviado — a suspensão só impede **novos** encaminhamentos.

---

## Escopo

- Selecionar departamento em campo pessoa de documento (grupo A).
- Selecionar departamento como destinatário de despacho (grupo B).
- Notificações por e-mail ao departamento (grupo C).
- Registro de visualização externa/rastreabilidade (grupo D).

---

## Fora de escopo

- **Exibição/seleção de participantes do departamento** (nível "Cidadão > PJ > Departamento > participantes") — confirmado por Rafael (03/09/2026): esta entrega cobre só o departamento em si. Por isso C2a, C2b e C10 (exibição de participantes/CPF no resultado da busca, seleção individual de membro) estão fora de escopo real, não são falha de execução. Isso vale só pra **exibição/seleção** — a notificação **interna** por membro elegível (CT-014 da SGV-11083) já é comportamento em escopo.
- **Seleção de membro individual do departamento como destinatário direto** e **departamento como signatário de assinatura** — conteúdo trazido pelo complemento do Figma (03/09/2026) que contradiz/excede o escopo fechado do requisito original; registrado como material da epic em [[QA Workspace/02 Demandas/DEV/SGV-9296 - Departamentos/Conhecimento/Complemento Figma - Departamento Destinatário E Signatário|Complemento Figma]], confirmado depois como a SGV-11177 (Parte 4).

---

## Critérios de aceite

### A. Selecionar departamento em campo pessoa de documento
- C1. Departamento só aparece como destinatário quando o campo pessoa está habilitado pra Pessoa Jurídica; desabilitado, nenhum departamento é exibido ou aceito. ^c1
- C2. Busca de departamentos retorna só os da mesma instância, a partir de 3 caracteres digitados, afunilando progressivamente; menos de 3 caracteres não retorna nada. ^c2
- C2a. Resultado do match já vem expandido, mostrando os participantes lotados, com o cluster aninhado sob a PJ. *(fora de escopo — ver Fora de escopo)* ^c2a
- C2b. CPF de pessoa física lotada no departamento é anonimizado na exibição do resultado expandido. *(fora de escopo — mesmo motivo do C2a)* ^c2b
- C2c. Área de clique do accordion (campo pessoa) distingue expandir/recolher (ícone de chevron) de selecionar o departamento (linha inteira). ^c2c
- C3. Vínculo entre documento, campo pessoa e departamento é persistido, e a API revalida configuração do campo, status e instância. ^c3
- C4. Multiplicidade do campo é respeitada e duplicidade do mesmo departamento é bloqueada. ^c4
- C5. PDF representa o departamento como "Nome do departamento (Razão social da PJ)", com parênteses. ^c5
- C6. Departamento invalidado (suspenso/excluído) antes do salvamento bloqueia a operação por inteiro, sem salvar parcialmente. *(não reproduzido nesta rodada — cenário de corrida)* ^c6

### B. Selecionar departamento como destinatário de despacho
- C7. Busca no campo de destinatário do despacho retorna departamentos ativos da mesma instância, a partir de 3 caracteres digitados. ^c7
- C8. Resultado da busca no despacho mostra nome do departamento e razão social da PJ, com o cluster aninhado sob ela. ^c8
- C8a. Área de clique do accordion (destinatário de despacho) distingue expandir/recolher de selecionar, mesma regra do C2c. ^c8a
- C9. Departamento é persistido como destinatário do despacho. ^c9
- C10. Membros do departamento não são selecionáveis individualmente no destinatário de despacho. *(fora de escopo — mesmo motivo do C2a)* ^c10
- C11. PDF do despacho representa o departamento no mesmo formato definido pro campo pessoa (C5). ^c11
- C12. Departamento invalidado após a seleção bloqueia o envio do despacho por inteiro, sem disparar notificação. *(não reproduzido nesta rodada — cenário de corrida)* ^c12
- C12a. Linha do evento de emissão com destinatário de nome extenso sempre trunca na 2ª linha, nunca já na 1ª. ^c12a
- C12b. Retificação de despacho preserva o departamento selecionado como destinatário, sem substituí-lo pelo cidadão PJ/empresa. ^c12b

### C. Notificações
- C13. E-mail é enviado ao endereço do departamento a cada encaminhamento efetivamente concluído. ^c13
- C14. E-mail é enviado apenas uma vez por endereço normalizado quando departamento e membro compartilham o mesmo endereço — sem duplicar; notificação interna por membro continua sendo criada à parte. *(cenário não reproduzido nesta rodada)* ^c14
- C15. Reprocessar o mesmo encaminhamento (retentativa do sistema) não duplica a notificação, nem e-mail nem interna. ^c15
- C16. E-mail reutiliza o template do evento, identifica o documento e o departamento, e inclui URL externa com `departmentId={publicIdentifier}`. ^c16

### D. Registro de visualização externa (rastreabilidade)
- C17. Todo departamento, novo ou existente, possui `publicIdentifier` UUID v4 único, imutável e não nulo. ^c17
- C18. URL externa gerada pela notificação sempre carrega o `publicIdentifier`, nunca o ID numérico interno. ^c18
- C19. Backend valida formato UUID, instância, vínculo real com o documento e as permissões externas já existentes antes de registrar qualquer interação. ^c19
- C20. `DocumentInteraction` só é registrada após todas as validações passarem e o conteúdo principal carregar com sucesso; requisições de assets/prévias/health checks não geram interação. ^c20
- C21. Parâmetro ausente, malformado ou sem vínculo não gera interação nem revela a existência do departamento ou do documento. ^c21
- C22. Suspensão do departamento após um encaminhamento não invalida o link histórico já enviado — só impede novos encaminhamentos. *(depende do grupo D, ainda não testado)* ^c22

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Confirmar `prioridade` e `pontos_alocados`.
- Depende funcionalmente da SGV-11083 (departamento precisa existir e ter participantes/status antes de ser encaminhável).
- Ainda não existe seção de "Departamentos" em `04 Conhecimento/Módulos/` — pendência de criar/atualizar quando esta demanda (e a 11083) forem validadas.

> [!bug] Defeitos confirmados em validação real (03-04/09/2026)
> - [[Defeitos/SGV-11312 - Defeito Area De Clique Do Accordion De Departamento Nao Segue O Figma|SGV-11312]] (C2c/C8a) — área de clique do accordion não respeitava a distinção chevron × linha. **Corrigido e aprovado em DEV.**
> - [[Defeitos/SGV-11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]] (achado em teste exploratório, formalizado como C12b) — departamento não era persistido ao retificar despacho (tela mostrava o cidadão PJ/empresa). **Corrigido e aprovado em DEV.**
> - [[Defeitos/SGV-11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]] (C12a) — truncamento de destinatário com nome extenso não segue o protótipo (campo de busca sem limite; despacho trunca já na 1ª linha). **Ainda aberto, aguardando DEV.**
