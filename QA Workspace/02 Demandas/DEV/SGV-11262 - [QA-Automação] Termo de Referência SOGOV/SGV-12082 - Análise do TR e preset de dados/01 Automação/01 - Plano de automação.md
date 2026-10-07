---
demanda: "[[../00 QA/01 - Demanda]]"
casos_origem: "[[../00 QA/03 - Casos de teste]]"
repo: "sogov-automation-playwright"
status: planejado
---

# Plano de automação — SGV-12082

> [!info]- Navegação QA
> **README:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Casos de análise:** [[../00 QA/03 - Casos de teste]]
> **Matriz:** [[../00 QA/Matriz - Análise do preset provável]]
> **Automação:** [[00 - Automação]]
> **Validação:** [[02 - Validação automação]]

> [!settings]- Controle do plano
> **Status:** `INPUT[inlineSelect(option(planejado),option(execucao),option(concluido)):status]`

> Plano de investigação técnica que segue a estrutura do template. A implementação só será planejada em entrega posterior, depois da decisão baseada em evidências.

## Objetivo e escopo

- **Objetivo:** entender como o projeto prepara e consome massa, avaliar reaproveitamento entre ambientes e recomendar o preset provável que atende aos requisitos do TR validáveis por automação/dados, relacionando evidências para os demais.
- **CTs incluídos:** verificações DISC-001–DISC-004; elas analisam o PDF completo e a automação existente. CT-001–CT-038 são casos existentes apenas dos requisitos 1.24–1.25, sem criar novos CTs funcionais.
- **Fora do escopo:** editar/executar o seed, alterar dados/instâncias e portar os CTs restantes.

## Estratégia por suíte

| Suíte / CTs | Camada | Dados e estado inicial | Reuso / mudança necessária | Dependência ou gate |
|---|---|---|---|---|
| DISC-001 — arquitetura | Repositório/documentação | Configuração Playwright, setup, provisionamento, manifesto e fixtures | Descrever capacidades existentes; não alterar código | Acesso de leitura ao repositório e definição do commit analisado |
| DISC-002 — cobertura do TR e dos 38 CTs existentes | Requisitos + casos/testes | Requisitos do PDF; atores, entidades, estados e operações dos CTs 1.24–1.25 | Classificar cobertura/evidência do TR e cruzar os casos existentes com código; agrupar só com justificativa | PDF integral e fonte dos 38 CTs; validar estado atual de cada suíte |
| DISC-003 — dados/ambientes | Configuração + dados | Endpoints, credenciais (nomes, sem valores), disponibilidade e isolamento | Distinguir parametrização existente de portabilidade comprovada | Configuração segura/documentação ou evidência registrada por ambiente |
| DISC-004 — recomendação | Síntese da matriz | Conjunto mínimo de dados/estados e restrições | Comparar opções sem presumir refatoração do seed | DISC-001–003 revisados |

## Pronto para codar quando

- [ ] Os requisitos do TR estão classificados; os testes/dados existentes e as lacunas de cobertura estão rastreados, incluindo análise detalhada dos 38 CTs de 1.24–1.25.
- [ ] Os ambientes relevantes e as lacunas de evidência estão identificados.
- [ ] O preset provável tem escopo mínimo, dependências, isolamento e forma de validação descritos.
- [ ] Refatorar seed, parametrizar configuração ou manter mecanismo atual foram comparados com evidências.

## Pronto para validar quando

- [ ] Mapa, matriz, recomendação e sequência de entregas candidatas estão revisados.
- [ ] Cada recomendação aponta para CTs e fontes verificáveis.
- [ ] Nenhum resultado documental é apresentado como execução em ambiente.

---

**Execução direta:** nesta entrega, “pronto para validar” significa revisão da análise e rastreabilidade; não significa código ou execução funcional.
