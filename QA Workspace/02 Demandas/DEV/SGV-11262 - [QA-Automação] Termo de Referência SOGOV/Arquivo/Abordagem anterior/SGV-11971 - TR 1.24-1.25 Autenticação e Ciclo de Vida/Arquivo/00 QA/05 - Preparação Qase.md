---
tags:
  - qa
  - qase
tipo: referencia
status: enviado
tipo_card: funcionalidade
projeto: ""
modulo: autenticacao
qase_projeto: SGV
qase_suite_id: 4
casos_origem: "[[03 - Casos de teste]]"
validacao_origem: "[[04 - Validação dev]]"
---
# Preparação Qase — SGV-11971 (TR 1.24-1.25)

> [!info]- Navegação QA  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[../01 Automação/00 - Automação|Automação]]

> Registro da sincronização **já executada** em 31/08/2026. Diferente dos outros pacotes do vault, aqui os casos **já existiam na Qase antes** do vault ter uma fonte única — a rodada foi de correção do que estava lá, não de criação a partir do `03`.

---

## Configuração

- **Projeto Qase:** `SGV`
- **Suite:** `4`
- **Script:** `Sistema/Scripts/qase-sync/11971-tr-1-24-1-25/` — `corrections.json` (payload) + `sync.js` (aplicação) + `README.md`
- **Fonte dos casos:** [[03 - Casos de teste]] (fonte única desde 31/08/2026)

> [!warning] Esta versão do script está congelada
> O `README.md` da raiz de `Sistema/Scripts/qase-sync/` desaconselha copiar daqui pra uma sincronização nova: esta versão é mais simples e não tem shared steps nem idempotência real. Pra um TR novo, copiar de `9296-departamentos/`, que é a versão mais recente.

---

## Mapeamento dos campos

| Campo da Qase | De onde vem | Observação |
|---|---|---|
| `title` | título do CT no `03` | só enviado nos casos em que o título mudou |
| `description` | `**Citação do Termo:**` do CT | texto literal da regra, com as notas entre colchetes quando o Termo é omisso |
| `preconditions` | cláusula `Dado` do CT | |
| `postconditions` | `**Pós-condição:**` do CT | |
| `steps` | cláusulas `Quando`/`E`/`Então` | formato `classic` |
| `severity` / `type` / `automation` | fixos | `normal` / `acceptance` / `is-not-automated` |
| `priority` | **não enviado** | decisão do Rafael em 31/08: preencher manualmente na Qase, pra não depender de um mapeamento de enum não confirmado |
| `behavior` | **nunca enviado** | mapeamento de valor incerto |

Regra do payload: **campo ausente num `update` = não mexer nesse campo.** A API da Qase faz update parcial de verdade.

---

## Shared steps

Os shared steps deste Termo (`SS-01a` a `SS-06`, ver [[03 - Casos de teste#Legenda — Shared Steps]]) são **rastreabilidade do vault**, não shared steps nativos da Qase: cada `Quando`/`E` do caso já traz a ação por extenso, e nada foi criado via `POST /v1/shared_step/`. A Qase tem o recurso nativo (`GET /v1/shared_step/{code}`), e vale conferir se já existem antes de escrever conteúdo novo — mas nesta rodada a decisão foi não usá-los.

*(Pacotes posteriores do vault — SGV-11177 e SGV-11178 — já usam shared steps nativos da Qase. Se este Termo for ressincronizado, vale alinhar.)*

---

## Casos preparados

A rodada de 31/08/2026 tocou os 39 casos que já existiam na suite 4:

| Operação | Qtd | Qase ids | Detalhe |
|---|---|---|---|
| **Atualizados** | 25 | 1, 2, 3, 5, 18–32, 34–39 | Conteúdo completo (precondição/pós-condição/passos); correção do card corrompido (`id 5`); correção da regra de acesso de leitura em Licença/Férias; correção dos nomes de nível de permissão no CT-020 (eram "Assistente/Auxiliar/Visualizador" — o certo é **Especialista / Usuário básico / Somente leitura**) |
| **Excluídos** | 2 | 13, 33 | Órfãos absorvidos no vault em 19/08 — a checagem de mensagens de erro distintas virou cláusula no `Então` de CT-009/010/014/031. Decisão do Rafael em 31/08: excluir de vez, não só depreciar |
| **Criados** | 1 | — | "Um servidor desbloqueia manualmente a conta pela tela do servidor" — equivalente ao CT-017, que nunca existiu na Qase |

> [!warning] Lacuna: o mapa CT ↔ id da Qase nunca foi registrado
> A sincronização foi feita **por id da Qase** contra os casos que já estavam lá, não por número de CT — e o `corrections.json` só traz `title` nos 4 casos em que o título mudou. Não dá pra reconstruir com segurança qual CT corresponde a qual id a partir do que está no vault hoje, e **não vou presumir**. Os 4 pares que o payload confirma são: `id 5` ↔ CT-005, `id 24` ↔ CT-024, `id 30` ↔ CT-030, `id 39` ↔ CT-035. Pra fechar o resto, é preciso um `GET` na suite 4 e cruzar por conteúdo — fica como pendência, não bloqueia nada hoje.

---

## Checklist de envio

- [x] Casos conferidos contra a fonte única do vault.
- [x] Payload montado só com o que realmente muda por caso.
- [x] `--inspect` num caso real antes de escrever (confirmou que `severity`/`type`/`automation`/`status` são **números** na API, mesmo o export mostrando texto).
- [x] `--only=<id>` num caso de baixo risco antes do lote.
- [x] Lote aplicado e conferido por amostragem (31/08/2026).
- [ ] `priority` preenchido manualmente na Qase (pendente desde 31/08, decisão consciente).
- [ ] Mapa CT ↔ id da Qase reconstruído e registrado aqui.
