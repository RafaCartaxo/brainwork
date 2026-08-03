---
tags:
  - bug
  - qa
  - anexo
  - despacho
task: "10482"
prioridade: media
status: aberto
data_inicio: 2026-08-03
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: anexo
ambiente: DEV
---
# Criação de documento e despacho falha ao anexar arquivos DWG específicos

### Descrição

Durante validação foi identificado que a criação de documento (e de despacho) **falha na geração** quando o arquivo anexado no campo de anexo DWG é um de três arquivos específicos. O anexo respeita as regras de negócio do campo — é aceito no upload — mas a submissão do documento retorna erro em vez de concluir a criação. Outros arquivos DWG passam normalmente pelo mesmo fluxo, então o defeito depende do arquivo, não do formato.

---

### Passo a passo para reproduzir

Dado que o usuário acesse a tela de criação de um novo documento (preferencialmente Licenciamento Urbano) ou de um despacho
E anexe no campo de anexo DWG um dos três arquivos da evidência (ex.: `visualization_conference_room.dwg`)
Quando submeter a criação do documento
Então ocorre um erro na geração do documento, e o documento não é criado

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://10482)

Evidência **externa, na task do Notion** (sem cópia local): `Evidência Bug 1.mp4` e os arquivos que reproduzem o defeito, `visualization_conference_room.dwg` e `visualization_-_condominium_with_skylight.dwg`. A descrição da task cita **3** anexos distintos com o problema; o terceiro não está nomeado no export.

---

### Resultado Esperado

O documento e o despacho são criados com sucesso com o anexo DWG. O arquivo respeita todas as regras de negócio do campo, então a submissão conclui normalmente — e um arquivo que não as respeite é recusado com mensagem ao usuário, não com erro na geração do documento.

---

### Critérios de aceite

- [ ] Criar documento anexando cada um dos 3 arquivos DWG da evidência conclui com sucesso, sem erro na geração
- [ ] Criar despacho com os mesmos 3 arquivos DWG conclui com sucesso
- [ ] Anexo DWG que já era aceito antes continua criando documento e despacho normalmente (sem regressão)
- [ ] O DWG anexado continua abrindo no revisor de anexos e aceitando selo, carimbo e anotação (sem regressão da SGV-8698)
- [ ] Arquivo DWG que não respeita as regras de negócio é recusado com mensagem clara ao usuário, em vez de erro na geração do documento

---

### Casos de Teste Básicos

#### **CT-B01 Documento é criado com os anexos DWG que falhavam**

**Dado** que o usuário esteja na tela de criação de um novo documento de Licenciamento Urbano
**E** anexe no campo de anexo DWG um dos três arquivos da evidência
**Quando** submeter a criação do documento
**Então** o documento é criado com sucesso, sem mensagem de erro, com o anexo DWG presente

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B02 Despacho é criado com os mesmos anexos DWG**

**Dado** que o usuário esteja criando um despacho em um documento
**E** anexe no campo de anexo DWG um dos três arquivos da evidência
**Quando** emitir o despacho
**Então** o despacho é criado com sucesso, sem mensagem de erro, com o anexo DWG presente

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

#### **CT-B03 Selo, carimbo e anotação seguem funcionando no DWG (regressão da SGV-8698)**

**Dado** que exista um documento criado com um dos anexos DWG da evidência
**E** o usuário abra esse anexo no revisor de anexos
**Quando** aplicar um selo, um carimbo e uma anotação sobre o arquivo
**Então** as três marcações são aplicadas e persistem no arquivo, como já ocorria antes da correção

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão: 12.36.38.2 (versão em que o defeito foi registrado)
- Ambiente: Homologação — detectado na rodada de homologação da SGV-8698, conforme registro do Waldemar em 30/07/2026. **A confirmar com o Rafael**: a task não declara o ambiente no próprio campo, e o card ainda não foi reproduzido por nós.

---

### Informações adicionais

- Demanda relacionada: SGV-8698 — *[MELHORIA-CX] Permitir aplicação de selos, carimbos e anotações em arquivos DWG* (a task 10482 é marcada como **Impactando** essa melhoria; a melhoria está "Aprovado por QA", aprovada em homologação na versão 12.36.38.2, e não tem card no vault)

- Observações:
    - **Gate de doc: lacuna.** Nenhum módulo em `04 Conhecimento/Módulos/` cobre anexos DWG nem o **Revisor de Anexos** — o vault não tem uma única menção a DWG. O resultado esperado acima está ancorado só na task do Notion e no comportamento observado, **sem respaldo de doc**, e em especial não há regra escrita dizendo **quais** arquivos o campo deve aceitar (tamanho, versão do formato). Entrou pendência de importar a doc do módulo (fluxo 8).
    - Dev responsável no Notion: Washington Junior. Status no Notion: "Em desenvolvimento" (sprint SP16 - 2026, previsão de conclusão 11/08/2026). Squad 1 - Rogue One.
    - A task foi criada no Notion em 01/07/2025 (campo "Resumo automático"); o card no vault nasce hoje, com os critérios de aceite.
    - O defeito **não foi impeditivo** para a aprovação da SGV-8698 — decisão registrada na própria task da melhoria, de tratar em paralelo.

- Histórico:
    - 2026-08-03 - 📝 Bug refinado (critérios de aceite prontos)
