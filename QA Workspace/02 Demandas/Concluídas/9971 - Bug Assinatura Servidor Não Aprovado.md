---
tags:
  - bug
  - qa
  - assinatura
  - servidor
task: "9971"
prioridade: alta
status: resolvido
data: 2026-07-13
responsavel: Rafael
modulo: assinatura-digital
data_inicio: 2026-07-13
data_fim: "2026-08-26"
ambiente: HML
---
# Sistema permite solicitar assinatura para servidor com cadastro "A aprovar"

### Descrição

Durante validação foi identificado que o sistema permite solicitar assinatura para um servidor cujo cadastro ainda está na situação "A aprovar". Ao selecionar esse servidor na solicitação de assinatura, nenhum indicador de cadastro incompleto é exibido e a solicitação é concluída normalmente, como se o cadastro estivesse aprovado.

---

### Passo a passo para reproduzir

Dado que o usuário acesse o ambiente como servidor
E exista um usuário com cadastro na situação "A aprovar"
Quando o usuário solicitar assinatura para esse usuário
Então o sistema deve exibir o badge de cadastro incompleto e impedir a conclusão da solicitação

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9971)

![[9971 - solicitar assinatura para servidor com cadastro incompleto.mp4]]

![[9971 - nao solicita assinatura para servidor com status a aprovar ok.mp4]]

---

### Resultado Esperado

O sistema não deve permitir concluir a solicitação de assinatura para servidores com cadastro na situação "A aprovar". Ao tentar selecionar um servidor nessa condição, deve ser exibido o badge de cadastro incompleto.

---

### Critérios de aceite

- [x] Servidores com cadastro "A aprovar" não devem estar disponíveis para solicitação de assinatura
- [ ] Deve ser exibido o badge de cadastro incompleto ao tentar selecionar um servidor nessa situação
- [ ] Após a aprovação do cadastro, o servidor deve passar a ficar disponível normalmente para solicitação de assinatura

---

### Casos de Teste Básicos

#### **CT-B01 Bloquear solicitação de assinatura para servidor com cadastro "A aprovar"**

**Dado** que exista um servidor com cadastro na situação "A aprovar"
**E** o usuário esteja solicitando assinatura em um documento
**Quando** o usuário buscar/selecionar esse servidor para a solicitação de assinatura
**Então** o sistema deve exibir o badge de cadastro incompleto e o servidor não deve estar disponível para solicitação de assinatura

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

![[9971 - nao solicita assinatura para servidor com status a aprovar ok.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-9971
- Observações:
    - Validar também o reaproveitamento de solicitações de assinatura já existentes para o mesmo servidor.
    - A evidência do reteste (`9971 - nao solicita assinatura para servidor com status a aprovar ok.mp4`) confirma diretamente o critério 1 (servidor "a aprovar" não fica disponível). Critérios 2 (badge de cadastro incompleto) e 3 (disponibilidade após aprovação) não foram confirmados especificamente por essa evidência — CT-B01 deixado sem marcação por cobrir os dois em conjunto.
- Histórico:
    - 2026-07-13 - 🐛 Bug cadastrado
    - 2026-08-26 - ✅ Aprovada em homologação (servidor com cadastro "a aprovar" não fica mais disponível para solicitação de assinatura)
