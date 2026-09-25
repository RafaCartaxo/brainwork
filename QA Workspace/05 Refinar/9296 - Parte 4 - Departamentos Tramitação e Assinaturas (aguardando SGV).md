# (9+) [Parte 4] Departamentos: Tramitação e assinaturas | Notion

[Skip to content](https://app.notion.com/p/alfa-group/Parte-4-Departamentos-Tramita-o-e-assinaturas-3de2aec67d308056b324dd227160881c#main)

# [Parte 4] Departamentos: Tramitação e assinaturas

ID

9

📥 Backlog

[Dev][Parte 4] Tramitação

Comments

![Rafael Borges](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fpublic.notion-static.com%2Fef939fea-d3ec-4519-9090-25b740848ed4%2FPerfil1.jpeg?width=240&userId=214d872b-594c-812d-a2fc-00029f132614&cache=v2&imgBuildSrc=requestProxiedImageUrl)

## Objetivo

Permitir a tramitação e a solicitação de assinatura para departamentos e seus membros, garantindo a identificação correta dos destinatários, o envio das notificações e o fluxo de assinatura para pessoas com ou sem cadastro no SOGOV.

## Requisitos funcionais

### RF01 — Tramitação para membro de departamento

### História de usuário

> Como usuário responsável por uma tramitação,
>
> quero localizar e selecionar um membro de departamento,
>
> para encaminhar a tramitação diretamente à pessoa responsável dentro da organização.

### Critérios de aceite

CA01 — Busca de membros nos campos de cidadão PJ

Dado que um campo permita pesquisar cidadãos PJ,

quando o usuário realizar uma busca,

então o sistema deverá listar, além dos departamentos correspondentes, os cidadãos membros desses departamentos que correspondam à busca.

CA02 — Identificação do tipo de resultado

Dado que a busca retorne departamentos e seus membros,

quando os resultados forem exibidos,

então o sistema deverá permitir distinguir visualmente um departamento de um membro, conforme o padrão definido no Figma.

CA03 — Seleção do membro

Dado que um membro de departamento seja exibido no resultado da busca,

quando o usuário selecioná-lo,

então o sistema deverá adicioná-lo à tramitação vinculado ao respectivo departamento.

### RF02 — Notificações da tramitação para membro de departamento

### História de usuário

> Como membro de um departamento incluído em uma tramitação,
>
> quero ser notificado pelos canais disponíveis,
>
> para tomar conhecimento e acompanhar a tramitação.

### Critérios de aceite

CA01 — Notificação do membro

Dado que um membro de departamento seja adicionado a uma tramitação,

quando a tramitação for efetivada,

então o sistema deverá notificar o membro por e-mail e por notificação interna.

CA02 — Notificação do departamento

Dado que um membro de departamento seja adicionado a uma tramitação,

quando as notificações forem enviadas,

então o e-mail do departamento também deverá continuar recebendo a notificação.

CA03 — Conteúdo das notificações

Dado que a tramitação seja destinada a um membro de departamento,

quando as notificações forem geradas,

então seu conteúdo e sua apresentação deverão seguir o padrão definido no Figma.

### RF03 — Exibição de membro de departamento na tramitação

### História de usuário

> Como usuário que consulta uma tramitação,
>
> quero identificar o membro selecionado, seu cargo e seu departamento,
>
> para compreender corretamente quem participa do fluxo.

### Critérios de aceite

CA01 — Padrão de exibição

Dado que um membro de departamento tenha sido adicionado à tramitação,

quando sua identificação for exibida,

então

o sistema deverá utilizar o padrão:

$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)

.

CA02 — Consistência da exibição

Dado que o membro apareça em diferentes componentes da tramitação,

quando sua identificação for renderizada,

então o padrão deverá ser aplicado de forma consistente nos locais previstos no Figma.

### RF04 — Exibição de membro de departamento em PDFs

### História de usuário

> Como usuário que gera ou consulta um PDF,
>
> quero visualizar corretamente os dados do membro de departamento,
>
> para identificar a pessoa, o cargo e a organização representada.

### Critérios de aceite

CA01 — Identificação no PDF

Dado que um membro de departamento tenha sido selecionado em uma tramitação,

quando o PDF correspondente for gerado,

então

sua identificação deverá seguir o padrão:

$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)

.

CA02 — Campo do tipo pessoa

Dado que um campo do tipo pessoa esteja preenchido com um membro de departamento,

quando um PDF que contenha esse campo for gerado,

então o mesmo padrão de identificação deverá ser aplicado.

### RF05 — Solicitação de assinatura para departamento

### História de usuário

> Como solicitante de assinatura,
>
> quero solicitar a assinatura de um departamento,
>
> para permitir que qualquer membro apto desse departamento assine o documento.

### Critérios de aceite

CA01 — Seleção do departamento

Dado que o usuário esteja configurando uma solicitação de assinatura,

quando pesquisar e selecionar um departamento,

então o departamento deverá ser adicionado como signatário.

CA02 — Membros aptos a assinar

Dado que a assinatura tenha sido solicitada a um departamento,

quando um membro desse departamento acessar a solicitação,

então deverá estar apto a realizar a assinatura.

CA03 — Restrição de assinatura via token

Dado que o signatário selecionado seja um departamento,

quando o solicitante configurar a assinatura,

então o sistema não deverá permitir a solicitação de assinatura via token.

CA04 — Header do componente signatário

