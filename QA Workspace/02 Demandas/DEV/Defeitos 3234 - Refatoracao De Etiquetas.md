---
tags:
  - bug
  - qa
  - etiquetas
task: ""
relacionado: "3234"
prioridade: alta
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Defeitos na refatoração de etiquetas (drawer, pesquisa, preview e menu pelo card)

> [!info] Card de registro — defeitos da 1ª rodada em DEV (reconciliação de 13/08)
> Card agrupado de propósito: problemas independentes, encontrados na **primeira validação em DEV** da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] em 13/08/2026. A entrega ainda está em desenvolvimento, então vão como **defeitos de melhoria**, não como bugs com SGV próprio. Cada item tem seu critério e seu CT.
>
> **Reconciliação de 13/08/2026**: os itens **1, 2, 3** foram **descartados** (comportamento correto confirmado pelo Rafael); o **4** foi extraído para [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]]; o **5** virou [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]]; o **7** foi fechado como **duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]]**; e o **8** (novo) virou [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]]. **A numeração 1–8 não mudou**: slots descontinuados (1, 2, 3, 4, 5, 7) ficam como registro do que saiu/foi descartado, e os demais mantêm o número — evita quebrar o vínculo com as evidências `EV-01/02/04/05/06`, já nomeadas com esses CTs ([[QA Workspace/Evidências/README|regra de não renumerar]]).
>
> **Nome sem o prefixo `3234`** de propósito: o `achar_card()` do `qa-atualiza.py` localiza card pelo primeiro arquivo que começa com `"3234 - "`, e um segundo card com esse prefixo faria o roteador de evidências escolher entre os dois de forma imprevisível. Pelo mesmo motivo o `task:` está vazio e o vínculo mora em `relacionado:` e no wikilink.

### Descrição

Durante a validação foi identificado que:

1. ~~**"Criar e aplicar" não habilita só com o nome**~~ — 🗑️ **Descartado**: o drawer de criação exige escolher uma opção de Compartilhamento (para mim/todos/setores específicos etc.) — comportamento correto confirmado pelo Rafael.
2. ~~**A pesquisa por etiqueta-pai não retorna o cluster completo**~~ — 🗑️ **Descartado**: a busca traz o resultado exato — etiqueta compartilhada aparece, não compartilhada não aparece — comportamento correto confirmado pelo Rafael.
3. ~~**O preview não exibe a linha "Responsável: \<setor\>"**~~ — 🗑️ **Descartado**: preview segue como está — aceito pelo Rafael.
4. ~~O box "Criar etiqueta [termo]" não acompanha a largura do campo de busca~~ — **extraído para [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]]**.
5. ~~**Os toasts de criação e edição divergem da copy** especificada na doc~~ — **extraído para [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]]**.
6. **O seletor de setores não tem a linha "Selecionados:"**, o contador `+qtd` nem o botão de limpar todos.
7. ~~**O menu de contexto do card não fecha** ao abrir o painel de etiquetas pela Mesa e, dependendo da posição do card, chega a cobrir o botão "Nova etiqueta"~~ — **fechado como duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]]** (mesmo ponto de entrada: meatball do card na Mesa).
8. **As opções das últimas etiquetas do submenu "Etiquetas >" do meatball ficam parcialmente ocultas** — **extraído para [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]]**.

---

### Passo a passo para reproduzir

**Defeito 1 — ~~"Criar e aplicar" exige Compartilhamento~~ (🗑️ descartado)**

~~**Dado** que eu abri o menu de aplicação de etiquetas em um documento
**E** acionei **"+ Nova etiqueta"**
**Quando** eu preencho apenas o campo de nome
**Então** verifico que o botão **"Criar e aplicar" segue desabilitado**, e só habilita depois que eu escolho uma opção em Compartilhamento~~

> Concluído em 13/08 que o comportamento é **correto**: criou-e-aplica exige definir o compartilhamento (meu/todos/setores específicos). Não é defeito.

**Defeito 2 — ~~busca pela pai não traz o cluster~~ (🗑️ descartado)**

~~**Dado** que existe uma etiqueta-pai com ao menos uma subetiqueta
**Quando** eu pesquiso pelo **nome da pai** no menu de aplicação
**Então** verifico que ela volta sozinha, **sem o contador `(n)` e sem o chevron** de expandir — e que pesquisar pelo nome da **subetiqueta** traz pai e sub corretamente~~

