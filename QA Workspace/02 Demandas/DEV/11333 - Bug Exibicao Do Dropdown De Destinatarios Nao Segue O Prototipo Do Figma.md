---
tags:
  - bug
  - qa
  - despachos
task: "11333"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-04
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despachos
ambiente: DEV
---
# Exibição do dropdown de múltiplos destinatários/cópia no despacho não segue o protótipo do Figma

### Descrição

Durante validação foi identificado que o campo "e mais *qtd* destinatário(s)" do despacho — e o equivalente "com cópia para *qtd*" quando há múltiplos em cópia — não exibe o dropdown de acordo com o protótipo do Figma. Hoje está despadronizado: mostra padrões diferentes entre si pra cada tipo de entidade (cidadão PF, cidadão PJ, departamento, setor, servidor) no mesmo dropdown, quando cada tipo deveria seguir o próprio padrão fixo definido no protótipo.

---

### Passo a passo para reproduzir

**Dado** que um despacho tem múltiplos destinatários (ou múltiplos em cópia), com tipos diferentes entre eles (cidadão PF, cidadão PJ, departamento, setor, servidor)
**Quando** o dropdown "e mais *qtd* destinatário(s)" e "com cópia para *qtd*) é expandido
**Então** verifico que a exibição de cada item não segue o padrão fixo por tipo definido no protótipo do Figma — os padrões aparecem misturados/inconsistentes entre os tipos

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://11333)

![[11333 - Divergência prototipo figma, multiplos destinárarios e múltiplos em cópia.mp4]]

---

### Resultado Esperado

Protótipo: [Figma — Refatoração Pessoa Jurídica (Interno/Externo)](https://www.figma.com/design/fgpK9HLfUsaQJm6vx9iocF/Refatora%C3%A7%C3%A3o-Pessoa-Jur%C3%ADdica--Interno---Externo-?node-id=518-15273)

![[11333 - Figma.png]]

Cada tipo de entidade no dropdown segue seu próprio padrão fixo de exibição (avatar + string), sem se misturar com o padrão de outro tipo:

| Tipo | Padrão de exibição no dropdown |
|---|---|
| Cidadão PF | Nome completo |
| Cidadão PJ | Nome de exibição (Cargo) |
| Departamento | Nome do departamento |
| Setor | Sigla · Nome do setor |
| Servidor | Sigla · Nome do servidor |

Quando o texto do item for extenso, **sempre trunca na 2ª linha**, mantendo a mesma sequência de string até o ponto de corte (mesma regra de truncamento já registrada nos CTs de departamento da [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]], CT-012a) — o callout do Figma reforça: "sempre será truncada na segunda linha".

---

### Critérios de aceite

- [ ] Cidadão PF aparece no dropdown com o próprio padrão (nome completo), sem se misturar com o de outro tipo
- [ ] Cidadão PJ aparece no dropdown com o próprio padrão (nome de exibição + cargo entre parênteses)
- [ ] Departamento aparece no dropdown com o próprio padrão (nome do departamento)
- [ ] Setor aparece no dropdown com o próprio padrão (sigla · nome do setor)
- [ ] Servidor aparece no dropdown com o próprio padrão (sigla · nome do servidor)
- [ ] Item extenso, de qualquer tipo, sempre trunca na 2ª linha, mantendo a mesma sequência de string até o corte

---

### Casos de Teste Básicos

#### **CT-B01 Cidadão PF no dropdown segue o próprio padrão**

**Dado** que um despacho tem múltiplos destinatários/cópias, incluindo um cidadão PF
**Quando** o dropdown "e mais $qtd" (ou "com cópia para") é expandido
**Então** o cidadão PF aparece com o nome completo, no padrão do protótipo

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11333 - Divergência prototipo figma, multiplos destinárarios e múltiplos em cópia.mp4]]

---

#### **CT-B02 Cidadão PJ no dropdown segue o próprio padrão**

**Dado** que um despacho tem múltiplos destinatários/cópias, incluindo um cidadão PJ
**Quando** o dropdown é expandido
**Então** o cidadão PJ aparece como "Nome de exibição (Cargo)", no padrão do protótipo

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11333 - Divergência prototipo figma, multiplos destinárarios e múltiplos em cópia.mp4]]

---

#### **CT-B03 Departamento no dropdown segue o próprio padrão**

**Dado** que um despacho tem múltiplos destinatários/cópias, incluindo um departamento
**Quando** o dropdown é expandido
**Então** o departamento aparece com o nome do departamento, no padrão do protótipo

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11333 - Divergência prototipo figma, multiplos destinárarios e múltiplos em cópia.mp4]]

---

#### **CT-B04 Setor no dropdown segue o próprio padrão**

**Dado** que um despacho tem múltiplos destinatários/cópias, incluindo um setor
**Quando** o dropdown é expandido
**Então** o setor aparece como "Sigla · Nome do setor", no padrão do protótipo

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11333 - Divergência prototipo figma, multiplos destinárarios e múltiplos em cópia.mp4]]

---

#### **CT-B05 Servidor no dropdown segue o próprio padrão**

**Dado** que um despacho tem múltiplos destinatários/cópias, incluindo um servidor
**Quando** o dropdown é expandido
**Então** o servidor aparece como "Sigla · Nome do servidor", no padrão do protótipo

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11333 - Divergência prototipo figma, multiplos destinárarios e múltiplos em cópia.mp4]]

---

#### **CT-B06 Item extenso sempre trunca na 2ª linha**

**Dado** que um item do dropdown (de qualquer tipo) tem texto extenso
**Quando** o dropdown é exibido
**Então** o texto trunca sempre na 2ª linha, mantendo a mesma sequência de string até o ponto de corte

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]] — mesmo mecanismo de truncamento do CT-012a, mas o bug aqui é mais amplo (afeta os 5 tipos de entidade do dropdown de destinatário/cópia do despacho, não só departamento).
- Observações:
    - Gate de doc: não existe seção no `04 Conhecimento/Módulos/Despachos.md` documentando o padrão de exibição por tipo de entidade no dropdown de destinatário/cópia — pendência de importar essa regra do Figma pra doc quando este bug for corrigido (fluxo 8).
    - CT-B03 e CT-B06 reprovados, confirmados com evidência dedicada em [[QA Workspace/02 Demandas/DEV/11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]] (defeito da SGV-11184, achado com cidadão de nome extenso — campo de busca sem limite de truncamento, despacho trunca já na 1ª linha em vez da 2ª).
    - Versão/ambiente exato (qual container `dev-*`) não informado — pendência preencher.
    - Evidência principal (vídeo da divergência) compartilhada com [[QA Workspace/02 Demandas/Concluídas/10784 - Bug Destinatarios Em Copia De Despacho Divergente Do Prototipo|SGV-10784]] — cópia renomeada, usada lá como reteste da aprovação em homologação.
- Histórico:
    - 2026-09-04 - 🐛 Bug cadastrado (achado na validação, evidência e protótipo Figma no vault)
    - 2026-09-04 - 🔎 CT-B03/CT-B06 confirmados com evidência dedicada, registrada como defeito da SGV-11184: [[QA Workspace/02 Demandas/DEV/11338 - Defeito Truncamento De Destinatario Com Nome Extenso Nao Segue O Prototipo|SGV-11338]]
