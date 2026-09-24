---
tags:
  - bug
  - qa
  - assinatura
task: "5783"
prioridade: alta
status: resolvido
data_inicio: 2026-07-17
data_fim: "2026-07-30"
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
---
# Representante legal incorreto na assinatura após alteração

### Descrição

Em cidadão **Pessoa Jurídica**, ao **alterar o responsável legal** do cadastro e em seguida assinar um documento, a assinatura saía com o representante **antigo** — os dados levados pro documento não acompanhavam a alteração.

Corrigido e validado em homologação em 30/07.

---

### Passo a passo para reproduzir

**Dado** que eu tenho um cidadão Pessoa Jurídica com responsável legal cadastrado
**E** que eu altero o responsável legal (informando outro CPF, com o nome atualizado pela API)
**Quando** eu assino um documento como essa PJ
**Então** verificava que o documento saía com os dados do responsável legal **anterior**, não do atualizado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://5783)

![[5783 - representante legal atualizado na assinatura aprovado em homologacao.mp4]]

---

### Resultado Esperado

Depois de alterar o responsável legal da PJ, a assinatura leva pro documento os dados **do responsável legal atual** — empresa + responsável atualizado.

---

### Critérios de aceite

- [x] Alterado o responsável legal da PJ, a assinatura seguinte leva pro documento o **responsável atualizado**
- [x] Vale para **Assinatura SoGov** (autenticação por senha da conta)
- [ ] Vale para **Assinatura ICP** (certificado vinculado ao CNPJ ou ao responsável legal) — não exercitado nesta validação
- [x] Documentos assinados **antes** da alteração seguem exibindo o responsável da época (o histórico não é reescrito)

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura após alteração do responsável legal (SoGov)**

**Dado** que eu tenho um cidadão PJ com responsável legal cadastrado
**E** que eu altero o CPF do responsável legal, com o nome atualizado pela API
**Quando** eu assino um documento como essa PJ pelo fluxo SoGov
**Então** verifico que o documento traz os dados da empresa e do **responsável legal atualizado**

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[5783 - representante legal atualizado na assinatura aprovado em homologacao.mp4]]

---

#### **CT-B02 Documentos assinados antes da alteração**

**Dado** que a PJ assinou um documento **antes** da troca de responsável legal
**Quando** eu consulto esse documento depois da troca
**Então** verifico que ele segue exibindo o responsável legal **da época da assinatura**, sem ser reescrito

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[5783 - representante legal atualizado na assinatura aprovado em homologacao.mp4]]

---

#### **CT-B03 Assinatura ICP após alteração do responsável legal**

**Dado** que eu tenho um cidadão PJ com certificado ICP e responsável legal alterado
**Quando** eu assino um documento pelo fluxo ICP
**Então** verifico que o documento traz os dados da empresa e do responsável legal atualizado

**Execução Passou?**
- [ ] Sim
- [ ] Não

> [!info]- Não executado nesta validação
> A doc de [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] trata SoGov e ICP como caminhos distintos, ambos levando "os dados da empresa **e** do responsável legal" pro documento. A validação cobriu o SoGov. O ICP exige certificado de teste vinculado ao CNPJ ou ao responsável legal — massa que não estava disponível.

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-5783** — `Alta`, dev **Diogo Sobreira** (Squad 1), batida na [[QA Workspace/Planejamento/SP15|Triagem SP15]] em 17/07 com o título "Representante legal incorreto na assinatura após alteração".
- **Card criado retroativamente em 30/07**, no momento da aprovação — o bug não tinha card no vault, só a entrada da triagem e o histórico de análise. Descrição e passo a passo reconstruídos do título oficial + narrativa da validação (mesmo caminho da [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]]).
- **Gate de doc** (2026-07-30, fluxo 8): **divergência confirmada** — o comportamento contrariava regra escrita em [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]], em dois pontos que se somam:

    | Onde | O que diz |
    |---|---|
    | § Cadastro da PJ | "**CPF do responsável legal**: se já existe, pode ser alterado — alterando, a API é consultada novamente e o **Nome do responsável legal é atualizado**" |
    | § Assinatura | "**Assinatura SoGov** / **Assinatura ICP**: no documento, entram os dados da empresa **e do responsável legal**" |

    Juntas: o cadastro se atualiza na troca, e a assinatura leva o responsável legal pro documento — logo a assinatura tem que levar o **atualizado**. Levar o antigo contraria as duas.
- **Histórico de análise já registrado no vault**:
    - 17/07 — batida na Triagem SP15, já com critérios definidos.
    - 20/07 — [MR !581](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/581) revisado (`git fetch` da ref): cenários de teste implementados conferidos contra o escopo (troca de representante legal PJ na assinatura), sem pendência gerada.
- ⚠️ **Ambiente inferido como homologação** — é onde o Rafael validou hoje. Corrigir se foi em DEV.
- **Vizinhança**: a [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Cidadão PJ sem responsável legal vinculado (30/06/2026)|SGV de 30/06 (PJ sem responsável legal)]] atacou o outro lado do mesmo dado — lá o problema era PJ **sem** responsável legal seguir disponível pra assinar; aqui era o responsável **desatualizado** chegar no documento. Se mexerem nesse trecho de novo, os dois merecem reteste.
- Histórico:
    - 2026-07-17 - 📋 SGV-5783 - Batida na Triagem SP15 (critérios já definidos)
    - 2026-07-20 - 🔎 SGV-5783 - Análise (MR !581 revisado; escopo bate com a troca de representante legal PJ na assinatura)
    - 2026-07-30 - ✅ SGV-5783 - Aprovada em homologação (assinatura passa a levar o responsável legal atualizado)
