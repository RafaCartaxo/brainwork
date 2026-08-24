---
tags:
  - bug
  - qa
  - despachos
  - usuario-cidadao
task: "9369"
prioridade: media
status: aberto
data_inicio: 2026-08-17
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: despachos
ambiente: DEV
---
# Cidadão consegue mencionar servidores via "@" no campo de despacho

### Descrição

Durante validação foi identificado que, ao realizar um despacho **logado como cidadão**, ao digitar `@` no campo de texto o sistema abre a listagem de menção e permite mencionar **servidores cadastrados na plataforma**.

A funcionalidade de menção é exclusiva de servidores — o ambiente cidadão não deveria oferecer o gatilho nem retornar servidores na busca.

---

### Passo a passo para reproduzir

Dado que estou logado como **cidadão**
E acesso uma demanda possível de responder
E clico em **"Responder"**
Quando é exibido o campo de texto
E insiro o caractere `@`
Então verifico que é possível mencionar vários servidores cadastrados na plataforma

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://9369)

![[9369 - cidadão não menciona ok.mp4]]


---

### Resultado Esperado

- O campo de texto do despacho **no ambiente cidadão não oferece a menção via `@`**: o caractere é tratado como texto comum e nenhuma listagem de sugestão é aberta
- Nenhum servidor da plataforma é exposto ao cidadão por essa via

---

### Critérios de aceite

- [ ] Logado como **cidadão**, digitar `@` (com ou sem os 3 caracteres do gatilho) no campo de despacho **não abre a listagem de menção**
- [ ] Nenhum nome de servidor é retornado ao cidadão em qualquer campo de texto aberto do ambiente cidadão (abertura, resposta, despacho)
- [ ] O `@` digitado pelo cidadão é preservado como **texto comum** no corpo do despacho, sem virar chip de menção
- [ ] **Regressão**: logado como **servidor**, a menção via `@` continua funcionando normalmente (gatilho de `@` + 3 caracteres, chip com nome + sigla da unidade)

---

### Casos de Teste Básicos

#### **CT-B01 Cidadão não tem menção via "@" no campo de despacho**

**Dado** que estou logado como **cidadão**
**E** acesso uma demanda possível de responder
**E** clico em **"Responder"**
**Quando** insiro `@` seguido de 3 caracteres no campo de texto
**Então** verifico que nenhuma listagem de menção é aberta e nenhum servidor é sugerido

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

---

#### **CT-B02 "@" do cidadão é preservado como texto comum**

**Dado** que estou logado como **cidadão**
**E** estou com o campo de texto do despacho aberto
**Quando** escrevo um texto contendo `@` e emito o despacho
**Então** verifico que o `@` aparece como texto comum no despacho emitido, sem chip de menção

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 Regressão — servidor mantém a menção via "@"**

**Dado** que estou logado como **servidor**
**E** acesso um processo em que estou envolvido
**Quando** insiro `@` + 3 caracteres iniciais de um servidor envolvido no processo
**Então** verifico que a listagem é aberta e a seleção renderiza o chip com nome completo + sigla da unidade

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão: a confirmar
- Ambiente: Desenvolvimento — correção ainda a ser desenvolvida pelo dev

---

### Informações adicionais

- Demanda relacionada: menção de servidores via "@" nos processos (`[Melhoria-CX]`, backlog da página de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]]) — SGV da entrega original não identificado nesta sessão
- Observações:
    - **Gate de doc** ([[Sistema/Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]): [[QA Workspace/04 Conhecimento/Módulos/Despachos#Menção de servidores via "@"|Despachos → Menção de servidores via "@"]] respalda o **recorte de quem aparece na busca** ("apenas servidores que estejam envolvidos no processo ou tenham permissão de acesso ao documento"), mas **não escreve a regra de quem pode mencionar** — a regra "somente servidores possuem o poder de mencionar" está na especificação da funcionalidade e **não foi importada** pro vault. Pendência de atualizar a doc registrada na daily de 17/08.
    - Este defeito viola a **regra 1** (quem pode mencionar). A **regra 2** (quem aparece na busca — envolvido no processo ou com permissão de acesso ao documento) **não foi verificada** nesta sessão e não está coberta pelos critérios acima; cabe caso próprio se falhar.
    - Exposição de dados: a listagem entrega ao cidadão **nome de servidores da plataforma**, o que é o impacto real além do comportamento indevido — vale considerar na priorização.
    - A doc registrava como **dúvida em aberto** se a menção via `@` estava implementada (item de fila parado há 14 dias). Este bug **responde**: está implementada e alcançável pelo ambiente cidadão.
- Histórico:
    - 2026-08-17 - 🐛 Bug cadastrado
