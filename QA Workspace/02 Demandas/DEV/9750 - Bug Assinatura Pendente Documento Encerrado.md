---
tags:
  - bug
  - qa
  - assinatura
task: "9750"
prioridade: alta
status: aberto
data_inicio: 2026-07-16
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: DEV
---
# Pedido de assinatura permanece pendente mesmo com o documento encerrado

### Descrição

Durante análise (Bruna Machado, 03/07/2026) foi identificada a causa raiz do relato de CX: **encerrar um documento para todos não cancela as solicitações de assinatura pendentes de despachos vinculados**. A pendência sobrevive ao encerramento — a assinatura segue aparecendo pro servidor (página inicial e mesa de trabalho) e, ao tentar assinar, ocorre erro, já que documento encerrado não aceita mais assinatura (a menos que reaberto).

Contraste que delimita o problema: na **retificação com troca de anexo**, a assinatura pendente é cancelada normalmente — o cancelamento só não acontece no encerramento. Reproduzido em produção: documento → despacho com solicitação de assinatura → encerrar para todos → assinatura do despacho segue pendente.

---

### Passo a passo para reproduzir

Dado que exista um documento criado (ex.: Processo Administrativo)
E um despacho tenha sido realizado com solicitação de assinatura para um servidor
Quando o documento for encerrado para todos
Então a solicitação de assinatura do despacho permanece pendente para o servidor
E ao tentar assinar (página inicial ou mesa de trabalho), após digitar a senha, surge erro e a assinatura não é efetivada

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9750)

- Evidências **na task do Notion**, sem cópia local: 2 vídeos anexados (relato CX) + print na análise da Bruna. Evidência local entra no fluxo normal quando houver validação em homologação.
- Documento do relato (produção Guarabira): https://guarabira-pb.sogov.com.br/cliente/41/documento/MR26NMMMQ0XGQ1Z34A
- Documento da reprodução na análise (produção): https://guarabira-pb.sogov.com.br/cliente/1/documento/MR56CO5OH0Y9D4B8K7

---

### Resultado Esperado

Ao encerrar um documento **para todos**, **todas as pendências de assinatura são canceladas** — do documento e dos despachos vinculados. Nenhum servidor fica com solicitação de assinatura pendente (ou erro ao tentar assinar) de documento encerrado.

---

### Critérios de aceite

- [ ] Encerrar um documento **para todos** cancela todas as solicitações de assinatura pendentes vinculadas a ele, inclusive as de despachos
- [ ] Encerrar **para mim** ou encerrar **para meu setor** **não** cancela solicitações de assinatura pendentes — o cancelamento é exclusivo do encerrar para todos
- [ ] Após o encerramento para todos, a assinatura cancelada não aparece mais como pendente pro servidor — nem na página inicial, nem na mesa de trabalho
- [ ] Sem regressão no cancelamento já existente: retificação com troca de anexo continua cancelando a assinatura pendente
- [ ] Sem regressão no fluxo normal: solicitação de assinatura em documento aberto segue sendo assinável após digitar a senha
- [ ] **Solicitações já pendentes de documentos encerrados antes da correção**: definir com dev/produto se a correção inclui saneamento retroativo — deixar explícito na entrega

---

### Casos de Teste Básicos

- **CT-B01 Encerrar para todos cancela assinatura pendente de despacho**
    Dado que um documento tenha um despacho com solicitação de assinatura pendente
    Quando o documento for encerrado para todos
    Então a solicitação de assinatura do despacho deve ser cancelada

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Servidor não vê pendência de documento encerrado**
    Dado que um documento com solicitação de assinatura pendente tenha sido encerrado para todos
    Quando o servidor acessar a página inicial e a mesa de trabalho
    Então nenhuma assinatura pendente do documento encerrado deve ser exibida, e não deve haver caminho pra tentar assiná-la

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Regressão: retificação com troca de anexo segue cancelando assinatura**
    Dado que um documento tenha uma solicitação de assinatura pendente
    Quando o documento for retificado com troca de anexo
    Então a solicitação de assinatura pendente deve ser cancelada (comportamento atual preservado)

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Regressão: assinatura em documento aberto funciona**
    Dado que um documento aberto tenha uma solicitação de assinatura pendente
    Quando o servidor assinar digitando a senha
    Então a assinatura deve ser efetivada normalmente

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B05 Encerramentos parciais não cancelam assinaturas**
    Dado que um documento tenha um despacho com solicitação de assinatura pendente
    Quando um envolvido encerrar o documento **para mim** (e, em novo cenário, **para meu setor**)
    Então as solicitações de assinatura pendentes permanecem inalteradas

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: (relato e análise em produção; correção segue esteira 3f — task de API, validação direto em homologação)

---

### Informações adicionais

- Demanda relacionada: SGV-9750 (origem CX — CX responsável: Vanessa Pacífico; análise: Bruna Machado, 03/07/2026; dev: Washington Junior, Squad 1 - Rogue One, Sprint SP15)
- Observações: Esteira 3f ([[Sistema/Contexto/FLUXOS|FLUXOS]]) — task `[API]`, sem validação em DEV: QA define critérios, dev implementa cenários, QA revisa cenários contra os critérios, teste real direto em homologação. **Status no Notion ao refinar: Revisar MR** (correção já implementada, MR em revisão) — próximo passo de QA é revisar os cenários de teste. Entrega prevista: 28/07/2026. Funcionalidade afetada: Assinatura. **Escopo do encerramento**: existem três variações (encerrar para mim, para meu setor, para todos) — o cancelamento em massa das assinaturas é **exclusivo do encerrar para todos**; as variações parciais não cancelam (critério negativo e CT-B05 cobrem). **Ponto em aberto (não é critério)**: comportamento das assinaturas canceladas caso o documento seja **reaberto** — levantar com dev/produto se relevante pra entrega.
- Histórico:
    - 2026-07-03 - Análise de causa raiz (Bruna Machado): encerramento de documento não cancela solicitações de assinatura pendentes de despacho (retificação com troca de anexo cancela); reproduzido em produção
    - 2026-07-16 - 📝 Bug refinado (critérios de aceite prontos; MR já em revisão)
    - 2026-07-16 - 📤 Bug atualizado no Notion (critérios de aceite registrados na task, incluindo o ponto a definir do saneamento retroativo)
