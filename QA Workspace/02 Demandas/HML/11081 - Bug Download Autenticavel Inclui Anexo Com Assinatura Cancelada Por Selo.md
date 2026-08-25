---
tags:
  - bug
  - qa
  - assinatura
  - selo
task: "11081"
pai: ""
prioridade: alta
status: aberto
data_inicio: 2026-08-25
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: assinatura
ambiente: HML
---
# Download da versão com assinaturas autenticáveis inclui anexo com assinatura cancelada por selo

### Descrição

Durante validação foi identificado que, ao gerar um documento modelo automatizado e usá-lo como selo sobre um anexo PDF já assinado (assinatura para revisão) em um documento do tipo urbanístico, o sistema **corretamente** cancela a assinatura do anexo e exibe a mensagem de cancelamento — comportamento esperado, sem regressão nesse ponto.

Porém, dois problemas foram identificados na sequência:
1. O botão **"baixar versão com assinaturas autenticáveis"** continua disponível mesmo depois de a assinatura do anexo ter sido cancelada;
2. O **anexo com o selo aplicado** — cuja assinatura foi cancelada — também é incluído no download dessa versão, quando não deveria estar disponível/incluído sem uma assinatura válida.

---

### Passo a passo para reproduzir

Dado que crio um documento do tipo urbanístico com anexo PDF
E assino o anexo para revisão
Quando gero um documento modelo automatizado e uso como selo no anexo assinado
Então verifico que o sistema retorna mensagem de que a assinatura foi cancelada, e a assinatura é de fato cancelada
E verifico que o botão de baixar versão com assinaturas autenticáveis continua disponível
E verifico que o anexo com o selo aplicado (assinatura cancelada) também vem incluído nesse download

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11081)

![[11081 - baixar documento autenticavel está baixando doc com selo e assinatura cancelada.mp4]]

---

### Resultado Esperado

- O cancelamento da assinatura do anexo pelo selo continua funcionando (mensagem + efeito) — sem regressão
- Depois que a assinatura do anexo é cancelada, o botão "baixar versão com assinaturas autenticáveis" não deve permanecer disponível pra esse anexo/documento sem assinatura válida
- O anexo com assinatura cancelada não deve ser incluído no download da versão com assinaturas autenticáveis

> [!warning]- Gate de doc: pendente
> Não existe ainda módulo **Selos** importado em `04 Conhecimento/Módulos/` (gap já registrado na fila) — sem doc oficial pra cruzar a regra de disponibilidade do botão e composição do download depois do cancelamento por selo. Registrar quando a doc for importada.

---

### Critérios de aceite

- [ ] Depois que o selo cancela a assinatura do anexo, o botão "baixar versão com assinaturas autenticáveis" não fica mais disponível pra esse anexo/documento sem assinatura válida
- [ ] O anexo com assinatura cancelada não é incluído no download da versão com assinaturas autenticáveis
- [ ] O cancelamento da assinatura do anexo pelo selo (mensagem + efeito) continua correto, sem regressão

---

### Casos de Teste Básicos

#### **CT-B01 Selo cancela assinatura do anexo, mas download autenticável ainda oferece o anexo cancelado**

**Dado** que crio um documento do tipo urbanístico com anexo PDF
**E** assino o anexo para revisão
**Quando** gero um documento modelo automatizado e uso como selo no anexo assinado
**Então** o sistema cancela a assinatura do anexo corretamente (mensagem + efeito)
**E** verifico que o botão de baixar versão com assinaturas autenticáveis não deveria ficar disponível, mas continua
**E** verifico que o anexo com assinatura cancelada não deveria vir no download, mas vem

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[11081 - baixar documento autenticavel está baixando doc com selo e assinatura cancelada.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação (inferido — mesma sessão de validação das SGV-8673/SGV-11079/SGV-11080; confirmar se foi em outro ambiente)

---

### Informações adicionais

- Demanda relacionada: SGV-11081 (Notion)
- Observações:
    - Mesma área da SGV-8867 (melhoria sobre comportamento de selo em anexo assinado, sem card local no vault) — vale conferir se este achado se relaciona com a regra definida naquela entrega antes de tratar como causa raiz nova.
- Histórico:
    - 2026-08-25 - 🐛 SGV-11081 - Bug cadastrado
