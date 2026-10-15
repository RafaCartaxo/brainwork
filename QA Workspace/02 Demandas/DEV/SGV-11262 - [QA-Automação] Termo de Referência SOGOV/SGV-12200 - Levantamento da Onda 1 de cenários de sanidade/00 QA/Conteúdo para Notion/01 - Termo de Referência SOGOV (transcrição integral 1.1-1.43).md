# Termo de Referência SOGOV — Transcrição Integral (itens 1.1–1.43)

Transcrição fiel do texto do Termo de Referência, item 1 ("Das Descrições Técnicas da Solução"), itens 1.1 a 1.43 e todos os seus subitens, na ordem e com a numeração originais do documento-fonte. Cada item de primeiro nível (1.1, 1.2, ... 1.43) é um heading estável, com a página do documento-fonte indicada. Pontos de quebra de página dentro de um mesmo item estão marcados em itálico.

---

## 1. Das Descrições Técnicas da Solução (p. 1)

### 1.1 (p. 1)

O sistema deve ser disponibilizado em servidor WEB, com certificado de segurança SSL, com disponibilidade de no mínimo 99%, disponível para acesso diretamente na internet.

### 1.2 (p. 1)

Servidores distribuídos em data center nacional para garantir baixa latência, abaixo de 50 milissegundos, conforme exigido pelas normas ISO/IEC 27001:2013, 27017:2015, 27018:2019 e ISO/IEC 9001:2015. Estando em conformidade com o Marco Civil da Internet e a Norma Complementar n. 14/IN01/DSIC/SCS/GSIPR, ao utilizar uma arquitetura que otimiza recursos, elástica, escalável, com manutenção simplificada, resiliente a falhas e permitindo uma operação eficiente, observando-se ainda a Lei Geral de Proteção de Dados (Lei nº 13.709/2018), que estabelece que as operações de tratamento de dados pessoais deverão ocorrer, preferencialmente, em território nacional, garantindo segurança, transparência e soberania no tratamento da informação.

### 1.3 (p. 1)

O sistema deverá gerenciar automaticamente a operabilidade e escalabilidade do banco de dados, com provisionamento automático e suporte para diferentes instâncias de banco de dados conforme demanda.

### 1.4 (p. 1)

O serviço deverá garantir backup, restauração, replicação e balanceamento de carga para as operações de banco de dados.

### 1.5 (p. 1)

Deverá haver compatibilidade com bancos de dados relacionais como MySQL, PostgreSQL ou outros, de acordo com a necessidade.

### 1.6 (p. 1)

Deverá fornecer recursos computacionais elásticos para suporte à infraestrutura da aplicação, permitindo a escalabilidade vertical e horizontal conforme o volume de acessos e carga de processamento.

### 1.7 (p. 1)

Deverá garantir uma rede privada e segura para comunicação entre os serviços da nuvem, com controle granular de acesso público e privado.

### 1.8 (p. 1)

O sistema deverá suportar a criação e gerenciamento de sub-redes (subnets), roteadores (gateways) e configurações de acesso seguro via VPN.

### 1.9 (p. 1)

Deverá monitorar a aplicação utilizando modelos de machine learning para detectar anomalias no desempenho e uso de recursos, gerando relatórios automáticos sobre possíveis problemas e soluções.

### 1.10 (p. 1)

Deverá permitir o envio escalável de notificações via e-mail, com capacidade de envio de até 50 mil e-mails diários e até 14 e-mails por segundo, garantindo a confiabilidade e entrega das mensagens.

### 1.11 (p. 1)

Deverá integrar sistemas de segurança como autenticação de remetente e proteção contra spam.

### 1.12 (p. 1)

Deverá gerenciar de forma segura as credenciais de banco de dados, chaves de API e outros segredos, com rotação automática de chaves e recuperação de informações criptografadas.

### 1.13 (p. 1)

O sistema deverá garantir a auditoria de acessos e alterações às credenciais.

### 1.14 (p. 1)

Deverá permitir a limitação e segurança das requisições por meio de políticas de uso e proteção contra DDoS.

### 1.15 (p. 1)

O sistema deverá armazenar de maneira segura todos os documentos e arquivos da aplicação, com alta disponibilidade e recuperação automática em caso de falha.

### 1.16 (p. 1)

Deverá permitir o armazenamento de grandes volumes de dados com políticas de ciclo de vida e versionamento.

### 1.17 (p. 1)

Deverá proteger a aplicação contra ameaças da web, como tentativas de exploração de vulnerabilidades comuns (SQL Injection, Cross-Site Scripting) e ataques de negação de serviço (DDoS).

### 1.18 (p. 1)

Deverá permitir a configuração de regras de segurança personalizadas e automação de respostas a ataques.

### 1.19 (p. 1)

O sistema deverá gerenciar a fila de mensagens entre os serviços para evitar sobrecarga e garantir a comunicação assíncrona entre os módulos.

### 1.20 (p. 1)

Deverá permitir a configuração de múltiplas filas com diferentes prioridades e tempos de espera.

### 1.21 (p. 1)

Deverá gerenciar as chaves criptográficas usadas para proteger os dados armazenados e transferidos entre os serviços, garantindo que todas as informações confidenciais estejam devidamente protegidas.

### 1.22 (p. 1)

O sistema deverá permitir o controle de acesso às chaves e a criação de políticas de segurança.

### 1.23 (p. 1)

Deverá ser capaz de rastrear e identificar gargalos ou falhas em qualquer ponto da infraestrutura.

### 1.24 (p. 1)

O sistema deverá permitir o login para os seguintes tipos de usuários, observando que cada acesso deverá ser único e vinculado exclusivamente a um único CPF ou CNPJ:

- 1.24.1. Servidor Público: Autenticação por CPF (Obrigatoriamente) e senha;
- 1.24.2. Cidadão (Pessoa Física): Autenticação por CPF (Obrigatoriamente) e senha;

*(quebra de página — continua na p. 2)*

- 1.24.3. Empresas e outras entidades (Pessoa Jurídica): Autenticação por CNPJ (Obrigatoriamente) e senha.

### 1.25 (p. 2)

O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão:

- 1.25.1. Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;
- 1.25.2. O sistema deverá exibir uma mensagem de erro clara quando as credenciais não forem reconhecidas;
- 1.25.3. Controle de acesso dinâmico baseado no ciclo de vida da identidade funcional:
  - 1.25.3.1. Estado Operacional Padrão (Ativo): O sistema deverá aplicar o conjunto completo de permissões e privilégios (entitlements) associados aos papéis do usuário cujo atributo de status funcional esteja definido como "Ativo", garantindo acesso irrestrito ao ambiente de trabalho conforme seu perfil de autorização;
  - 1.25.3.2. Estado de Afastamento Legal (Licença): Para um usuário em estado de "Licença", o sistema deverá acionar uma política de quarentena de privilégios, apresentando um aviso de status e restringindo dinamicamente o acesso a um subconjunto mínimo de funcionalidades não transacionais, suspendendo temporariamente direitos de modificação e aprovação;
  - 1.25.3.3. Estado de Afastamento Legal (Férias): De forma análoga ao estado de licença, um usuário cujo status seja "Férias" deverá ter seu acesso modulado pela mesma política de quarentena de privilégios, com a exibição de notificação e a suspensão de permissões de escrita e execução de fluxos de trabalho;
  - 1.25.3.4. Estado de Desprovisionamento Lógico (Inativo): Quando o vínculo do agente for encerrado (status "Inativo"), a plataforma deverá aplicar uma regra de negação explícita (explicit deny) a qualquer tentativa de autenticação, impossibilitando o acesso e exibindo uma mensagem de conta inativa.

### 1.26 (p. 2)

A plataforma deve possibilitar a estruturação organizacional do órgão por meio de organograma, que deverá fornecer uma representação hierárquica visual e funcional dos setores e subsetores da organização pública:

- 1.26.1. A ferramenta será usada para cadastrar setores, atribuir usuários e gerenciar a tramitação de documentos/processos com base na hierarquia organizacional definida;
- 1.26.2. A interface de gestão do organograma deverá renderizar a estrutura organizacional por meio de um componente de visualização hierárquica (tree view) interativo. Cada nó setorial que contenha subníveis deverá ser apresentado como um elemento expansível e retrátil, permitindo a navegação intuitiva em topologias de alta complexidade e profundidade;
- 1.26.3. A plataforma deverá possuir uma arquitetura que suporte a modelagem de estruturas organizacionais complexas, sem impor limitações quantitativas ao número de setores ou subsetores. Esta capacidade de escalabilidade é um requisito mandatório para assegurar a fidedignidade e a perenidade da representação do organograma, garantindo a adaptabilidade do sistema a futuras reformas administrativas e reestruturações orgânicas, que são inerentes à dinâmica do setor público;
- 1.26.4. A funcionalidade deve permitir a edição e o gerenciamento dos setores e subsetores, bem como a adição e suspensão de setores;
- 1.26.5. A funcionalidade deverá permitir a visualização dos usuários atribuídos a cada setor/subsetor, e a possibilidade de adicionar ou remover usuários;
- 1.26.6. A funcionalidade deverá permitir a suspensão temporária de setores/subsetores, sendo que a suspensão deverá impedir que documentos sejam tramitados por esses setores enquanto estiverem inativos;
- 1.26.7. O sistema deverá verificar pendências (documentos tramitados, configurações de fluxos de trabalho, usuários atribuídos e afins) antes de permitir a suspensão;
- 1.26.8. O sistema deve permitir a reativação de setores suspensos, restabelecendo suas funcionalidades e documentos associados;
- 1.26.9. O sistema deverá fornecer estatísticas consolidadas que apresentem a quantidade total de setores cadastrados e a quantidade total de usuários alocados nesses setores;
- 1.26.10. Deverá ser possível renomear setores e subsetores, com regras para garantir que documentos previamente tramitados mantenham o nome antigo do setor;
- 1.26.11. Deverá ainda ser possível que cada setor possa ter as suas próprias regras de tramitação em cada categoria de documento da organização - Circulares, Ofícios, Processos administrativos e afins -, incluindo todos os serviços e assuntos vinculados a cada um destes tipos de documentos. De modo que, qualquer usuário servidor, com as devidas permissões concedidas, possam configurar em quais categorias de documentos, serviços e assuntos o setor em questão poderá:
  - 1.26.11.1. Criar documentos;

