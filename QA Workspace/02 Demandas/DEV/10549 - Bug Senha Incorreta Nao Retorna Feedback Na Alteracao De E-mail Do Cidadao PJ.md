---
tags:
  - bug
  - qa
  - usuario-cidadao
task: "10549"
prioridade: media
status: aberto
data_inicio: 2026-08-03
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: usuario-cidadao
ambiente: DEV
---
# Senha incorreta não retorna feedback na alteração de e-mail do cidadão PJ

### Descrição

Durante validação foi identificado que, quando um **servidor** edita o cadastro de um **cidadão PJ** e aciona a alteração do e-mail, o sistema **primeiro** pede a **senha do usuário atual** (a do próprio servidor) — e só **depois** da senha correta é que o campo de e-mail aparece para ser trocado. A senha é a **porta de entrada** do fluxo, não uma confirmação no final.

Quando essa senha é informada **incorretamente**, nenhum feedback é exibido: não há mensagem de erro, nem indicação no campo, nem aviso de que a senha está errada. **Nada acontece** — e o campo de e-mail nunca é liberado. Para o servidor, a tela parece quebrada, sem caminho pra seguir e sem saber por quê, quando o único problema é a senha estar incorreta.

---

### Passo a passo para reproduzir

Dado que o usuário esteja logado como **servidor**
E acesse a área de cadastro de um **cidadão PJ**
E entre na edição desse cadastro e acione a alteração do e-mail
E o sistema solicite a senha do usuário atual antes de liberar o campo de e-mail
Quando informar uma senha **incorreta** e confirmar
Então verifico que nada acontece — sem mensagem de erro e sem indicação de que a senha está incorreta — e o campo de e-mail não é liberado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10549)

![[10549 - senha incorreta nao retorna feedback na alteracao de e.mp4]]


---

### Resultado Esperado

Ao informar uma senha incorreta, o sistema exibe mensagem de erro dizendo que a senha está incorreta e mantém o servidor na etapa da senha, podendo tentar novamente sem sair da tela. Com a senha correta, o campo de e-mail é liberado e a alteração segue normalmente.

É o mesmo tratamento que o **Login** já dá a credencial inválida: a doc do módulo registra que a mensagem de erro é exibida (com o e-mail anonimizado) e que 5 erros bloqueiam a conta — ou seja, senha errada nesse produto **tem** retorno visível; esta tela é a exceção. E como aqui a senha é o que **libera o campo**, ficar sem retorno deixa o servidor sem caminho nenhum: ele não erra um passo do fluxo, ele não consegue entrar nele.

---

### Critérios de aceite

- [ ] Senha incorreta exibe mensagem de erro informando que a senha está incorreta, em vez de não acontecer nada
- [ ] O servidor permanece na etapa da senha e consegue tentar de novo sem sair da tela nem reiniciar a edição
- [ ] Com a senha correta, o **campo de e-mail é liberado** e a alteração do e-mail do cidadão PJ conclui normalmente (sem regressão)
- [ ] Errar a senha nessa tela tem efeito **definido e visível** sobre o bloqueio de conta por 5 tentativas *(hoje, sem feedback nenhum, o servidor pode bloquear a própria conta sem saber por quê — comportamento a confirmar com produto; ver Observações)*

---

### Casos de Teste Básicos

#### **CT-B01 Senha incorreta exibe mensagem de erro e não libera o campo de e-mail**

**Dado** que o servidor esteja editando o cadastro de um cidadão PJ
**E** tenha acionado a alteração do e-mail, com o sistema pedindo a senha do usuário atual
**Quando** informar uma senha incorreta e confirmar
**Então** é exibida mensagem de erro informando que a senha está incorreta
**E** o campo de e-mail continua não liberado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Servidor consegue tentar a senha de novo depois do erro**

**Dado** que o servidor tenha informado a senha incorreta e recebido a mensagem de erro
**Quando** informar a senha correta na sequência, sem sair da tela
**Então** o campo de e-mail é liberado e ele consegue alterar o e-mail normalmente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Alteração de e-mail com senha correta segue funcionando (regressão)**

**Dado** que o servidor esteja editando o cadastro de um cidadão PJ
**E** tenha acionado a alteração do e-mail
**Quando** informar a senha correta de primeira
**Então** o campo de e-mail é liberado, o novo e-mail é gravado e a confirmação prevista no fluxo é exibida

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento (posição na esteira de correção)

