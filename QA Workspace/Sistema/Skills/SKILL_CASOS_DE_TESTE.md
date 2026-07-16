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

## CT-001 Nome do Cenário

Dado que...

Quando...

Então...

Execução Passou?

- [ ] Sim
- [ ] Não

Evidências de Testes:

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

### Evidências de Testes

Mesmo processo de qualquer evidência do vault (gravar → renomear `<número do card> - <breve descrição>.mp4` → mover pra subpasta do ambiente → embed na nota) — ver [[../Contexto/COMO_EU_TRABALHO.md#Evidências|COMO_EU_TRABALHO.md]]. Vale pra caso de teste tanto quanto pra bug.

## Resultado Esperado

Retornar uma lista organizada de casos de teste pronta para execução.