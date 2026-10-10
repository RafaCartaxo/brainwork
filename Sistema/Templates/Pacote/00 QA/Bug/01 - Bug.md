---
prioridade: media
origem: observado
pontos_alocados: ""
---

# <ID> — Bug <Título curto>

> [!info]- Navegação QA/DEV
> **README do card:** [[Sistema/Templates/Pacote/00 QA/00 README|Abrir README do card]]
> **Bug:** [[Sistema/Templates/Pacote/00 QA/Bug/01 - Bug]]
> **Plano de teste:** [[Sistema/Templates/Pacote/00 QA/02 - Plano de teste]]
> **Casos de teste:** [[Sistema/Templates/Pacote/00 QA/03 - Casos de teste]]
> **Validação:** [[Sistema/Templates/Pacote/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[Sistema/Templates/Pacote/00 QA/05 - Preparação Qase]]
> **Automação:** [[../01 Automação/00 - Automação|Automação]] *(opcional — só quando houver cobertura automatizada)*

> Bug simples (1-2 critérios, sem risco de regressão em outras camadas) pode pular `02 - Plano de teste.md` direto pra `03 - Casos de teste.md` — o plano não é obrigatório pra bug, só pra melhoria/funcionalidade.

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que ...

---

## Passo a passo para reproduzir

**Dado** que ...
**E** ...
**Quando** ...
**Então** ...

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/) [🔍](evidencia://<ID>)

Pendência — nenhuma evidência (vídeo/print) anexada ainda.

---

## Resultado Esperado

-

---

## Critérios de aceite

- [ ] O comportamento incorreto deixa de ocorrer após a correção.
- [ ] O fluxo relacionado permanece íntegro após a correção.

---

## Checklist de entrega ao DEV

- [ ] Sintoma, ambiente e passos de reprodução estão claros.
- [ ] Resultado esperado está definido.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

> **Defeito, não Bug?** Se este problema saiu da execução de um CT de uma task pai (melhoria/funcionalidade) em DEV, é **Defeito**, não Bug — troque a tag em `00 README.md` (`pai: "<ID da task pai>"`) e crie este pacote dentro de `<pai>/Defeitos/`, não como pacote solto. Regra completa: [[../../../../Contexto/PADROES_QA.md#Defeito × Bug|PADROES_QA]].
