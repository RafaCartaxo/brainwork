---
tags:
  - qa
  - refinamento
task: "9610"
status: refinado
data_inicio: 2026-07-17
responsavel: Rafael
modulo: associar-desassociar
---
# Refinamento: [BUG-CX] Servidor não consegue associar documento na abertura de um novo documento

> [!info]- Mesa de trabalho — [[../Sistema/Contexto/FLUXOS#6. Refinar demanda já cadastrada (Notion → vault)|fluxo 6]]
> Análise e suposição vivem aqui — o card em `02 Demandas/` nasce do **Destilado**, limpo. Ao concluir: análise → Notion (`📤`), card criado (`📝`), este arquivo → `04 Conhecimento/` (`status: refinado`).

## O problema (task no Notion)

**Passo a passo para reproduzir** — 1- acessar ambiente PM Guamaré e se colocar no setor SEMAVM - Manutenção de Veículos; 2- criar um novo documento do tipo memorando e clicar na opção Associar documento; 3- no processo de associar documento, buscar pelo documento Ofício 001839/2025 e identificar que o documento não aparece na listagem. Obs.: a situação foi reportada pela servidora Ana Beatriz Do Nascimento Maciel do setor SEMAMV.

**Comportamento atual** — A plataforma não está permitindo a associação de um documento no ato de abertura de um novo documento.

**Comportamento esperado** — Considerando que o servidor tem acesso ao documento que ele quer associar, o documento deveria aparecer para ser selecionado na escolha de documentos a serem associados.

**Análise** (Bruna Machado, 25/06/2026) — Foi realizada a consulta do documento 001839/2025 na mesa de trabalho SEMAVM, confirmando sua existência. Em seguida, foi criado um memorando com a associação do documento 001839/2025; porém, ao buscá-lo na lista para associar, ele não aparece na listagem. Foi realizado o mesmo teste no ambiente de homologação onde acessei o documento e associei o ofício 001839/2025 ao despacho e deu certo filtrar pela numeração e a associação, deste modo foi validado que **apenas o campo de busca de associar um documento ao criar um novo documento está apresentando a problemática**. Regras: [Associar/Desassociar (Notion)](https://app.notion.com/p/alfa-group/Associar-Desassociar-2942aec67d308030b4aae3be61041de3).

**Entrega do dev** (João Rodrigo, 07/07 — [MR !537](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/537), aprovado por B. Luan e Bruno Clementino) — Corrigir o bug no fluxo de associação de documentos, garantindo que a busca de documentos vinculáveis use corretamente o **setor atual do agente público na instância**. Ajustada a identificação do setor ativo para considerar o `lastAssociatedSector` (com fallback pro setor principal) e corrigido o envio do setor na busca de documentos associáveis (aceita `organizationalComponent.id` e `organizationalComponentId`), evitando consultas sem setor quando o usuário não está em modo cidadão. Testes adicionados (setor disponível, fallback, ausência de setor). Telas impactadas: **Abertura de Documento, Associação de Documentos e Assinatura de Documento**. Endpoints: `publicAgentByInstance`, `documentsToLink`. Arquivos web: `AddNewDocumentTab` (+ teste), `PublicAgent.queries.ts`, `SignatureToolbarItem.tsx`, `OpenDocumentPage.tsx` (+ configs de teste). Status no Notion: **Pronto pra teste em dev** (SP14/SP15 - 2026, Sustentação — cliente afetado: Prefeitura de Guamaré).

**Referências da task** — Documento afetado: `https://www.sogov.com.br/cliente/30/documento/MIRMG47ELROGYSKCT6` · Evidência: `Gravando_2026-06-25_135854_-_documento_no_sendo_associado.mp4` (anexo no Notion, não trazido pro vault).

---

## Análise

- **Regra violada (documentada)**: [[Módulos/Associar e Desassociar#Permissões e visibilidade|Associar/Desassociar]] — "o usuário só busca documentos aos quais tem acesso"; tendo acesso, o documento deve aparecer na busca. A funcionalidade de associação **na abertura** é a da atualização de 22/10/2025 (Drawer na toolbar inferior do formulário de criação).
- **Escopo isolado pela análise da Bruna**: só a busca do fluxo de **associar na abertura** falha; associar **via despacho** funciona (validado em HML com o mesmo documento). Compatível com a causa descrita no MR: a busca na abertura fazia consulta **sem setor** (setor ativo do agente não identificado corretamente).
- **Ponto de atenção do MR**: além das telas de abertura/associação, o MR toca `SignatureToolbarItem.tsx` (tela de **Assinatura de Documento**) e a query compartilhada `PublicAgent.queries.ts` — a validação deve cobrir regressão na assinatura via toolbar, não só a associação.
- **Evidências**: análise da Bruna (25/06, com print no Notion); vídeo de evidência anexo na task; descrição técnica do MR !537.
- **Hipóteses descartadas**: —

---

## Pontos a definir

- [x] ~~Reprodução em DEV~~ → **resolvido (Rafael, 2026-07-17)**: o gatilho é servidor **cadastrado em mais de um setor** tentando associar, na abertura, documento de um setor que ele **participa mas não está atuando** (switch em outro setor). Cenário registrado no Destilado
- [x] ~~Critérios de aceite~~ → derivados e refinados no Destilado (escopo isolado no cenário multi-setor)
- [ ] Vídeo de evidência ficou só no Notion — trazer pro vault (`Evidências/`) se for útil na validação, ou referenciar direto

---

## Destilado (rascunho do card)

> [!abstract] Só o problema — o que vai pro card, quase copy-paste: Descrição objetiva, passo a passo, resultado esperado, critérios de aceite, CTs. Nada de análise ou suposição.

### Descrição

Servidor cadastrado em mais de um setor não encontra, na busca de "Associar documentos" da **abertura de um novo documento**, documento ao qual tem acesso por um setor em que **não está atuando** no momento. O contraste que delimita o problema: a mesma busca, feita **via despacho**, encontra o documento normalmente (validado na análise de Bruna Machado, 25/06/2026). Causa apontada no MR !537: a busca da abertura era feita **sem informar o setor ativo** do usuário.

### Passo a passo para reproduzir

Dado que um servidor esteja cadastrado em mais de um setor (setor A e setor B)
E esteja atuando pelo setor A
Quando iniciar a abertura de um novo documento e buscar, em "Associar documentos", um documento acessível pelo setor B
Então o documento não aparece na listagem para associação

*(Cenário original: PM Guamaré, setor SEMAVM, memorando, Ofício 001839/2025.)*

### Resultado Esperado

Documento ao qual o servidor tem acesso — **por qualquer setor do qual participe, atuando por ele ou não** — aparece na busca de associação da abertura e pode ser selecionado.

### Critérios de aceite

- [ ] Servidor multi-setor atuando pelo setor A encontra, na busca da abertura, documento acessível pelo setor B
- [ ] Documento do próprio setor ativo continua aparecendo na busca da abertura
- [ ] A busca da abertura retorna os mesmos documentos que a busca de associação **via despacho**, pro mesmo usuário
- [ ] Documento ao qual o servidor **não** tem acesso por nenhum setor continua **fora** da listagem — a correção não pode ter liberado a busca sem filtro de setor
- [ ] Sem regressão nas telas tocadas pelo MR: associação via despacho e assinatura via toolbar seguem funcionando, inclusive com usuário multi-setor

### Casos de Teste Básicos

*(gerar CTs completos na validação — skill de casos de teste, usando [[Módulos/Associar e Desassociar|a doc do módulo]] como fonte de regras)*

---

## Histórico do refinamento

- 2026-07-17 - Material recebido (export do Notion, `~/Downloads/sgv-9610.md`) e organizado na mesa
- 2026-07-17 - 🔎 Análise: problema isolado (análise Bruna 25/06) à busca do fluxo de associar **na abertura**; regra violada está documentada em 04 Conhecimento (Associar/Desassociar); MR !537 corrige envio do setor ativo na busca — atenção à regressão em Assinatura (toolbar), tela também tocada. Destilado rascunhado; pendências: cenário de reprodução em DEV e destino do vídeo de evidência.
- 2026-07-17 - 🔎 Rodada 2 (com Rafael): reprodução confirmada — gatilho é servidor **multi-setor** buscando, na abertura, documento de setor que participa mas **não está atuando**. Passo a passo reescrito em Dado/Quando/Então e critérios de aceite refinados (cenário do bug, base, paridade com despacho, limite de acesso preservado, regressão nas telas do MR). Falta só decidir o destino do vídeo de evidência — destilado pronto pra virar card na validação.
- 2026-07-17 - 📝 Destilado aprovado (padrão dos cards do vault) e card criado em [[../02 Demandas/DEV/9610 - Bug Associar Documento Abertura Multi-Setor|02 Demandas/DEV/9610]] com 6 CTs básicos. Próximo passo (Rafael): marcar `status: refinado`, levar análise pro Notion (📤) e arquivar esta mesa em 04 Conhecimento.
- 2026-07-17 - 📤 Análise/critérios levados pro Notion (Rafael) e mesa arquivada em `04 Conhecimento/` (`status: refinado`). Ciclo do fluxo 6 concluído — resta a validação em DEV (pendência na fila).
