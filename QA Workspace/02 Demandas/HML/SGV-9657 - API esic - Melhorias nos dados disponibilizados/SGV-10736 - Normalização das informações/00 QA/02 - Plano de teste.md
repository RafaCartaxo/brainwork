---
demanda: "[[01 - Demanda]]"
status: concluido
responsavel: Rafael
pontos: ""
---

# Plano de teste — SGV-10736

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/00 README|Abrir README do card]]
> **Demanda/Bug:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar que os endpoints de **listagem de solicitações** e de **estatísticas** da API e-SIC passam a retornar os campos novos descritos em `01 - Demanda` (C1–C10), sem quebrar o contrato já existente usado pelos clientes (ex.: relatório da ATRICOM).

---

## Riscos e escopo

- **Risco principal:** cálculo de `orderDateDeadline` (dias úteis vs. corridos, solicitação sem prazo configurado) é a regra mais propensa a erro de borda — concentrar atenção nela.
- **Risco secundário:** campos do solicitante Pessoa Física (`dataNascimento`, `genero`) dependem de cadastro prévio — testar tanto o caso completo quanto o incompleto, sem gerar erro 500.
- **Fora do escopo desta rodada:** qualquer validação de tela (Parte 2 — SGV-10735, impedida). Performance/carga do endpoint não é objeto deste plano.

---

## Estratégia de teste

- **API/contrato:** chamada direta aos endpoints de listagem e de estatísticas (Postman/curl), validando estrutura, tipos e valores do payload de resposta contra os JSONs de retorno esperado (`novo-documentos.json`, `novo-estatistica.json`).
- **Regressão:** campos já existentes no retorno (protocolo, módulo, privacidade, setor) continuam presentes e sem alteração de formato.

Não se aplica (fluxo 3f, sem tela): unitário isolado de serviço (fica a critério do dev), UI/E2E.

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-001\|CT-001]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-002\|CT-002]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-003\|CT-003]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-004\|CT-004]] | Borda | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-005\|CT-005]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-006\|CT-006]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-007\|CT-007]] | Borda | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-008\|CT-008]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-009\|CT-009]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-010\|CT-010]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-011\|CT-011]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-012\|CT-012]] | Borda | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-013\|CT-013]] | Erro | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/03 - Casos de teste#^ct-014\|CT-014]] | Erro | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/00 QA/04 - Validação dev\|Registrar resultado]] |

> [!info]- Renumeração de 05/10/2026
> CT-008/CT-010 antigos (status "Respondido"/totalAnswered) saíram do escopo — ver `03 - Casos de teste#G. Fora de execução`. Os CTs acima já refletem a numeração atual.

---

## Entrada e saída

**Entrada:** ambiente de homologação com massa de dados de solicitações e-SIC variada (solicitantes PF com e sem cadastro completo, PJ, nomes repetidos, solicitações respondidas/em andamento/encerradas/sem prazo).
**Saída:** todos os CTs executados com resultado registrado em `04 - Validação dev`; nenhum critério de aceite (C1–C10) sem cobertura.
