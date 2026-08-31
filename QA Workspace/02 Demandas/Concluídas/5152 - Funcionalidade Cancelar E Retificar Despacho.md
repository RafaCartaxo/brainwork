---
tags:
  - demanda
  - qa
  - funcionalidade
  - despacho
task: "5152"
status: resolvido
prioridade: media
data_inicio: 2026-08-04
data_fim: 2026-08-11
responsavel: Rafael
modulo: despacho
---
# Demanda: Cancelar e retificar despacho

> [!info] Informações
> - **Tipo:** Funcionalidade
> - **Status:** Concluída (aprovada em homologação em 11/08/2026)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-5152 no Notion](https://app.notion.com/p/alfa-group/Cancelar-e-retificar-despacho-2502aec67d30814f9cddc0d96b993bb9) · Figma — Tramitação/Handoff: [Design Figma](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=7316-15502) · [handoff retificação](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=7316-21817) · [handoff cancelamento](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=7316-14888)
> - **Devs:** Gabriel Alves, Marcos Vinicius · **Design:** Fernando Junior, Ivo Costa, Vinícius
> - **Análise:** Bruna Machado (02/12/2025) · **Cliente:** Prefeitura de Paulo Afonso · **Projeto:** Sustentação
> - **Prioridade (Notion):** Média · **Deadline firmado com cliente:** 11/08/2026
> - **MR:** aprovado para testes em 28/07/2026 (revisores Bruno Clementino, Lucas Cabral) · **Reaberta em DEV em 30/07/2026** por Flávio Oliveira, com os retornos registrados como subitens · **Progresso de subitens:** 62,07% · Campo "Versão para deploy" **vazio**

---

> [!abstract] Resumo

Hoje só é possível cancelar o **documento inteiro**. Para invalidar a informação equivocada de **um despacho**, o usuário precisa anular o documento todo (inviável quando há outros trâmites válidos) ou emitir um novo despacho dizendo que o anterior não vale — caminho confuso e que sobrecarrega a tramitação.

A entrega adiciona duas ações no menu de opções do despacho, com escopo restrito ao despacho:

- **Cancelar despacho** — ação crítica e **irreversível**, que invalida o trâmite preservando a rastreabilidade: tag fixa na timeline, prazos removidos, assinaturas canceladas, autenticidade inválida, tarja de sem efeito na impressão e no download, justificativa obrigatória e notificação aos envolvidos.
- **Retificar despacho** — correção de erro de preenchimento em despacho já emitido, com **versionamento automático**, justificativa obrigatória, tag "Retificado", cancelamento de todas as assinaturas e **cancelamento dos despachos de resposta**.

Regras completas do módulo: [[QA Workspace/04 Conhecimento/Módulos/Despachos#Cancelar despacho|Despachos → Cancelar despacho]] e [[QA Workspace/04 Conhecimento/Módulos/Despachos#Retificar despacho|Despachos → Retificar despacho]]. Módulo pai: [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]].

---

## Regras de negócio

*Fonte primária: a doc do módulo [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] (cancelar documentado em 23/04/2026, retificar em 19/05/2026). A task traz critérios da análise de 02/12/2025 — **anteriores** à doc — e por isso está defasada onde conflita. Ver Pontos de atenção.*

### Cancelar despacho

Ação **crítica e irreversível**, cujo objetivo é invalidar o trâmite interno preservando rastreabilidade e segurança jurídica.

| Regra | Detalhe |
|---|---|
| Elegibilidade | Só despacho **em tramitação** pode ser cancelado |
| Restrição de origem | **Não** é permitido cancelar despacho gerado por ação sistêmica — Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou, Retomou (**8 ações**) |
| Permissão | Servidor **N1**, **Administrador** ou **Administrador Setorial** do **setor dono** do documento |
| Permissão (N2) | Usuário básico cancela **apenas despacho de sua própria autoria** |
| Irreversibilidade | Cancelado **não** pode ser reaberto nem retomado |
| Justificativa | **Obrigatória** (texto) para concluir |

**Fluxo:** localizar o despacho na timeline → "Cancelar despacho" no menu de opções → pop-up de confirmação detalhando as consequências e reforçando a irreversibilidade → "Continuar" **ancora o usuário no final da thread** daquele despacho e abre o campo de justificativa → o botão de confirmar fica **desabilitado até a justificativa ser digitada** → "Confirmar cancelamento".

**Impactos na estrutura:**

- **Comentar, Responder e o menu de opções deixam de existir**; no lugar, a tag fixa **"Despacho cancelado"**.
- **Todos os prazos** do despacho são removidos; a tag de cancelamento substitui as ações de prazo.
- Processos/documentos associados **passam a constar como desassociados** e **saem da head** do documento (ver [[QA Workspace/04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]]).
- **Anexos**: em praticamente toda situação de download (compactada, autenticável ou personalizada), o anexo vem com as assinaturas realizadas, mas **todas com a sinalização "Sem efeito"**. O anexo original só é obtido indo ao local do despacho e usando **baixar original**.
- A **justificativa** aparece na timeline **identada ao despacho original**, como registro final do trâmite.

**Assinaturas e autenticidade:**

- Todas as assinaturas do despacho (realizadas **ou pendentes**) passam a exibir status **"Cancelado"**.
- Consulta de autenticidade reporta **"Inválida"** para todos os itens.
- Na tela de verificação de autenticidade, onde haveria o botão de acesso ao documento, aparece **aviso de que o despacho foi cancelado**.
- No drawer de solicitações de assinatura, despacho e anexos aparecem **desabilitados e com a tag de cancelamento**.

**Impressão e download:** o despacho cancelado exibe **tarja de sem efeito**, sem validade. Em **PADES** (assinaturas autenticáveis), o arquivo mantém as assinaturas marcadas como **inválidas**, porque foram invalidadas no cancelamento. Contexto da página de assinaturas: [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas → Página extra]].

**Notificações:** todos os servidores envolvidos recebem notificação na central; e **e-mail** oficial de cancelamento vai a todos os participantes, **com link para a justificativa**.

### Retificar despacho

Permite **corrigir erros de preenchimento** em despacho já emitido e em tramitação, gerando **versionamento automático** no histórico, com visibilidade das mudanças para todas as partes envolvidas **a menos que seja retirado na retificação** — ou seja, a própria retificação pode suprimir essa visibilidade.

| Regra | Detalhe |
|---|---|
| Permissão | **Apenas o criador original** do despacho pode retificar |
| Gestão de acesso | Destinatário ou cópia **removido na retificação perde o acesso** à visualização do documento |
| Restrição de origem | **Não** é permitido retificar despacho gerado por ação sistêmica (mesma lista de 8 do cancelamento) |
| Numeração | A numeração original **permanece a mesma** |

**Fluxo:** "Retificar despacho" no menu de opções → pop-up alertando as consequências (incluindo **invalidação imediata de assinaturas**) → "Continuar" leva à página **"Retificar - Despacho [número]"** → alterar campos + **justificativa obrigatória** → "Retificar despacho". "Cancelar" volta ao documento sem aplicar nada.

**Campos editáveis:** destinatários, servidores em cópia, descrição da demanda, anexos e **nível de sigilo**. No despacho de justificativa é possível solicitar/realizar assinaturas, anexar arquivos e associar processos administrativos.

**Impactos:**

- Tag **"Retificado"** na timeline e **em todas as visualizações**.
- **Todas as assinaturas** (concluídas ou pendentes) do despacho original **e dos anexos** são canceladas, por alteração de conteúdo.
- Justificativa exibida ao **final da subthread** do despacho retificado.
- Notificações internas e e-mails automáticos para todos os envolvidos.
- **Todos os despachos de resposta ao despacho retificado são cancelados**, seguindo a regra de despacho cancelado.
- **Histórico de versões**: acessível no menu do despacho retificado para **todos com acesso ao documento**; modal em **tela cheia**, da versão **mais recente para a mais antiga**.
- **Autenticidade**: consulta em versões antigas retificadas segue o mesmo comportamento que já existe para documento retificado.

**Copys de "Ações realizadas"** (container exibido no despacho de justificativa) — asserção literal:

```
Alterou a descrição do despacho.
Adicionou destinatário '$assinatura-textual ($SIGLA)'.
Removeu destinatário '$assinatura-textual ($SIGLA)'.
Adicionou cópia para '$assinatura-textual ($SIGLA)'.
Removeu cópia para '$assinatura-textual ($SIGLA)'.
Adicionou anexo '$assinatura-textual ($SIGLA)'.
Removeu anexo '$assinatura-textual ($SIGLA)'.
Alterou sigilo para '$assinatura-textual ($SIGLA)'.
Alterou '$nome-do-campo' de '$valor-antigo' para '$valor-novo'.
```

### Referência de origem nos eventos (transversal)

Na concepção da feature notou-se que o subdespacho de resposta não dizia **qual** despacho estava sendo respondido — mostrava só "neste despacho". A referência ao despacho de origem foi incrementada, e o mesmo vale para as ações de **prazo**, **assinatura**, **cancelamento** e **retificação**, que passam a informar de onde a solicitação parte. São **quatro** tipos de evento a assertar, além da própria resposta (tema da [[QA Workspace/02 Demandas/Concluídas/8380 - Bug Referencia Resposta Despacho Cadeia Respostas|SGV-8380]]).

### Copys confirmadas no Figma (04/08/2026)

Lidas direto no arquivo **Tramitação — Handoff**, nas páginas `[SGV-7448] Cancelar despacho` e `[SGV-7450] Retificar despacho`. São **resultado esperado literal** — asserção de texto pode usar estas.

| Onde | Copy |
|---|---|
| **Diálogo de aviso — cancelar** | "**Cancelar despacho**" · "Ao cancelar, os prazos e solicitações de assinatura deste despacho serão cancelados. Essa ação é irreversível." · "Deseja mesmo continuar?" · `Voltar` / `Continuar` |
| **Diálogo de aviso — retificar** | "**Retificar despacho**" · "Ao retificar este documento, todas as ações anteriores realizadas no mesmo deverão ser refeitas, **incluindo as assinaturas realizadas**. Deseja mesmo continuar?" · `Voltar` / `Continuar` |
| **Notificação na central** | Título "**Despacho cancelado!**" · "O despacho `$Nome_nro_desp`, referente ao documento `$nome_nro_doc`, foi cancelado. Veja a justificativa!" |
| **E-mail** | Assunto/título "**`$Assinatura_textual`, um despacho foi cancelado!**" · "O despacho `$nome_despacho_nro`, referente ao documento `$Nome_nro_doc`, do qual você é participante, foi cancelado." · "Caso deseje mais informações, acesse o documento para visualizar a justificativa." · botão **`Acessar documento`** |
| **Tarja no PDF (impressão e download)** | **`SEM EFEITO`** — caixa alta, marca d'água **diagonal** sobre o despacho, com o bloco do despacho contornado por borda tracejada |
| **Tag no drawer de download personalizado** | **`Anulado`** — no despacho **e** em cada anexo dele |
| **Tela de autenticidade** | Banner "**O cancelamento do despacho torna as assinaturas sem efeito legal.**" · na linha do despacho, "Este despacho foi cancelado e as assinaturas invalidadas" · coluna Situação = **`Inválida`** em todas as assinaturas |

**Três coisas que essas copys resolveram, e que estavam em aberto:**

1. **A grafia da tarja é `SEM EFEITO`, em caixa alta** — a task estava certa e a doc do módulo estava errada ("Sem efeito"). Ponto de atenção correspondente já corrigido.
2. **Existe uma terceira copy que ninguém tinha registrado**: a tag **`Anulado`** no drawer de download personalizado. Não é a tarja do PDF nem a tag "Despacho cancelado" da timeline — são **três** elementos distintos, em três lugares.
3. **"Ações refeitas" inclui as assinaturas realizadas** — o diálogo da retificação diz isso explicitamente, fechando a ambiguidade que a task deixou.

> [!danger]- Defeito de copy no próprio design da retificação
> O diálogo diz "Ao retificar este **documento**" quando a ação é sobre o **despacho**. Como retificar documento e retificar despacho são features distintas no produto, a frase induz o usuário a achar que vai retificar o processo inteiro. Se o produto tiver implementado assim, **é bug de copy** — e vale checar antes, porque a correção é barata e o risco de confusão é alto.

**O que o Figma não tem**: **toast de sucesso** depois de concluir o cancelamento ou a retificação. Os frames trazem o diálogo *antes* da ação, notificação, e-mail e os artefatos de saída — nenhuma mensagem posterior. Se aparecer toast na execução, é copy nova e precisa ser registrada.

---

> [!warning] Pontos de atenção

- ⚠️ **Divergência de permissão task × doc — nos dois sentidos, e é o maior risco da rodada.** A doc é a regra; se o produto seguir a task, é **bug de permissão**.
	- **Cancelar** — doc: N1, Administrador ou Adm Setorial **do setor dono**, e N2 **só despacho de autoria própria**. Task: "apenas para usuários **a partir do Nível Usuário Básico**" (abre pra todos acima de Somente Leitura, sem recorte de setor dono nem de autoria).
	- **Retificar** — doc: **apenas o criador original**. Task: "a partir do Nível Usuário Básico". São regras **incompatíveis**, não graus da mesma regra.
	- Existe uma **terceira formulação**: [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]] descreve a retificação **geral** como N1/Adm/Adm setorial do setor dono, com N2 restrito ao que ele criou. **As três precisam ser reconciliadas com produto** — detalhe em "Divergências task × doc" na doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]].
