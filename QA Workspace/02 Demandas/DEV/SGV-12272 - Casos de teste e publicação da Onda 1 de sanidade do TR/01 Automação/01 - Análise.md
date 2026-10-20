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

# Análise da automação — SGV-12272 · Onda 1

**Ticket de origem:** SGV-12272 (Onda 1 aprovada na SGV-12200) · **Análises anteriores:** nenhuma — primeira onda.

> [!info]- Navegação QA/Automação
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos de teste:** [[../00 QA/03 - Casos de teste]]
> **Automação:** [[00 - Automação]]
> **Plano de automação:** [[02 - Plano de automação]]
> **Validação automação:** [[03 - Validação automação]]

> [!settings]- Controle da análise
> **Status:** `INPUT[inlineSelect(option(analise),option(pronta_para_planejar),option(concluida)):status]`
> **Framework:** `INPUT[inlineSelect(option(playwright),option(outro)):framework]`
> **Ambiente-alvo:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> [!info] Status atual
> **Próximo passo:** validação manual dos 20 CTs (gate) e decisões pendentes do Rafael (ver **Pendências de decisão**).

> A Análise responde **por que e como** automatizar esta onda, antes do plano tático. A fonte de verdade de **comandos e configuração** é o `playwright/README.md` e o `ENVIRONMENTS.md` do repositório e o [[00 - Índice da automação Playwright|índice de automação Playwright]] do vault. Enquanto houver item em **Pendências de decisão**, `status: analise`.

---

## Contexto / problema

A automação atual dispara e-mail demais e cria/usa dados sem controle — já chegou a interromper o envio de e-mail de produção. A automação do Termo de Referência precisa nascer **controlada e rastreável**: cada entrega sabe quais atores, módulos e instâncias usa, criados quando e para qual CT.

A Onda 1 (20 CTs de sanidade do TR 1.24–1.25, aprovados na SGV-12200) é a primeira. A massa dela fica como base para as próximas ondas (~20 CTs cada, o tamanho cresce com o tempo): ator/módulo/instância que um teste versionado precisa vai no `baseline.ts` (versionado, vale para todos), não em massa pessoal.

## Onda

- **Onda:** 1 — ~20 CTs (CT-001 a CT-020).
- **CTs:** fonte em [[../00 QA/03 - Casos de teste]]; hoje todos com `Automação: manual` e execução manual ainda pendente em [[../00 QA/04 - Validação dev]].
- **Herda de:** nada (primeira onda). As próximas ondas linkam esta Análise e registram só o que acrescentam.

---

## Decisões técnicas

Levantamento feito por nome de arquivo, serviço e grep; o spec **não foi lido por inteiro** onde está marcado *provável, a confirmar*. IDs `A##`/`E##` são os do repo.

