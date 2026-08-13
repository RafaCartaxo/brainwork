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

> [!info] Card de registro — sete defeitos na mesma rodada
> Card agrupado de propósito: são sete problemas independentes, encontrados na **primeira validação em DEV** da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] em 13/08/2026. A entrega ainda está em desenvolvimento, então vão como **defeitos de melhoria**, não como bugs com SGV próprio. Cada item tem seu critério e seu CT.
>
> **Nome sem o prefixo `3234`** de propósito: o `achar_card()` do `qa-atualiza.py` localiza card pelo primeiro arquivo que começa com `"3234 - "`, e um segundo card com esse prefixo faria o roteador de evidências escolher entre os dois de forma imprevisível. Pelo mesmo motivo o `task:` está vazio e o vínculo mora em `relacionado:` e no wikilink.

### Descrição

Durante a validação foi identificado que:

1. **"Criar e aplicar" não habilita só com o nome** — o drawer de criação exige também que se escolha uma opção de Compartilhamento.
2. **A pesquisa por etiqueta-pai não retorna o cluster completo** — a pai volta sozinha, sem as subetiquetas.
3. **O preview não exibe a linha "Responsável: \<setor\>"** — o slot existe no DOM, vazio.
4. **O box "Criar etiqueta [termo]" não acompanha a largura** do campo de busca e quebra o texto em duas linhas.
5. **Os toasts de criação e edição divergem da copy** especificada na doc.
6. **O seletor de setores não tem a linha "Selecionados:"**, o contador `+qtd` nem o botão de limpar todos.
7. **O menu de contexto do card não fecha** ao abrir o painel de etiquetas pela Mesa e, dependendo da posição do card, chega a cobrir o botão "Nova etiqueta".

---

### Passo a passo para reproduzir

**Defeito 1 — "Criar e aplicar" exige Compartilhamento**

**Dado** que eu abri o menu de aplicação de etiquetas em um documento
**E** acionei **"+ Nova etiqueta"**
**Quando** eu preencho apenas o campo de nome
**Então** verifico que o botão **"Criar e aplicar" segue desabilitado**, e só habilita depois que eu escolho uma opção em Compartilhamento

**Defeito 2 — busca pela pai não traz o cluster**

**Dado** que existe uma etiqueta-pai com ao menos uma subetiqueta
**Quando** eu pesquiso pelo **nome da pai** no menu de aplicação
**Então** verifico que ela volta sozinha, **sem o contador `(n)` e sem o chevron** de expandir — e que pesquisar pelo nome da **subetiqueta** traz pai e sub corretamente

**Defeito 3 — preview sem a linha "Responsável"**

**Dado** que eu abri o drawer de criação de etiqueta
**Quando** eu observo o card de pré-visualização
**Então** verifico que ele exibe a tag, o nome e o número do documento, **mas não a linha "Responsável: \<setor\>"**, mesmo havendo espaço em branco no card

**Defeito 4 — box da sugestão com largura quebrada**

**Dado** que o menu de aplicação está aberto
**Quando** eu digito um termo que não corresponde a nenhuma etiqueta
**Então** verifico que a opção **"Criar etiqueta '[termo]'"** aparece num box **mais estreito que o campo de busca**, com o texto quebrado em duas linhas

**Defeito 5 — copy dos toasts**

**Dado** que eu crio uma etiqueta e depois edito outra
**Quando** cada ação é concluída
**Então** verifico que os toasts exibem **"Etiqueta criada com sucesso!"** e **"Etiqueta editada com sucesso!"**, e não os títulos previstos na doc

**Defeito 6 — seletor de setores incompleto**

**Dado** que estou no drawer de criação
**Quando** eu escolho "Compartilhar com setores específicos" e seleciono setores
**Então** verifico que os chips ficam **dentro do campo**, sem a linha **"Selecionados:"**, sem o contador **`+qtd`** e **sem o botão de limpar todos**

**Defeito 7 — menu do card não fecha ao abrir o painel**

**Dado** que estou na Mesa de Trabalho
**Quando** eu abro o menu de opções de um card e aciono **"Etiqueta"**
**Então** verifico que o menu de contexto (**"Etiqueta" / "Copiar dados do documento"**) **permanece aberto**, sobreposto ao painel de etiquetas

