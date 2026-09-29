---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11910"
pai: "SGV-11177"
prioridade: media
status: aberto
data_inicio: 2026-09-29
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Assinatura do cidadão PJ falha quando localizado via departamento

### Descrição

Solicitar assinatura pro cidadão PJ funciona pela busca direta, mas exibe a tag "cadastro incompleto" quando o mesmo cidadão é achado via departamento ou membro (a busca retorna a hierarquia `Cidadão PJ > Departamento > Membro`). Mesmo cidadão, resultado diferente conforme o caminho.

---

### Passo a passo para reproduzir

**Dado** que existe um cidadão PJ com ao menos um departamento cadastrado
**Quando** o servidor pesquisa diretamente pelo cidadão PJ e solicita a assinatura dele
**Então** a solicitação é aceita normalmente

**Dado** o mesmo cidadão PJ
**Quando** o servidor pesquisa pelo nome de um departamento ou membro *desse* cidadão PJ, e a partir da linha `Cidadão PJ > Departamento > Membro`
**Então** o cidadão PJ (não o departamento, não o membro) verifico que o sistema retorna tag de cadastro incompleto, impedindo a solicitação.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11910)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

### Resultado Esperado

Mesmo resultado nos dois caminhos de busca (direto ou via departamento/membro). Ver [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c33|C33]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-033|CT-033]].

---

### Critérios de aceite

- [ ] Cidadão PJ aceita a solicitação de assinatura nos dois caminhos de busca (direto e via departamento/membro), sem a tag de cadastro incompleto

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura do cidadão PJ funciona igual nos dois caminhos de busca**

**Dado** que um cidadão PJ com departamento cadastrado é localizado pelos dois caminhos de busca (direto, e via departamento/membro)
**Quando** o servidor solicita assinatura pra esse cidadão PJ em cada um dos dois casos
**Então** os dois caminhos resultam na solicitação aceita normalmente, sem a tag de cadastro incompleto em nenhum dos dois

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

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação da SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-033|CT-033]] (critério C33, criado a partir deste achado).
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