> Concluído em 13/08 que o comportamento é **correto**: a busca traz o resultado exato — etiqueta compartilhada com o usuário aparece; a não compartilhada não aparece. Não é defeito.

**Defeito 3 — ~~preview sem a linha "Responsável"~~ (🗑️ descartado)**

~~**Dado** que eu abri o drawer de criação de etiqueta
**Quando** eu observo o card de pré-visualização
**Então** verifico que ele exibe a tag, o nome e o número do documento, **mas não a linha "Responsável: \<setor\>"**, mesmo havendo espaço em branco no card~~

> Aceito pelo Rafael em 13/08: preview segue como está. Não é defeito.

**Defeito 4 (extraído)** — ver [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]].

**Defeito 5 — copy dos toasts (extraído)**

~~**Dado** que eu crio uma etiqueta e depois edito outra
**Quando** cada ação é concluída
**Então** verifico que os toasts exibem **"Etiqueta criada com sucesso!"** e **"Etiqueta editada com sucesso!"**, e não os títulos previstos na doc~~

> Extraído para [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]]. Foi confirmado que o modal de confirmação ao salvar edição está **correto** — fora do escopo deste bug.

**Defeito 6 — seletor de setores incompleto**

**Dado** que estou no drawer de criação
**Quando** eu escolho "Compartilhar com setores específicos" e seleciono setores
**Então** verifico que os chips ficam **dentro do campo**, sem a linha **"Selecionados:"**, sem o contador **`+qtd`** e **sem o botão de limpar todos**

> [!info]- Item vizinho, não duplicata: SGV-10842
> [[QA Workspace/02 Demandas/DEV/10842 - Bug Select De Setores Parcialmente Oculto Ao Compartilhar Com Setores Especificos|SGV-10842]] (cadastrado pelo Rafael, 13/08) é o **mesmo campo de setores**, mas um **sintoma distinto**: com uma lista de setores grande, o *select* fica parcialmente oculto — problema de exibição por volume, diferente da falta de "Selecionados:"/`+qtd`/limpar todos registrada aqui. O próprio card do 10842 já faz essa distinção. Os dois seguem como itens separados.

**Defeito 7 — menu do card não fecha ao abrir o painel (fechado como duplicata)**

~~**Dado** que estou na Mesa de Trabalho
**Quando** eu abro o menu de opções de um card e aciono **"Etiqueta"**
**Então** verifico que o menu de contexto (**"Etiqueta" / "Copiar dados do documento"**) **permanece aberto**, sobreposto ao painel de etiquetas

**E** quando o card está posicionado de modo que o painel abra **para baixo**
**Então** o menu sobrepõe o **header** do painel e o botão **"Nova etiqueta"** fica **não clicável**~~

> [!success]- Fechado como duplicata do SGV-10832 em 13/08/2026
> Reconciliado com o Rafael: o ponto de entrada é o **mesmo** — o meatball do card na Mesa de Trabalho (o "ellipsis" do card e o "meatball" descrito no [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]] são o mesmo menu de contexto do card). Sintoma idêntico (menu não fecha ao abrir o painel de etiquetas). Este registro fica como referência; o ticket de correção é o SGV-10832.

> [!note]- A cobertura é condicional à posição do card
> Reproduzido nas duas condições em 13/08:
> - Card no **meio/fim** da coluna → o painel abre **para cima**, o menu fica sobre a área inferior e o botão segue clicável (`elementFromPoint` no centro do botão devolve o próprio `BUTTON`).
> - Card no **topo** da coluna → o painel abre **para baixo** e o menu cobre o header; `elementFromPoint` devolve `LI :: "Copiar dados do documento"`, ou seja, o clique não chega ao botão.
>
> O que é **constante** nas duas é o menu de contexto **não fechar**. A cobertura é a consequência mais grave, não a causa.

**Defeito 8 — opções das últimas etiquetas ocultas no submenu "Etiquetas >" (extraído)**

~~**Dado** que eu acesso o ambiente como Servidor
**E** verifico o meatball e clico em **"Etiquetas >"**
**Quando** clico nas opções das últimas etiquetas da lista
**Então** verifico que elas ficam **parcialmente ocultas**~~

