---
tags:
  - qa
  - refinamento
task: "11184"
status: refinado
data_inicio: 2026-09-03
responsavel: Rafael
modulo: servicos-pj
---
# Refinamento: Departamentos — encaminhar documentos e despachos

> [!info]- Mesa de trabalho — [[Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada|fluxo 6]]
> Análise e suposição vivem aqui — o card em `02 Demandas/` nasce do **Destilado**, limpo. Ao concluir: análise → Notion (`📤`), card criado (`📝`), este arquivo → `04 Conhecimento/` (`status: refinado`).
>
> **Parte 2** de duas — irmã de [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11083/2 - SGV-11083 - Refinamento Departamentos Para Cidadao PJ|SGV-11083 (Parte 1)]], sob a mesma epic pai [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/0 - SGV-9296 - Índice|SGV-9296]].

## O problema (task no Notion)

**Descrição** — [Parte 2] Departamentos: Encaminhar documentos/despachos para o departamento (SGV-11184, backlog "[Dev][Parte 2] Encaminhamento").

**Objetivo** — Permitir que departamentos (SGV-11083) sejam selecionados como destinatários em documentos e despachos, recebam as notificações correspondentes e tenham suas visualizações externas registradas com rastreabilidade. A seleção direta de um membro do departamento **não** faz parte desta entrega — só o departamento como um todo.

**Escopo e premissas fechadas** (já batidas na task, não são pontos em aberto):
- Departamento só é selecionável se estiver **ativo** e da **mesma instância** do documento/despacho.
- Seleção é no nível do departamento — membros não aparecem como opções individuais.
- Um documento pode ter mais de um departamento (respeitando a multiplicidade já configurada no campo pessoa); o mesmo departamento não pode se repetir no mesmo campo/lista.
- Departamento suspenso, excluído ou de outra instância não aparece na busca nem é aceito pela API.
- Figma é referência visual — o formato de exibição (CA05) foi confirmado por ele quando o texto original ficou em aberto; demais divergências de escopo (fora do que já está fechado acima) não entram automaticamente, exigem confirmação.
- Visualização externa é **somente leitura**; o identificador do departamento na URL não autoriza responder, assinar ou qualquer ação protegida.

### RF01 — Selecionar departamento em campo pessoa de documento

Como servidor, quero selecionar um departamento num campo pessoa configurado pra aceitar Pessoa Jurídica, pra encaminhar o documento ao setor correto da empresa.

**Critérios de aceitação (CA01-CA06):**
- CA01 — Departamento só aparece na busca se o campo pessoa tiver "Pessoa Jurídica" habilitado; desabilitado, nenhum departamento é exibido/aceito
- CA02 — Busca por nome do departamento ou razão social da PJ, sempre limitada à instância atual; cada resultado mostra nome do departamento + razão social
- CA03 — Ao salvar, o vínculo documento↔campo↔departamento é persistido; a API revalida configuração do campo, status do departamento e instância, independente da validação de interface
- CA04 — Respeita a multiplicidade configurada do campo (único/múltiplo) e impede repetir o mesmo departamento
- CA05 — No PDF, o departamento aparece como `Nome do departamento (Razão social da PJ)`, com parênteses (formato confirmado no complemento do Figma, 03/09/2026)
- CA06 — Se o departamento for invalidado (suspenso/excluído) entre a seleção e o salvamento, a operação é recusada por inteiro, sem salvar parcialmente, com aviso de que não está mais disponível

### RF02 — Selecionar departamento como destinatário de despacho

Como servidor, quero selecionar um departamento como destinatário de despacho, pra encaminhar a comunicação ao setor responsável da PJ.

**Critérios de aceitação (CA01-CA06):**
- CA01 — Busca no campo de destinatário do despacho retorna departamentos ativos da instância atual, por nome ou razão social
- CA02 — Resultado exibe nome do departamento + razão social
- CA03 — Departamento válido selecionado é persistido como destinatário ao salvar/enviar
- CA04 — Membros do departamento não são expandidos, sugeridos nem adicionáveis individualmente a partir dele
- CA05 — Representação no PDF segue o mesmo formato do RF01
- CA06 — Se o departamento virar inválido depois de selecionado, o envio é bloqueado por inteiro e nenhuma notificação é disparada

