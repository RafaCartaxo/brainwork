---
tags:
  - bug
  - qa
  - documentos-automatizados
  - campos-dinamicos
task: "9963"
prioridade: alta
status: aberto
data_inicio: 2026-07-15
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documentos-automatizados
ambiente: DEV
---
# Campos dinâmicos (@) quebram ao alterar o módulo do Assunto/Serviço vinculado ao modelo

### Descrição

Durante análise (Bruna Machado, 13/07) foi identificada a causa raiz: ao criar um modelo de documento automatizado vinculado a um Assunto/Serviço do módulo X e, depois, alterar o módulo desse Assunto/Serviço para Y, os campos dinâmicos (@) do modelo quebram. O erro **persiste mesmo revertendo** o Assunto/Serviço para o módulo X original — a alteração de módulo corrompe a referência de forma irreversível. Paliativa em uso: criar um novo Assunto/Serviço já no módulo correto e revinculá-lo ao modelo, evitando alteração de módulo em Assuntos/Serviços já usados por modelos existentes.

Contexto da função: o @ insere variáveis dinâmicas no modelo (campos do formulário do documento emissor + número do doc emissor, tipo do usuário externo, setor responsável do doc emissor, data de abertura do doc emissor, número do doc gerado, data de abertura do doc gerado), resolvidas com o dado vigente no momento da geração do documento.

---

### Passo a passo para reproduzir

Dado que exista um Assunto/Serviço vinculado ao módulo X
E um modelo de documento automatizado vinculado a esse Assunto/Serviço, com campos dinâmicos (@) funcionando corretamente
Quando o módulo do Assunto/Serviço for alterado de X para Y
E um documento automatizado vinculado a ele for aberto ou gerado
Então os campos dinâmicos (@) do modelo aparecem quebrados/corrompidos
E reverter o módulo de Y para X não restaura o funcionamento (o erro persiste)

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://9963)

- Vídeo da análise (`2026-07-13 09-48-29.mp4`) registrado **na task do Notion** — sem cópia local: este card é só a análise/definição de critérios. Evidências locais entram no fluxo normal quando houver validação em homologação.

---

### Resultado Esperado

Os campos dinâmicos (@) continuam funcionando normalmente após **qualquer** alteração de módulo do Assunto/Serviço — X→Y, Y→X, Y→Z, quantas trocas forem: a referência acompanha a mudança, sem corrupção em nenhum ponto do caminho.

---

### Critérios de aceite

- [ ] Alterar o módulo de um Assunto/Serviço **não quebra** os campos dinâmicos (@) dos modelos de documento automatizado vinculados — eles continuam resolvendo normalmente na geração
- [ ] Funciona em **qualquer sequência de trocas** de módulo (X→Y→X, X→Y→Z, ...): nenhuma alteração, em nenhuma ordem, corrompe a referência dos campos (@)
- [ ] Documentos **já gerados** antes da alteração de módulo permanecem íntegros (conteúdo resolvido não muda)
- [ ] Modelos **já corrompidos** por alterações de módulo anteriores à correção: definir com dev/produto se a correção inclui saneamento retroativo ou se vale a paliativa (novo Assunto/Serviço) — deixar explícito na entrega
- [ ] Sem regressão no fluxo normal: criar modelo novo com @ e gerar documento segue funcionando; todas as variáveis (campos do formulário + as 6 fixas) resolvem com o dado vigente no momento da geração

---

### Casos de Teste Básicos

- **CT-B01 Campos (@) continuam funcionando após alteração de módulo**
    Dado que um modelo automatizado com campos (@) esteja vinculado a um Assunto/Serviço do módulo X
    Quando o módulo do Assunto/Serviço for alterado pra Y e um documento for gerado a partir do modelo
    Então todos os campos dinâmicos devem resolver normalmente, com os dados vigentes

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Trocas múltiplas de módulo mantêm os campos funcionando**
    Dado que um Assunto/Serviço com modelo automatizado vinculado passe por uma sequência de trocas de módulo (ex.: X→Y→X, depois X→Z)
    Quando um documento for gerado após cada troca
    Então os campos dinâmicos devem resolver normalmente em todas as gerações, sem corrupção residual em nenhum ponto

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Documentos gerados antes da alteração permanecem íntegros**
    Dado que um documento automatizado tenha sido gerado antes da alteração de módulo
    Quando o módulo do Assunto/Serviço for alterado
    Então o conteúdo do documento já gerado permanece exatamente como foi resolvido na geração

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Fluxo normal sem regressão (todas as variáveis)**
    Dado que um modelo novo seja criado com campos do formulário e as variáveis fixas (número/data de abertura do doc emissor, tipo do usuário externo, setor responsável, número/data de abertura do doc gerado)
    Quando um documento for gerado a partir dele
    Então cada variável resolve pro valor vigente no momento da geração, sem nenhuma variável crua ou identificador técnico no resultado

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente: (validação direto em homologação — fluxo 3f, task de API sem etapa DEV)

---

### Informações adicionais

- Demanda relacionada: SGV-9963 (análise de Bruna Machado, 13/07/2026)
- Observações: Esteira 3f ([[Sistema/Contexto/FLUXOS|FLUXOS]]) — QA define critérios, dev implementa os cenários de teste, QA revisa os cenários contra estes critérios, teste real direto em homologação.
- Histórico:
    - 2026-07-13 - Análise de causa raiz (Bruna Machado): alteração de módulo corrompe referência dos (@) de forma irreversível
    - 2026-07-15 - 📝 Bug refinado (critérios de aceite prontos pro dev)
    - 2026-07-15 - Número confirmado (SGV-9963); evidência mantida na task do Notion, sem cópia local
    - 2026-07-15 - 📤 Análise e critérios de aceite registrados na task do Notion
