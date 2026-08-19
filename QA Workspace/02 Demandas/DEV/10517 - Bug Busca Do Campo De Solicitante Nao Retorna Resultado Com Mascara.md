---
tags:
  - bug
  - qa
  - formularios
task: "10517"
prioridade: media
status: aberto
data_inicio: 2026-07-31
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: formularios
ambiente: DEV
---
# Busca do campo de solicitante não retorna resultado quando o valor é digitado com máscara

### Descrição

Durante validação foi identificado que a busca do **campo de solicitante** — o campo configurável no formulário de abertura do documento — **não retorna nenhum resultado quando o valor é digitado com máscara** (com pontos, traço e barra). A mesma busca, digitada **sem** a pontuação, retorna o registro normalmente.

Como o campo apresenta a máscara para quem digita, o caminho natural do usuário é justamente o que não funciona: ele preenche no formato que a tela sugere e conclui que o solicitante não existe.

O comportamento **reproduz em produção e em homologação**, e é **anterior** à [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — não é regressão daquela entrega, apenas foi encontrado durante a execução dela.

---

### Passo a passo para reproduzir

Dado que existe um formulário de abertura com o **campo de solicitante** configurado
E que existe um solicitante já cadastrado
Quando eu pesquiso esse solicitante digitando o identificador **com máscara** (`XX.XXX.XXX/XXXX-XX`)
Então verifico que a busca **não retorna nenhum resultado**
E quando eu pesquiso o **mesmo** solicitante **sem** a pontuação, verifico que o registro é retornado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10517)

![[10517 - busca do campo de solicitante nao retorna resultado.mp4]]

---

### Resultado Esperado

A busca do campo de solicitante retorna o registro **independentemente da presença de pontuação** — digitando com máscara ou sem, o resultado é o mesmo.

> [!warning]- Gate de doc: não existe doc do construtor de formulários, mas existe precedente na doc de outro módulo
> **Não há doc do construtor de formulários** em `04 Conhecimento/Módulos/` — é a mesma lacuna já registrada nos CT-023 e CT-027 da [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]]. Então **nada escrito descreve como esta busca deve tratar pontuação**.
>
> O que existe é **precedente em outro módulo**: a doc de [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] tem regra explícita — *"o campo deve suportar CPF/CNPJ com pontuação (pontos, traços, barras); o sistema preserva visualmente o que foi digitado/colado, mas **a busca funciona independente da presença de pontuação**"* — e o tooltip daquele input cita justamente `solicitante (CPF/CNPJ)`.
>
> Isso **sustenta a expectativa** (o produto já decidiu como busca por CPF/CNPJ deve se comportar) mas **não é a regra desta tela**. Enquanto o construtor não tiver doc, o dev pode alegar que aqui a regra é outra. Pendência de documentação registrada (fluxo 8).

---

### Critérios de aceite

- [ ] A busca do campo de solicitante retorna o registro quando o valor é digitado **com máscara**
- [ ] A busca continua retornando o registro quando digitado **sem** pontuação (regressão: é o caminho que funciona hoje)
- [ ] O comportamento vale para valor **colado** e **digitado**, já que a máscara se aplica nos dois

---

### Casos de Teste Básicos

#### **CT-B01 Busca do solicitante com o valor mascarado**

**Dado** que existe um formulário de abertura com o campo de solicitante configurado
**E** que existe um solicitante já cadastrado
**Quando** pesquiso esse solicitante digitando o identificador com máscara
**Então** o registro é retornado na busca

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Regressão — busca sem pontuação segue funcionando**

**Dado** que existe um solicitante já cadastrado
**Quando** pesquiso esse solicitante **sem** pontuação
**Então** o registro é retornado na busca

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

*Este é o caminho que funciona hoje e foi o que provou que o registro existe — a busca sem máscara retorna. Fica no card como regressão: a correção não pode quebrá-lo.*

**Evidências de Testes:**

---

#### **CT-B03 Cobertura a confirmar — o mesmo vale para CPF**

**Dado** que existe um solicitante Pessoa Física cadastrado
**Quando** pesquiso esse solicitante digitando o CPF com máscara
**Então** o registro é retornado na busca

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Não executado. O defeito foi observado durante testes de CNPJ; se a causa é o tratamento de pontuação na busca, o CPF cai no mesmo problema — mas isso não foi verificado e **não está sendo afirmado**.*

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

> [!info]- Por que o card nasce em DEV se o bug está em produção e homologação
> Bug de produção em sustentação (correção não urgente) **não tem pasta própria** — o card nasce em `DEV/` com `ambiente: DEV`, que representa a **posição na esteira de correção**, e a origem fica na Descrição e no Histórico. Regra em [[Sistema/Contexto/PADROES_QA#Organização de Bugs|PADROES_QA]]; precedentes SGV-9963 e SGV-9750, e hoje também a [[QA Workspace/02 Demandas/Concluídas/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]].

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — **apenas origem do achado**. Reproduz em produção e homologação, é anterior ao CNPJ alfanumérico, e por isso **não virou CT da melhoria** nem afeta critério dela.

- Observações:
    - **Pode ser a mesma causa raiz do defeito que o Waldemar abriu** no `TC-712` (CT-016): *"Busca por CNPJ alfanumérico não retorna resultado (o item existe)"*. Se ele pesquisou **com máscara**, o que ele registrou como "alfanumérico não retorna" pode ser na verdade "**mascarado** não retorna" — mesmo defeito, diagnóstico diferente. Vale confirmar com ele antes que os dois virem correções separadas.
    - Sem doc do construtor de formulários, a expectativa se apoia em **precedente de outro módulo** ([[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]]), não em regra desta tela — ver o gate de doc no Resultado Esperado.

- Histórico:
    - 2026-07-31 - 🐛 Bug cadastrado (achado durante a execução da [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]]; confirmado como pré-existente em produção e homologação)
