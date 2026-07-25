---
tags:
  - bug
  - qa
  - documento
task: "6083"
prioridade: media
status: resolvido
data_inicio: 2026-07-24
data_fim: 2026-07-24
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Edição de documento não atualiza o conteúdo na assinatura ou download

### Descrição

Ao editar um documento, o conteúdo atualizado **não era refletido** no download e na assinatura do documento — a versão baixada/assinada mostrava o conteúdo antigo. Faz parte de um **problema em comum** com SGV-6873 e SGV-6348 (edição de documento não refletida no download): inicialmente pareciam cenários distintos, mas compartilham a mesma raiz. (Origem Notion SGV-6083, Matheus Godoi; prioridade Média conforme Triagem SP15.)

---

### Passo a passo para reproduzir

Dado um documento já existente
E que o servidor edite o conteúdo do documento
Quando o documento for baixado ou assinado
Então o arquivo gerado deve refletir a **última edição** (e não a versão anterior)

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://6083)

![[6083 - edicao documento reflete download assinatura aprovado em homologacao.mp4]]

---

### Resultado Esperado

Após editar um documento, o download e a assinatura refletem o conteúdo atualizado (a versão vigente da edição).

---

### Critérios de aceite

- [x] Editar o conteúdo de um documento e baixá-lo reflete a última edição
- [x] Editar o conteúdo de um documento e assiná-lo reflete a última edição

---

### Casos de Teste Básicos

- **CT-B01 Download reflete a edição**
    Dado um documento editado
    Quando o servidor faz o download
    Então o arquivo baixado mostra o conteúdo atualizado (última edição)

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[6083 - edicao documento reflete download assinatura aprovado em homologacao.mp4]]

- **CT-B02 Assinatura reflete a edição**
    Dado um documento editado
    Quando o servidor assina o documento
    Então o documento assinado mostra o conteúdo atualizado

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: HML (aprovada em homologação 2026-07-24, após reabertura e merge do fix da SGV-6873)

---

### Informações adicionais

- Demanda relacionada: SGV-6083 (Matheus Godoi; Sprint SP15/SP16). **Problema em comum** com [[QA Workspace/Planejamento/SP15|SGV-6873 e SGV-6348]] (edição não refletida no download).
- **Relação entre os fixes** (confirmada no git):
    - `fix/6083` original (`96dcb249`) — atualiza o conteúdo do documento para download e assinatura após edição;
    - **`fix/6873` foi mergeado dentro de `fix/6083`** (`bd8d86a6 fix(SGV-6083): Merge branch 'fix/6873' into fix/6083`) — a SGV-6873 ("download de documento temporário não refletia a edição") é a correção da raiz comum, e foi a que destravou o 6083;
    - **SGV-6348 tem fix PRÓPRIO e separado** (`f8d1cb4e` / `a8df3485` — "evita carregar dados desnecessários na regeneração do pdf" + "loga erro no download") — mesma área (download), mas **mudança distinta**; **não** é coberto pela validação do 6083.
- Gate de doc (2026-07-24): [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|Gerar Documento]] não cobre "download/assinatura refletir a edição do documento" — sem divergência; gap de doc (fluxo 8).
- Histórico:
    - 2026-07-24 - 📝 Bug importado (card criado a partir do ticket + narrativa da validação; sem export completo)
    - 2026-07-24 - 🔴 Reaberta em homologação — 1ª validação em HML deu erro (o problema comum ainda ocorria)
    - 2026-07-24 - 🔀 Fix da SGV-6873 mergeado em `fix/6083` (correção da raiz comum) e reenviado pra homologação
    - 2026-07-24 - 🔁 Retestada e aprovada em homologação (com o fix do 6873 incorporado)
    - 2026-07-24 - 🎬 Evidência anexada (`6083 - Documento editado ok.mp4`, gravada 15:09 — chegou depois da aprovação inicial)