- ⚠️ **A retificação depende do cancelamento.** Retificar obriga o cancelamento de **todos os despachos de resposta** ao retificado. Se o cancelamento estiver defeituoso, a retificação reprova por arrasto e o diagnóstico fica ambíguo — por isso os CTs de cancelamento vêm **antes** (grupos B a E) dos de retificação (F a H).
- ✅ **Grafia da tarja: resolvida.** O Figma mostra **`SEM EFEITO`** em caixa alta, marca d'água diagonal — a **task estava certa** e a doc do módulo estava errada. Já corrigido na doc. E são **três** elementos distintos, a não confundir: a **tarja `SEM EFEITO`** no PDF, a tag **`Anulado`** no drawer de download personalizado, e a tag **"Despacho cancelado"** da timeline.
- **Provável typo na task:** um critério fala em "tag de identificação para o despacho **notificado**". Quase certamente é "**retificado**" — confirmar com análise/produto antes de escrever qualquer asserção em cima disso.
- ✅ **Copys lidas no Figma em 04/08** — ver "Copys confirmadas no Figma" acima. Os CTs seguem escritos pelo **estado observável**, mas agora existe copy literal pra assertar mensagem onde ela existe. Nenhum texto foi inventado em momento nenhum. **Não há toast de sucesso no design** — se aparecer na execução, é copy nova.
- 🔎 **As páginas do Figma são nomeadas por SGV, e não é o 5152.** São `[SGV-7448] Cancelar despacho` e `[SGV-7450] Retificar despacho`. Como a 5152 está com **62,07% de subitens** e o escopo dela é "dividido em 2 entregas", o mais provável é que **7448 e 7450 sejam os subitens** — o que explicaria o progresso parcial. Vale confirmar: se for isso, o acompanhamento fino da entrega (e os retornos da reabertura de 30/07) mora nesses dois números, não no 5152.
- ⚠️ **Os subitens da task não vieram no export.** O progresso é **62,07%** e os retornos da reabertura de **30/07** foram registrados **como subitens** — sem eles não se sabe **o que já foi corrigido** e o que ainda está aberto na entrega. **Reexportar a task (com os subitens expandidos) antes de fechar a suíte**, sob risco de reprovar o que já era retorno conhecido ou aprovar o que ainda não subiu.
- **Ruído da task, a não usar como regra:** o campo Observação ainda diz "há intenção de fazer, mas não há definição de prazos" — contradito pelo próprio status "Testando em Dev" e pelo deadline de 11/08/2026.
- **Campo "Versão para deploy" vazio:** o que for aprovado aqui vale **em DEV**. Não assumir o comportamento em homologação nem em produção.

