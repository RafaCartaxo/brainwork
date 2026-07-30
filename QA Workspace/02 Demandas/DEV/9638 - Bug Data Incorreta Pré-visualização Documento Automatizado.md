---
tags:
  - bug
  - qa
  - documentos-automatizados
task: "9638"
prioridade: alta
status: aberto
data_inicio: 2026-07-24
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documentos-automatizados
ambiente: DEV
---
# Data exibida incorretamente na pré-visualização de documento automatizado

### Descrição

Ao pré-visualizar um documento automatizado cujo campo está configurado para exibir a **data de abertura do documento gerado**, a data apresentada está incorreta: o sistema exibe a **data de criação do documento pai**, quando o correto seria a **data atual** (momento da pré-visualização). (Origem: Notion SGV-9638, dev Diogo Sobreira, Squad 1; correção no [MR !619](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/619).)

---

### Passo a passo para reproduzir

Dado que estou logado como servidor
E possuo um documento automatizado com o campo de data de abertura do documento gerado
Quando clico em pré-visualizar
Então a data exibida é a **da criação do documento pai** (incorreta)

---

### Resultado Esperado

Ao pré-visualizar um documento automatizado com a configuração de data de geração, o sistema exibe a **data atual**, correspondente ao momento da pré-visualização.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9638)

- Evidência local entra no fluxo normal quando houver validação em homologação.

---

### Critérios de aceite

- [ ] A data exibida na pré-visualização do documento automatizado corresponde à **data atual** no momento da visualização (não à data do documento pai)

---

### Casos de Teste Básicos

#### **CT-B01 Pré-visualização usa a data atual (não a do pai)**

**Dado** um documento automatizado com campo de data de abertura do documento gerado
**Quando** o servidor pré-visualiza o documento
**Então** a data exibida é a data atual (posterior à data de criação do documento pai)

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B02 Botão de pré-visualizar só em documentos automatizados**

**Dado** documentos automatizados e não automatizados
**Quando** o servidor abre a toolbar/ações do documento
**Então** o botão de pré-visualizar aparece **apenas** para documentos automatizados

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão: 12.27.25.2
- Ambiente: validação direto em homologação (task de sustentação; MR aprovado para testes — sem etapa de validação em DEV)

---

### Informações adicionais

- Demanda relacionada: SGV-9638 (origem Notion; Sprint SP15/SP16; dev Diogo Sobreira, Squad 1; revisores Washington Junior e Gabriel Desidério). Relacionada a SGV-7795 (melhoria de pré-visualização de documentos automatizados). Prioridade assumida `alta` (o resumo do Notion citava "alta criticidade" — corrigir se souber).
- **Escopo do MR !619** (revisão de 2026-07-24): o fix usa `createdAt: new Date()` no mock do documento automatizado da pré-visualização (em vez de herdar o `createdAt` do documento pai); além disso, torna o botão de pré-visualizar **condicional** (só para documentos automatizados) em `ClientDocumentPage.tsx`.
- Gate de doc (2026-07-24): não há doc de módulo dedicada a **documentos automatizados / pré-visualização** em `04 Conhecimento/Módulos/` (a de [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] trata de gerar-a-partir-de-outro, não do preview) — sem divergência; gap de doc registrado (candidato a criar doc "Documentos Automatizados" via fluxo 8; mesmo módulo do [[QA Workspace/02 Demandas/DEV/9963 - Bug Campos Dinâmicos Alteração Módulo|SGV-9963]]).
- Histórico:
    - 2026-07-24 - 📝 Bug importado do Notion (modo B, card direto do export) — descrição, passo a passo e critério de aceite já vinham completos
    - 2026-07-24 - 👍 [MR !619](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/619) **aprovado pela QA** no code review (nível de cenários — critério coberto 1:1, escopo bate, liberado). Não é validação funcional: teste real (data no preview + botão condicional) em HML depois. Card segue `aberto`.
    - 2026-07-24 - 🔎 Cenários de teste do [MR !619](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/619) (commit `6296a6eb`) revisados a nível de escopo — 2 cenários em `previewAutomatedDocument.test.ts` ("previewAutomatedDocument - data da pré-visualização (SGV-9638)"): (1) o `createdAt` do preview é **posterior** ao do pai e fica **dentro de 60s de agora** (prova que usa a data atual); (2) sanidade do mock do preview (não persiste: `id` undefined, `requesterId` null, privacidade padrão, `automatedDocumentModelId` setado). **Cruzamento**: o único critério de aceite ✅ coberto **1:1** pela cenário 1. **Achado**: o MR entrega **também** a correção do botão de pré-visualizar (só para automatizados) — fora do critério único do card, coberto por mudança de UI (`ClientDocumentPage.tsx`), **não** pelos cenários de API; validar essa visibilidade manualmente em HML (virou CT-B02). Cobertura da data é API/unit. Seguir pra validação real.
