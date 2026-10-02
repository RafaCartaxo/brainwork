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
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[Automação/Plano de Automação|Plano]] · [[Automação/Handoff de execução|Handoff de execução]] · [[Automação/Documentação de Entrega|Documentação de Entrega]]

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
| Automação | 🔄 Em andamento — 35/38 codados em Cypress; **alvo migrou pra Playwright**, código a portar |

**Próximo passo:** decidir se os 4 achados reais de produto (CT-015, CT-029/030, CT-033) viram defeitos com SGV próprio ou seguem como achado de conformidade — decisão adiada em 02/10/2026. Em paralelo, portar a suíte de Cypress pra Playwright.

> [!warning]- O alvo da automação mudou: Cypress → Playwright (01/10/2026)
> O repo `sogov-automation-test` migrou pra Playwright em setembro (merge `1d78bf9`) enquanto esta automação estava parada. Tudo que está em `Automação/` descreve o trabalho em **Cypress** — continua válido como levantamento de regra de negócio, captura de API e placar de CT, mas o código terá de ser portado. O lado Playwright não tem nenhuma cobertura deste TR (zero ocorrências de `CT-0` em `playwright/`). Arquitetura e convenção nova em [[QA Workspace/04 Conhecimento/Referências/Automação Playwright|Automação Playwright]].

> [!info]- Origem
> **Primeiro ciclo** da guarda-chuva [[../Conhecimento/0 - SGV-11262 - Índice|SGV-11262 — [QA-Automação] Termo de Referência SOGOV]]. Verificação de conformidade do SOGOV com os itens 1.24 e 1.25 do Termo de Referência (mais os correlatos 1.13 e 1.27.x citados pelos casos). O trabalho começou em 31/08/2026 registrado só como automação; virou verificação do Termo inteiro em 02/09/2026 e ganhou SGV próprio em 02/10/2026.

Pacote QA para `SGV-11971`:

```text
SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/
├── 00 README.md
├── 01 - Demanda.md
├── 02 - Plano de teste.md
├── 03 - Casos de teste.md
├── 04 - Validação dev.md
├── 05 - Preparação Qase.md
└── Automação/
    ├── Plano de Automação.md
    ├── Handoff de execução.md
    └── Documentação de Entrega.md
```

---
