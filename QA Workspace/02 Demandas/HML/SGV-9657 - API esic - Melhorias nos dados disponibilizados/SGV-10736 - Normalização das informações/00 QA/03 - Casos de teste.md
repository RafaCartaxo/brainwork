---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]"
status: execucao
pontos: ""
---

# Casos de teste — SGV-10736

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os cenários executáveis. Todos os cenários são de **API** (fluxo 3f) — "Quando" chama o endpoint, "Então" valida o payload de resposta, sem tela envolvida.

> [!info]- Renumeração de 05/10/2026 (call com os responsáveis)
> CT-008 (status "Respondido" na listagem) e CT-010 (totalAnswered nas estatísticas) saíram da rodada ativa — "Respondido" não existe como status no sistema, confirmado por Marcos; totalAnswered foi retirado do contrato. Ver [[#G. Fora de execução — registro]]. CT-009 foi reescrito (não depende mais de "Respondido") e os CTs seguintes foram renumerados pra ficar contíguos: CT-011→CT-009, CT-012→CT-010, CT-013→CT-011, CT-014→CT-012. CT-013 e CT-014 atuais são novos, cobrindo os critérios C10/C11 (mensagem de erro em português e coerência status code↔message) que só entraram no escopo nesta call — ainda sem execução real.

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-003\|CT-003]], [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c4\|C4]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c5\|C5]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-006\|CT-006]], [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c6\|C6]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c7\|C7]] | *(retirado do contrato — ver [[#G. Fora de execução — registro]])* |
| [[01 - Demanda#^c8\|C8]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c9\|C9]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-010\|CT-010]], [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-011\|CT-011]], [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c10\|C10]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-013\|CT-013]] |
| [[01 - Demanda#^c11\|C11]] | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-014\|CT-014]] |

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
> **Execução:** aprovado — confirmado em homologação (05/10/2026)

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
> **Então** cada solicitação deve retornar `requester.type` correspondente, com os dados do solicitante preenchidos no bloco correto (pessoa física vs. pessoa jurídica)
>
> **Resultado esperado:** `requester.type` e o bloco de dados correspondente batem com o tipo real do solicitante.
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
> **Execução:** aprovado com ressalva — distinção funciona (`PF`/`PJ`); nomenclatura final ainda em padronização (ver `01 - Demanda`, pendência de nomenclatura)

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
> **Então** a solicitação deve retornar a data de nascimento e o gênero preenchidos com os valores cadastrados
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
> **Execução:** aprovado — confirmado em homologação (05/10/2026)

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
> **Então** a API deve responder normalmente (sem erro 500), retornando a solicitação com os campos de nascimento/gênero ausentes ou nulos, sem quebrar os demais campos da solicitação
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
> **Execução:** aguardando — sem registro de solicitante PF incompleto na massa de dados testada até agora

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
> **Execução:** aprovado — confirmado em homologação (05/10/2026)

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
> **Execução:** aguardando — sem registro de solicitação com prazo configurado na massa de dados testada até agora

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
> **Execução:** reprovado — `orderDateDeadline` veio `null` em 10/10 registros (ver [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/00 README|10736-CT-007]]). Confirmado real na call de 05/10/2026 — qual valor usar quando não há prazo configurado é decisão pendente do Marcos.

^ct-007

> [!example]- CT-008 · Distinguir corretamente os status Recebido, Em Andamento e Encerrado
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
> **Descrição:** confirma que a listagem distingue corretamente os três status de solicitação existentes no sistema — reescrito em 05/10/2026: a versão anterior também cobria "Respondido", status que não existe no sistema (confirmado por Marcos na call), removido do escopo (ver [[#G. Fora de execução — registro]]).
>
> **Pré-condições:**
> - Existir ao menos uma solicitação em cada status: Recebido, Em Andamento e Encerrado.
>
> **Dado** que existam solicitações em todos os status possíveis (Recebido, Em Andamento, Encerrado)
> **Quando** a listagem de solicitações for consultada
> **Então** cada solicitação deve retornar o `orderStatus` correspondente ao seu estado real, sem sobreposição entre os três
>
> **Resultado esperado:** os três status aparecem corretamente distribuídos entre as solicitações, sem sobreposição.
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
> **Execução:** aprovado com ressalva — "Encerrado" confirmado em 10/10 registros reais; "Recebido" e "Em Andamento" ainda sem exemplo cruzado na massa de dados testada

^ct-008

> [!example]- CT-009 · Retornar o ID do solicitante no ranking, diferenciando nomes iguais
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
> **Execução:** aprovado — `id` distinto confirmado entre 3 entradas "Sem Nome" do ranking. Achado à parte (não invalida este CT): [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/00 README|10736-CT-011]] — o campo `name` vem errado pra PJ e Anônimo

^ct-009

> [!example]- CT-010 · Contabilizar corretamente solicitações dentro do prazo
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
> **Execução:** aguardando — 0 solicitações "timely" na amostra testada do cliente

^ct-010

> [!example]- CT-011 · Contabilizar corretamente solicitações fora do prazo
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
> **Execução:** aguardando — 0 solicitações "delayed" na amostra testada do cliente

^ct-011

> [!example]- CT-012 · Contabilizar corretamente solicitações sem prazo configurado
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
> **Execução:** aprovado com ressalva — `undefined: 24` bate com as 24 solicitações do cliente, mas mascarado pelo Bug [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-007/00 QA/00 README|10736-CT-007]] (tudo cai em "undefined" porque nada é calculado) — confirmar de novo quando o Bug for corrigido

^ct-012

> [!example]- CT-013 · Retornar mensagem de erro em português
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
> **Descrição:** confirma que, em cenário de erro, a API retorna a mensagem (`message`) em português — item novo, trazido pela call de 05/10/2026 (padronização de erros).
>
> **Pré-condições:**
> - Existir um cenário de erro reproduzível na API (ex.: parâmetro inválido, recurso não encontrado).
>
> **Dado** que uma chamada à API resulte em erro
> **Quando** a resposta de erro for inspecionada
> **Então** o campo `message` deve vir em português, descrevendo o problema de forma compreensível
>
> **Resultado esperado:** `message` em português, sem termos técnicos/internos vazando pro texto.
>
> **Pós-condição:** nenhuma alteração de dado.
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado — ainda sem execução real; cenário de erro a definir com o time

^ct-013

> [!example]- CT-014 · Status code da resposta coerente com a mensagem de erro
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
> **Descrição:** confirma que o status code HTTP retornado é coerente com a mensagem de erro — item novo, trazido pela call de 05/10/2026 (padronização de erros).
>
> **Pré-condições:**
> - Existir um cenário de erro reproduzível na API (ex.: parâmetro inválido, recurso não encontrado, não autorizado).
>
> **Dado** que uma chamada à API resulte em erro
> **Quando** a resposta de erro for inspecionada
> **Então** o status code HTTP (ex.: 400, 404, 401) deve corresponder ao tipo de erro descrito na `message`
>
> **Resultado esperado:** nenhuma combinação incoerente (ex.: 200 com mensagem de erro, ou 500 para erro de validação de entrada).
>
> **Pós-condição:** nenhuma alteração de dado.
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** API
> **Automação:** manual
> **Execução:** planejado — ainda sem execução real; cenário de erro a definir com o time

^ct-014

---

## G. Fora de execução — registro

*Casos considerados e deliberadamente não executados nesta rodada. Ficam aqui pra não sumirem do histórico e pra não abrirem buraco na numeração dos ativos.*

| Caso | Decisão | Motivo |
|---|---|---|
| CT-008 (antigo) · Retornar o status "Respondido" para solicitação respondida | **Removido — não se aplica** (Marcos, 05/10/2026) | Status "Respondido" não existe no sistema — a API deriva `orderStatus` do andamento interno do documento (tramitação), não do fato de já ter sido respondido ao cidadão. Confirmado em call com os responsáveis. |
| CT-010 (antigo) · Contabilizar corretamente o total de solicitações respondidas nas estatísticas | **Removido — não se aplica** (Marcos, 05/10/2026) | Mesma causa: sem status "Respondido" no sistema, não há o que contar em `totalAnswered`. Requisito retirado do contrato (ver C7 em `01 - Demanda` e Bug [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-010/00 QA/00 README\|10736-CT-010]], fechado como requisito retirado). |
