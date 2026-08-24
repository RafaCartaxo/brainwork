---
tags:
  - qa
  - conhecimento
tipo: modulo
revisado: 2026-08-04
---
# Despachos

> [!warning] Cancelar e retificar despacho: **em teste em DEV**, não em produção (situação em 04/08/2026)
> As duas seções deixaram de ser especificação futura. A [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] cobre **as duas** ("escopo dividido em 2 entregas") e está com status **Testando em Dev**: MR aprovado em 28/07/2026 (revisores Bruno Clementino e Lucas Cabral) e **reaberta em DEV em 30/07/2026**, com os retornos registrados como subitens. Progresso de subitens 62,07%; QA responsável **Rafael**; deadline firmado com cliente **11/08/2026** (Prefeitura de Paulo Afonso).
>
> Vale como comportamento esperado **em DEV**. Não assumir em homologação nem em produção — o campo "Versão para deploy" da task está vazio.
>
> **A task diverge desta doc em permissões**, e a doc é a regra: ver "Divergências task × doc" em Comportamentos observados.
>
> Origem: export da página **Despachos** do Notion (`(9+)-despachos-notion.md`, reexportado 04/08/2026; página criada 17/09/2024, última edição 30/07/2026 por Flávio Oliveira). Página filha de **Tramitação** — ver [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]].

## Visão geral

Despacho é a forma de **comunicação usada para tramitar documentos** dentro do sistema. Existem variações conforme o contexto em que são acionadas, mas **todas seguem o modelo do despacho padrão** — o que faz do padrão a referência de comportamento esperado quando uma variação não estiver documentada.

Acionamento, pela toolbar do documento:

| Opção | Quando aparece |
|---|---|
| **Despacho** | Tramitar um processo administrativo |
| **Responder** / **Encaminhar** | Documentos oficiais ou comunicações interativas |
| Responder a um despacho já emitido | Cria uma **nova sub-thread** |

## Regras de negócio

### Destinatários

- Despacho que é **resposta**: o destinatário padrão já inclui quem originou o despacho anterior.
- Despacho **novo** num documento: o **setor responsável** é sugerido como destinatário, e **pode ser alterado**.

### Funcionalidades do despacho

Adicionar prazos · solicitar assinaturas · anexar arquivos · associar documentos.

### Prazos

- O prazo do despacho **deve respeitar o prazo geral do documento**.
- Podem ser atribuídos a **setores e servidores**, mas **não a cidadãos**.
- O prazo do **servidor** deve estar alinhado ao prazo do **setor**.

### Assinaturas

- Podem ser solicitadas de **qualquer pessoa ou setor que possa tramitar o documento**.
- Servidor que **não é destinatário** e é adicionado para assinar entra **automaticamente como destinatário**.
- Assinatura solicitada **depois** do despacho criado usa a opção "Solicitar Assinatura" no **meatball menu**, e cria um **sub-evento na thread** do despacho.

### Documentos associados

- Documentos associados são visíveis a **todos os envolvidos no despacho** — mas **a recíproca não vale**: só quem já tinha permissão prévia vê os documentos associados.
- Todo documento oficial gerado por meio do despacho **precisa ser emitido**; não pode ficar em elaboração.

### Despacho sigiloso

Versão restrita do padrão, acionada pelo radio button de sigilo. O que muda:

- Ganha a tag **"Com Sigilo"**.
- Prazos só podem ser atribuídos a **quem está diretamente envolvido** no despacho.
- Anexos continuam permitidos.

**Restrições de visibilidade:**

- O sigilo é restrito ao **setor dono** e aos **usuários configurados nas regras de tramitação** (ver [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]]).
- Quem **perde o acesso ao setor** envolvido deixa de ver o despacho, a menos que entre em outro setor com permissão.
- Para quem **não está envolvido**: aparecem apenas remetentes e destinatários, **sem o conteúdo**.
- **Externamente**: só um evento dizendo que "houve um despacho sigiloso" no processo.
- **Respostas a despacho sigiloso também são sigilosas.**
- **Impressão**: sem permissão de ver o despacho sigiloso, ele também não aparece na impressão.

