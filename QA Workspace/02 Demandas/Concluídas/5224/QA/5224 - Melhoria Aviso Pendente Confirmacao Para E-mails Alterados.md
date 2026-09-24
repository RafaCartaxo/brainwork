---
tags:
  - demanda
  - qa
  - melhoria
  - perfil
task: "5224"
status: resolvido
prioridade: media
data_inicio: 2026-08-14
data_fim: "2026-08-14"
responsavel: Rafael
modulo: perfil
ambiente: HML
---
# Demanda: Aviso "pendente confirmação" para e-mails alterados e ainda não confirmados

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** Concluída (aprovada em homologação em 14/08/2026)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-5224 no Notion](https://app.notion.com/p/alfa-group/Melhoria-Implementa-o-de-aviso-pendente-confirma-o-para-e-mails-rec-m-alterados-que-ainda-n-o-f-2572aec67d3080d58778de0f163f3332) · Figma — Ambiente Servidor/Handoff: [nó 2849-1113](https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=2849-1113) · [Plano de testes](https://app.notion.com/p/Execu-o-Plano-de-testes-SGV-5224-3ba2aec67d308079bdcbddb1405f07e9)
> - **Dev:** B. Luan · **Revisores MR:** Marcos Vinicius, Gabriel Desidério
> - **Design:** Ivo Costa
> - **Módulo (doc oficial SoGov):** Perfil (Minha conta) · **Projeto:** Sustentação
> - **Versão validada:** 12.40.44.2 (Homolog 13/08/2026)
> - **Progresso de subitens:** 83,33% · Sprints: SP6, SP7, SP14, SP15, SP16, SP17 (2026)

---

> [!abstract] Resumo

Ao alterar o e-mail, a interface exibia a mudança **imediatamente**, mas a alteração só passa a valer depois que o usuário confirma pelo link enviado ao novo endereço. Como isso não era comunicado, o usuário podia acreditar que já estava usando o e-mail novo — e agir com base nisso (tentar recuperação de senha, esperar notificações no endereço novo).

A melhoria pede um estado **"Pendente de confirmação"** ao lado do e-mail alterado, uma mensagem imediata dizendo pra onde o link foi enviado, e a possibilidade de **reenviar** o e-mail de confirmação.

Atinge **duas telas**: a do **Servidor** e a do **Cidadão**.

Módulo relacionado: **Perfil (Minha conta)** — ainda não importado pra `04 Conhecimento/Módulos/` (pendência de fluxo 8 registrada na daily).

---

## Regras de negócio

Transcritas da task (a melhoria nasceu como proposta de UX, não passou por refinamento neste vault):

- Enquanto a confirmação não acontece, o e-mail **antigo continua sendo o principal** — o novo é só um endereço pendente.
- O estado **"Pendente de confirmação"** fica visível ao lado do e-mail alterado até a confirmação.
- A mensagem imediata deve dizer **para qual endereço** o link foi enviado. Exemplos da task: *"Enviamos um link para novoemail@exemplo.com. Confirme por lá para concluir a troca de e-mail."* / *"Confirme no link enviado para novoemail@exemplo.com. Até lá, seu e-mail principal continua sendo antigoemail@exemplo.com."*
- Deve ser possível **reenviar** o e-mail de confirmação caso não chegue.

**Pontos que a task deixou em aberto com UX/Design**: qual padrão visual usar; como exibir o estado "pendente" sem poluir a tela; se o reenvio é liberado ao usuário; e o alinhamento entre a copy do e-mail de confirmação e a da interface.

---

> [!warning] Pontos de atenção

- ⚠️ **A entrega foi só visual.** Comentário do dev B. Luan na task (12/08/2026): *"Pelo que eu entendi, o fluxo executado nos vídeos não causa pendência de email, pelo que eu olhei no banco de dados. Essa tarefa só cobriu a aparência visual, não houve mudança na api."* Ou seja: o aviso aparece, mas o **estado de pendência real no banco** não foi objeto desta task — o que significa que a aprovação cobre a exibição, não o ciclo completo de confirmação.
- 🔗 **Existe defeito irmão em aberto**: a task registra `SGV-10773` — *[Defeito] Não está sendo exibida tag de confirmação no perfil cidadão PF/PJ após alteração de e-mail* — como **"Impactado por"**. Como esta melhoria atinge as duas telas (Servidor e Cidadão) e o defeito é do lado **Cidadão**, vale conferir se a aprovação de 14/08 cobriu a tela do cidadão ou só a do servidor.
- ⚠️ **Sem gate de doc.** O módulo oficial (**Perfil (Minha conta)**) não existe em `04 Conhecimento/Módulos/`, então a aprovação foi registrada sem o cruzamento contra documentação que o [[Sistema/Contexto/FLUXOS#3b–3d. Validar em DEV / HML / Hotfix|FLUXOS 3b–3d]] exige. Pendência de importar registrada na fila.
- 🔎 A demanda **arrasta desde a SP6** e passou por seis sprints (SP6, SP7, SP14, SP15, SP16, SP17), com seis datas previstas de conclusão sucessivas.
- Os campos "Passo a passo para reproduzir", "Comportamento atual" e "Comportamento esperado" estão **vazios** no Notion — o escopo vive só na Descrição.

---

## Casos de teste

*Nenhum escrito neste vault* — a validação foi executada a partir do [plano de testes no Notion](https://app.notion.com/p/Execu-o-Plano-de-testes-SGV-5224-3ba2aec67d308079bdcbddb1405f07e9), e o card nasceu depois da aprovação, para dar rastreabilidade.

---

> [!danger] Bugs encontrados

- `SGV-10773` - Não está sendo exibida tag de confirmação no perfil cidadão PF/PJ após alteração de e-mail — registrado na task como **"Impactado por"**. Sem card neste vault.

---

## Evidências

![[5224 - EV-01 - aviso pendente confirmacao para e-mails alterados.mp4]]

---

> [!tip] Observações

Aprovação registrada por mim na task em 14/08/2026: *"Status: Aprovado · Versão: 12.40.44.2"*.

O card foi criado no vault em 17/08, retroativo — a validação aconteceu na sexta (14/08) e ficou sem registro porque a sessão de trabalho atravessou o fim de semana.

---

## Histórico

- 2026-08-14 - ✅ Melhoria aprovada em homologação (versão 12.40.44.2)
- 2026-08-17 - Card criado no vault a partir do export da task, retroativo à aprovação de 14/08
