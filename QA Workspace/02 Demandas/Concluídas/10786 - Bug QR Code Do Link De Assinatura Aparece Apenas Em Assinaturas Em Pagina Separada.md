---
tags:
  - bug
  - qa
  - assinatura
task: "10786"
prioridade: media
status: resolvido
data_inicio: 2026-08-12
data_fim: 2026-09-02
responsavel: Rafael
cadastrado_por: Rafael
modulo: assinaturas
ambiente: HML
---
# QR Code do link de assinatura aparece apenas em assinaturas em página separada

### Descrição

Durante validação foi identificado que o **QR Code do link de assinatura** é exibido **apenas nas assinaturas em página separada** (página extra). Nas demais assinaturas — as de **posicionamento manual**, no corpo do documento — o QR Code **não aparece**.

O comportamento esperado é que o QR Code apareça em **todas** as assinaturas, independentemente de como foram posicionadas.

Encontrado durante a validação da [[QA Workspace/02 Demandas/Concluídas/10267 - Bug Link Verificacao Assinatura Nao Aparece Em Anexos Com Imagens Grandes|SGV-10267]], em homologação.

> [!success]- Aprovado em 02/09/2026
> QR Code passou a aparecer também nas assinaturas de posicionamento manual, em homologação.

---

### Passo a passo para reproduzir

Dado que eu tenho um documento com assinaturas **em página separada** e assinaturas **posicionadas manualmente**
Quando eu observo o link/QR Code de verificação em cada uma delas
Então verifico que o QR Code aparece **somente** nas assinaturas em página separada, e **não** nas de posicionamento manual

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Homologa%C3%A7%C3%A3o/) [🔍](evidencia://10786)

![[10786 - qr code apenas em assinatura em pagina separada.mp4]]

*Evidência compartilhada com [[QA Workspace/02 Demandas/Concluídas/10267 - Bug Link Verificacao Assinatura Nao Aparece Em Anexos Com Imagens Grandes|SGV-10267]] — mesmo vídeo, cópia renomeada.*

![[10786 - OK pt1.mp4]]

![[10786 - OK pt2.mp4]]

*Aprovação de 02/09/2026 (ver CTs abaixo).*

---

### Resultado Esperado

- O **QR Code do link de assinatura** é exibido em **todas** as assinaturas, tanto nas geradas na página extra quanto nas posicionadas manualmente

**Lastro documental — a doc já define isso literalmente.** [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas → Regra transversal (global update)]]:

> O QR Code e o texto de autenticidade no rodapé valem **também para o posicionamento manual** — independente de a assinatura ter sido posicionada à mão ou gerada na página extra, o QR Code deve estar presente conforme a especificação acima.

O comportamento observado é o **oposto exato** da regra escrita. O resultado esperado não é interpretação da QA.

---

### Critérios de aceite

- [x] O QR Code aparece nas assinaturas geradas na **página extra**
- [x] O QR Code aparece nas assinaturas de **posicionamento manual**, no corpo do documento
- [x] O QR Code exibido no posicionamento manual é **escaneável** e leva à verificação da assinatura correspondente

---

### Casos de Teste Básicos

#### **CT-B01 QR Code presente na assinatura de posicionamento manual**

**Dado** que eu tenho um documento com assinatura **posicionada manualmente**
**Quando** eu observo o rodapé de autenticidade dessa assinatura
**Então** verifico que o **QR Code está presente**, conforme a regra transversal da doc

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10786 - qr code apenas em assinatura em pagina separada.mp4]]

![[10786 - OK pt1.mp4]]

---

#### **CT-B02 QR Code do posicionamento manual é escaneável e leva à verificação correta**

**Dado** que a assinatura de posicionamento manual exibe o QR Code
**Quando** eu escaneio o QR Code
**Então** verifico que ele abre a verificação **daquela** assinatura

**Execução Passou?**
- [x] Sim
- [ ] Não

**Evidências de Testes:**

![[10786 - OK pt2.mp4]]

*(pt1/pt2 assumidos na ordem dos CTs — corrigir se a cobertura for outra)*

---

### Ambiente

- Versão:
- Ambiente: Homologação. Card nasceu em `DEV/` representando a posição na esteira de correção (defeito identificado em homologação, durante a validação da SGV-10267 — [[Sistema/Contexto/PADROES_QA#Organização de Bugs|PADROES_QA]]); aprovado direto em homologação, sem passagem por validação isolada em DEV.

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/Concluídas/10267 - Bug Link Verificacao Assinatura Nao Aparece Em Anexos Com Imagens Grandes|SGV-10267]] — este bug foi **encontrado durante a validação dela**, e as duas compartilham a mesma gravação
- Observações:
    - **Gate de doc: divergência confirmada, com citação literal.** A regra transversal de [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] diz que o QR Code vale **também para o posicionamento manual**. O produto faz exatamente o contrário — exibe só na página extra.
    - **Quarto bug no mesmo rodapé de autenticidade**, junto de [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]], [[QA Workspace/02 Demandas/HML/10457 - Bug Espacamento Do Link Inferior E Paginacao Sobreposta Em Documento Assinado|SGV-10457]] e a própria SGV-10267. A dúvida em aberto na doc — *"o ajuste do rodapé foi pontual onde a doc o trata como regra transversal?"* — ganha aqui a resposta mais direta até agora: **este defeito é literalmente o rodapé funcionando só num dos dois posicionamentos**.
    - Escopo **não apurado nesta rodada** (segue em aberto na aprovação de 02/09): se a ausência do QR também ocorria na **impressão** e no **download** (a página extra "torna-se parte integrante do arquivo PDF", conforme a doc), ou só na visualização — não confirmado se a validação de hoje cobriu isso. Ver Anotações da daily de 02/09.
- Histórico:
    - 2026-08-12 - 🐛 Bug cadastrado (identificado em homologação, durante a validação da SGV-10267)
    - 2026-09-02 - ✅ Aprovada em homologação (QR Code passou a aparecer também no posicionamento manual)
