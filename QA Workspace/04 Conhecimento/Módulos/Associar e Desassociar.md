---
title: Associar/Desassociar
tags:
  - qa
  - conhecimento
  - sogov
  - tramitacao
  - associar-desassociar
tipo: modulo
revisado: 2026-07-17
fonte: https://app.notion.com/p/alfa-group/Associar-Desassociar-2942aec67d308030b4aae3be61041de3
fonte_criado: 2025-10-22 (Ivo Costa)
fonte_ultima_edicao: 2025-10-24 (Ivo Costa)
---
# Associar/Desassociar

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-17 — a página do Notion (filha da página **Tramitação**) continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Os prints de tela do original não vieram no export — consultar o Notion pra referência visual. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste (QA)]].

## Definição geral

Associar um documento é a funcionalidade que permite vincular um documento a outro, criando vínculos e regras entre eles.

## Permissões e visibilidade

- **Quem pode associar/desassociar**: usuário com permissão **N1 (Especialista), N2 (Usuário básico), Adm ou Adm setorial** — do setor dono **ou** de um setor envolvido *("Especialista"/"Usuário básico" são a nomenclatura nova de N1/N2 — confirmado com Rafael em 2026-07-17, só renomeação, mesma regra)*;
- **Busca limitada ao acesso**: o usuário só busca documentos aos quais tem acesso. Documento válido/existente mas sem acesso: **é exibido, mas não permite associar**;
- **Visibilidade da associação**: uma vez associado, **todos os envolvidos no documento principal** passam a ver o documento associado;
	- **Restrição de ação**: quem só tem acesso ao associado por estar envolvido no principal (sem permissão intrínseca) apenas **visualiza** — nenhuma ação é permitida lá dentro (experiência análoga ao acesso via "mesas alheias");
- **Visibilidade inversa NÃO acontece**: os envolvidos no documento associado só veem o principal se já tiverem permissão prévia.

## Fluxos originais (v1 — via despacho)

### Associar

1. No despacho, acionar "Relacionar processo" (link button) → abre modal de seleção de um ou mais documentos/processos;
2. A busca filtra por tipo/numeração conforme se digita, trazendo os compatíveis;
3. Documento selecionado vai pra lista de associados no modal, com duas opções: **ver o documento** (outra página) ou **excluir a associação**;
4. Salvar → retorna ao despacho com a configuração setada;
5. Ao enviar/salvar o despacho: cria-se um **dropdown no despacho que associou e no header do documento**, com link que abre o formulário do associado em nova aba.

### Desassociar

1. No dropdown (header ou despacho que associou), acionar "Desassociar documentos";
2. Gera um **despacho específico na timeline principal**, onde se seleciona um ou mais documentos pra desassociar + **justificativa obrigatória**;
3. Esse despacho aceita **anexos** (podem ser necessários pra justificar);
4. Ao desassociar: flash message + despacho registrado na timeline.

## Atualização de 22/10/2025 — Drawer e associação na abertura

Regras de negócio de permissão/visibilidade **mantidas** (seção acima). Novidades:

### UI — header

- Ícones atualizados: o de "em quais documentos este está associado" e o de documentos associados no header;
- Documentos associados **na abertura** aparecem no header de forma consistente com os demais.

### O Drawer (novo mecanismo unificado de busca/seleção)

- **Busca** por: nome do módulo, serviço ou assunto; nome (servidor, PF ou PJ); CPF; título do documento;
- **Filtros**: tipo do documento, etiquetas, setor responsável;
- **Seleção** múltipla por checkbox nos cards listados;
- **Abas**: "Associar documento" (busca) e "Documentos selecionados" (revisão, com contagem);
- **Segurança**: fechar (X) ou cancelar com seleção feita → dialog de confirmação avisando que as seleções serão perdidas.

### Associação na criação (abertura)

1. No formulário de abertura, opção **"Associar documentos"** na toolbar inferior;
2. Drawer pra busca/seleção (filtros + checkboxes);
3. Finaliza no botão "Associar" do Drawer.

### Edição da associação na abertura

- Permitida **antes da emissão** do documento, reutilizando o Drawer;
- Clica no componente de documentos associados em "Configurações setadas" → Drawer reabre → pode **remover** documentos → "Salvar".

### Desassociação pós-criação (associação feita na abertura)

- Feita pelo **evento de associação na timeline** (mantém rastreamento);
- No componente do documento associado no evento → "Desassociar documentos" → seleciona o documento (campo de seleção) + **justificativa obrigatória** → "Desassociar";
- Sistema gera **novo despacho na timeline** registrando a desassociação.

### Associação/desassociação via despacho (pós-criação)

Fluxos v1 permanecem, com UI/UX uniformizada:

- **Associar**: funcionalidade "Associar documentos" no campo do despacho → Drawer → associação efetivada **no envio do despacho**;
- **Desassociar**: dropdown no despacho original de associação → "Desassociar documentos" → gera novo despacho com **justificativa obrigatória**.

## Backlog da página (Notion)

- [UI/UX] Permitir associação de documentos na etapa de abertura de novo documento;
- Permitir associação de documentos a partir do formulário de abertura do documento.

*(Ambos parecem já contemplados pela atualização de 22/10/2025 — confirmar status das tasks no Notion.)*

---

## Comportamentos observados em teste (QA)
<!-- Divergências entre esta doc e o sistema real, pegadinhas, efeitos colaterais — com data e ambiente -->
- 

## Dúvidas em aberto
- [x] ~~Nomenclatura de permissões divergente~~ → resolvida (2026-07-17): "Especialista"/"Usuário básico" = renomeação de N1/N2, mesma regra
- [ ] Desassociar documento associado **na abertura**: dá pra desassociar via header também, ou só pelo evento da timeline?
- [ ] Relação com o evento `DISASSOCIATE`/`DISPATCH_DISASSOCIATE` (docs do repo, `document-event`): confirmar mapeamento dos eventos gerados em cada fluxo
- [ ] Retificação × associação: despachos de associação/desassociação são "gerados por ação sistêmica" (Associou/Desassociou) e portanto **não retificáveis** (regra na doc de [[Fluxo de trabalho (Workflow)#Retificação de documento em qualquer etapa (~08/07/2026)|Workflow]]) — validar comportamento em teste

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- [[../../02 Demandas/DEV/9610 - Bug Associar Documento Abertura Multi-Setor|SGV-9610]] — busca de associação na abertura não retornava documento de setor em que o servidor multi-setor não está atuando (consulta sem setor ativo); card em validação em DEV ([[../../05 Refinar/SGV-9610|análise do refinamento]])
