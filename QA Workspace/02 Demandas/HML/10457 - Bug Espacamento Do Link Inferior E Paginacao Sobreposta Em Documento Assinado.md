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

Os dois ocorrem na mesma região da folha, mas em **condições diferentes**: o espaçamento errado aparece no documento assinado **independente de paginação**, enquanto a sobreposição só surge **quando as páginas enumeradas estão ativadas**. Por isso o card cobre os dois cenários separadamente — sem paginação e com paginação — e cada um tem critério e CT próprios.

**Impacto de uso**: o bloco de autenticidade é o que permite a um terceiro conferir se o documento é legítimo. Link cortado, encostado na margem ou coberto pela numeração compromete leitura e escaneamento do QR Code — ou seja, atinge a **função de verificação** do documento, não só a aparência. E como a página de assinaturas é parte integrante do PDF, o problema viaja no arquivo baixado e impresso, fora do sistema.

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

Gravadas em 30/07, uma por cenário — os dois critérios que fecham o escopo têm evidência própria.

**Cenário 1 — espaçamento do link inferior** (sem páginas enumeradas)

![[10457 - cenario 1.mp4]]

**Cenário 2 — paginação sobreposta** (download personalizado com páginas enumeradas)

![[10457 - cenario 2.mp4]]

---

### Resultado Esperado

O documento assinado sai **legível e íntegro no rodapé nos dois cenários** — com e sem a opção de páginas enumeradas:

- O link de verificação e o QR Code aparecem **completos, legíveis e afastados da borda e do conteúdo**, sem corte e sem encostar na margem.
- Com páginas enumeradas, a numeração e o bloco de autenticidade **convivem sem se sobrepor**: dá pra ler a numeração e ler/escanear o link e o QR Code no mesmo arquivo.
- O resultado se sustenta **no arquivo baixado e impresso**, não só na visualização em tela — a doc define que a página de assinaturas "não é apenas visual: torna-se parte integrante do arquivo PDF".

---

### Critérios de aceite

Os dois primeiros critérios são o par que fecha o escopo: **sem paginação** isola o espaçamento do rodapé, **com paginação** isola a colisão. Um pode passar e o outro falhar — por isso são critérios separados.

- [ ] **Sem a opção de páginas enumeradas**: no documento assinado baixado, o link de verificação e o QR Code do rodapé aparecem íntegros e legíveis, afastados da borda da folha e do conteúdo acima, sem corte nem sobreposição
- [ ] **Com a opção de páginas enumeradas** (download personalizado, numeração `1/4`, `2/4`…): a numeração da página e o bloco de autenticidade coexistem **sem sobreposição** — a numeração é legível e o link/QR Code seguem legíveis e escaneáveis
- [ ] O QR Code do rodapé continua **funcional** nos dois cenários: escaneado, abre a verificação de autenticidade do documento
- [ ] A numeração continua **contabilizando as páginas de assinatura** — corrigir o posicionamento não pode regredir essa regra
- [ ] O comportamento é o mesmo em **página extra de assinaturas** e em **assinatura posicionada manualmente**, já que a doc trata o rodapé de autenticidade como regra transversal
- [ ] O resultado se mantém no **arquivo baixado e na impressão**, não apenas na pré-visualização em tela

---

### Casos de Teste Básicos

#### **CT-B01 Rodapé de autenticidade sem páginas enumeradas**

**Dado** que eu tenho um documento assinado com o bloco de autenticidade no rodapé
**E** que a opção de páginas enumeradas **não** está ativada
**Quando** eu baixo o documento e abro o arquivo gerado
**Então** verifico que o link de verificação e o QR Code aparecem íntegros e legíveis, afastados da borda da folha e do conteúdo acima, sem corte

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10457 - cenario 1.mp4]]

---

#### **CT-B02 Rodapé de autenticidade com páginas enumeradas (download personalizado)**

**Dado** que eu tenho um documento assinado
**E** que eu baixo pela opção "personalizado" com páginas enumeradas ativada
**Quando** o arquivo é gerado com a numeração automática (`1/4`, `2/4`…)
**Então** verifico que a numeração e o bloco de autenticidade não se sobrepõem, e que os dois permanecem legíveis no arquivo

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10457 - cenario 2.mp4]]

---

#### **CT-B03 QR Code funcional nos dois cenários**

**Dado** que eu tenho os dois arquivos gerados (com e sem páginas enumeradas)
**Quando** eu escaneio o QR Code de cada um
**Então** verifico que ambos abrem a verificação de autenticidade do documento

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B04 Regressão — numeração inclui as páginas de assinatura**

**Dado** que eu tenho um documento com página extra de assinaturas
**Quando** eu baixo em personalizado com páginas enumeradas
**Então** verifico que a contagem total inclui as páginas de assinatura, conforme a doc do módulo

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B05 Assinaturas posicionadas manualmente**