| Grupo de CTs | Camada | Estratégia de dados | Reuso identificado / lacuna |
|---|---|---|---|
| CT-001 login de servidor | API | baseline: pool `agent` | **Já coberto:** `A02-C01` em `tests/api/auth/login.spec.ts` (título confere, `@smoke`). Nada novo. |
| CT-002 bloqueio por 5 senhas erradas | API (login por request) | **ator exclusivo novo** `lockoutTarget` | Sem teste (`credentials.spec.ts` só testa 1 senha errada). Desbloqueio: `unlockSogoUserAccess` com `userType: 'publicAgent'` (helper atual `unlockCitizenAccess` fixa `'citizen'`; parametrizar). |
| CT-003 status do servidor (Ativo/Licença/Férias/Inativo) | API + verificação de acesso | **ator exclusivo novo** `statusTarget`; restaurar `IN_ACTIVITY` no `cleanup` | Sem teste. Mutation `changePublicAgentWorkStatus` (valores `IN_ACTIVITY`, `LICENSE`, `VACATION`, `SUSPEND`) não existe em `src/api/services`. |
| CT-004 criar documento só pelo Setor criador | API | **ator exclusivo novo** `twoSectorCreator` (GP + DIR) + módulo `accessKey` do baseline (só o GP cria) | Provável: `module.ts`, `organizational.ts`, `documents.ts`, `tests/api\|e2e/matters-services` *(a confirmar)*. Lacuna: nenhum servidor do baseline tem dois setores sem pertencer a spec dono. |
| CT-005 categoria-base do Assunto/Serviço | API | baseline: módulos PA/DO/CO | Provável: `matters-services.ts`, `tests/api/matters-services` *(a confirmar)*. Atenção: criar A&S a cada execução deixa linhas permanentes; ver como o spec existente limpa. |
| CT-006 Setor removido do Assunto/Serviço | API | **módulo + A&S novos e exclusivos** (3 setores X/Y/Z) | Provável: `matters-services.ts`, `organizational.ts` *(a confirmar)*. Exige provisionamento novo em `provision.ts`. |
| CT-007 / CT-008 Zona e Processo urbanístico | — | — | **Nada no código** (só flag `urbanisticProcessesModules` em `instance.ts` e o módulo de selo `urbanisticStamp`, que é outro assunto). |
| CT-009 documento a partir de Modelo simples | E2E | baseline; modelos criados no teste | Provável: `models.ts`, `tests/e2e/models/automated-document*.spec.ts` *(a confirmar)*. Dúvida: o baseline não declara modelos (só a massa pessoal); os 2 modelos (com/sem herança) teriam de ser criados no teste a cada execução. |
| CT-010 Fluxo com despacho e assinatura obrigatória | API / E2E | baseline: módulos `workflow*` | Provável: `workflow.ts`, `tests/api\|e2e/workflow/dispatch-attachment-signature.spec.ts` *(a confirmar se já afirma o bloqueio do avanço)*. |
| CT-011 Mesa: resumo e alternância de setores | E2E | baseline; **precisa de servidor com mais de um setor** | Provável: `ui/internal/workboard.ts`, `changeLastSectorAccessed`, `tests/e2e/workboard/*` *(a confirmar)*. Avaliar reuso de `twoSectorCreator`. |
| CT-012 Etiqueta pessoal × compartilhada | API / E2E | baseline: pools `agent` (GP) + `secretary`/`director` | Provável: `tags.ts`, `ui/internal/labels.ts`, `tests/*/processing/label-management.spec.ts` *(a confirmar a visibilidade entre setores)*; `deleteTag` permite limpeza. |
| CT-013 Contato externo com e-mail de confirmação | API | pool `citizen`; identidade nova a cada execução (cadastro único por CPF/CNPJ) | Provável: `signupCitizenPJ`, `registerCitizenInternally`, `RegistrationMailbox`, `tests/*/citizen/quick-registration` *(a confirmar)*. E-mail é a própria asserção. |
| CT-014 Central de atendimento | E2E | baseline: pool `citizen`; A&S `PA` com abertura externa | Sem helper da Central de atendimento. |
| CT-015 Ambiente virtual do usuário externo | E2E | baseline: pool `citizen` | Provável: `tests/api/processing/response.spec.ts`, `citizen-mention-dispatch` *(a confirmar)*; "Demanda" e canal de notificação sem confirmação. |
| CT-016 Divulgação: mural × Jornal Oficial | API / E2E | baseline | Lado interno: `ui/internal/mural.ts`, `publish-document.spec.ts`, `mural-filter.spec.ts` (provável). Lado externo/Jornal Oficial público sem helper. |
| CT-017 Assinatura sequencial | E2E | baseline: pools (`agent`, `mayor`, `secretary`, `director`) + `citizen` | Provável: `signatures.ts`, `tests/e2e/signatures/sequential-*.spec.ts`. **Não usar** `seq*` (exclusivos de `sequential-access-levels.spec.ts`). "Assinar fora da vez" não tem cobertura. |
| CT-018 Chave de acesso | API / E2E | atores `accessKey*` já exclusivos | Provável: `access-keys.ts`, `ui/internal/access-keys.ts`, `access-key-document-creation.spec.ts` (api e e2e). Menor custo: estender esses specs, sem entrada nova. Notificação ao concedente sem evidência. |
| CT-019 Identidade visual do órgão | E2E | **3ª instância exclusiva** (condicional) | Sem helper de edição de personalização; `updateInstance` não é exportado em `services/instance.ts`; `ui/internal/instance.ts` cobre só o cadastro. |
| CT-020 Indicadores de Servidores | E2E | baseline (leitura) | Parcial: `ui/internal/statistics.ts` + `E73` cobrem os 3 cards (total/ativos/inativos). Gráficos por status e por nível dependem de job de BI que o seed não garante. |

---

## Escopo desta onda

*Candidatos, sujeitos às pendências e ao gate (nenhum CT foi validado manualmente ainda).*

