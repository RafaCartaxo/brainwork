---
tags:
  - bug
  - qa
  - despacho
  - assinatura
task: "10607"
prioridade: media
status: aberto
data_inicio: 2026-08-04
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: DEV
---
# Assinatura de resposta retificada ainda aparece na impressão do documento

### Descrição

Durante validação da retificação de despacho em DEV ([[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]]) foi identificado que, ao **retificar uma resposta que já havia sido assinada**, a assinatura **continua sendo trazida na impressão do documento** — sem sinalização de que foi invalidada.

A retificação deveria ter cancelado essa assinatura, já que o conteúdo do despacho mudou.

---

### Passo a passo para reproduzir

Dado que exista um despacho de resposta em um documento
E que essa resposta já tenha sido **assinada**
Quando o autor retificar a resposta
E o documento for impresso
Então verifico que a assinatura da resposta **continua aparecendo na impressão**, sem indicação de que foi invalidada

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10607)

![[10607 - assinatura de resposta retificada ainda aparece na.mp4]]


---

### Resultado Esperado

A assinatura da resposta retificada **não é apresentada como válida** na impressão. A doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] é explícita quanto ao efeito da retificação:

> **Todas as assinaturas** (concluídas ou pendentes) do despacho original **e dos anexos** são canceladas, por alteração de conteúdo.

E o pop-up de aviso da própria retificação, lido no Figma, avisa o usuário disso antes de confirmar: *"todas as ações anteriores realizadas no mesmo deverão ser refeitas, **incluindo as assinaturas realizadas**"*.

Como a assinatura foi cancelada, ela precisa chegar à impressão **marcada como sem efeito / inválida** — do mesmo modo que a doc já define para o despacho cancelado, cujas assinaturas saem com a sinalização de **sem efeito**. O que não pode acontecer é o que se observa hoje: a assinatura sair na impressão como se ainda valesse.

---

### Critérios de aceite

- [ ] Após retificar uma resposta assinada, a assinatura **não aparece como válida** na impressão do documento
- [ ] A assinatura cancelada pela retificação chega à impressão com **sinalização de invalidada** (ou é removida), de forma que quem lê o papel saiba que ela não vale
- [ ] O mesmo vale no **download** do documento, não só na impressão — a página de assinaturas é parte integrante do PDF
- [ ] **Sem regressão**: resposta assinada e **não** retificada continua trazendo a assinatura normalmente, como válida

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura de resposta retificada não sai como válida na impressão**

**Dado** um despacho de resposta já assinado
**Quando** o autor retificar a resposta e o documento for impresso
**Então** a assinatura não é apresentada como válida — aparece com sinalização de invalidada ou não aparece

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Mesmo comportamento no download do documento**

**Dado** o mesmo despacho de resposta retificado após a assinatura
**Quando** o documento for baixado
**Então** a assinatura também não é apresentada como válida no arquivo

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Resposta assinada e não retificada segue normal (regressão)**

**Dado** um despacho de resposta assinado e **sem** retificação
**Quando** o documento for impresso
**Então** a assinatura aparece normalmente, como válida

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] — **defeito de melhoria em DEV**, achado na validação da retificação de despacho.

- **Relacionado**: [[QA Workspace/02 Demandas/DEV/10596 - Bug Autor Nao Consegue Cancelar O Proprio Despacho|SGV-10596]] — segundo defeito da mesma rodada de validação, no cancelamento.

- Observações:
    - **Gate de doc: divergência confirmada.** A regra de invalidação das assinaturas na retificação é explícita, e o próprio diálogo de aviso do Figma avisa o usuário disso antes de confirmar. Não é lacuna de especificação — o comportamento observado contraria texto escrito.
    - 🔎 **Uma lacuna pequena a confirmar com produto**: a doc garante que as assinaturas são **canceladas**, mas descreve o **tratamento visual na saída** só para o despacho **cancelado** (assinaturas com sinalização de "sem efeito", tarja `SEM EFEITO` no PDF). Para o **retificado** ela define a tag "Retificado" na timeline e em todas as visualizações, sem detalhar como a assinatura invalidada deve aparecer no papel. Por isso o critério aceita as duas saídas — marcada como inválida **ou** ausente —, e o que reprova é sair **como válida**.
    - Cobertura enxuta por escolha: 3 CT-B para 4 critérios. O 2º critério (sinalização legível na saída) é asserção dentro do CT-B01 e do CT-B02, não CT próprio.

- Histórico:
    - 2026-08-04 - 🐛 Bug cadastrado
