---
tags:
  - qa
  - conhecimento
tipo: modulo
revisado: 2026-08-03
---
# Despachos

> [!warning] Leia antes de testar: parte desta doc é especificação, não comportamento atual
> O **Cancelar despacho** está documentado em detalhe aqui e **ainda não foi implementado** (informado pelo Rafael em 03/08/2026). A seção existe porque é a regra que vai valer — não porque o produto se comporta assim hoje. Cada seção nessa condição está marcada.
>
> Origem: export da página **Despachos** do Notion (`(9+)-despachos-notion.md`, baixado 03/08/2026; página criada 17/09/2024, última edição 30/07/2026 por Flávio Oliveira). Página filha de **Tramitação** — ver [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]].

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

> [!warning] ⚠️ NÃO IMPLEMENTADO (situação em 03/08/2026)
> Toda esta seção é **especificação de uma feature que ainda não existe no produto** — informado pelo Rafael em 03/08/2026. Documentada no Notion em **23/04/2026**, e ainda listada como item de backlog da página (`[UI/UX] Cancelar despacho`). **Não usar como comportamento esperado em validação** até que a implementação seja confirmada.

Ação **crítica e irreversível**. Objetivo: invalidar trâmites internos preservando rastreabilidade e segurança jurídica.

**Regras e permissões:**

| Regra | Detalhe |
|---|---|
| Elegibilidade | Só despacho **em tramitação** pode ser cancelado |
| Restrição de origem | **Não** é permitido cancelar despacho gerado por ação sistêmica (Retificou, Associou, Desassociou, Cancelou, Revogou, Suspendeu, Pausou, Retomou) |
| Permissão | Servidor **N1**, **Administrador** ou **Administrador Setorial** do setor dono do documento |
| Permissão (N2) | Usuário básico cancela **apenas despacho de sua própria autoria** |
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

**Impressão e download:** o despacho cancelado exibe **tarja "Sem efeito"** sem validade. Em **PADES** (assinaturas autenticáveis), o arquivo mantém as assinaturas marcadas como inválidas, já que foram invalidadas no cancelamento.

**Notificações:** todos os servidores envolvidos recebem notificação na central; e **e-mail** oficial de cancelamento vai a todos os participantes, **com link para a justificativa**.

**Referência de origem nos eventos:** na concepção da feature notou-se que o subdespacho de resposta não dizia **qual** despacho estava sendo respondido (mostrava só "neste despacho"). Foi incrementada a referência ao despacho respondido — e o mesmo vale para as ações de **prazo** e **assinatura**, que passam a informar a qual despacho se referem.

### Retificar despacho

> [!note]- Situação de implementação a confirmar
> Documentada no Notion em **19/05/2026** e também listada no backlog da página (`[UI/UX] Retificar despacho`, e um item "Cancelar e retificar despacho"). O Rafael confirmou que **o cancelar** não está implementado; **sobre o retificar não há confirmação** — ver Dúvidas em aberto.

Permite **corrigir erros de preenchimento** em despacho já emitido e em tramitação, gerando **versionamento automático** no histórico.

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
- **Todas as assinaturas** (concluídas ou pendentes) do despacho original **e dos anexos** são canceladas, por alteração de conteúdo.
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

- **2026-08-03 — Cancelar despacho documentado mas não implementado.** A doc do Notion descreve a feature por completo (23/04/2026) e o produto não a tem. Registrado aqui porque a doc, lida isolada, induz quem for testar a tratar a especificação como comportamento atual. Informado pelo Rafael.
- **2026-08-03 (DEV e homologação) — `.dwg` aceito no upload faz a criação do documento/despacho falhar** em 3 arquivos específicos: [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]]. Contradiz a regra de "Extensão DWG" acima, que manda aceitar `.dwg` como anexo em despacho no interno e no externo.

## Dúvidas em aberto
- [ ] **O "Retificar despacho" está implementado?** A doc é de 19/05/2026 e o item segue no backlog da página. O Rafael confirmou apenas que o **cancelar** não está — o retificar ficou sem resposta. Isso muda o que é validável hoje
- [ ] **A menção via "@" está implementada?** Mesma situação: doc de 13/05/2026 e item de backlog `[Melhoria-CX]` aberto
- [ ] **Quais arquivos `.dwg` são válidos?** A regra diz que a extensão é aceita, mas não define tamanho nem versão do formato — é exatamente a lacuna que deixa o 5º critério da [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]] inexecutável (não dá pra montar um arquivo "inválido" sem saber a regra)
- [ ] **Revisor de anexos (selos, carimbos, anotações em DWG) não está coberto por esta doc.** A SGV-8698 entregou isso e a regra não mora aqui nem em módulo nenhum do vault — falta identificar onde a doc oficial dessa funcionalidade vive
- [ ] O export trouxe "1 more…" na lista de itens do backlog da página — **um item ficou de fora**; reexportar rolando a lista se for preciso fechar a triagem do módulo

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- [[QA Workspace/02 Demandas/DEV/10482 - Bug Criacao De Documento E Despacho Falha Com Anexos DWG Especificos|SGV-10482]] — anexo DWG em documento/despacho (aberto; divergência com a regra de Extensão DWG)
- [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] — ações de tramitação e encerramento na emissão de despacho
- [[QA Workspace/02 Demandas/HML/7829 - Bug Anexos Despacho Não Carregados Emitir Assinar Cidadão|SGV-7829]] — anexos do despacho ao emitir e assinar como cidadão
- [[QA Workspace/02 Demandas/HML/5360 - Bug Assinatura Despacho Customizado Não Aparece Pendentes|SGV-5360]] — solicitação de assinatura em despacho customizado
- [[QA Workspace/02 Demandas/DEV/9977 - Bug Nome Oculto Cópia Despacho|SGV-9977]] — servidor em cópia no despacho
- [[QA Workspace/02 Demandas/Concluídas/9499 - Bug Sigilo Despacho Servidor Autor|SGV-9499]] e [[QA Workspace/99 Arquivo/Bug Sigilo Despacho Cidadão Autor|Bug Sigilo Despacho Cidadão Autor]] — regras de sigilo
- [[QA Workspace/02 Demandas/Concluídas/8380 - Bug Referencia Resposta Despacho Cadeia Respostas|SGV-8380]] — referência da resposta na cadeia, mesmo tema da seção "Referência de origem nos eventos"
- [[QA Workspace/02 Demandas/Concluídas/6375 - Bug Data Ausente Evento Despacho|SGV-6375]] — evento do despacho
- [[QA Workspace/02 Demandas/Concluídas/10246 - Bug Erro Emitir Assinar Despacho Cidadão|SGV-10246]] — emitir e assinar despacho como cidadão
- [[QA Workspace/00 Inbox/2026-07-14 - despacho sigiloso aparece mesmo com config desativada|captura: despacho sigiloso aparece mesmo com config desativada]] — as regras de visibilidade do sigilo acima são a referência pra transformar essa captura em card

## Referências
- Página **Despachos** no Notion: https://app.notion.com/p/alfa-group/Despachos-def108ccc3f743ceb97ead2313c8aa4e — página filha de Tramitação
- Módulo pai: [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] (regras de quem pode criar, receber, tramitar e ver)
- [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] — solicitação e realização de assinatura em despacho e anexos
