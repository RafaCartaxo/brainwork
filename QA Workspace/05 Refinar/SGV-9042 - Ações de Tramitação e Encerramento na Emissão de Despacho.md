---
tags:
  - qa
  - refinamento
task: "9042"
status: em_refinamento
data_inicio: 2026-07-29
responsavel: Rafael
modulo: tramitacao
---
# Refinamento: Ações de Tramitação e Encerramento na Emissão de Despacho

> [!info]- Mesa de trabalho — [[Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada|fluxo 6]]
> Análise e suposição vivem aqui — o card em `02 Demandas/` nasce do **Destilado**, limpo. Ao concluir: análise → Notion (`📤`), card criado (`📝`), este arquivo → `04 Conhecimento/` (`status: refinado`).

## O problema (task no Notion)

**Tipo**: Melhoria-CX · **Status no Notion**: Testando em homologação · **Prazo de conclusão**: 31/07/2026
**Designers**: Ivo Costa, Edu, Vinícius · **Devs**: Gabriel Desidério, Lucas Cabral · **Revisor MR**: Gabriel Desidério, Marcos Vinicius · **QA responsável**: *vazio no Notion*
**Sprints**: SP11/SP12/SP13 (Product designer) → SP15 Engenharia (Melhorias) → Sprint SGA 24/07-31/07
[Task no Notion](https://app.notion.com/p/alfa-group/MELHORIA-CX-Adicionar-tarefas-na-barra-de-ferramentas-na-cria-o-de-um-despacho-3722aec67d3081d8ba12d56fc6387c5b)

**Objetivo** — Evolução da tela de Emissão de Despacho: permitir que o usuário **defina o destino do documento no mesmo momento em que faz o despacho**, em vez de emitir e depois tramitar num segundo passo. Abrange documentos avulsos (sem fluxo) e estruturados (com fluxo), respeitando permissões, obrigatoriedade de metadados e assinatura legal.

**Escopo por tipo de documento** — na emissão aparece um painel **Ações de Destino**:

| Ação | Sem fluxo de trabalho | Com fluxo de trabalho | O que faz |
|---|---|---|---|
| **Encerrar no Setor** | ✅ | ✅ | Status vai pra Encerrado, **mantendo a custódia no setor atual** |
| **Encerrar na Mesa** | ✅ | ✅ | Status vai pra Encerrado, **removendo da fila de pendências gerais** e arquivando na mesa virtual do usuário logado |
| **Avançar Etapa** | — | ✅ | Move pra próxima etapa (ou etapas) previstas no fluxo |
| **Retroceder Etapa** | — | ✅ | Retorna a uma etapa anterior do processo |

**Saída atual** — a definição de destino não acontece na emissão; é ação separada depois de emitir.

**Entrega do dev** — sem MR citado no export. Status "Testando em homologação" sugere entrega já disponível; **confirmar o MR com Gabriel Desidério / Lucas Cabral** antes de validar.

---

## Análise

- **A própria spec declara 4 regras de negócio como pendentes de validação** (seção 3 do documento original): permissão para tramitação, pulo para tramitação, obrigatoriedade de despacho e obrigatoriedade de assinatura. Vêm como **títulos sem conteúdo** — não há regra escrita. Por isso este material foi pra mesa em vez de virar card direto: escrever critério de aceite aqui seria inventar regra.

- **Gate de doc (2026-07-29)** — cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] (importada hoje) e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]]:

  | Ação da spec | Respaldo na doc | Situação |
  |---|---|---|
  | Avançar / Retroceder Etapa | Workflow: *"**Setores que podem avançar ou retroceder** (obrigatório) — default: todos os participantes"* | ✅ Existe regra de permissão documentada — **base parcial pro ponto "regra de permissão para tramitação"** |
  | Encerrar no Setor | Tramitação (~15/06/2026): setor responsável pode *"encerrar no seu setor sem encerrar a tramitação do documento como um todo"*, equiparando-se a setor participante | ⚠️ Conceito existe, mas a regra documentada fala do **setor responsável**; a spec da 9042 não diz se herda esse escopo ou vale pra qualquer setor |
  | Encerrar na Mesa | **Nada** em nenhum módulo | 🔴 **Conceito novo, não documentado** — "arquivar na mesa virtual do usuário logado, removendo da fila de pendências gerais" não existe na doc |
  | Pulo de etapa | **Nada** — nem em Workflow nem em Tramitação | 🔴 Não documentado, e é um dos 4 pontos em aberto |

  **Leitura**: metade das ações tem lastro documental (avançar/retroceder e, parcialmente, encerrar no setor); a outra metade é conceito novo. Isso não bloqueia o refinamento, mas define onde a resposta do responsável é indispensável — e o que precisará ser **escrito na doc de Tramitação** depois que a regra for definida.

