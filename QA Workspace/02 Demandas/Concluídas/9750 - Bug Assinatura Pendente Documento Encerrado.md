---
tags:
  - bug
  - qa
  - assinatura
task: "9750"
prioridade: alta
status: resolvido
data_inicio: 2026-07-16
data_fim: 2026-07-23
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
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

- Evidências **na task do Notion**, sem cópia local: 2 vídeos anexados (relato CX) + print na análise da Bruna.
- Validação aprovada em homologação (2026-07-23):

![[9750 - encerrar documento para todos cancela assinatura pendente aprovado em homologacao.mp4]]

- Documento do relato (produção Guarabira): https://guarabira-pb.sogov.com.br/cliente/41/documento/MR26NMMMQ0XGQ1Z34A
- Documento da reprodução na análise (produção): https://guarabira-pb.sogov.com.br/cliente/1/documento/MR56CO5OH0Y9D4B8K7

---

### Resultado Esperado

Ao encerrar um documento **para todos**, **todas as pendências de assinatura são canceladas** — do documento e dos despachos vinculados. Nenhum servidor fica com solicitação de assinatura pendente (ou erro ao tentar assinar) de documento encerrado.

---

### Critérios de aceite

- [x] Encerrar um documento **para todos** cancela todas as solicitações de assinatura pendentes vinculadas a ele, inclusive as de despachos
- [x] Encerrar **para mim** ou encerrar **para meu setor** **não** cancela solicitações de assinatura pendentes — o cancelamento é exclusivo do encerrar para todos
- [x] Após o encerramento para todos, a assinatura cancelada não aparece mais como pendente pro servidor — nem na página inicial, nem na mesa de trabalho
- [x] Sem regressão no cancelamento já existente: retificação com troca de anexo continua cancelando a assinatura pendente
- [x] Sem regressão no fluxo normal: solicitação de assinatura em documento aberto segue sendo assinável após digitar a senha
- [ ] **Solicitações já pendentes de documentos encerrados antes da correção**: definir com dev/produto se a correção inclui saneamento retroativo — deixar explícito na entrega

---

### Casos de Teste Básicos

- **CT-B01 Encerrar para todos cancela assinatura pendente de despacho**
    Dado que um documento tenha um despacho com solicitação de assinatura pendente
    Quando o documento for encerrado para todos
    Então a solicitação de assinatura do despacho deve ser cancelada

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9750 - encerrar documento para todos cancela assinatura pendente aprovado em homologacao.mp4]]

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
- Ambiente: HML (relato e análise em produção; correção seguiu esteira 3f — task de API, validação direto em homologação, aprovada 2026-07-23)

---

### Informações adicionais

- Demanda relacionada: SGV-9750 (origem CX — CX responsável: Vanessa Pacífico; análise: Bruna Machado, 03/07/2026; dev: Washington Junior, Squad 1 - Rogue One, Sprint SP15)
- Observações: Esteira 3f ([[Sistema/Contexto/FLUXOS|FLUXOS]]) — task `[API]`, sem validação em DEV: QA define critérios, dev implementa cenários, QA revisa cenários contra os critérios, teste real direto em homologação. **Status no Notion ao refinar: Revisar MR** (correção já implementada, MR em revisão) — próximo passo de QA foi revisar os cenários e validar em homologação. Entrega prevista: 28/07/2026 (aprovada antes, em 23/07). Funcionalidade afetada: Assinatura. **Escopo do encerramento**: existem três variações (encerrar para mim, para meu setor, para todos) — o cancelamento em massa das assinaturas é **exclusivo do encerrar para todos**; as variações parciais não cancelam (critério negativo e CT-B05 cobrem). **Ponto em aberto (não é critério)**: comportamento das assinaturas canceladas caso o documento seja **reaberto** — levantar com dev/produto se relevante pra entrega.
- Gate de doc (2026-07-23): a doc [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] **não descreve** o cancelamento de assinaturas pendentes ao encerrar um documento — sem divergência com o aprovado; gap de doc registrado nas Dúvidas em aberto da doc (candidato a importar via fluxo 8).
- Histórico:
    - 2026-07-03 - Análise de causa raiz (Bruna Machado): encerramento de documento não cancela solicitações de assinatura pendentes de despacho (retificação com troca de anexo cancela); reproduzido em produção
    - 2026-07-16 - 📝 Bug refinado (critérios de aceite prontos; MR já em revisão)
    - 2026-07-16 - 📤 Bug atualizado no Notion (critérios de aceite registrados na task, incluindo o ponto a definir do saneamento retroativo)
    - 2026-07-20 - 🔎 Cenários de teste do MR revisados a nível de escopo ([MR !583](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/583)) — 6 cenários implementados batem com os 5 critérios de aceite, inclusive o caso de dado legado; fix cobre também revogação de documento (além de encerramento, que era o pedido original) — sem CT formal pra revogação no card ainda
    - 2026-07-23 - ✅ Aprovada em homologação (task de API, validação direto em HML; etapas de esteira DEV puladas por ser 3f). CT-B01 confirmado pela evidência gravada; critérios 1–5 atendidos. Gate de doc: Assinaturas não cobre o comportamento — sem divergência, gap anotado na doc (fluxo 8). Ponto em aberto do saneamento retroativo (critério 6) segue pra definição com dev/produto.
