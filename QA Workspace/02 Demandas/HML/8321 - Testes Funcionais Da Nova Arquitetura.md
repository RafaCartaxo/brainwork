---
tags:
  - demanda
  - funcionalidade
  - qa
  - arquitetura
task: "8321"
status: hml
prioridade: alta
mel: ""
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

Pontos de teste detalhados para validar a migração da arquitetura Lambda para EKS (app-sogov), abrangendo workers SQS, CronJobs, migrações Prisma, autenticação, upload de arquivos, e‑mail, geração de PDFs, banco de dados, cache Redis, credenciais AWS (IRSA), CI/CD com ArgoCD, performance/escalabilidade e regressão funcional de GraphQL/REST.

Esta nota nasce do processamento de 2 exports do Notion (`SKILL_LIMPEZA_EXPORT`, Modo B — card direto): o roteiro de testes original da SGV-8321 e a lista de bugs abertos/solucionados na rodada anterior de validação. Com o novo ambiente de homologação disponibilizado, a premissa é que os pontos de teste não mudaram — esta rodada existe pra confirmar isso.

---

## Regras de negócio

Não há regra de negócio nova — a interface funcional (GraphQL/REST) não muda. O que muda é o **runtime**: de Lambda + API Gateway para pods em EKS (Fastify nativo), com workers SQS dedicados, CronJobs no lugar de Lambda Schedule, migrações Prisma via initContainer, IRSA no lugar de credenciais estáticas, e deploy via ArgoCD no lugar de `serverless deploy`. Cada bloco de Casos de Teste abaixo carrega o "por quê" (o que mudou na arquitetura que justifica o teste).

---

> [!warning] Pontos de atenção
> - **Deadline do Notion está vencido** (27/04/2026 → 15/05/2026, e hoje é 2026-08-26) — sinalizar com Flávio/Produto se o prazo desta rodada de revalidação precisa ser refirmado.
> - **3 bugs da rodada anterior são especificamente de POC** (SGV-9076, SGV-9074, SGV-8658, tag `[BUG-Arquitetura-POC]`, ambiente "POC1") — confirmar se esse ambiente de POC ainda existe/é relevante no novo ambiente de homologação antes de tentar revalidar esses três.
> - O export original não trouxe "Responsáveis" preenchidos por ponto de teste (colunas vazias) — distribuir entre Rafael e Flávio ao iniciar a execução.
> - **SGV-9530** ("Erro ao tentar ativar instância") está com status **Cancelado** na rodada anterior — não faz parte da revalidação.

---

## Casos de Teste ([skill](../../../Sistema/Skills/SKILL_CASOS_DE_TESTE.md))

### A. Workers SQS (NOVO modelo — Crítico)

Antes: SQS → trigger automático do Lambda. Agora: pod em loop com long-polling, escalado por KEDA.

#### **CT-001 Processamento ponta a ponta em cada uma das 9 filas SQS** *(CA1)*

**Dado** que uma mensagem é publicada em cada uma das filas (sendMail, signDocuments, sendNotification, documentImport, createDocumentObject, generateBIReports, generateDispatchPDFs, generateDocumentPDF, documentImportPending)
**Quando** o worker dedicado da fila consome a mensagem
**Então** o processamento ocorre ponta a ponta com sucesso, sem depender de trigger automático da AWS

> 💡 Cada fila agora tem um Deployment próprio; uma falha isolada não é mais detectada por trigger AWS.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 Latência de pickup da mensagem SQS** *(CA2)*

**Dado** que uma mensagem é publicada em qualquer uma das 9 filas
**Quando** o worker faz long-poll (20s)
**Então** a mensagem é processada em até 25s

> 💡 Diferente do Lambda (~ms para invocar).

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-003 Mensagens grandes / payload com caracteres especiais** *(CA3)*

**Dado** que uma mensagem SQS contém payload grande ou com caracteres especiais
**Quando** o worker processa a mensagem
**Então** o parser processa corretamente, sem truncar ou corromper o conteúdo

> 💡 Parser pode diferir entre runtime Lambda e Node puro.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. CronJobs (NOVO — substituem Lambda Schedule)

13 tarefas via `node scheduler.js --type <task>`: restore-email, update-work-status, expire-invitation, clear-temporary-modules, notify-contract-expiration, publish-on-wall, activate-access-key, inactivate-access-key, check-downtime-modules-edit, notify-deadline-expiration, generate-bi-reports, generate-dispatch-pdfs, notify-publish-documents.

