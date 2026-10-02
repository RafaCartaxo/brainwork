---
tags: [qa, automacao, handoff]
tipo: referencia
revisado: ""
---

# Handoff de execução — <ID>

> [!info]- Navegação QA
> **README do card:** [[../QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[../QA/01 - Demanda]]
> **Plano de teste:** [[../QA/02 - Plano de teste]]
> **Casos de teste:** [[../QA/03 - Casos de teste]]
> **Validação:** [[../QA/04 - Validação dev]]
> **Preparação Qase:** [[../QA/05 - Preparação Qase]]
> **Automação:** [[00 - Automação]]

> [!info] Sobre esta nota
> Documento de transição pra **outra sessão de IA continuar** a automação. É a **camada de estado/orquestração**: o que já foi feito, o que está pendente, o que não pode ser esquecido. A arquitetura completa vive em [[01 - Plano de automação]] — **não duplicada aqui de propósito**, pra não criar duas fontes que divergem. Revisão cenário a cenário (o que cada CT faz, status atual) vive em [[03 - Documentação de entrega]].

---

## Estado da Fase 1 (investigação técnica)

<o que foi descoberto, confirmado, ainda em aberto>

---

## Estado da Fase 2/3 — <X de N CTs codados, Y confirmados>

### Achados reais (não são bugs do teste — confirmar com o responsável antes de "consertar")

- <achado de produto encontrado pela automação>

### Bugs reais de teste corrigidos (esse sim é bug do código do teste, não achado de produto)

- <correção feita na automação em si>

---

## Estado do repositório (`<repo>`)

<branch de trabalho, o que está commitado/mergeado, o que está pendente de subir>

---

## Regras transversais (valem para toda automação deste pacote)

- **Fonte única dos cenários é [[../QA/03 - Casos de teste|03 - Casos de teste]].** Nunca divergir dela.
- <demais regras específicas desta automação — login via command existente, não usar agente/dado global, docs só por acréscimo, etc.>

---

## Decisões pendentes — pare e pergunte

- <decisão que só o responsável pode tomar>

---

## Verificação final (antes de considerar a automação encerrada)

- [ ] <item de verificação>

---

## Cards relacionados

- [[../QA/00 README|<ID>]] — o pacote a que esta automação pertence.

---

## Referências

- [[01 - Plano de automação]] — arquitetura completa
- [[03 - Documentação de entrega]] — revisão cenário a cenário
- [[../QA/03 - Casos de teste|03 - Casos de teste]] — fonte única dos CTs
- Repo: `<nome do repo>`
