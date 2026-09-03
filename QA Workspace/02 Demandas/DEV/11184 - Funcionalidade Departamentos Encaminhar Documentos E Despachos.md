---
tags:
  - demanda
  - funcionalidade
  - qa
  - servicos-pj
task: "11184"
pai: ""
status: aberto
ambiente: DEV
prioridade: media
data_inicio: 2026-09-03
data_fim: ""
responsavel: Rafael
aguardando: ""
pontos: ""
modulo: servicos-pj
---
# Demanda: [Funcionalidade] Departamentos — encaminhar documentos e despachos

> [!info] Informações
> - **Tipo:** Funcionalidade
> - **Responsável QA:** Rafael
> - **Link:** SGV-11184 no Notion ("[Parte 2] Departamentos: Encaminhar documentos/despachos para o departamento")
> - **Parte 2** de duas, irmã de [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083 (Parte 1)]] — ambas sob a epic [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/0 - SGV-9296 - Índice|SGV-9296]]

---

> [!abstract] Resumo

Departamentos (SGV-11083) passam a poder ser selecionados como destinatários em documentos e despachos — no campo pessoa configurado pra Pessoa Jurídica, e no campo de destinatário de despacho. Ao serem efetivamente encaminhados, o departamento recebe notificação por e-mail (com deduplicação e idempotência), e o acesso externo ao documento via essa notificação é registrado com rastreabilidade (`publicIdentifier` UUID, validado contra o vínculo real com o documento) — sem nunca expor o ID interno nem autorizar responder/assinar pela URL.

Nasce do refinamento do requisito técnico do Notion — mesa em [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11184/2 - SGV-11184 - Refinamento Departamentos Encaminhar Documentos E Despachos|04 Conhecimento/Tasks/SGV-9296/SGV-11184]]. Resumo em linguagem simples (sem jargão de RF/CA): [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11184/1 - SGV-11184 - Resumo|SGV-11184 - Resumo]].

---

## Regras de negócio

- Departamento só é selecionável como destinatário se estiver **ativo** e da **mesma instância** do documento/despacho; suspenso, excluído ou de outra instância não aparece na busca nem é aceito pela API.
- Seleção é sempre no nível do departamento — membros não aparecem nem são selecionáveis individualmente a partir dele (nem no campo pessoa, nem no destinatário de despacho).
- Um documento pode ter mais de um departamento (respeitando a multiplicidade já configurada no campo pessoa); o mesmo departamento não pode se repetir no mesmo campo/lista de destinatários.
- Toda persistência é revalidada pela API (configuração do campo, status, instância), independente da validação de interface; departamento invalidado entre a seleção e o salvamento/envio bloqueia a operação por inteiro, sem salvar/enviar parcialmente.
- PDF exibe o departamento como `{Nome do departamento} — {Razão social da PJ}`, em documento e despacho.
- E-mail é enviado ao endereço do departamento a cada encaminhamento efetivo, com deduplicação por endereço normalizado (case-insensitive) e idempotência por evento — reprocessar não duplica.
- Todo departamento tem `publicIdentifier` (UUID v4, único, imutável) — a URL externa da notificação carrega esse identificador, nunca o ID interno.
- Visualização externa via link do departamento é **somente leitura**: a presença do identificador na URL não autoriza responder, assinar ou qualquer ação protegida. Registro de interação só acontece depois de validar formato, instância, vínculo real com o documento e as permissões externas já existentes.
- Departamento suspenso **depois** de um encaminhamento não invalida o link já enviado — a suspensão só impede **novos** encaminhamentos.

---

> [!warning] Pontos de atenção
> - Nenhum ponto em aberto pendente de decisão do Produto (diferente da SGV-11083) — o requisito veio completo.
> - **CA05** (formato de exibição no PDF, grupos A e B abaixo): o texto já define `{Nome} — {Razão Social}`, mas a task pede conferir o formato exato no Figma — é validação visual de detalhe na hora do teste, não uma decisão em aberto.
> - Mesmo gate de doc da SGV-11083: não existe seção de "Departamentos" em `04 Conhecimento/Módulos/` ainda — pendência de criar/atualizar a doc quando esta demanda (e a 11083) forem validadas (fluxo 8).

---

## Casos de teste

### A. Selecionar departamento em campo pessoa de documento

