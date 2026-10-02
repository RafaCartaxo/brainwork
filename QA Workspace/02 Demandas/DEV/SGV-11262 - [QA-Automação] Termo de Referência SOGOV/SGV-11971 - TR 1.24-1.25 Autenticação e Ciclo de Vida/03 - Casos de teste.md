---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: executado
pontos: ""
---

# Casos de teste — SGV-11971 (TR 1.24-1.25)

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[Automação/Plano de Automação|Plano]] · [[Automação/Handoff de execução|Handoff de execução]] · [[Automação/Documentação de Entrega|Documentação de Entrega]]

> **Fonte única** dos casos deste Termo. Numeração `CT-001`–`CT-038`, única e contígua ao longo das 5 suites, mais 3 extras `CT-E01`–`CT-E03` fora do escopo do Termo. A precondição de cada caso vive na cláusula `Dado`, como no documento original do Termo.

> [!info]- Histórico de revisões dos casos
> - **31/08/2026 — fonte única.** Três versões divergentes (planilha original de execução, versão organizada para a Qase e versão Gherkin do vault) foram consolidadas aqui. `Prioridade`, `Requisito` e `Citação do Termo` adicionados em todos os casos; granularidade de CT-018/CT-019 incorporada; precondição do CT-003 padronizada em "cidadão PJ".
> - **20/08/2026 — 37 → 38 casos.** O antigo TC-05 volta como CT-005 (caso redundante mas válido: um CPF nunca autentica no contexto de Empresa); tudo da posição 5 em diante desloca +1.
> - **19/08/2026 — 39 → 37 casos.** CT-005 antigo removido (premissa inexistente: a tela é campo único); CT-012 e CT-033 antigos absorvidos — a checagem de que as mensagens de erro são distintas virou cláusula no `Então` de CT-009/CT-010/CT-014/CT-031.
> - **18/08/2026 — arquitetura real.** Ver as decisões de produto em [[01 - Demanda#Decisões de produto]].

---

## Legenda — Shared Steps

Cada `Quando`/`E` abaixo já traz a ação por extenso; a tag `[SS-0N]` ao lado é só rastreabilidade — indica que aquele passo é uma instância de uma sequência reutilizada em outros casos. Um shared step só existe aqui se for de fato reusado em 2+ casos.

| ID | Ação completa |
|---|---|
| **SS-01a** | Acessar a tela do **servidor** (exclusiva, CPF apenas), informar o CPF cadastrado e a senha correta, e confirmar — usado em CT-001, CT-020 |
| **SS-01b** | Acessar a tela do **cidadão** — campo único de identificação, compartilhado entre CPF (pessoa física) e CNPJ (empresa) — informar o identificador correto e a senha correta, e confirmar — usado em CT-002, CT-003, CT-005, CT-009 |
| **SS-02** | Acessar a tela de login, informar um identificador válido e uma senha incorreta, e tentar autenticar (1 tentativa) — usado em CT-010 e como base do SS-03 |
| **SS-03** | Repetir o SS-02 **N** vezes seguidas para o mesmo usuário (N varia por caso) — usado em CT-013 (N=5), CT-014 (N=4), CT-018 (N=3, duas vezes), CT-019 (N=5) |
| **SS-04a** | Tentar autenticar normalmente com CPF e senha, estando em afastamento legal — usado em CT-021 (Licença), CT-027 (Férias) |
| **SS-04b** | Já logado, observar a tela inicial/mesa de trabalho — usado em CT-022 (Licença), CT-028 (Férias) |
| **SS-04c** | Tentar uma ação de escrita/aprovação — usado em CT-023 (Licença), CT-029 (Férias) |
| **SS-04d** | Tentar uma ação de leitura/consulta — **hoje sem nenhum acesso, nem de leitura** (o "subconjunto mínimo de funcionalidades não transacionais" do Termo não obriga a incluir visibilidade) — usado em CT-024 (Licença), CT-030 (Férias) |
| **SS-05** | Aguardar (ou simular) a data de término do período de Licença/Férias do servidor, e autenticar novamente — usado em CT-026 (Licença), CT-031 (Férias) |
| **SS-06** | Autenticar no **contexto de cidadão** com o CPF de um servidor que está em afastamento ou inativo — usado em CT-E01, CT-E02, CT-E03 (extras, fora do Termo) |

Os 2 casos de desbloqueio (CT-016/CT-017) não têm shared step próprio — cada um é uma ação única; só reaproveitam a pré-condição "conta bloqueada" do CT-015.

---

## Suite 1 — Tipos de acesso (1.24)

> [!example]- CT-001 · Servidor Público autentica com sucesso usando CPF e senha corretos
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
> **Descrição:** confirma a conformidade com o item 1.24.1 do Termo de Referência.
>
> **Dado** que o servidor está cadastrado, vinculado a um setor e com status "Ativo"  
> **Quando** ele acessa a tela de login do servidor, informa o CPF cadastrado e a senha correta, e confirma o login **[SS-01a]**  
> **Então** o acesso é concedido e o servidor é direcionado à sua mesa de trabalho, com as permissões do seu nível/perfil
>
> **Pós-condição:** sessão autenticada no contexto de servidor; sem outra alteração de estado persistente
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.24.1  
> **Citação do Termo:** 1.24.1. Servidor Público: Autenticação por CPF(Obrigatoriamente) e senha;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-001

> [!example]- CT-002 · Cidadão (Pessoa Física) autentica com sucesso usando CPF e senha corretos
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
> **Descrição:** confirma a conformidade com o item 1.24.2 do Termo de Referência.
>
> **Dado** que o cidadão está cadastrado na central de atendimento externo  
> **Quando** ele acessa a tela de login do cidadão — a mesma usada por empresas (pessoa jurídica), com um único campo de identificação — informa o CPF cadastrado e a senha correta, e confirma o login **[SS-01b]**  
> **Então** o acesso é concedido ao ambiente virtual do cidadão (acompanhamento de demandas)
>
> **Pós-condição:** sessão autenticada no contexto de cidadão; sem outra alteração de estado persistente
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.24.2  
> **Citação do Termo:** 1.24.2. Cidadão (Pessoa Física): Autenticação por CPF(Obrigatoriamente) e senha;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-002

> [!example]- CT-003 · Empresa (Pessoa Jurídica) autentica com sucesso usando CNPJ e senha corretos
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
> **Descrição:** confirma a conformidade com o item 1.24.3 do Termo de Referência.
>
> **Dado** que a empresa está cadastrada como cidadão PJ  
> **Quando** ela acessa a mesma tela de login do cidadão do CT-002 — campo único, compartilhado com pessoa física — informa o CNPJ cadastrado e a senha correta, e confirma o login **[SS-01b]**  
> **Então** o acesso é concedido ao ambiente virtual da empresa
>
> **Pós-condição:** sessão autenticada no contexto de empresa; sem outra alteração de estado persistente
>
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.24.3  
> **Citação do Termo:** 1.24.3. Empresas e outras entidades (Pessoa Jurídica): Autenticação por CNPJ (Obrigatoriamente) e senha.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-003

> [!example]- CT-004 · Servidor não consegue autenticar informando um CNPJ no campo de identificação
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
> **Descrição:** confirma a conformidade com o item 1.24.1 / 1.24.3 do Termo de Referência.
>
> **Dado** que a tela de login do servidor está aberta (tela própria, distinta da tela do cidadão)  
> **Quando** alguém informa um CNPJ (14 dígitos) no campo destinado à identificação do servidor  
> **E** tenta autenticar  
> **Então** o sistema não permite o envio ou rejeita a autenticação, porque o servidor deve se autenticar exclusivamente por CPF (11 dígitos)
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]] · [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.24.1 / 1.24.3  
> **Citação do Termo:** 1.24.1. Servidor Público: Autenticação por CPF(Obrigatoriamente) e senha; (...) 1.24.3. Empresas e outras entidades (Pessoa Jurídica): Autenticação por CNPJ (Obrigatoriamente) e senha.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-004

> [!example]- CT-005 · Ao informar um CPF na tela de login compartilhada, o sistema nunca autentica no contexto de Empresa
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
> **Descrição:** confirma a conformidade com o item 1.24.2 / 1.24.3 do Termo de Referência.
>
> **Dado** que a tela de login do cidadão está aberta — o mesmo campo único usado por pessoa física e empresa (mesma tela dos CT-002/CT-003)  
> **Quando** a pessoa informa um CPF cadastrado (11 dígitos) e a senha correta, na mesma tela usada pelas empresas **[SS-01b]**  
> **Então** o login funciona, mas sempre no contexto de Cidadão (pessoa física) — o perfil Empresa nunca é atribuído a um login feito com CPF, já que a empresa se identifica exclusivamente por CNPJ (14 dígitos)
>
> **Pós-condição:** se houver cadastro correspondente, sessão aberta no contexto de Cidadão; nunca no contexto de Empresa
>
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]] · [[01 - Demanda#^c5|C5]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.24.2 / 1.24.3  
> **Citação do Termo:** 1.24.2. Cidadão (Pessoa Física): Autenticação por CPF(Obrigatoriamente) e senha; (...) 1.24.3. Empresas e outras entidades (Pessoa Jurídica): Autenticação por CNPJ (Obrigatoriamente) e senha.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-005

> [!example]- CT-006 · Sistema rejeita CPF com dígito verificador inválido em qualquer tela de login
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
> **Descrição:** confirma a conformidade com o item 1.24 / 1.25 do Termo de Referência.
>
> **Dado** que uma tela de login que exige CPF está aberta (do servidor ou do cidadão)  
> **Quando** é informado um CPF com 11 dígitos, mas com dígito verificador inválido (ex.: 123.456.789-00)  
> **E** a pessoa tenta avançar  
> **Então** o sistema não faz nenhuma validação de formato antes do envio — a requisição segue normal e falha porque não existe nenhuma conta com esse CPF, com a mesma mensagem genérica de credenciais não reconhecidas (mesmo caminho do CT-011)
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]] · [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.24 / 1.25  
> **Citação do Termo:** [Regra de validação de formato não é explícita no documento] 1.24. "(...) o sistema deve permitir o login (...)"; 1.25. "O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-006

> [!example]- CT-007 · Sistema rejeita CNPJ com dígito verificador inválido na tela de login do cidadão
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
> **Descrição:** confirma a conformidade com o item 1.24 / 1.25 do Termo de Referência.
>
> **Dado** que a tela de login do cidadão está aberta (mesma tela compartilhada dos CT-002/CT-003)  
> **Quando** é informado um CNPJ com dígito verificador inválido (ex.: 12.345.678/0001-00)  
> **E** a pessoa tenta avançar  
> **Então** o sistema não faz nenhuma validação de formato antes do envio — a requisição segue normal e falha porque não existe nenhuma conta com esse CNPJ, com a mesma mensagem genérica de credenciais não reconhecidas (mesmo caminho do CT-011)
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]] · [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.24 / 1.25  
> **Citação do Termo:** [Regra de validação de formato não é explícita no documento] 1.24.3. "Empresas e outras entidades (Pessoa Jurídica): Autenticação por CNPJ (Obrigatoriamente) e senha."; 1.25. "O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-007

> [!example]- CT-008 · Sistema impede um segundo cadastro vinculado a um CPF/CNPJ já existente
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
> **Descrição:** confirma a conformidade com o item 1.24 do Termo de Referência.
>
> **Dado** que já existe um usuário (servidor, cidadão ou empresa) cadastrado com um determinado CPF/CNPJ  
> **Quando** alguém inicia um novo cadastro (interno, por link, ou externo)  
> **E** informa esse mesmo CPF/CNPJ já cadastrado  
> **E** tenta concluir o cadastro  
> **Então** o sistema impede a duplicidade e informa que o CPF/CNPJ já está vinculado a um cadastro existente
>
> **Pós-condição:** nenhum novo cadastro é criado; o cadastro original permanece único
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.24  
> **Citação do Termo:** 1.24. O sistema deverá permitir o login para os seguintes tipos de usuários, observando que cada acesso deverá ser único e vinculado exclusivamente a um único CPF ou CNPJ:  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-008

> [!example]- CT-009 · Servidor autentica na tela do cidadão com o próprio CPF, mas no contexto de cidadão
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
> **Descrição:** confirma a conformidade com o item 1.24 do Termo de Referência.
>
> **Dado** que o usuário está cadastrado como servidor e, por ser servidor, também possui acesso como cidadão vinculado ao mesmo CPF  
> **Quando** ele acessa a tela de login do cidadão (não a do servidor) e informa esse mesmo CPF e a senha correta **[SS-01b]**  
> **Então** o login é bem-sucedido, mas o acesso concedido é o do contexto de cidadão (ambiente de acompanhamento de demandas) — não o da mesa de trabalho de servidor
>
> **Pós-condição:** sessão ativa no contexto de cidadão; nenhuma sessão ou contexto de servidor é aberto a partir desse login
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.24  
> **Citação do Termo:** [Não há regra explícita no documento] Regra mais próxima — 1.24: "(...) observando que cada acesso deverá ser único e vinculado exclusivamente a um único CPF ou CNPJ:"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-009

## Suite 2 — Validação de credenciais (1.25 / 1.25.2)

> [!example]- CT-010 · Login recusado quando o CPF/CNPJ está correto mas a senha está incorreta
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
> **Descrição:** confirma a conformidade com o item 1.25 / 1.25.2 do Termo de Referência.
>
> **Dado** que o usuário está cadastrado e ativo  
> **Quando** ele informa um CPF/CNPJ válido e cadastrado, mas uma senha incorreta, e tenta autenticar **[SS-02]**  
> **Então** o acesso é negado e é exibida uma mensagem de erro clara e genérica, sem indicar se o erro está no identificador ou na senha — mensagem diferente da usada quando o identificador não existe, quando a conta está bloqueada, ou quando está inativa (ver CT-011, CT-015, CT-032)
>
> **Pós-condição:** nenhuma sessão aberta; a tentativa é contabilizada para efeito de bloqueio (ver Suite 3)
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]] · [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25 / 1.25.2  
> **Citação do Termo:** 1.25. O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão; 1.25.2. O sistema deverá exibir uma mensagem de erro clara quando as credenciais não forem reconhecidas;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-010

> [!example]- CT-011 · Login recusado quando o CPF/CNPJ informado não existe na base
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
> **Descrição:** confirma a conformidade com o item 1.25 / 1.25.2 do Termo de Referência.
>
> **Dado** que o CPF/CNPJ que será usado não possui cadastro em nenhum tipo de usuário  
> **Quando** alguém informa esse CPF/CNPJ inexistente com qualquer senha  
> **E** tenta autenticar  
> **Então** é exibida uma mensagem de erro clara informando que as credenciais não foram reconhecidas, sem revelar se o CPF/CNPJ existe ou não na base (evitando enumeração de usuários) — mensagem diferente da usada pra senha incorreta, conta bloqueada, ou conta inativa (ver CT-010, CT-015, CT-032)
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]] · [[01 - Demanda#^c8|C8]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25 / 1.25.2  
> **Citação do Termo:** 1.25. O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão; 1.25.2. O sistema deverá exibir uma mensagem de erro clara quando as credenciais não forem reconhecidas;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-011

> [!example]- CT-012 · Login bloqueado no envio quando CPF/CNPJ e/ou senha estão em branco
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
> **Descrição:** confirma a conformidade com o item 1.25 do Termo de Referência.
>
> **Dado** que a tela de login está aberta  
> **Quando** o usuário deixa o campo de CPF/CNPJ e/ou o de senha em branco  
> **E** tenta autenticar  
> **Então** o sistema impede o envio e exibe uma mensagem orientando o preenchimento dos campos obrigatórios
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25  
> **Citação do Termo:** [Regra de obrigatoriedade de campos não é explícita no documento] 1.25. "O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-012

## Suite 3 — Bloqueio por tentativas (1.25.1)

> [!example]- CT-013 · Conta é bloqueada exatamente na 5ª tentativa consecutiva de login malsucedida
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
> **Descrição:** confirma a conformidade com o item 1.25.1 do Termo de Referência.
>
> **Dado** que o usuário está cadastrado e ativo, sem tentativas malsucedidas recentes  
> **Quando** são feitas 5 tentativas consecutivas de login com senha incorreta para o mesmo usuário **[SS-03, N=5]**  
> **Então** a conta é bloqueada a partir da 5ª tentativa, e o sistema exibe uma mensagem informando o bloqueio
>
> **Pós-condição:** conta permanece bloqueada até um desbloqueio (ver CT-016/CT-017)
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.1  
> **Citação do Termo:** 1.25.1. Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-013

> [!example]- CT-014 · Conta não é bloqueada antes de completar 5 tentativas malsucedidas
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
> **Descrição:** confirma a conformidade com o item 1.25.1 do Termo de Referência.
>
> **Dado** que o usuário está cadastrado e ativo, sem tentativas malsucedidas recentes  
> **Quando** são feitas 4 tentativas de login com senha incorreta **[SS-03, N=4]**  
> **E** na 5ª tentativa é informada a senha correta  
> **Então** o login é bem-sucedido nessa 5ª tentativa, pois o bloqueio só ocorre ao completar 5 tentativas incorretas seguidas
>
> **Pós-condição:** sessão autenticada normalmente; contador de tentativas malsucedidas zerado
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.1  
> **Citação do Termo:** 1.25.1. Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-014

> [!example]- CT-015 · Conta bloqueada continua inacessível mesmo com a senha correta
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
> **Descrição:** confirma a conformidade com o item 1.25.1 do Termo de Referência.
>
> **Dado** que a conta já está bloqueada por 5 tentativas malsucedidas anteriores  
> **Quando** o usuário tenta autenticar informando a senha correta  
> **Então** o acesso permanece negado, e o sistema exibe uma mensagem informando que a conta está bloqueada — mensagem diferente das usadas pra credenciais inválidas ou conta inativa (ver CT-010, CT-011, CT-032)
>
> **Pós-condição:** conta permanece bloqueada; nenhuma sessão aberta
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.1  
> **Citação do Termo:** 1.25.1. Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** reprovado — achado real de produto, ver [[04 - Validação dev]]

^ct-015

> [!example]- CT-016 · Usuário se desbloqueia sozinho por link recebido em e-mail
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
> **Descrição:** confirma a conformidade com o item 1.25.1 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-17) do Termo de Referência.
>
> **Dado** que a conta está bloqueada (mesma pré-condição do CT-015)  
> **Quando** o usuário solicita o desbloqueio e recebe um link por e-mail, e utiliza esse link  
> **Então** a conta é desbloqueada e o usuário consegue autenticar normalmente em seguida
>
> **Pós-condição:** conta volta ao estado desbloqueado; contador de tentativas malsucedidas zerado
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.1 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-17)  
> **Citação do Termo:** [Não há regra explícita sobre o mecanismo de desbloqueio] 1.25.1. "Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** não automatizado  
> **Execução:** sem código — aguarda captura de API

