---
tags:
  - bug
  - qa
  - assinatura
task: "10267"
prioridade: media
status: resolvido
data_inicio: 2026-08-10
data_fim: 2026-08-12
responsavel: Rafael
cadastrado_por: ""
modulo: assinaturas
ambiente: HML
---
# [Bug - CX] Link de verificação de assinatura não aparece em anexos com imagens grandes (apenas o selo é exibido)

### Descrição

Durante validação foi identificado que, em documento com **anexo de imagem grande**, o **link de verificação de assinatura** saía **parcialmente oculto e incorreto** no rodapé — em alguns casos não aparecia, ficando apenas o selo visível.

Atinge a **função de verificação** do documento: sem o link/QR legível, não há como conferir a autenticidade da assinatura.

Reaberta em DEV em 10/08/2026 e **aprovada em homologação em 12/08/2026**.

---

### Passo a passo para reproduzir

Dado que eu tenho um documento assinado
E o documento tem um **anexo com imagem grande**, cujo conteúdo extrapola a página
Quando eu abro o documento e observo o rodapé de autenticidade
Então verifico que o link de verificação de assinatura aparece **parcialmente oculto ou não aparece**, restando apenas o selo

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://10267)

**Reprovação em DEV (10/08/2026)** — link ficando oculto:

![[10267 - link ficando oculto nok.mp4]]

**Aprovação em homologação (12/08/2026)** — link visível no anexo grande:

![[10267 - link em anexo gigante visivel ok.mp4]]

---

### Resultado Esperado

- O **link de verificação de assinatura** e o **QR Code** ficam **presentes e legíveis** no rodapé, mesmo quando o documento tem anexo com imagem grande

Lastro documental: [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas → Regra transversal]] — o QR Code e o texto de autenticidade valem para todo posicionamento, e a doc define como defeito "o link/QR sair cortado, encostado na margem ou coberto por outro elemento, a ponto de não dar pra ler ou escanear".

---

### Critérios de aceite

- [x] O link de verificação de assinatura aparece **íntegro e legível** no rodapé, em documento com anexo de imagem grande
- [x] O QR Code permanece **escaneável** no mesmo cenário

---

### Casos de Teste Básicos

#### **CT-B01 Link de verificação visível em documento com anexo de imagem grande**

**Dado** que eu tenho um documento assinado
**E** o documento tem um anexo com imagem grande
**Quando** eu abro o documento e observo o rodapé de autenticidade
**Então** verifico que o link de verificação de assinatura aparece **íntegro e legível**, e não apenas o selo

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10267 - link em anexo gigante visivel ok.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/10786 - Bug QR Code Do Link De Assinatura Aparece Apenas Em Assinaturas Em Pagina Separada|SGV-10786]] — bug **derivado desta validação**: durante a aprovação de 12/08 notou-se que o QR Code do link de assinatura só é exibido em assinaturas em **página separada**
- Observações:
    - **Card criado no dia da aprovação** (12/08/2026). A demanda existiu de 10/08 a 12/08 só como registro nas dailies — a descrição e o passo a passo foram reconstruídos a partir desses registros e das evidências.
    - **Gate de doc já realizado em 10/08**, com **divergência confirmada**: a doc de [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] trata o QR Code/texto de autenticidade como **regra transversal**, então o resultado esperado tem lastro escrito e não é interpretação da QA.
    - **Lacuna de doc que permanece**: a doc **não descreve** como um anexo cujo conteúdo extrapola a página afeta o layout do rodapé. Pendência de importação segue aberta na fila.
    - **Terceiro bug no mesmo rodapé de autenticidade**, junto de [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]] (link/QR na vertical) e [[QA Workspace/02 Demandas/HML/10457 - Bug Espacamento Do Link Inferior E Paginacao Sobreposta Em Documento Assinado|SGV-10457]] (link inferior + numeração sobreposta). Com a SGV-10786, são **quatro** — reforça a dúvida em aberto na doc: se o ajuste do rodapé foi **pontual** onde a doc o trata como regra transversal.
    - ⚠️ **A validação pulou a revalidação em DEV**: reprovou em DEV em 10/08 e foi aprovada direto em homologação em 12/08.
- Histórico:
    - 2026-08-10 - 🔴 Reaberta em DEV (link de verificação parcialmente oculto e incorreto em anexo com imagem grande)
    - 2026-08-10 - 🔎 Gate de doc: divergência confirmada contra a regra transversal do QR Code em [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]]
    - 2026-08-12 - 🔁 Retestada e aprovada em homologação (link visível em documento com anexo de imagem grande)
