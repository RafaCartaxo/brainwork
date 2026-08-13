---
tags:
  - bug
  - qa
  - etiquetas
task: "10831"
prioridade: media
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Etiqueta sem truncamento na busca e no card de sugestão, e nome com mais de 25 caracteres herdado na criação

### Descrição

Ao digitar buscas longas (a partir de ~25 caracteres) no menu de aplicação de etiquetas, o texto não tem tratamento de overflow: estoura a largura tanto do **campo de busca** quanto do card de sugestão **"Criar etiqueta [termo]"**.

Além disso, ao acionar essa sugestão com um termo de mais de 25 caracteres, o drawer de criação abre com o campo Nome **pré-preenchido acima do limite de 25 caracteres** que a própria etiqueta permite — mesmo sendo impossível criar uma etiqueta com esse tamanho.

---

### Passo a passo para reproduzir

**Dado** que estou em um documento, com o menu de aplicação de etiquetas aberto
**Quando** eu digito no campo de busca um termo inexistente com mais de 25 caracteres
**Então** verifico que o texto **não trunca** — nem no campo de busca, nem no card "Criar etiqueta '[termo]'" — estourando a largura dos dois

**E quando** eu aciono **"Criar etiqueta '[termo]'"**
**Então** verifico que o drawer de criação abre e **herda o nome com mais de 25 caracteres**, acima do limite que a própria etiqueta permite

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10831)

> [!warning]- Evidência parcial, reaproveitada — falta gravação dedicada
> A gravação abaixo é uma **cópia** da evidência do "Defeito 4" originalmente registrado no card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]], seguindo a regra de compartilhamento entre cards do [[QA Workspace/Evidências/README|Evidências/README]] (cópia renomeada com o número deste card).
>
> Ela mostra o card de sugestão quebrando com um termo **curto** (`Financeiro 2026`, 15 caracteres) — evidencia o **sintoma geral de overflow**, mas **não** cobre especificamente: o campo de busca com termo ≥25 caracteres, a ausência do ellipsis, nem a herança do nome no drawer. Gravação dedicada fica pendente (fila da daily de 13/08).

![[10831 - EV-01 - box da sugestao quebrado (evidencia parcial, reaproveitada da SGV-3234).gif]]

*Evidência compartilhada com [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]] — mesmo vídeo, cópia renomeada.*

---

### Resultado Esperado

*Fonte: descrição da task SGV-10831.*

- **Campo de busca**: truncar o texto em **1 linha com ellipsis** (`text-overflow: ellipsis; white-space: nowrap; overflow: hidden;`)
- **Card "Criar etiqueta [termo]"**: permitir **quebra em múltiplas linhas**, respeitando a largura do card (`word-break: break-word;`)
- **Herança no drawer**: o nome pré-preenchido não deveria ultrapassar os 25 caracteres que a etiqueta permite. A doc de [[QA Workspace/04 Conhecimento/Módulos/Etiquetas|Etiquetas]] define esse limite (*"Nome: limite de 25 caracteres, com contador n/25"*), e o campo já **bloqueia digitação** acima disso quando preenchido diretamente (confirmado na validação da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]], CT-027) — pré-preencher acima do limite é inconsistente com essa regra já validada.

---

### Critérios de aceite

- [ ] **(1)** O campo de busca trunca o texto em 1 linha com ellipsis quando o termo excede a largura do campo
- [ ] **(2)** O card "Criar etiqueta [termo]" quebra o texto em múltiplas linhas, respeitando a largura do card, sem estourar o container
- [ ] **(3)** Ao acionar "Criar etiqueta [termo]" com um termo de mais de 25 caracteres, o campo Nome no drawer é preenchido com, no máximo, 25 caracteres

---

### Casos de Teste Básicos

#### **CT-B01 Campo de busca trunca com ellipsis** *(1)*

**Dado** que o menu de aplicação de etiquetas está aberto
**Quando** eu digito um termo com mais de 25 caracteres no campo de busca
**Então** o texto trunca em uma linha, com reticências ao final, sem estourar a largura do campo

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Card de sugestão quebra em múltiplas linhas** *(2)*

**Dado** que digitei um termo sem correspondência, com mais de 25 caracteres
**Quando** observo o card "Criar etiqueta '[termo]'"
**Então** o texto quebra em múltiplas linhas dentro da largura do card, sem estourar o container

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[10831 - EV-01 - box da sugestao quebrado (evidencia parcial, reaproveitada da SGV-3234).gif]]
*Evidência parcial — mostra o sintoma com termo de 15 caracteres, não com 25+. Ver aviso na seção Evidências.*

---

#### **CT-B03 Nome herdado respeita o limite de 25 caracteres** *(3)*

**Dado** que digitei um termo sem correspondência, com mais de 25 caracteres
**Quando** aciono "Criar etiqueta '[termo]'"
**Então** o campo Nome do drawer é preenchido com, no máximo, 25 caracteres

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão: 12.38.39.2
- Ambiente: Desenvolvimento (`dev-lucas-cabral`)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — achado na 1ª rodada de validação em DEV, registrado inicialmente como "Defeito 4" no card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]] e **extraído pra ticket próprio** em 13/08/2026, a pedido do Rafael. A descrição da task já existente no Notion é mais precisa que o achado original (traz a causa em CSS) e revela um comportamento novo — a herança do nome — que não tinha sido testado até então.

- Observações:
    - **Prioridade ajustada pra média**: o achado original tinha severidade baixa (só o box quebrando visualmente). A herança do nome acima de 25 caracteres na criação é um problema de consistência de dado, não só visual — subiu a severidade.
    - **CT-B01 e CT-B03 estão sem evidência** — dependem de gravação dedicada com termo ≥25 caracteres, ainda não feita (ver aviso na seção Evidências).
    - O comportamento esperado (regras de CSS) veio da descrição da task no Notion. Não foi verificado contra um nó específico do Figma de handoff — se houver um, adicionar aqui.

- Histórico:
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10831 já existente no Notion; card do vault criado a partir da task, extraído do agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]])
