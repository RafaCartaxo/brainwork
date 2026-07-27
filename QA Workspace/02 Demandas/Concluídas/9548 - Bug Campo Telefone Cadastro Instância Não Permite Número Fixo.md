---
tags:
  - bug
  - qa
  - cadastro
task: "9548"
prioridade: baixa
status: resolvido
data_inicio: 2026-07-27
data_fim: 2026-07-27
responsavel: Rafael
cadastrado_por: ""
modulo: cadastro-instancia
ambiente: HML
---
# Campo de telefone no cadastro de instância não permite número fixo

### Descrição

No cadastro de instância, o campo de telefone não aceitava número fixo (sem o 9º dígito de celular). (Origem Notion SGV-9548, Matheus Godoi.)

---

### Resultado Esperado

Ao cadastrar uma instância, o campo de telefone aceita número fixo normalmente, sem exigir o formato de celular.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9548)

![[9548 - campo telefone cadastro instancia aceita numero fixo aprovado em homologacao.mp4]]

---

### Critérios de aceite

- [x] Campo de telefone no cadastro de instância aceita número fixo

---

### Casos de Teste Básicos

- **CT-B01 Cadastro de instância aceita telefone fixo**
    Dado a tela de cadastro de instância
    Quando o usuário informa um número de telefone fixo no campo de telefone
    Então o cadastro é aceito sem erro de validação

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9548 - campo telefone cadastro instancia aceita numero fixo aprovado em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: HML

---

### Informações adicionais

- Demanda relacionada: SGV-9548 (origem Notion; Triagem SP15, grupo "Pronto pra homologação"; Matheus Godoi).
- Sem export completo — card criado direto a partir do ticket + validação em homologação.
- Histórico:
    - 2026-07-27 - ✅ Aprovada em homologação
