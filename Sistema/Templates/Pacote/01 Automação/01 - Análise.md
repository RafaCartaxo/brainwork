---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-test"
framework: playwright
ambiente: hml
onda: 1
analises_anteriores: []
status: analise
---

# Análise da automação — <ID> · Onda <N>

**Ticket de origem:** <SGV/ATV, se diferente do ID do pacote> · **Análises anteriores:** <links para os `01 - Análise` das ondas anteriores, ou “nenhuma — primeira onda”>

> [!info]- Navegação QA/Automação
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Automação:** [[Sistema/Templates/Pacote/01 Automação/00 - Automação]]
> **Plano de automação:** [[Sistema/Templates/Pacote/01 Automação/02 - Plano de automação]]
> **Validação automação:** [[Sistema/Templates/Pacote/01 Automação/03 - Validação automação]]

> [!settings]- Controle da análise
> **Status:** `INPUT[inlineSelect(option(analise),option(pronta_para_planejar),option(concluida)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> [!info] Status atual
> **Próximo passo:** <registrar a próxima ação objetiva>.

> A Análise responde **por que e como** automatizar esta onda, antes do plano tático. Mantenha decisões curtas, ligadas aos CTs. A fonte de verdade de **comandos e configuração** é o `playwright/README.md` e o `ENVIRONMENTS.md` do repositório (e o [[00 - Índice da automação Playwright|índice de automação Playwright]] do vault); não os repita aqui. Enquanto houver item em **Pendências de decisão**, mantenha `status: analise`.

---

## Contexto / problema

Por que automatizar este conjunto agora? Que dor resolve (regressão, sanidade, risco de dado ou e-mail descontrolado)?

## Onda

- **Onda:** <número>, <~20 CTs; cresce com o tempo>.
- **CTs:** <intervalo ou lista> — fonte em [[../00 QA/03 - Casos de teste]].
- **Herda de:** <Análises anteriores — a massa e as decisões delas valem aqui; não repetir>.

---

## Decisões técnicas

| Grupo de CTs | Camada (API / E2E) | Estratégia de dados | Reuso identificado |
|---|---|---|---|
| <CTs ou tema> | <API / E2E> | <baseline compartilhado · ator/módulo exclusivo · instância exclusiva> | <fixtures de `src/fixtures`, helpers de `src/ui/internal/*`, serviços de `src/api/services/*`, specs existentes (ID `A##`/`E##`)> |

> Preferir API quando o comportamento é verificável por API; E2E quando só existe na tela. Uma linha por grupo com a mesma estratégia. **Antes de criar algo, procurar o que já existe** (spec com ID, serviço, helper) e registrar o mapa CT → teste existente em vez de duplicar.

---

## Escopo desta onda

- CTs que serão automatizados nesta onda, com a camada.

## Fora de escopo

- CT que fica manual e **por quê** (ex.: depende de job de BI que o seed não garante; manda e-mail real a cada execução; comportamento ainda não confirmado manualmente; nada no código para sustentar).

---

## Riscos

- **E-mail real:** quais CTs ou preparações disparam e-mail; volume por execução; plano de contenção.
- **Estado compartilhado:** o que o teste altera e quem mais lê isso (mutação em instância/módulo/ator compartilhado).
- **Dados permanentes:** o que não tem exclusão (ex.: instância nova avisa os analistas SOGOV e não pode ser removida).
- **Ambiente:** instabilidade e janela de execução.

---

## Massa desta entrega

> [!important] Regras da massa
> - **Cada onda registra só o que acrescenta** e linka as Análises anteriores; não repita as linhas delas.
> - **Ator/módulo/instância que um teste versionado precisa vai no `baseline.ts`** (versionado, vale para todos). `massa/<nome>.json` é pessoal, fora do git, **só para iteração local**.
> - **Rastreio no código:** comentário acima de cada entrada nova no `baseline.ts`: `// SGV-XXXX · CT-0xx: <motivo>`.
> - **Versão:** um incremento de `SEED_SCHEMA_VERSION` **por entrega** (não por CT), registrado na última coluna.
> - Quem **altera** cadastro precisa de ator exclusivo: dono em `ownership.ts` e spec marcado `@shared-state`. Pool por worker só para ator usado por vários arquivos.
> - Identidades do baseline são fixas e válidas (CPF/CNPJ não mudam a cada execução). Usar `PW_AGENT_REGISTRATION=invite` no primeiro seed para não mandar e-mail a cada servidor novo.

| Recurso | Tipo (ator / módulo / instância / A&S) | Novo ou reuso | CTs que usam | Exclusivo? (dono) | Dispara e-mail? | Entra em (versão do baseline / MR) |
|---|---|---|---|---|---|---|
| <chave no baseline ou nome> | <tipo> | <novo / reuso de onda N> | <CT-0xx, …> | <não · sim: caminho do spec dono> | <não · sim: quando e quantos> | <`SEED_SCHEMA_VERSION` = nn · link da MR> |

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise` e registrar quem decide.

## Gate: pronto para planejar

- [ ] Validação manual dos CTs da onda concluída e comportamento disponível no ambiente-alvo.
- [ ] Decisões técnicas fechadas (camada e estratégia de dados por grupo).
- [ ] Escopo e **fora de escopo** claros, com o motivo de cada CT que fica manual.
- [ ] Tabela **Massa desta entrega** preenchida (incluindo e-mail e dono dos exclusivos).
- [ ] Riscos de e-mail e dado permanente avaliados com o responsável.
- [ ] Análises anteriores linkadas.

Fechado o gate, seguir para [[Sistema/Templates/Pacote/01 Automação/02 - Plano de automação|02 - Plano de automação]].