#### **CT-004 Cada CronJob executa no horário esperado** *(CA4)*

**Dado** que cada uma das 13 tarefas está agendada como CronJob no Kubernetes
**Quando** o horário programado chega
**Então** a tarefa executa no horário esperado, confirmado nos logs (atenção a fuso UTC vs BRT)

> 💡 Schedule agora é cron string; erro de fuso é comum.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005 Idempotência do CronJob (ex.: restore-email)** *(CA5)*

**Dado** que a tarefa `restore-email` já executou uma vez
**Quando** ela é executada novamente (retry/re-run)
**Então** os e-mails não são duplicados

> 💡 Em CronJob com falha + retry, pode haver re-execução — no Lambda os retries automáticos eram raros.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### C. Migrações Prisma via initContainer (NOVO fluxo)

Agora rodam 3 schemas (`schema.prisma`, `bi/schema.prisma`, `transition/schema.prisma`) em um initContainer antes do pod principal subir.

#### **CT-006 Deploy aplica migração nos 3 schemas** *(CA6)*

**Dado** um novo deploy da aplicação
**Quando** o initContainer executa `prisma migrate deploy`
**Então** os 3 schemas (principal, BI, transition) são migrados com sucesso

> 💡 Schema transition é novo; não existia em produção.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-007 Falha de migração impede o pod de subir** *(CA7)*

**Dado** que uma migração Prisma falha no initContainer
**Quando** o Kubernetes tenta subir o pod principal
**Então** o rollout fica preso (pod não vira Ready)

> 💡 Antes era "deploy primeiro, migrate depois"; agora o pod só fica Ready se a migration passar.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-008 Múltiplos pods subindo simultaneamente não causam lock duplo no DB** *(CA8)*

**Dado** que múltiplos pods sobem ao mesmo tempo (ex.: rolling update)
**Quando** cada um roda seu initContainer de migração
**Então** o advisory lock do Prisma evita conflito/lock duplo no banco

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-009 Rollback do ArgoCD após migração preserva dados** *(CA9)*

**Dado** um deploy com migração já aplicada
**Quando** o ArgoCD faz rollback para a versão anterior
**Então** os dados são preservados e a aplicação volta a funcionar (migrações são forward-only — validar o comportamento real)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Autenticação, Sessão e Cookies (Mudanças sutis — Alto risco)

#### **CT-010 Cookie de sessão com Domain/SameSite/Secure corretos por ambiente** *(CA10)*

**Dado** um login bem-sucedido em qualquer ambiente (dev/hom/prod)
**Quando** o cookie `session_*` é definido
**Então** `Domain`, `SameSite` e `Secure` estão corretos para o ambiente

> 💡 Vars `APPLICATION_AUTH_DOMAIN` e `APPLICATION_AUTH_SAME_SITE` foram adicionadas/alteradas.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-011 Multi-tenant: troca de instância grava cookie instanceId** *(CA11)*

**Dado** um usuário autenticado
**Quando** ele troca de instância
**Então** o cookie `instanceId` é gravado e o backend o respeita nas próximas chamadas

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-012 Logout limpa cookie em todos os subdomínios** *(CA12)*

**Dado** um usuário autenticado em um subdomínio
**Quando** ele faz logout
**Então** o cookie de sessão é limpo em todos os subdomínios (não apenas no atual)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-013 Sessões legadas (criadas no Lambda) continuam válidas** *(CA13)*

**Dado** uma sessão criada antes do cutover para EKS
**Quando** o usuário acessa a aplicação já em EKS
**Então** a sessão legada continua válida, sem deslogar o usuário

> 💡 DbAuth deve re-encriptar; validar que usuários ativos não são deslogados no cutover.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-014 Login com SameSite=Strict em fluxo cross-site** *(CA14)*

**Dado** um fluxo cross-site (ex.: link de e-mail abrindo em nova aba)
**Quando** o usuário faz login
**Então** o login funciona mesmo com `SameSite=Strict` configurado

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Upload de Arquivos (S3 presigned URL)

#### **CT-015 Upload de arquivo maior que 6 MB** *(CA15)*

**Dado** um arquivo maior que 6 MB (limite antigo do Lambda)
**Quando** o upload é realizado
**Então** o upload é concluído com sucesso, sem a restrição antiga

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-016 Upload de arquivos grandes (50 MB, 100 MB, 500 MB)** *(CA16)*