---

## Plano de teste

| Item | Definição |
|---|---|
| **Demanda** | SGV-5152 — Funcionalidade (escopo dividido em 2 entregas: cancelar e retificar) |
| **Responsável** | Rafael |
| **Ambiente** | Homologação — a execução de 11/08/2026 foi em HML; a passagem por DEV não chegou a ser executada |
| **Escopo** | Cancelar despacho e retificar despacho no menu de opções do despacho: permissão, elegibilidade, restrições de origem, fluxo de confirmação, justificativa, impactos na thread, prazos, documentos associados, anexos, assinaturas, autenticidade, impressão/download, versionamento, notificações e referência de origem nos eventos |
| **Fora de escopo** | Cancelar/retificar **documento** (comportamento já existente na plataforma) · menção de servidores via "@" (não é desta entrega) · revisor de anexos |
| **Tipos de teste** | Funcional · Permissão · Negativo · Integração (assinaturas, autenticidade, notificações) |
| **Dependências** | Documento em tramitação com despacho emitido · perfis N1/Administrador/Adm Setorial e N2 em setores distintos · despacho com prazo, anexo, assinatura solicitada e processo associado · despacho de resposta (sub-thread) · despacho sigiloso · e-mail acessível dos participantes |

**Critérios de aceite**

*Derivados da doc do módulo [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]], não da task. Agrupados na mesma ordem dos casos de teste — um critério por comportamento verificável ([[Sistema/Skills/SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]]).*

