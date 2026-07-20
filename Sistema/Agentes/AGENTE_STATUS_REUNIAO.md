---
tags:
  - qa
  - agente
---
# Agente: Status — Reunião

Ler a daily de hoje e gerar o bloco **Status — reunião** (Fiz / Foco de hoje / Travas) automaticamente — lista rastreável do que foi feito, não roteiro de fala.

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

- **Lista rastreável, sem limite de itens**: um item por linha, sem cortar pra caber num tamanho fixo
- **Emoji + numeração na frente**: mesmo padrão das Atividades
- **Agrupado por estágio**: emojis se agrupam numa linha só (`📝📤` = refinado e levado pro Notion; `🗑️🔎` = descarte + análises no mesmo tema; `🐛📝` = bug trazido pro vault já com card refinado) — e itens **diferentes mas do mesmo tipo de trabalho** também podem ser consolidados numa linha só quando o detalhe completo já está em Planejamento (ex.: "5 MRs revisados a nível de escopo — SGV-A, SGV-B, SGV-C" em vez de 5 linhas separadas)
- **Tudo linkado**: card quando existe; sem card, a mesa de refinamento
- **Regenerado, não acumulado**: reescreve o bloco por inteiro a cada execução
- **Sempre visível**: o callout não é recolhível
- **Trava sem dono/ação não entra**: só o que bloqueia algo seu, com quem/o que se espera

### 3. Gera o bloco

```markdown
## Status — reunião
> [!abstract] Lista do que foi feito hoje (regenerado, não acumulado)
> **Fiz**
> - 
>
> **Foco de hoje**
> - 
>
> **Travas**
> - 
```

### 4. Ordem do Fiz

Ordem de execução — a ordem em que os itens aconteceram no dia (a mesma ordem em que já aparecem em Atividades), não por tipo/importância. Todo tipo de trabalho do dia entra (validação, refinamento, Notion, bug, triagem/documentação, automação/MR) — não existe categoria que fique de fora por não caber num ranking.

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
