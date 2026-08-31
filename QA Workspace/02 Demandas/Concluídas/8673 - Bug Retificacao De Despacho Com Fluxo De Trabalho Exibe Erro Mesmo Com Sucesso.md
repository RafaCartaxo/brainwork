---
tags:
  - bug
  - qa
  - despacho
task: "8673"
prioridade: ""
status: resolvido
data_inicio: 2026-08-20
data_fim: 2026-08-25
responsavel: Rafael
cadastrado_por: Rafael
modulo: despachos
ambiente: HML
---
# Retificação de despacho com fluxo de trabalho exibe erro mesmo quando é concluída com sucesso

### Descrição

Durante validação foi identificado que, ao retificar um despacho vinculado a um documento com **fluxo de trabalho**, o sistema **exibe uma mensagem de erro** — mas a retificação é **concluída com sucesso** mesmo assim.

> [!warning]- Card reaberto sem histórico local
> SGV-8673 está sendo **reaberta em homologação**, mas não há card anterior no vault — provavelmente só era acompanhada pelo Notion até agora. Este card nasce a partir da evidência gravada hoje e do que o Rafael relatou (reabertura, ambiente homologação); não tenho o histórico da ocorrência original nem a causa raiz anterior. Completar quando houver mais contexto.

---

### Passo a passo para reproduzir

Dado que existe um despacho já emitido, vinculado a um documento com fluxo de trabalho, criado por mim (retificação é restrita ao criador original — ver [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]])
Quando eu retifico esse despacho
Então o sistema exibe uma mensagem de erro
E verifico que a retificação foi concluída com sucesso mesmo assim (versionamento automático registrado, mudanças refletidas)

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://8673)

![[8673 - retificar doc fluxo de trabalho, retorna erro e retifica com sucesso..mp4]]

![[8673 - retificar doc com fluxo de trabalho ok.mp4]]

---

### Resultado Esperado

A retificação do despacho é concluída **sem exibir mensagem de erro** — o feedback da interface deve refletir corretamente que a ação teve sucesso.

> [!warning]- Gate de doc: pendente
> [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] documenta a regra de permissão da retificação (apenas o criador original) e o versionamento automático, mas não descreve o comportamento de feedback/mensagens de erro da ação. Não cruzado a fundo ainda — registrar quando houver mais detalhe do erro exibido.

---

### Critérios de aceite

- [x] Retificar um despacho com fluxo de trabalho **não exibe** mensagem de erro quando a ação é bem-sucedida
- [x] O versionamento automático continua sendo registrado corretamente (sem regressão)

---

### Casos de Teste Básicos

#### **CT-B01 Retificação de despacho com fluxo de trabalho não exibe erro falso**

**Dado** que existe um despacho emitido, com fluxo de trabalho, criado por mim
**Quando** eu retifico esse despacho
**Então** a retificação é concluída sem exibir mensagem de erro, e o versionamento reflete a mudança

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[8673 - retificar doc fluxo de trabalho, retorna erro e retifica com sucesso..mp4]]

![[8673 - retificar doc com fluxo de trabalho ok.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- **Relacionado**: [[QA Workspace/02 Demandas/Concluídas/5152 - Funcionalidade Cancelar E Retificar Despacho|SGV-5152]] — a funcionalidade de retificação de despacho é dessa entrega, já concluída. Este bug é sobre o comportamento em homologação, não um defeito da 5152 (não saiu da execução dos CTs dela).
- Observações:
    - Card criado hoje só com o que a evidência mostra e o relato de reabertura — sem mais contexto (mensagem de erro exata, se reproduz em todo tipo de despacho ou só nesse cenário, causa raiz). Completar conforme mais informação chegar.
- Histórico:
    - 2026-08-20 - 🔴 SGV-8673 - Reaberta em homologação (card criado agora no vault; retificação de despacho com fluxo de trabalho exibe erro mesmo tendo sucesso)
    - 2026-08-25 - 🔁 Retestada e aprovada em homologação (retificação de despacho com fluxo de trabalho não exibe mais o erro falso)