**Despacho sigiloso NÃO pode:** ter processos associados · ter solicitação de assinatura · assinar · emitir e assinar.

### Extensão DWG em anexo de despacho

Arquivos `.dwg` **devem ser aceitos como anexo nos despachos**, tanto no ambiente **interno** quanto no **externo** — a lista de tipos permitidos passa a incluir `.dwg`.

O motivo registrado na doc é um caso de uso concreto: quando um anexo é **reprovado na abertura do processo**, o cidadão precisa reencaminhar o arquivo, e sem suporte à extensão ele fica impedido de fazer isso.

> [!important] Regra que respalda a [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]]
> Esta é a regra escrita que faltava no gate de doc daquele card: DWG **é** formato aceito em despacho. Um `.dwg` que passa no upload e faz a criação do documento falhar **contradiz regra documentada** — não é lacuna de especificação.
>
> O que a doc **não** define: quais arquivos `.dwg` são válidos (tamanho, versão do formato). Então a distinção "recusar com mensagem" × "estourar erro na geração" segue sem respaldo escrito.

### Cancelar despacho

> [!note]- Em teste em DEV pela [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] (04/08/2026)
> Documentada no Notion em **23/04/2026**. Deixou de ser especificação futura: MR aprovado em 28/07/2026, reaberta em DEV em 30/07/2026. Vale como comportamento esperado **em DEV**. O item `[UI/UX] Cancelar despacho` segue no backlog da página, mas o backlog não reflete o status de implementação.

Ação **crítica e irreversível**. Objetivo: invalidar trâmites internos preservando rastreabilidade e segurança jurídica.

**Regras e permissões:**

| Regra | Detalhe |
|---|---|
| Elegibilidade | Só despacho **em tramitação** pode ser cancelado |
| Restrição de origem | **Não** é permitido cancelar despacho gerado por ação sistêmica (Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou, Retomou) |
| Permissão | Servidor **N1**, **Administrador** ou **Administrador Setorial** do **setor dono do documento** |
| Permissão (N2) | Usuário básico cancela **apenas despacho de sua própria autoria** |
| ⚠️ Divergência | **O produto não implementa esta regra.** O comportamento observado indica que a checagem olha **quem criou o documento** — ignorando tanto a autoria do despacho quanto o cargo no setor dono. É a [[QA Workspace/02 Demandas/DEV/10596 - Bug Autor Nao Consegue Cancelar O Proprio Despacho|SGV-10596]]; ver a tabela de cenários em Comportamentos observados |
| Irreversibilidade | Cancelado **não** pode ser reaberto nem retomado |
| Justificativa | **Obrigatória** (texto) para concluir |

**Fluxo:** localizar o despacho na timeline → "Cancelar despacho" no meatball → pop-up de confirmação detalhando as consequências e reforçando a irreversibilidade → "Continuar" **ancora o usuário no final da thread** daquele despacho e abre o campo de justificativa → o botão de confirmar fica **desabilitado até a justificativa ser digitada** → "Confirmar cancelamento".

**Impactos na estrutura:**

- **Comentar, Responder e o menu de opções deixam de existir**; no lugar, a tag fixa **"Despacho cancelado"**.
- **Todos os prazos** do despacho são removidos; a tag de cancelamento substitui as ações de prazo.
- Processos/documentos associados **passam a constar como desassociados** e saem da head do documento.
- **Anexos**: em praticamente toda situação de download (compactada, autenticável ou personalizada), o anexo vem com as assinaturas realizadas, mas **todas com a sinalização "Sem efeito"**. O anexo original só é obtido indo ao local do despacho e usando **baixar original**.
- A **justificativa** é exibida na timeline **identada ao despacho original**, como registro final do trâmite.

**Assinaturas e autenticidade:**

- Todas as assinaturas do despacho (realizadas **ou pendentes**) passam a exibir status **"Cancelado"**.
- Consulta de autenticidade reporta **"Inválida"** para todos os itens.
- Na tela de verificação de autenticidade, onde haveria o botão de acesso ao documento, aparece **aviso de que o despacho foi cancelado**.
- No drawer de solicitações de assinatura, despacho e anexos aparecem **desabilitados e com a tag de cancelamento**.