*(quebra de página — continua na p. 3)*

  - 1.26.11.2. Receber e tramitar documentos;
  - 1.26.11.3. Interagir com o cidadão, para os casos em que existem interações externas com o cidadão;
  - 1.26.11.4. Visualização de dados sigilosos, para os casos em que existam documentos classificados como sigilosos;
  - 1.26.11.5. Recebimento automático de documentos;
- 1.26.12. Deve ser possível reordenar setores e subsetores para outras hierarquias dentro do organograma. Sendo possível movimentação entre os "galhos" da estrutura, dinamicamente, para que as hierarquias se adequem à realidade do órgão. Dessa forma, deve haver a possibilidade de arrastar uma estrutura de setores e subsetores para uma outra hierarquia de setor, tornando os setores e subsetores arrastados, como subsetores do setor para o qual foram submetidos.

### 1.27 (p. 3)

A plataforma deve fornecer área para cadastro e gerenciamento do quadro de servidores do órgão, havendo a possibilidade de vinculá-los aos setores aos quais faz parte e com níveis de permissões específicas para cada setor vinculado.

- 1.27.1. A plataforma deverá prover um mecanismo de cadastro controlado para novos servidores, baseado em um fluxo de convite, pré-cadastro e homologação. Esta funcionalidade é projetada para delegar a ponta inicial do cadastro ao próprio usuário, ao mesmo tempo em que mantém um controle de acesso rigoroso, garantindo que apenas pessoal autorizado seja provisionado no sistema;
- 1.27.2. Para cadastro dos servidores é necessário que alguns níveis sejam fornecidos pela plataforma para que seja possível limitar as permissões que cada servidor possuirá dentro de todo o ecossistema. O sistema deve fornecer, pelo menos, os seguintes níveis de usuário:
  - 1.27.2.1. Administrador;
  - 1.27.2.2. Administrador setorial;
  - 1.27.2.3. Assistente administrativo;
  - 1.27.2.4. Auxiliar administrativo;
  - 1.27.2.5. Visualizador.
- 1.27.3. Os usuários no nível Administrador devem ter acesso master a todas as funcionalidades da plataforma, tendo permissão para acessar todas as configurações do sistema.
- 1.27.4. Os usuários do nível Administrador setorial devem ter as seguintes permissões:
  - 1.27.4.1. No organograma:
    - i. visualizar todo o organograma do órgão;
    - ii. cadastrar, editar e suspender setores na hierarquia do setor ao qual ele faz parte;
    - iii. vincular e desvincular servidores aos setores na hierarquia do setor ao qual ele faz parte;
  - 1.27.4.2. Na área de servidores:
    - i. visualizar todos os servidores da organização;
    - ii. cadastrar servidores na hierarquia do setor ao qual ele faz parte;
  - 1.27.4.3. Contatos externos:
    - i. Visualizar e cadastrar contatos externos para abertura de solicitações no órgão: pessoas físicas e pessoas jurídica;
  - 1.27.4.4. Assuntos e serviços:
    - i. Visualizar, cadastrar, editar e inativar serviços e assuntos relacionados aos módulos que estejam disponíveis.
- 1.27.5. Assistente administrativo:
  - 1.27.5.1. No organograma:
    - i. visualizar todo o organograma do órgão;
    - ii. cadastrar e editar setores na hierarquia do setor ao qual ele faz parte;
  - 1.27.5.2. Na área de servidores:
    - i. visualizar todos os servidores da organização;
    - ii. cadastrar, editar e suspender servidores na hierarquia do setor ao qual ele faz parte;
  - 1.27.5.3. Contatos externos:
    - i. Visualizar e cadastrar contatos externos para abertura de solicitações no órgão: pessoas físicas e pessoas jurídica;
  - 1.27.5.4. Assuntos e serviços:
    - i. Visualizar serviços e assuntos relacionados aos módulos que estejam disponíveis;
- 1.27.6. Auxiliar administrativo:
  - 1.27.6.1. No organograma:

*(quebra de página — continua na p. 4)*

    - i. visualizar todo o organograma do órgão;
  - 1.27.6.2. Na área de servidores:
    - i. visualizar todos os servidores da organização;
  - 1.27.6.3. Contatos externos:
    - i. Visualizar e cadastrar contatos externos para abertura de solicitações no órgão: pessoas físicas e pessoas jurídica;
- 1.27.7. Visualizador:
  - 1.27.7.1. No organograma:
    - i. visualizar todo o organograma do órgão;
  - 1.27.7.2. Na área de servidores:
    - i. visualizar todos os servidores da organização;
  - 1.27.7.3. Contatos externos:
    - i. Visualizar contatos externos cadastrados;
  - 1.27.7.4. Na tramitação, devem:
    - i. poder acessar, mas SEM PODER interagir nos documentos dos setores que fazem parte diretamente.
- 1.27.8. Para atender a individualidade de cada setor do órgão, devem existir permissões extras, que podem ser atribuídas aos usuários, para associação com as permissões que já existem em seus respectivos níveis de cadastro.
  - 1.27.8.1. Essas permissões devem ser concedidas no momento do cadastro ou na edição do servidor, por um servidor administrador ou que tenha nível de permissão para isso.
  - 1.27.8.2. Devem existir, pelo menos as seguintes permissões extras a seguir:
    - a) Cadastrar setores e subsetores no organograma;
    - b) Editar setores e subsetores no organograma;
    - c) Suspender setores e subsetores no organograma;
    - d) Atribuir usuários aos setores e subsetores no organograma;
    - e) Desvincular usuários de setores e subsetores no organograma;
    - f) Ajustar regras de tramitação dos setores na atuação em módulos, serviços e assuntos;
    - g) Cadastrar servidores;
    - h) Editar servidores;
    - i) Atualizar situação de atividade dos servidores;
    - j) Visualizar pré-cadastros;
    - k) Validar pré-cadastros;
    - l) Excluir pré-cadastros;
    - m) Cadastrar contatos externos;
    - n) Editar contatos externos;
    - o) Possibilidade de, nas permissões extras, cadastrar categorias e subcategorias de assuntos e serviços;
    - p) Cadastrar assuntos e serviços;
    - q) Editar assuntos e serviços;
    - r) Inativar assuntos e serviços;
    - s) Possibilidade de, nas permissões extras, dar acesso a mesas de outros setores, mas sem permissão de interação;
    - t) Visualizar fluxos de trabalho;
    - u) Cadastrar fluxos de trabalho;
    - v) Ativar e inativar fluxos de trabalho;
    - w) Editar fluxos de trabalho, incluindo excluí-lo;
    - x) Duplicar fluxos de trabalho.
- 1.27.9. A plataforma deve fornecer forma simplificada de cadastro de servidores, fornecendo, no mínimo, dois meios de cadastro conforme a seguir:
  - 1.27.9.1. Deve ser possível fazer o cadastro pela via interna, onde um usuário com permissão cadastre o servidor e este receba apenas um email para confirmação da vinculação ao órgão;
  - 1.27.9.2. Deve ser possível fazer o cadastro por meio de um link direto para ser enviado e usado em massa pelos servidores, para cadastro direto em um setor específico, necessitando apenas da aprovação e definição do nível destes pré-cadastros através de um usuário administrador;
  - 1.27.9.3. Para o cadastro de servidores, internamente, por um usuário com permissão, devem ser solicitadas as seguintes informações:
    - a) CPF - após a informação do CPF do servidor o sistema deve fazer consulta em alguma API que traga o nome completo do usuário, sem possibilidade de alteração;

*(quebra de página — continua na p. 5)*

    - b) E-mail;
    - c) Matrícula (caso haja);
    - d) Setores ao qual o servidor será vinculado. Em cada setor associado deve ser solicitado a indicação do Nível de acesso, conforme definido em itens anteriores;
    - e) Permissões extras (caso haja).
  - 1.27.9.3.2. Após a conclusão do cadastro um email deve ser enviado para o novo servidor, para que ele conclua o cadastro e comece a fazer parte da estrutura organizacional.
  - 1.27.9.3.3. Até que o servidor conclua o cadastro, o pré-cadastro enviado para ele deve ficar em área específica, com possibilidade de:
    - a) Excluir o pré-cadastro, e a partir desse momento o cadastro não deverá mais poder ser concluído;
    - b) Reenvio do email para conclusão do cadastro;
    - c) Edição - onde todos os dados do cadastro realizado poderão ser alterados, exceto o CPF.
  - 1.27.9.3.4. Através do email enviado o novo servidor deve ser direcionado para tela para conclusão do cadastro onde deve inserir os seguintes dados:
    - a) CPF - para confirmação da identidade do servidor. Caso seja inserido um CPF diferente do qual foi feito cadastro, o sistema deve impedir o prosseguimento;
    - b) Assinatura textual - assinatura que deverá acompanhar todos os atos do servidor durante as tramitações;
    - c) Cargo de contrato;
    - d) Cargo exercido em cada setor ao qual foi vinculado no cadastro;
    - e) Criação de senha com critérios de segurança, que incluem parâmetros que possam classificar a força da senha, possibilitando apenas o uso de senhas fortes;
    - f) Aceite dos termos de uso e política de privacidade.
  - 1.27.9.3.5. Após inseridos esses dados o usuário deve ser redirecionado para a tela de login para que realize o acesso à sua área de trabalho com as respectivas permissões atribuídas ao seu cadastro.
  - 1.27.9.4. Para o cadastro externo, um link deve ser gerado diretamente para um setor específico, através do organograma, e enviado para um ou mais servidores, para que assim eles realizem um pré-cadastro no setor direcionado.
    - 1.27.9.4.1. O cadastro realizado por esse link deve passar por uma aprovação de um usuário com permissão, a fim de que sejam validadas todas as informações fornecidas pelo servidor que se auto cadastrou.
    - 1.27.9.4.2. Para o cadastro externo devem ser exigidos os seguintes dados:
      - a) CPF - após a informação do CPF do servidor o sistema deve fazer consulta em alguma API que traga o nome completo do usuário, sem possibilidade de alteração;
      - b) E-mail;
      - c) Data de nascimento;
      - d) Sexo;
      - e) Telefone;
      - f) Assinatura textual - assinatura que deverá acompanhar todos os atos do servidor durante as tramitações;
      - g) Cargo de contrato;
      - h) Matrícula;
      - i) Cargo no setor do link enviado;
      - j) Criação de senha com critérios de segurança, que incluem parâmetros que possam classificar a senha como fraca, média e forte, possibilitando apenas o uso de senhas forte;
      - k) Aceite dos termos de uso e política de privacidade.
    - 1.27.9.4.3. Deve ser ainda, nesse fluxo, dada a possibilidade do servidor indicar outros setores que também faz parte, para agilizar o processo de aprovação e cadastro internamente.
    - 1.27.9.4.4. Após o envio, o pré-cadastro do servidor deve ser exibido internamente na plataforma, numa área específica para pré-cadastros.
    - 1.27.9.4.5. Na aprovação de um pré-cadastro o usuário, com permissão, deve ter que definir o nível nos setores informados no pré-cadastro e com possibilidade de adicionar mais setores, bem como, deve poder adicionar permissões extras ao usuário. Deve ainda haver a possibilidade de recusa do pré-cadastro, sendo necessário informar uma justificativa para a reprovação, que deve ser enviada, por e-mail, para o usuário que solicitou o pré-cadastro.
    - 1.27.9.4.6. Após aprovação do pré-cadastro, o servidor aprovado deve receber um email, confirmando o seu cadastro e link direcionando-o para a área de login na plataforma.