^ct-016

> [!example]- CT-017 · Um servidor desbloqueia manualmente a conta pela tela do servidor
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
> **Descrição:** confirma a conformidade com o item 1.25.1 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-17) do Termo de Referência.
>
> **Dado** que a conta está bloqueada (mesma pré-condição do CT-015) e existe um servidor com permissão de desbloqueio  
> **Quando** esse servidor acessa a tela do servidor e realiza o desbloqueio manual da conta  
> **Então** a conta é desbloqueada e o usuário consegue autenticar normalmente em seguida
>
> **Pós-condição:** conta volta ao estado desbloqueado; contador de tentativas malsucedidas zerado
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.1 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-17)  
> **Citação do Termo:** [Não há regra explícita sobre o mecanismo de desbloqueio] 1.25.1. "Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** não automatizado  
> **Execução:** sem código — aguarda captura de API

^ct-017

> [!example]- CT-018 · O contador de tentativas malsucedidas reinicia depois de um login bem-sucedido
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
> **Descrição:** confirma a conformidade com o item 1.25.1 (comportamento inferido) do Termo de Referência.
>
> **Dado** que o usuário está cadastrado e ativo  
> **Quando** são feitas 3 tentativas malsucedidas **[SS-03, N=3]** — ainda sem bloqueio, faltam 2 para o limite —, depois um login bem-sucedido, e em seguida mais 3 tentativas malsucedidas **[SS-03, N=3]**  
> **Então** a conta não bloqueia nessa segunda sequência de 3 tentativas, evidenciando que o contador reiniciou após o login bem-sucedido
>
> **Pós-condição:** contador de tentativas malsucedidas em 3 (não bloqueado)
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.1 (comportamento inferido)  
> **Citação do Termo:** [Comportamento inferido, não literal no documento] 1.25.1. "Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-018

