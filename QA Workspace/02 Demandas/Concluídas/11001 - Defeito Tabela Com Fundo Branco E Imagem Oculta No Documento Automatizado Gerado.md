---
tags:
  - defeito
  - qa
task: "11001"
pai: "7863"
prioridade: alta
status: resolvido
data_inicio: 2026-08-21
data_fim: 2026-08-26
responsavel: Rafael
cadastrado_por: ""
modulo: assinaturas
ambiente: DEV
---
# Tabela com fundo branco e imagem oculta no documento automatizado gerado

### Descrição

Durante validação da SGV-7863 (melhoria "Fundo do selo de documento automatizado deve ser transparente") foi identificado que o mesmo problema de fundo branco também afeta a tabela inserida no documento automatizado, e que há um segundo problema associado envolvendo imagem.

---

### Passo a passo para reproduzir

**Fundo branco na tabela**

Dado que insiro uma tabela em um documento automatizado
Quando gero o documento
Então verifico que a tabela é renderizada com fundo branco, em vez de fundo transparente

**Imagem oculta ao combinar com tabela**

Dado que insiro uma tabela e uma imagem em um documento automatizado
Quando gero o documento
Então verifico que apenas a tabela é exibida no arquivo gerado, e a imagem não é refletida

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://7863)

![[7863 - tabela com fundo branco e imagem oculta.png]]

![[7863 - tabela com fundo branco e imagem oculta 2.png]]

![[7863 - imagens não renderiza no gerado.mp4]]

---

### Resultado Esperado

- A tabela inserida no documento automatizado deve manter fundo transparente ao ser gerada, sem sobrepor conteúdo com fundo branco
- A imagem inserida junto com uma tabela no documento automatizado deve ser corretamente refletida no arquivo gerado

---

### Critérios de aceite

- [x] A tabela do documento automatizado gerado não exibe fundo branco
- [x] A imagem inserida junto com a tabela é exibida corretamente no documento automatizado gerado

---

### Casos de Teste Básicos

#### **CT-B01 Tabela com fundo transparente no documento automatizado gerado**

**Dado** que insiro uma tabela em um documento automatizado
**Quando** gero o documento
**Então** a tabela é exibida com fundo transparente, sem sobreposição de fundo branco

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[7863 - crop automatico e imagem fundo branco transparente ok.mp4]]

---

#### **CT-B02 Imagem exibida corretamente junto com tabela no documento automatizado gerado**

**Dado** que insiro uma tabela e uma imagem em um documento automatizado
**Quando** gero o documento
**Então** tanto a tabela quanto a imagem são exibidas corretamente no arquivo gerado

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[7863 - crop automatico e imagem fundo branco transparente ok.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: SGV-7863 — task pai, "[Melhoria] Fundo do selo de documento automatizado deve ser transparente"

- Observações:
    - Encontrado durante validação em DEV da SGV-7863. O problema de fundo branco tratado na melhoria (selo/carimbo) se estende à tabela do documento automatizado; e há um segundo problema, de mesma origem de teste, em que a imagem não é refletida quando combinada com tabela no documento gerado.
    - Evidências nomeadas com o número da SGV-7863 (capturadas durante a validação da task pai) — mantidas assim por já existirem no vault com esse número.
    - **Fechamento por reconciliação**: o Rafael confirmou a SGV-7863 (pai) finalizada, aprovada e já em produção. Os dois CTs foram marcados "Sim" por essa declaração final — não há evidência específica e separada por CT deste defeito, só a evidência compartilhada da pai (`7863 - crop automatico e imagem fundo branco transparente ok.mp4`).

- Histórico:
    - 2026-08-21 - 🐛 Defeito cadastrado (da SGV-7863)
    - 2026-08-26 - ✅ Defeito corrigido e retestado em DEV — fechado por reconciliação, já que a pai SGV-7863 foi confirmada aprovada e em produção
