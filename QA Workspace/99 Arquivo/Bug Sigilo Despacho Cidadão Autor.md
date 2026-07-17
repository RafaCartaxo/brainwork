---
tags:
  - bug
  - qa
  - sigilo
  - despacho
  - cidadao
task: ""
prioridade: alta
status: descartado
data: 2026-07-14
responsavel: Rafael
modulo: despacho
ambiente: DEV
---
# Cidadão autor de despacho sigiloso em resposta de Processo Administrativo pode não visualizar o próprio conteúdo (descartado — não ocorre)

### Descrição

Durante análise do código relacionado à correção do SGV-9499 foi identificado que, no fluxo de criação de despacho pelo **cidadão** (`createCitizenDispatch`), o próprio cidadão é explicitamente excluído da lista de envolvidos (`involvedInDispatch`) ao criar o despacho. A checagem de visibilidade de conteúdo sigiloso para despachos criados por cidadão depende de `isCurrentUserCanViewSensitiveData` (permissão exclusiva de servidor) ou de estar em `involvedInDispatch` — nenhuma das duas se aplica ao próprio cidadão autor. Isso sugere que um cidadão que cria uma resposta sigilosa no próprio Processo Administrativo não visualizaria o conteúdo do próprio despacho, reproduzindo o mesmo bug do SGV-9499, mas do lado do cidadão. **Ainda não reproduzido na UI — precisa confirmação.**

---

### Passo a passo para reproduzir

Dado que um cidadão acesse o próprio Processo Administrativo
E crie um despacho de resposta marcando a opção "Com Sigilo"
Quando ele mesmo visualizar o despacho que acabou de criar
Então (suspeita) o conteúdo do despacho não é exibido para ele mesmo sendo o autor

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9499)


---

### Resultado Esperado

O cidadão autor de um despacho sigiloso na própria resposta de Processo Administrativo deve conseguir visualizar o próprio conteúdo normalmente, da mesma forma que foi corrigido para o servidor no SGV-9499.

---

### Critérios de aceite

- [ ] O cidadão autor de um despacho sigiloso deve visualizar o próprio conteúdo normalmente
- [ ] Demais cidadãos/servidores sem envolvimento direto e que não são autores continuam sem acesso ao conteúdo sigiloso (regra de sigilo não deve regredir)

---

### Casos de Teste Básicos

- **CT-B01 Visualizar conteúdo do próprio despacho sigiloso como autor (cidadão)**
    Dado que um cidadão crie um despacho de resposta com a opção "Com Sigilo" marcada, no próprio Processo Administrativo
    Quando ele mesmo visualizar o despacho na linha do tempo do documento
    Então o conteúdo do despacho deve ser exibido normalmente para ele

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>
    - Evidências de Testes:

---

### Ambiente

- Versão:

- Ambiente: Desenvolvimento

- Navegador:

- Sistema Operacional:

---

### Informações adicionais

- Demanda relacionada: SGV-9499 (regressão relacionada, lado cidadão)
- Observações: Achado via análise de código (`api/src/services/documentEvents/documentEvents.ts` e `api/src/services/dispatches/dispatches.ts`, função `createCitizenDispatch`). **Descartado após investigação (14/07)**: o cenário não se aplica — o cidadão não cria despacho sigiloso na própria resposta (só o servidor cria); quando o servidor responde com sigilo, o cidadão já é automaticamente incluído em `involvedInDispatch`, então ele visualiza o conteúdo normalmente. Não há regressão equivalente ao SGV-9499 do lado do cidadão.
- Histórico:
    - 2026-07-14 - 🗑️ Descartado (não reproduz: cidadão não cria despacho sigiloso; auto-envolvimento cobre o cenário)
