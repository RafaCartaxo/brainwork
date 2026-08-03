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

Durante validação foi identificado que, ao alterar o e-mail de um cidadão PJ, o sistema pede a senha do usuário atual antes de concluir a alteração — e, quando a senha informada está **incorreta**, nenhum feedback é exibido. Não há mensagem de erro, nem indicação no campo, nem aviso de que a senha está errada: o fluxo simplesmente não conclui. Para quem está usando, a tela parece quebrada, quando o único problema é a senha estar incorreta.

---

### Passo a passo para reproduzir

Dado que o usuário esteja logado como cidadão PJ
E acesse a alteração do e-mail do seu cadastro
E o sistema solicite a senha do usuário atual
Quando informar uma senha **incorreta** e confirmar
Então verifico que nenhum feedback é exibido — sem mensagem de erro e sem indicação de que a senha está incorreta — e a alteração não é concluída

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10549)


---

### Resultado Esperado

Ao informar uma senha incorreta na confirmação da alteração de e-mail, o sistema exibe mensagem de erro dizendo que a senha está incorreta e mantém o usuário na etapa da senha, com o novo e-mail já digitado preservado, para tentar novamente. É o mesmo tratamento que o **Login** já dá a credencial inválida: a doc do módulo registra que a mensagem de erro é exibida (com o e-mail anonimizado) e que 5 erros bloqueiam a conta — ou seja, senha errada nesse produto **tem** retorno visível; esta tela é a exceção.

---

### Critérios de aceite

- [ ] Senha incorreta na confirmação da alteração de e-mail exibe mensagem de erro informando que a senha está incorreta
- [ ] O usuário permanece na etapa da senha e consegue tentar de novo, sem perder o novo e-mail já digitado
- [ ] Com a senha correta, a alteração de e-mail conclui normalmente (sem regressão)
- [ ] Errar a senha nessa tela tem efeito **definido e visível** sobre o bloqueio de conta por 5 tentativas *(hoje, sem feedback nenhum, é possível bloquear a conta sem saber por quê — comportamento a confirmar com produto; ver Observações)*

---

### Casos de Teste Básicos

#### **CT-B01 Senha incorreta exibe mensagem de erro**

**Dado** que o usuário esteja logado como cidadão PJ
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

**Dado** que o usuário tenha informado a senha incorreta e recebido a mensagem de erro
**Quando** informar a senha correta na sequência
**Então** a alteração de e-mail conclui, sem que ele precise digitar o novo e-mail outra vez

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Alteração de e-mail com senha correta segue funcionando (regressão)**

**Dado** que o usuário esteja logado como cidadão PJ
**E** esteja alterando o e-mail do seu cadastro
**Quando** informar a senha correta e confirmar
**Então** o e-mail é alterado com sucesso e o usuário recebe a confirmação prevista no fluxo

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
    - **Gate de doc — lacuna no módulo, com âncora transversal.** A doc de [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] descreve as etapas de e-mail e de senha do cadastro PJ, mas **não tem nenhuma regra sobre o retorno de senha incorreta** na alteração de e-mail — a lacuna foi registrada nas Dúvidas em aberto da doc. O respaldo do resultado esperado vem do módulo [[QA Workspace/04 Conhecimento/Módulos/Login|Login]], que documenta que credencial inválida **exibe** mensagem de erro (com o e-mail anonimizado). É analogia entre superfícies, não regra escrita para esta tela.
    - ⚠️ **Risco que o silêncio esconde**: a doc do Login registra que **errar a senha 5 vezes bloqueia a conta**, em todos os ambientes. Se a tentativa nessa tela contar para esse limite, o usuário pode **bloquear a própria conta sem receber aviso nenhum** — é o que faz esse bug ser mais que um incômodo de usabilidade. Confirmar com produto se conta ou não, e documentar a regra. É o 4º critério.
    - ❓ **Escopo a diagnosticar**: só foi observado no cidadão **PJ**. Falta saber se o mesmo silêncio acontece na alteração de e-mail do cidadão **PF** e do **servidor** — se acontecer, o defeito é da etapa de confirmação por senha, não do fluxo PJ, e o alcance da correção muda. Pendência aberta na fila.
    - Número **SGV-10549 reservado** pelo Rafael; o cadastro no Notion é dele e entra depois (pendência na fila). O card nasce com o número no nome justamente pra não precisar renomear card, `task`, evidência e wikilinks depois.

- Histórico:
    - 2026-08-03 - 🐛 Bug confirmado (card criado)
