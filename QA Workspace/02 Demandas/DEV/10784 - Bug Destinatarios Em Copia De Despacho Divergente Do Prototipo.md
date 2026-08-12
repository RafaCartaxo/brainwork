---
tags:
  - bug
  - qa
  - despacho
task: "10784"
prioridade: media
status: aberto
data_inicio: 2026-08-12
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: despacho
ambiente: DEV
---
# Destinatários em cópia de despacho divergente do protótipo

### Descrição

Durante validação foi identificado que a linha de **destinatários em cópia** do despacho está divergente do protótipo.

O protótipo prevê `com cópia para (N)` — texto com a **quantidade** de destinatários e **chevron para expandir**, no mesmo tratamento do elemento irmão `e mais N destinatário(s)` da linha de destinatários. O produto exibe `Com cópia para` seguido de **ícone de grupo e avatares empilhados**, sem número e sem chevron.

Na prática, o usuário **não consegue saber quantos setores estão em cópia** nem identificar que aquele elemento é expansível.

---

### Passo a passo para reproduzir

Dado que eu acesso um documento como **Servidor**
Quando realizo um **despacho** com setores em cópia
Então verifico que a linha de destinatários em cópia diverge do protótipo: exibe avatares empilhados, sem a quantidade e sem o chevron de expandir

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10784)

**Comportamento atual (incorreto):**

![[10784 - atual incorreto.png]]

**Protótipo (esperado):**

![[10784 - prototipo correto.png]]

---

### Resultado Esperado

- A linha de cópia exibe **`com cópia para (N)`**, com a quantidade de destinatários em cópia
- A linha de cópia tem **chevron de expandir**, no mesmo tratamento de link do elemento irmão `e mais N destinatário(s)`
- Ao expandir, os destinatários em cópia ficam visíveis

---

### Critérios de aceite

- [ ] A linha de cópia informa **quantos** destinatários estão em cópia, sem exigir nenhuma interação
- [ ] A linha de cópia indica visualmente que é **expansível**, como o `e mais N destinatário(s)` da linha acima
- [ ] Ao acionar a linha de cópia, os destinatários em cópia são **exibidos**
- [ ] A linha de cópia e o `e mais N destinatário(s)` têm o **mesmo tratamento visual** entre si — hoje um é link e o outro é texto estático com avatares

---

### Casos de Teste Básicos

#### **CT-B01 Linha de cópia exibe a quantidade de destinatários**

**Dado** que eu acesso um documento como **Servidor**
**E** o despacho tem setores em cópia
**Quando** eu observo a linha de destinatários em cópia
**Então** verifico que ela informa **quantos** destinatários estão em cópia, no formato `com cópia para (N)`, sem exigir interação

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10784 - atual incorreto.png]]

---

#### **CT-B02 Linha de cópia é expansível e lista os destinatários**

**Dado** que eu acesso um documento como **Servidor**
**E** o despacho tem setores em cópia
**Quando** eu observo a linha de cópia e a aciono
**Então** verifico que ela indica ser expansível (chevron, no mesmo tratamento do `e mais N destinatário(s)`) e que, ao ser acionada, exibe os destinatários em cópia

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10784 - atual incorreto.png]]
*Mesma evidência do CT-B01; comparar com `10784 - prototipo correto.png`.*

---

### Ambiente

- Versão: **12.39.44.2**
- Ambiente: Desenvolvimento — **posição na esteira de correção**. O defeito foi identificado em **homologação e em produção**; o card nasce em `DEV/` por ser bug novo ainda não corrigido em nenhum ambiente ([[Sistema/Contexto/PADROES_QA#Organização de Bugs|PADROES_QA]]).

---

### Informações adicionais

- Demanda relacionada:
- Observações:
    - **Não é regressão da 12.39.44.2**: o defeito aparece **em homologação e em produção**, ou seja, é pré-existente. Isso reduz a urgência de release e muda onde o dev procura.
    - **Escopo é só o despacho.** A criação de documento com setores em cópia foi conferida e **não apresenta a divergência** — por isso ficou fora do card.
    - O elemento irmão `e mais N destinatário(s)`, na linha de destinatários, **já segue o padrão** (contador + chevron). Isso sugere que o componente de cópia não foi alinhado ao mesmo padrão, e não que o padrão inteiro esteja errado.
    - 🔎 **Observação fora de escopo, a confirmar**: comparando as duas imagens, o `e mais N` do produto também parece não trazer a palavra *"destinatário(s)"* nem o tratamento de link azul que o protótipo mostra. Não foi validado nesta rodada e **não entrou nos critérios** — mas se for confirmado, é a mesma família de divergência.
    - Mesma tela da [[QA Workspace/02 Demandas/DEV/10740 - Bug Divergencias De Prototipo Na Exibicao Do Despacho|SGV-10740]] (divergências de protótipo na exibição do despacho) — vale tratar as duas na mesma passada de ajuste.
- Histórico:
    - 2026-08-12 - 🐛 Bug cadastrado (identificado em homologação e produção, versão 12.39.44.2)
