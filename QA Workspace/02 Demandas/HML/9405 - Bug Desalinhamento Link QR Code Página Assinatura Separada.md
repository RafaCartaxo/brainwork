---
tags:
  - bug
  - qa
  - assinatura
task: "9405"
prioridade: ""
status: aberto
data_inicio: 2026-07-28
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: HML
deploy: pendente_hml
---
# Desalinhamento do link e QR Code em documentos assinados com página de assinatura separada

### Descrição

Em documentos assinados configurados com **página de assinatura separada** (página extra de assinaturas), o **link de verificação e o QR Code saíam desalinhados** na página gerada.

---

### Resultado Esperado

No documento assinado com página de assinatura separada, o link de verificação e o QR Code aparecem alinhados corretamente, conforme o layout previsto para a página de assinaturas.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9405)

![[9405 - link e qr code alinhados pagina assinatura separada aprovado em dev.mp4]]

---

### Critérios de aceite

- [x] Link de verificação e QR Code alinhados na página de assinatura separada do documento assinado

---

### Casos de Teste Básicos

- **CT-B01 Link e QR Code alinhados na página de assinatura separada**
    Dado um documento configurado com página de assinatura separada
    Quando o documento é assinado e a página de assinaturas é gerada
    Então o link de verificação e o QR Code aparecem alinhados, sem deslocamento

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9405 - link e qr code alinhados pagina assinatura separada aprovado em dev.mp4]]

---

### Ambiente

- Versão:
- Ambiente: DEV (aprovada — segue pra homologação)

---

### Informações adicionais

- Demanda relacionada: SGV-9405 (origem Notion). Sem card/registro prévio no vault e **sem entrada na [[QA Workspace/Planejamento/SP15|Triagem SP15]]** — primeira aparição aqui; chegou direto pela validação.
- Sem export completo — card criado a partir do título do ticket + narrativa da validação.
- **Gate de doc** (2026-07-28, fluxo 8): [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] documenta o layout da página PAdES (hash ao lado do QR code, margens, selos — ajustes de 29/05/2024), mas **não cobre a página de assinatura separada**: ela aparece só como item da seção "Atualizações posteriores (conteúdo não veio no export)" — *"Atualização Página Extra de Assinaturas — 28/04/2026"* e *"Reposicionamento de selos de assinatura — 28/05/2026"*. Sem divergência de regra; é **gap de documentação com candidato nomeado** — esses dois itens são exatamente o que falta importar pra doc cobrir este comportamento.
- Histórico:
    - 2026-07-28 - ✅ Aprovada em DEV (link e QR Code alinhados na página de assinatura separada; segue pra homologação)
