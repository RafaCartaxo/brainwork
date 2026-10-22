---
prioridade: media
origem: validação
pontos_alocados: ""
---

# SGV-12379 — Mesa de trabalho não carrega mais documentos no scroll após trocar de setor

> [!info]- Navegação QA/HML
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/00 README|Abrir README do card]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/03 - Casos de teste|03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-12379 - Bug Mesa de trabalho não carrega documentos no scroll após trocar de setor/00 QA/04 - Validação HML|04 - Validação HML]]

> [!settings]- Controle do bug
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Descrição

Durante validação foi identificado que, depois de trocar de setor na mesa de trabalho, o **scroll não carrega mais documentos**. Ao atualizar a página (F5), o carregamento volta ao normal.

---

## Passo a passo para reproduzir

**Dado** que estou na mesa de trabalho no setor A
**Quando** troco para o setor B e a mesa é carregada
**E** faço scroll na mesa para carregar mais documentos
**Então** os documentos não carregam
**E** só depois de atualizar a página (F5) voltam a carregar normalmente

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://12379)

![[12379 - Ao realizar troca de Setor, documentos da mesa não carregam corretamente.mp4]]

---

## Resultado Esperado

O scroll carrega mais documentos do setor B logo após a troca de setor, **sem** precisar atualizar a página.

---

## Critérios de aceite

- [ ] Após trocar de setor, o scroll carrega mais documentos do novo setor, sem atualizar a página (F5).
- [ ] Regressão: no setor em que a mesa foi aberta, sem trocar de setor, o scroll segue carregando mais documentos.
- [ ] Regressão: trocar de setor mais de uma vez em sequência mantém o scroll funcionando em todos os setores.

---

## Ambiente

- Ambiente: Homologação
- Versão: a preencher

---

## Informações adicionais

- Notion: [SGV-12379 no Backlog](https://app.notion.com/p/40072f8c899081289428ecda76563d64)
- Módulo relacionado: [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]]
- Observações:
  - **O que a doc do módulo diz** (seção "Switch de setores"): ao clicar para mudar o setor, deve ser exibido um carregamento (load) e o usuário é direcionado para a **mesa do setor selecionado**. O estado "setor selecionado" é fixado para a próxima sessão.
  - **O que a doc não trata:** o carregamento de mais documentos por scroll (paginação/rolagem da listagem da mesa), nem o comportamento desse carregamento depois da troca de setor. A única paginação descrita na doc é a do dropdown de busca em outras mesas (10 por vez, botão "Carregar mais resultados"), que é outro componente.
  - Causa raiz não investigada.
- Histórico:
    - 2026-10-21 - 🐛 Bug cadastrado (reproduzido em homologação)
