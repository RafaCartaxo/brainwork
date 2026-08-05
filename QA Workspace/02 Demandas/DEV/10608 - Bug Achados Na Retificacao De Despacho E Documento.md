---
tags:
  - bug
  - qa
  - despacho
task: "10608"
prioridade: media
status: aberto
data_inicio: 2026-08-04
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: DEV
---
# Achados na retificação de despacho e documento (aviso, botão e copy)

> [!info] Card de registro — três achados na mesma rodada
> Card agrupado de propósito: são três problemas pequenos e independentes, encontrados na validação da retificação em DEV ([[QA Workspace/02 Demandas/DEV/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]]). Registro rápido de atuação; cada item tem seu critério e seu CT.

### Descrição

Durante validação foi identificado que:

1. **Aviso incorreto quando não há solicitante selecionado** na retificação do despacho.
2. **Botão de retificar documento fora do padrão** definido no Figma.
3. **Copy do despacho de resposta ao retificar está incorreta** — traz a copy de **despacho cancelado**.

---

### Passo a passo para reproduzir

**Achado 1 — aviso incorreto sem solicitante**

Dado que o usuário esteja na retificação de um despacho
E que **nenhum solicitante** esteja selecionado
Quando tentar prosseguir
Então verifico que o aviso exibido **não corresponde** à situação

**Achado 2 — botão fora do padrão**

Dado que o usuário esteja na tela de retificação de **documento**
Quando observar o botão de retificar
Então verifico que ele **não segue o padrão** definido no handoff do Figma

**Achado 3 — copy de cancelado na resposta retificada**

Dado que exista um despacho de **resposta**
Quando ele for **retificado**
Então verifico que a copy exibida é a de **despacho cancelado**, e não a de retificação

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10608)


---

### Resultado Esperado

1. **Aviso coerente com a situação**: sem solicitante selecionado, a mensagem deve dizer que falta selecionar o solicitante — e não outra coisa.
2. **Botão conforme o handoff**: o botão de retificar documento segue o padrão do Figma — [nó `7316-21611`](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=7316-21611) do arquivo Tramitação — Handoff.
3. **Copy de retificação, não de cancelamento**: a resposta retificada exibe a copy de **retificação**. A doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] separa os dois estados — o retificado recebe a tag **"Retificado"**, o cancelado a tag **"Despacho cancelado"** — e a justificativa da retificação é exibida ao final da subthread.

---

### Critérios de aceite

- [ ] **(1)** Sem solicitante selecionado, o aviso exibido descreve **essa** condição
- [ ] **(2)** O botão de retificar documento segue o padrão do nó `7316-21611` do handoff
- [ ] **(3)** Resposta retificada exibe copy e tag de **retificação**, não de cancelamento
- [ ] **Sem regressão** no caminho felizes de cada um: com solicitante selecionado o fluxo segue normal, e a copy de **cancelamento** continua correta onde ela realmente se aplica

---

### Casos de Teste Básicos

#### **CT-B01 Aviso correto quando nenhum solicitante está selecionado** *(1)*

**Dado** que o usuário esteja na retificação de um despacho
**E** não tenha selecionado solicitante
**Quando** tentar prosseguir
**Então** o aviso exibido informa que é preciso selecionar o solicitante

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Botão de retificar documento segue o handoff** *(2)*

**Dado** que o usuário esteja na tela de retificação de documento
**Quando** observar o botão de retificar
**Então** ele corresponde ao padrão definido no nó `7316-21611` do Figma

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Resposta retificada exibe copy de retificação** *(3)*

**Dado** um despacho de resposta
**Quando** ele for retificado
**Então** a copy e a tag exibidas são as de **retificação**, e não as de despacho cancelado

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

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] — **defeitos de melhoria em DEV**, os três achados na validação da retificação.

- **Relacionados** (mesma rodada): [[QA Workspace/02 Demandas/DEV/10596 - Bug Autor Nao Consegue Cancelar O Proprio Despacho|SGV-10596]] (permissão no cancelamento) e [[QA Workspace/02 Demandas/DEV/10607 - Bug Assinatura De Resposta Retificada Ainda Aparece Na Impressao|SGV-10607]] (assinatura na impressão).

- Observações:
    - ⚠️ **Cuidado no achado 3, pra o dev não "corrigir" comportamento certo.** A doc diz que **retificar o despacho principal cancela todos os despachos de resposta a ele**, seguindo a regra de despacho cancelado. Então existe um caso em que a copy de **cancelado** numa resposta está **correta**: quando o retificado foi o **principal**. O defeito é quando se retifica **a própria resposta** e ela exibe copy de cancelamento em vez de retificação. **Separar os dois cenários na validação** — é a diferença entre bug e regra.
    - **Copys a capturar**: o texto exato do aviso do achado 1 e da copy do achado 3 não estão transcritos aqui. Vale anexar print de cada um, porque asserção de copy sem o texto literal não fecha.
    - **Achado 2 sem o padrão transcrito**: o nó do Figma está linkado, mas não consegui abrir para descrever o padrão esperado (a extensão do navegador caiu no momento do registro). Antes de mandar pro dev, vale dizer **o que** está fora — cor, tipo de botão, posição, rótulo.
    - Card agrupado por decisão de agilidade. Se algum dos três crescer (virar discussão de produto ou pedir análise própria), vale separar em card dedicado.

- Histórico:
    - 2026-08-04 - 🐛 Bug cadastrado (card de registro com 3 achados da rodada de retificação)
