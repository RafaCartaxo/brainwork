---
tags:
  - bug
  - qa
  - usuario-cidadao
task: "10511"
prioridade: media
status: aberto
data_inicio: 2026-07-31
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: usuario-cidadao
ambiente: HML
deploy: pendente_hml
---
# CNPJ alfanumérico aceita letra minúscula sem normalizar no campo

### Descrição

Durante validação foi identificado que o campo de CNPJ aceita letras minúsculas durante a digitação, sem normalizá-las para maiúscula.

No **cadastro de cidadão PJ** — tanto o feito pelo servidor quanto o feito pelo próprio cidadão — o valor só é convertido para caixa alta **ao finalizar o cadastro**. O dado gravado fica correto, mas a digitação não acompanha, e a pessoa que cadastra vê um valor diferente do que será salvo.

No **campo com máscara de CNPJ do construtor de formulários** o comportamento é diferente e mais grave: a normalização **não acontece em nenhuma camada** — o front não converte e o back não trata — e o valor permanece exibido em minúsculas.

---

### Passo a passo para reproduzir

**Cenário 1 — cadastro de cidadão PJ pelo servidor**

Dado que estou em `/cliente/{id}/cidadaos/criar` como servidor
E que tenho um CNPJ alfanumérico válido
Quando digito as letras do CNPJ em **minúsculas** no campo
Então verifico que o campo **mantém as letras em minúsculas** enquanto eu digito
E verifico que só ao finalizar o cadastro o valor é convertido para maiúsculas

**Cenário 2 — cadastro público, o próprio cidadão**

Dado que acesso o cadastro público em `/cadastro/{instanceId}`
E que escolho o tipo Pessoa Jurídica
Quando digito as letras do CNPJ em **minúsculas** no campo
Então verifico que o campo **mantém as letras em minúsculas** enquanto eu digito
E verifico que só ao concluir o cadastro o valor é convertido para maiúsculas

**Cenário 3 — campo com máscara CNPJ no construtor de formulários**

Dado que existe um formulário com campo de número configurado com máscara de CNPJ
Quando preencho esse campo com um CNPJ alfanumérico digitando as letras em **minúsculas**
Então verifico que o valor **não é normalizado em momento nenhum** — nem na digitação nem ao salvar
E verifico que o CNPJ segue **exibido em minúsculas** depois de gravado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10511)

Duas gravações por cenário — o defeito e a correção aprovada. Todas embedadas também no CT correspondente.

| Cenário | CT | Defeito | Correção aprovada |
|---|---|---|---|
| Cadastro de cidadão PJ pelo servidor | CT-B01 | `10511 - cenário 1.mp4` | `10511 - cenário 1 ok.mp4` |
| Cadastro público (signup PJ) | CT-B02 | `10511 - cenário 2.mp4` | `10511 - cenário 2 ok.mp4` |
| Campo com máscara CNPJ no construtor | CT-B03 | `10511 - cenário 3.mp4` | `10511 - cenário 3 ok.mp4` |

---

### Resultado Esperado

A letra digitada em minúscula é **normalizada para maiúscula no próprio campo**, no momento da digitação, em todas as superfícies que usam máscara de CNPJ — e o valor segue em maiúscula depois de gravado e reexibido.

A regra já existe: o **CA5** da [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] estabelece que "letra digitada em minúscula é normalizada para maiúscula". O que falta é ela valer **no campo** (hoje só vale no salvamento) e alcançar **o construtor de formulários** (hoje não vale em lugar nenhum).

---

### Critérios de aceite

- [x] No cadastro de cidadão PJ **pelo servidor**, a letra digitada em minúscula aparece em maiúscula no próprio campo, antes de salvar
- [x] No **cadastro público** (signup PJ), a letra digitada em minúscula aparece em maiúscula no próprio campo, antes de concluir
- [x] No campo com máscara CNPJ do **construtor de formulários**, a letra minúscula é normalizada e o valor é exibido em maiúscula — inclusive depois de salvo e reaberto
- [x] Nas três superfícies, o **valor gravado** permanece em maiúscula (regressão: nos cenários 1 e 2 isso já funciona hoje e não pode quebrar)

