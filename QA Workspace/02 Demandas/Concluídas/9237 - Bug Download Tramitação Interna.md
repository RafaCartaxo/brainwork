---
tags:
  - bug
  - qa
  - download
  - tramitacao
task: "9237"
prioridade: alta
status: resolvido
data_inicio: 2026-07-07
data_fim: 2026-07-14
responsavel: Rafael
modulo: download-documentos
ambiente: HML
---
# Download realizado por cidadão inclui conteúdo de tramitação interna

### Descrição

Durante validação foi identificado que o download de documentos realizado por cidadão está incluindo conteúdo de tramitação interna (informações de processo interno que não deveriam ser visíveis ao cidadão). A correção passou em ambiente de desenvolvimento (DEV), mas apresentou erro em homologação (HML) em duas rodadas de validação (07/07 e 13/07). Retestado em 14/07 e aprovado em homologação.

---

### Passo a passo para reproduzir

Dado que um cidadão realize o download de um documento público
Quando o download for concluído
Então o conteúdo de tramitação interna não deve estar presente no arquivo baixado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9237)

![[9237 - Download cidadão contendo conteúdo interno - verificar caso, dev foi ok, hom n ok.mp4]]

![[9237 - Download cidadão contendo conteúdo interno - verificar caso, dev foi ok, hom n ok pt2.mp4]]

![[9237 - downlaod está trazendo todo o conteudo nok.mp4]]

![[9237 - retestado e aprovado em homologação.mp4]]

---

### Resultado Esperado

O download realizado por um cidadão não deve conter, em nenhuma hipótese, conteúdo de tramitação interna do processo.

---

### Critérios de aceite

- [ ] O arquivo baixado por um cidadão não deve conter informações de tramitação interna
- [ ] O comportamento deve ser consistente entre os ambientes de DEV, HML e PROD

---

### Casos de Teste Básicos

- **CT-B01 Validar que download do cidadão não exibe tramitação interna**
    Dado que um cidadão realize o download de um documento público
    Quando o download for concluído
    Então o conteúdo de tramitação interna não deve estar presente no arquivo baixado

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

- Demanda relacionada: SGV-9237
- Observações: A correção passou em DEV mas quebrou em HML por duas vezes antes de ser aprovada definitivamente.
- Histórico:
    - 2026-07-07 - ✅ Aprovada em DEV
    - 2026-07-07 - 🔴 Reaberta em homologação
    - 2026-07-13 - ✅ Aprovada em DEV (nova correção)
    - 2026-07-13 - 🔴 Reaberta novamente em homologação
    - 2026-07-14 - 🔁 Retestada e aprovada em homologação
