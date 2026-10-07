---
tags:
  - qa
  - automacao
  - roadmap
tipo: roadmap
demanda: SGV-11262
status: ativo
---
# Roadmap — Automação do Termo de Referência SOGOV

> [!info] Como usar este documento
> Este roadmap registra a direção, a ordem sugerida e as dependências da iniciativa. Ele não substitui os casos de teste, o plano ou o placar de uma entrega. Para localizar documentos e ciclos, consulte o [[Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]].

## Objetivo

Evoluir a automação dos requisitos do Termo de Referência em entregas pequenas, cada uma com escopo e validação próprios. A direção é permitir uma execução reproduzível da sanidade do SOGOV por cliente/instância e ambiente, reaproveitando os mecanismos de preparação já existentes sempre que fizer sentido.

O caminho começa pela estabilização e compreensão do que já existe. A execução configurável em diferentes clientes/instâncias e ambientes é objetivo da iniciativa e será alcançada incrementalmente, conforme os pré-requisitos técnicos forem conhecidos e entregues.

## Estado atual

O ciclo **TR 1.24–1.25 — Autenticação e ciclo de vida do usuário** está registrado na [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/00 QA/00 README|SGV-11971]]. Seus artefatos de QA — demanda, plano, casos, validação e preparação Qase — permanecem próprios desse ciclo. Os 38 CTs dessa entrega continuam sendo a referência funcional do escopo.

O placar de automação registra:

- **25/38 CTs aprovados** no histórico de validação;
- **13 CTs identificados em Playwright**, aprovados e sem falhas `@auth` no run de 06/10/2026;
- **12 CTs aprovados ainda associados ao Cypress**, pendentes de porte para Playwright;
- **4 CTs com falha/achado** (015, 029, 030 e 033);
- **6 CTs bloqueados** (022, 026, 028, 034, 035 e 036);
- **3 CTs aguardando código, captura de API ou investigação** (016, 017 e 037).

O fato de um CT estar verde não confirma, por si só, que seja independente e reproduzível em outra instância. A leitura do código dos 13 CTs e do seed foi concluída; a independência operacional em outra instância ainda não foi demonstrada por execução.

**Mapeamento de código concluído em 07/10:** os 13 CTs são CT-001–012 e CT-038. Todos dependem do seed global, mas usam diretamente apenas a instância e atores por worker; nenhum usa módulo, serviço ou documento. O seed já é idempotente e grava um manifesto de IDs, mas hoje aponta para um perfil fixo de instância. O inventário detalhado e as ressalvas de cobertura estão em [[Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]].

Segundo o hub atual da SGV-11971, CT-001–012 estão na `origin/main`; CT-038 passou em execuções repetidas, mas seu código ainda está em um worktree com `HEAD` destacado e sem commit. Confirmar essa situação ao reconciliar a baseline.

> [!warning] Números sujeitos a reconciliação
> As notas anteriores divergem sobre a quantidade restante a portar e algumas ainda descrevem Cypress como alvo. Até a revisão do pacote SGV-11971, use o placar em [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/02 - Validação automação|02 - Validação automação]] como referência dos estados por CT; o run de 06/10 cobre a suíte ampla e confirma apenas que os 13 CTs `@auth` não falharam naquela execução.

## Entregas existentes

| Entrega | Escopo | Situação |
|---|---|---|
| [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/00 QA/00 README\|SGV-11971 — TR 1.24–1.25]] | Ciclo funcional de autenticação e ciclo de vida: critérios, 38 CTs, validação e automação associada | 🔄 Em andamento; fonte atual dos CTs e do placar |
| Baseline Playwright — 13 CTs | CT-001 a CT-012 e CT-038 | ✅ Verdes no run registrado; dependências mapeadas no código, execução em outra instância ainda não validada |

O pacote padrão de automação da entrega usa [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/00 - Automação|00 — Automação]], [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/01 - Plano de automação|01 — Plano de automação]] e [[SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/01 Automação/02 - Validação automação|02 — Validação automação]]. Os arquivos `03 - Handoff de execução` e `04 - Documentação de entrega` ainda existem no pacote antigo; não são parte do padrão atualizado. Sua destinação será decidida ao reconciliar a documentação, preservando informação útil.