*(quebra de página — continua na p. 6)*

### 1.27.10 (p. 6)

- 1.27.10. Deve haver área de listagem de todos os servidores cadastrados no órgão, de modo que se possa consultar todo o quadro de servidores.
  - 1.27.10.1. Na listagem é necessário que sejam exibidos, no mínimo, as seguintes informações:
    - a) Nome do servidor;
    - b) Cargo;
    - c) Setor principal;
    - d) Email;
    - e) Status do servidor, informando se ele está, no momento da consulta:
      - i. Ativo: que deve representar o servidor que está com acesso à plataforma, de acordo com as permissões no seu nível;
      - ii. Inativo ("offline") - que deve representar o servidor que, no momento, não está logado ou operando na plataforma e, nesse caso, deve ser exibido também a data e hora da última vez em que esteve ativo;
      - iii. Suspenso - que deve representar servidores que tiverem seus acessos à plataforma suspensos;
      - iv. Licença - que deve representar os servidores que estiverem em algum período de licença das suas atividades;
      - v. Férias - que deve representar os servidores que estiverem em período de férias.
  - 1.27.10.2. Também na área de listagem dos servidores, deve haver a disponibilização dos seguintes dados:
    - a) Quantidade de servidores cadastrados no órgão;
    - b) Quantidade de servidores ativos.
  - 1.27.10.3. Ainda na área de listagem, deve ser possível visualizar, sem permissão de edição, os dados do servidor, exibindo informações mais detalhadas, sendo elas:
    - a) Nome do servidor;
    - b) Cargo de contrato;
    - c) Status;
    - d) Assinatura textual;
    - e) CPF, parcialmente protegido, de acordo à LGPD;
    - f) E-mail;
    - g) Matrícula;
    - h) Para os usuários que tiveram solicitação de cadastro por link gerado pelo organograma, o registro de quem aprovou o cadastro do usuário, junto com a data e hora da ação;
    - i) Setor principal, junto com nível e cargo do respectivo setor;
    - j) Setores adicionais, juntamente com os níveis e cargos de cada setor adicional.
  - 1.27.10.4. Dada a quantidade de servidores do órgão, na listagem desses, será necessário filtro para buscas mais ágeis e otimizadas. Dessa forma, deve ser disponibilizado os seguintes itens que auxiliem na busca por um servidor:
    - a) Campo de busca por palavra-chaves retornando resultados que envolvam:
      - i. Nome do servidor;
      - ii. Cargo;
      - iii. Setor;
      - iv. Email.
    - b) Filtros que retornem resultados que envolvam:
      - i. Usuários "offline";
      - ii. Usuários "online";
      - iii. Usuários de licença;
      - iv. Usuários de férias;
      - v. Usuários suspensos.
    - 1.27.10.4.2. Deve ser possível ainda fazer uso combinado do filtro com o campo de busca.

### 1.27.11 (p. 6)

- 1.27.11. A plataforma deve fornecer possibilidade de edição de cadastros e pré-cadastros de servidores.
  - 1.27.11.1. Os dados que poderão ser alterados dos servidores cadastrados, devem ser:
    - a) Assinatura textual;
    - b) E-mail institucional;
    - c) Matrícula;
    - d) Setor principal:
      - i. Nível;
      - ii. Cargo.

*(quebra de página — continua na p. 7)*

    - e) Setores adicionais - retirar e/ou acrescentar:
      - i. Nível;
      - ii. Cargo.
    - f) Permissões extras.
  - 1.27.11.2. Deve ser possível ainda, na área de edição do servidor, alterar o seu status de atividade, devendo existir, no mínimo, os seguintes status e possibilidades:
    - a) Em atividade;
    - b) Suspenso;
    - c) Licença;
    - d) Férias.
  - 1.27.11.3. Deve ser possível alterar livremente entre os status disponíveis, devendo apenas ser exigido uma data de início e fim para o novo status definido.
  - 1.27.11.4. A partir da definição do período do novo status de atividade do servidor, esse deve receber um email informando da alteração realizada e no período definido as alterações do seu ambiente de trabalho devem ser aplicados, de modo que, num cenário onde é definido que um usuário entrará de férias na próxima segunda e permanecerá por 30 dias, na segunda o usuário tenha o seu acesso à plataforma limitado, informando que ele está de férias e, ao término do período, o sistema reestabeleça as funções para que o servidor retorne às suas atividades.
  - 1.27.11.5. Os dados pessoais do usuário servidor devem ser exibidos na tela de edição, no entanto, algumas delas só poderão ser editadas por ele mesmo e outras não devem poder ser editadas por ninguém, a fim de manter a segurança e confiabilidade dos dados.
    - 1.27.11.5.1. As informações mencionadas deverão ser as descritas a seguir:
      - a) CPF - não editável;
      - b) Nome - não editável, pois deve ser vinculado ao retorno da API de consulta do CPF;
      - c) Telefone - editável só pelo próprio servidor;
      - d) Sexo - editável apenas pelo próprio servidor;
      - e) Data de nascimento - editável apenas pelo próprio servidor.
  - 1.27.11.6. Pré-cadastros que foram feitos internamente e externamente devem possuir uma área específica para gerenciamento e edição dos mesmos. Nela devem estar disponibilizadas as informações sobre os servidores que estão com pré-cadastros pendentes de aprovação ou aceitação.
    - 1.27.11.6.1. Os pré-cadastros externos devem ter a possibilidade de serem aprovados ou reprovados e, no caso de reprovação, uma justificativa deve ser exigida.

### 1.28 (p. 7)

A plataforma deve possuir funcionalidade de Gerenciamento de Serviços e Assuntos, devendo organizar e gerenciar a criação, edição, suspensão e exclusão de categorias, subcategorias, serviços e assuntos, além de permitir a aplicação de filtros e buscas, para facilitar o acesso e controle desses itens. Esta funcionalidade visa garantir que o fluxo de trabalho administrativo seja realizado de forma eficiente e organizada, respeitando as permissões e hierarquias definidas pelo administrador do sistema.

- 1.28.1. Para o cadastro de serviços e assuntos, devem ser disponibilizados no mínimo as informações que seguem:
  - a) Nome do serviço ou assunto;
  - b) Descrição do serviço ou assunto;
  - c) Categoria de documento em que esse serviço/assunto será disponibilizado;
  - d) Para os casos em que o referido assunto ou serviço será para tratamento de demandas com usuários externos, possibilidade de definição se o referido serviço/assunto pode ser aberto via central de atendimento, diretamente pelo interessado, através dos meios digitais do órgão;
  - e) Para os casos em que for definida a possibilidade de abertura externa, diretamente pelo interessado deve haver a possibilidade de definição de quais setores poderão interagir diretamente com o usuário externo;
  - f) Para os casos de possibilidade de abertura externa, diretamente pelo interessado, definição se o referido serviço/assunto necessita de classificação de sigilo da demanda, podendo ser identificado entre as seguintes opções:
    - i. Com sigilo: apenas setores específicos poderão ter acesso às partes sigilosas do processo;
    - ii. Sem sigilo: todos os setores envolvidos na demanda poderão ver todas as informações;
    - iii. Anônimo: o solicitante não é identificado, no entanto todos os setores envolvidos na demanda poderão ver todas as informações.
  - g) Para os casos em que for definido sigilo do processo, deve haver a solicitação de definição de quais setores poderão ter acesso aos dados sigilosos;

*(quebra de página — continua na p. 8)*

  - h) Definição se será permitido realizar despachos sigilosos durante o processo. Caso a configuração seja ativa, durante a tramitação do serviço ou assunto em questão, apenas os setores envolvidos no despacho classificado como sigiloso poderão ver o seu conteúdo;
  - i) Definição dos setores que poderão abrir processos do assunto/serviço;
  - j) Definição dos setores que poderão receber e tramitar processos do assunto/serviço;
  - k) Possibilidade de envio automático dos processos desse serviço/assunto a um setor específico, sempre que um novo processo for criado;
  - l) Possibilidade de definir um prazo oficial para conclusão dos processos abertos através do assunto/serviço. Havendo um prazo oficial definido, deve ser possível definir se:
    - i. O prazo vai ser executado em dias úteis ou corridos;
    - ii. Possibilidade de definição se o prazo aceita prorrogações. Caso o assunto/serviço aceite prorrogação, deve ser possível definir:
      - a. A quantidade de prorrogações aceitas;
      - b. Quantidade de dias que cada prorrogação aceitará (limitando a quantidade de dias do prazo oficial);
      - c. Possibilidade de definição se a prorrogação necessitará de justificativa.
  - m) Possibilidade de definição se os processos desse assunto/serviço já possuem uma numeração oficial pré-existente e, caso possua, deve ser possível informar a partir de que numeração os processos deverão ser numerados. Além disso, deve ser possível definir se essa numeração é reiniciada a cada ano ou se ela é uma sequência infinita.