**Impressão e download:** o despacho cancelado exibe **tarja `SEM EFEITO`** — caixa alta, marca d'água **diagonal** sobre o despacho, com o bloco contornado por borda tracejada (grafia e forma confirmadas no Figma em 04/08/2026). No **drawer de download personalizado** o despacho e cada anexo dele levam a tag **`Anulado`** — elemento diferente da tarja e da tag da timeline. Em **PADES** (assinaturas autenticáveis), o arquivo mantém as assinaturas marcadas como inválidas, já que foram invalidadas no cancelamento.

**Notificações:** todos os servidores envolvidos recebem notificação na central; e **e-mail** oficial de cancelamento vai a todos os participantes, **com link para a justificativa**.

**Referência de origem nos eventos:** na concepção da feature notou-se que o subdespacho de resposta não dizia **qual** despacho estava sendo respondido (mostrava só "neste despacho"). Foi incrementada a referência ao despacho respondido — e o mesmo vale para as ações de **prazo**, **assinatura**, **cancelamento** e **retificação**, que passam a informar de onde a solicitação parte. São **quatro** tipos de evento a assertar, não dois.

### Retificar despacho

> [!note]- Em teste em DEV pela [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] (04/08/2026)
> Documentada no Notion em **19/05/2026**. Mesmo card do cancelar — a SGV-5152 entrega as duas e tem um status só, então tratar uma como implementada e a outra como pendente não se sustenta. Vale como comportamento esperado **em DEV**.
>
> ⚠️ **Dependência entre as duas features**: a retificação obriga o cancelamento de todos os despachos de resposta ao retificado ("Impactos", abaixo), ou seja **retificar depende do cancelar funcionar**. Testar o cancelamento primeiro.

Permite **corrigir erros de preenchimento** em despacho já emitido e em tramitação, gerando **versionamento automático** no histórico, "assegurando que todas as partes envolvidas tenham visibilidade das mudanças realizadas **a menos que seja retirado na retificação**" — ou seja, a própria retificação pode **suprimir** essa visibilidade. Regra que muda a expectativa de teste sobre o histórico de versões.

| Regra | Detalhe |
|---|---|
| Permissão | **Apenas o criador original** do despacho pode retificar |
| Gestão de acesso | Destinatário ou cópia **removido na retificação perde o acesso** à visualização do documento |
| Restrição de origem | **Não** é permitido retificar despacho gerado por ação sistêmica (mesma lista do cancelamento) |
| Numeração | A numeração original **permanece a mesma** |

**Fluxo:** "Retificar despacho" no menu de opções → pop-up alertando as consequências (incluindo **invalidação imediata de assinaturas**) → "Continuar" leva à página **"Retificar - Despacho [número]"** → alterar campos + **justificativa obrigatória** → "Retificar despacho". "Cancelar" volta ao documento sem aplicar nada.

**Campos editáveis:** destinatários, servidores em cópia, descrição da demanda, anexos e **nível de sigilo**. No despacho de justificativa é possível solicitar/realizar assinaturas, anexar arquivos e associar processos administrativos.

**Impactos:**

- Tag **"Retificado"** na timeline e em todas as visualizações.
- **Todas as assinaturas** (concluídas ou pendentes) do despacho original **e dos anexos** são canceladas, por alteração de conteúdo. ⚠️ **O produto não faz isso na saída impressa**: ao retificar uma resposta já assinada, a assinatura segue aparecendo na impressão sem sinalização de invalidada — [[QA Workspace/02 Demandas/DEV/10607 - Bug Assinatura De Resposta Retificada Ainda Aparece Na Impressao|SGV-10607]].
- Justificativa exibida ao **final da subthread** do despacho retificado.
- Notificações internas e e-mails automáticos para todos os envolvidos.
- **Todos os despachos de resposta ao despacho retificado devem ser cancelados**, seguindo a regra de despacho cancelado.
- **Histórico de versões**: acessível no menu do despacho retificado para **todos com acesso ao documento**; modal em tela cheia, da versão mais recente para a mais antiga.
- **Autenticidade**: consulta em versões antigas retificadas segue o mesmo comportamento que já existe para documento retificado.