> Novo achado da rodada (13/08), não relacionado aos itens 1–7. Extraído para [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]].

> [!warning]- Possível duplicidade com SGV-10832 — não reconciliado
> [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]] (cadastrado em paralelo, também em 13/08) descreve o mesmo sintoma — menu de contexto do card não fecha ao abrir o modal de Etiquetas — pelo caminho **"Etiqueta >" no meatball**. Este Defeito 7 foi reproduzido pelo caminho do **ellipsis do card**. Podem ser a mesma causa com dois pontos de entrada, ou dois defeitos distintos que só parecem iguais.
>
> **Não fundi nem fechei nenhum dos dois** — decisão de reconciliar (manter os dois, ou fechar um como duplicata do outro) é do Rafael.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://3234)

*As gravações são as mesmas da validação da melhoria e ficam nomeadas com o número da SGV-3234 — o roteador do 🔄 é quem as arquiva. Índice completo CT → EV no card da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]].*

| Defeito | Evidência | CT do card da melhoria | Situação |
|---|---|---|---|
| **Defeito 1** | `EV-01` | CT-025, CT-012 | 🗑️ Descartado (comportamento correto) |
| **Defeito 2** | `EV-02` | CT-011 | 🗑️ Descartado (comportamento correto) |
| **Defeito 3** | `EV-03` | CT-023 | 🗑️ Descartado (aceito pelo Rafael) |
| **Defeito 4** | *extraído — ver [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao\|SGV-10831]]* | CT-012 | → SGV-10831 |
| **Defeito 5** | `EV-04` | CT-029 | → [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc\|SGV-10844]] |
| **Defeito 6** | `EV-05` | CT-017 | ativo — vizinho da [[QA Workspace/02 Demandas/DEV/10842 - Bug Select De Setores Parcialmente Oculto Ao Compartilhar Com Setores Especificos\|SGV-10842]] |
| **Defeito 7** | `EV-06` | CT-018 | duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas\|SGV-10832]] |
| **Defeito 8** | — | — | → [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball\|SGV-10833]] |

---

### Resultado Esperado

1. ~~**Botão condicionado só ao nome**~~ — ~~a doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]] é explícita~~ — **🗑️ descartado** em 13/08: criar-e-aplicar exige o compartilhamento (comportamento correto).
2. ~~**Cluster completo na busca pela pai**~~ — **🗑️ descartado** em 13/08: a busca traz o resultado exato por permissão de compartilhamento.
3. ~~**Preview com o setor responsável**~~ — **🗑️ descartado** em 13/08: preview aceito como está.
4. *(extraído — ver [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]])*
5. **Copy literal da doc** — `Etiqueta criada! A etiqueta foi criada e aplicada com sucesso` e `Etiqueta editada! A etiqueta foi editada e aplicada com sucesso`. O toast de exclusão (`Etiqueta excluída com sucesso!`) já está correto e serve de referência. → **extraído** para [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]].
6. **Seletor completo** — o Figma especifica a linha `↳ Selecionados:` com os chips `$sigla ×`, o excedente em `+ qtd` e o **botão de limpar todos** (ícone de lixeira) à direita.
7. **Menu de contexto fecha ao abrir o painel** — os fluxos de drawer devem funcionar **igualmente** pela toolbar e pelo card da Mesa; hoje o caminho pelo card não permite acionar "Nova etiqueta". → tratado no [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]].
8. **Opções das últimas etiquetas do submenu visíveis** — todas as opções das etiquetas do fim da lista ficam totalmente visíveis e acionáveis, sem ocultação parcial. → tratado no [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]].

---

### Critérios de aceite

