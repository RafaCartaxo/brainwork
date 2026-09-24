---
tags:
  - defeito
  - qa
  - tramitacao
task: "11815"
pai: "SGV-9982"
prioridade: media
status: aberto
data_inicio: 2026-09-24
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: tramitacao
ambiente: DEV
---
# Preferência "Permanecer no documento após encerrar" é gravada ao cancelar o encerramento

### Descrição

Durante a validação do CT-009 do pacote QA de SGV-9982 foi identificado que, ao marcar o checkbox "Permanecer no documento após encerrar" e em seguida clicar em "Cancelar" (ou fechar o dialog sem confirmar), a ação faz a preferência persistir mesmo assim — ferindo o resultado esperado, que é a preferência só ser gravada na confirmação do encerramento.

---

### Passo a passo para reproduzir

**Dado** que o usuário abre qualquer um dos três dialogs de encerramento de tramitação (documento inteiro, setor ou participação própria)
**E** marca o checkbox "Permanecer no documento após encerrar"
**Quando** ele clica em "Cancelar" (ou fecha o dialog sem confirmar)
**Então** verifico que a preferência é gravada mesmo assim — a próxima abertura de qualquer um dos três dialogs já mostra o checkbox pré-marcado, mesmo sem o usuário ter confirmado nenhum encerramento

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11815)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

### Resultado Esperado

A preferência só deve ser gravada no momento da confirmação do encerramento (clicar em "Encerrar"). Cancelar ou fechar o dialog não deve alterar a preferência do usuário nem encerrar a tramitação — ver [[01 - Demanda#^c5|C5]] e [[03 - Casos de teste#^ct-009|CT-009]].

---

### Critérios de aceite

- [ ] Cancelar o dialog (com o checkbox marcado ou desmarcado) não altera a preferência de permanência já salva do usuário
- [ ] Fechar o dialog sem confirmar não altera a preferência de permanência já salva do usuário
- [ ] Cancelar ou fechar o dialog não encerra a tramitação

---

### Casos de Teste Básicos

#### **CT-B01 Cancelar após marcar o checkbox não grava a preferência**

**Dado** que o usuário abre um dos três dialogs de encerramento e marca o checkbox "Permanecer no documento após encerrar"
**Quando** ele clica em "Cancelar" (ou fecha o dialog sem confirmar)
**Então** a preferência não é gravada e a tramitação não é encerrada — o checkbox volta a refletir a preferência anterior à tentativa na próxima abertura

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

Pendência — nenhuma evidência anexada ainda.

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[01 - Demanda|SGV-9982]]
- Observações: achado durante a validação do pacote QA de SGV-9982 — [[03 - Casos de teste#^ct-009|CT-009]].
- Histórico:
    - 2026-09-24 - 🐛 Defeito cadastrado (da SGV-9982)
