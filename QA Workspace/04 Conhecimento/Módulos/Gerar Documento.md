---
title: Gerar Documento
tags:
  - qa
  - conhecimento
  - sogov
  - tramitacao
  - gerar-documento
tipo: modulo
revisado: 2026-07-20
fonte: https://app.notion.com/p/alfa-group/Gerar-documento-2d22aec67d3080148515cb59d6cb398d
fonte_criado: 2025-12-23 (Rafael)
fonte_ultima_edicao: 2026-06-12 (Ivo Costa)
---
# Gerar Documento

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20 — página filha de **Tramitação**. A página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

## Visão geral

Funcionalidade que permite criar um novo documento **a partir de** um documento existente (ex.: gerar um Alvará a partir de um Protocolo), mantendo rastro entre os dois e propagando acesso aos envolvidos da tramitação original.

## Regras gerais

- Documentos **Em elaboração** não podem gerar outros documentos;
- Documentos **Encerrados** não podem gerar outros documentos;
- Só aparecem como opção pra geração os módulos configurados no construtor com o parâmetro **"Permitir conexão com outros módulos"**;
- Só servidores **N1 (Especialista) ou superior** podem usar a funcionalidade;
- Documentos Oficiais ou Comunicações Oficiais **gerados a partir de outro** documento:
	- Devem ser **emitidos imediatamente**;
	- **Não podem** permanecer no estado Em elaboração;
- O evento de geração no documento gerador só é registrado **após a emissão** do documento gerado;
- Documentos gerados a partir de outro devem: entrar na **impressão conjunta**, ser **exibidos na íntegra**, e **respeitar a ordem cronológica** de geração na timeline.

## Fluxo para gerar um documento

1. Clicar em "Gerar documento" → pop-up de confirmação;
2. No pop-up, selecionar (via select) qual documento deseja gerar;
3. Módulo sem permissão pra criar → opção aparece **desabilitada/indisponível** na seleção;
4. **Cancelar** → permanece no documento atual;
5. **Continuar** → direcionado pro formulário do novo documento;
6. Ao finalizar a criação e emissão: flash message de sucesso + **redirecionamento automático pro documento gerador**.

## Eventos e associação entre documentos

- O documento **gerador** recebe um evento na timeline principal indicando a geração do novo documento;
- O documento **gerado** exibe no header a informação de que foi gerado a partir de outro documento;
- No header do documento **gerador**, o documento gerado aparece como **documento associado**.

## Regras de acesso e permissões (ponto importante)

> [!warning] Propagação de acesso
> Ao gerar um documento a partir de outro (ex.: gerar um Alvará a partir de um Protocolo): **todos os usuários que faziam parte da tramitação do documento gerador passam a ter acesso ao documento gerado** — mesmo que não tivessem permissão prévia pra visualizar o módulo do documento gerado. O acesso é **restrito ao documento gerado e associado**, não concede permissão geral ao módulo.
>
> Exemplo: se um usuário com permissão gera um Alvará a partir de um Protocolo, qualquer outro usuário que participou da tramitação do Protocolo — mesmo sem permissão prévia pra visualizar Alvarás — pode visualizar **exclusivamente** o Alvará gerado e associado a esse Protocolo.

## Notificações

Todos os envolvidos recebem **notificação no sistema** e **e-mail** — a partir desse momento, passam a ter acesso ao novo documento gerado.

## Atualização de 12/06/2026 — Ocultação dinâmica da ação "Gerar Documento"

**Problema anterior**: o botão "Gerar Documento" permanecia visível e clicável na toolbar mesmo quando o setor atuante selecionado não tinha permissão pra tramitar/gerar determinados documentos — o usuário preenchia todo o formulário pra só no final receber alerta de falta de permissão (frustração, retrabalho, mais chamados de suporte).

**Princípio aplicado**: Prevenção de Erros (Nielsen) — melhor a interface não oferecer a ação inválida do que exibir um bom erro depois.

**Novo comportamento**: a visibilidade da ação "Gerar Documento" na toolbar passa a ser **estritamente contextual**, priorizando a **permissão do Setor Atuante** sobre a permissão do nível de acesso do usuário. Se o setor atuante não tem permissão pra gerar **nenhum** tipo de documento, a opção **não é exibida**.

## Backlog da página (Notion)

- [Melhoria] Desabilitar gerar documento quando o setor não tiver permissão para gerar documento

*(Esse item de backlog parece ser a mesma pauta da atualização de 12/06/2026 acima — confirmar no Notion se já foi implementado ou se ainda é planejamento.)*

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [ ] O backlog "[Melhoria] Desabilitar gerar documento..." e a atualização de 12/06/2026 parecem a mesma pauta — confirmar status real no Notion (implementado ou ainda planejado)
- [ ] A propagação de acesso (regra de permissões) é só na criação do documento gerado, ou persiste se o documento gerador for retificado/editado depois? Não especificado na doc
- [ ] Documento gerado a partir de outro, mas que depois é **desassociado** ([[Associar e Desassociar]]): o acesso propagado é revogado? Não coberto aqui — cruzar com a doc de Associar/Desassociar quando for testar

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- 
