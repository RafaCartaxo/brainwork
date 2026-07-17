---
tags:
  - bug
  - qa
  - formulario
  - repeticao-campo
task: "8805"
prioridade: media
status: resolvido
data_inicio: 2026-07-14
data_fim: 2026-07-14
responsavel: Rafael
modulo: formularios
ambiente: HML
---
# Descrição técnica exibida para campos repetidos em eventos de retificação

### Descrição

Durante validação foi identificado que os eventos de retificação de campos com repetição habilitada (opção "permitir repetição de campo" na construção do formulário — vale para qualquer tipo de campo: texto, numérico, data e hora, e-mail, link, etc.) exibiam uma descrição técnica ao invés do nome amigável do campo, por exemplo: `link-2_C-repetition-1`, `link-2_C-repetition-2`, `email-2_C-repetition-1`. Corrigido e aprovado em homologação — agora exibe corretamente o nome do campo e o número da repetição, ex.: "retificou o campo E-mail: (repetição 3) de '(vazio)' para 'camporepetido4-Retificado@gmail.com'".

---

### Passo a passo para reproduzir

Dado que um formulário tenha um campo configurado com "permitir repetição de campo"
E uma das repetições desse campo seja retificada
Quando o evento de retificação for exibido
Então o campo deve ser identificado pelo nome amigável e número da repetição, não por um identificador técnico

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://8805)

![[8805 - descrição técnica em campos repetidos corrigida.mp4]]

---

### Resultado Esperado

O evento de retificação deve exibir o nome amigável do campo e o número da repetição (ex.: "campo E-mail: (repetição 3)"), nunca o identificador técnico interno (ex.: `email-2_C-repetition-1`).

---

### Critérios de aceite

- [x] Eventos de retificação de campos repetidos devem exibir o nome amigável do campo, não o identificador técnico
- [x] Deve indicar corretamente o número da repetição (ex.: "repetição 3")
- [x] Deve valer para qualquer tipo de campo repetido (texto, numérico, data e hora, e-mail, link, etc.)

---

### Casos de Teste Básicos

- **CT-B01 Exibir nome amigável e número da repetição no evento de retificação**
    Dado que um campo com repetição habilitada seja retificado
    Quando o evento de retificação for exibido
    Então deve mostrar o nome amigável do campo e o número da repetição, sem identificador técnico

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-8805
- Observações: Confirmado também em retificação de outro usuário (Ursula C Borges, QA) no campo Descrição — "retificou o campo Descrição: (repetição 3)" exibido corretamente, não só no cenário testado originalmente.
- Histórico:
    - 2026-07-14 - ✅ Aprovada em homologação
