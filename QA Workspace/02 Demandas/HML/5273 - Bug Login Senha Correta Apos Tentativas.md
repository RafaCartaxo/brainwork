---
tags:
  - bug
  - qa
  - login
task: "5273"
prioridade: altíssima
status: em_validacao
data_inicio: 2025-12-26
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: login
ambiente: HML
---
# Login com senha correta não funciona após tentativas incorretas

### Descrição

Usuários do Sogov não conseguem fazer login com a senha correta após tentativas incorretas. O problema ocorre após quatro tentativas falhas: mesmo informando a senha correta na 5ª tentativa, o sistema bloqueia o acesso como se a senha estivesse errada. Impacta segurança e compliance — cliente(s) afetado(s): **todos**; funcionalidade afetada: recuperação de senha.

**Análise de causa raiz** (Bruna Machado, 26/12/2025) — confirmado que o usuário não consegue logar mesmo informando a senha correta, após tentativas anteriores com senha incorreta. A lógica aplicada bloqueava o acesso a partir da 4ª tentativa (verificando o limite de tentativas **antes** de verificar se a senha informada estava correta), informando que restava "uma última tentativa" mesmo quando essa tentativa usava a senha certa.

**Entrega do dev** (Matheus Godoi, 12/06/2026 — [MR !419](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/419), aprovado por Marcos Vinicius e Lucas Cabral em 16/06/2026) — Inverte a ordem do fluxo de autenticação em `auth-handler.ts`: agora a senha é verificada **antes** da checagem do limite de tentativas. Se a senha está correta, o login é concluído normalmente, ignorando o contador de tentativas. Só quando a senha está **incorreta** é que o fluxo verifica se o limite foi atingido (e aí bloqueia a conta e dispara e-mail de recuperação, como antes). Tela impactada: Login. Sem endpoint específico. **Nenhum teste automatizado foi adicionado** (arquivos tocados: só `auth-handler.ts` e `userToken.ts`).

**Aprovado em DEV** (Rafael, 10/07/2026) — Ambiente: `dev-marcos-santos.d10fnl6gn002xw.amplifyapp.com`. Status atual no Notion: **Testando em homologação**.

---

### Passo a passo para reproduzir

Dado que o usuário acesse a tela de login do Sogov
E realize 4 tentativas de login com senha incorreta
E veja a mensagem de aviso "Recuperar senha"
Quando realizar a 5ª tentativa de login com a senha **correta**
Então o login deveria ser efetuado — mas, no bug original, a conta aparecia bloqueada mesmo com a senha certa

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://5273)

- Evidências **na task do Notion**, sem cópia local: print anexado à descrição original (bug reproduzido) e evidência da aprovação em DEV mencionada no comentário de Rafael (10/07). Evidência local entra no fluxo normal na validação em HML.

---

### Resultado Esperado

Quando o usuário digitar as credenciais de acesso corretas — mesmo após ter esgotado as tentativas máximas —, o sistema deve efetuar o login com sucesso.

---

### Critérios de aceite

- [ ] Usuário consegue logar com a **senha correta** mesmo após ter atingido o limite máximo de tentativas (cenário original do bug)
- [ ] Senha **incorreta** informada após o limite de tentativas continua bloqueando a conta normalmente, com envio do e-mail de recuperação (regressão do fluxo de bloqueio — não pode ter sido removido, só reordenado)
- [ ] Dentro do limite, senha incorreta continua incrementando o contador de tentativas e exibindo corretamente quantas tentativas restam
- [ ] E-mail de recuperação exibido/enviado na mensagem de bloqueio continua **anonimizado** (ver [[QA Workspace/04 Conhecimento/Módulos/Login|Login]])
- [ ] **Sem teste automatizado cobrindo o fix** — toda validação é manual; conferir também em **Produção**, já que o export original cita Homologação e Produção como ambientes afetados

---

### Casos de Teste Básicos

- **CT-B01 Login com senha correta após esgotar tentativas (cenário do bug)**
    Dado que o usuário tenha errado a senha o número de vezes que antecede o bloqueio
    Quando informar a senha correta na tentativa seguinte
    Então o login deve ser efetuado com sucesso

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B02 Regressão: bloqueio continua funcionando com senha errada no limite**
    Dado que o usuário atinja o limite máximo de tentativas
    Quando errar a senha novamente (sem nunca acertar)
    Então a conta deve ser bloqueada e o e-mail de recuperação deve ser disparado, como antes do fix

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B03 Regressão: contador de tentativas dentro do limite**
    Dado que o usuário erre a senha uma vez, dentro do limite
    Quando visualizar a mensagem de erro
    Então deve ser informado corretamente quantas tentativas restam

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

- **CT-B04 Validação em Produção**
    Dado o mesmo cenário do CT-B01
    Quando reproduzido em ambiente de Produção
    Então o login com senha correta deve funcionar igualmente

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [ ] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes:

---

### Ambiente

- Versão: Homolog 12.32.32.2 (14/07/2026) / 12.33.36.2 (16/07/2026)
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: [MR !419](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/419) (Matheus Godoi — revisores Marcos Vinicius e Lucas Cabral; QA Responsável: Rafael Borges)
- Observações: Relacionado à **SGV-5428** (Notion — "Plataforma não está encaminhando o e-mail de recuperação de conta para usuário bloqueado", status **Despriorizado**) — mesmo fluxo de bloqueio/recuperação, mas item separado e sem prioridade no momento. Regras do módulo em [[QA Workspace/04 Conhecimento/Módulos/Login|Login]] (bloqueio em 5 tentativas, e-mail anonimizado).
- Histórico:
    - 2025-12-26 - 🔎 Análise de causa raiz (Bruna Machado): bloqueio ocorria por checar o limite de tentativas antes da senha
    - 2026-06-12 - Entrega do dev (Matheus Godoi, MR !419 aberto)
    - 2026-06-16 - MR aprovado para testes (Marcos Vinicius, Lucas Cabral)
    - 2026-07-10 - ✅ Aprovado em DEV (Rafael)
    - 2026-07-20 - 🐛 Card trazido pro vault a partir do export do Notion (status real: Testando em homologação) — critérios de aceite e CTs escritos a partir da descrição, análise e do diff do MR !419
