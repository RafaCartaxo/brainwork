---
tags:
  - qa
  - skill
---
# Skill: Criação e Organização de Bugs

Criar, revisar e organizar bugs seguindo o padrão utilizado no Vault QA. ([Template](../Templates/Bug Report.md))

## Objetivos

- Estruturar bugs de forma clara e reproduzível
- Garantir descrição objetiva do problema
- Padronizar redação e formatação
- Facilitar entendimento por Produto, Desenvolvimento e QA
- Garantir rastreabilidade do defeito

## Modos de entrada

Como a task pode chegar, e o que fazer em cada caso antes de aplicar a Estrutura Padrão abaixo:

- **Suspeita própria**: possível bug identificado durante o trabalho, ainda sem confirmação. Nasce como `❓ Suspeita de bug registrada` na daily (+ pendência de investigar). Só vira card **depois** de confirmado na investigação; descartado, vira `🗑️` sem card (trilha completa no catálogo do [[QA Workspace/01 Daily/README|01 Daily/README]]).
- **Relato rápido**: descrição em texto livre (Gherkin ou corrido) + número do SGV. Vai direto pro template, sem trabalho extra.
- **Contexto rico**: quando vier bastante material bruto (histórico, várias rodadas, análise de causa raiz, texto colado de outro lugar). Extrair os campos certos (ambiente, módulo, prioridade, passos, critérios de aceite) sem perder informação. Se algo ficar ambíguo, perguntar antes de assumir — não simplificar. Onde cada peça do material entra no card: ver "Bug com análise" nas Regras abaixo.
- **Via CX**: bug reportado pelo atendimento, normalmente em linguagem de usuário final, sem passo técnico claro. Antes de fechar o card: investigar o código relacionado pra entender o comportamento real (não só confiar na descrição do CX), perguntar o que não ficar claro pra reproduzir. Se mesmo assim não for possível confirmar/reproduzir sozinho, marcar isso em **Observações** ("precisa confirmação") em vez de fechar como se já tivesse validado.

Os três modos convergem no mesmo resultado: card no template certo, na pasta certa (`02 Demandas/<ambiente>/`), registrado em **Bugs encontrados** da daily do dia.

## Estrutura Padrão

# Título

### Descrição

Durante validação foi identificado que...

---

### Passo a passo para reproduzir

Dado que...
E...
Quando...
Então...

---

### Evidências [📁](file:///caminho/da/pasta/do/ambiente/) [🔍](evidencia://<número do card>)


---

### Resultado Esperado

-

---

### Critérios de aceite

- [ ] ...

---

### Casos de Teste Básicos

- **CT-B01 Título do caso de teste**
    Dado que...
    E...
    Quando...
    Então...

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão:
- Ambiente:

---

### Informações adicionais

- Demanda relacionada: SGV-XXXX
- Observações:
- Histórico:
    - YYYY-MM-DD - 🐛 Bug cadastrado

## Regras

### Título

Deve descrever claramente o problema.

Exemplos:

- CPF exibido com máscara incorreta na impressão
- Campo "Para" não é preenchido em resposta do cidadão
- Documento sigiloso exibe conteúdo na mesa de trabalho

Evitar:

- Erro na tela
- Problema no sistema
- Bug impressão

### Descrição

Explicar o comportamento encontrado.

Utilizar:

"Durante validação foi identificado que..."

Evitar:

- Explicações extensas
- Opiniões pessoais
- Hipóteses técnicas

### Passos

Preferencialmente no padrão:

Dado que...
Quando...
Então...

Os passos devem permitir reprodução do problema.

### Resultado Esperado

Descrever claramente o comportamento correto.

### Critérios de Aceite

Utilizar quando houver regra de negócio associada. Cada critério é um checkbox (`- [ ] <critério>`), marcado quando confirmado atendido na validação — mesma lógica do "Execução Passou?" dos CTs, mas por critério.

### Evidências

