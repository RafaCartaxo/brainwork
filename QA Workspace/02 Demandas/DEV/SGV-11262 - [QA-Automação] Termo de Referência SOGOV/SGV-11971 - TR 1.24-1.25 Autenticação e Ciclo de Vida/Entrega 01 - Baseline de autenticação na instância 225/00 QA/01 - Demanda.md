---
prioridade: media
origem: conversa
pontos_alocados: ""
---

# Entrega 01 — Baseline de autenticação na instância 225

**Ticket de origem:** SGV-11971 (demanda-pai) · **Iniciativa:** SGV-11262

> [!info]- Navegação QA/DEV
> **README:** [[00 README]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos desta entrega:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Automação:** [[../01 Automação/00 - Automação|Pacote de automação]]

> [!info] Próximo passo
> Implementar a seleção explícita e segura da instância 225 no seed Playwright.

## Problema / contexto

O seed atual procura uma instância pelo nome fixo E2E Automatic Test e pode criar outra se não a encontrar. Foi criada para este piloto a instância 225, “Termo De Referência - Sogov”. O seed ainda não a seleciona e uma execução sem ajuste pode preparar outra instância.

## Objetivo

Preparar e validar o baseline Playwright de autenticação na instância 225, mantendo o comportamento atual como padrão para as demais suítes quando não houver configuração explícita do alvo.

### Entrega desta capacidade

- Selecionar a instância pelo ID 225 quando a configuração específica estiver presente.
- Conferir o nome esperado antes de provisionar dados.
- Registrar o ID e o nome efetivamente usados no manifesto.
- Interromper com erro claro se o ID não existir, o nome divergir ou o ambiente não corresponder.
- Executar o seed de forma idempotente e validar CT-001–012 e CT-038 na instância dedicada.

## Decisões de produto

- A instância 225 é o alvo fixo do primeiro piloto; não criar uma instância nova a cada CT.
- Sem configuração explícita do ID, manter o comportamento atual do seed.
- O teste de criação de uma instância nova será uma entrega separada.
- O Roteiro de Sanidade 01 serve como contexto de negócio; não será copiado como preset nesta entrega.
- Os CTs funcionais pertencem à SGV-11971 e serão referenciados, não duplicados.

## Escopo

- Seleção por ID com validação do nome esperado.
- Proteção contra criação acidental de outro cliente quando o ID explícito foi informado.
- Preservação do caminho padrão atual sem override.
- Reexecução do seed e validação dos CTs de autenticação na instância 225.

## Fora de escopo

- Alterar o destino padrão de todas as suítes Playwright.
- Criar um cliente novo por execução.
- Replicar todos os módulos, setores e dados descritos no roteiro de sanidade.
- Portar outros CTs da SGV-11971.

## Critérios de aceite

- C1. Com ID 225 configurado, o seed busca essa instância e confirma que seu nome é “Termo De Referência - Sogov”. ^c1
- C2. Se o ID não existir ou o nome não corresponder, o seed encerra com erro antes de criar ou alterar dados de outra instância. ^c2
- C3. Sem configuração explícita do ID, o seed conserva o alvo padrão atual. ^c3
- C4. Duas execuções consecutivas com o ID 225 reutilizam a mesma instância e registram esse ID no manifesto. ^c4
- C5. CT-001–012 e CT-038 podem consumir o ID do manifesto e concluir na instância 225, sem fixar o ID dentro dos specs. ^c5

## Checklist de entrega ao DEV

- [ ] Ambiente configurado corresponde ao backend da instância 225.
- [ ] Critérios e escopo estão claros.
- [ ] Plano e casos técnicos estão vinculados.
- [ ] Estado da instância e acesso de administrador permitem a preparação.
- [ ] Pontos alocados definidos no tracker, quando a demanda filha for registrada.


## Pendências de decisão

Não há decisões de produto pendentes. A confirmação do backend da instância 225 e o destino do CT-038 são gates técnicos registrados no plano de automação.