**E** quando o card está posicionado de modo que o painel abra **para baixo**
**Então** o menu sobrepõe o **header** do painel e o botão **"Nova etiqueta"** fica **não clicável**

> [!note]- A cobertura é condicional à posição do card
> Reproduzido nas duas condições em 13/08:
> - Card no **meio/fim** da coluna → o painel abre **para cima**, o menu fica sobre a área inferior e o botão segue clicável (`elementFromPoint` no centro do botão devolve o próprio `BUTTON`).
> - Card no **topo** da coluna → o painel abre **para baixo** e o menu cobre o header; `elementFromPoint` devolve `LI :: "Copiar dados do documento"`, ou seja, o clique não chega ao botão.
>
> O que é **constante** nas duas é o menu de contexto **não fechar**. A cobertura é a consequência mais grave, não a causa.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://3234)

*As gravações são as mesmas da validação da melhoria e ficam nomeadas com o número da SGV-3234 — o roteador do 🔄 é quem as arquiva. Índice completo CT → EV no card da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]].*

| Defeito | Evidência | CT do card da melhoria |
|---|---|---|
| **Defeito 1** | `EV-01` | CT-025, CT-012 |
| **Defeito 2** | `EV-02` | CT-011 |
| **Defeito 3** | `EV-03` | CT-023 |
| **Defeito 4** | `EV-01` | CT-012 |
| **Defeito 5** | `EV-04` | CT-029 |
| **Defeito 6** | `EV-05` | CT-017 |
| **Defeito 7** | `EV-06` | CT-018 |

*Os Defeitos 1 e 4 compartilham a EV-01 — foram observados no mesmo fluxo.*

---

### Resultado Esperado

1. **Botão condicionado só ao nome** — a doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]] é explícita: *"Botão primário habilitado só após preencher o nome"*, e a tabela de estados registra `Criar e aplicar | Desabilitado por padrão; habilita ao preencher o nome`. O drawer de **subetiqueta**, que não tem campo de compartilhamento, já se comporta assim — é a prova de que a regra é essa.
2. **Cluster completo na busca pela pai** — *"se o termo estiver numa etiqueta com subetiquetas (ou for a pai), retorna o cluster completo"*.
3. **Preview com o setor responsável** — o Figma de handoff mostra a linha `Responsável: SIGLA - SIGLA` no card de pré-visualização do drawer.
4. **Sugestão legível em uma linha** — o Figma ancora o box ao campo de busca **com a largura do campo**; o passo 4 do fluxo de handoff descreve a opção como *"a primeira opção da lista de resultados"*.
5. **Copy literal da doc** — `Etiqueta criada! A etiqueta foi criada e aplicada com sucesso` e `Etiqueta editada! A etiqueta foi editada e aplicada com sucesso`. O toast de exclusão (`Etiqueta excluída com sucesso!`) já está correto e serve de referência.
6. **Seletor completo** — o Figma especifica a linha `↳ Selecionados:` com os chips `$sigla ×`, o excedente em `+ qtd` e o **botão de limpar todos** (ícone de lixeira) à direita.
7. **Menu de contexto fecha ao abrir o painel** — os fluxos de drawer devem funcionar **igualmente** pela toolbar e pelo card da Mesa; hoje o caminho pelo card não permite acionar "Nova etiqueta".

---

### Critérios de aceite

- [ ] **(1)** Com o nome preenchido e o Compartilhamento intocado, **"Criar e aplicar" está habilitado**
- [ ] **(2)** Pesquisar pelo nome da etiqueta-pai retorna **pai + subetiquetas**, com contador e chevron preservados
- [ ] **(3)** O preview do drawer e o da página de criação exibem a linha **"Responsável: \<setor\>"**
- [ ] **(4)** O box "Criar etiqueta '[termo]'" ocupa a **largura do campo de busca** e o texto cabe em uma linha
- [ ] **(5)** Os toasts de criação e edição exibem exatamente os títulos **"Etiqueta criada!"** e **"Etiqueta editada!"**
- [ ] **(6)** Com setores selecionados, aparecem a linha **"Selecionados:"**, o contador **`+qtd`** quando houver excedente e o **botão de limpar todos**, que esvazia a seleção
- [ ] **(7)** Ao abrir o painel de etiquetas pelo card da Mesa, o menu de contexto **fecha**; o botão "Nova etiqueta" fica clicável **em qualquer posição do card** na coluna
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
*Mesma gravação cobre o Defeito 4.*

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