**A. Permissão (cancelar e retificar)**

- [x] **CA1** — A opção **"Cancelar despacho"** é oferecida a servidor **N1, Administrador ou Adm Setorial do setor dono** do documento, e ao **N2 apenas no despacho de autoria própria**; para os demais a opção **não aparece**
- [x] **CA2** — A opção **"Retificar despacho"** é oferecida **apenas ao criador original** do despacho; para qualquer outro usuário a opção **não aparece**

**B. Cancelar — elegibilidade, restrições e fluxo**

- [x] **CA3** — Só despacho **em tramitação** pode ser cancelado
- [x] **CA4** — Despacho gerado por **ação sistêmica** (Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou, Retomou) **não** oferece a opção de cancelar
- [x] **CA5** — "Cancelar despacho" abre **pop-up de confirmação** que detalha as consequências e reforça a irreversibilidade; "Continuar" **ancora o usuário no final da thread** daquele despacho e abre o campo de justificativa
- [x] **CA6** — A **justificativa é obrigatória**: o botão de confirmar fica **desabilitado até o texto ser digitado**
- [x] **CA7** — O cancelamento é **irreversível**: despacho cancelado **não** pode ser reaberto nem retomado
- [x] **CA8** — A **justificativa** é exibida na timeline **identada ao despacho original**, como registro final do trâmite

**C. Cancelar — impactos na thread e no documento**

- [x] **CA9** — No despacho cancelado, **Comentar, Responder e o menu de opções deixam de existir**, e no lugar aparece a **tag fixa "Despacho cancelado"**
- [x] **CA10** — **Todos os prazos** do despacho são removidos, e a tag de cancelamento substitui as ações de prazo
- [x] **CA11** — Processos/documentos associados pelo despacho **passam a constar como desassociados** e **saem da head** do documento

**D. Cancelar — anexos, assinaturas e autenticidade**

- [x] **CA12** — Nos downloads do documento (compactado, autenticável ou personalizado), os anexos vêm com as assinaturas realizadas **todas sinalizadas como "Sem efeito"**; o arquivo íntegro só é obtido no local do despacho, por **"baixar original"**
- [x] **CA13** — Todas as assinaturas do despacho, **realizadas ou pendentes**, passam a exibir status **"Cancelado"**
- [x] **CA14** — A consulta de autenticidade reporta **"Inválida"** para todos os itens, e no lugar do botão de acesso ao documento aparece **aviso de que o despacho foi cancelado**
- [x] **CA15** — No **drawer de solicitações de assinatura**, o despacho e seus anexos aparecem **desabilitados e com a tag de cancelamento**

**E. Cancelar — impressão, download e notificações**

- [x] **CA16** — Na **impressão**, o despacho cancelado exibe a **tarja de sem efeito**, sem validade
- [x] **CA17** — No **download**, o despacho cancelado exibe a **tarja de sem efeito**, sem validade
- [x] **CA18** — Em **PADES**, o arquivo mantém as assinaturas do despacho cancelado marcadas como **inválidas**
- [x] **CA19** — Todos os servidores envolvidos recebem **notificação na central**
- [x] **CA20** — Todos os participantes recebem **e-mail** oficial de cancelamento, **com link para a justificativa**

**F. Retificar — restrições, fluxo e campos**

- [x] **CA21** — Despacho gerado por **ação sistêmica** (mesma lista de 8 do cancelamento) **não** oferece a opção de retificar
- [x] **CA22** — "Retificar despacho" abre **pop-up alertando as consequências**, incluindo a invalidação imediata das assinaturas; "Continuar" leva à página **"Retificar - Despacho [número]"** e "Cancelar" volta ao documento **sem aplicar nada**
- [x] **CA23** — São editáveis na retificação: **destinatários, servidores em cópia, descrição da demanda, anexos e nível de sigilo**
- [x] **CA24** — A **numeração original do despacho permanece a mesma** após a retificação
- [x] **CA25** — A **justificativa é obrigatória** para concluir a retificação, e é exibida ao **final da subthread** do despacho retificado
- [x] **CA26** — Destinatário ou servidor em cópia **removido na retificação perde o acesso** à visualização do documento

**G. Retificar — impactos**

- [x] **CA27** — A tag **"Retificado"** aparece na timeline **e em todas as visualizações** do despacho
- [x] **CA28** — **Todas as assinaturas** (concluídas ou pendentes) **do despacho e dos anexos** são canceladas pela retificação
- [x] **CA29** — **Todos os despachos de resposta** ao despacho retificado são **cancelados**, seguindo a regra de despacho cancelado
- [x] **CA30** — O container **"Ações realizadas"** no despacho de justificativa exibe as copys previstas, conforme a alteração feita (as 9 formulações da doc)

**H. Retificar — histórico de versões, autenticidade e notificações**

