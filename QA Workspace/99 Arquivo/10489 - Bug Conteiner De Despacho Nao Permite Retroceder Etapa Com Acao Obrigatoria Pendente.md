---
tags:
  - bug
  - qa
  - tramitacao
task: "10489"
prioridade: ""
status: descartado
data_inicio: 2026-07-30
data_fim: "2026-07-30"
responsavel: Rafael
cadastrado_por: Rafael
modulo: tramitacao
ambiente: HML
---
# Contêiner de despacho não permite retroceder etapa quando há ação obrigatória pendente (descartado — não é bug)

> [!warning] Descartado no mesmo dia — não é bug
> O bloqueio total do select **é o comportamento intencional**, confirmado no Figma em duas leituras e com o time pelo Rafael em 30/07.
>
> **De onde veio a confusão**: a doc de [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]] diz que com pendência *"só retroceder ou encerrar"*. Lido isolado, parece autorizar retroceder pelo contêiner. Mas as duas regras respondem perguntas diferentes: o Workflow diz **o que é permitido no documento** (retroceder, sim — pela toolbar); a spec da SGV-9042 diz **o que este contêiner oferece** (nada de movimentação com pendência). Retroceder é permitido; não por este caminho.
>
> O card fica aqui como registro do raciocínio, porque a conciliação entre as duas regras é sutil e vai enganar de novo. A nota está em [[QA Workspace/04 Conhecimento/Módulos/Tramitação#Ações de destino na emissão de despacho (SGV-9042)|Tramitação]].
>
> ⚠️ **Se o número já foi cadastrado no Notion**, fechar/cancelar a task lá também — o vault não faz isso.

### Descrição

No contêiner **"Próximo passo do documento"** da emissão de despacho, quando a etapa tem ação obrigatória pendente (despacho customizado não emitido ou assinatura não concluída), o select de movimentação é desabilitado **por inteiro** — fica fixo em "Permanecer na etapa atual" e não permite nem avançar nem **retroceder**.

Bloquear o **avanço** é correto. Bloquear o **retrocesso** não: pela toolbar do documento **é possível retroceder** nesse mesmo estado, e a regra do módulo diz que deve ser assim.

O resultado é uma incoerência entre dois caminhos para a mesma ação: retroceder está disponível na toolbar e indisponível no contêiner, com o documento no mesmo estado e o usuário com a mesma permissão.

---

### Passo a passo para reproduzir

**Dado** que eu tenho um documento com fluxo de trabalho configurado e iniciado
**E** que a etapa atual tem ação obrigatória pendente (despacho customizado não emitido)
**Quando** eu abro o contêiner "Próximo passo do documento" na emissão de despacho
**Então** verifico que o select está desabilitado também para **retroceder etapa**, embora a mesma ação esteja disponível pela toolbar do documento

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10489)

![[10489 - conteiner nao permite retroceder com acao obrigatoria pendente.mp4]]

*Evidência compartilhada com a [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] — mesmo vídeo, cópia renomeada. Lá é a gravação do CT-004/CT-006.*

---

### Resultado Esperado

Com ação obrigatória pendente na etapa, o contêiner "Próximo passo do documento":

- **bloqueia o avanço** — "Avançar etapa" e os atalhos progressivos seguem indisponíveis;
- **permite retroceder** — "Retroceder etapa" segue selecionável, como já acontece pela toolbar do documento;
- **permite encerrar** — as opções de encerramento seguem disponíveis.

O bloqueio é da **direção de avanço**, não do select inteiro.

---

### Critérios de aceite

- [ ] Com ação obrigatória pendente, o contêiner **permite selecionar "Retroceder etapa"**
- [ ] Com ação obrigatória pendente, o contêiner **continua bloqueando "Avançar etapa"** (não regredir o bloqueio correto)
- [ ] O comportamento é o mesmo para as duas pendências: **despacho customizado não emitido** e **assinatura não concluída**
- [ ] O tooltip do ⓘ informa o que está bloqueado de fato (o avanço), em vez de sugerir bloqueio total
- [ ] Retroceder pelo contêiner gera **evento na timeline com justificativa**, igual ao retrocesso pela toolbar
- [ ] Retroceder pelo contêiner **não cancela as pendências** da etapa — elas seguem pendentes para quando o documento voltar

---

### Casos de Teste Básicos

#### **CT-B01 Retroceder pelo contêiner com despacho customizado não emitido**

**Dado** que a etapa atual tem um despacho customizado **não emitido**
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que "Retroceder etapa" está disponível para seleção

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10489 - conteiner nao permite retroceder com acao obrigatoria pendente.mp4]]

