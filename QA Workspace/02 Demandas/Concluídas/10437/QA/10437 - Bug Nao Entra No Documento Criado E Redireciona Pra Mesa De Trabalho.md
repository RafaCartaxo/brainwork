---
tags:
  - bug
  - qa
  - documento
task: "10437"
prioridade: altíssima
status: resolvido
data_inicio: 2026-07-29
data_fim: "2026-07-30"
responsavel: Rafael
cadastrado_por: Rafael
modulo: documento
ambiente: HML
---
# Não é possível entrar no documento criado — sistema redireciona pra mesa de trabalho

> [!danger] Impeditivo
> Bloqueia a criação e o acesso a qualquer documento novo, e com isso **trava as validações que dependem de criar documento** (praticamente toda a esteira). Reportado como impeditivo pelo Rafael em 29/07.

### Descrição

Ao criar um documento novo, o sistema **não permite entrar no documento criado** — em vez de abrir o documento, redireciona o usuário pra **mesa de trabalho**.

O comportamento documentado é o oposto: ao finalizar a criação, deve haver flash message de sucesso e **redirecionamento automático pro documento**.

---

### Passo a passo para reproduzir

Dado que eu estou logado no sistema
E que tenho permissão pra criar documento no módulo
Quando eu crio um documento novo
E finalizo a criação
Então verifico que não consigo entrar no documento criado e sou redirecionado pra mesa de trabalho

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10437)

![[10437 - corrigido entra no documento criado sem redirecionar pra mesa.mp4]]

![[10437 - nao entra no documento criado e redireciona pra mesa de trabalho.mp4]]

---

### Resultado Esperado

Ao finalizar a criação de um documento novo, o usuário é **direcionado pro documento** (com flash message de sucesso), podendo acessá-lo normalmente — sem ser jogado pra mesa de trabalho.

---

### Critérios de aceite

- [x] Ao criar um documento novo, o usuário consegue entrar no documento criado
- [x] O redirecionamento após a criação leva **ao documento**, não à mesa de trabalho
- [x] A flash message de sucesso é exibida ao finalizar a criação

---

### Casos de Teste Básicos

#### **CT-B01 Acesso ao documento após a criação**

**Dado** que eu tenho permissão pra criar documento no módulo
**Quando** eu crio um documento novo e finalizo a criação
**Então** verifico que sou direcionado pro documento criado, com flash message de sucesso, e consigo acessá-lo

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10437 - corrigido entra no documento criado sem redirecionar pra mesa.mp4]]

Reprovação original de 29/07, mantida como histórico do defeito:

![[10437 - nao entra no documento criado e redireciona pra mesa de trabalho.mp4]]

---

#### **CT-B02 Documento gerado a partir de outro (fluxo "Gerar documento")**

**Dado** que eu estou num documento e uso a ação "Gerar documento"
**Quando** eu confirmo e finalizo a criação do novo documento
**Então** verifico que há redirecionamento automático pro documento gerador, conforme a doc do módulo — e não pra mesa de trabalho

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

> [!warning] Não executado
> Este CT cobre o fluxo "Gerar documento" (documento criado a partir de outro), que era a **dúvida de escopo do diagnóstico**: o defeito era em toda criação ou só nesse caminho? O CT-B01 aprovado responde pela criação comum; este caminho não foi exercitado.

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-10437** (número informado pelo Rafael em 29/07).
- ⚠️ **Ambiente inferido como homologação** — é onde o Rafael está validando hoje e onde a gravação foi feita (14:22). Corrigir se foi em DEV.
- **Prioridade `altíssima`** pelo caráter impeditivo declarado: sem conseguir entrar em documento novo, as validações que dependem de criar documento ficam bloqueadas.
- **Gate de doc** (2026-07-29, fluxo 8): **divergência confirmada contra doc**, não gap. [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento#Fluxo para gerar um documento|Gerar Documento § Fluxo para gerar um documento]] define no passo 6:

    > "Ao finalizar a criação e emissão: flash message de sucesso + **redirecionamento automático pro documento gerador**."

    Ou seja, há regra escrita dizendo que o destino é o documento — o redirecionamento pra mesa de trabalho a contraria. O CT-B02 cobre especificamente esse fluxo documentado.
- **A confirmar no diagnóstico**: o defeito ocorre em **toda** criação de documento ou só no fluxo "Gerar documento" (documento gerado a partir de outro)? O CT-B01 cobre a criação comum e o CT-B02 o fluxo gerador — a resposta muda o escopo do fix.
- Histórico:
    - 2026-07-29 - 🐛 SGV-10437 - Bug cadastrado (impeditivo; divergência confirmada contra a doc de Gerar Documento)
    - 2026-07-30 - ✅ Aprovada em homologação (impeditivo resolvido: entra no documento criado sem redirecionar pra mesa de trabalho)