- [x] **CA31** — O **histórico de versões** fica acessível no menu do despacho retificado para **todos que têm acesso ao documento**
- [x] **CA32** — O histórico abre em **modal de tela cheia**, listando as versões **da mais recente para a mais antiga**
- [x] **CA33** — A consulta de **autenticidade em versão antiga** retificada segue o mesmo comportamento já existente para **documento retificado**
- [x] **CA34** — Todos os envolvidos recebem **notificação interna e e-mail** automático da retificação

**I. Transversal — referência de origem nos eventos**

- [x] **CA35** — O evento de **prazo** informa **de qual despacho** a solicitação parte
- [x] **CA36** — O evento de **assinatura** informa **de qual despacho** a solicitação parte
- [x] **CA37** — O evento de **cancelamento** informa **qual despacho** foi cancelado
- [x] **CA38** — O evento de **retificação** informa **qual despacho** foi retificado

---

## Casos de teste

*Formato em [[Sistema/Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]]. **A ordem é deliberada**: os dois cenários de permissão vêm primeiro (é onde task e doc se contradizem de frente, e o resultado muda a leitura de tudo o que vem depois), o cancelamento vem antes da retificação (a retificação cancela os despachos de resposta, então depende do cancelamento funcionar).*

### A. Permissão

#### **CT-001 Opção de cancelar oferecida só a quem a doc autoriza** *(CA1)*

**Dado** que existe um despacho em tramitação num documento cujo setor dono eu conheço
**Quando** eu abro o menu de opções desse despacho logado como **N1 / Administrador / Adm Setorial do setor dono**, depois como **N2 autor do próprio despacho** e depois como **N2 que não é o autor** e como servidor de **outro setor**
**Então** verifico que "Cancelar despacho" aparece nos três primeiros perfis e **não aparece** para o N2 que não é autor nem para o servidor de outro setor

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-002 Opção de retificar oferecida só ao criador original** *(CA2)*

**Dado** que existe um despacho em tramitação criado por outro servidor
**Quando** eu abro o menu de opções desse despacho logado como **criador original** e, em seguida, como **destinatário**, como **N1 do setor dono** e como **Administrador**
**Então** verifico que "Retificar despacho" aparece **somente** para o criador original

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### B. Cancelar — elegibilidade, restrições e fluxo

#### **CT-003 Só despacho em tramitação pode ser cancelado** *(CA3)*

**Dado** que eu tenho um despacho **em tramitação** e outro que **não está em tramitação**
**Quando** eu abro o menu de opções de cada um
**Então** verifico que a opção de cancelar é oferecida **apenas** no despacho em tramitação

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-004 Despacho de ação sistêmica não oferece cancelamento** *(CA4)*

**Dado** que o documento tem despachos gerados por ação sistêmica — Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou e Retomou
**Quando** eu abro o menu de opções de cada um deles
**Então** verifico que **nenhum** oferece a opção de cancelar

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-005 Pop-up de confirmação detalha as consequências e a irreversibilidade** *(CA5)*

**Dado** que eu tenho permissão de cancelar um despacho em tramitação
**Quando** eu clico em "Cancelar despacho" no menu de opções
**Então** verifico que abre um pop-up de confirmação que **descreve as consequências** do cancelamento e **reforça que a ação é irreversível**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-006 "Continuar" ancora no final da thread e abre o campo de justificativa** *(CA5)*

**Dado** que o pop-up de confirmação do cancelamento está aberto
**Quando** eu clico em "Continuar"
**Então** verifico que a tela me leva ao **final da thread daquele despacho** e o **campo de justificativa** fica visível e pronto para digitação

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-007 Botão de confirmar fica desabilitado até a justificativa ser digitada** *(CA6)*

**Dado** que o campo de justificativa do cancelamento está aberto e **vazio**
**Quando** eu observo o botão "Confirmar cancelamento" e depois digito um texto de justificativa
**Então** verifico que o botão está **desabilitado** com o campo vazio e **habilita** quando o texto é digitado, e que o cancelamento se conclui com o despacho passando a exibir a tag de cancelado

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!success]- Copy confirmada no Figma (04/08/2026)
> **Diálogo de aviso do cancelamento** — página `[SGV-7448] Cancelar despacho`, frame "Dialog de aviso":
>
> > ⚠️ **Cancelar despacho**
> > Ao cancelar, os prazos e solicitações de assinatura deste despacho serão cancelados. Essa ação é irreversível.
> > Deseja mesmo continuar?
> > `Voltar` · `Continuar`
>
> Confirma a doc em dois pontos: o diálogo **detalha as consequências** e **reforça a irreversibilidade**, e o botão de avanço é **"Continuar"**.
>
> ⚠️ **O que eu não achei**: um **toast de sucesso** após concluir o cancelamento. O Figma traz o diálogo *antes* da ação e nenhum frame da página mostra mensagem posterior. Este CT segue assertando o **estado observável**; se aparecer toast na execução, é copy nova a registrar.

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-008 Despacho cancelado não pode ser reaberto nem retomado** *(CA7)*

**Dado** que eu tenho um despacho já cancelado
**Quando** eu procuro qualquer ação de reabrir ou retomar esse despacho, na timeline e na toolbar do documento
**Então** verifico que **não existe** caminho para desfazer o cancelamento

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-009 Justificativa exibida identada ao despacho original** *(CA8)*

**Dado** que eu cancelei um despacho informando a justificativa
**Quando** eu consulto a timeline do documento
**Então** verifico que a justificativa aparece **identada ao despacho original**, como registro final daquele trâmite

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### C. Cancelar — impactos na thread e no documento

#### **CT-010 Comentar, Responder e menu de opções somem e entra a tag "Despacho cancelado"** *(CA9)*