---

#### **CT-B02 Retroceder pelo contêiner com assinatura não concluída**

**Dado** que a etapa atual tem uma **assinatura não concluída**
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que "Retroceder etapa" está disponível para seleção

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 O bloqueio do avanço permanece**

**Dado** que a etapa atual tem ação obrigatória pendente
**Quando** eu abro o contêiner "Próximo passo do documento"
**Então** verifico que "Avançar etapa" e os atalhos progressivos seguem **indisponíveis**

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B04 Retrocesso pelo contêiner preserva as pendências**

**Dado** que a etapa atual tem ação obrigatória pendente
**E** que eu retrocedo a etapa pelo contêiner
**Quando** eu avanço de volta para essa etapa
**Então** verifico que as ações obrigatórias **continuam pendentes**, sem terem sido canceladas nem concluídas

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B05 Paridade entre toolbar e contêiner**

**Dado** que a etapa atual tem ação obrigatória pendente
**Quando** eu comparo as ações de movimentação oferecidas pela toolbar do documento e pelo contêiner
**Então** verifico que retroceder está disponível nos **dois** caminhos

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10489 - conteiner nao permite retroceder com acao obrigatoria pendente.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-10489** (número informado pelo Rafael em 30/07).
- **Origem**: validação da [[QA Workspace/02 Demandas/HML/9042 - Melhoria Ações de Tramitação e Encerramento na Emissão de Despacho|SGV-9042]] em homologação. O CA6 e o CT-006 daquele card apontam pra cá.
- **Gate de doc** (2026-07-30, fluxo 8): **divergência confirmada** contra [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Fluxo de trabalho (Workflow)]], que condiciona **apenas o avanço** ao cumprimento das ações obrigatórias — em quatro pontos independentes:

    | Onde | O que diz |
    |---|---|
    | § Despachos da etapa | "a etapa **só avança** quando o despacho for emitido (**sem ele, só retroceder ou encerrar**)" |
    | § Avançar e retroceder | "**Só avança** cumprindo todas as ações obrigatórias" |
    | § Ações obrigatórias | "precisam ser cumpridas **pra avançar**" |
    | § Comportamentos observados | "**Retroceder não cancela eventos**: pendências da etapa **continuam pendentes** e só podem ser feitas quando avançar de novo pra ela" |

    O último é o mais forte: essa regra **só existe porque se retrocede com pendência**. Se o retrocesso fosse bloqueado nesse estado, não haveria pendência para "continuar pendente". Confirmado com o time pelo Rafael em 30/07.
- ⚠️ **Uma regra errada tinha entrado no vault por minha conta, e este defeito quase foi aprovado como comportamento correto.** Ao ler o Figma em 29/07 eu registrei *"o bloqueio é total: inclui avançar, retroceder e todos os atalhos, nas duas direções"* — e levei isso pro card da 9042, pra doc de [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] e pro **CA6**, que chegou a ser **marcado como aprovado** na validação. O critério sancionava o defeito. Corrigido nos três lugares em 30/07.
- **A confirmar no diagnóstico**:
    - **Atalhos retroativos**: a doc libera "retroceder" com pendência, mas não fala de **atalho de recuo** (retrocesso não linear — [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)#Atalhos de etapas (27/05/2026)|Atalhos de etapas]] define "direção livre: progressivo e retroativo"). Por coerência deveriam seguir a regra do retrocesso linear, mas **não está escrito** — confirmar com produto e documentar.
    - **Copy do tooltip**: hoje ele informa a pendência num contexto de bloqueio total. Se o bloqueio passa a ser só do avanço, a copy precisa acompanhar.
    - Interação com **"só retrocede uma vez"** (regra da doc): se o retrocesso pelo contêiner consome esse direito da mesma forma que o da toolbar.
- Histórico:
    - 2026-07-30 - 🗑️ SGV-10489 - Descartado (não é bug: bloqueio total do select confirmado como intencional no Figma e com o time)
    - 2026-07-30 - 🐛 SGV-10489 - Bug cadastrado (contêiner bloqueia retroceder com ação obrigatória pendente; divergência confirmada contra o Workflow, que condiciona só o avanço)
