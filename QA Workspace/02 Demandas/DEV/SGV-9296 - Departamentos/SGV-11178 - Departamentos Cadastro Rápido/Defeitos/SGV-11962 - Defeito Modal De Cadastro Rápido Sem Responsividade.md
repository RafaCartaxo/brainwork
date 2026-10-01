---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11962"
pai: "SGV-11178"
prioridade: media
status: aberto
data_inicio: 2026-10-01
data_fim:
responsavel:
aguardando: dev
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Modal de cadastro rápido sem responsividade

### Descrição

O critério [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda#^c38|C38]] da SGV-11178 foi criado em 01/10/2026 (protótipo no Figma já definido) exigindo que o modal de cadastro rápido — o que abre ao clicar em "+Novo cadastro", com o seletor Pessoa Física/Pessoa Jurídica/Departamento e os formulários — seja responsivo em telas menores (mobile). A implementação atual quebra/não tem responsividade — [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-038|CT-038]] reprova contra o critério novo.

**Protótipo:** [Figma — Refatoração Pessoa Jurídica (Interno/Externo)](https://www.figma.com/design/fgpK9HLfUsaQJm6vx9iocF/Refatora%C3%A7%C3%A3o-Pessoa-Jur%C3%ADdica--Interno---Externo-?node-id=1361-2992)

---

### Passo a passo para reproduzir

**Dado** que o modal de cadastro rápido esteja aberto (atalho "+Novo cadastro")
**Quando** acessado em uma tela menor (mobile)
**Então** o layout quebra, sem a adaptação prevista no protótipo

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11962)

![[SGV-11962 - Responsividade, incorreto.mp4]]

---

### Resultado Esperado

Modal de cadastro rápido responsivo em telas menores, conforme o protótipo mobile do Figma.

---

### Critérios de aceite

- [ ] Modal de cadastro rápido se adapta corretamente a telas menores (mobile), conforme o protótipo Figma

---

### Casos de Teste Básicos

#### **CT-B01 Responsividade do modal de cadastro rápido**

**Dado** que o modal de cadastro rápido seja aberto
**Quando** acessado em uma tela menor (mobile)
**Então** o layout deve se adaptar corretamente, sem quebra, conforme o protótipo Figma

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[SGV-11962 - Responsividade, incorreto.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda|SGV-11178]]
- Observações: detalhe adicional (breakpoints, comportamento específico por campo) fica no próprio protótipo Figma vinculado, não duplicado aqui.
- Histórico:
    - 2026-10-01 - 🐛 Defeito cadastrado (C38/CT-038 criados pra exigir responsividade, ainda não implementada)
