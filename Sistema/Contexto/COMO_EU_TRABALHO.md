---
tags:
  - qa
  - contexto
---
# Como Eu Trabalho

## Sobre
Atuo como Analista de Testes (QA), trabalhando principalmente com validações funcionais, exploratórias, regressões, homologações, sanidades e análise de regras de negócio. Meu objetivo é garantir que as entregas atendam ao comportamento esperado, às regras documentadas e à experiência do usuário.

## Rotina
Começo o dia pela [[../../Dashboard/Dashboard|Dashboard]] — ela reúne a nota diária de hoje, os KPIs de bugs (abertos/resolvidos, por ambiente, por prioridade) e as pendências em aberto do Inbox e das dailies num só lugar, antes de entrar em cada pasta específica.

## Ambientes

### Desenvolvimento (DEV)
Utilizado para validação inicial de bugs, melhorias, funcionalidades e POCs.
- Execução de testes exploratórios
- Criação de [[../Skills/SKILL_CASOS_DE_TESTE.md|casos de teste]]
- Registro de [[../Skills/SKILL_BUGS.md|bugs]]
- Levantamento de dúvidas de negócio
- Validação de regras funcionais

### Homologação (HML)
Utilizado para revalidação de correções, regressões, sanidades de versão e validação final antes de produção. Nem sempre a mesma pessoa que validou em DEV realiza a validação em HML.

### Produção (PROD)
Normalmente utilizada apenas para análises, investigações e validação de comportamentos reportados.

## Tipos de Demandas

### Bug
Correção de comportamento incorreto já existente. Exige reprodução do problema, evidência, resultado esperado e critérios de aceite quando aplicável. É sempre uma nota única e autocontida (sem hub separado) — ver [[PADROES_QA.md#Organização de Bugs|regras de status, ambiente e organização de pastas]].

### Melhoria
Ajuste ou evolução de uma funcionalidade existente. Exige análise de escopo, [[../Skills/SKILL_CASOS_DE_TESTE.md|casos de teste]] e validação de regras de negócio.

### Funcionalidade
Implementação de um novo fluxo ou comportamento. Exige [[../Skills/SKILL_PLANO_DE_TESTE.md|plano de teste]], [[../Skills/SKILL_CASOS_DE_TESTE.md|casos de teste]] e validação completa do fluxo.

### POC
Validação de conceito ou análise exploratória. Pode gerar evidências, bugs, melhorias e conclusões técnicas.

### Sanidade
Validação rápida dos principais fluxos de uma versão. Objetivo: identificar bloqueios críticos e garantir estabilidade mínima para continuidade dos testes.

## Evidências
Sempre que possível registrar vídeos, prints, links e arquivos auxiliares. O guia completo (gravação com OBS, renomear, mover pra subpasta, embedar, links 📁/🔍, gravação compartilhada) está em [[../../QA Workspace/Evidências/README|Evidências/README]].

Detalhe de formatação pra bugs: ver [[../Skills/SKILL_BUGS#Evidências|SKILL_BUGS]].

## Diário
Utilizado para registrar atividades realizadas, demandas em andamento, bugs encontrados, melhorias de produto propostas, anotações rápidas, pendências e próximos passos. O diário não deve ser utilizado como documentação definitiva da demanda. Regra de como e quando linkar um SGV pro card dele, e de como registrar melhorias propostas: ver [[../../01 Daily/README|01 Daily/README]].

## Demandas
Melhoria, Funcionalidade e POC podem ter uma nota principal (hub) com [[../Skills/SKILL_PLANO_DE_TESTE.md|plano de teste]], [[../Skills/SKILL_CASOS_DE_TESTE.md|casos de teste]] e evidências. Bug é diferente: não usa hub, é sempre uma nota única com [[../Skills/SKILL_BUGS.md|estrutura própria]].