- 1.28.1.2. Após definidos os parâmetros do serviço ou assunto, deve ser possível customizar os campos personalizados que esse serviço ou assunto precisará, para ter as informações necessárias para a abertura do processo.
  - 1.28.1.2.1. Deve ser disponibilizado pelo menos os tipos de campos a seguir:
    - a) Texto curto - para textos com até 100 caracteres;
    - b) Texto grande - para textos com mais de 100 caracteres, devendo ter a possibilidade de possuir um texto base pré-definido, de modo que, ao ser acionado na abertura do processo, o texto pré-definido já venha disposto neste campo;
    - c) Número - para inserção de números simples ou com máscaras, dos seguintes tipos:
      - i. Número simples;
      - ii. Porcentagem;
      - iii. Moeda brasileira;
      - iv. Telefone;
      - v. Celular;
      - vi. CPF;
      - vii. CNPJ;
      - viii. m2;
      - ix. m3.
    - d) E-mail;
    - e) Mapa;
    - f) Link;
    - g) Arquivo;
    - h) Data e hora;
    - i) Escolha única e múltipla;
    - j) Grupo de campos, para aninhar um conjunto de campos e servir como setorizador no formulário, dando maior clareza no momento do preenchimento;
    - k) Texto informativo, sem característica padrão de ser um campo preenchível, deve servir como um bloco de texto para orientação ou disposição de informações adicionais para quem está preenchendo o formulário;
    - l) Seleção de referência de:
      - i. Pessoas (cidadãos, empresas e servidores) cadastrados no órgão;
      - ii. Setores.
  - 1.28.1.3. Os campos devem ainda ter a possibilidade de configuração de:
    - a) Título do campo;
    - b) Definição de para quem o campo será exibido, se:
      - i. Apenas para o servidor;
      - ii. Apenas para o cidadão;

*(quebra de página — continua na p. 9)*

      - iii. Para cidadão e servidor.
    - c) Descrição do campo;
    - d) Dica de como preencher o campo;
    - e) Definição se o campo terá seu preenchimento obrigatório ou não;
    - f) Possibilidade se o campo pode ser repetido ou não;
    - g) Definição se o campo possuirá conteúdo sensível, de modo que, para consultas externas, em respeito à LGPD, os dados desse campo seja protegido e não exibido para usuários não autorizados;
    - h) Definição se o campo em questão servirá como título dos documentos gerados no assunto/serviço em questão e assim serem visíveis na mesa de trabalho.
  - 1.28.1.4. Os campos do formulário devem ter a possibilidade de serem movimentados, para melhor distribuição e organização, respeitando os campos padrão, que já existiam na categoria ao qual o serviço/assunto foi vinculado.

### 1.29 (p. 9)

A solução deve possuir categorias de documentos para geração de processos digitais, bem como documentos e comunicação oficial. As categorias de documentos devem respeitar as regras de tramitação, entre setores, pré-estabelecidas pela entidade, permitindo definir os setores que poderão tramitar, criar e/ou receber automaticamente documentos e processos de cada módulo. Sendo assim deve ser disponibilizado quantas categorias de documentos quanto necessários para as atividades do órgão, sem restrição de quantidade, nos mesmos padrões de personalização de campos e regras de tramitação dos assuntos e serviços, ficando a cargo da empresa contratada a personalização e disponibilização, conforme demanda do órgão.

- 1.29.1. Para a correta execução das atividades do órgão, os documentos gerados pelas categorias de documentos devem ser classificados em umas das categorias a seguir:
  - a) Documento oficial (atos oficiais);
  - b) Comunicação oficial (memorando, ofício, circular e afins);
  - c) Processo administrativo (ouvidoria, protocolo, processo administrativo e afins).
- 1.29.2. A plataforma deve possuir categoria de documento que gerará documentos do tipo comunicação oficial, especificamente para criação de Memorandos, necessário para comunicação entre setores da instituição, seja de forma ampla, facilitando a comunicação entre setores principais, ou de maneira mais restrita, intermediando a comunicação entre subsetores de uma mesma secretaria.
  - 1.29.2.1. Campos e Parâmetros Necessários:
    - a) Numeração única e contínua para toda instituição;
    - b) Indicação de onde está saindo o memorando;
    - c) Setor Destinatário - esse campo deve aceitar enviar a um ou mais setores em cópia, possa inserir o contexto do documento;
    - d) Assunto - onde o setor que está enviando, de forma resumida, possa inserir o contexto do documento;
    - e) Campo de texto de livre preenchimento, com possibilidade de anexar documentos - para inserção do conteúdo do memorando.
- 1.29.3. A plataforma deve possuir categoria de documento que gerará documentos do tipo comunicação oficial, especificamente para criação de Circulares, necessário para envios de comunicados e informações em massa. Seja para todos os setores da organização ou ainda para apenas alguns setores de sua escolha.
  - 1.29.3.1. Campos e Parâmetros Necessários:
    - a) Numeração única e contínua para toda instituição;
    - b) Assunto - onde o setor que está enviando, de forma resumida, possa inserir o contexto da circular;
    - c) Campo de texto de livre preenchimento, com possibilidade de anexar documentos - para inserção do conteúdo da circular;
    - d) Ter a possibilidade de o setor criador definir se o documento pode ser respondido pelos setores que receberam a informação, ou se o documento é apenas informativo, ou seja, sem caráter de resposta.
- 1.29.4. A plataforma deve possuir categoria de documento que gerará documentos do tipo comunicação oficial, especificamente para o envio de documentos oficiais da entidade para contatos externos, sejam eles pessoas físicas, jurídicas ou até mesmo setores de outras organizações.
  - 1.29.4.1. Campos e parâmetros necessários:
    - a) Numeração única e contínua para toda instituição;
    - b) Indicação - de onde está saindo o ofício;
    - c) Destinatário externo;
    - d) Assunto - onde o setor que está enviando, de forma resumida, possa inserir o contexto do ofício;
    - e) Campo de texto de livre preenchimento, com possibilidade de anexar documentos - para inserção do conteúdo do ofício.

*(quebra de página — continua na p. 10)*

    - f) É extremamente importante que o setor de onde o ofício é enviado tenha alguma forma de confirmação de recebimento da entrega do documento;
    - g) O destinatário deve receber um alerta notificando que a instituição enviou um documento para o mesmo.
- 1.29.5. A plataforma deve possuir categoria de documento que gerará documentos do tipo processo administrativo de maneira mais robusta. Deverá tratar de demandas da atividade administrativa de maneira mais robusta, permitindo que trâmites que têm várias atividades compiladas e de responsabilidade de vários setores da instituição, a possibilidade de aplicação de regras em sua abertura e tramitação, assim como a possibilidade de assuntos pré-definidos.
  - 1.29.5.1. Campos e parâmetros necessários:
    - a) Numeração única, ou por assunto, e contínua para toda instituição;
    - b) Campo de seleção de assunto - vinculado à funcionalidade de Serviço e assunto, esse campo deve trazer os assuntos cadastrados e vinculados ao módulo processo administrativo, trazendo os respectivos campos personalizados, após a seleção do assunto desejado;
    - c) Indicação de onde está saindo o processo;
    - d) Setor Destinatário - esse campo deve aceitar enviar a um ou mais setores em cópia.
- 1.29.6. A plataforma deve possuir categoria de documento que gerará documentos do tipo processo administrativo. Servirá para que usuários externos - contribuintes, fornecedores, empresas, população de maneira geral - dê entrada em algum requerimento ou solicitação de serviço junto à instituição.
  - 1.29.6.1. Campos e parâmetros necessários:
    - a) Numeração única, ou por assunto, e contínua para toda instituição;
    - b) Demandante - quem está solicitando a demanda;
    - c) Setor destinatário - setor que irá receber a solicitação e dar a primeira tratativa;
    - d) Campo de seleção de assunto - vinculado à funcionalidade de Serviço e assunto, esse campo deve trazer os assuntos cadastrados e vinculados à categoria de documento em questão, trazendo os respectivos campos personalizados, após a seleção do assunto desejado;
    - e) Notificação em tempo real da movimentação do processo para o demandante, através de e-mail e notificações no próprio sistema;
    - f) Possibilidade de despachos sigilosos onde o conteúdo não seja visível ao demandante, quando a tramitação ocorrer entre setores da instituição.
- 1.29.7. A plataforma deve possuir categoria de documento que gerará documentos do tipo processo administrativo e que será responsável por atender a Lei 13.460/2017 que trata sobre a Ouvidoria, sendo o canal para recebimento de denúncias, reclamações, sugestões ou elogios relativos aos atendimentos e/ou serviços prestados pelos órgãos da instituição.
  - 1.29.7.1. Campos e parâmetros necessários:
    - a) Numeração única, ou por assunto, e contínua para toda instituição;
    - b) Demandante - quem está solicitando a demanda;
    - c) Deve ser disponibilizada ao demandante a possibilidade de a demanda ser feita de forma anônima, sigilosa ou não sigilosa;
    - d) Setor destinatário - setor que irá receber a solicitação e dar a primeira tratativa;
    - e) Assunto - onde o demandante, de forma resumida, defina o contexto da demanda;
    - f) Campo de texto de livre preenchimento, com possibilidade de anexar documentos - para inserção do conteúdo da demanda;
    - g) Notificação em tempo real da movimentação na ouvidoria, para o demandante, através de e-mail e notificações no próprio sistema;
    - h) Possibilidade de despachos sigilosos onde o conteúdo não seja visível ao demandante, quando a tramitação ocorrer entre setores da instituição;
    - i) Permitir, nos casos onde a demanda for sigilosa, que apenas o setor determinado na configuração do módulo tenha acessos aos dados sigilosos;
    - j) Deverá ter controle dos prazos, conforme prescrito pela Lei 13.460/2017.
- 1.29.8. A plataforma deve possuir categoria de documento que gerará documentos do tipo processo administrativo e que será responsável por atender a Lei 12.527/2011 que trata sobre o e-SIC, permitindo que qualquer usuário externo, seja pessoa física ou jurídica, encaminhe solicitações de informação geral e pública de dados e documentos sob a guarda da instituição.
  - 1.29.8.1. Campos e parâmetros necessários:
    - a) Numeração única, ou por assunto, e contínua para toda instituição;
    - b) Demandante - quem está solicitando a informação;

