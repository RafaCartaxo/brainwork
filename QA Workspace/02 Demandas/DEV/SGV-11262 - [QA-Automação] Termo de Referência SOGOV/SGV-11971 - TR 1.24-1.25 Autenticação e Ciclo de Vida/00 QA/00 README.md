---
status: execucao
demanda: SGV-11971
tipo: funcionalidade
ambiente: dev
etapa_atual: "QA · Validação"
---
# SGV-11971 — TR 1.24-1.25: Autenticação e ciclo de vida do usuário

> [!info]- Navegação QA/DEV  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/00 QA/03 - Casos de teste]]  
> **Validação:** [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/00 QA/04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[../01 Automação/00 - Automação|Automação]]
> **Entrega 01 — baseline na instância 225:** [[../Entrega 01 - Baseline de autenticação na instância 225/00 QA/00 README|Pacote QA]] · [[../Entrega 01 - Baseline de autenticação na instância 225/01 Automação/00 - Automação|Pacote de automação]]

> [!settings]- Controle do card  
> **Status:** `INPUT[inlineSelect(option(backlog),option(analise),option(execucao),option(validacao),option(concluido)):status]`  
> **Etapa atual:** `INPUT[inlineSelect(option(QA · Triagem),option(QA · Análise da demanda),option(QA · Plano de teste),option(QA · Casos de teste),option(DEV · Análise técnica),option(DEV · Plano de execução),option(DEV · Implementação),option(DEV · Code review),option(QA · Validação),option(Concluído)):etapa_atual]`

## Status do trabalho

| Etapa | Estado |
|---|---|
| Demanda | ✅ Preparada — 16 itens do Termo como critérios de aceite |
| Plano de teste | ✅ Preparado |
| Casos de teste | ✅ Preparados (CT-001 a CT-038 + 3 extras fora de escopo) |
| Validação | 🔄 Em andamento — **25/38 CTs confirmados** (01/10/2026); 4 achados reais, 6 falhas sem causa raiz, 3 sem código |
| Preparação Qase | 📤 Enviado (projeto SGV, suite 4 — 25 atualizados, 2 deprecated, 1 criado, 31/08/2026) |
| Automação | 🔄 Em andamento — 13 CTs identificados em Playwright (CT-001–012 e CT-038); outros 12 CTs aprovados seguem associados ao Cypress. Os 13 passaram no run registrado de 06/10/2026; placar dos 38 CTs em [[../01 Automação/02 - Validação automação\|02 - Validação automação]] |

**Entrega 01 da iniciativa:** pacote `00 QA` + `01 Automação/00–02` preparado para estabilizar o seed na **instância de teste dedicada** e validar CT-001–012 e CT-038. A implementação ainda não começou. A leitura confirmou que o código de CT-038 ainda está em `HEAD` destacado (`16c41e4`), sem commit; definir seu destino antes de encerrar a entrega. Este README e o pacote SGV-11971 continuam registrando o ciclo funcional de 38 CTs. Direção e sequência em [[../../Roadmap - Automação TR|Roadmap — Automação TR]].

> [!warning]- O alvo da automação mudou: Cypress → Playwright (01/10/2026) — correção em 02/10/2026
> O repositório migrou pra Playwright em setembro (merge `1d78bf9`). A evidência registrada em 06/10/2026 confirma que CT-001–012 e CT-038 não falharam no run amplo. Isso confirma os resultados observados, mas não demonstra execução reproduzível em outra instância. O mapa do código e do seed está em [[../../Conhecimento/Mapa do seed Playwright atual - SGV-11971|Mapa do seed Playwright atual]].

> [!info]- Origem
> **Primeiro ciclo** da guarda-chuva [[../../Conhecimento/0 - SGV-11262 - Índice|SGV-11262 — [QA-Automação] Termo de Referência SOGOV]]. Verificação de conformidade do SOGOV com os itens 1.24 e 1.25 do Termo de Referência (mais os correlatos 1.13 e 1.27.x citados pelos casos). O trabalho começou em 31/08/2026 registrado só como automação; virou verificação do Termo inteiro em 02/09/2026 e ganhou SGV próprio em 02/10/2026.

Pacote QA para `SGV-11971`:

```text
SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/
├── 00 QA/
│   ├── 00 README.md
│   ├── 01 - Demanda.md
│   ├── 02 - Plano de teste.md
│   ├── 03 - Casos de teste.md
│   ├── 04 - Validação dev.md
│   └── 05 - Preparação Qase.md
└── 01 Automação/
    ├── 00 - Automação.md
    ├── 01 - Plano de automação.md
    ├── 02 - Validação automação.md
    ├── 03 - Handoff de execução.md       ← arquivo do pacote antigo, em revisão
    └── 04 - Documentação de entrega.md   ← arquivo do pacote antigo, em revisão
```

O padrão atualizado da automação é `00 - Automação`, `01 - Plano de automação` e `02 - Validação automação`. Os arquivos `03` e `04` permanecem no pacote enquanto a informação útil é reconciliada; eles não fazem parte do fluxo novo.

---
