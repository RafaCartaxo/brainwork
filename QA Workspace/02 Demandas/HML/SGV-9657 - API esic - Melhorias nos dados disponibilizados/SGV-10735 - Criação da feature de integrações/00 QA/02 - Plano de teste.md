---
demanda: "[[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda]]"
status: planejado
responsavel: Rafael
pontos: ""
---

# Plano de teste — SGV-10735

> [!info]- Navegação QA
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/00 README|Abrir README do card]]
> **Demanda:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/05 - Preparação Qase]]

> [!settings]- Controle do plano de teste
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

---

## Objetivo

Validar a tela de Integrações no Gerenciador de clientes (ativação, credenciais, seleção de módulos, desativação e histórico), conforme `01 - Demanda` (C1–C14).

---

## Riscos e escopo

- **Risco principal:** estados de credenciais (ativa → desativada → reativada) precisam preservar os mesmos valores — regressão aqui quebra integrações já configuradas de clientes reais.
- **Risco secundário:** confirmações (salvar seleção de módulos, sair com alterações pendentes, desativar) são fáceis de pular no protótipo e fáceis de esquecer na implementação.
- **Fora do escopo desta rodada:** backend de geração de credenciais (já validado na Parte 1); bugs já tratados na SGV-10736 (ranking, paginação).

---

## Estratégia de teste

- **UI/E2E:** fluxo completo pela tela — ativar, copiar credenciais, selecionar/salvar módulos, desativar, reativar, consultar histórico.
- **Regressão:** cliente com integração já ativa antes desta entrega mantém credenciais e módulos após qualquer alteração de estado.

Não se aplica: API/contrato (coberto pela SGV-10736); unitário isolado de serviço (critério do dev).

---

## Matriz de cobertura

| CT | Tipo | Camada | Automação | Validação |
|---|---|---|---|---|
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-001\|CT-001]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-002\|CT-002]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-003\|CT-003]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-004\|CT-004]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-005\|CT-005]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-006\|CT-006]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-007\|CT-007]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-008\|CT-008]] | Borda | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-009\|CT-009]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-010\|CT-010]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-011\|CT-011]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-012\|CT-012]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-013\|CT-013]] | Funcional | UI | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |
| [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste#^ct-014\|CT-014]] | Funcional | API | Manual | [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev\|Registrar resultado]] |

---

## Entrada e saída

**Entrada:** ambiente de teste/dev com ao menos um cliente ativo e um inativo, cada um com módulos contratados variados; acesso ao Gerenciador de clientes com perfil interno.
**Saída:** todos os CTs executados com resultado registrado em `04 - Validação dev`; nenhum critério de aceite (C1–C14) sem cobertura.