**Dado** arquivos de 50 MB, 100 MB e 500 MB
**Quando** o upload é realizado
**Então** cada upload é concluído com sucesso (validar `client_max_body_size` no Ingress/ALB/Istio)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-017 Presigned URL expira corretamente** *(CA17)*

**Dado** uma presigned URL de upload gerada
**Quando** o tempo configurado de expiração passa
**Então** a tentativa de uso retorna 403

> 💡 SDK v3 tem comportamento ligeiramente diferente do v2.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-018 Anexos em texto longo (endpoint dedicado)** *(CA18)*

**Dado** um anexo vinculado a um campo de texto longo
**Quando** o upload usa o endpoint `getSignedUrlToUploadAttachmentInBigText`
**Então** o upload funciona corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-019 Upload simultâneo de múltiplos arquivos** *(CA19)*

**Dado** múltiplos arquivos selecionados para upload
**Quando** os uploads são disparados simultaneamente
**Então** todos são concluídos corretamente, sem falhas de conexão

> 💡 Conexões keep-alive em pods longos podem se comportar diferente.

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### F. E-mail (SES SDK v2 → v3 + nodemailer)

#### **CT-020 Envio direto de e-mail (bySqs=false)** *(CA20)*

**Dado** uma ação que dispara e-mail direto (sem fila)
**Quando** o envio é processado
**Então** o e-mail é entregue corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-021 Envio via fila sendMail (bySqs=true)** *(CA21)*

**Dado** uma ação que dispara e-mail via fila `sendMail`
**Quando** o worker novo consome a mensagem
**Então** o e-mail é entregue corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-022 Templates React Email + Handlebars renderizam corretamente** *(CA22)*

**Dado** um e-mail transacional (ex.: convite, boas-vindas, notificação)
**Quando** o template é renderizado
**Então** o HTML sai correto e sem quebra de formatação

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-023 E-mails com anexos** *(CA23)*

**Dado** um e-mail que deve incluir anexo
**Quando** ele é enviado pelo novo nodemailer
**Então** o anexo chega corretamente (sem corromper encoding/multipart)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-024 Bounce/complaint handling** *(CA24)*

**Dado** um envio que gera bounce ou complaint
**Quando** o SES processa o evento
**Então** o comportamento é tratado corretamente (vars `AWS_SES_HOST/PORT/CREDENTIAL_USER` foram removidas — agora é SDK puro)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### G. Geração de PDF (assíncrona via fila)

#### **CT-025 Geração PAdES completa (mutation → polling → download)** *(CA25)*

**Dado** uma solicitação de geração de PDF assinado (PAdES)
**Quando** a mutation dispara, o status é consultado via polling e o download é solicitado
**Então** o fluxo completo funciona ponta a ponta via SQS + worker `generateDocumentPDF`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-026 Geração de despachos em lote** *(CA26)*

**Dado** múltiplos despachos selecionados
**Quando** a geração em lote é disparada (`generateDispatchPDFs`)
**Então** todos os PDFs são gerados sem estourar `activeDeadlineSeconds`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-027 Tempo de geração comparável ao baseline do Lambda** *(CA27)*

**Dado** um cenário de geração de PDF equivalente ao usado como baseline no Lambda
**Quando** o tempo total é medido no novo ambiente
**Então** o tempo é comparável (documentar se está mais rápido ou mais lento e por quê)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-028 Concorrência: múltiplos usuários gerando PDF simultaneamente** *(CA28)*

**Dado** múltiplos usuários solicitando geração de PDF ao mesmo tempo
**Quando** as solicitações chegam simultaneamente
**Então** o KEDA escala os workers de PDF e todas as gerações são concluídas

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### H. Banco de Dados (Read replicas e múltiplos schemas)

#### **CT-029 Queries de leitura usando DATABASE_URL_RO** *(CA29)*

**Dado** uma operação de leitura
**Quando** ela é roteada para a replica de leitura
**Então** os dados retornam corretamente via `DATABASE_URL_RO`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-030 Relatórios BI usando DATABASE_BI_URL_RO** *(CA30)*

**Dado** a geração de um relatório BI
**Quando** a consulta é executada
**Então** os dados retornam corretamente via `DATABASE_BI_URL_RO`

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-031 Lag de replicação não causa dados "sumidos" após escrita** *(CA31)*

