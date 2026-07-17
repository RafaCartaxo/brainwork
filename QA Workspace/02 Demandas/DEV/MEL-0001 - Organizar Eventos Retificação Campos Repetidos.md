---
tags:
  - demanda
  - qa
  - formulario
  - repeticao-campo
task: ""
mel: "0001"
status: dev
prioridade: media
data_inicio: 2026-07-14
data_fim:
responsavel: Rafael
cadastrado_por:
modulo: formularios
---
# Demanda: Organizar a exibição dos eventos de retificação de campos repetidos

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** Aguardando cadastro externo (depois: DEV)
> - **Responsável QA:** Rafael
> - **Link:** (preencher com o SGV ao cadastrar — e renomear este arquivo pra `<SGV> - <título>`)

---

> [!abstract] Resumo

Campos com "permitir repetição de campo" podem ser duplicados N vezes (repetição 1, 2, 3, 4...), e um formulário pode ter vários campos assim (Descrição, Mapa, Número etc.). Quando várias repetições de vários campos são retificadas, os eventos aparecem na linha do tempo **sem ordem definida**: a repetição 1 de um campo lá em cima, as repetições 2 e 3 juntas mais abaixo, a 4 em outro ponto, intercaladas com retificações de outros campos. A melhoria é organizar a exibição: **agrupar as retificações por campo, com as repetições em ordem numérica, e os campos na ordem em que aparecem no formulário**. (O conteúdo de cada evento já está correto desde o [[QA Workspace/02 Demandas/Concluídas/8805 - Bug Descrição Técnica Campos Repetidos|SGV-8805]] — aqui é só a organização/ordenação.)

---

## Regras de negócio

- Retificações de um mesmo campo repetido aparecem **agrupadas** (juntas na linha do tempo), não intercaladas com as de outros campos.
- Dentro do grupo de um campo, as repetições seguem **ordem numérica crescente** (repetição 1 → 2 → 3 → 4...).
- Entre campos, a ordem segue a **posição do campo no formulário**.
- O formato do texto de cada evento não muda — continua o padrão do SGV-8805: `campo <Label>: (repetição <N>) de '<valor anterior>' para '<valor novo>'`.

---

> [!warning] Pontos de atenção
> - Não alterar o conteúdo/formato dos eventos (já validado no 8805) — só a ordenação/agrupamento da exibição. Cobrir regressão com CT.
> - Verificar se a ordenação vale tanto pra retificação feita numa tacada só (vários campos de uma vez) quanto pra retificações em momentos diferentes.

---

## Casos de teste

- **CT-001 Repetições do mesmo campo agrupadas e em ordem numérica**
    Dado que um campo com repetição habilitada tenha as repetições 1, 3 e 4 retificadas
    Quando os eventos de retificação forem exibidos na linha do tempo
    Então as três retificações devem aparecer juntas, na ordem 1 → 3 → 4

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-002 Vários campos repetidos retificados seguem a ordem do formulário**
    Dado que dois ou mais campos repetidos (ex.: Descrição, Número) tenham repetições retificadas
    Quando os eventos forem exibidos
    Então as retificações devem vir agrupadas por campo, com os campos na ordem em que aparecem no formulário, sem intercalar

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-003 Regressão do 8805 — texto do evento continua amigável**
    Dado que qualquer repetição de campo seja retificada
    Quando o evento for exibido
    Então o texto continua no formato "campo <Label>: (repetição N) de '...' para '...'", sem identificador técnico

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

> [!danger] Bugs encontrados

---

## Evidências

---

> [!tip] Observações
> Apoio técnico (investigação de 14/07 na branch development): a exibição dos eventos de retificação mora em `web/src/shared/components/DocumentEvent/DocumentEventCard.tsx` (caso `FIELD_RECTIFIED`), e o texto é montado por `buildDiffComment` em `api/src/services/dispatches/dispatches.ts` (~linha 5648). Sugestão secundária pro dev, se fizer sentido junto: extrair a tradução técnico→amigável (hoje inline na `buildDiffComment`) pra um helper reutilizável, prevenindo regressão em pontos futuros de descrição de evento. Não é o foco da melhoria.

---

## Histórico

- 2026-07-14 - 💭 Melhoria proposta (origem: SGV-8805)
- 2026-07-15 - 📝 Melhoria refinada (card criado; escopo: agrupar por campo, repetições em ordem, campos na ordem do formulário). Aguardando cadastro externo.
