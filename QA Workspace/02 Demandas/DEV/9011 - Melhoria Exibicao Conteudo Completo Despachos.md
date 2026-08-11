---
tags:
  - demanda
  - qa
  - despacho
task: "9011"
status: dev
prioridade: media
mel: ""
data_inicio: 2026-08-11
data_fim: ""
responsavel: Rafael
modulo: despacho
---
# Demanda: Melhoria na exibição de conteúdo completo de despachos

> [!info] Informações
> - **Tipo:** Melhoria (CX)
> - **Status:** DEV — **Reaberto** (reaberta em 11/08/2026)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-9011 no Notion](https://app.notion.com/p/alfa-group/Melhoria-CX-Melhoria-na-exibi-o-de-conte-do-completo-de-despachos-36f2aec67d3081cc9719c33e9ca4422d) · Figma — Tramitação/Handoff: [nó 8601-2511](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8601-2511)
> - **Dev:** B. Luan · **Revisores MR:** Marcos Vinicius, Gabriel Desidério
> - **CX responsável:** Edivaldo Lima · **Design:** Ivo Costa, Fernando Junior, Edu, Vinícius
> - **Cliente(s) afetado(s):** Todos · **Projeto:** Sustentação · **Funcionalidade afetada:** Despacho
> - **Progresso de subitens:** 83,33% · Sprints: SP11, SP12, SP15, SP16, SP17 (2026) · Campo "Versão para deploy" **vazio**

---

> [!abstract] Resumo

Hoje, na visualização de documentos, despacho com muito texto tem o conteúdo **parcialmente ocultado** — o usuário precisa clicar em "Exibir mais" pra ler tudo. O mesmo vale para **anexos**: ficam escondidos até o despacho ser expandido manualmente, então nem dá pra saber que existem sem interagir.

A melhoria pede que o despacho mostre tudo de cara. O que a task lista como escopo (texto literal da solicitação, **não** um refinamento meu):

- Conteúdo textual exibido **integralmente por padrão**, sem "Exibir mais"
- **Anexos** exibidos direto na visualização inicial
- Usuário identifica de imediato **texto, data e hora de emissão e anexos**
- Navegação mais fluida, com menos interações para leitura

Módulo relacionado: [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] · [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]].

---

## Regras de negócio

*Ainda não refinadas neste vault.* O card nasceu **enxuto na reabertura de 11/08/2026**, só para dar rastreabilidade ao ciclo — o escopo acima é transcrição da task, não destilado de refinamento. Pendência de refinar está na fila da daily.

---

> [!warning] Pontos de atenção

- 🔴 **Reaberta em DEV em 11/08/2026** por divergência de protótipo em **3 pontos**: posição do horário do despacho, botão "Exibir detalhes" e alinhamento de "Ver interações". Defeito cadastrado como [[QA Workspace/02 Demandas/DEV/10740 - Bug Divergencias De Prototipo Na Exibicao Do Despacho|SGV-10740]] (fluxo [[Sistema/Contexto/FLUXOS#3g. Reprovação com bug novo (SGV próprio)|3g]]).
- ⚠️ **A task não tem passo a passo nem comportamento esperado preenchidos** — os campos "Passo a passo para reproduzir", "Qual o comportamento apresentado atualmente" e "Qual o comportamento esperado?" estão vazios no Notion. O escopo vive só no campo Descrição.
- ⚠️ **Progresso de subitens em 83,33% e os subitens não vieram no export** — não dá pra saber o que já subiu e o que falta da entrega.
- 🔎 A demanda **arrasta desde a SP11** e já passou por cinco sprints (SP11, SP12, SP15, SP16, SP17), com cinco datas previstas de conclusão sucessivas — a última em 25/08/2026.

---

## Casos de teste

*Nenhum escrito ainda* — o card foi criado na reabertura, sem passar por refinamento. Escrever os CTs a partir dos 4 pontos de escopo é a pendência de refino registrada na daily de 11/08.

---

> [!danger] Bugs encontrados

- [[QA Workspace/02 Demandas/DEV/10740 - Bug Divergencias De Prototipo Na Exibicao Do Despacho|SGV-10740]] - Divergências de protótipo na exibição do despacho (posição do horário, botão "Exibir detalhes" e alinhamento de "Ver interações") — **motivo da reabertura**

---

## Evidências

A evidência da reabertura mora no card do defeito: [[QA Workspace/02 Demandas/DEV/10740 - Bug Divergencias De Prototipo Na Exibicao Do Despacho|SGV-10740]] (`10740 - divergencias de prototipo na exibicao do despacho.png`, em `Evidências/Desenvolvimento/`).

---

> [!tip] Observações

Registro da reabertura no Notion (comentário de 11/08/2026): *"@B. Luan Reaberto em DEV — Defeito cadastrado - 10740"*.

---

## Histórico

- 2026-08-11 - 🔴 Melhoria reaberta em DEV (3 divergências de protótipo; defeito [[QA Workspace/02 Demandas/DEV/10740 - Bug Divergencias De Prototipo Na Exibicao Do Despacho|SGV-10740]] cadastrado)
- 2026-08-11 - Card criado no vault, enxuto, para dar rastreabilidade à reabertura — a demanda existia só no Notion até aqui
