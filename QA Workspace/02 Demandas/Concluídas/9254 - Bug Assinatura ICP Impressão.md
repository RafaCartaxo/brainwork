---
tags:
  - bug
  - qa
  - assinatura
  - icp
  - impressao
task: "9254"
prioridade: alta
status: resolvido
data_inicio: 2026-07-03
data_fim: 2026-07-03
responsavel: Rafael
modulo: assinatura-digital
ambiente: PROD
---
# Erro ao imprimir documento com assinatura ICP

### Descrição

Durante validação foi identificado que, ao baixar o documento PAdES, o comportamento é o esperado, mas ao tentar imprimir a última página — onde consta apenas a assinatura ICP — ela não é exibida corretamente. O selo fica em local em branco do documento e, ao posicioná-lo, não mostra a estrutura da última página. O mesmo ocorre na visualização mobile (o conteúdo da última página não aparece, apenas a assinatura).

---

### Passo a passo para reproduzir

Dado que o documento contenha assinatura ICP na última página
E o documento seja baixado no formato PAdES
Quando o usuário tentar imprimir o documento
Então a última página deve ser exibida corretamente com o selo e o conteúdo

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9254)

![[9254 - assinatura icp impressão validada.mp4]]

---

### Resultado Esperado

A última página de um documento com assinatura ICP deve ser exibida corretamente na impressão, com o selo posicionado sobre o conteúdo original da página, tanto em desktop quanto em dispositivos mobile, inclusive para documentos muito grandes.

---

### Critérios de aceite

- [x] A última página com assinatura ICP deve exibir corretamente o selo e o conteúdo ao imprimir
- [x] A visualização mobile deve exibir o conteúdo completo da última página, não apenas a assinatura
- [x] Documentos muito grandes devem exibir todas as páginas corretamente ao imprimir

---

### Casos de Teste Básicos

- **CT-B01 Validar impressão de documento com assinatura ICP**
    Dado que o documento contenha assinatura ICP na última página
    Quando o usuário imprimir o documento
    Então a última página deve ser exibida corretamente com o selo e o conteúdo

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Validar visualização mobile de documento com assinatura ICP**
    Dado que o documento contenha assinatura ICP
    Quando visualizado em dispositivo mobile
    Então o conteúdo da última página deve ser exibido completamente, não apenas a assinatura

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Validar impressão em documentos grandes com assinatura ICP**
    Dado que o documento contenha assinatura ICP e seja um documento muito grande
    Quando o usuário imprimir o documento
    Então todas as páginas devem ser exibidas corretamente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: Produção

---

### Informações adicionais

- Demanda relacionada: SGV-9254
- Observações: Atenção a cenários de documentos muito grandes. Validar em diferentes dispositivos (desktop, mobile). Verificar tanto PAdES quanto impressão física/virtual.
- Histórico:
    - 2026-07-03 - ✅ Aprovada em produção