- [x] ~~**(1)** Com o nome preenchido e o Compartilhamento intocado, **"Criar e aplicar" está habilitado**~~ — 🗑️ descartado: criar-e-aplicar exige compartilhamento
- [x] ~~**(2)** Pesquisar pelo nome da etiqueta-pai retorna **pai + subetiquetas**, com contador e chevron preservados~~ — 🗑️ descartado: busca por permissão
- [x] ~~**(3)** O preview do drawer e o da página de criação exibem a linha **"Responsável: \<setor\>"**~~ — 🗑️ descartado: aceito
- [ ] ~~**(4)**~~ *(extraído — ver critério próprio em [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]])*
- [ ] ~~**(5)** Os toasts de criação e edição exibem exatamente os títulos **"Etiqueta criada!"** e **"Etiqueta editada!"**~~ *(extraído — ver critério próprio em [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]])*
- [ ] **(6)** Com setores selecionados, aparecem a linha **"Selecionados:"**, o contador **`+qtd`** quando houver excedente e o **botão de limpar todos**, que esvazia a seleção
- [ ] ~~**(7)** Ao abrir o painel de etiquetas pelo card da Mesa, o menu de contexto **fecha**; o botão "Nova etiqueta" fica clicável **em qualquer posição do card** na coluna~~ *(duplicata — ver critério próprio em [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]])*
- [ ] ~~**(8)** As opções das últimas etiquetas do submenu "Etiquetas >" ficam totalmente visíveis e acionáveis~~ *(extraído — ver critério próprio em [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]])*
- [ ] **Sem regressão** nos caminhos que já funcionam: criação por subetiqueta segue habilitando só com o nome, busca pela subetiqueta segue trazendo a pai, toast de exclusão segue correto, e o fluxo pela **toolbar** do documento segue íntegro

---

### Casos de Teste Básicos

#### **CT-B01 "Criar e aplicar" habilita só com o nome** *(1)*

**Dado** que o drawer de criação está aberto a partir de um documento
**E** que o campo de Compartilhamento não foi tocado
**Quando** eu preencho apenas o nome da etiqueta
**Então** o botão **"Criar e aplicar" está habilitado**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-01 - CT-012, CT-025 - box da sugestao quebrado e criar e aplicar travado sem compartilhamento.gif]]
*Mesma gravação também aparece (cópia renomeada) em [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]], como evidência parcial do defeito que foi extraído pra lá.*

---

#### **CT-B02 Busca pela etiqueta-pai retorna o cluster completo** *(2)*

**Dado** uma etiqueta-pai com ao menos uma subetiqueta
**Quando** eu pesquiso pelo nome da pai no menu de aplicação
**Então** o resultado traz a pai **e** suas subetiquetas, mantendo contador e chevron

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-02 - CT-011 - busca pela etiqueta-pai nao retorna o cluster completo.gif]]

---

#### **CT-B03 Preview exibe o setor responsável** *(3)*

**Dado** que eu abri o drawer de criação de etiqueta
**Quando** observo o card de pré-visualização
**Então** ele exibe a linha **"Responsável: \<setor\>"** abaixo do número do documento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-03 - CT-023 - preview do drawer sem a linha responsavel.gif]]

---

#### **CT-B04 (movido)** *(4 — extraído)*

Extraído para [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]] em 13/08/2026 — ver aquele card para reprodução, critério e evidência (renomeados `CT-B01`–`CT-B03` lá).

---

#### **CT-B05 Copy dos toasts de criação e edição** *(5 — extraído)*

Extraído para [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]] em 13/08/2026 — ver aquele card para reprodução, critérios e CTs (renomeados `CT-B01`/`CT-B02` lá).

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-04 - CT-029 - toasts de criacao e edicao com copy divergente.gif]]

---

#### **CT-B06 Seletor de setores com "Selecionados:", contador e limpar todos** *(6)*

**Dado** que escolhi "Compartilhar com setores específicos"
**Quando** eu seleciono setores além do que cabe na linha e aciono o botão de limpar todos
**Então** vejo a linha **"Selecionados:"** com os chips, o contador **`+qtd`** no excedente, e a seleção é **esvaziada** pelo botão

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-05 - CT-017 - seletor de setores sem selecionados, qtd e limpar todos.gif]]

---

#### **CT-B07 Menu de contexto fecha e "Nova etiqueta" fica clicável pelo card** *(7 — duplicata)*

Duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]] confirmada em 13/08/2026 — mesmo ponto de entrada (meatball do card na Mesa) e mesmo sintoma. Ver aquele card para reprodução, critério e CT.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-06 - CT-018 - menu de contexto do card nao fecha ao abrir o painel de etiquetas.gif]]

---

#### **CT-B08 Opções das últimas etiquetas totalmente visíveis** *(8)*

**Dado** que eu acesso o ambiente como Servidor
**E** abri o submenu "Etiquetas >" pelo meatball
**Quando** clico nas opções das últimas etiquetas da lista
**Então** as opções ficam **totalmente visíveis e acionáveis**, sem ocultação parcial

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

