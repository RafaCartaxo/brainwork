---
tags:
  - bug
  - qa
  - servicos-e-assuntos
task: "10711"
pai: ""
prioridade: alta
status: resolvido
data_inicio: 2026-08-27
data_fim: 2026-09-02
responsavel: Rafael
cadastrado_por: ""
modulo: servicos-e-assuntos
ambiente: HML
---
# Configuração de setores em "Ver dados sigilosos" não é mantida após salvar

### Descrição

Verificado que, ao configurar os setores que podem ver dados sigilosos (e interações externas) de um serviço/assunto, a seleção realizada não é mantida após salvar.

Ao utilizar a opção de selecionar todos e, em seguida, desmarcar para manter apenas alguns setores selecionados, a configuração é apresentada corretamente antes de salvar. Porém, após salvar e acessar novamente a edição do serviço/assunto, todos os setores aparecem selecionados de novo.

---

### Passo a passo para reproduzir

Dado que estou logado como servidor
E esse serviço/assunto possui sigilo
E desmarco os setores que não devem ter acesso, mantendo apenas alguns selecionados
E salvo a edição
Quando acesso novamente a edição do serviço/assunto
Então verifico que todos os setores são exibidos como selecionados, desconsiderando a configuração realizada anteriormente

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10711)

![[10711 - OK.mp4]]

---

### Resultado Esperado

- Os setores selecionados na seção "Ver dados sigilosos" e "interações externas" são mantidos após salvar a configuração. Ao editar novamente o serviço/assunto, somente os setores previamente selecionados permanecem marcados.

**Lastro documental** — [[QA Workspace/04 Conhecimento/Módulos/Serviços e Assuntos|Serviços e Assuntos]] documenta o campo "Somente estes setores poderão ver dados sigilosos" (seção 04, Regras de Tramitação) como seleção múltipla — a persistência da seleção após salvar é comportamento básico esperado, não é regra de negócio em disputa.

---

### Critérios de aceite

- [x] A seleção dos setores é salva corretamente ao editar o serviço/assunto
- [x] Ao acessar novamente a configuração, apenas os setores selecionados anteriormente permanecem marcados

---

### Casos de Teste Básicos

#### **CT-B01 Seleção de setores em "Ver dados sigilosos" persiste após salvar**

**Dado** que desmarco alguns setores em "Ver dados sigilosos", mantendo só parte selecionada
**E** salvo a edição do serviço/assunto
**Quando** acesso novamente a edição
**Então** só os setores previamente selecionados aparecem marcados

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10711 - OK.mp4]]

---

### Ambiente

- Versão: 12.44.51.2
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: possível relação com [[QA Workspace/02 Demandas/DEV/6373 - Bug Setores Regras Tramitação Não Mantidos Avançar Retroceder Etapas AS|SGV-6373]] — o export do Notion marcava esta SGV-10711 como "Impactando" a 6373 (mesma família: setores não mantidos em telas de configuração), não confirmado se é causa raiz comum
- Observações: Origem — export do Notion (SGV-10711, squad Rogue One, projeto Sustentação). MR aberto por Diogo Sobreira (dev), revisado por João Rodrigo e João Marcelo, arquivo `Section4.tsx` (fluxo guiado de criação de serviço/assunto). Aprovado por Rafael direto em homologação (comentário da task: "Status: Aprovado em homologação Versão: 12.44.51.2"), sem validação isolada em DEV registrada.
- Histórico:
    - 2026-08-27 - 🐛 Bug identificado, MR aberto (Diogo Sobreira)
    - 2026-09-02 - ✅ Aprovada em homologação (v. 12.44.51.2) — seleção de setores em "Ver dados sigilosos" mantida após salvar