- **Relação com a SGV-6373** (reaberta em DEV, 27/07): aquele bug é justamente "setores das Regras de tramitação não são mantidos ao avançar/retroceder etapas na criação de A&S". A 9042 **adiciona** avançar/retroceder num novo ponto de entrada (a emissão de despacho). Se a 6373 não estiver corrigida, a 9042 pode herdar o mesmo defeito por outro caminho — testar as duas em conjunto.

---

### Rodada 2 — regras extraídas do Figma (29/07)

> [!important] Procedência: **Figma — Tramitação/Handoff, página `[SGV-9042]`** (lido em 29/07/2026)
> Fonte **mais atualizada que o Notion**, por orientação do Rafael. Autores das anotações: **Edu** e **Vinícius** (post-its tipo "Orientação"). Onde o Figma diverge do export do Notion, **o Figma vale** — as divergências estão marcadas abaixo.

**Elegibilidade — quando o contêiner existe** (Edu):
> "O contêiner 'Próximo passo do documento' só existe em documentos que possuem fluxo de trabalho configurado **e com o fluxo já iniciado**. Fluxo não iniciado não pode ser movimentado nem encerrado — nesse estado o contêiner não é exibido e vale a toolbar de fluxo não iniciado. Documentos sem workflow seguem o layout padrão do despacho, sem este contêiner."

**Regra mestra de movimentação** (Vinícius):
> "Não é permitido ter movimentações de etapa caso esta possua alguma pendência. **Mesmo que a ação premeditada seja de retroceder a etapa.**"

**Obrigatoriedade de despacho e de assinatura — o mecanismo é o mesmo** (Edu):
> "Com qualquer ação obrigatória pendente na etapa (**despacho customizado não emitido** ou **assinatura não concluída**), o select de movimentação fica desabilitado, fixo em 'Permanecer na etapa atual', com tooltip informando a pendência. **Retroceder ou encerrar nesse estado só pela toolbar do documento.** O select habilita quando todas as pendências forem cumpridas."

Tooltip do estado desabilitado (texto literal da UI):
> "Esta ação só esta disponível ao concluir as ações obrigatórias da etapa atual." *(o "esta" sem acento é do original — vale reportar como typo de copy)*

**Regra de pulo = "atalhos"** (Edu, frame "Etapa com atalhos configurados"):
> "Com qualquer ação obrigatória pendente na etapa atual (...), o select de movimentação fica desabilitado **por completo**, fixo em 'Permanecer na etapa atual' — **inclui avançar, retroceder e todos os atalhos, nas duas direções**."

**Assinatura muda o número de cliques** (Edu):
> "O split button permanece com as opções atuais (**Emitir / Emitir e Assinar**). **Atenção**: se o despacho exigir assinaturas, **o avanço não pode ser concluído no mesmo clique**, pois as solicitações são disparadas após a emissão."

