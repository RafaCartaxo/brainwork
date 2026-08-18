---
tags:
  - qa
  - skill
---
# Skill: Criação e Organização de Bugs

Criar, revisar e organizar bugs seguindo o padrão utilizado no Vault QA. ([Template](../Templates/Bug Report.md))

## Objetivos

- Estruturar bugs de forma clara e reproduzível
- Garantir descrição objetiva do problema
- Padronizar redação e formatação
- Facilitar entendimento por Produto, Desenvolvimento e QA
- Garantir rastreabilidade do defeito

## Antes de tudo: é **Bug** ou **Defeito**?

Primeira pergunta, antes de escolher o modo de entrada — porque muda tag, nome do arquivo, frontmatter e esteira inteira.

**O problema saiu da execução de um CT de uma task pai (Melhoria/Funcionalidade), em DEV?**

- **Sim → é Defeito.** Tag `defeito`, arquivo `<SGV> - Defeito <Título>`, `pai: "<SGV da task>"` preenchido. Fecha em `Concluídas/` com `ambiente: DEV`, sem passar por HML. Fluxo completo: [[../Contexto/FLUXOS#3i. Defeito (filho de task pai)|FLUXOS → 3i]].
- **Não → é Bug.** Tag `bug`, arquivo `<SGV> - Bug <Título>`, `pai: ""` vazio. Esteira normal DEV → HML → Concluídas.

Regra completa (incluindo por que o defeito não é retestado em HML): [[../Contexto/PADROES_QA#Defeito × Bug|PADROES_QA → Defeito × Bug]].

> [!important] A fronteira é **origem + ambiente**, não gravidade
> Defeito não é "bug pequeno". Um defeito pode ser grave e um bug pode ser trivial. Problema encontrado em **homologação** é Bug mesmo que a task pai seja a mesma — em HML valida-se a entrega inteira, e o que aparece lá tem vida própria.

Tudo abaixo (modos de entrada, estrutura, regras de escrita) vale para os dois, exceto onde estiver dito o contrário.

## Modos de entrada

Como a task pode chegar, e o que fazer em cada caso antes de aplicar a Estrutura Padrão abaixo:

- **Suspeita própria**: possível bug identificado durante o trabalho, ainda sem confirmação. Nasce como `❓ Suspeita de bug registrada` na daily (+ pendência de investigar). Só vira card **depois** de confirmado na investigação; descartado, vira `🗑️` sem card (trilha completa no catálogo do [[QA Workspace/01 Daily/README|01 Daily/README]]).
- **Relato rápido**: descrição em texto livre (Gherkin ou corrido) + número do SGV. Vai direto pro template, sem trabalho extra.
- **Contexto rico**: quando vier bastante material bruto (histórico, várias rodadas, análise de causa raiz, texto colado de outro lugar). Extrair os campos certos (ambiente, módulo, prioridade, passos, critérios de aceite) sem perder informação. Se algo ficar ambíguo, perguntar antes de assumir — não simplificar. Onde cada peça do material entra no card: ver "Bug com análise" nas Regras abaixo.
- **Via CX**: bug reportado pelo atendimento, normalmente em linguagem de usuário final, sem passo técnico claro. Antes de fechar o card: investigar o código relacionado pra entender o comportamento real (não só confiar na descrição do CX), perguntar o que não ficar claro pra reproduzir. Se mesmo assim não for possível confirmar/reproduzir sozinho, marcar isso em **Observações** ("precisa confirmação") em vez de fechar como se já tivesse validado.

Os três modos convergem no mesmo resultado: card no template certo, na pasta certa (`02 Demandas/<ambiente>/`), registrado em **Bugs encontrados** da daily do dia.

## Estrutura Padrão

# Título

### Descrição

Durante validação foi identificado que...

---

### Passo a passo para reproduzir

Dado que...
E...
Quando...
Então...

---

### Evidências [📁](file:///caminho/da/pasta/do/ambiente/) [🔍](evidencia://<número do card>)


---

### Resultado Esperado

-

---

### Critérios de aceite

- [ ] ...

---

### Casos de Teste Básicos

#### **CT-B01 Título do caso de teste**

**Dado** ...
**E** ...
**Quando** ...
**Então** ...

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente:

---

### Informações adicionais

- Demanda relacionada: SGV-XXXX
- Observações:
- Histórico:
    - YYYY-MM-DD - 🐛 Bug cadastrado

## Regras

### Nome do arquivo do card

| Situação | Nome do arquivo | `task` | `pai` | Tag |
|---|---|---|---|---|
| Bug já cadastrado no Notion (tem SGV) | `<SGV> - Bug <Título>` | `"XXXX"` | `""` | `bug` |
| **Bug confirmado sem SGV ainda** | `Bug <Título>` (sem prefixo numérico) | `""` | `""` | `bug` |
| **Defeito** (reprovou o CT de uma task pai, em DEV) | `<SGV> - Defeito <Título>` | `"XXXX"` | `"<SGV da pai>"` | `defeito` |

No caso sem SGV: evidência vai pra `Evidências/Cadastrar/` (não pra subpasta de ambiente — ver [[../../QA Workspace/Evidências/README|Evidências/README]]), copy da daily é `🐛 Bug confirmado (card criado): [[card]]`, e **entra pendência obrigatória** "obter o SGV, preencher `task` e renomear o card". Quando o número chegar, o botão 🔄 renomeia e reescreve os links sozinho (mesmo mecanismo do `MEL-NNNN → SGV`).

> [!tip] Peça o número antes de criar
> Se a demanda já está no Notion, **pedir o SGV** custa uma pergunta; criar sem ele custa renomear card, `task`, evidência, link `evidencia://`, copy da daily e todos os wikilinks. Só usar a forma sem número quando o bug realmente ainda não foi cadastrado (precedente: SGV-10404, 28/07).

### Título

Deve descrever claramente o problema.

Exemplos:

- CPF exibido com máscara incorreta na impressão
- Campo "Para" não é preenchido em resposta do cidadão
- Documento sigiloso exibe conteúdo na mesa de trabalho

Evitar:

- Erro na tela
- Problema no sistema
- Bug impressão

### Descrição

Explicar o comportamento encontrado.

Utilizar:

"Durante validação foi identificado que..."

Evitar:

- Explicações extensas
- Opiniões pessoais
- Hipóteses técnicas

### Passos

**Sempre em BDD** — não é preferência, é o formato:

```
Dado que ...
E ...
Quando ...
Então ...
```

O `E` é step válido pra encadear pré-condição ou ação (`E Assino o documento`). Mesma gramática dos **Casos de Teste** — ver [[../Templates/Casos de teste|Casos de teste]].

Nunca usar lista numerada (`1. 2. 3.`) nem texto corrido: o passo a passo é o que o dev executa pra reproduzir, e a forma BDD deixa explícito o que é pré-condição, o que é ação e o que é o defeito observado.

Diferença de foco entre as duas seções, que é fácil de trocar:

| Seção | O `Então` descreve |
|---|---|
| **Passo a passo para reproduzir** | o **defeito** — "Então verifico que o arquivo vem sem a página extra" |
| **Casos de Teste** | o **comportamento esperado** — "Então o arquivo vem com a página extra" (e o CT fica marcado `Não` enquanto falha) |

Os passos devem permitir reprodução do problema.

### Resultado Esperado

Descrever claramente o comportamento correto. Ao defini-lo, cruzar contra a doc do módulo ([[SKILL_VERIFICACAO_DOC]]) — a doc respalda o resultado esperado, ou há divergência a registrar.

### Critérios de Aceite

Utilizar quando houver regra de negócio associada. Cada critério é um checkbox (`- [ ] <critério>`), marcado quando confirmado atendido na validação — mesma lógica do "Execução Passou?" dos CTs, mas por critério.

**Critério é o que a QA consegue observar e o que o usuário perde.** Escrever pelo comportamento verificável em caixa preta — "o link aparece íntegro e legível, sem sobreposição", não "o link está a 8px da margem".

**Medida de handoff não é critério de aceite.** Número de especificação (px, hex, token de espaçamento, duração de animação) vem do Figma/Notion pro **dev** implementar. Como critério ele fica inverificável — a QA não mede pixel dentro de um PDF — e desloca a discussão pra aritmética de margem em vez da função quebrada do produto. Registrar a medida em **Informações adicionais como referência**: serve pra localizar o ajuste e pra sustentar a conversa se o dev alegar conformidade.

**Variável que liga e desliga o defeito rende um critério por estado.** Se um estado pode passar e o outro falhar, os dois não cabem no mesmo checkbox — e cada um puxa o seu CT. Ex.: rodapé **sem** paginação isola o espaçamento; **com** paginação isola a colisão.

> [!example]- Precedente: SGV-10457 (29/07/2026)
> O card nasceu com critérios em pixel, copiados da tabela de handoff do QR Code que tinha acabado de entrar na doc de Assinaturas — inclusive porque a importação rotulou aquela tabela como "o critério objetivo pra julgar desalinhamento", glosa que também foi corrigida. Rafael perguntou "de onde vieram os pixels?" e mandou usar critério que reflita caso de uso. Refeito: link íntegro e legível, QR escaneável, sem sobreposição, no arquivo baixado e impresso — tudo ancorado em regra escrita da doc ("a página de assinaturas torna-se parte integrante do arquivo PDF" e o rodapé de autenticidade como regra transversal).

### Evidências

Referenciar vídeos, imagens ou links utilizados na validação. O guia completo de evidências (gravar → renomear → mover → embed, subpastas, links 📁/🔍, gravação compartilhada) está em [[../../QA Workspace/Evidências/README|Evidências/README]].

O título da seção leva dois links de atalho: `### Evidências [📁](file:///caminho/da/pasta/do/ambiente/) [🔍](evidencia://<número do card>)`. Infra do `evidencia://`: [[../../Sistema/Contexto/Plugins Instalados|Plugins Instalados]].

### Casos de Teste Básicos

Detalhar os cenários de validação no padrão Dado/Quando/Então (CT-B01, CT-B02...), com "Execução Passou?" e "Evidências de Testes" por caso.

**Cada CT é um cabeçalho `#### **CT-BNN Título**`**, não um item de lista — assim entra no outline do card e dobra sozinho. O `####` é deliberado: mantém o CT **aninhado** sob `### Casos de Teste Básicos` em vez de virar irmão de Descrição/Evidências. Palavras-chave em negrito (`**Dado**`, `**E**`, `**Quando**`, `**Então**`), uma por linha, sem bullet e sem indentação. `**Execução Passou?**` seguido de `- [ ] Sim` / `- [ ] Não` em **texto puro, sem `<span>` colorido**. `---` entre CTs. Formato completo e o porquê da mudança (30/07/2026) em [[SKILL_CASOS_DE_TESTE#Estrutura Padrão|SKILL_CASOS_DE_TESTE]], que traz também os **três estados de execução** (`Sim` / `Não` / `Não se aplica`) e o grupo **`Fora de execução — registro`**, pra caso retirado do escopo depois de escrito — que não vira buraco na numeração nem desaparece.

### Informações adicionais

O **Histórico** registra cada etapa vivida pelo card, com a frase padrão prefixada pela data (`- YYYY-MM-DD - <frase com emoji>` — mesma copy do [[../../QA Workspace/01 Daily/README|01 Daily/README]]). O card nasce com a primeira linha: `🐛 Bug cadastrado` quando já tem SGV; `🐛 Bug confirmado (card criado)` quando ainda não tem.

### Bug com análise (causa raiz)

Quando o bug vem acompanhado de análise, a análise **não entra no card**. Ela mora na mesa de trabalho do `05 Refinar/` (template [[../Templates/Refinamento.md|Refinamento.md]]). O card nasce **destilado** — só o problema, reprodução, resultado esperado, critérios e CTs. O fluxo completo de refinamento está em [[../../QA Workspace/05 Refinar/README|05 Refinar/README]] e no [[../Contexto/FLUXOS#6. Refinar demanda já cadastrada|FLUXOS (fluxo 6)]].

O que sobra da análise no card:
- **Observações**: wikilink pro arquivo de refinamento em `04 Conhecimento/`
- **Critérios de aceite**: incluir dados já corrompidos/afetados e regressão do fluxo normal
- **Histórico**: `- YYYY-MM-DD - Análise de causa raiz (<quem>): <síntese curta>`
- **Evidência externa** (Notion): anotar na seção Evidências **onde ela está**, sem cópia local
- **Na daily**: `🔎` pra cada rodada, `📝` pro destilado, `📤` pro Notion (catálogo em [[../../QA Workspace/01 Daily/README|01 Daily/README]])

## Resultado Esperado

Retornar o bug pronto para registro no Notion ou ferramenta equivalente.