#### **CT-B04 Box da sugestão acompanha a largura do campo** *(4)*

**Dado** que o menu de aplicação está aberto
**Quando** eu digito um termo sem correspondência
**Então** o box "Criar etiqueta '[termo]'" tem a largura do campo de busca e o texto ocupa **uma linha**

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-01 - CT-012, CT-025 - box da sugestao quebrado e criar e aplicar travado sem compartilhamento.gif]]
*Mesma gravação cobre o Defeito 1.*

---

#### **CT-B05 Copy dos toasts de criação e edição** *(5)*

**Dado** que eu crio uma etiqueta e depois edito outra
**Quando** cada ação é concluída
**Então** os toasts exibem **"Etiqueta criada!"** e **"Etiqueta editada!"**, com os corpos previstos na doc

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

#### **CT-B07 Menu de contexto fecha e "Nova etiqueta" fica clicável pelo card** *(7)*

**Dado** que estou na Mesa de Trabalho
**E** que repito o caso com um card no **topo** e outro no **fim** da coluna
**Quando** abro o menu de opções do card e aciono "Etiqueta"
**Então** o menu de contexto **fecha** nos dois casos e o botão **"Nova etiqueta"** fica visível e clicável

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[3234 - EV-06 - CT-018 - menu de contexto do card nao fecha ao abrir o painel de etiquetas.gif]]

---

### Ambiente

- Versão: 12.38.39.2
- Ambiente: Desenvolvimento (`dev-lucas-cabral`)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — **defeitos de melhoria em DEV**, os sete achados na primeira rodada de validação (28 dos 29 CTs executados).

- **Fonte de cada veredito**: os defeitos **1, 3, 6 e 7** foram confirmados contra o [Figma — Etiquetas / Handoff](https://www.figma.com/design/3KcRVaH0yYJqpiZ3VAGL9d/Etiquetas----Handoff?node-id=4013-24202); os defeitos **2 e 5** contra a doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]]; o **4** contra os dois.

- Observações:
    - 🚨 **Os subitens da task estão em 87,50% e não vieram no export.** Enquanto não forem reexportados, qualquer um destes sete pode ser algo que **ainda não subiu** — é a razão de estarem registrados como defeito de melhoria e não como bug cadastrado. Confirmar antes de mandar pro dev.
    - **Defeito 7 é vizinho do item "modal de etiquetas não fecha ao aplicar na mesa"**, que está no grupo H do card da melhoria como caso sem especificação. Pode ser a mesma causa — o menu de contexto do card não fechando. Vale tratar junto.
    - **Defeito 1 tem prova por contraste**: o drawer de **subetiqueta** não tem seção de compartilhamento e habilita normalmente só com o nome. Isso isola a causa no acoplamento entre o botão primário e o campo de Compartilhamento.
    - **Defeito 3 fica mascarado na página de criação**: lá o container `pre-visualizacao` tem altura fixa de 160px e corta o card por desenho, então a ausência não aparece. No **drawer**, onde há 183px de card e espaço em branco sobrando, ela fica visível. Foi o que separou o defeito real do critério mal escrito.
    - **Dois falsos positivos descartados nesta rodada**, ambos por conferência no produto: o **"Limpar filtro"** do filtro da Mesa **existe** (é condicional a haver seleção) e o **accordion de subetiquetas** **existe** (vive no menu de aplicação, não no card). Nenhum dos dois virou defeito.
    - Card agrupado por decisão de agilidade. Se algum item crescer — virar discussão de produto ou pedir análise própria — vale separar em card dedicado.

- Histórico:
    - 2026-08-13 - 🐛 Bug confirmado (card de registro com 7 defeitos da 1ª rodada de validação em DEV da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])
