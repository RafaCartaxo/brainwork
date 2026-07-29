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

## Pontos a definir

- [ ] **(Declarado pela spec) Regra de permissão para tramitação** — quem pode usar cada ação do painel Ações de Destino? O default do Workflow ("todos os participantes podem avançar/retroceder") vale aqui, ou a emissão de despacho tem regra própria? E "Encerrar no Setor" segue a regra de 15/06 (só setor responsável) ou qualquer setor participante?
- [ ] **(Declarado pela spec) Regra de pulo para tramitação** — é permitido pular etapas ao avançar? Nada documentado em Workflow nem Tramitação sobre pulo. Se sim, quais etapas podem ser puladas e por quem?
- [ ] **(Declarado pela spec) Obrigatoriedade de despacho** — a ação de destino exige que o despacho seja efetivamente preenchido/emitido, ou é possível só tramitar? Em que combinações?
- [ ] **(Declarado pela spec) Obrigatoriedade de assinatura** — a spec cita "respeitando assinatura legal". Encerrar/avançar exige assinatura concluída? O que acontece se houver assinatura pendente ou recusada?
- [ ] **"Encerrar na Mesa" precisa de definição de regra e de doc** — remover da fila de pendências gerais e arquivar na mesa do usuário logado é comportamento novo. Quem vê o documento depois? Ele sai da mesa do setor? Como se desfaz?
- [ ] **MR da entrega** — o export não cita MR e o Notion já marca "Testando em homologação". Confirmar com os devs qual MR entrega isso, pra poder revisar escopo antes de validar.
- [ ] **Interação com a SGV-6373** — validar se o bug de setores não mantidos ao avançar/retroceder afeta este novo ponto de entrada.

---

## Destilado (rascunho do card)

> [!abstract] Só o problema — o que vai pro card, quase copy-paste: Descrição objetiva, passo a passo, resultado esperado, critérios de aceite, CTs. Nada de análise ou suposição.

> [!warning] Bloqueado
> Destilado aguardando os 4 pontos que a **própria spec** declara como "regras de negócio que precisam de validação". Sem elas não há critério de aceite verificável — e um CT por critério é a regra do fluxo 6. Não destilar antes.

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
