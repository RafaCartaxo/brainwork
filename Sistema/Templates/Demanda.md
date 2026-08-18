---
tags:
  - demanda
  - qa
task: ""
status: dev
ambiente: DEV
prioridade: media
mel: ""
data_inicio: <% tp.date.now("YYYY-MM-DD") %>
data_fim:
responsavel:
modulo:
---
# Demanda: {{Título}}

> [!info] Informações
> - **Tipo:** [Bug / Melhoria / Funcionalidade / POC]
> - **Status:** [DEV / HML / Concluída]
> - **Responsável QA:**
> - **Link:**

---

> [!abstract] Resumo

Breve descrição da demanda.

---

## Regras de negócio

---

> [!warning] Pontos de atenção

---

## Casos de teste

- Criar casos de teste no padrão de cabeçalho — `#### **CT-NNN Título** *(CAn)*`, palavras-chave em negrito, `- [ ] Sim` / `- [ ] Não` / `- [ ] Não se aplica`, `---` entre casos. Formato completo em [[Sistema/Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]] · exemplo em [[Sistema/Templates/Casos de teste|Casos de teste]]
- Com muitos casos, agrupar por tema (`### A. <grupo>`) e manter **um CT por critério**
- Caso retirado ou adiado depois de escrito vai pro grupo de registro abaixo — **não** apagar nem deixar buraco na numeração

### G. Fora de execução — registro

*Só criar esta seção quando houver caso retirado/adiado. Caso × decisão × motivo.*

| Caso | Decisão | Motivo |
|---|---|---|
|  |  |  |

---

> [!danger] Bugs encontrados

---

## Evidências

---

> [!tip] Observações

---

## Histórico

- DD/MM/AAAA - Início da validação
- DD/MM/AAAA - Finalizada validação DEV
- DD/MM/AAAA - Revalidação HML