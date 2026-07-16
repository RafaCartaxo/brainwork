---
tags:
  - bug
  - qa
  - despacho
  - copia
task: "9977"
prioridade: media
status: aberto
data: 2026-07-13
responsavel: Rafael
modulo: despacho
data_inicio: 2026-07-13
ambiente: DEV
---
# Nome do envolvido em cópia fica oculto no componente do despacho após emissão

### Descrição

Durante validação foi identificado que, ao adicionar um servidor, setor ou cidadão em cópia na criação de um despacho, o nome do envolvido fica oculto no componente do despacho após a emissão.

---

### Passo a passo para reproduzir

Dado que o usuário acesse o ambiente como servidor
E crie um despacho
Quando adicionar um servidor, setor ou cidadão como cópia
Então, ao emitir o despacho, o nome do envolvido deve ser exibido corretamente no componente do despacho

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9977)

![[9977 - nome do envolvido em copia oculto.mp4]]

---

### Resultado Esperado

O nome do servidor, setor ou cidadão adicionado como cópia deve ser exibido corretamente no componente do despacho após a emissão.

---

### Critérios de aceite

- O nome do envolvido em cópia como servidor deve ser exibido no componente do despacho emitido
- O nome do envolvido em cópia como setor deve ser exibido no componente do despacho emitido
- O nome do envolvido em cópia como cidadão deve ser exibido no componente do despacho emitido

---

### Casos de Teste Básicos

- **CT-B01 Exibir nome do servidor em cópia no despacho emitido**
    - Dado que o usuário crie um despacho
    - E adicione um servidor como cópia
    - Quando o despacho for emitido
    - Então o nome do servidor deve ser exibido corretamente no componente do despacho

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B02 Exibir nome do setor em cópia no despacho emitido**
    - Dado que o usuário crie um despacho
    - E adicione um setor como cópia
    - Quando o despacho for emitido
    - Então o nome do setor deve ser exibido corretamente no componente do despacho

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B03 Exibir nome do cidadão em cópia no despacho emitido**
    - Dado que o usuário crie um despacho
    - E adicione um cidadão como cópia
    - Quando o despacho for emitido
    - Então o nome do cidadão deve ser exibido corretamente no componente do despacho

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

---

### Ambiente

- Versão:
    
- Ambiente: Desenvolvimento
    
- Navegador:
    
- Sistema Operacional:
    

---

### Informações adicionais

- Demanda relacionada: SGV-9977
- Observações:
- Histórico:
    - 2026-07-13 - 🐛 Bug cadastrado
