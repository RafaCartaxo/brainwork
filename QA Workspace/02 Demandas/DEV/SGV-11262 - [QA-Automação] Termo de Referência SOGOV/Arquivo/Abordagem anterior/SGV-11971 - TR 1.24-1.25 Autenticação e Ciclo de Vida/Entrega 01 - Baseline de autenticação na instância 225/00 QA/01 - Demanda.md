---
prioridade: media
origem: conversa
pontos_alocados: ""
---

# Entrega 01 — Baseline de autenticação na instância 225

**Ticket de origem:** SGV-11971 · **Iniciativa:** SGV-11262

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|CTs da SGV-11971]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** Não se aplica; esta entrega não cria casos funcionais novos na Qase.
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** confirmar o backend da instância 225 e resolver o destino do CT-038; em seguida, implementar a seleção segura do alvo no seed.

---

## Problema / contexto

O seed procura uma instância pelo perfil fixo `E2E Automatic Test` e pode criar outra se não encontrar esse nome. Foi criada para este piloto a instância 225, “Termo De Referência - Sogov”, mas o seed atual não a seleciona. Sem uma seleção explícita, a preparação pode atingir outro cliente.

## Objetivo

Permitir que o seed e os testes de autenticação usem uma instância de teste dedicada, sem alterar o alvo padrão das demais suítes.

### Entrega desta capacidade

O seed aceitará o ID 225 como configuração explícita, validará que o nome corresponde à instância esperada, registrará o alvo no manifesto e interromperá sem criar outro cliente se a validação falhar. Sem configuração explícita, manterá o comportamento padrão. A entrega inclui a execução de CT-001–012 e CT-038 na instância 225.

---

## Decisões de produto

- O primeiro alvo é a instância dedicada 225.
- Sem ID explícito, o seed mantém seu comportamento padrão atual.
- ID ausente ou nome divergente com alvo explícito interrompe a preparação antes de criar ou alterar dados.
- Criar uma instância nova por execução fica para uma entrega separada.
- O Roteiro de Sanidade 01 fornece contexto de negócio, sem ser replicado integralmente como preset nesta entrega.
- CT-001–012 e CT-038 continuam definidos nos [[../../Arquivo/00 QA/03 - Casos de teste|casos funcionais da SGV-11971]]; esta entrega os referencia sem copiá-los.

---

## Escopo

- Seleção explícita da instância 225 e validação da identidade.
- Proteção contra criação acidental de outro cliente quando o ID foi informado.
- Preservação do caminho padrão quando a configuração específica não existe.
- Reexecução idempotente do seed e execução dos CTs de autenticação incluídos.
- Quatro verificações técnicas do seed listadas em [[03 - Casos de teste]].

---

## Fora de escopo

- Criar uma nova instância em cada execução ou CT.
- Alterar o destino padrão de todas as suítes Playwright.
- Replicar todos os módulos, setores e dados do Roteiro de Sanidade 01.
- Portar outros CTs da SGV-11971 ou ampliar o catálogo além desta fatia.

---

## Critérios de aceite

- C1. Com ID 225 explícito, o seed resolve a instância, confirma “Termo De Referência - Sogov” e grava ID/nome no manifesto. ^c1
- C2. Se o ID não existir ou o nome divergir, o seed encerra antes de provisionar dados e não cria nem seleciona outro cliente. ^c2
- C3. Sem ID explícito, o seed mantém o alvo padrão atual. ^c3
- C4. Duas execuções consecutivas reutilizam a instância 225 e não duplicam instância nem atores-chave. ^c4
- C5. CT-001–012 e CT-038 consomem o ID do manifesto e podem rodar na instância 225 sem fixar o ID nos specs. ^c5

---

## Checklist de entrega ao DEV

- [x] Decisões de escopo e comportamento estão registradas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` será definido quando a entrega receber estimativa no tracker.

---

## Pendências de decisão

- Confirmar que o ambiente configurado aponta ao backend onde a instância 225 foi criada.
- Definir o destino do arquivo CT-038, hoje em `HEAD` destacado (`16c41e4`) e sem commit.

São gates técnicos; não há decisão de produto pendente. Manter `status: analise` até resolvê-los.