### RF03 — Notificar departamento e membros

Como integrante de um departamento destinatário, quero ser notificado sobre documentos/despachos encaminhados ao setor, pra saber da tramitação.

**Critérios de aceitação (CA01-CA04):**
- CA01 — E-mail enviado ao endereço do departamento sempre que um documento/despacho é efetivamente encaminhado a ele
- CA02 — Deduplicação: um só e-mail por endereço normalizado (case-insensitive), mesmo se o endereço do departamento coincidir com o de um membro, ou dois membros compartilharem endereço; notificação interna continua uma por membro elegível
- CA03 — Idempotência: reprocessar o mesmo evento não duplica e-mail nem notificação interna pra mesma combinação evento+canal+destinatário
- CA04 — E-mail reaproveita o template do evento e inclui: identificação do documento, indicação de que foi encaminhado ao departamento, nome do departamento + razão social, remetente/resumo já previstos, e URL externa com `departmentId={publicIdentifier}`

### RF04 — Registrar visualização externa do departamento (rastreabilidade)

Como responsável pela rastreabilidade, quero registrar quando um documento encaminhado a um departamento for visualizado via notificação, pra manter evidência do acesso externo.

**Critérios de aceitação (CA01-CA06):**
- CA01 — Todo departamento (novo ou existente) tem `publicIdentifier` UUID v4, único, imutável, não nulo
- CA02 — URL externa da notificação carrega `departmentId={publicIdentifier}` (nome do parâmetro mantido por compatibilidade, valor é o identificador público, nunca o ID interno)
- CA03 — Ao abrir a URL, o backend valida (nessa ordem): formato UUID → localiza por `publicIdentifier` → confirma mesma instância do documento → confirma vínculo do departamento ao documento (campo pessoa ou destinatário de despacho) → aplica permissões externas existentes → só então registra a interação
- CA04 — Passando todas as validações e carregado o conteúdo principal, cria uma `DocumentInteraction` (referência ao documento, tipo "visualização", `departmentId` interno resolvido, IP normalizado, demais metadados já exigidos). Cada carregamento válido = uma interação; asset/prévia/health-check/validação de URL não geram interação
- CA05 — Parâmetro ausente → segue o comportamento atual, sem interação de departamento. Parâmetro malformado/sem correspondência/sem vínculo → resposta genérica de recurso indisponível, sem revelar existência do departamento/documento, sem registrar interação
- CA06 — Departamento suspenso **depois** do encaminhamento: o vínculo histórico continua válido pra visualização/registro — a suspensão só impede **novos** encaminhamentos

---

## Análise

