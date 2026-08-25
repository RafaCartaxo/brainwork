---
tags:
  - bug
  - qa
  - despachos
  - usuario-cidadao
task: "11080"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-25
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: despachos
ambiente: HML
---
# Destinatário da resposta exibe "undefined" a partir da segunda resposta

### Descrição

Durante validação foi identificado que, ao acessar o ambiente como cidadão e realizar 2 ou mais respostas a um documento, a primeira resposta exibe o destinatário correto ("Para: Gabinete do Prefeito e envolvidos", igual ao do despacho), mas a partir da segunda resposta o destinatário aparece como "Para: undefined e envolvidos" — o setor não está sendo herdado corretamente do despacho a partir da segunda resposta em diante.

---

### Passo a passo para reproduzir

Dado que eu acesso o ambiente como cidadão
E crio um documento
Quando realizo 2 respostas ou mais a esse documento
Então verifico que a primeira resposta mostra o destinatário correto "Para: Gabinete do Prefeito e envolvidos", igual ao do despacho
E que, a partir da segunda resposta, o destinatário aparece como "Para: undefined e envolvidos"

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11080)

![[11080 - despacho destinatario undefined na impressão.mp4]]

---

### Resultado Esperado

Todas as respostas herdam corretamente o setor do despacho original no destinatário — o destinatário deve ser exibido de forma consistente ("Para: Gabinete do Prefeito e envolvidos") em todas as respostas, não só na primeira.

---

### Critérios de aceite

- [ ] A partir da segunda resposta, o destinatário exibe o nome do setor corretamente, não "undefined"
- [ ] O destinatário de todas as respostas é consistente com o despacho original

---

### Casos de Teste Básicos

#### **CT-B01 Destinatário das respostas herda corretamente o setor do despacho**

**Dado** que eu acesso o ambiente como cidadão
**E** crio um documento
**Quando** realizo 2 respostas ou mais a esse documento
**Então** todas as respostas exibem o destinatário correto, herdado do despacho, sem "undefined" a partir da segunda

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[11080 - despacho destinatario undefined na impressão.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação (inferido — mesma sessão de validação das SGV-8673/SGV-11079; confirmar se foi em outro ambiente)

---

### Informações adicionais

- Demanda relacionada: SGV-11080 (Notion)
- Observações:
    - Nome do arquivo de evidência menciona "na impressão" — vale confirmar se o defeito aparece só no documento impresso/baixado ou também na tela, ao acompanhar a correção.
- Histórico:
    - 2026-08-25 - 🐛 SGV-11080 - Bug cadastrado
