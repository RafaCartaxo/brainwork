---
tags:
  - bug
  - qa
  - assinatura
task: "10457"
prioridade: ""
status: aberto
data_inicio: 2026-07-29
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: assinatura
ambiente: HML
---
# Espaçamento do link inferior não respeitado e paginação sobreposta ao link em documento assinado

### Descrição

Dois problemas no **bloco de autenticidade do rodapé** (link de verificação + QR Code) de documento assinado:

1. **Espaçamento não respeitado** — além do link na vertical já tratado na [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]], existe **outro link na parte inferior** cujo espaçamento não está sendo respeitado.
2. **Paginação sobreposta ao link** — no download **personalizado** com a opção de **páginas enumeradas** ativada (que insere automaticamente `1/4`, `2/4`, `3/4`…), a numeração da página fica **sobreposta ao link**.

Os dois compartilham a mesma região da folha, o que sugere causa comum: o rodapé de autenticidade e a numeração disputam o mesmo espaço, e as medidas fixas da especificação não estão sendo aplicadas.

---

### Passo a passo para reproduzir

**Cenário 1 — espaçamento do link inferior**

Dado que eu tenho um documento assinado com o bloco de autenticidade no rodapé
Quando eu abro o documento e confiro o link de verificação da parte inferior
Então verifico que o espaçamento dele não é respeitado, divergindo das medidas fixas da especificação

**Cenário 2 — paginação sobreposta ao link**

Dado que eu tenho um documento assinado
E que eu baixo pela opção "personalizado"
E que a opção de páginas enumeradas está ativada
Quando o arquivo é gerado com a numeração automática (`1/4`, `2/4`, `3/4`…)
Então verifico que a numeração da página fica sobreposta ao link de autenticidade

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://10457)

> [!warning] Evidência pendente
> Não havia gravação nova na raiz de `Evidências/` quando este card foi criado, e o Rafael não indicou arquivo. Gravar/nomear como `10457 - <descrição>.mp4` e rodar o 🔄 — o roteador move e embeda aqui sozinho. **Evidência é o que sustenta o card na discussão com o dev; sem ela o bug depende de memória.**
>
> Vale capturar as duas situações: (a) o rodapé com o espaçamento errado, de preferência com régua/medida visível, e (b) o PDF baixado em personalizado com páginas enumeradas mostrando a sobreposição.

---

### Resultado Esperado

O bloco de autenticidade do rodapé (link + QR Code) respeita as **medidas fixas da especificação** — QR Code de 20×20px, **8px** de margem inferior, **8px** de margem esquerda e **8px** de espaçamento até o texto — e a **numeração de páginas** do download personalizado é posicionada **sem sobrepor** esse bloco, mantendo a regra de que a numeração inclui as páginas de assinatura.

---

### Critérios de aceite

- [ ] O bloco de autenticidade do rodapé respeita margem inferior de **8px**, margem esquerda de **8px** e espaçamento até o texto de **8px**
- [ ] O QR Code mantém a proporção de **20×20px**
- [ ] No download **personalizado com páginas enumeradas**, a numeração **não se sobrepõe** ao link de autenticidade
- [ ] A numeração continua **incluindo as páginas de assinatura** (não regredir a regra documentada ao corrigir o posicionamento)
- [ ] O comportamento vale igualmente para **página extra de assinaturas** e **posicionamento manual** (regra transversal da doc)

---

### Casos de Teste Básicos

