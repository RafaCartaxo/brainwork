---
tags:
  - melhoria
  - qa
  - assinatura
task: "7371"
prioridade: media
status: resolvido
data_inicio: 2026-07-22
data_fim: 2026-07-22
responsavel: Rafael
modulo: assinaturas
ambiente: HML
---
# [Melhoria] Alterar URL de validação de assinatura para não expor código

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** Concluída
> - **Responsável QA:** Rafael
> - **Link:**

---

> [!abstract] Resumo

Melhoria no módulo Assinaturas: a URL de validação de assinatura passou a não expor o código de validação. Aprovada em homologação.

---

### Descrição

A URL usada para validar uma assinatura expunha o código de validação diretamente. A melhoria altera essa URL para que o código não fique exposto. Validado e aprovado em homologação.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://7371)

![[7371 - alterar url validacao assinatura nao expor codigo aprovado em homologacao.mp4]]

---

### Resultado Esperado

A URL de validação de assinatura não deve expor o código de validação.

---

### Critérios de aceite

- [x] A URL de validação de assinatura não expõe o código de validação

---

### Casos de Teste Básicos

- **CT-B01 URL de validação de assinatura não expõe o código**
    Dado que uma assinatura seja realizada
    Quando a URL de validação da assinatura for acessada/exibida
    Então o código de validação não deve estar exposto na URL

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes: ![[7371 - alterar url validacao assinatura nao expor codigo aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-7371
- Observações: Card criado em modo enxuto (relato rápido) — descrição destilada do título, sem passo a passo técnico detalhado disponível. Gate de doc: [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|doc de Assinaturas]] conferida — não descreve a URL de validação de assinatura nem exposição do código; sem divergência com o comportamento aprovado.
- Histórico:
    - 2026-07-22 - 💡 Melhoria cadastrada
    - 2026-07-22 - ✅ Aprovada em HML (Rafael)