> [!example]- CT-019 · O bloqueio de um usuário não afeta o acesso de outros usuários
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
> **Descrição:** confirma a conformidade com o item 1.25.1 (comportamento inferido) do Termo de Referência.
>
> **Dado** que existem dois usuários distintos, ambos cadastrados e ativos  
> **Quando** o Usuário A é bloqueado após 5 tentativas malsucedidas **[SS-03, N=5]**  
> **E** o Usuário B tenta autenticar com suas próprias credenciais corretas  
> **Então** o Usuário A permanece bloqueado e o Usuário B consegue autenticar normalmente — o bloqueio fica restrito à conta do Usuário A
>
> **Pós-condição:** Usuário A bloqueado; Usuário B com sessão autenticada normalmente
>
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.1 (comportamento inferido)  
> **Citação do Termo:** [Comportamento inferido, não literal no documento] 1.25.1. "Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-019

## Suite 4 — Ciclo de vida da identidade (1.25.3)

> [!example]- CT-020 · Servidor "Ativo" tem acesso irrestrito conforme o seu nível de permissão
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
> **Descrição:** confirma a conformidade com o item 1.25.3.1 do Termo de Referência.
>
> **Dado** que o servidor está cadastrado com status "Ativo", em qualquer nível (Administrador, Administrador Setorial, Especialista, Usuário básico ou Somente leitura)  
> **Quando** ele autentica na tela do servidor **[SS-01a]** e percorre as funcionalidades disponíveis para o seu nível  
> **Então** todas as funcionalidades e permissões previstas para o seu perfil estão disponíveis, sem nenhuma restrição adicional ligada ao status funcional
>
> **Pós-condição:** sessão autenticada com permissões plenas do perfil; sem outra alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.1  
> **Citação do Termo:** 1.25.3.1. Estado Operacional Padrão (Ativo): O sistema deverá aplicar o conjunto completo de permissões e privilégios (entitlements) associados aos papéis do usuário cujo atributo de status funcional esteja definido como "Ativo", garantindo acesso irrestrito ao ambiente de trabalho conforme seu perfil de autorização;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-020