## Próximos passos e entregas candidatas

As linhas abaixo são candidatas de roadmap, não demandas já criadas. O escopo final das implementações depende da investigação inicial.

| Ordem | Entrega / passo | Resultado esperado | Dependência | Situação |
|---:|---|---|---|---|
| 1 | **Reconciliar documentação e baseline** | Alinhar números, framework-alvo e status entre índice, README, hub e placar; confirmar estado do código CT-038 | Mapeamento de código já feito | 🔜 Próximo passo — atualização documental |
| 2 | **Definir o alvo de instância do seed** | Decidir se a execução cria/reusa uma instância de teste ou prepara uma instância existente; registrar permissões e parâmetros necessários | Inventário atual em [[Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]] | 📝 Decisão necessária antes do desenho da implementação |
| 3 | **Primeira entrega técnica: alvo configurável para a fatia de autenticação** | Executar CT-001–012 e CT-038 contra um alvo selecionado, preparando/reusando apenas os dados necessários e mantendo o resultado isolado por CT | Passos 1–2; critério de aceite próprio e escopo técnico confirmado | 📝 Candidata; não criar demanda até fechar a decisão do passo 2 |
| 4 | **Portar e validar grupos restantes de CTs** | Evoluir Playwright em fatias funcionais delimitadas, cada qual com seu próprio pacote `00–02` e CTs exclusivos | Mapeamento dos dados/estados por grupo e decisões dos CTs incluídos | 📝 Candidata; grupos a definir |
| 5 | **Desbloquear CTs pendentes de comportamento/API** | Separar descoberta de API, investigação de falhas e decisões de produto da tarefa de porte | Evidência ou decisão técnica/produto por CT | ⏳ Dependências abertas |
| 6 | **Expandir preparação reutilizável conforme necessidade** | Acrescentar ao seed somente os dados e estados exigidos pelas próximas fatias; não criar um catálogo geral do SOGOV | Necessidades confirmadas nas entregas de CTs | 📝 Candidata contínua |
| 7 | **Executar a sanidade por cliente/instância e ambiente** | Preparar e executar a cobertura validada com configuração explícita por alvo e ambiente | Passos 2–6, autenticação e acesso compatíveis | 🎯 Objetivo da iniciativa, evolução incremental |

Cada futura entrega acompanhará apenas os CTs do seu escopo em seu pacote `00–02`. Se uma entrega for de preparação/infraestrutura, terá critérios de aceite próprios e CTs-piloto explícitos. O placar consolidado desta iniciativa deverá apontar para os resultados por entrega, sem duplicar a validação detalhada dos CTs.

## Ordem sugerida

```mermaid
flowchart TD
    M[Mapa do seed e dependências atuais<br/>documentado] --> A[Reconciliar documentação e baseline]
    A --> B[Definir como selecionar/criar/reusar a instância]
    B --> C[Planejar entrega-piloto com escopo e aceite próprios]
    C --> D[Preparar os dados necessários ao escopo]
    D --> E[Validar CTs do piloto no alvo configurado]
    E --> F[Estender a cobertura em entregas delimitadas]
    G[Resolver investigação, API e decisões de produto] --> F
    F --> H[Sanidade reproduzível por cliente/instância e ambiente]
```

## Critérios para abrir uma nova entrega

Criar uma demanda filha somente quando a análise confirmar uma fatia executável e revisável. O plano de cada entrega deve declarar problema, objetivo, CTs incluídos e excluídos, dados/estados necessários, dependências, estratégia e critério de aceite. A validação registra apenas os CTs daquela fatia; a nota da iniciativa mantém a visão geral e links para as entregas.

Não abrir agora demandas para todos os grupos restantes, nem assumir que é necessário construir um mecanismo chamado `Preset`. A investigação do código e dos 13 CTs atuais deve determinar a forma e a sequência das primeiras implementações.
