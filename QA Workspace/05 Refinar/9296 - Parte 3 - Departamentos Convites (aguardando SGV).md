# (9+) [Parte 3] Departamentos: Convites | Notion

[Skip to content](https://app.notion.com/p/alfa-group/Parte-3-Departamentos-Convites-3c82aec67d3080fa9777e34e8768b410#main)

# [Parte 3] Departamentos: Convites

ID

6

📥 Backlog

[Dev][Parte 3] Convites

Comments

![Rafael Borges](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fpublic.notion-static.com%2Fef939fea-d3ec-4519-9090-25b740848ed4%2FPerfil1.jpeg?width=240&userId=214d872b-594c-812d-a2fc-00029f132614&cache=v2&imgBuildSrc=requestProxiedImageUrl)

## Objetivo

Permitir a entrada de participantes em departamentos por links de convite e o filtro de solicitações por departamento.

## Requisitos funcionais

### RF01 — Link permanente do departamento

### História de usuário

> Como responsável por um departamento,
>
> quero receber um link permanente de convite,
>
> para permitir novos cadastros no departamento.

### Critérios de aceite

#### CA01 — Geração do link

Dado que um departamento seja criado,

quando a criação for concluída,

então o sistema deverá gerar um link de convite sem expiração e sem limite de uso.

#### CA02 — Envio por e-mail

Dado que o departamento tenha sido criado,

quando o e-mail de notificação for enviado ao departamento,

então a mensagem deverá conter o link permanente de convite.

### RF02 — Link temporário gerado por servidor

### História de usuário

> Como servidor,
>
> quero gerar um link de convite para um departamento,
>
> para convidar uma pessoa com acesso único e temporário.

### Critérios de aceite

#### CA01 — Geração pela lista de cidadãos

Dado que o servidor esteja na lista de cidadãos,

quando selecionar “Convidar via link” no menu de opções de um cidadão,

então deverá escolher um departamento ativo desse cidadão e gerar o convite.

#### CA02 — Geração pela edição do cidadão

Dado que o servidor esteja editando um cidadão,

quando selecionar “Convidar via link” em um departamento,

então o sistema deverá gerar o convite para esse departamento.

#### CA03 — Cópia do link

Dado que o convite seja gerado,

quando a operação for concluída,

então o link deverá ser copiado automaticamente para a área de transferência.

#### CA04 — Validade

Dado que o link tenha sido gerado por um servidor,

quando for utilizado,

então deverá aceitar apenas um cadastro e expirar após 7 dias.

#### CA05 — Link inválido

Dado que o link já tenha sido utilizado ou esteja expirado,

quando alguém tentar acessá-lo,

então o sistema deverá impedir o cadastro e informar que o convite não é válido.

#### CA06 — Dados persistidos no convite

Dado que um convite seja gerado por um servidor,

quando o convite for criado,

então o sistema deverá persistir o servidor que gerou o link.

E dado que o link seja utilizado para concluir um cadastro,

quando o cidadão concluir o cadastro,

então o sistema deverá persistir no convite o cidadão cadastrado.

### RF03 — Entrada no departamento pelo convite

### História de usuário

> Como pessoa convidada,
>
> quero acessar o convite com ou sem uma conta no SOGOV,
>
> para entrar no departamento informando minha função.

### Critérios de aceite

#### CA01 — Pessoa com cadastro

Dado que a pessoa convidada já possua cadastro no SOGOV,

quando acessar um convite válido,

então deverá realizar login, informar sua função e confirmar a entrada no departamento.

#### CA02 — Pessoa sem cadastro

Dado que a pessoa convidada não possua cadastro no SOGOV,

quando acessar um convite válido,

então deverá concluir o cadastro, informar sua função e confirmar a entrada no departamento.

#### CA03 — Vínculo com o departamento

Dado que a pessoa conclua o fluxo de um convite válido,

quando confirmar sua função,

então deverá ser adicionada como participante do departamento.

### RF04 — Filtro de solicitações por departamento

### História de usuário

> Como cidadão participante de departamentos,
>
> quero filtrar minhas solicitações por perfil,
>
> para visualizar as solicitações pessoais ou de um departamento.

### Critérios de aceite

#### CA01 — Valor padrão

Dado que o cidadão acesse a tela de solicitações,

quando o seletor de perfil for exibido,

então o valor padrão deverá ser “Perfil pessoal”.

#### CA02 — Departamentos disponíveis

Dado que o cidadão participe de departamentos,

quando abrir o seletor,

então deverão ser listados os CNPJs e seus respectivos departamentos conforme o Figma.

#### CA03 — Aplicação do filtro

Dado que o cidadão selecione um departamento,

quando a seleção for aplicada,

então a tela deverá exibir somente as solicitações relacionadas ao departamento escolhido.

#### CA04 — Perfil pessoal

Dado que o cidadão selecione “Perfil pessoal”,

quando a seleção for aplicada,

então a tela deverá exibir todas as suas solicitações.

>