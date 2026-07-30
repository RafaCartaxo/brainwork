---
tags:
  - bug
  - qa
  - login
task: "5269"
prioridade: altíssima
status: resolvido
data_inicio: 2026-07-24
data_fim: 2026-07-24
responsavel: Rafael
cadastrado_por: ""
modulo: login
ambiente: HML
---
# Botão de recuperar senha não redireciona para o fluxo de esqueci senha

### Descrição

O botão de recuperar senha na tela de login não redirecionava para o fluxo de "esqueci minha senha". (Origem Notion SGV-5269, Matheus Godoi.)

---

### Resultado Esperado

Ao clicar no botão de recuperar senha, o usuário é redirecionado corretamente para o fluxo de "esqueci minha senha".

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://5269)

![[5269 - botao recuperar senha redireciona esqueci senha aprovado em homologacao.mp4]]

---

### Critérios de aceite

- [x] Botão de recuperar senha redireciona corretamente para o fluxo de esqueci senha

---

### Casos de Teste Básicos

#### **CT-B01 Botão de recuperar senha redireciona corretamente**

**Dado** a tela de login
**Quando** o usuário clica no botão de recuperar senha
**Então** é redirecionado para o fluxo de esqueci senha, sem erros

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[5269 - botao recuperar senha redireciona esqueci senha aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: SGV-5269 (origem Notion; Sprint SP15/SP16; Matheus Godoi). Notion: Disponível para homologação (Release homolog, 24/07) → aprovada por QA (24/07).
- ⚠️ **Suposição (corrija se precisar)**: ambiente assumido como **HML**, com base no status "Disponível para homologação" do Notion — não foi explicitado na sessão se o teste foi em DEV ou HML.
- Havia uma gravação anterior reprovada (`5269 - Botão recuperar senha nok.mp4`, em `Evidências/Desenvolvimento/`) de uma tentativa anterior — mantida, não apagada.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Login|Login]] não descreve o fluxo de recuperação/esqueci senha — sem divergência; gap de doc (fluxo 8, candidato a importar).
- Histórico:
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa da validação; sem export completo)
    - 2026-07-24 - ✅ Aprovada em homologação