> [!example]- CT-021 · Servidor em "Licença" consegue fazer login, mas com acesso restrito
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
> **Descrição:** confirma a conformidade com o item 1.25.3.2 do Termo de Referência.
>
> **Dado** que o servidor está com status "Licença" vigente  
> **Quando** ele tenta autenticar normalmente com CPF e senha **[SS-04a, status=Licença]**  
> **Então** o login é permitido (diferente do que ocorre com "Inativo"), mas o acesso fica restrito a um subconjunto de funcionalidades não transacionais
>
> **Pós-condição:** sessão autenticada em modo restrito (quarentena de privilégios)
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.2  
> **Citação do Termo:** 1.25.3.2. Estado de Afastamento Legal (Licença): Para um usuário em estado de "Licença", o sistema deverá acionar uma política de quarentena de privilégios, apresentando um aviso de status e restringindo dinamicamente o acesso a um subconjunto mínimo de funcionalidades não transacionais, suspendendo temporariamente direitos de modificação e aprovação;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-021

> [!example]- CT-022 · Servidor em "Licença" recebe um aviso de status ao entrar no sistema
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
> **Descrição:** confirma a conformidade com o item 1.25.3.2 do Termo de Referência.
>
> **Dado** que o servidor com status "Licença" vigente já concluiu o login  
> **Quando** ele observa a tela inicial/mesa de trabalho **[SS-04b, status=Licença]**  
> **Então** o sistema exibe um aviso/notificação informando que o usuário está em licença
>
> **Pós-condição:** sem alteração de estado além da sessão autenticada em modo restrito
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.3.2  
> **Citação do Termo:** 1.25.3.2. (...) apresentando um aviso de status e restringindo dinamicamente o acesso a um subconjunto mínimo de funcionalidades não transacionais, suspendendo temporariamente direitos de modificação e aprovação;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** falha sem causa raiz identificada, ver [[04 - Validação dev]]

