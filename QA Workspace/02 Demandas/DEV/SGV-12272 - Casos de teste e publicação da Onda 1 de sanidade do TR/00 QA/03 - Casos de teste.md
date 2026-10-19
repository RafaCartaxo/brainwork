---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — SGV-12272

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle dos casos de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Os critérios ficam em `01 - Demanda`; esta nota concentra os 20 cenários executáveis, um por cenário aprovado na Proposta da Onda 1 (SGV-12200). **Lotes 1 e 2 (CT-001 a CT-010) redigidos; CT-011 a CT-020 seguem pendentes.**

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-002\|CT-002]], [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-005\|CT-005]], [[03 - Casos de teste#^ct-006\|CT-006]], [[03 - Casos de teste#^ct-007\|CT-007]], [[03 - Casos de teste#^ct-008\|CT-008]], [[03 - Casos de teste#^ct-009\|CT-009]], [[03 - Casos de teste#^ct-010\|CT-010]] *(CT-011 a CT-020 pendentes — próximos lotes)* |

Atualize esta matriz a cada lote de CTs redigido.

---

> [!example]- CT-001 · Login de Servidor Público com CPF e senha válidos (ONDA1-01)
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
> **Origem:** ONDA1-01 da Proposta da Onda 1 (SGV-12200). **TR:** 1.24 (regra geral de login por tipo de usuário), 1.24.1 (Servidor Público), 1.25 (validação de credenciais).
>
> **Descrição:** confirma que um Servidor Público autentica-se informando CPF e senha, e que o sistema valida essas credenciais contra o cadastro existente.
>
> **Pré-condições:**
> - Existe um Servidor Público já cadastrado e ativo, com CPF e senha conhecidos.
>
> **Dado** que o Servidor Público está na tela de login
> **Quando** ele informa seu CPF e sua senha corretos e confirma
> **Então** o sistema autentica o Servidor e abre sua sessão no contexto de Servidor
>
> **Resultado esperado:** login bem-sucedido; sessão aberta no contexto de Servidor Público, não em outro contexto (Cidadão/Empresa).
>
> **Pós-condição:** sessão autenticada no contexto de Servidor; nenhuma outra alteração de estado persistente.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-001

> [!example]- CT-002 · Bloqueio de conta após 5 tentativas de login malsucedidas (ONDA1-02)
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
> **Origem:** ONDA1-02 da Proposta da Onda 1 (SGV-12200). **TR:** 1.25.1.
>
> **Descrição:** confirma que, após 5 tentativas de login malsucedidas, a conta do usuário é bloqueada.
>
> **Pré-condições:**
> - Existe uma conta cadastrada e ativa (Servidor, Cidadão ou Empresa), sem bloqueio nem tentativa malsucedida recente.
>
> **Dado** que o usuário está na tela de login com uma conta válida
> **Quando** ele informa a senha incorreta 5 vezes seguidas para essa conta
> **Então** a conta é bloqueada
>
> **Resultado esperado:** na 5ª tentativa malsucedida, a conta passa a bloqueada.
>
> **Pós-condição:** conta em estado bloqueado.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-002

> [!example]- CT-003 · Mudança de estado funcional da identidade aplica o nível de restrição correto (ONDA1-03)
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
> **Origem:** ONDA1-03 da Proposta da Onda 1 (SGV-12200). **TR:** 1.25.3–1.25.3.4 (estados Ativo, Licença, Férias, Inativo).
>
> **Descrição:** confirma que, ao mudar o estado funcional de um Servidor entre Ativo, Licença, Férias e Inativo, o sistema aplica o nível de restrição de permissões descrito pelo TR para cada estado.
>
> **Pré-condições:**
> - Existe um Servidor cadastrado com status "Ativo" e permissões completas.
>
> **Dado** que o Servidor está com status "Ativo" e acesso irrestrito conforme seu nível
> **Quando** o status funcional do Servidor é alterado para "Licença", depois para "Férias", e depois para o estado que o TR chama de "Inativo"
> **Então** o sistema restringe as permissões do Servidor conforme o nível descrito pelo TR em cada estado
>
> **Resultado esperado:** em "Licença" (1.25.3.2), o acesso é restringido a um subconjunto mínimo de funcionalidades não transacionais, com direitos de modificação e aprovação suspensos; em "Férias" (1.25.3.3), a mesma política de quarentena se aplica, com permissões de escrita e execução de fluxos de trabalho suspensas; no estado que o TR chama de "Inativo" (1.25.3.4), a plataforma aplica negação explícita a qualquer tentativa de autenticação.
>
> **Pós-condição:** permissões do Servidor refletem o status funcional vigente.
>
> > [!warning] Nomenclatura dupla não resolvida (herdada da Proposta, ONDA1-03)
> > O TR usa o rótulo "Inativo" (§1.25.3.4); o cadastro atual do produto usa o rótulo "Suspenso" (§1.27.11.2) para o status editável correspondente. A Proposta registra essa nomenclatura dupla sem resolvê-la — ao executar este CT, confirmar visualmente qual rótulo a tela de cadastro usa para aplicar o estado de negação total descrito em 1.25.3.4, e registrar aqui o que foi observado, sem presumir equivalência.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-003

> [!example]- CT-004 · Servidor consegue criar documento só pelo Setor habilitado como criador (ONDA1-04)
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
> **Origem:** ONDA1-04 da Proposta da Onda 1 (SGV-12200). **TR:** 1.26.5 (um Servidor pode estar vinculado a mais de um Setor), 1.26.11/1.26.11.1 (cada Setor pode ter permissão própria para criar documentos).
>
> **Descrição:** confirma que um Servidor vinculado a dois Setores consegue criar documento de um Serviço/Assunto pelo Setor que tem permissão de criação, e é barrado ao tentar pelo outro Setor, que não tem essa permissão.
>
> **Pré-condições:**
> - O Servidor está vinculado, por vínculo N:N, aos Setores A e B, dentro do mesmo Módulo.
> - O Setor A está marcado como "Setor criador" do Módulo para a categoria usada no teste.
> - O Setor B participa normalmente do recebimento/tramitação desse Módulo, mas não está marcado como "Setor criador".
> - O Serviço/Assunto usado mantém a lista herdada de "Setores que criam" sem retirar o Setor A.
>
> > [!warning] Origem da regra (não é texto literal do TR)
> > A relação "só pode ser marcado como criador o Setor que já participa do recebimento/tramitação" vem da documentação de produto (`Regras de Tramitação`/`Tramitação`), não do texto do TR — o TR só confirma que cada Setor pode ter permissão própria de criação (1.26.11.1). Não tratar essa relação como requisito do TR ao avaliar o resultado deste CT.
>
> **Dado** que o Servidor está vinculado aos Setores A (criador) e B (não-criador) do mesmo Módulo
> **Quando** ele tenta criar um documento desse Serviço/Assunto atuando pelo Setor A
> **E** em seguida tenta criar um documento do mesmo Serviço/Assunto atuando pelo Setor B
> **Então** a criação pelo Setor A é permitida, e a criação pelo Setor B é impedida
>
> **Resultado esperado:** documento criado com sucesso atuando por A; tentativa de criação por B é bloqueada.
>
> **Pós-condição:** nenhum documento criado pelo Setor B; documento do Setor A registrado normalmente.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-004

> [!example]- CT-005 · Assunto/Serviço criado sob um Módulo herda a categoria-base correta (ONDA1-05)
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
> **Origem:** ONDA1-05 da Proposta da Onda 1 (SGV-12200). **TR:** 1.28.1 (campos mínimos do serviço/assunto), 1.29.1 (3 categorias-base: Documento oficial, Comunicação oficial, Processo administrativo).
>
> **Descrição:** confirma que um Assunto/Serviço criado sob um Módulo herda corretamente a categoria-base (DO/CO/PA) desse Módulo.
>
> **Pré-condições:**
> - Existe um Módulo já cadastrado, com uma categoria-base definida (uma das 3: Documento oficial, Comunicação oficial ou Processo administrativo).
> - O Servidor tem permissão para criar Assunto/Serviço.
>
> **Dado** que existe um Módulo cadastrado com categoria-base definida
> **Quando** o Servidor com permissão cria um novo Assunto/Serviço vinculado a esse Módulo
> **Então** o Assunto/Serviço criado é registrado com a mesma categoria-base do Módulo
>
> **Resultado esperado:** o Assunto/Serviço criado é registrado com a mesma categoria-base do Módulo ao qual está vinculado.
>
> **Pós-condição:** Assunto/Serviço persistido com a categoria-base correta.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-005

> [!example]- CT-006 · Setor removido de um Assunto/Serviço deixa de receber documentos ali (ONDA1-06)
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
> **Origem:** ONDA1-06 da Proposta da Onda 1 (SGV-12200). **TR:** 1.29 (categorias de documentos respeitam regras de tramitação definidas por módulo, seguindo os mesmos padrões usados em Assuntos e Serviços).
>
> **Descrição:** confirma que um Setor removido da lista de "Setores que recebem e tramitam" de um Assunto/Serviço específico deixa de receber documentos desse Assunto/Serviço, sem deixar de receber dos outros Assuntos/Serviços do mesmo Módulo.
>
> **Pré-condições:**
> - Um Módulo tem três Setores (X, Y, Z) que recebem e tramitam seus documentos.
> - Existem pelo menos dois Assuntos/Serviços desse Módulo.
> - Num desses Assuntos/Serviços, o Setor Z (que não é criador) é removido da lista de "Setores que recebem e tramitam".
>
> > [!warning] Origem da regra (não é texto literal do TR)
> > A herança da lista de "Setores que recebem e tramitam" do Módulo para o Assunto/Serviço, e a possibilidade de remover um Setor não-criador só nesse Assunto/Serviço, vêm da documentação de produto (`Tramitação`/`Regras de Tramitação`) — o TR 1.29 só confirma que Assunto/Serviço segue os mesmos padrões de regras de tramitação do Módulo, sem detalhar herança ou remoção.
>
> **Dado** que o Setor Z foi removido de "Setores que recebem e tramitam" só no Assunto/Serviço A
> **Quando** um documento é criado nesse Assunto/Serviço A
> **E** outro documento é criado num Assunto/Serviço B do mesmo Módulo, onde o Setor Z não foi removido
> **Então** o Setor Z não aparece recebendo o documento do Assunto/Serviço A, mas aparece recebendo normalmente o documento do Assunto/Serviço B
>
> **Resultado esperado:** Setor Z ausente da tramitação do documento criado em A; Setor Z presente na tramitação do documento criado em B.
>
> **Pós-condição:** nenhuma alteração persistente além dos dois documentos criados para o teste.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-006

> [!example]- CT-007 · Consulta pública de Zona publicada e Categoria de uso associada (ONDA1-07)
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
> **Origem:** ONDA1-07 da Proposta da Onda 1 (SGV-12200). **TR:** 1.29.10.2 ("a ferramenta deve ser acessível tanto para servidores quanto para cidadãos e empresas"), 1.29.10.4.g ("quando publicado, cidadãos e empresas poderão consultar as zonas e categorias de uso diretamente na central").
>
> **Descrição:** confirma que um Cidadão/Empresa consegue consultar, na central de atendimento, uma Zona publicada e as Categorias de uso associadas a ela.
>
> **Pré-condições:**
> - Existe uma Zona publicada, com ao menos uma Categoria de uso associada.
>
> **Dado** que existe uma Zona publicada com Categorias de uso associadas
> **Quando** um Cidadão/Empresa acessa a central de atendimento e consulta essa Zona
> **Então** o Cidadão/Empresa consegue visualizar a Zona e as Categorias de uso associadas a ela
>
> **Resultado esperado:** Zona e Categorias de uso exibidas corretamente na consulta pública.
>
> **Pós-condição:** nenhuma alteração de estado — é uma consulta.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-007

> [!example]- CT-008 · Abertura de Processo urbanístico a partir de Zona e revisão de Anexo (ONDA1-08)
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
> **Origem:** ONDA1-08 da Proposta da Onda 1 (SGV-12200). **TR:** 1.29.10.4.g (abrir processo a partir das informações da Zona), 1.29.10.4.h ("ao visualizar uma zona, o usuário poderá... iniciar um processo urbanístico diretamente relacionado à zona selecionada"), 1.29.10.4.i–j (anexos revisados por servidores, com possibilidade de aprovação ou reprovação, destaque de áreas e comentários).
>
> **Descrição:** confirma que um Cidadão/Empresa consegue iniciar um Processo urbanístico a partir de uma Zona publicada, e que um Servidor com permissão revisa o Anexo desse processo.
>
> **Pré-condições:**
> - Existe uma Zona publicada.
> - O Processo urbanístico iniciado a partir dela tem ao menos um Anexo.
>
> **Dado** que existe uma Zona publicada
> **Quando** um Cidadão/Empresa inicia um Processo urbanístico a partir dela e anexa um arquivo
> **E** um Servidor com permissão acessa o Anexo para revisão
> **Então** o Servidor consegue aprovar ou reprovar o Anexo, podendo destacar áreas e inserir comentários
>
> **Resultado esperado:** Processo urbanístico criado a partir da Zona; Anexo disponível para revisão do Servidor, com aprovação/reprovação e anotações registradas.
>
> **Pós-condição:** Anexo com status de revisão (aprovado ou reprovado) registrado.
>
> > [!info] Limite conhecido
> > O estado de revisão do Anexo (revisado/aprovado/reprovado) não tem confirmação em código localizada na análise que sustenta esta Onda — registrar na execução exatamente os rótulos/estados observados na tela, sem presumir que correspondem aos termos do TR.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-008

> [!example]- CT-009 · Documento a partir de Modelo simples, com e sem herança de dados (ONDA1-09)
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
> **Origem:** ONDA1-09 da Proposta da Onda 1 (SGV-12200). **TR:** 1.31.1 (Modelos simples integrados ao campo de texto grande/editor de despachos), 1.31.1.1.b ("definição se o modelo terá ou não herança de dados"), 1.31.1.1.b.i (com herança: "o sistema preencherá esses espaços automaticamente com os dados que foram preenchidos no formulário inicial"), 1.31.1.1.b.ii (sem herança: "o conteúdo desse modelo é totalmente estático").
>
> **Descrição:** confirma que um documento criado a partir de um Modelo simples preenche automaticamente os campos vinculados quando o modelo tem herança de dados, e permanece estático quando não tem.
>
> **Pré-condições:**
> - Existem dois Modelos simples compatíveis com a mesma categoria/serviço/assunto: um configurado com herança de dados, outro sem.
> - Existe um formulário já preenchido cujos dados podem ser herdados.
>
> **Dado** que existem um Modelo simples com herança de dados e outro sem herança, ambos compatíveis com o formulário preenchido
> **Quando** o Servidor usa o Modelo com herança durante a tramitação
> **E** em seguida usa o Modelo sem herança
> **Então** o primeiro documento tem os campos vinculados preenchidos automaticamente com os dados do formulário; o segundo mantém o conteúdo estático do modelo, sem preenchimento automático
>
> **Resultado esperado:** herança sim → campos preenchidos automaticamente; herança não → conteúdo estático, sem preenchimento.
>
> **Pós-condição:** dois documentos gerados, cada um refletindo o comportamento do modelo usado.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-009

> [!example]- CT-010 · Tramitação por Fluxo com despacho customizado e assinatura obrigatória (ONDA1-10)
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
> **Origem:** ONDA1-10 da Proposta da Onda 1 (SGV-12200). **TR:** 1.30.1.d/e (despachos e assinaturas obrigatórias configuráveis por Etapa), 1.30.2.b ("o sistema deverá permitir a inserção de solicitações de assinatura obrigatória como parte do despacho, garantindo que a tramitação só avance para uma nova etapa após a assinatura").
>
> **Descrição:** confirma que uma Etapa de Fluxo configurada com despacho customizado e assinatura obrigatória bloqueia o avanço do documento até que ambos sejam concluídos.
>
> **Pré-condições:**
> - O módulo "Fluxo de trabalho" está contratado/habilitado para o Ambiente Cliente usado no teste (funcionalidade opcional/contratada, não padrão universal).
> - Existe um Fluxo com uma Etapa configurada com despacho customizado obrigatório e assinatura obrigatória.
> - Existe um Documento tramitando por esse Fluxo, parado nessa Etapa.
>
> **Dado** que o Documento está na Etapa com despacho customizado e assinatura obrigatórios, nenhum dos dois concluído
> **Quando** o Servidor tenta avançar a Etapa sem emitir o despacho nem concluir a assinatura
> **Então** o avanço é bloqueado
> **Quando** o Servidor emite o despacho customizado e a assinatura é concluída
> **Então** o avanço para a próxima Etapa passa a ser permitido
>
> **Resultado esperado:** avanço bloqueado enquanto despacho/assinatura estiverem pendentes; avanço liberado só depois dos dois concluídos.
>
> **Pós-condição:** Documento avançado para a próxima Etapa, com despacho e assinatura registrados na Etapa anterior.
>
> **Critérios cobertos:** [[01 - Demanda#^c1|C1]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-010
