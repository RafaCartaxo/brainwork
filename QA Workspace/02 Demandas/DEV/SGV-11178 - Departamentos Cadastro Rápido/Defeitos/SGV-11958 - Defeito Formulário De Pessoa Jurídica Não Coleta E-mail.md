---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11958"
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
# Formulário de Pessoa Jurídica não coleta e-mail

### Descrição

O critério [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda#^c15|C15]] da SGV-11178 foi atualizado em 01/10/2026 (protótipo no Figma já atualizado) pra exigir também o campo E-mail no formulário de cadastro rápido de Pessoa Jurídica, reduzindo a ocorrência de cadastros incompletos (ver [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]]). A implementação atual ainda não tem esse campo — [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/03 - Casos de teste#^ct-015|CT-015]] reprova contra o critério atualizado.

---

### Passo a passo para reproduzir

**Dado** que a opção Pessoa Jurídica esteja selecionada no cadastro rápido
**Quando** o formulário for exibido
**Então** o campo E-mail não aparece junto aos demais (CNPJ, Razão Social, Nome fantasia, Telefone, CPF do responsável legal, Nome do responsável legal)

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11958)

![[11958 - Campo e-mail PJ não tem no formulário, incorreto.png]]

---

### Resultado Esperado

Formulário de cadastro rápido de Pessoa Jurídica exibe o campo E-mail, conforme protótipo atualizado no Figma.

---

### Critérios de aceite

- [ ] Formulário de cadastro rápido de Pessoa Jurídica exibe o campo E-mail, junto aos 6 já existentes

---

### Casos de Teste Básicos

#### **CT-B01 Campo E-mail no formulário de PJ**

**Dado** que o formulário de cadastro rápido de Pessoa Jurídica seja exibido
**Quando** os campos forem carregados
**Então** deve aparecer o campo E-mail, junto aos 6 já existentes

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11958 - Campo e-mail PJ não tem no formulário, incorreto.png]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/01 - Demanda|SGV-11178]]
- Observações: detalhe adicional (obrigatoriedade do campo, validação, link do protótipo) registrado em comentário no Notion, não duplicado aqui.
- Histórico:
    - 2026-10-01 - 🐛 Defeito cadastrado (C15/CT-015 atualizados pra exigir e-mail, ainda não implementado)
