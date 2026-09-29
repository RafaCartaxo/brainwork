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

Durante a validação real da SGV-11177 (Parte 4 da epic SGV-9296) foi identificado um efeito colateral da busca nova de departamento/membro sobre uma capacidade pré-existente: solicitar assinatura diretamente para um cidadão Pessoa Jurídica (a empresa, não um departamento nem um membro).

O componente de busca de destinatário/signatário retorna o resultado numa hierarquia única — `Cidadão PJ > Departamento > Membro` — e permite localizar o mesmo cidadão PJ tanto pesquisando diretamente pelo nome/CNPJ dele quanto pesquisando pelo nome de um departamento ou membro seu (a busca expande a hierarquia e devolve o cidadão PJ como parte do mesmo resultado). O caminho de busca não deveria mudar o resultado da seleção — mas muda: selecionar o cidadão PJ pela busca direta funciona normalmente; selecionar o **mesmo** cidadão PJ a partir de um resultado encontrado via departamento retorna erro de **"cadastro incompleto"**, mesmo o cidadão tendo cadastro completo (comprovado pelo caminho direto funcionar).

---

### Passo a passo para reproduzir

**Dado** que existe um cidadão PJ com ao menos um departamento cadastrado
**Quando** o servidor pesquisa diretamente pelo cidadão PJ e solicita a assinatura dele
**Então** a solicitação é aceita normalmente

**Dado** o mesmo cidadão PJ
**Quando** o servidor pesquisa pelo nome de um departamento ou membro desse cidadão PJ, e a partir da linha `Cidadão PJ > Departamento > Membro` retornada seleciona o cidadão PJ (não o departamento, não o membro)
**Então** verifico que o sistema retorna erro de cadastro incompleto, impedindo a solicitação — divergindo do resultado do caminho direto

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11910)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

### Resultado Esperado

Selecionar o cidadão PJ como signatário deve dar o mesmo resultado independentemente do caminho usado para localizá-lo — busca direta pelo cidadão PJ, ou busca por um departamento/membro seu com o cidadão PJ selecionado a partir da hierarquia expandida. Ver [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c33|C33]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-033|CT-033]].

---

### Critérios de aceite

- [ ] Selecionar o cidadão PJ a partir da busca direta aceita a solicitação de assinatura normalmente (comportamento já correto, preservar)
- [ ] Selecionar o mesmo cidadão PJ a partir do resultado expandido de um departamento/membro seu também aceita a solicitação normalmente, sem erro de cadastro incompleto
- [ ] O caminho de busca (direto vs. via departamento/membro) não interfere na validação de completude do cadastro do cidadão PJ

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura do cidadão PJ funciona igual nos dois caminhos de busca**

**Dado** que um cidadão PJ com departamento cadastrado é localizado pelos dois caminhos de busca (direto, e via departamento/membro)
**Quando** o servidor solicita assinatura pra esse cidadão PJ em cada um dos dois casos
**Então** os dois caminhos resultam na solicitação aceita normalmente, sem erro de cadastro incompleto em nenhum dos dois

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
- Observações: achado durante a validação real do pacote QA de SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-033|CT-033]] (critério C33 criado a partir deste achado, fora de sequência). Efeito colateral da busca nova de departamento/membro (RF01/C1) sobre uma capacidade pré-existente de assinatura direta pro cidadão PJ, não coberta por nenhum critério anterior a este achado.
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
