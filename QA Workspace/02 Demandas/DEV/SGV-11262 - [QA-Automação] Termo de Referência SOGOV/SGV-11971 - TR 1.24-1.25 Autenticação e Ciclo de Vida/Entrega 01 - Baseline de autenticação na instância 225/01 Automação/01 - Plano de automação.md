---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
casos_funcionais_origem: "[[../../Arquivo/00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
status: planejado
---
# Plano de automação — Entrega 01: Baseline na instância 225

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos técnicos da entrega:** [[../00 QA/03 - Casos de teste]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|CTs da SGV-11971]]
> **Automação:** [[00 - Automação]]
> **Validação automação:** [[02 - Validação automação]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Este plano registra o escopo, a estratégia e as dependências antes da implementação. O andamento geral fica em [[00 - Automação]]; o placar atual fica em [[02 - Validação automação]].

## Objetivo e escopo

- **Objetivo:** selecionar a instância 225 com segurança pelo seed e executar nela os casos técnicos e funcionais incluídos.
- **CTs técnicos:** SEED-001–004 em `../00 QA/03 - Casos de teste`.
- **CTs funcionais:** CT-001–012 e CT-038, definidos no pacote funcional da SGV-11971.
- **Fora do escopo:** demais CTs do ciclo, criar cliente por execução, mudar o alvo padrão das outras suítes e expandir o catálogo de dados.

## Estratégia por suíte

| Suíte / CTs | Camada | Dados e estado inicial | Reuso / mudança necessária | Dependência ou gate |
|---|---|---|---|---|
| SEED-001–004 | Unidade/API | ID 225, nome esperado, configuração ausente e identidade divergente em testes controlados | Adicionar seleção opcional por ID, validar nome e falhar sem fallback de criação; sem ID preservar o perfil atual | Confirmar backend; testar alvo inválido sem provisionar dados |
| CT-001–009 | API | Instância 225 e atores de servidor/cidadão preparados por worker | Reusar specs, fixtures e pools existentes; specs consomem alvo do manifesto | Confirmar backend e autenticação dos atores |
| CT-010–012 | API | Instância 225; credenciais inválidas ou identificador gerado pelo teste | Reusar specs e fixtures existentes; garantir alvo pelo manifesto | Confirmar backend |
| CT-038 | API | Sessão/auditoria no alvo configurado | Reusar spec existente | Resolver arquivo `16c41e4`, hoje em HEAD destacado e sem commit |
| Setup global | API/setup | Seed atual também prepara recursos de outras suítes | Sem override preservar padrão; com ID explícito validar identidade e não criar outra instância | Executar somente esta fatia; não apontar a suíte completa à 225 |

## Pronto para codar quando

- [ ] CTs e comportamento esperado estão definidos em [[../00 QA/03 - Casos de teste]] e no pacote funcional de origem.
- [ ] Backend e identidade da instância 225 foram confirmados.
- [ ] Seleção do alvo, validação do nome e falha sem criação alternativa estão definidas.
- [ ] O comportamento padrão sem configuração específica foi preservado.
- [ ] Destino de CT-038 definido ou caso explicitamente bloqueado nesta rodada.

## Pronto para validar quando

- [ ] Implementação concluída e revisada.
- [ ] Seed executado duas vezes; ambas usam ID 225 sem instância duplicada.
- [ ] SEED-001–004 e CT-001–012/038 registrados em [[02 - Validação automação]] e [[../00 QA/04 - Validação dev]].
- [ ] Ambiente, instância e artefatos de execução registrados.

**Execução desta entrega:** rodar somente o seed e os casos listados acima com seleção explícita habilitada. Não apontar a suíte completa à 225. Criar instância nova por execução será tratado separadamente.
