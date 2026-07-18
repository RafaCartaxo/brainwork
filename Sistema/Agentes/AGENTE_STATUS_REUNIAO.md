---
tags:
  - qa
  - agente
---
# Agente: Status — Reunião

Ler a daily de hoje e gerar o bloco **Status — reunião** (Fiz / Foco de hoje / Travas) automaticamente, no formato de standup de 30 segundos.

## Por que existe

O bloco Status — reunião é "regenerado, não acumulado" — ele deve refletir o estado atual, não acumular itens dia após dia. Hoje é feito manualmente ou sob demanda ("gera meu status da reunião"). Automatizar elimina esse passo e garante que o bloco sempre reflita o que está registrado na daily.

## Gatilhos

| Gatilho | Quando dispara |
|---|---|
| **🔄 Atualizar** | Junto com o script `qa-atualiza.py`, ao clicar o botão na Dashboard |
| **Sessão interativa** | "gera meu status da reunião" |
| **Abertura da daily** | Ao abrir a daily de hoje e o bloco estiver vazio ou desatualizado |

## O que faz

### 1. Lê a daily de hoje
Escaneia as seções:
- `## Atividades` → alimenta o **Fiz**
- `## A fazer hoje` (itens não marcados) → alimenta o **Foco de hoje**
- `## A fazer hoje` com menção a bloqueio ou `⏳` → alimenta **Travas**
- `## Bugs encontrados` com card criado hoje → entra no **Fiz**

### 2. Aplica as regras do bloco

**Regras oficiais** (definidas em [[../../../QA Workspace/01 Daily/README#Status — reunião (primeira seção da daily)\|01 Daily/README]]):

- **Cabe em 30 segundos**: máx. 3 itens por bloco
- **Emoji + numeração na frente**: mesmo padrão das Atividades
- **Agrupado por estágio**: emojis se agrupam numa linha só (`📝📤` = refinado e levado pro Notion)
- **Tudo linkado**: card quando existe; sem card, a mesa de refinamento
- **Regenerado, não acumulado**: reescreve o bloco por inteiro a cada execução
- **Sempre visível**: o callout não é recolhível
- **Trava sem dono/ação não entra**: só o que bloqueia algo seu, com quem/o que se espera

### 3. Gera o bloco

```markdown
## Status — reunião
> [!abstract] Resumo pra falar na daily (regenerado, não acumulado — máx. 3 itens por bloco)
> **Fiz**
> - 
>
> **Foco de hoje**
> - 
>
> **Travas**
> - 
```

### 4. Priorização do Fiz

Ordem de importância:
1. Validações concluídas (✅/🔁)
2. Refinamentos e análises (📝/🔎)
3. Cadastros e atualizações no Notion (📤/💡)
4. Bugs cadastrados (🐛)
5. Triagens e documentação (📋/📚)

### 5. Detecção de Travas

Considera trava:
- Item em **A fazer hoje** com `⏳` e menção a "aguardando"
- `🔴 Reaberta` sem correção disponível ainda
- Menção explícita a bloqueio por outro time/responsável
- Card sem dono claro ("definir com dev/produto")

### 6. O que NÃO entra

- Itens já concluídos sem ação pendente
- Melhorias propostas (já têm seção própria na Dashboard)
- Pendências de rotina sem bloqueio
- Itens com mais de 2 dias sem atualização (sinaliza como `⏳ parado` no Foco)

## Relação com outros agentes

- **AGENTE_ORGANIZADOR**: Alimenta as Atividades e a fila que este agente lê
- **AGENTE_MIGRACAO_CARDS**: Cards migrados hoje aparecem no Fiz

## Marca de geração

O bloco gerado inclui uma nota invisível (HTML comment) com a data/hora da última geração:

```html
<!-- gerado em 2026-07-18 08:30 -->
```

Isso permite detectar se o bloco está desatualizado (última geração ≠ hoje) e regenerar automaticamente.