#### **CT-001 Departamento só aparece com Pessoa Jurídica habilitada no campo** *(CA01)*

**Dado** que um campo pessoa está configurado pra aceitar Pessoa Jurídica
**Quando** o servidor pesquisa um destinatário
**Então** a busca inclui departamentos ativos vinculados a cidadãos PJ; com a configuração desabilitada, nenhum departamento é exibido ou aceito

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Busca de departamentos por nome ou razão social, só da mesma instância** *(CA02)*

**Dado** que a busca de departamentos está habilitada no campo
**Quando** o servidor informa parte do nome do departamento ou a razão social da PJ
**Então** o sistema retorna os departamentos correspondentes do mesmo cliente/instância, exibindo nome do departamento e razão social da PJ em cada resultado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-003 Vínculo é persistido e revalidado pela API** *(CA03)*

**Dado** que o servidor selecionou um departamento válido no campo pessoa
**Quando** salva o documento
**Então** o vínculo entre documento, campo pessoa e departamento é persistido, e a API revalida a configuração do campo, o status do departamento e a instância, independente da validação da interface

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-004 Multiplicidade do campo é respeitada e duplicidade é bloqueada** *(CA04)*

**Dado** um campo pessoa de seleção única ou múltipla
**Quando** o servidor seleciona departamentos
**Então** o sistema respeita a multiplicidade configurada e impede repetir o mesmo departamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005 Representação do departamento no PDF do documento** *(CA05)*

**Dado** que o documento tem um departamento num campo pessoa
**Quando** o PDF é gerado ou regenerado
**Então** o valor aparece no formato "Nome do departamento — Razão social da PJ" (conferir formato exato no Figma)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-006 Departamento invalidado antes do salvamento bloqueia a operação** *(CA06)*

**Dado** que um departamento selecionado foi suspenso, excluído ou movido pra condição inválida antes da confirmação
**Quando** o documento é salvo
**Então** a operação é recusada por inteiro, com aviso de que o departamento não está mais disponível, sem salvar parcialmente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Selecionar departamento como destinatário de despacho

#### **CT-007 Busca no campo de destinatário do despacho** *(CA01)*

**Dado** que um servidor está criando ou editando um despacho
**Quando** pesquisa no campo de destinatário
**Então** o sistema retorna departamentos ativos do mesmo cliente/instância, por nome ou razão social da PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-008 Apresentação do resultado no componente** *(CA02)*

**Dado** que um departamento é retornado na busca de destinatário do despacho
**Quando** o resultado é exibido
**Então** o componente mostra o nome do departamento e a razão social da PJ

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-009 Departamento é persistido como destinatário** *(CA03)*

**Dado** que um departamento válido está selecionado no despacho
**Quando** o despacho é salvo ou enviado
**Então** o departamento é persistido como destinatário

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-010 Membros do departamento não são selecionáveis individualmente** *(CA04)*

**Dado** que um departamento com membros é selecionado no destinatário do despacho
**Quando** o servidor abre a busca ou seleciona o departamento
**Então** os membros não são expandidos, sugeridos nem adicionados como destinatários individuais

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-011 Representação do departamento no PDF do despacho** *(CA05)*

**Dado** que um despacho tem um departamento como destinatário
**Quando** o PDF do documento/despacho é gerado
**Então** o destinatário é representado no mesmo formato definido pro campo pessoa (CT-005)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-012 Departamento invalidado após seleção bloqueia o envio** *(CA06)*

**Dado** que o departamento selecionado no despacho se tornou inválido após a seleção
**Quando** o servidor envia o despacho
**Então** o envio é bloqueado por inteiro e nenhuma notificação é disparada

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### C. Notificações

#### **CT-013 E-mail enviado ao endereço do departamento** *(CA01)*

**Dado** que um documento ou despacho foi efetivamente encaminhado a um departamento
**Quando** a operação é concluída
**Então** uma notificação por e-mail é enviada ao endereço do departamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-014 Deduplicação de e-mail por endereço normalizado** *(CA02)*

**Dado** que o endereço do departamento também pertence a um membro, ou dois membros compartilham o mesmo endereço
**Quando** os destinatários de e-mail são montados
**Então** é enviado apenas um e-mail por endereço normalizado (sem diferenciar maiúsculas/minúsculas); a notificação interna continua sendo criada uma vez por membro elegível

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-015 Idempotência no reprocessamento do evento** *(CA03)*