> [!info]- Origem: reproduz em DEV e em homologação
> Observado primeiro em **DEV** e confirmado também em **homologação** pelo Rafael em 03/08/2026, durante a execução dos CTs da melhoria de CNPJ ([[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]]). Reproduzir nos dois ambientes é o que sustenta a classificação de **pré-existente**.
>
> O card mora em `DEV/` com `ambiente: DEV` porque o campo reflete a **posição na esteira de correção**, não o último ambiente testado ([[Sistema/Contexto/PADROES_QA|PADROES_QA]] → Organização de Bugs).

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — encontrado **durante** a validação dela, mas **não é regressão** e **não é CT dela**: já existia antes e não tem relação com o formato de CNPJ. Mesmo tratamento dado à [[QA Workspace/02 Demandas/DEV/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]] e à [[QA Workspace/02 Demandas/DEV/10517 - Bug Busca Do Campo De Solicitante Nao Retorna Resultado Com Mascara|SGV-10517]], também achadas na mesma frente. Nenhum critério da 9493 é afetado.

- Observações:
    - **Gate de doc — lacuna no módulo, com âncora transversal.** A doc de [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão#1. Cadastro interno da pessoa jurídica (feito por um servidor)|Usuário Cidadão § Cadastro interno da PJ (feito por um servidor)]] cobre exatamente esta superfície, mas só os **campos de criação** — não diz nada sobre **edição** de cadastro já existente, nem sobre a **confirmação por senha**, nem sobre o retorno de senha inválida. Lacuna registrada nas Dúvidas em aberto da doc. O respaldo do resultado esperado vem do módulo [[QA Workspace/04 Conhecimento/Módulos/Login|Login]], que documenta que credencial inválida **exibe** mensagem de erro (com o e-mail anonimizado): é analogia entre superfícies, não regra escrita para esta tela.
    - ⚠️ **Risco que o silêncio esconde — e aqui a conta é do servidor.** A doc do Login registra que **errar a senha 5 vezes bloqueia a conta**, em todos os ambientes. A senha pedida nessa tela é a do **usuário atual, o próprio servidor**. Se a tentativa contar para esse limite, o servidor **bloqueia a própria conta de trabalho sem receber aviso nenhum**, no meio de uma rotina de cadastro — e sem feedback ele naturalmente tenta de novo, o que acelera o bloqueio. É o que faz esse bug ser mais que um incômodo de usabilidade. É o 4º critério, e depende de confirmação de produto.
    - 🔍 **Vale testar a validação do passo seguinte.** Depois que a senha libera o campo, a próxima validação do fluxo é a de **e-mail único no sistema** (regra da doc do módulo). Se o erro de senha é engolido, cabe verificar se o de **e-mail duplicado** também é — se as duas forem silenciosas, o defeito é do **tratamento de erro dessa tela**, não da checagem de senha, e o dev procura em outro lugar.
    - 💡 **A senha é porta de entrada, não confirmação — e é isso que explica o sintoma.** Em fluxos onde a senha confirma uma ação no final, errar a senha ainda deixa o usuário vendo o que ele tentou fazer. Aqui a senha **libera o campo**: sem retorno, o servidor não erra um passo do fluxo, ele **não consegue entrar nele** — fica olhando uma tela que não reage, sem nada pra corrigir. Vale como argumento de prioridade.
    - ❓ **Escopo a diagnosticar**: observado com o **servidor editando cadastro de cidadão PJ**. Faltam duas superfícies vizinhas: o servidor editando o e-mail de um cidadão **PF**, e o **cidadão alterando o próprio e-mail** (meu perfil, autosserviço). Se o silêncio acontecer nas três, o defeito é da **etapa de confirmação por senha** e não do fluxo PJ, e o alcance da correção muda. Pendência aberta na fila.
    - Número **SGV-10549 reservado** pelo Rafael; o cadastro no Notion é dele e entra depois (pendência na fila). O card nasce com o número no nome justamente pra não precisar renomear card, `task`, evidência e wikilinks depois.

- Histórico:
    - 2026-08-03 - 🐛 Bug confirmado (card criado)
    - 2026-08-03 - 📝 Cenário corrigido pelo Rafael: o ator é o **servidor** editando o cadastro do cidadão PJ, não o cidadão alterando o próprio e-mail (versão inicial do card estava errada nesse ponto). Descrição, passos, critérios e os 3 CTs reescritos