^ct-022

> [!example]- CT-023 · Servidor em "Licença" não pode modificar nem aprovar nada
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
> **Descrição:** confirma a conformidade com o item 1.25.3.2 do Termo de Referência.
>
> **Dado** que o servidor com status "Licença" está autenticado no sistema  
> **Quando** ele tenta editar um documento, aprovar/assinar uma tramitação, ou avançar uma etapa de fluxo de trabalho **[SS-04c, status=Licença]**  
> **Então** todas essas ações de modificação e aprovação ficam bloqueadas/indisponíveis
>
> **Pós-condição:** nenhuma alteração de estado é produzida pelas tentativas bloqueadas
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.2  
> **Citação do Termo:** 1.25.3.2. (...) suspendendo temporariamente direitos de modificação e aprovação;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-023

> [!example]- CT-024 · Servidor em "Licença" não tem acesso a nenhuma funcionalidade, nem de leitura/consulta
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
> **Descrição:** confirma a conformidade com o item 1.25.3.2 do Termo de Referência.
>
> **Dado** que o servidor com status "Licença" está autenticado no sistema  
> **Quando** ele tenta consultar/visualizar documentos e processos aos quais teria acesso caso estivesse "Ativo" **[SS-04d, status=Licença]**  
> **Então** nenhuma dessas funcionalidades de consulta/visualização fica acessível — o acesso é limitado, sem visibilidade de conteúdo
>
> **Pós-condição:** sem alteração de estado além da sessão autenticada em modo restrito
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.3.2  
> **Citação do Termo:** 1.25.3.2. (...) restringindo dinamicamente o acesso a um subconjunto mínimo de funcionalidades não transacionais (...)  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-024

> [!example]- CT-025 · Mudança de status para "Licença" durante uma sessão ativa é aplicada imediatamente
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
> **Descrição:** confirma a conformidade com o item 1.25.3.2 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-25) do Termo de Referência.
>
> **Dado** que o servidor está logado no sistema (sessão ativa) com status "Ativo"  
> **Quando** um Administrador altera o status dele para "Licença", com início imediato, enquanto a sessão segue aberta  
> **Então** as restrições de "Licença" passam a valer imediatamente na sessão em curso — não é preciso um novo login para a quarentena de privilégios entrar em vigor
>
> **Pós-condição:** sessão em curso passa a operar em modo restrito a partir do momento da alteração
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.2 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-25)  
> **Citação do Termo:** [Comportamento em sessão ativa não detalhado no documento] 1.25.3.2. "(...) o sistema deverá acionar uma política de quarentena de privilégios, apresentando um aviso de status e restringindo dinamicamente o acesso a um subconjunto mínimo de funcionalidades não transacionais, suspendendo temporariamente direitos de modificação e aprovação;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-025

