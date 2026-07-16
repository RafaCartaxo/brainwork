---
tags:
  - bug
  - qa
task: "8917"
prioridade: alta
status: resolvido
data_inicio: 2026-07-03
data_fim: 2026-07-15
responsavel: Rafael
modulo: geracao-documentos
mr: "#479"
versao: "12.15.22.2.1"
ambiente: HML
---
# Não é possível gerar documento quando o setor criador não tem permissão de criação para o módulo selecionado

### Descrição

Durante validação foi identificado que a geração de documentos automatizados falha quando o servidor atua por um setor sem permissão de criação (canCreate) para o módulo/assunto/serviço do documento. O card passou por 2 rodadas de MR: a MR #479 corrigiu a checagem de permissão e tornou a visibilidade do botão reativa à troca de setor; uma segunda rodada corrigiu um side effect onde documentos sem assunto/serviço deixaram de exibir o botão.

---

### Passo a passo para reproduzir

Dado que o servidor esteja atuando por um setor sem permissão de criação (canCreate) no módulo do documento
E o documento automatizado esteja vinculado ao Módulo, ou ao Assunto e Serviço
Quando ele tentar gerar o documento
Então o botão "Gerar documento" não deve ser exibido

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://8917)

![[8917 - permissão geração documento validada em DEV.mp4]]

![[8917 - permissão geração documento aprovada em homologação.mp4]]

---

### Resultado Esperado

O botão "Gerar documento" não deve ser exibido quando o setor em que o servidor está atuando não possuir permissão de criação (canCreate) para o módulo, assunto ou serviço vinculado ao documento automatizado, mesmo após troca de setor sem reload da página.

---

### Critérios de aceite

- O botão "Gerar documento" não deve aparecer para documentos vinculados diretamente ao Módulo quando o setor não tem permissão
- O botão "Gerar documento" não deve aparecer para documentos vinculados a Assunto e Serviço quando o setor não tem permissão
- A visibilidade do botão deve reagir à troca de setor sem necessidade de reload
- Documentos sem assunto/serviço vinculado devem continuar exibindo o botão normalmente quando o setor tem permissão

---

### Casos de Teste Básicos

- **CT-B01 Bloquear geração de documento vinculado ao Módulo quando setor não tem permissão**
    - Dado que o servidor esteja atuando por um setor sem permissão de criação (canCreate) no módulo do documento
    - E o documento automatizado esteja vinculado diretamente ao Módulo
    - Quando ele tentar gerar o documento
    - Então o botão "Gerar documento" não deve ser exibido

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B02 Bloquear geração de documento vinculado ao Assunto e Serviço quando setor não tem permissão**
    - Dado que o servidor esteja atuando por um setor sem permissão de criação (canCreate) no módulo do documento
    - E o documento automatizado esteja vinculado ao Assunto e Serviço
    - Quando ele tentar gerar o documento
    - Então o botão "Gerar documento" não deve ser exibido

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

---

### Ambiente

- Versão: 12.15.22.2.1
    
- Ambiente: Homologação
    
- Navegador:
    
- Sistema Operacional:
    

---

### Informações adicionais

- Demanda relacionada: SGV-8917 (MR #479)
- Observações: Priorizar cenários 4.x e 5.x (pontos que geraram reaberturas anteriores). Validar em DEV primeiro, depois repetir cenários críticos em HML.
- Histórico:
    - 2026-07-03 - 🚀 Início de validação
    - 2026-07-03 - ✅ Aprovada em DEV (MR #479, 2 rodadas) — segue pra homologação
    - 2026-07-15 - ✅ Aprovada em homologação (cenário proposto validado; evidência gravada)
