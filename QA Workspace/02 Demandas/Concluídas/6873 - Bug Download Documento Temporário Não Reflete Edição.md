---
tags:
  - bug
  - qa
  - documento
task: "6873"
prioridade: media
status: resolvido
data_inicio: 2026-07-24
data_fim: 2026-07-24
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Download de documento temporário não corresponde à versão editada

### Descrição

Ao baixar um documento temporário, o arquivo não refletia a **última edição** — mostrava a versão anterior. É a **correção da raiz comum** do problema compartilhado com [[QA Workspace/02 Demandas/Concluídas/6083 - Bug Edição Documento Não Atualiza Download Assinatura|SGV-6083]] e SGV-6348 (edição não refletida no download). (Origem Notion SGV-6873, Matheus Godoi, Squad 2, Sanidade-004; prioridade Média.)

---

### Resultado Esperado

Ao baixar um documento (inclusive temporário) após edição, o arquivo reflete o conteúdo atualizado (a versão vigente da edição).

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://6873)

- Sem cópia local: **aprovação por herança** (ver Histórico) — a validação funcional foi a da SGV-6083, que carrega o mesmo fix.

---

### Casos de Teste Básicos

#### **CT-B01 Download reflete a edição (documento temporário)**

**Dado** um documento temporário editado
**Quando** o servidor faz o download
**Então** o arquivo baixado reflete a última edição

**Execução Passou?**
- [x] Sim (por herança — mesmo fix validado na SGV-6083)
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: SGV-6873 (Matheus Godoi, Squad 2, Sanidade-004). Raiz comum com SGV-6083 e SGV-6348.
- **Rastreio da resolução (IMPORTANTE — aprovação por herança, não validação independente)**:
    - O fix da SGV-6873 (`fix/6873`, commits `4e04503a`/`1c16421e` — "corrige download de documento temporário que não refletia a edição") é a **correção da raiz comum**.
    - Ele foi **mergeado dentro do branch `fix/6083`** (`bd8d86a6 fix(SGV-6083): Merge branch 'fix/6873' into fix/6083`).
    - A **SGV-6083 foi validada e aprovada em homologação (2026-07-24) com esse fix incorporado** → o mesmo código que corrige a 6873 foi exercitado. Por isso a 6873 é dada como **aprovada por herança / coberta**, sem validação funcional independente do sintoma específico dela.
    - **MR da 6873**: superseded pelo merge no `fix/6083` — **fechada no GitLab (2026-07-24, Rafael)**. Se em algum momento quiser a prova direta do sintoma do 6873 (download de doc temporário), fazer um teste pontual em HML.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] não cobre "download refletir a edição" — sem divergência; gap de doc (fluxo 8, junto com 6083).
- Histórico:
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa; sem export completo)
    - 2026-07-24 - ✅ Resolvida **por herança**: fix da 6873 mergeado em `fix/6083` e validado via a aprovação da [[QA Workspace/02 Demandas/Concluídas/6083 - Bug Edição Documento Não Atualiza Download Assinatura|SGV-6083]] em homologação. Sem validação funcional independente; MR superseded pelo merge.
    - 2026-07-24 - 🔒 MR fechada no GitLab (superseded — o código já está em produção via `fix/6083`)