*(quebra de página — continua na p. 11)*

    - c) Setor destinatário - setor que irá receber a solicitação e dar a primeira tratativa;
    - d) Assunto - onde o demandante, de forma resumida, define o contexto da solicitação;
    - e) Campo de texto de livre preenchimento, com possibilidade de anexar documentos - para inserção do conteúdo da solicitação;
    - f) Notificação em tempo real da movimentação no setor responsável, para o demandante, através de e-mail e notificações no próprio sistema;
    - g) Possibilidade de despachos sigilosos onde o conteúdo não seja visível ao demandante, quando a tramitação ocorrer entre setores da instituição.
- 1.29.9. A plataforma deve possuir módulo que gerará documentos do tipo documento oficial, para elaboração de Atos oficiais, com decisões ou normas que oficializam determinada ação da instituição. São considerados atos oficiais: Leis, portarias, decretos, resoluções e instruções normativas.
  - 1.29.9.1. Campos e parâmetros necessários:
    - a) Numeração única, ou por assunto, e contínua para toda instituição;
    - b) Setor emissor: de onde está saindo o Ato;
    - c) Setor Destinatário - esse campo deve aceitar enviar a um ou mais setores em cópia;
    - d) Assunto - onde o emissor, de forma resumida, possa definir o contexto do documento;
    - e) Campo de texto de livre preenchimento para inserção do conteúdo do documento.
- 1.29.10. A plataforma deve possuir categoria de documento para atender à necessidade de transparência e clareza nas solicitações de usuários externos (cidadãos e empresas) no que se refere à viabilidade de construções e licenciamento urbanístico. Através dele deve ser possível realizar consultas prévias ao zoneamento urbano do município e, a partir da zona de interesse, abrir diretamente uma solicitação junto ao órgão, dentro dos usos permitidos da zona selecionada.
  - 1.29.10.1. O objetivo desta funcionalidade é disponibilizar uma ferramenta que permita a criação, gestão e consulta de zoneamentos urbanos dentro do sistema.
  - 1.29.10.2. A ferramenta deve ser acessível tanto para servidores quanto para cidadãos e empresas, possibilitando consultas prévias de viabilidade de construção e o acompanhamento de processos urbanísticos.
  - 1.29.10.3. Além disso, a funcionalidade deve facilitar o gerenciamento de zoneamentos e categorias de uso por parte de usuários servidores.
  - 1.29.10.4. Os servidores, com permissão, devem poder criar e editar zoneamentos, zonas e usos permitidos do município, de duas formas: manualmente ou por upload de arquivo de zoneamento da cidade.
    - a) Criação Manual, onde deverá definir:
      - i. nome, descrição, bairros/localidades e categorias de uso associadas.
    - b) Upload de Mapa:
      - i. Ao realizar o upload de um arquivo .kmz, as zonas já existentes serão sobrescritas pelas informações do arquivo;
      - ii. Deve ser possível visualizar a lista de zonas ou o mapa;
    - c) As categorias de uso podem ser criadas e associadas às zonas, sendo compostas por nome, descrição e parâmetros (unidade de medida e valor);
    - d) O sistema deve ser capaz de armazenar e gerenciar os arquivos de georreferenciamento do município para exibição dos mapas de zoneamento urbano;
    - e) O sistema deve permitir a publicação e republicação do zoneamento urbano na central de atendimento ao cidadão;
    - f) Tanto zonas quanto categorias de uso deverão ter um histórico completo de criação, edição, incluindo mudanças de parâmetros, associações e dissociações com zonas e categorias;
    - g) Quando publicado, cidadãos e empresas poderão consultar as zonas e categorias de uso diretamente na central, e abrir processos urbanísticos a partir dessas informações;
    - h) Ao visualizar uma zona, o usuário poderá consultar os parâmetros de uso permitidos e iniciar um processo urbanístico diretamente relacionado à zona selecionada;
    - i) Todos os anexos inseridos em processos urbanísticos, seja via upload de arquivo ou por despachos, deverão poder ser revisados por servidores, com a possibilidade de aprovação ou reprovação;
    - j) A revisão dos anexos deve permitir o destaque de áreas, comentários e anotações sobre o arquivo por analistas do órgão, para que o solicitante faça as correções necessárias, caso haja.

### 1.30 (p. 11)

O sistema deve possibilitar a criação e gerenciamento de fluxos de trabalho, aplicáveis a qualquer tipo de processo administrativo, possibilitando a configuração de cada etapa com ações obrigatórias.

- 1.30.1. Cada etapa do fluxo de trabalho deverá conter as seguintes configurações:

*(quebra de página — continua na p. 12)*

  - a) Nome da Etapa;
  - b) Setor Responsável;
  - c) Regras de Tramitação:
    - i. Definir setores que podem participar da etapa (visualizar, participar, ou retroceder/avançar a etapa);
    - ii. Setores que podem encerrar/interromper a tramitação do processo (mesmo que a etapa não seja a última).
  - d) Despachos obrigatórios com a possibilidade de inserção de formulário personalizados, caso necessário;
  - e) Assinaturas obrigatórias, quando necessário.
  - f) O sistema deverá permitir que os fluxos de trabalho sejam gerenciados de modo que permita:
    - i. Listagem de todos os fluxos de trabalho, com filtros por categoria de documento, serviço, assunto e status (ativo, inativo ou rascunho);
    - ii. Ações de ativar, inativar, duplicar, editar ou excluir fluxos de trabalho existentes;
    - iii. Histórico de alterações realizadas em cada fluxo de trabalho.
  - g) O sistema deverá garantir que somente usuários autorizados possam visualizar, editar ou encerrar etapas e fluxos de trabalho, mantendo logs de todas as alterações feitas.
- 1.30.2. O sistema deverá permitir que as etapas incluam despachos customizados, contendo:
  - a) Possibilidade de inserir formulário personalizado à estrutura padrão do despacho:
    - i. O formulário deverá ter campos específicos que o usuário poderá configurar, garantindo a flexibilidade necessária para atender a diferentes tipos de demandas.
  - b) O sistema deverá permitir a inserção de solicitações de assinatura obrigatória como parte do despacho, garantindo que a tramitação só avance para uma nova etapa após a assinatura.
- 1.30.3. O sistema deverá garantir que, ao iniciar a tramitação de um documento que segue um fluxo de trabalho, as etapas e ações obrigatórias configuradas no fluxo de trabalho sejam respeitadas, incluindo:
  - a) A etapa só poderá ser avançada após a conclusão de todas as ações obrigatórias configuradas em sua criação;
  - b) O sistema deverá permitir retroceder uma única etapa, justificando a ação;
  - c) Ao iniciar uma etapa devem ser exibidos todos os requisitos configurados para aquela etapa e, cada vez que um item dessa lista for completado, deve ficar registrado e transparente para todos os envolvidos, o que já foi feito até então.

### 1.31 (p. 12)

A plataforma deve possuir funcionalidade de modelos de documentos, devendo permitir que os servidores criem, compartilhem, editem e utilizem modelos de documentos e despachos dentro do sistema, mantendo padrões de documentação e facilitando o trabalho dos servidores. A funcionalidade deverá ser dividida nas categorias "Modelos Simples" e "Documentos Automatizados", e permitir a herança de dados de um formulário preenchido, permitindo que os modelos "herdem" informações automaticamente de um formulário preenchido. De modo que:

- 1.31.1. Os modelos simples deverão ser integrados com o campo de Texto grande e os Editores de textos dos despachos para utilização durante a tramitação dos documentos;
  - 1.31.1.1. Para criação de um modelo simples, o sistema deverá permitir inserir as seguintes informações para melhor organização:
    - a) Nome do Modelo - para correta identificação no momento de utilizá-lo durante a tramitação;
    - b) Definição se o modelo terá ou não herança de dados;
      - i. Caso o modelo seja configurado para possuir herança de dados, o modelo deverá ser vinculado a uma categoria de documento, serviço ou assunto e poder ter na sua estrutura a referência a campos desse vínculo. Na prática, quando o servidor for usar esse modelo em um documento, o sistema preencherá esses espaços automaticamente com os dados que foram preenchidos no formulário inicial;
      - ii. Caso o modelo seja configurado sem a herança de dados o conteúdo desse modelo é totalmente estático.
    - c) Categoria de documento, serviço ou assunto ao qual o modelo deve ficar vinculado;
    - d) Campo de texto para o corpo do modelo em questão;
    - e) Na criação deve ter ainda a possibilidade de definir se o modelo vai ser exclusivo para o servidor que está criando ou se ele deseja compartilhar com outros setores.
  - 1.31.1.2. O sistema deverá manter um histórico das alterações realizadas em cada modelo. Todas as ações relacionadas à criação, edição e duplicação, deverão ser registradas para fins de auditoria, incluindo informações como data, hora, ação realizada e usuário responsável;

*(quebra de página — continua na p. 13)*

  - 1.31.1.3. Na tramitação de um documento, onde houver um campo de texto grande ou editor de texto, deverá ser exibida a opção de inserir um modelo de documento;
  - 1.31.1.4. Apenas os modelos compatíveis com a categoria de documento/serviço/assunto selecionado deverão ser exibidos para o usuário.
- 1.31.2. Modelos de documentos automatizados devem ser modelos que podem ser completamente configurados com herança de dados, assim como no modelo simples, mas nesse caso, eles possam ser de fato um documento independente, ou seja, enquanto no modelo simples, o modelo é um texto pré-definido e utilizado no escopo da tramitação de um documento que foi criado manualmente, os modelos automatizado, devem permitir gerar um documento individualmente, com o escopo de texto que foi definido na sua criação, incluindo a herança de dados, mas que deverão poder ter "vida" própria, ou seja, terão tramitação independente, para além do seu documento gerador, necessário para emissão de Alvarás, Licenças e documentos semelhantes, que são fruto de um processo de análise e que no final possuem um modelo padrão que precisa ser emitido com os dados já informados no início da solicitação.
  - 1.31.2.1. Para criação de um modelo automatizado o sistema deverá permitir inserir as seguintes informações para melhor organização:
    - 1.31.2.1.1. Nome do Modelo - para correta identificação no momento de utilizá-lo durante a tramitação;
    - 1.31.2.1.2. Categoria de documento, serviço ou assunto ao qual o modelo deve ficar vinculado;
    - 1.31.2.1.3. Estilização do cabeçalho e rodapé:
      - 1.31.2.1.3.1. Conteúdo do escopo do modelo, incluindo a herança de dados;
      - 1.31.2.1.3.2. Deve ser possível ainda configurar uma validade pré-definida para o documento, a contar após emissão dele.