**Dado** que eu tenho um documento com assinaturas **posicionadas manualmente**, sem página extra
**Quando** o documento é assinado e eu baixo o arquivo, com e sem páginas enumeradas
**Então** verifico que o rodapé de autenticidade se comporta igual ao da página extra, sem sobreposição e sem corte

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B06 Arquivo impresso**

**Dado** que eu tenho o documento assinado baixado nos dois cenários
**Quando** eu imprimo o arquivo
**Então** verifico que o rodapé de autenticidade sai íntegro e legível também no impresso, sem corte na margem

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: **SGV-10457** (número informado pelo Rafael em 29/07).
- ⚠️ **Ambiente inferido como homologação** — é onde o Rafael está validando hoje. Corrigir se foi em DEV.
- **Prioridade não definida** — não foi declarada. Definir na triagem.
- **Gate de doc** (2026-07-29, fluxo 8) contra [[QA Workspace/04 Conhecimento/Módulos/Assinaturas#Página extra de assinaturas (28/04/2026)|Assinaturas § Página extra de assinaturas]]:
    - A doc estabelece que a página de assinaturas **"não é apenas visual: torna-se parte integrante do arquivo PDF"** — logo o rodapé precisa se sustentar no arquivo baixado e impresso, não só em tela. É o que fundamenta o critério de download/impressão.
    - A doc declara **regra transversal**: *"o QR Code e o texto de autenticidade no rodapé valem também para o posicionamento manual"*. O rodapé de autenticidade é obrigação em qualquer configuração de assinatura — daí o CT-B05.
    - A doc afirma que *"se o usuário paginar, a numeração inclui as páginas de assinatura"* (arquivos ≤ 2GB), ou seja **paginação e página de assinaturas devem coexistir**. Mas **não define onde a numeração é desenhada** nem como resolver colisão com o rodapé — **gap**, registrado como dúvida em aberto na doc. A sobreposição contraria a coexistência que a doc pressupõe.
- **Sobre a especificação numérica do QR Code — por que ela não é critério de aceite aqui.** A doc traz uma tabela de handoff (QR de 20×20px; 8px das margens inferior e esquerda; 8px até o texto), vinda do export do Notion processado em 29/07. Ela é **referência de implementação pro dev** e serve pra ele localizar o que ajustar. **Não** foi usada como critério de aceite porque:
    - medir pixel dentro de um PDF não é verificação que a QA faz em caixa preta — o critério ficaria inverificável na prática;
    - o defeito não é "está a 6px em vez de 8px", é "o link sai cortado / coberto e não dá pra usar". O critério tem que descrever o **caso de uso quebrado**, senão a discussão com o dev vira aritmética de margem em vez de função do documento.

    Se em algum momento a régua exata for necessária (ex.: dev alegar que está conforme), a tabela está na doc pra sustentar a conversa — mas o aceite se dá pelo comportamento observável.
- **Relação com a [[QA Workspace/02 Demandas/HML/9405 - Bug Desalinhamento Link QR Code Página Assinatura Separada|SGV-9405]]** — a 9405 tratou o link **na vertical** e está aprovada em DEV com `deploy: pendente_hml`. Este card é o link da **parte inferior**, ou seja **outro elemento**, não reincidência do mesmo. Duas leituras a confirmar no diagnóstico:
    - O fix da 9405 pode ter sido **pontual** (um elemento) onde a especificação é transversal (todo o rodapé, manual ou automático) — nesse caso os dois são sintomas de a spec não ter sido aplicada globalmente.
    - ⚠️ **Reforça a ressalva já registrada na 9405**: a aprovação dela em DEV olhou **um elemento** (o link na vertical). Quando ela chegar em HML, conferir o **rodapé inteiro** nos dois cenários de paginação — não só o elemento que originou o ticket. Se o link de baixo estava quebrado o tempo todo, "aprovado" ali significou aprovado parcialmente.
- **Escopo — um card ou dois?** Registrei os dois defeitos juntos porque o Rafael deu **um único número** e eles dividem a mesma região da folha. Se o diagnóstico mostrar **causas independentes** (espaçamento base × camada de numeração do gerador de PDF), vale separar — o CT-B01 e o CT-B02 já isolam cada um.
- **Vizinhança no download personalizado**: a opção "personalizado" é a mesma família de [[QA Workspace/02 Demandas/HML/6628 - Bug Selecionar Todos Download Documentos Personalizados|SGV-6628]] (selecionar todos no download personalizado) e de [[QA Workspace/02 Demandas/Concluídas/10404 - Bug Download Assinaturas Autenticaveis Ignora Pagina Extra Assinaturas|SGV-10404]] (autenticáveis ignoram a página extra). **Três bugs distintos no mesmo menu de download** — se o time for mexer ali, vale olhar os três juntos.
- Histórico:
    - 2026-07-29 - 🐛 SGV-10457 - Bug cadastrado (espaçamento do rodapé: divergência confirmada contra a spec do QR Code; sobreposição da paginação: gap de posicionamento. Evidência pendente)