**Encerramento — as duas dimensões são independentes** (Edu):
> "Movimentação do fluxo e comportamento do documento são decisões **independentes e combináveis**: é possível, por exemplo, 'Avançar etapa' + 'Encerrar para mim' na mesma emissão. Todas as regras de tramitação referentes a **continuar aberto, encerrar para mim ou encerrar para meu setor** devem ser respeitadas **conforme já implementado na plataforma**."

**Sigilo** (Edu):
> "O grupo de sigilo só aparece quando o despacho possui opções de sigilo. Em despachos customizados de etapa, isso é herdado da configuração do módulo, serviço e/ou assunto — **o fluxo de trabalho não configura sigilo**."

#### ⚠️ Divergência de nomenclatura Notion × Figma

| Export do Notion (spec) | Figma (mais atual) |
|---|---|
| "Encerrar no Setor" | **"Encerrar para meu setor"** |
| "Encerrar na Mesa" | **"Encerrar para mim"** |
| — | **"Continuar aberto"** (3ª opção, ausente na spec do Notion) |

E o mais importante: o Figma diz que essas regras **já estão implementadas na plataforma** — ou seja, "Encerrar na Mesa" **não é conceito novo**, é a regra existente de encerramento com outro rótulo. Isso derruba a suposição da rodada 1 de que era comportamento inédito e não documentado.

#### Estados de UI mapeados (viram CTs)

| Estado | Comportamento |
|---|---|
| `Select disable` | Select fixo em "Permanecer na etapa atual", desabilitado, com tooltip da pendência |
| `Tooltip - Disable` | Exibe o texto da pendência ao passar o mouse no ⓘ |
| `Double-select` | Etapa com atalhos configurados — select de movimentação com as opções de atalho |
| `Select-disable` (seção atalho) | Atalhos também desabilitados por completo quando há pendência |

## Pontos a definir

- [x] ~~**(Declarado pela spec) Regra de permissão para tramitação**~~ → **RESPONDIDO pelo Figma**: elegibilidade = documento com fluxo **configurado e já iniciado**; fluxo não iniciado não move nem encerra (vale a toolbar de fluxo não iniciado). Movimentação bloqueada com qualquer pendência na etapa, **inclusive retroceder**.
- [x] ~~**(Declarado pela spec) Regra de pulo para tramitação**~~ → **RESPONDIDO pelo Figma**: "pulo" = **atalhos** configurados na etapa. Com pendência, o select desabilita **por completo — avançar, retroceder e todos os atalhos, nas duas direções**.
- [x] ~~**(Declarado pela spec) Obrigatoriedade de despacho**~~ → **RESPONDIDO**: despacho customizado **não emitido** é pendência e desabilita o select.
- [x] ~~**(Declarado pela spec) Obrigatoriedade de assinatura**~~ → **RESPONDIDO**: assinatura **não concluída** é pendência e desabilita o select. Além disso, se o despacho exigir assinatura, **o avanço não se conclui no mesmo clique** — as solicitações disparam após a emissão.
- [x] ~~**"Encerrar na Mesa" precisa de definição de regra e de doc**~~ → **RESOLVIDO**: no Figma chama-se **"Encerrar para mim"** e as regras "devem ser respeitadas conforme **já implementado na plataforma**" — não é conceito novo, é a regra de encerramento existente com outro rótulo.

**Ainda abertos:**

- [ ] **Confirmar a nomenclatura final com o time** — Notion diz "Encerrar no Setor / na Mesa", Figma diz "Encerrar para meu setor / para mim" + "Continuar aberto". Qual vai pra tela? O CT precisa do rótulo correto, e a doc de Tramitação precisa registrar o vocabulário oficial.
- [ ] **MR da entrega** — nem o export nem o Figma citam MR, e o Notion já marca "Testando em homologação". Confirmar com Gabriel Desidério / Lucas Cabral.
- [ ] **Interação com a SGV-6373** — validar se o bug de setores não mantidos ao avançar/retroceder afeta este novo ponto de entrada.
- [ ] **Combinações de encerramento × movimentação** — o Figma garante que são independentes e combináveis ("Avançar etapa" + "Encerrar para mim"). Mapear a matriz de combinações válidas pros CTs, porque "todas as regras já implementadas" é uma remissão genérica que não lista os casos.
- [ ] **Typo de copy pra reportar**: o tooltip diz *"Esta ação só **esta** disponível..."* — falta o acento em "está". Vale abrir como ajuste de copy (ou incluir no card).

