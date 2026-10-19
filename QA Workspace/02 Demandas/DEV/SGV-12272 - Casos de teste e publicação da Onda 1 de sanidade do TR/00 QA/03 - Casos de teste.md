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

> Os critérios ficam em `01 - Demanda`; esta nota concentra os 20 cenários executáveis, um por cenário aprovado na Proposta da Onda 1 (SGV-12200). **Lote 1 (CT-001 a CT-005) redigido; CT-006 a CT-020 seguem pendentes.**

---

## Matriz de cobertura

| Critério | CTs |
|---|---|
| [[01 - Demanda#^c1\|C1]] | [[03 - Casos de teste#^ct-001\|CT-001]], [[03 - Casos de teste#^ct-002\|CT-002]], [[03 - Casos de teste#^ct-003\|CT-003]], [[03 - Casos de teste#^ct-004\|CT-004]], [[03 - Casos de teste#^ct-005\|CT-005]] *(CT-006 a CT-020 pendentes — próximos lotes)* |

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
> **Resultado esperado:** na 5ª tentativa malsucedida, a conta passa a bloqueada; uma nova tentativa com a senha correta não consegue autenticar enquanto o bloqueio estiver ativo.
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
> **Resultado esperado:** em "Licença" e "Férias", o Servidor mantém um subconjunto mínimo de funcionalidades não transacionais (não é bloqueio total); no estado que o TR chama de "Inativo", o acesso é negado por completo.
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
> **Resultado esperado:** o Assunto/Serviço exibe a categoria-base herdada do Módulo, sem exigir que o Servidor a escolha manualmente.
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
