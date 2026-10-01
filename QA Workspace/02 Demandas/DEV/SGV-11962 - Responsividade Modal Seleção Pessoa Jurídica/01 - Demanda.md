---
prioridade: media
origem: observado
pontos_alocados: ""
---

# SGV-11962 — Responsividade do modal de seleção de Pessoa Jurídica

**Ticket de origem:** observado em uso real · **Protótipo:** [Figma — Refatoração Pessoa Jurídica (Interno/Externo)](https://www.figma.com/design/fgpK9HLfUsaQJm6vx9iocF/Refatora%C3%A7%C3%A3o-Pessoa-Jur%C3%ADdica--Interno---Externo-?node-id=1361-2992)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Automação:** [[06 - Automação]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** confirmar `pontos_alocados` e rotear pro DEV.

---

## Problema / contexto

O modal que aparece para selecionar a Pessoa Jurídica quebra e não tem responsividade hoje. Design já trouxe o protótipo de como deve ficar, incluindo o comportamento no mobile, no Figma vinculado acima.

**Evidência:**
![[QA Workspace/Evidências/Desenvolvimento/SGV-11962 - Responsividade, incorreto.mp4]]

## Objetivo

O modal de seleção de Pessoa Jurídica passa a ser responsivo, conforme o protótipo atualizado no Figma (desktop e mobile).

### Entrega desta capacidade

A definir — depende da confirmação de `pontos_alocados`.

---

## Decisões de produto

- Protótipo (Figma) já define o comportamento esperado em desktop e mobile — usar como referência única, sem criar regra nova fora dele.

---

## Escopo

- Responsividade do modal de seleção de Pessoa Jurídica (layout, quebra de conteúdo, comportamento em telas menores), conforme o protótipo Figma vinculado.

---

## Fora de escopo

- Responsividade de outros modais/componentes não citados no protótipo vinculado.

---

## Critérios de aceite

- C1. O modal de seleção de Pessoa Jurídica se adapta corretamente a telas menores (mobile), sem quebra de layout, conforme o protótipo Figma "Refatoração Pessoa Jurídica (Interno/Externo)". ^c1

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Confirmar `prioridade` e `pontos_alocados` antes de rotear pro DEV.
