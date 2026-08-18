---
tags:
  - qa
  - skill
---
# Skill: Criação de Casos de Teste

Criar e organizar casos de teste seguindo o padrão utilizado pelo QA. ([Template](../Templates/Casos de teste.md))

## Objetivos

- Garantir cobertura funcional
- Validar regras de negócio
- Facilitar execução manual
- Padronizar documentação de testes

## Estrutura Padrão

Mesmo formato dos CTs embutidos em cards de bug ([[SKILL_BUGS|SKILL_BUGS]]) — um padrão único de CT em todo o vault, o que muda é só a numeração (CT-001 na nota avulsa, CT-B01 no card de bug):

```markdown
### **CT-001 Nome do Cenário**

**Dado** ...
**Quando** ...
**Então** ...

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---
```

**Cada CT é um cabeçalho, não um item de lista.** Isso é o que faz ele aparecer no outline da nota, dobrar/desdobrar sozinho e ser linkável por `[[nota#CT-001 ...]]`.

| Elemento | Regra |
|---|---|
| Cabeçalho | `### **CT-NNN Título**` em **nota avulsa**; `#### **CT-BNN Título**` dentro de card, pra ficar **aninhado** sob `### Casos de Teste Básicos` em vez de virar irmão de Descrição/Evidências |
| Palavra-chave | `**Dado**` / `**E**` / `**Quando**` / `**Então**` em **negrito**, uma por linha, sem bullet e sem indentação |
| Execução | `**Execução Passou?**` em negrito, seguido de `- [ ] Sim` / `- [ ] Não` — **texto puro, sem `<span>` colorido** |
| Evidências | `**Evidências de Testes:**` em negrito; o embed vem depois, em linha própria |
| Separador | `---` entre CTs |

> [!note]- Por que mudou (30/07/2026)
> O formato anterior era um item de lista com tudo indentado como continuação (`- **CT-001 ...**` + linhas indentadas + `<span>` verde/vermelho). Funcionava, mas: não entrava no outline, dificultava dobrar CT por CT numa nota com 12 casos, e o HTML inline atrapalhava a leitura no modo edição. Rafael passou o formato desejado em 30/07 e o padrão foi trocado. Amostra viva: [[QA Workspace/02 Demandas/Concluídas/10437 - Bug Nao Entra No Documento Criado E Redireciona Pra Mesa De Trabalho|SGV-10437]].

---

## Regras

### Numeração

Utilizar:

CT-001
CT-002
CT-003

Mantendo sequência dentro da demanda.

### Título

Descrever claramente o cenário validado.

Exemplos:

- Visualizar permissão de desbloqueio na criação de Servidor
- Salvar permissões de desbloqueio na edição de Servidor
- Exibir status Bloqueado na listagem de usuários

### Escrita

Utilizar padrão:

Dado que...
Quando...
Então...

Evitar:

- Linguagem técnica excessiva
- Explicações longas
- Múltiplos cenários no mesmo caso

### Cobertura

Sempre avaliar:

- Fluxo principal
- Fluxos alternativos
- Regras de negócio
- Permissões
- Persistência de dados
- Exibição de informações
- Cenários negativos quando aplicável

### Completude (contrato com os critérios de aceite)

Antes de dar os CTs por prontos, casar **CT ↔ critério** do card:

- **Cada critério de aceite** tem ao menos **1 CT** que o exercita.
- **Cada CT** amarra em pelo menos um critério (CT que não valida nenhum critério: remover ou justificar).
- Nenhum critério fica descoberto — se faltar, escrever o CT antes de seguir pra validação.
- **Critério com estado que liga/desliga o defeito rende um CT por estado**, e cada um recebe **sua própria evidência** — regra completa em [[SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]]. Precedente: SGV-10457, com um CT sem páginas enumeradas e outro com, cada um embedando a gravação do seu cenário.
- **CT não verifica medida de handoff** (px, hex, token de espaçamento): o `Então` diz "íntegro e legível, sem sobreposição", não "a 8px da margem". Medida de especificação é referência pro dev, não passo de teste de caixa preta.