- 1.31.3. Os modelos de documentos devem ainda poder ser editados e excluídos, por usuários servidores com as devidas permissões, além de dispor de histórico de alterações realizadas.

### 1.32 (p. 13)

Deve haver no sistema área para cadastro e gerenciamento de contatos externos, sejam cidadãos (pessoa física) ou empresas (pessoas jurídicas) os cadastros devem ser feitos através de CPF ou CNPJ, conforme o caso, para que seja garantida a cadastro único na plataforma desses tipos de usuário.

- 1.32.1. Ao serem cadastrados na plataforma os respectivos novos contatos, devem receber um email para confirmação do cadastro.

### 1.33 (p. 13)

O sistema a ser implementado deverá possuir funcionalidade de mesa de trabalho permitindo que os servidores públicos gerenciem documentos e processos administrativos de forma integrada e dinâmica, possibilitando a troca de informações entre diferentes setores e facilitando a organização de suas atividades diárias.

- 1.33.1. Além disso, deverá permitir que os usuários alternem entre diferentes setores de forma ágil, visualizando e gerenciando documentos e processos pertencentes a cada setor.
- 1.33.2. Ao acessar a plataforma o servidor deve ter à sua disposição, na primeira tela de acesso, um resumo de todas as demandas que ele tem a fazer.
  - 1.33.2.1. Nessa tela de boas-vindas devem ser informados para o servidor a quantidade de documentos nas situações definidas a seguir:
    - a) Em aberto - documentos novos que chegaram na mesa do servidor;
    - b) Em tramitação - documentos que o servidor já iniciou a tramitação;
    - c) Concluído - documentos que já passaram pela mesa do servidor, mas que já foram resolvidos;
    - d) Assinaturas pendentes - documentos que estão dependendo da assinatura do servidor;
    - e) Demandas prestes a vencer nos próximos dias e/ou já vencidas.
- 1.33.3. O sistema deve oferecer uma mesa de trabalho para cada servidor, contendo os documentos e processos relacionados a suas atividades individuais e aos setores em que estão vinculados.
  - 1.33.3.1. A visualização padrão da mesa de trabalho do servidor e dos setores que ele faz parte, deve ser em formato Kanban, permitindo a organização dos itens por colunas.
  - 1.33.3.2. A mesa também deve ter uma visualização em lista, exibindo os documentos e processos em uma lista vertical;
  - 1.33.3.3. A mesa de trabalho deve exibir alertas relacionados a prazos, status de documentos e novas demandas, independentemente do setor ativo;
  - 1.33.3.4. O sistema deve exibir alertas para documentos e processos com prazos próximos ao vencimento ou já vencidos;
  - 1.33.3.5. O sistema deve possibilitar a filtragem de documentos com prazos vencidos ou próximos ao vencimento;

*(quebra de página — continua na p. 14)*

  - 1.33.3.6. O sistema deve gerenciar o status dos documentos e das mesas de trabalho, classificando-os: em aberto, em elaboração, em tramitação, pausado, encerrado;
  - 1.33.3.7. O sistema deve permitir a reabertura de documentos encerrados.
  - 1.33.4. Tanto nas mesas pessoais como nas mesas dos setores, independentemente do tipo de visualização que está sendo usada, deve ser possível aplicar os seguintes filtros, buscas e ordenação, isolados ou em conjunto:
    - a) Busca por palavra-chave;
    - b) Busca por pessoas;
    - c) Busca por CPF;
    - d) Busca por CNPJ;
    - e) Ordenação por ordem alfabética;
    - f) Ordenação por pendente de assinatura;
    - g) Ordenação por pendente de revisão;
    - h) Filtro por status;
    - i) Filtro por módulo;
    - j) Filtro por assunto ou serviço;
    - k) Filtro por período.
  - 1.33.5. Nos documentos presentes nas mesas, deve ser possível ainda identificar de forma prática:
    - 1.33.5.1. O setor responsável pelo documento;
    - 1.33.5.2. Data e hora da última atividade;
    - 1.33.5.3. Notificações de novas interações diretas, para identificação de solicitações de assinaturas, envio de despachos e solicitações de revisão direcionados ao servidor ou setor em questão;
  - 1.33.6. Ainda na mesa de trabalho, deve ser disponibilizada ferramenta de rastreio para realização de busca ampla por documentos, de modo que a busca não restrinja apenas à mesa de trabalho em visualização, mas em todo o escopo da organização, resguardando o devido acesso ao seu conteúdo, de acordo com a permissão do usuário que está realizando a consulta.

### 1.34 (p. 14)

O sistema deverá disponibilizar uma funcionalidade de etiquetas para auxiliar na organização, categorização, filtragem e identificação de documentos nas mesas de trabalho de setores e servidores.

- 1.34.1. Deve ser possível criar etiquetas nos seguintes tipos:
  - a) Etiquetas pessoais: criadas exclusivamente para o uso individual do servidor, ou seja, visíveis apenas na mesa pessoal dele;
  - b) Etiquetas compartilhadas: criadas e compartilhadas entre setores ou hierarquias de setores, permitindo que mais servidores acessem essas etiquetas.
  - 1.34.1.2. O sistema deverá incluir uma etiqueta padrão denominada "Urgente", visível e aplicável por todos os setores e usuários. Esta etiqueta NÃO PODERÁ ser excluída;
  - 1.34.1.3. O sistema deverá permitir que as etiquetas sejam usadas como filtros na mesa de trabalho, facilitando a visualização e organização de documentos por categorias;
  - 1.34.1.4. A visualização de etiquetas aplicadas nos documentos deverá ser restrita, conforme o setor do usuário. Dessa forma, mesmo que exista uma etiqueta aplicada num documento, os servidores só devem conseguir visualizar essas etiquetas se elas estiverem relacionadas com seus setores.
- 1.34.2. O sistema deverá permitir a criação de novas etiquetas com a personalização de nome, cor e setores para compartilhamento, caso necessário;
  - 1.34.2.1. Etiquetas que forem criadas com a opção de compartilhar devem ser exibidas numa seção de etiquetas compartilhadas, visível para todos os usuários do setor;
  - 1.34.2.2. O sistema deverá permitir a criação de subetiquetas ligadas a uma etiqueta principal;
  - 1.34.2.3. O sistema deverá permitir a edição de nome, cor e setores associados a qualquer etiqueta;
  - 1.34.2.4. Todas as alterações deverão ser aplicadas automaticamente às etiquetas já aplicadas em documentos nas mesas de trabalho;
  - 1.34.2.5. Caso uma etiqueta seja excluída, nos documentos onde foi aplicada ela deve permanecer aplicada e exibida, mas não poderá ser adicionada a novos documentos.

### 1.35 (p. 14)

Os documentos e processos devem tramitar entre setores, de acordo com a estrutura organizacional definida no organograma do órgão, respeitando os limites de permissões de cada setor, de modo que os servidores só tenham acesso aos documentos e processos que façam parte da tramitação das mesas dos setores aos quais pertence.

- 1.35.1. Para a devida transparência e rastreio de atividades, todas as ações que acontecerem durante a tramitação dos documentos e processos, devem ser registradas na linha do tempo da tramitação, com o registro de:

*(quebra de página — continua na p. 15)*

  - a) Usuário que executou a ação;
  - b) Setor do usuário (no caso de ter sido um servidor o executor da ação);
  - c) data e hora em que a ação aconteceu;
  - d) Registro de quem já visualizou aquela ação e quantidade de vezes que cada uma dessas pessoas já visualizou, com o registro de data e hora da última visualização.
- 1.35.2. Os documentos e processos precisarão ter "status" para classificá-los durante a tramitação, para que assim seja possível definir uma melhor organização das demandas da entidade.
  - 1.35.2.1. Deve se ter na plataforma as seguintes classificações de situação dos documentos:
    - a) Em aberto: documentos novos que chegaram na mesa do setor ou na mesa pessoal do servidor;
    - b) Em elaboração: documentos que estão ainda na fase de elaboração, ou seja, ainda não são considerados documentos oficiais;
    - c) Em tramitação: processos e documentos oficiais que estão em tramitação nos setores para resolução ou conhecimento;
    - d) Pausado: documentos e processos que precisam ter sua tramitação interrompida, temporariamente, seja por um empecilho jurídico ou por estar esperando um retorno de usuários ou órgãos externos;
    - e) Encerrado: documentos que já tiveram as suas demandas atendidas e dessa forma suas tramitações estão concluídas.
  - 1.35.2.2. Também, devem ser disponibilizadas, de acordo com cada tipo de documento ou processo gerado, as funcionalidades que serão descritas adiante:
    - 1.35.2.2.1. Após a abertura de processos administrativos deve ser possível que os setores envolvidos realizem despachos, durante a tramitação do processo, com a finalidade de dar encaminhamento às tratativas necessárias de cada setor.
      - 1.35.2.2.1.1. A plataforma deve fornecer um campo de livre preenchimento, com a possibilidade de anexar arquivos e definição dos destinatários do despacho, inclusive setores que devem receber em cópia.
      - 1.35.2.2.1.2. O campo de texto em questão deve ainda fornecer as possibilidades que seguem:
        - a) Possibilidade de, através de um despacho, apensar um outro documento da entidade que precise fazer parte da tramitação em questão. O documento associado deve ficar identificado no documento ou processo que o associou, bem como, na impressão do documento ou processo que contém o documento associado, este também deve ser incluído.
      - 1.35.2.2.1.3. Os despachos realizados, dependendo da natureza do processo, devem ter a possibilidade de serem feitos de forma sigilosa ou não.
      - 1.35.2.2.1.4. Possibilidade de indicar um prazo, para os destinatários envolvidos no despacho, respeitando os prazos oficiais e do documento pré-existentes, não podendo ultrapassá-los.
      - 1.35.2.2.1.5. Possibilidade de assinar ou solicitar assinaturas em um despacho específico e seus respectivos anexos, caso haja. Deve ser fornecida a possibilidade de assinar tanto com assinatura nativa da plataforma, quanto ICP.
      - 1.35.2.2.1.6. Possibilidade de imprimir pontualmente um despacho emitido de uma tramitação, incluindo, os seus anexos e as assinaturas que ele porventura venha a ter.
    - 1.35.2.3. Possibilidade de retificação do documento de abertura de um processo administrativo, com os devidos registros de histórico e justificativa legal para a retificação.
    - 1.35.2.4. Possibilidade de solicitação de revisão de documentos e comunicações oficiais, ainda no seu estado pré-elaboração, ou seja, quando ele ainda não foi emitido oficialmente ainda, para que seja possível editá-los, antes da sua emissão oficial.
    - 1.35.2.5. Possibilidade de edição do documento de abertura de um documento ou comunicação oficial, ainda no seu estado pré-elaboração, ou seja, quando ele ainda não foi emitido oficialmente ainda, com os devidos registros de histórico de cada edição realizada.
    - 1.35.2.6. Possibilidade de definição de prazos para os documentos que por conseguinte devem ser aplicados de forma hierárquica para os setores e servidores envolvidos no documento.
    - 1.35.2.7. Os prazos devem respeitar uma sequência hierárquica de importância, do seguinte modo:
      - a) Prazo oficial - prazo definido por lei e parametrizado no módulo e/ou no serviço ou assunto. Quando há um prazo oficial esse, automaticamente, passa a ser o prazo do documento, não podendo ser mudado;

