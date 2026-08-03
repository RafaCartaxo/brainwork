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
modulo: documento
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

Isso está **respaldado por regra escrita**: a doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]], na seção "Extensão DWG", determina que `.dwg` seja aceito como anexo em despacho, no ambiente interno e no externo.

---

### Critérios de aceite

- [ ] Criar documento anexando cada um dos 3 arquivos DWG da evidência conclui com sucesso, sem erro na geração
- [ ] Criar despacho com os mesmos 3 arquivos DWG conclui com sucesso
- [ ] Anexo DWG que já era aceito antes continua criando documento e despacho normalmente (sem regressão)
- [ ] O DWG anexado continua abrindo no revisor de anexos e aceitando selo, carimbo e anotação (sem regressão da SGV-8698)
- [ ] Arquivo DWG que não respeita as regras de negócio é recusado com mensagem clara ao usuário, em vez de erro na geração do documento *(depende da regra de aceitação do campo, que não existe escrita — ver o gate de doc em Observações; sem ela a QA não sabe montar o arquivo inválido)*

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
- [ ] Não se aplica

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
- [ ] Não se aplica

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
- [ ] Não se aplica

**Evidências de Testes:**

---

### Ambiente

- Versão: 12.36.38.2
- Ambiente: Desenvolvimento (posição na esteira de correção — o fix está com o dev)

> [!info]- Origem: homologação, versão 12.36.38.2
> O defeito foi observado em **homologação**, na rodada da SGV-8698, conforme registro do Waldemar em 30/07/2026 — confirmado pelo Rafael em 03/08/2026.
>
> O card mora em `DEV/` com `ambiente: DEV` porque o campo reflete a **posição na esteira**, não o último ambiente testado: bug de homologação em sustentação nasce na posição de correção e sobe de novo pela esteira ([[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|módulo]] ainda sem regra de anexos — ver o gate de doc em Observações; regra da esteira em [[Sistema/Contexto/PADROES_QA|PADROES_QA]] → Organização de Bugs).

---

### Informações adicionais

- Referência no Notion: [SGV-10482 no Notion](https://app.notion.com/p/alfa-group/BUG-Erro-na-cria-o-de-documento-despacho-com-anexo-dwg-espec-fico-3ad2aec67d3080cbb48cec6688878887) — é lá que moram a evidência (`Evidência Bug 1.mp4`) e os arquivos `.dwg` que reproduzem o defeito.

- Demanda relacionada: SGV-8698 — *[MELHORIA-CX] Permitir aplicação de selos, carimbos e anotações em arquivos DWG* ([task no Notion](https://app.notion.com/p/alfa-group/MELHORIA-CX-Permitir-aplica-o-de-selos-carimbos-e-anota-es-em-arquivos-DWG-3642aec67d308185ba03e55016e5ff0c)). A task 10482 é marcada como **Impactando** essa melhoria; a melhoria está "Aprovado por QA", aprovada em homologação na versão 12.36.38.2, e não tem card no vault. O defeito foi encontrado na execução do plano de testes dela: [Execução Plano de testes: SGV-8698 01](https://app.notion.com/p/Execu-o-Plano-de-testes-SGV-8698-01-3ab2aec67d30803d8d54c2efec2b4a6e) (Waldemar, 30/07).

- Observações:
    - **Cobertura de CT deliberadamente enxuta**: 3 CT-B para 5 critérios, por decisão do Rafael em 03/08/2026. A regra do vault é um CT por critério ([[Sistema/Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]]), então fica registrado o que ficou de fora: o **3º critério** (DWG que já funcionava — regressão) e o **5º** (arquivo fora das regras recusado com mensagem) não têm CT próprio. O 3º se valida junto do CT-B01, usando um arquivo que já passava; o 5º está bloqueado pela lacuna de doc abaixo. **Não é lacuna esquecida.**
    - **Gate de doc — reclassificado em 2026-08-03: de "lacuna" para DIVERGÊNCIA CONFIRMADA.** Com a importação da doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]], existe regra escrita, na seção "Extensão DWG":

        > "O sistema deve reconhecer e aceitar arquivos no formato `.dwg` na funcionalidade de despacho. […] a lista de tipos de arquivo permitidos passa a incluir o `.dwg`, garantindo que o cidadão consiga anexá-lo com sucesso."

        E vale explicitamente pro **ambiente interno e externo**. Ou seja: um `.dwg` que passa no upload e faz a criação do documento/despacho falhar **contraria regra documentada** — não é lacuna de especificação. Isso fortalece o card: o resultado esperado não é interpretação da QA, e o dev não pode alegar "formato não suportado".

        A doc registra ainda o **caso de uso que motivou a regra**: quando um anexo é reprovado na abertura do processo, o cidadão precisa reencaminhar o arquivo — sem suporte à extensão ele fica impedido. Vale conferir esse caminho na validação, porque é o cenário que a regra existe pra proteger.

        **O que continua sem respaldo** (e por isso o 5º critério segue bloqueado): a doc **não** define *quais* arquivos `.dwg` são válidos — nada sobre tamanho ou versão do formato. Sem isso, não há como montar um arquivo "fora das regras" pra testar a recusa com mensagem. Registrado nas Dúvidas em aberto da doc do módulo.
    - **O Revisor de Anexos segue sem doc.** A doc de Despachos cobre a **aceitação** do DWG como anexo, não a aplicação de selos, carimbos e anotações sobre ele (o que a SGV-8698 entregou) — que é o 4º critério. Nenhum módulo do vault cobre essa funcionalidade; a pendência de importar segue aberta, agora com esse escopo residual.
    - Dev responsável no Notion: Washington Junior. Status no Notion: "Em desenvolvimento" (sprint SP16 - 2026, previsão de conclusão 11/08/2026). Squad 1 - Rogue One.
    - A task foi criada no Notion em 01/07/2025 (campo "Resumo automático"); o card no vault nasce hoje, com os critérios de aceite.
    - O defeito **não foi impeditivo** para a aprovação da SGV-8698 — decisão registrada na própria task da melhoria, de tratar em paralelo.

- Histórico:
    - 2026-08-03 - 📝 Bug refinado (critérios de aceite prontos)
    - 2026-08-03 - 📚 Gate de doc reclassificado para divergência confirmada, com a importação da doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] (seção "Extensão DWG")
