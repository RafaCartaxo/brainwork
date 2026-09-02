---
tags:
  - bug
  - qa
task: "11215"
pai: ""
prioridade: media
status: resolvido
data_inicio: 2026-09-01
data_fim: 2026-09-02
responsavel: Rafael
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Documento não carrega para realizar assinatura

### Descrição

Durante validação foi identificado que, ao solicitar a assinatura de um servidor num documento/despacho/anexo e clicar pra assinar, o documento não é carregado com sucesso — a assinatura não pode ser concluída. Achado no mesmo ambiente de homologação (nova arquitetura) da [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]].

**Vizinho da [[QA Workspace/02 Demandas/Concluídas/11158 - Bug Prévia De Documento Não Carrega Para Solicitação De Assinatura|SGV-11158]], mas ponto de falha diferente**: na 11158 a tela de **solicitar** assinatura é que não carregava a prévia. Aqui a tela de solicitar funcionou normal — é o documento não carregando na hora de **assinar em si**, depois que a solicitação já foi feita.

> [!success]- Aprovado parcialmente em 02/09/2026 (v. 14.17.0)
> Considerado aprovado **apenas o carregamento do documento** para a tentativa de assinatura — o problema original deste card. A conclusão da assinatura em si segue com falha, agora tratada em [[QA Workspace/02 Demandas/HML/11249 - Bug Assinatura De Documento Ou Despacho Não É Concluída Com Sucesso|SGV-11249]] (comentário deixado por Rafael na task).

---

### Passo a passo para reproduzir

Dado que solicito a assinatura de um servidor em um documento/despacho/anexo
Quando clico para assinar
Então verifico que o documento não é carregado com sucesso

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Arquitetura/) [🔍](evidencia://11215)

![[11215 - parcial OK.mp4]]

![[11215 - Erro ao carregar documento para realizar assinatura.mp4]]

---

### Resultado Esperado

- Documento carrega normalmente na hora de assinar, permitindo concluir a assinatura

---

### Critérios de aceite

- [x] Ao clicar para assinar, o documento/despacho/anexo carrega com sucesso
- [ ] A assinatura pode ser concluída normalmente após o documento carregar — **fora do escopo desta aprovação, segue em [[QA Workspace/02 Demandas/HML/11249 - Bug Assinatura De Documento Ou Despacho Não É Concluída Com Sucesso|SGV-11249]]**

---

### Casos de Teste Básicos

#### **CT-B01 Documento carrega ao assinar**

**Dado** que solicito a assinatura de um servidor em um documento/despacho/anexo
**Quando** clico para assinar
**Então** o documento carrega com sucesso e a assinatura pode ser concluída

**Execução Passou?**
- [x] Sim
- [ ] Não

*(aprovado apenas quanto ao carregamento do documento — a conclusão da assinatura segue em [[QA Workspace/02 Demandas/HML/11249 - Bug Assinatura De Documento Ou Despacho Não É Concluída Com Sucesso|SGV-11249]])*

**Evidências de Testes:**

---

### Ambiente

- Versão: 14.17.0
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/HML/8321 - Testes Funcionais Da Nova Arquitetura|SGV-8321]]
- Observações: Bate direto com o **CT-002** ("Assinar um documento continua funcionando") da SGV-8321 — o cenário do CT é exatamente ter um documento pronto pra assinatura → assinar → confirmar que fica assinado. Marcado como reprovado lá. **Gate de doc** ([[Sistema/Skills/SKILL_VERIFICACAO_DOC|SKILL_VERIFICACAO_DOC]]): confirmação de paridade pós-migração de arquitetura, não regra de negócio nova — resultado esperado é reproduzir o comportamento pré-migração; válido pra parte aprovada (carregamento). Aprovação parcial registrada por Rafael diretamente na task (comentário): "Assinatura ainda não está sendo realizada com sucesso, porém foi aberto outra task para seguir com a tratativa, sendo essa considerada para aprovação, apenas o carregamento do documento para a realização da tentativa de assinatura no documento. Bug relacionado: SGV-11249".
- Histórico:
    - 2026-09-01 - 🐛 Bug cadastrado
    - 2026-09-02 - ✅ Aprovada parcialmente em homologação (v. 14.17.0) — carregamento do documento resolvido; conclusão da assinatura segue em [[QA Workspace/02 Demandas/HML/11249 - Bug Assinatura De Documento Ou Despacho Não É Concluída Com Sucesso|SGV-11249]]
