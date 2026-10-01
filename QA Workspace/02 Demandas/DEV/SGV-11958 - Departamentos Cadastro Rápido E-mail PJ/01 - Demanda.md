---
prioridade: media
origem: observado
pontos_alocados: ""
---

# SGV-11958 — Cadastro rápido de PJ passa a solicitar e-mail

**Ticket de origem:** SGV-11178 (defeito [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]], descartado) · **Protótipo:** a confirmar (ver Pendências de decisão)

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
> **Próximo passo:** confirmar com produto/DEV os detalhes do campo de e-mail e o link do protótipo atualizado no Figma.

---

## Problema / contexto

Durante a validação da SGV-11178 (cadastro rápido de Departamentos), foi identificado que o seletor de Pessoa Jurídica não trazia nenhuma opção quando a PJ não possuía Nome fantasia cadastrado ([[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]], CT-029/C29). Em vez de implementar o fallback originalmente esperado (exibir Razão Social + CNPJ), o produto decidiu redesenhar a identificação da PJ no cadastro rápido, passando a também capturar/exibir o e-mail — o protótipo no Figma já foi atualizado nesse sentido.

## Objetivo

O formulário de cadastro rápido de Pessoa Jurídica passa a solicitar/exibir o campo e-mail, conforme o novo protótipo.

### Entrega desta capacidade

A definir — depende da confirmação do protótipo atualizado (ver Pendências de decisão).

---

## Decisões de produto

- Protótipo (Figma) do cadastro rápido de PJ já foi atualizado com o campo de e-mail — link ainda não anexado aqui (ver Pendências de decisão).
- O defeito [[QA Workspace/02 Demandas/DEV/SGV-11178 - Departamentos Cadastro Rápido/Defeitos/SGV-11957 - Defeito Seletor De PJ Sem Nome Fantasia Não Traz Nada|SGV-11957]] foi descartado — o fallback originalmente esperado em C29 da SGV-11178 não será implementado; esta nova capacidade substitui aquele encaminhamento.

---

## Escopo

- Campo de e-mail no formulário de cadastro rápido de Pessoa Jurídica (mesmo atalho de origem da SGV-11178, embutido nos componentes de seleção de pessoa).

---

## Fora de escopo

- Cadastro rápido de Pessoa Física e Departamento — sem alteração neste momento.
- Fluxos de cadastro completo/dedicado (fora do atalho rápido).
- Reteste do defeito SGV-11957/CT-029 — decisão de produto já fechou aquele encaminhamento, sem pendência de revalidação dele.

---

## Critérios de aceite

- C1. O formulário de cadastro rápido de Pessoa Jurídica exibe um campo de e-mail, conforme o protótipo atualizado no Figma. ^c1

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Link do protótipo (Figma) atualizado — anexar aqui, pra detalhar os demais critérios (obrigatoriedade do campo, validação de formato, posição no formulário, mensagens de erro).
- Confirmar se o campo e-mail é obrigatório ou opcional no cadastro rápido de PJ.
- Confirmar `prioridade`, `pontos_alocados` e `modulo` antes de rotear pro DEV.
