---
tags:
  - bug
  - qa
  - despacho
task: "10596"
prioridade: media
status: descartado
data_inicio: 2026-08-04
data_fim: 2026-08-04
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: DEV
---
# Opção de cancelar despacho não aparece para Adm atuando por outro setor

> [!info] Descartado no mesmo dia — não é defeito
> Investigado em 04/08/2026 e **descartado**: o comportamento observado **está conforme a regra**. A permissão de cancelar tem duas trilhas alternativas — **setor dono** ou **autoria** — e o cenário reportado não satisfaz nenhuma das duas. Detalhe em Observações.

### Descrição

Durante validação do cancelamento de despacho (melhoria em DEV, [[QA Workspace/02 Demandas/DEV/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]]) observou-se que, em documento cujo setor responsável é o **CIM**, um servidor **administrador multissetor** envolvido em um despacho criado por outro servidor vê a opção **"Cancelar despacho"** quando está atuando **pelo CIM**, mas **não** a vê quando está atuando **por outro setor** — mesmo sendo administrador nesse outro setor também.

---

### Passo a passo para reproduzir

Dado que exista um documento cujo setor responsável seja o **CIM**
E que o **Servidor 2** crie um despacho nesse documento
E que o **Servidor 1**, administrador de mais de um setor, seja envolvido nesse despacho
Quando o Servidor 1 atuar **pelo setor CIM** e abrir o menu do despacho
Então a opção "Cancelar despacho" é exibida
Mas quando ele atuar **por outro setor**, mesmo sendo administrador nele, a opção **não** é exibida

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10596)

![[10596 - opcao de cancelar despacho nao aparece para adm.mp4]]


---

### Resultado Esperado

**O comportamento observado é o esperado.** A permissão de cancelar é satisfeita por **uma** de duas trilhas: ser **N1, Administrador ou Administrador Setorial do setor dono do documento**, ou ser **autor do despacho**. Atuando pelo CIM, o Servidor 1 exerce autoridade no setor dono e a opção aparece; atuando por outro setor, ele não é do setor dono e não é autor, então a opção não deve aparecer.

Ser administrador multissetor **não** concede autoridade simultânea em todos os setores: a permissão é avaliada contra o **setor ativo**.

---

### Critérios de aceite

- [x] Com o servidor atuando pelo **setor dono** do documento, a opção de cancelar é exibida
- [x] Com o mesmo servidor atuando por **setor que não é o dono** e sem ser autor do despacho, a opção **não** é exibida
- [x] A permissão é avaliada contra o **setor ativo**, não contra o conjunto de setores do usuário

---

### Casos de Teste Básicos

#### **CT-B01 Opção de cancelar aparece para Adm atuando pelo setor dono**

**Dado** um documento com setor responsável CIM e um despacho criado por outro servidor
**E** um servidor administrador multissetor envolvido no despacho
**Quando** ele atuar **pelo CIM** e abrir o menu do despacho
**Então** a opção "Cancelar despacho" é exibida

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:** `10596 - opcao de cancelar despacho nao aparece para adm.mp4`

---

#### **CT-B02 Opção não aparece para Adm atuando por setor que não é o dono**

**Dado** o mesmo documento e o mesmo servidor
**E** que ele não seja autor do despacho
**Quando** ele atuar **por outro setor**, mesmo sendo administrador nele
**Então** a opção "Cancelar despacho" **não** é exibida

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:** `10596 - opcao de cancelar despacho nao aparece para adm.mp4`

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] — o cenário surgiu durante a validação do cancelamento de despacho, que é entrega dessa funcionalidade.

- Observações:
    - **Motivo do descarte: comportamento conforme a regra.** A doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] define a permissão de cancelar por **duas trilhas alternativas** — setor dono **ou** autoria. O cenário reportado não satisfaz nenhuma: o servidor não estava atuando pelo setor dono e não era autor do despacho. Não há defeito.
    - **O que fechou o veredito foi um quarto cenário, validado pelo Rafael**: o **autor** do despacho consegue cancelar **mesmo sendo Administrador** e não N2. Isso confirmou que a trilha de autoria vale para **qualquer nível** e que o produto aplica "setor dono OU autoria" de forma coerente nos quatro casos testados.
    - ⚠️ **A investigação achou um erro na doc, não no produto.** A página do módulo dizia "Usuário básico cancela **apenas** despacho de sua própria autoria", o que fazia parecer que a autoria era exclusividade do N2 — e gerou uma suspeita de inversão (um N2 autor poderia cancelar e um Adm autor não). **Essa inversão não existe no produto**; era artefato da redação. A tabela de permissão da doc foi corrigida em 04/08/2026, com o registro em "Comportamentos observados em teste".
    - **O que segue em aberto e não afeta este descarte**: a permissão de **retificar** continua com três formulações incompatíveis no vault, e o cenário que as separa é "Adm do setor dono que não criou o despacho". Registrado nas Dúvidas em aberto da doc do módulo.
    - Este card nasceu direto em `99 Arquivo/` com `status: descartado`, conforme a regra de **descarte sem card prévio no vault** ([[Sistema/Contexto/PADROES_QA|PADROES_QA]]) — a task existia só no Notion. Diferente do precedente da SGV-3413, aqui **havia material**: cenário detalhado pelo Rafael e evidência gravada, então descrição e passo a passo são reais, não inferidos do título.

- Histórico:
    - 2026-08-04 - 🔎 Análise em DEV: comportamento cruzado contra a regra de permissão da doc do módulo
    - 2026-08-04 - 🗑️ Descartado (não é bug: comportamento conforme a regra — permissão por setor dono ou autoria)
