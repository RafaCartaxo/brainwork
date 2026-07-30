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

```markdown
### **CT-001 Nome do Cenário**

**Dado** ...
**Quando** ...
**Então** ...

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---
```

**Cada CT é um cabeçalho, não um item de lista.** Isso é o que faz ele aparecer no outline da nota, dobrar/desdobrar sozinho e ser linkável por `[[nota#CT-001 ...]]`.

| Elemento | Regra |
|---|---|
| Cabeçalho | `### **CT-NNN Título**` em **nota avulsa**; `#### **CT-BNN Título**` dentro de card, pra ficar **aninhado** sob `### Casos de Teste Básicos` em vez de virar irmão de Descrição/Evidências |
| Palavra-chave | `**Dado**` / `**E**` / `**Quando**` / `**Então**` em **negrito**, uma por linha, sem bullet e sem indentação |
| Execução | `**Execução Passou?**` em negrito, seguido de `- [ ] Sim` / `- [ ] Não` — **texto puro, sem `<span>` colorido** |
| Evidências | `**Evidências de Testes:**` em negrito; o embed vem depois, em linha própria |
| Separador | `---` entre CTs |

> [!note]- Por que mudou (30/07/2026)
> O formato anterior era um item de lista com tudo indentado como continuação (`- **CT-001 ...**` + linhas indentadas + `<span>` verde/vermelho). Funcionava, mas: não entrava no outline, dificultava dobrar CT por CT numa nota com 12 casos, e o HTML inline atrapalhava a leitura no modo edição. Rafael passou o formato desejado em 30/07 e o padrão foi trocado. Amostra viva: [[QA Workspace/02 Demandas/Concluídas/10437 - Bug Nao Entra No Documento Criado E Redireciona Pra Mesa De Trabalho|SGV-10437]].

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
- **Critério com estado que liga/desliga o defeito rende um CT por estado**, e cada um recebe **sua própria evidência** — regra completa em [[SKILL_BUGS#Critérios de Aceite|SKILL_BUGS]]. Precedente: SGV-10457, com um CT sem páginas enumeradas e outro com, cada um embedando a gravação do seu cenário.
- **CT não verifica medida de handoff** (px, hex, token de espaçamento): o `Então` diz "íntegro e legível, sem sobreposição", não "a 8px da margem". Medida de especificação é referência pro dev, não passo de teste de caixa preta.

### Evidências de Testes

Mesmo processo de qualquer evidência do vault — ver [[../../QA Workspace/Evidências/README|Evidências/README]]. Vale pra caso de teste tanto quanto pra bug.

## Resultado Esperado

Retornar uma lista organizada de casos de teste pronta para execução.