---

### Casos de Teste Básicos

#### **CT-B01 Normalização no campo — cadastro de cidadão PJ pelo servidor**

**Dado** que estou em `/cliente/{id}/cidadaos/criar` como servidor
**E** que tenho um CNPJ alfanumérico válido
**Quando** digito as letras do CNPJ em minúsculas
**Então** o campo exibe as letras já em **maiúsculas** durante a digitação
**E** o valor gravado permanece em maiúsculas

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[10511 - cenário 1.mp4]]

*Mesma gravação copiada para a [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] como `9493 - EV-01 - CT-019 - ...`, onde reprova o CT-019.*

![[10511 - cenário 1 ok.mp4]]

*Correção aprovada em DEV (31/07). A gravação acima é o defeito; esta é o comportamento corrigido.*

---

#### **CT-B02 Normalização no campo — cadastro público (signup PJ)**

**Dado** que acesso o cadastro público em `/cadastro/{instanceId}`
**E** que escolho o tipo Pessoa Jurídica
**Quando** digito as letras do CNPJ em minúsculas
**Então** o campo exibe as letras já em **maiúsculas** durante a digitação
**E** o valor gravado permanece em maiúsculas

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[10511 - cenário 2.mp4]]

![[10511 - cenário 2 ok.mp4]]

*Correção aprovada em DEV (31/07). A gravação acima é o defeito; esta é o comportamento corrigido.*

---

#### **CT-B03 Normalização no campo com máscara CNPJ do construtor de formulários**

**Dado** que existe um formulário com campo de número configurado com máscara de CNPJ
**Quando** preencho o campo com um CNPJ alfanumérico digitando as letras em minúsculas
**Então** o campo exibe as letras já em **maiúsculas** durante a digitação
**E** o valor gravado está em maiúsculas
**E** ao reabrir o registro o CNPJ é exibido em maiúsculas

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!warning]- Este cenário falha diferente dos outros dois
> Nos CT-B01 e CT-B02 o **dado final fica correto** — a falha é de digitação, e o back normaliza ao salvar. Aqui **não há normalização em camada nenhuma**: o valor é gravado e reexibido em minúsculas. Se a correção for só no front, este cenário continua falhando na reexibição de registro antigo.

**Evidências de Testes:**

![[10511 - cenário 3.mp4]]

*Foi a primeira gravação da sessão — nasceu com nome genérico e foi renomeada pro padrão `cenário N` quando o Rafael confirmou a qual cenário pertencia.*

![[10511 - cenário 3 ok.mp4]]

*Correção aprovada em DEV (31/07). A gravação acima é o defeito; esta é o comportamento corrigido.*

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — achado na execução exploratória dos casos de teste da melhoria de CNPJ alfanumérico

- Observações:
    - O caso que este bug reprova é o **CT-019** da [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] (critério **CA5**), que afirma a conversão **no campo** e o valor salvo em maiúsculas — a segunda metade passa, a primeira não.
    - O cenário 3 toca também o **CT-027** da 9493 (campo com máscara CNPJ no construtor, critério **CA23**), que segue **não executado**: o defeito foi observado de forma exploratória, não numa execução completa daquele CT nas três configurações que ele cobre (módulo principal, módulo cliente e assunto/serviço).
    - Evidência compartilhada com [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — o **cenário 1** foi copiado como `9493 - EV-01 - CT-019 - ...` e embedado no CT-019 daquele card. É o cenário certo pra lá: o CT-019 afirma a normalização no campo **e** o valor salvo em maiúsculas, que é exatamente o meio-sucesso do cadastro. O cenário 3 falha nas duas metades e pertence ao CT-027, que ainda não foi executado.
    - Rafael relatou que provavelmente **1 ou 2 ajustes** resolvem os três cenários — os dois primeiros compartilham a mesma causa (normalização só no submit), o terceiro é uma superfície que ficou de fora.

- Histórico:
    - 2026-07-31 - 🐛 Bug cadastrado
    - 2026-07-31 - ✅ Aprovada em DEV (os 3 cenários retestados e aprovados; card segue pra HML com `deploy: pendente_hml`)