> [!tip] Fonte a consultar antes da próxima rodada
> **[Figma — Tramitação/Handoff](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8765-2765)** (indicado pelo Rafael em 29/07): os tooltips e anotações do Figma **são mais atualizados que o Notion** e referenciam boa parte das regras desta mesa. É a fonte mais promissora pra fechar os 4 pontos declarados pela spec e definir "Encerrar na Mesa".
> Ao trazer conteúdo de lá, **marcar a procedência** (Figma vs Notion) — se um dia divergirem, tem que ser rastreável qual regra veio de onde.

---

## Destilado (rascunho do card)

> [!abstract] Só o problema — o que vai pro card, quase copy-paste: Descrição objetiva, passo a passo, resultado esperado, critérios de aceite, CTs. Nada de análise ou suposição.

> [!tip] Desbloqueado em 29/07 — pronto pra destilar
> As 4 regras que a spec declarava pendentes foram respondidas pelas anotações do Figma (rodada 2). O que resta em aberto (nomenclatura final, MR, matriz de combinações) **não impede** escrever os critérios de aceite do comportamento principal — impede só fechar o rótulo dos botões.
> Próxima rodada: destilar + escrever um CT por critério, deixando o rótulo como variável a confirmar.

### Descrição

### Passo a passo para reproduzir

### Resultado Esperado

### Critérios de aceite

- [ ] ...

### Casos de Teste Básicos

---

## Histórico do refinamento

- 2026-07-29 - Material recebido (export do Notion `SGV-9042.md`) e organizado na mesa. Rota **Modo A** (mesa) e não card direto: a seção 3 da spec declara 4 regras de negócio pendentes de validação, sem conteúdo.
- 2026-07-29 - 🔎 Análise (1ª): gate de doc cruzado contra [[QA Workspace/04 Conhecimento/Módulos/Tramitação|Tramitação]] (importada hoje) e [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)|Workflow]]. Avançar/retroceder tem regra de permissão documentada; "Encerrar no Setor" tem conceito parcial (regra de 15/06 fala do setor responsável); **"Encerrar na Mesa" e pulo de etapa não estão documentados em nenhum módulo**. 7 pontos mapeados em Pontos a definir. Destilado bloqueado.
- 2026-07-29 - 🔎 Análise (2ª, [Figma Tramitação/Handoff](https://www.figma.com/design/ikWmC65IpdQRkx5WACE7en/Tramita%C3%A7%C3%A3o---Handoff?node-id=8765-2765) — fonte indicada pelo Rafael como mais atual que o Notion): **as 4 regras que a spec declarava pendentes foram respondidas** pelas anotações de Edu e Vinícius. Elegibilidade (fluxo configurado **e iniciado**), regra mestra (pendência bloqueia movimentação, inclusive retroceder), obrigatoriedade de despacho e de assinatura (mesmo mecanismo: select desabilitado + tooltip), e "pulo" = **atalhos**, também bloqueados por completo nas duas direções. **Divergência de nomenclatura registrada**: o Figma usa "Encerrar para mim / para meu setor / Continuar aberto" contra "Encerrar na Mesa / no Setor" do Notion — e afirma que essas regras **já estão implementadas na plataforma**, o que derruba a suposição da rodada 1 de que "Encerrar na Mesa" era conceito inédito. **Destilado desbloqueado**; restam nomenclatura final, MR e matriz de combinações.