**Dado** que o processamento de uma notificação seja repetido
**Quando** o mesmo evento é consumido novamente
**Então** o sistema não duplica e-mails nem notificações internas pra mesma combinação de evento, canal e destinatário

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-016 Conteúdo e link do e-mail** *(CA04)*

**Dado** que um documento/despacho foi encaminhado a um departamento
**Quando** o e-mail é enviado
**Então** ele reutiliza o template do evento e inclui identificação do documento, indicação de encaminhamento ao departamento, nome do departamento + razão social da PJ, remetente/resumo já previstos, e URL externa com `departmentId={publicIdentifier}`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Registro de visualização externa (rastreabilidade)

#### **CT-017 Departamento sempre tem publicIdentifier** *(CA01)*

**Dado** um departamento novo ou existente
**Quando** seus dados são persistidos ou migrados
**Então** ele possui um `publicIdentifier` UUID v4, único, imutável e não nulo

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-018 URL externa carrega o publicIdentifier, nunca o ID interno** *(CA02)*

**Dado** que uma notificação é enviada para o departamento ou seus membros
**Quando** a URL externa é gerada
**Então** ela contém `departmentId={publicIdentifier}` — o nome do parâmetro é mantido por compatibilidade, mas o valor é sempre o identificador público, nunca o ID numérico interno

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-019 Validação completa do vínculo antes de qualquer registro** *(CA03)*

**Dado** que a URL contém um `departmentId`
**Quando** o usuário abre o documento
**Então** o backend valida o formato UUID, localiza o departamento por `publicIdentifier`, confirma que pertence à mesma instância do documento, confirma o vínculo real com o documento (campo pessoa ou destinatário de despacho) e aplica as permissões externas já existentes — só então registra a interação

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-020 Interação registrada só após carregamento válido do conteúdo** *(CA04)*

**Dado** que todas as validações foram aprovadas e o conteúdo principal do documento carregou com sucesso
**Quando** a visualização ocorre
**Então** é criada uma `DocumentInteraction` (referência ao documento, tipo visualização, `departmentId` interno resolvido, IP normalizado, demais metadados do modelo atual); requisições de assets, prévias, health checks e validações de URL não geram interação

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-021 Parâmetro ausente ou inválido não gera interação nem revela existência** *(CA05)*

**Dado** que o parâmetro está ausente, malformado, sem correspondência ou sem vínculo com o documento
**Quando** a URL é acessada (ou o documento é acessado por outro fluxo válido, no caso de ausência)
**Então** o sistema não registra interação de departamento; se o parâmetro for malformado/sem vínculo, retorna a mesma resposta genérica de recurso indisponível, sem revelar a existência do departamento ou do documento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-022 Suspensão após encaminhamento não invalida o link histórico** *(CA06)*

**Dado** que o departamento foi suspenso depois de receber o documento
**Quando** uma URL anteriormente enviada é acessada
**Então** o vínculo histórico continua válido para visualização e registro da interação — a suspensão impede apenas novos encaminhamentos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Fora de execução — registro

*Só preencher quando algum CT acima for retirado/adiado desta rodada.*

| Caso | Decisão | Motivo |
|---|---|---|
|  |  |  |

---

> [!danger] Bugs encontrados

---

## Evidências

Nenhuma anexada ainda — funcionalidade ainda não implementada (backlog no Notion).

---

> [!tip] Observações

- Refinado a partir do requisito técnico do Notion — análise completa em [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11184/2 - SGV-11184 - Refinamento Departamentos Encaminhar Documentos E Despachos|04 Conhecimento/Tasks/SGV-9296/SGV-11184]].
- Depende funcionalmente da SGV-11083 (departamento precisa existir e ter participantes/status antes de ser encaminhável) — validar a 11083 primeiro, ou pelo menos em paralelo com dados de teste compatíveis.
- Gate de doc: não existe seção de "Departamentos" em `04 Conhecimento/Módulos/` ainda — importar quando esta demanda (e a 11083) forem validadas (fluxo 8).

---

## Histórico

- 2026-09-03 - 📝 Funcionalidade refinada (critérios de aceite prontos) — refinamento do requisito técnico do Notion, cruzado com o doc de produto consolidado ("Departamento CNPJ")