**Dado** que eu tenho um despacho recém-cancelado na timeline
**Quando** eu observo esse despacho
**Então** verifico que **Comentar, Responder e o menu de opções não existem mais** e que no lugar aparece a **tag fixa "Despacho cancelado"**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-011 Cancelamento remove todos os prazos do despacho** *(CA10)*

**Dado** que o despacho tem prazos atribuídos a setor e a servidor
**Quando** eu cancelo esse despacho
**Então** verifico que **todos os prazos foram removidos** e que a tag de cancelamento aparece no lugar das ações de prazo

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-012 Documentos associados pelo despacho passam a desassociados e saem da head** *(CA11)*

**Dado** que o despacho associou um processo/documento ao documento atual
**Quando** eu cancelo esse despacho
**Então** verifico que o item passa a constar como **desassociado** e **deixa de aparecer na head** do documento

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### D. Cancelar — anexos, assinaturas e autenticidade

#### **CT-013 Anexos baixados trazem as assinaturas sinalizadas como "Sem efeito"** *(CA12)*

**Dado** que o despacho cancelado tinha anexos com assinaturas realizadas
**Quando** eu baixo o documento nas formas compactada, autenticável e personalizada
**Então** verifico que os anexos vêm com as assinaturas realizadas, **todas sinalizadas como "Sem efeito"**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-014 Anexo íntegro só pelo "baixar original" no local do despacho** *(CA12)*

**Dado** que o despacho cancelado tinha anexos assinados
**Quando** eu vou ao local do despacho na timeline e uso **"baixar original"**
**Então** verifico que o arquivo vem **sem a sinalização de sem efeito**, diferente do que os downloads do documento entregam

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-015 Assinaturas realizadas e pendentes passam a "Cancelado"** *(CA13)*

**Dado** que o despacho tinha uma assinatura **já realizada** e outra **ainda pendente**
**Quando** eu cancelo o despacho
**Então** verifico que **as duas** passam a exibir o status **"Cancelado"**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-016 Autenticidade reporta "Inválida" e exibe aviso de cancelamento** *(CA14)*

**Dado** que o despacho cancelado tinha assinaturas com consulta de autenticidade disponível
**Quando** eu consulto a autenticidade pelo código/QR Code
**Então** verifico que todos os itens são reportados como **"Inválida"** e que, no lugar do botão de acesso ao documento, aparece **aviso de que o despacho foi cancelado**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-017 Drawer de solicitações mostra despacho e anexos desabilitados** *(CA15)*

**Dado** que existiam solicitações de assinatura no despacho e nos seus anexos
**Quando** eu abro o drawer de solicitações de assinatura depois do cancelamento
**Então** verifico que o despacho e os anexos aparecem **desabilitados e com a tag de cancelamento**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### E. Cancelar — impressão, download e notificações

#### **CT-018 Tarja de sem efeito na impressão** *(CA16)*

**Dado** que o documento tem um despacho cancelado
**Quando** eu **imprimo** o documento
**Então** verifico que o despacho cancelado sai com a **tarja de sem efeito**, indicando que não tem validade

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!info]- Grafia da tarja
> A doc do módulo registra **"Sem efeito"** e a task **"SEM EFEITO"**. Conferir no produto qual é a real **antes** de reprovar por texto — a divergência está em Pontos de atenção. E não confundir esta **tarja** com a **tag "Despacho cancelado"** da timeline (CT-010).

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-019 Tarja de sem efeito no download** *(CA17)*

**Dado** que o documento tem um despacho cancelado
**Quando** eu **baixo** o documento
**Então** verifico que o despacho cancelado sai com a **tarja de sem efeito** no arquivo, indicando que não tem validade

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-020 PADES mantém as assinaturas do despacho cancelado como inválidas** *(CA18)*

**Dado** que o despacho cancelado tinha assinaturas autenticáveis
**Quando** eu baixo o arquivo em **PADES** e confiro as assinaturas nele
**Então** verifico que as assinaturas **continuam no arquivo, marcadas como inválidas**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-021 Notificação de cancelamento na central para os envolvidos** *(CA19)*

**Dado** que o despacho tinha remetente, destinatários e servidores em cópia
**Quando** o despacho é cancelado
**Então** verifico que **todos os servidores envolvidos** recebem a notificação do cancelamento na central de notificações

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-022 E-mail de cancelamento com link para a justificativa** *(CA20)*

**Dado** que o despacho tinha participantes com e-mail cadastrado
**Quando** o despacho é cancelado
**Então** verifico que **todos os participantes** recebem o e-mail oficial de cancelamento e que o **link da justificativa** no e-mail abre a justificativa registrada

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### F. Retificar — restrições, fluxo e campos

#### **CT-023 Despacho de ação sistêmica não oferece retificação** *(CA21)*

**Dado** que o documento tem despachos gerados por ação sistêmica — Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou e Retomou
**Quando** eu abro o menu de opções de cada um deles como criador original
**Então** verifico que **nenhum** oferece a opção de retificar

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-024 Pop-up de consequências, "Continuar" leva à página de retificação e "Cancelar" não aplica nada** *(CA22)*

**Dado** que eu sou o criador original de um despacho em tramitação
**Quando** eu clico em "Retificar despacho", leio o pop-up, clico em "Cancelar" e repito o caminho clicando em "Continuar"
**Então** verifico que o pop-up **alerta as consequências, incluindo a invalidação imediata das assinaturas**, que "Cancelar" **volta ao documento sem aplicar nada** e que "Continuar" abre a página **"Retificar - Despacho [número]"**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-025 Campos editáveis na retificação** *(CA23)*

