---
tags:
  - bug
  - qa
  - assinatura
task: "11047"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-24
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: assinatura
ambiente: HML
---
# Link de verificação de assinaturas também ignora a página extra de assinaturas

### Descrição

Durante a validação da [[QA Workspace/02 Demandas/Concluídas/10404 - Bug Download Assinaturas Autenticaveis Ignora Pagina Extra Assinaturas|SGV-10404]] foi identificado que, apesar do download da versão com assinaturas autenticáveis já respeitar a página extra de assinaturas, o **link de verificação de assinaturas** também não respeita essa configuração — mesmo problema de fundo, superfície diferente.

Evidência compartilhada com a SGV-10404 (mesmo vídeo, cópia renomeada) — **o trecho entre 4min e 5min** mostra o achado.

---

### Passo a passo para reproduzir

Dado que eu tenho um cliente com documento com a função de assinatura em página extra ativada
E assino o documento
Quando clico no link de verificação de assinaturas
Então verifico que a página extra de assinaturas não é respeitada

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11047)

![[11047 - link verificacao assinaturas ignora pagina extra.mp4]]

---

### Resultado Esperado

- O link de verificação de assinaturas respeita a configuração de assinatura em página extra, do mesmo jeito que o download já passou a respeitar após a correção da SGV-10404

---

### Critérios de aceite

- [ ] Ao clicar no link de verificação de assinaturas, a página extra de assinaturas é exibida/considerada corretamente

---

### Casos de Teste Básicos

#### **CT-B01 Link de verificação de assinaturas respeita a página extra**

**Dado** que eu tenho um cliente com documento com a função de assinatura em página extra ativada
**E** assino o documento
**Quando** clico no link de verificação de assinaturas
**Então** verifico que a página extra de assinaturas é respeitada

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[11047 - link verificacao assinaturas ignora pagina extra.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-11047 (Notion). Achado durante a validação/aprovação da [[QA Workspace/02 Demandas/Concluídas/10404 - Bug Download Assinaturas Autenticaveis Ignora Pagina Extra Assinaturas|SGV-10404]] em 24/08.
- Observações:
    - Evidência compartilhada com [[QA Workspace/02 Demandas/Concluídas/10404 - Bug Download Assinaturas Autenticaveis Ignora Pagina Extra Assinaturas|SGV-10404]] — mesmo vídeo, cópia renomeada. **Trecho de 4min a 5min** é onde o achado aparece.
    - Mesma área de regra documentada da SGV-10404 ([[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas § Página extra de assinaturas]]: "a página extra não é apenas visual; ela se torna parte integrante do arquivo PDF") — vale conferir se o link de verificação usa o mesmo caminho de renderização problemático.
- Histórico:
    - 2026-08-24 - 🐛 SGV-11047 - Bug cadastrado (achado durante validação da SGV-10404)