**Dado** uma escrita recém-realizada
**Quando** uma leitura é feita logo em seguida (replica RO)
**Então** o dado aparece corretamente, sem sumir por lag de replicação

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-032 Connection pool não esgota sob carga** *(CA32)*

**Dado** múltiplos pods rodando simultaneamente (`connection_limit=1` por pod)
**Quando** a carga aumenta (replicaCount × workers)
**Então** o pod não esgota conexões com o banco

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-033 Schema transition não interfere com o schema principal** *(CA33)*

**Dado** o schema `transition/schema.prisma` (novo, staging de migração de dados)
**Quando** operações rodam no schema principal
**Então** não há interferência entre os dois schemas

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### I. Cache Redis (opcional — novo no fluxo)

#### **CT-034 App funciona com USE_REDIS_CACHE=false** *(CA34)*

**Dado** a variável `USE_REDIS_CACHE=false` (default)
**Quando** a aplicação opera normalmente
**Então** ela funciona corretamente usando fallback para o banco

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-035 App funciona com Redis habilitado** *(CA35)*

**Dado** o Redis habilitado
**Quando** funcionalidades como `userCache.getUserLastEnvironment/Activity` são usadas
**Então** elas funcionam corretamente usando o cache

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-036 Queda do Redis não derruba a aplicação** *(CA36)*

**Dado** o Redis habilitado e em uso
**Quando** o Redis cai durante a operação
**Então** a aplicação degrada graciosamente, sem cair junto

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### J. IRSA / Credenciais AWS (Crítico em prod)

#### **CT-037 Pod acessa S3 sem AWS_ACCESS_KEY_ID no env** *(CA37)*

**Dado** um pod sem `AWS_ACCESS_KEY_ID` definido no ambiente
**Quando** ele precisa acessar o S3
**Então** o acesso funciona via IRSA (obrigatório em prod)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-038 Pod envia e-mails via SES sem credenciais estáticas** *(CA38)*

**Dado** um pod sem credenciais estáticas configuradas
**Quando** ele envia e-mail via SES
**Então** o envio funciona via IRSA

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-039 Worker SQS lê/deleta mensagens via IRSA** *(CA39)*

**Dado** um worker SQS operando via Service Account (IRSA)
**Quando** ele lê e deleta mensagens da fila
**Então** as permissões da Service Account são suficientes e a operação funciona

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-040 Erros 403/AccessDenied retornam mensagem clara nos logs** *(CA40)*

**Dado** um erro de permissão IRSA (403/AccessDenied)
**Quando** ele ocorre em qualquer integração AWS
**Então** o log traz uma mensagem clara o suficiente para diagnóstico

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### K. CI/CD e Deploy via ArgoCD

#### **CT-041 Promoção dev → hom → prod via auto-MR** *(CA41)*

**Dado** uma alteração aprovada
**Quando** ela é promovida de dev para hom e depois para prod via auto-MR
**Então** o fluxo funciona corretamente (substitui o antigo `serverless deploy`)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-042 Rollback de versão no ArgoCD restaura app funcional** *(CA42)*

**Dado** uma versão com problema em produção/homologação
**Quando** o rollback é feito no ArgoCD
**Então** a aplicação volta a funcionar normalmente na versão anterior

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-043 Preview environment cria namespace funcional** *(CA43)*

**Dado** uma branch `feature/*`
**Quando** o preview environment é criado
**Então** o namespace `preview-<slug>` sobe com a aplicação funcional (recurso novo, não existia em Lambda)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-044 Cleanup automático do preview ao fechar/mergear MR** *(CA44)*

**Dado** um preview environment ativo
**Quando** o MR correspondente é fechado ou mergeado
**Então** o preview é removido automaticamente, sem deixar lixo no cluster

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-045 DB de preview isolado do DB de dev** *(CA45)*

**Dado** um preview environment com migrações rodando
**Quando** as migrações são aplicadas
**Então** elas rodam em um DB próprio, sem poluir o DB de dev

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### L. Performance e Escalabilidade

#### **CT-046 Locust com cenários atuais comparado ao Lambda** *(CA46)*

**Dado** os cenários existentes (`scenarios.py`)
**Quando** o Locust roda contra o novo ambiente
**Então** p50/p95/p99 são comparáveis ao baseline do Lambda (obrigatório antes do cutover)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-047 HPA escala o Deployment principal sob carga** *(CA47)*

**Dado** carga de 100/500/1000 VUs
**Quando** a carga aumenta
**Então** o HPA escala o Deployment principal corretamente

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-048 Limites de CPU/memória suficientes para PDF/BI** *(CA48)*