**Dado** que eu estou na página "Retificar - Despacho [número]"
**Quando** eu altero **destinatários, servidores em cópia, descrição da demanda, anexos e nível de sigilo** e concluo a retificação
**Então** verifico que os cinco campos eram editáveis e que as alterações aparecem aplicadas no despacho retificado

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!success]- Copy confirmada no Figma (04/08/2026) — e ela tem um defeito
> **Diálogo de aviso da retificação** — página `[SGV-7450] Retificar despacho`, frame "Dialog de aviso":
>
> > ⚠️ **Retificar despacho**
> > Ao retificar este **documento**, todas as ações anteriores realizadas no mesmo deverão ser refeitas, **incluindo as assinaturas realizadas**. Deseja mesmo continuar?
> > `Voltar` · `Continuar`
>
> 🔴 **Defeito de copy no próprio design**: o texto diz "este **documento**" quando a ação é sobre o **despacho**. Num produto em que retificar documento e retificar despacho são features distintas, isso induz o usuário a achar que vai retificar o processo inteiro. **Vale abrir como bug de copy** se o produto tiver implementado assim.
>
> Do lado bom, o diálogo resolve uma ambiguidade que a task deixou: "ações refeitas" **inclui as assinaturas realizadas** — era o que estava sem enumeração.

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-026 Numeração do despacho preservada após a retificação** *(CA24)*

**Dado** que eu anotei o número do despacho antes de retificar
**Quando** eu concluo a retificação
**Então** verifico que o despacho **mantém exatamente o mesmo número**, na timeline e na impressão

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-027 Justificativa obrigatória e exibida ao final da subthread** *(CA25)*

**Dado** que eu estou na página de retificação com alterações feitas e o campo de justificativa **vazio**
**Quando** eu tento concluir a retificação sem justificativa e depois preencho o texto e concluo
**Então** verifico que **sem justificativa não é possível concluir** e que, concluída, a justificativa aparece ao **final da subthread** do despacho retificado

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-028 Destinatário removido na retificação perde o acesso ao documento** *(CA26)*

**Dado** que o despacho tem um destinatário e um servidor em cópia que **só têm acesso ao documento por esse despacho**
**Quando** eu removo os dois na retificação
**Então** verifico que, logado como cada um deles, **o documento não é mais acessível**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### G. Retificar — impactos

#### **CT-029 Tag "Retificado" na timeline e em todas as visualizações** *(CA27)*

**Dado** que eu retifiquei um despacho
**Quando** eu percorro a timeline, a visualização do despacho, a impressão e o download do documento
**Então** verifico que a tag **"Retificado"** aparece em **todas** essas visualizações

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-030 Retificação cancela as assinaturas do despacho e dos anexos** *(CA28)*

**Dado** que o despacho tinha assinaturas **concluídas e pendentes**, tanto no despacho quanto nos anexos
**Quando** eu retifico o despacho
**Então** verifico que **todas** essas assinaturas aparecem **canceladas**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-031 Retificação cancela todos os despachos de resposta** *(CA29)*

**Dado** que o despacho tem **dois despachos de resposta** na sub-thread
**Quando** eu retifico o despacho
**Então** verifico que **todos os despachos de resposta ficam cancelados**, com a tag de cancelado e sem Comentar/Responder/menu, como no cancelamento direto

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-032 Container "Ações realizadas" exibe as copys previstas** *(CA30)*

**Dado** que na retificação eu alterei a descrição, adicionei e removi destinatário, adicionei e removi cópia, adicionei e removi anexo e alterei o sigilo
**Quando** eu abro o despacho de justificativa
**Então** verifico que o container **"Ações realizadas"** lista uma linha por alteração, no texto previsto na doc ("Alterou a descrição do despacho.", "Adicionou destinatário '…'", "Removeu destinatário '…'", "Adicionou cópia para '…'", "Removeu cópia para '…'", "Adicionou anexo '…'", "Removeu anexo '…'", "Alterou sigilo para '…'", "Alterou '…' de '…' para '…'")

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### H. Retificar — histórico de versões, autenticidade e notificações

#### **CT-033 Histórico de versões acessível a todos com acesso ao documento** *(CA31)*

**Dado** que eu retifiquei um despacho
**Quando** eu abro o menu do despacho retificado logado como criador, como destinatário e como servidor de setor com acesso ao documento
**Então** verifico que **todos** encontram o histórico de versões e conseguem abri-lo

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-034 Histórico abre em tela cheia, da versão mais recente para a mais antiga** *(CA32)*

**Dado** que o despacho tem mais de uma versão no histórico
**Quando** eu abro o histórico de versões
**Então** verifico que ele abre em **modal de tela cheia** e que as versões estão listadas **da mais recente para a mais antiga**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-035 Autenticidade de versão antiga segue o comportamento de documento retificado** *(CA33)*

**Dado** que existe uma versão antiga do despacho, anterior à retificação, com consulta de autenticidade
**Quando** eu consulto a autenticidade dessa versão antiga
**Então** verifico que o retorno é o **mesmo comportamento já existente para documento retificado**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-036 Notificação interna e e-mail da retificação para os envolvidos** *(CA34)*

**Dado** que o despacho tinha remetente, destinatários e servidores em cópia
**Quando** eu retifico o despacho
**Então** verifico que **todos os envolvidos** recebem a notificação interna **e** o e-mail automático da retificação

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

### I. Transversal — referência de origem nos eventos

#### **CT-037 Evento de prazo informa de qual despacho parte a solicitação** *(CA35)*

**Dado** que existe mais de um despacho no documento e eu atribuo um prazo por um deles
**Quando** eu leio o evento de prazo na timeline
**Então** verifico que o evento **identifica o despacho de origem**, e não apenas "neste despacho"

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-038 Evento de assinatura informa de qual despacho parte a solicitação** *(CA36)*