> [!example]- CT-026 · Permissões do servidor são restabelecidas automaticamente ao fim da "Licença"
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
> **Descrição:** confirma a conformidade com o item 1.25.3.2 / 1.27.11.4 do Termo de Referência.
>
> **Dado** que o servidor tem um período de "Licença" configurado com data de término definida  
> **Quando** essa data de término chega (ou é simulada) e ele autentica novamente **[SS-05, status=Licença]**  
> **Então** o sistema restabelece automaticamente as permissões plenas do servidor, que retorna ao status "Ativo"
>
> **Pós-condição:** servidor retorna a status "Ativo", com permissões plenas restauradas
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]] · [[01 - Demanda#^c16|C16]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.2 / 1.27.11.4  
> **Citação do Termo:** 1.27.11.4. A partir da definição do período do novo status de atividade do servidor, esse deve receber um email informando da alteração realizada e no período definido as alterações do seu ambiente de trabalho devem ser aplicadas, de modo que, num cenário onde é definido que um usuário entrará em férias na próxima segunda e permanecerá por 30 dias, na segunda o usuário tenha o seu acesso à plataforma limitado, informando que ele está de férias e, ao término do período, o sistema restabeleça as funções para que o servidor retorne às suas atividades.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** falha sem causa raiz identificada, ver [[04 - Validação dev]]

^ct-026

> [!example]- CT-027 · Servidor em "Férias" consegue fazer login, mas com acesso restrito
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
> **Descrição:** confirma a conformidade com o item 1.25.3.3 do Termo de Referência.
>
> **Dado** que o servidor está com status "Férias" vigente  
> **Quando** ele tenta autenticar normalmente com CPF e senha **[SS-04a, status=Férias]**  
> **Então** o login é permitido, com o acesso restrito pela mesma política de quarentena de privilégios aplicada à "Licença"
>
> **Pós-condição:** sessão autenticada em modo restrito (quarentena de privilégios)
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.3  
> **Citação do Termo:** 1.25.3.3. Estado de Afastamento Legal (Férias): De forma análoga ao estado de licença, um usuário cujo status seja "Férias" deverá ter seu acesso modulado pela mesma política de quarentena de privilégios, com a exibição de notificação e a suspensão de permissões de escrita e execução de fluxos de trabalho;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-027

> [!example]- CT-028 · Servidor em "Férias" recebe uma notificação de status ao entrar no sistema
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
> **Descrição:** confirma a conformidade com o item 1.25.3.3 do Termo de Referência.
>
> **Dado** que o servidor com status "Férias" vigente já concluiu o login  
> **Quando** ele observa a tela inicial/mesa de trabalho **[SS-04b, status=Férias]**  
> **Então** o sistema exibe uma notificação informando que o usuário está em período de férias
>
> **Pós-condição:** sem alteração de estado além da sessão autenticada em modo restrito
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.3.3  
> **Citação do Termo:** 1.25.3.3. (...) com a exibição de notificação e a suspensão de permissões de escrita e execução de fluxos de trabalho;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** falha sem causa raiz identificada, ver [[04 - Validação dev]]

^ct-028

> [!example]- CT-029 · Servidor em "Férias" tem as permissões de escrita e de fluxo de trabalho suspensas
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
> **Descrição:** confirma a conformidade com o item 1.25.3.3 do Termo de Referência.
>
> **Dado** que o servidor com status "Férias" está autenticado no sistema  
> **Quando** ele tenta editar/criar um documento, ou executar/avançar uma etapa de fluxo de trabalho **[SS-04c, status=Férias]**  
> **Então** essas ações de escrita e execução de fluxo ficam bloqueadas/indisponíveis
>
> **Pós-condição:** nenhuma alteração de estado é produzida pelas tentativas bloqueadas
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.3  
> **Citação do Termo:** 1.25.3.3. (...) e a suspensão de permissões de escrita e execução de fluxos de trabalho;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** reprovado — achado real de produto, ver [[04 - Validação dev]]

^ct-029

> [!example]- CT-030 · Servidor em "Férias" não tem acesso a nenhuma funcionalidade, nem de leitura/consulta
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
> **Descrição:** confirma a conformidade com o item 1.25.3.3 do Termo de Referência.
>
> **Dado** que o servidor com status "Férias" está autenticado no sistema  
> **Quando** ele tenta consultar/visualizar documentos e processos aos quais teria acesso caso estivesse "Ativo" **[SS-04d, status=Férias]**  
> **Então** nenhuma dessas funcionalidades de consulta/visualização fica acessível — o acesso é limitado, sem visibilidade de conteúdo
>
> **Pós-condição:** sem alteração de estado além da sessão autenticada em modo restrito
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.3.3  
> **Citação do Termo:** [Comportamento inferido por analogia ao estado de Licença, não literal no documento] 1.25.3.3. "(...) deverá ter seu acesso modulado pela mesma política de quarentena de privilégios (...)"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** reprovado — achado real de produto, ver [[04 - Validação dev]]

^ct-030

> [!example]- CT-031 · Permissões do servidor são restabelecidas automaticamente ao fim das "Férias"
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
> **Descrição:** confirma a conformidade com o item 1.25.3.3 / 1.27.11.4 do Termo de Referência.
>
> **Dado** que o servidor tem um período de "Férias" configurado com data de término definida  
> **Quando** essa data de término chega (ou é simulada) e ele autentica novamente **[SS-05, status=Férias]**  
> **Então** o sistema restabelece automaticamente as permissões plenas do servidor, que retorna ao status "Ativo"
>
> **Pós-condição:** servidor retorna a status "Ativo", com permissões plenas restauradas
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]] · [[01 - Demanda#^c16|C16]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.3 / 1.27.11.4  
> **Citação do Termo:** 1.27.11.4. (...) e, ao término do período, o sistema restabeleça as funções para que o servidor retorne às suas atividades.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-031

> [!example]- CT-032 · Servidor "Inativo" nunca consegue autenticar, mesmo com credenciais corretas
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
> **Descrição:** confirma a conformidade com o item 1.25.3.4 do Termo de Referência.
>
> **Dado** que o servidor está cadastrado com status "Inativo" (vínculo encerrado)  
> **Quando** ele tenta autenticar com CPF e senha corretos  
> **Então** o acesso é negado de forma explícita (explicit deny), mesmo com credenciais corretas, e o sistema exibe uma mensagem de conta inativa — mensagem diferente das usadas pra credenciais inválidas ou conta bloqueada (ver CT-010, CT-011, CT-015)
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.4  
> **Citação do Termo:** 1.25.3.4. Estado de Desprovisionamento Lógico (Inativo): Quando o vínculo do agente for encerrado (status "Inativo"), a plataforma deverá aplicar uma regra de negação explícita (explicit deny) a qualquer tentativa de autenticação, impossibilitando o acesso e exibindo uma mensagem de conta inativa.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-032

> [!example]- CT-033 · Mudança de status para "Inativo" durante uma sessão ativa é aplicada imediatamente
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
> **Descrição:** confirma a conformidade com o item 1.25.3.4 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-34) do Termo de Referência.
>
> **Dado** que o servidor está logado no sistema (sessão ativa) com status "Ativo"  
> **Quando** um Administrador altera o status dele para "Inativo" enquanto a sessão segue aberta  
> **Então** o acesso é revogado imediatamente na sessão em curso — a sessão não continua válida até um novo login
>
> **Pós-condição:** sessão em curso encerrada/revogada a partir do momento da alteração
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3.4 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-34)  
> **Citação do Termo:** [Comportamento em sessão ativa não detalhado no documento] 1.25.3.4. "(...) a plataforma deverá aplicar uma regra de negação explícita (explicit deny) a qualquer tentativa de autenticação, impossibilitando o acesso (...)"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** reprovado — achado real de produto, ver [[04 - Validação dev]]

^ct-033

> [!example]- CT-034 · Reativar um servidor "Inativo" restabelece o acesso normalmente
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
> **Descrição:** confirma a conformidade com o item 1.25.3.4 (inferido por reversão do status) do Termo de Referência.
>
> **Dado** que o servidor estava inativo e foi reativado por um Administrador (status volta para "Ativo")  
> **Quando** ele tenta autenticar novamente  
> **Então** o login é bem-sucedido, com as permissões plenas do seu perfil totalmente restauradas
>
> **Pós-condição:** servidor retorna a status "Ativo", com permissões plenas restauradas
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.25.3.4 (inferido por reversão do status)  
> **Citação do Termo:** [Comportamento inferido por reversão do status, não literal no documento] 1.25.3.1. "(...) O sistema deverá aplicar o conjunto completo de permissões e privilégios (entitlements) (...) garantindo acesso irrestrito ao ambiente de trabalho conforme seu perfil de autorização;"  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** falha sem causa raiz identificada, ver [[04 - Validação dev]]

^ct-034