- **Com base no código existente (mapear e completar):** CT-001, CT-004, CT-005, CT-009, CT-010, CT-011, CT-012, CT-014, CT-015, CT-017, CT-018, CT-016 (lado interno).
- **Com massa nova identificada:** CT-003 (`statusTarget`), CT-006 (módulo + A&S), CT-004 (`twoSectorCreator`).
- **CT-020 parcial:** só os 3 cards.

## Fora de escopo

- **CT-007 e CT-008:** nada no código (sem serviço nem helper de Zona/Categoria de uso/Processo urbanístico) e o comportamento de revisão de Anexo não está confirmado.
- **CT-020 (gráficos por status e por nível):** dependem de job de BI fora do controle do seed.
- **CT-016 (acesso público ao Jornal Oficial sem login):** sem helper nem evidência.
- **Em pendência, não decididos:** CT-002, CT-013 e CT-019 (ver **Pendências de decisão**).

---

## Riscos

- **E-mail real:**
  - **CT-002:** a 5ª senha errada envia um e-mail de reativação ao usuário (token `ENABLE_ACCOUNT`), um por bloqueio, para a caixa Gmail compartilhada.
  - **CT-013:** o e-mail de confirmação é a própria asserção; "cadastro único por CPF/CNPJ" impede repetir a identidade, então cada execução cria uma nova (volume).
  - **CT-015, CT-017, CT-018:** podem disparar e-mail/notificação; canal não confirmado, observar antes de assumir.
  - **Seed:** `PW_AGENT_REGISTRATION=email` manda e-mail para cada servidor criado; cidadãos sempre confirmam por e-mail. Usar `invite` no primeiro seed dos servidores novos.
- **Estado compartilhado:** CT-003, CT-006 e CT-019 alteram cadastro/configuração; sem exclusividade contaminam outros specs. Bloqueio de login é da pessoa, em todas as instâncias (CPF/e-mail são únicos no ambiente).
- **Dados permanentes:** instância não pode ser excluída e a criação **avisa os analistas SOGOV** do ambiente; o `baseline.ts` vale para todos os QAs e ambientes (e-mails na 1ª criação em cada ambiente).
- **Leitura do produto:** os achados sobre `unlockSogoUserAccess`, `changePublicAgentWorkStatus` e `MAX_LOGIN_ATTEMPTS` vêm de um checkout local (`Sogov-application`, branch `development`, último commit de 14/07/2026), possivelmente defasado em relação ao homolog.
- **Ambiente:** a validação manual dos CTs é em DEV (decisão de 20/10/2026) e a suíte ataca o homolog (`PW_BASE_URL`): o comportamento precisa existir no ambiente-alvo.

---

## Massa desta entrega

> [!important] Regras da massa
> - **Cada onda registra só o que acrescenta** e linka as Análises anteriores; não repita as linhas delas.
> - **Ator/módulo/instância que um teste versionado precisa vai no `baseline.ts`** (versionado, vale para todos). `massa/<nome>.json` é pessoal, fora do git, **só para iteração local**.
> - **Rastreio no código:** comentário acima de cada entrada nova no `baseline.ts`: `// SGV-12272 · CT-0xx: <motivo>`.
> - **Versão:** um incremento de `SEED_SCHEMA_VERSION` **por entrega** (não por CT), registrado na última coluna.
> - Quem **altera** cadastro precisa de ator exclusivo: dono em `ownership.ts` e spec marcado `@shared-state`. Pool por worker só para ator usado por vários arquivos.
> - Identidades do baseline são fixas e válidas (CPF/CNPJ não mudam a cada execução). Usar `PW_AGENT_REGISTRATION=invite` no primeiro seed para não mandar e-mail a cada servidor novo.

**Novos**

| Recurso | Tipo | Novo ou reuso | CTs que usam | Exclusivo? (dono) | Dispara e-mail? | Entra em (versão do baseline / MR) |
|---|---|---|---|---|---|---|
| `lockoutTarget` (servidor GP, nível 2–3, CPF fixo) | ator | novo | CT-002 | sim — spec dono a definir (login/bloqueio) | **sim:** 1 e-mail de reativação por bloqueio; sem `sendRecoveryEmail` extra no desbloqueio | a definir |
| `statusTarget` (servidor GP, nível 2–3, CPF fixo) | ator | novo | CT-003 | sim — spec dono a definir | não esperado *(a confirmar)* | a definir |
| `twoSectorCreator` (servidor com GP + DIR) | ator | novo | CT-004 (e avaliar CT-011) | sim — spec dono a definir | não (criado por convite) | a definir |
| Módulo + A&S do CT-006 (3 setores X/Y/Z; nome de módulo ≤ 29 caracteres) | módulo + A&S | novo | CT-006 | sim — spec dono a definir | não | a definir |
| 3ª instância de identidade visual *(condicional à pendência a)* | instância | novo | CT-019 | sim | **sim:** avisa os analistas SOGOV na criação + e-mail dos servidores | a definir |
| Administrador (nível 5) e servidor de outro nível (2–4) da 3ª instância *(condicional)* | ator ×2 | novo | CT-019 | sim | por convite: não; por `email`: sim | a definir |