**Dado** que existe mais de um despacho no documento e eu solicito assinatura por um deles
**Quando** eu leio o evento de assinatura na timeline
**Então** verifico que o evento **identifica o despacho de origem** da solicitação

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-039 Evento de cancelamento informa qual despacho foi cancelado** *(CA37)*

**Dado** que existe mais de um despacho no documento e eu cancelo um deles
**Quando** eu leio o evento de cancelamento na timeline
**Então** verifico que o evento **identifica qual despacho foi cancelado**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

#### **CT-040 Evento de retificação informa qual despacho foi retificado** *(CA38)*

**Dado** que existe mais de um despacho no documento e eu retifico um deles
**Quando** eu leio o evento de retificação na timeline
**Então** verifico que o evento **identifica qual despacho foi retificado**

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4]]
*Mesma gravação cobre CT-001 a CT-040.*

---

> [!danger] Bugs encontrados

Nenhum bug novo aberto na validação de 11/08/2026 — os 40 CTs passaram em homologação.

Os achados anteriores da feature seguem em cards próprios e **não foram encerrados por esta aprovação**: [[QA Workspace/02 Demandas/DEV/10596 - Bug Autor Nao Consegue Cancelar O Proprio Despacho|SGV-10596]], [[QA Workspace/02 Demandas/DEV/10607 - Bug Assinatura De Resposta Retificada Ainda Aparece Na Impressao|SGV-10607]] e [[QA Workspace/02 Demandas/DEV/10608 - Bug Achados Na Retificacao De Despacho E Documento|SGV-10608]].

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://5152)

As gravações vão **embedadas em cada CT**, no padrão `5152 - EV-NN - CT-NNN[, CT-NNN] - <descrição>.mp4`. Gravação que cobre mais de um caso é **um arquivo só**, referenciado em cada CT com nota de compartilhamento — convenção em [[QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]].

**Índice CT × EV** (execução de 11/08/2026, em homologação):

| EV | Arquivo | CTs cobertos |
|---|---|---|
| **EV-01** | `5152 - EV-01 - CT-001 a CT-040 - retificar e cancelar despacho.mp4` | CT-001 a CT-040 (os 40) |

Gravação única cobrindo a suíte inteira — cancelamento (grupos B a E), retificação (F a H) e a referência de origem nos eventos (I).

---

> [!tip] Observações

**Regras que só a task tem** — não estão na doc do módulo, e são testáveis. Valem como material de teste **com a ressalva de que não têm respaldo na doc**: se falharem, a conversa antes de abrir card é "isso é regra?".

- **Anexos aprovados voltam a pendentes de aprovação** quando o despacho é retificado. Encaixa na lacuna do revisor de anexos, que segue sem doc no vault.
- **Despacho sigiloso**: a opção de cancelar/retificar só aparece **para quem tem permissão de visualizar** o despacho. É derivável das regras de visibilidade do sigilo em [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]], mas o *gating da opção de menu* não está escrito lá.
- "Todas as ações realizadas precisarão ser **refeitas**" (retificação) × "serão **desfeitas**" (cancelamento) — a task **não enumera quais ações**, então não dá pra transformar em asserção fechada.

**Lacunas — nem a task nem a doc definem.** Cada uma está registrada em [[QA Workspace/04 Conhecimento/Módulos/Despachos#Dúvidas em aberto|Despachos → Dúvidas em aberto]]; aqui só a lista do que trava asserção nesta rodada, para levar a produto:

- Despacho que **movimentou etapa de fluxo de trabalho** pode ser cancelado/retificado? O que acontece com a etapa já avançada e com o contêiner "Próximo passo do documento" ([[QA Workspace/02 Demandas/Concluídas/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]], [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]]).
- **Profundidade da cascata** de cancelamento (respostas das respostas, N níveis; despacho-pai × sub-thread) — o CT-031 cobre **um** nível de propósito.
- **Retificar duas vezes, retificar cancelado, cancelar retificado.**
- **Página extra de assinaturas × cancelamento**: a página ainda é gerada? Com que marcação? ([[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]]).
- **Assinatura pendente**: "status Cancelado" ≠ "solicitação removida" — sai da lista de pendências do signatário e da assinatura em massa?
- **Alterar sigilo na retificação** colide com as proibições do despacho sigiloso (sem processo associado, sem solicitação de assinatura, sem assinar).
- **Cidadão** recebe o e-mail com link da justificativa? Vê a tarja no ambiente externo?
- **Escopo de "ações desfeitas/refeitas"** (comentários, menções, solicitações criadas depois pelo meatball).
- **Numeração do despacho cancelado**: preservação está escrita só para a retificação.

**Eventos de retificação com campos repetidos** já têm melhoria própria em [[QA Workspace/02 Demandas/DEV/MEL-0001 - Organizar Eventos Retificação Campos Repetidos|MEL-0001]] — se os eventos desta entrega ficarem repetitivos, é aquele escopo, não bug novo.

---

## Histórico

- 2026-07-30 - 🔴 Reaberta em DEV (retornos de Flávio Oliveira registrados como subitens da task — **retro-registrado em 11/08/2026**: o evento é anterior ao card e não constava desta lista, só do bloco de Informações)
- 2026-08-04 - Card criado para a validação em DEV (task em "Testando em Dev", reaberta em 30/07)
- 2026-08-11 - 🔁 Retestada e aprovada em homologação (40/40 CTs e 38/38 critérios, evidência EV-01) — card movido de `DEV/` para `Concluídas/` sem passar pela validação em DEV
