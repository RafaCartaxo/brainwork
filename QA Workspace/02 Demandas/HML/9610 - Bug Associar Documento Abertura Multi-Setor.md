---
tags:
  - bug
  - qa
  - associar-desassociar
task: "9610"
prioridade: media
status: aberto
data_inicio: 2026-07-17
data_fim: ""
responsavel: Rafael
cadastrado_por: "CX (Edivaldo Lima)"
modulo: associar-desassociar
ambiente: HML
---
# Servidor não consegue associar documento na abertura de um novo documento

### Descrição

Servidor cadastrado em mais de um setor não encontra, na busca de "Associar documentos" da **abertura de um novo documento**, documento ao qual tem acesso por um setor em que **não está atuando** no momento. O contraste que delimita o problema: a mesma busca, feita **via despacho**, encontra o documento normalmente (validado na análise de Bruna Machado, 25/06/2026). Causa apontada no MR !537: a busca da abertura era feita **sem informar o setor ativo** do usuário.

---

### Passo a passo para reproduzir

Dado que um servidor esteja cadastrado em mais de um setor (setor A e setor B)
E esteja atuando pelo setor A
Quando iniciar a abertura de um novo documento e buscar, em "Associar documentos", um documento acessível pelo setor B
Então o documento não aparece na listagem para associação

*(Cenário original: PM Guamaré, setor SEMAVM, memorando, Ofício 001839/2025.)*

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://9610)

**Antes da correção** (bug reproduzido em DEV — documento de setor não ativo não aparecia na busca da abertura):
![[9610 - abertura nao associa documento de setor nao ativo antes da correcao.mp4]]

**Depois da correção** (aprovado em DEV — documento passa a aparecer e permite associar):
![[9610 - abertura associa documento de setor nao ativo aprovado em dev.mp4]]

- Evidências **na task do Notion**, sem cópia local: vídeo `Gravando_2026-06-25_135854_-_documento_no_sendo_associado.mp4` (relato) + print na análise da Bruna.
- Documento do relato (produção Guamaré): https://www.sogov.com.br/cliente/30/documento/MIRMG47ELROGYSKCT6

---

### Resultado Esperado

Documento ao qual o servidor tem acesso — **por qualquer setor do qual participe, atuando por ele ou não** — aparece na busca de associação da abertura e pode ser selecionado.

---

### Critérios de aceite

- [x] Servidor multi-setor atuando pelo setor A encontra, na busca da abertura, documento acessível pelo setor B
- [x] Documento do próprio setor ativo continua aparecendo na busca da abertura
- [x] A busca da abertura retorna os mesmos documentos que a busca de associação **via despacho**, pro mesmo usuário
- [x] Documento ao qual o servidor **não** tem acesso por nenhum setor continua **fora** da listagem — a correção não pode ter liberado a busca sem filtro de setor
- [x] Sem regressão nas telas tocadas pelo MR: associação via despacho e assinatura via toolbar seguem funcionando, inclusive com usuário multi-setor

---

### Casos de Teste Básicos

- **CT-B01 Associar na abertura documento de setor em que não está atuando**
    Dado que um servidor esteja cadastrado nos setores A e B
    E esteja atuando pelo setor A
    Quando buscar, na abertura de um novo documento, um documento acessível pelo setor B
    Então o documento deve aparecer na listagem e permitir a associação

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:
        ![[9610 - abertura associa documento de setor nao ativo aprovado em dev.mp4]]

- **CT-B02 Associar na abertura documento do setor ativo**
    Dado que um servidor esteja atuando pelo setor A
    Quando buscar, na abertura de um novo documento, um documento acessível pelo próprio setor A
    Então o documento deve aparecer na listagem e permitir a associação

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Paridade entre a busca da abertura e a busca via despacho**
    Dado que um servidor tenha acesso a um documento
    E esse documento seja encontrado na busca de associação via despacho
    Quando o mesmo servidor buscar o mesmo documento na associação da abertura
    Então o documento deve ser encontrado nas duas buscas

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Documento sem acesso continua fora da listagem**
    Dado que um servidor não tenha acesso a um documento por nenhum dos seus setores
    Quando buscar esse documento na associação da abertura
    Então o documento não deve aparecer na listagem para associação

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B05 Regressão: associação via despacho**
    Dado que um servidor multi-setor esteja num documento em tramitação
    Quando associar um documento através de um despacho
    Então a associação deve ser concluída normalmente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B06 Regressão: assinatura via toolbar**
    Dado que um servidor multi-setor esteja num documento com locais passíveis de assinatura
    Quando acionar a assinatura pela toolbar e concluir o fluxo
    Então a assinatura deve ser realizada normalmente

    - Execução Passou?
        - [x] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [MR !537](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/537) (João Rodrigo — aprovado por B. Luan e Bruno Clementino; status Notion: pronto pra teste em dev)
    
- Observações: análise completa do refinamento em [[../../04 Conhecimento/SGV-9610 - Refinamento Associar Documento Abertura Multi-Setor|SGV-9610 (refinamento arquivado)]]; regras do módulo em [[../../04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]]; plano de automação (quando validar) em [[../../04 Conhecimento/SGV-9610 - Plano de Automação|SGV-9610 - Plano de Automação]]
    
- Histórico:
    - 2026-07-17 - 🐛 Card criado a partir do refinamento (destilado)
    - 2026-07-17 - 📤 Análise/critérios registrados na task no Notion; mesa de refinamento arquivada em 04 Conhecimento
    - 2026-07-23 - 🔎 Verificado contra doc [[../../04 Conhecimento/Módulos/Associar e Desassociar|Associar e Desassociar]] — doc respalda (busca limitada ao acesso, por qualquer setor do qual participe; não por setor ativo)
    - 2026-07-23 - ✅ Aprovada em DEV (6 CTs e 5 critérios atendidos; segue pra homologação)
