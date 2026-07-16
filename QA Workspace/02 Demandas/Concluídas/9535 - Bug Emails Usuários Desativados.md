---
tags:
  - bug
  - qa
  - email
  - notificacao
task: "9535"
prioridade: alta
status: resolvido
data_inicio: 2026-07-13
data_fim: 2026-07-14
responsavel: Rafael
modulo: notificacoes
ambiente: HML
---
# Usuários desativados recebem e-mails de notificação indevidos

### Descrição

Durante validação foi identificado que usuários desativados estavam recebendo notificações por e-mail que não deveriam receber, em dois cenários: (1) usuário mencionado/envolvido em despacho ou documento continuava recebendo e-mail de assinatura realizada, mesmo estando desativado; (2) administrador de módulo continuava recebendo e-mail de atualização do módulo, mesmo estando desativado. Corrigido e aprovado em homologação em 14/07.

---

### Passo a passo para reproduzir

Dado que exista um usuário desativado no sistema
E esse usuário esteja envolvido em um despacho/documento assinado, ou seja administrador de um módulo atualizado
Quando o evento (assinatura ou atualização de módulo) ocorrer
Então o usuário desativado não deve receber nenhum e-mail de notificação

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9535)

![[9535 - bloqueio de emails para usuários inativos aprovado.mp4]]

---

### Resultado Esperado

Usuários desativados não devem receber e-mails de notificação do sistema (assinatura de documentos em que estão envolvidos, atualização de módulos que administram), independente do tipo de evento. Usuários ativos devem continuar recebendo essas notificações normalmente.

---

### Critérios de aceite

- Usuário desativado mencionado/envolvido em despacho ou documento não deve receber e-mail quando o documento for assinado
- Administrador desativado não deve receber e-mail de atualização de módulo
- Usuários ativos devem continuar recebendo essas notificações normalmente (sem regressão)

---

### Casos de Teste Básicos

- **CT-B01 Bloquear e-mail de assinatura para usuário desativado envolvido em despacho/documento**
    - Dado que um usuário esteja desativado e mencionado/envolvido em um despacho ou documento
    - Quando esse despacho/documento for assinado
    - Então o usuário desativado não deve receber o e-mail de notificação de assinatura

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B02 Manter e-mail de assinatura para usuário ativo envolvido em despacho/documento**
    - Dado que um usuário esteja ativo e mencionado/envolvido em um despacho ou documento
    - Quando esse despacho/documento for assinado
    - Então o usuário ativo deve continuar recebendo o e-mail de notificação de assinatura normalmente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B03 Bloquear e-mail de atualização de módulo para administrador desativado**
    - Dado que um administrador de um módulo esteja desativado
    - Quando o módulo for atualizado
    - Então o administrador desativado não deve receber o e-mail de notificação de atualização

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B04 Manter e-mail de atualização de módulo para administrador ativo**
    - Dado que um administrador de um módulo esteja ativo
    - Quando o módulo for atualizado
    - Então o administrador ativo deve continuar recebendo o e-mail de notificação de atualização normalmente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
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

- Demanda relacionada: SGV-9535
- Observações:
- Histórico:
    - 2026-07-13 - 🚀 Início de validação
    - 2026-07-14 - ✅ Aprovada em homologação
