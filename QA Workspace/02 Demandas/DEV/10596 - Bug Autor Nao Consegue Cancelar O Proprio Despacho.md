---
tags:
  - bug
  - qa
  - despacho
task: "10596"
prioridade: media
status: aberto
data_inicio: 2026-08-04
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: DEV
---
# Autor não consegue cancelar o próprio despacho, mesmo sendo Administrador do setor dono

### Descrição

Durante validação do cancelamento de despacho em DEV ([[QA Workspace/02 Demandas/DEV/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]]) foi identificado que um servidor **não consegue cancelar o despacho que ele mesmo criou**: ao tentar, o sistema informa que **não possui permissão para realizar a operação**.

O caso é forte porque esse servidor satisfaz **as duas trilhas** de permissão previstas na regra, e é negado nas duas — ele é o **autor do despacho** e é **Administrador do setor dono do documento**. A única coisa que ele não é: **o criador do documento**, que foi criado por outro servidor do mesmo setor.

O conjunto de cenários testados indica que a checagem de permissão está olhando **quem criou o documento**, e não quem criou o despacho nem o cargo no setor dono.

---

### Passo a passo para reproduzir

Dado que o **Servidor 1**, do setor **CIM**, crie um documento cujo setor responsável é o CIM
E que o **Servidor 2**, também do **CIM** e com perfil **Administrador**, crie um despacho nesse documento
Quando o Servidor 2 abrir o menu do próprio despacho e acionar "Cancelar despacho"
Então verifico que o sistema informa que **não possuo permissão para realizar a operação**, em vez de permitir o cancelamento

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10596)

**Cenário 5 — o defeito** (autor e Adm do setor dono recebendo "não possuo permissão"), gravado às 15:40:

![[10596 - autor nao consegue cancelar o proprio despacho mesmo.mp4]]

**Cenário 1 — contraste** (Adm atuando pelo setor dono, com a opção disponível), gravado às 13:54. Serve para mostrar que a opção existe e funciona quando o servidor é o criador do documento:

![[10596 - opcao de cancelar despacho nao aparece para adm.mp4]]

---

### Resultado Esperado

O Servidor 2 consegue cancelar o despacho. Ele satisfaz as duas trilhas de permissão definidas na doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]]:

> Permissão: Servidor **N1**, **Administrador** ou **Administrador Setorial** do **setor dono do documento**
> Permissão (N2): Usuário básico cancela **apenas despacho de sua própria autoria**

Ser ou não o **criador do documento** não aparece na regra em momento nenhum — nem como condição, nem como exceção. A permissão de cancelar um despacho é sobre o **despacho** e sobre o **setor dono**, não sobre a autoria do documento que o contém.

---

### Critérios de aceite

- [ ] O **autor do despacho** consegue cancelá-lo, independentemente de ter criado ou não o documento
- [ ] **Administrador, Adm Setorial ou N1 do setor dono** consegue cancelar despacho do documento, mesmo sem ser o autor e sem ter criado o documento
- [ ] **N2 que não é autor e não tem cargo no setor dono** continua **sem** a permissão (sem regressão da restrição)
- [ ] A mensagem de erro de permissão só aparece em cenário que realmente **não** satisfaz nenhuma das duas trilhas

---

### Casos de Teste Básicos

#### **CT-B01 Autor cancela o próprio despacho em documento criado por outro servidor**

**Dado** um documento criado pelo Servidor 1, com setor responsável CIM
**E** um despacho criado pelo Servidor 2, Administrador do CIM
**Quando** o Servidor 2 acionar "Cancelar despacho" no próprio despacho
**Então** o cancelamento é permitido e o despacho passa a exibir a tag "Despacho cancelado"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Adm do setor dono cancela despacho de terceiro em documento que não criou**

**Dado** um documento criado pelo Servidor 1, com setor responsável CIM
**E** um despacho criado pelo Servidor 2
**Quando** um terceiro servidor, **Administrador do CIM** e que não criou o documento, acionar "Cancelar despacho"
**Então** o cancelamento é permitido

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Destinatário Adm de outro setor NÃO pode cancelar despacho alheio (permissão indevida)**

