---
tags:
  - bug
  - qa
  - assinatura
  - servidor
task: "9971"
prioridade: alta
status: aberto
data: 2026-07-13
responsavel: Rafael
modulo: assinatura-digital
data_inicio: 2026-07-13
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

---

### Resultado Esperado

O sistema não deve permitir concluir a solicitação de assinatura para servidores com cadastro na situação "A aprovar". Ao tentar selecionar um servidor nessa condição, deve ser exibido o badge de cadastro incompleto.

---

### Critérios de aceite

- Servidores com cadastro "A aprovar" não devem estar disponíveis para solicitação de assinatura
- Deve ser exibido o badge de cadastro incompleto ao tentar selecionar um servidor nessa situação
- Após a aprovação do cadastro, o servidor deve passar a ficar disponível normalmente para solicitação de assinatura

---

### Casos de Teste Básicos

- **CT-B01 Bloquear solicitação de assinatura para servidor com cadastro "A aprovar"**
    - Dado que exista um servidor com cadastro na situação "A aprovar"
    - E o usuário esteja solicitando assinatura em um documento
    - Quando o usuário buscar/selecionar esse servidor para a solicitação de assinatura
    - Então o sistema deve exibir o badge de cadastro incompleto e o servidor não deve estar disponível para solicitação de assinatura

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

---

### Ambiente

- Versão:
    
- Ambiente: Homologação
    
- Navegador:
    
- Sistema Operacional:
    

---

### Informações adicionais

- Demanda relacionada: SGV-9971
- Observações: Validar também o reaproveitamento de solicitações de assinatura já existentes para o mesmo servidor.
- Histórico:
    - 2026-07-13 - 🐛 Bug cadastrado
