---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../../Arquivo/00 QA/03 - Casos de teste]]"
casos_entrega: "[[../00 QA/03 - Casos de teste]]"
repo: sogov-automation-playwright
status: planejado
---
# Plano de automação — Entrega 01: Baseline na instância 225

> [!info]- Navegação QA
> **README:** [[../00 QA/00 README|Entrega 01]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos da entrega:** [[../00 QA/03 - Casos de teste]]
> **Casos funcionais de origem:** [[../../Arquivo/00 QA/03 - Casos de teste|SGV-11971]]
> **Automação:** [[00 - Automação]]
> **Validação:** [[02 - Validação automação]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Este plano registra o recorte, a estratégia e as dependências antes da implementação. Os quatro casos técnicos de seleção/preparação estão no QA desta entrega; abaixo fica a estratégia de automação dos CTs funcionais incluídos.

## Objetivo e escopo

- **Objetivo:** usar de forma segura e repetível a instância de teste dedicada 225 e validar nela a cobertura de autenticação incluída.
- **CTs incluídos:** CT-001–012 e CT-038, definidos na SGV-11971.
- **Fora do escopo:** demais CTs da SGV-11971, criação de nova instância por execução, alteração do destino padrão de todas as suítes e expansão do seed para além dos atores necessários.

## Estratégia por suíte

| Suíte / CTs | Camada | Dados e estado inicial | Reuso / mudança necessária | Dependência ou gate |
|---|---|---|---|---|
| CT-001–009 | API | Instância 225 acessível; atores de servidor e cidadão por worker | Reusar specs, fixtures e pools atuais; permitir seleção explícita de instância e registrar alvo no manifesto | Confirmar backend da 225 e estado/autenticação dos atores |
| CT-010–012 | API | Instância 225 acessível; credenciais inválidas ou identificador gerado pelo teste | Reusar specs e fixtures existentes; garantir que a instância resolvida vem do manifesto | Confirmar backend da 225 |
| CT-038 | API | Sessão/auditoria no alvo configurado | Reusar spec existente após resolver o destino do arquivo no worktree | CT-038 está em `HEAD` destacado (`16c41e4`), sem commit |
| Setup global | API/setup | Seed amplo usado pelo projeto atualmente | Sem override, manter padrão. Com ID explícito, validar ID e nome e falhar sem fallback de criação | Executar somente o escopo desta entrega; não apontar a suíte toda à 225 |

## Pronto para implementar quando

- [ ] Backend configurado corresponde ao ambiente em que a instância 225 foi criada.
- [ ] Identidade esperada e acesso administrativo à instância foram confirmados.
- [ ] Seleção explícita por ID valida o nome e falha sem criar outro cliente.
- [ ] Com configuração ausente, o comportamento padrão atual permanece.
- [ ] Destino de CT-038 definido ou CT explicitamente bloqueado nesta rodada.

## Pronto para validar quando

- [ ] Alteração implementada e revisada.
- [ ] Seed executado duas vezes; ambas reutilizam ID 225 sem instância duplicada.
- [ ] CT-001–012 e CT-038 executados e registrados em [[02 - Validação automação]].
- [ ] Ambiente, instância e artefatos do run registrados.

**Execução direta:** se não houver outra escolha técnica, manter a tabela curta, indicar API, o reuso atual e o gate aplicável. O plano continua obrigatório mesmo quando a mudança for pequena.