**Dado** um documento criado pelo **Servidor 1**, Administrador do setor **PJ**, com setor responsável **PJ**
**E** que o Servidor 1 emita um despacho **para o Servidor 2**, Administrador do setor **CG**
**Quando** o Servidor 2, como **destinatário** do despacho, abrir o menu dele
**Então** a opção de cancelar **não** é oferecida, ou a operação é negada — ser destinatário não concede a permissão, e ser Adm de outro setor não dá poder sobre documento do PJ

> [!warning]- Este CT testa o lado oposto do defeito — e a hipótese de causa
> O CT-B01 e o CT-B02 verificam **permissão faltante** (quem deveria poder, não pode). Este verifica **permissão indevida** (quem não deveria poder, pode) — que é a falha mais grave das duas, porque significaria um setor anulando ato administrativo de outro.
>
> Serve também como teste da hipótese de causa: se a checagem usa **criador do documento**, o Servidor 2 não é criador e deve ser negado. **Negado** → a hipótese se sustenta. **Permitido** → a hipótese cai e a implementação é mais frouxa que qualquer uma das três regras escritas no vault, o que é defeito novo e de gravidade maior que este card.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] — o defeito nasceu da validação do cancelamento de despacho, que é entrega dessa funcionalidade. É **defeito de melhoria em DEV**, não bug de produção.

- Observações:
    - **Hipótese de causa, para o dev**: a checagem parece usar **o criador do documento** como critério de permissão. Foi o único critério que explicou os cinco cenários testados:

        | # | Criador do **documento**? | Autor do **despacho**? | Cargo no setor dono? | Observado |
        |---|---|---|---|---|
        | 1 | **Sim** | Não | Adm, atuando pelo CIM | Opção aparece |
        | 2 | Sim | Não | Adm, atuando por **outro setor** | Não aparece |
        | 3 | Não | Não | Adm do GP, destinatário | Não aparece |
        | 4 | **Sim** | Sim | Adm | Opção aparece |
        | 5 | **Não** | **Sim** | **Adm do CIM** (setor dono) | **Negado** — este card |

        Os cenários **4 e 5** são o par que isola a variável: mesma pessoa no papel de autor e de Adm, e o que muda é **só** ter criado o documento.
    - **Por que este é o cenário mais forte**: no 5 o servidor deveria passar por **duas** trilhas independentes — autoria do despacho e cargo no setor dono — e é negado nas duas. Não é caso de fronteira, é a regra não sendo aplicada.
    - ⚠️ **Este card foi descartado por engano mais cedo hoje e depois reaberto.** Na primeira análise, com os cenários 1 a 4, concluí que o comportamento estava conforme a regra e criei o card em `99 Arquivo/` com `status: descartado`. O cenário 5 mostrou que a leitura estava errada: no cenário 4 o autor conseguia cancelar porque **também era o criador do documento**, não porque era autor. Card movido de volta para `DEV/`, renomeado e reescrito; a doc do módulo, que eu havia "corrigido" com base naquela leitura, foi restaurada. O rastro fica no Histórico de propósito.
    - **Impacto no plano de teste da 5152**: o **CT-001** e o **CT-002** (grupo A, permissão) reprovam por este defeito. E a divergência de permissão **task × doc** perde parte da relevância aqui — o problema não é qual das duas redações vale, é que **nenhuma das duas** descreve o que o produto faz.
    - **Duas gravações anexadas, uma por cenário**: a do **cenário 5** (o defeito, 15:40) e a do **cenário 1** (o contraste, 13:54). São arquivos distintos — confirmado por tamanho e hash — e o 🔄 nomeou cada um pelo título que o card tinha no momento do roteamento, o que explica os nomes não seguirem o mesmo padrão. Ficam como estão para não quebrar os embeds.

- Histórico:
    - 2026-08-04 - 🔎 Análise em DEV: cenários 1 a 3 cruzados contra a regra de permissão da doc do módulo
    - 2026-08-04 - 🗑️ Descartado por leitura equivocada (conclusão tirada do cenário 4 sem separar a variável "criador do documento")
    - 2026-08-04 - 🐛 Reaberto e cadastrado como defeito, com o cenário 5: autor e Adm do setor dono sendo negado ao cancelar o próprio despacho
