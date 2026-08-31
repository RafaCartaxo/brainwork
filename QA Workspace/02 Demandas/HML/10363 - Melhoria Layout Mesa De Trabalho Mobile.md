---
tags:
  - demanda
  - qa
  - melhoria
  - mesa-de-trabalho
task: "10363"
pai: ""
status: em_validacao
ambiente: HML
deploy: pendente_hml
prioridade: media
data_inicio: 2026-08-18
data_fim:
responsavel:
cadastrado_por: ""
modulo: mesa de trabalho
---
# Demanda: Melhoria no layout da mesa de trabalho mobile

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** HML (aprovada em DEV em 18/08/2026)
> - **Responsável QA:** — **sem dono**, disponível pra quem pegar
> - **Link:** *(task no Notion — evidências anexadas lá)*
> - **Parte 5** de uma melhoria maior de layout da mesa de trabalho

---

> [!warning] Card de mapeamento — sem casos de teste, de propósito
> A task é **visual** (layout da mesa de trabalho no mobile) e foi validada de forma exploratória, sem CTs formais. Este card existe pra **rastreabilidade**: registrar que a validação em DEV aconteceu, quais defeitos saíram dela e onde estão as evidências. Não é base de execução.
>
> A regra que sustenta os defeitos fecharem em DEV sem CT está em [[Sistema/Contexto/PADROES_QA#Por que o defeito fecha em DEV|PADROES_QA → Defeito × Bug]]: o que vale é a **validação da pai** cobrir a homologação, não o artefato.

> [!important] Sem dono — qualquer QA pode pegar a homologação
> O campo `responsavel` está **vazio de propósito**: o trabalho de DEV foi do Rafael, mas a validação em homologação está aberta pro time. Por isso este card **não gera pendência na fila** de ninguém — ele aparece na [[QA Workspace/Dashboard/Dashboard|Dashboard]], em "Sem dono — disponível pra pegar" ([[Sistema/Contexto/PADROES_QA#Organização de Bugs|regra]]).
>
> Quem pegar: preencher `responsavel` e o card volta pra fila normalmente.

---

> [!abstract] Resumo

Ajustes de layout da **mesa de trabalho na visualização mobile**. É a **parte 5** de uma melhoria maior, fatiada em entregas — as partes anteriores não têm card no vault.

Validada e **aprovada em DEV em 18/08/2026**. Os 4 defeitos encontrados na validação eram problemas **visuais básicos**, todos corrigidos e retestados no mesmo dia.

---

## Regras de negócio

*Não refinadas neste vault* — card de mapeamento. O escopo e o comportamento esperado vivem na task do Notion.

---

## Defeitos

Os 4 saíram da validação em DEV desta task. Seguem a esteira do defeito ([[Sistema/Contexto/PADROES_QA#Defeito × Bug|PADROES_QA]]): fecharam de `DEV/` direto pra `Concluídas/`, com `ambiente: DEV` — **não são retestados em homologação**, porque quem valida em HML é esta task.

| Defeito | Situação | Evidência |
|---|---|---|
| [[QA Workspace/02 Demandas/Concluídas/10859 - Defeito Visual 1\|SGV-10859]] | ✅ Corrigido e retestado em DEV (18/08) | Notion |
| [[QA Workspace/02 Demandas/Concluídas/10860 - Defeito Visual 2\|SGV-10860]] | ✅ Corrigido e retestado em DEV (18/08) | Notion |
| [[QA Workspace/02 Demandas/Concluídas/10861 - Defeito Visual 3\|SGV-10861]] | ✅ Corrigido e retestado em DEV (18/08) | Notion |
| [[QA Workspace/02 Demandas/Concluídas/10862 - Defeito Visual 4\|SGV-10862]] | ✅ Corrigido e retestado em DEV (18/08) | Notion |

> [!note] A numeração 1–4 é só identificação
> Segue a **ordem crescente de SGV**, não prioridade nem ordem de descoberta. Os quatro eram problemas visuais básicos e não tiveram descrição individual registrada aqui — o detalhe está em cada task do Notion, junto da gravação.

---

## Casos de teste

*Nenhum* — ver o aviso no topo. Task visual validada de forma exploratória.

---

## Evidências

> [!important] As evidências estão **no Notion**, não no vault
> Gravadas pelo celular durante a validação e anexadas diretamente nas tasks (a da melhoria e a de cada defeito). **Não há arquivo local** em `Evidências/` — por isso o 🔄 não roteia nem avisa nada sobre esta task.
>
> Se em algum momento essas gravações forem trazidas pro vault, seguir a convenção do [[QA Workspace/Evidências/README|Evidências/README]] e embedar aqui.

---

> [!tip] Observações

- **Aprovada em DEV sem passar por refinamento no vault**: a task chegou pronta, o escopo é visual e a validação foi exploratória. Registro feito pra mapeamento a pedido do Rafael.
- `deploy: pendente_hml` — aprovada em DEV, mas **não foi confirmado** se o fix já subiu pra homologação. Quem pegar a validação confere antes e remove o campo.
- **Gate de doc não executado**: não há doc de módulo de mesa de trabalho mobile em `04 Conhecimento/` cobrindo este layout. Como é card de mapeamento e a aprovação de DEV já aconteceu, fica registrado aqui em vez de virar pendência — ver o item de importação da doc de **Mesa de trabalho** que já está na fila.

---

## Histórico

- 2026-08-18 - ✅ Melhoria aprovada em DEV (validação exploratória, sem CTs; 4 defeitos encontrados, corrigidos e retestados no mesmo dia)
- 2026-08-18 - Card criado no vault para mapeamento — parte 5 de uma melhoria maior; `responsavel` deixado vazio de propósito, homologação aberta pro time
