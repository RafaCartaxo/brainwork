---
tags:
  - bug
  - qa
task: "SGV-6975"
prioridade: media
status: resolvido
data_inicio: 2026-07-21
data_fim: 2026-07-21
responsavel: Rafael
cadastrado_por: ""
modulo: Cadastro de clientes
ambiente: HML
---
# Erro 503 ao ativar clientes com status "Em implantação"

### Descrição

Durante validação foi identificado que a ativação de um cliente com status "Em implantação" retornava erro 503, impedindo a conclusão da ativação.

---

### Passo a passo para reproduzir

Dado que existe um cliente com status "Em implantação"
Quando o cliente é ativado
Então o sistema retorna erro 503 e a ativação não é concluída

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://6975)

![[6975 - erro 503 ao ativar cliente em implantacao aprovado em homologacao.mp4]]

---

### Resultado Esperado

- A ativação de um cliente com status "Em implantação" é concluída com sucesso, sem erro 503.

---

### Critérios de aceite

- [x] Cliente com status "Em implantação" é ativado sem retornar erro 503

---

### Casos de Teste Básicos

- **CT-B01 Ativar cliente com status "Em implantação"**
    Dado que existe um cliente com status "Em implantação"
    Quando o cliente é ativado
    Então a ativação é concluída com sucesso, sem erro 503

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes: ![[6975 - erro 503 ao ativar cliente em implantacao aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-6975
- Observações: Card criado retroativamente no momento do registro da validação (aprovada em homologação). Origem: triagem [[QA Workspace/05 Refinar/Triagem - SP15|Triagem SP15]] (Sanidade-006, prioridade Média, dev Matheus Godoi). Material de reprodução detalhado não foi fornecido — descrição/passo a passo destilados do título; quem reabrir no futuro deve reconstituir o passo a passo pela task no Notion.
- Histórico:
    - 2026-07-21 - ✅ Aprovada em homologação
