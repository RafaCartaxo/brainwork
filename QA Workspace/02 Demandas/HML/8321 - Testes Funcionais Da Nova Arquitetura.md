---
tags:
  - demanda
  - funcionalidade
  - qa
  - arquitetura
task: "8321"
status: aberto
prioridade: alta
data_inicio: 2026-08-26
data_fim: ""
responsavel: Rafael Borges, Flávio Oliveira
cadastrado_por: ""
modulo: arquitetura
ambiente: HML
---
# Demanda: [Funcionalidade] Testes funcionais da nova arquitetura

> [!info] Informações
> - **Tipo:** Funcionalidade — Plano de Teste (migração de arquitetura Lambda → EKS)
> - **Status:** HML (novo ambiente de homologação disponibilizado — rodada de revalidação)
> - **Responsável QA:** Rafael Borges, Flávio Oliveira
> - **Link:** [SGV-8321 no Notion](https://app.notion.com/p/alfa-group/Testes-funcionais-da-nova-arquitetura-34c2aec67d308025b995c6880652eeb7)
> - **Dev responsável:** Flávio Oliveira
> - **Cliente(s) afetado(s):** — (não informado no export) · **Projetos:** Arquitetura, Sustentação
> - **Deadline firmado com cliente (Notion):** 27/04/2026 → 15/05/2026 *(já vencido — ver Pontos de atenção)* · **Progresso de subitens:** 4,17%

---

> [!abstract] Resumo

O time trocou a "sala de máquinas" do sistema — de Lambda (funções que rodavam sob demanda) pra pods em Kubernetes (EKS), sempre ligados. Pra quem usa o SoGov pela tela, **nada deveria mudar**: os mesmos botões, os mesmos fluxos, o mesmo resultado. Esta nota existe pra confirmar isso na prática, no novo ambiente de homologação.

Nasce do processamento de 2 exports do Notion (`SKILL_LIMPEZA_EXPORT`, Modo B — card direto): o roteiro de testes original da SGV-8321 e a lista de bugs abertos/solucionados na rodada anterior. Reescrita em 2026-08-26 pra sair do tom técnico do export original (worker, SQS, initContainer, IRSA, ArgoCD) e virar algo que dá pra executar clicando na tela, do jeito que o resto do vault já faz.

---

## Regras de negócio

Não existe regra de negócio nova — a interface continua a mesma. O que muda é **como o sistema processa por trás**: ações que antes aconteciam na hora (enviar e-mail, assinar, importar, gerar PDF) agora passam primeiro por uma fila de espera; tarefas programadas (avisos, expiração de convite, publicações) rodam por conta própria em vez de disparadas por evento; o deploy de cada versão nova atualiza o banco de dados sozinho antes de liberar o sistema. Cada grupo de Casos de Teste abaixo carrega uma nota curta do "por quê" quando o contexto ajuda a entender o risco.

---

> [!warning] Pontos de atenção
> - **Deadline do Notion está vencido** (27/04/2026 → 15/05/2026, e hoje é 2026-08-26) — sinalizar com Flávio/Produto se o prazo desta rodada de revalidação precisa ser refirmado.
> - **3 bugs da rodada anterior são especificamente de POC** (SGV-9076, SGV-9074, SGV-8658, tag `[BUG-Arquitetura-POC]`, ambiente "POC1") — confirmar se esse ambiente de POC ainda existe/é relevante no novo ambiente de homologação antes de tentar revalidar esses três.
> - O export original não trouxe "Responsáveis" preenchidos por ponto de teste (colunas vazias) — distribuir entre Rafael e Flávio ao iniciar a execução.
> - **SGV-9530** ("Erro ao tentar ativar instância") está com status **Cancelado** na rodada anterior — não faz parte da revalidação.
> - Esta nota separa dois tipos de verificação: **Casos de Teste** (dá pra clicar e observar sozinho na tela) e **Verificações técnicas** (dependem de log/painel/teste de carga feito pelo Dev ou Infra — não existe fluxo de tela pra elas). Ver as duas seções abaixo.

---

## Casos de Teste ([skill](../../../Sistema/Skills/SKILL_CASOS_DE_TESTE.md))

*O que dá pra clicar, observar e confirmar direto na tela.*

### A. Ações que agora passam por uma fila de espera antes de acontecer (Crítico)

Antes, ações como enviar e-mail, assinar documento ou importar arquivo aconteciam na hora. Agora cada uma passa primeiro por um processamento em segundo plano — pode levar alguns segundos a mais, e se uma travar, as outras continuam funcionando normalmente (não é mais tudo ou nada).

#### **CT-001 Enviar um e-mail pelo sistema continua funcionando** *(CA1)*

**Dado** que eu realizo uma ação que dispara e-mail (ex.: enviar um convite de cadastro)
**Quando** eu confirmo a ação
**Então** verifico que o e-mail chega certo na caixa de entrada, em até 30 segundos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Assinar um documento continua funcionando** *(CA2)*

**Dado** que eu tenho um documento pronto pra assinatura
**Quando** eu assino
**Então** verifico que o documento fica assinado corretamente, em até 30 segundos

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

> [!danger]- Reprovado em 01/09/2026 (segue reprovado) — bugs [[QA Workspace/02 Demandas/Concluídas/11215 - Bug Documento Não Carrega Para Realizar Assinatura|SGV-11215]] (aprovada parcialmente em 02/09) e [[QA Workspace/02 Demandas/HML/11249 - Bug Assinatura De Documento Ou Despacho Não É Concluída Com Sucesso|SGV-11249]]
> Ao solicitar a assinatura de um servidor num documento/despacho/anexo e clicar pra assinar, o documento não carregava — resolvido, aprovado em 02/09/2026 v. 14.17.0 (SGV-11215). Mas a assinatura em si segue não sendo concluída com sucesso, com ou sem anexo — CT-002 continua reprovado por isso (SGV-11249, aberta).

**Evidências de Testes:**

---

#### **CT-003 Receber uma notificação continua funcionando** *(CA3)*

**Dado** que uma ação minha ou de outro usuário deveria gerar notificação (ex.: documento tramitado pra mim)
**Quando** essa ação acontece
**Então** verifico que a notificação chega pra mim, em até 30 segundos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-004 Importar um documento continua funcionando** *(CA4)*

**Dado** que eu tenho um arquivo pra importar como documento
**Quando** eu importo
**Então** verifico que o documento é criado corretamente a partir do arquivo, em até 30 segundos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005 Criar um documento continua funcionando** *(CA5)*

**Dado** que eu preencho os dados de um novo documento
**Quando** eu confirmo a criação
**Então** verifico que o documento é criado com sucesso, em até 30 segundos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-006 Gerar um relatório de BI continua funcionando** *(CA6)*

**Dado** que eu solicito um relatório de BI
**Quando** eu confirmo a geração
**Então** verifico que o relatório fica disponível, com os dados corretos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-007 Gerar PDF de vários despachos de uma vez continua funcionando** *(CA7)*

**Dado** que eu selecionei vários despachos
**Quando** eu peço pra gerar/baixar o PDF de todos juntos
**Então** verifico que todos os PDFs são gerados corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-008 Gerar o PDF final de um documento assinado continua funcionando** *(CA8)*

**Dado** que eu tenho um documento pronto pra emissão/assinatura
**Quando** eu peço pra gerar o PDF final
**Então** verifico que o PDF sai correto e disponível pra download

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-009 Retomar uma importação que ficou pendente continua funcionando** *(CA9)*

**Dado** que uma importação de documento minha ficou pendente
**Quando** eu volto mais tarde pra conferir
**Então** verifico que ela concluiu sozinha, sem ficar travada pra sempre

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-010 Texto longo ou com acentos/caracteres especiais não trava nenhuma dessas ações** *(CA10)*

**Dado** que eu preencho um campo com texto longo, acentos ou caracteres especiais (ex.: "ç", "ã", símbolos)
**Quando** eu realizo qualquer uma das ações acima (CT-001 a CT-009)
**Então** verifico que o conteúdo chega correto do outro lado, sem cortar ou corromper

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Convite, prazo e publicação automática

Rotinas que rodam sozinhas em horário programado, sem eu precisar clicar em nada.

#### **CT-011 Convite de cadastro expira no prazo certo** *(CA11)*

**Dado** que eu enviei um convite de cadastro pra alguém
**Quando** o prazo de validade do convite passa
**Então** verifico que o convite não pode mais ser usado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-012 Aviso de prazo de processo vencendo chega no dia certo** *(CA12)*

**Dado** que um processo/documento meu está com prazo perto de vencer
**Quando** a data de aviso programada chega
**Então** verifico que o aviso/notificação chega certinho

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-013 Aviso de contrato de cliente vencendo chega no dia certo** *(CA13)*

**Dado** que um contrato de cliente está perto do vencimento
**Quando** a data de aviso programada chega
**Então** verifico que quem precisa saber é avisado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-014 Documento programado pra publicar no mural sai na data certa** *(CA14)*

**Dado** que eu programei um documento pra publicar no mural numa data futura
**Quando** essa data chega
**Então** verifico que ele é publicado sozinho, sem eu precisar fazer nada manualmente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

> [!info]- Rotinas sem tela pra observar direto
> Existem outras rotinas automáticas (limpeza de módulos temporários, atualização de status de trabalho, ativação/inativação de chave de acesso, aviso de módulo fora do ar, geração agendada de relatórios) que não têm uma tela específica pra eu conferir sozinho — ficam na seção **Verificações técnicas**, no fim desta nota.

---

### C. Login, troca de instância e sessão (Alto risco)

#### **CT-015 Login funciona normalmente** *(CA15)*

**Dado** que eu tenho usuário e senha válidos
**Quando** eu faço login
**Então** verifico que entro normalmente e fico conectado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-016 Trocar de prefeitura/instância mostra os dados certos** *(CA16)*

**Dado** que eu tenho acesso a mais de uma instância
**Quando** eu troco de instância pelo seletor
**Então** verifico que os dados exibidos mudam pra da instância selecionada, sem misturar com a anterior

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-017 Logout desconecta de verdade** *(CA17)*

**Dado** que eu estou logado
**Quando** eu clico em sair
**Então** verifico que realmente saio — ao tentar acessar uma página interna de novo, sou redirecionado pro login

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-018 Continuo logado depois da atualização do sistema** *(CA18)*

**Dado** que eu já estava logado antes da virada pra nova versão do sistema
**Quando** o sistema muda de versão
**Então** verifico que continuo conectado, sem ser desconectado à força

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-019 Login funciona a partir de um link de e-mail aberto em nova aba** *(CA19)*

**Dado** que eu recebo um e-mail com link de ação (ex.: convite, redefinição de senha)
**Quando** eu clico no link e ele abre numa aba nova
**Então** verifico que consigo fazer login normalmente nessa aba

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Upload e download de arquivos

#### **CT-020 Upload de arquivo grande (acima de 6MB) funciona** *(CA20)*

**Dado** que eu tenho um arquivo maior que 6MB
**Quando** eu faço upload dele (documento, anexo, foto de perfil, logo da instância)
**Então** verifico que o upload conclui com sucesso (antes existia um limite de 6MB que não existe mais)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-021 Upload de arquivos bem grandes (50, 100, 500MB) funciona** *(CA21)*

**Dado** que eu tenho arquivos bem grandes
**Quando** eu tento o upload
**Então** verifico que ele conclui, ou — se houver um limite — que a mensagem de erro é clara

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-022 Link de upload/download não fica válido pra sempre** *(CA22)*

**Dado** que eu tenho um link de upload/download gerado pelo sistema
**Quando** eu tento usá-lo bem depois de ele ter sido gerado
**Então** verifico que ele já não funciona mais (expirou) — checagem de segurança

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-023 Anexar arquivo em campo de texto longo funciona** *(CA23)*

**Dado** que eu tenho um formulário com campo de texto longo que aceita anexo
**Quando** eu anexo um arquivo nesse campo
**Então** verifico que ele é salvo corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-024 Vários uploads ao mesmo tempo não travam** *(CA24)*

**Dado** que eu selecionei vários arquivos
**Quando** eu envio todos de uma vez
**Então** verifico que todos concluem certo, sem nenhum travar ou corromper

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Conteúdo e aparência dos e-mails do sistema

#### **CT-025 E-mails do sistema chegam corretamente** *(CA25)*

**Dado** que eu realizo uma ação que dispara e-mail
**Quando** o e-mail é enviado
**Então** verifico que ele chega normalmente na caixa de entrada

**Execução Passou?**
- [ ] Sim
- [x] Não

> [!danger]- Reprovado em 26/08/2026 — bug [[QA Workspace/02 Demandas/HML/Bug E-mail De Confirmacao De Cadastro Nao Chega No Novo Ambiente De Homologacao|Bug E-mail De Confirmação De Cadastro]]
> Testado via automação (setup de pré-cadastro de agente) e confirmado manualmente checando a caixa Gmail: o e-mail de confirmação de cadastro não chega no `dev.sogov.net`. Card do bug aberto, aguardando SGV.

**Evidências de Testes:**

---

#### **CT-026 Aparência dos e-mails está correta** *(CA26)*

**Dado** que eu recebo um e-mail do sistema
**Quando** eu abro
**Então** verifico que o layout e o texto aparecem certos, sem quebra de formatação

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-027 E-mail com anexo chega correto** *(CA27)*

**Dado** que eu recebo um e-mail que deveria vir com anexo
**Quando** eu abro
**Então** verifico que o anexo está lá e abre sem problema

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-028 Logo do SOGOV aparece no e-mail "Finalize seu cadastro"** *(CA28)*

**Dado** que eu sou um cidadão Pessoa Física recebendo o e-mail de finalização de cadastro
**Quando** eu abro o e-mail
**Então** verifico que a logo do SOGOV aparece corretamente

> 💡 Bug conhecido da rodada anterior (SGV-8602) — atenção redobrada aqui.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### F. Geração e download de PDF (documentos e despachos)

#### **CT-029 Emitir/assinar e baixar documento em PDF funciona ponta a ponta** *(CA29)*

**Dado** que eu tenho um documento pronto pra emissão/assinatura
**Quando** eu gero o PDF assinado e baixo
**Então** verifico que o PDF sai correto

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-030 Gerar PDF de vários despachos de uma vez funciona** *(CA30)*

**Dado** que eu selecionei vários despachos
**Quando** eu peço a geração em lote
**Então** verifico que todos saem corretos

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-031 Tempo de geração de PDF continua razoável** *(CA31)*

**Dado** que eu gero um PDF (documento ou despacho)
**Quando** eu comparo com o tempo que levava antes da mudança
**Então** verifico que não está visivelmente mais lento

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-032 Vários usuários gerando PDF ao mesmo tempo não trava o sistema** *(CA32)*

**Dado** que mais de uma pessoa gera PDF ao mesmo tempo (testar com outro QA/colega, se possível)
**Quando** as gerações acontecem juntas
**Então** verifico que todas concluem normalmente, sem erro pra ninguém

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### G. O que eu cadastro aparece certo e na hora

#### **CT-033 O que acabei de cadastrar aparece na hora** *(CA33)*

**Dado** que eu acabei de criar/editar algo (documento, setor, usuário)
**Quando** eu vou pra tela que lista/mostra esse dado
**Então** verifico que ele já aparece, sem precisar recarregar várias vezes

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-034 Relatórios de BI mostram números corretos** *(CA34)*

**Dado** que eu gero um relatório de BI
**Quando** eu confiro os números
**Então** verifico que eles batem com o que está cadastrado no sistema

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### H. Fluxos principais continuam funcionando (regressão geral)

#### **CT-035 Fluxos principais do sistema continuam funcionando** *(CA35)*

**Dado** que eu uso o sistema normalmente
**Quando** eu passo pelos principais fluxos (mesa de trabalho, kanban, busca, documentos, notificações, assinaturas, mural)
**Então** verifico que tudo funciona igual a antes da mudança de arquitetura

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-036 Integrações antigas continuam respondendo** *(CA36)*

**Dado** que existe uma integração mais antiga usada por fora do sistema (ex.: listagem de documentos)
**Quando** ela é chamada
**Então** verifico que continua respondendo normalmente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-037 Notificações em tempo real continuam chegando na hora** *(CA37)*

**Dado** que uma ação minha ou de outro usuário gera notificação em tempo real
**Quando** ela acontece
**Então** verifico que a notificação chega na hora, sem eu precisar recarregar a página

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### I. Achados via automação — sugestão de novos CTs *(ainda não confirmados manualmente)*

Encontrados rodando a suíte `sogov-automation-test` contra `dev.sogov.net` (ver seção
**Automação**, abaixo). Ainda não foram reproduzidos clicando na tela — a automação apontou o
problema, falta confirmar manualmente antes de virar bug de verdade.

#### **CT-038 Menu de opções do despacho abre corretamente** *(sugerido via automação)*

**Dado** que eu tenho um despacho já existente
**Quando** eu clico no menu de opções (⋮) desse despacho
**Então** verifico que o menu abre, mostrando as ações disponíveis

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-039 Carimbo de assinatura mostra o cargo correto do assinante** *(sugerido via automação)*

**Dado** que um servidor com um cargo específico (ex.: "Tester") assina um documento
**Quando** eu abro o PDF assinado
**Então** verifico que o carimbo de assinatura mostra o cargo real do assinante, e não um valor
genérico como "Signatário"

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-040 Botão de emitir aparece disponível num fluxo de trabalho** *(sugerido via automação)*

**Dado** que eu tenho um fluxo de trabalho (workflow) em andamento
**Quando** chega a etapa de emissão de documento
**Então** verifico que o botão de emitir aparece disponível na tela

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-041 Geração de documento automatizado leva pra tela correta** *(sugerido via automação)*

**Dado** que eu gero um documento automatizado a partir de um fluxo de trabalho
**Quando** a geração conclui
**Então** verifico que sou levado pra tela do documento recém-gerado (não fico numa tela
anterior/errada)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

> [!info]- Padrão recorrente pra investigar (não é um CT por si só)
> Em ~4 pontos diferentes rodando a automação (busca de servidor por nome, listagem em tabela),
> um elemento da tela demorou mais que o esperado pra ficar visível/carregado, fazendo o teste
> automatizado "desistir" achando que não existe. Já corrigimos exatamente esse tipo de problema
> uma vez (select de módulo em Assuntos e Serviços, que carrega a lista de forma assíncrona).
> Pode ser a mesma causa se repetindo em outras telas — vale o Dev checar se existe um padrão de
> carregamento assíncrono comum a essas telas de busca/listagem.

---

### J. Fora de execução — registro

*Só preencher quando algum CT acima for retirado/adiado desta rodada.*

| Caso | Decisão | Motivo |
|---|---|---|
|  |  |  |

---

## Verificações técnicas

*Mudanças de arquitetura sem tela pra eu observar direto — dependem de log, painel interno ou teste de carga feito pelo Dev/Infra. Não são CTs no sentido tradicional (não dá pra clicar sozinho), mas continuam sendo parte do que precisa ser confirmado antes de dar a migração por validada.*

- [ ] Deploy de nova versão sobe sem erro, mesmo com a atualização automática do banco de dados durante a subida
- [ ] Se a atualização do banco falhar durante um deploy, o sistema não fica no ar quebrado (trava a subida ou avisa claramente — pedir ao Dev pra simular esse cenário)
- [ ] Reverter uma versão com problema (rollback) funciona e não perde dados
- [ ] Rotinas automáticas "invisíveis" (limpeza de módulos temporários, atualização de status de trabalho, ativação/inativação de chave de acesso, aviso de módulo fora do ar, geração agendada de relatórios/PDFs em lote) rodam no horário certo, confirmado nos logs pelo Dev
- [ ] Rodar a mesma rotina automática duas vezes não duplica nada (ex.: não duplica e-mail de recuperação de senha) — pedir ao Dev pra forçar a re-execução
- [ ] Sistema continua funcionando igual com o cache (Redis) ligado ou desligado; se o cache cair no meio do uso, o sistema não sai do ar
- [ ] Acesso a arquivos e envio de e-mail não dependem de senha fixa configurada no código — checagem de segurança feita pelo Dev
- [ ] Sistema aguenta carga de uso e picos de acesso sem cair (teste de performance feito pelo time de Infra, comparado com a versão anterior)
- [ ] Ambiente de teste temporário de uma branch (se for usado durante o projeto) funciona durante o teste e some sozinho depois que o MR é fechado/mergeado

---

## Automação (`sogov-automation-test`)

*Resumo pra quem for continuar rodando a suíte automatizada contra o novo ambiente.*

- **Onde**: `sogov-automation-test-devnet` — cópia isolada de `sogov-automation-test`, criada
  pra não conflitar com outro trabalho no repo original. `cypress.env.json` aponta pro
  `dev.sogov.net`, instância **44** ("E2E Automatic Test", 11 atores de teste já cadastrados e
  ativos — não precisa recriar).
- **3 correções já aplicadas no código de teste** (locais, não commitadas ainda): sessão do
  admin sendo perdida depois de logar um cidadão (`getCitizenOrCreate`), timing no select de
  módulo de Assuntos e Serviços (`selectMatterServiceModule`), e o CT de criação de Setor
  passou a validar o resultado real (setor listado) em vez de só o texto do toast.
- **Como rodar**: por pasta/lote, não a suíte inteira de uma vez — rodar tudo junto sobrecarrega
  o serviço de geração de PDF do backend e gera falhas que não são bugs reais. Orçamento
  sugerido: ~15-20min por lote; se estourar, interromper e seguir pro próximo.
- **Specs de assinatura são anormalmente lentos** (`sign.processing.api.cy.js`,
  `sign.document.cy.js`) — nem 30min foi suficiente pra terminar rodando sozinhos. Tratar à
  parte, com bastante tempo reservado.
- **Falha conhecida, não é bug de teste**: `system.messages.pdf-generator-attachment-error` —
  capacidade/concorrência do serviço de PDF do backend (já existia no ambiente antigo também,
  não é da migração). Some quando roda em lotes menores.
- **Última rodada completa**: 30 specs, 78 testes — 41 passando, 13 falhando, 24 pendentes
  (~40min de execução total). As 13 falhas viraram os CTs sugeridos na seção J acima, mais o
  padrão de timing já registrado como investigação pro Dev.
- Skills do repo (`criar-teste-api`/`criar-teste-e2e`) servem pra estender a suíte se algum CT
  novo dos grupos acima precisar virar teste automatizado.

---

> [!danger] Bugs encontrados

- 🐛 [[QA Workspace/02 Demandas/HML/Bug E-mail De Confirmacao De Cadastro Nao Chega No Novo Ambiente De Homologacao|Bug E-mail de confirmação de cadastro não chega]] — confirmado em 26/08/2026, CT-025 reprovado, sem SGV ainda.
- 🐛 [[QA Workspace/02 Demandas/Concluídas/11151 - Bug Documento Não É Criado Com Anexo No Módulo E No Assunto E Serviço|SGV-11151]] — cadastrado em 28/08/2026, documento não criado com anexo no módulo/assunto e serviço; não bate com CT existente (ver Observações do card).
- 🐛 [[QA Workspace/02 Demandas/Concluídas/11153 - Bug Erro Ao Tentar Realizar Download Versão Compactada|SGV-11153]] — cadastrado em 28/08/2026, regressão da SGV-8660 (tabela de Regressão acima).
- 🐛 [[QA Workspace/02 Demandas/Concluídas/11158 - Bug Prévia De Documento Não Carrega Para Solicitação De Assinatura|SGV-11158]] — cadastrado em 28/08/2026, prévia de documento não carrega na solicitação de assinatura; sem CT/regressão exata (ver Observações do card).
- 🐛 [[QA Workspace/02 Demandas/Concluídas/11159 - Bug Campo De Mapa Não Carrega Para Seleção De Localização|SGV-11159]] — cadastrado em 28/08/2026, regressão da SGV-9074 (tabela de Regressão acima, antes tag POC1).
- 🐛 [[QA Workspace/02 Demandas/Concluídas/11215 - Bug Documento Não Carrega Para Realizar Assinatura|SGV-11215]] — cadastrado em 01/09/2026, CT-002 reprovado (documento não carrega ao clicar pra assinar; vizinho da SGV-11158, ponto de falha diferente). Aprovado parcialmente em 02/09/2026 (v. 14.17.0) — só o carregamento; conclusão da assinatura segue em SGV-11249.
- 🐛 [[QA Workspace/02 Demandas/HML/11249 - Bug Assinatura De Documento Ou Despacho Não É Concluída Com Sucesso|SGV-11249]] — cadastrado em 02/09/2026, CT-002 reprovado (documento/despacho, com ou sem anexo, carrega mas a assinatura não conclui; vizinho da SGV-11215, ponto de falha diferente).

---

## Evidências

Nenhuma anexada ainda — esta rodada ainda não começou a ser executada.

---

## Regressão — bugs da rodada anterior

24 bugs foram abertos na rodada anterior de validação da nova arquitetura (export "itens que foram abertos e solucionados na rodada anterior"). **Não viraram cards individuais no vault** — isto é apenas uma checklist de referência para revalidação no novo ambiente de homologação. A coluna "CT correlacionado" aponta pro caso de teste prático (acima) que mais se aproxima do que o bug descreve — títulos sem contexto adicional (só o que veio no export) podem estar incorretos, revisar ao executar.

| SGV | Título | Status rodada anterior | CT correlacionado | Revalidar em HML |
|---|---|---|---|---|
| SGV-9530 | Erro ao tentar ativar instância "Em implantação" | Cancelado | — | ☐ *(não se aplica — cancelado)* |
| SGV-9076 | Erro ao excluir pré-cadastro de servidor (ambiente POC1) | Aprovado no Dev | Sem CT claro — tag POC, confirmar se POC1 existe no novo ambiente | ☐ |
| SGV-9074 | Erro ao selecionar localização em campo do tipo mapa (POC1) | Aprovado no Dev | Sem CT claro — tag POC, confirmar se POC1 existe no novo ambiente | ☑ *(reaberto fora do POC1 como [[QA Workspace/02 Demandas/Concluídas/11159 - Bug Campo De Mapa Não Carrega Para Seleção De Localização\|SGV-11159]], corrigido e aprovado em 01/09)* |
| SGV-8820 | Sessão como Cidadão PJ não é persistida | Aprovado no Dev | CT-015 / CT-018 (Login e sessão) | ☐ |
| SGV-8806 | Impossibilidade de criar novos documentos | Aprovado no Dev | CT-005 (Criar documento) | ☐ |
| SGV-8775 | Erro ao tentar realizar importação de documentos | Aprovado no Dev | CT-004 (Importar documento) | ☐ |
| SGV-8689 | Download de documento por cidadão não é realizado corretamente | Aprovado no Dev | CT-020 / CT-022 (Upload/download) | ☐ |
| SGV-8688 | Erro ao tentar abrir qualquer solicitação como cidadão | Aprovado no Dev | CT-015 / CT-035 (Login ou regressão geral) | ☐ |
| SGV-8669 | Erro ao emitir documento para cliente (ambiente administrativo) | Aprovado no Dev | CT-029 (Emitir/baixar documento) | ☐ |
| SGV-8661 | Documentos e despachos não carregam ao baixar documento personalizado | Aprovado no Dev | CT-029 / CT-030 (Geração/download de PDF) | ☐ |
| SGV-8660 | Erro ao tentar realizar download Versão compactada | Aprovado no Dev | CT-022 (Link de download) | ☑ *(reaberto como [[QA Workspace/02 Demandas/Concluídas/11153 - Bug Erro Ao Tentar Realizar Download Versão Compactada\|SGV-11153]], corrigido e aprovado em 01/09)* |
| SGV-8658 | Erro ao realizar ou solicitar Assinaturas (POC) | Aprovado no Dev | Sem CT claro — tag POC; correlato a CT-029 (assinatura) se aplicável fora de POC | ☐ |
| SGV-8609 | Falha ao cadastrar servidor no ambiente com nova arquitetura | Aprovado no Dev | Sem CT claro — pode estar ligado ao deploy (ver Verificações técnicas), confirmar contexto | ☐ |
| SGV-8602 | Logo do SOGOV não exibida no e-mail "Finalize seu cadastro" (cidadão PF) | Aprovado no Dev | CT-028 (Logo no e-mail de cadastro) | ☐ |
| SGV-8447 | Erro ao avançar etapa no cadastro via link | Aprovado no Dev | CT-019 (Login via link de e-mail) | ☐ |
| SGV-8446 | Erro ao enviar e-mail ao realizar cadastro de Servidor/cidadão | Aprovado no Dev | CT-025 (E-mails do sistema) | ☐ |
| SGV-8381 | ApolloError: system.messages.something-went-wrong ao acessar tela inicial | Aprovado no Dev | CT-035 (Regressão geral) | ☐ |
| SGV-8377 | Erro ao tentar anexar arquivo em despacho | Aprovado no Dev | CT-020 / CT-024 (Upload de arquivo) | ☐ |
| SGV-8375 | Erro 500 ao realizar despacho com prazo | Aprovado no Dev | CT-030 / CT-035 (PDF em lote ou regressão) | ☐ |
| SGV-8372 | Erro ao realizar upload de imagem para perfil de Servidor/cidadão | Aprovado no Dev | CT-020 (Upload de arquivo) | ☐ |
| SGV-8371 | Erro ao acessar link de convite para servidor | Aprovado no Dev | CT-019 (Login via link) | ☐ |
| SGV-8366 | Erro ao realizar upload de imagem (logos) em instância | Aprovado no Dev | CT-020 (Upload de arquivo) | ☐ |
| SGV-8365 | Erro ao criar documento | Aprovado no Dev | CT-005 (Criar documento) | ☐ |
| SGV-8362 | Erro ao consultar CPF/CNPJ | Aprovado no Dev | Sem CT claro — integração externa não coberta pelos CTs acima | ☐ |

**Leitura geral:** a maioria dos bugs da rodada anterior (17 dos 24) correlaciona claramente com casos de teste práticos já listados acima — o que é esperado, dado que essas são justamente as áreas com maior mudança por trás da tela (documentos, sessão, upload, e-mail, PDF). 3 são especificamente de POC (ambiente separado, confirmar se ainda existe). 1 foi cancelado. 3 não têm CT claro pelo título isolado (SGV-8609, SGV-8688, SGV-8362) — vale confirmar contexto antes de revalidar.

---

> [!tip] Observações
> - Origem: 2 exports do Notion processados em 2026-08-26 (`SKILL_LIMPEZA_EXPORT`, Modo B) — plano de testes original da SGV-8321 e lista de bugs da rodada anterior. Reescrita no mesmo dia pra sair do tom técnico do export (worker, SQS, initContainer, IRSA, ArgoCD) e virar Casos de Teste no formato Dado/Quando/Então que dá pra executar clicando na tela, separando o que é tecnicamente inobservável em "Verificações técnicas".
> - Escopo desta rodada: apenas documentação/preparo. Execução manual no novo ambiente de homologação é o próximo passo, condicionado a ter URL/acesso do ambiente.
> - Ordem de execução recomendada: priorizar primeiro o grupo **A** (ações que passam pela fila de espera) e **C** (login/sessão) — são os de maior risco — e rodar a checklist de regressão dos 24 bugs em paralelo aos CTs correlacionados. As Verificações técnicas podem ser combinadas com o Dev em paralelo, sem bloquear os Casos de Teste.
> - Automação via `sogov-automation-test` (skills `criar-teste-api`/`criar-teste-e2e` do repo) é um passo posterior, só depois que a validação manual confirmar que os pontos realmente não mudaram — mesmo padrão já seguido no TR 1.24-1.25.

---

## Histórico

- 2026-08-26 - 📝 Plano de teste criado a partir do export do Notion (SGV-8321), 52 pontos técnicos organizados em 13 áreas.
- 2026-08-26 - 📝 Casos de Teste reescritos (37 CTs práticos em 8 grupos + checklist de "Verificações técnicas" separada) a pedido do Rafael — a primeira versão estava técnica demais (linguagem de worker/SQS/IRSA/ArgoCD), sem bater com o padrão do resto do vault de testar pelo que o usuário vê e faz na tela.
- 2026-08-26 - 🐛 CT-025 reprovado — e-mail de confirmação de cadastro não chega no `dev.sogov.net` (confirmado via automação e checagem manual da caixa Gmail). Bug cadastrado sem SGV ainda.
- 2026-08-28 - 🐛 SGV-11151 cadastrado — documento não criado com anexo no campo do módulo e no campo de assunto e serviço. Achado testando criação/anexo; sem CT correspondente na lista atual.
- 2026-08-28 - 🐛 SGV-11153 cadastrado — regressão confirmada da SGV-8660 (tabela de Regressão): download da versão compactada do documento retorna erro.
- 2026-08-28 - 🐛 SGV-11158 cadastrado — prévia de documento não carrega na tela de solicitação de assinatura. Sem CT/regressão exata correspondente.
- 2026-08-28 - 🐛 SGV-11159 cadastrado — regressão confirmada da SGV-9074 (tabela de Regressão): campo de mapa não carrega para seleção de localização; reproduz fora do ambiente POC1.
- 2026-09-01 - 🐛 CT-002 reprovado — SGV-11215 cadastrado (documento não carrega ao clicar pra assinar).
- 2026-09-02 - 🐛 CT-002 segue reprovado — SGV-11249 cadastrado (documento/despacho, com ou sem anexo, carrega mas a assinatura não conclui com sucesso).
- 2026-09-02 - ✅ SGV-11215 aprovada parcialmente em homologação (v. 14.17.0) — carregamento do documento resolvido; conclusão da assinatura segue em SGV-11249.
- 2026-09-01 - ✅ SGV-11159, SGV-11158 e SGV-11153 aprovadas em homologação (campo de mapa, prévia de assinatura e download compactado) — SGV-11159 e SGV-11153 fecham as regressões da SGV-9074 e SGV-8660 (tabela de Regressão acima).
- 2026-09-01 - ✅ SGV-11151 aprovada em homologação (criação de documento com anexo no módulo e no assunto e serviço).
- 2026-09-04 - 🤖 Automação (`sogov-automation-test-devnet`) desbloqueada e rodada contra `dev.sogov.net` em lotes (30 specs, 78 testes: 41 passando / 13 falhando / 24 pendentes). 3 correções de teste aplicadas (sessão de admin, timing de select, validação real no CT de criação de Setor). Achados novos viraram CT-038 a CT-041 (seção J) — ainda não confirmados manualmente. `pdf-generator-attachment-error` confirmado como sobrecarga de backend, não bug de teste. Specs de assinatura (`sign.*`) identificados como anormalmente lentos, tratamento à parte pendente.
