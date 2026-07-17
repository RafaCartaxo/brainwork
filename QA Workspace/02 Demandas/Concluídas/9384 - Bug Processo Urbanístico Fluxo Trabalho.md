---
tags:
  - bug
  - qa
  - urbanistico
  - fluxo-trabalho
task: "9384"
prioridade: alta
status: resolvido
data_inicio: 2026-07-07
data_fim: 2026-07-13
responsavel: Rafael
modulo: fluxo-trabalho
ambiente: HML
---
# Processo Urbanístico não é carregado para seleção em Fluxo de Trabalho

### Descrição

Durante validação foi identificado que o Processo Urbanístico não era carregado corretamente para seleção no Fluxo de Trabalho. A demanda foi corrigida e aprovada em homologação em 13/07.

---

### Passo a passo para reproduzir

Dado que o usuário acesse o Fluxo de Trabalho para selecionar um Processo Urbanístico
Quando a lista de processos for carregada
Então o Processo Urbanístico deve aparecer disponível para seleção

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9384)

![[9384 - criação instancia nok.mp4]]

![[9384 - criação modulo nok.mp4]]

![[9384 - seleção processo urbanistico ok.mp4]]

---

### Resultado Esperado

O Processo Urbanístico deve ser carregado e exibido corretamente na lista de seleção do Fluxo de Trabalho.

---

### Critérios de aceite

- [ ] O Processo Urbanístico deve aparecer disponível para seleção ao acessar o Fluxo de Trabalho

---

### Casos de Teste Básicos

- **CT-B01 Validar carregamento de Processo Urbanístico para seleção no Fluxo de Trabalho**
    Dado que o usuário acesse o Fluxo de Trabalho para selecionar um Processo Urbanístico
    Quando a lista de processos for carregada
    Então o Processo Urbanístico deve aparecer disponível para seleção

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

- Demanda relacionada: SGV-9384
- Observações:
- Histórico:
    - 2026-07-07 - 🔴 Reaberta em homologação (seleção de Processo Urbanístico ainda incorreta)
    - 2026-07-13 - ✅ Aprovada em homologação