### Três estados de execução

O "Execução Passou?" tem **três** opções, não duas:

```markdown
**Execução Passou?**
- [ ] Sim
- [ ] Não
- [x] Não se aplica
```

**"Não se aplica"** é para CT cuja **pré-condição é inalcançável** — não é "não testei ainda" (isso é deixar em branco) nem "passou". Ao marcar, explicar em callout fechado logo abaixo **por que** é inalcançável e o que aconteceria se o produto mudasse:

```markdown
> [!info]- Por que não se aplica
> <o que torna a pré-condição impossível>. O critério segue válido como regra —
> está satisfeito **por construção**, não por teste. Se <mudança no produto>,
> este CT volta a ser executável.
```

O critério de aceite correspondente **não é marcado como aprovado**: ele fica desmarcado com a nota `*(satisfeito por construção — ver CT-NNN)*`. Aprovar critério que não foi exercitado é registro falso.

Precedente: SGV-9042, CT-003 — documento com fluxo não iniciado não emite despacho, então a tela onde o contêiner apareceria não existe.

### CT que reprovou e depois passou — callout de reconciliação

Quando um CT vai de `Não` pra `Sim` porque o **defeito que ele encontrou foi corrigido**, a marcação nova sozinha apaga a história: quem lê o card depois vê um CT aprovado e não sabe que ele já reprovou, nem que existe um card de defeito por trás. Marcar `Sim` e seguir é perder o rastro.

Ao reconciliar, **marcar `Sim` e abrir callout fechado** logo abaixo:

```markdown
> [!success]- Reprovado em <data>, aprovado no reteste de <data>
> O defeito virou [[card|SGV-XXXX]], foi corrigido e o reteste passou —
> gravação da execução de <data> embedada abaixo, junto com a evidência
> que registrou o problema original. O card do defeito está em `Concluídas/`.
```

Regras:
- O callout **linka o card do defeito** — é o que liga o CT ao registro do problema
- Cita **as duas datas**: quando reprovou e quando passou
- **As duas evidências convivem**: a do problema original e a do reteste. A do reteste não substitui a outra — juntas elas contam o ciclo
- O callout é **fechado** (`-`), pelo mesmo motivo dos Detalhes: bater o olho mostra CT aprovado; expandir mostra a história

**Precedente**: SGV-3234, 17/08 — CT-012, CT-017, CT-018 e CT-029 passaram de `Não` pra `Sim` depois que os defeitos SGV-10831, SGV-10842, SGV-10832 e SGV-10844 foram corrigidos. O padrão foi praticado ali antes de existir esta regra.

Ciclo completo do defeito: [[../Contexto/FLUXOS#3i. Defeito (filho de task pai)|FLUXOS → 3i]] · [[../Contexto/PADROES_QA#Defeito × Bug|PADROES_QA → Defeito × Bug]].

### Caso retirado do escopo — grupo de registro

CT **retirado ou adiado** depois de escrito não vira buraco na numeração nem desaparece. Vai pra uma seção no **fim** do card, com tabela de caso × decisão × motivo:

```markdown
### G. Fora de execução — registro

*Casos considerados e deliberadamente não executados nesta rodada. Ficam aqui pra
não sumirem do histórico e pra não abrirem buraco na numeração dos ativos.*

| Caso | Decisão | Motivo |
|---|---|---|
| <título do caso> | **Retirado** / **Adiado** / **Removido — não se aplica** (quem, quando) | <por que, com o que muda se voltar> |
```

Os CTs ativos são **renumerados pra ficarem contíguos** — e as evidências são renomeadas **no mesmo movimento** ([[../../QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]]). Precedente: SGV-9042, grupo G com 4 casos e renumeração de 26 → 21 CTs.

### Evidências de Testes

Mesmo processo de qualquer evidência do vault — ver [[../../QA Workspace/Evidências/README|Evidências/README]]. Vale pra caso de teste tanto quanto pra bug.

## Resultado Esperado

Retornar uma lista organizada de casos de teste pronta para execução.