---
tags:
  - bug
  - qa
  - documento
task: "10512"
prioridade: media
status: aberto
data_inicio: 2026-07-31
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: DEV
---
# CNPJ do cidadão PJ é exibido anonimizado na impressão do documento

### Descrição

Durante validação foi identificado que, quando o cidadão Pessoa Jurídica abre um documento e o imprime, o **CNPJ aparece anonimizado** na impressão, em vez de ser exibido por extenso.

O comportamento **não é regressão** da [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]]: já ocorria em **produção** antes da mudança de formato de CNPJ, e isso foi validado. O bug foi apenas **encontrado** durante a execução dos casos daquela melhoria.

---

### Passo a passo para reproduzir

Dado que existe um cidadão Pessoa Jurídica com documento no sistema
E que estou autenticado como esse cidadão PJ
Quando abro o documento e aciono a impressão
Então verifico que o CNPJ é exibido **anonimizado** no documento impresso
E verifico que o mesmo ocorre em **produção**, sem relação com o formato alfanumérico

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10512)

![[10512 - cnpj do cidadao pj e exibido anonimizado na impressao.mp4]]

---

### Resultado Esperado

O CNPJ do cidadão Pessoa Jurídica é exibido **por extenso e formatado** na impressão do documento, como qualquer outro dado de identificação do interessado.

> [!warning]- Gate de doc: a regra não está documentada
> Cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] e [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] em 31/07 — **nenhuma das duas diz como o CNPJ deve aparecer na impressão**, nem se existe alguma regra de mascaramento nessa saída.
>
> O apoio mais próximo é a regra de [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] de que documentos entram na impressão conjunta e são **"exibidos na íntegra"** — mas isso trata da composição do documento, não do dado do interessado, então não sustenta o critério sozinho.
>
> Registrado como **pendência de documentação** (fluxo 8): quando a regra for confirmada com produto, ela entra na doc do módulo.

---

### Critérios de aceite

- [ ] Na impressão do documento aberto pelo cidadão PJ, o CNPJ aparece **por extenso**, sem mascaramento
- [ ] O CNPJ impresso está **formatado** no padrão `XX.XXX.XXX/XXXX-XX` e corresponde ao valor cadastrado
- [ ] O comportamento vale para CNPJ **numérico** e **alfanumérico** — a correção não pode depender do formato

---

### Casos de Teste Básicos

#### **CT-B01 CNPJ exibido por extenso na impressão feita pelo cidadão PJ**

**Dado** que existe um cidadão Pessoa Jurídica com documento no sistema
**E** que estou autenticado como esse cidadão PJ
**Quando** abro o documento e aciono a impressão
**Então** o CNPJ é exibido por extenso e formatado, sem mascaramento
**E** o valor corresponde ao CNPJ cadastrado

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Regressão — o comportamento vale para CNPJ numérico e alfanumérico**

**Dado** que existem dois cidadãos PJ, um com CNPJ numérico e outro com CNPJ alfanumérico
**Quando** cada um abre o próprio documento e aciona a impressão
**Então** os dois CNPJs são exibidos por extenso e formatados

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

*Não executado. Existe para garantir que o fix não resolva só um dos formatos — o defeito é anterior ao alfanumérico, mas a correção vai conviver com ele.*

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

> [!info]- Por que o card nasce em DEV se o bug é de produção
> Bug de produção em sustentação (correção não urgente) **não tem pasta própria** — o card nasce em `DEV/` com `ambiente: DEV`, que representa a **posição na esteira de correção**, e a origem em produção fica na Descrição e no Histórico. Regra em [[Sistema/Contexto/PADROES_QA#Organização de Bugs|PADROES_QA]]; precedentes: SGV-9963 e SGV-9750.
>
> Se a correção for tratada como **urgente**, o card muda para `Hotfix/` com `ambiente: HOTFIX`.

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]] — **apenas origem do achado**, não é defeito daquela entrega. Encontrado durante a execução exploratória dos casos da melhoria; como já ocorria em produção, **não virou CT da 9493** e não afeta nenhum critério de aceite dela.

- Observações:
    - **O produto já usa mascaramento em outro lugar de propósito**: a doc de [[QA Workspace/04 Conhecimento/Módulos/Login|Login]] registra o e-mail anonimizado na mensagem de erro como comportamento intencional. Vale antecipar que o dev pode alegar que a anonimização do CNPJ também é intencional — como não há regra escrita pra esta saída, essa conversa precisa de decisão de produto, e é o que a pendência de documentação resolve.
    - Reproduz em **produção**, confirmado por Rafael, e é anterior à SGV-9493.

- Histórico:
    - 2026-07-31 - 🐛 Bug cadastrado (achado em DEV durante a execução da [[QA Workspace/02 Demandas/DEV/9493 - Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ|SGV-9493]]; confirmado como pré-existente em produção)
