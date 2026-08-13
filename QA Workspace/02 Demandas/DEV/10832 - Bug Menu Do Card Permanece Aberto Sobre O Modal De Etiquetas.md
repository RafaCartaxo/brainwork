---
tags:
  - bug
  - qa
  - etiquetas
task: "10832"
prioridade: alta
status: aberto
data_inicio: 2026-08-13
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: etiquetas
ambiente: DEV
---
# Menu do card permanece aberto sobre o modal de etiquetas ao acionar "Etiqueta >" pela Mesa

### Descrição

Durante validação foi identificado que, ao acionar **"Etiqueta >"** pelo meatball do card na Mesa de Trabalho, o menu de contexto do card **permanece aberto por cima do modal de Etiquetas**, sobrepondo-o — em vez de fechar quando o modal abre, ele fica sobre o painel e pode cobrir seus elementos.

---

### Passo a passo para reproduzir

**Dado** que eu acesso a mesa de trabalho
**Quando** verifico um documento e clico na meatball do card
**E** clico no botão **"Etiqueta >"**
**Então** verifico que ele permanece aberto **por cima do modal de Etiquetas**

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10832)

![[10832 - meetball etiquetas modal permanece aberto.mp4]]


---

### Resultado Esperado

- Ao acionar **"Etiqueta >"**, o menu de contexto do card **fecha** e o modal de Etiquetas abre por cima, **sem sobreposição** — todos os elementos do modal ficam visíveis e clicáveis.

---

### Critérios de aceite

- [ ] Ao acionar "Etiqueta >" pelo meatball do card, o menu de contexto **fecha** e o modal de Etiquetas abre **totalmente visível e acessível**, sem sobreposição

---

### Casos de Teste Básicos

#### **CT-B01 Menu do card fecha ao abrir o modal de etiquetas**

**Dado** que eu acesso a mesa de trabalho
**E** abro o meatball de um documento do card
**Quando** clico no botão **"Etiqueta >"**
**Então** o menu de contexto **fecha** e o modal de Etiquetas abre por cima, totalmente visível e acessível, sem sobreposição

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão: 12.38.39.2
- Ambiente: Desenvolvimento (`dev-lucas-cabral`)

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] — achado na validação da refatoração de etiquetas em DEV.
    
- Observações:
    - ✅ **Fechou o Defeito 7** do card agrupado [[QA Workspace/02 Demandas/DEV/Defeitos 3234 - Refatoracao De Etiquetas|Defeitos 3234]] como **duplicata deste card** (reconciliado em 13/08/2026): mesmo ponto de entrada — o meatball/ellipsis do card na Mesa — e mesmo sintoma (menu não fecha ao abrir o painel de etiquetas). O registro lá fica como referência; a correção é deste ticket.
    - ⚠️ Os subitens da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]] estão em 87,50% e não vieram no export — este achado pode ser algo que **ainda não subiu**. Confirmar antes de tratar como bug fechado.

- Histórico:
    - 2026-08-13 - 🐛 Bug cadastrado (SGV-10832; achado na validação da [[QA Workspace/02 Demandas/DEV/3234 - Melhoria Refatoracao De Etiquetas|SGV-3234]])