---
tags:
  - bug
  - qa
  - assinatura
task: "9959"
prioridade: media
status: resolvido
data_inicio: 2026-07-10
data_fim: 2026-07-23
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
---
# Inconsistência de status entre drawer de solicitação e evento de assinatura após recusa em assinatura sequencial

### Descrição

Em fluxo de **assinatura sequencial**, ao recusar uma assinatura, o status exibido no **drawer de solicitação** ficava inconsistente com o status do **evento de assinatura** — a recusa/cancelamento das assinaturas pendentes posteriores não se refletia de forma coerente entre as duas visões. Bug do módulo Assinaturas (Assinatura Sequencial), cadastrado a partir da análise de 10/07 (João Marcelo, Squad 3). Correção validada e aprovada em homologação.

---

### Resultado Esperado

Ao recusar uma assinatura num fluxo sequencial, as assinaturas pendentes posteriores são canceladas, e o status fica **consistente** entre o drawer de solicitação e o evento de assinatura. Após o cancelamento, é possível criar nova solicitação para os mesmos servidores e assiná-la normalmente, preservando o histórico de recusa/cancelamento da solicitação anterior.

---

### Critérios de aceite

- [x] Ao recusar uma assinatura em fluxo sequencial, todas as assinaturas pendentes posteriores são canceladas
- [x] Após o cancelamento, é possível criar nova solicitação de assinatura para os mesmos servidores
- [x] A nova solicitação pode ser assinada normalmente, sem bloqueios decorrentes do cancelamento anterior
- [x] O evento da solicitação anterior preserva o histórico de recusa/cancelamento, independentemente de novas solicitações criadas

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9959)

- Validação aprovada em homologação (2026-07-23):

![[9959 - status drawer x evento apos recusa assinatura sequencial aprovado em homologacao.mp4]]

---

### Casos de Teste Básicos

- **CT-B01 Cancelar assinaturas pendentes ao recusar assinatura em fluxo sequencial**
    Dado que exista uma solicitação de assinatura sequencial com múltiplos servidores
    Quando um servidor recusar sua assinatura
    Então as assinaturas pendentes dos servidores posteriores devem ser canceladas

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9959 - status drawer x evento apos recusa assinatura sequencial aprovado em homologacao.mp4]]

- **CT-B02 Permitir nova solicitação de assinatura para servidor após cancelamento**
    Dado que a assinatura de um servidor tenha sido cancelada após recusa em um fluxo sequencial
    Quando uma nova solicitação de assinatura for criada para esse servidor
    Então a nova solicitação deve ser exibida com status "Pendente" no drawer de solicitação de assinaturas

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Manter histórico de recusa e cancelamento no evento da solicitação anterior**
    Dado que uma assinatura tenha sido recusada e as demais assinaturas da solicitação tenham sido canceladas
    Quando eu acessar o evento da assinatura referente a essa solicitação
    Então o status deve permanecer exibido como "Recusado"/"Cancelado", preservando o histórico
    E esse registro não deve ser alterado por uma nova solicitação criada posteriormente

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Assinar normalmente em nova solicitação após cancelamento anterior**
    Dado que exista uma nova solicitação de assinatura pendente para um servidor cuja assinatura anterior foi cancelada
    Quando o servidor assinar a nova solicitação
    Então a assinatura deve ser concluída normalmente, sem erros ou bloqueios

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: HML (bug cadastrado a partir de análise em 10/07; validação e aprovação em homologação, 2026-07-23)

---

### Informações adicionais

- Demanda relacionada: SGV-9959 (Assinatura Sequencial; prioridade Média; João Marcelo, Squad 3). CTs e critérios rascunhados originalmente na daily de [[QA Workspace/01 Daily/2026-07/10-07|10/07]] (`## SGV-9959 - Casos de Teste — Assinatura Sequencial`).
- Gate de doc (2026-07-23): a regra "recusa de qualquer signatário cancela todas as assinaturas da sequência, inclusive as já efetuadas" **já está documentada** em [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] (seções "Solicitação sequencial" e "Assinando uma solicitação sequencial") e **bate com o comportamento aprovado** — sem divergência. A consistência de status drawer × evento é detalhe de UI não descrito na doc; sem regra de negócio a importar.
- Histórico:
    - 2026-07-10 - 🐛 Bug cadastrado (Assinatura Sequencial; CTs e critérios de aceite rascunhados na daily de 10/07)
    - 2026-07-23 - ✅ Aprovada em homologação (validação direto em HML; card local criado em modo enxuto já em Concluídas — etapas de esteira anteriores concluídas implicitamente). CT-B01 confirmado pela evidência gravada; critérios de aceite atendidos.
