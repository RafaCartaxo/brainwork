---
tags:
  - bug
  - qa
  - assinatura
  - associar-desassociar
task: "3413"
prioridade: media
status: descartado
data_inicio: 2026-07-20
data_fim: 2026-07-20
responsavel: Rafael
cadastrado_por: ""
modulo: assinatura
ambiente: DEV
---
# Erro ao assinar despacho de desassociação de documentos

### Descrição

Reportado no Notion como "[BUG] Erro ao assinar despacho de desassociação de documentos" (Squad 3). Sem material detalhado (descrição/passo a passo) disponível no momento de trazer pro vault — card criado direto com o resultado da investigação de Rafael.

---

### Passo a passo para reproduzir

Não especificado no material disponível — ver a task original no Notion (SGV-3413) se precisar do passo a passo completo.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://3413)

**Evidência do descarte** — gravação de 20/07 mostrando que o cenário **não reproduz mais** (a assinatura em despacho de desassociação funciona). É o lastro do `status: descartado`: se o defeito reaparecer, este vídeo é o registro de que em 20/07 o comportamento estava correto.

![[3413 - nao reproduz mais assinatura em despacho de desassociacao.mp4]]

> [!note]- Por que essa evidência ficou 10 dias solta
> A gravação ficou na **raiz de `Evidências/`** de 20/07 a 30/07, e este card dizia "sem cópia local no vault" — afirmação falsa, com o arquivo a uma pasta de distância. O roteador de evidências do `qa-atualiza.py` procura o card só em `02 Demandas/`, e este já estava em `99 Arquivo/` desde o descarte; então ele avisava "card do SGV-3413 não existe" em toda execução, todos os dias. Anexada à mão em 30/07.

---

### Resultado Esperado

Deve ser possível assinar um despacho de desassociação de documentos sem ocorrência de erro.

---

### Critérios de aceite

- [x] Assinar despacho de desassociação de documentos conclui sem erro (confirmado — ver Observações)

---

### Casos de Teste Básicos

- **CT-B01 Assinar despacho de desassociação de documentos**
    Dado um despacho de desassociação de documentos ([[QA Workspace/04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]])
    Quando o usuário assinar o despacho
    Então a assinatura deve ser concluída sem erro

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: SGV-3413 (Squad 3)
- Observações: **Descartado após investigação (20/07/2026, Rafael)** — verificado diretamente que o erro não ocorre mais. Sem material de causa raiz disponível (sem MR/fix identificado até agora) — se o comportamento voltar a falhar, reabrir citando este arquivo.
- Histórico:
    - 2026-07-20 - 🗑️ Descartado (não reproduz: verificado manualmente por Rafael)