- **Fonte**: só o requisito técnico bruto desta vez (sem "Resumo" pré-simplificado, diferente da SGV-11083). Schema Prisma (`Department.publicIdentifier`, `DocumentInteraction.ip`/`departmentId`) e Tarefas técnicas de dev removidos do Destilado por não serem QA — ficam só aqui como contexto se precisar.
- **Cruzamento com o doc de produto consolidado** ("Departamento CNPJ", mesmo usado na SGV-11083) — seção "Departamentos na tramitação": confirma que a busca de destinatário na abertura de documento mostra a árvore completa (cidadãos PF/PJ + departamentos + participantes com cargo + servidores), que a emissão depois de escolhido o destinatário é idêntica à atual (sem notificação na abertura em si — só no encaminhamento efetivo, que bate com RF03), e que despachos mostram "destinatário com contexto (departamento — empresa)" — reforça o formato de exibição do RF01 CA05/RF02 CA05.
- **CA05 resolvido com o complemento do Figma** (recebido 03/09/2026, `~/Documentos/Complemento 11184.txt`): formato de exibição é `Nome (Razão Social)` — parênteses, não o travessão do texto original do requisito. Complemento trouxe também detalhes de UX sem contradição aparente com o escopo já fechado (busca a partir de 3 caracteres, cluster aninhado sob a PJ, área de clique do accordion restrita ao chevron, regra de truncate a ~16px da data e truncamento sempre na 2ª linha) — incorporados aos CTs do card. A parte de **resultado expandido mostrando participantes + CPF anonimizado** foi incorporada nessa rodada, mas **revertida em seguida** (ver bullet abaixo) — não fazia parte do escopo real.
- **Conteúdo do complemento fora do escopo desta entrega, não incorporado**: (1) seleção de membro individual do departamento como destinatário direto — contradiz a premissa fechada do RF01 ("seleção direta de membro não faz parte desta entrega"); Rafael vai conferir e confirmar se é mudança de escopo ou parte futura da epic; (2) departamento como signatário de solicitação de assinatura (com selos e strings de notificação próprias) — não existe no requisito original, que cobre só tramitação (documento/despacho), não assinatura. Ambos os pontos preservados como material de referência da epic em [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/Complemento Figma - Departamento Destinatário E Signatário|Tasks/SGV-9296]], sem entrar no Destilado/CTs abaixo.
- **Escopo confirmado por Rafael (03/09/2026), validando os CTs**: a entrega cobre só o **departamento em si** como destinatário — a hierarquia completa seria Cidadão > PJ > Departamento > **participantes**, e o nível "participantes" **não está implementado agora** (nem exibição, nem seleção). Por isso os CTs de resultado expandido/CPF anonimizado (CT-002a, CT-002b, parte do CT-008) foram marcados fora de escopo no card — engano meu ao ler o complemento do Figma como "sem contradição" quando na verdade dependia desse nível ainda não implementado.
- **Gap de cobertura exposto pelo defeito [[QA Workspace/02 Demandas/DEV/11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]]**: nenhum RF/CA cobre retificação de despacho — a tela de retificação não preserva o departamento selecionado como destinatário, mostrando o cidadão PJ/empresa no lugar. Ancorado em [[QA Workspace/04 Conhecimento/Módulos/Despachos#Retificar despacho|Despachos.md]] ("campos editáveis: destinatários" pressupõe mostrar o valor atual real).

---

## Destilado (rascunho do card)

### Descrição

Departamentos (SGV-11083) passam a poder ser selecionados como destinatários em documentos e despachos — no campo pessoa configurado pra Pessoa Jurídica, e no campo de destinatário de despacho. Ao serem efetivamente encaminhados, o departamento recebe notificação por e-mail (com deduplicação e idempotência), e o acesso externo ao documento via essa notificação é registrado com rastreabilidade (`publicIdentifier` UUID, validado contra o vínculo real com o documento) — sem nunca expor o ID interno nem autorizar responder/assinar pela URL.

### Resultado Esperado

- Departamento aparece na busca de destinatário (campo pessoa PJ e despacho) só se ativo e da mesma instância; membros nunca aparecem individualmente a partir dele.
- Seleção/persistência respeita multiplicidade, duplicidade e revalidação pela API; departamento invalidado entre seleção e salvamento bloqueia a operação por inteiro.
- PDF exibe `Nome do departamento (Razão social da PJ)`.
- E-mail vai ao endereço do departamento a cada encaminhamento efetivo, sem duplicar (dedup por e-mail normalizado, idempotência por evento).
- Visualização externa via link do departamento é somente leitura, registra `DocumentInteraction` só depois de validar formato/vínculo/instância/permissão, e nunca revela existência de documento/departamento em caso de link inválido.

### Critérios de aceite

#### A. Selecionar departamento em campo pessoa de documento
- [ ] Departamento só aparece na busca se o campo pessoa tiver Pessoa Jurídica habilitado
- [ ] Busca retorna por nome do departamento ou razão social da PJ, só da mesma instância, exibindo os dois
- [ ] Vínculo documento-campo-departamento é persistido ao salvar, com revalidação da API (configuração do campo, status, instância)
- [ ] Multiplicidade do campo (único/múltiplo) é respeitada e departamento repetido é bloqueado
- [ ] PDF exibe o departamento como "Nome do departamento (Razão social da PJ)"
- [ ] Busca retorna resultado só a partir de 3 caracteres digitados, afunilando progressivamente
- [ ] Cluster do departamento aninhado sob a PJ (~~resultado expandido mostrando participantes, CPF anonimizado~~ — não se aplica, nível "participantes" não implementado nesta entrega)
- [ ] Área de clique do accordion (chevron) não interfere na seleção do departamento (linha inteira)
- [ ] Departamento invalidado entre seleção e salvamento bloqueia a operação por inteiro, com aviso claro

#### B. Selecionar departamento como destinatário de despacho
- [ ] Busca no campo de destinatário do despacho retorna departamentos ativos da instância, por nome ou razão social
- [ ] Resultado exibe nome do departamento e razão social
- [ ] Departamento válido é persistido como destinatário ao salvar/enviar o despacho
- [ ] Membros do departamento não são expandidos nem selecionáveis individualmente a partir dele
- [ ] PDF do despacho exibe o departamento no mesmo formato do campo pessoa
- [ ] Departamento invalidado após seleção bloqueia o envio por inteiro, sem disparar notificação
- [ ] Linha do evento (remetente + destinatários) recebe truncate a ~16px da data; listas longas de destinatário sempre truncam na 2ª linha

#### C. Notificações
- [ ] E-mail é enviado ao endereço do departamento sempre que um documento/despacho é efetivamente encaminhado a ele
- [ ] Só um e-mail por endereço normalizado (sem diferenciar maiúsculas/minúsculas), mesmo com endereço compartilhado entre departamento e membro(s); notificação interna continua uma por membro elegível
- [ ] Reprocessar o mesmo evento não duplica e-mail nem notificação interna
- [ ] E-mail reaproveita o template do evento e inclui documento, indicação de encaminhamento ao departamento, nome+razão social, e URL com `departmentId={publicIdentifier}`

#### D. Registro de visualização externa (rastreabilidade)
- [ ] Todo departamento tem `publicIdentifier` (UUID v4, único, imutável, não nulo)
- [ ] URL externa da notificação carrega `departmentId={publicIdentifier}` — nunca o ID interno
- [ ] Acesso à URL só registra interação depois de validar formato, localizar por `publicIdentifier`, confirmar instância, confirmar vínculo real com o documento e aplicar as permissões externas já existentes
- [ ] Interação registrada (`DocumentInteraction`) só depois do carregamento válido do conteúdo principal; asset/prévia/health-check não geram interação
- [ ] Parâmetro ausente segue o comportamento atual sem interação de departamento; parâmetro malformado/sem vínculo retorna a mesma resposta genérica de indisponível, sem revelar existência de documento/departamento
- [ ] Departamento suspenso depois do encaminhamento não invalida o link já enviado — a suspensão só impede novos encaminhamentos

### Casos de Teste Básicos

Ver seção "## Casos de teste" do card — CTs completos com Dado/Quando/Então, um por critério acima.

---

## Histórico do refinamento

- 2026-09-03 - Material recebido (export do Notion — requisito técnico completo, sem "Resumo" pré-simplificado desta vez)
- 2026-09-03 - Destilado escrito cruzando com o doc de produto consolidado ("Departamento CNPJ" → seção Departamentos na tramitação); nenhum ponto em aberto identificado
- 2026-09-03 - 🔎 Complemento do Figma recebido e cruzado com os 22 CTs já existentes: CA05 (formato de exibição) resolvido a favor do parênteses; 7 detalhes de UX sem contradição incorporados aos CTs (busca 3 caracteres, resultado expandido/cluster aninhado, CPF anonimizado, área de clique do accordion, truncamento). Seleção de membro individual e departamento-como-signatário identificados como fora do escopo desta entrega — preservados como material da epic (SGV-9296), aguardando confirmação de Rafael sobre se viram parte futura.
- 2026-09-03 - 🔎 Ajuste de escopo, na validação: nível "participantes" do departamento não implementado nesta entrega — resultado expandido/CPF anonimizado (CT-002a, CT-002b, parte do CT-008) marcados fora de escopo; cluster aninhado sob a PJ e o accordion continuam válidos.
- 2026-09-03 - 🐛 Defeito cadastrado (achado em teste exploratório): [[QA Workspace/02 Demandas/DEV/11319 - Defeito Departamento Nao E Persistido Ao Retificar Despacho|SGV-11319]] — departamento não persistido ao retificar despacho, gap de cobertura (sem CT de retificação)