> [!example]- CT-035 · Status "Suspenso" se comporta exatamente como "Inativo": negação total de acesso
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
> **Descrição:** confirma a conformidade com o item 1.25.3 / 1.27.10 / 1.27.11.2 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-39; ausência no item 1.25.3 era ambiguidade de redação) do Termo de Referência.
>
> **Dado** que o servidor está cadastrado com status "Suspenso"  
> **Quando** ele tenta autenticar com CPF e senha corretos  
> **Então** o acesso é negado de forma explícita (explicit deny), do mesmo jeito que o status "Inativo" — nenhum acesso é concedido
>
> **Pós-condição:** nenhuma sessão aberta; nenhuma alteração de estado
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]] · [[01 - Demanda#^c14|C14]] · [[01 - Demanda#^c15|C15]] · [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3 / 1.27.10 / 1.27.11.2 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-39; ausência no item 1.25.3 era ambiguidade de redação)  
> **Citação do Termo:** [Ausente no item 1.25.3] 1.27.10.1.e.iii. Suspenso - que deve representar servidores que tiverem seus acessos à plataforma suspensos; 1.27.11.2. (...) devendo existir, no mínimo, os seguintes status e possibilidades: a) Em atividade; b) Suspenso; c) Licença; d) Férias.  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** falha sem causa raiz identificada, ver [[04 - Validação dev]]

^ct-035

> [!example]- CT-036 · O comportamento de acesso acompanha corretamente cada mudança de status, em sequência
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
> **Descrição:** confirma a conformidade com o item 1.25.3 do Termo de Referência.
>
> **Dado** que o servidor está cadastrado e um Administrador pode alterar seu status livremente  
> **Quando** o status é alternado na sequência Ativo → Férias → Ativo → Licença → Inativo, e após cada mudança é feita uma tentativa de autenticar/agir  
> **Então** em cada etapa o comportamento de acesso (permitido, restrito ou negado) corresponde exatamente ao status vigente naquele momento
>
> **Pós-condição:** servidor termina a sequência com status "Inativo" e sem acesso
>
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Alta  
> **Item do Termo:** 1.25.3  
> **Citação do Termo:** 1.25.3. Controle de acesso dinâmico baseado no ciclo de vida da identidade funcional:  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** falha sem causa raiz identificada, ver [[04 - Validação dev]]

^ct-036

## Suite 5 — Transversais e auditoria

