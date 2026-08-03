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

Durante validação foi identificado que, quando um **servidor** edita o cadastro de um **cidadão PJ** e tenta alterar o e-mail, o sistema pede a **senha do usuário atual** (a do próprio servidor) para confirmar a alteração — e, quando essa senha é informada **incorretamente**, nenhum feedback é exibido. Não há mensagem de erro, nem indicação no campo, nem aviso de que a senha está errada: **nada acontece**. Para o servidor, a tela parece quebrada, quando o único problema é a senha estar incorreta.

---

### Passo a passo para reproduzir

Dado que o usuário esteja logado como **servidor**
E acesse a área de cadastro de um **cidadão PJ**
E entre na edição desse cadastro para alterar o e-mail
E o sistema solicite a senha do usuário atual para confirmar
Quando informar uma senha **incorreta** e confirmar
Então verifico que nada acontece — sem mensagem de erro e sem indicação de que a senha está incorreta — e a alteração não é concluída

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10549)

![[10549 - senha incorreta nao retorna feedback na alteracao de e.mp4]]


---

### Resultado Esperado

Ao informar uma senha incorreta na confirmação, o sistema exibe mensagem de erro dizendo que a senha está incorreta e mantém o servidor na etapa da senha, com o novo e-mail já digitado preservado, para tentar novamente. É o mesmo tratamento que o **Login** já dá a credencial inválida: a doc do módulo registra que a mensagem de erro é exibida (com o e-mail anonimizado) e que 5 erros bloqueiam a conta — ou seja, senha errada nesse produto **tem** retorno visível; esta tela é a exceção.

---

### Critérios de aceite

- [ ] Senha incorreta na confirmação exibe mensagem de erro informando que a senha está incorreta
- [ ] O servidor permanece na etapa da senha e consegue tentar de novo, sem perder o novo e-mail já digitado
- [ ] Com a senha correta, o e-mail do cidadão PJ é alterado normalmente (sem regressão)
- [ ] Errar a senha nessa tela tem efeito **definido e visível** sobre o bloqueio de conta por 5 tentativas *(hoje, sem feedback nenhum, o servidor pode bloquear a própria conta sem saber por quê — comportamento a confirmar com produto; ver Observações)*

---

### Casos de Teste Básicos

#### **CT-B01 Senha incorreta exibe mensagem de erro**

**Dado** que o servidor esteja editando o cadastro de um cidadão PJ
**E** esteja na etapa de senha da alteração de e-mail
**Quando** informar uma senha incorreta e confirmar
**Então** é exibida mensagem de erro informando que a senha está incorreta

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Usuário consegue tentar de novo sem reescrever o e-mail**

**Dado** que o servidor tenha informado a senha incorreta e recebido a mensagem de erro
**Quando** informar a senha correta na sequência
**Então** a alteração de e-mail conclui, sem que ele precise digitar o novo e-mail outra vez

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Alteração de e-mail com senha correta segue funcionando (regressão)**

**Dado** que o servidor esteja editando o cadastro de um cidadão PJ
**E** informe o novo e-mail
**Quando** informar a senha correta e confirmar
**Então** o e-mail do cidadão é alterado com sucesso e a confirmação prevista no fluxo é exibida

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
    - 🔍 **Vale testar a validação vizinha na mesma tela.** A doc define que o **e-mail institucional é único no sistema**. Se essa tela engole o erro de senha, cabe verificar se engole também o de **e-mail duplicado** — se as duas validações são silenciosas, o defeito é do tratamento de erro da tela, não da checagem de senha, e isso muda o diagnóstico do dev.
    - ❓ **Escopo a diagnosticar**: observado com o **servidor editando cadastro de cidadão PJ**. Faltam duas superfícies vizinhas: o servidor editando o e-mail de um cidadão **PF**, e o **cidadão alterando o próprio e-mail** (meu perfil, autosserviço). Se o silêncio acontecer nas três, o defeito é da **etapa de confirmação por senha** e não do fluxo PJ, e o alcance da correção muda. Pendência aberta na fila.
    - Número **SGV-10549 reservado** pelo Rafael; o cadastro no Notion é dele e entra depois (pendência na fila). O card nasce com o número no nome justamente pra não precisar renomear card, `task`, evidência e wikilinks depois.

- Histórico:
    - 2026-08-03 - 🐛 Bug confirmado (card criado)
    - 2026-08-03 - 📝 Cenário corrigido pelo Rafael: o ator é o **servidor** editando o cadastro do cidadão PJ, não o cidadão alterando o próprio e-mail (versão inicial do card estava errada nesse ponto). Descrição, passos, critérios e os 3 CTs reescritos
