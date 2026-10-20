---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: execucao
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

> Os critérios ficam em `01 - Demanda`; esta nota concentra os 20 cenários executáveis, um por cenário aprovado na Proposta da Onda 1 (SGV-12200). **Os 20 CTs (CT-001 a CT-020) estão redigidos, aguardando validação em `04 - Validação dev.md`.**

---

## Matriz de cobertura

| Critério | CT |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]] |
| [[01 - Demanda#^c2\|C2]] | [[03 - Casos de teste#^ct-002\|CT-002]] |
| [[01 - Demanda#^c3\|C3]] | [[03 - Casos de teste#^ct-003\|CT-003]] |
| [[01 - Demanda#^c4\|C4]] | [[03 - Casos de teste#^ct-004\|CT-004]] |
| [[01 - Demanda#^c5\|C5]] | [[03 - Casos de teste#^ct-005\|CT-005]] |
| [[01 - Demanda#^c6\|C6]] | [[03 - Casos de teste#^ct-006\|CT-006]] |
| [[01 - Demanda#^c7\|C7]] | [[03 - Casos de teste#^ct-007\|CT-007]] |
| [[01 - Demanda#^c8\|C8]] | [[03 - Casos de teste#^ct-008\|CT-008]] |
| [[01 - Demanda#^c9\|C9]] | [[03 - Casos de teste#^ct-009\|CT-009]] |
| [[01 - Demanda#^c10\|C10]] | [[03 - Casos de teste#^ct-010\|CT-010]] |
| [[01 - Demanda#^c11\|C11]] | [[03 - Casos de teste#^ct-011\|CT-011]] |
| [[01 - Demanda#^c12\|C12]] | [[03 - Casos de teste#^ct-012\|CT-012]] |
| [[01 - Demanda#^c13\|C13]] | [[03 - Casos de teste#^ct-013\|CT-013]] |
| [[01 - Demanda#^c14\|C14]] | [[03 - Casos de teste#^ct-014\|CT-014]] |
| [[01 - Demanda#^c15\|C15]] | [[03 - Casos de teste#^ct-015\|CT-015]] |
| [[01 - Demanda#^c16\|C16]] | [[03 - Casos de teste#^ct-016\|CT-016]] |
| [[01 - Demanda#^c17\|C17]] | [[03 - Casos de teste#^ct-017\|CT-017]] |
| [[01 - Demanda#^c18\|C18]] | [[03 - Casos de teste#^ct-018\|CT-018]] |
| [[01 - Demanda#^c19\|C19]] | [[03 - Casos de teste#^ct-019\|CT-019]] |
| [[01 - Demanda#^c20\|C20]] | [[03 - Casos de teste#^ct-020\|CT-020]] |

Matriz completa: 20 critérios (C1–C20), um por CT, cobertura 1:1. Critérios de processo (C21–C24) ficam em `01 - Demanda.md`. Próxima atualização ocorre na validação (`04 - Validação dev.md`).

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
> **Critérios cobertos:** [[01 - Demanda#^c2|C2]]
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
> **Critérios cobertos:** [[01 - Demanda#^c3|C3]]
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
> **Critérios cobertos:** [[01 - Demanda#^c4|C4]]
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
> **Critérios cobertos:** [[01 - Demanda#^c5|C5]]
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
> **Critérios cobertos:** [[01 - Demanda#^c6|C6]]
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
> **Critérios cobertos:** [[01 - Demanda#^c7|C7]]
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
> **Critérios cobertos:** [[01 - Demanda#^c8|C8]]
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
> **Critérios cobertos:** [[01 - Demanda#^c9|C9]]
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
> **Critérios cobertos:** [[01 - Demanda#^c10|C10]]
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

> [!example]- CT-011 · Mesa de trabalho: resumo de demandas e alternância entre setores (ONDA1-11)
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
> **Origem:** ONDA1-11 da Proposta da Onda 1 (SGV-12200). **TR:** 1.33.1 ("deverá permitir que os usuários alternem entre diferentes setores de forma ágil, visualizando e gerenciando documentos e processos pertencentes a cada setor"), 1.33.2/1.33.2.1 ("resumo de todas as demandas" na primeira tela, com as quantidades em: a) Em aberto, b) Em tramitação, c) Concluído, d) Assinaturas pendentes, e) Demandas prestes a vencer e/ou já vencidas).
>
> **Descrição:** confirma que, ao acessar a Mesa de trabalho, o Servidor vê o resumo de demandas descrito pelo TR e consegue alternar entre os setores aos quais está vinculado.
>
> **Pré-condições:**
> - O Servidor está vinculado a mais de um Setor.
> - Existem documentos do Servidor/Setor nas situações "Em aberto", "Em tramitação", "Concluído" e com assinatura pendente ou prazo vencendo/vencido.
>
> **Dado** que o Servidor acessa a Mesa de trabalho pela primeira tela
> **Quando** a tela é exibida
> **Então** o resumo mostra as quantidades de documentos em aberto, em tramitação, concluídos, com assinatura pendente e prestes a vencer/vencidos
> **Quando** o Servidor alterna para outro Setor ao qual está vinculado
> **Então** a Mesa passa a exibir os documentos e processos desse outro Setor
>
> **Resultado esperado:** resumo exibido conforme as 5 categorias do TR; alternância de setor reflete corretamente os documentos do setor selecionado.
>
> **Pós-condição:** setor ativo do Servidor alterado para o setor selecionado.
>
> > [!info] Limite conhecido
> > O estado da Mesa como entidade própria não tem prova técnica de enum confirmada no código (02 §5) — este CT verifica o comportamento observável na tela, não a modelagem interna.
>
> **Critérios cobertos:** [[01 - Demanda#^c11|C11]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-011

> [!example]- CT-012 · Etiqueta pessoal não aparece para outros, etiqueta compartilhada aparece (ONDA1-12)
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
> **Origem:** ONDA1-12 da Proposta da Onda 1 (SGV-12200). **TR:** 1.34.1.a ("Etiquetas pessoais: criadas exclusivamente para o uso individual do servidor... visíveis apenas na mesa pessoal dele"), 1.34.1.b ("Etiquetas compartilhadas: criadas e compartilhadas entre setores ou hierarquias de setores, permitindo que mais servidores acessem essas etiquetas").
>
> **Descrição:** confirma que uma Etiqueta pessoal fica visível só para quem a criou, e uma Etiqueta compartilhada fica visível para os Setores com quem foi compartilhada.
>
> **Pré-condições:**
> - O Servidor A cria uma Etiqueta pessoal e aplica a um Documento.
> - O Servidor A cria uma Etiqueta compartilhada (com o Setor do Servidor B) e aplica a outro Documento.
> - Nenhuma das duas etiquetas usadas no teste é a etiqueta padrão "Urgente" do sistema — são criadas especificamente para este CT.
>
> **Dado** que o Servidor A criou e aplicou uma Etiqueta pessoal a um Documento
> **Quando** o Servidor B (outro Setor) acessa esse Documento na mesa
> **Então** o Servidor B não vê a Etiqueta pessoal
> **Quando** o Servidor A cria e aplica uma Etiqueta compartilhada com o Setor do Servidor B a outro Documento
> **Então** o Servidor B consegue ver essa Etiqueta compartilhada
>
> **Resultado esperado:** Etiqueta pessoal visível só na mesa de quem criou; Etiqueta compartilhada visível para os Setores com quem foi compartilhada.
>
> **Pós-condição:** duas Etiquetas criadas e aplicadas, cada uma com a visibilidade testada.
>
> **Critérios cobertos:** [[01 - Demanda#^c12|C12]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-012

> [!example]- CT-013 · Cadastro de Contato externo (PF/PJ) com e-mail de confirmação (ONDA1-13)
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
> **Origem:** ONDA1-13 da Proposta da Onda 1 (SGV-12200). **TR:** 1.32 ("área para cadastro e gerenciamento de contatos externos, sejam cidadãos (pessoa física) ou empresas (pessoas jurídicas)... cadastro único na plataforma"), 1.32.1 ("ao serem cadastrados... os respectivos novos contatos devem receber um email para confirmação do cadastro").
>
> **Descrição:** confirma que um novo Contato externo (Cidadão PF ou Empresa PJ) recebe e-mail de confirmação ao se cadastrar.
>
> **Pré-condições:**
> - O CPF/CNPJ usado no cadastro ainda não tem Contato externo associado (garante cadastro único).
>
> **Dado** que o Cidadão/Empresa preenche o cadastro de Contato externo com CPF ou CNPJ
> **Quando** o cadastro é concluído
> **Então** o sistema envia um e-mail de confirmação do cadastro para o Contato
>
> **Resultado esperado:** cadastro criado; e-mail de confirmação recebido.
>
> **Pós-condição:** Contato externo registrado como novo cadastro.
>
> > [!info] Limite conhecido
> > O auto-registro de Pessoa Física (fluxo específico de PF se auto-cadastrando) não foi localizado no código consultado (02 §6) — executar este CT pelo fluxo de cadastro efetivamente disponível na tela, registrando qual foi usado.
>
> **Critérios cobertos:** [[01 - Demanda#^c13|C13]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-013

> [!example]- CT-014 · Central de atendimento: acesso a Serviço via canais digitais do órgão (ONDA1-14)
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
> **Origem:** ONDA1-14 da Proposta da Onda 1 (SGV-12200). **TR:** 1.36 ("deve ser disponibilizado uma central de atendimento para que os cidadãos, empresas e entes externos possam ter acesso, através dos canais digitais do órgão, para realizar as suas solicitações e ter acesso aos serviços oferecidos pela entidade").
>
> **Descrição:** confirma que Cidadãos, Empresas e Entes externos acessam, pela Central de atendimento, um Serviço oferecido pelo órgão.
>
> **Pré-condições:**
> - Existe um Serviço disponibilizado pelo órgão, acessível pela Central de atendimento.
>
> **Dado** que existe um Serviço disponibilizado pela Central de atendimento
> **Quando** um Cidadão/Empresa/Ente externo acessa a Central
> **Então** ele consegue ver e acessar esse Serviço
>
> **Resultado esperado:** Serviço visível e acessível na Central de atendimento.
>
> **Pós-condição:** nenhuma alteração de estado — é um acesso/consulta.
>
> > [!info] Limite conhecido
> > O TR (1.36) não detalha o mecanismo exato dos "canais digitais do órgão" — este CT verifica o(s) canal(is) efetivamente disponível(is) no ambiente de teste, sem presumir qual(is) o TR pretendia.
>
> **Critérios cobertos:** [[01 - Demanda#^c14|C14]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-014

> [!example]- CT-015 · Ambiente virtual do Usuário externo: abertura e acompanhamento de Demanda (ONDA1-15)
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
> **Origem:** ONDA1-15 da Proposta da Onda 1 (SGV-12200). **TR:** 1.37 ("cada usuário externo deverá ter acesso a um ambiente virtual próprio, onde poderá receber notificações e acompanhar o andamento das demandas que abriu ou solicitou... assim como, abrir novas demandas").
>
> **Descrição:** confirma que um Usuário externo abre uma Demanda e consegue acompanhá-la (notificações, andamento) no seu ambiente virtual próprio.
>
> **Pré-condições:**
> - O Usuário externo está cadastrado e tem acesso ao seu ambiente virtual.
>
> **Dado** que o Usuário externo está no seu ambiente virtual
> **Quando** ele abre uma nova Demanda
> **Então** a Demanda aparece no seu ambiente, e ele recebe notificações e consegue acompanhar o andamento dela
>
> **Resultado esperado:** Demanda aberta; notificações recebidas; andamento visível para o Usuário externo no seu ambiente.
>
> **Pós-condição:** Demanda registrada, associada ao Usuário externo que a abriu.
>
> > [!info] Limite conhecido
> > Se "Demanda" é uma entidade própria ou um Documento/Processo comum de origem externa segue em aberto (inferência da fatia 05, não confirmada — 02 §6) — não presumir qual é; registrar na execução o que foi observado.
>
> **Critérios cobertos:** [[01 - Demanda#^c15|C15]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-015

> [!example]- CT-016 · Divulgação de Documento: mural interno vs. canal externo/Jornal Oficial (ONDA1-16)
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
> **Origem:** ONDA1-16 da Proposta da Onda 1 (SGV-12200). **TR:** 1.38.1.a (divulgação interna: "documentos e/ou comunicações oficiais sejam divulgados no mural interno, visível a todos os servidores cadastrados"); 1.38.1.b.i (divulgação externa em canal oficial, "acessível por qualquer pessoa com acesso à internet, sem a necessidade de login"); 1.38.3.1 ("cidadãos possam acessar os documentos divulgados no jornal oficial por meio de uma interface pública, com funcionalidades de busca e filtros").
>
> **Descrição:** confirma que um Documento divulgado aparece no mural interno do Servidor e, quando configurado para canal externo, fica acessível publicamente no Jornal Oficial, localizável por busca/filtros.
>
> **Pré-condições:**
> - Existe um Documento configurado para divulgação (mural interno e/ou canal externo).
>
> **Dado** que um Documento é divulgado no mural interno
> **Quando** um Servidor acessa seu mural
> **Então** ele visualiza o Documento divulgado
>
> **Dado** que um Documento é divulgado no canal externo/Jornal Oficial
> **Quando** um Cidadão acessa a interface pública do Jornal Oficial
> **Então** ele consegue localizar o Documento, inclusive usando busca/filtros
>
> **Resultado esperado:** Documento visível no mural interno do Servidor destinatário; Documento acessível publicamente no Jornal Oficial, sem necessidade de login, e localizável via busca/filtros.
>
> **Pós-condição:** nenhuma alteração de estado — é um acesso/consulta.
>
> > [!info] Limite conhecido
> > O acesso público sem login (1.38.1.b.i) é exigência literal do TR, mas não há evidência de teste automatizado localizada para esse acesso específico (02 §7) — registrar na execução o que foi observado, sem presumir ausência no produto.
>
> **Critérios cobertos:** [[01 - Demanda#^c16|C16]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-016

> [!example]- CT-017 · Solicitação de assinatura sequencial com signatários internos/externos (ONDA1-17)
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
> **Origem:** ONDA1-17 da Proposta da Onda 1 (SGV-12200). **TR:** 1.40.3.b (assinaturas sequenciais: "a ordem de assinaturas do documento, pelos signatários, deve ser seguida conforme foi definido na configuração. De modo que, enquanto o signatário da vez não assinar, os demais devem ficar impossibilitados de assinar"); 1.40.3.c (seleção de signatários internos — servidores — e externos — pessoas físicas ou jurídicas).
>
> **Descrição:** confirma que uma solicitação de assinatura sequencial, com signatários internos e externos, respeita a ordem definida: um signatário fora da sua vez não consegue assinar antes do signatário da vez.
>
> **Pré-condições:**
> - Existe uma solicitação de assinatura sequencial criada, com pelo menos um signatário interno (Servidor) e um externo, em ordem definida.
>
> **Dado** que uma solicitação de assinatura sequencial foi criada com signatários internos e externos em ordem definida
> **Quando** um signatário fora da sua vez tenta assinar
> **Então** o sistema impede essa assinatura
>
> **Quando** o signatário da vez assina
> **Então** a assinatura é registrada e a vez passa ao próximo signatário da ordem definida
>
> **Resultado esperado:** tentativa de assinatura fora da vez bloqueada; assinatura do signatário da vez aceita, liberando a vez do próximo signatário.
>
> **Pós-condição:** Documento permanece com assinaturas pendentes dos signatários restantes, respeitando a ordem definida.
>
> > [!info] Limite conhecido
> > A cobertura técnica localizada (fatia 17, CTs A30-C01–C08) testa a criação/execução da solicitação sequencial, mas não uma tentativa de assinatura fora da vez — esse bloqueio é o alvo declarado deste CT, a verificar na execução. "Contribuinte" como ator distinto do signatário externo não tem evidência de código localizada (02 §7) — não presumir distinção sem confirmação. **Fora deste CT:** recusa de assinatura (TR 1.40.5) é item distinto de 1.40.3, não tratado aqui.
>
> **Critérios cobertos:** [[01 - Demanda#^c17|C17]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-017

> [!example]- CT-018 · Criação delegada de documento via Chave de acesso (ONDA1-18)
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
> **Origem:** ONDA1-18 da Proposta da Onda 1 (SGV-12200). **TR:** 1.41.1.b.ii (ao criar a chave, definir "um limite de uso para a chave... um período de uso e/ou uma quantidade de documentos possíveis de ser gerado com a chave"); 1.41.2.a (servidor pode usar permissões próprias ou "uma chave de acesso concedida por outro servidor" ao criar documento); 1.41.2.d ("sempre que um documento for gerado utilizando uma chave de acesso, o servidor que criou a chave receberá uma notificação, podendo visualizar e acompanhar o documento gerado").
>
> **Descrição:** confirma que um Servidor convenente usa uma Chave de acesso concedida por um Servidor concedente para criar um Documento dentro do limite de uso definido, e que o concedente é notificado.
>
> **Pré-condições:**
> - Existe uma Chave de acesso concedida por um Servidor concedente a um Servidor convenente, com limite de uso definido.
>
> **Dado** que o Servidor convenente possui uma Chave de acesso concedida dentro do limite de uso
> **Quando** ele cria um Documento usando essa chave
> **Então** o Documento é criado vinculado à chave, dentro do limite definido
> **E** o Servidor concedente recebe uma notificação do uso
>
> **Resultado esperado:** Documento criado via Chave de acesso, respeitando o limite de uso definido; notificação enviada ao Servidor concedente.
>
> **Pós-condição:** uso da chave registrado para rastreabilidade (1.41.2.e); ao atingir o limite estabelecido, a chave é encerrada automaticamente (1.41.1.c.i).
>
> > [!warning] Limite conhecido
> > A notificação ao concedente (1.41.2.d) não teve evidência de teste automatizado localizada na fatia 18 — registrar na execução o que foi observado, sem presumir ausência no produto. O fluxo para quando o servidor tem só permissão própria (sem chave) para o tipo de documento (1.41.2.c, recorte 09) segue A confirmar e não é tratado por este CT.
>
> **Critérios cobertos:** [[01 - Demanda#^c18|C18]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-018

> [!example]- CT-019 · Edição de identidade visual do órgão: administrador geral autorizado, demais barrados (ONDA1-19)
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
> **Origem:** ONDA1-19 da Proposta da Onda 1 (SGV-12200). **TR:** 1.42.1.b ("possibilidade de editar as cores temáticas da interface do menu principal do sistema"); 1.42.1.c ("upload e gerenciamento das imagens institucionais do órgão que serão exibidas em todo o sistema").
>
> **Descrição:** confirma que um Servidor com permissão de administrador geral consegue editar as cores temáticas do menu principal e fazer upload/gerenciamento de imagens da marca do órgão (tela de Configurações da Instância), e que um Servidor sem administrador geral e sem a permissão extra "configuração de instância" é barrado ao tentar a mesma ação.
>
> **Pré-condições:**
> - Existe um Servidor com permissão de administrador geral.
> - Existe um Servidor sem permissão de administrador geral e sem a permissão extra "configuração de instância" ativa.
>
> **Dado** que um Servidor com permissão de administrador geral acessa a tela de Configurações da Instância
> **Quando** ele edita as cores temáticas
> **Então** as cores são atualizadas na interface
>
> **Quando** ele faz upload de uma imagem da marca
> **Então** a imagem passa a ser gerenciada e exibida no sistema
>
> **Dado** que um Servidor sem administrador geral e sem a permissão extra "configuração de instância" acessa a tela de Configurações da Instância
> **Quando** ele tenta editar as cores temáticas ou fazer upload de uma imagem da marca
> **Então** o sistema barra a ação
>
> **Resultado esperado:** administrador geral edita as cores temáticas e envia/gerencia imagem da marca com sucesso; Servidor sem administrador geral e sem a permissão extra é barrado ao tentar a mesma ação.
>
> **Pós-condição:** alterações de personalização persistem até nova edição, quando realizadas pelo administrador geral; nenhuma alteração ocorre na tentativa barrada.
>
> > [!warning] Origem de produto, não do TR
> > A exigência de permissão para esta funcionalidade — administrador geral **ou** a permissão extra "configuração de instância" ativa — é documentada no módulo de produto [[QA Workspace/04 Conhecimento/Módulos/Configurações da Instância|Configurações da Instância]] (importado do Notion em 20/10/2026, ainda **sem comportamento observado em execução/teste**), não afirmada pelo texto literal do TR: 1.42.1.b/c não especifica o ator autorizado nem restrições de acesso. Este cenário usa o administrador geral como ator positivo único e o bloqueio de quem não tem nenhuma das duas permissões como negativo. Não apresentar essa exigência como requisito do TR.
>
> > [!info] Fora deste CT
> > Acesso às informações cadastrais do órgão (1.42.1.a) não faz parte deste cenário.
>
> **Critérios cobertos:** [[01 - Demanda#^c19|C19]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-019

> [!example]- CT-020 · Consulta de indicadores de Servidores agrupados por status e por nível de permissão (ONDA1-20)
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
> **Origem:** ONDA1-20 da Proposta da Onda 1 (SGV-12200). **TR:** 1.43.5.a ("total de servidores: ativos e inativos"), 1.43.5.b ("servidores por status: quantidade de servidores categorizados por status"), 1.43.5.c ("servidores por nível de permissão: exibição por níveis").
>
> **Descrição:** confirma que o painel de Estatísticas exibe, para os servidores cadastrados, o total de ativos/inativos e os agrupamentos por status e por nível de permissão.
>
> **Pré-condições:**
> - Existem servidores cadastrados com diferentes status e níveis de permissão.
>
> **Dado** que existem servidores cadastrados com diferentes status e níveis de permissão
> **Quando** um Administrador/usuário autorizado consulta o painel de Estatísticas de Servidores
> **Então** ele visualiza o total de servidores ativos/inativos, agrupados por status e por nível de permissão
>
> **Resultado esperado:** indicadores exibidos: total de ativos/inativos, servidores por status, servidores por nível de permissão.
>
> **Pós-condição:** nenhuma alteração de estado — é consulta/exibição.
>
> > [!info] Limite conhecido
> > Este CT verifica a exibição dos indicadores, sem incluir filtro interativo de tela — o TR (1.43.5) não confirma a existência desse filtro neste subitem, e nenhuma fonte revisada confirma um, por isso nenhum filtro é incluído no cenário. Cálculo/implementação do indicador não verificado. A correspondência entre "administradores e usuários autorizados" (termo do TR) e os 5 níveis canônicos segue A confirmar (recorte 11).
>
> **Critérios cobertos:** [[01 - Demanda#^c20|C20]]
>
> ---
>
> **Informações do CT**
>
> **Tipo:** funcional
> **Camada:** UI/API
> **Automação:** manual
> **Execução:** planejado

^ct-020