**Copys de "Ações realizadas"** (container no despacho de justificativa) — úteis pra asserção literal em teste:

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

### Menção de servidores via "@"

> [!note]- Situação de implementação a confirmar
> Documentada no Notion em **13/05/2026**; consta no backlog da página como `*[Melhoria-CX] SOGOV - Menção de servidores via "@" nos processos`. Situação de implementação não confirmada — ver Dúvidas em aberto.

Menção de servidores em campos de texto de processos (despacho, respostas).

- **Gatilho**: `@` + **3 caracteres** iniciais.
- **Quem aparece na busca**: apenas servidores que **estejam envolvidos no processo** ou **tenham permissão de acesso ao documento**.
- **Dismiss**: a listagem fecha ao clicar fora do container ou ao apagar o caractere gatilho.
- **Seleção**: renderiza **nome do servidor + sigla da unidade** como badge/chip no corpo do texto, com botão **X** para exclusão rápida.
- Exibição na lista: avatar (se houver) + nome completo + sigla da unidade como badge à direita.
- ⚠️ **Não se aplica** na criação de **Modelos de Documentos** — só quando usado como template num campo aberto (abertura, despacho, etc.).
- Consistência esperada: mesma API de busca/ordenação da menção de **comentários**; navegação por setas do teclado.

## Comportamentos observados em teste

### Divergências task × doc — SGV-5152 (04/08/2026)

A [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] traz critérios de aceite escritos na **análise da Bruna Machado em 02/12/2025** — **anteriores** a esta doc (cancelar 23/04/2026, retificar 19/05/2026). É o que explica as divergências. **Esta doc é a regra**; a task, quando conflita, está defasada.

| Ponto | Esta doc | A task | Como testar |
|---|---|---|---|
| **Permissão de cancelar** | N1, Administrador ou Adm Setorial **do setor dono**; N2 **só despacho de autoria própria** | "apenas para usuários **a partir do Nível Usuário Básico**" | **Pela doc.** A task abre pra todos acima de Somente Leitura, sem recorte de setor dono nem de autoria. Se o produto seguir a task, é **bug de permissão** |
| **Permissão de retificar** | **Apenas o criador original** | "apenas para usuários **a partir do Nível Usuário Básico**" | **Pela doc.** É a divergência mais grave: são regras incompatíveis, não graus da mesma regra |

⚠️ Existe uma **terceira formulação** no vault: [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]] descreve a retificação **geral** como N1/Adm/Adm setorial do setor dono, com N2 restrito ao que ele criou. A regra do **despacho** (só o criador) é a mais específica e a mais recente — mas as três precisam ser reconciliadas com produto.

**Regras que só a task tem** (não estão nesta doc, e são testáveis):

- **Anexos aprovados voltam a pendentes de aprovação** quando o despacho é retificado. Encaixa na lacuna do revisor de anexos, que segue sem doc no vault.
- **Despacho sigiloso**: a opção de cancelar/retificar só aparece **para quem tem permissão de visualizar** o despacho. Derivável das regras de visibilidade do sigilo, mas o *gating da opção de menu* não está escrito aqui.
- "Todas as ações realizadas precisarão ser **refeitas**" (retificação) × "serão **desfeitas**" (cancelamento) — a task não enumera quais ações. Ver Dúvidas em aberto.

**Ruído da task, a não usar como regra**: o campo Observação ainda diz "há intenção de fazer, mas não há definição de prazos", contradito pelo próprio status e pelo deadline de 11/08. E um critério fala em "tag de identificação para o despacho **notificado**" — quase certamente erro de digitação de "retificado"; confirmar antes de escrever asserção.

### Permissão de cancelar — o produto não segue a regra (DEV, 04/08/2026)

Cinco cenários validados pelo Rafael, todos em documento com **setor dono CIM**:

