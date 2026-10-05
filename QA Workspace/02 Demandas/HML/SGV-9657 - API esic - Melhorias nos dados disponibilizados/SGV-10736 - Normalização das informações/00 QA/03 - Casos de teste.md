---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-10736

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis. Todos os cenários são de **API** (fluxo 3f) — "Quando" chama o endpoint, "Então" valida o payload de resposta, sem tela envolvida.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-006\|CT-006]], [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-008\|CT-008]], [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-010\|CT-010]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-011\|CT-011]] |
| [[01 - Demanda#^c9\|C9]] | [[03 - Casos de teste#^ct-012\|CT-012]], [[03 - Casos de teste#^ct-013\|CT-013]], [[03 - Casos de teste#^ct-014\|CT-014]] |

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

---

> [!example]- CT-001 · Retornar ID do solicitante na listagem, diferenciando nomes iguais
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que a listagem de solicitações identifica unicamente cada solicitante, mesmo quando dois têm o mesmo nome.
>
> **Pré-condições:**
> - Existirem ao menos duas solicitações de solicitantes diferentes com o mesmo nome completo cadastrado.
>
> **Dado** que existam solicitações de dois solicitantes distintos com o mesmo nome completo
> **Quando** a listagem de solicitações for consultada
> **Então** cada solicitação deve retornar `requester.id` próprio, permitindo distinguir os dois solicitantes mesmo com o nome igual
>
> **Resultado esperado:** `requester.id` presente e diferente entre as duas solicitações, apesar do nome idêntico.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Retornar o tipo do solicitante (Pessoa Física/Jurídica)
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que a listagem informa corretamente se o solicitante é Pessoa Física ou Pessoa Jurídica.
>
> **Pré-condições:**
> - Existir ao menos uma solicitação de um solicitante Pessoa Física e uma de Pessoa Jurídica.
>
> **Dado** que existam solicitações de um solicitante Pessoa Física e de um solicitante Pessoa Jurídica
> **Quando** a listagem de solicitações for consultada
> **Então** cada solicitação deve retornar `requester.type` correspondente ("Pessoa Física" ou "Pessoa Jurídica"), com os dados em `data.PessoaFisica` preenchidos para o primeiro e `data.PessoaJuridica` para o segundo
>
> **Resultado esperado:** `requester.type` e o bloco `data` correspondente batem com o tipo real do solicitante.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Retornar data de nascimento e gênero do solicitante PF com cadastro completo
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que, quando o solicitante Pessoa Física tem data de nascimento e gênero cadastrados, a API retorna os dois campos.
>
> **Pré-condições:**
> - Existir solicitação de solicitante Pessoa Física com data de nascimento e gênero preenchidos no cadastro.
>
> **Dado** que exista uma solicitação de um solicitante Pessoa Física com data de nascimento e gênero cadastrados
> **Quando** a listagem de solicitações for consultada
> **Então** a solicitação deve retornar `data.PessoaFisica.dataNascimento` e `data.PessoaFisica.genero` preenchidos com os valores cadastrados
>
> **Resultado esperado:** os dois campos aparecem com os valores corretos, sem formatação divergente da cadastrada.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Não quebrar a API quando solicitante PF não tiver data de nascimento/gênero cadastrados
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que a ausência de data de nascimento/gênero no cadastro do solicitante não gera erro nem quebra a resposta da API.
>
> **Pré-condições:**
> - Existir solicitação de solicitante Pessoa Física **sem** data de nascimento e/ou gênero cadastrados.
>
> **Dado** que exista uma solicitação de um solicitante Pessoa Física sem data de nascimento e gênero cadastrados
> **Quando** a listagem de solicitações for consultada
> **Então** a API deve responder normalmente (sem erro 500), retornando a solicitação com `dataNascimento` e/ou `genero` ausentes ou nulos, sem quebrar os demais campos da solicitação
>
> **Resultado esperado:** resposta HTTP de sucesso, campos faltantes vêm ausentes/nulos, demais dados da solicitação intactos.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** borda
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Retornar a data de abertura da solicitação
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que toda solicitação retornada traz sua data de abertura.
>
> **Pré-condições:**
> - Existir ao menos uma solicitação registrada.
>
> **Dado** que exista uma solicitação registrada no sistema
> **Quando** a listagem de solicitações for consultada
> **Então** a solicitação deve retornar `orderDate` preenchido com a data real de abertura
>
> **Resultado esperado:** `orderDate` presente e coerente com a data de criação da solicitação.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Calcular a data limite da solicitação quando há prazo configurado
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que, havendo prazo configurado, a API calcula e retorna a data limite, a quantidade de dias e o tipo de contagem.
>
> **Pré-condições:**
> - Existir solicitação com prazo de atendimento configurado (dias úteis ou corridos).
>
> **Dado** que exista uma solicitação com prazo de atendimento configurado
> **Quando** a listagem de solicitações for consultada
> **Então** a solicitação deve retornar `orderDateDeadline.date`, `orderDateDeadline.days` e `orderDateDeadline.type` ("Dias úteis" ou "Dias corridos") consistentes com o prazo configurado
>
> **Resultado esperado:** os três campos presentes e com valores compatíveis com a regra de prazo configurada.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Calcular a data limite mesmo quando a solicitação não tem prazo configurado
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que a ausência de prazo configurado não impede o cálculo da data limite — regra central desta entrega.
>
> **Pré-condições:**
> - Existir solicitação **sem** prazo de atendimento configurado.
>
> **Dado** que exista uma solicitação sem prazo de atendimento configurado
> **Quando** a listagem de solicitações for consultada
> **Então** a solicitação deve retornar `orderDateDeadline` preenchido (não nulo/ausente), calculado por uma regra padrão, permitindo saber se a solicitação está ou não dentro do prazo mesmo sem configuração explícita
>
> **Resultado esperado:** `orderDateDeadline` presente e coerente, nunca ausente só por falta de configuração.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** borda
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-007

> [!example]- CT-008 · Retornar o status "Respondido" para solicitação respondida
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que uma solicitação já respondida é identificada com o novo status "Respondido", e não mais como "Em Andamento".
>
> **Pré-condições:**
> - Existir solicitação já respondida pelo órgão.
>
> **Dado** que exista uma solicitação já respondida
> **Quando** a listagem de solicitações for consultada
> **Então** a solicitação deve retornar `orderStatus` como "Respondido"
>
> **Resultado esperado:** `orderStatus` = "Respondido" para essa solicitação.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-008

> [!example]- CT-009 · Distinguir "Respondido" dos demais status (Recebido, Em Andamento, Encerrado)
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o novo status "Respondido" não se confunde com os demais status já existentes.
>
> **Pré-condições:**
> - Existir ao menos uma solicitação em cada status: Recebido, Em Andamento, Respondido e Encerrado.
>
> **Dado** que existam solicitações em todos os status possíveis (Recebido, Em Andamento, Respondido, Encerrado)
> **Quando** a listagem de solicitações for consultada
> **Então** cada solicitação deve retornar o `orderStatus` correspondente ao seu estado real, sem nenhuma solicitação "Em Andamento" ou "Encerrada" sendo classificada como "Respondido" e vice-versa
>
> **Resultado esperado:** os quatro status aparecem corretamente distribuídos entre as solicitações, sem sobreposição.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-009

> [!example]- CT-010 · Contabilizar corretamente o total de solicitações respondidas nas estatísticas
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o endpoint de estatísticas soma corretamente as solicitações com status "Respondido".
>
> **Pré-condições:**
> - Existir uma quantidade conhecida de solicitações com status "Respondido".
>
> **Dado** que exista uma quantidade conhecida de solicitações respondidas
> **Quando** o endpoint de estatísticas for consultado
> **Então** `statistics.status.totalAnswered` deve corresponder exatamente à quantidade de solicitações com status "Respondido"
>
> **Resultado esperado:** `totalAnswered` bate com a contagem real, sem incluir solicitações de outros status.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-010

> [!example]- CT-011 · Retornar o ID do solicitante no ranking, diferenciando nomes iguais
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o ranking de solicitantes nas estatísticas identifica unicamente cada solicitante, mesmo com nomes iguais.
>
> **Pré-condições:**
> - Existirem dois solicitantes distintos com o mesmo nome, ambos no ranking.
>
> **Dado** que existam dois solicitantes distintos de mesmo nome, ambos com solicitações suficientes para aparecer no ranking
> **Quando** o endpoint de estatísticas for consultado
> **Então** `rankingRequesters` deve retornar uma entrada por solicitante, cada uma com seu `id` próprio, mesmo com o campo `name` igual nas duas entradas
>
> **Resultado esperado:** duas entradas distintas no ranking, com `id` diferente e contagem (`ordersPerPage`) correta para cada uma.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-011

> [!example]- CT-012 · Contabilizar corretamente solicitações dentro do prazo
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o endpoint de estatísticas soma corretamente as solicitações dentro do prazo de atendimento.
>
> **Pré-condições:**
> - Existir uma quantidade conhecida de solicitações dentro do prazo (`orderDateDeadline` ainda não vencido).
>
> **Dado** que exista uma quantidade conhecida de solicitações dentro do prazo
> **Quando** o endpoint de estatísticas for consultado
> **Então** `statistics.deadline.timely` deve corresponder exatamente à quantidade de solicitações dentro do prazo
>
> **Resultado esperado:** `timely` bate com a contagem real.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-012

> [!example]- CT-013 · Contabilizar corretamente solicitações fora do prazo
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o endpoint de estatísticas soma corretamente as solicitações já fora do prazo de atendimento.
>
> **Pré-condições:**
> - Existir uma quantidade conhecida de solicitações fora do prazo (`orderDateDeadline` já vencido e sem resposta).
>
> **Dado** que exista uma quantidade conhecida de solicitações fora do prazo
> **Quando** o endpoint de estatísticas for consultado
> **Então** `statistics.deadline.delayed` deve corresponder exatamente à quantidade de solicitações fora do prazo
>
> **Resultado esperado:** `delayed` bate com a contagem real.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-013

> [!example]- CT-014 · Contabilizar corretamente solicitações sem prazo configurado
>
> ```meta-bind-button
> style: primary
> label: ↩ Validação
> action:
>   type: open
>   link: "[[04 - Validação dev#Resultado dos casos de teste]]"
> ```
>
> ## Cenário
>
> **Descrição:** confirma que o endpoint de estatísticas identifica separadamente as solicitações sem prazo configurado, sem misturá-las com "dentro" ou "fora" do prazo.
>
> **Pré-condições:**
> - Existir uma quantidade conhecida de solicitações sem prazo de atendimento configurado.
>
> **Dado** que exista uma quantidade conhecida de solicitações sem prazo configurado
> **Quando** o endpoint de estatísticas for consultado
> **Então** `statistics.deadline.undefined` deve corresponder exatamente a essa quantidade, sem que essas solicitações sejam contadas em `timely` ou `delayed`
>
> **Resultado esperado:** `undefined` bate com a contagem real, e a soma de `timely + delayed + undefined` corresponde ao total de solicitações.
>
> **Pós-condição:** nenhuma alteração de dado — consulta somente leitura.
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** borda
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado

^ct-014
