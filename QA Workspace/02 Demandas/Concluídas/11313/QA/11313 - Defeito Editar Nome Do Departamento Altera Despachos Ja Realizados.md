---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11313"
pai: "11083"
prioridade: alta
status: resolvido
data_inicio: 2026-09-03
data_fim: "2026-09-03"
responsavel: Rafael
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Editar nome do departamento altera despachos já realizados (não preserva o histórico)

### Descrição

Durante validação foi identificado que, ao editar o nome de um departamento, os despachos já realizados (emitidos antes da edição) também são alterados — passam a exibir o nome novo em vez do nome vigente na época da emissão, reescrevendo o histórico. O comportamento esperado é o mesmo já aplicado à edição do nome de setor: interações já realizadas não devem ser alteradas por uma mudança de nome posterior.

---

### Passo a passo para reproduzir

**Dado** que um departamento tem ao menos um despacho já realizado com o nome atual
**Quando** o nome do departamento é editado
**Então** verifico que os despachos já realizados passam a exibir o nome novo do departamento — o histórico é reescrito

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://11313)

![[11313 - Editar nome de departamente, também edita os já emitidos.mp4]]

---

### Resultado Esperado

Mesma regra já documentada pra edição do nome de **setor** ([[QA Workspace/04 Conhecimento/Módulos/Organograma#Edição de setor ou subsetor|Organograma]]), aplicada por analogia ao departamento:

- Despacho **já realizado** antes da edição mantém o nome do departamento vigente no momento da tramitação — a edição não altera interações passadas.
- A partir da data/horário da edição em diante, novas tramitações já saem com o nome novo.
- Se o departamento **não** tem nenhum despacho/documento tramitado, a edição do nome se aplica normalmente, sem ressalva.

---

### Critérios de aceite

- [ ] Despacho já realizado antes da edição do nome do departamento mantém o nome antigo, mesmo após a edição
- [ ] Despacho realizado depois da edição do nome do departamento exibe o nome novo
- [ ] Departamento sem nenhum despacho/documento tramitado tem a edição de nome aplicada normalmente, sem ressalva

---

### Casos de Teste Básicos

#### **CT-B01 Despacho já realizado preserva o nome antigo do departamento após edição**

**Dado** que um departamento tem ao menos um despacho já realizado, exibindo seu nome atual
**Quando** o nome do departamento é editado
**Então** o despacho já realizado continua exibindo o nome do departamento vigente no momento da tramitação, sem alteração retroativa

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

> [!success]- Reprovado em 03/09, aprovado no reteste de 03/09
> Corrigido e reteste passou — gravação da execução abaixo, junto com a evidência que registrou o problema original.

**Evidências de Testes:**

![[11313 - Editar nome de departamente, também edita os já emitidos.mp4]]
![[11313 - OK.mp4]]

---

#### **CT-B02 Despacho realizado após a edição usa o nome novo**

**Dado** que o nome de um departamento foi editado
**Quando** um novo despacho é realizado com esse departamento depois da edição
**Então** o despacho exibe o nome novo do departamento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

> [!info]- Não retestado explicitamente nesta rodada
> A aprovação de 03/09 confirmou o CT-B01 (nome antigo preservado). Este CT (nome novo em despacho futuro) não foi confirmado por essa evidência especificamente — validar durante a validação da SGV-11083 se ainda não tiver sido coberto.

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083]] — a task já inclui "edição" no escopo (título da task no Notion), mas o requisito técnico refinado não detalhava regra de efeito da edição sobre tramitações passadas nem tinha CT próprio pra isso; gap exposto por este defeito.
- Observações:
    - Resultado esperado ancorado por analogia na regra já documentada pra **setor** ([[QA Workspace/04 Conhecimento/Módulos/Organograma|Organograma]]), citada pelo Rafael como referência — inclui o alerta ao usuário ("documentos já tramitados permanecerão com o nome antigo") quando há tramitação prévia. Esse alerta **não tem CT próprio ainda** — não foi confirmado se faz parte desta correção ou é só o efeito de dado (nome preservado) sem a UX de aviso; confirmar com Rafael antes de cobrar o alerta como critério.
    - Versão/ambiente exato (qual container `dev-*`) não informado — pendência preencher.
- Histórico:
    - 2026-09-03 - 🐛 Defeito cadastrado (achado na validação da SGV-11083, evidência já no vault)
    - 2026-09-03 - ✅ Aprovado em DEV (corrigido, reteste OK) — card fechado sem etapa de HML: é defeito da [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083]], validação em homologação acontece pela task principal. CT-B02 (nome novo em despacho futuro) segue sem retest explícito — ver Observações.
