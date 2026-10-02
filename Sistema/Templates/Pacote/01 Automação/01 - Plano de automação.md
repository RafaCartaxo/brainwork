---
tags: [qa, automacao]
criado: ""
revisado: ""
status: planejando
---

# Plano de Automação — <ID>

> [!info]- Navegação QA
> **README do card:** [[../QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../QA/01 - Demanda]]
> **Plano de teste:** [[../QA/02 - Plano de teste]]
> **Casos de teste:** [[../QA/03 - Casos de teste]]
> **Validação:** [[../QA/04 - Validação dev]]
> **Preparação Qase:** [[../QA/05 - Preparação Qase]]
> **Automação:** [[00 - Automação]]

> [!info] Sobre esta nota
> Plano técnico de arquitetura pra automatizar os CTs de [[../QA/03 - Casos de teste|03 - Casos de teste]] no repositório `<repo>`. Escrito antes de tocar no repo — mexer no repo é passo separado, autorizado depois. Não duplica estado/progresso (fica em [[02 - Handoff de execução]]) nem revisão cenário a cenário (fica em [[03 - Documentação de entrega]]) — só arquitetura e decisões de como construir.

---

## Resumo

<objetivo da automação, framework escolhido, nº de CTs alvo>

---

## Pontos-chave

### 1. Organização de pastas/arquivos no repo

<convenção de nome de spec/arquivo — 1 por suíte/domínio ou por CT>

### 2. Estratégia de reaproveitamento

<commands/factories/fixtures já existentes a reaproveitar; o que precisa ser criado>

### 3. Camada API vs E2E — regra geral

<quando um CT é melhor coberto via API e quando precisa de E2E de verdade>

### 4. Caminho de investigação técnica

<o que precisa ser descoberto antes de codar — captura de API, shape de payload, mutation/enum reais>

### 5. Faseamento

<fases do trabalho — ex.: Fase 0 investigação, Fase 1 infraestrutura, Fase 2 codar, Fase 3 validar>

---

## Dúvidas em aberto

- <pergunta pra confirmar antes de assumir>

---

## Aplicação no QA / Sogov

<como este plano vira trabalho real — ordem de execução, gates antes de autorizar>

---

## Referências

- [[../QA/03 - Casos de teste|03 - Casos de teste]] — fonte única dos CTs
- Repo: `<nome do repo>`