*(quebra de página — continua na p. 16)*

      - b) Prazo do documento - quando não houver um prazo oficial definido, deve ser possível a definição de um prazo macro para que um documento ou processo seja finalizado, a fim de que a rotina administrativa se mantenha em dia. Esse prazo deve ser aplicado para todos os envolvidos no documento/processo;
      - c) Prazo de assinatura - quando houver solicitação de assinaturas, possibilidade de definir um prazo para que os signatários realizem as assinaturas. Esse prazo deve, obrigatoriamente, respeitar o prazo do documento ou oficial, caso haja;
      - d) Prazo individual - possibilidade de um servidor definir um prazo para ele mesmo, num documento ou processo, para sua melhor organização. Esse prazo deve, obrigatoriamente, respeitar o prazo do documento ou oficial, caso haja.
- 1.35.3. Com o intuito de garantir a fluidez e eficiência no gerenciamento de demandas a plataforma deverá fornecer possibilidades flexíveis de encerramento das tramitações, devendo haver, no mínimo, as seguintes possibilidades:
  - a) Encerrar a tramitação individualmente para cada servidor, onde, quando o servidor já cumpriu o que precisava resolver no processo, ele ter a possibilidade de encerrar a tramitação daquele documento em sua mesa de trabalho individual, mas mantendo a tramitação normal nos demais setores e servidores;
  - b) Encerrar a tramitação num setor envolvido, onde, quando as responsabilidades de um setor, num determinado processo ou documento, já foi cumprida, seja possível encerrar a tramitação no setor em questão, e assim, em massa, nas respectivas mesas dos servidores que fazem parte dele, mas mantendo a tramitação normal nos demais setores envolvidos;
  - c) Encerrar a tramitação total do documento, onde, quando o setor responsável identificar que o processo chegou ao fim da sua tramitação, possa encerrar a tramitação total daquele documento e, por ser o setor responsável, consequentemente encerrar a tramitação do documento nas mesas de todos os setores e servidores envolvidos, de uma só vez.
- 1.35.4. Possibilidade, de acordo com necessidade e parametrização prévia, de gerar um documento de outro módulo e, automaticamente, associá-lo ao processo/documento em questão.
  - 1.35.4.1. O documento associado deve ser identificado que está apensado em outro documento ou processo, bem como, na impressão do documento ou processo que contém o documento associado, este também deve ser incluído.
- 1.35.5. Possibilidade de visualização do histórico do documento ou processo quando este tiver passado por retificações ou edições.

### 1.36 (p. 16)

Deve ser disponibilizado uma central de atendimento para que os cidadãos, empresas e entes externos possam ter acesso, através dos canais digitais do órgão, para realizar as suas solicitações e ter acesso aos serviços oferecidos pela entidade.

### 1.37 (p. 16)

Para acompanhamento das demandas externas, cada usuário externo deverá ter acesso a um ambiente virtual próprio, onde poderá receber notificações e acompanhar o andamento das demandas que abriu ou solicitou, bem como, realizar novas interações, realizar assinaturas, imprimir documentos, assim como, abrir novas demandas.

### 1.38 (p. 16)

O sistema a ser contratado deverá oferecer uma funcionalidade que permita a divulgação de documentos oficiais e comunicações internas, tanto para uso interno no órgão quanto para acesso público. Esta funcionalidade visa garantir a conformidade com as exigências legais, oferecendo os recursos que seguem descritos.

- 1.38.1. A funcionalidade de divulgação de documentos deverá incluir os seguintes tipos:
  - a) Divulgação interna (mural de servidores):
    - i. O sistema deverá permitir que documentos e/ou comunicações oficiais sejam divulgados no mural interno, visível a todos os servidores cadastrados;
    - ii. O sistema deverá dispor, em área particular de cada servidor, um mural onde devem ficar disponibilizadas as divulgações vinculadas a ele.
  - b) Divulgação Externa (Canal Oficial):
    - i. O sistema deverá permitir a divulgação de documentos em canal oficial do órgão, disponível na central de atendimento e acessível por qualquer pessoa com acesso à internet, sem a necessidade de login;
    - ii. A divulgação externa deverá incluir documentos como leis, decretos, portarias e editais, conforme regulamentado pelas normas internas do órgão.
- 1.38.2. O sistema deverá permitir que os documentos sejam configurados para divulgação enquanto estão em elaboração ou após emitidos, com opções para:
  - a) Divulgação imediata: ou seja, o documento será publicado assim que emitido;

*(quebra de página — continua na p. 17)*

  - b) Divulgação agendada: o documento será publicado em uma data específica, definida pelo usuário;
  - c) O sistema deverá permitir a edição das configurações de divulgação a qualquer momento, desde que o documento não tenha sido divulgado ainda;
  - d) Se a divulgação já tiver sido realizada, o sistema deverá permitir a remoção da publicação.
- 1.38.3. O sistema deverá permitir que os servidores ao acessar os documentos divulgados nos seus respectivos murais possam: visualizar, interagir ou tramitar os documentos, de acordo com suas permissões de usuário no documento em questão;
  - 1.38.3.1. O sistema deverá garantir que os cidadãos possam acessar os documentos divulgados no jornal oficial por meio de uma interface pública, com funcionalidades de busca e filtros para facilitar a consulta de documentos.

### 1.39 (p. 17)

O sistema deve permitir a exportação e impressão de documentos e processos administrativos, de forma flexível e segura, gerando arquivos em formato PDF que possam ser impressos ou compartilhados digitalmente.

- 1.39.1. O sistema deve garantir que diferentes partes de documentos e processos sejam exportadas conforme especificações técnicas a seguir.
- 1.39.2. A funcionalidade de exportação deve contemplar a geração de toda a árvore do processo em formato ".PDF", que deve incluir todas as movimentações do documento ou processo, tais como: anexos, despachos, documentos apensados, assinaturas e afins.
- 1.39.3. O sistema deve permitir a exportação da árvore do processo nos seguintes formatos:
  - a) Árvore básica: versão base do processo ou documento, com todas as suas partes, tais como: anexos, despachos, documentos apensados, assinaturas e afins;
  - b) Árvore personalizada: versão em que o servidor pode escolher quais partes da árvore do processo devem ser incluídos na exportação;
  - c) Árvore em formato PAdES: versão gerada toda vez que o documento for assinado, garantindo conformidade com a legislação de assinaturas digitais, para validação em sistema de reconhecimento de assinaturas digitais, tais como o ITI.
- 1.39.4. O sistema deve possibilitar a exportação de despachos isoladamente, contemplando o conteúdo do despacho, com anexos e documentos associados.
- 1.39.5. O sistema deve ainda prover esquema de segurança e otimização de exportação de documentos muito grandes, de modo que, documentos com tamanhos excessivos devam ser exportados já no formato zipado. Para esses casos as partes assinadas do documento devem vir em seu formato autenticável para validação das assinaturas realizadas;
- 1.39.6. Para documentos com tamanho regular, ou seja, aqueles que não são classificados como muito grandes e assim não sendo necessário baixá-los de forma compactada, deve ser oferecida a possibilidade de fazer o download destes de forma unificada e com a possibilidade de paginar.
  - 1.39.6.1. Para os casos, onde a estrutura do documento vai ser afetada durante a junção e paginação, ou seja, invalidando as assinaturas que por ventura venham a ter, deve se manter visivelmente os selos das assinaturas aplicadas, junto com link de direcionamento para área específica do sistema para validação das assinaturas no documento em questão, juntamente com a possibilidade de verificação do conteúdo do documento em questão, salvo os casos em que o documento é sigiloso, para que possa ser identificado se as assinaturas aplicadas estão válidas e se o conteúdo do documento corresponde ao que está sendo apresentado.

### 1.40 (p. 17)

O sistema deve disponibilizar o uso de assinaturas eletrônicas e digitais. Isso é especialmente importante para documentos sujeitos a auditorias, fiscalização externa, ou que necessitem de validação jurídica para trâmites em esferas públicas e privadas.

- 1.40.1. O sistema a ser contratado deverá atender aos seguintes requisitos técnicos:
  - a) Autenticação segura: Integração com tokens de autenticação para garantir a identidade do signatário, com suporte a certificação digital (ICP-Brasil);
  - b) Interface intuitiva: interface simples e intuitiva para permitir a fácil solicitação e realização de assinaturas por servidores e cidadãos;
  - c) Notificações: o sistema deverá enviar notificações automáticas para os signatários, informando-os das solicitações de assinatura, assim como para os solicitantes, conforme os signatários forem assinando;
  - d) Verificação de assinaturas: o sistema deverá permitir a verificação da autenticidade das assinaturas realizadas, em meio oficial do órgão.
- 1.40.2. O sistema deverá contemplar a utilização de diferentes tipos de assinaturas, variando de acordo com o nível de segurança e validade jurídica, sendo cada uma aplicável a contextos específicos de acordo com sua