- **CT-B01 Espaçamento do bloco de autenticidade no rodapé**
    Dado que eu tenho um documento assinado com o bloco de autenticidade no rodapé
    Quando eu confiro as medidas do QR Code e do link
    Então verifico QR Code de 20×20px, 8px de margem inferior, 8px de margem esquerda e 8px de espaçamento até o texto

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [x] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Download personalizado com páginas enumeradas**
    Dado que eu tenho um documento assinado
    E que eu baixo pela opção "personalizado" com páginas enumeradas ativada
    Quando o arquivo é gerado com a numeração automática
    Então verifico que a numeração não se sobrepõe ao link de autenticidade e ambos permanecem legíveis

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [x] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Regressão — numeração inclui as páginas de assinatura**
    Dado que eu tenho um documento com página extra de assinaturas
    Quando eu baixo em personalizado com páginas enumeradas
    Então verifico que a contagem total inclui as páginas de assinatura, conforme a doc do módulo

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Posicionamento manual das assinaturas**
    Dado que eu tenho um documento com assinaturas **posicionadas manualmente** (sem página extra)
    Quando o documento é assinado e eu confiro o rodapé
    Então verifico que o QR Code e o texto de autenticidade seguem a mesma especificação de espaçamento

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-10457** (número informado pelo Rafael em 29/07).
- ⚠️ **Ambiente inferido como homologação** — é onde o Rafael está validando hoje. Corrigir se foi em DEV.
- **Prioridade não definida** — não foi declarada. Definir na triagem.
- **Gate de doc** (2026-07-29, fluxo 8): **divergência confirmada** no espaçamento, **gap** no posicionamento da paginação. Os dois lados vêm da [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas § Página extra de assinaturas]], importada hoje:
    - A doc traz a **especificação numérica do QR Code** (20×20px; margem inferior 8px; margem esquerda 8px; espaçamento até o texto 8px) e a apresenta como *"o critério objetivo pra julgar desalinhamento"*. Espaçamento errado **contraria regra escrita** — não é questão de percepção.
    - A doc declara isso **regra transversal**: *"o QR Code e o texto de autenticidade no rodapé valem também para o posicionamento manual"*. Ou seja, a especificação vale pro rodapé **em qualquer configuração** — por isso o CT-B04.
    - A doc afirma que *"se o usuário paginar, a numeração inclui as páginas de assinatura"* (arquivos ≤ 2GB), o que estabelece que paginação e página de assinaturas **devem coexistir**. Mas **não define onde a numeração é posicionada** nem como resolver colisão com o rodapé — esse é o **gap**. Ainda assim a sobreposição é defeito por consequência: se a numeração invade o bloco, o "espaçamento até o texto de 8px" deixa de ser respeitado.
- **Relação com a [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]]** — a 9405 tratou o link **na vertical** e está aprovada em DEV com `deploy: pendente_hml`. Este card é o link da **parte inferior**, ou seja **outro elemento**, não reincidência do mesmo. Duas leituras a confirmar no diagnóstico:
    - O fix da 9405 pode ter sido **pontual** (um elemento) onde a especificação é transversal (todo o rodapé, manual ou automático) — nesse caso os dois são sintomas de a spec não ter sido aplicada globalmente.
    - ⚠️ **Reforça a ressalva já registrada na 9405**: a aprovação dela em DEV foi julgada **a olho, antes de a especificação numérica existir no vault**. Vale medir a 9405 contra os 8px quando ela chegar em HML, em vez de confiar no "parece alinhado".
- **Escopo — um card ou dois?** Registrei os dois defeitos juntos porque o Rafael deu **um único número** e eles dividem a mesma região da folha. Se o diagnóstico mostrar **causas independentes** (espaçamento base × camada de numeração do gerador de PDF), vale separar — o CT-B01 e o CT-B02 já isolam cada um.
- **Vizinhança no download personalizado**: a opção "personalizado" é a mesma família de [[QA Workspace/02 Demandas/HML/6628 - Bug Selecionar Todos Download Documentos Personalizados|SGV-6628]] (selecionar todos no download personalizado) e de [[QA Workspace/02 Demandas/HML/10404 - Bug Download Assinaturas Autenticaveis Ignora Pagina Extra Assinaturas|SGV-10404]] (autenticáveis ignoram a página extra). **Três bugs distintos no mesmo menu de download** — se o time for mexer ali, vale olhar os três juntos.
- Histórico:
    - 2026-07-29 - 🐛 SGV-10457 - Bug cadastrado (espaçamento do rodapé: divergência confirmada contra a spec do QR Code; sobreposição da paginação: gap de posicionamento. Evidência pendente)
