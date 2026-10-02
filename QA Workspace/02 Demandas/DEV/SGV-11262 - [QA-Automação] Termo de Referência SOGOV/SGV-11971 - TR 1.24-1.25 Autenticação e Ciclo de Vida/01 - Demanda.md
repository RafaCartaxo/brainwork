---
prioridade: alta
status: execucao
tipo: funcionalidade
etapa_atual: "QA · Validação"
modulo: autenticacao
plano: ""
execucao: ""
ambiente: dev
origem: repo
projeto: ""
pai: "SGV-11262"
data_inicio: "2026-08-31"
data_fim: ""
responsavel: Rafael
pontos_alocados: ""
---

# SGV-11971 — TR 1.24-1.25: Autenticação e ciclo de vida do usuário

**Termo de Referência:** itens 1.24 e 1.25 (com itens 1.13 e 1.27.x correlatos) · **Ciclo:** 1.24-1.25

> [!info]- Navegação QA/DEV  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]  
> **Automação:** [[Automação/Plano de Automação|Plano]] · [[Automação/Handoff de execução|Handoff de execução]] · [[Automação/Documentação de Entrega|Documentação de Entrega]]

> [!settings]- Controle da demanda  
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** portar a suíte de Cypress pra Playwright e fechar os 4 achados reais de produto (CT-015, CT-029/030, CT-033) com produto/backend.

> [!info] Ciclo da guarda-chuva
> Este é o **primeiro ciclo** da [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/Conhecimento/0 - SGV-11262 - Índice|SGV-11262 — [QA-Automação] Termo de Referência SOGOV]]. Cada Termo de Referência verificado vira um pacote irmão deste, dentro da mesma guarda-chuva.

---

## Problema / contexto

O Termo de Referência do SOGOV fixa, nos itens 1.24 e 1.25, como a plataforma deve autenticar cada tipo de usuário (servidor por CPF, cidadão PF por CPF, PJ por CNPJ), como deve tratar credencial inválida e bloqueio por tentativas, e como o acesso deve mudar conforme o ciclo de vida da identidade funcional (Ativo, Licença, Férias, Inativo, Suspenso).

Esta demanda é a **verificação de conformidade** do que está implementado contra o que o Termo exige — não é uma entrega de funcionalidade nova. O produto do trabalho é a cobertura automatizada dos cenários mais o registro dos pontos em que o sistema diverge do Termo.

## Objetivo

Confirmar, com cobertura automatizada e evidência reproduzível, que o SOGOV atende aos 16 itens do Termo listados abaixo — e registrar formalmente cada divergência encontrada.

---

## Decisões de produto

Confirmadas com o Rafael em 18/08/2026, a partir da arquitetura real (resolveram gaps da planilha original):

- Cidadão PF (CPF) e PJ (CNPJ) usam a **mesma tela**, com campo único de identificação; o servidor tem tela própria.
- Todo servidor também é cidadão — o mesmo CPF autentica nos dois contextos (CT-009).
- Desbloqueio de conta tem dois caminhos: link por e-mail (CT-016) e desbloqueio manual por servidor (CT-017).
- Mudança de status é aplicada **imediatamente na sessão em curso** (CT-025 Licença, CT-033 Inativo).
- Licença e Férias hoje **não** dão acesso nem de leitura — o "subconjunto mínimo de funcionalidades não transacionais" do Termo não obriga a incluir visibilidade (CT-024/CT-030).
- "Suspenso" e "Inativo" são o mesmo estado no sistema (CT-035).
- Múltiplas sessões simultâneas são permitidas — o Termo não proíbe (CT-038).
- Os níveis de permissão corretos são **Especialista / Usuário básico / Somente leitura** (CT-020) — confirmado em 4 fontes (i18n, migration, docs de business-rules e nota do vault).

---

## Escopo

- Tipos de acesso e autenticação por identificador correto (Suite 1 — CT-001 a CT-009).
- Validação de credenciais e mensagens de erro (Suite 2 — CT-010 a CT-012).
- Bloqueio por tentativas e desbloqueio (Suite 3 — CT-013 a CT-019).
- Ciclo de vida da identidade: Ativo, Licença, Férias, Inativo, Suspenso (Suite 4 — CT-020 a CT-036).
- Transversais e auditoria (Suite 5 — CT-037 e CT-038).

## Fora de escopo

- **CT-E01 a CT-E03** — comportamento de servidor em Licença/Férias/Inativo acessando no **contexto de cidadão**. Não é exigido pelo Termo; ficam registrados no `03` como extras, sem execução. Pendência histórica: decidir se viram suíte e2e própria.
- Itens do Termo fora de 1.24/1.25 (e dos correlatos 1.13 e 1.27.x citados pelos CTs).

---

## Critérios de aceite

Cada critério é um item do Termo de Referência, com o texto literal da regra. Conferidos contra o PDF original em 31/08/2026 — bateram palavra por palavra nos itens até 1.26, que é até onde aquele PDF vai; os itens 1.27.x mantiveram o texto que já estava na Qase.

