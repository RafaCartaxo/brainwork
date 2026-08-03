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

- [ ] **Documento** com anexo `.dwg` é criado sem erro na geração — inclusive com os arquivos da evidência, que hoje falham
- [ ] **Despacho** com anexo `.dwg` é emitido sem erro, tanto no ambiente **interno** (servidor) quanto no **externo** (cidadão), como a doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] determina
- [ ] O cidadão consegue **reencaminhar** um `.dwg` depois de ter o anexo reprovado na abertura do processo — é o caso de uso que a regra existe pra garantir
- [ ] **Nenhum** arquivo `.dwg` produz erro na geração do documento: ou o arquivo é aceito, ou é recusado **no upload**, com mensagem ao usuário
- [ ] **Sem regressão**: `.dwg` que já era aceito segue criando documento e despacho, e o anexo criado continua abrindo no revisor de anexos com selo, carimbo e anotação (SGV-8698)

---

### Casos de Teste Básicos

#### **CT-B01 Documento é criado com os anexos DWG que falhavam**

**Dado** que o servidor esteja na tela de criação de um novo documento de Licenciamento Urbano
**E** anexe no campo de anexo DWG um dos arquivos da evidência
**Quando** submeter a criação do documento
**Então** o documento é criado com sucesso, sem mensagem de erro, com o anexo DWG presente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B02 Despacho é emitido com anexo DWG pelo servidor (ambiente interno)**

**Dado** que o servidor esteja criando um despacho em um documento
**E** anexe no campo de anexo DWG um dos arquivos da evidência
**Quando** emitir o despacho
**Então** o despacho é emitido com sucesso, sem mensagem de erro, com o anexo DWG presente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B03 Cidadão reencaminha o DWG após o anexo ser reprovado (ambiente externo)**

**Dado** que o cidadão tenha um anexo reprovado na abertura do processo
**E** precise reencaminhar o arquivo em uma resposta ou despacho
**Quando** anexar o arquivo `.dwg` e enviar
**Então** o anexo é aceito e o envio conclui sem erro — é o caminho que a regra de aceitação do DWG existe pra garantir

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-B04 Selo, carimbo e anotação seguem funcionando no DWG (regressão da SGV-8698)**

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
    - **Cobertura de CT deliberadamente enxuta**: 4 CT-B para 5 critérios, por decisão do Rafael em 03/08/2026 (a regra do vault é um CT por critério — [[Sistema/Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]]). Mapa: CA1→CT-B01, CA2→CT-B02 (interno) e CT-B03 (externo), CA3→CT-B03, CA5→CT-B04. O **CA4** ("nenhum `.dwg` produz erro na geração") não tem CT próprio de propósito: é uma asserção transversal, verificada **em todos** os CTs acima — a cada arquivo testado, a resposta aceitável é criar ou recusar no upload, nunca estourar na geração. A parte do CA5 sobre o arquivo que já funcionava se valida no CT-B01, trocando o insumo. **Não é lacuna esquecida.**
    - **Gate de doc — reclassificado em 2026-08-03: de "lacuna" para DIVERGÊNCIA CONFIRMADA.** Com a importação da doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]], existe regra escrita, na seção "Extensão DWG":

        > "O sistema deve reconhecer e aceitar arquivos no formato `.dwg` na funcionalidade de despacho. […] a lista de tipos de arquivo permitidos passa a incluir o `.dwg`, garantindo que o cidadão consiga anexá-lo com sucesso."

        E vale explicitamente pro **ambiente interno e externo**. Ou seja: um `.dwg` que passa no upload e faz a criação do documento/despacho falhar **contraria regra documentada** — não é lacuna de especificação. Isso fortalece o card: o resultado esperado não é interpretação da QA, e o dev não pode alegar "formato não suportado".

        A doc registra ainda o **caso de uso que motivou a regra**: quando um anexo é reprovado na abertura do processo, o cidadão precisa reencaminhar o arquivo — sem suporte à extensão ele fica impedido. Vale conferir esse caminho na validação, porque é o cenário que a regra existe pra proteger.

        **O que continua sem respaldo**: a doc **não** define *quais* arquivos `.dwg` são válidos — nada sobre tamanho ou versão do formato. Registrado nas Dúvidas em aberto da doc do módulo. Isso **não bloqueia mais nenhum critério**: o CA4 foi reescrito pra afirmar o que é verificável sem essa regra — erro na geração não é resposta aceitável pra nenhum arquivo; ou aceita, ou recusa no upload com mensagem. Saber o limite exato continua útil pra cobrir o caso negativo com precisão, não pra executar o critério.
    - **O Revisor de Anexos segue sem doc.** A doc de Despachos cobre a **aceitação** do DWG como anexo, não a aplicação de selos, carimbos e anotações sobre ele (o que a SGV-8698 entregou) — que é a segunda metade do **CA5**. Nenhum módulo do vault cobre essa funcionalidade; a pendência de importar segue aberta, com esse escopo residual.
    - Dev responsável no Notion: Washington Junior. Status no Notion: "Em desenvolvimento" (sprint SP16 - 2026, previsão de conclusão 11/08/2026). Squad 1 - Rogue One.
    - A task foi criada no Notion em 01/07/2025 (campo "Resumo automático"); o card no vault nasce hoje, com os critérios de aceite.
    - O defeito **não foi impeditivo** para a aprovação da SGV-8698 — decisão registrada na própria task da melhoria, de tratar em paralelo.

- Histórico:
    - 2026-08-03 - 📝 Bug refinado (critérios de aceite prontos)
    - 2026-08-03 - 📚 Gate de doc reclassificado para divergência confirmada, com a importação da doc de [[QA Workspace/04 Conhecimento/Módulos/Despachos|Despachos]] (seção "Extensão DWG")
    - 2026-08-03 - 📝 Critérios reescritos: passaram a afirmar a regra documentada (aceitação do `.dwg` no interno e no externo, e o reenvio pelo cidadão) em vez de contar os arquivos da evidência; entrou o CT-B03 do cidadão e o critério da recusa foi reformulado pra ser verificável sem a regra de validade dos arquivos
