---
tags:
  - bug
  - qa
  - sigilo
  - despacho
task: "9499"
prioridade: alta
status: resolvido
data_inicio: 2026-07-02
data_fim: 2026-07-14
responsavel: Rafael
modulo: despacho
ambiente: HML
---
# Opção Com Sigilo em respostas de Processo Administrativo oculta o conteúdo do despacho para o próprio autor (servidor)

### Descrição

Durante validação foi identificado que, ao marcar a opção "Com Sigilo" em um despacho de resposta de Processo Administrativo, o próprio servidor autor do despacho não conseguia visualizar o conteúdo do que havia criado. Corrigido e reaprovado em homologação em 14/07: o servidor autor consegue visualizar normalmente o próprio despacho sigiloso, e usuários sem envolvimento direto no despacho continuam sem acesso ao conteúdo (regra de sigilo preservada).

---

### Passo a passo para reproduzir

Dado que um servidor crie um despacho de resposta em um Processo Administrativo
E marque a opção "Com Sigilo"
Quando o próprio servidor autor visualizar ou baixar o despacho emitido
Então o conteúdo do despacho deve ser exibido normalmente para ele

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9499)

![[9499 - sigilo despacho servidor autor aprovado.mp4]]

---

### Resultado Esperado

O servidor autor de um despacho sigiloso deve conseguir visualizar o próprio conteúdo normalmente (na visualização e no download), tanto quanto servidores diretamente envolvidos no despacho. Servidores sem envolvimento direto e não autores devem continuar sem acesso ao conteúdo sigiloso — regra de sigilo não pode ser afetada por side-effect.

---

### Critérios de aceite

- O servidor autor de um despacho sigiloso deve visualizar o próprio conteúdo normalmente (tela e download/PDF)
- Servidores diretamente envolvidos no despacho devem continuar visualizando o conteúdo normalmente
- Servidores/setores sem envolvimento direto e que não são autores não devem visualizar o conteúdo sigiloso, mesmo sendo donos/responsáveis pelo processo administrativo em questão

---

### Casos de Teste Básicos

- **CT-B01 Visualizar conteúdo do próprio despacho sigiloso como autor (servidor)**
    - Dado que um servidor crie um despacho de resposta com a opção "Com Sigilo" marcada
    - Quando ele mesmo visualizar o despacho na linha do tempo do documento
    - Então o conteúdo do despacho deve ser exibido normalmente para ele

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B02 Baixar PDF do próprio despacho sigiloso como autor (servidor)**
    - Dado que um servidor tenha criado um despacho de resposta com a opção "Com Sigilo" marcada
    - Quando ele mesmo solicitar o download/PDF do despacho
    - Então o conteúdo do despacho deve constar normalmente no arquivo gerado

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

- **CT-B03 Ocultar conteúdo do despacho sigiloso para servidor sem envolvimento direto**
    - Dado que exista um despacho sigiloso criado por outro servidor no processo
    - E o servidor atual não esteja diretamente envolvido nesse despacho (mesmo sendo responsável/dono do processo, ex.: cenário "Ursula")
    - Quando ele acessar a linha do tempo do documento
    - Então o conteúdo do despacho sigiloso não deve ser exibido para ele

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

---

### Ambiente

- Versão:

- Ambiente: Homologação

- Navegador:

- Sistema Operacional:

---

### Informações adicionais

- Demanda relacionada: SGV-9499
- Observações: Validado apenas o cenário do lado do **servidor** (autor do despacho). Chegou a se suspeitar de um cenário equivalente do lado do **cidadão** — ver [[QA Workspace/99 Arquivo/Bug Sigilo Despacho Cidadão Autor|Bug Sigilo Despacho Cidadão Autor]] (descartado em 14/07: cidadão não cria despacho sigiloso na própria resposta, e quando o servidor responde com sigilo o cidadão já é incluído automaticamente em `involvedInDispatch`).
- Histórico:
    - 2026-07-02 a 2026-07-10 - 🔴 Diversas rodadas de correção; reaberto em 10/07 por regressão em regra de sigilo (side-effect)
    - 2026-07-14 - 🔁 Retestada e aprovada em homologação (cenário servidor)