- C1. **1.13** — O sistema deverá garantir a auditoria de acessos e alterações às credenciais; *(CTs: CT-037)* ^c1
- C2. **1.24** — O sistema deverá permitir o login para os seguintes tipos de usuários, observando que cada acesso deverá ser único e vinculado exclusivamente a um único CPF ou CNPJ: *(CTs: CT-006, CT-007, CT-008, CT-009, CT-038)* ^c2
- C3. **1.24.1** — Servidor Público: Autenticação por CPF(Obrigatoriamente) e senha; *(CTs: CT-001, CT-004)* ^c3
- C4. **1.24.2** — Cidadão (Pessoa Física): Autenticação por CPF(Obrigatoriamente) e senha; *(CTs: CT-002, CT-005)* ^c4
- C5. **1.24.3** — Empresas e outras entidades (Pessoa Jurídica): Autenticação por CNPJ (Obrigatoriamente) e senha. *(CTs: CT-003, CT-004, CT-005)* ^c5
- C6. **1.25** — O sistema deverá verificar as credenciais fornecidas (CPF ou CNPJ) obrigatoriamente e senha, validando-as de acordo com o cadastro do usuário em questão; *(CTs: CT-006, CT-007, CT-010, CT-011, CT-012, CT-037, CT-038)* ^c6
- C7. **1.25.1** — Após cinco tentativas de login malsucedidas, a conta do usuário deverá ser bloqueada; *(CTs: CT-013, CT-014, CT-015, CT-016, CT-017, CT-018, CT-019)* ^c7
- C8. **1.25.2** — O sistema deverá exibir uma mensagem de erro clara quando as credenciais não forem reconhecidas; *(CTs: CT-010, CT-011)* ^c8
- C9. **1.25.3** — Controle de acesso dinâmico baseado no ciclo de vida da identidade funcional: *(CTs: CT-035, CT-036)* ^c9
- C10. **1.25.3.1** — Estado Operacional Padrão (Ativo): O sistema deverá aplicar o conjunto completo de permissões e privilégios (entitlements) associados aos papéis do usuário cujo atributo de status funcional esteja definido como "Ativo", garantindo acesso irrestrito ao ambiente de trabalho conforme seu perfil de autorização; *(CTs: CT-020)* ^c10
- C11. **1.25.3.2** — Estado de Afastamento Legal (Licença): Para um usuário em estado de "Licença", o sistema deverá acionar uma política de quarentena de privilégios, apresentando um aviso de status e restringindo dinamicamente o acesso a um subconjunto mínimo de funcionalidades não transacionais, suspendendo temporariamente direitos de modificação e aprovação; *(CTs: CT-021, CT-022, CT-023, CT-024, CT-025, CT-026)* ^c11
- C12. **1.25.3.3** — Estado de Afastamento Legal (Férias): De forma análoga ao estado de licença, um usuário cujo status seja "Férias" deverá ter seu acesso modulado pela mesma política de quarentena de privilégios, com a exibição de notificação e a suspensão de permissões de escrita e execução de fluxos de trabalho; *(CTs: CT-027, CT-028, CT-029, CT-030, CT-031)* ^c12
- C13. **1.25.3.4** — Estado de Desprovisionamento Lógico (Inativo): Quando o vínculo do agente for encerrado (status "Inativo"), a plataforma deverá aplicar uma regra de negação explícita (explicit deny) a qualquer tentativa de autenticação, impossibilitando o acesso e exibindo uma mensagem de conta inativa. *(CTs: CT-032, CT-033, CT-034)* ^c13
- C14. **1.27.10** — 1.27.10.1.e.iii. Suspenso — que deve representar servidores que tiverem seus acessos à plataforma suspensos; *(CTs: CT-035)* ^c14
- C15. **1.27.11.2** — (...) devendo existir, no mínimo, os seguintes status e possibilidades: a) Em atividade; b) Suspenso; c) Licença; d) Férias. *(CTs: CT-035)* ^c15
- C16. **1.27.11.4** — A partir da definição do período do novo status de atividade do servidor, esse deve receber um email informando da alteração realizada e no período definido as alterações do seu ambiente de trabalho devem ser aplicadas (...) e, ao término do período, o sistema restabeleça as funções para que o servidor retorne às suas atividades. *(CTs: CT-026, CT-031)* ^c16

---

## Checklist de entrega ao DEV

- [x] Itens do Termo extraídos e conferidos contra o PDF original.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite rastreáveis até o texto literal do Termo.
- [x] Casos de teste vinculados aos critérios.
- [ ] 4 achados reais de produto confirmados com produto/backend.
- [ ] `pontos_alocados` preenchido.

---

## Pendências de decisão

- Os 4 achados reais (CT-015, CT-029/030, CT-033) ainda **não** viraram defeitos com SGV próprio — decisão adiada em 02/10/2026, ver `00 README`.
- `priority` dos casos na Qase segue pendente de preenchimento manual (decisão consciente de 31/08, não esquecimento).
- A suíte está em Cypress e o alvo passou a ser Playwright ([[QA Workspace/04 Conhecimento/Referências/Automação Playwright|Automação Playwright]]) — o código precisa ser portado antes de subir.