*(Extraído para [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]] — ver aquele card; evidência `10833 - botão de opções de etiqueta esta ficando oculto.mp4`.)*

---

### Ambiente

- Versão: 12.38.39.2
- Ambiente: Desenvolvimento (`dev-lucas-cabral`)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — **defeitos de melhoria em DEV**, dos oito achados da primeira rodada de validação (28 dos 29 CTs executados). Situação após reconciliação de 13/08: itens **1, 2, 3 descartados**; **4** extraído para [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]]; **5** extraído para [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]]; **6** segue ativo aqui (vizinho da [[QA Workspace/02 Demandas/DEV/10842 - Bug Select De Setores Parcialmente Oculto Ao Compartilhar Com Setores Especificos|SGV-10842]]); **7** duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]]; **8** extraído para [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]].

- **Fonte de cada veredito**: os defeitos **1, 3, 6 e 7** foram confirmados contra o [Figma — Etiquetas / Handoff](https://www.figma.com/design/3KcRVaH0yYJqpiZ3VAGL9d/Etiquetas----Handoff?node-id=4013-24202); os defeitos **2 e 5** contra a doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]]. O antigo defeito 4 (fonte cruzada com os dois) está agora em [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]]; o **8** foi achado na mesma rodada e virou [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]].

- Observações:
    - 🚨 **Os subitens da task estão em 87,50% e não vieram no export.** Enquanto não forem reexportados, qualquer um dos itens aqui pode ser algo que **ainda não subiu** — é a razão de estarem registrados como defeito de melhoria e não como bug cadastrado. Confirmar antes de mandar pro dev.
    - 🗑️ **Itens 1, 2 e 3 descartados** pelo Rafael em 13/08, após verificação do comportamento: (1) criar-e-aplicar exige compartilhamento (pode ser para mim/todos/etc.); (2) a busca traz o resultado exato — compartilhada aparece, não compartilhada não; (3) preview segue como está.
    - ✅ **Modal de confirmação ao salvar edição verificado — correto**; ficou de fora do escopo da [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]] (que cobre só a copy dos toasts).
    - **Defeito 7 é vizinho do item "modal de etiquetas não fecha ao aplicar na mesa"**, que está no grupo H do card da melhoria como caso sem especificação. Pode ser a mesma causa — o menu de contexto do card não fechando. Fechado como duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]]; vale tratar junto.
    - **Dois falsos positivos descartados nesta rodada**, ambos por conferência no produto: o **"Limpar filtro"** do filtro da Mesa **existe** (é condicional a haver seleção) e o **accordion de subetiquetas** **existe** (vive no menu de aplicação, não no card). Nenhum dos dois virou defeito.
    - Card agrupado por decisão de agilidade. Se algum item crescer — virar discussão de produto ou pedir análise própria — vale separar em card dedicado.

- Histórico:
    - 2026-08-13 - 🐛 Bug confirmado (card de registro com 7 defeitos da 1ª rodada de validação em DEV da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])
    - 2026-08-13 - ✂️ Defeito 4 extraído para [[QA Workspace/02 Demandas/DEV/10831 - Bug Etiqueta Sem Truncamento Na Busca E Nome Maior Que 25 Caracteres Herdado Na Criacao|SGV-10831]] — já existia como task própria no Notion; numeração 1–7 preservada, slot 4 fica como registro do que saiu
    - 2026-08-13 - 🗑️ Itens 1, 2 e 3 descartados (comportamento correto confirmado pelo Rafael), Defeito 5 extraído para [[QA Workspace/02 Demandas/DEV/10844 - Bug Toasts De Criacao E Edicao Com Copy Divergente Da Doc|SGV-10844]], Defeito 7 fechado como duplicata do [[QA Workspace/02 Demandas/DEV/10832 - Bug Menu Do Card Permanece Aberto Sobre O Modal De Etiquetas|SGV-10832]] e Defeito 8 extraído para [[QA Workspace/02 Demandas/DEV/10833 - Bug Opcoes Das Ultimas Etiquetas Parcialmente Ocultas No Submenu Etiquetas Do Meatball|SGV-10833]] — reconciliação dos achados da 1ª rodada