Referenciar vídeos, imagens ou links utilizados na validação. Processo completo (gravar → renomear → mover pra subpasta do ambiente → embed): ver [[../Contexto/COMO_EU_TRABALHO.md#Evidências|COMO_EU_TRABALHO.md]]. Nome do arquivo: `<número do card> - <breve descrição>.mp4` (ex.: `9971 - solicitar assinatura para servidor com cadastro incompleto.mp4`). Referenciar como embed, não como caminho em texto: `![[9971 - solicitar assinatura para servidor com cadastro incompleto.mp4]]`.

**Mesma gravação servindo a mais de um caso** (ex.: validação que reprova uma demanda e abre um bug novo): criar uma cópia do arquivo renomeada com o número de cada card — cada card embeda a sua — e anotar o compartilhamento em **Observações** dos dois lados (ex.: "Evidência compartilhada com SGV-XXXX — mesmo vídeo, cópia renomeada").

O título da seção leva dois links de atalho, só o ícone: `### Evidências [📁](file:///caminho/da/pasta/do/ambiente/) [🔍](evidencia://<número do card>)`.
- **📁**: abre a pasta do ambiente inteira (Desenvolvimento/Homologação/Produção/etc.) no gerenciador de arquivos. Confiável, mas mostra todos os vídeos daquele ambiente, não só os do card.
- **🔍**: usa um esquema de URI customizado (`evidencia://`) que abre o Nautilus em modo de busca pelo número do card — mais rápido quando funciona, mas a busca não é restrita à pasta Evidências (pode trazer resultado de fora). Por isso os dois ficam lado a lado por enquanto, até melhorar a precisão da busca.

Infra do `evidencia://`: script `~/.local/bin/abrir-evidencia` + `.desktop` em `~/.local/share/applications/abrir-evidencia.desktop`, registrado via `xdg-mime default` pra `x-scheme-handler/evidencia` (detalhe completo em [[Plugins Instalados.md]]). Só funciona nesta máquina (Linux/GNOME/Nautilus) — em outro computador ou com outra IA, cai de volta só pro link `file://` de pasta.

### Casos de Teste Básicos

Detalhar os cenários de validação no padrão Dado/Quando/Então (CT-B01, CT-B02...), com "Execução Passou?" e "Evidências de Testes" por caso. Estruturar cada caso como um item de lista (`- **CT-B01 Título**`) com o Dado/E/Quando/Então **sem bullet própria** — linhas soltas, só indentadas, como continuação do mesmo item (fica menos poluído visualmente e ainda recolhe o CT inteiro de uma vez no Obsidian, já que a dobra segue o item pai). O "Execução Passou?" deve ser uma to-do list com "Sim" em verde e "Não" em vermelho, para facilitar a visualização do resultado.

### Informações adicionais

O **Histórico** registra cada etapa vivida pelo card, com a frase padrão prefixada pela data (`- YYYY-MM-DD - <frase com emoji>` — mesma copy do [[../../01 Daily/README|01 Daily/README]]). O card nasce com a primeira linha: `🐛 Bug cadastrado` quando já tem SGV; `🐛 Bug confirmado (card criado)` quando ainda não tem.

### Bug com análise (causa raiz)

Quando o card nasce de uma análise — própria ou de outra pessoa, comum ao transformar um bug já cadastrado no Notion pro padrão do vault (precedente: SGV-9963, análise de causa raiz de terceiro) — o material se distribui assim:

- **Descrição**: comportamento observado + causa raiz **resumida**, com autoria e data ("Durante análise (<quem>, <data>) foi identificada a causa raiz: ..."). Paliativa em uso, se existir, também entra aqui. *(Este é o caso que excetua o "evitar explicações extensas/hipóteses técnicas" da regra de Descrição: análise confirmada não é hipótese.)*
- **Contexto técnico**: só o que ajuda a escrever e entender os CTs (o que a função faz, variáveis envolvidas) — parágrafo próprio na Descrição, nada além disso.
- **Critérios de aceite** são o coração do refinamento: além do comportamento correto, cobrir os **dados já corrompidos/afetados** pelo bug (correção retroativa ou paliativa? deixar explícito pra decidir com dev/produto) e a **regressão do fluxo normal**.
- **Histórico**: a análise é a primeira linha, datada e com autoria — `- YYYY-MM-DD - Análise de causa raiz (<quem>): <síntese curta>`.
- **Evidência que mora fora** (ex.: vídeo anexado na task do Notion): anotar na seção Evidências **onde ela está**, sem cópia local — evidência local entra no fluxo normal quando houver validação.
- **Na daily**: análise sua rende `🔎 SGV-XXXX - Análise (<resultado curto>)`; o refinamento rende `📝 SGV-XXXX - Bug refinado (critérios de aceite prontos)` e, levando pro Notion, `📤`.

## Resultado Esperado

Retornar o bug pronto para registro no Notion ou ferramenta equivalente.