| # | Criador do **documento**? | Autor do **despacho**? | Cargo no setor dono? | Observado |
|---|---|---|---|---|
| 1 | **Sim** | Não | Adm, atuando pelo CIM | Opção **aparece** |
| 2 | Sim | Não | Adm, atuando por **outro setor** | **Não aparece** |
| 3 | Não | Não | Adm do GP, **destinatário** | **Não aparece** |
| 4 | **Sim** | Sim | Adm | Opção **aparece** |
| 5 | **Não** | **Sim** | **Adm do CIM** (setor dono) | **Negado**: "não possuo permissão para realizar a operação" |

O único critério que explica os cinco é **"é o criador do documento?"** — avaliado no setor ativo. E isso **contraria a regra documentada em duas frentes**:

- **Ignora a autoria do despacho.** No cenário 5 o servidor criou o próprio despacho e não consegue cancelá-lo. A regra dá essa permissão explicitamente.
- **Ignora o cargo no setor dono.** Ainda no 5, ele é **Administrador do CIM**, que é o setor dono. Deveria passar pela trilha principal, independente da autoria.

O cenário 5 é o mais forte porque o servidor deveria passar por **duas** trilhas e é negado nas duas. Virou a [[QA Workspace/02 Demandas/DEV/10596 - Bug Autor Nao Consegue Cancelar O Proprio Despacho|SGV-10596]].

> [!warning]- Correção de rota: o que eu havia registrado aqui mais cedo estava errado
> Na primeira versão desta seção (manhã de 04/08) eu concluí, a partir do cenário 4 isolado, que a regra real era "setor dono **ou** autoria, com autoria valendo para qualquer nível" — e cheguei a reescrever a tabela de permissão por causa disso. O cenário 5 falsificou essa leitura: no 4 o autor conseguia cancelar porque **também era o criador do documento**, não porque era autor. A tabela de permissão foi restaurada para o texto da doc oficial, e a divergência passou a ser registrada como defeito do produto, que é o que ela é.
>
> Lição de método: **um cenário só não estabelece regra.** O que parecia confirmação era coincidência de duas variáveis não separadas.


### Outros

- **2026-08-04 (DEV) — retificar resposta assinada não invalida a assinatura na impressão.** A regra manda cancelar **todas** as assinaturas por alteração de conteúdo, e o diálogo do Figma avisa o usuário disso antes de confirmar. Na prática a assinatura segue saindo no papel **como se valesse**: [[QA Workspace/02 Demandas/DEV/10607 - Bug Assinatura De Resposta Retificada Ainda Aparece Na Impressao|SGV-10607]]. Segundo defeito da mesma rodada de validação da 5152 — o outro é no cancelamento.

- **2026-08-04 — a grafia da tarja foi resolvida no Figma, e esta doc estava errada.** A página do módulo escreve "Sem efeito"; o design mostra **`SEM EFEITO`** em caixa alta, e a **task estava certa**. Corrigido acima. Ficou claro também que são **três** elementos distintos, que vinham sendo confundidos: a **tarja `SEM EFEITO`** (marca d'água diagonal no PDF), a tag **`Anulado`** (drawer de download personalizado, no despacho e em cada anexo) e a tag **"Despacho cancelado"** (timeline).
- **2026-08-04 — copys de notificação e e-mail lidas no Figma** (páginas `[SGV-7448]` e `[SGV-7450]` do arquivo Tramitação — Handoff). Estão transcritas no card da [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]], em "Copys confirmadas no Figma". Dois pontos que mudam expectativa de teste: **(a)** o e-mail traz o botão **"Acessar documento"** e o texto "acesse o documento para visualizar a justificativa" — ou seja o link leva ao **documento**, não direto à justificativa, ao contrário do que esta doc afirmava; **(b)** o diálogo da retificação diz "Ao retificar este **documento**" quando a ação é sobre o **despacho** — provável **defeito de copy no design**.
- **2026-08-04 — o design não tem toast de sucesso.** Nem para cancelar nem para retificar: existem o diálogo de confirmação *antes* da ação, a notificação na central, o e-mail e os artefatos de saída. Se aparecer toast na execução, é copy nova e não especificada.
- **2026-08-03 (DEV e homologação) — `.dwg` aceito no upload faz a criação do documento/despacho falhar** em 3 arquivos específicos: [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]]. Contradiz a regra de "Extensão DWG" acima, que manda aceitar `.dwg` como anexo em despacho no interno e no externo.