**Reuso**

| Recurso | Tipo | Novo ou reuso | CTs que usam | Exclusivo? (dono) | Dispara e-mail? | Entra em (versão do baseline / MR) |
|---|---|---|---|---|---|---|
| Pools `agent`, `mayor`, `secretary`, `director` (GP/SCTA/DIR) | ator | reuso (baseline atual) | CT-001, CT-005, CT-011, CT-012, CT-017 | não (pool por worker) | não | já existe |
| Pool `citizen` | ator | reuso | CT-014, CT-015, CT-017 | não | não | já existe |
| Módulos `PA`, `DO`, `CO` e A&S do baseline | módulo / A&S | reuso | CT-004, CT-005, CT-009 | não | não | já existe |
| Módulo `accessKey` (só o GP cria) | módulo | reuso | CT-004 | não | não | já existe |
| Módulos `workflow*` do baseline | módulo | reuso | CT-010 | não | não | já existe |
| Atores `accessKey*` e specs de chave de acesso | ator | reuso (estender os specs) | CT-018 | sim — `access-key-document-creation.spec.ts` | a confirmar | já existe |
| `otherInstance` ("Prefeitura Vizinha E2E") | instância | **não serve para o CT-019** | — | — | — | — |

> [!note] Por que a `otherInstance` não serve ao CT-019
> É a prefeitura de origem do cidadão (usada em toda execução por 4 specs de registro/vínculo e por `src/data/quick-registration.ts`) e **fica em implantação de propósito**, sem setor, módulo nem servidor. O CT-019 precisa de um Administrador e de outro nível logando na instância, com setor; ativá-la exige módulo e mudaria o papel da instância. A identidade visual também aparece em impressões e na verificação de assinatura de outros specs, então editá-la na instância compartilhada contamina testes em paralelo.

> [!warning] Não usar
> Os atores `seqBasic/seqSpecialist/seqSectorAdmin/seqAdmin` e `accessKey*` são exclusivos de specs próprios; `ownership.ts` e o `parallel-safety.spec.ts` reprovam o uso em outro arquivo.

---

## Pendências de decisão

Quem decide: **Rafael** (salvo indicação).

- [ ] **(a) CT-019:** criar a 3ª instância (código novo em `provision.ts`, instância permanente, avisa analistas SOGOV) ou manter o CT manual.
- [ ] **(b) CT-002:** alinhar o texto do CT com o comportamento real do produto — a 5ª senha errada gera `account-blocked` + e-mail de reativação, e a senha correta **ainda autentica** depois do bloqueio.
- [ ] **(c) CTs que ficam manuais de vez** (candidatos naturais: CT-002, CT-013, CT-019).
- [ ] **(d) Ambiente da Onda 1:** confirmar o homolog como alvo (a validação manual é em DEV).
- [ ] **(e) Convenção do baseline:** confirmar com quem o mantém um incremento de `SEED_SCHEMA_VERSION` por entrega.
- [ ] **(f) Achados do código do produto:** confirmar no homolog `userType: 'publicAgent'`, `changePublicAgentWorkStatus` e `MAX_LOGIN_ATTEMPTS`.

## Gate: pronto para planejar

- [ ] Validação manual dos CTs da onda concluída e comportamento disponível no ambiente-alvo.
- [ ] Decisões técnicas fechadas (camada e estratégia de dados por grupo).
- [ ] Escopo e **fora de escopo** claros, com o motivo de cada CT que fica manual.
- [ ] Tabela **Massa desta entrega** preenchida (incluindo e-mail e dono dos exclusivos).
- [ ] Riscos de e-mail e dado permanente avaliados com o responsável.
- [x] Análises anteriores linkadas (primeira onda: nenhuma).

Fechado o gate, seguir para [[02 - Plano de automação]].