> [!example]- CT-037 · Tentativas de login, com sucesso ou falha, ficam registradas para auditoria
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
> **Descrição:** confirma a conformidade com o item 1.13 / 1.25 do Termo de Referência.
>
> **Dado** que existe acesso a um relatório/log de auditoria de acessos (perfil Administrador)  
> **Quando** são feitas tentativas de login com sucesso e com falha para o mesmo usuário  
> **E** o log/relatório de auditoria é consultado  
> **Então** todas as tentativas (sucesso e falha) aparecem registradas com data, hora e resultado, permitindo rastreabilidade
>
> **Pós-condição:** log de auditoria com as novas entradas registradas permanentemente
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]] · [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Média  
> **Item do Termo:** 1.13 / 1.25  
> **Citação do Termo:** 1.13. O sistema deverá garantir a auditoria de acessos e alterações às credenciais;  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** não automatizado  
> **Execução:** sem código — aguarda captura de API

^ct-037

> [!example]- CT-038 · O sistema permite múltiplas sessões simultâneas do mesmo usuário em dispositivos diferentes
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
> **Descrição:** confirma a conformidade com o item 1.24 / 1.25 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-38; o Termo não proíbe isso explicitamente) do Termo de Referência.
>
> **Dado** que o usuário está cadastrado e ativo  
> **Quando** ele autentica em dois dispositivos/navegadores distintos, simultaneamente, com as mesmas credenciais  
> **Então** ambas as sessões permanecem ativas e funcionais, permitindo requisições normalmente em qualquer uma delas, sem que uma sessão encerre a outra
>
> **Pós-condição:** duas sessões ativas simultâneas para o mesmo usuário
>
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]] · [[01 - Demanda#^c6|C6]]
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** Baixa  
> **Item do Termo:** 1.24 / 1.25 (confirmado com o Rafael em 18/08 — resolve o antigo Gap TC-38; o Termo não proíbe isso explicitamente)  
> **Citação do Termo:** [Não há regra explícita no documento sobre sessões simultâneas]  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** automatizado em Cypress — a portar pra Playwright  
> **Execução:** confirmado contra HML pela suíte automatizada (31/08/2026)

^ct-038

## Extra — fora do escopo do Termo de Referência

> [!example]- CT-E01 · [Extra] Servidor em "Licença" — acesso no contexto de cidadão
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
> **Descrição:** cenário extra, fora do escopo do Termo de Referência — mantido por valor de cobertura, sem execução prevista.
>
> **Dado** que o servidor está com status "Licença" e, por ser servidor, também é cidadão pelo mesmo CPF  
> **Quando** ele acessa a tela de login do cidadão com esse CPF **[SS-06, status=Licença]**  
> **Então** *[A DEFINIR — fora do escopo do Termo de Referência; candidato a validação e2e]*
>
> **Pós-condição:** *[A DEFINIR]*
>
> **Critérios cobertos:** — (fora do Termo)
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** —  
> **Item do Termo:** — (fora do Termo)  
> **Citação do Termo:** —  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** não automatizado  
> **Execução:** não executado — fora do escopo do Termo

^ct-e01

> [!example]- CT-E02 · [Extra] Servidor em "Férias" — acesso no contexto de cidadão
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
> **Descrição:** cenário extra, fora do escopo do Termo de Referência — mantido por valor de cobertura, sem execução prevista.
>
> **Dado** que o servidor está com status "Férias" e, por ser servidor, também é cidadão pelo mesmo CPF  
> **Quando** ele acessa a tela de login do cidadão com esse CPF **[SS-06, status=Férias]**  
> **Então** *[A DEFINIR — fora do escopo do Termo de Referência; candidato a validação e2e]*
>
> **Pós-condição:** *[A DEFINIR]*
>
> **Critérios cobertos:** — (fora do Termo)
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** —  
> **Item do Termo:** — (fora do Termo)  
> **Citação do Termo:** —  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** não automatizado  
> **Execução:** não executado — fora do escopo do Termo

^ct-e02

> [!example]- CT-E03 · [Extra] Servidor "Inativo" — acesso no contexto de cidadão
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
> **Descrição:** cenário extra, fora do escopo do Termo de Referência — mantido por valor de cobertura, sem execução prevista.
>
> **Dado** que o servidor está com status "Inativo" e, por ser servidor, também é cidadão pelo mesmo CPF  
> **Quando** ele acessa a tela de login do cidadão com esse CPF **[SS-06, status=Inativo]**  
> **Então** *[A DEFINIR — fora do escopo do Termo de Referência; candidato a validação e2e]*
>
> **Pós-condição:** *[A DEFINIR]*
>
> **Critérios cobertos:** — (fora do Termo)
>
> ---
>
> **Informações do CT**
>
> **Prioridade:** —  
> **Item do Termo:** — (fora do Termo)  
> **Citação do Termo:** —  
> **Tipo:** funcional  
> **Camada:** API  
> **Automação:** não automatizado  
> **Execução:** não executado — fora do escopo do Termo

^ct-e03

---

## Matriz de cobertura

Use esta matriz para verificar a cobertura sem abrir a demanda. Atualize-a ao criar ou alterar CTs.

| Critério | Item do Termo | CTs |
|---|---|---|
| [[01 - Demanda#^c1\|C1]] | 1.13 | [[03 - Casos de teste#^ct-037\|CT-037]] |
| [[01 - Demanda#^c2\|C2]] | 1.24 | [[03 - Casos de teste#^ct-006\|CT-006]] · [[03 - Casos de teste#^ct-007\|CT-007]] · [[03 - Casos de teste#^ct-008\|CT-008]] · [[03 - Casos de teste#^ct-009\|CT-009]] · [[03 - Casos de teste#^ct-038\|CT-038]] |
| [[01 - Demanda#^c3\|C3]] | 1.24.1 | [[03 - Casos de teste#^ct-001\|CT-001]] · [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c4\|C4]] | 1.24.2 | [[03 - Casos de teste#^ct-002\|CT-002]] · [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c5\|C5]] | 1.24.3 | [[03 - Casos de teste#^ct-003\|CT-003]] · [[03 - Casos de teste#^ct-004\|CT-004]] · [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | 1.25 | [[03 - Casos de teste#^ct-006\|CT-006]] · [[03 - Casos de teste#^ct-007\|CT-007]] · [[03 - Casos de teste#^ct-010\|CT-010]] · [[03 - Casos de teste#^ct-011\|CT-011]] · [[03 - Casos de teste#^ct-012\|CT-012]] · [[03 - Casos de teste#^ct-037\|CT-037]] · [[03 - Casos de teste#^ct-038\|CT-038]] |
| [[01 - Demanda#^c7\|C7]] | 1.25.1 | [[03 - Casos de teste#^ct-013\|CT-013]] · [[03 - Casos de teste#^ct-014\|CT-014]] · [[03 - Casos de teste#^ct-015\|CT-015]] · [[03 - Casos de teste#^ct-016\|CT-016]] · [[03 - Casos de teste#^ct-017\|CT-017]] · [[03 - Casos de teste#^ct-018\|CT-018]] · [[03 - Casos de teste#^ct-019\|CT-019]] |
| [[01 - Demanda#^c8\|C8]] | 1.25.2 | [[03 - Casos de teste#^ct-010\|CT-010]] · [[03 - Casos de teste#^ct-011\|CT-011]] |
| [[01 - Demanda#^c9\|C9]] | 1.25.3 | [[03 - Casos de teste#^ct-035\|CT-035]] · [[03 - Casos de teste#^ct-036\|CT-036]] |
| [[01 - Demanda#^c10\|C10]] | 1.25.3.1 | [[03 - Casos de teste#^ct-020\|CT-020]] |
| [[01 - Demanda#^c11\|C11]] | 1.25.3.2 | [[03 - Casos de teste#^ct-021\|CT-021]] · [[03 - Casos de teste#^ct-022\|CT-022]] · [[03 - Casos de teste#^ct-023\|CT-023]] · [[03 - Casos de teste#^ct-024\|CT-024]] · [[03 - Casos de teste#^ct-025\|CT-025]] · [[03 - Casos de teste#^ct-026\|CT-026]] |
| [[01 - Demanda#^c12\|C12]] | 1.25.3.3 | [[03 - Casos de teste#^ct-027\|CT-027]] · [[03 - Casos de teste#^ct-028\|CT-028]] · [[03 - Casos de teste#^ct-029\|CT-029]] · [[03 - Casos de teste#^ct-030\|CT-030]] · [[03 - Casos de teste#^ct-031\|CT-031]] |
| [[01 - Demanda#^c13\|C13]] | 1.25.3.4 | [[03 - Casos de teste#^ct-032\|CT-032]] · [[03 - Casos de teste#^ct-033\|CT-033]] · [[03 - Casos de teste#^ct-034\|CT-034]] |
| [[01 - Demanda#^c14\|C14]] | 1.27.10 | [[03 - Casos de teste#^ct-035\|CT-035]] |
| [[01 - Demanda#^c15\|C15]] | 1.27.11.2 | [[03 - Casos de teste#^ct-035\|CT-035]] |
| [[01 - Demanda#^c16\|C16]] | 1.27.11.4 | [[03 - Casos de teste#^ct-026\|CT-026]] · [[03 - Casos de teste#^ct-031\|CT-031]] |

---

## Fora de execução — registro

*Casos considerados e deliberadamente não executados — ficam aqui pra não sumirem do histórico e pra não abrirem buraco na numeração dos ativos.*

| Caso original | Suite | Decisão | Motivo |
|---|---|---|---|
| CT-012 (versão 19/08, antiga) — Mensagens de erro diferentes por motivo | Validação de credenciais | **Absorvido** | Reexecutava 4 cenários já cobertos individualmente (CT-009/010/014/031 de agora). A checagem de que as mensagens são distintas virou uma cláusula no `Então` de cada um deles. |
| CT-033 (versão 19/08, antiga) — Mensagem de conta inativa distinta | Ciclo de vida da identidade | **Absorvido** | Mesmo problema do CT-012 acima, comparando 3 dos mesmos 4 cenários — redundante. |

