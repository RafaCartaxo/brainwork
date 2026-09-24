---
prioridade: media
origem: observado
pontos_alocados: ""
---

# <ID> — Bug <Título curto>

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Bug:** [[01 - Bug]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> Bug simples (1-2 critérios, sem risco de regressão em outras camadas) pode pular `02 - Plano de teste.md` direto pra `03 - Casos de teste.md` — o plano não é obrigatório pra bug, só pra melhoria/funcionalidade.

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Problema / contexto

Durante validação foi identificado que ... (o que está acontecendo, pra quem, em qual situação)

---

## Passo a passo para reproduzir

**Dado** que ...
**E** ...
**Quando** ...
**Então** ...

---

## Objetivo

Qual comportamento correto deve passar a funcionar depois da correção?

---

## Escopo

- O que esta correção cobre.

---

## Fora de escopo

- O que não muda.

---

## Critérios de aceite

- C1. O comportamento incorreto deixa de ocorrer após a correção. ^c1
- C2. O fluxo relacionado permanece íntegro após a correção. ^c2

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/) [🔍](evidencia://<ID>)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

## Checklist de entrega ao DEV

- [ ] Problema, contexto e passos de reprodução estão claros.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano (se houver) e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Nenhuma. Se houver pendência, manter `status: analise` em `00 README`.

> **Defeito, não Bug?** Se este problema saiu da execução de um CT de uma task pai (melhoria/funcionalidade) em DEV, é **Defeito**, não Bug — troque a tag em `00 README.md` (`pai: "<ID da task pai>"`) e crie este pacote dentro de `<pai>/Defeitos/`, não como pacote solto. Regra completa: [[../../Contexto/PADROES_QA.md#Defeito × Bug|PADROES_QA]].