**Dado** os `resources.limits` configurados para os pods de PDF/BI
**Quando** operações pesadas de PDF/BI rodam
**Então** não ocorre OOMKill

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### M. Regressão funcional GraphQL/REST

Apesar de a interface GraphQL não ter mudado, o runtime mudou (Lambda+API Gateway → Fastify nativo em pod).

#### **CT-049 Suite completa de regressão do app** *(CA49)*

**Dado** os principais fluxos do app (workboard, kanban, busca, documentos, notificações, assinaturas, mural)
**Quando** a suite de regressão é executada
**Então** nada quebrou ao trocar o runtime

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-050 Endpoints REST legados continuam funcionando** *(CA50)*

**Dado** o endpoint `/solicitacoes/listar-documentos` (e demais legados)
**Quando** ele é chamado
**Então** continua funcionando corretamente via Fastify

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-051 WebSockets/long-polling de notificações** *(CA51)*

**Dado** uma notificação em tempo real
**Quando** ela é entregue via WebSocket/long-polling
**Então** a conexão longa se comporta corretamente fora do Lambda

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-052 Headers customizados preservados** *(CA52)*

**Dado** uma chamada com headers customizados (tenant header, correlation IDs)
**Quando** ela chega ao backend
**Então** os headers chegam intactos, sem manipulação indevida (o API Gateway antigo podia alterá-los)

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### N. Fora de execução — registro

*Só preencher quando algum CT acima for retirado/adiado desta rodada.*

| Caso | Decisão | Motivo |
|---|---|---|
|  |  |  |

---

> [!danger] Bugs encontrados

Nenhum registrado ainda nesta rodada — esta nota nasce antes do início da execução manual no novo ambiente de homologação.

---

## Evidências

Nenhuma anexada ainda — esta rodada ainda não começou a ser executada.

---

## Regressão — bugs da rodada anterior

24 bugs foram abertos na rodada anterior de validação da nova arquitetura (export "itens que foram abertos e solucionados na rodada anterior"). **Não viraram cards individuais no vault** — isto é apenas uma checklist de referência para revalidação no novo ambiente de homologação. A coluna "Área correlacionada" é uma inferência a partir do título do bug cruzado com as 13 áreas técnicas do plano acima (seção Casos de Teste) — títulos sem contexto adicional (só o que veio no export) podem estar incorretos, revisar ao executar.

