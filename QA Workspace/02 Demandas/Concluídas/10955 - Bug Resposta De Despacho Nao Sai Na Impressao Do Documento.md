---
tags:
  - bug
  - qa
  - documento
task: "10955"
prioridade: alta
status: resolvido
data_inicio: 2026-08-19
data_fim: "2026-08-25"
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Resposta de despacho não sai na impressão do documento

### Descrição

Durante validação foi identificado que, quando o cidadão realiza uma resposta em um despacho, essa resposta **não aparece na impressão do documento**.

Encontrado durante a validação em homologação da [[QA Workspace/02 Demandas/Concluídas/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]] — não tem relação com aquele bug, é um achado à parte na mesma sessão de teste.

---

### Passo a passo para reproduzir

Dado que existe um documento com um despacho
E que o cidadão responde a esse despacho
Quando alguém abre o documento e aciona a impressão
Então verifico que a resposta do despacho não aparece no documento impresso

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10955)

![[10955 - resposta do despacho nao sai na impressao do documento.mp4]]

![[10955 - resposta cidadão visivel no download.mp4]]

---

### Resultado Esperado

A resposta do despacho aparece na impressão do documento, junto com o restante do conteúdo/andamento do processo.

> [!warning]- Gate de doc: lacuna, não confirmação
> Cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] e [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] em 19/08 — nenhuma das duas afirma explicitamente que todo despacho de resposta deve entrar na impressão do documento. A Despachos.md só trata o **inverso** (quando um despacho **não** deve aparecer: sigiloso sem permissão, cancelado leva tarja) — não define a regra positiva de que respostas normais devem aparecer. A regra mais próxima é a de Gerar Documento (linha 34: "documentos gerados a partir de outro devem... ser exibidos na íntegra"), mas essa trata de documentos gerados via a funcionalidade "Gerar documento", não de despachos — não sustenta o critério sozinho.
>
> Registrado como **pendência de documentação** (fluxo 8): quando a regra for confirmada com produto, ela entra na doc do módulo certo.

---

### Critérios de aceite

- [x] A resposta do cidadão a um despacho aparece na impressão do documento
- [ ] O comportamento vale independente de quem respondeu (cidadão ou servidor) — a verificar se o defeito é geral ou específico do fluxo do cidadão
- [ ] A resposta aparece na posição cronológica correta, junto ao despacho original

---

### Casos de Teste Básicos

#### **CT-B01 Resposta de despacho do cidadão aparece na impressão do documento**

**Dado** que existe um documento com um despacho
**E** o cidadão responde a esse despacho
**Quando** o documento é impresso
**Então** verifico que a resposta aparece na impressão do documento

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10955 - resposta cidadão visivel no download.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/Concluídas/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]] — achado incidental durante a validação em homologação daquele bug, sem relação de causa

- Observações:
    - Evidência compartilhada com [[QA Workspace/02 Demandas/Concluídas/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]] — mesmo vídeo, cópia renomeada
    - Aprovado pelo fluxo do **cidadão** (critério 1). **Critério 2 (resposta de servidor) e critério 3 (posição cronológica) não foram retestados especificamente** nesta rodada — a evidência `10955 - resposta cidadão visivel no download.mp4` cobre só o cenário do cidadão.

- Histórico:
    - 2026-08-19 - 🐛 Bug cadastrado (achado durante a validação em homologação da [[QA Workspace/02 Demandas/Concluídas/10512 - Bug CNPJ Do Cidadao PJ Exibido Anonimizado Na Impressao Do Documento|SGV-10512]])
    - 2026-08-25 - ✅ Aprovada em homologação (resposta do cidadão passou a aparecer na impressão do documento)
    - 2026-08-25 - ✅ Aprovada em homologação