## Dúvidas em aberto
- [ ] **Como a assinatura invalidada deve aparecer na saída do despacho RETIFICADO?** A doc garante que as assinaturas são canceladas, mas descreve o tratamento visual só para o **cancelado** (sinalização de sem efeito, tarja `SEM EFEITO`). Para o retificado define a tag "Retificado" nas visualizações, sem dizer o que acontece com a assinatura no papel. É a lacuna que faz o critério da [[QA Workspace/02 Demandas/DEV/10607 - Bug Assinatura De Resposta Retificada Ainda Aparece Na Impressao|SGV-10607]] aceitar "marcada como inválida" **ou** "ausente"
- [x] ~~**O "Retificar despacho" está implementado?**~~ **Respondido em 04/08/2026**: sim, em DEV — mesmo card do cancelar, a SGV-5152, status "Testando em Dev"
- [ ] **A menção via "@" está implementada?** Mesma situação: doc de 13/05/2026 e item de backlog `[Melhoria-CX]` aberto. **Não** está coberta pela SGV-5152, que é só cancelar/retificar
- [x] ~~**Qual a regra de permissão de cancelar que vale?**~~ **Resolvido por validação em 04/08/2026**: é **setor dono OU autoria**, com a autoria valendo para qualquer nível — ver "Permissão de cancelar" em Comportamentos observados. A redação desta página estava errada, não o produto
- [ ] **Qual a regra de permissão de RETIFICAR vale?** Esta continua aberta, e as três fontes seguem incompatíveis: **"apenas o criador original"** (aqui), **N1/Adm/Adm setorial do setor dono, N2 só o que criou** ([[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho]], retificação geral) e **"a partir do Nível Usuário Básico"** (task). O cenário que separa as três: **Adm do setor dono que NÃO criou o despacho** — pela regra daqui não pode, pelas outras duas pode. Não dá pra reconciliar por leitura: "apenas o criador" e "Adm do setor dono pode" se contradizem
- [ ] **Cancelar/retificar despacho que movimentou etapa de fluxo de trabalho** é permitido? A lista de restrições de origem não inclui "movimentou etapa", e nada define o que acontece com a etapa já avançada nem com o contêiner "Próximo passo do documento"
- [ ] **Profundidade da cascata de cancelamento.** A retificação manda cancelar os despachos **de resposta**; não define respostas **das respostas** (N níveis), nem se cancelar um despacho-pai cancela a sub-thread
- [ ] **Retificar duas vezes, retificar cancelado, cancelar retificado.** O histórico "da mais recente para a mais antiga" sugere N versões, mas nada afirma que um despacho já retificado pode ser retificado de novo. E a elegibilidade "em tramitação" só está escrita para o cancelamento
- [ ] **Página extra de assinaturas × cancelamento.** Se todas as assinaturas viram "Cancelado"/"Inválida", a página extra ainda é gerada? Com que marcação? O QR Code aponta pra uma verificação que dirá "Inválida"? Nenhuma fonte cruza as duas features — ver [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]]
- [ ] **Assinatura pendente: "status Cancelado" ≠ "solicitação removida".** A doc diz que a pendente exibe status "Cancelado" e fica desabilitada no drawer; não diz se **sai** da lista de pendências do signatário e da assinatura em massa
- [ ] **Alterar sigilo na retificação colide com as proibições do sigiloso.** Sigilo é campo editável, mas despacho sigiloso não pode ter processo associado, solicitação de assinatura nem assinar. Retificar um despacho não sigiloso que **já tem** essas coisas para sigiloso: bloqueia, remove ou passa? E o caminho inverso expõe conteúdo retroativamente?
- [ ] **Cidadão.** A notificação interna fala em "servidores envolvidos" e o e-mail em "participantes". Cidadão em documento com abertura externa recebe o e-mail com link da justificativa? Vê a tarja "Sem efeito" no ambiente externo?
- [ ] **O que entra em "ações desfeitas/refeitas"?** Comentários, menções via "@", solicitações de assinatura criadas depois pelo meatball — nenhuma fonte enumera o conjunto
- [ ] **Numeração de despacho cancelado.** Preservação está escrita só para a retificação. Cancelado mantém o número (deixando buraco na sequência) ou é reaproveitado?
- [ ] **Quais arquivos `.dwg` são válidos?** A regra diz que a extensão é aceita, mas não define tamanho nem versão do formato — é exatamente a lacuna que deixa o 5º critério da [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]] inexecutável (não dá pra montar um arquivo "inválido" sem saber a regra)
- [ ] **Revisor de anexos (selos, carimbos, anotações em DWG) não está coberto por esta doc.** A SGV-8698 entregou isso e a regra não mora aqui nem em módulo nenhum do vault — falta identificar onde a doc oficial dessa funcionalidade vive
- [ ] O export trouxe "1 more…" na lista de itens do backlog da página — **um item ficou de fora**. O reexport de 04/08 **cortou no mesmo lugar**, então o 6º item segue desconhecido; pra fechar é preciso expandir a lista no Notion **antes** de exportar
- [ ] ⚠️ **O export está truncado no fim, e existe um callout que nunca chegou ao vault.** A última linha dos dois exports é um `>` solitário, logo depois da seção "Extensão DWG" — é o início de um callout cujo conteúdo não veio. **É o candidato mais provável a conter a regra de quais `.dwg` são válidos** (tamanho, versão), que é justamente a lacuna acima e o que bloqueia o caso negativo da [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]]. Vale abrir a página no Notion e ler esse bloco

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]] — anexo DWG em documento/despacho (aberto; divergência com a regra de Extensão DWG)
- [[QA Workspace/02 Demandas/Concluídas/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] — ações de tramitação e encerramento na emissão de despacho
- [[QA Workspace/02 Demandas/HML/7829 - Bug Anexos Despacho Não Carregados Emitir Assinar Cidadão|SGV-7829]] — anexos do despacho ao emitir e assinar como cidadão
- [[QA Workspace/02 Demandas/HML/5360 - Bug Assinatura Despacho Customizado Não Aparece Pendentes|SGV-5360]] — solicitação de assinatura em despacho customizado
- [[QA Workspace/02 Demandas/HML/9977 - Bug Nome Oculto Cópia Despacho|SGV-9977]] — servidor em cópia no despacho
- [[QA Workspace/02 Demandas/Concluídas/9499 - Bug Sigilo Despacho Servidor Autor|SGV-9499]] e [[QA Workspace/99 Arquivo/Bug Sigilo Despacho Cidadão Autor|Bug Sigilo Despacho Cidadão Autor]] — regras de sigilo
- [[QA Workspace/02 Demandas/Concluídas/8380 - Bug Referencia Resposta Despacho Cadeia Respostas|SGV-8380]] — referência da resposta na cadeia, mesmo tema da seção "Referência de origem nos eventos"
- [[QA Workspace/02 Demandas/Concluídas/6375 - Bug Data Ausente Evento Despacho|SGV-6375]] — evento do despacho
- [[QA Workspace/02 Demandas/Concluídas/10246 - Bug Erro Emitir Assinar Despacho Cidadão|SGV-10246]] — emitir e assinar despacho como cidadão
- [[QA Workspace/00 Inbox/2026-07-14 - despacho sigiloso aparece mesmo com config desativada|captura: despacho sigiloso aparece mesmo com config desativada]] — as regras de visibilidade do sigilo acima são a referência pra transformar essa captura em card

## Referências
- Página **Despachos** no Notion: https://app.notion.com/p/alfa-group/Despachos-def108ccc3f743ceb97ead2313c8aa4e — página filha de Tramitação
- Módulo pai: [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] (regras de quem pode criar, receber, tramitar e ver)
- [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] — solicitação e realização de assinatura em despacho e anexos
