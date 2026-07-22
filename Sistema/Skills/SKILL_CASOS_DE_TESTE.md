---
tags:
  - qa
  - skill
---
# Skill: Criação de Casos de Teste

Criar e organizar casos de teste seguindo o padrão utilizado pelo QA. ([Template](../Templates/Casos de teste.md))

## Objetivos

- Garantir cobertura funcional
- Validar regras de negócio
- Facilitar execução manual
- Padronizar documentação de testes

## Estrutura Padrão

Mesmo formato dos CTs embutidos em cards de bug ([[SKILL_BUGS|SKILL_BUGS]]) — um padrão único de CT em todo o vault, o que muda é só a numeração (CT-001 na nota avulsa, CT-B01 no card de bug):

- **CT-001 Nome do Cenário**
    Dado que...
    Quando...
    Então...

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

Cada caso é um item de lista (`- **CT-001 Título**`) com o Dado/E/Quando/Então **sem bullet própria** — linhas soltas, indentadas como continuação do item. O "Execução Passou?" é uma to-do list com "Sim" em verde e "Não" em vermelho.

---

## Regras

### Numeração

Utilizar:

CT-001
CT-002
CT-003

Mantendo sequência dentro da demanda.

### Título

Descrever claramente o cenário validado.

Exemplos:

- Visualizar permissão de desbloqueio na criação de Servidor
- Salvar permissões de desbloqueio na edição de Servidor
- Exibir status Bloqueado na listagem de usuários

### Escrita

Utilizar padrão:

Dado que...
Quando...
Então...

Evitar:

- Linguagem técnica excessiva
- Explicações longas
- Múltiplos cenários no mesmo caso

### Cobertura

Sempre avaliar:

- Fluxo principal
- Fluxos alternativos
- Regras de negócio
- Permissões
- Persistência de dados
- Exibição de informações
- Cenários negativos quando aplicável

### Completude (contrato com os critérios de aceite)

Antes de dar os CTs por prontos, casar **CT ↔ critério** do card:

- **Cada critério de aceite** tem ao menos **1 CT** que o exercita.
- **Cada CT** amarra em pelo menos um critério (CT que não valida nenhum critério: remover ou justificar).
- Nenhum critério fica descoberto — se faltar, escrever o CT antes de seguir pra validação.

### Evidências de Testes

Mesmo processo de qualquer evidência do vault — ver [[../../QA Workspace/Evidências/README|Evidências/README]]. Vale pra caso de teste tanto quanto pra bug.

## Resultado Esperado

Retornar uma lista organizada de casos de teste pronta para execução.