| SGV | Título | Status rodada anterior | Área correlacionada | Revalidar em HML |
|---|---|---|---|---|
| SGV-9530 | Erro ao tentar ativar instância "Em implantação" | Cancelado | — | ☐ *(não se aplica — cancelado)* |
| SGV-9076 | Erro ao excluir pré-cadastro de servidor (ambiente POC1) | Aprovado no Dev | Sem área clara — tag POC, confirmar se POC1 existe no novo ambiente | ☐ |
| SGV-9074 | Erro ao selecionar localização em campo do tipo mapa (POC1) | Aprovado no Dev | Sem área clara — tag POC, confirmar se POC1 existe no novo ambiente | ☐ |
| SGV-8820 | Sessão como Cidadão PJ não é persistida | Aprovado no Dev | D. Autenticação, Sessão e Cookies (CT-010/CT-013) | ☐ |
| SGV-8806 | Impossibilidade de criar novos documentos | Aprovado no Dev | A. Workers SQS — fila `createDocumentObject` (CT-001) | ☐ |
| SGV-8775 | Erro ao tentar realizar importação de documentos | Aprovado no Dev | A. Workers SQS — fila `documentImport` (CT-001) | ☐ |
| SGV-8689 | Download de documento por cidadão não é realizado corretamente | Aprovado no Dev | E. Upload/Download S3 (CT-015/CT-017) | ☐ |
| SGV-8688 | Erro ao tentar abrir qualquer solicitação como cidadão | Aprovado no Dev | D. Autenticação/Sessão ou M. Regressão (CT-010/CT-049) | ☐ |
| SGV-8669 | Erro ao emitir documento para cliente (ambiente administrativo) | Aprovado no Dev | G. Geração de PDF (CT-025) | ☐ |
| SGV-8661 | Documentos e despachos não carregam ao baixar documento personalizado | Aprovado no Dev | G. Geração de PDF (CT-025/CT-026) | ☐ |
| SGV-8660 | Erro ao tentar realizar download Versão compactada | Aprovado no Dev | E. Upload/Download S3 (CT-017) | ☐ |
| SGV-8658 | Erro ao realizar ou solicitar Assinaturas (POC) | Aprovado no Dev | Sem área clara — tag POC; correlato a G. PDF/Assinatura (CT-025) se aplicável fora de POC | ☐ |
| SGV-8609 | Falha ao cadastrar servidor no ambiente com nova arquitetura | Aprovado no Dev | C. Migrações Prisma ou H. Banco de Dados (CT-006/CT-029) | ☐ |
| SGV-8602 | Logo do SOGOV não exibida no e-mail "Finalize seu cadastro" (cidadão PF) | Aprovado no Dev | F. E-mail — templates (CT-022) | ☐ |
| SGV-8447 | Erro ao avançar etapa no cadastro via link | Aprovado no Dev | D. Autenticação — link cross-site (CT-014) | ☐ |
| SGV-8446 | Erro ao enviar e-mail ao realizar cadastro de Servidor/cidadão | Aprovado no Dev | F. E-mail (CT-020/CT-021) | ☐ |
| SGV-8381 | ApolloError: system.messages.something-went-wrong ao acessar tela inicial | Aprovado no Dev | M. Regressão GraphQL/REST (CT-049) | ☐ |
| SGV-8377 | Erro ao tentar anexar arquivo em despacho | Aprovado no Dev | E. Upload de Arquivos (CT-015/CT-019) | ☐ |
| SGV-8375 | Erro 500 ao realizar despacho com prazo | Aprovado no Dev | G. Geração de PDF ou M. Regressão (CT-026/CT-049) | ☐ |
| SGV-8372 | Erro ao realizar upload de imagem para perfil de Servidor/cidadão | Aprovado no Dev | E. Upload de Arquivos (CT-015) | ☐ |
| SGV-8371 | Erro ao acessar link de convite para servidor | Aprovado no Dev | D. Autenticação — link (CT-014) | ☐ |
| SGV-8366 | Erro ao realizar upload de imagem (logos) em instância | Aprovado no Dev | E. Upload de Arquivos (CT-015) | ☐ |
| SGV-8365 | Erro ao criar documento | Aprovado no Dev | A. Workers SQS — fila `createDocumentObject` (CT-001) | ☐ |
| SGV-8362 | Erro ao consultar CPF/CNPJ | Aprovado no Dev | Sem área clara — integração externa não citada nas 13 áreas do plano | ☐ |

**Leitura geral:** a maioria dos bugs da rodada anterior (17 dos 24) correlaciona claramente com áreas centrais da migração (Workers SQS, Autenticação/Sessão, Upload de Arquivos, E-mail, Geração de PDF) — o que é esperado, dado que essas são justamente as áreas com maior mudança de runtime. 3 são especificamente de POC (ambiente separado, confirmar se ainda existe). 1 foi cancelado. 3 não têm área clara o suficiente pelo título isolado (SGV-8688, SGV-8609, SGV-8362) — vale confirmar contexto antes de revalidar.

---

> [!tip] Observações
> - Origem: 2 exports do Notion processados em 2026-08-26 (`SKILL_LIMPEZA_EXPORT`, Modo B) — plano de testes original da SGV-8321 e lista de bugs da rodada anterior.
> - Escopo desta rodada: apenas documentação/preparo. Execução manual no novo ambiente de homologação é o próximo passo, condicionado a ter URL/acesso do ambiente.
> - Ordem de execução recomendada: priorizar primeiro os blocos marcados como "Crítico"/"Alto risco" no plano original — A. Workers SQS, C. Migrações Prisma, D. Autenticação/Sessão/Cookies, J. IRSA — e rodar a checklist de regressão dos 24 bugs em paralelo aos blocos correlacionados. Blocos de menor risco (I. Redis, L. Performance) podem vir depois.
> - Automação via `sogov-automation-test` (skills `criar-teste-api`/`criar-teste-e2e` do repo) é um passo posterior, só depois que a validação manual confirmar que os pontos realmente não mudaram — mesmo padrão já seguido no TR 1.24-1.25.

---

## Histórico

- 2026-08-26 - 📝 Plano de teste criado a partir do export do Notion (SGV-8321), 52 CTs organizados em 13 áreas técnicas, com checklist de regressão dos 24 bugs da rodada anterior anexada. Motivado pela disponibilização de novo ambiente de homologação com a nova arquitetura.
