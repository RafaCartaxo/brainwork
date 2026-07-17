---
tags:
  - bug
  - qa
  - ancoragem
task: "7523"
prioridade: media
status: resolvido
data_inicio: 2026-07-07
data_fim: 2026-07-07
responsavel: Rafael
modulo: interface-componentes
ambiente: HML
---
# Botão flutuante de ancoragem não aparece no local correto enquanto a página é carregada

### Descrição

Durante validação foi identificado que o botão flutuante de ancoragem não aparece no local correto durante o carregamento da página.

---

### Passo a passo para reproduzir

Dado que a página esteja carregando
Quando o botão flutuante de ancoragem for renderizado
Então ele deve aparecer na posição correta desde o início do carregamento

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://7523)

![[7523 - Componente ancoragem ok.mp4]]

---

### Resultado Esperado

O botão flutuante de ancoragem deve aparecer na posição correta desde o início do carregamento da página, sem deslocamento visual.

---

### Critérios de aceite

- [ ] O botão de ancoragem deve ser exibido na posição correta durante todo o carregamento da página

---

### Casos de Teste Básicos

- **CT-B01 Validar posicionamento do botão de ancoragem durante carregamento**
    Dado que a página esteja carregando
    E o botão flutuante de ancoragem for renderizado
    Quando o carregamento avançar
    Então ele deve aparecer na posição correta desde o início

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

- Demanda relacionada: SGV-7523
- Observações: Aprovado em homologação sem ressalvas.
- Histórico:
    - 2026-07-07 - ✅ Aprovada em homologação