*(quebra de página — continua na p. 18)*

  regulamentação e uso da a Lei nº 14.063, de 23 de setembro de 2020, e a Medida Provisória nº 2.200-2, de 24 de agosto de 2001.
  - 1.40.2.1. O sistema deverá fornecer as seguintes opções de tipos de assinatura:
    - a) Assinatura eletrônica simples: para processos administrativos internos ou em situações que não exigem um alto nível de segurança, deve fornecer a identificação do signatário, associando seus dados a documentos, processos, despachos e afins que este se vincular, tendo como dispositivo de segurança a autenticação, por login e senha ou uso de credenciais corporativas;
    - b) Assinatura eletrônica avançada: para transações que exigem segurança adicional, esse tipo de assinatura deve associar de forma inequívoca o signatário ao documento, garantindo que qualquer alteração posterior ao ato de assinatura seja detectada;
    - c) Assinatura eletrônica qualificada: para situações de documentos e processos de maior sensibilidade, como contratos, documentos fiscais ou documentos que serão submetidos a auditorias ou fiscalizações, deve ser possível a utilização de assinaturas baseadas em certificados digitais, emitidos por Autoridades Certificadoras vinculadas à estrutura da Infraestrutura de Chaves Públicas Brasileira.
- 1.40.3. O sistema deverá permitir que assinaturas sejam solicitadas por servidores em documentos e processos administrativos. Entre os principais requisitos estão:
  - a) Assinaturas simples: possibilitar a solicitação de assinaturas - de qualquer um dos tipos já determinados anteriormente - de qualquer servidor, cidadão ou contribuinte cadastrado no ambiente do órgão;
  - b) Assinaturas sequenciais: nos casos em que seja necessário possibilitar a definição de uma ordem de assinaturas, onde a ordem de assinaturas do documento, pelos signatários, deve ser seguida conforme foi definido na configuração. De modo que, enquanto o signatário da vez não assinar, os demais devem ficar impossibilitados de assinar;
  - c) Seleção de signatários: permitir a escolha de signatários internos (servidores) e externos (pessoas físicas ou jurídicas), respeitando as permissões e regras de tramitação do documento;
  - d) Locais de Assinatura: o sistema deverá oferecer a opção de selecionar os locais do documento onde o signatário deverá assinar, como documentos de abertura, anexos, despachos e outros.
- 1.40.4. O sistema deverá permitir o gerenciamento de solicitações de assinatura, possibilitando a edição e o cancelamento de assinaturas que ainda não tenham sido realizadas.
  - 1.40.4.1. As funcionalidades de gerenciamento devem incluir:
    - a) Nos casos em que a assinatura ainda não tenha sido realizada, possibilidade de alteração do tipo de assinatura e do papel do signatário;
    - b) Exclusão de signatários de solicitações de assinatura que ainda não assinaram, com registro automático do cancelamento no histórico do documento.
- 1.40.5. O sistema deve permitir que signatários, tanto internos quanto externos, possam recusar assinaturas, justificando o motivo da recusa. A recusa deve ser registrada e notificada ao solicitante.
- 1.40.6. O sistema deve permitir que servidores possam realizar assinaturas em massa de múltiplos documentos ou solicitações de uma só vez, garantindo agilidade nos processos com grande volume de assinaturas pendentes.

### 1.41 (p. 18)

Com o objetivo de garantir a delegação de tarefas administrativas sem comprometer a segurança e a rastreabilidade das ações, o sistema deve oferecer a possibilidade de criação de chaves de acesso para que seja possível que servidores autorizados possam criar documentos em nome de outros, de acordo com as permissões previamente estabelecidas, sem comprometer as credenciais de acesso. Essa função é fundamental para garantir a continuidade de processos administrativos de forma controlada, sem comprometer a segurança e a rastreabilidade das ações.

- 1.41.1. Para criação e gerenciamento de novas chaves deve ser possível o que segue:
  - a) A criação de chaves de acesso deverá ser possível de ser feita por qualquer nível de usuário, exceto o nível Visualizador;
  - b) Para criar uma nova chave, o servidor deverá, de acordo com os Arts 12 e 14 da Lei 9.784/1999, informar:
    - i. Servidor convenente;
    - ii. Um limite de uso para a chave, de modo que ele possa definir um período de uso e/ou uma quantidade de documentos possíveis de ser gerado com a chave;
    - iii. Os tipos de documentos que poderão ser gerados pela chave;
  - c) Uma chave de acesso deverá ser possível de ser concedida para um servidor que não faça parte do mesmo setor do servidor concedente;

*(quebra de página — continua na p. 19)*

    - i. uma vez atingido as permissões estabelecidas, a chave deverá ser automaticamente encerrada.
  - d) Os servidores deverão ter a possibilidade de ter uma visualização das chaves que tem como concedente e como convenente, podendo filtrá-las por:
    - i. Ativas;
    - ii. Encerradas;
    - iii. Agendadas.
  - e) Cada chave de acesso deverá manter um histórico de documentos gerados por ela, onde tanto o servidor convenente como concedente poderão acessar esse histórico e visualizar os documentos criados por meio da chave.
- 1.41.2. A seguir, estão descritos outros requisitos que a funcionalidade de chaves de acesso deverá atender:
  - a) Para um usuário que possua chave(s) de acesso(s) vinculada(s) a ele, ao criar um novo documento, o servidor deverá poder utilizar as permissões pessoais, de acordo com nível e setor(es) que pertence, ou uma chave de acesso concedida por outro servidor. O sistema deverá exibir os tipos de documentos disponíveis para o setor no qual o servidor está operando. Esta exibição deve considerar se o servidor possui acesso próprio e/ou uma chave de acesso;
  - b) Se o servidor tiver, para um determinado tipo de documento, apenas chave de acesso, ou seja, não tiver permissões próprias, ele deverá ser enviado diretamente para criação do documento, sem precisar passar por nenhum tipo de seleção;
  - c) Se o servidor possuir diferentes opções para gerar o documento (como chaves de acesso e permissões próprias), deverá ser apresentado um aviso de seleção, no qual o servidor escolherá se deseja criar o documento em seu nome ou utilizando a chave de outro servidor;
  - d) Sempre que um documento for gerado utilizando uma chave de acesso, o servidor que criou a chave receberá uma notificação, podendo visualizar e acompanhar o documento gerado;
  - e) Todo o uso da chave de acesso deverá ser registrado para garantir a rastreabilidade e controle de atividades;
  - f) As chaves de acesso podem ser encerradas automaticamente ou manualmente, dependendo das regras que foram definidas no momento de sua criação ou quando da vontade do usuário que a concedeu.

### 1.42 (p. 19)

O sistema deve oferecer ainda área destinada à personalização de informações relacionadas ao cadastro e à identidade visual do órgão.

- 1.42.1. As ações permitidas incluem:
  - a) Acesso às informações cadastrais do órgão, tais como:
    - i. Quantidade de licenças;
    - ii. Período de contrato;
    - iii. Módulos contratados.
  - b) Possibilidade de editar as cores temáticas da interface do menu principal do sistema;
  - c) Upload e gerenciamento das imagens institucionais do órgão que serão exibidas em todo o sistema.

### 1.43 (p. 19)

O sistema deverá possuir funcionalidade de estatísticas da solução que permita aos administradores e usuários autorizados a visualização detalhada e organizada de dados do uso e desempenho de várias áreas do sistema, como setores, módulos, servidores e consumo de recursos, facilitando a tomada de decisões baseadas em dados concretos e em conformidade com as exigências legais.

- 1.43.1. O sistema deverá utilizar os seguintes visualizadores:
  - a) Gráficos: destinados a uma visão gerencial, exibindo dados agregados;
  - b) Tabelas: destinadas a uma visão operacional detalhada, complementando as informações dos gráficos.
- 1.43.2. Os relatórios de estatísticas deverão ser categorizados nas seguintes áreas:
  - a) Setores;
  - b) Módulos;
  - c) Servidores;
  - d) Consumo de recursos.
- 1.43.3. O sistema deverá exibir dados referentes aos setores e subsetores cadastrados, permitindo comparações entre eles.
  - 1.43.3.1. Além de gráficos, deverá haver uma exibição de dados gerais, como:
    - a) Total de setores e quantidade de: setores principais, subsetores, setores ativos e setores inativos;
    - b) Demandas recebidas: quantidade de documentos recebidos, categorizados em demandas internas e externas, com a aplicação de filtros por período e setor;
    - c) Tempo médio de resolução de demandas: cálculo do tempo médio até o encerramento dos documentos com base nos dados dos setores;

*(quebra de página — continua na p. 20)*

    - d) Documentos por situação: quantidade de documentos, por setor, categorizados por status (em aberto, em elaboração, em tramitação, pausado, encerrado);
    - e) Engajamento de setores: média de engajamento de cada setor, com cálculo baseado nas ações realizadas nos documentos;
    - f) Qualidade de atendimento externo: avaliações de satisfação dos usuários externos nos documentos e/ou processos que participaram, por setor.
- 1.43.4. O sistema deverá apresentar dados estatísticos sobre os documentos criados nos módulos contratados, como:
  - a) Total de documentos criados: categorizado em documentos internos e externos, com filtros por período, módulo ou assunto ou serviço;
  - b) Demandas por módulo: categorizando em rankings de utilização, identificando aqueles que possuem o maior volume de utilização;
  - c) Demandas por serviço ou assunto: categorizando em rankings de utilização, identificando aqueles que possuem o maior volume de utilização;
  - d) Documentos por situação: visualização dos documentos criados em cada módulo, por status (em aberto, em elaboração, em tramitação, pausado, encerrado);
  - e) Qualidade de atendimento externo: avaliações de satisfação dos usuários externos nos documentos e/ou processos que participaram, por módulo.
- 1.43.5. O sistema deverá exibir informações detalhadas sobre os servidores cadastrados na plataforma, incluindo:
  - a) Total de servidores: ativos e inativos;
  - b) Servidores por status: quantidade de servidores categorizados por status (ativos, inativos, em licença, em férias);
  - c) Servidores por nível de permissão: exibição por níveis;
  - d) Tempo médio de permanência na plataforma: tempo médio de permanência dos servidores no sistema;
  - e) Engajamento por usuário: exibição dos usuários mais e menos engajados, com cálculo baseado nas ações realizadas nos documentos.
- 1.43.6. O sistema deverá exibir o consumo de recursos e a economia gerada pela digitalização dos processos, incluindo:
  - a) Armazenamento total: quantidade total de armazenamento de arquivos em MB ou GB;
  - b) Economia gerada: estimativa do valor economizado em papel e tinta, com base na utilização do sistema;
  - c) Impressões e assinaturas: quantidade de documentos impressos e assinaturas realizadas;
  - d) Usuários externos e atendimentos: quantidade de usuários externos e atendimentos realizados.