Dado que um departamento tenha sido adicionado como signatário,

quando o componente signatário for exibido,

então seu header deverá seguir o padrão definido no Figma.

CA05 — Eventos de assinatura

Dado que ocorram eventos relacionados à assinatura solicitada a um departamento,

quando esses eventos forem exibidos,

então o componente de eventos deverá identificar corretamente o departamento conforme o Figma.

CA06 — Notificação do departamento

Dado que uma assinatura seja solicitada a um departamento,

quando a solicitação for criada,

então o sistema deverá enviar a notificação ao e-mail do departamento.

### RF06 — Solicitação de assinatura para membro de departamento

### História de usuário

> Como solicitante de assinatura,
>
> quero solicitar a assinatura de um membro específico de um departamento,
>
> para direcionar a responsabilidade da assinatura à pessoa selecionada.

### Critérios de aceite

CA01 — Seleção do membro

Dado que o usuário esteja configurando uma solicitação de assinatura,

quando pesquisar e selecionar um membro de departamento,

então o membro deverá ser adicionado como signatário vinculado ao respectivo departamento.

CA02 — Assinatura via token

Dado que o signatário selecionado seja um membro de departamento,

quando o solicitante configurar a assinatura,

então o sistema deverá permitir a solicitação de assinatura via token.

CA03 — Header do componente signatário

Dado que um membro de departamento tenha sido adicionado como signatário,

quando o componente signatário for exibido,

então seu header deverá identificar corretamente o membro e o departamento conforme o Figma.

CA04 — Eventos de assinatura

Dado que ocorram eventos relacionados à assinatura solicitada a um membro,

quando esses eventos forem exibidos,

então o componente de eventos deverá identificar corretamente o membro e o departamento conforme o Figma.

CA05 — Notificação do membro

Dado que uma assinatura seja solicitada a um membro de departamento,

quando a solicitação for criada,

então o sistema deverá notificar o membro por e-mail e por notificação interna.

CA06 — Notificação do departamento

Dado que uma assinatura seja solicitada a um membro de departamento,

quando as notificações forem enviadas,

então o e-mail do departamento também deverá continuar recebendo a notificação.

### RF07 — Fluxo de assinatura para usuário externo

### História de usuário

> Como pessoa que acessa externamente uma solicitação de assinatura destinada a um departamento,
>
> quero me identificar e concluir a assinatura,
>
> para assinar o documento mesmo que eu ainda não seja membro do departamento ou não possua cadastro completo no SOGOV.

### Critérios de aceite

CA01 — Identificação por CPF

Dado que uma pessoa acesse externamente o fluxo de assinatura,

quando iniciar sua identificação,

então o sistema deverá solicitar o CPF e verificar se existe um cadastro correspondente.

CA02 — Pessoa cadastrada e vinculada ao departamento

Dado que o CPF pertença a uma pessoa cadastrada e já vinculada ao departamento destinatário,

quando a identificação for concluída,

então a pessoa deverá informar sua senha e poderá realizar a assinatura.

CA03 — Pessoa cadastrada sem vínculo com o departamento

Dado que o CPF pertença a uma pessoa cadastrada, mas ainda não vinculada ao departamento destinatário,

quando prosseguir com a assinatura,

então a pessoa deverá informar seu cargo, ser vinculada ao departamento e poderá realizar a assinatura.

CA04 — Pré-cadastro de pessoa sem cadastro

Dado que não exista cadastro para o CPF informado,

quando a pessoa prosseguir com a assinatura,

então o sistema deverá solicitar CPF, e-mail e cargo para realizar o pré-cadastro.

CA05 — Termos e declaração de maioridade

Dado que a pessoa esteja realizando o pré-cadastro,

quando confirmar seus dados,

então deverá aceitar os termos aplicáveis e declarar ser maior de idade no modal definido no Figma.

CA06 — Criação do pré-cadastro e vínculo

Dado que a pessoa sem cadastro informe dados válidos e forneça os consentimentos obrigatórios,

quando confirmar o pré-cadastro,

então o sistema deverá criar o pré-cadastro e vinculá-la ao departamento com o cargo informado.

CA07 — Assinatura após o pré-cadastro

Dado que o pré-cadastro tenha sido concluído com sucesso,

quando o vínculo com o departamento for criado,

então a pessoa deverá poder realizar a assinatura no mesmo fluxo.

CA08 — Convite para conclusão do cadastro

Dado que a pessoa tenha assinado por meio de um pré-cadastro,

quando a assinatura for concluída,

então o sistema deverá enviar um e-mail com as instruções para completar o cadastro no SOGOV.

CA09 — Validações e mensagens de erro

Dado que ocorra uma inconsistência na identificação, autenticação, vinculação ou criação do pré-cadastro,

quando não for possível prosseguir,

então o sistema deverá impedir a assinatura e apresentar uma mensagem de erro adequada, sem criar vínculos ou cadastros duplicados.

## Pontos para validação

Confirmar no Figma o padrão visual dos resultados de busca de departamentos e membros.

Confirmar no Figma o conteúdo e a apresentação das notificações.

Confirmar no Figma a aplicação do padrão de identificação nas telas e nos PDFs.

Confirmar no Figma os headers dos componentes de signatário para departamento e membro.

Confirmar no Figma a apresentação dos eventos de assinatura.

Confirmar no Figma o modal de pré-cadastro, aceite dos termos e declaração de maioridade.

>